# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-07-25T01:04:59.568595

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris_train/Qwen_Qwen3.5-35B-A3B/person/2026-07-24/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 2000 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 1525 |
| Validation documents | 382 |
| Test documents | 477 |
| Train sentences | 2909 |
| Validation sentences | 765 |
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

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | 35 |
| Best Batch F1 | 0.19432502149613068 |
| Best Rules Serialized | [{'id': 'd72ced5c', 'name': 'names_in_criminal_proceedings', 'description': "Matches names of accused persons in criminal cases after 'Strafsache gegen' or 'des Verbrechens/Vergehens'. Captures the full name including suffixes like 'und andere'.", 'format': 'regex', 'content': '(?:Strafsache\\s+gegen\\s+|des\\s+Verbrechens\\s+des\\s+|des\\s+Verbrechens\\s+der\\s+|des\\s+Vergehens\\s+des\\s+|des\\s+Vergehens\\s+der\\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\\s+und\\s+andere)?)', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '8dc2a693', 'name': 'bare_names_in_criminal_context', 'description': "Matches bare names in criminal contexts like 'des [Name] betreffend' or 'des [Name] zu töten'.", 'format': 'regex', 'content': '(?:des\\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\\s+(?:von|zu|von\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)\\s+(?:betreffend|zu\\s+töten|zu\\s+verurteilen|zu\\s+bestrafen)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '2683a416', 'name': 'bare_names_after_verbs', 'description': "Matches bare names after verbs like 'wurde', 'besteht bei', 'entstammt'. Excludes trailing whitespace and common false positives.", 'format': 'regex', 'content': '(?:wurde\\s+|besteht\\s+bei\\s+|entstammt\\s+|hat\\s+|habe\\s+|sei\\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\\s+(?:von|zu|von\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'f6c3e39a', 'name': 'names_with_titles_and_suffixes', 'description': 'Matches names with academic/professional titles, capturing the full name including suffixes, while handling titles followed by institutional phrases.', 'format': 'regex', 'content': '(?:OMedR|OSR|StR|Techn\\s+R|RgR|MedR|Prof\\.in|DDr|OStR|HR|VetR|KzlR|KzlR\\s+RgR|Senatspräsident(?:in)?(?:\\s+des\\s+Obersten\\s+Gerichtshofs)?|Vizepräsident(?:in)?|Hofrat(?:in)?(?:\\s+des\\s+Obersten\\s+Gerichtshofs)?|fachkundiger\\s+Laienrichter(?:in)?|Richter(?:in)?|Schriftführer(?:in)?|Generalprokurator(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Rechtsanwält(?:in)?|Univ\\.-?Prof\\.\\s+Dr\\.\\s+|Hon\\.-?Prof\\.\\s+PD\\s+Dr\\.\\s+|Hon\\.-?Prof\\.\\s+Dr\\.\\s+|Univ\\.-?Prof\\.\\s+|Prof\\.\\s+Dr\\.\\s+|Dr\\.\\s+Univ\\.-?Prof\\.\\s+|Dr\\.\\s+|Mag\\.\\s+|Mag\\.\\s+Dr\\.\\s+|MMag\\.\\s+|DI\\s+|Dipl\\.-?Ing\\.\\s+|Bakk\\.+\\s+iur\\.+\\s+|Priv\\.-?Doz\\.\\s+|Dipl\\.\\s+|Ing\\.\\s+|OSR\\s+|StR\\s+|Prof\\.in\\s+Univ\\.-?Prof\\.\\s+|MedR\\s+|RgR\\s+|StR\\s+|HR\\s+|VetR\\s+|KzlR\\s+|KzlR\\s+RgR\\s+|Senatspräsident\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Vizepräsident\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Hofrat\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|fachkundiger\\s+Laienrichter\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Richter\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Schriftführer\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Generalprokurator\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Anwalt\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Rechtsanwalt\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Rechtsanwältin\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Univ\\.-?Prof\\.\\s+Dr\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Hon\\.-?Prof\\.\\s+PD\\s+Dr\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Hon\\.-?Prof\\.\\s+Dr\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Univ\\.-?Prof\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Prof\\.\\s+Dr\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Dr\\.\\s+Univ\\.-?Prof\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Dr\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Mag\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Mag\\.\\s+Dr\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|DI\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Dipl\\.-?Ing\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Bakk\\.+\\s+iur\\.+\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Priv\\.-?Doz\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Dipl\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Ing\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|OSR\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|StR\\s+des\\s+Obersten\\s+Gerichtshofs\\s+|Prof\\.in\\s+Univ\\.-?Prof\\.\\s+des\\s+Obersten\\s+Gerichtshofs\\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\\s+(?:von|zu|von\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'f9a5bf09', 'name': 'bare_names_in_lists', 'description': "Matches bare names in lists or after 'und', excluding sentence starters and common false positives.", 'format': 'regex', 'content': '(?:^|[,;]\\s*)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\\s+(?:von|zu|von\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?)(?=\\s*(?:,|\\s+und\\s+|\\s+zu\\s+|\\s+des\\s+|\\s+der\\s+|\\s+die\\s+|\\s+den\\s+|\\s+als\\s+|\\s+von\\s+|\\s+mit\\s+|\\s+gegen\\s+|\\s+nach\\s+|\\s+vor\\s+|\\s+über\\s+|\\s+unter\\s+|\\s+auf\\s+|\\s+an\\s+|\\s+bei\\s+|\\s+für\\s+|\\s+ohne\\s+|\\s+neben\\s+|\\s+zwischen\\s+|\\s+sowie\\s+|\\s+oder\\s+|\\s+aber\\s+|\\s+doch\\s+|\\s+sondern\\s+|\\s+weder\\s+|\\s+noch\\s+|\\s+entweder\\s+|\\s+\\)|\\s+\\]|\\s+\\.|\\s*$))', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'b7b0ec68', 'name': 'names_with_legal_titles', 'description': "Matches names preceded by specific legal titles like 'Senatspräsident', 'Hofrat', 'Vizepräsident' to ensure the full name is captured including the title context.", 'format': 'regex', 'content': '(?:Senatspräsident(?:in)?(?:\\s+des\\s+Obersten\\s+Gerichtshofs)?|Vizepräsident(?:in)?|Hofrat(?:in)?(?:\\s+des\\s+Obersten\\s+Gerichtshofs)?|fachkundiger\\s+Laienrichter(?:in)?|Richter(?:in)?|Schriftführer(?:in)?|Generalprokurator(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Rechtsanwält(?:in)?)(\\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\\s+(?:von|zu|von\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)', 'priority': 8, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 80.2% |
| True Positives | 1145 |
| False Positives | 6323 |
| False Negatives | 3020 |
| Total Gold Entities | 4165 |
| Micro Precision | 15.3% |
| Micro Recall | 27.5% |
| Micro F1 | 19.7% |
| Macro F1 | 19.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `names_in_criminal_proceedings` | 2.0% | 43.4% | 1.0% | 99 | 43 | 56 |
| `names_with_titles_and_suffixes` | 28.2% | 32.1% | 25.2% | 3276 | 1051 | 2225 |
| `bare_names_in_criminal_context` | 0.5% | 17.5% | 0.2% | 57 | 10 | 47 |
| `bare_names_in_lists` | 1.0% | 1.0% | 1.0% | 4018 | 41 | 3977 |
| `bare_names_after_verbs` | 0.0% | 0.0% | 0.0% | 71 | 0 | 71 |
| `names_with_legal_titles` | 0.0% | 0.0% | 0.0% | 307 | 0 | 307 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `names_in_criminal_proceedings`

**F1:** 0.020 | **Precision:** 0.434 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `d72ced5c`  
**Description:**
Matches names of accused persons in criminal cases after 'Strafsache gegen' or 'des Verbrechens/Vergehens'. Captures the full name including suffixes like 'und andere'.

**Content:**
```
(?:Strafsache\s+gegen\s+|des\s+Verbrechens\s+des\s+|des\s+Verbrechens\s+der\s+|des\s+Vergehens\s+des\s+|des\s+Vergehens\s+der\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+und\s+andere)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.434 | 0.010 | 0.020 | 99 | 43 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 43 | 56 | 3664 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bernhard Buddäus` | `Bernhard Buddäus` |

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
- `Norbert Wehrhahn` (person)
- `Landesgerichts Salzburg` (organisation)
- `Mag. Höpler` (person)
- `Mag. Rienmüller` (person)

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Richard Lindt` | `Richard Lindt` |

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
- `Landesgerichts Salzburg` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Andreas Schiessl` | `Andreas Schiessl` |

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
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Kur` | `Daniel Kur` |

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
- `Landesgerichts Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Gerhard Bukowska` | `Gerhard Bukowska` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `OGH` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Ahmed Koehnen` | `Ahmed Koehnen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `OGH` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Thomas Michenfelder` | `Thomas Michenfelder` |

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
- `Landesgerichts Krems an der Donau` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Nenad Pschor` | `Nenad Pschor` |

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
- `Bezirksgerichts Leopoldstadt` (organisation)
- `Mag. Schneider, LL.M.` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Jennifer Janauscheck` | `Jennifer Janauscheck` |

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
- `Bezirksgerichts Kufstein` (organisation)
- `Dr. Eisenmenger` (person)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Thomas Leutz` | `Thomas Leutz` |

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
- `Landesgerichts Innsbruck` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Maximilian Gompertz` | `Maximilian Gompertz` |

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
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_3`)


Kopf Der Oberste Gerichtshof hat am 5. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Brenner als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Kaltenbrunner als Schriftführerin in der Strafsache gegen Johannes Barkhof wegen des Vergehens der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB und weiterer strafbarer Handlungen, AZ 51 Hv 32/13i des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen den Beschluss des genannten Gerichts vom 4. Mai 2014, GZ 51 Hv 32/13i-35, und weitere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, und der Verteidigerin Mag. Reisinger zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Johannes Barkhof` | `Johannes Barkhof` |

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
- `Landesgerichts Feldkirch` (organisation)
- `Dr. Eisenmenger` (person)
- `Mag. Reisinger` (person)

**Example 12** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Lendl, Mag. Michel und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Roman Ueberlein und einen weiteren Angeklagten wegen des Verbrechens des schweren gewerbsmäßig durch Einbruch begangenen Diebstahls nach §§ 127, 128 Abs 1 Z 5, 129 Abs 2 Z 1 (iVm Abs 1 Z 1), 130 Abs 3 (iVm Abs 1 erster Fall) und 15 StGB sowie einer weiteren strafbaren Handlung, AZ 37 Hv 122/18b des Landesgerichts Innsbruck, über den Antrag des Verurteilten Roman Urbath auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roman Ueberlein` | `Roman Ueberlein` |

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
- `Landesgerichts Innsbruck` (organisation)
- `Roman Urbath` (person)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Schoenwiese wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Zoltan Schoenwiese` | `Zoltan Schoenwiese` |

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
- `Landesgerichts Eisenstadt` (organisation)
- `Mag. Höpler` (person)
- `Mag. Urak` (person)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Manderscheidt wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag. Jenichl, des Verurteilten sowie seines Verteidigers Mag. Wolm zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Nikola Manderscheidt` | `Nikola Manderscheidt` |

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
- `Landesgerichts Salzburg` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `MMag. Jenichl` (person)
- `Mag. Wolm` (person)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Martin Pfaffenberg wegen des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 5. September 2019, GZ 43 Hv 73/19x-48, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Martin Pfaffenberg` | `Martin Pfaffenberg` |

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
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mehdi Rekemeyer` | `Mehdi Rekemeyer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schuber` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_3`)


Kopf Der Oberste Gerichtshof hat am 9. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtswärters Mag. Schönmann als Schriftführer in der Strafsache gegen Thomas Enulait wegen des Verbrechens des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 und 3 erster Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 1. September 2015, GZ 20 Hv 13/15y-53, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Enulait` | `Thomas Enulait` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schönmann` (person)
- `Landesgerichts St. Pölten` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Wolniak` | `Karl Wolniak` |

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
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Erik Jirouch` | `Erik Jirouch` |

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

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jamrozy, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

| Predicted | Gold |
|---|---|
| `Erik Jamrozy` | `Erik Jamrozy` |

**Missed by this rule (FN):**

- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Wolfgang Weide` | `Wolfgang Weide` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Korner` (person)
- `Bezirksgerichts Weiz` (organisation)
- `Dr. Ulrich` (person)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Aissa Bussmann` | `Aissa Bussmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Plesser` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Clößner wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mihai Clößner` | `Mihai Clößner` |

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
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_3`)


Kopf Der Oberste Gerichtshof hat am 6. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Michael Wakup wegen des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 21. März 2017, GZ 22 Hv 1/17p-32, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf bedingter Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michael Wakup` | `Michael Wakup` |

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
- `Landesgerichts Linz` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Robert Ultsch` | `Robert Ultsch` |

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
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Mag. Schneider` (person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Grießbaum wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ernst Grießbaum` | `Ernst Grießbaum` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Ratz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Einwagner` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Christoph Holthuijsen` | `Christoph Holthuijsen` |

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
- `Landesgerichts Klagenfurt` (organisation)
- `Oberlandesgerichts Graz` (organisation)
- `Mag. Höpler` (person)
- `Mag. Sternad` (person)
- `Mag. Höllwerth` (person)

**Example 28** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in der Strafsache gegen Daniel Bruchmüller wegen der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 4 U 118/18k des Bezirksgerichts St. Pölten und zu AZ 18 U 242/18p des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Daniel Bruchmüller` | `Daniel Bruchmüller` |

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
- `Bezirksgerichts St. Pölten` (organisation)
- `Bezirksgerichts Linz` (organisation)
- `OGH` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Ferenc Florin` | `Ferenc Florin` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Gabor Schwiecker` (person)
- `Bezirksgerichts Innsbruck` (organisation)
- `OGH` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Herwig Bernts`
- `Widerstands` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 1** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Mordes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fruhmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gebhard Sayin`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `Nenad Pschor`(person)
- `Bezirksgerichts Leopoldstadt`(organisation)
- `Mag. Schneider, LL.M.`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Leopoldstadt`(organisation)
- `Nenad Panagiotakopoulou`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

**False Positives:**

- `Raufhandels` — no gold match — likely missing annotation

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
- `Mag. Gotsmy`(person)
- `Jennifer Janauscheck`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Dr. Eisenmenger`(person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__7`)


Text Gründe: Die am 26. Jänner 1991 geborene Jennifer Johannwerner wurde mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, mehrerer Vergehen der Körperverletzung nach § 83 Abs 1 StGB und des Vergehens der Sachbeschädigung nach § 125 StGB schuldig erkannt und hiefür unter Anwendung des § 5 Z 4 JGG zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von zwei Monaten verurteilt (Blg ./2 zum Bezugsakt AZ 3 U 166/07x des Bezirksgerichts Kufstein).

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jennifer Johannwerner`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Bezirksgerichts Kufstein`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Holzweber`
- `Fälschung` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Fälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Viktor Marschmeyer und andere` — partial — gold is substring of pred: `Viktor Marschmeyer`
- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktor Meisterernst`(person)
- `Dr. Stefan Tydeck`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Müller`(person)
- `Maximilian Gompertz`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Maximilian Gudzentat der Verbrechen des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (1./), der Vergewaltigung nach § 201 Abs 1 StGB und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (2./) sowie des Vergehens der Nötigung nach § 105 Abs 1 StGB (3./) schuldig erkannt.

**False Positives:**

- `Nötigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximilian Gudzentat`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

**False Positives:**

- `Natascha` — partial — pred is substring of gold: `Natascha von Bohr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Mag. Anscheringer`(person)
- `Natascha von Bohr`(person)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Bezirksgerichts Linz`(organisation)
- `Bezirksgericht Linz`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

**False Positives:**

- `Alois Petraschek und andere` — partial — gold is substring of pred: `Alois Petraschek`
- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_4`)


Text Gründe: Mit Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v, wurde der von Sebastian Niemz am 24. Mai 2019 gestellte Antrag auf Fortführung des aufgrund seiner Anzeige von der Staatsanwaltschaft Graz zu AZ 22 St 47/14v gegen Alois Paasch und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen geführten und gegen sämtliche Beschuldigte gemäß § 190 Z 2 StPO eingestellten Ermittlungsverfahrens als unzulässig zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Sebastian Niemz`(person)
- `Alois Paasch`(person)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Salzburg`(organisation)
- `Nikola Miscenko`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Raubes` — no gold match — likely missing annotation

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

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Mag` — similar text (different position): `Mag. Michel`
- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Bachl`(person)
- `Mag. Johanna Fletcher`(person)
- `Herbert Onesseit`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

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

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Karl Wodarcyk des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karl Wodarcyk`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Erik Jirouch`(person)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

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
- `Mag. Plesser`(person)
- `Aissa Bussmann`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_7`)


Text Gründe: Mit dem angefochtenen Urteil wurde Aissa Boness des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aissa Boness`(person)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_8`)


Abs 1 fünfter Fall, Abs 2 Z 3 SMG (A) sowie des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 erster und zweiter Fall SMG (B) schuldig erkannt.

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Michael Wessollek des Vergehens der Sachbeschädigung nach § 125 StGB (1/a), des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB (1/b) und des Vergehens der Körperverletzung nach § 83 Abs 1 StGB (2) schuldig erkannt.

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation
- `Körperverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Michael Wessollek`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Lengjel und andere` — partial — gold is substring of pred: `Michael Lengjel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Michael Lengjel`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Anna Wynand`(person)
- `Brian Waltemate`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Urkundenfälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 29** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Diebstahls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Ferenc Florin`(person)
- `Gabor Schwiecker`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `OGH`(organisation)

</details>

---

## `names_with_titles_and_suffixes`

**F1:** 0.282 | **Precision:** 0.321 | **Recall:** 0.252  

**Format:** `regex`  
**Rule ID:** `f6c3e39a`  
**Description:**
Matches names with academic/professional titles, capturing the full name including suffixes, while handling titles followed by institutional phrases.

**Content:**
```
(?:OMedR|OSR|StR|Techn\s+R|RgR|MedR|Prof\.in|DDr|OStR|HR|VetR|KzlR|KzlR\s+RgR|Senatspräsident(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|Vizepräsident(?:in)?|Hofrat(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|fachkundiger\s+Laienrichter(?:in)?|Richter(?:in)?|Schriftführer(?:in)?|Generalprokurator(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Rechtsanwält(?:in)?|Univ\.-?Prof\.\s+Dr\.\s+|Hon\.-?Prof\.\s+PD\s+Dr\.\s+|Hon\.-?Prof\.\s+Dr\.\s+|Univ\.-?Prof\.\s+|Prof\.\s+Dr\.\s+|Dr\.\s+Univ\.-?Prof\.\s+|Dr\.\s+|Mag\.\s+|Mag\.\s+Dr\.\s+|MMag\.\s+|DI\s+|Dipl\.-?Ing\.\s+|Bakk\.+\s+iur\.+\s+|Priv\.-?Doz\.\s+|Dipl\.\s+|Ing\.\s+|OSR\s+|StR\s+|Prof\.in\s+Univ\.-?Prof\.\s+|MedR\s+|RgR\s+|StR\s+|HR\s+|VetR\s+|KzlR\s+|KzlR\s+RgR\s+|Senatspräsident\s+des\s+Obersten\s+Gerichtshofs\s+|Vizepräsident\s+des\s+Obersten\s+Gerichtshofs\s+|Hofrat\s+des\s+Obersten\s+Gerichtshofs\s+|fachkundiger\s+Laienrichter\s+des\s+Obersten\s+Gerichtshofs\s+|Richter\s+des\s+Obersten\s+Gerichtshofs\s+|Schriftführer\s+des\s+Obersten\s+Gerichtshofs\s+|Generalprokurator\s+des\s+Obersten\s+Gerichtshofs\s+|Anwalt\s+des\s+Obersten\s+Gerichtshofs\s+|Rechtsanwalt\s+des\s+Obersten\s+Gerichtshofs\s+|Rechtsanwältin\s+des\s+Obersten\s+Gerichtshofs\s+|Univ\.-?Prof\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Hon\.-?Prof\.\s+PD\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Hon\.-?Prof\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Univ\.-?Prof\.\s+des\s+Obersten\s+Gerichtshofs\s+|Prof\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Dr\.\s+Univ\.-?Prof\.\s+des\s+Obersten\s+Gerichtshofs\s+|Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Mag\.\s+des\s+Obersten\s+Gerichtshofs\s+|Mag\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|DI\s+des\s+Obersten\s+Gerichtshofs\s+|Dipl\.-?Ing\.\s+des\s+Obersten\s+Gerichtshofs\s+|Bakk\.+\s+iur\.+\s+des\s+Obersten\s+Gerichtshofs\s+|Priv\.-?Doz\.\s+des\s+Obersten\s+Gerichtshofs\s+|Dipl\.\s+des\s+Obersten\s+Gerichtshofs\s+|Ing\.\s+des\s+Obersten\s+Gerichtshofs\s+|OSR\s+des\s+Obersten\s+Gerichtshofs\s+|StR\s+des\s+Obersten\s+Gerichtshofs\s+|Prof\.in\s+Univ\.-?Prof\.\s+des\s+Obersten\s+Gerichtshofs\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.321 | 0.252 | 0.282 | 3276 | 1051 | 2225 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1051 | 2225 | 3114 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Rützler` | `Mag. Martin Rützler` |
| `Mag. Klaus Köck` | `Mag. Klaus Köck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ernst Michael Lang` | `Mag. Ernst Michael Lang` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Kordelia Meelis` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)
- `Fatima Tengel` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)
- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Ober-Automotive GmbH` (organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Katharina Rothschadl` (person)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Maximilian Kocher` | `Mag. Maximilian Kocher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Bezirksgerichts Kitzbühel` (organisation)
- `Karin Ciliberto` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Dr. Roland Kassowitz` | `Dr. Roland Kassowitz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Landesgerichts Linz` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Thomas Girardi` | `Dr. Thomas Girardi` |
| `Dr. Franz Pechmann` | `Dr. Franz Pechmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mur Dorftalnex Technologien -GmbH` (organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich` (address)
- `Dr. Peter` (person)
- `Dr. Hermann` (person)
- `Ober Dertri GmbH` (organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich` (address)
- `Rudolf Ketelhut` (person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich` (address)
- `Dr. Bernhard Hämmerle GmbH` (organisation)
- `Völkertz Energie GmbH` (organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich` (address)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Alois Schneider` | `Dr. Alois Schneider` |
| `Dr. Walter Hausberger` | `Dr. Walter Hausberger` |
| `Dr. Alfred Schmidt` | `Dr. Alfred Schmidt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Stefula` (person)
- `Schneidergruberweg 37, 5132 Reith, Österreich` (address)
- `Dario von Ebers` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `HR Sophie Elefteriadis` | `HR Sophie Elefteriadis` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Karl-Heinz Plankel` | `Dr. Karl-Heinz Plankel` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Eva Abdelrahman` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Lederer Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ralph Trischler` | `Dr. Ralph Trischler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Bundesbeschaffung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Bernhard Birek` | `Dr. Bernhard Birek` |
| `Mag. Christian Breit` | `Mag. Christian Breit` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Ludmilla von Amelunxen` (person)
- `Svetlana Leinhäuser` (person)
- `Dr. Thomas` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Mag. Kevin Maassen` | `Mag. Kevin Maassen` |
| `Dr. Clemens Lintschinger` | `Dr. Clemens Lintschinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Mag. Dr. Georg Backhausen` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Helwig Schuster` | `Mag. Helwig Schuster` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Hofrätin Dr. Wallner-Friedl` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Walter Reichholf` | `Dr. Walter Reichholf` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Verein für Konsumenteninformation` (organisation)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Kraft & Winternitz Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. PD Dr. Rassi` | `Hon.-Prof. PD Dr. Rassi` |
| `Mag. Franz Eckl` | `Mag. Franz Eckl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Dr. Steger` (person)
- `Dr. Annerl` (person)
- `Hofrätin Dr. Wallner-Friedl` (person)
- `Ralph Prusseit` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Faber` | `Dr. Faber` |
| `Dr. Sven Rudolf Thorstensen` | `Dr. Sven Rudolf Thorstensen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


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

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Oliver Simoncic` | `Mag. Oliver Simoncic` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr.Neumayr` (person)
- `Dr. Schramm` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `AXA Software Institut Gesellschaft mbH` (organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich` (address)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Anton Bohmert` | `Mag. Anton Bohmert` |

**Missed by this rule (FN):**

- `Lars Ballogh` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei James Jooß, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Klaus Schiller` | `Dr. Klaus Schiller` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `James Jooß` (person)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Michael Schneditz-Bolfras` | `Dr. Michael Schneditz-Bolfras` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Gustav Thöning` | `Dr. Gustav Thöning` |
| `Dr. Madeleine Musialik` | `Dr. Madeleine Musialik` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofräte Dr. Schramm` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Pieler & Pieler & Partner KG` (organisation)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Dr. Alexandra Slama` | `Dr. Alexandra Slama` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Bau Zorostfurt GmbH` (organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich` (address)
- `Buitenkamp und Rothauge Landwirtschaft GmbH` (organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich` (address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Linz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Vollmaier ` — partial — gold is substring of pred: `Dr. Vollmaier`
- `Mag. Alexander Gerngross ` — partial — gold is substring of pred: `Mag. Alexander Gerngross`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Vollmaier`(person)
- `Jason Langeloh`(person)
- `Mag. Martin Rützler`(person)
- `Selma Einoeder`(person)
- `Mag. Alexander Gerngross`(person)
- `Mag. Klaus Köck`(person)
- `Bezirksgerichts Graz-Ost`(organisation)
- `Bezirksgericht Dornbirn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_6`)


Er habe den von der Beklagten erworbenen, mangelhaften PKW VW Golf VII Variant 1.6 TDI Comfort aufgrund deren Verbesserungsverweigerung selbst reparieren lassen müssen, wodurch ihm Kosten in dieser Höhe entstanden seien.

**False Positives:**

- `DI Comfort ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Florens Drehkopf, LLB`(person)
- `16. Dezember 1952`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger ` — positional overlap with gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Schramm`(person)
- `Gerhard Lohrmann`(person)
- `10. August 1983`(date)
- `Veit Künneken`(person)
- `31. Mai 1967`(date)
- `Bezirksgerichts Feldkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Dr. Nowotny ` — partial — gold is substring of pred: `Dr. Nowotny`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Nowotny`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger ` — positional overlap with gold: `Hofräte Dr. Fellinger`
- `Dr. Hoch ` — partial — gold is substring of pred: `Dr. Hoch`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`
- `KzlR Iris Makowska` — partial — pred is substring of gold: `Hon.-Prof.in KzlR Iris Makowska`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hon.-Prof.in KzlR Iris Makowska`(person)
- `Skribe Rechtsanwaelte GmbH`(organisation)
- `Dieter Apfelbacher`(person)
- `Am Fundbach 31w, 9170 Tratten, Österreich`(address)
- `Bezirksgericht Schwechat`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger ` — positional overlap with gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Neumayr`(person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich`(address)
- `Manfred Johann Puff`(person)
- `Bezirksgerichts Kitzbühel`(organisation)
- `Karin Ciliberto`(person)
- `Mag. Maximilian Kocher`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht Linz`(organisation)
- `Steidlen+Ysner Daten GmbH`(organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich`(address)
- `Dr. Roland Kassowitz`(person)
- `Verlag Waldlemder GmbH`(organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich`(address)
- `Prof. Haslinger`(person)
- `Landesgerichts Linz`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Peter Lechner ` — partial — gold is substring of pred: `Dr. Peter`
- `Dr. Hermann Pfurtscheller` — partial — gold is substring of pred: `Dr. Hermann`
- `Dr. Bernhard Hämmerle Gmb` — partial — pred is substring of gold: `Dr. Bernhard Hämmerle GmbH`

> overlaps gold: 7  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mur Dorftalnex Technologien -GmbH`(organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich`(address)
- `Dr. Peter`(person)
- `Dr. Hermann`(person)
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

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`
- `Mag. Ziegelbauer ` — partial — gold is substring of pred: `Mag. Ziegelbauer`
- `Dr. Stefula ` — partial — gold is substring of pred: `Dr. Stefula`
- `Dr. Katharina Moritz ` — no gold match — likely missing annotation

> overlaps gold: 5  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Stefula`(person)
- `Schneidergruberweg 37, 5132 Reith, Österreich`(address)
- `Dr. Alois Schneider`(person)
- `Dario von Ebers`(person)
- `Dr. Walter Hausberger`(person)
- `Dr. Alfred Schmidt`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Rattenberg`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Bartholomäus Junghahn`(person)
- `HR Sophie Elefteriadis`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_19`)


DasRekursgerichtgab dem Rekurs der beiden Minderjährigen Folge und änderte die Beschlüsse des Erstgerichts jeweils dahin ab, dass den Minderjährigen auch für den Monat Februar 2010 monatliche Unterhaltsvorschüsse in Höhe von 210 EUR (für den minderjährigen Ariadne Jefferys ) und von 180 EUR (für die minderjährige OStR Univ.-Prof.in Sascha Elfferding ) gewährt wurden.

**False Positives:**

- `StR Univ` — partial — pred is substring of gold: `OStR Univ.-Prof.in Sascha Elfferding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ariadne Jefferys`(person)
- `OStR Univ.-Prof.in Sascha Elfferding`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Korn ` — partial — gold is substring of pred: `Mag. Korn`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Eva Abdelrahman`(person)
- `Dr. Karl-Heinz Plankel`(person)
- `Hochenadel Immobilien GmbH`(organisation)
- `Ritterhof 11, 2661 Graben, Österreich`(address)
- `Lederer Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_6`)


Text Entscheidungsgründe: Über Vermittlung der Beklagten und nach Beratung durch deren Mitarbeiter Ing. Doris Waeltermann erwarb die Klägerin im Mai 2007 um 20.000 EUR Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Ing. Doris Waeltermann ` — partial — gold is substring of pred: `Ing. Doris Waeltermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Doris Waeltermann`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_7`)


Als sie einen Kursverfall dieser Aktien 2008/2009 zu einem nicht mehr näher feststellbaren Zeitpunkt wahrnahm, stellte sie erstmals fest, dass sie mit diesen Aktien ein Finanzprodukt erworben hatte, das weder dem Inhalt der Beratung des Ing. Lisa Widders noch vom Risiko und der Risikostreuung im „Portfolio“ her dem entsprach, was sie 2007 hatte erwerben wollen.

**False Positives:**

- `Ing. Lisa Widders ` — partial — gold is substring of pred: `Ing. Lisa Widders`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Lisa Widders`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Marion Woltz im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Ing. Marion Woltz ` — partial — gold is substring of pred: `Ing. Marion Woltz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Marion Woltz`(person)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr. Lovrek ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Lovrek`
- `Mag. Ziegelbauer` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Thunhart ` — partial — gold is substring of pred: `Dr. Thunhart`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Juri Gerstl`(person)
- `Mutten 18, 3251 Schauboden, Österreich`(address)
- `Dr. Ralph Trischler`(person)
- `Bundesbeschaffung GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Leander Lindlahr`(person)
- `Yussuf Prussog`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr` — partial — pred is substring of gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Hon.-Prof. Dr. Lovrek ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Lovrek`
- `Mag. Ziegelbauer` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Thomas Brückl` — partial — gold is substring of pred: `Dr. Thomas`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Mag. Dr` — partial — pred is substring of gold: `Mag. Dr. Georg Backhausen`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Mag. Schober` — partial — pred is substring of gold: `Hofräte Mag. Schober`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Vollmaier ` — partial — gold is substring of pred: `Dr. Vollmaier`
- `Dr. Wallner-Friedl` — partial — pred is substring of gold: `Hofrätin Dr. Wallner-Friedl`
- `Ing. Mag` — partial — pred is substring of gold: `Ing. Mag. Pamela Gotterbauer`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Hofrätin Dr. Wallner-Friedl`(person)
- `Ing. Mag. Pamela Gotterbauer`(person)
- `Mag. Helwig Schuster`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Verein für Konsumenteninformation`(organisation)
- `Dr. Walter Reichholf`(person)
- `SüdSanitär Gruppe GmbH`(organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich`(address)
- `Kraft & Winternitz Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Dr. Steger ` — positional overlap with gold: `Hofräte Dr. Steger`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Wallner-Friedl` — partial — pred is substring of gold: `Hofrätin Dr. Wallner-Friedl`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Hofräte Dr. Steger`(person)
- `Dr. Annerl`(person)
- `Hofrätin Dr. Wallner-Friedl`(person)
- `Ralph Prusseit`(person)
- `Mag. Franz Eckl`(person)
- `Akbayrak Metall GmbH`(organisation)
- `Schroateck 57, 4710 Niederweng, Österreich`(address)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)
- `Bezirksgerichts Zwettl`(organisation)

</details>

---

## `bare_names_in_criminal_context`

**F1:** 0.005 | **Precision:** 0.175 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `d064d891`  
**Description:**
Matches bare names in criminal contexts like 'des Angeklagten [Name]' or 'des [Name] betreffend' to capture names that were previously missed.

**Content:**
```
(?:des\s+Angeklagten\s+|des\s+Verbrechens\s+des\s+|des\s+Verbrechens\s+der\s+|des\s+Vergehens\s+des\s+|des\s+Vergehens\s+der\s+|des\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+\s+betreffend\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.175 | 0.002 | 0.005 | 57 | 10 | 47 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 47 | 3682 |

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

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_11`)


Hierauf beantragte die Staatsanwaltschaft Feldkirch in dem Johannes Bergknecht betreffenden Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch am 12. März 2014 gemäß § 355 StPO iVm § 352 Abs 1 Z 1 StPO die Wiederaufnahme des Strafverfahrens im Umfang des am 5. Juni 2013 ergangenen Freispruchs des Angeklagten Johannes Bertrang, weil dieser durch die falsche Beweisaussage der Zeugin Sabrina Holzschuher herbeigeführt worden sei (ON 29).

| Predicted | Gold |
|---|---|
| `Johannes Bertrang` | `Johannes Bertrang` |

**Missed by this rule (FN):**

- `Johannes Bergknecht` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Sabrina Holzschuher` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

| Predicted | Gold |
|---|---|
| `Johannes Bartlmäß` | `Johannes Bartlmäß` |

**Missed by this rule (FN):**

- `Landesgericht Feldkirch` (organisation)
- `Landesgerichts Feldkirch` (organisation)
- `Landesgerichts Feldkirch` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_3`)


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

**Example 7** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_9`)


Rechtliche Beurteilung Der dagegen aus Z 5 und 10 des § 281 Abs 1 StPO ergriffenen Nichtigkeitsbeschwerde des Angeklagten Kretschmer kommt keine Berechtigung zu. Entgegen dem zu beiden Schuldspruchpunkten erhobenen Einwand der Mängelrüge liegt Unvollständigkeit (Z 5 zweiter Fall) zufolge Unterbleibens einer Erörterung der Verantwortungen der jeweils beteiligten Angeklagten nicht vor.

| Predicted | Gold |
|---|---|
| `Kretschmer` | `Kretschmer` |

**Example 8** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_13`)


Zu I/E wurden die Depositionen der Angeklagten Reichenbach und Corinna Pumpenmeier ausdrücklich berücksichtigt und (unter vorangegangener Bezugnahme auf eine Reihe von Verfahrensergebnissen) ebenso als unglaubwürdig beurteilt wie die Behauptung des Beschwerdeführers und des Angeklagten Ruzicka, einander nicht zu kennen (US 15 f).

| Predicted | Gold |
|---|---|
| `Ruzicka` | `Ruzicka` |

**Missed by this rule (FN):**

- `Reichenbach` (person)
- `Corinna Pumpenmeier` (person)

**Example 9** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_15`)


Dies gilt umso mehr für die Einlassung des Angeklagten Kandlbinder selbst, weil dieser von seinem Recht zu schweigen Gebrauch machte und sich zum eigentlichen Anklagevorwurf auf die Aussage beschränkte, nicht geständig zu sein (ON 156 S 42 f).

| Predicted | Gold |
|---|---|
| `Kandlbinder` | `Kandlbinder` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Widerstands` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 1** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Mordes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fruhmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gebhard Sayin`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `Nenad Pschor`(person)
- `Bezirksgerichts Leopoldstadt`(organisation)
- `Mag. Schneider, LL.M.`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Leopoldstadt`(organisation)
- `Nenad Panagiotakopoulou`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

**False Positives:**

- `Raufhandels` — no gold match — likely missing annotation

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
- `Mag. Gotsmy`(person)
- `Jennifer Janauscheck`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Dr. Eisenmenger`(person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__7`)


Text Gründe: Die am 26. Jänner 1991 geborene Jennifer Johannwerner wurde mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, mehrerer Vergehen der Körperverletzung nach § 83 Abs 1 StGB und des Vergehens der Sachbeschädigung nach § 125 StGB schuldig erkannt und hiefür unter Anwendung des § 5 Z 4 JGG zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von zwei Monaten verurteilt (Blg ./2 zum Bezugsakt AZ 3 U 166/07x des Bezirksgerichts Kufstein).

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jennifer Johannwerner`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Bezirksgerichts Kufstein`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Fälschung` — no gold match — likely missing annotation

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

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Fälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktor Meisterernst`(person)
- `Dr. Stefan Tydeck`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Müller`(person)
- `Maximilian Gompertz`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Maximilian Gudzentat der Verbrechen des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (1./), der Vergewaltigung nach § 201 Abs 1 StGB und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (2./) sowie des Vergehens der Nötigung nach § 105 Abs 1 StGB (3./) schuldig erkannt.

**False Positives:**

- `Nötigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximilian Gudzentat`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_4`)


Text Gründe: Mit Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v, wurde der von Sebastian Niemz am 24. Mai 2019 gestellte Antrag auf Fortführung des aufgrund seiner Anzeige von der Staatsanwaltschaft Graz zu AZ 22 St 47/14v gegen Alois Paasch und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen geführten und gegen sämtliche Beschuldigte gemäß § 190 Z 2 StPO eingestellten Ermittlungsverfahrens als unzulässig zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Sebastian Niemz`(person)
- `Alois Paasch`(person)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Salzburg`(organisation)
- `Nikola Miscenko`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Raubes` — no gold match — likely missing annotation

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

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

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
- `Mag. Bachl`(person)
- `Mag. Johanna Fletcher`(person)
- `Herbert Onesseit`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

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

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Karl Wodarcyk des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karl Wodarcyk`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Erik Jirouch`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

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
- `Mag. Plesser`(person)
- `Aissa Bussmann`(person)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_7`)


Text Gründe: Mit dem angefochtenen Urteil wurde Aissa Boness des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aissa Boness`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_8`)


Abs 1 fünfter Fall, Abs 2 Z 3 SMG (A) sowie des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 erster und zweiter Fall SMG (B) schuldig erkannt.

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Michael Wessollek des Vergehens der Sachbeschädigung nach § 125 StGB (1/a), des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB (1/b) und des Vergehens der Körperverletzung nach § 83 Abs 1 StGB (2) schuldig erkannt.

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation
- `Körperverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Michael Wessollek`(person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Urkundenfälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 27** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Diebstahls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Ferenc Florin`(person)
- `Gabor Schwiecker`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `OGH`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahlwarth wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Reichly`(person)
- `Tomislav Ahlwarth`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Mag. Hautz in Gegenwart der Richteramtsanwärterin Mag. Wöss als Schriftführerin in der Strafsache gegen Heinrich Käter wegen des Vergehens der Urkundenunterdrückung nach § 229 Abs 1 StGB, AZ 5 U 21/09y des Bezirksgerichts Ybbs, über die Beschwerde des Heinrich Kowacki und der Annemarie Kloiber gegen den Beschluss des Oberlandesgerichts Wien vom 8. April 2010, AZ 18 Bs 73/10g (ON 11), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Urkundenunterdrückung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Hautz`(person)
- `Mag. Wöss`(person)
- `Heinrich Käter`(person)
- `Heinrich Kowacki`(person)
- `Annemarie Kloiber`(person)
- `Oberlandesgerichts Wien`(organisation)

</details>

---

## `bare_names_in_lists`

**F1:** 0.010 | **Precision:** 0.010 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `f9a5bf09`  
**Description:**
Matches bare names in lists or after 'und', excluding sentence starters and common false positives.

**Content:**
```
(?:^|[,;]\s*)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?)(?=\s*(?:,|\s+und\s+|\s+zu\s+|\s+des\s+|\s+der\s+|\s+die\s+|\s+den\s+|\s+als\s+|\s+von\s+|\s+mit\s+|\s+gegen\s+|\s+nach\s+|\s+vor\s+|\s+über\s+|\s+unter\s+|\s+auf\s+|\s+an\s+|\s+bei\s+|\s+für\s+|\s+ohne\s+|\s+neben\s+|\s+zwischen\s+|\s+sowie\s+|\s+oder\s+|\s+aber\s+|\s+doch\s+|\s+sondern\s+|\s+weder\s+|\s+noch\s+|\s+entweder\s+|\s+\)|\s+\]|\s+\.|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.010 | 0.010 | 0.010 | 4018 | 41 | 3977 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 41 | 3977 | 4124 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Selma Einoeder` | `Selma Einoeder` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

**False Positives:**

- `Die Weiterführung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_30`)


Zweckmäßigkeitserwägungen, die eindeutig im Sinn aller Verfahrensbeteiligten für die vom Kläger beantragte Delegierung sprechen, liegen somit nicht vor (RS0046324).

**False Positives:**

- `Zweckmäßigkeitserwägungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_35`)


Ihr Schriftsatz mit der Stellungnahme zum Delegationsantrag enthält auch Vorbringen zur Sache und Beweisanträge und ist damit im Hauptverfahren verwertbar (RS0036025 [T5, T8, T10]).

**False Positives:**

- `Ihr Schriftsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Schweiz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

**False Positives:**

- `Ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_4`)


Die Kosten der von der beklagten Partei im Delegierungsverfahren eingebrachten Äußerung (Klagebeantwortung) sind weitere Verfahrenskosten.

**False Positives:**

- `Die Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_11`)


Das Sicherstellungsbegehren und der Vertragsrücktritt seien rechtsmissbräuchlich erfolgt.

**False Positives:**

- `Das Sicherstellungsbegehren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

**False Positives:**

- `Die Verhandlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

**False Positives:**

- `Sowohl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Linz`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

**False Positives:**

- `Die Delegierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

**False Positives:**

- `Mehrere von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Linz`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

**False Positives:**

- `Dass` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_38`)


Ist die Delegierung strittig, so ist das darüber geführte Verfahren ein Zwischenstreit, über dessen Kosten unabhängig vom Ausgang der Hauptsache zu entscheiden ist (RS0036025).

**False Positives:**

- `Ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_39`)


Nicht zu honorieren sind dabei allerdings solche Schriftsätze, die auch Vorbringen zur Hauptsache enthalten (RS0036025 [T5]).

**False Positives:**

- `Nicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Russische Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_7`)


Rechtliche Beurteilung Die Gerichtskompetenz für die Vollstreckbarerklärung eines ausländischen Exekutionstitels richtet sich nach § 82 EO.

**False Positives:**

- `Rechtliche Beurteilung Die Gerichtskompetenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_12`)


Ausschlaggebendes Kriterium für die Übertragung der Zuständigkeit zur Führung einer Pflegschaftssache ist stets das Wohl des Kindes (RIS-Justiz RS0047074; RS0046908).

**False Positives:**

- `Ausschlaggebendes Kriterium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_16`)


Wird der Übertragungsbeschluss hingegen rechtskräftig bestätigt, so bedarf es der Genehmigung des übergeordneten Gerichts (3 Nc 1/23m).

**False Positives:**

- `Wird` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Hongkong` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_5`)


In eventu begehrte die klagende Partei die Feststellung, dass zwischen den Parteien kein Vertrag über die Weitergabe und Nutzung von Rechten, Lizenzen, Daten, Know-How, technischen Informationen und Unterlagen betreffend mikroverkapseltem Clomazone sowie über eine Zusammenarbeit hinsichtlich der Entwicklung und Produktion von mikroverkapseltem Clomazone mit belastenden Bestimmungen, wie insbesondere der Untersagung der Weitergabe der bekannten Informationen an Dritte, wirksam abgeschlossen worden sei oder bestehe, sodass der Beklagten keine wie auch immer gearteten Rechte gegenüber der Klägerin zustünden.

**False Positives:**

- `Lizenzen` — no gold match — likely missing annotation
- `Daten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_13`)


Das von § 28 Abs 1 Z 2 JN geforderte Naheverhältnis der Klägerin zum Inland ergebe sich aus dem inländischen Unternehmenssitz der Klägerin.

**False Positives:**

- `Das` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_14`)


Die Unzumutbarkeit der Rechtsverfolgung im Ausland ergebe sich daraus, dass eine ausländische Entscheidung in Österreich nicht anerkannt und vollstreckt werden würde, eine dringende Entscheidung nicht erreicht werden könne und eine Prozessführung im Ausland äußerst kostspielig wäre.

**False Positives:**

- `Die Unzumutbarkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_22`)


Das Vorliegen der zweiten Voraussetzung (nämlich die Unmöglichkeit oder Unzumutbarkeit der Rechtsverfolgung im Ausland) wird in der Rechtsprechung insbesondere dann bejaht, wenn die ausländische Entscheidung in Österreich nicht anerkannt oder vollstreckt wird (unter der weiteren Voraussetzung, dass eine Exekutionsführung im Inland überhaupt geplant ist - RIS-Justiz RS0046148 [T10]), eine dringende Entscheidung im Ausland nicht rechtzeitig erreicht werden kann, eine Prozessführung im Ausland wenigstens eine der Parteien politischer Verfolgung aussetzen würde oder wenn die Prozessführung im Ausland äußerst kostspielig wäre (MayrinRechberger, ZPO4§ 28 JN Rz 4 mwN; RIS-Justiz RS0046148).

**False Positives:**

- `Das Vorliegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_25`)


Dabei ist im vorliegenden Fall im Hinblick auf das von der Klägerin ausschließlich erhobene Feststellungsbegehren zu berücksichtigen, dass ein Feststellungsurteil eines ausländischen Gerichts, das eine vermögensrechtliche Angelegenheit zum Gegenstand hat, auf Antrag einer der Parteien gemäß den §§ 79, 85 EO im Inland zwar anerkannt werden kann, Feststellungsurteile aber nur deklarative Wirkung haben, also keinen Leistungsanspruch schaffen, und daher - abgesehen von einem in das Urteil aufgenommenen Leistungsausspruch über den Prozesskostenersatz - nicht vollstreckbar sind (vglFaschinginFasching/Konecny2III § 228 ZPO Rz 145).

**False Positives:**

- `Feststellungsurteile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_26`)


Den Angaben der Klägerin ist nicht zu entnehmen, dass die Beklagte über irgendein Vermögen im Inland verfügt.

**False Positives:**

- `Den Angaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_33`)


Konkrete Umstände des Einzelfalls, die auf eine besondere Kostspieligkeit der Rechtsverfolgung in Hongkong hindeuten würden, hat die Klägerin nicht dargetan.

**False Positives:**

- `Konkrete Umstände` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Russische Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_5`)


Die Mutter und die Kinder sind Staatsangehörige der Russischen Föderation und als Asylwerber im Inland aufhältig.

**False Positives:**

- `Die Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_4`)


Text Begründung: Die Klägerin macht gegen die beklagte Partei, eine ägyptische Fluglinie, Ansprüche nach der Verordnung (EG) 261/2004 des Europäischen Parlaments und des Rates vom 11. Februar 2004 über eine gemeinsame Regelung für Ausgleichs- und Unterstützungsleistungen für Fluggäste im Fall der Nichtbeförderung und bei Annullierung oder großer Verspätung von Flügen (EU-Fluggastrechte-VO) geltend.

**False Positives:**

- `Ansprüche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `names_with_legal_titles`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b7b0ec68`  
**Description:**
Matches names preceded by specific legal titles like 'Senatspräsident', 'Hofrat', 'Vizepräsident' to ensure the full name is captured including the title context.

**Content:**
```
(?:Senatspräsident(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|Vizepräsident(?:in)?|Hofrat(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|fachkundiger\s+Laienrichter(?:in)?|Richter(?:in)?|Schriftführer(?:in)?|Generalprokurator(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Rechtsanwält(?:in)?)(\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 307 | 0 | 307 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 307 | 4148 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schramm`
- `Univ` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Florens Drehkopf, LLB`(person)
- `16. Dezember 1952`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Nowotny`
- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Nowotny`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gmb` — similar text (different position): `Hochenadel Immobilien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Eva Abdelrahman`(person)
- `Dr. Karl-Heinz Plankel`(person)
- `Hochenadel Immobilien GmbH`(organisation)
- `Ritterhof 11, 2661 Graben, Österreich`(address)
- `Lederer Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Juri Gerstl`(person)
- `Mutten 18, 3251 Schauboden, Österreich`(address)
- `Dr. Ralph Trischler`(person)
- `Bundesbeschaffung GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `DDr.in Cornelia Rinaldo`(person)
- `Dr. Sven Rudolf Thorstensen`(person)
- `Conmon-Verlag Limited`(organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich`(address)
- `Brandl Talos Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Bau Zorostfurt GmbH`(organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich`(address)
- `Dr. Alexandra Slama`(person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH`(organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich`(address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Sandra Hilt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sandra Hilt`(person)
- `Mag. Manuel Kumas`(person)
- `MMMag. Gottfried Fegbeitel`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Paolo Barley`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Paolo Barley`(person)
- `Mag. Klarissa Hausteiner`(person)
- `Mag. Viola Brauch`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Maja Dolleschell`(person)
- `14. August`(date)
- `Bezirkshauptmannschaft Melk`(organisation)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts Melk`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Leander Andermann`(person)
- `Dr. Martin Leitner`(person)
- `Ing. Ferdinand Abramova`(person)
- `Mag. Wilhelm Deutschmann MBA`(person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Dr. Annerl`(person)
- `Meinrad Bruhnsen`(person)
- `30. Januar`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Othmar Mertl`(person)
- `Malik Fridt`(person)
- `Krist Bubits Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Dr` — similar text (different position): `Univ.-Prof. Dr. Neumayr`
- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Scarlett Achatzi`(person)
- `Mag. Ewald Aszmutat`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Gmb` — partial — pred is substring of gold: `Vogl Rechtsanwalt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `DI Cassandra Wespi`(person)
- `Vogl Rechtsanwalt GmbH`(organisation)
- `Bilek Lebensmittel GmbH`(organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich`(address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — similar text (different position): `Dr. Hradil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofrat Dr. Fellinger`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `KR Hermann Furtner`(person)
- `AR Angelika Neuhauser`(person)
- `Birgit Jaros`(person)
- `Dr. Herbert Pochieser`(person)
- `Dr. Heinz Edelmann`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr` — similar text (different position): `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Schwab`

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

**Example 24** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Schwab`

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

**Example 25** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Solé`
- `Dr` — similar text (different position): `Dr. Solé`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 26** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel treten aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an deren Stelle (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Schroll`

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

</details>

---

## `bare_names_after_verbs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2683a416`  
**Description:**
Matches bare names after verbs like 'wurde', 'besteht bei', 'entstammt'. Excludes trailing whitespace and common false positives.

**Content:**
```
(?:wurde\s+|besteht\s+bei\s+|entstammt\s+|hat\s+|habe\s+|sei\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 71 | 0 | 71 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 71 | 4108 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

**False Positives:**

- `Ordinationsanträgen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_42`)


Bei jeder Mahnung hat Waldkelkraft auf die Möglichkeit zur Inanspruchnahme der Beratungsstelle des bestehenden Energielieferanten, soweit diese gemäß § 82 Abs 7 ElWOG einzurichten ist, hinzuweisen.

**False Positives:**

- `Waldkelkraft ` — partial — gold is substring of pred: `Waldkelkraft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldkelkraft`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_48`)


Die faktische Geschäftsführung habe Ottokar Lucker ausgeübt.

**False Positives:**

- `Ottokar Lucker ` — partial — gold is substring of pred: `Ottokar Lucker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottokar Lucker`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_160`)


Wenngleich dieses Kriterium in § 25d Abs 2 KSchG nicht (nochmals) unmittelbar einbezogen werden kann, ist es doch der Abstufung zugänglich und hat Einfluss auf die Gesamtbewertung (RIS-Justiz RS0115165 [T2]).

**False Positives:**

- `Einfluss ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_94`)


Im vorliegenden Fall sei Gegenstand des Rechtsstreits aber nur eine Leistungssache nach § 65 Abs 1 Z 1 ASGG.

**False Positives:**

- `Gegenstand ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_165`)


Der Kläger hat seine - wenngleich als „sozialrechtlich“ bezeichnete - Klage auch auf den Titel der Amtshaftung und darüber hinaus auf sämtliche erdenklichen Rechtsgrundlagen mit dem Vorbringen gestützt, die beklagte Partei habe Leistungen bewilligt, ohne ihn darüber aufzuklären, dass Kostenersatz nicht möglich sei.

**False Positives:**

- `Leistungen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_28`)


11. 2015 im Herz Jesu Heim in Neuratting 52, 4943 Nonsbach, Österreich als „Hilfsarbeiterin“ beschäftigt gewesen sei, sei Ergebnis einer unbedenklichen Beweiswürdigung.

**False Positives:**

- `Ergebnis ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Neuratting 52, 4943 Nonsbach, Österreich`(address)

**Example 7** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Andreas Safranski des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB schuldig erkannt.

**False Positives:**

- `Andreas Safranski ` — partial — gold is substring of pred: `Andreas Safranski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Safranski`(person)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_5`)


Gründe:  Rechtliche Beurteilung Bereits mit Beschlüssen des Obersten Gerichtshofs vom 15. September 2011, AZ 12 Ns 56/11y (12 Ns 75/11t), und vom 24. Oktober 2011, AZ 12 Ns 89/11a, wurde Anträgen des Angeklagten auf Delegierung nach § 39 Abs 1 StPO nicht Folge gegeben.

**False Positives:**

- `Anträgen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

**False Positives:**

- `Thomas Maksym ` — partial — gold is substring of pred: `Thomas Maksym`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Maksym`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_8`)


Text Gründe: Mit dem angefochtenen Urteil wurde Thomas Leesmeister des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB (A./) sowie mehrerer Vergehen der Fälschung eines Beweismittels nach § 293 Abs 1 StGB (B./) schuldig erkannt.

**False Positives:**

- `Thomas Leesmeister ` — partial — gold is substring of pred: `Thomas Leesmeister`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Leesmeister`(person)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Ernst`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Maximilian Gudzentat der Verbrechen des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (1./), der Vergewaltigung nach § 201 Abs 1 StGB und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (2./) sowie des Vergehens der Nötigung nach § 105 Abs 1 StGB (3./) schuldig erkannt.

**False Positives:**

- `Maximilian Gudzentat ` — partial — gold is substring of pred: `Maximilian Gudzentat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximilian Gudzentat`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_10`)


Mit gekürzt ausgefertigtem Urteil des Landesgerichts Feldkirch vom 2. September 2013, GZ 20 Hv 68/13f-13, wurde Sabrina Harrazin im Sinne dieser Alternativanklage schuldig erkannt.

**False Positives:**

- `Sabrina Harrazin ` — partial — gold is substring of pred: `Sabrina Harrazin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Sabrina Harrazin`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__11`)


Am 4. April 2017 wurde Zoltan Sundmacher von den ungarischen Behörden an Österreich übergeben (ON 136).

**False Positives:**

- `Zoltan Sundmacher von` — partial — gold is substring of pred: `Zoltan Sundmacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zoltan Sundmacher`(person)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

**False Positives:**

- `Nikola Miscenko ` — partial — gold is substring of pred: `Nikola Miscenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Salzburg`(organisation)
- `Nikola Miscenko`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Martin Pollaczek des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Martin Pollaczek ` — partial — gold is substring of pred: `Martin Pollaczek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Martin Pollaczek`(person)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Mehdi Rater des Vergehens (richtig: Verbrechens) des Raubes nach §§ 15, 142 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Mehdi Rater ` — partial — gold is substring of pred: `Mehdi Rater`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mehdi Rater`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Thomas Eschberger der Verbrechen der Vergewaltigung nach § 201 Abs 2 StGB idF BGBl I 2001/130 (I) und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 und 3 erster Fall StGB (II/A/1), jeweils mehrerer Verbrechen des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (II/A/1) und des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (II/A/2) sowie mehrerer Vergehen des Missbrauchs eines Autoritätsverhältnisses nach § 212 Abs 1 Z 2 StGB (II/A/3) schuldig erkannt.

**False Positives:**

- `Thomas Eschberger ` — partial — gold is substring of pred: `Thomas Eschberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Eschberger`(person)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Karl Wodarcyk des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Karl Wodarcyk ` — partial — gold is substring of pred: `Karl Wodarcyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karl Wodarcyk`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__8`)


Text Gründe: Mit dem angefochtenen Urteil wurde Erik Justing (richtig:) mehrerer Verbrechen des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 2 Z 1 (zu ergänzen: iVm Abs 3 zweiter Fall) SMG (I/1) sowie der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall SMG (I/2) und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB (II) schuldig erkannt.

**False Positives:**

- `Erik Justing ` — partial — gold is substring of pred: `Erik Justing`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Erik Justing`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_6`)


Text Gründe: Mit in Rechtskraft erwachsenem Urteil des Landesgerichts für Strafsachen Graz vom 23. April 2015, AZ 16 Hv 32/15a, wurde Wolfgang Woerz zu einer Freiheitsstrafe von fünfzehn Monaten verurteilt, wovon ein Strafteil von zehn Monaten gemäß § 43a

**False Positives:**

- `Wolfgang Woerz zu` — partial — gold is substring of pred: `Wolfgang Woerz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Wolfgang Woerz`(person)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_8`)


Mit rechtskräftigem Abwesenheitsurteil des Bezirksgerichts Weiz vom 25. Juli 2018, GZ 10 U 13/17b-69, wurde Wenholz einer (vom 9. Mai 2016 bis zum 7. September 2017 begangenen) strafbaren Handlung schuldig erkannt.

**False Positives:**

- `Wenholz ` — partial — gold is substring of pred: `Wenholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Weiz`(organisation)
- `Wenholz`(person)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_7`)


Text Gründe: Mit dem angefochtenen Urteil wurde Aissa Boness des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Aissa Boness ` — partial — gold is substring of pred: `Aissa Boness`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Aissa Boness`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Michael Wessollek des Vergehens der Sachbeschädigung nach § 125 StGB (1/a), des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB (1/b) und des Vergehens der Körperverletzung nach § 83 Abs 1 StGB (2) schuldig erkannt.

**False Positives:**

- `Michael Wessollek ` — partial — gold is substring of pred: `Michael Wessollek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Michael Wessollek`(person)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__7`)


Text Gründe: Mit Urteil des Bezirksgerichts Innere Stadt Wien (ON 19) wurde Robert Ulrici jeweils eines Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB schuldig erkannt und hiefür zu einer bedingt nachgesehenen Freiheitsstrafe verurteilt. Nach Verkündung des Urteils und erteilter Rechtsmittelbelehrung erklärte der – nicht durch einen Verteidiger vertretene (vgl § 57 Abs 2 dritter Satz StPO;Fabrizy, StPO13§ 57 Rz 10) – Angeklagte zunächst, auf Rechtsmittel zu verzichten (ON 18 S 5).

**False Positives:**

- `Robert Ulrici ` — partial — gold is substring of pred: `Robert Ulrici`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Robert Ulrici`(person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Ernst Goerlich mehrerer Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB (B) und des Vergehens des sexuellen Missbrauchs von Jugendlichen nach §§ 15, 207b Abs 3 StGB (A) schuldig erkannt.

**False Positives:**

- `Ernst Goerlich ` — partial — gold is substring of pred: `Ernst Goerlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ernst Goerlich`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_5`)


Text Gründe: Mit Urteil des Landesgerichts Klagenfurt als Einzelrichter vom 13. Mai 2019 (ON 20) wurde Christoph Huertler des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB schuldig erkannt und zu einer Geldstrafe sowie dazu verurteilt, dem Privatbeteiligten Fabian Pfandler 500 Euro Schmerzengeld zu zahlen.

**False Positives:**

- `Christoph Huertler ` — partial — gold is substring of pred: `Christoph Huertler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Klagenfurt`(organisation)
- `Christoph Huertler`(person)
- `Fabian Pfandler`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_6`)


Indem sie nämlich - zusammengefasst - allgemein behauptet, der Beschwerdeführer sei Opfer staatlich veranlasster unzulässiger Tatprovokation geworden, und sich weiters gegen die als gesetzwidrig erachtete Verfahrensführung des - nach dem Beschwerdestandpunkt parteilichen und voreingenommenen - Vorsitzenden des Schöffensenats in der am 11. August 2010 durchgeführten und auf unbestimmte Zeit vertagten Hauptverhandlung wendet, richtet sie sich nicht gegen eine - genau zu bezeichnende (§ 3 Abs 1 GRBG) - mit Grundrechtsbeschwerde anfechtbare strafgerichtliche Entscheidung oder Verfügung nach Ausschöpfung des Instanzenzugs (§ 1 Abs 1 GRBG).

**False Positives:**

- `Opfer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__7`)


Text Gründe: Mit Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 2. Dezember 2010, GZ 15 Hv 126/10k-38, wurde Bernd Kalverkamp der Verbrechen der absichtlichen schweren Körperverletzung nach § 87 Abs 1 und Abs 2 erster Fall StGB (I/1) und der schweren Nötigung nach §§ 15, 105 Abs 1, 106 Abs 1 Z 1 und 2 StGB (I/2) schuldig erkannt und hiefür unter Anwendung des § 28 StGB nach § 87 Abs 2 erster Halbsatz StGB zu einer Freiheitsstrafe von 18 (achtzehn) Monaten verurteilt, wovon gemäß § 43a Abs 3 StGB ein Teil von 15 (fünfzehn) Monaten bedingt nachgesehen wurde.

**False Positives:**

- `Bernd Kalverkamp ` — partial — gold is substring of pred: `Bernd Kalverkamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Bernd Kalverkamp`(person)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

</details>

---

<details>
<summary>📋 All Rules</summary>

## `names_with_titles_and_suffixes`

**F1:** 0.282 | **Precision:** 0.321 | **Recall:** 0.252  

**Format:** `regex`  
**Rule ID:** `f6c3e39a`  
**Description:**
Matches names with academic/professional titles, capturing the full name including suffixes, while handling titles followed by institutional phrases.

**Content:**
```
(?:OMedR|OSR|StR|Techn\s+R|RgR|MedR|Prof\.in|DDr|OStR|HR|VetR|KzlR|KzlR\s+RgR|Senatspräsident(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|Vizepräsident(?:in)?|Hofrat(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|fachkundiger\s+Laienrichter(?:in)?|Richter(?:in)?|Schriftführer(?:in)?|Generalprokurator(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Rechtsanwält(?:in)?|Univ\.-?Prof\.\s+Dr\.\s+|Hon\.-?Prof\.\s+PD\s+Dr\.\s+|Hon\.-?Prof\.\s+Dr\.\s+|Univ\.-?Prof\.\s+|Prof\.\s+Dr\.\s+|Dr\.\s+Univ\.-?Prof\.\s+|Dr\.\s+|Mag\.\s+|Mag\.\s+Dr\.\s+|MMag\.\s+|DI\s+|Dipl\.-?Ing\.\s+|Bakk\.+\s+iur\.+\s+|Priv\.-?Doz\.\s+|Dipl\.\s+|Ing\.\s+|OSR\s+|StR\s+|Prof\.in\s+Univ\.-?Prof\.\s+|MedR\s+|RgR\s+|StR\s+|HR\s+|VetR\s+|KzlR\s+|KzlR\s+RgR\s+|Senatspräsident\s+des\s+Obersten\s+Gerichtshofs\s+|Vizepräsident\s+des\s+Obersten\s+Gerichtshofs\s+|Hofrat\s+des\s+Obersten\s+Gerichtshofs\s+|fachkundiger\s+Laienrichter\s+des\s+Obersten\s+Gerichtshofs\s+|Richter\s+des\s+Obersten\s+Gerichtshofs\s+|Schriftführer\s+des\s+Obersten\s+Gerichtshofs\s+|Generalprokurator\s+des\s+Obersten\s+Gerichtshofs\s+|Anwalt\s+des\s+Obersten\s+Gerichtshofs\s+|Rechtsanwalt\s+des\s+Obersten\s+Gerichtshofs\s+|Rechtsanwältin\s+des\s+Obersten\s+Gerichtshofs\s+|Univ\.-?Prof\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Hon\.-?Prof\.\s+PD\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Hon\.-?Prof\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Univ\.-?Prof\.\s+des\s+Obersten\s+Gerichtshofs\s+|Prof\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Dr\.\s+Univ\.-?Prof\.\s+des\s+Obersten\s+Gerichtshofs\s+|Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|Mag\.\s+des\s+Obersten\s+Gerichtshofs\s+|Mag\.\s+Dr\.\s+des\s+Obersten\s+Gerichtshofs\s+|DI\s+des\s+Obersten\s+Gerichtshofs\s+|Dipl\.-?Ing\.\s+des\s+Obersten\s+Gerichtshofs\s+|Bakk\.+\s+iur\.+\s+des\s+Obersten\s+Gerichtshofs\s+|Priv\.-?Doz\.\s+des\s+Obersten\s+Gerichtshofs\s+|Dipl\.\s+des\s+Obersten\s+Gerichtshofs\s+|Ing\.\s+des\s+Obersten\s+Gerichtshofs\s+|OSR\s+des\s+Obersten\s+Gerichtshofs\s+|StR\s+des\s+Obersten\s+Gerichtshofs\s+|Prof\.in\s+Univ\.-?Prof\.\s+des\s+Obersten\s+Gerichtshofs\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.321 | 0.252 | 0.282 | 3276 | 1051 | 2225 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1051 | 2225 | 3114 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Rützler` | `Mag. Martin Rützler` |
| `Mag. Klaus Köck` | `Mag. Klaus Köck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ernst Michael Lang` | `Mag. Ernst Michael Lang` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Kordelia Meelis` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)
- `Fatima Tengel` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)
- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Ober-Automotive GmbH` (organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Katharina Rothschadl` (person)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Maximilian Kocher` | `Mag. Maximilian Kocher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Bezirksgerichts Kitzbühel` (organisation)
- `Karin Ciliberto` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Dr. Roland Kassowitz` | `Dr. Roland Kassowitz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Landesgerichts Linz` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Thomas Girardi` | `Dr. Thomas Girardi` |
| `Dr. Franz Pechmann` | `Dr. Franz Pechmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mur Dorftalnex Technologien -GmbH` (organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich` (address)
- `Dr. Peter` (person)
- `Dr. Hermann` (person)
- `Ober Dertri GmbH` (organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich` (address)
- `Rudolf Ketelhut` (person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich` (address)
- `Dr. Bernhard Hämmerle GmbH` (organisation)
- `Völkertz Energie GmbH` (organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich` (address)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Alois Schneider` | `Dr. Alois Schneider` |
| `Dr. Walter Hausberger` | `Dr. Walter Hausberger` |
| `Dr. Alfred Schmidt` | `Dr. Alfred Schmidt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Stefula` (person)
- `Schneidergruberweg 37, 5132 Reith, Österreich` (address)
- `Dario von Ebers` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `HR Sophie Elefteriadis` | `HR Sophie Elefteriadis` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Karl-Heinz Plankel` | `Dr. Karl-Heinz Plankel` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Eva Abdelrahman` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Lederer Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ralph Trischler` | `Dr. Ralph Trischler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Bundesbeschaffung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Bernhard Birek` | `Dr. Bernhard Birek` |
| `Mag. Christian Breit` | `Mag. Christian Breit` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Ludmilla von Amelunxen` (person)
- `Svetlana Leinhäuser` (person)
- `Dr. Thomas` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Mag. Kevin Maassen` | `Mag. Kevin Maassen` |
| `Dr. Clemens Lintschinger` | `Dr. Clemens Lintschinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Mag. Dr. Georg Backhausen` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Helwig Schuster` | `Mag. Helwig Schuster` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Hofrätin Dr. Wallner-Friedl` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Walter Reichholf` | `Dr. Walter Reichholf` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Verein für Konsumenteninformation` (organisation)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Kraft & Winternitz Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. PD Dr. Rassi` | `Hon.-Prof. PD Dr. Rassi` |
| `Mag. Franz Eckl` | `Mag. Franz Eckl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Dr. Steger` (person)
- `Dr. Annerl` (person)
- `Hofrätin Dr. Wallner-Friedl` (person)
- `Ralph Prusseit` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Faber` | `Dr. Faber` |
| `Dr. Sven Rudolf Thorstensen` | `Dr. Sven Rudolf Thorstensen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


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

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Oliver Simoncic` | `Mag. Oliver Simoncic` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr.Neumayr` (person)
- `Dr. Schramm` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `AXA Software Institut Gesellschaft mbH` (organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich` (address)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Anton Bohmert` | `Mag. Anton Bohmert` |

**Missed by this rule (FN):**

- `Lars Ballogh` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei James Jooß, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Klaus Schiller` | `Dr. Klaus Schiller` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `James Jooß` (person)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Michael Schneditz-Bolfras` | `Dr. Michael Schneditz-Bolfras` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Gustav Thöning` | `Dr. Gustav Thöning` |
| `Dr. Madeleine Musialik` | `Dr. Madeleine Musialik` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofräte Dr. Schramm` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Pieler & Pieler & Partner KG` (organisation)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Dr. Alexandra Slama` | `Dr. Alexandra Slama` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Bau Zorostfurt GmbH` (organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich` (address)
- `Buitenkamp und Rothauge Landwirtschaft GmbH` (organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich` (address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Mag. Herwig Bortzlaff` | `Mag. Herwig Bortzlaff` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

| Predicted | Gold |
|---|---|
| `Dr. Sandra Hilt` | `Dr. Sandra Hilt` |

**Missed by this rule (FN):**

- `Mag. Manuel Kumas` (person)
- `MMMag. Gottfried Fegbeitel` (person)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Mag. Hans-Christian Obernberger` | `Mag. Hans-Christian Obernberger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Jaden Meyerjohann` (person)
- `3. Juli 2020` (date)
- `Leroy Jungschmidt` (person)
- `28. Mai 1965` (date)
- `Clemens Theocharakis` (person)
- `25. März 1999` (date)
- `Emanuela Janischefsky` (person)
- `Bezirkshauptmannschaft Feldkirch` (organisation)
- `Ashley Biesert` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Melk` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Martin Leitner` | `Dr. Martin Leitner` |
| `Ing. Ferdinand Abramova` | `Ing. Ferdinand Abramova` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Leander Andermann` (person)
- `Mag. Wilhelm Deutschmann MBA` (person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Johannes Bügler` | `Mag. Johannes Bügler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Langhansl+Antonewitz Chemie AG` (organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich` (address)
- `Poinstingl & Partner Rechtsanwälte OG` (organisation)
- `Drau-Pharma GmbH` (organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. PD Dr. Rassi` | `Hon.-Prof. PD Dr. Rassi` |
| `Dr. Sandro Gädecken` | `Dr. Sandro Gädecken` |
| `Dr. Oliver Kühnl` | `Dr. Oliver Kühnl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Hofrätin Dr. Wallner-Friedl` (person)
- `Karim Mielewczik` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Ing. Emanuel Puff` | `Ing. Emanuel Puff` |
| `Dr. Gottfried Kassin` | `Dr. Gottfried Kassin` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Maja Pirkmayr` (person)
- `Dr. Georg Gorton` (person)
- `DDr. Birgit Gorton` (person)
- `Landesgerichts Klagenfurt` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Mag. Werner Thurner` | `Mag. Werner Thurner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `DI Dr. Bodo Kaczynski` (person)
- `25. Juli 1975` (date)
- `Wolfgang Lombardini` (person)
- `4. Dezember 2022` (date)
- `Livia Löblein` (person)
- `11. Januar 1966` (date)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_4`)


Dr. Serge Schieferle, Niederlande, und 3.)

| Predicted | Gold |
|---|---|
| `Dr. Serge Schieferle` | `Dr. Serge Schieferle` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Felix Cornils` | `Dr. Felix Cornils` |

**Missed by this rule (FN):**

- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Othmar Mertl` (person)
- `Malik Fridt` (person)
- `Krist Bubits Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Mag. Ewald Aszmutat` | `Mag. Ewald Aszmutat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Scarlett Achatzi` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hoch` | `Dr. Hoch` |
| `Mag. Dirk Hükelheim` | `Mag. Dirk Hükelheim` |
| `Mag. Roland Marko` | `Mag. Roland Marko` |
| `Dr. Francisco Rumpf` | `Dr. Francisco Rumpf` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofräte Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Mikolaj Eleftheriadou` (person)
- `Helge Schuchmann` (person)
- `Isabel Rahnfeld` (person)
- `PhD Daniel Coutand` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Grohmann` | `Dr. Grohmann` |
| `DI Cassandra Wespi` | `DI Cassandra Wespi` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hofrätinnen Dr. Fichtenau` (person)
- `Hofrat Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Vogl Rechtsanwalt GmbH` (organisation)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Schober` | `Mag. Schober` |
| `Mag. Benedikt Walch` | `Mag. Benedikt Walch` |
| `Mag. German Bertsch` | `Mag. German Bertsch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Dr. Weber` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Agatha von der Heide` (person)
- `MMag. Dr. Sebastian Pribas` (person)
- `Alva Sengül` (person)
- `Selina Birkmeir` (person)
- `Harald Ladwig, LLM` (person)
- `In der Klaus 72, 4785 Bach, Österreich` (address)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Christoph Orgler` | `Dr. Christoph Orgler` |
| `Dr. Michael Stögerer` | `Dr. Michael Stögerer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Thomas` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Herbert Pochieser` | `Dr. Herbert Pochieser` |
| `Dr. Heinz Edelmann` | `Dr. Heinz Edelmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Hofrat Dr. Fellinger` (person)
- `Hofrätin Dr. Fichtenau` (person)
- `KR Hermann Furtner` (person)
- `AR Angelika Neuhauser` (person)
- `Birgit Jaros` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Marie-Luise Safranek` | `Dr. Marie-Luise Safranek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Hofräte Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Mag. Höpler` | `Mag. Höpler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Dr. Oshidari` (person)
- `Dr. Parapatits` (person)
- `Bernhard Buddäus` (person)
- `Norbert Wehrhahn` (person)
- `Landesgerichts Salzburg` (organisation)
- `Mag. Rienmüller` (person)

**Example 51** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Mag. Sommer` (person)
- `Richard Lindt` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Dr. Oshidari` (person)
- `Mag. Kurzthaler` (person)
- `Andreas Schiessl` (person)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Rathgeb` (person)
- `Daniel Kur` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Marek` | `Mag. Marek` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Wieser` (person)
- `Gerald Winand` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Herwig Bäseke` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Fürnkranz` (person)
- `OGH` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Fürnkranz` (person)
- `Mag. Herwig Berto` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

| Predicted | Gold |
|---|---|
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Dr. Setz-Hummel` | `Dr. Setz-Hummel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Fürnkranz` (person)

**Example 58** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


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

**Example 59** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_5`)


An Stelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger tritt Hofrat des Obersten Gerichtshofs Dr. Nordmeyer.

| Predicted | Gold |
|---|---|
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_11`)


Hofrat des Obersten Gerichtshofs Dr. Nordmeyer tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs anstelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_5`)


An deren Stelle treten Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski.

| Predicted | Gold |
|---|---|
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Obersten Gerichtshofs` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

| Predicted | Gold |
|---|---|
| `Dr. Christine Schwab` | `Dr. Christine Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Vollmaier ` — partial — gold is substring of pred: `Dr. Vollmaier`
- `Mag. Alexander Gerngross ` — partial — gold is substring of pred: `Mag. Alexander Gerngross`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Vollmaier`(person)
- `Jason Langeloh`(person)
- `Mag. Martin Rützler`(person)
- `Selma Einoeder`(person)
- `Mag. Alexander Gerngross`(person)
- `Mag. Klaus Köck`(person)
- `Bezirksgerichts Graz-Ost`(organisation)
- `Bezirksgericht Dornbirn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_6`)


Er habe den von der Beklagten erworbenen, mangelhaften PKW VW Golf VII Variant 1.6 TDI Comfort aufgrund deren Verbesserungsverweigerung selbst reparieren lassen müssen, wodurch ihm Kosten in dieser Höhe entstanden seien.

**False Positives:**

- `DI Comfort ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Florens Drehkopf, LLB`(person)
- `16. Dezember 1952`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger ` — positional overlap with gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Schramm`(person)
- `Gerhard Lohrmann`(person)
- `10. August 1983`(date)
- `Veit Künneken`(person)
- `31. Mai 1967`(date)
- `Bezirksgerichts Feldkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Dr. Nowotny ` — partial — gold is substring of pred: `Dr. Nowotny`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Nowotny`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger ` — positional overlap with gold: `Hofräte Dr. Fellinger`
- `Dr. Hoch ` — partial — gold is substring of pred: `Dr. Hoch`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`
- `KzlR Iris Makowska` — partial — pred is substring of gold: `Hon.-Prof.in KzlR Iris Makowska`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hon.-Prof.in KzlR Iris Makowska`(person)
- `Skribe Rechtsanwaelte GmbH`(organisation)
- `Dieter Apfelbacher`(person)
- `Am Fundbach 31w, 9170 Tratten, Österreich`(address)
- `Bezirksgericht Schwechat`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger ` — positional overlap with gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Neumayr`(person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich`(address)
- `Manfred Johann Puff`(person)
- `Bezirksgerichts Kitzbühel`(organisation)
- `Karin Ciliberto`(person)
- `Mag. Maximilian Kocher`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht Linz`(organisation)
- `Steidlen+Ysner Daten GmbH`(organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich`(address)
- `Dr. Roland Kassowitz`(person)
- `Verlag Waldlemder GmbH`(organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich`(address)
- `Prof. Haslinger`(person)
- `Landesgerichts Linz`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Peter Lechner ` — partial — gold is substring of pred: `Dr. Peter`
- `Dr. Hermann Pfurtscheller` — partial — gold is substring of pred: `Dr. Hermann`
- `Dr. Bernhard Hämmerle Gmb` — partial — pred is substring of gold: `Dr. Bernhard Hämmerle GmbH`

> overlaps gold: 7  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mur Dorftalnex Technologien -GmbH`(organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich`(address)
- `Dr. Peter`(person)
- `Dr. Hermann`(person)
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

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`
- `Mag. Ziegelbauer ` — partial — gold is substring of pred: `Mag. Ziegelbauer`
- `Dr. Stefula ` — partial — gold is substring of pred: `Dr. Stefula`
- `Dr. Katharina Moritz ` — no gold match — likely missing annotation

> overlaps gold: 5  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Stefula`(person)
- `Schneidergruberweg 37, 5132 Reith, Österreich`(address)
- `Dr. Alois Schneider`(person)
- `Dario von Ebers`(person)
- `Dr. Walter Hausberger`(person)
- `Dr. Alfred Schmidt`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Rattenberg`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Bartholomäus Junghahn`(person)
- `HR Sophie Elefteriadis`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_19`)


DasRekursgerichtgab dem Rekurs der beiden Minderjährigen Folge und änderte die Beschlüsse des Erstgerichts jeweils dahin ab, dass den Minderjährigen auch für den Monat Februar 2010 monatliche Unterhaltsvorschüsse in Höhe von 210 EUR (für den minderjährigen Ariadne Jefferys ) und von 180 EUR (für die minderjährige OStR Univ.-Prof.in Sascha Elfferding ) gewährt wurden.

**False Positives:**

- `StR Univ` — partial — pred is substring of gold: `OStR Univ.-Prof.in Sascha Elfferding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ariadne Jefferys`(person)
- `OStR Univ.-Prof.in Sascha Elfferding`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Korn ` — partial — gold is substring of pred: `Mag. Korn`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Eva Abdelrahman`(person)
- `Dr. Karl-Heinz Plankel`(person)
- `Hochenadel Immobilien GmbH`(organisation)
- `Ritterhof 11, 2661 Graben, Österreich`(address)
- `Lederer Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_6`)


Text Entscheidungsgründe: Über Vermittlung der Beklagten und nach Beratung durch deren Mitarbeiter Ing. Doris Waeltermann erwarb die Klägerin im Mai 2007 um 20.000 EUR Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Ing. Doris Waeltermann ` — partial — gold is substring of pred: `Ing. Doris Waeltermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Doris Waeltermann`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_7`)


Als sie einen Kursverfall dieser Aktien 2008/2009 zu einem nicht mehr näher feststellbaren Zeitpunkt wahrnahm, stellte sie erstmals fest, dass sie mit diesen Aktien ein Finanzprodukt erworben hatte, das weder dem Inhalt der Beratung des Ing. Lisa Widders noch vom Risiko und der Risikostreuung im „Portfolio“ her dem entsprach, was sie 2007 hatte erwerben wollen.

**False Positives:**

- `Ing. Lisa Widders ` — partial — gold is substring of pred: `Ing. Lisa Widders`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Lisa Widders`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Marion Woltz im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Ing. Marion Woltz ` — partial — gold is substring of pred: `Ing. Marion Woltz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Marion Woltz`(person)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr. Lovrek ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Lovrek`
- `Mag. Ziegelbauer` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Thunhart ` — partial — gold is substring of pred: `Dr. Thunhart`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Juri Gerstl`(person)
- `Mutten 18, 3251 Schauboden, Österreich`(address)
- `Dr. Ralph Trischler`(person)
- `Bundesbeschaffung GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Leander Lindlahr`(person)
- `Yussuf Prussog`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr` — partial — pred is substring of gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Hon.-Prof. Dr. Lovrek ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Lovrek`
- `Mag. Ziegelbauer` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Thomas Brückl` — partial — gold is substring of pred: `Dr. Thomas`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Mag. Dr` — partial — pred is substring of gold: `Mag. Dr. Georg Backhausen`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Mag. Schober` — partial — pred is substring of gold: `Hofräte Mag. Schober`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Vollmaier ` — partial — gold is substring of pred: `Dr. Vollmaier`
- `Dr. Wallner-Friedl` — partial — pred is substring of gold: `Hofrätin Dr. Wallner-Friedl`
- `Ing. Mag` — partial — pred is substring of gold: `Ing. Mag. Pamela Gotterbauer`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Hofrätin Dr. Wallner-Friedl`(person)
- `Ing. Mag. Pamela Gotterbauer`(person)
- `Mag. Helwig Schuster`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Verein für Konsumenteninformation`(organisation)
- `Dr. Walter Reichholf`(person)
- `SüdSanitär Gruppe GmbH`(organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich`(address)
- `Kraft & Winternitz Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Dr. Steger ` — positional overlap with gold: `Hofräte Dr. Steger`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Wallner-Friedl` — partial — pred is substring of gold: `Hofrätin Dr. Wallner-Friedl`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Hofräte Dr. Steger`(person)
- `Dr. Annerl`(person)
- `Hofrätin Dr. Wallner-Friedl`(person)
- `Ralph Prusseit`(person)
- `Mag. Franz Eckl`(person)
- `Akbayrak Metall GmbH`(organisation)
- `Schroateck 57, 4710 Niederweng, Österreich`(address)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)
- `Bezirksgerichts Zwettl`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Korn ` — partial — gold is substring of pred: `Mag. Korn`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Heimcon Software GmbH`(organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich`(address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH`(organisation)
- `Gunter Landwirtschaft GmbH`(organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich`(address)
- `Stolz & Schartner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Annabelle Thurnher`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Mag. Ziegelbauer` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `DDr.in Cornelia Rinaldo`(person)
- `Dr. Sven Rudolf Thorstensen`(person)
- `Conmon-Verlag Limited`(organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich`(address)
- `Brandl Talos Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Hofräte Univ.-Prof. Dr.Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Korn ` — partial — gold is substring of pred: `Mag. Korn`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr.Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `AXA Software Institut Gesellschaft mbH`(organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich`(address)
- `Mag. Oliver Simoncic`(person)

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_11`)


Da Ottokar Leuthäusser wegen eines Konkurses die Geschäftsführertätigkeit in Österreich nicht mehr ausüben konnte, fungierte vorerst Ing. Gerald Stoecks als handelsrechtlicher Geschäftsführer;

**False Positives:**

- `Ing. Gerald Stoecks ` — partial — gold is substring of pred: `Ing. Gerald Stoecks`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottokar Leuthäusser`(person)
- `Ing. Gerald Stoecks`(person)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_13`)


Am 12. 9. 2012 wurde der Zweitbeklagte auf Ersuchen des Ottokar Loehner als Nachfolger des Ing. Gerald Schmieden auch handelsrechtlicher Geschäftsführer.

**False Positives:**

- `Ing. Gerald Schmieden ` — partial — gold is substring of pred: `Ing. Gerald Schmieden`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottokar Loehner`(person)
- `Ing. Gerald Schmieden`(person)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Neumayr`(person)
- `Dr. Schramm`(person)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei James Jooß, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `James Jooß`(person)
- `Dr. Klaus Schiller`(person)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_37`)


Er äußerte dabei, mit Dipl. Kff. Iris Jakomait „nicht mehr arbeiten zu können und zu wollen“.

**False Positives:**

- `Dipl. Kff` — partial — pred is substring of gold: `Dipl. Kff. Iris Jakomait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl. Kff. Iris Jakomait`(person)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_41`)


Ein Schreiben von Dr. Hagen Janischewsky mit dem Inhalt, dass die Lizenzverträge einvernehmlich aufgehoben oder beendet worden seien, erreichte den Kläger nie.

**False Positives:**

- `Dr. Hagen Janischewsky ` — partial — gold is substring of pred: `Dr. Hagen Janischewsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hagen Janischewsky`(person)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm` — partial — pred is substring of gold: `Hofräte Dr. Schramm`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`
- `Mag. Ziegelbauer ` — partial — gold is substring of pred: `Mag. Ziegelbauer`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofräte Dr. Schramm`(person)
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

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Bau Zorostfurt GmbH`(organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich`(address)
- `Dr. Alexandra Slama`(person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH`(organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich`(address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Dr. Schinko ` — partial — gold is substring of pred: `Dr. Schinko`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Hon.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)
- `Mag. Herwig Bortzlaff`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_6`)


11. 2008, GZ 38 Nc 13/08i-2, den Ablehnungsantrag des Mag. Herwig Berkenbrink in dessen Rekurs gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 13.

**False Positives:**

- `Mag. Herwig Berkenbrink ` — partial — gold is substring of pred: `Mag. Herwig Berkenbrink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Herwig Berkenbrink`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

**False Positives:**

- `Mag. Manuel Kumas ` — partial — gold is substring of pred: `Mag. Manuel Kumas`
- `MMag. Gottfried Fegbeitel ` — positional overlap with gold: `MMMag. Gottfried Fegbeitel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sandra Hilt`(person)
- `Mag. Manuel Kumas`(person)
- `MMMag. Gottfried Fegbeitel`(person)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

**False Positives:**

- `Dr. Paolo Barley ` — partial — gold is substring of pred: `Dr. Paolo Barley`
- `Mag. Klarissa Hausteiner ` — partial — gold is substring of pred: `Mag. Klarissa Hausteiner`
- `Mag. Viola Brauch ` — partial — gold is substring of pred: `Mag. Viola Brauch`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Paolo Barley`(person)
- `Mag. Klarissa Hausteiner`(person)
- `Mag. Viola Brauch`(person)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
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

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Hoch ` — partial — gold is substring of pred: `Dr. Hoch`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Karsten Alberter`(person)
- `2. April 2010`(date)
- `Helmut Dreilich`(person)
- `Landesgerichts Korneuburg`(organisation)
- `Bezirksgerichts Schwechat`(organisation)
- `Lena Amini`(person)

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Maja Dolleschell`(person)
- `14. August`(date)
- `Bezirkshauptmannschaft Melk`(organisation)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts Melk`(organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Hon.-Prof. Dr. Lovrek ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Lovrek`
- `Mag. Ziegelbauer` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`
- `Mag. Schober ` — positional overlap with gold: `Hofräte Mag. Schober`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Mag. Wilhelm Deutschmann ` — partial — pred is substring of gold: `Mag. Wilhelm Deutschmann MBA`
- `Priv.-Doz. Mag` — partial — pred is substring of gold: `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`
- `Dr. Henriette Boscheinen-Duursma` — partial — pred is substring of gold: `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`

> overlaps gold: 8  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Leander Andermann`(person)
- `Dr. Martin Leitner`(person)
- `Ing. Ferdinand Abramova`(person)
- `Mag. Wilhelm Deutschmann MBA`(person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_11`)


Nach längeren Verhandlungen unterfertigte die Klägerin am 18. Dezember 2018 folgende Erklärung: „1. Wir haben gegen Ing. Kai Achler [...] ('der Schuldner') eine Forderung von 500.000,00 EUR (in Worten[richtig:]fünfhunderttausend).

**False Positives:**

- `Ing. Kai Achler ` — partial — gold is substring of pred: `Ing. Kai Achler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Kai Achler`(person)

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Korn ` — partial — gold is substring of pred: `Mag. Korn`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Mag. Johannes Bügler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Dr. Annerl ` — positional overlap with gold: `Hofräte Dr. Annerl`
- `Dr. Vollmaier ` — partial — gold is substring of pred: `Dr. Vollmaier`
- `Dr. Wallner-Friedl` — partial — pred is substring of gold: `Hofrätin Dr. Wallner-Friedl`
- `Ing. Dr` — partial — pred is substring of gold: `Ing. Dr. Stefan Krall`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Hofräte Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Hofrätin Dr. Wallner-Friedl`(person)
- `Karim Mielewczik`(person)
- `Dr. Sandro Gädecken`(person)
- `Ing. Dr. Stefan Krall`(person)
- `Dr. Oliver Kühnl`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Seekirchen`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Dr. Georg Gorton ` — partial — gold is substring of pred: `Dr. Georg Gorton`
- `Dr. Birgit Gorton` — partial — pred is substring of gold: `DDr. Birgit Gorton`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Maja Pirkmayr`(person)
- `Dr. Georg Gorton`(person)
- `DDr. Birgit Gorton`(person)
- `Ing. Emanuel Puff`(person)
- `Dr. Gottfried Kassin`(person)
- `Landesgerichts Klagenfurt`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`
- `Mag. Schober` — partial — pred is substring of gold: `Hofräte Mag. Schober`
- `Dr. Thunhart ` — partial — gold is substring of pred: `Dr. Thunhart`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Dr. Annerl`(person)
- `Meinrad Bruhnsen`(person)
- `30. Januar`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `DI Dr` — partial — pred is substring of gold: `DI Dr. Bodo Kaczynski`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `DI Dr. Bodo Kaczynski`(person)
- `25. Juli 1975`(date)
- `Mag. Werner Thurner`(person)
- `Wolfgang Lombardini`(person)
- `4. Dezember 2022`(date)
- `Livia Löblein`(person)
- `11. Januar 1966`(date)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-Ost`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Korn ` — partial — gold is substring of pred: `Mag. Korn`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
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

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_25`)


Mit dem nunmehr angefochtenen Beschluss vom 10. 12. 2014 (ON 106) gab das Rekursgericht dem Rekurs der Minderjährigen teilweise Folge und änderte den Titelbeschluss dahingehend ab, dass die Unterhaltspflicht ab 1. 3. 2012 mit monatlich insgesamt 220 EUR für Ludmilla Waßerthal und mit 160 EUR für Dipl. Kfm. Elias Meroldt festgesetzt wurde (Punkt 1 des Spruchs).

**False Positives:**

- `Dipl. Kfm` — partial — pred is substring of gold: `Dipl. Kfm. Elias Meroldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ludmilla Waßerthal`(person)
- `Dipl. Kfm. Elias Meroldt`(person)

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Othmar Mertl`(person)
- `Malik Fridt`(person)
- `Krist Bubits Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Dr. Grohmann ` — partial — gold is substring of pred: `Dr. Grohmann`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Scarlett Achatzi`(person)
- `Mag. Ewald Aszmutat`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger` — partial — pred is substring of gold: `Hofräte Dr. Fellinger`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Mikolaj Eleftheriadou`(person)
- `Helge Schuchmann`(person)
- `Isabel Rahnfeld`(person)
- `PhD Daniel Coutand`(person)
- `Mag. Dirk Hükelheim`(person)
- `Mag. Roland Marko`(person)
- `Dr. Francisco Rumpf`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätinnen Dr. Fichtenau`
- `Mag. Ziegelbauer ` — positional overlap with gold: `Hofrat Mag. Ziegelbauer`
- `Dr. Faber ` — partial — gold is substring of pred: `Dr. Faber`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `DI Cassandra Wespi`(person)
- `Vogl Rechtsanwalt GmbH`(organisation)
- `Bilek Lebensmittel GmbH`(organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich`(address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hon.-Prof. Dr. Nowotny ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Nowotny`
- `Dr. Weber` — partial — pred is substring of gold: `Hofräte Dr. Weber`
- `Dr. Annerl ` — partial — gold is substring of pred: `Dr. Annerl`
- `Dr. Vollmaier ` — partial — gold is substring of pred: `Dr. Vollmaier`
- `MMag. Dr` — partial — pred is substring of gold: `MMag. Dr. Sebastian Pribas`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hofräte Dr. Weber`(person)
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

**Example 65** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Ing. Christian Stangl-Brachnik` — partial — pred is substring of gold: `Ing. Christian Stangl-Brachnik, MA BA`
- `Mag. Claudia Gründel ` — partial — gold is substring of pred: `Mag. Claudia Gründel`
- `Dr. Thomas Stampfer ` — partial — gold is substring of pred: `Dr. Thomas`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Ing. Christian Stangl-Brachnik, MA BA`(person)
- `Mag. Claudia Gründel`(person)
- `Mathias Jendl`(person)
- `Dr. Thomas`(person)
- `Dr. Christoph Orgler`(person)
- `Dr. Michael Stögerer`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Hradil ` — partial — gold is substring of pred: `Dr. Hradil`
- `Dr. Fellinger ` — positional overlap with gold: `Hofrat Dr. Fellinger`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofrat Dr. Fellinger`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `KR Hermann Furtner`(person)
- `AR Angelika Neuhauser`(person)
- `Birgit Jaros`(person)
- `Dr. Herbert Pochieser`(person)
- `Dr. Heinz Edelmann`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Univ.-Prof. Dr. Neumayr ` — partial — gold is substring of pred: `Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Dr. Fichtenau ` — positional overlap with gold: `Hofrätin Dr. Fichtenau`
- `Dr. Gabriele Griehsel ` — partial — gold is substring of pred: `Dr. Gabriele Griehsel`
- `Dr. Wolfgang Kozak ` — partial — gold is substring of pred: `Dr. Wolfgang Kozak`

> overlaps gold: 5  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Fellinger ` — partial — gold is substring of pred: `Dr. Fellinger`
- `Univ.-Prof. Dr. Neumayr ` — positional overlap with gold: `Hofräte Univ.-Prof. Dr. Neumayr`
- `Dr. Schramm ` — partial — gold is substring of pred: `Dr. Schramm`
- `Mag. Dr` — partial — pred is substring of gold: `Mag. Dr. Wolfgang Höfle`
- `Ing. Thomas Bauer ` — partial — gold is substring of pred: `Ing. Thomas Bauer`
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft ` — partial — pred is substring of gold: `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`

> overlaps gold: 6  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mag. Dr. Wolfgang Höfle`(person)
- `Ing. Thomas Bauer`(person)
- `Willibald Kollowrat, BEd`(person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`(organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau`(organisation)
- `Dr. Marie-Luise Safranek`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Zehetner ` — partial — gold is substring of pred: `Dr. Zehetner`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`
- `Dr. Oshidari ` — partial — gold is substring of pred: `Dr. Oshidari`
- `Dr. Parapatits ` — partial — gold is substring of pred: `Dr. Parapatits`
- `Mag. Rienmüller zu` — partial — gold is substring of pred: `Mag. Rienmüller`

> overlaps gold: 5  |  likely missing annotation: 0

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

**Example 70** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Zehetner ` — partial — gold is substring of pred: `Dr. Zehetner`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`
- `Mag. Sommer ` — partial — gold is substring of pred: `Mag. Sommer`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 71** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Zehetner ` — partial — gold is substring of pred: `Dr. Zehetner`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`
- `Dr. Oshidari ` — partial — gold is substring of pred: `Dr. Oshidari`
- `Mag. Kurzthaler ` — partial — gold is substring of pred: `Mag. Kurzthaler`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Oshidari`(person)
- `Mag. Kurzthaler`(person)
- `Andreas Schiessl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Schwab ` — partial — gold is substring of pred: `Dr. Schwab`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`
- `Mag. Fürnkranz ` — partial — gold is substring of pred: `Mag. Fürnkranz`
- `Hofrat des Obersten Gerichtshofs Dr` — similar text (different position): `Obersten Gerichtshofs`
- `Mag. Rathgeb ` — partial — gold is substring of pred: `Mag. Rathgeb`

> overlaps gold: 5  |  likely missing annotation: 0

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

**Example 73** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Schwab ` — partial — gold is substring of pred: `Dr. Schwab`
- `Mag. Fürnkranz ` — partial — gold is substring of pred: `Mag. Fürnkranz`
- `Hofrat des Obersten Gerichtshofs Dr` — similar text (different position): `Obersten Gerichtshofs`
- `Mag. Wieser ` — partial — gold is substring of pred: `Mag. Wieser`

> overlaps gold: 4  |  likely missing annotation: 0

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

**Example 74** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Dr. Solé ` — partial — gold is substring of pred: `Dr. Solé`
- `Hofrat des Obersten Gerichtshofs Dr` — similar text (different position): `Obersten Gerichtshofs`
- `Mag. Herwig Bäseke ` — partial — gold is substring of pred: `Mag. Herwig Bäseke`
- `Dr. Schwab ` — partial — gold is substring of pred: `Dr. Schwab`
- `Mag. Fürnkranz ` — partial — gold is substring of pred: `Mag. Fürnkranz`
- `Senatspräsident des Obersten Gerichtshofs Dr` — similar text (different position): `Obersten Gerichtshofs`
- `Mag. Fürnkranz ` — similar text (different position): `Mag. Fürnkranz`
- `Mag. Herwig Berto ` — partial — gold is substring of pred: `Mag. Herwig Berto`

> overlaps gold: 8  |  likely missing annotation: 0

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

**Example 75** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`
- `Mag. Fürnkranz ` — partial — gold is substring of pred: `Mag. Fürnkranz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)

**Example 77** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

**False Positives:**

- `Mag. Herwig Bleuler ` — partial — gold is substring of pred: `Mag. Herwig Bleuler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Herwig Bleuler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel treten aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an deren Stelle (§ 45 Abs 2 StPO).

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Hon.-Prof. Dr. Schroll ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Schroll`
- `Hofrat des Obersten Gerichtshofs Dr` — similar text (different position): `Obersten Gerichtshofs`
- `Dr. Brenner ` — partial — gold is substring of pred: `Dr. Brenner`
- `Dr. Schwab ` — partial — gold is substring of pred: `Dr. Schwab`

> overlaps gold: 4  |  likely missing annotation: 0

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

**Example 80** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Oliver Paukstat`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_5`)


An Stelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger tritt Hofrat des Obersten Gerichtshofs Dr. Nordmeyer.

**False Positives:**

- `Hofrat des Obersten Gerichtshofs Dr` — similar text (different position): `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender des zuständigen 11.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)

**Example 83** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

**False Positives:**

- `Dr. Christine Schwab ` — partial — gold is substring of pred: `Dr. Christine Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Christine Schwab`(person)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_10`)


Als deren Angehöriger (§ 72 StGB) ist Senatspräsident des Obersten Gerichtshofs Dr. Schwab gemäß § 43 Abs 3 StPO von der Entscheidung über die vorliegende Beschwerde ausgeschlossen.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)

**Example 85** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_11`)


Hofrat des Obersten Gerichtshofs Dr. Nordmeyer tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs anstelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger (§ 45 Abs 2 StPO).

**False Positives:**

- `Hofrat des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)

**Example 86** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Hon.-Prof. Dr. Schroll ` — partial — gold is substring of pred: `Hon.-Prof. Dr. Schroll`
- `Dr. Oshidari ` — partial — gold is substring of pred: `Dr. Oshidari`
- `Dr. Schwab ` — partial — gold is substring of pred: `Dr. Schwab`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`

> overlaps gold: 4  |  likely missing annotation: 0

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

**Example 87** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)
- `Gerhard Boesl`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_5`)


An deren Stelle treten Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski.

**False Positives:**

- `Hofrat des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)

**Example 89** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender, Hofrätin des Obersten Gerichtshofs Mag. Michel ist Mitglied des zuständigen 11.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`
- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)

**Example 90** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Dr. Christine Schwab`(person)

**Example 91** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_15`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist damit von der Entscheidung über das vorliegende Rechtsmittel ausgeschlossen.

**False Positives:**

- `Senatspräsident des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)

**Example 92** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_16`)


2. Hofrätin des Obersten Gerichtshofs Mag. Michel war in diesem Verfahren zu 1 OStA 74/08s als Staatsanwältin tätig, sodass sie gemäß § 43 Abs 1 Z 1 StPO als Richterin vom gesamten Verfahren ausgeschlossen ist.

**False Positives:**

- `Mag. Michel ` — partial — gold is substring of pred: `Mag. Michel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)

**Example 93** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_17`)


3. An die Stelle der Ausgeschlossenen treten aufgrund der laufenden Vertretungsregelung Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski. (§ 45 Abs 2 StPO).

**False Positives:**

- `Hofrat des Obersten Gerichtshofs Dr` — partial — gold is substring of pred: `Obersten Gerichtshofs`
- `Dr. Michel-Kwapinski` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)

</details>

---

## `names_in_criminal_proceedings`

**F1:** 0.020 | **Precision:** 0.434 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `d72ced5c`  
**Description:**
Matches names of accused persons in criminal cases after 'Strafsache gegen' or 'des Verbrechens/Vergehens'. Captures the full name including suffixes like 'und andere'.

**Content:**
```
(?:Strafsache\s+gegen\s+|des\s+Verbrechens\s+des\s+|des\s+Verbrechens\s+der\s+|des\s+Vergehens\s+des\s+|des\s+Vergehens\s+der\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+und\s+andere)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.434 | 0.010 | 0.020 | 99 | 43 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 43 | 56 | 3664 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bernhard Buddäus` | `Bernhard Buddäus` |

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
- `Norbert Wehrhahn` (person)
- `Landesgerichts Salzburg` (organisation)
- `Mag. Höpler` (person)
- `Mag. Rienmüller` (person)

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Richard Lindt` | `Richard Lindt` |

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
- `Landesgerichts Salzburg` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Andreas Schiessl` | `Andreas Schiessl` |

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
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Kur` | `Daniel Kur` |

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
- `Landesgerichts Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Gerhard Bukowska` | `Gerhard Bukowska` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `OGH` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Ahmed Koehnen` | `Ahmed Koehnen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `OGH` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Thomas Michenfelder` | `Thomas Michenfelder` |

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
- `Landesgerichts Krems an der Donau` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Nenad Pschor` | `Nenad Pschor` |

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
- `Bezirksgerichts Leopoldstadt` (organisation)
- `Mag. Schneider, LL.M.` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Jennifer Janauscheck` | `Jennifer Janauscheck` |

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
- `Bezirksgerichts Kufstein` (organisation)
- `Dr. Eisenmenger` (person)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Thomas Leutz` | `Thomas Leutz` |

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
- `Landesgerichts Innsbruck` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Maximilian Gompertz` | `Maximilian Gompertz` |

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
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_3`)


Kopf Der Oberste Gerichtshof hat am 5. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Brenner als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Kaltenbrunner als Schriftführerin in der Strafsache gegen Johannes Barkhof wegen des Vergehens der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB und weiterer strafbarer Handlungen, AZ 51 Hv 32/13i des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen den Beschluss des genannten Gerichts vom 4. Mai 2014, GZ 51 Hv 32/13i-35, und weitere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, und der Verteidigerin Mag. Reisinger zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Johannes Barkhof` | `Johannes Barkhof` |

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
- `Landesgerichts Feldkirch` (organisation)
- `Dr. Eisenmenger` (person)
- `Mag. Reisinger` (person)

**Example 12** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Lendl, Mag. Michel und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Roman Ueberlein und einen weiteren Angeklagten wegen des Verbrechens des schweren gewerbsmäßig durch Einbruch begangenen Diebstahls nach §§ 127, 128 Abs 1 Z 5, 129 Abs 2 Z 1 (iVm Abs 1 Z 1), 130 Abs 3 (iVm Abs 1 erster Fall) und 15 StGB sowie einer weiteren strafbaren Handlung, AZ 37 Hv 122/18b des Landesgerichts Innsbruck, über den Antrag des Verurteilten Roman Urbath auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roman Ueberlein` | `Roman Ueberlein` |

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
- `Landesgerichts Innsbruck` (organisation)
- `Roman Urbath` (person)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Schoenwiese wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Zoltan Schoenwiese` | `Zoltan Schoenwiese` |

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
- `Landesgerichts Eisenstadt` (organisation)
- `Mag. Höpler` (person)
- `Mag. Urak` (person)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Manderscheidt wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag. Jenichl, des Verurteilten sowie seines Verteidigers Mag. Wolm zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Nikola Manderscheidt` | `Nikola Manderscheidt` |

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
- `Landesgerichts Salzburg` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `MMag. Jenichl` (person)
- `Mag. Wolm` (person)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Martin Pfaffenberg wegen des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 5. September 2019, GZ 43 Hv 73/19x-48, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Martin Pfaffenberg` | `Martin Pfaffenberg` |

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
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mehdi Rekemeyer` | `Mehdi Rekemeyer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schuber` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_3`)


Kopf Der Oberste Gerichtshof hat am 9. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtswärters Mag. Schönmann als Schriftführer in der Strafsache gegen Thomas Enulait wegen des Verbrechens des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 und 3 erster Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 1. September 2015, GZ 20 Hv 13/15y-53, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Enulait` | `Thomas Enulait` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schönmann` (person)
- `Landesgerichts St. Pölten` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Wolniak` | `Karl Wolniak` |

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
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Erik Jirouch` | `Erik Jirouch` |

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

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jamrozy, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

| Predicted | Gold |
|---|---|
| `Erik Jamrozy` | `Erik Jamrozy` |

**Missed by this rule (FN):**

- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Wolfgang Weide` | `Wolfgang Weide` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Korner` (person)
- `Bezirksgerichts Weiz` (organisation)
- `Dr. Ulrich` (person)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Aissa Bussmann` | `Aissa Bussmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Plesser` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Clößner wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mihai Clößner` | `Mihai Clößner` |

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
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_3`)


Kopf Der Oberste Gerichtshof hat am 6. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Michael Wakup wegen des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 21. März 2017, GZ 22 Hv 1/17p-32, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf bedingter Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michael Wakup` | `Michael Wakup` |

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
- `Landesgerichts Linz` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Robert Ultsch` | `Robert Ultsch` |

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
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Mag. Schneider` (person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Grießbaum wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ernst Grießbaum` | `Ernst Grießbaum` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Ratz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Einwagner` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Christoph Holthuijsen` | `Christoph Holthuijsen` |

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
- `Landesgerichts Klagenfurt` (organisation)
- `Oberlandesgerichts Graz` (organisation)
- `Mag. Höpler` (person)
- `Mag. Sternad` (person)
- `Mag. Höllwerth` (person)

**Example 28** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in der Strafsache gegen Daniel Bruchmüller wegen der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 4 U 118/18k des Bezirksgerichts St. Pölten und zu AZ 18 U 242/18p des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Daniel Bruchmüller` | `Daniel Bruchmüller` |

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
- `Bezirksgerichts St. Pölten` (organisation)
- `Bezirksgerichts Linz` (organisation)
- `OGH` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Ferenc Florin` | `Ferenc Florin` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Gabor Schwiecker` (person)
- `Bezirksgerichts Innsbruck` (organisation)
- `OGH` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahlwarth wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Tomislav Ahlwarth` | `Tomislav Ahlwarth` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Reichly` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__3`)


Kopf Der Oberste Gerichtshof hat am 24. Jänner 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin in der Strafsache gegen Bernd Karacabey wegen des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 und Abs 2 erster Fall StGB und einer anderen strafbaren Handlung über die von der Generalprokuratur gegen die Beschlüsse des Landesgerichts für Strafsachen Graz vom 20. Juni 2011, GZ 15 Hv 126/10k-44, und des Oberlandesgerichts Graz vom 11. August 2011, AZ 9 Bs 259/11y, sowie einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Knibbe, des Angeklagten und seines Verteidigers Dr. Vacarescu zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bernd Karacabey` | `Bernd Karacabey` |

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
- `Landesgerichts für Strafsachen Graz` (organisation)
- `Oberlandesgerichts Graz` (organisation)
- `Mag. Knibbe` (person)

**Example 32** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Mag. Hautz in Gegenwart der Richteramtsanwärterin Mag. Wöss als Schriftführerin in der Strafsache gegen Heinrich Käter wegen des Vergehens der Urkundenunterdrückung nach § 229 Abs 1 StGB, AZ 5 U 21/09y des Bezirksgerichts Ybbs, über die Beschwerde des Heinrich Kowacki und der Annemarie Kloiber gegen den Beschluss des Oberlandesgerichts Wien vom 8. April 2010, AZ 18 Bs 73/10g (ON 11), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Heinrich Käter` | `Heinrich Käter` |

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
- `Heinrich Kowacki` (person)
- `Annemarie Kloiber` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/15Ns104_16m`) (sent_id: `deanon_260716_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Herdemertens wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Markus Herdemertens` | `Markus Herdemertens` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Dr. Mann` (person)
- `Bezirksgerichts Bad Ischl` (organisation)
- `OGH` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_3`)


Kopf Der Oberste Gerichtshof hat am 16. November 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Beran als Schriftführer in der Strafsache gegen Peter Eckehardt wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 StGB und einer weiteren strafbaren Handlung, über die von der Generalprokuratur gegen den Beschluss des Bezirksgerichts Steyr vom 7. Mai 2013, GZ 5 U 44/12h-39, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Janda, sowie des Angeklagten zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Peter Eckehardt` | `Peter Eckehardt` |

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
- `Bezirksgerichts Steyr` (organisation)
- `Dr. Janda` (person)

**Example 35** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_5`)


Text Gründe: In der Strafsache gegen Peter Ellsäßer wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 5 U 44/12h des Bezirksgerichts Steyr, stellte der Einzelrichter des Bezirksgerichts das aufgrund einer von Martin Bartelme erhobenen Privatanklage geführte Verfahren mit – am 30. April 2013 in Rechtskraft erwachsenem (ON 38) – Beschluss vom 27. März 2013 (ON 32) gemäß § 71 Abs 6 StPO ein und verpflichtete den Privatankläger gemäß § 390 Abs 1 zweiter Satz StPO zum Ersatz der Kosten des Verfahrens.

| Predicted | Gold |
|---|---|
| `Peter Ellsäßer` | `Peter Ellsäßer` |

**Missed by this rule (FN):**

- `Bezirksgerichts Steyr` (organisation)
- `Martin Bartelme` (person)

**Example 36** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_3`)


Kopf Der Oberste Gerichtshof hat am 26. September 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Ertl, LL.M., als Schriftführer in der Strafsache gegen Arijan Peschak wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wels als Schöffengericht vom 14. Juni 2018, GZ 39 Hv 7/18a-76, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arijan Peschak` | `Arijan Peschak` |

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
- `Mag. Ertl, LL.M.` (person)
- `Landesgerichts Wels` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Backus wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Manfred Backus` | `Manfred Backus` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Mag. Müller` (person)
- `Landesgerichts Korneuburg` (organisation)
- `Mag. Mugler` (person)
- `Mag. Machac` (person)
- `Mag. Kessler` (person)

**Example 38** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart des Rechtspraktikanten Mag. Zechner als Schriftführer in der Strafsache gegen Manfred Mudder und einen weiteren Angeklagten wegen des Vergehens des Betrugs nach § 146 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 28. Jänner 2015, GZ 34 Hv 118/14b-50, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Manfred Mudder` | `Manfred Mudder` |

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
- `Mag. Zechner` (person)
- `Landesgerichts Linz` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Riemenschneider und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Johann Riemenschneider` | `Johann Riemenschneider` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)

**Example 40** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_3`)


Kopf Der Oberste Gerichtshof hat am 11. August 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie durch die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger in Gegenwart des Richteramtsanwärters Mag. Mechtler als Schriftführer in der Strafsache gegen Andreas Gudszenties wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 7 U 49/08s des Bezirksgerichts Innsbruck, über die von der Generalprokuratur erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes gegen die Unterlassung der Verständigung des Vollzugsgerichts von der Verlängerung der Probezeit nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Andreas Gudszenties` | `Andreas Gudszenties` |

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
- `Bezirksgerichts Innsbruck` (organisation)
- `Mag. Holzleithner` (person)

**Example 41** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_3`)


Kopf Der Oberste Gerichtshof hat am 29. Februar 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin in der Strafsache gegen Georg Haßelbring wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Georg Haßelbring` | `Georg Haßelbring` |

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
- `MMag. Linzner` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Dr. Sperker` (person)

**Example 42** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_3`)


Kopf Der Oberste Gerichtshof hat am 12. Mai 2014 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Kotanko als Schriftführerin in der Strafsache gegen Arno Enste wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 24. September 2013, GZ 50 Hv 37/13t-48, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arno Enste` | `Arno Enste` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Ratz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Mag. Kotanko` (person)
- `Landesgerichts Feldkirch` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Herwig Bernts`
- `Widerstands` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 1** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Mordes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fruhmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gebhard Sayin`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `Nenad Pschor`(person)
- `Bezirksgerichts Leopoldstadt`(organisation)
- `Mag. Schneider, LL.M.`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Leopoldstadt`(organisation)
- `Nenad Panagiotakopoulou`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

**False Positives:**

- `Raufhandels` — no gold match — likely missing annotation

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
- `Mag. Gotsmy`(person)
- `Jennifer Janauscheck`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Dr. Eisenmenger`(person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__7`)


Text Gründe: Die am 26. Jänner 1991 geborene Jennifer Johannwerner wurde mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, mehrerer Vergehen der Körperverletzung nach § 83 Abs 1 StGB und des Vergehens der Sachbeschädigung nach § 125 StGB schuldig erkannt und hiefür unter Anwendung des § 5 Z 4 JGG zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von zwei Monaten verurteilt (Blg ./2 zum Bezugsakt AZ 3 U 166/07x des Bezirksgerichts Kufstein).

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jennifer Johannwerner`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Bezirksgerichts Kufstein`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Holzweber`
- `Fälschung` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Fälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Viktor Marschmeyer und andere` — partial — gold is substring of pred: `Viktor Marschmeyer`
- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktor Meisterernst`(person)
- `Dr. Stefan Tydeck`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Müller`(person)
- `Maximilian Gompertz`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Maximilian Gudzentat der Verbrechen des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (1./), der Vergewaltigung nach § 201 Abs 1 StGB und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (2./) sowie des Vergehens der Nötigung nach § 105 Abs 1 StGB (3./) schuldig erkannt.

**False Positives:**

- `Nötigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximilian Gudzentat`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

**False Positives:**

- `Natascha` — partial — pred is substring of gold: `Natascha von Bohr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Mag. Anscheringer`(person)
- `Natascha von Bohr`(person)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Bezirksgerichts Linz`(organisation)
- `Bezirksgericht Linz`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

**False Positives:**

- `Alois Petraschek und andere` — partial — gold is substring of pred: `Alois Petraschek`
- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_4`)


Text Gründe: Mit Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v, wurde der von Sebastian Niemz am 24. Mai 2019 gestellte Antrag auf Fortführung des aufgrund seiner Anzeige von der Staatsanwaltschaft Graz zu AZ 22 St 47/14v gegen Alois Paasch und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen geführten und gegen sämtliche Beschuldigte gemäß § 190 Z 2 StPO eingestellten Ermittlungsverfahrens als unzulässig zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Sebastian Niemz`(person)
- `Alois Paasch`(person)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Salzburg`(organisation)
- `Nikola Miscenko`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Raubes` — no gold match — likely missing annotation

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

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Mag` — similar text (different position): `Mag. Michel`
- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Bachl`(person)
- `Mag. Johanna Fletcher`(person)
- `Herbert Onesseit`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

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

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Karl Wodarcyk des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karl Wodarcyk`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Erik Jirouch`(person)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

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
- `Mag. Plesser`(person)
- `Aissa Bussmann`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_7`)


Text Gründe: Mit dem angefochtenen Urteil wurde Aissa Boness des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aissa Boness`(person)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_8`)


Abs 1 fünfter Fall, Abs 2 Z 3 SMG (A) sowie des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 erster und zweiter Fall SMG (B) schuldig erkannt.

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Michael Wessollek des Vergehens der Sachbeschädigung nach § 125 StGB (1/a), des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB (1/b) und des Vergehens der Körperverletzung nach § 83 Abs 1 StGB (2) schuldig erkannt.

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation
- `Körperverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Michael Wessollek`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Lengjel und andere` — partial — gold is substring of pred: `Michael Lengjel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Michael Lengjel`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Anna Wynand`(person)
- `Brian Waltemate`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Urkundenfälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 29** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Diebstahls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Ferenc Florin`(person)
- `Gabor Schwiecker`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `OGH`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Riffart und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kunkelmann gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Misha Riffart und andere` — partial — gold is substring of pred: `Misha Riffart`

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

**Example 31** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahlwarth wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Reichly`(person)
- `Tomislav Ahlwarth`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Mag. Hautz in Gegenwart der Richteramtsanwärterin Mag. Wöss als Schriftführerin in der Strafsache gegen Heinrich Käter wegen des Vergehens der Urkundenunterdrückung nach § 229 Abs 1 StGB, AZ 5 U 21/09y des Bezirksgerichts Ybbs, über die Beschwerde des Heinrich Kowacki und der Annemarie Kloiber gegen den Beschluss des Oberlandesgerichts Wien vom 8. April 2010, AZ 18 Bs 73/10g (ON 11), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Urkundenunterdrückung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Hautz`(person)
- `Mag. Wöss`(person)
- `Heinrich Käter`(person)
- `Heinrich Kowacki`(person)
- `Annemarie Kloiber`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Kira Nesselrodt und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Erwin Nungässer gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Shafiqullah Kira Nesselrodt und andere` — partial — gold is substring of pred: `Kira Nesselrodt`

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

**Example 34** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_3`)


Kopf Der Oberste Gerichtshof hat am 26. September 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Ertl, LL.M., als Schriftführer in der Strafsache gegen Arijan Peschak wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wels als Schöffengericht vom 14. Juni 2018, GZ 39 Hv 7/18a-76, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `Mag. Ertl, LL.M.`(person)
- `Arijan Peschak`(person)
- `Landesgerichts Wels`(organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Arijan Preisentans des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG, § 15 StGB als Beteiligter nach § 12 dritter Fall StGB (1.) und des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall SMG (2.) schuldig erkannt.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation
- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Arijan Preisentans`(person)

**Example 36** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_10`)


Da der Tatbestand des Verbrechens des Suchtgifthandels nach § 28a SMG nicht auf „generalpräventive Gesichtspunkte“ abstellt, diese somit die Strafdrohung nicht bestimmen, liegt kein Verstoß gegen das Doppelverwertungsverbot vor.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Backus wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Mag. Müller`(person)
- `Manfred Backus`(person)
- `Landesgerichts Korneuburg`(organisation)
- `Mag. Mugler`(person)
- `Mag. Machac`(person)
- `Mag. Kessler`(person)

**Example 38** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_7`)


RIS-Justiz RS0119509) des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter und dritter Fall SMG (A./1./), (richtig:) des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2 und Abs 4 SMG (A./2./), des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter Fall, Abs 2 SMG (A./3./), (richtig:) der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 (richtig:) zweiter und dritter Fall, Abs 2 SMG (B./I./) und des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 2, Abs 2 SMG (B./II./) schuldig erkannt und unter Anwendung des § 28 Abs 1 StGB nach § 28 Abs 4 SMG zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von sechs Monaten verurteilt. Nach dem Inhalt des Schuldspruchs hat Manfred Börekci in Aussichtsstraße 10, 4201 Aschlberg, Österreich A./ im Zeitraum von 2006 bis zum 8. Oktober 2009 1./ vorschriftswidrig Cannabis mit einem Reinheitsgehalt von zumindest 123 Gramm Delta 9-THC erzeugt und besessen, indem er eine unbekannte Menge an Cannabispflanzen anbaute, erntete, die Blüten trocknete und jedenfalls zum Teil Cannabisharz daraus gewann;

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manfred Börekci`(person)
- `Aussichtsstraße 10, 4201 Aschlberg, Österreich`(address)

**Example 39** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart des Rechtspraktikanten Mag. Zechner als Schriftführer in der Strafsache gegen Manfred Mudder und einen weiteren Angeklagten wegen des Vergehens des Betrugs nach § 146 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 28. Jänner 2015, GZ 34 Hv 118/14b-50, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 40** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_6`)


Text Gründe: Mit dem angefochtenen Urteil, das auch in Rechtskraft erwachsene Freisprüche dieses und eines weiteren Angeklagten enthält, wurde Manfred Mikuteit des Vergehens des Betrugs nach § 146 StGB schuldig erkannt.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manfred Mikuteit`(person)

**Example 41** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Riemenschneider und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Johann Riemenschneider`(person)

**Example 42** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_8`)


Text Gründe: Die Staatsanwaltschaft Wels führt zu AZ 17 St 77/19g ein Ermittlungsverfahren gegen Johann Reithinger wegen des Verdachts des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG und weiterer strafbarer Handlungen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johann Reithinger`(person)

**Example 43** (doc_id: `deanon_260716_TRAIN/15Os71_21m`) (sent_id: `deanon_260716_TRAIN/15Os71_21m_3`)


Kopf Der Oberste Gerichtshof hat am 2. August 2021 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in der Strafsache gegen unbekannte Täter zum Nachteil des DI Robert Leichtlein wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 49 Bl 31/20w des Landesgerichts Salzburg, über die Beschwerde des DI Laurin Beekman gegen den Beschluss des Oberlandesgerichts Linz vom 23. Oktober 2020, GZ 8 Bs 90/20x-1, nach Einsichtnahme in die Akten durch die Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `DI Robert Leichtlein`(person)
- `Landesgerichts Salzburg`(organisation)
- `DI Laurin Beekman`(person)
- `Oberlandesgerichts Linz`(organisation)
- `OGH`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_3`)


Kopf Der Oberste Gerichtshof hat am 11. August 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie durch die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger in Gegenwart des Richteramtsanwärters Mag. Mechtler als Schriftführer in der Strafsache gegen Andreas Gudszenties wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 7 U 49/08s des Bezirksgerichts Innsbruck, über die von der Generalprokuratur erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes gegen die Unterlassung der Verständigung des Vollzugsgerichts von der Verlängerung der Probezeit nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, zu Recht erkannt:  Spruch

**False Positives:**

- `Körperverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schmucker`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Dr. T. Solé`(person)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Mechtler`(person)
- `Andreas Gudszenties`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `Mag. Holzleithner`(person)

**Example 45** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_3`)


Kopf Der Oberste Gerichtshof hat am 29. Februar 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin in der Strafsache gegen Georg Haßelbring wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Dr. Michel-Kwapinski`(person)
- `MMag. Linzner`(person)
- `Georg Haßelbring`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Dr. Sperker`(person)

**Example 46** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_7`)


Text Gründe: Mit dem unangefochten in Rechtskraft erwachsenen Urteil des Landesgerichts Feldkirch vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, wurde Georg Höfs - abweichend von dem in Richtung §§ 146, 147 Abs 2 StGB erhobenen Strafantrag - des Vergehens des Betrugs nach § 146 StGB schuldig erkannt und zu einer teilweise bedingt nachgesehenen Geldstrafe verurteilt. Nach dem Schuldspruch hat er in Chikago 2. Gasse 8, 4613 Hupfau, Österreich mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Bedienstete der (richtig:) Nobars und Huenecken E‑Commerce GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro nicht übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Georg Höfs`(person)
- `Chikago 2. Gasse 8, 4613 Hupfau, Österreich`(address)
- `Nobars und Huenecken E‑Commerce GmbH`(organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_3`)


Kopf Der Oberste Gerichtshof hat am 12. Mai 2014 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Kotanko als Schriftführerin in der Strafsache gegen Arno Enste wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 24. September 2013, GZ 50 Hv 37/13t-48, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Ratz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Kotanko`(person)
- `Arno Enste`(person)
- `Landesgerichts Feldkirch`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Arno Ellerbrook - soweit im Verfahren über die Nichtigkeitsbeschwerde von Bedeutung - des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Arno Ellerbrook`(person)

</details>

---

## `bare_names_in_lists`

**F1:** 0.010 | **Precision:** 0.010 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `f9a5bf09`  
**Description:**
Matches bare names in lists or after 'und', excluding sentence starters and common false positives.

**Content:**
```
(?:^|[,;]\s*)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?)(?=\s*(?:,|\s+und\s+|\s+zu\s+|\s+des\s+|\s+der\s+|\s+die\s+|\s+den\s+|\s+als\s+|\s+von\s+|\s+mit\s+|\s+gegen\s+|\s+nach\s+|\s+vor\s+|\s+über\s+|\s+unter\s+|\s+auf\s+|\s+an\s+|\s+bei\s+|\s+für\s+|\s+ohne\s+|\s+neben\s+|\s+zwischen\s+|\s+sowie\s+|\s+oder\s+|\s+aber\s+|\s+doch\s+|\s+sondern\s+|\s+weder\s+|\s+noch\s+|\s+entweder\s+|\s+\)|\s+\]|\s+\.|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.010 | 0.010 | 0.010 | 4018 | 41 | 3977 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 41 | 3977 | 4124 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Selma Einoeder` | `Selma Einoeder` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hofräte Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

**False Positives:**

- `Die Weiterführung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz-Ost`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_30`)


Zweckmäßigkeitserwägungen, die eindeutig im Sinn aller Verfahrensbeteiligten für die vom Kläger beantragte Delegierung sprechen, liegen somit nicht vor (RS0046324).

**False Positives:**

- `Zweckmäßigkeitserwägungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_35`)


Ihr Schriftsatz mit der Stellungnahme zum Delegationsantrag enthält auch Vorbringen zur Sache und Beweisanträge und ist damit im Hauptverfahren verwertbar (RS0036025 [T5, T8, T10]).

**False Positives:**

- `Ihr Schriftsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Schweiz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

**False Positives:**

- `Ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_4`)


Die Kosten der von der beklagten Partei im Delegierungsverfahren eingebrachten Äußerung (Klagebeantwortung) sind weitere Verfahrenskosten.

**False Positives:**

- `Die Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_11`)


Das Sicherstellungsbegehren und der Vertragsrücktritt seien rechtsmissbräuchlich erfolgt.

**False Positives:**

- `Das Sicherstellungsbegehren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

**False Positives:**

- `Die Verhandlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

**False Positives:**

- `Sowohl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Linz`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

**False Positives:**

- `Die Delegierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

**False Positives:**

- `Mehrere von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Linz`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

**False Positives:**

- `Dass` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_38`)


Ist die Delegierung strittig, so ist das darüber geführte Verfahren ein Zwischenstreit, über dessen Kosten unabhängig vom Ausgang der Hauptsache zu entscheiden ist (RS0036025).

**False Positives:**

- `Ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_39`)


Nicht zu honorieren sind dabei allerdings solche Schriftsätze, die auch Vorbringen zur Hauptsache enthalten (RS0036025 [T5]).

**False Positives:**

- `Nicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Russische Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_7`)


Rechtliche Beurteilung Die Gerichtskompetenz für die Vollstreckbarerklärung eines ausländischen Exekutionstitels richtet sich nach § 82 EO.

**False Positives:**

- `Rechtliche Beurteilung Die Gerichtskompetenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_12`)


Ausschlaggebendes Kriterium für die Übertragung der Zuständigkeit zur Führung einer Pflegschaftssache ist stets das Wohl des Kindes (RIS-Justiz RS0047074; RS0046908).

**False Positives:**

- `Ausschlaggebendes Kriterium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_16`)


Wird der Übertragungsbeschluss hingegen rechtskräftig bestätigt, so bedarf es der Genehmigung des übergeordneten Gerichts (3 Nc 1/23m).

**False Positives:**

- `Wird` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Hongkong` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_5`)


In eventu begehrte die klagende Partei die Feststellung, dass zwischen den Parteien kein Vertrag über die Weitergabe und Nutzung von Rechten, Lizenzen, Daten, Know-How, technischen Informationen und Unterlagen betreffend mikroverkapseltem Clomazone sowie über eine Zusammenarbeit hinsichtlich der Entwicklung und Produktion von mikroverkapseltem Clomazone mit belastenden Bestimmungen, wie insbesondere der Untersagung der Weitergabe der bekannten Informationen an Dritte, wirksam abgeschlossen worden sei oder bestehe, sodass der Beklagten keine wie auch immer gearteten Rechte gegenüber der Klägerin zustünden.

**False Positives:**

- `Lizenzen` — no gold match — likely missing annotation
- `Daten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_13`)


Das von § 28 Abs 1 Z 2 JN geforderte Naheverhältnis der Klägerin zum Inland ergebe sich aus dem inländischen Unternehmenssitz der Klägerin.

**False Positives:**

- `Das` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_14`)


Die Unzumutbarkeit der Rechtsverfolgung im Ausland ergebe sich daraus, dass eine ausländische Entscheidung in Österreich nicht anerkannt und vollstreckt werden würde, eine dringende Entscheidung nicht erreicht werden könne und eine Prozessführung im Ausland äußerst kostspielig wäre.

**False Positives:**

- `Die Unzumutbarkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_22`)


Das Vorliegen der zweiten Voraussetzung (nämlich die Unmöglichkeit oder Unzumutbarkeit der Rechtsverfolgung im Ausland) wird in der Rechtsprechung insbesondere dann bejaht, wenn die ausländische Entscheidung in Österreich nicht anerkannt oder vollstreckt wird (unter der weiteren Voraussetzung, dass eine Exekutionsführung im Inland überhaupt geplant ist - RIS-Justiz RS0046148 [T10]), eine dringende Entscheidung im Ausland nicht rechtzeitig erreicht werden kann, eine Prozessführung im Ausland wenigstens eine der Parteien politischer Verfolgung aussetzen würde oder wenn die Prozessführung im Ausland äußerst kostspielig wäre (MayrinRechberger, ZPO4§ 28 JN Rz 4 mwN; RIS-Justiz RS0046148).

**False Positives:**

- `Das Vorliegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_25`)


Dabei ist im vorliegenden Fall im Hinblick auf das von der Klägerin ausschließlich erhobene Feststellungsbegehren zu berücksichtigen, dass ein Feststellungsurteil eines ausländischen Gerichts, das eine vermögensrechtliche Angelegenheit zum Gegenstand hat, auf Antrag einer der Parteien gemäß den §§ 79, 85 EO im Inland zwar anerkannt werden kann, Feststellungsurteile aber nur deklarative Wirkung haben, also keinen Leistungsanspruch schaffen, und daher - abgesehen von einem in das Urteil aufgenommenen Leistungsausspruch über den Prozesskostenersatz - nicht vollstreckbar sind (vglFaschinginFasching/Konecny2III § 228 ZPO Rz 145).

**False Positives:**

- `Feststellungsurteile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_26`)


Den Angaben der Klägerin ist nicht zu entnehmen, dass die Beklagte über irgendein Vermögen im Inland verfügt.

**False Positives:**

- `Den Angaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_33`)


Konkrete Umstände des Einzelfalls, die auf eine besondere Kostspieligkeit der Rechtsverfolgung in Hongkong hindeuten würden, hat die Klägerin nicht dargetan.

**False Positives:**

- `Konkrete Umstände` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Russische Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_5`)


Die Mutter und die Kinder sind Staatsangehörige der Russischen Föderation und als Asylwerber im Inland aufhältig.

**False Positives:**

- `Die Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_4`)


Text Begründung: Die Klägerin macht gegen die beklagte Partei, eine ägyptische Fluglinie, Ansprüche nach der Verordnung (EG) 261/2004 des Europäischen Parlaments und des Rates vom 11. Februar 2004 über eine gemeinsame Regelung für Ausgleichs- und Unterstützungsleistungen für Fluggäste im Fall der Nichtbeförderung und bei Annullierung oder großer Verspätung von Flügen (EU-Fluggastrechte-VO) geltend.

**False Positives:**

- `Ansprüche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_5`)


Das von der Klägerin mit ihrer Klage angerufene Bezirksgericht Schwechat hat die internationale und örtliche Zuständigkeit rechtskräftig verneint (RIS-Justiz RS0046450).

**False Positives:**

- `Das von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Schwechat`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_8`)


Auf die Begründung insbesondere dieser Entscheidungen kann auch für den vorliegenden Fall sinngemäß verwiesen werden.

**False Positives:**

- `Auf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_9`)


Für die Auswahl des zu ordinierenden Gerichts (in örtlicher Hinsicht) enthält § 28 JN keine ausdrücklichen Vorgaben.

**False Positives:**

- `Für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Vereinigtes Königreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_6`)


Sein Flug von Wien nach Bristol sei annulliert worden, weshalb er von der Beklagten die Rückerstattung der Flugscheinkosten nach Art 8 Abs 1 lit a EU-FluggastVO fordere.

**False Positives:**

- `Sein Flug von Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_14`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des vom Kläger angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568).

**False Positives:**

- `An` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgerichts Schwechat`(organisation)
- `Oberste Gerichtshof`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_16`)


Für den Fall, dass für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts nicht gegeben oder nicht zu ermitteln sind, bestimmt § 28 Abs 1 Z 2 JN, dass der Oberste Gerichtshof aus den sachlich zuständigen Gerichten eines zu bestimmen hat, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

**False Positives:**

- `Für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_20`)


Dem Vorbringen des Klägers lässt sich gerade noch ausreichend deutlich entnehmen, dass er die Vollstreckung in Österreich anstrebt.

**False Positives:**

- `Dem Vorbringen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_27`)


Auch eine Vollstreckung britischer Entscheidungen in Österreich nach dem EuGVÜ oder dem LGVÜ kommt nicht in Betracht (Exenberger/Karl, Anerkennung und Vollstreckung zivilgerichtlicher Entscheidungen Post-Brexit, ecolex 2021/227, 320; vgl auchCap, BREXIT – Die justizielle Zusammenarbeit mit dem Vereinigten Königreich in Zivilrechtssachen nach 31.

**False Positives:**

- `Anerkennung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_29`)


Es bleibt damit – jedenfalls im hier zu beurteilenden Fall (vgl zum Anwendungsbereich des Haager Übereinkommens über Gerichtsstandsvereinbarungen in Zivil- und Handelssachen:Tretthahn-Wolski/Förstel-Cherng, Nein zu Lugano – Zu den Auswirkungen des harten Brexits auf Cross-Border-Streitigkeiten, ÖJZ 2021/92, 708) – nur ein (allfälliger:Cap, RZ 2021, 124 [128]) Rückgriff auf den bilateralen Vollstreckungsvertrag.

**False Positives:**

- `Nein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_31`)


Trotz der in Art II Abs 2 vorgesehenen grundsätzlichen Möglichkeit zur Vollstreckung auch von Entscheidungen „unterer“ Gerichte („Dieser Vertrag schließt nicht aus …“) kommt eine Vollstreckung der Entscheidung eines britischen „unteren“ Gerichts in Österreich mangels qualifizierter Gegenseitigkeit (§ 406 EO) nicht in Betracht (1 Nd 502/85 SZ 58/109 = JBl 1986, 191 [Pfersmann];

**False Positives:**

- `Trotz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_37`)


Bei der Auswahl des zu bestimmenden Gerichts ist auf die Kriterien der Sach- und Parteinähe sowie der Zweckmäßigkeit Bedacht zu nehmen (RS0106680 [T13]).

**False Positives:**

- `Bei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

**False Positives:**

- `Anstelle` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgerichts Kitzbühel`(organisation)
- `Bezirksgericht Mödling`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_10`)


Im Hinblick auf die angeführten Umstände erscheint die Übertragung der Zuständigkeit an das Bezirksgericht Mödling im Sinne des § 31 Abs 1 JN zweckmäßig und geeignet, eine Verkürzung und Verbilligung des Verfahrens zu bewirken.

**False Positives:**

- `Im Hinblick` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_6`)


Die Leistungen der beklagten Partei seien in Bezug auf Trittschallschutz-Decke und Bodenaufbau Nassräume und Technikräume mangelhaft, wodurch der klagenden Partei (in Form von Sanierungskosten und Mietzinsentgang) ein Schaden in Höhe des Klagsbetrags entstanden sei.

**False Positives:**

- `Die Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_9`)


In der Streitverhandlung vom 27. Jänner 2015 beantragte die klagende Partei die Delegierung an das Handelsgericht Wien.

**False Positives:**

- `In` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_13`)


Bei Abschluss der Gerichtsstandsvereinbarung sei nicht vorhersehbar gewesen, dass zahlreiche Personen aus dem Nahebereich von Wien einzuvernehmen seien.

**False Positives:**

- `Bei Abschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_15`)


Ihr Geschäftsführer und ein von ihr beantragter Zeuge seien in Linz wohnhaft;

**False Positives:**

- `Ihr Geschäftsführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_36`)


Den Gegenstand des vorliegenden Rechtsstreits bilden zwar keine Hauptleistungsansprüche aus dem Werkvertrag zwischen den Parteien, in dem die Gerichtsstandsvereinbarung getroffen wurde.

**False Positives:**

- `Den Gegenstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_47`)


Das Objekt, auf das sich der Rechtsstreit bezieht, ist in Wien gelegen, sodass auch ein Ortsaugenschein sowie die Befundaufnahme durch Sachverständige in Wien durchzuführen sind.

**False Positives:**

- `Das Objekt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_48`)


Ob der Komplexität der Streitthemen und der Vielzahl der zu vernehmenden Personen ist die Durchführung eines Großteils des Beweisverfahrens im Wege einer Videokonferenz aufwändig und nicht unbedingt zielführend.

**False Positives:**

- `Ob` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_6`)


Die Kosten des Revisionsverfahrens sind weitere Verfahrenskosten.

**False Positives:**

- `Die Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_10`)


Das Honorar der Klägerin bemaß sich in Prozentsätzen der Nettoherstellungskosten.

**False Positives:**

- `Das Honorar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_13`)


Mit der am 25. 10.

**False Positives:**

- `Mit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_18`)


Die von der Beklagten behaupteten Mängel lägen nicht vor.

**False Positives:**

- `Die von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_21`)


Die der Beklagten am 31. 8. 2001 übermittelte Schlussrechnung sei konkretisiert und detailliert.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_22`)


Unabhängig von allfälligen Mängeln habe die Beklagte nach dem Vertrag jedenfalls zwei Teilzahlungen von je 1 Mio S leisten müssen, weil sie nur acht der vereinbarten Raten bezahlt habe.

**False Positives:**

- `Unabhängig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_41`)


Die Verträge mit den Professionisten habe vielmehr die Beklagte abgeschlossen.

**False Positives:**

- `Die Verträge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_52`)


Rechtliche Beurteilung Die gegen das Teilurteil erhobene Revision der Beklagten ist - wie ausgeführt werden wird - zulässig;

**False Positives:**

- `Rechtliche Beurteilung Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_69`)


Teilzahlungen auf den Werklohn vor der Fertigstellung des Werks, die - wie im Anlassfall - nicht bestimmte Teilleistungen abgelten sollen, sind als Vorschüsse zu qualifizieren (8 Ob 157/99t = SZ 72/112).

**False Positives:**

- `Teilzahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_75`)


Dass der Anspruch der Klägerin auf Zahlung des restlichen Vorschusses fällig ist, bestreitet die Revisionswerberin daher zu Recht nicht.

**False Positives:**

- `Dass` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_80`)


Da die Beklagte der Klägerin nach den Feststellungen der Vorinstanzen mehr als die Hälfte des ungeminderten Honorars gezahlt hat, wäre das Klagebegehren abzuweisen, wenn der geminderte Werklohn den schon bezahlten Betrag nicht übersteigt.

**False Positives:**

- `Da` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_83`)


Eine Vereinbarung, wonach die Beklagte Zahlungen wegen Gewährleistungsansprüchen nicht zurückhalten dürfe (s RIS-Justiz RS0016592), wurde nämlich weder behauptet noch festgestellt. Dass die Beklagte Vorleistungspflichtige der Vorschüsse ist, führt nicht dazu, dass sie insoweit das Preisminderungsrecht nicht mit Einrede, sondern mit Klage geltend machen müsste, macht doch das Gesetz die Geltendmachung von Gewährleistungsrechten nicht von der Erfüllung der eigenen Verbindlichkeit abhängig.

**False Positives:**

- `Eine Vereinbarung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_12`)


Für die weiteren vom Beklagten vorgenommenen Neupflanzungen bestehe keine rechtliche Grundlage.

**False Positives:**

- `Für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_13`)


Durch die Grundbuchseintragungen im Jahr 1958 seien die betroffenen Grundstücke „lastenfrei abgeschrieben“ worden;

**False Positives:**

- `Durch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_22`)


Aus den Feststellungen sind folgende – für das Revisionsverfahren noch wesentliche – Feststellungen hervorzuheben: Im A2-Blatt der Liegenschaft der Klägerin ist mit „Stand 1911“ eingetragen: „Die auf Gst ... stehenden Obstbäume bilden selbständige Vermögensobjekte“.

**False Positives:**

- `Aus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_26`)


In den 1930-iger und 1940-iger-Jahren bewirtschafteten die Eltern des Beklagten zwanzig bis dreißig Obstbäume auf der Liegenschaft der Klägerin.

**False Positives:**

- `In` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_27`)


Infolge von Geländeveränderungen (Einebnungen und Aufschüttungen) gingen einige Bäume zugrunde oder wurden entfernt.

**False Positives:**

- `Infolge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_31`)


In der Vollversammlung vom 10. 3. 1977, an der auch der Beklagte – der zugleich Mitglied der Klägerin ist – teilnahm, stellte er ein entsprechendes „Grundansuchen“.

**False Positives:**

- `In` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_47`)


Die Nichtübertragung der Grundbuchseintragung auf die betroffenen Grundstücke schade nicht.

**False Positives:**

- `Die Nichtübertragung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_48`)


Das Eigentumsrecht des Beklagten an den Obstbäumen sei daher durch die Grundstücksteilungen und Abschreibungen nicht verloren gegangen.

**False Positives:**

- `Das Eigentumsrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_52`)


Ob und inwieweit die unterbliebene Mitübertragung der Anmerkung berichtigungsfähig sei, sei nicht zu erörtern.

**False Positives:**

- `Ob` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_53`)


Die Beweisrüge zu den allenfalls in der Vollversammlung 1977 getroffenen Vereinbarungen müsse aus rechtlichen Gründen nicht erledigt werden, weil seither mehr als 30 Jahre vergangen seien und ein Anspruch aus der von der Klägerin behaupteten Vereinbarung jedenfalls verjährt sei.

**False Positives:**

- `Die Beweisrüge zu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_54`)


Soweit die Streitteile vereinbart haben sollten, dass der Verzicht auf die Obstbäume schlagend werde, wenn die klagende Partei das Grundstück benötige, stehe auch dieser Passus einer Verjährung nicht entgegen.

**False Positives:**

- `Soweit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_56`)


Infolge Fortbestehens des Eigentums an den Obstbäumen habe der Beklagte auch Nachpflanzungen vornehmen dürfen, nachdem ein Teil der 1958 bestehenden Obstbäume bei Geländeveränderungen eingegangen bzw entfernt worden war.

**False Positives:**

- `Infolge Fortbestehens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_58`)


Rechtliche Beurteilung Die Revision der Klägerin ist aus dem vom Berufungsgericht genannten Grund zulässig;

**False Positives:**

- `Rechtliche Beurteilung Die Revision` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_64`)


Für die Zukunft sollten solche Sonderrechte jedoch nicht mehr begründet werden können (Justizausschussbericht 1516 der Beilagen zu den stenographischen Protokollen des Abgeordnetenhauses XI. Session, 2 f, 5 ff;Pitreich, Zur Geschichte des Immobiliarrechtes seit der Kodifikation in: FS Jahrhundertfeier ABGB [1911] II 493).

**False Positives:**

- `Für` — no gold match — likely missing annotation
- `Pitreich` — no gold match — likely missing annotation
- `Zur Geschichte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 77** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_71`)


Die Verpflichtung des Grundeigenthümers, die Benützung einer Grundfläche im Umkreise solcher Bäume zu deren Pflege und Genuß zu gestatten, bildet keinen Gegenstand der Eintragung in das Grundbuch.

**False Positives:**

- `Die Verpflichtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_74`)


Das Löschungsgesuch, das eine genaue Bezeichnung der Liegenschaft zu enthalten hat, ist im Grundbuche durch eine Anmerkung ersichtlich zu machen.

**False Positives:**

- `Das Löschungsgesuch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_81`)


Die Wirksamkeit des Artikels IX beginnt mit dem Tage der Kundmachung des Gesetzes.

**False Positives:**

- `Die Wirksamkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_83`)


Von der individuellen Eintragung der Bäume (etwa als eigene Grundbuchskörper) wurde jedoch bewusst Abstand genommen.

**False Positives:**

- `Von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_85`)


Zur Vermeidung von Zweifeln über die Erwerbungsart „hinsichtlich der vom Grundbuche ausgeschlossenen Bäume“ wurde eine Bestimmung über die künftige Erwerbungsart getroffen (Artikel IV Abs. 2).

**False Positives:**

- `Zur Vermeidung von Zweifeln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_91`)


Rassi, Grundbuchsrecht² Rz 216, erwähnt die betreffenden Bäume in Tirol (neben dem Stockwerkseigentum) unter dem Aspekt des real geteilten Eigentums.

**False Positives:**

- `Rassi` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_93`)


Anmerkungen nach § 20 lit b GBG sind zur Begründung bestimmter, nach den Vorschriften des Grundbuchsgesetzes oder eines anderen Gesetzes damit verbundener Rechtswirkungen zulässig (RIS-Justiz RS0060679).

**False Positives:**

- `Anmerkungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_95`)


Sie unterscheiden sich von der Einverleibung oder Vormerkung vor allem dadurch, dass sie nur dazu dienen, Tatsachen, die gewisse rechtliche Folgen nach sich ziehen, festzustellen;

**False Positives:**

- `Tatsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_101`)


Der Wegfall der Anmerkung (aus welchem Grund auch immer) führt demnach nicht zum Erlöschen des Eigentums, weil eine Anmerkung nicht zur Veränderung (Aufhebung) dinglicher Rechte führen kann.

**False Positives:**

- `Der Wegfall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Amt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofräte Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Bartholomäus Junghahn`(person)
- `HR Sophie Elefteriadis`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_16`)


Ein auf Gewährung von Unterhaltsvorschüssen auch für den Monat Februar 2010 gerichtetes Mehrbegehren der beiden Minderjährigen wies es ab.

**False Positives:**

- `Ein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_23`)


Gegen die Entscheidung des Rekursgerichts richtet sich der Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, mit dem Antrag, den angefochtenen Beschluss im Sinne einer Wiederherstellung der Beschlüsse des Erstgerichts abzuändern.

**False Positives:**

- `Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Marion Woltz im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Mit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Marion Woltz`(person)

**Example 90** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_12`)


In der Verhandlungstagsatzung am 24. 11.

**False Positives:**

- `In` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_16`)


In der darauf anberaumten Verhandlungstagsatzung am 1. 10.

**False Positives:**

- `In` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_23`)


Mangelndes Interesse der Klägerin an der Fortsetzung des Verfahrens lasse sich aus ihrem Verhalten nicht ableiten.

**False Positives:**

- `Mangelndes Interesse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_26`)


Da die Klägerin über die dreimonatige Dauer des in der Tagsatzung vom 24. 11.

**False Positives:**

- `Da` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_30`)


Auch die Auslegungsregel des § 915 ABGB komme nicht in Betracht, liege doch keine undeutliche Erklärung vor.

**False Positives:**

- `Auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_31`)


Selbst die restriktive Auslegung von Verzichtserklärungen helfe nicht weiter, dürfe doch ein Rechtsausübender auf den Bestand des § 903 dritter Satz ABGB vertrauen.

**False Positives:**

- `Selbst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_33`)


Rechtliche Beurteilung Die von der Klägerin beantwortete Revision der Beklagten ist zwar zulässig;

**False Positives:**

- `Rechtliche Beurteilung Die von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_36`)


Durch die Koppelung des Verjährungsverzichts an eine rechtzeitige Fortsetzung, spätestens bis zum 30. 6. 2013, sei im Zweifel „die Fortsetzung im Verhältnis zwischen den Streitparteien daher vor dem 30.

**False Positives:**

- `Durch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_45`)


Die Unterlassung der gehörigen Fortsetzung der Klage ist kein eigener selbständiger Verjährungsgrund.

**False Positives:**

- `Die Unterlassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `bare_names_in_criminal_context`

**F1:** 0.005 | **Precision:** 0.175 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `d064d891`  
**Description:**
Matches bare names in criminal contexts like 'des Angeklagten [Name]' or 'des [Name] betreffend' to capture names that were previously missed.

**Content:**
```
(?:des\s+Angeklagten\s+|des\s+Verbrechens\s+des\s+|des\s+Verbrechens\s+der\s+|des\s+Vergehens\s+des\s+|des\s+Vergehens\s+der\s+|des\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+\s+betreffend\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.175 | 0.002 | 0.005 | 57 | 10 | 47 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 47 | 3682 |

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

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_11`)


Hierauf beantragte die Staatsanwaltschaft Feldkirch in dem Johannes Bergknecht betreffenden Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch am 12. März 2014 gemäß § 355 StPO iVm § 352 Abs 1 Z 1 StPO die Wiederaufnahme des Strafverfahrens im Umfang des am 5. Juni 2013 ergangenen Freispruchs des Angeklagten Johannes Bertrang, weil dieser durch die falsche Beweisaussage der Zeugin Sabrina Holzschuher herbeigeführt worden sei (ON 29).

| Predicted | Gold |
|---|---|
| `Johannes Bertrang` | `Johannes Bertrang` |

**Missed by this rule (FN):**

- `Johannes Bergknecht` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Sabrina Holzschuher` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

| Predicted | Gold |
|---|---|
| `Johannes Bartlmäß` | `Johannes Bartlmäß` |

**Missed by this rule (FN):**

- `Landesgericht Feldkirch` (organisation)
- `Landesgerichts Feldkirch` (organisation)
- `Landesgerichts Feldkirch` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_3`)


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

**Example 7** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_9`)


Rechtliche Beurteilung Der dagegen aus Z 5 und 10 des § 281 Abs 1 StPO ergriffenen Nichtigkeitsbeschwerde des Angeklagten Kretschmer kommt keine Berechtigung zu. Entgegen dem zu beiden Schuldspruchpunkten erhobenen Einwand der Mängelrüge liegt Unvollständigkeit (Z 5 zweiter Fall) zufolge Unterbleibens einer Erörterung der Verantwortungen der jeweils beteiligten Angeklagten nicht vor.

| Predicted | Gold |
|---|---|
| `Kretschmer` | `Kretschmer` |

**Example 8** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_13`)


Zu I/E wurden die Depositionen der Angeklagten Reichenbach und Corinna Pumpenmeier ausdrücklich berücksichtigt und (unter vorangegangener Bezugnahme auf eine Reihe von Verfahrensergebnissen) ebenso als unglaubwürdig beurteilt wie die Behauptung des Beschwerdeführers und des Angeklagten Ruzicka, einander nicht zu kennen (US 15 f).

| Predicted | Gold |
|---|---|
| `Ruzicka` | `Ruzicka` |

**Missed by this rule (FN):**

- `Reichenbach` (person)
- `Corinna Pumpenmeier` (person)

**Example 9** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_15`)


Dies gilt umso mehr für die Einlassung des Angeklagten Kandlbinder selbst, weil dieser von seinem Recht zu schweigen Gebrauch machte und sich zum eigentlichen Anklagevorwurf auf die Aussage beschränkte, nicht geständig zu sein (ON 156 S 42 f).

| Predicted | Gold |
|---|---|
| `Kandlbinder` | `Kandlbinder` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Widerstands` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 1** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Mordes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fruhmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gebhard Sayin`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `Nenad Pschor`(person)
- `Bezirksgerichts Leopoldstadt`(organisation)
- `Mag. Schneider, LL.M.`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Veruntreuung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Leopoldstadt`(organisation)
- `Nenad Panagiotakopoulou`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

**False Positives:**

- `Raufhandels` — no gold match — likely missing annotation

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
- `Mag. Gotsmy`(person)
- `Jennifer Janauscheck`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Dr. Eisenmenger`(person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__7`)


Text Gründe: Die am 26. Jänner 1991 geborene Jennifer Johannwerner wurde mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, mehrerer Vergehen der Körperverletzung nach § 83 Abs 1 StGB und des Vergehens der Sachbeschädigung nach § 125 StGB schuldig erkannt und hiefür unter Anwendung des § 5 Z 4 JGG zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von zwei Monaten verurteilt (Blg ./2 zum Bezugsakt AZ 3 U 166/07x des Bezirksgerichts Kufstein).

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jennifer Johannwerner`(person)
- `Bezirksgerichts Kufstein`(organisation)
- `Bezirksgerichts Kufstein`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Fälschung` — no gold match — likely missing annotation

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

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Fälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktor Meisterernst`(person)
- `Dr. Stefan Tydeck`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Müller`(person)
- `Maximilian Gompertz`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Maximilian Gudzentat der Verbrechen des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (1./), der Vergewaltigung nach § 201 Abs 1 StGB und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (2./) sowie des Vergehens der Nötigung nach § 105 Abs 1 StGB (3./) schuldig erkannt.

**False Positives:**

- `Nötigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximilian Gudzentat`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_4`)


Text Gründe: Mit Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v, wurde der von Sebastian Niemz am 24. Mai 2019 gestellte Antrag auf Fortführung des aufgrund seiner Anzeige von der Staatsanwaltschaft Graz zu AZ 22 St 47/14v gegen Alois Paasch und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen geführten und gegen sämtliche Beschuldigte gemäß § 190 Z 2 StPO eingestellten Ermittlungsverfahrens als unzulässig zurückgewiesen.

**False Positives:**

- `Untreue` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Sebastian Niemz`(person)
- `Alois Paasch`(person)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Salzburg`(organisation)
- `Nikola Miscenko`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Raubes` — no gold match — likely missing annotation

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

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

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
- `Mag. Bachl`(person)
- `Mag. Johanna Fletcher`(person)
- `Herbert Onesseit`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

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

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Karl Wodarcyk des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Vergewaltigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karl Wodarcyk`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Erik Jirouch`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

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
- `Mag. Plesser`(person)
- `Aissa Bussmann`(person)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_7`)


Text Gründe: Mit dem angefochtenen Urteil wurde Aissa Boness des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aissa Boness`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_8`)


Abs 1 fünfter Fall, Abs 2 Z 3 SMG (A) sowie des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 erster und zweiter Fall SMG (B) schuldig erkannt.

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Michael Wessollek des Vergehens der Sachbeschädigung nach § 125 StGB (1/a), des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB (1/b) und des Vergehens der Körperverletzung nach § 83 Abs 1 StGB (2) schuldig erkannt.

**False Positives:**

- `Sachbeschädigung` — no gold match — likely missing annotation
- `Körperverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Michael Wessollek`(person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Urkundenfälschung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 27** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Diebstahls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Ferenc Florin`(person)
- `Gabor Schwiecker`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `OGH`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahlwarth wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Reichly`(person)
- `Tomislav Ahlwarth`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Mag. Hautz in Gegenwart der Richteramtsanwärterin Mag. Wöss als Schriftführerin in der Strafsache gegen Heinrich Käter wegen des Vergehens der Urkundenunterdrückung nach § 229 Abs 1 StGB, AZ 5 U 21/09y des Bezirksgerichts Ybbs, über die Beschwerde des Heinrich Kowacki und der Annemarie Kloiber gegen den Beschluss des Oberlandesgerichts Wien vom 8. April 2010, AZ 18 Bs 73/10g (ON 11), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Urkundenunterdrückung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Hautz`(person)
- `Mag. Wöss`(person)
- `Heinrich Käter`(person)
- `Heinrich Kowacki`(person)
- `Annemarie Kloiber`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_3`)


Kopf Der Oberste Gerichtshof hat am 26. September 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Ertl, LL.M., als Schriftführer in der Strafsache gegen Arijan Peschak wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wels als Schöffengericht vom 14. Juni 2018, GZ 39 Hv 7/18a-76, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `Mag. Ertl, LL.M.`(person)
- `Arijan Peschak`(person)
- `Landesgerichts Wels`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Arijan Preisentans des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG, § 15 StGB als Beteiligter nach § 12 dritter Fall StGB (1.) und des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall SMG (2.) schuldig erkannt.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation
- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Arijan Preisentans`(person)

**Example 32** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_10`)


Da der Tatbestand des Verbrechens des Suchtgifthandels nach § 28a SMG nicht auf „generalpräventive Gesichtspunkte“ abstellt, diese somit die Strafdrohung nicht bestimmen, liegt kein Verstoß gegen das Doppelverwertungsverbot vor.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Backus wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Mag. Müller`(person)
- `Manfred Backus`(person)
- `Landesgerichts Korneuburg`(organisation)
- `Mag. Mugler`(person)
- `Mag. Machac`(person)
- `Mag. Kessler`(person)

**Example 34** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_7`)


RIS-Justiz RS0119509) des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter und dritter Fall SMG (A./1./), (richtig:) des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2 und Abs 4 SMG (A./2./), des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter Fall, Abs 2 SMG (A./3./), (richtig:) der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 (richtig:) zweiter und dritter Fall, Abs 2 SMG (B./I./) und des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 2, Abs 2 SMG (B./II./) schuldig erkannt und unter Anwendung des § 28 Abs 1 StGB nach § 28 Abs 4 SMG zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von sechs Monaten verurteilt. Nach dem Inhalt des Schuldspruchs hat Manfred Börekci in Aussichtsstraße 10, 4201 Aschlberg, Österreich A./ im Zeitraum von 2006 bis zum 8. Oktober 2009 1./ vorschriftswidrig Cannabis mit einem Reinheitsgehalt von zumindest 123 Gramm Delta 9-THC erzeugt und besessen, indem er eine unbekannte Menge an Cannabispflanzen anbaute, erntete, die Blüten trocknete und jedenfalls zum Teil Cannabisharz daraus gewann;

**False Positives:**

- `Vorbereitung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manfred Börekci`(person)
- `Aussichtsstraße 10, 4201 Aschlberg, Österreich`(address)

**Example 35** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart des Rechtspraktikanten Mag. Zechner als Schriftführer in der Strafsache gegen Manfred Mudder und einen weiteren Angeklagten wegen des Vergehens des Betrugs nach § 146 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 28. Jänner 2015, GZ 34 Hv 118/14b-50, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 36** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_6`)


Text Gründe: Mit dem angefochtenen Urteil, das auch in Rechtskraft erwachsene Freisprüche dieses und eines weiteren Angeklagten enthält, wurde Manfred Mikuteit des Vergehens des Betrugs nach § 146 StGB schuldig erkannt.

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manfred Mikuteit`(person)

**Example 37** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Riemenschneider und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Johann Riemenschneider`(person)

**Example 38** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_8`)


Text Gründe: Die Staatsanwaltschaft Wels führt zu AZ 17 St 77/19g ein Ermittlungsverfahren gegen Johann Reithinger wegen des Verdachts des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG und weiterer strafbarer Handlungen.

**False Positives:**

- `Suchtgifthandels` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johann Reithinger`(person)

**Example 39** (doc_id: `deanon_260716_TRAIN/15Os71_21m`) (sent_id: `deanon_260716_TRAIN/15Os71_21m_3`)


Kopf Der Oberste Gerichtshof hat am 2. August 2021 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in der Strafsache gegen unbekannte Täter zum Nachteil des DI Robert Leichtlein wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 49 Bl 31/20w des Landesgerichts Salzburg, über die Beschwerde des DI Laurin Beekman gegen den Beschluss des Oberlandesgerichts Linz vom 23. Oktober 2020, GZ 8 Bs 90/20x-1, nach Einsichtnahme in die Akten durch die Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
- `DI Robert Leichtlein`(person)
- `Landesgerichts Salzburg`(organisation)
- `DI Laurin Beekman`(person)
- `Oberlandesgerichts Linz`(organisation)
- `OGH`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_3`)


Kopf Der Oberste Gerichtshof hat am 11. August 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie durch die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger in Gegenwart des Richteramtsanwärters Mag. Mechtler als Schriftführer in der Strafsache gegen Andreas Gudszenties wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 7 U 49/08s des Bezirksgerichts Innsbruck, über die von der Generalprokuratur erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes gegen die Unterlassung der Verständigung des Vollzugsgerichts von der Verlängerung der Probezeit nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, zu Recht erkannt:  Spruch

**False Positives:**

- `Körperverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schmucker`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Dr. T. Solé`(person)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Mechtler`(person)
- `Andreas Gudszenties`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `Mag. Holzleithner`(person)

**Example 41** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_3`)


Kopf Der Oberste Gerichtshof hat am 29. Februar 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin in der Strafsache gegen Georg Haßelbring wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Dr. Michel-Kwapinski`(person)
- `MMag. Linzner`(person)
- `Georg Haßelbring`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Dr. Sperker`(person)

**Example 42** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_7`)


Text Gründe: Mit dem unangefochten in Rechtskraft erwachsenen Urteil des Landesgerichts Feldkirch vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, wurde Georg Höfs - abweichend von dem in Richtung §§ 146, 147 Abs 2 StGB erhobenen Strafantrag - des Vergehens des Betrugs nach § 146 StGB schuldig erkannt und zu einer teilweise bedingt nachgesehenen Geldstrafe verurteilt. Nach dem Schuldspruch hat er in Chikago 2. Gasse 8, 4613 Hupfau, Österreich mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Bedienstete der (richtig:) Nobars und Huenecken E‑Commerce GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro nicht übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Betrugs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Georg Höfs`(person)
- `Chikago 2. Gasse 8, 4613 Hupfau, Österreich`(address)
- `Nobars und Huenecken E‑Commerce GmbH`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_3`)


Kopf Der Oberste Gerichtshof hat am 12. Mai 2014 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Kotanko als Schriftführerin in der Strafsache gegen Arno Enste wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 24. September 2013, GZ 50 Hv 37/13t-48, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Ratz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Kotanko`(person)
- `Arno Enste`(person)
- `Landesgerichts Feldkirch`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Arno Ellerbrook - soweit im Verfahren über die Nichtigkeitsbeschwerde von Bedeutung - des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Missbrauchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Arno Ellerbrook`(person)

</details>

---

## `bare_names_after_verbs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2683a416`  
**Description:**
Matches bare names after verbs like 'wurde', 'besteht bei', 'entstammt'. Excludes trailing whitespace and common false positives.

**Content:**
```
(?:wurde\s+|besteht\s+bei\s+|entstammt\s+|hat\s+|habe\s+|sei\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 71 | 0 | 71 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 71 | 4108 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

**False Positives:**

- `Ordinationsanträgen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_42`)


Bei jeder Mahnung hat Waldkelkraft auf die Möglichkeit zur Inanspruchnahme der Beratungsstelle des bestehenden Energielieferanten, soweit diese gemäß § 82 Abs 7 ElWOG einzurichten ist, hinzuweisen.

**False Positives:**

- `Waldkelkraft ` — partial — gold is substring of pred: `Waldkelkraft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldkelkraft`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_48`)


Die faktische Geschäftsführung habe Ottokar Lucker ausgeübt.

**False Positives:**

- `Ottokar Lucker ` — partial — gold is substring of pred: `Ottokar Lucker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottokar Lucker`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_160`)


Wenngleich dieses Kriterium in § 25d Abs 2 KSchG nicht (nochmals) unmittelbar einbezogen werden kann, ist es doch der Abstufung zugänglich und hat Einfluss auf die Gesamtbewertung (RIS-Justiz RS0115165 [T2]).

**False Positives:**

- `Einfluss ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_94`)


Im vorliegenden Fall sei Gegenstand des Rechtsstreits aber nur eine Leistungssache nach § 65 Abs 1 Z 1 ASGG.

**False Positives:**

- `Gegenstand ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_165`)


Der Kläger hat seine - wenngleich als „sozialrechtlich“ bezeichnete - Klage auch auf den Titel der Amtshaftung und darüber hinaus auf sämtliche erdenklichen Rechtsgrundlagen mit dem Vorbringen gestützt, die beklagte Partei habe Leistungen bewilligt, ohne ihn darüber aufzuklären, dass Kostenersatz nicht möglich sei.

**False Positives:**

- `Leistungen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_28`)


11. 2015 im Herz Jesu Heim in Neuratting 52, 4943 Nonsbach, Österreich als „Hilfsarbeiterin“ beschäftigt gewesen sei, sei Ergebnis einer unbedenklichen Beweiswürdigung.

**False Positives:**

- `Ergebnis ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Neuratting 52, 4943 Nonsbach, Österreich`(address)

**Example 7** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Andreas Safranski des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB schuldig erkannt.

**False Positives:**

- `Andreas Safranski ` — partial — gold is substring of pred: `Andreas Safranski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Safranski`(person)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_5`)


Gründe:  Rechtliche Beurteilung Bereits mit Beschlüssen des Obersten Gerichtshofs vom 15. September 2011, AZ 12 Ns 56/11y (12 Ns 75/11t), und vom 24. Oktober 2011, AZ 12 Ns 89/11a, wurde Anträgen des Angeklagten auf Delegierung nach § 39 Abs 1 StPO nicht Folge gegeben.

**False Positives:**

- `Anträgen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

**False Positives:**

- `Thomas Maksym ` — partial — gold is substring of pred: `Thomas Maksym`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Maksym`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_8`)


Text Gründe: Mit dem angefochtenen Urteil wurde Thomas Leesmeister des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB (A./) sowie mehrerer Vergehen der Fälschung eines Beweismittels nach § 293 Abs 1 StGB (B./) schuldig erkannt.

**False Positives:**

- `Thomas Leesmeister ` — partial — gold is substring of pred: `Thomas Leesmeister`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Leesmeister`(person)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Ernst`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Maximilian Gudzentat der Verbrechen des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (1./), der Vergewaltigung nach § 201 Abs 1 StGB und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (2./) sowie des Vergehens der Nötigung nach § 105 Abs 1 StGB (3./) schuldig erkannt.

**False Positives:**

- `Maximilian Gudzentat ` — partial — gold is substring of pred: `Maximilian Gudzentat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximilian Gudzentat`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_10`)


Mit gekürzt ausgefertigtem Urteil des Landesgerichts Feldkirch vom 2. September 2013, GZ 20 Hv 68/13f-13, wurde Sabrina Harrazin im Sinne dieser Alternativanklage schuldig erkannt.

**False Positives:**

- `Sabrina Harrazin ` — partial — gold is substring of pred: `Sabrina Harrazin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Sabrina Harrazin`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__11`)


Am 4. April 2017 wurde Zoltan Sundmacher von den ungarischen Behörden an Österreich übergeben (ON 136).

**False Positives:**

- `Zoltan Sundmacher von` — partial — gold is substring of pred: `Zoltan Sundmacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zoltan Sundmacher`(person)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

**False Positives:**

- `Nikola Miscenko ` — partial — gold is substring of pred: `Nikola Miscenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Salzburg`(organisation)
- `Nikola Miscenko`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Martin Pollaczek des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Martin Pollaczek ` — partial — gold is substring of pred: `Martin Pollaczek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Martin Pollaczek`(person)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Mehdi Rater des Vergehens (richtig: Verbrechens) des Raubes nach §§ 15, 142 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Mehdi Rater ` — partial — gold is substring of pred: `Mehdi Rater`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mehdi Rater`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Thomas Eschberger der Verbrechen der Vergewaltigung nach § 201 Abs 2 StGB idF BGBl I 2001/130 (I) und des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 und 3 erster Fall StGB (II/A/1), jeweils mehrerer Verbrechen des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 StGB (II/A/1) und des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB (II/A/2) sowie mehrerer Vergehen des Missbrauchs eines Autoritätsverhältnisses nach § 212 Abs 1 Z 2 StGB (II/A/3) schuldig erkannt.

**False Positives:**

- `Thomas Eschberger ` — partial — gold is substring of pred: `Thomas Eschberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Eschberger`(person)

**Example 19** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Karl Wodarcyk des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Karl Wodarcyk ` — partial — gold is substring of pred: `Karl Wodarcyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karl Wodarcyk`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__8`)


Text Gründe: Mit dem angefochtenen Urteil wurde Erik Justing (richtig:) mehrerer Verbrechen des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 2 Z 1 (zu ergänzen: iVm Abs 3 zweiter Fall) SMG (I/1) sowie der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall SMG (I/2) und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB (II) schuldig erkannt.

**False Positives:**

- `Erik Justing ` — partial — gold is substring of pred: `Erik Justing`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Erik Justing`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_6`)


Text Gründe: Mit in Rechtskraft erwachsenem Urteil des Landesgerichts für Strafsachen Graz vom 23. April 2015, AZ 16 Hv 32/15a, wurde Wolfgang Woerz zu einer Freiheitsstrafe von fünfzehn Monaten verurteilt, wovon ein Strafteil von zehn Monaten gemäß § 43a

**False Positives:**

- `Wolfgang Woerz zu` — partial — gold is substring of pred: `Wolfgang Woerz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Wolfgang Woerz`(person)

**Example 22** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_8`)


Mit rechtskräftigem Abwesenheitsurteil des Bezirksgerichts Weiz vom 25. Juli 2018, GZ 10 U 13/17b-69, wurde Wenholz einer (vom 9. Mai 2016 bis zum 7. September 2017 begangenen) strafbaren Handlung schuldig erkannt.

**False Positives:**

- `Wenholz ` — partial — gold is substring of pred: `Wenholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Weiz`(organisation)
- `Wenholz`(person)

**Example 23** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_7`)


Text Gründe: Mit dem angefochtenen Urteil wurde Aissa Boness des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Aissa Boness ` — partial — gold is substring of pred: `Aissa Boness`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Aissa Boness`(person)

**Example 24** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Michael Wessollek des Vergehens der Sachbeschädigung nach § 125 StGB (1/a), des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB (1/b) und des Vergehens der Körperverletzung nach § 83 Abs 1 StGB (2) schuldig erkannt.

**False Positives:**

- `Michael Wessollek ` — partial — gold is substring of pred: `Michael Wessollek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Michael Wessollek`(person)

**Example 25** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__7`)


Text Gründe: Mit Urteil des Bezirksgerichts Innere Stadt Wien (ON 19) wurde Robert Ulrici jeweils eines Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB schuldig erkannt und hiefür zu einer bedingt nachgesehenen Freiheitsstrafe verurteilt. Nach Verkündung des Urteils und erteilter Rechtsmittelbelehrung erklärte der – nicht durch einen Verteidiger vertretene (vgl § 57 Abs 2 dritter Satz StPO;Fabrizy, StPO13§ 57 Rz 10) – Angeklagte zunächst, auf Rechtsmittel zu verzichten (ON 18 S 5).

**False Positives:**

- `Robert Ulrici ` — partial — gold is substring of pred: `Robert Ulrici`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Robert Ulrici`(person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Ernst Goerlich mehrerer Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB (B) und des Vergehens des sexuellen Missbrauchs von Jugendlichen nach §§ 15, 207b Abs 3 StGB (A) schuldig erkannt.

**False Positives:**

- `Ernst Goerlich ` — partial — gold is substring of pred: `Ernst Goerlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ernst Goerlich`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_5`)


Text Gründe: Mit Urteil des Landesgerichts Klagenfurt als Einzelrichter vom 13. Mai 2019 (ON 20) wurde Christoph Huertler des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB schuldig erkannt und zu einer Geldstrafe sowie dazu verurteilt, dem Privatbeteiligten Fabian Pfandler 500 Euro Schmerzengeld zu zahlen.

**False Positives:**

- `Christoph Huertler ` — partial — gold is substring of pred: `Christoph Huertler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Klagenfurt`(organisation)
- `Christoph Huertler`(person)
- `Fabian Pfandler`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_6`)


Indem sie nämlich - zusammengefasst - allgemein behauptet, der Beschwerdeführer sei Opfer staatlich veranlasster unzulässiger Tatprovokation geworden, und sich weiters gegen die als gesetzwidrig erachtete Verfahrensführung des - nach dem Beschwerdestandpunkt parteilichen und voreingenommenen - Vorsitzenden des Schöffensenats in der am 11. August 2010 durchgeführten und auf unbestimmte Zeit vertagten Hauptverhandlung wendet, richtet sie sich nicht gegen eine - genau zu bezeichnende (§ 3 Abs 1 GRBG) - mit Grundrechtsbeschwerde anfechtbare strafgerichtliche Entscheidung oder Verfügung nach Ausschöpfung des Instanzenzugs (§ 1 Abs 1 GRBG).

**False Positives:**

- `Opfer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__7`)


Text Gründe: Mit Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 2. Dezember 2010, GZ 15 Hv 126/10k-38, wurde Bernd Kalverkamp der Verbrechen der absichtlichen schweren Körperverletzung nach § 87 Abs 1 und Abs 2 erster Fall StGB (I/1) und der schweren Nötigung nach §§ 15, 105 Abs 1, 106 Abs 1 Z 1 und 2 StGB (I/2) schuldig erkannt und hiefür unter Anwendung des § 28 StGB nach § 87 Abs 2 erster Halbsatz StGB zu einer Freiheitsstrafe von 18 (achtzehn) Monaten verurteilt, wovon gemäß § 43a Abs 3 StGB ein Teil von 15 (fünfzehn) Monaten bedingt nachgesehen wurde.

**False Positives:**

- `Bernd Kalverkamp ` — partial — gold is substring of pred: `Bernd Kalverkamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Bernd Kalverkamp`(person)

**Example 30** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_6`)


Text Gründe: Mit auch unbekämpfte Schuldsprüche anderer Angeklagter enthaltendem Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 14. Februar 2017, GZ 24 Hv 4/16v-90, wurde Shafiqullah Gudrun Noeltner des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB schuldig erkannt und – unter Anrechnung von Vorhaftzeiten vom 5. September 2016 bis zum Urteilszeitpunkt – zu einer Freiheitsstrafe von vierundzwanzig Monaten verurteilt, wobei gemäß § 43a

**False Positives:**

- `Shafiqullah Gudrun Noeltner ` — partial — gold is substring of pred: `Gudrun Noeltner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Graz`(organisation)
- `Gudrun Noeltner`(person)

**Example 31** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Arijan Preisentans des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG, § 15 StGB als Beteiligter nach § 12 dritter Fall StGB (1.) und des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall SMG (2.) schuldig erkannt.

**False Positives:**

- `Arijan Preisentans ` — partial — gold is substring of pred: `Arijan Preisentans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arijan Preisentans`(person)

**Example 32** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_10`)


Mit Beschluss des Landesgerichts Wiener Neustadt als Vollzugsgericht vom 24. August 2010, GZ 44 BE 397/10a-5, wurde Radmila Maseizik am 5. November 2010 aus dem Vollzug der mit Urteil des Landesgerichts für Strafsachen Wien vom 12. August 2009, AZ 81 Hv 85/09a, verhängten unbedingten Freiheitsstrafe von 27 Monaten und der mit Urteil des Landesgerichts für Strafsachen Wien vom 8. November 2006, AZ 75 Hv 151/06h, ausgesprochenen zehnmonatigen Freiheitsstrafe nach Verbüßung eines Teils von 25 Monaten gemäß § 46 StGB bedingt entlassen.

**False Positives:**

- `Radmila Maseizik ` — partial — gold is substring of pred: `Radmila Maseizik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Wiener Neustadt`(organisation)
- `Radmila Maseizik`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_6`)


Text Gründe: Mit in Rechtskraft erwachsenem, gekürzt ausgefertigtem Urteil des Einzelrichters des Landesgerichts Korneuburg vom 13. Juni 2012 (ON 69) wurde Manfred Bäumcker des Vergehens (richtig: der Vergehen;

**False Positives:**

- `Manfred Bäumcker ` — partial — gold is substring of pred: `Manfred Bäumcker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Korneuburg`(organisation)
- `Manfred Bäumcker`(person)

**Example 34** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_7`)


RIS-Justiz RS0119509) des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter und dritter Fall SMG (A./1./), (richtig:) des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2 und Abs 4 SMG (A./2./), des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter Fall, Abs 2 SMG (A./3./), (richtig:) der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 (richtig:) zweiter und dritter Fall, Abs 2 SMG (B./I./) und des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 2, Abs 2 SMG (B./II./) schuldig erkannt und unter Anwendung des § 28 Abs 1 StGB nach § 28 Abs 4 SMG zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von sechs Monaten verurteilt. Nach dem Inhalt des Schuldspruchs hat Manfred Börekci in Aussichtsstraße 10, 4201 Aschlberg, Österreich A./ im Zeitraum von 2006 bis zum 8. Oktober 2009 1./ vorschriftswidrig Cannabis mit einem Reinheitsgehalt von zumindest 123 Gramm Delta 9-THC erzeugt und besessen, indem er eine unbekannte Menge an Cannabispflanzen anbaute, erntete, die Blüten trocknete und jedenfalls zum Teil Cannabisharz daraus gewann;

**False Positives:**

- `Manfred Börekci ` — partial — gold is substring of pred: `Manfred Börekci`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manfred Börekci`(person)
- `Aussichtsstraße 10, 4201 Aschlberg, Österreich`(address)

**Example 35** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_6`)


Text Gründe: Mit dem angefochtenen Urteil, das auch in Rechtskraft erwachsene Freisprüche dieses und eines weiteren Angeklagten enthält, wurde Manfred Mikuteit des Vergehens des Betrugs nach § 146 StGB schuldig erkannt.

**False Positives:**

- `Manfred Mikuteit ` — partial — gold is substring of pred: `Manfred Mikuteit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manfred Mikuteit`(person)

**Example 36** (doc_id: `deanon_260716_TRAIN/15Os55_11v`) (sent_id: `deanon_260716_TRAIN/15Os55_11v_5`)


Text Gründe: Mit dem angefochtenen Urteil wurde Elfriede Rentemeister in eine Anstalt für geistig abnorme Rechtsbrecher gemäß § 21 Abs 1 StGB eingewiesen, weil sie am 9. August 2010 in Linz unter dem Einfluss eines ihre Zurechnungsfähigkeit ausschließenden Zustands (§ 11 StGB), der auf einer geistigen oder seelischen Abartigkeit von höherem Grad beruhte, nämlich einer anhaltenden wahnhaften Störung bzw einer paranoiden Schizophrenie, Andrea Göklü eine schwere Körperverletzung (§ 84 Abs 1 StGB) absichtlich zuzufügen versuchte, indem sie auf diese zweimal mit einem Obst- bzw Gemüsemesser in den Brust- und Bauchbereich einstach, wodurch Andrea Gemmi eine 5 mm lange und 5 mm tiefe, bis zum Brustbein reichende Stichwunde am Unterrand der Drosselgrube sowie eine 3 mm lange und knapp 1 cm tiefe Bauchstichwunde erlitt, und hiedurch eine Tat begangen hat, die mit einer ein Jahr übersteigenden Freiheitsstrafe bedroht ist und die ihr, wäre sie zur Tatzeit zurechnungsfähig gewesen, als das Verbrechen der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB zuzurechnen gewesen wäre, und weil nach ihrer Person, ihrem Zustand sowie nach der Art der Tat zu befürchten stand, sie werde unter dem Einfluss ihrer geistigen oder seelischen Abartigkeit eine mit Strafe bedrohte Handlung mit schweren Folgen begehen.

**False Positives:**

- `Elfriede Rentemeister ` — partial — gold is substring of pred: `Elfriede Rentemeister`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Elfriede Rentemeister`(person)
- `Andrea Göklü`(person)
- `Andrea Gemmi`(person)

**Example 37** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_5`)


Text Gründe: Mit rechtskräftigem Beschluss des Landesgerichts Innsbruck als Vollzugsgericht vom 5. Dezember 2006, GZ 23 BE 29/06a-6, wurde Andreas Grieguszies gemäß § 46 Abs 2 StGB aus dem Vollzug mehrerer Freiheitsstrafen (mit einem Strafrest von zwei Monaten) unter Bestimmung einer Probezeit von drei Jahren mit Wirkung vom 2. Jänner 2007 bedingt entlassen.

**False Positives:**

- `Andreas Grieguszies ` — partial — gold is substring of pred: `Andreas Grieguszies`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Innsbruck`(organisation)
- `Andreas Grieguszies`(person)

**Example 38** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_6`)


Mit - auch Freisprüche enthaltendem - Urteil des Bezirksgerichts Innsbruck vom 4. August 2009, GZ 7 U 49/08s-20, wurde Andreas Großjann des (während der Probezeit begangenen) Vergehens der Körperverletzung nach § 83 Abs 1 StGB schuldig erkannt und zu einer Freiheitsstrafe von sechs Wochen verurteilt. Zugleich fasste die Bezirksrichterin den Beschluss, vom Widerruf der im Verfahren AZ 23 BE 29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung abzusehen und die Probezeit auf fünf Jahre zu verlängern (§ 494a Abs 1 Z 2, Abs 6 StPO; s S 4 in ON 18 bzw US 4).

**False Positives:**

- `Andreas Großjann ` — partial — gold is substring of pred: `Andreas Großjann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innsbruck`(organisation)
- `Andreas Großjann`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_7`)


Text Gründe: Mit dem unangefochten in Rechtskraft erwachsenen Urteil des Landesgerichts Feldkirch vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, wurde Georg Höfs - abweichend von dem in Richtung §§ 146, 147 Abs 2 StGB erhobenen Strafantrag - des Vergehens des Betrugs nach § 146 StGB schuldig erkannt und zu einer teilweise bedingt nachgesehenen Geldstrafe verurteilt. Nach dem Schuldspruch hat er in Chikago 2. Gasse 8, 4613 Hupfau, Österreich mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Bedienstete der (richtig:) Nobars und Huenecken E‑Commerce GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro nicht übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Georg Höfs ` — partial — gold is substring of pred: `Georg Höfs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Georg Höfs`(person)
- `Chikago 2. Gasse 8, 4613 Hupfau, Österreich`(address)
- `Nobars und Huenecken E‑Commerce GmbH`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_6`)


Text Gründe: Mit dem angefochtenen Urteil wurde Arno Ellerbrook - soweit im Verfahren über die Nichtigkeitsbeschwerde von Bedeutung - des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB schuldig erkannt.

**False Positives:**

- `Arno Ellerbrook ` — partial — gold is substring of pred: `Arno Ellerbrook`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arno Ellerbrook`(person)

**Example 41** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_9`)


Das Erstgericht ging hinsichtlich des Tatbestandsmerkmals des wissentlichen Befugnismissbrauchs im Wesentlichen von folgendem Sachverhalt aus: Am 23. Dezember 2011 habe Arno Engleitner den verfahrensgegenständlichen PKW gemäß § 57a Abs 1 KFG begutachtet und bestätigt, dass dieses Fahrzeug keine Mängel aufweise.

**False Positives:**

- `Arno Engleitner ` — partial — gold is substring of pred: `Arno Engleitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arno Engleitner`(person)

**Example 42** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_46`)


Der obere, nicht so sumpfige Bereich wurde als Wiese genutzt (es wurde Gras gemäht und Heu aufgehängt).

**False Positives:**

- `Gras ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_38`)


Hier sei Grund für das Engagement des Klägers das Interesse der Beklagten an der Besicherung des Kredits gewesen.

**False Positives:**

- `Grund ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Xaver Springinsgut`

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

**Example 45** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_15`)


Die richterliche Feststellung des Erbrechts sei Sache des Verlassenschaftsverfahrens, in dem die in Frage kommenden Personen ihre Ansprüche schon vor Einantwortung gerichtlich geltend machen könnten.

**False Positives:**

- `Sache ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_20`)


Der Kläger sei Begünstigter von Punkt 6 des Schenkungsvertrags, der einen Vertrag zugunsten Dritter darstelle.

**False Positives:**

- `Begünstigter von` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_260716_TRAIN/2Ob28_14b`) (sent_id: `deanon_260716_TRAIN/2Ob28_14b_24`)


Personenschutz sei Sache der Exekutive.

**False Positives:**

- `Sache ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_260716_TRAIN/2Ob99_24h`) (sent_id: `deanon_260716_TRAIN/2Ob99_24h_17`)


Der Geschädigte, der Zeit und Geld zur Behebung des Schadens aufwenden müsse, habe Anspruch auf Ersatz dieses Mehraufwands.

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_260716_TRAIN/3Ob182_11b`) (sent_id: `deanon_260716_TRAIN/3Ob182_11b_86`)


Der Klägerin sei schon vor Abruf der Bankgarantie deren Ziehung angekündigt worden, sie habe Kenntnis davon gehabt, dass die zu erwartenden Sanierungskosten die Garantiesumme übersteigen werden, und die Bauherrin habe am 12. August 2005 gegenüber der Klägerin ausdrücklich erklärt, die Garantiesumme als Deckungskapital für die durchzuführende Reparatur zu vereinnahmen.

**False Positives:**

- `Kenntnis ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/3Ob201_19h`) (sent_id: `deanon_260716_TRAIN/3Ob201_19h_12`)


Die Betreibende stehe zu Unrecht auf dem Standpunkt, sie habe Anspruch auf weitere Zahlungen, weil sie mit ihrem Rechtsvertreter im Innenverhältnis ein Zeithonorar vereinbart habe, das den gesetzlichen Rechtsanwaltstarif weit übersteige.

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_61`)


Sie habe Anspruch auf das Deckungskapital für die zu erwartenden Sanierungskosten, wobei die Angemessenheit der begehrten Beträge durch Kostenvoranschläge oder durch Sachverständigengutachten nachgewiesen werden könne.

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_260716_TRAIN/4Ob149_13k`) (sent_id: `deanon_260716_TRAIN/4Ob149_13k_5`)


Die Urteile der Vorinstanzen, die in der Abweisung des Hauptunterlassungsbegehrens bestätigt werden, werden im übrigen dahin abgeändert, dass die Entscheidung nunmehr zu lauten hat:“ 2. In den Entscheidungsgründen hat Punkt 10.

**False Positives:**

- `Punkt ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_260716_TRAIN/4Ob23_24x`) (sent_id: `deanon_260716_TRAIN/4Ob23_24x_14`)


[4] DerBeklagtebeantragte die Abweisung des Klagebegehrens und entgegnete, er habe Kaufverträge über Medizinprodukte vermittelt und nicht mit Medizinprodukten gehandelt. Seine Gewerbeberechtigung als Handelsagent umfasse auch die Vermittlung von Kaufverträgen über Medizinprodukte.

**False Positives:**

- `Kaufverträge ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_260716_TRAIN/5Ob106_20d`) (sent_id: `deanon_260716_TRAIN/5Ob106_20d_12`)


Der mj OSR Richard Froschmaier werde vom Vater vernachlässigt, der mj Ernestine Dornedden habe Suizidabsichten geäußert.

**False Positives:**

- `Suizidabsichten ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR Richard Froschmaier`(person)
- `Ernestine Dornedden`(person)

**Example 55** (doc_id: `deanon_260716_TRAIN/5Ob106_20d`) (sent_id: `deanon_260716_TRAIN/5Ob106_20d_110`)


Er ist Bote und Überbringer des Kindeswillens und hat Unterstützungs- und Beistandsfunktion (10 Ob 47/14f).

**False Positives:**

- `Unterstützungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_260716_TRAIN/5Ob152_12g`) (sent_id: `deanon_260716_TRAIN/5Ob152_12g_21`)


Sie werde auch für Streit zwischen diesen verantwortlich gemacht und habe Angst, so wie im Sommer davor, eingesperrt zu werden.

**False Positives:**

- `Angst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_260716_TRAIN/5Ob152_12g`) (sent_id: `deanon_260716_TRAIN/5Ob152_12g_27`)


Im Zeitpunkt der Krisenunterbringung der Minderjährigen sei Gefahr im Verzug vorgelegen, weil häusliche Probleme schon aus der Vorgeschichte bekannt gewesen seien und die Minderjährige gedroht habe, von zu Hause wegzulaufen.

**False Positives:**

- `Gefahr ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_260716_TRAIN/5Ob152_12g`) (sent_id: `deanon_260716_TRAIN/5Ob152_12g_71`)


Sie werde auch für Streit zwischen diesen verantwortlich gemacht und habe Angst, so wie im Sommer davor, eingesperrt zu werden.

**False Positives:**

- `Angst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_260716_TRAIN/5Ob177_20w`) (sent_id: `deanon_260716_TRAIN/5Ob177_20w_147`)


Demgemäß besteht bei Auslegung eines Gesetzes auch keine Bindung an die in den Gesetzesmaterialien geäußerte Meinung (RS0008799).

**False Positives:**

- `Auslegung ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_42`)


Es begründete dies damit, die Vorfrage der Genehmigungspflicht der Anteilsabtretungen und damit die offenbare Unrichtigkeit der Abtretungen im Sinne des § 10 Abs 2 FBG sei Gegenstand eines früheren Firmenbuchverfahrens des Erstgerichts gewesen.

**False Positives:**

- `Gegenstand ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_418`)


DieBeklagteentgegnete, die beanstandete Klausel sei nicht Bestandteil ihrer AGB, sondern sei Angeboten entnommen, für die ausschließlich der jeweilige Anbieter verantwortlich sei, ohne dass sie darauf Einfluss habe.

**False Positives:**

- `Angeboten ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_508`)


Die Beklagte hat Anspruch auf den Ersatz eines Drittels der Kosten ihrer Berufungsbeantwortung auf einer Bemessungsgrundlage von 9.818,18 EUR, das sind 361,84 EUR (darin 60,31 EUR USt).

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_511`)


Der Kläger hat Anspruch auf den Ersatz von 42 % der Kosten seiner Berufungsbeantwortung auf der verzeichneten Bemessungsgrundlage von 18.000 EUR, das sind 731,10 EUR (darin 121,85 EUR USt).

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_515`)


Der Kläger hat Anspruch auf den Ersatz eines Drittels der Kosten seiner Revisionsbeantwortung auf der verzeichneten Bemessungsgrundlage von 27.818,18 EUR, das sind 601,50 EUR (darin 100,25 EUR USt).

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_260716_TRAIN/6Ob69_23z`) (sent_id: `deanon_260716_TRAIN/6Ob69_23z_10`)


Er sei Angestellter der Fahrschule „ Manuel Stüvcke “ gewesen und erst später (am 15. 5. 2020) als Inhaber der „Fahrschule Schöttl Sanitär – Ing Garten Deral “ im Firmenbuch eingetragen worden.

**False Positives:**

- `Angestellter ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manuel Stüvcke`(organisation)
- `Schöttl Sanitär`(organisation)
- `Garten Deral`(organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/6Ob69_23z`) (sent_id: `deanon_260716_TRAIN/6Ob69_23z_17`)


Zuvor sei Ing. Alessia Wahlen Inhaber gewesen;

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Alessia Wahlen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Alessia Wahlen`(person)

**Example 67** (doc_id: `deanon_260716_TRAIN/7Ob203_24i`) (sent_id: `deanon_260716_TRAIN/7Ob203_24i_19`)


Nur eine vom Versicherungsnehmer willkürlich herbeigeführte Gefahrenerhöhung hat Leistungsfreiheit nach § 25 Abs 1 VersVG zur Folge.

**False Positives:**

- `Leistungsfreiheit ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_69`)


Der österreichische Gesetzgeber hat Art 186 Abs 1 der Solvabilität-II-Richtlinie mit dem Bundesgesetz, mit dem das Versicherungsvertragsgesetz, das Konsumentenschutzgesetz und das Versicherungsaufsichtsgesetz 2016 geändert werden (BGBl I 2018/51) in Form des einheitlichen Rücktrittsrechts nach § 5c VersVG (idgF) umgesetzt.

**False Positives:**

- `Art ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_260716_TRAIN/8Ob86_23i`) (sent_id: `deanon_260716_TRAIN/8Ob86_23i_10`)


Die Klägerin habe Anspruch auf Unterhalt nach den Vorgaben des § 94 ABGB.

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_71`)


Die Beklagte habe Anspruch darauf, den Mangel zu beheben.

**False Positives:**

- `Anspruch ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `names_with_legal_titles`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b7b0ec68`  
**Description:**
Matches names preceded by specific legal titles like 'Senatspräsident', 'Hofrat', 'Vizepräsident' to ensure the full name is captured including the title context.

**Content:**
```
(?:Senatspräsident(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|Vizepräsident(?:in)?|Hofrat(?:in)?(?:\s+des\s+Obersten\s+Gerichtshofs)?|fachkundiger\s+Laienrichter(?:in)?|Richter(?:in)?|Schriftführer(?:in)?|Generalprokurator(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Rechtsanwält(?:in)?)(\s+)([A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)*(?:\s+(?:von|zu|von\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)?(?:\s*-[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+(?:\s+[A-Z][a-zäöüßÄÖÜéèêëàâîïôûç]+)?)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 307 | 0 | 307 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 307 | 4148 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schramm`
- `Univ` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Florens Drehkopf, LLB`(person)
- `16. Dezember 1952`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Nowotny`
- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Nowotny`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gmb` — similar text (different position): `Hochenadel Immobilien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Eva Abdelrahman`(person)
- `Dr. Karl-Heinz Plankel`(person)
- `Hochenadel Immobilien GmbH`(organisation)
- `Ritterhof 11, 2661 Graben, Österreich`(address)
- `Lederer Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Juri Gerstl`(person)
- `Mutten 18, 3251 Schauboden, Österreich`(address)
- `Dr. Ralph Trischler`(person)
- `Bundesbeschaffung GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Hofräte Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `DDr.in Cornelia Rinaldo`(person)
- `Dr. Sven Rudolf Thorstensen`(person)
- `Conmon-Verlag Limited`(organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich`(address)
- `Brandl Talos Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Bau Zorostfurt GmbH`(organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich`(address)
- `Dr. Alexandra Slama`(person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH`(organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich`(address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Sandra Hilt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sandra Hilt`(person)
- `Mag. Manuel Kumas`(person)
- `MMMag. Gottfried Fegbeitel`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Paolo Barley`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Paolo Barley`(person)
- `Mag. Klarissa Hausteiner`(person)
- `Mag. Viola Brauch`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Maja Dolleschell`(person)
- `14. August`(date)
- `Bezirkshauptmannschaft Melk`(organisation)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts Melk`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Leander Andermann`(person)
- `Dr. Martin Leitner`(person)
- `Ing. Ferdinand Abramova`(person)
- `Mag. Wilhelm Deutschmann MBA`(person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Hofräte Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Dr. Annerl`(person)
- `Meinrad Bruhnsen`(person)
- `30. Januar`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Othmar Mertl`(person)
- `Malik Fridt`(person)
- `Krist Bubits Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Dr` — similar text (different position): `Univ.-Prof. Dr. Neumayr`
- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Scarlett Achatzi`(person)
- `Mag. Ewald Aszmutat`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Ziegelbauer`
- `Gmb` — partial — pred is substring of gold: `Vogl Rechtsanwalt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Hofrätinnen Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hofrat Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `DI Cassandra Wespi`(person)
- `Vogl Rechtsanwalt GmbH`(organisation)
- `Bilek Lebensmittel GmbH`(organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich`(address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — similar text (different position): `Dr. Hradil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Hofrat Dr. Fellinger`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `KR Hermann Furtner`(person)
- `AR Angelika Neuhauser`(person)
- `Birgit Jaros`(person)
- `Dr. Herbert Pochieser`(person)
- `Dr. Heinz Edelmann`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr` — similar text (different position): `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Hofrätin Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Schwab`

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

**Example 24** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Schwab`

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

**Example 25** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Solé`
- `Dr` — similar text (different position): `Dr. Solé`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 26** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel treten aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an deren Stelle (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Schroll`

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

**Example 30** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Oliver Paukstat`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_5`)


An Stelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger tritt Hofrat des Obersten Gerichtshofs Dr. Nordmeyer.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Bachner-Foregger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)

**Example 32** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender des zuständigen 11.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)

**Example 33** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_10`)


Als deren Angehöriger (§ 72 StGB) ist Senatspräsident des Obersten Gerichtshofs Dr. Schwab gemäß § 43 Abs 3 StPO von der Entscheidung über die vorliegende Beschwerde ausgeschlossen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)

**Example 34** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_11`)


Hofrat des Obersten Gerichtshofs Dr. Nordmeyer tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs anstelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Nordmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)

**Example 35** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)
- `Gerhard Boesl`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_5`)


An deren Stelle treten Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Nordmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)

**Example 37** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender, Hofrätin des Obersten Gerichtshofs Mag. Michel ist Mitglied des zuständigen 11.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)

**Example 38** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Dr. Christine Schwab`(person)

**Example 39** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_15`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist damit von der Entscheidung über das vorliegende Rechtsmittel ausgeschlossen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schwab`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)

**Example 40** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_17`)


3. An die Stelle der Ausgeschlossenen treten aufgrund der laufenden Vertretungsregelung Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski. (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Nordmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Hon` — similar text (different position): `Hon.-Prof. Dr. Schroll`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 42** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_5`)


An ihre Stelle tritt Hofrat des Obersten Gerichtshofs Dr. Oshidari.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Oshidari`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)

**Example 43** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_11`)


Hofrat des Obersten Gerichtshofs Dr. Oshidari tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an ihre Stelle (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Oshidari`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. T. Solé`
- `Dr` — similar text (different position): `Dr. T. Solé`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 45** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_7`)


Senat des Oberlandesgerichts Wien, dem der Senatspräsident Dr. Krenn sowie die Richterinnen Mag. Edwards und Mag. Sanda angehörten, dieses Urteil „in amtswegiger Wahrnehmung des Nichtigkeitsgrunds des § 281 Abs 1 Z 9 lit a iVm § 489 Abs 1 StPO“ wegen des Vorliegens von Rechtsfehlern mangels Feststellungen (vgl zu diesem BegriffRatz, WK-StPO § 281 Rz 605 ff) in den Schuldsprüchen I./ und III./, demgemäß im Strafausspruch und im Ausspruch über den Privatbeteiligtenanspruch auf und verwies die Sache in diesem Umfang zu neuerlicher Verhandlung und Entscheidung an das Erstgericht.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Krenn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Krenn`(person)
- `Mag. Edwards`(person)
- `Mag. Sanda`(person)

**Example 46** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_12`)


Mit Beschluss vom 17. Oktober 2018, AZ 130 Ns 31/18w, stellte der Präsident des Oberlandesgerichts Wien fest, dass Senatspräsident Dr. Krenn sowie die Richterinnen Mag. Edwards und Mag. Sanda „im Berufungsverfahren über die vom Erstangeklagten Thomas Mecit erhobene Berufung (ON 107) ausgeschlossen“ seien.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Krenn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Krenn`(person)
- `Mag. Edwards`(person)
- `Mag. Sanda`(person)
- `Thomas Mecit`(person)

**Example 47** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Schroll`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fruhmann`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Gebhard Sayin`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. T. Solé`
- `Dr` — similar text (different position): `Dr. T. Solé`

> overlaps gold: 2  |  likely missing annotation: 0

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
- `Nenad Pschor`(person)
- `Bezirksgerichts Leopoldstadt`(organisation)
- `Mag. Schneider, LL.M.`(person)

**Example 49** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — similar text (different position): `Dr. Solé`

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

**Example 50** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Oshidari`

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

**Example 51** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Schroll`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Müller`(person)
- `Maximilian Gompertz`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Novko im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Lässig`

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

**Example 53** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Lendl, Mag. Michel und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Roman Ueberlein und einen weiteren Angeklagten wegen des Verbrechens des schweren gewerbsmäßig durch Einbruch begangenen Diebstahls nach §§ 127, 128 Abs 1 Z 5, 129 Abs 2 Z 1 (iVm Abs 1 Z 1), 130 Abs 3 (iVm Abs 1 erster Fall) und 15 StGB sowie einer weiteren strafbaren Handlung, AZ 37 Hv 122/18b des Landesgerichts Innsbruck, über den Antrag des Verurteilten Roman Urbath auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Lässig`

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

**Example 54** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Lässig`

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

**Example 55** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Schoenwiese wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Lässig`

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

**Example 56** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__3`)


Kopf Der Oberste Gerichtshof hat am 5. April 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig und die Hofrätin des Obersten Gerichtshofs Mag. Marek in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin im Verfahren zur Unterbringung der Mag. Türkan Maja Besold in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 33 Hv 24/12g des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde der Betroffenen nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Kirchbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `MMag. Linzner`(person)
- `Maja Besold`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Kirchbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Erik Jirouch`(person)

**Example 58** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — similar text (different position): `Mag. Michel`

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

**Example 59** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Kirchbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Temper`(person)
- `Michael Lengjel`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Anna Wynand`(person)
- `Brian Waltemate`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Grießbaum wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Ratz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Ratz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Einwagner`(person)
- `Ernst Grießbaum`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Lässig`

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

**Example 62** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_3`)


Kopf Der Oberste Gerichtshof hat am 24. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Straf- und Medienrechtssache der Privatanklägerin und Antragstellerin Petra Schwegle gegen den Angeklagten und Antragsgegner Holger Voelke wegen des Vergehens der üblen Nachrede nach § 111 StGB und einer weiteren strafbaren Handlung sowie § 6 Abs 1 und § 34 Abs 1 MedienG, AZ 92 Hv 58/19a des Landesgerichts für Strafsachen Wien, über den Antrag des Angeklagten und Antragsgegners auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Danek`

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

**Example 63** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Philipp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Ferenc Florin`(person)
- `Gabor Schwiecker`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `OGH`(organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahlwarth wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Philipp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Reichly`(person)
- `Tomislav Ahlwarth`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/14Os133_19v`) (sent_id: `deanon_260716_TRAIN/14Os133_19v_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Finanzstrafsache gegen Dr. Peter Johanni wegen des Finanzvergehens der Abgabenhinterziehung nach §§ 33 Abs 1, 13 FinStrG, AZ 14 Hv 3/10a des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 23. Oktober 2019, AZ 23 Bs 323/19x, nach Einsichtnahme der Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Prof. Dr. Danek`

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

**Example 66** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Mag. Hautz in Gegenwart der Richteramtsanwärterin Mag. Wöss als Schriftführerin in der Strafsache gegen Heinrich Käter wegen des Vergehens der Urkundenunterdrückung nach § 229 Abs 1 StGB, AZ 5 U 21/09y des Bezirksgerichts Ybbs, über die Beschwerde des Heinrich Kowacki und der Annemarie Kloiber gegen den Beschluss des Oberlandesgerichts Wien vom 8. April 2010, AZ 18 Bs 73/10g (ON 11), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Philipp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Hautz`(person)
- `Mag. Wöss`(person)
- `Heinrich Käter`(person)
- `Heinrich Kowacki`(person)
- `Annemarie Kloiber`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/15Ns104_16m`) (sent_id: `deanon_260716_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Herdemertens wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Dr. Danek`

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

**Example 68** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_3`)


Kopf Der Oberste Gerichtshof hat am 16. November 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Beran als Schriftführer in der Strafsache gegen Peter Eckehardt wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 StGB und einer weiteren strafbaren Handlung, über die von der Generalprokuratur gegen den Beschluss des Bezirksgerichts Steyr vom 7. Mai 2013, GZ 5 U 44/12h-39, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Janda, sowie des Angeklagten zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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

**Example 69** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Kira Nesselrodt und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Erwin Nungässer gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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

**Example 70** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_3`)


Kopf Der Oberste Gerichtshof hat am 26. September 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Ertl, LL.M., als Schriftführer in der Strafsache gegen Arijan Peschak wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wels als Schöffengericht vom 14. Juni 2018, GZ 39 Hv 7/18a-76, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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
- `Mag. Ertl, LL.M.`(person)
- `Arijan Peschak`(person)
- `Landesgerichts Wels`(organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Backus wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Mag. Müller`(person)
- `Manfred Backus`(person)
- `Landesgerichts Korneuburg`(organisation)
- `Mag. Mugler`(person)
- `Mag. Machac`(person)
- `Mag. Kessler`(person)

**Example 72** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart des Rechtspraktikanten Mag. Zechner als Schriftführer in der Strafsache gegen Manfred Mudder und einen weiteren Angeklagten wegen des Vergehens des Betrugs nach § 146 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 28. Jänner 2015, GZ 34 Hv 118/14b-50, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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

**Example 73** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Riemenschneider und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Johann Riemenschneider`(person)

**Example 74** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


Kopf Der Oberste Gerichtshof hat am 11. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH und eine weitere Antragsgegnerin wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018 (ON 65 der Hv-Akten) und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, des Vertreters des Antragstellers, Dr. Bauer, und des Vertreters der Antragsgegnerin Analyse Fenheim GmbH, Mag. Bauer, zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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

**Example 75** (doc_id: `deanon_260716_TRAIN/15Os71_21m`) (sent_id: `deanon_260716_TRAIN/15Os71_21m_3`)


Kopf Der Oberste Gerichtshof hat am 2. August 2021 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in der Strafsache gegen unbekannte Täter zum Nachteil des DI Robert Leichtlein wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 49 Bl 31/20w des Landesgerichts Salzburg, über die Beschwerde des DI Laurin Beekman gegen den Beschluss des Oberlandesgerichts Linz vom 23. Oktober 2020, GZ 8 Bs 90/20x-1, nach Einsichtnahme in die Akten durch die Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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
- `DI Robert Leichtlein`(person)
- `Landesgerichts Salzburg`(organisation)
- `DI Laurin Beekman`(person)
- `Oberlandesgerichts Linz`(organisation)
- `OGH`(organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Lendl`

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

**Example 77** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_3`)


Kopf Der Oberste Gerichtshof hat am 11. August 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie durch die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger in Gegenwart des Richteramtsanwärters Mag. Mechtler als Schriftführer in der Strafsache gegen Andreas Gudszenties wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 7 U 49/08s des Bezirksgerichts Innsbruck, über die von der Generalprokuratur erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes gegen die Unterlassung der Verständigung des Vollzugsgerichts von der Verlängerung der Probezeit nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Schmucker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schmucker`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Danek`(person)
- `Dr. T. Solé`(person)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Mechtler`(person)
- `Andreas Gudszenties`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `Mag. Holzleithner`(person)

**Example 78** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Lovrek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Musger`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Hofrätin Dr. Kodek`(person)
- `Hofrat Dr. Stefula`(person)
- `Dr. Joshua Reupold`(person)
- `Wald-Versand Gesellschaft mbH`(organisation)
- `Kugelmannplatz 4, 5121 Döstling, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Johanna Baldczus`(person)
- `MedR Nadja Grela`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Lovrek`
- `Dr` — similar text (different position): `Hon.-Prof. Dr. Lovrek`
- `Gmb` — partial — pred is substring of gold: `Stephan Briem Rechtsanwalt GmbH`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hofrat Dr. Musger`(person)
- `Mag. Malesich`(person)
- `Dr. Kodek`(person)
- `Hofrat Dr. Stefula`(person)
- `Pascal Alsweh`(person)
- `Stephan Briem Rechtsanwalt GmbH`(organisation)
- `Dr. Simone Pittruff`(person)
- `Unter-Analyse Aktiengesellschaft`(organisation)
- `Shamiyeh & Reiser Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Hon.-Prof. PD Dr. Rassi als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Nowotny, den Hofrat Mag. Painsi, die Hofrätin Dr. Kodek und den Hofrat Dr. Thunhart in der Rechtssache der klagenden Partei Janis Klooth, vertreten durch Mag. Robert Levovnik, Rechtsanwalt in Klagenfurt am Wörthersee, gegen die beklagte Partei Wendy Jannßen, vertreten durch Mag. Michael Wirrer, Rechtsanwalt in Wien, wegen Aufhebung eines Schiedsspruchs (Streitwert 3.600 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird zurückgewiesen und das bisherige Verfahren als nichtig aufgehoben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Hofrat Mag. Painsi`
- `Dr` — similar text (different position): `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hofrat Mag. Painsi`(person)
- `Hofrätin Dr. Kodek`(person)
- `Hofrat Dr. Thunhart`(person)
- `Janis Klooth`(person)
- `Mag. Robert Levovnik`(person)
- `Wendy Jannßen`(person)
- `Mag. Michael Wirrer`(person)

**Example 81** (doc_id: `deanon_260716_TRAIN/1Nc10_18p`) (sent_id: `deanon_260716_TRAIN/1Nc10_18p_6`)


In seinem zugrundeliegenden Verfahrenshilfeantrag hatte er als Fehlverhalten, das er zum Anlass nehmen möchte, einen Amtshaftungsanspruch gegen den Bund geltend zu machen, die Aussetzung von zwei Verfahren des Landesgerichts für Zivilrechtssachen Graz (gemäß § 6a ZPO) durch die Richterin Mag. Hartmut Remolt angeführt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Hartmut Remolt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Mag. Hartmut Remolt`(person)

**Example 82** (doc_id: `deanon_260716_TRAIN/1Ob160_10a`) (sent_id: `deanon_260716_TRAIN/1Ob160_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Dr. Fichtenau, Dr. Grohmann, Univ.-Prof. Dr. Kodek und Dr. E. Solé als weitere Richter in der Pflegschaftssache des am 10. August 2000 geborenen mj Nino Küntzelmann, über den außerordentlichen Revisionsrekurs des Vaters Daniel Kohlhase, vertreten durch Mag. Stefan Aberer, Rechtsanwalt in Bregenz, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 27. Juli 2010, GZ 3 R 247/10m-60, mit dem der Beschluss des Bezirksgerichts Bregenz vom 22. Juni 2010, GZ 24 PS 46/09s-52, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof. Dr. Bydlinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. E. Solé`(person)
- `Nino Küntzelmann`(person)
- `Daniel Kohlhase`(person)
- `Mag. Stefan Aberer`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Bregenz`(organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Aloisa Moosleitner, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Catharina Uppenbrink, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Wurzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Wurzer`(person)
- `Hofräte Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Kodek`(person)
- `Aloisa Moosleitner`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Catharina Uppenbrink`(person)
- `Dr. Alexander Haas`(person)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Fürstenfeld`(organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/1Ob216_19z`) (sent_id: `deanon_260716_TRAIN/1Ob216_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Mag. Wurzer als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer, Dr. Parzmayr und Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Charles Adlwarth, MMSc, Haidspitzgasse 53R, 4294 Rehberg, Österreich, vertreten durch Dr. Michael Pallauf, LL.M., und andere, Rechtsanwälte in Salzburg, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 41.978,49 EUR sA sowie Feststellung (Streitwert 40.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. September 2019, GZ 14 R 75/19f-18, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2019, GZ 33 Cg 26/18p-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Wurzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Dr. Faber`(person)
- `Charles Adlwarth`(person)
- `Haidspitzgasse 53R, 4294 Rehberg, Österreich`(address)
- `Dr. Michael Pallauf, LL.M.`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_18`)


[4] Das Pflegschaftsgericht bestellte mit Beschluss vom 18. 12. 2018 den Rechtsanwalt Dr. Bartholomäus Hoepcke zum gerichtlichen Erwachsenenvertreter für den Beklagten, unter anderem zur Vertretung in gerichtlichen Verfahren, insbesondere auch zur Vertretung des Betroffenen im bereits anhängigen Scheidungsverfahren.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Bartholomäus Hoepcke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Bartholomäus Hoepcke`(person)

**Example 86** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_12`)


Hingegen wurden durch die Abweisung des Antrags auf Vernehmung des Zeugen Rechtsanwalt Dr. Herwig Mauche zum Beweis dafür, dass der Disziplinarbeschuldigte nicht Verfasser sämtlicher inkriminierter Schriftsätze und er „nicht unmittelbar in die Errichtung derselben eingebunden“ war, ferner in der Kanzlei des Disziplinarbeschuldigten die Diktatzeichen auf Schriftsätzen keinen sicheren Rückschluss auf den jeweiligen Schriftsatzverfasser ermöglichen und dessen Kanzlei derart organisiert ist, dass die Freigabe von Schriftsätzen, somit auch der inkriminierten, jeweils von einem sachbearbeitenden eingetragenen (zum Zeichen der Freigabe das jeweilige ERV-Deckblatt paraphierenden) Rechtsanwalt erfolgt, Verteidigungsrechte verletzt.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Herwig Mauche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Herwig Mauche`(person)

**Example 87** (doc_id: `deanon_260716_TRAIN/2Ob114_24i`) (sent_id: `deanon_260716_TRAIN/2Ob114_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dorothea Woltzen, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Edeltraud Eickemeyer, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Grohmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hofräte MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Hofrätin Mag. Fitz`(person)
- `Dorothea Woltzen`(person)
- `Metzler & Partner Rechtsanwälte GmbH`(organisation)
- `Edeltraud Eickemeyer`(person)
- `Nenning & Tockner, Rechtsanwälte`(organisation)
- `Landesgerichts Steyr`(organisation)
- `Bezirksgerichts Kirchdorf an der Krems`(organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/2Ob145_15k`) (sent_id: `deanon_260716_TRAIN/2Ob145_15k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei VetR Julia Schnicke, vertreten durch Dr. Michael Langhofer, Rechtsanwalt in Neumarkt am Wallersee, gegen die beklagte Partei Jason Hegenloh, vertreten durch Dr. Anton Waltl, Rechtsanwalt in Zell am See, wegen 197.272,07 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Mai 2015, GZ 6 R 69/15g-81, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Danzl`

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

**Example 89** (doc_id: `deanon_260716_TRAIN/2Ob159_18y`) (sent_id: `deanon_260716_TRAIN/2Ob159_18y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Constantin Tritscher, vertreten durch Dr. Heinrich Oppitz, Rechtsanwalt in Wels, wider die beklagten Parteien 1. Quirin Kläß, 2. Anneliese Imholt, und 3. Roswitha Große-Venhaus, alle vertreten durch Dr. Wolfgang Muchitsch, Rechtsanwalt in Graz, wegen 32.086 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2018, GZ 6 R 21/18b-59, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Wels vom 15. Dezember 2017, GZ 36 Cg 34/16a-55, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Veith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Hofrat Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Hofräte Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Constantin Tritscher`(person)
- `Dr. Heinrich Oppitz`(person)
- `Quirin Kläß`(person)
- `Anneliese Imholt`(person)
- `Roswitha Große-Venhaus`(person)
- `Dr. Wolfgang Muchitsch`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Prof.in Romana Janaseck, vertreten durch Lirk Spielbüchler Hirtzberger Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Simone Gintautas, wegen Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 18. Juli 2023, GZ 21 R 75/23k-7, mit dem der Beschluss des Bezirksgerichts St. Johann im Pongau vom 28. Februar 2023, GZ 305 C 9/23x-3, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Grohmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda und Dr. Kikinger`(person)
- `Hofrätin Mag. Fitz`(person)
- `Prof.in Romana Janaseck`(person)
- `Hirtzberger Rechtsanwälte OG`(organisation)
- `Simone Gintautas`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/2Ob175_21f`) (sent_id: `deanon_260716_TRAIN/2Ob175_21f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Roxana Eisenhoefer, vertreten durch Mag. Axel Bauer, Rechtsanwalt in Wien, gegen die beklagte Partei Magdalena Wosniak, vertreten durch Dr. Manfred Sommerbauer ua, Rechtsanwälte in Wiener Neustadt, wegen 44.903,84 EUR sA, über die Revision der beklagten Partei gegen das Zwischenurteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. Juni 2021, GZ 11 R 79/21z-66, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. März 2021, GZ 5 Cg 105/19a-50 in der Fassung des Berichtigungsbeschlusses vom 16. März 2021, GZ 5 Cg 105/19a-51, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Grohmann`
- `Dr` — similar text (different position): `Dr. Grohmann`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hofrat Dr. Musger`(person)
- `Hofrätin Dr. Solé`(person)
- `Hofräte Dr. Nowotny`(person)
- `MMag. Sloboda`(person)
- `Roxana Eisenhoefer`(person)
- `Mag. Axel Bauer`(person)
- `Magdalena Wosniak`(person)
- `Dr. Manfred Sommerbauer`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 92** (doc_id: `deanon_260716_TRAIN/2Ob179_15k`) (sent_id: `deanon_260716_TRAIN/2Ob179_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Evelyn Wieders, Bakk. iur., vertreten durch Dr. Klaus Estl, Rechtsanwalt in Salzburg, gegen die beklagten Parteien 1. Cäcilia Schlemmer, und 2. Dr. Priv.-Doz. Dietmar Aydinlik, vertreten durch Dr. Roland Reichl, Rechtsanwalt in Salzburg, wegen 10.000 EUR sA und Feststellung (Streitinteresse 5.000 EUR), über den Rekurs der zweitbeklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 22. Juli 2015, GZ 22 R 169/15d-52, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Salzburg vom 2. April 2015, GZ 32 C 896/12f-47, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Danzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Danzl`(person)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Evelyn Wieders, Bakk. iur.`(person)
- `Dr. Klaus Estl`(person)
- `Cäcilia Schlemmer`(person)
- `Dr. Priv.-Doz. Dietmar Aydinlik`(person)
- `Dr. Roland Reichl`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Salzburg`(organisation)

**Example 93** (doc_id: `deanon_260716_TRAIN/2Ob180_21s`) (sent_id: `deanon_260716_TRAIN/2Ob180_21s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden sowie den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Ing. Serge Keilacker, vertreten durch Dr. Alexander Bosio, Rechtsanwalt in Zell am See, gegen die beklagten Parteien 1. KzlR Gerhard Baltronat, Bakk. art., und 2. Gerald Povilaitis, MSc, beide vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, wegen 21.376,95 EUR sA und Feststellung (Streitwert: 10.000 EUR), über die Revisionen der klagenden und der zweitbeklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 6. August 2021, GZ 53 R 110/21i-23, womit das Teil- und Teilzwischenurteil des Bezirksgerichts Zell am See vom 6. April 2021, GZ 18 C 892/20z-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen der klagenden und der zweitbeklagten Partei werden zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Veith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Hofrat Dr. Musger`(person)
- `Hofrätin Dr. Solé`(person)
- `Hofräte Dr. Nowotny`(person)
- `MMag. Sloboda`(person)
- `Ing. Serge Keilacker`(person)
- `Dr. Alexander Bosio`(person)
- `KzlR Gerhard Baltronat, Bakk. art.`(person)
- `Gerald Povilaitis, MSc`(person)
- `Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH`(organisation)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Zell am See`(organisation)

**Example 94** (doc_id: `deanon_260716_TRAIN/2Ob189_17h`) (sent_id: `deanon_260716_TRAIN/2Ob189_17h_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofrätinnen und Hofräte Dr. Fichtenau, Dr. Musger, Dr. E. Solé und Dr. Nowotny als weitere Richter in der Pflegschaftssache des mj Sabrina Bauers, geboren am 9. Juli 2012, über den außerordentlichen Revisionsrekurs der Mutter Chiara Goudsmid, vertreten durch MMag. Dr. Franz Stefan Pechmann, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. August 2017, GZ 44 R 391/17a-199, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG).

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. Dr. Lovrek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Fichtenau`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Sabrina Bauers`(person)
- `9. Juli 2012`(date)
- `Chiara Goudsmid`(person)
- `MMag. Dr. Franz Stefan Pechmann`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Grohmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda`(person)
- `Dr. Kikinger`(person)
- `Hofrätin Mag. Fitz`(person)
- `Denise Markstaler`(person)
- `Weber Rechtsanwälte GmbH`(organisation)
- `Rut Adamheit`(person)
- `BEURLE Rechtsanwälte GmbH & Co KG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 96** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Veith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Hofrat Dr. Musger`(person)
- `Hofrätin Dr. Solé`(person)
- `Hofräte Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Haßtenteufel Umwelt GmbH & Co KG`(organisation)
- `Peter Zauner Weg 324, 5273 Wesen, Österreich`(address)
- `Gheneff - Rami - Sommer Rechtsanwälte OG`(organisation)
- `Isaak Tomzak`(person)
- `Dr. Maximilian Motschiunig`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 97** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Grohmann`
- `Gmb` — similar text (different position): `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hofräte MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Hofrätin Mag. Fitz`(person)
- `Dagobert Drügemöller`(person)
- `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH`(organisation)
- `Rosalinde Nölker`(person)
- `Mag. Simon Wallner Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/2Ob216_18f`) (sent_id: `deanon_260716_TRAIN/2Ob216_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Sandra Olbrechts, vertreten durch Mag. Martin Paar und Mag. Hermann Zwanzger, Rechtsanwälte in Wien, gegen die beklagte Partei Inn Kraftfengart AG, Julius Jax-Gasse 64, 4623 Waldenberg, Österreich, vertreten durch Dr. Helmut Weinzettl, Rechtsanwalt in Wiener Neustadt, wegen 14.817,50 EUR sA, über die Revisionen beider Parteien gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Juni 2018, GZ 18 R 11/18y-64, mit welchem das Urteil des Bezirksgerichts Baden vom 28. Dezember 2017, GZ 7 C 1010/15x-58, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Veith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Hofrat Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Hofräte Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Sandra Olbrechts`(person)
- `Mag. Martin Paar`(person)
- `Mag. Hermann Zwanzger`(person)
- `Inn Kraftfengart AG`(organisation)
- `Julius Jax-Gasse 64, 4623 Waldenberg, Österreich`(address)
- `Dr. Helmut Weinzettl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Bezirksgerichts Baden`(organisation)

**Example 99** (doc_id: `deanon_260716_TRAIN/2Ob57_20a`) (sent_id: `deanon_260716_TRAIN/2Ob57_20a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Elina Faber, vertreten durch Dr. Gernot Lehner, Rechtsanwalt in Neumarkt im Hausruckkreis, gegen die beklagten Parteien 1. Chiara Prukop, 2.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Veith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Hofrat Dr. Musger`(person)
- `Hofrätin Dr. Solé`(person)
- `Hofräte Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Elina Faber`(person)
- `Dr. Gernot Lehner`(person)
- `Chiara Prukop`(person)

</details>

---

</details>

---

