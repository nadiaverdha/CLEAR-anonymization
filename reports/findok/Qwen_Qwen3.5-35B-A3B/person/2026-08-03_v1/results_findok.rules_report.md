# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-03T16:53:42.951601

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-03_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 0 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2515 |
| Validation documents | 629 |
| Test documents | 791 |
| Train sentences | 4346 |
| Validation sentences | 1075 |
| Test sentences | 91812 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 30 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | True |
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

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | 94 |
| Best Batch F1 | 0.5612403100775194 |
| Best Rules Serialized | [{'id': 'fa663fdd', 'name': 'MedR Title Name', 'description': "Specifically matches person names following the 'MedR' title, ensuring the full name is captured including preceding titles like 'RgR' or 'DDr'.", 'format': 'regex', 'content': '\\b((?:RgR\\s+|DDr\\s+|Mag\\.\\s+|Dr\\.\\s+|Univ\\.-Prof\\.(?:in\\s+)?\\s+)?MedR\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s+-\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s*,\\s*[A-Z]{2,})?(?:\\s+(?:MSc|MBA|LL\\.M|LL\\.B|B\\.Sc|B\\.A|B\\.Ed|MA|LLB|B\\.Sc|B\\.A|B\\.Ed|BEd|B\\.Ed|Bakk\\.\\s+techn\\.|Bakk\\.\\s+iur\\.|Bakk\\.\\s+rer\\.\\s+\\w+)*)(?=[\\s,;\\n]|$))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '633e173e', 'name': 'Name Born Context', 'description': "Matches person names following 'geboren am' or 'geb.' to capture names in birth contexts, ensuring the name follows the date context.", 'format': 'regex', 'content': '(?:geboren\\s+am\\s+|geb\\.\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s+-\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*)(?=[\\s,;\\n]|$|\\s+KG|\\s+Bf\\.|\\s+\\.\\s*$|\\s+\\(|\\s+\\))', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'c15108ab', 'name': 'Bf Parenthetical Name', 'description': "Captures person names following 'Bf.' or 'Bf' in parenthetical definitions (e.g., 'Bf. genannt) Name' or 'Bf) Name').", 'format': 'regex', 'content': '\\b(?:Bf\\.|Bf)\\s*(?:genannt\\s*)?\\)?\\s*([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '8ba4434c', 'name': 'Frau Title Name Pattern', 'description': "Captures person names following 'Frau', strictly requiring a valid name pattern immediately after and stopping at non-name characters to avoid false positives like 'Frau Grundsteuer'.", 'format': 'regex', 'content': '\\bFrau\\s+([A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*(?:\\s+(?:LL\\.B\\.?\\s+LL\\.M\\.?|LL\\.M\\.?\\s+LL\\.B\\.?|B\\.Sc|B\\.A|B\\.Ed|MA|LLB|BEd|B\\.Ed|Bakk\\.\\s+techn\\.|Bakk\\.\\s+iur\\.|Bakk\\.\\s+rer\\.\\s+\\w+|MSc|MBA|Dr\\.[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|Mag\\.[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|Univ\\.-Prof\\.(?:in)?[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|Priv\\.-Doz\\.(?:in)?[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|Hon\\.-Prof\\.(?:in)?[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|StR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|KommR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|\\u00d6kR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|VetR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|Ing\\.[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|OSR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|OMedR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|KzlR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|RgR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|Techn\\s+R[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*|MedR[\\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*))?)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'fa0b9fa1', 'name': 'Herr Title Name Pattern', 'description': "Captures person names following 'Herr', ensuring the full name is captured including suffixes and complex titles like 'Techn R OMedR'. Handles cases like 'Herr KindB'.", 'format': 'regex', 'content': '\\bHerr\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+(?:di|de|der|von|zu|van|vanden|ter|ter\\s+|da|della|del|des|dos|da\\s+|di\\s+|de\\s+|der\\s+|von\\s+|zu\\s+|van\\s+|vanden\\s+|ter\\s+|ter\\s+|da\\s+|della\\s+|del\\s+|des\\s+|dos\\s+|da\\s+))*[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s+-\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s*,?\\s*(?:LL\\.B|LL\\.M|LLB|MSc|MBA|B\\.Sc|B\\.A|B\\.Ed|MA|BEd|Bakk\\.\\s+techn\\.|Bakk\\.\\s+iur\\.|Bakk\\.\\s+rer\\.\\s+\\w+)*))(?=[\\s,;\\n]|$|\\s+KG|\\s+Bf\\.|\\s+\\.\\s*$|\\s+\\(|\\s+\\))', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '391d7a7e', 'name': 'Single Letter Name Pattern', 'description': "Captures anonymized single-letter names (e.g., 'M. Mayr') when preceded by titles or in specific contexts, ensuring the full title+initial is captured.", 'format': 'regex', 'content': '\\b((?:Dr\\.|Mag\\.|KommR|StR|Priv\\.-Doz\\.|Univ\\.-Prof\\.|Hon\\.-Prof\\.|Ri\\.|R\\.\\s+)([A-Z]\\.)\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+))(?=[\\s,;\\n]|$|\\s+KG|\\s+Bf\\.|\\s+\\.\\s*$|\\s+\\(|\\s+\\))', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'da791678', 'name': 'Anonymized Doctor Pattern', 'description': "Captures anonymized doctor names like 'Dr. B.' or 'Dr. A.' which are common in legal texts but missed by standard name patterns.", 'format': 'regex', 'content': '\\bDr\\.\\s+[A-Z]\\.', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '09f93e48', 'name': 'Long Academic Title Name', 'description': 'Captures specific long academic titles and names that are often standalone or preceded by prepositions, generalizing the pattern to include suffixes.', 'format': 'regex', 'content': '\\b(?:Valentina Kulbarsch, Bakk\\. rer\\. nat\\.|Ing\\. StR Dipl\\. Kff\\. Sonja Bonholt|Hon\\.-Prof\\.in Delila Luether|Dr\\. Jonathan M\\u00fctterthies|Ma(?:g\\.a (?:Natalie Schreckhas|Katharina Fisera)|ja Schlagbaum)|Karina Tkachenko, BA|Dalibor Czeschelski|StR Marion Dallmeir|Dr\\. Anna Radschek|Dr\\. Peter Steurer|Roxana Bendhaack|Fiona Clesen|Dr\\. B\\.)', 'priority': 11, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '66b7aa44', 'name': 'Complainant Name Pattern', 'description': "Captures person names following 'in der Beschwerdesache', handling multi-word names (e.g., 'di Francesco') and academic suffixes.", 'format': 'regex', 'content': 'in\\s+der\\s+Beschwerdesache\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+(?:di|de|der|von|zu|van|vanden|ter|ter\\s+|da|della|del|des|dos|da\\s+|di\\s+|de\\s+|der\\s+|von\\s+|zu\\s+|van\\s+|vanden\\s+|ter\\s+|ter\\s+|da\\s+|della\\s+|del\\s+|des\\s+|dos\\s+|da\\s+))*[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s+-\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*(?:\\s+(?:LL\\.B\\.\\s+LL\\.M\\.|LL\\.M\\.\\s+LL\\.B\\.|LL\\.B\\.\\s+LLB|LLB|LL\\.M\\.|MSc|MBA|MAS|BA|B\\.Sc|B\\.A|B\\.Ed|MA|BEd|Bakk\\.\\s+techn\\.|Bakk\\.\\s+iur\\.|Bakk\\.\\s+rer\\.\\s+\\w+)*))(?=[\\s,;\\n]|$|\\s+KG|\\s+Bf\\.|\\s+\\.\\s*$|\\s+\\(|\\s+\\))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '81012d3c', 'name': 'Specific Academic Title Pattern (Mag.a/Dr.in)', 'description': "Captures person names with German academic titles, strictly stopping before common legal nouns. Updated to include suffixes like ', BA', ', BSc', ', Bakk.' and handle complex title chains.", 'format': 'regex', 'content': '\\b((?:Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|Mag\\.|Mag\\.-Doz\\.|Dr\\.|Dr\\.in|Hon\\.-Prof\\.|Hon\\.-Prof\\.in|RgR|DDr\\.|DDr\\.in|OStR|Dipl\\. Kff\\.|Ing\\.|KommR|RA|VetR|Techn\\. R)\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00DC]+)*(?:\\s*,\\s*(?:BA|BSc|B\\.Sc|B\\.A\\.|Bakk\\. rer\\. nat\\.|Dipl\\.|Ing\\.))?)(?![\\s,]*Vollmacht|\\s+\\d|\\s+\\.|\\s+\\)|\\s+\\n|$)', 'priority': 15, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '9f823d7f', 'name': 'Judge Name Context Pattern', 'description': "Captures person names immediately following 'Richter' or 'Richterin', ensuring the full name including titles and suffixes is captured.", 'format': 'regex', 'content': '(?:Richter|Richterin)\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00DC]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00DC]+)*(?:\\s*,\\s*(?:BA|BSc|B\\.Sc|B\\.A\\.|Bakk\\. rer\\. nat\\.|Dipl\\.|Ing\\.|B\\.Sc\\.))?)(?=\\s*,|\\s+\\d|\\s+\\.|\\s+\\)|\\s+\\n|$)', 'priority': 13, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '20406141', 'name': 'Organization Name as Person Pattern', 'description': "Captures names following 'Fußballklub' or 'FC' which are misidentified as organizations but are person entities in this specific legal context (e.g., Verona Kemper).", 'format': 'regex', 'content': '(?:Fu\\u00dfballklub|FC)\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)*)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'e714b19d', 'name': 'Title Preceded Name Pattern', 'description': "Captures names preceded by 'RA' (Rechtsanwalt) or 'Dr.' without the academic suffix, ensuring the full name is captured.", 'format': 'regex', 'content': '\\b((?:RA|Dr\\.)\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00dc]+)+)(?![\\s,]*Vollmacht)', 'priority': 12, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '371c3c3b', 'name': 'Non-Academic Title Name Pattern', 'description': "Captures names preceded by specific non-academic professional titles like 'VetR' (Veterinär) or 'Techn R' (Technischer Rat) which are not covered by the academic title rule.", 'format': 'regex', 'content': '\\b((?:VetR|Techn\\sR|RA\\s|Dr\\.\\s|Mag\\.\\s|Hon\\.-Prof\\.in\\s|Univ\\.-Prof\\.in\\s|Priv\\.-Doz\\.\\s|Dr\\.in\\s|Mag\\.in\\s|Mag\\.a\\s)\\s+[A-Z][a-zäöüßÄÖÜ]+(?:\\s+[A-Z][a-zäöüßÄÖÜ]+)*)', 'priority': 14, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '80f93592', 'name': 'Complainant Name Context Pattern', 'description': "Captures person names following 'in der Beschwerdesache', strictly requiring a title or a full name pattern with suffixes (e.g., ', BA') to avoid partial matches or false positives on legal nouns.", 'format': 'regex', 'content': 'in\\s+der\\s+Beschwerdesache\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00DC]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df\\u00c4\\u00d6\\u00DC]+)*(?:\\s*,\\s*(?:BA|BSc|B\\.Sc|B\\.A\\.|Bakk\\. rer\\. nat\\.|Dipl\\.|Ing\\.|B\\.Sc\\.))?)(?=\\s*,|\\s+\\d|\\s+\\.|\\s+\\)|\\s+\\n|$)', 'priority': 14, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.6% |
| True Positives | 1086 |
| False Positives | 769 |
| False Negatives | 929 |
| Total Gold Entities | 2015 |
| Micro Precision | 58.5% |
| Micro Recall | 53.9% |
| Micro F1 | 56.1% |
| Macro F1 | 56.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Long Academic Title Name` | 2.1% | 100.0% | 1.0% | 21 | 21 | 0 |
| `Complainant Name Context Pattern` | 31.3% | 92.5% | 18.9% | 411 | 380 | 31 |
| `Title Preceded Name Pattern` | 15.7% | 76.5% | 8.7% | 230 | 176 | 54 |
| `Specific Academic Title Pattern (Mag.a/Dr.in)` | 43.9% | 67.0% | 32.7% | 982 | 658 | 324 |
| `Non-Academic Title Name Pattern` | 2.2% | 63.9% | 1.1% | 36 | 23 | 13 |
| `Frau Title Name Pattern` | 2.6% | 27.7% | 1.4% | 101 | 28 | 73 |
| `Anonymized Doctor Pattern` | 0.5% | 10.0% | 0.2% | 50 | 5 | 45 |
| `MedR Title Name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Name Born Context` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Bf Parenthetical Name` | 0.0% | 0.0% | 0.0% | 295 | 0 | 295 |
| `Herr Title Name Pattern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Single Letter Name Pattern` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Complainant Name Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Judge Name Context Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Organization Name as Person Pattern` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Long Academic Title Name`

**F1:** 0.021 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `09f93e48`  
**Description:**
Captures specific long academic titles and names that are often standalone or preceded by prepositions, generalizing the pattern to include suffixes.

**Content:**
```
\b(?:Valentina Kulbarsch, Bakk\. rer\. nat\.|Ing\. StR Dipl\. Kff\. Sonja Bonholt|Hon\.-Prof\.in Delila Luether|Dr\. Jonathan M\u00fctterthies|Ma(?:g\.a (?:Natalie Schreckhas|Katharina Fisera)|ja Schlagbaum)|Karina Tkachenko, BA|Dalibor Czeschelski|StR Marion Dallmeir|Dr\. Anna Radschek|Dr\. Peter Steurer|Roxana Bendhaack|Fiona Clesen|Dr\. B\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.010 | 0.021 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 21 | 0 | 1922 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Danelzik` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/132478.1`) (sent_id: `deanon_BFG_TRAIN/132478.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Juri Weich, Spitalanger 19, 3910 Ratschenhof, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 9. März 2015 betreffend Einkommensteuervorauszahlungen 2015 zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Weich` (person)
- `Spitalanger 19, 3910 Ratschenhof, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ernestine Schittenhelm, Clementinengasse 29, 8692 Krampen, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ernestine Schittenhelm` (person)
- `Clementinengasse 29, 8692 Krampen, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 3** (doc_id: `deanon_BFG_TRAIN/132878.1`) (sent_id: `deanon_BFG_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Sabrina Boger, Heugraben 15, 6233 Mariatal, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sabrina Boger` (person)
- `Heugraben 15, 6233 Mariatal, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/133301.1`) (sent_id: `deanon_BFG_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Francois Stürnkorb, Lobisser Straße 37, 4153 Schönberg, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Stürnkorb` (person)
- `Lobisser Straße 37, 4153 Schönberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/136317.1`) (sent_id: `deanon_BFG_TRAIN/136317.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Gerlinde Schönheinz, Leinburger Straße 42B, 5113 Aglassing, Österreich, betreffend die Beschwerden vom 30. August 2019, 30. September  2019 und 31. September 2019 gegen die Bescheide des damaligen Finanzamtes 3/6/7/11/15  Schwechat Gerasdorf vom 25. Juli 2019 zu Steuernummer 63-118/1188  betreffend  Einkommensteuer 2012, sowie Umsatz-und Einkommensteuer 2014 bis 2017 beschlossen:  Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerlinde Schönheinz` (person)
- `Leinburger Straße 42B, 5113 Aglassing, Österreich` (address)
- `63-118/1188` (tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/137567.1`) (sent_id: `deanon_BFG_TRAIN/137567.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Cassandra Franzas, Ketzerhub 14, 4730 Auwies, Österreich, vertreten durch Rudolf Peter, Esteplatz 3 Tür 9, 1030 Wien,  betreffend Beschwerde vom 20. Mai 2016 gegen die Bescheide des damaligen Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 21. April 2016 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) für 2009, 2010, 2012 und 2013, sowie den Bescheid vom 2.  Oktober 2019 betreffend Umsatzsteuer 2015, Steuernummer 57-376/4892, beschlossen:  I. a)

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cassandra Franzas` (person)
- `Ketzerhub 14, 4730 Auwies, Österreich` (address)
- `Rudolf Peter` (person)
- `57-376/4892` (tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138051.1`) (sent_id: `deanon_BFG_TRAIN/138051.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  OStR Lukas Janowitsch, Waizbauerweg 68, 9620 Presseggen, Österreich, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich über die Erklärung zur Arbeitnehmerveranlagung 2021, beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Lukas Janowitsch` (person)
- `Waizbauerweg 68, 9620 Presseggen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/138967.1`) (sent_id: `deanon_BFG_TRAIN/138967.1_137`)


Daran können  auch die Bestätigungen der Erlöse der drei Hauptkunden in Deutschland nichts ändern, zum  einen, da dadurch nicht ausgeschlossen wird, dass auch an andere Kunden Umsätze getätigt  wurden (worauf auch die mit „verschiedene Kunden" und „Dr. B." benannten Konten schließen  lassen), zum anderen war eine exakte Zuordnung der Rechnungsnummern bzw. Rechnungen  nicht möglich.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/141691.1`) (sent_id: `deanon_BFG_TRAIN/141691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Verwaltungsstraf- sache gegen Cornelia Große-Beck, Dobretshofen 10, 4760 Großprambach, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde der Beschuldigten vom 3. Juli 2023 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Juni 2023, GZ. MA67/Zahl/2022, zu Recht  erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Große-Beck` (person)
- `Dobretshofen 10, 4760 Großprambach, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_TRAIN/142516.1`) (sent_id: `deanon_BFG_TRAIN/142516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der  Verwaltungsstrafsache gegen Priv.-Doz. Karlheinz Barnekow, Seltschacher Straße 9I, 9585 Techanting, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 18. August 2023 gegen  das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Juli 2023, GZ.  MA67/236700356855/2023, zu Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde insofern Folge gegeben als gemäß § 38 VwGVG iVm  § 45 Abs. 1 Z. 4 VStG von der Verhängung einer Strafe abgesehen und der  beschwerdeführenden Partei unter Hinweis auf die Rechtswidrigkeit ihres Verhaltens eine  Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Karlheinz Barnekow` (person)
- `Seltschacher Straße 9I, 9585 Techanting, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_TRAIN/143056.1`) (sent_id: `deanon_BFG_TRAIN/143056.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Melinda Ade, Nachdemsee 10, 9322 Micheldorf, Österreich  vertreten durch die Hon.-Prof.in Erika Opdenhövel  Steuerberatung Werkval-Medien GMBH, über die  Beschwerde gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt Österreich)  vom 25. November 2019 betreffend Einkommensteuer 2018, 54-549/3530, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melinda Ade` (person)
- `Nachdemsee 10, 9322 Micheldorf, Österreich` (address)
- `Hon.-Prof.in Erika Opdenhövel` (person)
- `Werkval-Medien GMBH` (organisation)
- `Finanzamt Österreich` (organisation)
- `54-549/3530` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/144349.1`) (sent_id: `deanon_BFG_TRAIN/144349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  VetR Marlies Thalmayr, Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom 6. Februar  2024 gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2024 betreffend  Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 01.12.2022 bis  30.06.2023, Steuernummer 88-272/3661, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Marlies Thalmayr` (person)
- `Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `88-272/3661` (tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/144505.1`) (sent_id: `deanon_BFG_TRAIN/144505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Gabriele Hattendorff, Trautenfels 55, 4224 Altenhaus, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum 01.12.2022  bis 30.06.2023, Steuernummer 59-032/8627, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gabriele Hattendorff` (person)
- `Trautenfels 55, 4224 Altenhaus, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `59-032/8627` (tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/144827.1`) (sent_id: `deanon_BFG_TRAIN/144827.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rainer Weinschenk, Streitmayerweg 33C, 8263 Radersdorf, Österreich, vertreten durch Meissner & Passin Rechtsanwalts GmbH,  Himmelpfortgasse 17/14, 1010 Wien, betreffend Beschwerde vom 15. Juni 2022 gegen den  Bescheid des Magistratsabteilung 6, Referat Landes- und Gemeindeabgaben, vom 4. März 2022  betreffend Wettterminalabgabe für Mai bis Dezember 2017, GZ MA 6/ARL – 551965/2018-14,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rainer Weinschenk` (person)
- `Streitmayerweg 33C, 8263 Radersdorf, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/145612.1`) (sent_id: `deanon_BFG_TRAIN/145612.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pagitsch, der  Richterin Dr. Anna Radschek sowie die fachkundigen Laienrichter KR Ing. Hans Eisenkölbl und  Mag. Michael Heumesser in der Beschwerdesache Laura Kaplaner, Zehetmayrgut 160, 4710 Niederweng, Österreich, vertreten durch  APP Steuerberatung GmbH, Schenkenstraße 4 / 6.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KR Ing. Hans Eisenkölbl` (person)
- `Mag. Michael Heumesser` (person)
- `Laura Kaplaner` (person)
- `Zehetmayrgut 160, 4710 Niederweng, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/145630.1`) (sent_id: `deanon_BFG_TRAIN/145630.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde der   Lisa Firneisz, Färbereigasse 23, 6682 Vils, Österreich, vom 23. Juli 2024, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 15. Juli 2024, GZ. MA67/GZ/2024, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt  der Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  Landesgesetzblatt für Wien Nr. 9/2006 in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als gemäß § 45 Abs. 1  VStG von der Verhängung einer Strafe abgesehen und der Beschwerdeführerin unter Hinweis  auf die Rechtswidrigkeit ihres Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lisa Firneisz` (person)
- `Färbereigasse 23, 6682 Vils, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/146687.1`) (sent_id: `deanon_BFG_TRAIN/146687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Amy Bayrakcioglu, Bakk. phil., Badnerstraße 75, 9423 Hofwiesen, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Österreich  vom 11. November 2021 betreffend Einkommensteuer 2019, 35-160/3790, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amy Bayrakcioglu, Bakk. phil.` (person)
- `Badnerstraße 75, 9423 Hofwiesen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `35-160/3790` (tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_526`)


Ebenso konnte aus dem Belegmaterial (OZ. 77) entnommen werden, dass die Bf. zahlreiche  Facharztbesuche, Physiotherapeuten, Heilpraktiker, ärztliche Labors (Re v. 22.8.2014,  1.10.2014 Dr. M., 30.10.2014 Dr. Sch., 30.10.2014 Dr. Sz., 16.1.2015 Dr. E., 26.1.2015 Dr. W.,  4.3.2015 Diagnostik M., 28.8.2015 Heilpraktikerin H., 14.12.2015 Heilpraktikerin H., 17.12.2015  Labor Dres., 30.12.2015 Heilpraktikerin H., 29.11.2016 Dr. E., 10.2.2017 Zahnarzt 4 Sitzungen,  21.3.2017 Facharzt 4 Sitzungen, 11.8.2017 Zahnarzt, 12.10.2017 Dr. E., 27.12.2017 Dr. B. 2  Sitzungen, absolviert hat.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Missed by this rule (FN):**

- `M.` (person)
- `M.` (person)

**Example 19** (doc_id: `deanon_BFG_TRAIN/148214.1`) (sent_id: `deanon_BFG_TRAIN/148214.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Renate Kukulys, Parisdorfer Straße 53, 8490 Pfarrsdorf, Österreich, über die Beschwerde vom 9. August 2023 gegen den Bescheid des  Finanzamtes Österreich vom 19. Juli 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 73-183/8909, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Renate Kukulys` (person)
- `Parisdorfer Straße 53, 8490 Pfarrsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `73-183/8909` (tax_number)

**Example 20** (doc_id: `deanon_BFG_TRAIN/149749.1`) (sent_id: `deanon_BFG_TRAIN/149749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Heidemarie Zangel, Furtmüllerstraße 66, 5142 Hehenberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Österreich  betreffend Einkommensteuer 2019 und 2020, 08-156/6554, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heidemarie Zangel` (person)
- `Furtmüllerstraße 66, 5142 Hehenberg, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `08-156/6554` (tax_number)

</details>

---

## `Complainant Name Context Pattern`

**F1:** 0.313 | **Precision:** 0.925 | **Recall:** 0.189  

**Format:** `regex`  
**Rule ID:** `80f93592`  
**Description:**
Captures person names following 'in der Beschwerdesache', strictly requiring a title or a full name pattern with suffixes (e.g., ', BA') to avoid partial matches or false positives on legal nouns.

**Content:**
```
in\s+der\s+Beschwerdesache\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+)*(?:\s*,\s*(?:BA|BSc|B\.Sc|B\.A\.|Bakk\. rer\. nat\.|Dipl\.|Ing\.|B\.Sc\.))?)(?=\s*,|\s+\d|\s+\.|\s+\)|\s+\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.925 | 0.189 | 0.313 | 411 | 380 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 380 | 31 | 1633 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Janis Forch, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Forch` | `Janis Forch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128942.1`) (sent_id: `deanon_BFG_TRAIN/128942.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Julia Potthöfer, Hofmannstraße 41, 9300 Tschirnig, Österreich, vertreten durch Vertreter, Vertreter Adresse, über die Beschwerde vom 27. März 2014  gegen den Bescheid des Finanzamtes Graz-Stadt vom 24. Februar 2014 betreffend Aufhebung  des Bescheides über die Umsatzsteuer 2010, Steuernummer 58-698/6537, zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julia Potthöfer` | `Julia Potthöfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hofmannstraße 41, 9300 Tschirnig, Österreich` (address)
- `58-698/6537` (tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128975.1`) (sent_id: `deanon_BFG_TRAIN/128975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Rita Zwirner,  Bodenring 61, 3261 Windpassing, Österreich, vertreten durch Wijnkamp Advocatuur/Advokatur GmbH, Sirapuit 7, 6460  Imst, und Prodinger & Partner Wirtschaftstreuhand-Steuerberatungs GmbH & Co KG,  Prof.Ferry Porsche Straße 28, 5700 Zell am See, über die Beschwerde vom 7. Februar 2018  gegen den Bescheid des Finanzamtes St. Johann Tamsweg Zell am See vom 21. Dezember 2016  betreffend Umsatzsteuer 2006, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rita Zwirner` | `Rita Zwirner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bodenring 61, 3261 Windpassing, Österreich` (address)
- `Wijnkamp Advocatuur/Advokatur GmbH` (organisation)
- `Imst, und Prodinger & Partner Wirtschaftstreuhand-Steuerberatungs GmbH & Co KG` (organisation)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129005.1`) (sent_id: `deanon_BFG_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Thassilo Trabschuh,  Ernst-Derfeser-Straße 30, 5134 Polzwies, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Thassilo Trabschuh` | `Thassilo Trabschuh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ernst-Derfeser-Straße 30, 5134 Polzwies, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129068.1`) (sent_id: `deanon_BFG_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Jens Spilken, Hillere 22, 8453 Saggau, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-228/4517  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jens Spilken` | `Jens Spilken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Hillere 22, 8453 Saggau, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `69-228/4517` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129071.1`) (sent_id: `deanon_BFG_TRAIN/129071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Edwin Bachmair, Bergliftstraße 479I, 9861 Densdorf, Österreich,  vertreten durch Nepomuk Polcin, Madleinweg 22, 4154 Mollmannsreith, Österreich, über die Beschwerde vom  21. August 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Juli 2019  betreffend Einkommensteuer 2014, Steuernummer ,zu Recht erkannt:   I. Der Beschwerde wird im Umfang der Beschwerdevorentscheidung teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Edwin Bachmair` | `Edwin Bachmair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bergliftstraße 479I, 9861 Densdorf, Österreich` (address)
- `Nepomuk Polcin` (person)
- `Madleinweg 22, 4154 Mollmannsreith, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Lubomir Baltßun` | `Lubomir Baltßun` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129218.1`) (sent_id: `deanon_BFG_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Brian Detloff,  Übersbach 6l, 7540 Großmürbisch, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Brian Detloff` | `Brian Detloff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Übersbach 6l, 7540 Großmürbisch, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129231.1`) (sent_id: `deanon_BFG_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Bartholomäus Malcharzik, Ogugasse 8, 4483 Pirchhorn, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Bartholomäus Malcharzik` | `Bartholomäus Malcharzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Elisabeth Traxler` (person)
- `Ogugasse 8, 4483 Pirchhorn, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Doris Goralik, Baron-Kutschera-Allee 13, 6432 Sautens, Österreich, vertreten durch Stb, Steuerberater Wirtschaftstreuhänder, Baron-Kutschera-Allee 13, 6432 Sautens, Österreich, über die  Beschwerde vom 28. August 2013 gegen den Bescheid des Finanzamtes B vom 23. August  2013, Steuernummer , betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Doris Goralik` | `Doris Goralik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Baron-Kutschera-Allee 13, 6432 Sautens, Österreich` (address)
- `Baron-Kutschera-Allee 13, 6432 Sautens, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Anton Danelzik` | `Anton Danelzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129533.1`) (sent_id: `deanon_BFG_TRAIN/129533.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Erna Ackers, Wollsdorf 52, 9582 Latschach, Österreich, vertreten durch Stb, über die Beschwerde vom 21.12.2012 gegen den Bescheid des  Finanzamtes A vom 13.11.2012, betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Erna Ackers` | `Erna Ackers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wollsdorf 52, 9582 Latschach, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Reinhard Komarova, Gabrielweg 4, 4725 Adelsgrub, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 92-139/9763  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Reinhard Komarova` | `Reinhard Komarova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ralf Schatzl` (person)
- `Gabrielweg 4, 4725 Adelsgrub, Österreich` (address)
- `92-139/9763` (tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Edgar Neidenberger, Nussallee 89, 8143 Unterpremstätten, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Edgar Neidenberger` | `Edgar Neidenberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nussallee 89, 8143 Unterpremstätten, Österreich` (address)
- `DI Heinrich Richter Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129696.1`) (sent_id: `deanon_BFG_TRAIN/129696.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gabriele Roggensack, Frimmelgasse 29, 4870 Maulham, Österreich, über die Beschwerde vom 2. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 7. August 2019 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe für das Kind x im Zeitraum vom 01.07.2014 bis zum 30.09.2016 Recht erkannt:   Der Beschwerde wird gemäß § 279 teilweise BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gabriele Roggensack` | `Gabriele Roggensack` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frimmelgasse 29, 4870 Maulham, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129733.1`) (sent_id: `deanon_BFG_TRAIN/129733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Wilfried Wedral  in der Beschwerdesache Ramona Goedeken,  Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich, vertreten durch Union TAX&LAW, Donau-City-Straße 7, DV Tower/30th floor,  1220 Wien, über die Beschwerde vom 16. April 2019 gegen den Bescheid des Finanzamtes  Innsbruck vom 19. März 2019 betreffend Familienbeihilfe (Ausgleichszahlung) für die Monate  Jänner 2015 bis Dezember 2017, [Ordnungsbegriff],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ramona Goedeken` | `Ramona Goedeken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Wilfried Wedral` (person)
- `Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129828.1`) (sent_id: `deanon_BFG_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Pascal Beerlage, Tannwaldweg 35L, 9133 Jerischach, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 13-489/9399  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Pascal Beerlage` | `Pascal Beerlage` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Tannwaldweg 35L, 9133 Jerischach, Österreich` (address)
- `Dr. Helmut Herbert Moritz` (person)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `13-489/9399` (tax_number)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129907.1`) (sent_id: `deanon_BFG_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. R. in der Beschwerdesache Zarin Enneken,  Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 90-142/3945  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Zarin Enneken` | `Zarin Enneken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. R.` (person)
- `Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich` (address)
- `90-142/3945` (tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Shoshana Schweinforth, Brenggenalm 15, 8551 Gieselegg, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 78-461/2049  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shoshana Schweinforth` | `Shoshana Schweinforth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brenggenalm 15, 8551 Gieselegg, Österreich` (address)
- `78-461/2049` (tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129969.1`) (sent_id: `deanon_BFG_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hilde Heinsohn, Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Hilde Heinsohn` | `Hilde Heinsohn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 20** (doc_id: `deanon_BFG_TRAIN/130024.1`) (sent_id: `deanon_BFG_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Marlon William, J. Ranzoni-Straße 1L, 9554 Reggen, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlon William` | `Marlon William` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `J. Ranzoni-Straße 1L, 9554 Reggen, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 21** (doc_id: `deanon_BFG_TRAIN/130064.1`) (sent_id: `deanon_BFG_TRAIN/130064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Aurelia Heizel, Schifferweg 60, 8463 Kranach, Österreich, vertreten durch Joachim Herbert Aigner, Gewerbepark 1, 4920 Schildorn, über die  Beschwerde vom 23. Februar 2018 gegen den Haftungsbescheid des Finanzamtes Braunau Ried  Schärding vom 24. Jänner 2018, Steuernummer StNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben, der Haftungsbetrag von  4.588,35 € um 2.258,02 € auf den Betrag von 2.330,33 € eingeschränkt und wie folgt  aufgeschlüsselt:   Abgabenart Zeitraum Fälligkeit Betrag in Euro  Umsatzsteuer 03/2016 17.05.2016 16,87  Dienstgeberbeitrag 05/2016 15.06.2016 60,50  Zuschlag zum DB 05/2016 15.06.2016 4,48  Lohnsteuer 05/2016 15.06.2016 25,86  Umsatzsteuer 04/2016 15.06.2016 48,32  Dienstgeberbeitrag 06/2016 15.07.2016 66,69  Zuschlag zum DB 06/2016 15.07.2016 5,34  Lohnsteuer 06/2016 15.07.2016 25,86  Umsatzsteuer 05/2016 15.07.2016 71,65  Säumniszuschlag 1 2016 18.07.2016 24,75  Dienstgeberbeitrag 07/2016 16.08.2016 85,30  Zuschlag zum DB 07/2016 16.08.2016 6,82  1 von 15 Seite 2 von 15

| Predicted | Gold |
|---|---|
| `Aurelia Heizel` | `Aurelia Heizel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schifferweg 60, 8463 Kranach, Österreich` (address)
- `Joachim Herbert Aigner` (person)
- `Finanzamtes Braunau Ried` (organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Julia Schulteß, Anton-Sattler-Gasse 42, 3531 Brand, Österreich, vertreten durch Mag. Anton Heisinger,  Mühlallee 1, 7301 Deutschkreutz, über die Beschwerde vom 29. Februar 2016 gegen den  Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 29. Jänner 2016 betreffend Haftung  gemäß § 99 EStG 1988 für den Zeitraum 2014 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Julia Schulteß` | `Julia Schulteß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Anton-Sattler-Gasse 42, 3531 Brand, Österreich` (address)
- `Mag. Anton Heisinger` (person)

**Example 23** (doc_id: `deanon_BFG_TRAIN/130311.1`) (sent_id: `deanon_BFG_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Juliana Cano, Schreier 19, 5121 Ölling, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Zlatan Gemünd  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juliana Cano` | `Juliana Cano` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schreier 19, 5121 Ölling, Österreich` (address)
- `Zlatan Gemünd` (person)

**Example 24** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Christoph Mehlbeer` | `Christoph Mehlbeer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schötz Gasse 45, 7434 Holzschlag, Österreich` (address)
- `Margarete Wiepking` (person)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Esmeralda Lubert, Kaschlgasse 9, 3100 Witzendorf, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Esmeralda Lubert` | `Esmeralda Lubert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Kaschlgasse 9, 3100 Witzendorf, Österreich` (address)
- `Sigrid Lamböck` (person)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130367.1`) (sent_id: `deanon_BFG_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Petra Ullemeyer, Mariexner Straße 8, 3141 Rassing, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Petra Ullemeyer` | `Petra Ullemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Mariexner Straße 8, 3141 Rassing, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/130407.1`) (sent_id: `deanon_BFG_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Emma Sebestik, Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Emma Sebestik` | `Emma Sebestik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich` (address)
- `Harald Schmidt` (person)
- `Finanzamtes Spittal Villach` (organisation)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Schulwiesen 13, 4203 Stratreith, Österreich` (address)
- `Mag. Margot Artner` (person)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Danzfuss, BSc` | `Marlies Danzfuss, BSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/124843.1`) (sent_id: `deanon_BFG_TRAIN/124843.1_0`)


GZ. RV/7100201/2013 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der Beschwerdesache Bf, Adr, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 01.10.2012 (datiert mit 28.9.2012) gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom Juli 2012 betreffend Festsetzung von Normverbrauchsabgabe für Mai 2012 in Höhe von € 19.131,60 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128709.1`) (sent_id: `deanon_BFG_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Felizitas Muendl, Bakk. phil., Güttling 9, 9321 Latschach, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

**False Positives:**

- `Felizitas Muendl` — partial — pred is substring of gold: `Felizitas Muendl, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Felizitas Muendl, Bakk. phil.`(person)
- `Güttling 9, 9321 Latschach, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bauermeister Getränke` — type mismatch — same span as gold: `Bauermeister Getränke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `Mag. Dieter Walla`(person)
- `09-169/6729`(tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129336.1`) (sent_id: `deanon_BFG_TRAIN/129336.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Trafenfen Automotive,  Rebenland-Center-Straße 100, 4793 Ginzldorf, Österreich  vertreten durch Stb., über die Beschwerde vom 17.10.2011 gegen den Bescheid  des Finanzamtes Lilienfeld St. Pölten vom 13.7.2011 betreffend Einkommensteuer 2009 nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Trafenfen Automotive` — type mismatch — same span as gold: `Trafenfen Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Trafenfen Automotive`(organisation)
- `Rebenland-Center-Straße 100, 4793 Ginzldorf, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Helge Reinardy, Bakk. techn., Ganglweg 69, 9535 Penken, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  41-653/0116  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Helge Reinardy` — partial — pred is substring of gold: `Helge Reinardy, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Helge Reinardy, Bakk. techn.`(person)
- `Ganglweg 69, 9535 Penken, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `41-653/0116`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/130559.1`) (sent_id: `deanon_BFG_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Julia Nöllecke  in der Beschwerdesache Esra Leßnick, LLB,  Hackermillerstraße 133, 8940 Döllach, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  06-833/3820, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Esra Leßnick` — partial — pred is substring of gold: `Esra Leßnick, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Julia Nöllecke`(person)
- `Esra Leßnick, LLB`(person)
- `Hackermillerstraße 133, 8940 Döllach, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `06-833/3820`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

</details>

---

## `Title Preceded Name Pattern`

**F1:** 0.157 | **Precision:** 0.765 | **Recall:** 0.087  

**Format:** `regex`  
**Rule ID:** `e714b19d`  
**Description:**
Captures names preceded by 'RA' (Rechtsanwalt) or 'Dr.' without the academic suffix, ensuring the full name is captured.

**Content:**
```
\b((?:RA|Dr\.)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)+)(?![\s,]*Vollmacht)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.765 | 0.087 | 0.157 | 230 | 176 | 54 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 176 | 54 | 1831 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128700.1`) (sent_id: `deanon_BFG_TRAIN/128700.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Imre Schmidl  in der Beschwerdesache [...], [...],  über die Beschwerde vom 12. Februar 2018 gegen den Bescheid des Finanzamtes Lilienfeld St.  Pölten vom 16. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Imre Schmidl` | `Dr. Imre Schmidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128709.1`) (sent_id: `deanon_BFG_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Felizitas Muendl, Bakk. phil., Güttling 9, 9321 Latschach, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Muendl, Bakk. phil.` (person)
- `Güttling 9, 9321 Latschach, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Dr. Gerlinde  Rieser` | `Dr. Gerlinde  Rieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Raphael Skowroneck, MBA` (person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129068.1`) (sent_id: `deanon_BFG_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Jens Spilken, Hillere 22, 8453 Saggau, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-228/4517  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jens Spilken` (person)
- `Hillere 22, 8453 Saggau, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `69-228/4517` (tax_number)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lubomir Baltßun` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129168.1`) (sent_id: `deanon_BFG_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  Dolores Jodjürgis, BA MBA, Feldsiedlung 87, 5242 Obereck, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dolores Jodjürgis, BA MBA` (person)
- `Feldsiedlung 87, 5242 Obereck, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Danelzik` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129520.1`) (sent_id: `deanon_BFG_TRAIN/129520.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Verwaltungsstrafsache  gegen KzlR Wolf Wältl, MBA, Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich, über die Beschwerde des Beschuldigten vom 26. März 2020  gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 10. März 2020, Zahl:  MA67/196700631216/2019, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Wolf Wältl, MBA` (person)
- `Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129555.1`) (sent_id: `deanon_BFG_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache ÖkR Nadine Fritzekötter, Fahnbach 3, 3752 Nonnersdorf, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Nadine Fritzekötter` (person)
- `Fahnbach 3, 3752 Nonnersdorf, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Reinhard Komarova, Gabrielweg 4, 4725 Adelsgrub, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 92-139/9763  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reinhard Komarova` (person)
- `Gabrielweg 4, 4725 Adelsgrub, Österreich` (address)
- `92-139/9763` (tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 11** (doc_id: `deanon_BFG_TRAIN/129828.1`) (sent_id: `deanon_BFG_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Pascal Beerlage, Tannwaldweg 35L, 9133 Jerischach, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 13-489/9399  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |
| `Dr. Helmut Herbert Moritz` | `Dr. Helmut Herbert Moritz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pascal Beerlage` (person)
- `Tannwaldweg 35L, 9133 Jerischach, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `13-489/9399` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Cedric Leutheusser, Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Cedric Leutheusser` (person)
- `Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Dr.in Ljiljana Kos` (person)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Example 15** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

| Predicted | Gold |
|---|---|
| `Dr. Sasan Hamzavi` | `Dr. Sasan Hamzavi` |

**Example 16** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Esmeralda Lubert, Kaschlgasse 9, 3100 Witzendorf, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esmeralda Lubert` (person)
- `Kaschlgasse 9, 3100 Witzendorf, Österreich` (address)
- `Sigrid Lamböck` (person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/130367.1`) (sent_id: `deanon_BFG_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Petra Ullemeyer, Mariexner Straße 8, 3141 Rassing, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Petra Ullemeyer` (person)
- `Mariexner Straße 8, 3141 Rassing, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 19** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 20** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  KzlR Leroy Krätschmar, Hohe Wand-Str. 12, 8345 Krusdorf, Österreich, über die Beschwerde vom 29. Mai 2019 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 30. April 2019 betreffend Rückforderung der  für VN-Sohn NN für den Zeitraum Jänner 2018 bis Dezember 2018 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Leroy Krätschmar` (person)
- `Hohe Wand-Str. 12, 8345 Krusdorf, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 21** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marlies Danzfuss, BSc` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

**Example 22** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Paula Jagiella, Medienpark 18, 3384 Eidletzberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paula Jagiella` (person)
- `Medienpark 18, 3384 Eidletzberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Dr. Elke Hager` | `Dr. Elke Hager` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wladimir Nüssli` (person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/130686.1`) (sent_id: `deanon_BFG_TRAIN/130686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde der  Alana Single, Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich, vom 19. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 17. August 2020, Zahl MA67/Zahl/2019, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alana Single` (person)
- `Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Matthäus Buskens` (person)
- `Edlach 19, 3141 Oberkilling, Österreich` (address)
- `Helmut Binder` (person)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130748.1`) (sent_id: `deanon_BFG_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Valentina Cagli, A. Böhm Gasse 67F, 4310 Oberzirking, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 76-512/9228  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentina Cagli` (person)
- `A. Böhm Gasse 67F, 4310 Oberzirking, Österreich` (address)
- `76-512/9228` (tax_number)

**Example 27** (doc_id: `deanon_BFG_TRAIN/130759.1`) (sent_id: `deanon_BFG_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Justin Feuerheerdt, Naglergasse 6, 4794 Grafendorf, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Justin Feuerheerdt` (person)
- `Naglergasse 6, 4794 Grafendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 28** (doc_id: `deanon_BFG_TRAIN/131365.1`) (sent_id: `deanon_BFG_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Mario Gajewska, Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mario Gajewska` (person)
- `Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 29** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Prof. Gernot Woortmann, Spitzbergweg 116, 3204 Tradigistgegend, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 16-817/8793  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Gernot Woortmann` (person)
- `Spitzbergweg 116, 3204 Tradigistgegend, Österreich` (address)
- `16-817/8793` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/130749.1`) (sent_id: `deanon_BFG_TRAIN/130749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Dr. OStR Benedikt Paszkowiak, Susalitsch 160, 8230 Staudach, Österreich, über die Beschwerde vom 28. Juni 2018 gegen  den Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 19. Juni 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Dr. OStR Benedikt Paszkowiak`(person)
- `Susalitsch 160, 8230 Staudach, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131742.1`) (sent_id: `deanon_BFG_TRAIN/131742.1_9`)


Die beschwerdeführende Partei sei der  Auffassung von Herrn Univ.-Prof. Dr. Reinhold Beiser (SWK 9/2017, 498): „Wenn es zu einer  Betriebsaufgabe kommt, so bleiben die Wertpapiere die vorher für die Ausnutzung eines  Gewinnfreibetrages angeschafft wurden, notwendiges nachträgliches Betriebsvermögen unter  der Voraussetzung, dass sie bis zum Ablauf der Behaltefrist gehalten werden.

**False Positives:**

- `Dr. Reinhold Beiser` — partial — pred is substring of gold: `Univ.-Prof. Dr. Reinhold Beiser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Dr. Reinhold Beiser`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/132030.1`) (sent_id: `deanon_BFG_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Bernadette Birkfeld, Pipitzhof 7, 3388 Knetzersdorf, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Bernadette Birkfeld`(person)
- `Pipitzhof 7, 3388 Knetzersdorf, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/132106.1`) (sent_id: `deanon_BFG_TRAIN/132106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jessica Osborn, Am Richardschacht 28, 2880 Lehen, Österreich, über die Beschwerde vom 5. Dezember 2014  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 6. November 2014 betreffend  Umsatzsteuer und Einkommensteuer 2012 und 2013 sowie gegen den Bescheid des  Finanzamtes Kirchdorf Perg Steyr vom 10. November 2014 betreffend Festsetzung des ersten  Säumniszuschlages von der Umsatzsteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Jessica Osborn`(person)
- `Am Richardschacht 28, 2880 Lehen, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/132731.1`) (sent_id: `deanon_BFG_TRAIN/132731.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat über die Beschwerde vom  11. September 2020 des Beschwerdeführers Sean Mütz, Seßlebene 15, 5661 Rauris, Österreich, vertreten durch die  Dr. Heinz Häupl Rechtsanwalts GmbH, 4865 Nußdorf, Stockwinkl 18, gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 10. August 2020  betreffend Abweisung des Antrages vom 24.07.2020 auf Aufhebung der  Umsatzsteuerbescheide 2011 und 2013 sowie der Einkommensteuerbescheide 2010, 2011  und 2013 gemäß § 299 Abs 1 BAO den Beschluss:      I)

**False Positives:**

- `Dr. Heinz Häupl Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sean Mütz`(person)
- `Seßlebene 15, 5661 Rauris, Österreich`(address)
- `Finanzamt Österreich`(organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Rebecca Woizeschke, Stöcklweg 2, 8632 Wegscheid, Österreich, vertreten durch Dr. Eva Deutsch-Goldoni, Waldwiese 4, 2540 Bad  Vöslau, über die Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 76-599/3261  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Eva Deutsch` — partial — pred is substring of gold: `Dr. Eva Deutsch-Goldoni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Aigner`(person)
- `Rebecca Woizeschke`(person)
- `Stöcklweg 2, 8632 Wegscheid, Österreich`(address)
- `Dr. Eva Deutsch-Goldoni`(person)
- `76-599/3261`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/133151.1`) (sent_id: `deanon_BFG_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Leila Togan  in der   Beschwerdesache Pia Minarsch, Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Michael Jöstl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Leila Togan`(person)
- `Pia Minarsch`(person)
- `Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/133689.1`) (sent_id: `deanon_BFG_TRAIN/133689.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin MMag.Dr. Ingrid Fehrer im  Beschwerdeverfahren über die Beschwerde der RgR Hartwig Mickus, Wetzles 3, 4323 Pilgram, Österreich, vom  3. August 2020 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 14. Mai  2020, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer  55-808/0270, mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom  3. August 2020 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2017 vom  14. Mai 2020 ein Vorlageantrag nicht eingebracht.

**False Positives:**

- `Dr. Ingrid Fehrer` — partial — pred is substring of gold: `MMag.Dr. Ingrid Fehrer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag.Dr. Ingrid Fehrer`(person)
- `RgR Hartwig Mickus`(person)
- `Wetzles 3, 4323 Pilgram, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `55-808/0270`(tax_number)
- `Bundesfinanzgerichts`(organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/134395.1`) (sent_id: `deanon_BFG_TRAIN/134395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Alice Märcklin, Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH,  Gauermanngasse 2-4, 1010 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich)  vom 25. Oktober 2018 betreffend Einkommensteuer 2016, Steuernummer 12-225/3285  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Erich Loitzl Straße` — partial — pred is substring of gold: `Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Alice Märcklin`(person)
- `Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Finanzamt Österreich`(organisation)
- `12-225/3285`(tax_number)

**Example 9** (doc_id: `deanon_BFG_TRAIN/134768.1`) (sent_id: `deanon_BFG_TRAIN/134768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache James Johanntokrax, Wandeckstraße 6, 4730 Aschach, Österreich, vertreten durch Mag. Manuela Henrich, Dr. Karl Renner Str. 5, 2560 Berndorf, über die  Beschwerde vom 28.06.2019  gegen den Bescheid des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich) vom 27. Mai 2019 betreffend Wiedereinsetzung in den vorigen Stand  nach Durchführung einer mündlichen Verhandlung betreffend Einkommensteuer für das Jahr  2012 Steuernummer 68-133/5727  zu Recht erkannt:   Die Beschwerde gegen die Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Karl Renner Str` — partial — gold is substring of pred: `Dr. Karl Renner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `James Johanntokrax`(person)
- `Wandeckstraße 6, 4730 Aschach, Österreich`(address)
- `Mag. Manuela Henrich`(person)
- `Dr. Karl Renner`(person)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `68-133/5727`(tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/135112.1`) (sent_id: `deanon_BFG_TRAIN/135112.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Zlatan Deisen  in der Beschwerdesache des  Prof. Richard Paulick, Scharmühlwinkel 13, 3144 Baumgarten, Österreich, über 1) die Beschwerde vom 27.9.2017 gegen den Bescheid des  Finanzamtes Bruck Leoben Mürzzuschlag (nunmehr Finanzamt Österreich) vom 4.9.2017  betreffend Umsatzsteuer 2015 sowie über 2) die Beschwerde vom 7.9.2018 gegen den  Bescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 21.8.2018 betreffend Abweisung  von Anträgen auf Aufhebung der Bescheide hinsichtlich Umsatzsteuer 2011 bis 2014 nach  Durchführung einer mündlichen Verhandlung am 2.12.2021 zu Recht erkannt:   I. Den Beschwerden wird Folge gegeben.

**False Positives:**

- `Dr. Zlatan Deisen` — partial — pred is substring of gold: `Dr. Dr. Zlatan Deisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dr. Zlatan Deisen`(person)
- `Prof. Richard Paulick`(person)
- `Scharmühlwinkel 13, 3144 Baumgarten, Österreich`(address)
- `Finanzamt Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_TRAIN/135571.1`) (sent_id: `deanon_BFG_TRAIN/135571.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Univ.-Prof. Quentin Gerdener  in der Beschwerdesache Hon.-Prof.in Tatjana Schweneke, MSc,  Moorweg 23, 9300 Hörzendorf, Österreich, vertreten durch Steuerberatung Dr. Alfred Sorger GmbH, Steyrergasse 89,  8010 Graz, über die Beschwerde vom 8.3.2018 gegen die Bescheide des Finanzamtes Graz- Umgebung vom 14.12.2017 betreffend Einkommensteuer und Umsatzsteuer, jeweils für die  Jahre 2007 bis 2012 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Dr. Alfred Sorger Gmb` — partial — pred is substring of gold: `Steuerberatung Dr. Alfred Sorger GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Univ.-Prof. Quentin Gerdener`(person)
- `Hon.-Prof.in Tatjana Schweneke, MSc`(person)
- `Moorweg 23, 9300 Hörzendorf, Österreich`(address)
- `Steuerberatung Dr. Alfred Sorger GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_TRAIN/136145.1`) (sent_id: `deanon_BFG_TRAIN/136145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Gernot Sieglen, Oberlederau 7, 4224 Klingenwehr, Österreich  wohnhaft, StNr.: X1, vertreten durch Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010 Wien, betreffend die Berufung vom  25.05.2011 gegen die Einkommensteuerbescheide für die Jahre 2008 und 2009, vom  9.05.2011, zugestellt am 12.05.2011, des Finanzamtes Bruck Eisenstadt Oberwart  zu Recht erkannt

**False Positives:**

- `Dr. Hans Bodendorfer  Steuerberatungsges` — partial — pred is substring of gold: `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Gernot Sieglen`(person)
- `Oberlederau 7, 4224 Klingenwehr, Österreich`(address)
- `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`(organisation)

**Example 13** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter  Mag.Dr. Thomas Leitner sowie die fachkundigen Laienrichter Dipl.Ing. Christian Löw und  MMag.a Michaela Schmidt in der Beschwerdesache Beatrix Enke, Ried Riesberg 16, 2860 Stang, Österreich, vertreten  durch QUINTAX gerlich-fischer-kopp steuerberatungsgmbh, Ignaz-Rieder-Kai 13A, 5020  Salzburg, RA Dr. Fabian Maschke, Dominikanerbastei 17/11, 1010 Wien. und RA Rolf  Karpenstein, Gerhofstraße 40, D - 20354 Hamburg, über die Beschwerde vom 5. März 2013  gegen den Bescheid des FA Salzburg-Land vom 7. Februar 2013 betreffend Umsatzsteuer 2011,  die Beschwerde vom 31. März 2015 gegen den Bescheid des Finanzamtes Salzburg-Land vom 2.  März 2015 betreffend Umsatzsteuer 2013, die Beschwerde vom 1. Juli 2015 gegen den  Bescheid des Finanzamtes Salzburg-Land vom 11. Juni 2015 betreffend Umsatzsteuer 2014 und  die Beschwerde vom 5. Mai 2017 gegen den Bescheid des Finanzamtes Salzburg-Land vom 11.  April 2017 betreffend Umsatzsteuer 2015 zu Recht erkannt:  I. Die Bescheide betreffend Umsatzsteuer 2013, Umsatzsteuer 2014 und Umsatzsteuer 2015  werden jeweils dahingehend abgeändert, dass die Abgabenfestsetzung endgültig erfolgt.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`
- `Dr. Fabian Maschke` — partial — pred is substring of gold: `RA Dr. Fabian Maschke`
- `RA Rolf  Karpenstein` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `Mag.Dr. Thomas Leitner`(person)
- `Beatrix Enke`(person)
- `Ried Riesberg 16, 2860 Stang, Österreich`(address)
- `RA Dr. Fabian Maschke`(person)
- `FA Salzburg-Land`(organisation)

**Example 14** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_46`)


Im Rahmen der am 28. April 2022 durchgeführten mündlichen Verhandlung wurde seitens der  Beschwerdeführerin durch ihren anwaltlichen Vertreter RA Rolf Karpenstein das  Beschwerdevorbringen zusammengefasst insbesondere dahingehend ergänzt, dass nach der  Maßgabe der Rsp des EuGH nicht von einem steuerbaren Leistungsaustausch auszugehen sei  und dass die Mehrwertsteuer für die Beschwerdeführerin mangels Überwälzbarkeit auf den  Kunden einen Kostenfaktor darstelle und dies dem Grundsatz der Neutralität der  Mehrwertsteuer zuwiderlaufe.

**False Positives:**

- `RA Rolf Karpenstein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_49`)


Durch den anwaltlichen Vertreter der Beschwerdeführerin RA  Dr. Fabian Maschke wurde weiters in Zusammenhang mit dem Beschwerdevorbringen der  unionsrechtlich gebotenen umsatzsteuerlichen Gleichbehandlung von konzessionierten und  nicht konzessionierten Spielbanken die Einholung eines Gutachtens eines gerichtlich beeideten  und zertifizierten Sachverständigen aus dem Fachbereich Glücks- und Geschicklichkeitsspiele  beantragt („zum Beweis dafür, dass der hier gegenständlich relevante Sachverhalt bzw die  Handlungen der Beschwerdeführerin nicht umsatzsteuerpflichtig sind“).

**False Positives:**

- `Dr. Fabian Maschke` — partial — pred is substring of gold: `RA  Dr. Fabian Maschke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA  Dr. Fabian Maschke`(organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/136576.1`) (sent_id: `deanon_BFG_TRAIN/136576.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Mag.a HR Florentine Schönhaar, Dr. Karl Stenzel-Gasse 36, 5124 Weyer, Österreich, vom 28. Februar 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 22. Februar 2022, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Dr. Karl Stenzel` — partial — pred is substring of gold: `Dr. Karl Stenzel-Gasse 36, 5124 Weyer, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a HR Florentine Schönhaar`(person)
- `Dr. Karl Stenzel-Gasse 36, 5124 Weyer, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/136626.1`) (sent_id: `deanon_BFG_TRAIN/136626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  Muran Jostmann, Franz-Pilz-Straße 20, 8854 Krakaudorf, Österreich, vertreten durch RA Dr. Gregor Klammer, Lerchenfelder Gürtel  45/11, 1160 Wien, vom 18. August 2017, gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 20. Juli 2017, betreffend Abweisung des Antrages auf  Gewährung der Familienbeihilfe von Juni 2015 bis Juli 2017, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gregor Klammer` — partial — pred is substring of gold: `RA Dr. Gregor Klammer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Doktor`(person)
- `Muran Jostmann`(person)
- `Franz-Pilz-Straße 20, 8854 Krakaudorf, Österreich`(address)
- `RA Dr. Gregor Klammer`(person)

</details>

---

## `Specific Academic Title Pattern (Mag.a/Dr.in)`

**F1:** 0.439 | **Precision:** 0.670 | **Recall:** 0.327  

**Format:** `regex`  
**Rule ID:** `81012d3c`  
**Description:**
Captures person names with German academic titles, strictly stopping before common legal nouns. Updated to include suffixes like ', BA', ', BSc', ', Bakk.' and handle complex title chains.

**Content:**
```
\b((?:Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Mag\.|Mag\.-Doz\.|Dr\.|Dr\.in|Hon\.-Prof\.|Hon\.-Prof\.in|RgR|DDr\.|DDr\.in|OStR|Dipl\. Kff\.|Ing\.|KommR|RA|VetR|Techn\. R)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+)*(?:\s*,\s*(?:BA|BSc|B\.Sc|B\.A\.|Bakk\. rer\. nat\.|Dipl\.|Ing\.))?)(?![\s,]*Vollmacht|\s+\d|\s+\.|\s+\)|\s+\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.670 | 0.327 | 0.439 | 982 | 658 | 324 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 658 | 324 | 1357 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128700.1`) (sent_id: `deanon_BFG_TRAIN/128700.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Imre Schmidl  in der Beschwerdesache [...], [...],  über die Beschwerde vom 12. Februar 2018 gegen den Bescheid des Finanzamtes Lilienfeld St.  Pölten vom 16. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Imre Schmidl` | `Dr. Imre Schmidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Konrad Conrady  in der Beschwerdesache  Prof.  Ashley Lauterwasser, Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich, über die Beschwerde vom 23. September 2016 gegen den Bescheid  des Finanzamtes Linz vom 25. August 2016 betreffend Einkommensteuer 2014 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Konrad Conrady` | `Univ.-Prof. Konrad Conrady` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ashley Lauterwasser` (person)
- `Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128709.1`) (sent_id: `deanon_BFG_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Felizitas Muendl, Bakk. phil., Güttling 9, 9321 Latschach, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Muendl, Bakk. phil.` (person)
- `Güttling 9, 9321 Latschach, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Walla` | `Mag. Dieter Walla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `M.` (person)
- `Bauermeister Getränke` (organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich` (address)
- `09-169/6729` (tax_number)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128894.1`) (sent_id: `deanon_BFG_TRAIN/128894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nancy Brandlmayr  in der Beschwerdesache der  Süd-Landwirtschaft, Freundling 10, 4190 Amesschlag, Österreich, über die Beschwerde vom 5. Juni 2019, beim zuständigen  Finanzamt eingelangt am 6. Juni 2019, gegen den Bescheid des Finanzamt Vorarlberg  vom 24. Mai 2019  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 (Steuernummer  82-615/9369 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung vom  3.September 2019 Folge gegeben;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Nancy Brandlmayr` | `Univ.-Prof.in Nancy Brandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Süd-Landwirtschaft` (organisation)
- `Freundling 10, 4190 Amesschlag, Österreich` (address)
- `Finanzamt Vorarlberg` (organisation)
- `82-615/9369` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl. Kff. Gwendolin Ziehr,  Reebokplatz 60, 4083 Gemersdorf, Österreich, vertreten durch BG&P Binder Grossek & Partner Steuerberatung und  Wirtschafts- prüfung GmbH, Neufeldweg 93, 8010 Graz, über die Beschwerden vom 10. Juni  2015 gegen die Bescheide des Finanzamtes Graz-Umgebung vom 14. April 2015 betreffend  Festsetzung des Dienstgeberbeitrages (DB) und des Zuschlages zum Dienstgeberbeitrag (DZ)  für die Jahre 2009, 2010, 2011, 2012 und 2013, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Emmerich Bleekmann` | `Mag. Emmerich Bleekmann` |
| `Dipl. Kff. Gwendolin Ziehr` | `Dipl. Kff. Gwendolin Ziehr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reebokplatz 60, 4083 Gemersdorf, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Dr. Gerlinde  Rieser` | `Dr. Gerlinde  Rieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raphael Skowroneck, MBA` (person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129068.1`) (sent_id: `deanon_BFG_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Jens Spilken, Hillere 22, 8453 Saggau, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-228/4517  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |
| `Mag. Achmed Ghazal Aswad` | `Mag. Achmed Ghazal Aswad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jens Spilken` (person)
- `Hillere 22, 8453 Saggau, Österreich` (address)
- `69-228/4517` (tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lubomir Baltßun` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Beate Melik  in der Beschwerdesache Techn R Dr.in Maria Repstock,  Silberrain 14a, 5542 Flachau, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Beate Melik` | `Priv.-Doz.in Beate Melik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Dr.in Maria Repstock` (person)
- `Silberrain 14a, 5542 Flachau, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129103.1`) (sent_id: `deanon_BFG_TRAIN/129103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache DDr. Rocco Bernhards, Obere Festwiese 8, 4863 Steindorf, Österreich, über die Beschwerde vom 18. Juli 2013 gegen den Bescheid des Zollamtes Linz Wels  vom 18. Juni 2013 betreffend Vorschreibung eines Altlastenbeitrag für die Quartale 2-4 des  Jahres 2003 zu Recht erkannt:   Der angefochtene Bescheid wird hinsichtlich des Altlastenbeitrags - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `DDr. Rocco Bernhards` | `DDr. Rocco Bernhards` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obere Festwiese 8, 4863 Steindorf, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich` (address)
- `Eva Maria Koller-Rohrschach` (person)
- `84-986/6948` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_18`)


Nur dem Dienstnehmer AB, welcher der Sohn des Einzelunternehmers OStR Karl Ostendarp  ist, wurde  unterstellt, diese Fahrzeuge auch für private Zwecke zu nutzen.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Example 13** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_46`)


3) Die Fahrzeuge wurden nach Dienstende am Firmensitz: Adresse abgestellt. Die  Fahrzeugschlüssel und Papiere wurden von Herrn OStR Karl Ostendarp  oder Frau AB persönlich  entgegengenommen und im Büro versperrt aufbewahrt.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Example 14** (doc_id: `deanon_BFG_TRAIN/129168.1`) (sent_id: `deanon_BFG_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  Dolores Jodjürgis, BA MBA, Feldsiedlung 87, 5242 Obereck, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dolores Jodjürgis, BA MBA` (person)
- `Feldsiedlung 87, 5242 Obereck, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129231.1`) (sent_id: `deanon_BFG_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Bartholomäus Malcharzik, Ogugasse 8, 4483 Pirchhorn, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Elisabeth Traxler` | `Mag. Elisabeth Traxler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bartholomäus Malcharzik` (person)
- `Ogugasse 8, 4483 Pirchhorn, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |
| `Mag. Wolfgang Freudelsperger` | `Mag. Wolfgang Freudelsperger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janis Dollnig` (person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129379.1`) (sent_id: `deanon_BFG_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Johanna Harazin  in der Beschwerdesache des  Konstanze Seyfrieds, Rudolf-von-Gutmann-Straße 19, 9545 Dabor, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Bruck Eisenstadt Oberwart  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Johanna Harazin` | `Univ.-Prof.in Johanna Harazin` |
| `Mag. Hermann Rupert Zittmayr` | `Mag. Hermann Rupert Zittmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Konstanze Seyfrieds` (person)
- `Rudolf-von-Gutmann-Straße 19, 9545 Dabor, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129421.1`) (sent_id: `deanon_BFG_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Konepatzki  in der Beschwerdesache KommR MedR Jeannine Wegerhoff,  Burleiten 563, 9423 Matschenbloch, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Jacqueline Konepatzki` | `Univ.-Prof.in Jacqueline Konepatzki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR MedR Jeannine Wegerhoff` (person)
- `Burleiten 563, 9423 Matschenbloch, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129437.1`) (sent_id: `deanon_BFG_TRAIN/129437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alexandra Halbmeyer  in der Beschwerdesache des  Dragan Cayci, Ronklerbrunnen 5, 3860 Haslau, Österreich, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamt Gmunden Vöcklabruck  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Alexandra Halbmeyer` | `Hon.-Prof.in Alexandra Halbmeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dragan Cayci` (person)
- `Ronklerbrunnen 5, 3860 Haslau, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)

**Example 20** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Danelzik` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 21** (doc_id: `deanon_BFG_TRAIN/129520.1`) (sent_id: `deanon_BFG_TRAIN/129520.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Verwaltungsstrafsache  gegen KzlR Wolf Wältl, MBA, Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich, über die Beschwerde des Beschuldigten vom 26. März 2020  gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 10. März 2020, Zahl:  MA67/196700631216/2019, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Wolf Wältl, MBA` (person)
- `Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/129555.1`) (sent_id: `deanon_BFG_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache ÖkR Nadine Fritzekötter, Fahnbach 3, 3752 Nonnersdorf, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Nadine Fritzekötter` (person)
- `Fahnbach 3, 3752 Nonnersdorf, Österreich` (address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Reinhard Komarova, Gabrielweg 4, 4725 Adelsgrub, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 92-139/9763  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reinhard Komarova` (person)
- `Gabrielweg 4, 4725 Adelsgrub, Österreich` (address)
- `92-139/9763` (tax_number)

**Example 24** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 25** (doc_id: `deanon_BFG_TRAIN/129671.1`) (sent_id: `deanon_BFG_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Katharina Stäubling  in der Beschwerdesache Rüterborries+Friderich Möbel,  General-Arnold-Straße 13, 9111 Dobrowa, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Katharina Stäubling` | `Priv.-Doz.in Katharina Stäubling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rüterborries+Friderich Möbel` (organisation)
- `General-Arnold-Straße 13, 9111 Dobrowa, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/129733.1`) (sent_id: `deanon_BFG_TRAIN/129733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Wilfried Wedral  in der Beschwerdesache Ramona Goedeken,  Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich, vertreten durch Union TAX&LAW, Donau-City-Straße 7, DV Tower/30th floor,  1220 Wien, über die Beschwerde vom 16. April 2019 gegen den Bescheid des Finanzamtes  Innsbruck vom 19. März 2019 betreffend Familienbeihilfe (Ausgleichszahlung) für die Monate  Jänner 2015 bis Dezember 2017, [Ordnungsbegriff],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Wilfried Wedral` | `Hon.-Prof. Wilfried Wedral` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ramona Goedeken` (person)
- `Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/129778.1`) (sent_id: `deanon_BFG_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache VetR Silvester Johäntges, Fischauer Gasse 37, 4616 Hetzendorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 25-402/5507  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `VetR Silvester Johäntges` | `VetR Silvester Johäntges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Fischauer Gasse 37, 4616 Hetzendorf, Österreich` (address)
- `25-402/5507` (tax_number)

**Example 28** (doc_id: `deanon_BFG_TRAIN/129789.1`) (sent_id: `deanon_BFG_TRAIN/129789.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über den Antrag der  Rebecca Sümnicht, Haselgraben 126, 4083 Hinterberg, Österreich, vertreten durch BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, QBC 4 – Am Belvedere 4, 1100 Wien, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer  für das Jahr 2014 erhobenen ordentlichen Revision vom 24. Juni 2020 die aufschiebende  Wirkung zuzuerkennen, beschlossen:  Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rebecca Sümnicht` (person)
- `Haselgraben 126, 4083 Hinterberg, Österreich` (address)
- `BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_TRAIN/129828.1`) (sent_id: `deanon_BFG_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Pascal Beerlage, Tannwaldweg 35L, 9133 Jerischach, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 13-489/9399  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |
| `Dr. Helmut Herbert Moritz` | `Dr. Helmut Herbert Moritz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pascal Beerlage` (person)
- `Tannwaldweg 35L, 9133 Jerischach, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `13-489/9399` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/102855.1`) (sent_id: `deanon_BFG_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr. Mag. Adrian Bembenick  in der Beschwerdesache Mag.a Julia Leitgöb, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. Adrian Bembenick`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mag. Adrian Bembenick`(person)
- `Mag.a Julia Leitgöb`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/124843.1`) (sent_id: `deanon_BFG_TRAIN/124843.1_0`)


GZ. RV/7100201/2013 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der Beschwerdesache Bf, Adr, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 01.10.2012 (datiert mit 28.9.2012) gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom Juli 2012 betreffend Festsetzung von Normverbrauchsabgabe für Mai 2012 in Höhe von € 19.131,60 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri. in der Beschwerdesache RgR Univ.-Prof.in KommR Corinna Bebenek, Teurniastraße 10, 6346 Hausern, Österreich, vertreten durch Alfred Klaus Fenzl, Am Steinbühel 27b, 4030 Linz, über die  Beschwerde vom 18. November 2013 gegen den Bescheid des Finanzamtes Linz vom  13. November 2013 betreffend Einkommensteuer 2011 und die Beschwerde vom 27. Jänner  2015 gegen den Bescheid vom 19. Jänner 2015 betreffend Einkommensteuer 2012 zu  Steuernummer 65-309/8174  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)
- `Teurniastraße 10, 6346 Hausern, Österreich`(address)
- `Alfred Klaus Fenzl`(person)
- `65-309/8174`(tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_44`)


Demnach war Frau RgR Univ.-Prof.in KommR Corinna Bebenek  von 01.12.2010 bis zum 29.02.2012 bei A R. als  Dienstnehmerin beschäftigt.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_69`)


„Frau RgR Univ.-Prof.in KommR Corinna Bebenek  war von 1.12.2010 bis 29.02.2012 bei A R. als Dienstnehmerin  (Dienstgeberkonto lautend auf Personenbeförderung W T.) beschäftigt.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_77`)


Bei der Einvernahme der Frau RgR Univ.-Prof.in KommR Corinna Bebenek  am 2.12.2013 am FA U. P. R als Zeugin wurden  folgende Unterlagen übergeben: Jahreslohnkonten, Auszug Gewerbeberechtigungen  Taxigewerbe und Mietwagengewerbe, Stundenaufzeichnung Dezember 2010, händische  Auszahlungslisten Mai, Juni, Juli, August, September, Oktober 2011 und Übersicht  Auszahlungsliste Februar 2012 und oa. Sachverhalt mitgeteilt.  Für die Behörde ist in freier Würdigung der der Beschwerdeführerin zur Kenntnis gebrachten  Beweismittel erwiesen, dass Frau RgR Univ.-Prof.in KommR Corinna Bebenek  für die zur Verfügungstellung der Taxikonzession  zusätzlich zu den am Lohnkonto ausgewiesenen Beträge € 7.000,- in bar übergeben wurden.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `RgR Univ` — similar text (different position): `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — similar text (different position): `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)
- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 6** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_86`)


Aus vorgenannten Gründen kann es keine Stundenaufzeichnungen der RgR Univ.-Prof.in KommR Corinna Bebenek  geben, bzw.  sind solche, wenn sie vorliegen, gefälscht.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 7** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_119`)


Aus vorgenannten Gründen kann es keine Stundenaufzeichnungen der RgR Univ.-Prof.in KommR Corinna Bebenek  geben, bzw.  sind solche, wenn sie vorliegen, gefälscht.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129033.1`) (sent_id: `deanon_BFG_TRAIN/129033.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Karola Haferland, Furthofer Straße 18, 4661 Unterpühret, Österreich  vom 25. Februar 2018 gegen den Bescheid des  Finanzamtes St. Johann Tamsweg Zell am See, Brucker Bundesstraße 13, 5700 Zell am See vom  8. Februar 2018 betreffend Festsetzung der Normverbrauchsabgabe für Jänner 2018 zu Recht  erkannt:  1.

**False Positives:**

- `Dr. Maria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Karola Haferland`(person)
- `Furthofer Straße 18, 4661 Unterpühret, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Beate Melik  in der Beschwerdesache Techn R Dr.in Maria Repstock,  Silberrain 14a, 5542 Flachau, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Maria Repstock` — partial — pred is substring of gold: `Techn R Dr.in Maria Repstock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Beate Melik`(person)
- `Techn R Dr.in Maria Repstock`(person)
- `Silberrain 14a, 5542 Flachau, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `OStR Karl Ostendarp`(person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich`(address)
- `Eva Maria Koller-Rohrschach`(person)
- `84-986/6948`(tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Dr.in Ulrike Kusnierz  in der Beschwerdesache K GmbH,  Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Dr.in Dr` — partial — pred is substring of gold: `Dr.in Dr.in Ulrike Kusnierz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Dr.in Ulrike Kusnierz`(person)
- `Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129421.1`) (sent_id: `deanon_BFG_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Konepatzki  in der Beschwerdesache KommR MedR Jeannine Wegerhoff,  Burleiten 563, 9423 Matschenbloch, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `KommR Med` — partial — pred is substring of gold: `KommR MedR Jeannine Wegerhoff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Jacqueline Konepatzki`(person)
- `KommR MedR Jeannine Wegerhoff`(person)
- `Burleiten 563, 9423 Matschenbloch, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

**False Positives:**

- `Dr. Doringer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `Dr.in Monika Wörther` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

**False Positives:**

- `Dr. Doringer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dr.in Monika Wörther` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

**False Positives:**

- `Dr. Doringer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/129778.1`) (sent_id: `deanon_BFG_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache VetR Silvester Johäntges, Fischauer Gasse 37, 4616 Hetzendorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 25-402/5507  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `VetR Silvester Johäntges`(person)
- `Fischauer Gasse 37, 4616 Hetzendorf, Österreich`(address)
- `25-402/5507`(tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

**False Positives:**

- `Dr. Schmid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alexander Nahler`(person)

**Example 20** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Julia Schulteß, Anton-Sattler-Gasse 42, 3531 Brand, Österreich, vertreten durch Mag. Anton Heisinger,  Mühlallee 1, 7301 Deutschkreutz, über die Beschwerde vom 29. Februar 2016 gegen den  Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 29. Jänner 2016 betreffend Haftung  gemäß § 99 EStG 1988 für den Zeitraum 2014 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Julia Schulteß`(person)
- `Anton-Sattler-Gasse 42, 3531 Brand, Österreich`(address)
- `Mag. Anton Heisinger`(person)

**Example 21** (doc_id: `deanon_BFG_TRAIN/130407.1`) (sent_id: `deanon_BFG_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Emma Sebestik, Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Emma Sebestik`(person)
- `Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich`(address)
- `Harald Schmidt`(person)
- `Finanzamtes Spittal Villach`(organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Helena Özarslan, An der Hortigstraße 1, 5133 Hub, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Amtsvertr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Helena Özarslan`(person)
- `An der Hortigstraße 1, 5133 Hub, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)

**Example 23** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_199`)


Der Bf führte in seinem Schussantrag aus, dass er die ImmoESt gar nicht schulde, sondern hätte  diese vielmehr sein vormaliger steuerlicher Vertreter, StB Dr. St, zu tragen.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_350`)


Eine Haftung des ehemaligen  steuerlichen Vertreters des Bf, StB Dr. St, auf Grundlage der Bestimmung des § 30c Abs. 3 leg.  cit.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

**False Positives:**

- `Dr. Praus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Mag. Artner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

**False Positives:**

- `Dr. Praus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

**False Positives:**

- `Mag. Artne` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

**False Positives:**

- `Dr. Prause Heilsarme` — partial — pred is substring of gold: `Dr. Prause Heilsarmee`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Prause Heilsarmee`(person)

</details>

---

## `Non-Academic Title Name Pattern`

**F1:** 0.022 | **Precision:** 0.639 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `371c3c3b`  
**Description:**
Captures names preceded by specific non-academic professional titles like 'VetR' (Veterinär) or 'Techn R' (Technischer Rat) which are not covered by the academic title rule.

**Content:**
```
\b((?:VetR|Techn\sR|RA\s|Dr\.\s|Mag\.\s|Hon\.-Prof\.in\s|Univ\.-Prof\.in\s|Priv\.-Doz\.\s|Dr\.in\s|Mag\.in\s|Mag\.a\s)\s+[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.639 | 0.011 | 0.022 | 36 | 23 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 13 | 1948 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129778.1`) (sent_id: `deanon_BFG_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache VetR Silvester Johäntges, Fischauer Gasse 37, 4616 Hetzendorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 25-402/5507  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `VetR Silvester Johäntges` | `VetR Silvester Johäntges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Fischauer Gasse 37, 4616 Hetzendorf, Österreich` (address)
- `25-402/5507` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/130444.1`) (sent_id: `deanon_BFG_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Lars Hoerl  in der Beschwerdesache VetR Christina Schlotfeldt,  Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Christina Schlotfeldt` | `VetR Christina Schlotfeldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Lars Hoerl` (person)
- `Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/131343.1`) (sent_id: `deanon_BFG_TRAIN/131343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Techn R Damian Weida, Maierniggalpe 210, 4712 Niederwödling, Österreich, über die Beschwerde vom 21. August 2018 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 2. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Techn R Damian Weida` | `Techn R Damian Weida` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maierniggalpe 210, 4712 Niederwödling, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der  Verwaltungsstrafsache gegen Techn R Gwendolin Omar, Schrötten 38, 3860 Aalfang, Österreich, über die Beschwerde des  Beschuldigten vom 9.11.2020 gegen die Vollstreckungsverfügungen des Magistrates der Stadt  Wien, Magistratsabteilung 6, vom 11. Jänner 2020, 1) MA67/196700867324/2019 und 2)  MA67/196700891928/2019 vom 14.1.2020, MA67/196700890302/2019 und vom 25.1.2020,   MA67/196700930712/2019, alle in Zusammenhang mit einer Verwaltungsübertretung gemäß  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, i.d.g.F., in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, i.d.g.F. zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und werden die angefochtenen  Vollstreckungsverfügungen ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Schrötten 38, 3860 Aalfang, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 6` (organisation)
- `Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_23`)


Auf Grund einer Anfrage des Bundesfinanzgerichtes bei der für Meldeangelegenheiten  zuständigen Fachdienststelle in der Stadt Wien, der MA 62, teilte diese mit E-Mail vom  25.2.2021 folgendes mit:  „Zu Ihrer Anfrage teile ich Ihnen seitens der Magistratsabteilung 62 als zuständiger  Fachdienststelle für Meldeangelegenheiten in der Stadt Wien mit, dass Herr Techn R Gwendolin Omar  wie  von ihm angegeben von uns nach Durchführung eines Verfahrens nach § 15 Meldegesetz  amtlich von der Adresse xy abgemeldet wurde.

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_26`)


Der Erheber bekam vor Ort am  14. Jänner 2020 von einer Hauspartei, deren Identität wir nicht kennen, die Auskunft, dass Herr  Techn R Gwendolin Omar  unbekannt wohin verzogen sei.

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_27`)


Herr Techn R Gwendolin Omar  wurde von uns zweimal im  Verfahren angeschrieben, davon einmal mit RSb-Rückscheinbrief, und hat darauf nicht  reagiert.“

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/135036.1`) (sent_id: `deanon_BFG_TRAIN/135036.1_3`)


über die Beschwerde des Techn R Volker Eschermann,  Deuschlergasse 5, 5600 Floitensberg, Österreich, vom 23. Oktober 2021 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 23. September 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Techn R Volker Eschermann` | `Techn R Volker Eschermann` |

**Missed by this rule (FN):**

- `Deuschlergasse 5, 5600 Floitensberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/136171.1`) (sent_id: `deanon_BFG_TRAIN/136171.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache VetR Susette Käse, Alte Tauernstraße 16, 4161 Lichtenberg, Österreich, über die Beschwerde vom 1. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 28. März 2017 betreffend Rückforderung von  Ausgleichszahlung gemäß der Verordnung (EG) 883/2004 (Familienbeihilfe) für den Zeitraum  April 2016 bis Oktober 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Susette Käse` | `VetR Susette Käse` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Alte Tauernstraße 16, 4161 Lichtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_TRAIN/139715.1`) (sent_id: `deanon_BFG_TRAIN/139715.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Elfriede Murtinger über die Beschwerde  des Techn R Emil Stueven, Rutzendorfer Straße 20, 5242 Frauschereck, Österreich, vom 13. Dezember 2022 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. November 2022, GZ.  MA67/Zahl/2022, wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Techn R Emil Stueven` | `Techn R Emil Stueven` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elfriede Murtinger` (person)
- `Rutzendorfer Straße 20, 5242 Frauschereck, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_TRAIN/143278.1`) (sent_id: `deanon_BFG_TRAIN/143278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Leila Hussack, Bakk. iur. MA, Krumauerstraße 21, 4223 Katsdorf, Österreich, vertreten durch HAUNSCHMIDT & PARTNER  Steuerberatungs GmbH, Julius Tandler Pl 6 Tür 9, 1090 Wien, über die Beschwerde vom  26. März 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom  9. März 2020 betreffend Stundungszinsen 2020 nach der am 4.12.2023 am  Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO i.V.m. § 274 Abs. 1 Z 1 BAO) in  Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und in Anwesenheit von Mag.  Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte Behörde durchgeführten  mündlichen Verhandlung zur Steuernummer 77-604/4717  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.  Martin Holzapfel` | `Mag.  Martin Holzapfel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Leila Hussack, Bakk. iur. MA` (person)
- `Krumauerstraße 21, 4223 Katsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Mag. Sebastian Rivo-Wastl, BA` (person)
- `77-604/4717` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/143446.1`) (sent_id: `deanon_BFG_TRAIN/143446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Barbara Straka, die Richterin  Mag. Irene Kohler sowie die fachkundigen Laienrichter Dip.Ing. Gerald Patschka und Mag.  Michael Heumesser in der Beschwerdesache Dr. Herbert Schießwohl, Wopenkastraße 17, 4802 Ebensee, Österreich, vertreten durch  Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38,  1020 Wien, über die Beschwerde vom 22. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 23. Februar 2023 betreffend Einkommensteuer 2013, Steuernummer  50-732/9932, in der Sitzung am 17. Jänner 2024, erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.  Michael Heumesser` | `Mag.  Michael Heumesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Barbara Straka` (person)
- `Mag. Irene Kohler` (person)
- `Dip.Ing. Gerald Patschka` (person)
- `Dr. Herbert Schießwohl` (person)
- `Wopenkastraße 17, 4802 Ebensee, Österreich` (address)
- `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `50-732/9932` (tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/144349.1`) (sent_id: `deanon_BFG_TRAIN/144349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  VetR Marlies Thalmayr, Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom 6. Februar  2024 gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2024 betreffend  Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 01.12.2022 bis  30.06.2023, Steuernummer 88-272/3661, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Marlies Thalmayr` | `VetR Marlies Thalmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `88-272/3661` (tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Andrea Ebner in der Rechtssache  Techn R Francois Bartoszek, Porr Headquaters 139, 8403 Göttling, Österreich, betreffend den Antrag nach § 299 BAO vom 11. Juli 2024 auf  Aufhebung des Beschlusses des Bundesfinanzgerichtes vom 3. Juli 2024, RV/7101936/2024,  Steuernummer 94-241/1081, den Beschluss:  I. Der Antrag nach § 299 BAO vom 11. Juli 2024 auf Aufhebung des Beschlusses des  Bundesfinanzgerichtes vom 3. Juli 2024, RV/7101936/2024 wird als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Porr Headquaters 139, 8403 Göttling, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)
- `94-241/1081` (tax_number)
- `Bundesfinanzgerichtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_3`)


Begründung  Techn R Francois Bartoszek  brachte bei der belangten Behörde am 22. November 2023 unter anderem eine  Vorlageerinnerung betreffend den Bescheid des Finanzamtes Österreich vom 21. September  2021 ein.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Finanzamtes Österreich` (organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_6`)


Der vorgenannte Beschluss (Mängelbehebungsauftrag) wurde am 18. Juni 2024 zugestellt.  Mit E-Mail vom 19. Juni 2024 kündigte Techn R Francois Bartoszek  an, „die Vorlageerinnerung vom 221123 betr  Gebührenbescheide vom 210921 wird zurückgezogen“.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Example 17** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_9`)


Da Techn R Francois Bartoszek  dem Auftrag zur Mängelbehebung unstrittig beim Bundesfinanzgericht innerhalb  der gesetzten Frist nicht nachgekommen ist, galt die Vorlageerinnerung mit Ablauf der  gesetzten Frist als zurückgenommen (siehe betreffenden Beschluss des BFG vom 3. Juli 2024,  RV/7101936/2024).

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 18** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_35`)


Der Antrag des Herrn Techn R Francois Bartoszek  vom 11. Juli 2024 auf Aufhebung des Beschusses des  Bundesfinanzgerichtes vom 13. Juni 2024, RV/7101936/2024 wird daher als unzulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_TRAIN/147360.1`) (sent_id: `deanon_BFG_TRAIN/147360.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Namli  in der Beschwerdesache VetR Georg Versteegen,  Kirchenlucken 549, 4845 Mairhof, Österreich, über die Beschwerde vom 6. April 2018 gegen den Bescheid des FA Steiermark Mitte  (nunmehr Finanzamt Österreich) vom 23. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Steuernummer 33-748/3939  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Georg Versteegen` | `VetR Georg Versteegen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Namli` (person)
- `Kirchenlucken 549, 4845 Mairhof, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `Finanzamt Österreich` (organisation)
- `33-748/3939` (tax_number)

**Example 20** (doc_id: `deanon_BFG_TRAIN/147401.1`) (sent_id: `deanon_BFG_TRAIN/147401.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicole Landt  in der Beschwerdesache Techn R Benjamin Liebetanz,  Sandbühel 31, 4784 Bach, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 29. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt  Österreich/FAÖ) vom 1. August 2016, Erf. Nr. 111x, betreffend  1. Festsetzung der Gebühren gemäß § 14 TP 2 Abs.1 Z 1, TP 5 Abs. 1, TP 6 Abs. 2       und TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO zur Gänze als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Techn R Benjamin Liebetanz` | `Techn R Benjamin Liebetanz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Nicole Landt` (person)
- `Sandbühel 31, 4784 Bach, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/147401.1`) (sent_id: `deanon_BFG_TRAIN/147401.1_4`)


Die Bezirkshauptmannschaft A-Ort1 hat am 11.4.2016 acht amtliche Befunde (zu   GZ. XY1-8) über die "Verkürzung von Stempel- oder Rechtsgebühren" hinsichtlich der  "Meldung des Ausflugsverkehrs gemäß Tiroler Schischulgesetz 1995" je v. 4.1.2016 für acht  Schilehrer (AA, BB, CC, DD, EE, FF, GG, HH) durch die Techn R Benjamin Liebetanz (= Beschwerdeführerin, Bf),  eine deutsche Schischule, erstellt und an das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel, nunmehr Finanzamt Österreich, übermittelt.   Gegenstand der Gebühr waren den Befunden zufolge jeweils die Meldung des  Ausflugsverkehrs gemäß Tiroler Schischulgesetz samt Beilagen und Kopien der  Lichtbildausweise der gemeldeten Lehrer sowie die schriftliche Erledigung durch die  Bezirkshauptmannschaft.

| Predicted | Gold |
|---|---|
| `Techn R Benjamin Liebetanz` | `Techn R Benjamin Liebetanz` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/148329.1`) (sent_id: `deanon_BFG_TRAIN/148329.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Barbara Eismont  in der Beschwerdesache Techn R Joseph Balnuweit,  Hauzendorf 7, 4180 Zwettl an der Rodl, Österreich, vertreten durch Raiffeisenverband Steiermark, Raiffeisen-Platz 11, 8074  Raaba-Grambach, über die Beschwerde vom 15. November 2018 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. Oktober 2018 betreffend Berichtigung §§ 293 ff BAO 2012,  Steuernummer 48-226/2592  zu Recht erkannt:    I. Der angefochtene Bescheid wird gem. dem VwGH-Erkenntnis Ra 2023/15/0112-8  abgeändert.

| Predicted | Gold |
|---|---|
| `Techn R Joseph Balnuweit` | `Techn R Joseph Balnuweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Barbara Eismont` (person)
- `Hauzendorf 7, 4180 Zwettl an der Rodl, Österreich` (address)
- `Raiffeisenverband Steiermark` (organisation)
- `48-226/2592` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Beate Melik  in der Beschwerdesache Techn R Dr.in Maria Repstock,  Silberrain 14a, 5542 Flachau, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Dr` — partial — pred is substring of gold: `Techn R Dr.in Maria Repstock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Beate Melik`(person)
- `Techn R Dr.in Maria Repstock`(person)
- `Silberrain 14a, 5542 Flachau, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/134371.1`) (sent_id: `deanon_BFG_TRAIN/134371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Techn R Lee Ditscheidt, Bakk. art. Bakk. art., Heitzmannweg 11, 4661 Mitterbuch, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31.März 2014 gegen die Bescheide des Finanzamtes für Großbetriebe je vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2008 bis  2012 (Steuernummer 38-978/7129 ) nach Durchführung einer mündlichen Verhandlung am  04.08.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn R Lee Ditscheidt` — partial — pred is substring of gold: `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`(person)
- `Heitzmannweg 11, 4661 Mitterbuch, Österreich`(address)
- `Finanzamtes für Großbetriebe`(organisation)
- `38-978/7129`(tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/134371.1`) (sent_id: `deanon_BFG_TRAIN/134371.1_240`)


Die Gesellschafter  der OG wurden bereichert und bei der Techn R Lee Ditscheidt, Bakk. art. Bakk. art.  ist der Aufwand verdeckte  Gewinnausschüttung.“

**False Positives:**

- `Techn R Lee Ditscheidt` — partial — pred is substring of gold: `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`(person)

**Example 3** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_49`)


Durch den anwaltlichen Vertreter der Beschwerdeführerin RA  Dr. Fabian Maschke wurde weiters in Zusammenhang mit dem Beschwerdevorbringen der  unionsrechtlich gebotenen umsatzsteuerlichen Gleichbehandlung von konzessionierten und  nicht konzessionierten Spielbanken die Einholung eines Gutachtens eines gerichtlich beeideten  und zertifizierten Sachverständigen aus dem Fachbereich Glücks- und Geschicklichkeitsspiele  beantragt („zum Beweis dafür, dass der hier gegenständlich relevante Sachverhalt bzw die  Handlungen der Beschwerdeführerin nicht umsatzsteuerpflichtig sind“).

**False Positives:**

- `RA  Dr` — partial — pred is substring of gold: `RA  Dr. Fabian Maschke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA  Dr. Fabian Maschke`(organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/136984.1`) (sent_id: `deanon_BFG_TRAIN/136984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache VetR Cedric Özturan, Scholzstraße 25, 8113 Södingberg, Österreich, über die Beschwerde der Beschwerdeführerin (Bf.) vom 12. August 2021 gegen den  Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2020 des Finanzamtes Österreich vom  9. August 2021 zu Steuernummer 40-154/0143  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

**False Positives:**

- `VetR Cedric` — partial — pred is substring of gold: `VetR Cedric Özturan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Cedric Özturan`(person)
- `Scholzstraße 25, 8113 Södingberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `40-154/0143`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/137224.1`) (sent_id: `deanon_BFG_TRAIN/137224.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Techn R Prof. Ronald Carnegie, Anton-Schrammel-Hof 18, 3341 Schwarzois, Österreich, über die Beschwerde vom 18.01.2021 gegen den Bescheid des  Finanzamtes Österreich vom 15. Jänner 2021, betreffend Einkommensteuer 2019, zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn R Prof` — partial — pred is substring of gold: `Techn R Prof. Ronald Carnegie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Techn R Prof. Ronald Carnegie`(person)
- `Anton-Schrammel-Hof 18, 3341 Schwarzois, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/137796.1`) (sent_id: `deanon_BFG_TRAIN/137796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Lee Kolesnichenko, Hannovermarkt 59, 4801 Eben, Österreich, vertreten durch Ing. Thomas Millesich, Dr.  Wlasakstraße 83, 2410 Hainburg, über die Beschwerde vom 25. März 2022 gegen den Bescheid  des Finanzamtes Österreich vom 23. Februar 2022 betreffend Festsetzung einer Zwangsstrafe,  Steuernummer 25-414/2087, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.  Wlasakstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Lee Kolesnichenko`(person)
- `Hannovermarkt 59, 4801 Eben, Österreich`(address)
- `Ing. Thomas Millesich`(person)
- `Finanzamtes Österreich`(organisation)
- `25-414/2087`(tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138549.1`) (sent_id: `deanon_BFG_TRAIN/138549.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  HR Techn R Wolfgang Strauscheidt, Sixenstraße 86, 4892 Fornach, Österreich, über die Beschwerde vom gegen den Bescheid des Finanzamtes  Österreich vom 29. Oktober 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2020 Steuernummer 90-061/3966  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Wolfgang Strauscheidt` — partial — pred is substring of gold: `HR Techn R Wolfgang Strauscheidt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `HR Techn R Wolfgang Strauscheidt`(person)
- `Sixenstraße 86, 4892 Fornach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `90-061/3966`(tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/140957.1`) (sent_id: `deanon_BFG_TRAIN/140957.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Adriana van den Heuvel  in der Beschwerdesache VetR Prof.in Fiona Helmholz,  Pfarrsteig 7h, 8312 Breitenbach, Österreich, vertreten durch Grant Thornton Austria GmbH Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Handelskai 92/Gate 2/Top 7A, 1200 Wien, betreffend  Beschwerde vom 01.08.2008 gegen die Bescheide über die Wiederaufnahme des Verfahrens  hinsichtlich der Umsatzsteuer der Jahre 2000 bis 2003 und gegen die Umsatzsteuerbescheide  der Jahre 2000 bis 2005, jeweils vom 30.06.2008 sowie betreffend die Beschwerde vom  08.08.2008 gegen die Haftungs- und Abgabenbescheide hinsichtlich Kapitalertragsteuer der  Jahre 2000 bis 2004, jeweils vom 13.06.2008 zu Steuernummer 24-683/2597  beschlossen:   I. Das Beschwerdeverfahren wird eingestellt.   II. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `VetR Prof` — partial — pred is substring of gold: `VetR Prof.in Fiona Helmholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Adriana van den Heuvel`(person)
- `VetR Prof.in Fiona Helmholz`(person)
- `Pfarrsteig 7h, 8312 Breitenbach, Österreich`(address)
- `Grant Thornton Austria GmbH`(organisation)
- `24-683/2597`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/140957.1`) (sent_id: `deanon_BFG_TRAIN/140957.1_23`)


Über die Beschwerdeführerin, VetR Prof.in Fiona Helmholz, wurde mit Beschluss des Handelsgerichtes Wien AZ  das Konkursverfahren eröffnet.

**False Positives:**

- `VetR Prof` — partial — pred is substring of gold: `VetR Prof.in Fiona Helmholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Prof.in Fiona Helmholz`(person)

**Example 10** (doc_id: `deanon_BFG_TRAIN/141448.1`) (sent_id: `deanon_BFG_TRAIN/141448.1_8`)


die Bestellung der RA      MagB zur (neuen) Erwachsenenvertreterin der Bf, für diese folgende     Angelegenheiten zu besorgen: Vertretung vor Gerichten, Behörden etc; Vermögens-     und Einkünfteverwaltung;

**False Positives:**

- `RA      Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/143865.1`) (sent_id: `deanon_BFG_TRAIN/143865.1_73`)


Möglicherweise seien sie aber "vor" Erteilung eines Auftrags durch Herrn Dr.  Theophil German  einfach nicht für diese Angelegenheit zuständig.

**False Positives:**

- `Dr.  Theophil German` — partial — gold is substring of pred: `Theophil German`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theophil German`(person)

**Example 12** (doc_id: `deanon_BFG_TRAIN/148201.1`) (sent_id: `deanon_BFG_TRAIN/148201.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Techn R Dr. Diego Wachsmann, Spetterbrücke 14, 9462 Schönberg, Österreich, über die Beschwerde vom 26. November 2024  gegen den Bescheid des Finanzamtes Österreich vom 19. November 2024 betreffend  Einkommensteuer 2023 Steuernummer 66-050/1184  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Dr` — partial — pred is substring of gold: `Techn R Dr. Diego Wachsmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Techn R Dr. Diego Wachsmann`(person)
- `Spetterbrücke 14, 9462 Schönberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `66-050/1184`(tax_number)

</details>

---

## `Frau Title Name Pattern`

**F1:** 0.026 | **Precision:** 0.277 | **Recall:** 0.014  

**Format:** `regex`  
**Rule ID:** `8ba4434c`  
**Description:**
Captures person names following 'Frau', strictly requiring a valid name pattern immediately after and stopping at non-name characters to avoid false positives like 'Frau Grundsteuer'.

**Content:**
```
\bFrau\s+([A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*(?:\s+(?:LL\.B\.?\s+LL\.M\.?|LL\.M\.?\s+LL\.B\.?|B\.Sc|B\.A|B\.Ed|MA|LLB|BEd|B\.Ed|Bakk\.\s+techn\.|Bakk\.\s+iur\.|Bakk\.\s+rer\.\s+\w+|MSc|MBA|Dr\.[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Mag\.[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Univ\.-Prof\.(?:in)?[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Priv\.-Doz\.(?:in)?[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Hon\.-Prof\.(?:in)?[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|StR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|KommR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|\u00d6kR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|VetR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Ing\.[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|OSR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|OMedR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|KzlR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|RgR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Techn\s+R[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|MedR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*))?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.277 | 0.014 | 0.026 | 101 | 28 | 73 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 28 | 73 | 1967 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/130035.1`) (sent_id: `deanon_BFG_TRAIN/130035.1_10`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrates der Stadt Wien vom 5. August 2020, GZ. MA6/100/2019  (vormals: MA 6/ARP u.a.), wurde Frau Hedwig Brumund, Sparstraße 5, 4212 Pernau, Österreich (in weiterer Folge:  Beschuldigte) schuldig erkannt, sie habe als verantwortliche Beauftragte der AG von  01.09.2017 bis 24.01.2018 vor der Liegenschaft in Adresse1 auf dem öffentlichen  Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustelleneinrichtungsfläche  (Aufstellung eines Gerüstes) im Ausmaß von 52,50 m2 vorgenommen gehabt, wobei sie hiefür  bis zum 24.01.2018 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `Hedwig Brumund` | `Hedwig Brumund` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `Sparstraße 5, 4212 Pernau, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130035.1`) (sent_id: `deanon_BFG_TRAIN/130035.1_99`)


Von der AG wurde mitgeteilt, dass Frau Hedwig Brumund  von der AG als verantwortliche Beauftragte  gemäß § 9 Abs. 2 Satz 2 VStG bestellt wurde (vgl. vorgelegtes Schreiben vom 24. März 2015, in  dem Hedwig Brumund  ihrer Bestellung zum verantwortlichen Beauftragten zugestimmt hat).

| Predicted | Gold |
|---|---|
| `Hedwig Brumund` | `Hedwig Brumund` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_5`)


Entscheidungsgründe  I. Verfahrensgang:  1. Aufgrund einer anonymen Anzeige im April 2013 wurden finanzpolizeiliche Ermittlungen  durchgeführt und erhoben, dass Frau Martha Michenfelder (= Beschwerdeführerin, Bf) das Fahrzeug der  Marke X1, FIN Nr1, Erstzulassung (EZ) 1.10.2012, mit dem deutschen Kennzeichen AA1, im  Inland verwendet.

| Predicted | Gold |
|---|---|
| `Martha Michenfelder` | `Martha Michenfelder` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/132294.1`) (sent_id: `deanon_BFG_TRAIN/132294.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Frau Balthasar Jamrus, Ameisbühel 21, 8673 Landau, Österreich  damals vertreten durch WT, über die  Beschwerden der Abgabepflichtigen   1. vom 15. Dezember 2014 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf (nunmehr Finanzamt Österreich) vom 22. Oktober 2014 über die  Abweisung ihres Antrages auf Bewilligung von Aussetzungen der Einhebung vom 30. Juli  2014 betreffend die Einkommens- und Umsatzsteuer 2005-2011  2.

| Predicted | Gold |
|---|---|
| `Balthasar Jamrus` | `Balthasar Jamrus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Ameisbühel 21, 8673 Landau, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/132617.1`) (sent_id: `deanon_BFG_TRAIN/132617.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Konrad Schneidewendt (= Beschwerdeführerin, Bf), geb. Juni 1998, hatte mit Formular Beih100 im  September 2019 für sich die Zuerkennung der Familienbeihilfe (FB) wegen "Ausbildung" bzw.  "Lehre" mit einer voraussichtlichen Dauer bis 28.1.2022 beantragt.

| Predicted | Gold |
|---|---|
| `Konrad Schneidewendt` | `Konrad Schneidewendt` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_5`)


Im April 2012 hatte Frau Ute Kirchhoefel (= Beschwerdeführerin, Bf) eine Erklärung über die  Normverbrauchsabgabe (NoVA) und über den Erwerb neuer Fahrzeuge  (Fahrzeugeinzelbesteuerung) zum Fahrzeug MarkeX, FahrgestellNr. (FIN) 111xx, Leistung 90  kW, Benziner, CO²-Emission 144 g/km, Erwerb 30.10.2009, beim Finanzamt eingereicht;

| Predicted | Gold |
|---|---|
| `Ute Kirchhoefel` | `Ute Kirchhoefel` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_50`)


4. In dem dagegen fristgerecht eingebrachten Vorlageantrag vom 01.04.2020 wurde zunächst  auf die beiden Beschwerden verwiesen und weiter vorgebracht:  „Frau Reinhold Moellenkamp  ist Schweizer Staatsbürgerin.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_60`)


Frau Reinhold Moellenkamp  hat auch einen starken persönlichen Bezug zur Schweiz.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_65`)


Der  anonymen Anzeige ist unschwer zu entnehmen, dass irgendjemand Frau Reinhold Moellenkamp  und Herrn  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_68`)


Nachdem Herr A. erst seit 23.5.2016 in Ort1 (Ö) wohnhaft ist, ist es ausgeschlossen, dass Frau  Reinhold Moellenkamp  seit 5-6 Jahren bei ihm in Ort1 (Ö) wohnhaft ist.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 10** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_70`)


Frau  Reinhold Moellenkamp  hat Herrn A. erst vor ca 4 - 5 Jahren kennengelernt.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 11** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_71`)


Nachdem sich diese  Freundschaft intensivierte, kam Herr A. zu Frau Reinhold Moellenkamp  nach Ort1 (CH).

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 12** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_74`)


Frau Reinhold Moellenkamp  hat immer wieder bei ihrem Freund, Herrn A., übernachtet;

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 13** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_77`)


Frau Reinhold Moellenkamp  ist weder Eigentümerin, Mieterin, Ehegattin oder  sonst irgendwie nachhaltig berechtigt, im Haus von Herrn A. zu übernachten oder es sonst wie  zu nutzen.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 14** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_81`)


Er hat  regelmäßig zu Mittag bei Frau Reinhold Moellenkamp  gegessen und auch immer wieder bei ihr genächtigt.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 15** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_82`)


Er hatte dort auch familiären Kontakt zur Mutter von Frau Reinhold Moellenkamp.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 16** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_83`)


Entweder schläft Frau  Reinhold Moellenkamp  bei Herrn A., oder Herr A. bei Frau Reinhold Moellenkamp  in der Schweiz.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 17** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_84`)


Auch die  Wochenenden werden sowohl in Vorarlberg als auch in der Schweiz verbracht, wobei  diesbezüglich auf die Angaben von Frau Reinhold Moellenkamp  anlässlich ihrer Einvernahme vom  18.11.2019 verwiesen wird.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 18** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_85`)


Als die Beziehung ein Level erreicht hat, bei dem es um die Planung einer gemeinsamen  Zukunft ging, haben Frau Reinhold Moellenkamp  und Herr A. beschlossen, einen Immobilienmakler zu  beauftragen um ein Haus in der Schweiz zu suchen, in das sie gemeinsam einziehen und einen  gemeinsamen Wohnsitz gründen wollten.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 19** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_88`)


Frau Reinhold Moellenkamp  ist daher zweifellos in Ort1 (CH) steuerlich ansässig.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 20** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dieter Papakiriakou` | `Dieter Papakiriakou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Theobald Korschinek` (person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich` (address)
- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 21** (doc_id: `deanon_BFG_TRAIN/139792.1`) (sent_id: `deanon_BFG_TRAIN/139792.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 5. Juli 2021 beantragte Frau Jasper Eisenhoefer, die Beschwerdeführerin, die  Rückzahlung des Betrages von 1.374,00 €.

| Predicted | Gold |
|---|---|
| `Jasper Eisenhoefer` | `Jasper Eisenhoefer` |

**Example 22** (doc_id: `deanon_BFG_TRAIN/145500.1`) (sent_id: `deanon_BFG_TRAIN/145500.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Thaddäus Kusmierek  in der Beschwerdesache Sven Attanasio,  Rumänien , vertreten durch Frau Felicitas Niedermann, Rechtsanwältin, CH-8590 Romanshorn,  betreffend Säumnisbeschwerde vom 13.6.2024 betreffend Einkommensteuer 2022  (Arbeitnehmerveranlagung) gegen die Amtspartei FA Tirol Ost  beschlossen:  Das Beschwerdeverfahren wird gem. § 284 Abs 2 BAO eingestellt.   Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Felicitas Niedermann` | `Felicitas Niedermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Thaddäus Kusmierek` (person)
- `Sven Attanasio` (person)
- `FA Tirol Ost` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 23** (doc_id: `deanon_BFG_TRAIN/145907.1`) (sent_id: `deanon_BFG_TRAIN/145907.1_16`)


Im Vorlagebericht hat das Finanzamt unter Sacherhalt  ausgeführt:   „Sachverhalt:   Frau Adelheid Strehler  erhält regelmäßige Zahlungen aus dem Tronc (Trinkgeldkasse).

| Predicted | Gold |
|---|---|
| `Adelheid Strehler` | `Adelheid Strehler` |

**Example 24** (doc_id: `deanon_BFG_TRAIN/145907.1`) (sent_id: `deanon_BFG_TRAIN/145907.1_24`)


Im Vorlageantrag macht Frau Adelheid Strehler  die Steuerfreistellung der Trinkgelder geltend.

| Predicted | Gold |
|---|---|
| `Adelheid Strehler` | `Adelheid Strehler` |

**Example 25** (doc_id: `deanon_BFG_TRAIN/146516.1`) (sent_id: `deanon_BFG_TRAIN/146516.1_10`)


Mit drei Strafverfügungen vom 1) 24. September 2024, 2) und 3) 17. September 2024 wurde  der nunmehrigen Beschwerdeführerin (kurz: Bf.), Frau Dalibor Schlagböhmer  angelastet, sie habe als zur  Vertretung nach außen berufene Person der Zulassungsbesitzerin (Firma Firma) des in Rede  stehenden Fahrzeuges dem jeweils ordnungsgemäß zugestellten Verlangen der MA 67 vom 1)  10. Juli 2024, 2) 01. Juli 2024 und 3) 03. Juli 2024, jeweils innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem dieses Fahrzeug zu den genannten Zeitpunkten überlassen  worden sei, sodass dieses bei den genannten Örtlichkeiten gestanden sei, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Dalibor Schlagböhmer` | `Dalibor Schlagböhmer` |

**Example 26** (doc_id: `deanon_BFG_TRAIN/147375.1`) (sent_id: `deanon_BFG_TRAIN/147375.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Frau Enrico Landfried (Beschwerdeführerin, Bf.) betreibt am Standort Karl Kleinrath-Weg 5 - 8, 8010 Hönigtal, Österreich  einen  Gewerbebetrieb und wurde für die Jahre 2021 bis 2023 einer Lohnabgabenprüfung (PLB)  unterzogen.

| Predicted | Gold |
|---|---|
| `Enrico Landfried` | `Enrico Landfried` |

**Missed by this rule (FN):**

- `Karl Kleinrath-Weg 5 - 8, 8010 Hönigtal, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_44`)


Demnach war Frau RgR Univ.-Prof.in KommR Corinna Bebenek  von 01.12.2010 bis zum 29.02.2012 bei A R. als  Dienstnehmerin beschäftigt.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_46`)


Frau Bf war laut  Gewerberegisterauszug gewerberechtliche Geschäftsführerin im Mietwagengewerbe vom  07.12.2010 bis zum 07.02.2012.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_50`)


Aus den gewerberechtlichen Unterlagen ist ersichtlich, dass Frau Bf von 05.05.2011 bis  23.02.2012 auch gewerberechtliche Geschäftsführerin betreffend das Taxigewerbe mit den  Standorten X., Y. und Z. war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_63`)


Der  Abfluss von Bargeldbeständen wurde unter anderem damit erklärt, dass Frau Bf zusätzliche  Gelder erhalten hätte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_69`)


„Frau RgR Univ.-Prof.in KommR Corinna Bebenek  war von 1.12.2010 bis 29.02.2012 bei A R. als Dienstnehmerin  (Dienstgeberkonto lautend auf Personenbeförderung W T.) beschäftigt.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_72`)


Laut Gewerberegisterauszug war Frau Bf gewerberechtliche Geschäftsführerin im  Mietwagengewerbe für die Standorte Y., X. und Z. vom 7.12.2010 bis zum 23.2.2012.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_75`)


Aus den gewerberechtlichen Unterlagen ist ersichtlich, dass Frau Bf vom 5.5.2011 bis  23.02.2012 auch gewerberechtliche Geschäftsführerin betreffend das Taxigewerbe mit den  Standorten X., Y. und Z. war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_77`)


Bei der Einvernahme der Frau RgR Univ.-Prof.in KommR Corinna Bebenek  am 2.12.2013 am FA U. P. R als Zeugin wurden  folgende Unterlagen übergeben: Jahreslohnkonten, Auszug Gewerbeberechtigungen  Taxigewerbe und Mietwagengewerbe, Stundenaufzeichnung Dezember 2010, händische  Auszahlungslisten Mai, Juni, Juli, August, September, Oktober 2011 und Übersicht  Auszahlungsliste Februar 2012 und oa. Sachverhalt mitgeteilt.  Für die Behörde ist in freier Würdigung der der Beschwerdeführerin zur Kenntnis gebrachten  Beweismittel erwiesen, dass Frau RgR Univ.-Prof.in KommR Corinna Bebenek  für die zur Verfügungstellung der Taxikonzession  zusätzlich zu den am Lohnkonto ausgewiesenen Beträge € 7.000,- in bar übergeben wurden.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `Rg` — similar text (different position): `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)
- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 8** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_181`)


Seite des Protokolls der  Zeugeneinvernahme von Frau Bf befindet sich eine Stundenaufzeichnung über angebliche  Leistungen der Frau Bf im Dezember 2010.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 9** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_183`)


Es bedarf mE keiner graphologischen  Fachkenntnis, um festzustellen, dass die hier aufscheinende Unterschrift sich von jenen  unterscheidet, welche im Steuerakt der Frau Bf und auf bei mir befindlichen Unterlagen  mehrmalig aufscheint.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_196`)


Die Beschwerdeführerin  bestreitet jedoch wiederholt die Korrektheit einer Stundenaufzeichnung über angebliche  Leistungen der Frau Bf im Dezember 2010, welche jedoch nicht Grundlage für die  Abgabenfestsetzung war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/129437.1`) (sent_id: `deanon_BFG_TRAIN/129437.1_16`)


Eine weitere Bestätigung der X- Versicherung a.G. vom 2.5.2019 enthält folgenden Passus: „…Da Sie und Ihre Frau Ihren  Wohnsitz ins Ausland verlegt haben, unterliegen Sie nicht der Versicherungspflicht in  Deutschland.

**False Positives:**

- `Ihren  Wohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Margot Artner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Margot Artner`(person)

**Example 13** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Grillenreith`(city)

**Example 14** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 15** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 16** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_93`)


Im Antwortschreiben vom 7.12.2020 wird seitens der Bf ausgeführt:  " … Ad 1) Frau Dl Bf hat im strittigen Zeitraum ab Oktober 2012 nach ihren Angaben und nach  ihrer Erinnerung mehrmals monatlich die Strecke D/Y (Hauptwohnsitz) nach A/X  (Nebenwohnsitz) zurück gelegt.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_97`)


Herr und Frau Bf besuchen dort  gemeinsam Restaurants, das FitnessCenter, Ärzte oder absolvieren Theaterbesuche.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_98`)


In Land3 besitzt Frau Dl Bf ein Haus, das sie alle ca. 6 Wochen im Jahr für einige Tage entweder  allein oder mit ihrem Gatten aufsucht.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_103`)


Überdies besitzt es einen großen Obstgarten mit ca. 800 m2 (Kirschen, Äpfel,  Pflaumen, Walnüsse), die jedes Jahr von Frau Dl Bf selbst geernet werden.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_104`)


Anmerkungen:  Der Vollständigkeit halber möchten wir festhalten, dass Frau Dl Bf immer ihren Hauptwohnsitz  in Deutschland, D/Z bzw. D/Y, hatte.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_111`)


Frau Dl Bf ist und war ausschließlich in Deutschland versichert, bezahlt ihre Steuern nur in  Deutschland und war stets in Deutschland beschäftigt (XX) und wohnhaft (Hauptwohnsitz).

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_114`)


Herr C ist 1985  nach Österreich zurückgekehrt, Frau Bf hat ihren deutschen Hauptwohnsitz hingegen  beibehalten.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_117`)


Nach ihrer Pensionierung ist Frau Dl Bf von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_122`)


Frau Dl Bf hat sich immer wieder in A/X aufgehalten.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_125`)


Frau Dl Bf hat nie die Aussage getätigt, dass sie sich zu irgend einem Zeitpunkt überwiegend in  Österreich aufhält. Dies wäre schlichtweg falsch.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/133721.1`) (sent_id: `deanon_BFG_TRAIN/133721.1_548`)


Relevantes daraus (siehe auch Abschnitt H/k):  Aus Seite 10 f. des ersten Teiles (vor Schriftführerwechsel) des Protokolles über den ersten  Verhandlungstag 22.6.2011: Die vorsitzende Richterin hielt dem Angeklagten (GesGf1) ein  Gespräch mit Frau Lohnbüro vor, deren Lohnbüro sich mit der Verwaltung der Arbeiter der Fa.  41 von 75 Seite 42 von 75

**False Positives:**

- `Lohnbüro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/133721.1`) (sent_id: `deanon_BFG_TRAIN/133721.1_550`)


Der Angeklagte gab an, oft mit Frau Lohnbüro telefoniert zu haben, weil  GesGfSubUnt1 (Geschäftsführer der Fa. SubUnt1) selten erreichbar gewesen sei (zweimal pro  Woche) und den Angeklagten gebeten habe, die Urlaubsmeldungen der SubUnt1-Arbeiter dem  Lohnbüro Lohnbüro mitzuteilen.

**False Positives:**

- `Lohnbüro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_73`)


Erst vor ca 3 Jahren besuchte Frau Reinhold Moellenkamp  Herrn A. erstmals in Ort1  (Ö).

**False Positives:**

- `Reinhold Moellenkamp  Herrn` — partial — gold is substring of pred: `Reinhold Moellenkamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reinhold Moellenkamp`(person)

</details>

---

## `Anonymized Doctor Pattern`

**F1:** 0.005 | **Precision:** 0.100 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `da791678`  
**Description:**
Captures anonymized doctor names like 'Dr. B.' or 'Dr. A.' which are common in legal texts but missed by standard name patterns.

**Content:**
```
\bDr\.\s+[A-Z]\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.100 | 0.002 | 0.005 | 50 | 5 | 45 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 45 | 2005 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129907.1`) (sent_id: `deanon_BFG_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. R. in der Beschwerdesache Zarin Enneken,  Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 90-142/3945  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zarin Enneken` (person)
- `Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich` (address)
- `90-142/3945` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_61`)


II. Das Bundesfinanzgericht hat erwogen:  Mit Rechnung vom 31. August 2018 stellte Dr. R. Beratung & Coaching der Bf. für die  Teilnahme am Diplomlehrgang zum Relationalen Coach 2018/2019 € 9.900,00 in Rechnung.

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_63`)


Am 03. September 2018 überwies die Bf. von ihrem Konto € 6.000,00 auf das in der o.a.  Rechnung angegebene Konto Dr. R. (Bankbeleg).

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/138967.1`) (sent_id: `deanon_BFG_TRAIN/138967.1_137`)


Daran können  auch die Bestätigungen der Erlöse der drei Hauptkunden in Deutschland nichts ändern, zum  einen, da dadurch nicht ausgeschlossen wird, dass auch an andere Kunden Umsätze getätigt  wurden (worauf auch die mit „verschiedene Kunden" und „Dr. B." benannten Konten schließen  lassen), zum anderen war eine exakte Zuordnung der Rechnungsnummern bzw. Rechnungen  nicht möglich.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_526`)


Ebenso konnte aus dem Belegmaterial (OZ. 77) entnommen werden, dass die Bf. zahlreiche  Facharztbesuche, Physiotherapeuten, Heilpraktiker, ärztliche Labors (Re v. 22.8.2014,  1.10.2014 Dr. M., 30.10.2014 Dr. Sch., 30.10.2014 Dr. Sz., 16.1.2015 Dr. E., 26.1.2015 Dr. W.,  4.3.2015 Diagnostik M., 28.8.2015 Heilpraktikerin H., 14.12.2015 Heilpraktikerin H., 17.12.2015  Labor Dres., 30.12.2015 Heilpraktikerin H., 29.11.2016 Dr. E., 10.2.2017 Zahnarzt 4 Sitzungen,  21.3.2017 Facharzt 4 Sitzungen, 11.8.2017 Zahnarzt, 12.10.2017 Dr. E., 27.12.2017 Dr. B. 2  Sitzungen, absolviert hat.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Missed by this rule (FN):**

- `M.` (person)
- `M.` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_65`)


Beweis: als Zeugen Dr. P. - H. - M. - F. N.. Habe dann um 10:12 h den Verhandlungssaal verlassen und danach den Schuldnervertreter Mag. S. T. Y., danach habe ich den Masseverwalter und zuletzt den Steuerberater angerufen und von dem Vorfall beim Spruchsenat berichtet.

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_349`)


Mit der Vertragserrichtung beauftragt wurde Rechtsanwalt Dr. J. Dieser gilt als  Parteienvertreter iSd § 30c Abs. 3 EStG 1988, welcher unter den genannten Voraussetzungen  für die richtige Berechnung der strittigen Steuer haftet.

**False Positives:**

- `Dr. J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_20`)


Als Beilagen zu der Beschwerde wurden (Beil.1:) die Bestätigung der SRBV GmbH betreffend  verrechnete Leistungen im Jahr 2018 vom 23.01.2019, (Beil.2:) die Krankengeschichte samt  Stellungnahme der Bf. vom 13.09.2019, (Beil. 2/a:) der OP-Bericht des OA Dr. A., Herz Jesu-KH  vom 6.12.2001 (Operation an der Wirbelsäule), (Beil.2/b:) der Arztbrief des Prim. Univ.-Prof.  DDr. B., Unfallabteilung Landesklinikum Baden-Mödling vom 06.05.2013   (OP: Oberschenkelknochen- Bruch), (Beil.2/c:) die Niederschrift des Prim. Univ.- Prof. Dr. C.,  Evangelisches Krankenhaus vom 9.04.2014 zur Operation am Darm vom 8.04.2014,   AZ: 2014/XXXX, (Beil.2/d:) der Befundbericht Therapievorschlag des Dr. Med. Univ.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation
- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `SRBV GmbH`(organisation)
- `Prim. Univ.-Prof.  DDr. B.`(person)

**Example 3** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_24`)


Der Bericht des OA Dr. A., Herz Jesu-KH vom 6.12.2001 über die Operation der Bf. an der  Wirbelsäule vom Vortag (Beilage 2/a) lautet wie folgt:  „

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_39`)


Dem Ergänzungsersuchen entsprechend wurden dem Finanzamt die Bestätigung der Ärztin Dr.  E. vom 16.12.2019 mit Angaben der Diagnosen „kombiniertes Aortenklappenvitium“, „Axonale  PNP“ und „Zn DP 14 L5 mit Massenprolaps 2001“ als Beweis für die Bf. als eine  pflegebedürftige Patientin, der Residenzvertrag, Broschüren über „Pflegeaufenthalt“ und  „Dauerwohnen“, der Beleg über die von der SRBV mit der Bf. verrechneten Leistungen für das  Streitjahr sowie die Tarifliste betreffend die NÖ Pflege- und Betreuungszentren, NÖ Pflege- und  Förderzentren für das Jahr 2019, zur Entscheidung über die Beschwerde vorgelegt.

**False Positives:**

- `Dr.  E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_54`)


Laut der vorgelegten Arztbestätigung der Dr. E. vom 16.12.2019 sei die Bf. aufgrund der in dem  Schreiben genannten Diagnosen und ihrem Alter von 90 Jahren zwar pflegebedürftig, jedoch  liege ein detailliertes Gutachten trotz Aufforderung nicht vor.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_62`)


VwGH 30.06.2010, 2008/13/0145, VwGH 26.05.2010, 2007/13/0051, und die im  Schreiben von Dr. E. vom 16.12.2019 angeführten Leiden der Bf. wurde zum  "kombinierten Aortenklappenvitium" unter Verweis auf den Artikel von Franziska  Mettke, Ärztin, Dresden auf https: // befunddolmetscher.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_90`)


Angesichts der im  Schreiben von Dr. E. vom 16.12.2019 angesprochenen Diagnose "Zn DP 14 L5 mit  Massenprolaps 2001" erging das an die Bf. adressierte Ersuchen um Vorlage einer  Beschreibung der letztgenannten Krankheit, wobei diesen Ausführungen in Hinblick auf  die Unbekanntheit der Art und der Folgen dieser Erkrankung sämtliche der der Bf. zur  Verfügung stehenden Beweismittel (z.B. Befunde, Krankenhausergebnisse,  Testergebnisse, etc.) beizulegen wären.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_105`)


Mit Schreiben des BFG vom 26.02.2021 wurden das Schreiben der steuerlichen Vertreterin  vom 20.02.2021, der Befundbericht von Dr. E. vom 30.07.2020 (Kopie), der Röntgen-Befund  vom 25.04.2017, das VwGH-Erkenntnis vom 30.06.2010, 2008/13/0145 (Serie (erledigt im  gleichen Sinn): VwGH 30.06.2010, 2008/13/0126) und die UFS-Berufungsentscheidung vom  23.10.2012, RV/2933-W/12, an die Amtsvertretung weitergeleitet.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_145`)


Mit den Schreiben der die Bf. seit Jahren betreuenden und behandelnden Ärztin Dr. E. vom  16.12.2019 und 30.07.2020 ist der Amtsvertretung die Tatsache, dass die Bf. infolge der in den  Schreiben genannten Diagnosen und ihrem Alter im Jahr 2018 pflegebedürftig und ein Leben  ohne Unterstützung aufgrund der Erkrankungen an PNP und dem kombinierten Aortenvitium  unmöglich war, bestätigt worden.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_146`)


2. Beweiswürdigung  Die Sachverhaltsfeststellungen beruhen auf a) dem Bescheid, mit dem der Bf. Pflegegeld Stufe  1 zuerkannt worden ist, b) den Schreiben der langjährigen Hausärztin Dr. E. vom 16.12.2019  und 30.7.2020, c) dem Bericht des OA Dr. A., Herz Jesu-KH, vom 6.12.2001 über die Operation  an der Wirbelsäule vom Vortag (Beilage 2/a), d) dem Arztbrief des Prim. Univ.-Prof. DDr. B.,  Unfallabteilung, Landesklinikum Baden Mödling, betreffend die frakturbedingte Operation vom  6.05.2013, e) der Niederschrift des Prim. Univ.- Prof. Dr. C. , Evangelisches Krankenhaus, vom  9.04.2014 betreffend die Operation am Darm vom 8.04.2014, f) dem Röntgen-Befund der  Radiologischen Gruppenpraxis Baden OG vom 25.04.2017 (Wirbelsäule), g) dem Befundbericht  des Dr. Med. Univ.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation
- `Dr. A.` — no gold match — likely missing annotation
- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 11** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_150`)


Im Gegensatz zur steuerlichen Vertretung  vertritt die Amtsvertretung die Rechtsmeinung, dass die Bf. aufgrund der in der  Arztbestätigung der Dr. E. vom 16.12.2019 genannten Diagnosen und ihrem Alter zwar  pflegebedürftig sei, jedoch liege ein detailliertes Gutachten trotz Aufforderung nicht vor.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_214`)


Die  Verschlechterung des Gesundheitszustands wurde durch den nachfolgend abgelichteten  Befundbericht der Hausärztin Dr. E. vom 30.07.2020 bestätigt:   „

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_219`)


Angesichts der Eigenschaft der  Bf. als langjährige Patientin der Dr. E. war es der Allgemeinmedizinerin möglich, den  Befundbericht vom 30.07.2020 mit der Darstellung des Status und der Kontinuität der  Behandlung der Bf. zu erstellen und die Angaben durch Vorlage der der Krankengeschichte  beigelegten Beweismittel (a) OP-Bericht des OA Dr. A., Herz Jesu-KH, vom 6.12.2001,  b) Arztbrief des Prim. Univ.-Prof. DDr. B. vom 6.05.2013, c) Niederschrift des Prim. Univ.- Prof.  Dr. C., Evangelisches KH, vom 9.04.2014, d) Befundbericht des Dr. Med. Univ.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation
- `Dr. A.` — no gold match — likely missing annotation
- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 14** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_230`)


Den Bedenken der Amtsvertretung gegen den Befundbericht der Dr. E. war zu erwidern, dass  prinzipiell ein niedergelassener Arzt für Allgemeinmedizin der erste Ansprechpartner eines  Patienten ist, folglich dessen üblicherweise bei ihm die Dokumentation der ärztlichen  Leistungen betreffend den Patienten zusammenläuft.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/133679.1`) (sent_id: `deanon_BFG_TRAIN/133679.1_164`)


Zu der Zeit, als die Befragte im Labor des Bf tätig war, hätten  weitere immer unterschiedliche Ärzte in der Makroskopie gearbeitet, Dr. H, Dr. A (bis 2008  jeden Donnerstag), die angestellte Dr. C. Auf Grund der Haftung des Labors für falsche  Befundungen wären schwierige Fälle zB bei Tumoren von einer Fachärztin der Pathologie Dr. H  noch einmal begutachtet worden.

**False Positives:**

- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_12`)


300,93  km: 2.497,76   4.956,70  Weiters wurden vorgelegt:   - eine Aufstellung der geltend gemachten Fahrtkosten in Form von km-Geldern   - Listen über den Therapieablauf im Gesundheitszentrum Bad Sauerbrunn für Physiotherapien  und Heilmassagen im Zeitraum 06.02.2019 - 14.03.2019   - Rechnung Impuls Hotel Tirol Bad Hofgastein vom 08.04.2019 (an den Bf.)   - Therapieplan vom 27.03.2019 zur Stollentherapie 2019 im Gasteiner Heilstollen über acht  Einfahrten in der Zeit von 09.09.2019 - 21.09.2019   - Behandlungsbeitragsvorschreibungen der Versicherungsanstalt öffentlich Bediensteter (BVA)  des Jahres 2019 (an den Bf.)   - Honorarnote des Facharztes für physikalische Medizin und Rheumatologie Dr. P. vom  07.01.2019 samt Zahlungsbeleg   - Honorarnote der Fachärztin für Innere Medizin und Rheumatologie Dr. K. vom 14.05.2019   - Honorarnote der Fachärztin für Haut- und Geschlechtskrankheiten Dr. M. vom 24.07.2019  - Honorarnote des Ambulatoriums für medizinische und chemische Labordiagnostik vom  2 von 17 Seite 3 von 17

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. K.` — no gold match — likely missing annotation
- `Dr. M.` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `M.`(person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_53`)


Anbei übermittle ich ihnen den Arztbrief  sowie die ausgefüllten Kuranträge von Dr. P. und Dr. N.-S. und ersuche um Anerkennung der  außergewöhnlichen Belastung.“

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_54`)


Mit Schreiben vom 05.03.2021 ersuchte das Finanzamt den Bf. um Übermittlung der  Unterlagen, die er im Vorlageantrag erwähnt hatte (Arztbrief sowie die ausgefüllten  Kuranträge von Dr. P. und Dr. N.-S.).

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 19** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_58`)


Ich übersende ihnen nochmals die Kopie  betreffend Kuraufenthalt von Dr. P., Arztbrief Dr. K. sowie Ärztliche Verordnung vom Gasteiner  Heilstollen.“

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_60`)


X ja   Wann 2016, 2017, 2018   Wo Bad Hofgastein)   - Ärztliche Stellungnahme zu (Bf., Geburtsjahr) des Dr. P., Facharzt für physikalische Medizin,  Rehabilitation und Rheumatologie vom 07.01.2019:   Aktuelle Vorgeschichte – soweit antragsrelevant   Seit Jahren bekannte M. Bechterew Erkrankung seit Nov.

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 21** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_66`)


Patient ist heimfähig x ja, kurfähig x ja, benötigt Diät x ja,   ist gehfähig x ja, mit Hilfsmittel x nein, Rollstuhl x nein,   benötigt Begleitperson x nein,   benötigt fremde Hilfe (waschen, anziehen usw.) x nein,   benötigt Transport x nein   - Ärztliche Verordnung des Dr. med. univ. O., Facharzt für Physikalische und Rehabilitative  Medizin, Krankenanstalt Gasteiner Heilstollen, vom 09.09.2019 (bereits mit der Beantwortung  des Vorhalteschreibens vom 03.09.2020 vorgelegt)   - Arztbrief der Dr. K., Fachärztin für Innere Medizin und Rheumatologie, vom 14.05.2019  (Diagnose: Morbus Bechterew, akuter Schub)

**False Positives:**

- `Dr. K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_147`)


Bezüglich der Kur in Bad Hofgastein März-April 2019 legte der Bf. mit Antwortschreiben vom  16.05.2021 zum Vorhalt vom 05.03.2021 nicht nur den Antrag auf Rehabilitations-, Kur- bzw.  Erholungsaufenthalt vom 10.01.2019 vor, sondern auch die ärztliche Stellungnahme des Dr. P.,  Facharzt für physikalische Medizin, Rehabilitation und Rheumatologie vom 07.01.2019 (oben in  Punkt I. im Wesentlichen wiedergegeben): In dieser wird als antragsrelevante Diagnose  Morbus Bechterew (Erkrankung seit Nov. 2017) genannt und die Rehabilitation bzw. das  Kurheilverfahren für den Bewegungs- und Stützapparat bzw. den rheumatologischen  Formenkreis ausdrücklich in Bad Hofgastein Impuls Hotel Tirol inkl. Stolleneinfahrten  vorgeschlagen (mit dem Hinweis, dass der vorgeschlagene Ort nach Möglichkeit berücksichtigt  werde) samt Begründung für die vorgeschlagene Maßnahme (Verbesserung des AZ und der  Beweglichkeit, Maximierung der Alltagsaktivitäten, Reduktion der Schmerzmittel und  Krankenstände).

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_150`)


Außerdem geht aus der ärztlichen Stellungnahme des Dr. P. vom 07.01.2019 hervor, dass der  Bf. keine Begleitperson benötigt (vgl. oben in Punkt I.).

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_153`)


Weiters wurde ein Arztbrief der Dr. K., Fachärztin für Innere Medizin und Rheumatologie, vom  14.05.2019 vorgelegt.

**False Positives:**

- `Dr. K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_99`)


Von seinem Onkel, Herrn Dr. A. R., der ebenfalls in diesem Haus wohnt, sowie  seiner Schwester, Frau R. H., sei ihm mitgeteilt worden, dass der Autoschlüssel samt allen  Papieren seit Monaten verschwunden sei.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_148`)


Herr Dr. A. R., der Onkel des Bf, wohnhaft in Adresse hat im Schreiben vom 28. Dezember 2020  an das Bezirksgericht D iZm dem Verfahren über die Bestellung eines Erwachsenenvertreters  für Frau B. H. zum verfahrensgegenständlichen Fahrzeug ausgeführt:  „Mitunter setzt sich Frau B. H. in ihr in der K-Straße geparktes - offenbar unversperrtes - Kfz und  versucht dieses in Betrieb zu nehmen.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht D`(organisation)

**Example 27** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_157`)


Mit E-Mail vom 11. November 2024 hielt Herr Dr. A. R. gegenüber der belangten Behörde,  dieses Mal explizit im Zusammenhang mit dem Beschwerdeverfahren, fest:  „Über Ersuchen meines Neffen Antonia Adding  bestätige ich gerne die Richtigkeit meiner  seinerzeitigen Wahrnehmungen hinsichtlich des Kfz meiner Schwägerin B. H. (Alfa Romeo Grün,  an das Kennzeichen kann ich mich nicht mehr erinnern).

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Antonia Adding`(person)

**Example 28** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_185`)


In diesem Zusammenhang ist auch darauf hinzuweisen, dass dem Erwachsenenvertreter zum  Zeitpunkt seiner Eingabe vom 28. Jänner 2022 an die belangte Behörde die Angaben des Herrn  Dr. A. R. im Schreiben vom 28. Dezember 2020 (Fahrzeug zumindest 8 Monate lang nicht  bewegt;

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_189`)


In einer Gesamtbetrachtung der Umstände ist aufgrund der Aussagen der Auskunftspersonen  Dr. A. R. und R. H. sowie insbesondere der diesbezüglich übereinstimmenden Aufzeichnungen  der Meldungsleger der MA mit hoher Wahrscheinlichkeit davon auszugehen, dass das  Fahrzeug bereits im Februar 2020, dh Monate vor dem strittigen Vorschreibungszeitraum, an  der angegebenen Adresse abgestellt worden ist und in der Folge dort unverändert verblieben  ist.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Bf Parenthetical Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c15108ab`  
**Description:**
Captures person names following 'Bf.' or 'Bf' in parenthetical definitions (e.g., 'Bf. genannt) Name' or 'Bf) Name').

**Content:**
```
\b(?:Bf\.|Bf)\s*(?:genannt\s*)?\)?\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 295 | 0 | 295 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 295 | 2012 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/124843.1`) (sent_id: `deanon_BFG_TRAIN/124843.1_67`)


Der Text der Beschwerde lautet: „    Innerhalb offener Frist erheben wir im Namen von Herrn Bf Berufung gegen den „Bescheid   ü   ber die Festsetzung der Normverbrauchsabgabe f   ü   r den Zeitraum Seite 6 von 18 Mai 2012“  („N0VA-Beseheid“) vom 9.7.2012, der durch Bescheidbegr ü   ndung des Finanzamtes Bruck Eisenstadt Oberwart vom 13.7.2012 erg   ä   nzt und dessen Frist zur Berufung am 10.8.2012 auf den 30.9.2012 erstreckt wurde, und begehren die Herabsetzung der festgesetzten Normverbrauchsabgabe f   ü   r den Zeitraum Mai 2012 von EUR 19.131,60    um EUR 19.131,60 auf EUR 0,00.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/128975.1`) (sent_id: `deanon_BFG_TRAIN/128975.1_64`)


Tabelle der Bf  Die adaptierte Prognoserechnung weist einen kumulierten Überschuss von € + 13.576,00 aus.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/129005.1`) (sent_id: `deanon_BFG_TRAIN/129005.1_56`)


Desweiteren übermittelte der Bf. Zahlungsaufstellungen betreffend Strom, Miete, Gas, Telefon  und Internet.

**False Positives:**

- `Zahlungsaufstellungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/129033.1`) (sent_id: `deanon_BFG_TRAIN/129033.1_79`)


Diesem Schreiben fügte der Bf. Fotos der einzelnen aufgelisteten Ausstattungselemente bei.

**False Positives:**

- `Fotos` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_5`)


Dagegen hat die Bf. Beschwerde erhoben und ausgeführt, dass sie in Wien kein Grab gehabt  und es neu errichten habe lassen.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)
- `Mag. Wolfgang Freudelsperger`(person)
- `Finanzamtes Wien 1/23`(organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_63`)


Im gegenständlichen Fall wurden durch die Bf. Betriebsausgaben iHv Euro 180.000,00 geltend  gemacht, denen in der Rechnung der M-GmbH (Rechnungsdatum 8.3.2008) angeführte  Leistungen zugrunde lagen.

**False Positives:**

- `Betriebsausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_8`)


Zusätzlich übermittelte der Bf Kopien von sechs Bankbelegen, aus  1 von 6 Seite 2 von 6

**False Positives:**

- `Kopien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_11`)


Mit Schriftsatz vom 28.08.2013 erhob die steuerliche Vertretung des Bf Berufung gegen den  Einkommensteuerbescheid 2012 vom 23.08.2013 und beantragte, die Rückzahlung der  Notstandshilfe in Höhe von 12.383,52 € ebenso wie die in der Erklärung noch nicht geltend  gemachten Kurkosten in Höhe von 338,27 € sowie die pauschalen Diätkosten für  Zuckerkrankheit in Höhe von 840 € als außergewöhnliche Belastungen gemäß § 34 EStG zu  berücksichtigen.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_25`)


Aufgrund seiner Zuckerkrankheit machte der Bf Mehraufwendungen wegen  Krankendiätverpflegung in Höhe des Pauschbetrages als außergewöhnliche Belastungen  geltend.

**False Positives:**

- `Mehraufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_60`)


Wichtig sei im vorliegenden Verfahren nur die korrekte Leistungserbringung durch die Firma T  an den Bf.  Betreffend die Firma C GmbH führte der Bf. aus, dass am 29.11.2012 der Konkurs über das  Vermögen dieser Firma eröffnet und mangels Masse abgelehnt worden sei.

**False Positives:**

- `Betreffend` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_69`)


Im Zuge des Verfahrens legte der Bf. Kopien von folgenden Unterlagen vor:  An ihn gelegten Rechnungen der Firma T:  1.)

**False Positives:**

- `Kopien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_74`)


Weiters legte der Bf. Ablichtungen der Kasseneingangsbelege  der Firma T gerichtet an den Bf.  vor:  1.)

**False Positives:**

- `Ablichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_89`)


Bezüglich der Fremdleistungen der Firma C GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der C GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

**False Positives:**

- `Ablichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/129533.1`) (sent_id: `deanon_BFG_TRAIN/129533.1_7`)


Während seiner Dienstverrichtung in Österreich wurden dem Bf Stock Options und Restricted  Stock Units (RSU) gewährt, die er im Jahr 2011 ausübte.

**False Positives:**

- `Stock Options` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/129533.1`) (sent_id: `deanon_BFG_TRAIN/129533.1_12`)


Mit Schreiben vom 21.12.2012 erhob die steuerliche Vertretung des Bf Berufung gegen den  Einkommensteuerbescheid 2011 vom 21.11.2012 und begründete diese im Wesentlichen  damit, dass der Vorteil aus der Ausübung der Stock Options bzw RSUs sonstige Bezüge gemäß  § 67 Abs 1 EStG 1988 darstellte, der innerhalb des Jahressechstels mit dem begünstigten  Steuersatz von 6 % zu versteuern sei und dass für die Berechnung des Jahressechstels auch die  laufenden Bezugsteile einzubeziehen seien, die in Österreich nicht steuerpflichtig seien.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_228`)


Bf. Diagramme, technische Zeichnungen sowie Fotos vorgelegt.

**False Positives:**

- `Diagramme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_334`)


- Probetrocknungen in der Pilotanlage WJ 2011  Die nachgereichten Unterlagen enthalten keine weiterreichenden Informationen zu  eigenbetrieblich durchgeführten F&E-Aktivitäten der Bf.   Trotz konkreter Rückfrage wird nicht ausreichend beschrieben, welche Probetrocknungen im  Detail mit welcher technologischen Zielsetzung durchgeführt wurden.

**False Positives:**

- `Trotz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_337`)


- Fortsetzung der Probetrocknungen in der Pilotanlage WJ 2012  Die nachgereichten Unterlagen enthalten keine weiterreichenden Informationen zu  eigenbetrieblich durchgeführten F&E-Aktivitäten der Bf.   Die von der FFG am 25. Oktober 2016 gestellten Fragen blieben inhaltlich unbeantwortet.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_349`)


- Probetrocknungen im Serien-Prototypen WJ 2012   Die nachgereichten Unterlagen enthalten keine weiterreichenden Informationen zu  eigenbetrieblich durchgeführten F&E-Aktivitäten der Bf.   Die von der FFG am 25. Oktober 2016 gestellten Fragen blieben inhaltlich unbeantwortet.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/129671.1`) (sent_id: `deanon_BFG_TRAIN/129671.1_161`)


Bescheid über die Festsetzung des Zuschlages zum DB (DZ) für das Jahr 2010 in Höhe  von 150,06 €  Am 28.7.2011 erstattete die Bf Berufung gegen acht der zehn Bescheide vom 29.6.2011 – alle  ausgenommen der Bescheide betreffend der Säumniszuschläge.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_75`)


Bezüglich der unbaren Erlöse der AGMbH wurden vom Bf. Rechnungen an die Auftragsfirma  gelegt und diese auch verbucht.

**False Positives:**

- `Rechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_10`)


Das Finanzamt folgte dieser Feststellung und erließ für 2014 einen Haftungsbescheid gemäß  § 99 EStG 1988 und schrieb der Bf Abzugssteuer in Höhe von 10.140,00 Euro vor.

**False Positives:**

- `Abzugssteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_77`)


A habe bei  seiner Einvernahme bestätigt, dass er für die Bf Eisenbeton-Montagen mit vier Angestellten  durchgeführt habe.

**False Positives:**

- `Eisenbeton` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_16`)


Weiters   - das Jahreszeugnis vom 01. Februar 2019, wonach der Sohn der Bf. Schüler der 3BSI (dritte  Fachklasse) für den Lehrberuf Informationstechnologie-Technik war und die 3. Klasse  (12. Schulstufe) mit gutem Erfolg abschloss und zum Aufsteigen in die 4. Klasse (13. Schulstufe)  berechtigt war.

**False Positives:**

- `Schüler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_75`)


Die Geschäftsführung des den Diplomlehrgang veranstaltenden Instituts bestätigte der Bf.  Folgendes:  Gerne bestätige ich, Dr. …, Begründerin und Eigentümerin des Instituts für Relationale  Beratung (IRBW) und langjährige Coaching-Expertin, dass (die Bf.) die Coaching-Ausbildung in  unserem Institut absolviert hat.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/130413.1`) (sent_id: `deanon_BFG_TRAIN/130413.1_46`)


Gegen die Strafverfügung wurde vom Bf. Einspruch erhoben (E-Mail vom 29. Juli 2019) und die  Strafverfügung dem Grunde und der Höhe nach bestritten.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/130413.1`) (sent_id: `deanon_BFG_TRAIN/130413.1_105`)


Die Protokollliste wurde dem BFG am 6. Februar übermittelt.  Aus der Protokollliste geht hervor, dass der Meldungsleger KO am 27. März 2020 in der Xstraße  folgende Beanstandungen durchgeführt hat:  Xstraße *2 10:21 Uhr  Xstraße *1 10:26 Uhr (= Fahrzeug des Bf.)  Xstraße *3 10:33 Uhr  Der Bf. wurde zu der am 21. Juli 2020 anberaumten mündlichen Verhandlung zeitgerecht und  ordnungsgemäß geladen.

**False Positives:**

- `Xstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_131`)


Im Zuge des verwaltungsgerichtlichen Verfahrens wurde dem Bf Gelegenheit gegeben, dem  BFG ein fundiertes Sachverständigengutachten über den Wert der Liegenschaft  vorzulegen.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_10`)


Dagegen erhob die Bf. Beschwerde und brachte u.a. Folgendes vor:  "Der Sohn der Beschwerdeführerin, VN-Sohn NN, geboren am GEBURTSDATUM, hat im Jahr  2018 insgesamt einen Betrag von EUR 15.621,03 als Einkommen aus unselbstständiger  Erwerbstätigkeit bezogen;

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Complainant Name Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66b7aa44`  
**Description:**
Captures person names following 'in der Beschwerdesache', handling multi-word names (e.g., 'di Francesco') and academic suffixes.

**Content:**
```
in\s+der\s+Beschwerdesache\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+(?:di|de|der|von|zu|van|vanden|ter|ter\s+|da|della|del|des|dos|da\s+|di\s+|de\s+|der\s+|von\s+|zu\s+|van\s+|vanden\s+|ter\s+|ter\s+|da\s+|della\s+|del\s+|des\s+|dos\s+|da\s+))*[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+(?:LL\.B\.\s+LL\.M\.|LL\.M\.\s+LL\.B\.|LL\.B\.\s+LLB|LLB|LL\.M\.|MSc|MBA|MAS|BA|B\.Sc|B\.A|B\.Ed|MA|BEd|Bakk\.\s+techn\.|Bakk\.\s+iur\.|Bakk\.\s+rer\.\s+\w+)*))(?=[\s,;\n]|$|\s+KG|\s+Bf\.|\s+\.\s*$|\s+\(|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Judge Name Context Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9f823d7f`  
**Description:**
Captures person names immediately following 'Richter' or 'Richterin', ensuring the full name including titles and suffixes is captured.

**Content:**
```
(?:Richter|Richterin)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+)*(?:\s*,\s*(?:BA|BSc|B\.Sc|B\.A\.|Bakk\. rer\. nat\.|Dipl\.|Ing\.|B\.Sc\.))?)(?=\s*,|\s+\d|\s+\.|\s+\)|\s+\n|$)
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

## `Specific Academic Title Pattern (Mag.a/Dr.in)`

**F1:** 0.439 | **Precision:** 0.670 | **Recall:** 0.327  

**Format:** `regex`  
**Rule ID:** `81012d3c`  
**Description:**
Captures person names with German academic titles, strictly stopping before common legal nouns. Updated to include suffixes like ', BA', ', BSc', ', Bakk.' and handle complex title chains.

**Content:**
```
\b((?:Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Mag\.|Mag\.-Doz\.|Dr\.|Dr\.in|Hon\.-Prof\.|Hon\.-Prof\.in|RgR|DDr\.|DDr\.in|OStR|Dipl\. Kff\.|Ing\.|KommR|RA|VetR|Techn\. R)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+)*(?:\s*,\s*(?:BA|BSc|B\.Sc|B\.A\.|Bakk\. rer\. nat\.|Dipl\.|Ing\.))?)(?![\s,]*Vollmacht|\s+\d|\s+\.|\s+\)|\s+\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.670 | 0.327 | 0.439 | 982 | 658 | 324 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 658 | 324 | 1357 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128700.1`) (sent_id: `deanon_BFG_TRAIN/128700.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Imre Schmidl  in der Beschwerdesache [...], [...],  über die Beschwerde vom 12. Februar 2018 gegen den Bescheid des Finanzamtes Lilienfeld St.  Pölten vom 16. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Imre Schmidl` | `Dr. Imre Schmidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Konrad Conrady  in der Beschwerdesache  Prof.  Ashley Lauterwasser, Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich, über die Beschwerde vom 23. September 2016 gegen den Bescheid  des Finanzamtes Linz vom 25. August 2016 betreffend Einkommensteuer 2014 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Konrad Conrady` | `Univ.-Prof. Konrad Conrady` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ashley Lauterwasser` (person)
- `Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128709.1`) (sent_id: `deanon_BFG_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Felizitas Muendl, Bakk. phil., Güttling 9, 9321 Latschach, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Muendl, Bakk. phil.` (person)
- `Güttling 9, 9321 Latschach, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Walla` | `Mag. Dieter Walla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `M.` (person)
- `Bauermeister Getränke` (organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich` (address)
- `09-169/6729` (tax_number)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128894.1`) (sent_id: `deanon_BFG_TRAIN/128894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nancy Brandlmayr  in der Beschwerdesache der  Süd-Landwirtschaft, Freundling 10, 4190 Amesschlag, Österreich, über die Beschwerde vom 5. Juni 2019, beim zuständigen  Finanzamt eingelangt am 6. Juni 2019, gegen den Bescheid des Finanzamt Vorarlberg  vom 24. Mai 2019  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 (Steuernummer  82-615/9369 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung vom  3.September 2019 Folge gegeben;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Nancy Brandlmayr` | `Univ.-Prof.in Nancy Brandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Süd-Landwirtschaft` (organisation)
- `Freundling 10, 4190 Amesschlag, Österreich` (address)
- `Finanzamt Vorarlberg` (organisation)
- `82-615/9369` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl. Kff. Gwendolin Ziehr,  Reebokplatz 60, 4083 Gemersdorf, Österreich, vertreten durch BG&P Binder Grossek & Partner Steuerberatung und  Wirtschafts- prüfung GmbH, Neufeldweg 93, 8010 Graz, über die Beschwerden vom 10. Juni  2015 gegen die Bescheide des Finanzamtes Graz-Umgebung vom 14. April 2015 betreffend  Festsetzung des Dienstgeberbeitrages (DB) und des Zuschlages zum Dienstgeberbeitrag (DZ)  für die Jahre 2009, 2010, 2011, 2012 und 2013, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Emmerich Bleekmann` | `Mag. Emmerich Bleekmann` |
| `Dipl. Kff. Gwendolin Ziehr` | `Dipl. Kff. Gwendolin Ziehr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reebokplatz 60, 4083 Gemersdorf, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Dr. Gerlinde  Rieser` | `Dr. Gerlinde  Rieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raphael Skowroneck, MBA` (person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129068.1`) (sent_id: `deanon_BFG_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Jens Spilken, Hillere 22, 8453 Saggau, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-228/4517  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |
| `Mag. Achmed Ghazal Aswad` | `Mag. Achmed Ghazal Aswad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jens Spilken` (person)
- `Hillere 22, 8453 Saggau, Österreich` (address)
- `69-228/4517` (tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lubomir Baltßun` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Beate Melik  in der Beschwerdesache Techn R Dr.in Maria Repstock,  Silberrain 14a, 5542 Flachau, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Beate Melik` | `Priv.-Doz.in Beate Melik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Dr.in Maria Repstock` (person)
- `Silberrain 14a, 5542 Flachau, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129103.1`) (sent_id: `deanon_BFG_TRAIN/129103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache DDr. Rocco Bernhards, Obere Festwiese 8, 4863 Steindorf, Österreich, über die Beschwerde vom 18. Juli 2013 gegen den Bescheid des Zollamtes Linz Wels  vom 18. Juni 2013 betreffend Vorschreibung eines Altlastenbeitrag für die Quartale 2-4 des  Jahres 2003 zu Recht erkannt:   Der angefochtene Bescheid wird hinsichtlich des Altlastenbeitrags - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `DDr. Rocco Bernhards` | `DDr. Rocco Bernhards` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obere Festwiese 8, 4863 Steindorf, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich` (address)
- `Eva Maria Koller-Rohrschach` (person)
- `84-986/6948` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_18`)


Nur dem Dienstnehmer AB, welcher der Sohn des Einzelunternehmers OStR Karl Ostendarp  ist, wurde  unterstellt, diese Fahrzeuge auch für private Zwecke zu nutzen.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Example 13** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_46`)


3) Die Fahrzeuge wurden nach Dienstende am Firmensitz: Adresse abgestellt. Die  Fahrzeugschlüssel und Papiere wurden von Herrn OStR Karl Ostendarp  oder Frau AB persönlich  entgegengenommen und im Büro versperrt aufbewahrt.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Example 14** (doc_id: `deanon_BFG_TRAIN/129168.1`) (sent_id: `deanon_BFG_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  Dolores Jodjürgis, BA MBA, Feldsiedlung 87, 5242 Obereck, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dolores Jodjürgis, BA MBA` (person)
- `Feldsiedlung 87, 5242 Obereck, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129231.1`) (sent_id: `deanon_BFG_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Bartholomäus Malcharzik, Ogugasse 8, 4483 Pirchhorn, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Elisabeth Traxler` | `Mag. Elisabeth Traxler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bartholomäus Malcharzik` (person)
- `Ogugasse 8, 4483 Pirchhorn, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |
| `Mag. Wolfgang Freudelsperger` | `Mag. Wolfgang Freudelsperger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janis Dollnig` (person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129379.1`) (sent_id: `deanon_BFG_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Johanna Harazin  in der Beschwerdesache des  Konstanze Seyfrieds, Rudolf-von-Gutmann-Straße 19, 9545 Dabor, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Bruck Eisenstadt Oberwart  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Johanna Harazin` | `Univ.-Prof.in Johanna Harazin` |
| `Mag. Hermann Rupert Zittmayr` | `Mag. Hermann Rupert Zittmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Konstanze Seyfrieds` (person)
- `Rudolf-von-Gutmann-Straße 19, 9545 Dabor, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129421.1`) (sent_id: `deanon_BFG_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Konepatzki  in der Beschwerdesache KommR MedR Jeannine Wegerhoff,  Burleiten 563, 9423 Matschenbloch, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Jacqueline Konepatzki` | `Univ.-Prof.in Jacqueline Konepatzki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR MedR Jeannine Wegerhoff` (person)
- `Burleiten 563, 9423 Matschenbloch, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129437.1`) (sent_id: `deanon_BFG_TRAIN/129437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alexandra Halbmeyer  in der Beschwerdesache des  Dragan Cayci, Ronklerbrunnen 5, 3860 Haslau, Österreich, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamt Gmunden Vöcklabruck  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Alexandra Halbmeyer` | `Hon.-Prof.in Alexandra Halbmeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dragan Cayci` (person)
- `Ronklerbrunnen 5, 3860 Haslau, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)

**Example 20** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Danelzik` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 21** (doc_id: `deanon_BFG_TRAIN/129520.1`) (sent_id: `deanon_BFG_TRAIN/129520.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Verwaltungsstrafsache  gegen KzlR Wolf Wältl, MBA, Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich, über die Beschwerde des Beschuldigten vom 26. März 2020  gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 10. März 2020, Zahl:  MA67/196700631216/2019, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Wolf Wältl, MBA` (person)
- `Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/129555.1`) (sent_id: `deanon_BFG_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache ÖkR Nadine Fritzekötter, Fahnbach 3, 3752 Nonnersdorf, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Nadine Fritzekötter` (person)
- `Fahnbach 3, 3752 Nonnersdorf, Österreich` (address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Reinhard Komarova, Gabrielweg 4, 4725 Adelsgrub, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 92-139/9763  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reinhard Komarova` (person)
- `Gabrielweg 4, 4725 Adelsgrub, Österreich` (address)
- `92-139/9763` (tax_number)

**Example 24** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 25** (doc_id: `deanon_BFG_TRAIN/129671.1`) (sent_id: `deanon_BFG_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Katharina Stäubling  in der Beschwerdesache Rüterborries+Friderich Möbel,  General-Arnold-Straße 13, 9111 Dobrowa, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Katharina Stäubling` | `Priv.-Doz.in Katharina Stäubling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rüterborries+Friderich Möbel` (organisation)
- `General-Arnold-Straße 13, 9111 Dobrowa, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/129733.1`) (sent_id: `deanon_BFG_TRAIN/129733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Wilfried Wedral  in der Beschwerdesache Ramona Goedeken,  Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich, vertreten durch Union TAX&LAW, Donau-City-Straße 7, DV Tower/30th floor,  1220 Wien, über die Beschwerde vom 16. April 2019 gegen den Bescheid des Finanzamtes  Innsbruck vom 19. März 2019 betreffend Familienbeihilfe (Ausgleichszahlung) für die Monate  Jänner 2015 bis Dezember 2017, [Ordnungsbegriff],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Wilfried Wedral` | `Hon.-Prof. Wilfried Wedral` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ramona Goedeken` (person)
- `Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/129778.1`) (sent_id: `deanon_BFG_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache VetR Silvester Johäntges, Fischauer Gasse 37, 4616 Hetzendorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 25-402/5507  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `VetR Silvester Johäntges` | `VetR Silvester Johäntges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Fischauer Gasse 37, 4616 Hetzendorf, Österreich` (address)
- `25-402/5507` (tax_number)

**Example 28** (doc_id: `deanon_BFG_TRAIN/129789.1`) (sent_id: `deanon_BFG_TRAIN/129789.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über den Antrag der  Rebecca Sümnicht, Haselgraben 126, 4083 Hinterberg, Österreich, vertreten durch BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, QBC 4 – Am Belvedere 4, 1100 Wien, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer  für das Jahr 2014 erhobenen ordentlichen Revision vom 24. Juni 2020 die aufschiebende  Wirkung zuzuerkennen, beschlossen:  Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rebecca Sümnicht` (person)
- `Haselgraben 126, 4083 Hinterberg, Österreich` (address)
- `BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_TRAIN/129828.1`) (sent_id: `deanon_BFG_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Pascal Beerlage, Tannwaldweg 35L, 9133 Jerischach, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 13-489/9399  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |
| `Dr. Helmut Herbert Moritz` | `Dr. Helmut Herbert Moritz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pascal Beerlage` (person)
- `Tannwaldweg 35L, 9133 Jerischach, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `13-489/9399` (tax_number)

**Example 30** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Cedric Leutheusser, Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |
| `Mag. Cedric Leutheusser` | `Mag. Cedric Leutheusser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 31** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr.in Ljiljana Kos` | `Dr.in Ljiljana Kos` |
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Example 32** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Example 33** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

| Predicted | Gold |
|---|---|
| `Dr. Sasan Hamzavi` | `Dr. Sasan Hamzavi` |

**Example 34** (doc_id: `deanon_BFG_TRAIN/130024.1`) (sent_id: `deanon_BFG_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Marlon William, J. Ranzoni-Straße 1L, 9554 Reggen, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marlon William` (person)
- `J. Ranzoni-Straße 1L, 9554 Reggen, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 35** (doc_id: `deanon_BFG_TRAIN/130034.1`) (sent_id: `deanon_BFG_TRAIN/130034.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache des Karina Wissmann, Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich, betreffend eine  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, über die Beschwerde vom 16. Juli 2020 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 –  Parkraumüberwachung, als Abgabenstrafbehörde vom 18. Juni 2020, Zahl MA67/Zahlzu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde vom  16. Juli 2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  – Parkraumüberwachung, MA67/Zahl, vom 18. Juni 2020 als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Wissmann` (person)
- `Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 36** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Julia Schulteß, Anton-Sattler-Gasse 42, 3531 Brand, Österreich, vertreten durch Mag. Anton Heisinger,  Mühlallee 1, 7301 Deutschkreutz, über die Beschwerde vom 29. Februar 2016 gegen den  Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 29. Jänner 2016 betreffend Haftung  gemäß § 99 EStG 1988 für den Zeitraum 2014 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Anton Heisinger` | `Mag. Anton Heisinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Julia Schulteß` (person)
- `Anton-Sattler-Gasse 42, 3531 Brand, Österreich` (address)

**Example 37** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Esmeralda Lubert, Kaschlgasse 9, 3100 Witzendorf, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esmeralda Lubert` (person)
- `Kaschlgasse 9, 3100 Witzendorf, Österreich` (address)
- `Sigrid Lamböck` (person)

**Example 38** (doc_id: `deanon_BFG_TRAIN/130367.1`) (sent_id: `deanon_BFG_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Petra Ullemeyer, Mariexner Straße 8, 3141 Rassing, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Petra Ullemeyer` (person)
- `Mariexner Straße 8, 3141 Rassing, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daisy Mikoleizik` (person)
- `Schulwiesen 13, 4203 Stratreith, Österreich` (address)

**Example 40** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 41** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 42** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  KzlR Leroy Krätschmar, Hohe Wand-Str. 12, 8345 Krusdorf, Österreich, über die Beschwerde vom 29. Mai 2019 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 30. April 2019 betreffend Rückforderung der  für VN-Sohn NN für den Zeitraum Jänner 2018 bis Dezember 2018 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Leroy Krätschmar` (person)
- `Hohe Wand-Str. 12, 8345 Krusdorf, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 43** (doc_id: `deanon_BFG_TRAIN/130444.1`) (sent_id: `deanon_BFG_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Lars Hoerl  in der Beschwerdesache VetR Christina Schlotfeldt,  Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Lars Hoerl` | `Hon.-Prof. Lars Hoerl` |
| `VetR Christina Schlotfeldt` | `VetR Christina Schlotfeldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich` (address)

**Example 44** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Cevik  in der Beschwerdesache der Bf., (im  Beschwerdeverfahren) vertreten durch Rechtsanwälte Lehofer & Lehofer,  Kalchberggasse 6/1.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lubomir Cevik` | `Priv.-Doz. Lubomir Cevik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 45** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marlies Danzfuss, BSc` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

**Example 46** (doc_id: `deanon_BFG_TRAIN/130536.1`) (sent_id: `deanon_BFG_TRAIN/130536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Baumgartner über die  Beschwerde des Arabella Neunhöfer, Hohlen 11, 8786 Klamm, Österreich, vom 22. Juni 2020, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 19. Mai 2020, MA67/000/2020,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006 zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Christian Baumgartner` | `Mag. Christian Baumgartner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Arabella Neunhöfer` (person)
- `Hohlen 11, 8786 Klamm, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_BFG_TRAIN/130559.1`) (sent_id: `deanon_BFG_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Julia Nöllecke  in der Beschwerdesache Esra Leßnick, LLB,  Hackermillerstraße 133, 8940 Döllach, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  06-833/3820, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Julia Nöllecke` | `Univ.-Prof.in Julia Nöllecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esra Leßnick, LLB` (person)
- `Hackermillerstraße 133, 8940 Döllach, Österreich` (address)
- `Mag. András Radics` (person)
- `Finanzamt Wien` (organisation)
- `06-833/3820` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 48** (doc_id: `deanon_BFG_TRAIN/130601.1`) (sent_id: `deanon_BFG_TRAIN/130601.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde des  Isolde Muegge, August-Riener-Gasse 18, 8511 Zirknitz, Österreich, Deutschland, vom 1. Juli 2020, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 16. Dezember 2019,  MA67/186700129131/2018, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung iVm § 4 Abs. 1 Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Irene Kohler` | `Mag. Irene Kohler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Isolde Muegge` (person)
- `August-Riener-Gasse 18, 8511 Zirknitz, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 49** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Paula Jagiella, Medienpark 18, 3384 Eidletzberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paula Jagiella` (person)
- `Medienpark 18, 3384 Eidletzberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 50** (doc_id: `deanon_BFG_TRAIN/130631.1`) (sent_id: `deanon_BFG_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Denise Stegger  in der Verwaltungsstrafsache gegen  Helge Toennesmann, Hadersfelderweg 5, 8511 Lichtenhof, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Denise Stegger` | `Univ.-Prof.in Denise Stegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Helge Toennesmann` (person)
- `Hadersfelderweg 5, 8511 Lichtenhof, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 51** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Dr. Elke Hager` | `Dr. Elke Hager` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wladimir Nüssli` (person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich` (address)

**Example 52** (doc_id: `deanon_BFG_TRAIN/130686.1`) (sent_id: `deanon_BFG_TRAIN/130686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde der  Alana Single, Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich, vom 19. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 17. August 2020, Zahl MA67/Zahl/2019, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alana Single` (person)
- `Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 53** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Matthäus Buskens` (person)
- `Edlach 19, 3141 Oberkilling, Österreich` (address)
- `Helmut Binder` (person)

**Example 54** (doc_id: `deanon_BFG_TRAIN/130748.1`) (sent_id: `deanon_BFG_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Valentina Cagli, A. Böhm Gasse 67F, 4310 Oberzirking, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 76-512/9228  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentina Cagli` (person)
- `A. Böhm Gasse 67F, 4310 Oberzirking, Österreich` (address)
- `76-512/9228` (tax_number)

**Example 55** (doc_id: `deanon_BFG_TRAIN/130754.1`) (sent_id: `deanon_BFG_TRAIN/130754.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Madeleine Uhlmer  in der Verwaltungsstrafsache  Waldemar Beimfohr, Ried Zephirau 9, 4894 Obernberg, Österreich, 1.) über die Beschwerde vom 19.06.2020 gegen die Strafverfügung  des Magistrats der Stadt Wien vom 30.12.2019, zugestellt am 27.02.2020, Geschäftszahl  MA67/196701166656/2019, und 2.) über die Beschwerde vom 19.06.2020 gegen die Strafver- fügung des Magistrats der Stadt Wien vom 20.01.2020, zugestellt am 03.03.2020, Geschäfts- zahl MA67/196701283117/2019, beschlossen:    Die Beschwerden werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Madeleine Uhlmer` | `Priv.-Doz.in Madeleine Uhlmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waldemar Beimfohr` (person)
- `Ried Zephirau 9, 4894 Obernberg, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt Wien` (organisation)

**Example 56** (doc_id: `deanon_BFG_TRAIN/130759.1`) (sent_id: `deanon_BFG_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Justin Feuerheerdt, Naglergasse 6, 4794 Grafendorf, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Justin Feuerheerdt` (person)
- `Naglergasse 6, 4794 Grafendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 57** (doc_id: `deanon_BFG_TRAIN/130804.1`) (sent_id: `deanon_BFG_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Siegfried Wigandt, Ober dem Marktplatz 120, 6870 Reuthe, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Irene Kohler` | `Mag. Irene Kohler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Wigandt` (person)
- `Ober dem Marktplatz 120, 6870 Reuthe, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 58** (doc_id: `deanon_BFG_TRAIN/130834.1`) (sent_id: `deanon_BFG_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich` (address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich` (address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich` (address)
- `BKS Steuerberatungs GmbH` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Baden Mödling` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 59** (doc_id: `deanon_BFG_TRAIN/131046.1`) (sent_id: `deanon_BFG_TRAIN/131046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Hugo Moewius, Studenygasse 11, 4623 Buchleiten, Österreich, vertreten durch SCHIETZ + MAUREDER Steuerberatung GmbH,  Veldner Straße 29, 4120 Neufelden, über die Beschwerde vom 20. Juni 2017 gegen den  Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 9. Juni 2017 betreffend  Einkommensteuer 2015 Steuernummer 03-874/1042  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hugo Moewius` (person)
- `Studenygasse 11, 4623 Buchleiten, Österreich` (address)
- `03-874/1042` (tax_number)

**Example 60** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Silvia Geidies, Schönengrund 34, 4209 Innertreffling, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 17-823/0942  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Geidies` (person)
- `Schönengrund 34, 4209 Innertreffling, Österreich` (address)
- `17-823/0942` (tax_number)

**Example 61** (doc_id: `deanon_BFG_TRAIN/131110.1`) (sent_id: `deanon_BFG_TRAIN/131110.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Renate Stoesser  in der Beschwerdesache der  Vossbein Lebensmittel, Truckenstetten 116, 4064 Oberbachham, Österreich, über die Beschwerde vom 4. November 2019 gegen die Bescheide  des Finanzamt Klagenfurt St. Veit Wolfsberg  vom 30. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017 zur Steuernummer 99-999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Renate Stoesser` | `Dr.in Renate Stoesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Vossbein Lebensmittel` (organisation)
- `Truckenstetten 116, 4064 Oberbachham, Österreich` (address)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 62** (doc_id: `deanon_BFG_TRAIN/131225.1`) (sent_id: `deanon_BFG_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Wendelin Dumröse, Dr.-Werner-Gasse 41, 5143 Otterfing, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendelin Dumröse` (person)
- `Dr.-Werner-Gasse 41, 5143 Otterfing, Österreich` (address)

**Example 63** (doc_id: `deanon_BFG_TRAIN/131299.1`) (sent_id: `deanon_BFG_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Othmar Misch, Freitzenschlag 122, 4723 Dopl, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 35-689/1540  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Zwilling` | `Mag. Josef Zwilling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Othmar Misch` (person)
- `Freitzenschlag 122, 4723 Dopl, Österreich` (address)
- `35-689/1540` (tax_number)

**Example 64** (doc_id: `deanon_BFG_TRAIN/131341.1`) (sent_id: `deanon_BFG_TRAIN/131341.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Valentin Kottsiepen, Fratresstraße 24, 3814 Aigen, Österreich, betreffend Beschwerde vom 23. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 1/23 vom 3. Februar 2016 betreffend   Haftung zur Einbehaltung und Abfuhr der Lohnsteuer, Festsetzung des Dienstgeberbeitrages  (DB) und Festsetzung des Zuschlags zum Dienstgeberbeitrag (DZ) für die Kalenderjahre 2010 bis  2014 sowie Festsetzung von Säumniszuschlägen für Lohnsteuer 2010 bis 2014,  Steuernummer 12-752/9462  beschlossen:  Die Beschwerde wird als gegenstandslos erklärt und das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentin Kottsiepen` (person)
- `Fratresstraße 24, 3814 Aigen, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `12-752/9462` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 65** (doc_id: `deanon_BFG_TRAIN/131365.1`) (sent_id: `deanon_BFG_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Mario Gajewska, Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mario Gajewska` (person)
- `Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 66** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Prof. Gernot Woortmann, Spitzbergweg 116, 3204 Tradigistgegend, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 16-817/8793  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Gernot Woortmann` (person)
- `Spitzbergweg 116, 3204 Tradigistgegend, Österreich` (address)
- `16-817/8793` (tax_number)

**Example 67** (doc_id: `deanon_BFG_TRAIN/131450.1`) (sent_id: `deanon_BFG_TRAIN/131450.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Carmen Wielander  in der Beschwerdesache Ulrich Hecktor,  St. Nikolaus Straße 16, 4904 Reichering, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 26. Februar 2020,  betreffend Rückforderung von Familienbeihilfe und Kinderabsetzbeträge für die Zeiträume  Oktober 2017 bis Juni 2019, zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Carmen Wielander` | `Priv.-Doz.in Carmen Wielander` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ulrich Hecktor` (person)
- `St. Nikolaus Straße 16, 4904 Reichering, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/102855.1`) (sent_id: `deanon_BFG_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr. Mag. Adrian Bembenick  in der Beschwerdesache Mag.a Julia Leitgöb, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. Adrian Bembenick`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mag. Adrian Bembenick`(person)
- `Mag.a Julia Leitgöb`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/124843.1`) (sent_id: `deanon_BFG_TRAIN/124843.1_0`)


GZ. RV/7100201/2013 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der Beschwerdesache Bf, Adr, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 01.10.2012 (datiert mit 28.9.2012) gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom Juli 2012 betreffend Festsetzung von Normverbrauchsabgabe für Mai 2012 in Höhe von € 19.131,60 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri. in der Beschwerdesache RgR Univ.-Prof.in KommR Corinna Bebenek, Teurniastraße 10, 6346 Hausern, Österreich, vertreten durch Alfred Klaus Fenzl, Am Steinbühel 27b, 4030 Linz, über die  Beschwerde vom 18. November 2013 gegen den Bescheid des Finanzamtes Linz vom  13. November 2013 betreffend Einkommensteuer 2011 und die Beschwerde vom 27. Jänner  2015 gegen den Bescheid vom 19. Jänner 2015 betreffend Einkommensteuer 2012 zu  Steuernummer 65-309/8174  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)
- `Teurniastraße 10, 6346 Hausern, Österreich`(address)
- `Alfred Klaus Fenzl`(person)
- `65-309/8174`(tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_44`)


Demnach war Frau RgR Univ.-Prof.in KommR Corinna Bebenek  von 01.12.2010 bis zum 29.02.2012 bei A R. als  Dienstnehmerin beschäftigt.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_69`)


„Frau RgR Univ.-Prof.in KommR Corinna Bebenek  war von 1.12.2010 bis 29.02.2012 bei A R. als Dienstnehmerin  (Dienstgeberkonto lautend auf Personenbeförderung W T.) beschäftigt.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_77`)


Bei der Einvernahme der Frau RgR Univ.-Prof.in KommR Corinna Bebenek  am 2.12.2013 am FA U. P. R als Zeugin wurden  folgende Unterlagen übergeben: Jahreslohnkonten, Auszug Gewerbeberechtigungen  Taxigewerbe und Mietwagengewerbe, Stundenaufzeichnung Dezember 2010, händische  Auszahlungslisten Mai, Juni, Juli, August, September, Oktober 2011 und Übersicht  Auszahlungsliste Februar 2012 und oa. Sachverhalt mitgeteilt.  Für die Behörde ist in freier Würdigung der der Beschwerdeführerin zur Kenntnis gebrachten  Beweismittel erwiesen, dass Frau RgR Univ.-Prof.in KommR Corinna Bebenek  für die zur Verfügungstellung der Taxikonzession  zusätzlich zu den am Lohnkonto ausgewiesenen Beträge € 7.000,- in bar übergeben wurden.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `RgR Univ` — similar text (different position): `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — similar text (different position): `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)
- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 6** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_86`)


Aus vorgenannten Gründen kann es keine Stundenaufzeichnungen der RgR Univ.-Prof.in KommR Corinna Bebenek  geben, bzw.  sind solche, wenn sie vorliegen, gefälscht.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 7** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_119`)


Aus vorgenannten Gründen kann es keine Stundenaufzeichnungen der RgR Univ.-Prof.in KommR Corinna Bebenek  geben, bzw.  sind solche, wenn sie vorliegen, gefälscht.

**False Positives:**

- `RgR Univ` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `KommR Corinna Bebenek` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129033.1`) (sent_id: `deanon_BFG_TRAIN/129033.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Karola Haferland, Furthofer Straße 18, 4661 Unterpühret, Österreich  vom 25. Februar 2018 gegen den Bescheid des  Finanzamtes St. Johann Tamsweg Zell am See, Brucker Bundesstraße 13, 5700 Zell am See vom  8. Februar 2018 betreffend Festsetzung der Normverbrauchsabgabe für Jänner 2018 zu Recht  erkannt:  1.

**False Positives:**

- `Dr. Maria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Karola Haferland`(person)
- `Furthofer Straße 18, 4661 Unterpühret, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Beate Melik  in der Beschwerdesache Techn R Dr.in Maria Repstock,  Silberrain 14a, 5542 Flachau, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Maria Repstock` — partial — pred is substring of gold: `Techn R Dr.in Maria Repstock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Beate Melik`(person)
- `Techn R Dr.in Maria Repstock`(person)
- `Silberrain 14a, 5542 Flachau, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `OStR Karl Ostendarp`(person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich`(address)
- `Eva Maria Koller-Rohrschach`(person)
- `84-986/6948`(tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Dr.in Ulrike Kusnierz  in der Beschwerdesache K GmbH,  Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Dr.in Dr` — partial — pred is substring of gold: `Dr.in Dr.in Ulrike Kusnierz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Dr.in Ulrike Kusnierz`(person)
- `Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129421.1`) (sent_id: `deanon_BFG_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Konepatzki  in der Beschwerdesache KommR MedR Jeannine Wegerhoff,  Burleiten 563, 9423 Matschenbloch, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `KommR Med` — partial — pred is substring of gold: `KommR MedR Jeannine Wegerhoff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Jacqueline Konepatzki`(person)
- `KommR MedR Jeannine Wegerhoff`(person)
- `Burleiten 563, 9423 Matschenbloch, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

**False Positives:**

- `Dr. Doringer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `Dr.in Monika Wörther` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

**False Positives:**

- `Dr. Doringer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dr.in Monika Wörther` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

**False Positives:**

- `Dr. Doringer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/129778.1`) (sent_id: `deanon_BFG_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache VetR Silvester Johäntges, Fischauer Gasse 37, 4616 Hetzendorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 25-402/5507  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `VetR Silvester Johäntges`(person)
- `Fischauer Gasse 37, 4616 Hetzendorf, Österreich`(address)
- `25-402/5507`(tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

**False Positives:**

- `Dr. Schmid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alexander Nahler`(person)

**Example 20** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Julia Schulteß, Anton-Sattler-Gasse 42, 3531 Brand, Österreich, vertreten durch Mag. Anton Heisinger,  Mühlallee 1, 7301 Deutschkreutz, über die Beschwerde vom 29. Februar 2016 gegen den  Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 29. Jänner 2016 betreffend Haftung  gemäß § 99 EStG 1988 für den Zeitraum 2014 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Julia Schulteß`(person)
- `Anton-Sattler-Gasse 42, 3531 Brand, Österreich`(address)
- `Mag. Anton Heisinger`(person)

**Example 21** (doc_id: `deanon_BFG_TRAIN/130407.1`) (sent_id: `deanon_BFG_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Emma Sebestik, Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Emma Sebestik`(person)
- `Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich`(address)
- `Harald Schmidt`(person)
- `Finanzamtes Spittal Villach`(organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Helena Özarslan, An der Hortigstraße 1, 5133 Hub, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Amtsvertr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Helena Özarslan`(person)
- `An der Hortigstraße 1, 5133 Hub, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)

**Example 23** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_199`)


Der Bf führte in seinem Schussantrag aus, dass er die ImmoESt gar nicht schulde, sondern hätte  diese vielmehr sein vormaliger steuerlicher Vertreter, StB Dr. St, zu tragen.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_350`)


Eine Haftung des ehemaligen  steuerlichen Vertreters des Bf, StB Dr. St, auf Grundlage der Bestimmung des § 30c Abs. 3 leg.  cit.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

**False Positives:**

- `Dr. Praus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Mag. Artner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

**False Positives:**

- `Dr. Praus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

**False Positives:**

- `Mag. Artne` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

**False Positives:**

- `Dr. Prause Heilsarme` — partial — pred is substring of gold: `Dr. Prause Heilsarmee`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Prause Heilsarmee`(person)

**Example 30** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

**False Positives:**

- `Dr. Padesse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.  Tadesse Bedasa`(person)

**Example 31** (doc_id: `deanon_BFG_TRAIN/130475.1`) (sent_id: `deanon_BFG_TRAIN/130475.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache OMedR Hermann Voigtlander, Martha-Wölger-Weg 27, 2292 Stopfenreuth, Österreich, über die Beschwerden vom 22.12.2018  (hinsichtlich des Jahres 2014) und vom 13.01.2019 (hinsichtlich der Jahre 2015 und 2016)  gegen die Berichtigungsbescheide gemäß § 293 BAO zu den Einkommensteuerbescheiden für  die Jahre 2014 bis 2016 jeweils vom 18.12.2018 des Finanzamtes Wien 2/20/21/22   zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Andrea Müller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Hermann Voigtlander`(person)
- `Martha-Wölger-Weg 27, 2292 Stopfenreuth, Österreich`(address)

**Example 32** (doc_id: `deanon_BFG_TRAIN/130559.1`) (sent_id: `deanon_BFG_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Julia Nöllecke  in der Beschwerdesache Esra Leßnick, LLB,  Hackermillerstraße 133, 8940 Döllach, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  06-833/3820, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Radics`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Julia Nöllecke`(person)
- `Esra Leßnick, LLB`(person)
- `Hackermillerstraße 133, 8940 Döllach, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `06-833/3820`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 33** (doc_id: `deanon_BFG_TRAIN/130727.1`) (sent_id: `deanon_BFG_TRAIN/130727.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über den Antrag  der Adelheid Tripel, Josef-Kutscha-Gasse 16, 7542 Sulz im Burgenland, Österreich  vom 23. März 2020 auf Gewährung der Verfahrenshilfe für das  Beschwerdeverfahren gegen den Bescheid der belangten Behörde Finanzamt Bruck Eisenstadt  Oberwart vom 28. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 beschlossen:  Der Antragstellerin wird gemäß § 292 BAO Verfahrenshilfe bewilligt.

**False Positives:**

- `Dr. Maria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Adelheid Tripel`(person)
- `Josef-Kutscha-Gasse 16, 7542 Sulz im Burgenland, Österreich`(address)
- `Finanzamt Bruck Eisenstadt  Oberwart`(organisation)

**Example 34** (doc_id: `deanon_BFG_TRAIN/130744.1`) (sent_id: `deanon_BFG_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Esmeralda Halbgebauer, Akazienplatz 349, 9634 Rauth, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Esmeralda Halbgebauer`(person)
- `Akazienplatz 349, 9634 Rauth, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)

**Example 35** (doc_id: `deanon_BFG_TRAIN/130749.1`) (sent_id: `deanon_BFG_TRAIN/130749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Dr. OStR Benedikt Paszkowiak, Susalitsch 160, 8230 Staudach, Österreich, über die Beschwerde vom 28. Juni 2018 gegen  den Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 19. Juni 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`
- `OStR Benedikt Paszkowiak` — partial — pred is substring of gold: `Dr. OStR Benedikt Paszkowiak`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Dr. OStR Benedikt Paszkowiak`(person)
- `Susalitsch 160, 8230 Staudach, Österreich`(address)

**Example 36** (doc_id: `deanon_BFG_TRAIN/130834.1`) (sent_id: `deanon_BFG_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Dr. Wagner` — partial — pred is substring of gold: `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`
- `Dr. Wagner` — similar text (different position): `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`
- `Dr. Wagner` — similar text (different position): `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `BKS Steuerberatungs GmbH`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Baden Mödling`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 37** (doc_id: `deanon_BFG_TRAIN/130834.1`) (sent_id: `deanon_BFG_TRAIN/130834.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Baden Mödling als Finanzstrafbehörde vom 12. April 2018, SpS 18, , Strafnummer  001 ff, 002 ff, wurde in den Finanzstrafsachen gegen   1. A B Geschäftsführer, wohnhaft in Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  2. C B Geschäftsführerin, wohnhaft in Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  3. V1 als belangter Verband, mit Sitz in Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  4. B GmbH als belangter Verband, mit Sitz in Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  zu Recht erkannt:   A B, die V1 und die B GmbH sind schuldig, es haben im Bereich des Finanzamtes Baden Mödling  grob fahrlässig  1) A B   I) als Geschäftsführer der Firma V1  a) infolge Abgabe unrichtiger Umsatz- und Körperschaftsteuererklärungen, sohin unter  Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bescheidmäßig  festzusetzende Abgaben, nämlich    2011 2012 2013 2014 2015 Summe  Umsatzsteuer iHv 2.619,96 8.934,65 300,00 437,00 450,00 € 12.741,61  Köst iHv 1.500,59 10.337,20 7.250,00 3.796,88 562,50 € 21.447,30  Summe in € 4.120,55 19.271,85 7.550,00 4.233,88 1.012,50 € 36.188.78  verkürzt, sowie  b) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 96 Abs. 3 EStG entsprechenden  Kapitalertragsteueranmeldungen, somit unter Verletzung der abgabenrechtlich gebotenen  Offenlegungs- und Wahrheitspﬂicht, Verkürzung an  Kapitalertragsteuer 2012 in der Höhe von € 1.440,63  2013 in der Höhe von € 9.765,69  2014 in der Höhe von € 5.207,81  2015 in der Höhe von € 899,91  insgesamt somit € 17.312,04 bewirkt.

**False Positives:**

- `Dr. Wagner` — partial — pred is substring of gold: `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`
- `Dr. Wagner` — similar text (different position): `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`
- `Dr. Wagner` — similar text (different position): `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`
- `Dr. Wagner` — similar text (different position): `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 38** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 39** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Jeanne von Fritz  in der Beschwerdesache Martha Michenfelder,  Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Univ.-Prof.in Jeanne` — partial — pred is substring of gold: `Mag.a Univ.-Prof.in Jeanne von Fritz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Univ.-Prof.in Jeanne von Fritz`(person)
- `Martha Michenfelder`(person)
- `Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich`(address)

**Example 40** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_2`)


Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 92-182/0749  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

**False Positives:**

- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft` — partial — pred is substring of gold: `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Erwin Baldauf`(person)
- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `92-182/0749`(tax_number)

</details>

---

## `Complainant Name Context Pattern`

**F1:** 0.313 | **Precision:** 0.925 | **Recall:** 0.189  

**Format:** `regex`  
**Rule ID:** `80f93592`  
**Description:**
Captures person names following 'in der Beschwerdesache', strictly requiring a title or a full name pattern with suffixes (e.g., ', BA') to avoid partial matches or false positives on legal nouns.

**Content:**
```
in\s+der\s+Beschwerdesache\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+)*(?:\s*,\s*(?:BA|BSc|B\.Sc|B\.A\.|Bakk\. rer\. nat\.|Dipl\.|Ing\.|B\.Sc\.))?)(?=\s*,|\s+\d|\s+\.|\s+\)|\s+\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.925 | 0.189 | 0.313 | 411 | 380 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 380 | 31 | 1633 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Janis Forch, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Forch` | `Janis Forch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128942.1`) (sent_id: `deanon_BFG_TRAIN/128942.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Julia Potthöfer, Hofmannstraße 41, 9300 Tschirnig, Österreich, vertreten durch Vertreter, Vertreter Adresse, über die Beschwerde vom 27. März 2014  gegen den Bescheid des Finanzamtes Graz-Stadt vom 24. Februar 2014 betreffend Aufhebung  des Bescheides über die Umsatzsteuer 2010, Steuernummer 58-698/6537, zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julia Potthöfer` | `Julia Potthöfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hofmannstraße 41, 9300 Tschirnig, Österreich` (address)
- `58-698/6537` (tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128975.1`) (sent_id: `deanon_BFG_TRAIN/128975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Rita Zwirner,  Bodenring 61, 3261 Windpassing, Österreich, vertreten durch Wijnkamp Advocatuur/Advokatur GmbH, Sirapuit 7, 6460  Imst, und Prodinger & Partner Wirtschaftstreuhand-Steuerberatungs GmbH & Co KG,  Prof.Ferry Porsche Straße 28, 5700 Zell am See, über die Beschwerde vom 7. Februar 2018  gegen den Bescheid des Finanzamtes St. Johann Tamsweg Zell am See vom 21. Dezember 2016  betreffend Umsatzsteuer 2006, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rita Zwirner` | `Rita Zwirner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bodenring 61, 3261 Windpassing, Österreich` (address)
- `Wijnkamp Advocatuur/Advokatur GmbH` (organisation)
- `Imst, und Prodinger & Partner Wirtschaftstreuhand-Steuerberatungs GmbH & Co KG` (organisation)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129005.1`) (sent_id: `deanon_BFG_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Thassilo Trabschuh,  Ernst-Derfeser-Straße 30, 5134 Polzwies, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Thassilo Trabschuh` | `Thassilo Trabschuh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ernst-Derfeser-Straße 30, 5134 Polzwies, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129068.1`) (sent_id: `deanon_BFG_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Jens Spilken, Hillere 22, 8453 Saggau, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-228/4517  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jens Spilken` | `Jens Spilken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Hillere 22, 8453 Saggau, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `69-228/4517` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129071.1`) (sent_id: `deanon_BFG_TRAIN/129071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Edwin Bachmair, Bergliftstraße 479I, 9861 Densdorf, Österreich,  vertreten durch Nepomuk Polcin, Madleinweg 22, 4154 Mollmannsreith, Österreich, über die Beschwerde vom  21. August 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Juli 2019  betreffend Einkommensteuer 2014, Steuernummer ,zu Recht erkannt:   I. Der Beschwerde wird im Umfang der Beschwerdevorentscheidung teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Edwin Bachmair` | `Edwin Bachmair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bergliftstraße 479I, 9861 Densdorf, Österreich` (address)
- `Nepomuk Polcin` (person)
- `Madleinweg 22, 4154 Mollmannsreith, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Lubomir Baltßun` | `Lubomir Baltßun` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129218.1`) (sent_id: `deanon_BFG_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Brian Detloff,  Übersbach 6l, 7540 Großmürbisch, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Brian Detloff` | `Brian Detloff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Übersbach 6l, 7540 Großmürbisch, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129231.1`) (sent_id: `deanon_BFG_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Bartholomäus Malcharzik, Ogugasse 8, 4483 Pirchhorn, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Bartholomäus Malcharzik` | `Bartholomäus Malcharzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Elisabeth Traxler` (person)
- `Ogugasse 8, 4483 Pirchhorn, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Doris Goralik, Baron-Kutschera-Allee 13, 6432 Sautens, Österreich, vertreten durch Stb, Steuerberater Wirtschaftstreuhänder, Baron-Kutschera-Allee 13, 6432 Sautens, Österreich, über die  Beschwerde vom 28. August 2013 gegen den Bescheid des Finanzamtes B vom 23. August  2013, Steuernummer , betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Doris Goralik` | `Doris Goralik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Baron-Kutschera-Allee 13, 6432 Sautens, Österreich` (address)
- `Baron-Kutschera-Allee 13, 6432 Sautens, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Anton Danelzik` | `Anton Danelzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129533.1`) (sent_id: `deanon_BFG_TRAIN/129533.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Erna Ackers, Wollsdorf 52, 9582 Latschach, Österreich, vertreten durch Stb, über die Beschwerde vom 21.12.2012 gegen den Bescheid des  Finanzamtes A vom 13.11.2012, betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Erna Ackers` | `Erna Ackers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wollsdorf 52, 9582 Latschach, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Reinhard Komarova, Gabrielweg 4, 4725 Adelsgrub, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 92-139/9763  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Reinhard Komarova` | `Reinhard Komarova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ralf Schatzl` (person)
- `Gabrielweg 4, 4725 Adelsgrub, Österreich` (address)
- `92-139/9763` (tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Edgar Neidenberger, Nussallee 89, 8143 Unterpremstätten, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Edgar Neidenberger` | `Edgar Neidenberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nussallee 89, 8143 Unterpremstätten, Österreich` (address)
- `DI Heinrich Richter Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129696.1`) (sent_id: `deanon_BFG_TRAIN/129696.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gabriele Roggensack, Frimmelgasse 29, 4870 Maulham, Österreich, über die Beschwerde vom 2. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 7. August 2019 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe für das Kind x im Zeitraum vom 01.07.2014 bis zum 30.09.2016 Recht erkannt:   Der Beschwerde wird gemäß § 279 teilweise BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gabriele Roggensack` | `Gabriele Roggensack` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frimmelgasse 29, 4870 Maulham, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129733.1`) (sent_id: `deanon_BFG_TRAIN/129733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Wilfried Wedral  in der Beschwerdesache Ramona Goedeken,  Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich, vertreten durch Union TAX&LAW, Donau-City-Straße 7, DV Tower/30th floor,  1220 Wien, über die Beschwerde vom 16. April 2019 gegen den Bescheid des Finanzamtes  Innsbruck vom 19. März 2019 betreffend Familienbeihilfe (Ausgleichszahlung) für die Monate  Jänner 2015 bis Dezember 2017, [Ordnungsbegriff],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ramona Goedeken` | `Ramona Goedeken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Wilfried Wedral` (person)
- `Am Kittenberg 37, 4903 Schachen bei Wolfshütte, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129828.1`) (sent_id: `deanon_BFG_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Pascal Beerlage, Tannwaldweg 35L, 9133 Jerischach, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 13-489/9399  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Pascal Beerlage` | `Pascal Beerlage` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Tannwaldweg 35L, 9133 Jerischach, Österreich` (address)
- `Dr. Helmut Herbert Moritz` (person)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `13-489/9399` (tax_number)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129907.1`) (sent_id: `deanon_BFG_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. R. in der Beschwerdesache Zarin Enneken,  Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 90-142/3945  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Zarin Enneken` | `Zarin Enneken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. R.` (person)
- `Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich` (address)
- `90-142/3945` (tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Shoshana Schweinforth, Brenggenalm 15, 8551 Gieselegg, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 78-461/2049  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shoshana Schweinforth` | `Shoshana Schweinforth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brenggenalm 15, 8551 Gieselegg, Österreich` (address)
- `78-461/2049` (tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129969.1`) (sent_id: `deanon_BFG_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hilde Heinsohn, Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Hilde Heinsohn` | `Hilde Heinsohn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 20** (doc_id: `deanon_BFG_TRAIN/130024.1`) (sent_id: `deanon_BFG_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Marlon William, J. Ranzoni-Straße 1L, 9554 Reggen, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlon William` | `Marlon William` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `J. Ranzoni-Straße 1L, 9554 Reggen, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 21** (doc_id: `deanon_BFG_TRAIN/130064.1`) (sent_id: `deanon_BFG_TRAIN/130064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Aurelia Heizel, Schifferweg 60, 8463 Kranach, Österreich, vertreten durch Joachim Herbert Aigner, Gewerbepark 1, 4920 Schildorn, über die  Beschwerde vom 23. Februar 2018 gegen den Haftungsbescheid des Finanzamtes Braunau Ried  Schärding vom 24. Jänner 2018, Steuernummer StNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben, der Haftungsbetrag von  4.588,35 € um 2.258,02 € auf den Betrag von 2.330,33 € eingeschränkt und wie folgt  aufgeschlüsselt:   Abgabenart Zeitraum Fälligkeit Betrag in Euro  Umsatzsteuer 03/2016 17.05.2016 16,87  Dienstgeberbeitrag 05/2016 15.06.2016 60,50  Zuschlag zum DB 05/2016 15.06.2016 4,48  Lohnsteuer 05/2016 15.06.2016 25,86  Umsatzsteuer 04/2016 15.06.2016 48,32  Dienstgeberbeitrag 06/2016 15.07.2016 66,69  Zuschlag zum DB 06/2016 15.07.2016 5,34  Lohnsteuer 06/2016 15.07.2016 25,86  Umsatzsteuer 05/2016 15.07.2016 71,65  Säumniszuschlag 1 2016 18.07.2016 24,75  Dienstgeberbeitrag 07/2016 16.08.2016 85,30  Zuschlag zum DB 07/2016 16.08.2016 6,82  1 von 15 Seite 2 von 15

| Predicted | Gold |
|---|---|
| `Aurelia Heizel` | `Aurelia Heizel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schifferweg 60, 8463 Kranach, Österreich` (address)
- `Joachim Herbert Aigner` (person)
- `Finanzamtes Braunau Ried` (organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Julia Schulteß, Anton-Sattler-Gasse 42, 3531 Brand, Österreich, vertreten durch Mag. Anton Heisinger,  Mühlallee 1, 7301 Deutschkreutz, über die Beschwerde vom 29. Februar 2016 gegen den  Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 29. Jänner 2016 betreffend Haftung  gemäß § 99 EStG 1988 für den Zeitraum 2014 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Julia Schulteß` | `Julia Schulteß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Anton-Sattler-Gasse 42, 3531 Brand, Österreich` (address)
- `Mag. Anton Heisinger` (person)

**Example 23** (doc_id: `deanon_BFG_TRAIN/130311.1`) (sent_id: `deanon_BFG_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Juliana Cano, Schreier 19, 5121 Ölling, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Zlatan Gemünd  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juliana Cano` | `Juliana Cano` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schreier 19, 5121 Ölling, Österreich` (address)
- `Zlatan Gemünd` (person)

**Example 24** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Christoph Mehlbeer` | `Christoph Mehlbeer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schötz Gasse 45, 7434 Holzschlag, Österreich` (address)
- `Margarete Wiepking` (person)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Esmeralda Lubert, Kaschlgasse 9, 3100 Witzendorf, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Esmeralda Lubert` | `Esmeralda Lubert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Kaschlgasse 9, 3100 Witzendorf, Österreich` (address)
- `Sigrid Lamböck` (person)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130367.1`) (sent_id: `deanon_BFG_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Petra Ullemeyer, Mariexner Straße 8, 3141 Rassing, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Petra Ullemeyer` | `Petra Ullemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Mariexner Straße 8, 3141 Rassing, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/130407.1`) (sent_id: `deanon_BFG_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Emma Sebestik, Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Emma Sebestik` | `Emma Sebestik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Heberplatzl 4, 7441 Bubendorf im Burgenland, Österreich` (address)
- `Harald Schmidt` (person)
- `Finanzamtes Spittal Villach` (organisation)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Schulwiesen 13, 4203 Stratreith, Österreich` (address)
- `Mag. Margot Artner` (person)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Danzfuss, BSc` | `Marlies Danzfuss, BSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Nüssli` | `Wladimir Nüssli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Aigner` (person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich` (address)
- `Dr. Elke Hager` (person)

**Example 31** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Matthäus Buskens` | `Matthäus Buskens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alfred Klaming` (person)
- `Edlach 19, 3141 Oberkilling, Österreich` (address)
- `Helmut Binder` (person)

**Example 32** (doc_id: `deanon_BFG_TRAIN/130748.1`) (sent_id: `deanon_BFG_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Valentina Cagli, A. Böhm Gasse 67F, 4310 Oberzirking, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 76-512/9228  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Valentina Cagli` | `Valentina Cagli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `A. Böhm Gasse 67F, 4310 Oberzirking, Österreich` (address)
- `76-512/9228` (tax_number)

**Example 33** (doc_id: `deanon_BFG_TRAIN/130927.1`) (sent_id: `deanon_BFG_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Kassandra Liewerenz  in der Beschwerdesache Charlotte Schaffarz,  Röhrenweg 39, 4751 Altmannsdorf, Österreich, vertreten durch Dkfm.

| Predicted | Gold |
|---|---|
| `Charlotte Schaffarz` | `Charlotte Schaffarz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Kassandra Liewerenz` (person)
- `Röhrenweg 39, 4751 Altmannsdorf, Österreich` (address)

**Example 34** (doc_id: `deanon_BFG_TRAIN/130967.1`) (sent_id: `deanon_BFG_TRAIN/130967.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Delia Kraußer, Gropper 3, 3911 Arnreith, Österreich, betreffend Beschwerde gegen die Bescheide des Finanzamtes Wien 4/5/10 vom  23. April 2018 betreffend Umsatzsteuer und Einkommensteuer 2016 Steuernummer  95-402/2327  beschlossen:   Der Vorlageantrag vom 21.7.2018 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264 Abs. 4  BAO und § 278 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Delia Kraußer` | `Delia Kraußer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gropper 3, 3911 Arnreith, Österreich` (address)
- `95-402/2327` (tax_number)

**Example 35** (doc_id: `deanon_BFG_TRAIN/131046.1`) (sent_id: `deanon_BFG_TRAIN/131046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Hugo Moewius, Studenygasse 11, 4623 Buchleiten, Österreich, vertreten durch SCHIETZ + MAUREDER Steuerberatung GmbH,  Veldner Straße 29, 4120 Neufelden, über die Beschwerde vom 20. Juni 2017 gegen den  Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 9. Juni 2017 betreffend  Einkommensteuer 2015 Steuernummer 03-874/1042  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hugo Moewius` | `Hugo Moewius` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Studenygasse 11, 4623 Buchleiten, Österreich` (address)
- `03-874/1042` (tax_number)

**Example 36** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Silvia Geidies, Schönengrund 34, 4209 Innertreffling, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 17-823/0942  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Silvia Geidies` | `Silvia Geidies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Schönengrund 34, 4209 Innertreffling, Österreich` (address)
- `17-823/0942` (tax_number)

**Example 37** (doc_id: `deanon_BFG_TRAIN/131065.1`) (sent_id: `deanon_BFG_TRAIN/131065.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Alina Trechsler  in der Beschwerdesache  Birgit Nelle, Kudlichgasse 63, 4240 Sankt Peter, Österreich, vertreten durch X-Steuerberatung über die Beschwerde vom  19. Februar 2016 gegen den Bescheid des FA Linz  vom 15. Jänner 2016 betreffend  Feststellung der Einkünfte § 188 BAO 2012 zur Steuernummer 999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Birgit Nelle` | `Birgit Nelle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Mag.a Alina Trechsler` (person)
- `Kudlichgasse 63, 4240 Sankt Peter, Österreich` (address)
- `FA Linz` (organisation)

**Example 38** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Endrowait` | `Willibald Endrowait` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 39** (doc_id: `deanon_BFG_TRAIN/131225.1`) (sent_id: `deanon_BFG_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Wendelin Dumröse, Dr.-Werner-Gasse 41, 5143 Otterfing, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wendelin Dumröse` | `Wendelin Dumröse` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Dr.-Werner-Gasse 41, 5143 Otterfing, Österreich` (address)

**Example 40** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Jeanne von Fritz  in der Beschwerdesache Martha Michenfelder,  Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich, vertreten durch Dkfm.

| Predicted | Gold |
|---|---|
| `Martha Michenfelder` | `Martha Michenfelder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Univ.-Prof.in Jeanne von Fritz` (person)
- `Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_TRAIN/131299.1`) (sent_id: `deanon_BFG_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Othmar Misch, Freitzenschlag 122, 4723 Dopl, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 35-689/1540  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Othmar Misch` | `Othmar Misch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Freitzenschlag 122, 4723 Dopl, Österreich` (address)
- `35-689/1540` (tax_number)

**Example 42** (doc_id: `deanon_BFG_TRAIN/131341.1`) (sent_id: `deanon_BFG_TRAIN/131341.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Valentin Kottsiepen, Fratresstraße 24, 3814 Aigen, Österreich, betreffend Beschwerde vom 23. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 1/23 vom 3. Februar 2016 betreffend   Haftung zur Einbehaltung und Abfuhr der Lohnsteuer, Festsetzung des Dienstgeberbeitrages  (DB) und Festsetzung des Zuschlags zum Dienstgeberbeitrag (DZ) für die Kalenderjahre 2010 bis  2014 sowie Festsetzung von Säumniszuschlägen für Lohnsteuer 2010 bis 2014,  Steuernummer 12-752/9462  beschlossen:  Die Beschwerde wird als gegenstandslos erklärt und das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Valentin Kottsiepen` | `Valentin Kottsiepen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Fratresstraße 24, 3814 Aigen, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `12-752/9462` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 43** (doc_id: `deanon_BFG_TRAIN/131450.1`) (sent_id: `deanon_BFG_TRAIN/131450.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Carmen Wielander  in der Beschwerdesache Ulrich Hecktor,  St. Nikolaus Straße 16, 4904 Reichering, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 26. Februar 2020,  betreffend Rückforderung von Familienbeihilfe und Kinderabsetzbeträge für die Zeiträume  Oktober 2017 bis Juni 2019, zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ulrich Hecktor` | `Ulrich Hecktor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Carmen Wielander` (person)
- `St. Nikolaus Straße 16, 4904 Reichering, Österreich` (address)

**Example 44** (doc_id: `deanon_BFG_TRAIN/131467.1`) (sent_id: `deanon_BFG_TRAIN/131467.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Vera Lüerß, BA, Gewerbepark Hinterholz 3, 4974 Stött, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom  29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer  ***, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Vera Lüerß, BA` | `Vera Lüerß, BA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Gewerbepark Hinterholz 3, 4974 Stött, Österreich` (address)
- `BKS Steuerberatung GmbH & Co  KG` (organisation)

**Example 45** (doc_id: `deanon_BFG_TRAIN/131467.1`) (sent_id: `deanon_BFG_TRAIN/131467.1_4`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Vera Lüerß, BA, Gewerbepark Hinterholz 3, 4974 Stött, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, betreffend Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Einkommensteuer 2003 – 2010 und vom 29.4.2013 betreffend Einkommensteuer  2011, Steuernummer **, beschlossen:   Die Beschwerde vom 18. Mai 2013 wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Vera Lüerß, BA` | `Vera Lüerß, BA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Gewerbepark Hinterholz 3, 4974 Stött, Österreich` (address)
- `BKS Steuerberatung GmbH & Co  KG` (organisation)

**Example 46** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

| Predicted | Gold |
|---|---|
| `Karen Vennemeyer` | `Karen Vennemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Neu-Reinbach 11, 4693 Fallholz, Österreich` (address)
- `Intercura Teuhand Revisions  GmbH` (organisation)

**Example 47** (doc_id: `deanon_BFG_TRAIN/131601.1`) (sent_id: `deanon_BFG_TRAIN/131601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Jana Maquard, Eberdorf 1, 4633 Kematen am Innbach, Österreich, über die Beschwerde vom 3. Oktober 2018 gegen die Bescheide des Finanzamtes Wien  1/23 vom 30. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 und  2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jana Maquard` | `Jana Maquard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eberdorf 1, 4633 Kematen am Innbach, Österreich` (address)

**Example 48** (doc_id: `deanon_BFG_TRAIN/131624.1`) (sent_id: `deanon_BFG_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Ruprecht Lupold  in der Beschwerdesache Delia Schlossnickl,  Bodenalpbahn 727, 3161 Kropfsdorf, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Delia Schlossnickl` | `Delia Schlossnickl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Ruprecht Lupold` (person)
- `Bodenalpbahn 727, 3161 Kropfsdorf, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_TRAIN/131687.1`) (sent_id: `deanon_BFG_TRAIN/131687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Gundula Schiedhelm, Formstein 69, 2860 Ungerbach, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft mbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 1. Februar 2017 gegen den Bescheid  des Finanzamtes Gänserndorf Mistelbach vom 12. Jänner 2017 betreffend Einkommensteuer  2015, Steuernummer 03-127/1832, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gundula Schiedhelm` | `Gundula Schiedhelm` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Formstein 69, 2860 Ungerbach, Österreich` (address)
- `03-127/1832` (tax_number)

**Example 50** (doc_id: `deanon_BFG_TRAIN/131742.1`) (sent_id: `deanon_BFG_TRAIN/131742.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Mag.a Erika Froschhäuser  in der Beschwerdesache Pablo Cuypers, August-Reuss-Gasse 11, 5112 Schwerting, Österreich  vertreten durch Milena Brauner, über die Beschwerde vom 4. Juni 2018 gegen den  Bescheid des FA Graz-Stadt  vom 26. März 2018 betreffend Einkommensteuer 2016, Steuernummer  04-620/2121, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Pablo Cuypers` | `Pablo Cuypers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Erika Froschhäuser` (person)
- `August-Reuss-Gasse 11, 5112 Schwerting, Österreich` (address)
- `Milena Brauner` (person)
- `FA Graz-Stadt` (organisation)
- `04-620/2121` (tax_number)

**Example 51** (doc_id: `deanon_BFG_TRAIN/131773.1`) (sent_id: `deanon_BFG_TRAIN/131773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melinda Endele  in der Beschwerdesache Constantin Oberboersch,  Eidendorfer Straße 3, 8441 Höch, Österreich ,EU-Land, über die Beschwerde vom 19. Dezember 2017 gegen den  Abweisungsbescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 11. Dezember 2017  betreffend Ausgleichszahlung (Familienbeihilfe) für Kind1, geb. xx.xx..1994, Kind2, geb.  yy.yy..2002 und Kind3, geb. zz.zz..2000, je für den Zeitraum Jänner 2016 bis Dezember 2016 zu  Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Constantin Oberboersch` | `Constantin Oberboersch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Melinda Endele` (person)
- `Eidendorfer Straße 3, 8441 Höch, Österreich` (address)

**Example 52** (doc_id: `deanon_BFG_TRAIN/131804.1`) (sent_id: `deanon_BFG_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Gerda Mauder, Exerzierplatz 16, 4962 Mining, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Gerda Mauder` | `Gerda Mauder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Exerzierplatz 16, 4962 Mining, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_TRAIN/131880.1`) (sent_id: `deanon_BFG_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Zacharias Moehring, Edmundshof 49j, 9020 Walddorf, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 77-674/4781  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Zacharias Moehring` | `Zacharias Moehring` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Edmundshof 49j, 9020 Walddorf, Österreich` (address)
- `77-674/4781` (tax_number)

**Example 54** (doc_id: `deanon_BFG_TRAIN/131914.1`) (sent_id: `deanon_BFG_TRAIN/131914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Paula Stokmann, Krastalstraße 1, 4707 Mitterndorf, Österreich, über die Beschwerde vom 28. Oktober 2019  gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 7. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 72-251/6474  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Paula Stokmann` | `Paula Stokmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Krastalstraße 1, 4707 Mitterndorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `72-251/6474` (tax_number)

**Example 55** (doc_id: `deanon_BFG_TRAIN/131969.1`) (sent_id: `deanon_BFG_TRAIN/131969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache Richarda Tessar, Ballstraße 28, 4084 Freiling, Österreich, über die Beschwerde vom 23. Mai 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 26. April 2019 betreffend Rückforderung Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum November 2017 bis April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Richarda Tessar` | `Richarda Tessar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ballstraße 28, 4084 Freiling, Österreich` (address)

**Example 56** (doc_id: `deanon_BFG_TRAIN/131982.1`) (sent_id: `deanon_BFG_TRAIN/131982.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Horst Symanzik, Scheichergasse 120, 4893 Kohlstatt, Österreich, gegen die Bescheide des Finanzamtes Spittal Villach vom 11. November 2011  betreffend Umsatzsteuer 2010 und Einkommensteuer 2010, Steuernummer, den Beschluss  gefasst:   Die Beschwerde wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Horst Symanzik` | `Horst Symanzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Scheichergasse 120, 4893 Kohlstatt, Österreich` (address)
- `Finanzamtes Spittal Villach` (organisation)

**Example 57** (doc_id: `deanon_BFG_TRAIN/132030.1`) (sent_id: `deanon_BFG_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Bernadette Birkfeld, Pipitzhof 7, 3388 Knetzersdorf, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernadette Birkfeld` | `Bernadette Birkfeld` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Pipitzhof 7, 3388 Knetzersdorf, Österreich` (address)

**Example 58** (doc_id: `deanon_BFG_TRAIN/132106.1`) (sent_id: `deanon_BFG_TRAIN/132106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jessica Osborn, Am Richardschacht 28, 2880 Lehen, Österreich, über die Beschwerde vom 5. Dezember 2014  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 6. November 2014 betreffend  Umsatzsteuer und Einkommensteuer 2012 und 2013 sowie gegen den Bescheid des  Finanzamtes Kirchdorf Perg Steyr vom 10. November 2014 betreffend Festsetzung des ersten  Säumniszuschlages von der Umsatzsteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jessica Osborn` | `Jessica Osborn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Am Richardschacht 28, 2880 Lehen, Österreich` (address)

**Example 59** (doc_id: `deanon_BFG_TRAIN/132142.1`) (sent_id: `deanon_BFG_TRAIN/132142.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Silvius Lanvermeyer, Ödenkirchenstraße 73, 4152 Mairhof, Österreich, über die Beschwerde vom 27. Dezember 2019 gegen den Bescheid  des Finanzamtes Österreich vom 4. Dezember 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvius Lanvermeyer` | `Silvius Lanvermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Ödenkirchenstraße 73, 4152 Mairhof, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_TRAIN/132215.1`) (sent_id: `deanon_BFG_TRAIN/132215.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Joshua Könker  in der Beschwerdesache Hildegard Kähler,  Dr.-Rudolf-Krause-Straße 59, 3161 Obergegend, Österreich, gegen den von der belangten Behörde Finanzamt Baden Mödling, nunmehr Finanzamt  Österreich, am 24. Mai 2018 ausgefertigten Bescheid mit der Bezeichnung „BESCHEID 2015“,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hildegard Kähler` | `Hildegard Kähler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Joshua Könker` (person)
- `Dr.-Rudolf-Krause-Straße 59, 3161 Obergegend, Österreich` (address)
- `Finanzamt Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 61** (doc_id: `deanon_BFG_TRAIN/132255.1`) (sent_id: `deanon_BFG_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Chen Helwig  in der Beschwerdesache Roxana Gehrbrandt,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roxana Gehrbrandt` | `Roxana Gehrbrandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Chen Helwig` (person)
- `Dr Christian Leskoschek` (person)
- `Finanzamtes Österreich` (organisation)

**Example 62** (doc_id: `deanon_BFG_TRAIN/132303.1`) (sent_id: `deanon_BFG_TRAIN/132303.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elvira Schaffranek  in der Beschwerdesache Judith Kuhr,  Unterm Kirchenberg 337, 4064 Hausleiten, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 07. April 2020,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Judith Kuhr` | `Judith Kuhr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elvira Schaffranek` (person)
- `Unterm Kirchenberg 337, 4064 Hausleiten, Österreich` (address)

**Example 63** (doc_id: `deanon_BFG_TRAIN/132361.1`) (sent_id: `deanon_BFG_TRAIN/132361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dora Streb, Rosemarie-Preh-Allee 19, 9113 Grutschen, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1/Freyung, 1010  Wien, über die Beschwerde vom 13. Juni 2014 gegen den Bescheid des Finanzamtes Wien 1/23  vom 11. August 2010 betreffend Berichtigung gemäß § 293b BAO des Bescheides vom 1. Juni  2007 betreffend Umsatzsteuer 2005 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dora Streb` | `Dora Streb` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie-Preh-Allee 19, 9113 Grutschen, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 64** (doc_id: `deanon_BFG_TRAIN/132368.1`) (sent_id: `deanon_BFG_TRAIN/132368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Hugo Denhart, Eichhorn 8, 9413 Hinterwölch, Österreich, vertreten durch Dr. Peter Eisele, Öffentlicher Notar, 7540 Güssing, Hauptplatz 1, über  die Beschwerde vom 18. Dezember 2017 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 11. Dezember 2017 betreffend Rechtsgebühr,  Steuernummer 10- 90-207/0668, Erf.Nr. 10- 2017, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hugo Denhart` | `Hugo Denhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eichhorn 8, 9413 Hinterwölch, Österreich` (address)
- `Dr. Peter Eisele` (person)
- `90-207/0668` (tax_number)

**Example 65** (doc_id: `deanon_BFG_TRAIN/132403.1`) (sent_id: `deanon_BFG_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hartmut Großekämper, Bonnleiten 7, 8301 Höf, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 45-360/9049  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hartmut Großekämper` | `Hartmut Großekämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bonnleiten 7, 8301 Höf, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `45-360/9049` (tax_number)

**Example 66** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Karola Birkenzeller, Reifnitz 2, 4532 Rohr im Kremstal, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Pascal Tiessen, Dipl. Kfm. StR Dagobert Carstedt  und Priv.-Doz.in KommR Ida Sackerer, MBA  für den  Zeitraum August 2014 bis April 2016 bezogener Beträge an Familienbeihilfe,  Kinderabsetzbetrag und Ausgleichszahlung gemäß Verordnung (EG) 833/2004 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karola Birkenzeller` | `Karola Birkenzeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reifnitz 2, 4532 Rohr im Kremstal, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `Pascal Tiessen` (person)
- `Dipl. Kfm. StR Dagobert Carstedt` (person)
- `Priv.-Doz.in KommR Ida Sackerer, MBA` (person)

**Example 67** (doc_id: `deanon_BFG_TRAIN/132478.1`) (sent_id: `deanon_BFG_TRAIN/132478.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Juri Weich, Spitalanger 19, 3910 Ratschenhof, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 9. März 2015 betreffend Einkommensteuervorauszahlungen 2015 zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juri Weich` | `Juri Weich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Spitalanger 19, 3910 Ratschenhof, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 68** (doc_id: `deanon_BFG_TRAIN/132486.1`) (sent_id: `deanon_BFG_TRAIN/132486.1_2`)


Das Bundesfinanzgericht hat durch die Richterinri in der Beschwerdesache Iris Plogstert, Rüsthausgasse 114S, 4111 Hamberg, Österreich, vertreten durch Thuller & Partner Wirtschaftstreuhand & Steuerberatungs GmbH,  Villacher Straße 83, 9020 Klagenfurt am Wörthersee,  über die Beschwerde vom 27. August 2018 gegen den Einkommensteuerbescheid für das Jahr  2017 des Finanzamtes Klagenfurt (nunmehr Finanzamt Österreich) vom 31. Juli 2018,  Steuernummer 60-977/4138, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Iris Plogstert` | `Iris Plogstert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rüsthausgasse 114S, 4111 Hamberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `60-977/4138` (tax_number)

**Example 69** (doc_id: `deanon_BFG_TRAIN/132501.1`) (sent_id: `deanon_BFG_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Huberta Petratschek, Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Huberta Petratschek` | `Huberta Petratschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 70** (doc_id: `deanon_BFG_TRAIN/132578.1`) (sent_id: `deanon_BFG_TRAIN/132578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Aloisa Füchsel, Wimhub 18, 3443 Henzing, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 6.3.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Aloisa Füchsel` | `Aloisa Füchsel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Wimhub 18, 3443 Henzing, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 71** (doc_id: `deanon_BFG_TRAIN/132584.1`) (sent_id: `deanon_BFG_TRAIN/132584.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Othmar Möhlenberg, Ritzhofstraße 36, 6060 Hall in Tirol, Österreich, vertreten durch Mag. Rainer Hochstöger,  Breitwiesergutstraße 10, 4020 Linz, über die Beschwerde - Maßnahmenbeschwerde – vom  23. Dezember 2017 wegen Ausübung unmittelbarer verwaltungsbehördlicher Befehls- und  Zwangsgewalt in einer Angelegenheit nach dem Glücksspielgesetz am 15.11.2017 im Lokal  Adresse durch Organe der belangten Behörde FA Wien 4/5/10, FPFPT   zu Recht erkannt:   I. Die angefochtene Maßnahme – Mitnahme eines Reporters zur Kontrolle – wird  gem. § 28 Abs. 6 erster Satz VwGVG für rechtswidrig erklärt.

| Predicted | Gold |
|---|---|
| `Othmar Möhlenberg` | `Othmar Möhlenberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Ritzhofstraße 36, 6060 Hall in Tirol, Österreich` (address)
- `Mag. Rainer Hochstöger` (person)
- `FA Wien 4/5/10` (organisation)

**Example 72** (doc_id: `deanon_BFG_TRAIN/132601.1`) (sent_id: `deanon_BFG_TRAIN/132601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Elena Scheidlin  in der Beschwerdesache Martin Chalupny,  Anton Gotsch-Gasse 26, 8492 Klöchberg, Österreich, vertreten durch StB, über die Beschwerde vom 23. Juli 2018 gegen den  Bescheid des Finanzamtes vom 25. Juni 2018 betreffend Einkommensteuervorauszahlungen  2018 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Martin Chalupny` | `Martin Chalupny` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Elena Scheidlin` (person)
- `Anton Gotsch-Gasse 26, 8492 Klöchberg, Österreich` (address)

**Example 73** (doc_id: `deanon_BFG_TRAIN/132617.1`) (sent_id: `deanon_BFG_TRAIN/132617.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Panzerbieter  in der Beschwerdesache Konrad Schneidewendt,  Teschnergasse 4, 7574 Burgauberg, Österreich, über die Beschwerde vom 27.1.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 16.1.2020, SV-Nr, betreffend die Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Jänner 2020 zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Konrad Schneidewendt` | `Konrad Schneidewendt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Linn Panzerbieter` (person)
- `Teschnergasse 4, 7574 Burgauberg, Österreich` (address)

**Example 74** (doc_id: `deanon_BFG_TRAIN/132647.1`) (sent_id: `deanon_BFG_TRAIN/132647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Janet Spatzl,  Alois-Jenewein-Weg 17, 5124 Weyer, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH, Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 23. Februar 2017 gegen den  Bescheid des Finanzamtes Gänserndorf Mistelbach vom 21. Dezember 2016 betreffend  Einkommensteuer 2014, Steuernummer 30-739/8407, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Janet Spatzl` | `Janet Spatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alois-Jenewein-Weg 17, 5124 Weyer, Österreich` (address)
- `30-739/8407` (tax_number)

**Example 75** (doc_id: `deanon_BFG_TRAIN/132704.1`) (sent_id: `deanon_BFG_TRAIN/132704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Corinna Bastgen  in der Beschwerdesache Ernestine Josef,  Claretinergasse 28, 8530 Garanas, Österreich, vertreten durch König, Ermacora, Klotz & Partner Rechtsanwälte, Erlerstraße  4/3, 6020 Innsbruck, über die Beschwerde vom 6. Februar 2018 gegen die Bescheide des  Finanzamt Salzburg-Land  vom 23. Jänner 2018 betreffend Einkommensteuer 2014, Einkommensteuer 2015  und Einkommensteuervorauszahlungen 2018 zu Recht erkannt:   I. Der Beschwerde gegen den Einkommensteuerbescheid 2014 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Ernestine Josef` | `Ernestine Josef` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Corinna Bastgen` (person)
- `Claretinergasse 28, 8530 Garanas, Österreich` (address)
- `Finanzamt Salzburg-Land` (organisation)

**Example 76** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ernestine Schittenhelm, Clementinengasse 29, 8692 Krampen, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ernestine Schittenhelm` | `Ernestine Schittenhelm` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Clementinengasse 29, 8692 Krampen, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 77** (doc_id: `deanon_BFG_TRAIN/132794.1`) (sent_id: `deanon_BFG_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Edwin Uebel, Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich, vertreten durch Dkfm.

| Predicted | Gold |
|---|---|
| `Edwin Uebel` | `Edwin Uebel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich` (address)

**Example 78** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Claire Wielpütz  in der Beschwerdesache Stanislaus Calisir,  St.Martin Straße 8, 9463 Sommerau, Österreich, über die Beschwerde vom 15. Oktober 2013 gegen den Bescheid des  Finanzamtes Kufstein Schwaz vom 10.9.2013, StrNr, betreffend die Zurückweisung des  Antrages vom 8.8.2013 auf Rückerstattung des NoVA-Zuschlages gemäß § 6a NoVAG zu Recht  erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Claire Wielpütz` (person)
- `St.Martin Straße 8, 9463 Sommerau, Österreich` (address)

**Example 79** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Rebecca Woizeschke, Stöcklweg 2, 8632 Wegscheid, Österreich, vertreten durch Dr. Eva Deutsch-Goldoni, Waldwiese 4, 2540 Bad  Vöslau, über die Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 76-599/3261  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Rebecca Woizeschke` | `Rebecca Woizeschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Aigner` (person)
- `Stöcklweg 2, 8632 Wegscheid, Österreich` (address)
- `Dr. Eva Deutsch-Goldoni` (person)
- `76-599/3261` (tax_number)

**Example 80** (doc_id: `deanon_BFG_TRAIN/132878.1`) (sent_id: `deanon_BFG_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Sabrina Boger, Heugraben 15, 6233 Mariatal, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabrina Boger` | `Sabrina Boger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Heugraben 15, 6233 Mariatal, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 81** (doc_id: `deanon_BFG_TRAIN/132893.1`) (sent_id: `deanon_BFG_TRAIN/132893.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Ute Höltje, Burghof 44, 5222 Spreitzenberg, Österreich, vertreten durch KAPAS Steuerberatung GmbH, Birkfelder Straße 25, 8160 Weiz, über  die Beschwerde vom 19.12.2019 gegen den Bescheid des Finanzamtes FA vom 13.05.2020  betreffend Feststellung von Einkünften gemäß § 188 BAO 2018 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ute Höltje` | `Ute Höltje` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Burghof 44, 5222 Spreitzenberg, Österreich` (address)
- `KAPAS Steuerberatung GmbH` (organisation)

**Example 82** (doc_id: `deanon_BFG_TRAIN/132953.1`) (sent_id: `deanon_BFG_TRAIN/132953.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Vitalis Wienerth, Gewerbestraße Mitte 7, 4783 Stöbichen, Österreich, über die Beschwerde vom 28. Mai 2020 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 04-302/6040  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vitalis Wienerth` | `Vitalis Wienerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Gewerbestraße Mitte 7, 4783 Stöbichen, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `04-302/6040` (tax_number)

**Example 83** (doc_id: `deanon_BFG_TRAIN/132996.1`) (sent_id: `deanon_BFG_TRAIN/132996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bodo Broekhoven, Gallnbrunn 3, 5131 Pimbach, Österreich, über die Beschwerde vom 27. Oktober 2016 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. September 2016 betreffend Wiederaufnahme § 303 BAO / Sonstige  2009 des Verfahrens betreffend Einkommensteuer für das Jahr 2009 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bodo Broekhoven` | `Bodo Broekhoven` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gallnbrunn 3, 5131 Pimbach, Österreich` (address)

**Example 84** (doc_id: `deanon_BFG_TRAIN/133004.1`) (sent_id: `deanon_BFG_TRAIN/133004.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Corinna Köppelmann  in der Beschwerdesache Isidor Stahn,  Wattener Weg 12, 9321 Unterpassering, Österreich, betreffend Beschwerde vom 5. Mai 2020 gegen den Bescheid des Finanzamtes  Bruck Eisenstadt Oberwart vom 20. Februar 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 72-317/5629  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Isidor Stahn` | `Isidor Stahn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Corinna Köppelmann` (person)
- `Wattener Weg 12, 9321 Unterpassering, Österreich` (address)
- `72-317/5629` (tax_number)

**Example 85** (doc_id: `deanon_BFG_TRAIN/133011.1`) (sent_id: `deanon_BFG_TRAIN/133011.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Karin Erdönmez  in der Beschwerdesache Juri Haßler,  Breitau 43, 5143 Gietzing, Österreich, vertreten durch Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H,  Wienerstraße 73, 2604 Theresienfeld, betreffend Beschwerde vom 28. Februar 2020 gegen die  Bescheide des Finanzamtes Baden Mödling vom 31. Jänner 2020 betreffend Einkommensteuer  2015, 2016 und 2017, Steuernummer 32-409/1114, beschlossen:  Die Vorlageanträge vom 16. Februar 2021 gegen die Beschwerdevorentscheidungen 2015,  2016 und 2017 vom 15. Jänner 2021 werden gemäß § 260 Abs. 1 lit b BAO in Verbindung mit  § 264 Abs. 4 lit e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Haßler` | `Juri Haßler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Karin Erdönmez` (person)
- `Breitau 43, 5143 Gietzing, Österreich` (address)
- `Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `32-409/1114` (tax_number)

**Example 86** (doc_id: `deanon_BFG_TRAIN/133037.1`) (sent_id: `deanon_BFG_TRAIN/133037.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Hilde Guthehrle, Großalm 20, 8462 Fötschach, Österreich, über die Beschwerde vom 9. November 2017  gegen den Bescheid des Finanzamtes Österreich vom 19. Oktober 2017 betreffend Haftung für  Kapitalertragsteuer für die Jahre 2009 bis 2012, Steuernummer 38-294/0594, zu Recht  erkannt:   Der Beschwerde betreffend Haftung für Kapitalertragsteuer 2009 wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hilde Guthehrle` | `Hilde Guthehrle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Großalm 20, 8462 Fötschach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `38-294/0594` (tax_number)

**Example 87** (doc_id: `deanon_BFG_TRAIN/133114.1`) (sent_id: `deanon_BFG_TRAIN/133114.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Pamela Strauch, Durrach 45i, 8265 Kroisbach an der Feistritz, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 8.1.2020  gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich)  betreffend  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2013 vom 12.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2014 vom 13.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2015 vom 13.12.2019  zu Recht erkannt:   I. Soweit sich die Beschwerden vom 8.1.2020 gegen die Bescheide über die  Wiederaufnahme der Verfahren betreffend Einkommensteuer 2013, 2014 und 2015  richten, wird diesen gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Pamela Strauch` | `Pamela Strauch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Durrach 45i, 8265 Kroisbach an der Feistritz, Österreich` (address)
- `Pallauf Meißnitzer Staindl & Partner` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 88** (doc_id: `deanon_BFG_TRAIN/133133.1`) (sent_id: `deanon_BFG_TRAIN/133133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Tanja Klinglmayr, U-Bahn Station Vorgartenstraße 115, 4070 Grüben, Österreich, über die Beschwerde vom 3. November 2015 gegen die Bescheide des Finanzamtes  Bruck Eisenstadt Oberwart vom 1. Oktober 2015 betreffend Wiederaufnahme § 303 BAO /  ESt  01.10.2015 betreffend Einkommensteuer für die Jahre 2012 und 2013, Steuernummer  38-607/6324  zu Recht erkannt: .  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tanja Klinglmayr` | `Tanja Klinglmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `U-Bahn Station Vorgartenstraße 115, 4070 Grüben, Österreich` (address)
- `38-607/6324` (tax_number)

**Example 89** (doc_id: `deanon_BFG_TRAIN/133151.1`) (sent_id: `deanon_BFG_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Leila Togan  in der   Beschwerdesache Pia Minarsch, Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Pia Minarsch` | `Pia Minarsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Leila Togan` (person)
- `Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich` (address)

**Example 90** (doc_id: `deanon_BFG_TRAIN/133292.1`) (sent_id: `deanon_BFG_TRAIN/133292.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Gustav Luther  in der Beschwerdesache Richarda Linnenkugel,  Palmsdorf 57, 3972 Seifritz, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, gegen den Bescheid des Finanzamtes Wien 1/23 vom  8. Jänner 2019 betreffend Forschungsprämie § 108c EStG 1988 2015 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Richarda Linnenkugel` | `Richarda Linnenkugel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Gustav Luther` (person)
- `Palmsdorf 57, 3972 Seifritz, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 91** (doc_id: `deanon_BFG_TRAIN/133294.1`) (sent_id: `deanon_BFG_TRAIN/133294.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Christiane Ratzeburg, Untervocken 67, 4141 Wurzwoll, Österreich, vertreten durch Erich WOLF Wirtschaftsprüfungs  Gesellschaft m.b.H., Ferdinandstraße 4 Tür 4.OG, 1020 Wien, über die Beschwerde vom  27. April 2021 gegen den Bescheid des Finanzamtes Österreich vom 9. April 2021 betreffend  die Zurückweisung eines Antrag auf Verlustrücktrag (Einkommensteuer 2017 ) Steuernummer  10-546/3597  zu Recht:   I. Der angefochtene Bescheid wird – ersatzlos – aufgehoben.

| Predicted | Gold |
|---|---|
| `Christiane Ratzeburg` | `Christiane Ratzeburg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Untervocken 67, 4141 Wurzwoll, Österreich` (address)
- `Erich WOLF Wirtschaftsprüfungs  Gesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-546/3597` (tax_number)

**Example 92** (doc_id: `deanon_BFG_TRAIN/133301.1`) (sent_id: `deanon_BFG_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Francois Stürnkorb, Lobisser Straße 37, 4153 Schönberg, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Francois Stürnkorb` | `Francois Stürnkorb` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Lobisser Straße 37, 4153 Schönberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 93** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Huberta Schwandt, Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 30-672/6934  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Huberta Schwandt` | `Huberta Schwandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Krafft` (person)
- `Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich` (address)
- `Commendatio Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `30-672/6934` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/124843.1`) (sent_id: `deanon_BFG_TRAIN/124843.1_0`)


GZ. RV/7100201/2013 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der Beschwerdesache Bf, Adr, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 01.10.2012 (datiert mit 28.9.2012) gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom Juli 2012 betreffend Festsetzung von Normverbrauchsabgabe für Mai 2012 in Höhe von € 19.131,60 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128709.1`) (sent_id: `deanon_BFG_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Felizitas Muendl, Bakk. phil., Güttling 9, 9321 Latschach, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

**False Positives:**

- `Felizitas Muendl` — partial — pred is substring of gold: `Felizitas Muendl, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Felizitas Muendl, Bakk. phil.`(person)
- `Güttling 9, 9321 Latschach, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bauermeister Getränke` — type mismatch — same span as gold: `Bauermeister Getränke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `Mag. Dieter Walla`(person)
- `09-169/6729`(tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129336.1`) (sent_id: `deanon_BFG_TRAIN/129336.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Trafenfen Automotive,  Rebenland-Center-Straße 100, 4793 Ginzldorf, Österreich  vertreten durch Stb., über die Beschwerde vom 17.10.2011 gegen den Bescheid  des Finanzamtes Lilienfeld St. Pölten vom 13.7.2011 betreffend Einkommensteuer 2009 nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Trafenfen Automotive` — type mismatch — same span as gold: `Trafenfen Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Trafenfen Automotive`(organisation)
- `Rebenland-Center-Straße 100, 4793 Ginzldorf, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Helge Reinardy, Bakk. techn., Ganglweg 69, 9535 Penken, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  41-653/0116  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Helge Reinardy` — partial — pred is substring of gold: `Helge Reinardy, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Helge Reinardy, Bakk. techn.`(person)
- `Ganglweg 69, 9535 Penken, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `41-653/0116`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/130559.1`) (sent_id: `deanon_BFG_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Julia Nöllecke  in der Beschwerdesache Esra Leßnick, LLB,  Hackermillerstraße 133, 8940 Döllach, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  06-833/3820, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Esra Leßnick` — partial — pred is substring of gold: `Esra Leßnick, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Julia Nöllecke`(person)
- `Esra Leßnick, LLB`(person)
- `Hackermillerstraße 133, 8940 Döllach, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `06-833/3820`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

</details>

---

## `Title Preceded Name Pattern`

**F1:** 0.157 | **Precision:** 0.765 | **Recall:** 0.087  

**Format:** `regex`  
**Rule ID:** `e714b19d`  
**Description:**
Captures names preceded by 'RA' (Rechtsanwalt) or 'Dr.' without the academic suffix, ensuring the full name is captured.

**Content:**
```
\b((?:RA|Dr\.)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)+)(?![\s,]*Vollmacht)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.765 | 0.087 | 0.157 | 230 | 176 | 54 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 176 | 54 | 1831 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128700.1`) (sent_id: `deanon_BFG_TRAIN/128700.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Imre Schmidl  in der Beschwerdesache [...], [...],  über die Beschwerde vom 12. Februar 2018 gegen den Bescheid des Finanzamtes Lilienfeld St.  Pölten vom 16. Jänner 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Imre Schmidl` | `Dr. Imre Schmidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128709.1`) (sent_id: `deanon_BFG_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Felizitas Muendl, Bakk. phil., Güttling 9, 9321 Latschach, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Muendl, Bakk. phil.` (person)
- `Güttling 9, 9321 Latschach, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Dr. Gerlinde  Rieser` | `Dr. Gerlinde  Rieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Raphael Skowroneck, MBA` (person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129068.1`) (sent_id: `deanon_BFG_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Jens Spilken, Hillere 22, 8453 Saggau, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-228/4517  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jens Spilken` (person)
- `Hillere 22, 8453 Saggau, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `69-228/4517` (tax_number)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lubomir Baltßun` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129168.1`) (sent_id: `deanon_BFG_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  Dolores Jodjürgis, BA MBA, Feldsiedlung 87, 5242 Obereck, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dolores Jodjürgis, BA MBA` (person)
- `Feldsiedlung 87, 5242 Obereck, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Danelzik` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129520.1`) (sent_id: `deanon_BFG_TRAIN/129520.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Verwaltungsstrafsache  gegen KzlR Wolf Wältl, MBA, Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich, über die Beschwerde des Beschuldigten vom 26. März 2020  gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 10. März 2020, Zahl:  MA67/196700631216/2019, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Wolf Wältl, MBA` (person)
- `Am Pfarrerfeld 13, 9952 St. Johann im Walde, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129555.1`) (sent_id: `deanon_BFG_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache ÖkR Nadine Fritzekötter, Fahnbach 3, 3752 Nonnersdorf, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Nadine Fritzekötter` (person)
- `Fahnbach 3, 3752 Nonnersdorf, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Reinhard Komarova, Gabrielweg 4, 4725 Adelsgrub, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 92-139/9763  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reinhard Komarova` (person)
- `Gabrielweg 4, 4725 Adelsgrub, Österreich` (address)
- `92-139/9763` (tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/129583.1`) (sent_id: `deanon_BFG_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 11** (doc_id: `deanon_BFG_TRAIN/129828.1`) (sent_id: `deanon_BFG_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Pascal Beerlage, Tannwaldweg 35L, 9133 Jerischach, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 13-489/9399  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |
| `Dr. Helmut Herbert Moritz` | `Dr. Helmut Herbert Moritz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pascal Beerlage` (person)
- `Tannwaldweg 35L, 9133 Jerischach, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `13-489/9399` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Cedric Leutheusser, Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Cedric Leutheusser` (person)
- `Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Dr.in Ljiljana Kos` (person)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Example 15** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

| Predicted | Gold |
|---|---|
| `Dr. Sasan Hamzavi` | `Dr. Sasan Hamzavi` |

**Example 16** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Esmeralda Lubert, Kaschlgasse 9, 3100 Witzendorf, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esmeralda Lubert` (person)
- `Kaschlgasse 9, 3100 Witzendorf, Österreich` (address)
- `Sigrid Lamböck` (person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/130367.1`) (sent_id: `deanon_BFG_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Petra Ullemeyer, Mariexner Straße 8, 3141 Rassing, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Petra Ullemeyer` (person)
- `Mariexner Straße 8, 3141 Rassing, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 19** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 20** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  KzlR Leroy Krätschmar, Hohe Wand-Str. 12, 8345 Krusdorf, Österreich, über die Beschwerde vom 29. Mai 2019 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 30. April 2019 betreffend Rückforderung der  für VN-Sohn NN für den Zeitraum Jänner 2018 bis Dezember 2018 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Leroy Krätschmar` (person)
- `Hohe Wand-Str. 12, 8345 Krusdorf, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 21** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marlies Danzfuss, BSc` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

**Example 22** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Paula Jagiella, Medienpark 18, 3384 Eidletzberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paula Jagiella` (person)
- `Medienpark 18, 3384 Eidletzberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Dr. Elke Hager` | `Dr. Elke Hager` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wladimir Nüssli` (person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/130686.1`) (sent_id: `deanon_BFG_TRAIN/130686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde der  Alana Single, Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich, vom 19. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 17. August 2020, Zahl MA67/Zahl/2019, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alana Single` (person)
- `Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Matthäus Buskens` (person)
- `Edlach 19, 3141 Oberkilling, Österreich` (address)
- `Helmut Binder` (person)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130748.1`) (sent_id: `deanon_BFG_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Valentina Cagli, A. Böhm Gasse 67F, 4310 Oberzirking, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 76-512/9228  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentina Cagli` (person)
- `A. Böhm Gasse 67F, 4310 Oberzirking, Österreich` (address)
- `76-512/9228` (tax_number)

**Example 27** (doc_id: `deanon_BFG_TRAIN/130759.1`) (sent_id: `deanon_BFG_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Justin Feuerheerdt, Naglergasse 6, 4794 Grafendorf, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Justin Feuerheerdt` (person)
- `Naglergasse 6, 4794 Grafendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 28** (doc_id: `deanon_BFG_TRAIN/131365.1`) (sent_id: `deanon_BFG_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Mario Gajewska, Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mario Gajewska` (person)
- `Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 29** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Prof. Gernot Woortmann, Spitzbergweg 116, 3204 Tradigistgegend, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 16-817/8793  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Gernot Woortmann` (person)
- `Spitzbergweg 116, 3204 Tradigistgegend, Österreich` (address)
- `16-817/8793` (tax_number)

**Example 30** (doc_id: `deanon_BFG_TRAIN/131467.1`) (sent_id: `deanon_BFG_TRAIN/131467.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Vera Lüerß, BA, Gewerbepark Hinterholz 3, 4974 Stött, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, über die Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Wiederaufnahme der Einkommensteuerverfahren 2003 bis 2010 sowie vom  29.4.2013  betreffend Wiederaufnahme des Einkommensteuerverfahren 2011, Steuernummer  ***, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Lüerß, BA` (person)
- `Gewerbepark Hinterholz 3, 4974 Stött, Österreich` (address)
- `BKS Steuerberatung GmbH & Co  KG` (organisation)

**Example 31** (doc_id: `deanon_BFG_TRAIN/131467.1`) (sent_id: `deanon_BFG_TRAIN/131467.1_4`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Vera Lüerß, BA, Gewerbepark Hinterholz 3, 4974 Stött, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg an der Traisen, betreffend Beschwerde vom  18. Mai 2013 gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 26. April 2013  betreffend Einkommensteuer 2003 – 2010 und vom 29.4.2013 betreffend Einkommensteuer  2011, Steuernummer **, beschlossen:   Die Beschwerde vom 18. Mai 2013 wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Lüerß, BA` (person)
- `Gewerbepark Hinterholz 3, 4974 Stött, Österreich` (address)
- `BKS Steuerberatung GmbH & Co  KG` (organisation)

**Example 32** (doc_id: `deanon_BFG_TRAIN/131567.1`) (sent_id: `deanon_BFG_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Severin Wöllecke  in der Finanzstrafsache gegen die  Beschuldigte Nicole Schlemper, Uteweg 12, 9624 Latschach, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

| Predicted | Gold |
|---|---|
| `Dr. Severin Wöllecke` | `Dr. Severin Wöllecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nicole Schlemper` (person)
- `Uteweg 12, 9624 Latschach, Österreich` (address)
- `Mag. Heinz Wolfbauer` (person)

**Example 33** (doc_id: `deanon_BFG_TRAIN/131880.1`) (sent_id: `deanon_BFG_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Zacharias Moehring, Edmundshof 49j, 9020 Walddorf, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 77-674/4781  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zacharias Moehring` (person)
- `Edmundshof 49j, 9020 Walddorf, Österreich` (address)
- `77-674/4781` (tax_number)

**Example 34** (doc_id: `deanon_BFG_TRAIN/131914.1`) (sent_id: `deanon_BFG_TRAIN/131914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Paula Stokmann, Krastalstraße 1, 4707 Mitterndorf, Österreich, über die Beschwerde vom 28. Oktober 2019  gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 7. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 72-251/6474  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paula Stokmann` (person)
- `Krastalstraße 1, 4707 Mitterndorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `72-251/6474` (tax_number)

**Example 35** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf., Farchern 45, 4362 Kühweid, Österreich, über die Beschwerde vom 27. Mai 2016 gegen den  Bescheid des Finanzamtes KirchdorfPerg Steyr vom 27. April 2016 betreffend  Kapitalertragsteuer 2012 und die Bescheide vom 3. Mai 2016 betreffend Körperschaftssteuer  2012, 2013 und 2014, Steuernummer 77-859/7031, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Farchern 45, 4362 Kühweid, Österreich` (address)
- `77-859/7031` (tax_number)

**Example 36** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_86`)


Grundstücksmärkte und Immobilienenbewertung von Prof. Dr. Wolfgang Feilmayr)  eingegangen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Feilmayr` | `Dr. Wolfgang Feilmayr` |

**Example 37** (doc_id: `deanon_BFG_TRAIN/132215.1`) (sent_id: `deanon_BFG_TRAIN/132215.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Joshua Könker  in der Beschwerdesache Hildegard Kähler,  Dr.-Rudolf-Krause-Straße 59, 3161 Obergegend, Österreich, gegen den von der belangten Behörde Finanzamt Baden Mödling, nunmehr Finanzamt  Österreich, am 24. Mai 2018 ausgefertigten Bescheid mit der Bezeichnung „BESCHEID 2015“,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joshua Könker` | `Dr. Joshua Könker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hildegard Kähler` (person)
- `Dr.-Rudolf-Krause-Straße 59, 3161 Obergegend, Österreich` (address)
- `Finanzamt Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 38** (doc_id: `deanon_BFG_TRAIN/132368.1`) (sent_id: `deanon_BFG_TRAIN/132368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Hugo Denhart, Eichhorn 8, 9413 Hinterwölch, Österreich, vertreten durch Dr. Peter Eisele, Öffentlicher Notar, 7540 Güssing, Hauptplatz 1, über  die Beschwerde vom 18. Dezember 2017 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 11. Dezember 2017 betreffend Rechtsgebühr,  Steuernummer 10- 90-207/0668, Erf.Nr. 10- 2017, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Eisele` | `Dr. Peter Eisele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hugo Denhart` (person)
- `Eichhorn 8, 9413 Hinterwölch, Österreich` (address)
- `90-207/0668` (tax_number)

**Example 39** (doc_id: `deanon_BFG_TRAIN/132478.1`) (sent_id: `deanon_BFG_TRAIN/132478.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Juri Weich, Spitalanger 19, 3910 Ratschenhof, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 9. März 2015 betreffend Einkommensteuervorauszahlungen 2015 zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Weich` (person)
- `Spitalanger 19, 3910 Ratschenhof, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 40** (doc_id: `deanon_BFG_TRAIN/132482.1`) (sent_id: `deanon_BFG_TRAIN/132482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  MedR Roland Ruschemeier, Schöferhof 401, 9832 Untersteinwand, Österreich, über die Beschwerde vom 30. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 9. März 2020 betreffend Einkommensteuer  2018, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Roland Ruschemeier` (person)
- `Schöferhof 401, 9832 Untersteinwand, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_TRAIN/132501.1`) (sent_id: `deanon_BFG_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Huberta Petratschek, Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Huberta Petratschek` (person)
- `Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ernestine Schittenhelm, Clementinengasse 29, 8692 Krampen, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ernestine Schittenhelm` (person)
- `Clementinengasse 29, 8692 Krampen, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_TRAIN/132752.1`) (sent_id: `deanon_BFG_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Manuel de Keijzer, Schmieddorf 5, 6215 Achenkirch, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Maria Brandstetter` | `Dr. Maria Brandstetter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Manuel de Keijzer` (person)
- `Schmieddorf 5, 6215 Achenkirch, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 44** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Rebecca Woizeschke, Stöcklweg 2, 8632 Wegscheid, Österreich, vertreten durch Dr. Eva Deutsch-Goldoni, Waldwiese 4, 2540 Bad  Vöslau, über die Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 76-599/3261  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rebecca Woizeschke` (person)
- `Stöcklweg 2, 8632 Wegscheid, Österreich` (address)
- `Dr. Eva Deutsch-Goldoni` (person)
- `76-599/3261` (tax_number)

**Example 45** (doc_id: `deanon_BFG_TRAIN/132878.1`) (sent_id: `deanon_BFG_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Sabrina Boger, Heugraben 15, 6233 Mariatal, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sabrina Boger` (person)
- `Heugraben 15, 6233 Mariatal, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_TRAIN/132953.1`) (sent_id: `deanon_BFG_TRAIN/132953.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Vitalis Wienerth, Gewerbestraße Mitte 7, 4783 Stöbichen, Österreich, über die Beschwerde vom 28. Mai 2020 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 04-302/6040  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vitalis Wienerth` (person)
- `Gewerbestraße Mitte 7, 4783 Stöbichen, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `04-302/6040` (tax_number)

**Example 47** (doc_id: `deanon_BFG_TRAIN/133262.1`) (sent_id: `deanon_BFG_TRAIN/133262.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Dipl.-Ing. Liu Sklarzyk, Birnbaum 73, 6235 Scheffach, Österreich, über die Beschwerde vom 16. Oktober 2020 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 16. September 2020  betreffend Wiederaufnahme des Verfahrens hinsichtlich des Antrages auf Familienbeihilfe vom  22. Juli 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Liu Sklarzyk` (person)
- `Birnbaum 73, 6235 Scheffach, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_TRAIN/133301.1`) (sent_id: `deanon_BFG_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Francois Stürnkorb, Lobisser Straße 37, 4153 Schönberg, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Stürnkorb` (person)
- `Lobisser Straße 37, 4153 Schönberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Huberta Schwandt, Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 30-672/6934  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Gabriele Krafft` | `Dr. Gabriele Krafft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Huberta Schwandt` (person)
- `Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich` (address)
- `Commendatio Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `30-672/6934` (tax_number)

**Example 50** (doc_id: `deanon_BFG_TRAIN/133447.1`) (sent_id: `deanon_BFG_TRAIN/133447.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Kevin Griepekoven  in der Beschwerdesache Moritz Danielek,  Ulricusstraße 7, 6951 Lingenau, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des  Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Deutschlandsberg Leibnitz Voitsberg), jeweils  vom 11. Dezember  2014 betreffend    Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010,  jeweils zur Steuernummer 84-350/7355  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Kevin Griepekoven` | `Dr. Kevin Griepekoven` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Moritz Danielek` (person)
- `Ulricusstraße 7, 6951 Lingenau, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)
- `84-350/7355` (tax_number)

**Example 51** (doc_id: `deanon_BFG_TRAIN/134315.1`) (sent_id: `deanon_BFG_TRAIN/134315.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Karim Mauritz,  Derrenalpe 12, 3071 Lanzendorf, Österreich, vertreten durch Dr. Ceconi Andreas, Steuerberater, Schiffmanngasse 19, 5020  Salzburg, über die Beschwerde vom 22. August 2019 gegen den Bescheid des Finanzamtes  Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 25. Juli 2019 betreffend  Einkommensteuer 2012 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ceconi Andreas` | `Dr. Ceconi Andreas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karim Mauritz` (person)
- `Derrenalpe 12, 3071 Lanzendorf, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_TRAIN/134384.1`) (sent_id: `deanon_BFG_TRAIN/134384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Torsten Jokuschies, Taxerweg 19, 4952 Appersting, Österreich, vertreten durch Gstöttner & Partner  Steuerberatung Gesellschaft m.b.H. & Co. KG, Linzerstraße 10, 4320 Perg, über die Beschwerde  vom 26. Februar 2018 gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom  22. Jänner 2018 betreffend Feststellung der Einkünfte § 188 BAO 2011 Steuernummer  04-517/2751  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Torsten Jokuschies` (person)
- `Taxerweg 19, 4952 Appersting, Österreich` (address)
- `Gstöttner & Partner  Steuerberatung Gesellschaft m.b.H. & Co. KG` (organisation)
- `04-517/2751` (tax_number)

**Example 53** (doc_id: `deanon_BFG_TRAIN/134395.1`) (sent_id: `deanon_BFG_TRAIN/134395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Alice Märcklin, Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH,  Gauermanngasse 2-4, 1010 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich)  vom 25. Oktober 2018 betreffend Einkommensteuer 2016, Steuernummer 12-225/3285  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alice Märcklin` (person)
- `Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich` (address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH` (organisation)
- `Finanzamt Österreich` (organisation)
- `12-225/3285` (tax_number)

**Example 54** (doc_id: `deanon_BFG_TRAIN/134424.1`) (sent_id: `deanon_BFG_TRAIN/134424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Quirin Doster, Zunigalm 34, 4743 Osternach, Österreich, über die Beschwerde vom 31. März 2021 gegen den Bescheid des  Finanzamtes Österreich vom 24. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 55-758/2357  zu Recht erkannt:  I. Der angefochtene Bescheid wird wie mit Beschwerdevorentscheidung abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quirin Doster` (person)
- `Zunigalm 34, 4743 Osternach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `55-758/2357` (tax_number)

**Example 55** (doc_id: `deanon_BFG_TRAIN/134507.1`) (sent_id: `deanon_BFG_TRAIN/134507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Dipl.-Ing. Xaver Kühlwetter, Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich, vertreten durch Dr. Ferdinand Jenni, Jahngasse 18, 6850  Dornbirn, über die Beschwerde vom 10. November 2014 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Oktober 2014 betreffend Einkommensteuer 2013, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ferdinand Jenni` | `Dr. Ferdinand Jenni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Dipl.-Ing. Xaver Kühlwetter` (person)
- `Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich` (address)

**Example 56** (doc_id: `deanon_BFG_TRAIN/134703.1`) (sent_id: `deanon_BFG_TRAIN/134703.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Irene Hildebrecht  in der Beschwerdesache KommR Dipl.-Ing. ÖkR Valentina Steinbrunn,  Ebrasdorf 161, 4320 Oberwagram, Österreich, vertreten durch Dr. Anke Reisch, Franz-Reisch-Straße 4, 6370 Kitzbühel, über  die Beschwerde vom 28. Juni 2013 gegen die Bescheide des Finanzamtes Kitzbühel Lienz  (nunmehr: Finanzamt Österreich) vom 22. Mai 2013, Str. Nr. 36-608/1721, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Oktober 2010      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Dr. Anke Reisch` | `Dr. Anke Reisch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Irene Hildebrecht` (person)
- `KommR Dipl.-Ing. ÖkR Valentina Steinbrunn` (person)
- `Ebrasdorf 161, 4320 Oberwagram, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `36-608/1721` (tax_number)

**Example 57** (doc_id: `deanon_BFG_TRAIN/134786.1`) (sent_id: `deanon_BFG_TRAIN/134786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Adriana Himmelspach, Sulzegg 3i, 3122 Aichberg, Österreich, über die Beschwerde vom 6. September 2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. August 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2015, Einkommensteuer  (Arbeitnehmerveranlagung) 2016 und Einkommensteuer (Arbeitnehmerveranlagung) 2017  Steuernummer 30-977/4895  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adriana Himmelspach` (person)
- `Sulzegg 3i, 3122 Aichberg, Österreich` (address)
- `30-977/4895` (tax_number)

**Example 58** (doc_id: `deanon_BFG_TRAIN/134866.1`) (sent_id: `deanon_BFG_TRAIN/134866.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Daniel Priskorn  in der Beschwerdesache Felix Kerling,  Rassbergstraße 13, 3742 Passendorf, Österreich, wegen behaupteter Verletzung der Entscheidungspflicht des FA St. Johann Tamsweg Zell am See  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 beschlossen:   Die Säumnisbeschwerde wird als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Daniel Priskorn` | `Dr. Daniel Priskorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felix Kerling` (person)
- `Rassbergstraße 13, 3742 Passendorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)

**Example 59** (doc_id: `deanon_BFG_TRAIN/135025.1`) (sent_id: `deanon_BFG_TRAIN/135025.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr über den Antrag auf  Gewährung der Verfahrenshilfe vom 14. September 2021  der  Jan Schrötl, Eduard-Hanslick-Gasse 59, 9961 Plon, Österreich, im  Beschwerdeverfahren betreffend den vom Finanzamt Österreich erlassenen Bescheid vom  5. August 2021 betreffend die Einkommensteuer 2016 zu Steuernummer 85-359/2407  beschlossen:  Der Antrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jan Schrötl` (person)
- `Eduard-Hanslick-Gasse 59, 9961 Plon, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `85-359/2407` (tax_number)

**Example 60** (doc_id: `deanon_BFG_TRAIN/135060.1`) (sent_id: `deanon_BFG_TRAIN/135060.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Othmar Burgstahler, Andreas-Mayerplatz 6, 2020 Wieselsfeld, Österreich, vom 8. November 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 7. Oktober 2021, Zl. MA67/Zahl/2021,  iZmVerwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Othmar Burgstahler` (person)
- `Andreas-Mayerplatz 6, 2020 Wieselsfeld, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 61** (doc_id: `deanon_BFG_TRAIN/135287.1`) (sent_id: `deanon_BFG_TRAIN/135287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Bertram Säumenicht, De Venne-Weg 4, 2276 Katzelsdorf, Österreich, vom 30. Juni 2021, gegen den Bescheid des Finanzamtes  Österreich vom 8. Juni 2021, betreffend Rückforderung zu Unrecht bezogener Familienbeihilfe  und Kinderabsetzbeträge für den Zeitraum April 2018 bis Dezember 2019 sowie Februar 2020  und März 2020, zu Recht erkannt:   Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bertram Säumenicht` (person)
- `De Venne-Weg 4, 2276 Katzelsdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 62** (doc_id: `deanon_BFG_TRAIN/135372.1`) (sent_id: `deanon_BFG_TRAIN/135372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Jelena Priesterrath, Flohleiten 13, 5123 Kreuzlinden, Österreich, über die Beschwerde vom 17. September 2018  gegen den Bescheid des Finanzamtes Linz vom 23.August 2018 betreffend Einkommensteuer  2015 und 2016, Steuernummer 97-678/1705, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jelena Priesterrath` (person)
- `Flohleiten 13, 5123 Kreuzlinden, Österreich` (address)
- `97-678/1705` (tax_number)

**Example 63** (doc_id: `deanon_BFG_TRAIN/135536.1`) (sent_id: `deanon_BFG_TRAIN/135536.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_TRAIN/135955.1`) (sent_id: `deanon_BFG_TRAIN/135955.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Elisabeth Hafner in der Beschwerdesache  Dipl. Kff. Magdalena Girold, Georg Plattner-Straße 49, 3390 Pielachberg, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH,  Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom 30. September 2020 gegen die  Bescheide des Finanzamtes Klagenfurt vom 8. Juli 2020 betreffend  I. die Wiederaufnahme des Verfahrens zur Festsetzung des Vergütungsbetrages nach dem  Energieabgabenvergütungsgesetz für den Zeitraum 2014 und  II. die Festsetzung des Vergütungsbetrages nach dem Energieabgabengesetz für den Zeitraum  2014  I. zu Recht erkannt:  Der Beschwerde gegen den Bescheid betreffend die Wiederaufnahme des Verfahrens zur  Festsetzung des Vergütungsbetrages nach dem Energieabgabenvergütungsgesetz für den  Zeitraum 2014 wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Magdalena Girold` (person)
- `Georg Plattner-Straße 49, 3390 Pielachberg, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)

**Example 65** (doc_id: `deanon_BFG_TRAIN/136066.1`) (sent_id: `deanon_BFG_TRAIN/136066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die sechs Beschwerden  des Waltraud Czaikowski, Granitzen 40, 3730 Gauderndorf, Österreich, vertreten durch Dr. Josef Krist, Liebiggasse 4, 1010 Wien, vom  11. Februar 2021 (Anmerkung BFG, gemeint: 11. Februar 2022) gegen die Straferkenntnisse der  belangten Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 1)  17.01.2022, Zahl MA67/Zahl1/2021, 2) 19.01.2022, Zahl MA67/Zahl2/2021, 3) 19.01.2022, Zahl  MA67/Zahl3/2021, 4) 19.01.2022, Zahl MA67/Zahl4/2021, 5) 19.01.2022, Zahl  MA67/Zahl5/2021 und 6) 19.01.2022, Zahl MA67/Zahl6/2021, alle sechs wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird den sechs Beschwerden  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |
| `Dr. Josef Krist` | `Dr. Josef Krist` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waltraud Czaikowski` (person)
- `Granitzen 40, 3730 Gauderndorf, Österreich` (address)
- `BFG` (organisation)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 66** (doc_id: `deanon_BFG_TRAIN/136111.1`) (sent_id: `deanon_BFG_TRAIN/136111.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Gundula Schwartzmann, Stein an der Enns 4, 8793 Windischbühel, Österreich, vertreten durch BDO Audit GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien, über die Beschwerde gegen den  Bescheid des Finanzamtes Graz-Stadt vom 15. Dezember 2016 betreffend Festsetzung der  Umsatzsteuer 04.2012 und Umsatzsteuer 3.2015 Steuernummer 86-894/0847  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gundula Schwartzmann` (person)
- `Stein an der Enns 4, 8793 Windischbühel, Österreich` (address)
- `86-894/0847` (tax_number)

**Example 67** (doc_id: `deanon_BFG_TRAIN/136201.1`) (sent_id: `deanon_BFG_TRAIN/136201.1_1`)


IM NAMEN DER REPUBLI K  A.  Erkenntnis  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Karin Iosifescu, Bakk. iur., Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich, vertreten durch BDO Audit Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Am Belvedere 4, 1100 Wien, über die Beschwerde vom 17. Februar  2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom 6. Februar 2017 betreffend  1. Wiederaufnahme des Verfahrens der Vorsteuererstattung für 1-12/2012  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karin Iosifescu, Bakk. iur.` (person)
- `Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich` (address)

**Example 68** (doc_id: `deanon_BFG_TRAIN/136201.1`) (sent_id: `deanon_BFG_TRAIN/136201.1_6`)


B.  Beschluss  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Karin Iosifescu, Bakk. iur., Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich  vertreten durch BDO Audit Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Am Belvedere 4, 1100 Wien, über die Beschwerden vom 17. Februar  2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom 6. Februar 2017 betreffend die  (Sach-) Bescheide im  1. wiederaufgenommenen Verfahren der Vorsteuererstattung für 1-12/2012  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karin Iosifescu, Bakk. iur.` (person)
- `Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich` (address)

**Example 69** (doc_id: `deanon_BFG_TRAIN/136317.1`) (sent_id: `deanon_BFG_TRAIN/136317.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Gerlinde Schönheinz, Leinburger Straße 42B, 5113 Aglassing, Österreich, betreffend die Beschwerden vom 30. August 2019, 30. September  2019 und 31. September 2019 gegen die Bescheide des damaligen Finanzamtes 3/6/7/11/15  Schwechat Gerasdorf vom 25. Juli 2019 zu Steuernummer 63-118/1188  betreffend  Einkommensteuer 2012, sowie Umsatz-und Einkommensteuer 2014 bis 2017 beschlossen:  Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerlinde Schönheinz` (person)
- `Leinburger Straße 42B, 5113 Aglassing, Österreich` (address)
- `63-118/1188` (tax_number)

**Example 70** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter  Mag.Dr. Thomas Leitner sowie die fachkundigen Laienrichter Dipl.Ing. Christian Löw und  MMag.a Michaela Schmidt in der Beschwerdesache Beatrix Enke, Ried Riesberg 16, 2860 Stang, Österreich, vertreten  durch QUINTAX gerlich-fischer-kopp steuerberatungsgmbh, Ignaz-Rieder-Kai 13A, 5020  Salzburg, RA Dr. Fabian Maschke, Dominikanerbastei 17/11, 1010 Wien. und RA Rolf  Karpenstein, Gerhofstraße 40, D - 20354 Hamburg, über die Beschwerde vom 5. März 2013  gegen den Bescheid des FA Salzburg-Land vom 7. Februar 2013 betreffend Umsatzsteuer 2011,  die Beschwerde vom 31. März 2015 gegen den Bescheid des Finanzamtes Salzburg-Land vom 2.  März 2015 betreffend Umsatzsteuer 2013, die Beschwerde vom 1. Juli 2015 gegen den  Bescheid des Finanzamtes Salzburg-Land vom 11. Juni 2015 betreffend Umsatzsteuer 2014 und  die Beschwerde vom 5. Mai 2017 gegen den Bescheid des Finanzamtes Salzburg-Land vom 11.  April 2017 betreffend Umsatzsteuer 2015 zu Recht erkannt:  I. Die Bescheide betreffend Umsatzsteuer 2013, Umsatzsteuer 2014 und Umsatzsteuer 2015  werden jeweils dahingehend abgeändert, dass die Abgabenfestsetzung endgültig erfolgt.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Thomas Leitner` (person)
- `Beatrix Enke` (person)
- `Ried Riesberg 16, 2860 Stang, Österreich` (address)
- `RA Dr. Fabian Maschke` (person)
- `FA Salzburg-Land` (organisation)

**Example 71** (doc_id: `deanon_BFG_TRAIN/136764.1`) (sent_id: `deanon_BFG_TRAIN/136764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Lothar Rauchhaupt, Trabesing 17, 4643 Etzelsdorf, Österreich, über die Beschwerde vom 11. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 7. Mai 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 87-126/9127  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lothar Rauchhaupt` (person)
- `Trabesing 17, 4643 Etzelsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `87-126/9127` (tax_number)

**Example 72** (doc_id: `deanon_BFG_TRAIN/136778.1`) (sent_id: `deanon_BFG_TRAIN/136778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Laurentia Schnellert, Balzerlen 15l, 9334 Guttaringberg, Österreich  vertreten durch Dr. Michael Battlogg, Gerichtsweg 2, 6780 Schruns,  über die Beschwerde vom 20. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  26. April 2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 111 BAO zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Battlogg` | `Dr. Michael Battlogg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Laurentia Schnellert` (person)
- `Balzerlen 15l, 9334 Guttaringberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 73** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Jennifer Wildfang, Kirchbrücke 7, 3352 St. Peter in der Au-Markt, Österreich, über die Beschwerde vom 20. August 2013 gegen den Bescheid des  FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Körperschaftsteuer 2008 bis 2010,  Steuernummer 24-852/6682  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Wildfang` (person)
- `Kirchbrücke 7, 3352 St. Peter in der Au-Markt, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `24-852/6682` (tax_number)

**Example 74** (doc_id: `deanon_BFG_TRAIN/137197.1`) (sent_id: `deanon_BFG_TRAIN/137197.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Fiona Loeschel, Nelkenstraße 6, 3542 Grottendorf, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 3. März 2022 gegen den Bescheid des Finanzamtes Österreich  Finanzamtes Österreich vom 11. Februar 2022 betreffend Berichtigung (§ 293 BAO) des  Aufhebungsbescheides (§ 299 BAO) vom 3. Dezember 2021 hinsichtlich Einkommensteuer  2019 Steuernummer 29-264/6267  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Gabriele Krafft` | `Dr. Gabriele Krafft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Loeschel` (person)
- `Nelkenstraße 6, 3542 Grottendorf, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `29-264/6267` (tax_number)

**Example 75** (doc_id: `deanon_BFG_TRAIN/137353.1`) (sent_id: `deanon_BFG_TRAIN/137353.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Aurelia Hoentschke, MBA, U-Bahnstation XXXX - Adressbez, 1020 Wien, vertreten durch Mag. Dieter  Schneider, Gartengasse 21/10, 1050 Wien, über die Beschwerde vom 22. Dezember 2015  gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 23. November 2015 betreffend  Umsatzsteuer 2014, Steuernummer 12 469/6972 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aurelia Hoentschke, MBA` (person)
- `Mag. Dieter  Schneider` (person)

**Example 76** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Theobald Korschinek` | `Dr. Theobald Korschinek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dieter Papakiriakou` (person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich` (address)
- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 77** (doc_id: `deanon_BFG_TRAIN/137554.1`) (sent_id: `deanon_BFG_TRAIN/137554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Rebecca Blaschke, Zauchensee 25, 9342 Glanz, Österreich, vom 8. Juni 2020, gegen den Bescheid des Finanzamtes Österreich  vom 27. Mai 2020, betreffend Abweisung des Antrages auf Gewährung der erhöhten  Familienbeihilfe von November 2018 bis Februar 2022, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rebecca Blaschke` (person)
- `Zauchensee 25, 9342 Glanz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 78** (doc_id: `deanon_BFG_TRAIN/137567.1`) (sent_id: `deanon_BFG_TRAIN/137567.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Cassandra Franzas, Ketzerhub 14, 4730 Auwies, Österreich, vertreten durch Rudolf Peter, Esteplatz 3 Tür 9, 1030 Wien,  betreffend Beschwerde vom 20. Mai 2016 gegen die Bescheide des damaligen Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 21. April 2016 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) für 2009, 2010, 2012 und 2013, sowie den Bescheid vom 2.  Oktober 2019 betreffend Umsatzsteuer 2015, Steuernummer 57-376/4892, beschlossen:  I. a)

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cassandra Franzas` (person)
- `Ketzerhub 14, 4730 Auwies, Österreich` (address)
- `Rudolf Peter` (person)
- `57-376/4892` (tax_number)

**Example 79** (doc_id: `deanon_BFG_TRAIN/137587.1`) (sent_id: `deanon_BFG_TRAIN/137587.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Ewald Kiebeler, Gentzgasse 47, 9556 Eggen II, Österreich, betreffend Beschwerde vom 8. Februar 2022 gegen den Bescheid  des Finanzamtes Österreich vom 7. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 60-956/8538  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ewald Kiebeler` (person)
- `Gentzgasse 47, 9556 Eggen II, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `60-956/8538` (tax_number)

**Example 80** (doc_id: `deanon_BFG_TRAIN/137603.1`) (sent_id: `deanon_BFG_TRAIN/137603.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Klara Ericke  in der Beschwerdesache Bernarda Khalili,  Weizer Straße 46, 7461 Rauhriegel, Österreich, vertreten durch Dr. Helmut Grubmüller, Weyrgasse 5, 1030 Wien, über die  Beschwerde vom 22. Jänner 2020 gegen den Bescheid des Magistrats der Stadt Wien,  Rechnungs und Abgabenwesen, Referat Landes- und Gemeindeabgaben vom 23. Dezember  2019 betreffend Kommunalsteuer 2014 bis 2016, Steuernummer MA 6/***, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Grubmüller` | `Dr. Helmut Grubmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Klara Ericke` (person)
- `Bernarda Khalili` (person)
- `Weizer Straße 46, 7461 Rauhriegel, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 81** (doc_id: `deanon_BFG_TRAIN/137683.1`) (sent_id: `deanon_BFG_TRAIN/137683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Georg Unterwegner  in der Beschwerdesache Mathias Schneidermeier,  Juvinastraße 7, 6553 See, Österreich, Tschechische Republik, über die Beschwerde vom 13. Jänner 2021 gegen den  Bescheid des Finanzamt Tirol Ost  vom 15. Dezember 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 13-078/3886  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Georg Unterwegner` | `Dr. Georg Unterwegner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mathias Schneidermeier` (person)
- `Juvinastraße 7, 6553 See, Österreich` (address)
- `Finanzamt Tirol Ost` (organisation)
- `13-078/3886` (tax_number)

**Example 82** (doc_id: `deanon_BFG_TRAIN/137690.1`) (sent_id: `deanon_BFG_TRAIN/137690.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  KommR Zeno Henricy, Kaplan Herzlik Straße 2, 4962 Gundholling, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 13. August 2015 gegen die Bescheide des Finanzamtes Österreich vom  14. Juli 2015 betreffend  1. Wiederaufnahme des Verfahrens der Vorsteuererstattung für 01-03/2008  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Zeno Henricy` (person)
- `Kaplan Herzlik Straße 2, 4962 Gundholling, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 83** (doc_id: `deanon_BFG_TRAIN/137771.1`) (sent_id: `deanon_BFG_TRAIN/137771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr.in Wendy Norkus, Kohlhüttenweg 14, 4822 Obersee, Österreich, über die Beschwerde vom 25. März 2022 gegen  den Bescheid des Finanzamtes Österreich vom 17. März 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 Steuernummer 67-029/9262  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Wendy Norkus` (person)
- `Kohlhüttenweg 14, 4822 Obersee, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `67-029/9262` (tax_number)

**Example 84** (doc_id: `deanon_BFG_TRAIN/137800.1`) (sent_id: `deanon_BFG_TRAIN/137800.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Ilse Gasparetti, St.Christoph Straße 9, 4122 Stierberg, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 9. April 2018 gegen die Bescheide des Finanzamtes Graz- Stadt vom 5. März 2018 Steuernummer 71-367/7381   I. Über die Beschwerde vom 9. April 2018 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 5. März 2018 betreffend  1. Festsetzung von Umsatzsteuer für 01-12/2011  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ilse Gasparetti` (person)
- `St.Christoph Straße 9, 4122 Stierberg, Österreich` (address)
- `71-367/7381` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/130749.1`) (sent_id: `deanon_BFG_TRAIN/130749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Dr. OStR Benedikt Paszkowiak, Susalitsch 160, 8230 Staudach, Österreich, über die Beschwerde vom 28. Juni 2018 gegen  den Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 19. Juni 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Dr. OStR Benedikt Paszkowiak`(person)
- `Susalitsch 160, 8230 Staudach, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131742.1`) (sent_id: `deanon_BFG_TRAIN/131742.1_9`)


Die beschwerdeführende Partei sei der  Auffassung von Herrn Univ.-Prof. Dr. Reinhold Beiser (SWK 9/2017, 498): „Wenn es zu einer  Betriebsaufgabe kommt, so bleiben die Wertpapiere die vorher für die Ausnutzung eines  Gewinnfreibetrages angeschafft wurden, notwendiges nachträgliches Betriebsvermögen unter  der Voraussetzung, dass sie bis zum Ablauf der Behaltefrist gehalten werden.

**False Positives:**

- `Dr. Reinhold Beiser` — partial — pred is substring of gold: `Univ.-Prof. Dr. Reinhold Beiser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Dr. Reinhold Beiser`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/132030.1`) (sent_id: `deanon_BFG_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Bernadette Birkfeld, Pipitzhof 7, 3388 Knetzersdorf, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Bernadette Birkfeld`(person)
- `Pipitzhof 7, 3388 Knetzersdorf, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/132106.1`) (sent_id: `deanon_BFG_TRAIN/132106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jessica Osborn, Am Richardschacht 28, 2880 Lehen, Österreich, über die Beschwerde vom 5. Dezember 2014  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 6. November 2014 betreffend  Umsatzsteuer und Einkommensteuer 2012 und 2013 sowie gegen den Bescheid des  Finanzamtes Kirchdorf Perg Steyr vom 10. November 2014 betreffend Festsetzung des ersten  Säumniszuschlages von der Umsatzsteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Jessica Osborn`(person)
- `Am Richardschacht 28, 2880 Lehen, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/132731.1`) (sent_id: `deanon_BFG_TRAIN/132731.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat über die Beschwerde vom  11. September 2020 des Beschwerdeführers Sean Mütz, Seßlebene 15, 5661 Rauris, Österreich, vertreten durch die  Dr. Heinz Häupl Rechtsanwalts GmbH, 4865 Nußdorf, Stockwinkl 18, gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 10. August 2020  betreffend Abweisung des Antrages vom 24.07.2020 auf Aufhebung der  Umsatzsteuerbescheide 2011 und 2013 sowie der Einkommensteuerbescheide 2010, 2011  und 2013 gemäß § 299 Abs 1 BAO den Beschluss:      I)

**False Positives:**

- `Dr. Heinz Häupl Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sean Mütz`(person)
- `Seßlebene 15, 5661 Rauris, Österreich`(address)
- `Finanzamt Österreich`(organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Rebecca Woizeschke, Stöcklweg 2, 8632 Wegscheid, Österreich, vertreten durch Dr. Eva Deutsch-Goldoni, Waldwiese 4, 2540 Bad  Vöslau, über die Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 76-599/3261  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Eva Deutsch` — partial — pred is substring of gold: `Dr. Eva Deutsch-Goldoni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Aigner`(person)
- `Rebecca Woizeschke`(person)
- `Stöcklweg 2, 8632 Wegscheid, Österreich`(address)
- `Dr. Eva Deutsch-Goldoni`(person)
- `76-599/3261`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/133151.1`) (sent_id: `deanon_BFG_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Leila Togan  in der   Beschwerdesache Pia Minarsch, Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Michael Jöstl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Leila Togan`(person)
- `Pia Minarsch`(person)
- `Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/133689.1`) (sent_id: `deanon_BFG_TRAIN/133689.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin MMag.Dr. Ingrid Fehrer im  Beschwerdeverfahren über die Beschwerde der RgR Hartwig Mickus, Wetzles 3, 4323 Pilgram, Österreich, vom  3. August 2020 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 14. Mai  2020, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer  55-808/0270, mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom  3. August 2020 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2017 vom  14. Mai 2020 ein Vorlageantrag nicht eingebracht.

**False Positives:**

- `Dr. Ingrid Fehrer` — partial — pred is substring of gold: `MMag.Dr. Ingrid Fehrer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag.Dr. Ingrid Fehrer`(person)
- `RgR Hartwig Mickus`(person)
- `Wetzles 3, 4323 Pilgram, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `55-808/0270`(tax_number)
- `Bundesfinanzgerichts`(organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/134395.1`) (sent_id: `deanon_BFG_TRAIN/134395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Alice Märcklin, Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH,  Gauermanngasse 2-4, 1010 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich)  vom 25. Oktober 2018 betreffend Einkommensteuer 2016, Steuernummer 12-225/3285  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Erich Loitzl Straße` — partial — pred is substring of gold: `Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Alice Märcklin`(person)
- `Dr. Erich Loitzl Straße 11, 8342 Höf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Finanzamt Österreich`(organisation)
- `12-225/3285`(tax_number)

**Example 9** (doc_id: `deanon_BFG_TRAIN/134768.1`) (sent_id: `deanon_BFG_TRAIN/134768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache James Johanntokrax, Wandeckstraße 6, 4730 Aschach, Österreich, vertreten durch Mag. Manuela Henrich, Dr. Karl Renner Str. 5, 2560 Berndorf, über die  Beschwerde vom 28.06.2019  gegen den Bescheid des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich) vom 27. Mai 2019 betreffend Wiedereinsetzung in den vorigen Stand  nach Durchführung einer mündlichen Verhandlung betreffend Einkommensteuer für das Jahr  2012 Steuernummer 68-133/5727  zu Recht erkannt:   Die Beschwerde gegen die Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Karl Renner Str` — partial — gold is substring of pred: `Dr. Karl Renner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `James Johanntokrax`(person)
- `Wandeckstraße 6, 4730 Aschach, Österreich`(address)
- `Mag. Manuela Henrich`(person)
- `Dr. Karl Renner`(person)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `68-133/5727`(tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/135112.1`) (sent_id: `deanon_BFG_TRAIN/135112.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Zlatan Deisen  in der Beschwerdesache des  Prof. Richard Paulick, Scharmühlwinkel 13, 3144 Baumgarten, Österreich, über 1) die Beschwerde vom 27.9.2017 gegen den Bescheid des  Finanzamtes Bruck Leoben Mürzzuschlag (nunmehr Finanzamt Österreich) vom 4.9.2017  betreffend Umsatzsteuer 2015 sowie über 2) die Beschwerde vom 7.9.2018 gegen den  Bescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 21.8.2018 betreffend Abweisung  von Anträgen auf Aufhebung der Bescheide hinsichtlich Umsatzsteuer 2011 bis 2014 nach  Durchführung einer mündlichen Verhandlung am 2.12.2021 zu Recht erkannt:   I. Den Beschwerden wird Folge gegeben.

**False Positives:**

- `Dr. Zlatan Deisen` — partial — pred is substring of gold: `Dr. Dr. Zlatan Deisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dr. Zlatan Deisen`(person)
- `Prof. Richard Paulick`(person)
- `Scharmühlwinkel 13, 3144 Baumgarten, Österreich`(address)
- `Finanzamt Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_TRAIN/135571.1`) (sent_id: `deanon_BFG_TRAIN/135571.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Univ.-Prof. Quentin Gerdener  in der Beschwerdesache Hon.-Prof.in Tatjana Schweneke, MSc,  Moorweg 23, 9300 Hörzendorf, Österreich, vertreten durch Steuerberatung Dr. Alfred Sorger GmbH, Steyrergasse 89,  8010 Graz, über die Beschwerde vom 8.3.2018 gegen die Bescheide des Finanzamtes Graz- Umgebung vom 14.12.2017 betreffend Einkommensteuer und Umsatzsteuer, jeweils für die  Jahre 2007 bis 2012 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Dr. Alfred Sorger Gmb` — partial — pred is substring of gold: `Steuerberatung Dr. Alfred Sorger GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Univ.-Prof. Quentin Gerdener`(person)
- `Hon.-Prof.in Tatjana Schweneke, MSc`(person)
- `Moorweg 23, 9300 Hörzendorf, Österreich`(address)
- `Steuerberatung Dr. Alfred Sorger GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_TRAIN/136145.1`) (sent_id: `deanon_BFG_TRAIN/136145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Gernot Sieglen, Oberlederau 7, 4224 Klingenwehr, Österreich  wohnhaft, StNr.: X1, vertreten durch Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010 Wien, betreffend die Berufung vom  25.05.2011 gegen die Einkommensteuerbescheide für die Jahre 2008 und 2009, vom  9.05.2011, zugestellt am 12.05.2011, des Finanzamtes Bruck Eisenstadt Oberwart  zu Recht erkannt

**False Positives:**

- `Dr. Hans Bodendorfer  Steuerberatungsges` — partial — pred is substring of gold: `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Gernot Sieglen`(person)
- `Oberlederau 7, 4224 Klingenwehr, Österreich`(address)
- `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`(organisation)

**Example 13** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter  Mag.Dr. Thomas Leitner sowie die fachkundigen Laienrichter Dipl.Ing. Christian Löw und  MMag.a Michaela Schmidt in der Beschwerdesache Beatrix Enke, Ried Riesberg 16, 2860 Stang, Österreich, vertreten  durch QUINTAX gerlich-fischer-kopp steuerberatungsgmbh, Ignaz-Rieder-Kai 13A, 5020  Salzburg, RA Dr. Fabian Maschke, Dominikanerbastei 17/11, 1010 Wien. und RA Rolf  Karpenstein, Gerhofstraße 40, D - 20354 Hamburg, über die Beschwerde vom 5. März 2013  gegen den Bescheid des FA Salzburg-Land vom 7. Februar 2013 betreffend Umsatzsteuer 2011,  die Beschwerde vom 31. März 2015 gegen den Bescheid des Finanzamtes Salzburg-Land vom 2.  März 2015 betreffend Umsatzsteuer 2013, die Beschwerde vom 1. Juli 2015 gegen den  Bescheid des Finanzamtes Salzburg-Land vom 11. Juni 2015 betreffend Umsatzsteuer 2014 und  die Beschwerde vom 5. Mai 2017 gegen den Bescheid des Finanzamtes Salzburg-Land vom 11.  April 2017 betreffend Umsatzsteuer 2015 zu Recht erkannt:  I. Die Bescheide betreffend Umsatzsteuer 2013, Umsatzsteuer 2014 und Umsatzsteuer 2015  werden jeweils dahingehend abgeändert, dass die Abgabenfestsetzung endgültig erfolgt.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`
- `Dr. Fabian Maschke` — partial — pred is substring of gold: `RA Dr. Fabian Maschke`
- `RA Rolf  Karpenstein` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `Mag.Dr. Thomas Leitner`(person)
- `Beatrix Enke`(person)
- `Ried Riesberg 16, 2860 Stang, Österreich`(address)
- `RA Dr. Fabian Maschke`(person)
- `FA Salzburg-Land`(organisation)

**Example 14** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_46`)


Im Rahmen der am 28. April 2022 durchgeführten mündlichen Verhandlung wurde seitens der  Beschwerdeführerin durch ihren anwaltlichen Vertreter RA Rolf Karpenstein das  Beschwerdevorbringen zusammengefasst insbesondere dahingehend ergänzt, dass nach der  Maßgabe der Rsp des EuGH nicht von einem steuerbaren Leistungsaustausch auszugehen sei  und dass die Mehrwertsteuer für die Beschwerdeführerin mangels Überwälzbarkeit auf den  Kunden einen Kostenfaktor darstelle und dies dem Grundsatz der Neutralität der  Mehrwertsteuer zuwiderlaufe.

**False Positives:**

- `RA Rolf Karpenstein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_49`)


Durch den anwaltlichen Vertreter der Beschwerdeführerin RA  Dr. Fabian Maschke wurde weiters in Zusammenhang mit dem Beschwerdevorbringen der  unionsrechtlich gebotenen umsatzsteuerlichen Gleichbehandlung von konzessionierten und  nicht konzessionierten Spielbanken die Einholung eines Gutachtens eines gerichtlich beeideten  und zertifizierten Sachverständigen aus dem Fachbereich Glücks- und Geschicklichkeitsspiele  beantragt („zum Beweis dafür, dass der hier gegenständlich relevante Sachverhalt bzw die  Handlungen der Beschwerdeführerin nicht umsatzsteuerpflichtig sind“).

**False Positives:**

- `Dr. Fabian Maschke` — partial — pred is substring of gold: `RA  Dr. Fabian Maschke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA  Dr. Fabian Maschke`(organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/136576.1`) (sent_id: `deanon_BFG_TRAIN/136576.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Mag.a HR Florentine Schönhaar, Dr. Karl Stenzel-Gasse 36, 5124 Weyer, Österreich, vom 28. Februar 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 22. Februar 2022, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Dr. Karl Stenzel` — partial — pred is substring of gold: `Dr. Karl Stenzel-Gasse 36, 5124 Weyer, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a HR Florentine Schönhaar`(person)
- `Dr. Karl Stenzel-Gasse 36, 5124 Weyer, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/136626.1`) (sent_id: `deanon_BFG_TRAIN/136626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  Muran Jostmann, Franz-Pilz-Straße 20, 8854 Krakaudorf, Österreich, vertreten durch RA Dr. Gregor Klammer, Lerchenfelder Gürtel  45/11, 1160 Wien, vom 18. August 2017, gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 20. Juli 2017, betreffend Abweisung des Antrages auf  Gewährung der Familienbeihilfe von Juni 2015 bis Juli 2017, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gregor Klammer` — partial — pred is substring of gold: `RA Dr. Gregor Klammer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Doktor`(person)
- `Muran Jostmann`(person)
- `Franz-Pilz-Straße 20, 8854 Krakaudorf, Österreich`(address)
- `RA Dr. Gregor Klammer`(person)

</details>

---

## `Frau Title Name Pattern`

**F1:** 0.026 | **Precision:** 0.277 | **Recall:** 0.014  

**Format:** `regex`  
**Rule ID:** `8ba4434c`  
**Description:**
Captures person names following 'Frau', strictly requiring a valid name pattern immediately after and stopping at non-name characters to avoid false positives like 'Frau Grundsteuer'.

**Content:**
```
\bFrau\s+([A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*(?:\s+(?:LL\.B\.?\s+LL\.M\.?|LL\.M\.?\s+LL\.B\.?|B\.Sc|B\.A|B\.Ed|MA|LLB|BEd|B\.Ed|Bakk\.\s+techn\.|Bakk\.\s+iur\.|Bakk\.\s+rer\.\s+\w+|MSc|MBA|Dr\.[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Mag\.[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Univ\.-Prof\.(?:in)?[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Priv\.-Doz\.(?:in)?[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Hon\.-Prof\.(?:in)?[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|StR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|KommR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|\u00d6kR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|VetR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Ing\.[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|OSR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|OMedR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|KzlR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|RgR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|Techn\s+R[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*|MedR[\s]*[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*))?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.277 | 0.014 | 0.026 | 101 | 28 | 73 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 28 | 73 | 1967 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/130035.1`) (sent_id: `deanon_BFG_TRAIN/130035.1_10`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrates der Stadt Wien vom 5. August 2020, GZ. MA6/100/2019  (vormals: MA 6/ARP u.a.), wurde Frau Hedwig Brumund, Sparstraße 5, 4212 Pernau, Österreich (in weiterer Folge:  Beschuldigte) schuldig erkannt, sie habe als verantwortliche Beauftragte der AG von  01.09.2017 bis 24.01.2018 vor der Liegenschaft in Adresse1 auf dem öffentlichen  Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustelleneinrichtungsfläche  (Aufstellung eines Gerüstes) im Ausmaß von 52,50 m2 vorgenommen gehabt, wobei sie hiefür  bis zum 24.01.2018 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `Hedwig Brumund` | `Hedwig Brumund` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `Sparstraße 5, 4212 Pernau, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130035.1`) (sent_id: `deanon_BFG_TRAIN/130035.1_99`)


Von der AG wurde mitgeteilt, dass Frau Hedwig Brumund  von der AG als verantwortliche Beauftragte  gemäß § 9 Abs. 2 Satz 2 VStG bestellt wurde (vgl. vorgelegtes Schreiben vom 24. März 2015, in  dem Hedwig Brumund  ihrer Bestellung zum verantwortlichen Beauftragten zugestimmt hat).

| Predicted | Gold |
|---|---|
| `Hedwig Brumund` | `Hedwig Brumund` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_5`)


Entscheidungsgründe  I. Verfahrensgang:  1. Aufgrund einer anonymen Anzeige im April 2013 wurden finanzpolizeiliche Ermittlungen  durchgeführt und erhoben, dass Frau Martha Michenfelder (= Beschwerdeführerin, Bf) das Fahrzeug der  Marke X1, FIN Nr1, Erstzulassung (EZ) 1.10.2012, mit dem deutschen Kennzeichen AA1, im  Inland verwendet.

| Predicted | Gold |
|---|---|
| `Martha Michenfelder` | `Martha Michenfelder` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/132294.1`) (sent_id: `deanon_BFG_TRAIN/132294.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Frau Balthasar Jamrus, Ameisbühel 21, 8673 Landau, Österreich  damals vertreten durch WT, über die  Beschwerden der Abgabepflichtigen   1. vom 15. Dezember 2014 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf (nunmehr Finanzamt Österreich) vom 22. Oktober 2014 über die  Abweisung ihres Antrages auf Bewilligung von Aussetzungen der Einhebung vom 30. Juli  2014 betreffend die Einkommens- und Umsatzsteuer 2005-2011  2.

| Predicted | Gold |
|---|---|
| `Balthasar Jamrus` | `Balthasar Jamrus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Ameisbühel 21, 8673 Landau, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/132617.1`) (sent_id: `deanon_BFG_TRAIN/132617.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Konrad Schneidewendt (= Beschwerdeführerin, Bf), geb. Juni 1998, hatte mit Formular Beih100 im  September 2019 für sich die Zuerkennung der Familienbeihilfe (FB) wegen "Ausbildung" bzw.  "Lehre" mit einer voraussichtlichen Dauer bis 28.1.2022 beantragt.

| Predicted | Gold |
|---|---|
| `Konrad Schneidewendt` | `Konrad Schneidewendt` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_5`)


Im April 2012 hatte Frau Ute Kirchhoefel (= Beschwerdeführerin, Bf) eine Erklärung über die  Normverbrauchsabgabe (NoVA) und über den Erwerb neuer Fahrzeuge  (Fahrzeugeinzelbesteuerung) zum Fahrzeug MarkeX, FahrgestellNr. (FIN) 111xx, Leistung 90  kW, Benziner, CO²-Emission 144 g/km, Erwerb 30.10.2009, beim Finanzamt eingereicht;

| Predicted | Gold |
|---|---|
| `Ute Kirchhoefel` | `Ute Kirchhoefel` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_50`)


4. In dem dagegen fristgerecht eingebrachten Vorlageantrag vom 01.04.2020 wurde zunächst  auf die beiden Beschwerden verwiesen und weiter vorgebracht:  „Frau Reinhold Moellenkamp  ist Schweizer Staatsbürgerin.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_60`)


Frau Reinhold Moellenkamp  hat auch einen starken persönlichen Bezug zur Schweiz.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_65`)


Der  anonymen Anzeige ist unschwer zu entnehmen, dass irgendjemand Frau Reinhold Moellenkamp  und Herrn  4 von 9 Seite 5 von 9

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_68`)


Nachdem Herr A. erst seit 23.5.2016 in Ort1 (Ö) wohnhaft ist, ist es ausgeschlossen, dass Frau  Reinhold Moellenkamp  seit 5-6 Jahren bei ihm in Ort1 (Ö) wohnhaft ist.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 10** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_70`)


Frau  Reinhold Moellenkamp  hat Herrn A. erst vor ca 4 - 5 Jahren kennengelernt.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 11** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_71`)


Nachdem sich diese  Freundschaft intensivierte, kam Herr A. zu Frau Reinhold Moellenkamp  nach Ort1 (CH).

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 12** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_74`)


Frau Reinhold Moellenkamp  hat immer wieder bei ihrem Freund, Herrn A., übernachtet;

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 13** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_77`)


Frau Reinhold Moellenkamp  ist weder Eigentümerin, Mieterin, Ehegattin oder  sonst irgendwie nachhaltig berechtigt, im Haus von Herrn A. zu übernachten oder es sonst wie  zu nutzen.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 14** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_81`)


Er hat  regelmäßig zu Mittag bei Frau Reinhold Moellenkamp  gegessen und auch immer wieder bei ihr genächtigt.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 15** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_82`)


Er hatte dort auch familiären Kontakt zur Mutter von Frau Reinhold Moellenkamp.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 16** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_83`)


Entweder schläft Frau  Reinhold Moellenkamp  bei Herrn A., oder Herr A. bei Frau Reinhold Moellenkamp  in der Schweiz.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 17** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_84`)


Auch die  Wochenenden werden sowohl in Vorarlberg als auch in der Schweiz verbracht, wobei  diesbezüglich auf die Angaben von Frau Reinhold Moellenkamp  anlässlich ihrer Einvernahme vom  18.11.2019 verwiesen wird.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 18** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_85`)


Als die Beziehung ein Level erreicht hat, bei dem es um die Planung einer gemeinsamen  Zukunft ging, haben Frau Reinhold Moellenkamp  und Herr A. beschlossen, einen Immobilienmakler zu  beauftragen um ein Haus in der Schweiz zu suchen, in das sie gemeinsam einziehen und einen  gemeinsamen Wohnsitz gründen wollten.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 19** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_88`)


Frau Reinhold Moellenkamp  ist daher zweifellos in Ort1 (CH) steuerlich ansässig.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 20** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dieter Papakiriakou` | `Dieter Papakiriakou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Theobald Korschinek` (person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich` (address)
- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 21** (doc_id: `deanon_BFG_TRAIN/139792.1`) (sent_id: `deanon_BFG_TRAIN/139792.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 5. Juli 2021 beantragte Frau Jasper Eisenhoefer, die Beschwerdeführerin, die  Rückzahlung des Betrages von 1.374,00 €.

| Predicted | Gold |
|---|---|
| `Jasper Eisenhoefer` | `Jasper Eisenhoefer` |

**Example 22** (doc_id: `deanon_BFG_TRAIN/145500.1`) (sent_id: `deanon_BFG_TRAIN/145500.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Thaddäus Kusmierek  in der Beschwerdesache Sven Attanasio,  Rumänien , vertreten durch Frau Felicitas Niedermann, Rechtsanwältin, CH-8590 Romanshorn,  betreffend Säumnisbeschwerde vom 13.6.2024 betreffend Einkommensteuer 2022  (Arbeitnehmerveranlagung) gegen die Amtspartei FA Tirol Ost  beschlossen:  Das Beschwerdeverfahren wird gem. § 284 Abs 2 BAO eingestellt.   Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Felicitas Niedermann` | `Felicitas Niedermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Thaddäus Kusmierek` (person)
- `Sven Attanasio` (person)
- `FA Tirol Ost` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 23** (doc_id: `deanon_BFG_TRAIN/145907.1`) (sent_id: `deanon_BFG_TRAIN/145907.1_16`)


Im Vorlagebericht hat das Finanzamt unter Sacherhalt  ausgeführt:   „Sachverhalt:   Frau Adelheid Strehler  erhält regelmäßige Zahlungen aus dem Tronc (Trinkgeldkasse).

| Predicted | Gold |
|---|---|
| `Adelheid Strehler` | `Adelheid Strehler` |

**Example 24** (doc_id: `deanon_BFG_TRAIN/145907.1`) (sent_id: `deanon_BFG_TRAIN/145907.1_24`)


Im Vorlageantrag macht Frau Adelheid Strehler  die Steuerfreistellung der Trinkgelder geltend.

| Predicted | Gold |
|---|---|
| `Adelheid Strehler` | `Adelheid Strehler` |

**Example 25** (doc_id: `deanon_BFG_TRAIN/146516.1`) (sent_id: `deanon_BFG_TRAIN/146516.1_10`)


Mit drei Strafverfügungen vom 1) 24. September 2024, 2) und 3) 17. September 2024 wurde  der nunmehrigen Beschwerdeführerin (kurz: Bf.), Frau Dalibor Schlagböhmer  angelastet, sie habe als zur  Vertretung nach außen berufene Person der Zulassungsbesitzerin (Firma Firma) des in Rede  stehenden Fahrzeuges dem jeweils ordnungsgemäß zugestellten Verlangen der MA 67 vom 1)  10. Juli 2024, 2) 01. Juli 2024 und 3) 03. Juli 2024, jeweils innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem dieses Fahrzeug zu den genannten Zeitpunkten überlassen  worden sei, sodass dieses bei den genannten Örtlichkeiten gestanden sei, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Dalibor Schlagböhmer` | `Dalibor Schlagböhmer` |

**Example 26** (doc_id: `deanon_BFG_TRAIN/147375.1`) (sent_id: `deanon_BFG_TRAIN/147375.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Frau Enrico Landfried (Beschwerdeführerin, Bf.) betreibt am Standort Karl Kleinrath-Weg 5 - 8, 8010 Hönigtal, Österreich  einen  Gewerbebetrieb und wurde für die Jahre 2021 bis 2023 einer Lohnabgabenprüfung (PLB)  unterzogen.

| Predicted | Gold |
|---|---|
| `Enrico Landfried` | `Enrico Landfried` |

**Missed by this rule (FN):**

- `Karl Kleinrath-Weg 5 - 8, 8010 Hönigtal, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_44`)


Demnach war Frau RgR Univ.-Prof.in KommR Corinna Bebenek  von 01.12.2010 bis zum 29.02.2012 bei A R. als  Dienstnehmerin beschäftigt.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_46`)


Frau Bf war laut  Gewerberegisterauszug gewerberechtliche Geschäftsführerin im Mietwagengewerbe vom  07.12.2010 bis zum 07.02.2012.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_50`)


Aus den gewerberechtlichen Unterlagen ist ersichtlich, dass Frau Bf von 05.05.2011 bis  23.02.2012 auch gewerberechtliche Geschäftsführerin betreffend das Taxigewerbe mit den  Standorten X., Y. und Z. war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_63`)


Der  Abfluss von Bargeldbeständen wurde unter anderem damit erklärt, dass Frau Bf zusätzliche  Gelder erhalten hätte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_69`)


„Frau RgR Univ.-Prof.in KommR Corinna Bebenek  war von 1.12.2010 bis 29.02.2012 bei A R. als Dienstnehmerin  (Dienstgeberkonto lautend auf Personenbeförderung W T.) beschäftigt.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_72`)


Laut Gewerberegisterauszug war Frau Bf gewerberechtliche Geschäftsführerin im  Mietwagengewerbe für die Standorte Y., X. und Z. vom 7.12.2010 bis zum 23.2.2012.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_75`)


Aus den gewerberechtlichen Unterlagen ist ersichtlich, dass Frau Bf vom 5.5.2011 bis  23.02.2012 auch gewerberechtliche Geschäftsführerin betreffend das Taxigewerbe mit den  Standorten X., Y. und Z. war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_77`)


Bei der Einvernahme der Frau RgR Univ.-Prof.in KommR Corinna Bebenek  am 2.12.2013 am FA U. P. R als Zeugin wurden  folgende Unterlagen übergeben: Jahreslohnkonten, Auszug Gewerbeberechtigungen  Taxigewerbe und Mietwagengewerbe, Stundenaufzeichnung Dezember 2010, händische  Auszahlungslisten Mai, Juni, Juli, August, September, Oktober 2011 und Übersicht  Auszahlungsliste Februar 2012 und oa. Sachverhalt mitgeteilt.  Für die Behörde ist in freier Würdigung der der Beschwerdeführerin zur Kenntnis gebrachten  Beweismittel erwiesen, dass Frau RgR Univ.-Prof.in KommR Corinna Bebenek  für die zur Verfügungstellung der Taxikonzession  zusätzlich zu den am Lohnkonto ausgewiesenen Beträge € 7.000,- in bar übergeben wurden.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Univ.-Prof.in KommR Corinna Bebenek`
- `Rg` — similar text (different position): `RgR Univ.-Prof.in KommR Corinna Bebenek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)
- `RgR Univ.-Prof.in KommR Corinna Bebenek`(person)

**Example 8** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_181`)


Seite des Protokolls der  Zeugeneinvernahme von Frau Bf befindet sich eine Stundenaufzeichnung über angebliche  Leistungen der Frau Bf im Dezember 2010.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 9** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_183`)


Es bedarf mE keiner graphologischen  Fachkenntnis, um festzustellen, dass die hier aufscheinende Unterschrift sich von jenen  unterscheidet, welche im Steuerakt der Frau Bf und auf bei mir befindlichen Unterlagen  mehrmalig aufscheint.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/128739.1`) (sent_id: `deanon_BFG_TRAIN/128739.1_196`)


Die Beschwerdeführerin  bestreitet jedoch wiederholt die Korrektheit einer Stundenaufzeichnung über angebliche  Leistungen der Frau Bf im Dezember 2010, welche jedoch nicht Grundlage für die  Abgabenfestsetzung war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/129437.1`) (sent_id: `deanon_BFG_TRAIN/129437.1_16`)


Eine weitere Bestätigung der X- Versicherung a.G. vom 2.5.2019 enthält folgenden Passus: „…Da Sie und Ihre Frau Ihren  Wohnsitz ins Ausland verlegt haben, unterliegen Sie nicht der Versicherungspflicht in  Deutschland.

**False Positives:**

- `Ihren  Wohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Margot Artner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Margot Artner`(person)

**Example 13** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Grillenreith`(city)

**Example 14** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 15** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 16** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_93`)


Im Antwortschreiben vom 7.12.2020 wird seitens der Bf ausgeführt:  " … Ad 1) Frau Dl Bf hat im strittigen Zeitraum ab Oktober 2012 nach ihren Angaben und nach  ihrer Erinnerung mehrmals monatlich die Strecke D/Y (Hauptwohnsitz) nach A/X  (Nebenwohnsitz) zurück gelegt.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_97`)


Herr und Frau Bf besuchen dort  gemeinsam Restaurants, das FitnessCenter, Ärzte oder absolvieren Theaterbesuche.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_98`)


In Land3 besitzt Frau Dl Bf ein Haus, das sie alle ca. 6 Wochen im Jahr für einige Tage entweder  allein oder mit ihrem Gatten aufsucht.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_103`)


Überdies besitzt es einen großen Obstgarten mit ca. 800 m2 (Kirschen, Äpfel,  Pflaumen, Walnüsse), die jedes Jahr von Frau Dl Bf selbst geernet werden.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_104`)


Anmerkungen:  Der Vollständigkeit halber möchten wir festhalten, dass Frau Dl Bf immer ihren Hauptwohnsitz  in Deutschland, D/Z bzw. D/Y, hatte.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_111`)


Frau Dl Bf ist und war ausschließlich in Deutschland versichert, bezahlt ihre Steuern nur in  Deutschland und war stets in Deutschland beschäftigt (XX) und wohnhaft (Hauptwohnsitz).

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_114`)


Herr C ist 1985  nach Österreich zurückgekehrt, Frau Bf hat ihren deutschen Hauptwohnsitz hingegen  beibehalten.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_117`)


Nach ihrer Pensionierung ist Frau Dl Bf von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_122`)


Frau Dl Bf hat sich immer wieder in A/X aufgehalten.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_125`)


Frau Dl Bf hat nie die Aussage getätigt, dass sie sich zu irgend einem Zeitpunkt überwiegend in  Österreich aufhält. Dies wäre schlichtweg falsch.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/133721.1`) (sent_id: `deanon_BFG_TRAIN/133721.1_548`)


Relevantes daraus (siehe auch Abschnitt H/k):  Aus Seite 10 f. des ersten Teiles (vor Schriftführerwechsel) des Protokolles über den ersten  Verhandlungstag 22.6.2011: Die vorsitzende Richterin hielt dem Angeklagten (GesGf1) ein  Gespräch mit Frau Lohnbüro vor, deren Lohnbüro sich mit der Verwaltung der Arbeiter der Fa.  41 von 75 Seite 42 von 75

**False Positives:**

- `Lohnbüro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/133721.1`) (sent_id: `deanon_BFG_TRAIN/133721.1_550`)


Der Angeklagte gab an, oft mit Frau Lohnbüro telefoniert zu haben, weil  GesGfSubUnt1 (Geschäftsführer der Fa. SubUnt1) selten erreichbar gewesen sei (zweimal pro  Woche) und den Angeklagten gebeten habe, die Urlaubsmeldungen der SubUnt1-Arbeiter dem  Lohnbüro Lohnbüro mitzuteilen.

**False Positives:**

- `Lohnbüro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_73`)


Erst vor ca 3 Jahren besuchte Frau Reinhold Moellenkamp  Herrn A. erstmals in Ort1  (Ö).

**False Positives:**

- `Reinhold Moellenkamp  Herrn` — partial — gold is substring of pred: `Reinhold Moellenkamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reinhold Moellenkamp`(person)

**Example 30** (doc_id: `deanon_BFG_TRAIN/136066.1`) (sent_id: `deanon_BFG_TRAIN/136066.1_9`)


Das Fahrzeug sei auf Frau Frau, AdrFrau, zugelassen gewesen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_TRAIN/136358.1`) (sent_id: `deanon_BFG_TRAIN/136358.1_10`)


Zu besagtem Zeitpunkt war ich sehr wohl der Erwachsenenvertreter von Frau Frau2.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_TRAIN/137644.1`) (sent_id: `deanon_BFG_TRAIN/137644.1_5`)


Entscheidungsgründe  I. Verfahrensgang  A. Erklärung, Ersuchen um Ergänzung  Im Rahmen der am 01.03.2019 eingereichten Erklärung zur Arbeitnehmerveranlagung 2018  wurden von Frau Theodor von den Hoff (in der Folge „Beschwerdeführerin“ oder „Bf“) Werbungskosten für  – unter anderem – beruflich veranlasste Reisekosten in Höhe von EUR 5.435,71 geltend  gemacht.

**False Positives:**

- `Theodor` — partial — pred is substring of gold: `Theodor von den Hoff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodor von den Hoff`(person)

**Example 33** (doc_id: `deanon_BFG_TRAIN/139993.1`) (sent_id: `deanon_BFG_TRAIN/139993.1_23`)


Am 06.02.2023 fand vor dem erkennenden Gericht eine mündliche Verhandlung statt, im Zuge  derer auch Frau Name als Zeugin einvernommen wurde;

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_TRAIN/140059.1`) (sent_id: `deanon_BFG_TRAIN/140059.1_10`)


Mit Schreiben vom 22. November 2022 teilte das Sozialministeriumservice dem Magistrat mit,  dass der Parkausweis mit der Nummer Nr2 für Frau Frau1 ausgestellt worden und unbefristet  gültig sei.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_TRAIN/140059.1`) (sent_id: `deanon_BFG_TRAIN/140059.1_39`)


Eine Nachfrage beim Sozialministeriumservice Wien habe ergeben, dass der Ausweis gem.  §29b StVO 1960 mit der Nummer Nr2 auf Frau Frau6, ausgestellt worden sei.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_TRAIN/140303.1`) (sent_id: `deanon_BFG_TRAIN/140303.1_273`)


Betreffend der von der BF getätigten Investitionen der BF in das private Wohnhaus von Frau  MR (vgl. oben unter Punkt 2 getroffene Feststellungen zu den Tz 11, 12, 13, 14, 15, 16, 17, 18,  22, 23 und 26) ist von einer verdeckten Ausschüttung „an der Wurzel“ auszugehen, da die  Investitionen in das Eigentum der Gebäudeeigentümerin MR übergegangen sind (die von der  BF getätigten Investitionen stellen keine selbständigen Wirtschaftsgüter dar, sondern sind  unselbständiger Bestandteil des privaten Wohngebäudes), ohne dass eine Abgeltung der  Investitionen durch Frau Rotschopf vereinbart worden oder eine Nutzung durch die BF erfolgt  wären.

**False Positives:**

- `Rotschopf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_TRAIN/140303.1`) (sent_id: `deanon_BFG_TRAIN/140303.1_283`)


Betreffend der angeführten Privataufwendungen sind die Zuflusszeitpunkte entsprechend den  Feststellungen der belangten Behörde zu jenen Zeitpunkten anzunehmen, an denen die  Empfängerin (= Frau Rotschopf) über den Vorteil verfügen konnte, also mit der Einbuchung der  – fälschlicherweise – auf die BF ausgestellten Rechnungen durch die BF.

**False Positives:**

- `Rotschopf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_TRAIN/140350.1`) (sent_id: `deanon_BFG_TRAIN/140350.1_56`)


Die Kosten für die Erstellung von Förderanträgen sowie Kosten für Gutachter wurden nicht wie  von [der Komplementärin] behauptet von der [Bf.] getragen, sondern von den Förderstellen  bzw. Gutachtern direkt an die Fa. Z verrechnet und von dieser auch bezahlt. Dies ergab eine  Erhebung durch die steuerliche Vertretung bei einem der Gutachter, wie mir Frau Mag. H  (steuerliche Vertreterin der Bf.) im Rahmen der Nachschau mitteilte.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_TRAIN/140350.1`) (sent_id: `deanon_BFG_TRAIN/140350.1_153`)


Die Kosten für die Erstellung von  Förderanträgen sowie Kosten für Gutachter wurden nicht wie von [der Komplementärin]  behauptet von der [Bf.] getragen, sondern von den Förderstellen bzw. Gutachtern direkt an die  Fa. Z verrechnet und von dieser auch bezahlt. Dies ergab eine Erhebung durch die steuerliche  Vertretung bei einem der Gutachter, wie mir Frau Mag. H (steuerliche Vertreterin der Bf.) im  Rahmen der Nachschau mitteilte.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_173`)


In Bezug auf die Frage der Ansässigkeit gemäß MwStSystRL bei einer Wohnungsvermietung  ist zudem darauf zu verweisen, dass Generalanwältin Kokott im EuGH-Verfahren Ingrid  Schmelz gegen Finanzamt Waldviertel, Rechtssache C-97/09, erklärte, Frau Schmelz, eine  deutsche Staatsbürgerin mit Wohnsitz in Deutschland, welche in Ostösterreich eine Wohnung  vermietet hatte, habe gemäß der Mehrwertsteuersystemrichtlinie als in Österreich ansässige  Person zu gelten (vgl. Endfellner, FJ 2010, 270, zweitletzter Aufzählungspunkt).

**False Positives:**

- `Schmelz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Waldviertel`(organisation)

**Example 41** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_174`)


Darauf  hinzuweisen ist weiters, dass der Rat der Europäischen Union die Erheblichkeit der vorgelegten  Frage der Vereinbarkeit der Kleinunternehmerregelung in der Richtlinie mit dem Primärrecht  bezweifelte, zumal sich die Frage der Ansässigkeit von Frau Schmelz in Österreich stelle (EuGH- Urteil in der Sache Schmelz, Rz 27).

**False Positives:**

- `Schmelz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_176`)


Inhaltlich  traf der EuGH jedoch zur Frage der Ansässigkeit von Frau Schmelz keine Aussagen, womit die  Rechtsmeinungen der Generalanwältin und des Rates der Europäischen Union nichts an  Relevanz verloren haben.

**False Positives:**

- `Schmelz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_181`)


Im Ergebnis erklärte der EuGH, eine Ansässigkeit von  Frau Schmelz in Deutschland bzw. eine Nichtansässigkeit in Österreich könne nicht von  vornherein ausgeschlossen werden, was für die Zulässigkeit der Vorlagefragen ausgereicht hat,  aber kein inhaltliches Urteil darstellt. Zu verweisen ist auch auf Ritter in LJZ 1998, 67, wonach  eine Zurückweisung von Auslegungsersuchen „nur in extremen Ausnahmefällen in Betracht“  kommt.

**False Positives:**

- `Schmelz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_184`)


So leitete der UFS Wien aus der fehlenden Zurückweisung des  Vorabentscheidungsersuchens unzulässigerweise ab, der EuGH habe die Ansicht vertreten,  Frau Schmelz - die zwischenzeitlich verstorben war - sei für Zwecke der Umsatzsteuer in  Deutschland ansässig gewesen, obwohl sich der EuGH inhaltlich mit der Frage der Ansässigkeit  gar nicht auseinandergesetzt hatte.

**False Positives:**

- `Schmelz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_188`)


Der UFS Wien  prüfte die Frage der Ansässigkeit von Frau Schmelz nur in Bezug auf eine allfällige feste  Niederlassung, nicht jedoch bezüglich des Kriteriums des Sitzes der wirtschaftlichen Tätigkeit.

**False Positives:**

- `Schmelz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_TRAIN/141448.1`) (sent_id: `deanon_BFG_TRAIN/141448.1_4`)


Mit Anträgen Beih3 und Beih100 vom 19.4.2021 hat Frau Quentin Groeber, BA (= Beschwerdeführerin,  Bf), geb. 01/1967, die Zuerkennung von Familienbeihilfe (FB) sowie des FB-Erhöhungsbetrages  wegen erheblicher Behinderung für sich beantragt.

**False Positives:**

- `Quentin Groeber` — partial — pred is substring of gold: `Quentin Groeber, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Quentin Groeber, BA`(person)

**Example 47** (doc_id: `deanon_BFG_TRAIN/141448.1`) (sent_id: `deanon_BFG_TRAIN/141448.1_32`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:  ja  GdB liegt vor seit:      10/2021  Frau Quentin Groeber, BA  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:   JA  Dies besteht seit:      10/2021  Anmerkung bzw Begründung betreffend die Fähigkeit bzw voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Tätigkeiten nur unter ständiger Aufsicht und Anleitung möglich, keine abgeschlossene Lehre  o.ä.  Dauerzustand …..".

**False Positives:**

- `Quentin Groeber` — partial — pred is substring of gold: `Quentin Groeber, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Quentin Groeber, BA`(person)

**Example 48** (doc_id: `deanon_BFG_TRAIN/141448.1`) (sent_id: `deanon_BFG_TRAIN/141448.1_81`)


Frau Quentin Groeber, BA  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:   JA   Dies besteht seit:     09/2020   5 von 23 Seite 6 von 23

**False Positives:**

- `Quentin Groeber` — partial — pred is substring of gold: `Quentin Groeber, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Quentin Groeber, BA`(person)

**Example 49** (doc_id: `deanon_BFG_TRAIN/141448.1`) (sent_id: `deanon_BFG_TRAIN/141448.1_222`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:   ja  GdB liegt vor seit:             09/2020  ……..  Frau Quentin Groeber, BA  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:    JA  Dies besteht seit:             09/2020  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Die Intelligenzminderung wurde erstmals 09/2020 in einem der vorgelegten Befunde  beschrieben.

**False Positives:**

- `Quentin Groeber` — partial — pred is substring of gold: `Quentin Groeber, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Quentin Groeber, BA`(person)

**Example 50** (doc_id: `deanon_BFG_TRAIN/142376.1`) (sent_id: `deanon_BFG_TRAIN/142376.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin, Frau Bf (in der Folge Beschwerdeführerin: Bf) brachte am 30.06.2021  ihre Erklärung zur Arbeitnehmerveranlagung 2020 beim Finanzamt elektronisch ein und  erklärte neben einer bezugauszahlenden Stelle tatsächliche Kosten bei Behinderung in Höhe  von 150,00 Euro als außergewöhnliche Belastung.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_TRAIN/142995.1`) (sent_id: `deanon_BFG_TRAIN/142995.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Aron Sperle  in der Angelegenheit der Parteien  Gottfried Schwärzl (Beschwerdeführerin), vertreten durch Frau Mag. Martina Elsner, 9020 Klagenfurt  und Finanzamt Österreich als Amtspartei und als Gesamtrechtsnachfolger des Finanzamt Gmunden Vöcklabruck  über  die Beschwerde vom 1.2.2020 gegen den Bescheid des Finanzamtes vom 27.1.2020 betreffend  Abweisung des Antrages vom 4.10.2019 auf Aufhebung des Einkommensteuerbescheides 2018  vom 10.7.2019 und über die Beschwerde vom 8.5.2020 gegen die Beschwerdevorentscheidung  vom 26.3.2020  beschlossen:  Die Beschwerde vom 8.5.2020 gegen die Beschwerdevorentscheidung vom 26.3.2020 wird  zurückgewiesen.

**False Positives:**

- `Mag` — similar text (different position): `Mag. Aron Sperle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Aron Sperle`(person)
- `Gottfried Schwärzl`(person)
- `Mag. Martina Elsner`(person)
- `Finanzamt Österreich`(organisation)
- `Finanzamt Gmunden Vöcklabruck`(organisation)

**Example 52** (doc_id: `deanon_BFG_TRAIN/144052.1`) (sent_id: `deanon_BFG_TRAIN/144052.1_9`)


Die von Frau Mag. Janosch Moehrle, Bakk. rer. nat.  bis zu ihrer Übersiedelung in  1 von 10 Seite 2 von 10

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Janosch Moehrle, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Janosch Moehrle, Bakk. rer. nat.`(person)

**Example 53** (doc_id: `deanon_BFG_TRAIN/144052.1`) (sent_id: `deanon_BFG_TRAIN/144052.1_17`)


Vom UG wurde von Frau Mag. Janosch Moehrle, Bakk. rer. nat.  die Dusche mit WC, der 1. Lagerraum als Bügelzimmer, der  Hobbyraum als Fitnessraum und der 2. Lagerraum als Wäsche und Trockenraum, sowie  Aktenlager verwendet.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Janosch Moehrle, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Janosch Moehrle, Bakk. rer. nat.`(person)

**Example 54** (doc_id: `deanon_BFG_TRAIN/144052.1`) (sent_id: `deanon_BFG_TRAIN/144052.1_37`)


Ich helfe seit 2011 Frau Mag. Janosch Moehrle, Bakk. rer. nat., wenn sie abwesend oder krank ist (X-Straße).

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Janosch Moehrle, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Janosch Moehrle, Bakk. rer. nat.`(person)

**Example 55** (doc_id: `deanon_BFG_TRAIN/145692.1`) (sent_id: `deanon_BFG_TRAIN/145692.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Lee Ortpaul  in der Beschwerdesache von Frau  Fatima Herschelmann, BA, Haunolfstraße 38, 4131 Windhag, Österreich, über die Beschwerde vom 2. Februar 2023 gegen den Bescheid des  Finanzamtes Österreich vom 25.  Jänner 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu der Steuernummer 17-331/1560  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Fatima Herschelmann` — partial — pred is substring of gold: `Fatima Herschelmann, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Lee Ortpaul`(person)
- `Fatima Herschelmann, BA`(person)
- `Haunolfstraße 38, 4131 Windhag, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `17-331/1560`(tax_number)

**Example 56** (doc_id: `deanon_BFG_TRAIN/146327.1`) (sent_id: `deanon_BFG_TRAIN/146327.1_28`)


Die Kapitalertragssteuer wird Frau Dr.in Daria Stancke  direkt auf ihr Steuerkonto  vorgeschrieben.“

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr.in Daria Stancke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Daria Stancke`(person)

**Example 57** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_38`)


Darüber hinaus hat mein Sohn nach Einlangen der Aufforderung vom 12.07.2024 telefonisch die  Behörde (Frau Hermann) über meine Abwesenheit bis Ende 2024 informiert.

**False Positives:**

- `Hermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_341`)


Die 1924 geborene Mutter meiner Mandantschaft, Frau Anneliese M., lebte in Kempten und  musste betreut werden.

**False Positives:**

- `Anneliese` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 59** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_345`)


d) Wohnsitz M. (A) – Al.(I):  Bei dieser Fahrtstrecke werden 187 km in Österreich (M.- Arnoldstein) und 376 km in Italien  (Arnoldstein – Al.)  e) regelmäßige Fahrten am Wohnsitz M. (A):  Frau Bf. ist begeisterte Pferdesportlerin und hat die Pferde sowohl in Ai. (2014 u. 2015) als auch  in J. in Bayern (2014 - laufend) eingestellt. Anlässlich ihrer Aufenthalte in M. ist sie nahezu  täglich nach Ai. (einfache Strecke 24 km) gefahren.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)
- `M.`(person)
- `M.`(person)

**Example 60** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_347`)


f) Ferienwohnsitz Al. (I):  Bei ihren Ferienaufenthalten in Italien fuhr Frau Bf. gelegentlich zu Kulturveranstaltungen oder  Einkäufen nach Venedig (155 km) oder Mailand (160 km).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_348`)


Das KFZ von Frau Bf. wird ausschließlich privat genutzt, da sie keiner aktiven Erwerbstätigkeit  nachgeht.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_350`)


Da das Kraftfahrzeug von Frau Bf. ausschließlich privater Natur war, sind meiner Meinung  nach zum Nachweis des dauernden Standortes des Fahrzeuges nicht Judikatur zu  Kilometergeldern, Lohnsteuerrichtlinien und Literatur zu Werbekosten anzuwenden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_362`)


In ihrer zusammenfassenden Beurteilung  kommt die Bf. zu folgenden Ergebnissen:    In der Stellungnahme vom 4. Dezember 2023 (OZ. 53) hat sich die belangte Behörde zu diesen  Ausführungen wie folgt geäußert:  „Von 2002 bis 2018 hatte Frau Bf. den Hauptwohnsitz in Österreich.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_400`)


Weiters befänden sich im beigefügten Ordner jahrgangsweise geordnete Belege der  Bf.  Mit E-Mail vom 30. April 2024 (OZ. 64-68) führte der steuerliche Vertreter folgendes aus:  „ …  Wegen der teilweise schwierigen Lesbarkeit der Aufzeichnungen in den Terminkalendern von  Frau Bf. übermittle ich Ihnen in der Anlage monatlich gegliedert eine Übertragung der  handschriftlichen Aufzeichnungen in Schreibschrift.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_401`)


Ergänzend erlaube ich mir dazu auszuführen, dass jene Fahrten, die Frau Bf. gemeinsam mit  Ihrem Ehemann - das sind im Wesentlichen die Fahrten zu den Wohnsitzen nach Österreich und  Italien sowie an den Urlaubsort Lech am Arlberg - im Regelfall bei einer geplanten  gemeinsamen Hin- und Rückfahrt im Auto vom Hr. N.R. (Ehemann) durchgeführt wurden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_TRAIN/148571.1`) (sent_id: `deanon_BFG_TRAIN/148571.1_130`)


E Mail vom 14. Juli 2023   Von: aufnahmeverfahren <aufnahmeverfahren@wu.ac.at>   Betreff: Ergebnisse Aufnahmeverfahren | Bachelorstudium Wirtschaftsrecht an der WU Wien   Liebe Frau Kollegin!

**False Positives:**

- `Kollegin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_TRAIN/149407.1`) (sent_id: `deanon_BFG_TRAIN/149407.1_59`)


Nach dem Urteil von Frau Mag. R hätte Frau B gefragt, wie es ihren Hunden gehe.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_TRAIN/149407.1`) (sent_id: `deanon_BFG_TRAIN/149407.1_176`)


Wenn dies im Erkenntnis  von Frau Mag. R rechtlich anders beurteilt worden ist, so stellt dies keinen  Wiederaufnahmegrund dar.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Non-Academic Title Name Pattern`

**F1:** 0.022 | **Precision:** 0.639 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `371c3c3b`  
**Description:**
Captures names preceded by specific non-academic professional titles like 'VetR' (Veterinär) or 'Techn R' (Technischer Rat) which are not covered by the academic title rule.

**Content:**
```
\b((?:VetR|Techn\sR|RA\s|Dr\.\s|Mag\.\s|Hon\.-Prof\.in\s|Univ\.-Prof\.in\s|Priv\.-Doz\.\s|Dr\.in\s|Mag\.in\s|Mag\.a\s)\s+[A-Z][a-zäöüßÄÖÜ]+(?:\s+[A-Z][a-zäöüßÄÖÜ]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.639 | 0.011 | 0.022 | 36 | 23 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 13 | 1948 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129778.1`) (sent_id: `deanon_BFG_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache VetR Silvester Johäntges, Fischauer Gasse 37, 4616 Hetzendorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 25-402/5507  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `VetR Silvester Johäntges` | `VetR Silvester Johäntges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Fischauer Gasse 37, 4616 Hetzendorf, Österreich` (address)
- `25-402/5507` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/130444.1`) (sent_id: `deanon_BFG_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Lars Hoerl  in der Beschwerdesache VetR Christina Schlotfeldt,  Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Christina Schlotfeldt` | `VetR Christina Schlotfeldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Lars Hoerl` (person)
- `Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/131343.1`) (sent_id: `deanon_BFG_TRAIN/131343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Techn R Damian Weida, Maierniggalpe 210, 4712 Niederwödling, Österreich, über die Beschwerde vom 21. August 2018 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 2. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Techn R Damian Weida` | `Techn R Damian Weida` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maierniggalpe 210, 4712 Niederwödling, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der  Verwaltungsstrafsache gegen Techn R Gwendolin Omar, Schrötten 38, 3860 Aalfang, Österreich, über die Beschwerde des  Beschuldigten vom 9.11.2020 gegen die Vollstreckungsverfügungen des Magistrates der Stadt  Wien, Magistratsabteilung 6, vom 11. Jänner 2020, 1) MA67/196700867324/2019 und 2)  MA67/196700891928/2019 vom 14.1.2020, MA67/196700890302/2019 und vom 25.1.2020,   MA67/196700930712/2019, alle in Zusammenhang mit einer Verwaltungsübertretung gemäß  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, i.d.g.F., in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, i.d.g.F. zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und werden die angefochtenen  Vollstreckungsverfügungen ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Schrötten 38, 3860 Aalfang, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 6` (organisation)
- `Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_23`)


Auf Grund einer Anfrage des Bundesfinanzgerichtes bei der für Meldeangelegenheiten  zuständigen Fachdienststelle in der Stadt Wien, der MA 62, teilte diese mit E-Mail vom  25.2.2021 folgendes mit:  „Zu Ihrer Anfrage teile ich Ihnen seitens der Magistratsabteilung 62 als zuständiger  Fachdienststelle für Meldeangelegenheiten in der Stadt Wien mit, dass Herr Techn R Gwendolin Omar  wie  von ihm angegeben von uns nach Durchführung eines Verfahrens nach § 15 Meldegesetz  amtlich von der Adresse xy abgemeldet wurde.

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_26`)


Der Erheber bekam vor Ort am  14. Jänner 2020 von einer Hauspartei, deren Identität wir nicht kennen, die Auskunft, dass Herr  Techn R Gwendolin Omar  unbekannt wohin verzogen sei.

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_27`)


Herr Techn R Gwendolin Omar  wurde von uns zweimal im  Verfahren angeschrieben, davon einmal mit RSb-Rückscheinbrief, und hat darauf nicht  reagiert.“

| Predicted | Gold |
|---|---|
| `Techn R Gwendolin Omar` | `Techn R Gwendolin Omar` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/135036.1`) (sent_id: `deanon_BFG_TRAIN/135036.1_3`)


über die Beschwerde des Techn R Volker Eschermann,  Deuschlergasse 5, 5600 Floitensberg, Österreich, vom 23. Oktober 2021 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 23. September 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Techn R Volker Eschermann` | `Techn R Volker Eschermann` |

**Missed by this rule (FN):**

- `Deuschlergasse 5, 5600 Floitensberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/136171.1`) (sent_id: `deanon_BFG_TRAIN/136171.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache VetR Susette Käse, Alte Tauernstraße 16, 4161 Lichtenberg, Österreich, über die Beschwerde vom 1. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 28. März 2017 betreffend Rückforderung von  Ausgleichszahlung gemäß der Verordnung (EG) 883/2004 (Familienbeihilfe) für den Zeitraum  April 2016 bis Oktober 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Susette Käse` | `VetR Susette Käse` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Alte Tauernstraße 16, 4161 Lichtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 10** (doc_id: `deanon_BFG_TRAIN/139715.1`) (sent_id: `deanon_BFG_TRAIN/139715.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Elfriede Murtinger über die Beschwerde  des Techn R Emil Stueven, Rutzendorfer Straße 20, 5242 Frauschereck, Österreich, vom 13. Dezember 2022 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. November 2022, GZ.  MA67/Zahl/2022, wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Techn R Emil Stueven` | `Techn R Emil Stueven` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elfriede Murtinger` (person)
- `Rutzendorfer Straße 20, 5242 Frauschereck, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_TRAIN/143278.1`) (sent_id: `deanon_BFG_TRAIN/143278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Leila Hussack, Bakk. iur. MA, Krumauerstraße 21, 4223 Katsdorf, Österreich, vertreten durch HAUNSCHMIDT & PARTNER  Steuerberatungs GmbH, Julius Tandler Pl 6 Tür 9, 1090 Wien, über die Beschwerde vom  26. März 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom  9. März 2020 betreffend Stundungszinsen 2020 nach der am 4.12.2023 am  Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO i.V.m. § 274 Abs. 1 Z 1 BAO) in  Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und in Anwesenheit von Mag.  Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte Behörde durchgeführten  mündlichen Verhandlung zur Steuernummer 77-604/4717  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.  Martin Holzapfel` | `Mag.  Martin Holzapfel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Leila Hussack, Bakk. iur. MA` (person)
- `Krumauerstraße 21, 4223 Katsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Mag. Sebastian Rivo-Wastl, BA` (person)
- `77-604/4717` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/143446.1`) (sent_id: `deanon_BFG_TRAIN/143446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Barbara Straka, die Richterin  Mag. Irene Kohler sowie die fachkundigen Laienrichter Dip.Ing. Gerald Patschka und Mag.  Michael Heumesser in der Beschwerdesache Dr. Herbert Schießwohl, Wopenkastraße 17, 4802 Ebensee, Österreich, vertreten durch  Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38,  1020 Wien, über die Beschwerde vom 22. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 23. Februar 2023 betreffend Einkommensteuer 2013, Steuernummer  50-732/9932, in der Sitzung am 17. Jänner 2024, erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.  Michael Heumesser` | `Mag.  Michael Heumesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Barbara Straka` (person)
- `Mag. Irene Kohler` (person)
- `Dip.Ing. Gerald Patschka` (person)
- `Dr. Herbert Schießwohl` (person)
- `Wopenkastraße 17, 4802 Ebensee, Österreich` (address)
- `Hallas & Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `50-732/9932` (tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/144349.1`) (sent_id: `deanon_BFG_TRAIN/144349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  VetR Marlies Thalmayr, Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom 6. Februar  2024 gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2024 betreffend  Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 01.12.2022 bis  30.06.2023, Steuernummer 88-272/3661, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Marlies Thalmayr` | `VetR Marlies Thalmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `88-272/3661` (tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Andrea Ebner in der Rechtssache  Techn R Francois Bartoszek, Porr Headquaters 139, 8403 Göttling, Österreich, betreffend den Antrag nach § 299 BAO vom 11. Juli 2024 auf  Aufhebung des Beschlusses des Bundesfinanzgerichtes vom 3. Juli 2024, RV/7101936/2024,  Steuernummer 94-241/1081, den Beschluss:  I. Der Antrag nach § 299 BAO vom 11. Juli 2024 auf Aufhebung des Beschlusses des  Bundesfinanzgerichtes vom 3. Juli 2024, RV/7101936/2024 wird als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Porr Headquaters 139, 8403 Göttling, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)
- `94-241/1081` (tax_number)
- `Bundesfinanzgerichtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_3`)


Begründung  Techn R Francois Bartoszek  brachte bei der belangten Behörde am 22. November 2023 unter anderem eine  Vorlageerinnerung betreffend den Bescheid des Finanzamtes Österreich vom 21. September  2021 ein.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Finanzamtes Österreich` (organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_6`)


Der vorgenannte Beschluss (Mängelbehebungsauftrag) wurde am 18. Juni 2024 zugestellt.  Mit E-Mail vom 19. Juni 2024 kündigte Techn R Francois Bartoszek  an, „die Vorlageerinnerung vom 221123 betr  Gebührenbescheide vom 210921 wird zurückgezogen“.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Example 17** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_9`)


Da Techn R Francois Bartoszek  dem Auftrag zur Mängelbehebung unstrittig beim Bundesfinanzgericht innerhalb  der gesetzten Frist nicht nachgekommen ist, galt die Vorlageerinnerung mit Ablauf der  gesetzten Frist als zurückgenommen (siehe betreffenden Beschluss des BFG vom 3. Juli 2024,  RV/7101936/2024).

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)

**Example 18** (doc_id: `deanon_BFG_TRAIN/145401.1`) (sent_id: `deanon_BFG_TRAIN/145401.1_35`)


Der Antrag des Herrn Techn R Francois Bartoszek  vom 11. Juli 2024 auf Aufhebung des Beschusses des  Bundesfinanzgerichtes vom 13. Juni 2024, RV/7101936/2024 wird daher als unzulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Techn R Francois Bartoszek` | `Techn R Francois Bartoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_TRAIN/147360.1`) (sent_id: `deanon_BFG_TRAIN/147360.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Namli  in der Beschwerdesache VetR Georg Versteegen,  Kirchenlucken 549, 4845 Mairhof, Österreich, über die Beschwerde vom 6. April 2018 gegen den Bescheid des FA Steiermark Mitte  (nunmehr Finanzamt Österreich) vom 23. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Steuernummer 33-748/3939  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Georg Versteegen` | `VetR Georg Versteegen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Namli` (person)
- `Kirchenlucken 549, 4845 Mairhof, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `Finanzamt Österreich` (organisation)
- `33-748/3939` (tax_number)

**Example 20** (doc_id: `deanon_BFG_TRAIN/147401.1`) (sent_id: `deanon_BFG_TRAIN/147401.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicole Landt  in der Beschwerdesache Techn R Benjamin Liebetanz,  Sandbühel 31, 4784 Bach, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 29. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt  Österreich/FAÖ) vom 1. August 2016, Erf. Nr. 111x, betreffend  1. Festsetzung der Gebühren gemäß § 14 TP 2 Abs.1 Z 1, TP 5 Abs. 1, TP 6 Abs. 2       und TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO zur Gänze als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Techn R Benjamin Liebetanz` | `Techn R Benjamin Liebetanz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Nicole Landt` (person)
- `Sandbühel 31, 4784 Bach, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/147401.1`) (sent_id: `deanon_BFG_TRAIN/147401.1_4`)


Die Bezirkshauptmannschaft A-Ort1 hat am 11.4.2016 acht amtliche Befunde (zu   GZ. XY1-8) über die "Verkürzung von Stempel- oder Rechtsgebühren" hinsichtlich der  "Meldung des Ausflugsverkehrs gemäß Tiroler Schischulgesetz 1995" je v. 4.1.2016 für acht  Schilehrer (AA, BB, CC, DD, EE, FF, GG, HH) durch die Techn R Benjamin Liebetanz (= Beschwerdeführerin, Bf),  eine deutsche Schischule, erstellt und an das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel, nunmehr Finanzamt Österreich, übermittelt.   Gegenstand der Gebühr waren den Befunden zufolge jeweils die Meldung des  Ausflugsverkehrs gemäß Tiroler Schischulgesetz samt Beilagen und Kopien der  Lichtbildausweise der gemeldeten Lehrer sowie die schriftliche Erledigung durch die  Bezirkshauptmannschaft.

| Predicted | Gold |
|---|---|
| `Techn R Benjamin Liebetanz` | `Techn R Benjamin Liebetanz` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)

**Example 22** (doc_id: `deanon_BFG_TRAIN/148329.1`) (sent_id: `deanon_BFG_TRAIN/148329.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Barbara Eismont  in der Beschwerdesache Techn R Joseph Balnuweit,  Hauzendorf 7, 4180 Zwettl an der Rodl, Österreich, vertreten durch Raiffeisenverband Steiermark, Raiffeisen-Platz 11, 8074  Raaba-Grambach, über die Beschwerde vom 15. November 2018 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. Oktober 2018 betreffend Berichtigung §§ 293 ff BAO 2012,  Steuernummer 48-226/2592  zu Recht erkannt:    I. Der angefochtene Bescheid wird gem. dem VwGH-Erkenntnis Ra 2023/15/0112-8  abgeändert.

| Predicted | Gold |
|---|---|
| `Techn R Joseph Balnuweit` | `Techn R Joseph Balnuweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Barbara Eismont` (person)
- `Hauzendorf 7, 4180 Zwettl an der Rodl, Österreich` (address)
- `Raiffeisenverband Steiermark` (organisation)
- `48-226/2592` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Beate Melik  in der Beschwerdesache Techn R Dr.in Maria Repstock,  Silberrain 14a, 5542 Flachau, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Dr` — partial — pred is substring of gold: `Techn R Dr.in Maria Repstock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Beate Melik`(person)
- `Techn R Dr.in Maria Repstock`(person)
- `Silberrain 14a, 5542 Flachau, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/134371.1`) (sent_id: `deanon_BFG_TRAIN/134371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Techn R Lee Ditscheidt, Bakk. art. Bakk. art., Heitzmannweg 11, 4661 Mitterbuch, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31.März 2014 gegen die Bescheide des Finanzamtes für Großbetriebe je vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2008 bis  2012 (Steuernummer 38-978/7129 ) nach Durchführung einer mündlichen Verhandlung am  04.08.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn R Lee Ditscheidt` — partial — pred is substring of gold: `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`(person)
- `Heitzmannweg 11, 4661 Mitterbuch, Österreich`(address)
- `Finanzamtes für Großbetriebe`(organisation)
- `38-978/7129`(tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/134371.1`) (sent_id: `deanon_BFG_TRAIN/134371.1_240`)


Die Gesellschafter  der OG wurden bereichert und bei der Techn R Lee Ditscheidt, Bakk. art. Bakk. art.  ist der Aufwand verdeckte  Gewinnausschüttung.“

**False Positives:**

- `Techn R Lee Ditscheidt` — partial — pred is substring of gold: `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Lee Ditscheidt, Bakk. art. Bakk. art.`(person)

**Example 3** (doc_id: `deanon_BFG_TRAIN/136523.1`) (sent_id: `deanon_BFG_TRAIN/136523.1_49`)


Durch den anwaltlichen Vertreter der Beschwerdeführerin RA  Dr. Fabian Maschke wurde weiters in Zusammenhang mit dem Beschwerdevorbringen der  unionsrechtlich gebotenen umsatzsteuerlichen Gleichbehandlung von konzessionierten und  nicht konzessionierten Spielbanken die Einholung eines Gutachtens eines gerichtlich beeideten  und zertifizierten Sachverständigen aus dem Fachbereich Glücks- und Geschicklichkeitsspiele  beantragt („zum Beweis dafür, dass der hier gegenständlich relevante Sachverhalt bzw die  Handlungen der Beschwerdeführerin nicht umsatzsteuerpflichtig sind“).

**False Positives:**

- `RA  Dr` — partial — pred is substring of gold: `RA  Dr. Fabian Maschke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA  Dr. Fabian Maschke`(organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/136984.1`) (sent_id: `deanon_BFG_TRAIN/136984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache VetR Cedric Özturan, Scholzstraße 25, 8113 Södingberg, Österreich, über die Beschwerde der Beschwerdeführerin (Bf.) vom 12. August 2021 gegen den  Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2020 des Finanzamtes Österreich vom  9. August 2021 zu Steuernummer 40-154/0143  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

**False Positives:**

- `VetR Cedric` — partial — pred is substring of gold: `VetR Cedric Özturan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Cedric Özturan`(person)
- `Scholzstraße 25, 8113 Södingberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `40-154/0143`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/137224.1`) (sent_id: `deanon_BFG_TRAIN/137224.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Techn R Prof. Ronald Carnegie, Anton-Schrammel-Hof 18, 3341 Schwarzois, Österreich, über die Beschwerde vom 18.01.2021 gegen den Bescheid des  Finanzamtes Österreich vom 15. Jänner 2021, betreffend Einkommensteuer 2019, zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn R Prof` — partial — pred is substring of gold: `Techn R Prof. Ronald Carnegie`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Techn R Prof. Ronald Carnegie`(person)
- `Anton-Schrammel-Hof 18, 3341 Schwarzois, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/137796.1`) (sent_id: `deanon_BFG_TRAIN/137796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Lee Kolesnichenko, Hannovermarkt 59, 4801 Eben, Österreich, vertreten durch Ing. Thomas Millesich, Dr.  Wlasakstraße 83, 2410 Hainburg, über die Beschwerde vom 25. März 2022 gegen den Bescheid  des Finanzamtes Österreich vom 23. Februar 2022 betreffend Festsetzung einer Zwangsstrafe,  Steuernummer 25-414/2087, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.  Wlasakstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Lee Kolesnichenko`(person)
- `Hannovermarkt 59, 4801 Eben, Österreich`(address)
- `Ing. Thomas Millesich`(person)
- `Finanzamtes Österreich`(organisation)
- `25-414/2087`(tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138549.1`) (sent_id: `deanon_BFG_TRAIN/138549.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  HR Techn R Wolfgang Strauscheidt, Sixenstraße 86, 4892 Fornach, Österreich, über die Beschwerde vom gegen den Bescheid des Finanzamtes  Österreich vom 29. Oktober 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2020 Steuernummer 90-061/3966  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Wolfgang Strauscheidt` — partial — pred is substring of gold: `HR Techn R Wolfgang Strauscheidt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `HR Techn R Wolfgang Strauscheidt`(person)
- `Sixenstraße 86, 4892 Fornach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `90-061/3966`(tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/140957.1`) (sent_id: `deanon_BFG_TRAIN/140957.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Adriana van den Heuvel  in der Beschwerdesache VetR Prof.in Fiona Helmholz,  Pfarrsteig 7h, 8312 Breitenbach, Österreich, vertreten durch Grant Thornton Austria GmbH Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Handelskai 92/Gate 2/Top 7A, 1200 Wien, betreffend  Beschwerde vom 01.08.2008 gegen die Bescheide über die Wiederaufnahme des Verfahrens  hinsichtlich der Umsatzsteuer der Jahre 2000 bis 2003 und gegen die Umsatzsteuerbescheide  der Jahre 2000 bis 2005, jeweils vom 30.06.2008 sowie betreffend die Beschwerde vom  08.08.2008 gegen die Haftungs- und Abgabenbescheide hinsichtlich Kapitalertragsteuer der  Jahre 2000 bis 2004, jeweils vom 13.06.2008 zu Steuernummer 24-683/2597  beschlossen:   I. Das Beschwerdeverfahren wird eingestellt.   II. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `VetR Prof` — partial — pred is substring of gold: `VetR Prof.in Fiona Helmholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Adriana van den Heuvel`(person)
- `VetR Prof.in Fiona Helmholz`(person)
- `Pfarrsteig 7h, 8312 Breitenbach, Österreich`(address)
- `Grant Thornton Austria GmbH`(organisation)
- `24-683/2597`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/140957.1`) (sent_id: `deanon_BFG_TRAIN/140957.1_23`)


Über die Beschwerdeführerin, VetR Prof.in Fiona Helmholz, wurde mit Beschluss des Handelsgerichtes Wien AZ  das Konkursverfahren eröffnet.

**False Positives:**

- `VetR Prof` — partial — pred is substring of gold: `VetR Prof.in Fiona Helmholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Prof.in Fiona Helmholz`(person)

**Example 10** (doc_id: `deanon_BFG_TRAIN/141448.1`) (sent_id: `deanon_BFG_TRAIN/141448.1_8`)


die Bestellung der RA      MagB zur (neuen) Erwachsenenvertreterin der Bf, für diese folgende     Angelegenheiten zu besorgen: Vertretung vor Gerichten, Behörden etc; Vermögens-     und Einkünfteverwaltung;

**False Positives:**

- `RA      Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/143865.1`) (sent_id: `deanon_BFG_TRAIN/143865.1_73`)


Möglicherweise seien sie aber "vor" Erteilung eines Auftrags durch Herrn Dr.  Theophil German  einfach nicht für diese Angelegenheit zuständig.

**False Positives:**

- `Dr.  Theophil German` — partial — gold is substring of pred: `Theophil German`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theophil German`(person)

**Example 12** (doc_id: `deanon_BFG_TRAIN/148201.1`) (sent_id: `deanon_BFG_TRAIN/148201.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Techn R Dr. Diego Wachsmann, Spetterbrücke 14, 9462 Schönberg, Österreich, über die Beschwerde vom 26. November 2024  gegen den Bescheid des Finanzamtes Österreich vom 19. November 2024 betreffend  Einkommensteuer 2023 Steuernummer 66-050/1184  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Dr` — partial — pred is substring of gold: `Techn R Dr. Diego Wachsmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Techn R Dr. Diego Wachsmann`(person)
- `Spetterbrücke 14, 9462 Schönberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `66-050/1184`(tax_number)

</details>

---

## `Long Academic Title Name`

**F1:** 0.021 | **Precision:** 1.000 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `09f93e48`  
**Description:**
Captures specific long academic titles and names that are often standalone or preceded by prepositions, generalizing the pattern to include suffixes.

**Content:**
```
\b(?:Valentina Kulbarsch, Bakk\. rer\. nat\.|Ing\. StR Dipl\. Kff\. Sonja Bonholt|Hon\.-Prof\.in Delila Luether|Dr\. Jonathan M\u00fctterthies|Ma(?:g\.a (?:Natalie Schreckhas|Katharina Fisera)|ja Schlagbaum)|Karina Tkachenko, BA|Dalibor Czeschelski|StR Marion Dallmeir|Dr\. Anna Radschek|Dr\. Peter Steurer|Roxana Bendhaack|Fiona Clesen|Dr\. B\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.010 | 0.021 | 21 | 21 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 21 | 0 | 1922 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129460.1`) (sent_id: `deanon_BFG_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Anton Danelzik, Alois Sindl-Stra 114m, 4920 Piereth, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  12-224/1788  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Danelzik` (person)
- `Alois Sindl-Stra 114m, 4920 Piereth, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `12-224/1788` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/132478.1`) (sent_id: `deanon_BFG_TRAIN/132478.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Juri Weich, Spitalanger 19, 3910 Ratschenhof, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 9. März 2015 betreffend Einkommensteuervorauszahlungen 2015 zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Weich` (person)
- `Spitalanger 19, 3910 Ratschenhof, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ernestine Schittenhelm, Clementinengasse 29, 8692 Krampen, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ernestine Schittenhelm` (person)
- `Clementinengasse 29, 8692 Krampen, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 3** (doc_id: `deanon_BFG_TRAIN/132878.1`) (sent_id: `deanon_BFG_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Sabrina Boger, Heugraben 15, 6233 Mariatal, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sabrina Boger` (person)
- `Heugraben 15, 6233 Mariatal, Österreich` (address)
- `Finanzamt  Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/133301.1`) (sent_id: `deanon_BFG_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Francois Stürnkorb, Lobisser Straße 37, 4153 Schönberg, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Stürnkorb` (person)
- `Lobisser Straße 37, 4153 Schönberg, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/136317.1`) (sent_id: `deanon_BFG_TRAIN/136317.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Gerlinde Schönheinz, Leinburger Straße 42B, 5113 Aglassing, Österreich, betreffend die Beschwerden vom 30. August 2019, 30. September  2019 und 31. September 2019 gegen die Bescheide des damaligen Finanzamtes 3/6/7/11/15  Schwechat Gerasdorf vom 25. Juli 2019 zu Steuernummer 63-118/1188  betreffend  Einkommensteuer 2012, sowie Umsatz-und Einkommensteuer 2014 bis 2017 beschlossen:  Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerlinde Schönheinz` (person)
- `Leinburger Straße 42B, 5113 Aglassing, Österreich` (address)
- `63-118/1188` (tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/137567.1`) (sent_id: `deanon_BFG_TRAIN/137567.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Cassandra Franzas, Ketzerhub 14, 4730 Auwies, Österreich, vertreten durch Rudolf Peter, Esteplatz 3 Tür 9, 1030 Wien,  betreffend Beschwerde vom 20. Mai 2016 gegen die Bescheide des damaligen Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 21. April 2016 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) für 2009, 2010, 2012 und 2013, sowie den Bescheid vom 2.  Oktober 2019 betreffend Umsatzsteuer 2015, Steuernummer 57-376/4892, beschlossen:  I. a)

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cassandra Franzas` (person)
- `Ketzerhub 14, 4730 Auwies, Österreich` (address)
- `Rudolf Peter` (person)
- `57-376/4892` (tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138051.1`) (sent_id: `deanon_BFG_TRAIN/138051.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  OStR Lukas Janowitsch, Waizbauerweg 68, 9620 Presseggen, Österreich, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich über die Erklärung zur Arbeitnehmerveranlagung 2021, beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Lukas Janowitsch` (person)
- `Waizbauerweg 68, 9620 Presseggen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/138967.1`) (sent_id: `deanon_BFG_TRAIN/138967.1_137`)


Daran können  auch die Bestätigungen der Erlöse der drei Hauptkunden in Deutschland nichts ändern, zum  einen, da dadurch nicht ausgeschlossen wird, dass auch an andere Kunden Umsätze getätigt  wurden (worauf auch die mit „verschiedene Kunden" und „Dr. B." benannten Konten schließen  lassen), zum anderen war eine exakte Zuordnung der Rechnungsnummern bzw. Rechnungen  nicht möglich.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/141691.1`) (sent_id: `deanon_BFG_TRAIN/141691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Verwaltungsstraf- sache gegen Cornelia Große-Beck, Dobretshofen 10, 4760 Großprambach, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde der Beschuldigten vom 3. Juli 2023 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 13. Juni 2023, GZ. MA67/Zahl/2022, zu Recht  erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Große-Beck` (person)
- `Dobretshofen 10, 4760 Großprambach, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_TRAIN/142516.1`) (sent_id: `deanon_BFG_TRAIN/142516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der  Verwaltungsstrafsache gegen Priv.-Doz. Karlheinz Barnekow, Seltschacher Straße 9I, 9585 Techanting, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 18. August 2023 gegen  das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Juli 2023, GZ.  MA67/236700356855/2023, zu Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde insofern Folge gegeben als gemäß § 38 VwGVG iVm  § 45 Abs. 1 Z. 4 VStG von der Verhängung einer Strafe abgesehen und der  beschwerdeführenden Partei unter Hinweis auf die Rechtswidrigkeit ihres Verhaltens eine  Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Karlheinz Barnekow` (person)
- `Seltschacher Straße 9I, 9585 Techanting, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_TRAIN/143056.1`) (sent_id: `deanon_BFG_TRAIN/143056.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Melinda Ade, Nachdemsee 10, 9322 Micheldorf, Österreich  vertreten durch die Hon.-Prof.in Erika Opdenhövel  Steuerberatung Werkval-Medien GMBH, über die  Beschwerde gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt Österreich)  vom 25. November 2019 betreffend Einkommensteuer 2018, 54-549/3530, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melinda Ade` (person)
- `Nachdemsee 10, 9322 Micheldorf, Österreich` (address)
- `Hon.-Prof.in Erika Opdenhövel` (person)
- `Werkval-Medien GMBH` (organisation)
- `Finanzamt Österreich` (organisation)
- `54-549/3530` (tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/144349.1`) (sent_id: `deanon_BFG_TRAIN/144349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  VetR Marlies Thalmayr, Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich  vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom 6. Februar  2024 gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2024 betreffend  Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 01.12.2022 bis  30.06.2023, Steuernummer 88-272/3661, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Marlies Thalmayr` (person)
- `Josef-Seilern-Straße 6, 4550 Rohr im Kremstal, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `88-272/3661` (tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/144505.1`) (sent_id: `deanon_BFG_TRAIN/144505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Gabriele Hattendorff, Trautenfels 55, 4224 Altenhaus, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum 01.12.2022  bis 30.06.2023, Steuernummer 59-032/8627, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gabriele Hattendorff` (person)
- `Trautenfels 55, 4224 Altenhaus, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `59-032/8627` (tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/144827.1`) (sent_id: `deanon_BFG_TRAIN/144827.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rainer Weinschenk, Streitmayerweg 33C, 8263 Radersdorf, Österreich, vertreten durch Meissner & Passin Rechtsanwalts GmbH,  Himmelpfortgasse 17/14, 1010 Wien, betreffend Beschwerde vom 15. Juni 2022 gegen den  Bescheid des Magistratsabteilung 6, Referat Landes- und Gemeindeabgaben, vom 4. März 2022  betreffend Wettterminalabgabe für Mai bis Dezember 2017, GZ MA 6/ARL – 551965/2018-14,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rainer Weinschenk` (person)
- `Streitmayerweg 33C, 8263 Radersdorf, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/145612.1`) (sent_id: `deanon_BFG_TRAIN/145612.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pagitsch, der  Richterin Dr. Anna Radschek sowie die fachkundigen Laienrichter KR Ing. Hans Eisenkölbl und  Mag. Michael Heumesser in der Beschwerdesache Laura Kaplaner, Zehetmayrgut 160, 4710 Niederweng, Österreich, vertreten durch  APP Steuerberatung GmbH, Schenkenstraße 4 / 6.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KR Ing. Hans Eisenkölbl` (person)
- `Mag. Michael Heumesser` (person)
- `Laura Kaplaner` (person)
- `Zehetmayrgut 160, 4710 Niederweng, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)

**Example 16** (doc_id: `deanon_BFG_TRAIN/145630.1`) (sent_id: `deanon_BFG_TRAIN/145630.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde der   Lisa Firneisz, Färbereigasse 23, 6682 Vils, Österreich, vom 23. Juli 2024, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 15. Juli 2024, GZ. MA67/GZ/2024, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt  der Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  Landesgesetzblatt für Wien Nr. 9/2006 in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als gemäß § 45 Abs. 1  VStG von der Verhängung einer Strafe abgesehen und der Beschwerdeführerin unter Hinweis  auf die Rechtswidrigkeit ihres Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lisa Firneisz` (person)
- `Färbereigasse 23, 6682 Vils, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/146687.1`) (sent_id: `deanon_BFG_TRAIN/146687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Amy Bayrakcioglu, Bakk. phil., Badnerstraße 75, 9423 Hofwiesen, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Österreich  vom 11. November 2021 betreffend Einkommensteuer 2019, 35-160/3790, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amy Bayrakcioglu, Bakk. phil.` (person)
- `Badnerstraße 75, 9423 Hofwiesen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `35-160/3790` (tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_526`)


Ebenso konnte aus dem Belegmaterial (OZ. 77) entnommen werden, dass die Bf. zahlreiche  Facharztbesuche, Physiotherapeuten, Heilpraktiker, ärztliche Labors (Re v. 22.8.2014,  1.10.2014 Dr. M., 30.10.2014 Dr. Sch., 30.10.2014 Dr. Sz., 16.1.2015 Dr. E., 26.1.2015 Dr. W.,  4.3.2015 Diagnostik M., 28.8.2015 Heilpraktikerin H., 14.12.2015 Heilpraktikerin H., 17.12.2015  Labor Dres., 30.12.2015 Heilpraktikerin H., 29.11.2016 Dr. E., 10.2.2017 Zahnarzt 4 Sitzungen,  21.3.2017 Facharzt 4 Sitzungen, 11.8.2017 Zahnarzt, 12.10.2017 Dr. E., 27.12.2017 Dr. B. 2  Sitzungen, absolviert hat.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Missed by this rule (FN):**

- `M.` (person)
- `M.` (person)

**Example 19** (doc_id: `deanon_BFG_TRAIN/148214.1`) (sent_id: `deanon_BFG_TRAIN/148214.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Renate Kukulys, Parisdorfer Straße 53, 8490 Pfarrsdorf, Österreich, über die Beschwerde vom 9. August 2023 gegen den Bescheid des  Finanzamtes Österreich vom 19. Juli 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 73-183/8909, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Renate Kukulys` (person)
- `Parisdorfer Straße 53, 8490 Pfarrsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `73-183/8909` (tax_number)

**Example 20** (doc_id: `deanon_BFG_TRAIN/149749.1`) (sent_id: `deanon_BFG_TRAIN/149749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Heidemarie Zangel, Furtmüllerstraße 66, 5142 Hehenberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Österreich  betreffend Einkommensteuer 2019 und 2020, 08-156/6554, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heidemarie Zangel` (person)
- `Furtmüllerstraße 66, 5142 Hehenberg, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `08-156/6554` (tax_number)

</details>

---

## `Anonymized Doctor Pattern`

**F1:** 0.005 | **Precision:** 0.100 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `da791678`  
**Description:**
Captures anonymized doctor names like 'Dr. B.' or 'Dr. A.' which are common in legal texts but missed by standard name patterns.

**Content:**
```
\bDr\.\s+[A-Z]\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.100 | 0.002 | 0.005 | 50 | 5 | 45 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 45 | 2005 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129907.1`) (sent_id: `deanon_BFG_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. R. in der Beschwerdesache Zarin Enneken,  Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 90-142/3945  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zarin Enneken` (person)
- `Bruno-Gallee-Weg 5Q, 9990 Debant, Österreich` (address)
- `90-142/3945` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_61`)


II. Das Bundesfinanzgericht hat erwogen:  Mit Rechnung vom 31. August 2018 stellte Dr. R. Beratung & Coaching der Bf. für die  Teilnahme am Diplomlehrgang zum Relationalen Coach 2018/2019 € 9.900,00 in Rechnung.

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_63`)


Am 03. September 2018 überwies die Bf. von ihrem Konto € 6.000,00 auf das in der o.a.  Rechnung angegebene Konto Dr. R. (Bankbeleg).

| Predicted | Gold |
|---|---|
| `Dr. R.` | `Dr. R.` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/138967.1`) (sent_id: `deanon_BFG_TRAIN/138967.1_137`)


Daran können  auch die Bestätigungen der Erlöse der drei Hauptkunden in Deutschland nichts ändern, zum  einen, da dadurch nicht ausgeschlossen wird, dass auch an andere Kunden Umsätze getätigt  wurden (worauf auch die mit „verschiedene Kunden" und „Dr. B." benannten Konten schließen  lassen), zum anderen war eine exakte Zuordnung der Rechnungsnummern bzw. Rechnungen  nicht möglich.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_526`)


Ebenso konnte aus dem Belegmaterial (OZ. 77) entnommen werden, dass die Bf. zahlreiche  Facharztbesuche, Physiotherapeuten, Heilpraktiker, ärztliche Labors (Re v. 22.8.2014,  1.10.2014 Dr. M., 30.10.2014 Dr. Sch., 30.10.2014 Dr. Sz., 16.1.2015 Dr. E., 26.1.2015 Dr. W.,  4.3.2015 Diagnostik M., 28.8.2015 Heilpraktikerin H., 14.12.2015 Heilpraktikerin H., 17.12.2015  Labor Dres., 30.12.2015 Heilpraktikerin H., 29.11.2016 Dr. E., 10.2.2017 Zahnarzt 4 Sitzungen,  21.3.2017 Facharzt 4 Sitzungen, 11.8.2017 Zahnarzt, 12.10.2017 Dr. E., 27.12.2017 Dr. B. 2  Sitzungen, absolviert hat.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Missed by this rule (FN):**

- `M.` (person)
- `M.` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_65`)


Beweis: als Zeugen Dr. P. - H. - M. - F. N.. Habe dann um 10:12 h den Verhandlungssaal verlassen und danach den Schuldnervertreter Mag. S. T. Y., danach habe ich den Masseverwalter und zuletzt den Steuerberater angerufen und von dem Vorfall beim Spruchsenat berichtet.

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_349`)


Mit der Vertragserrichtung beauftragt wurde Rechtsanwalt Dr. J. Dieser gilt als  Parteienvertreter iSd § 30c Abs. 3 EStG 1988, welcher unter den genannten Voraussetzungen  für die richtige Berechnung der strittigen Steuer haftet.

**False Positives:**

- `Dr. J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_20`)


Als Beilagen zu der Beschwerde wurden (Beil.1:) die Bestätigung der SRBV GmbH betreffend  verrechnete Leistungen im Jahr 2018 vom 23.01.2019, (Beil.2:) die Krankengeschichte samt  Stellungnahme der Bf. vom 13.09.2019, (Beil. 2/a:) der OP-Bericht des OA Dr. A., Herz Jesu-KH  vom 6.12.2001 (Operation an der Wirbelsäule), (Beil.2/b:) der Arztbrief des Prim. Univ.-Prof.  DDr. B., Unfallabteilung Landesklinikum Baden-Mödling vom 06.05.2013   (OP: Oberschenkelknochen- Bruch), (Beil.2/c:) die Niederschrift des Prim. Univ.- Prof. Dr. C.,  Evangelisches Krankenhaus vom 9.04.2014 zur Operation am Darm vom 8.04.2014,   AZ: 2014/XXXX, (Beil.2/d:) der Befundbericht Therapievorschlag des Dr. Med. Univ.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation
- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `SRBV GmbH`(organisation)
- `Prim. Univ.-Prof.  DDr. B.`(person)

**Example 3** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_24`)


Der Bericht des OA Dr. A., Herz Jesu-KH vom 6.12.2001 über die Operation der Bf. an der  Wirbelsäule vom Vortag (Beilage 2/a) lautet wie folgt:  „

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_39`)


Dem Ergänzungsersuchen entsprechend wurden dem Finanzamt die Bestätigung der Ärztin Dr.  E. vom 16.12.2019 mit Angaben der Diagnosen „kombiniertes Aortenklappenvitium“, „Axonale  PNP“ und „Zn DP 14 L5 mit Massenprolaps 2001“ als Beweis für die Bf. als eine  pflegebedürftige Patientin, der Residenzvertrag, Broschüren über „Pflegeaufenthalt“ und  „Dauerwohnen“, der Beleg über die von der SRBV mit der Bf. verrechneten Leistungen für das  Streitjahr sowie die Tarifliste betreffend die NÖ Pflege- und Betreuungszentren, NÖ Pflege- und  Förderzentren für das Jahr 2019, zur Entscheidung über die Beschwerde vorgelegt.

**False Positives:**

- `Dr.  E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_54`)


Laut der vorgelegten Arztbestätigung der Dr. E. vom 16.12.2019 sei die Bf. aufgrund der in dem  Schreiben genannten Diagnosen und ihrem Alter von 90 Jahren zwar pflegebedürftig, jedoch  liege ein detailliertes Gutachten trotz Aufforderung nicht vor.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_62`)


VwGH 30.06.2010, 2008/13/0145, VwGH 26.05.2010, 2007/13/0051, und die im  Schreiben von Dr. E. vom 16.12.2019 angeführten Leiden der Bf. wurde zum  "kombinierten Aortenklappenvitium" unter Verweis auf den Artikel von Franziska  Mettke, Ärztin, Dresden auf https: // befunddolmetscher.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_90`)


Angesichts der im  Schreiben von Dr. E. vom 16.12.2019 angesprochenen Diagnose "Zn DP 14 L5 mit  Massenprolaps 2001" erging das an die Bf. adressierte Ersuchen um Vorlage einer  Beschreibung der letztgenannten Krankheit, wobei diesen Ausführungen in Hinblick auf  die Unbekanntheit der Art und der Folgen dieser Erkrankung sämtliche der der Bf. zur  Verfügung stehenden Beweismittel (z.B. Befunde, Krankenhausergebnisse,  Testergebnisse, etc.) beizulegen wären.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_105`)


Mit Schreiben des BFG vom 26.02.2021 wurden das Schreiben der steuerlichen Vertreterin  vom 20.02.2021, der Befundbericht von Dr. E. vom 30.07.2020 (Kopie), der Röntgen-Befund  vom 25.04.2017, das VwGH-Erkenntnis vom 30.06.2010, 2008/13/0145 (Serie (erledigt im  gleichen Sinn): VwGH 30.06.2010, 2008/13/0126) und die UFS-Berufungsentscheidung vom  23.10.2012, RV/2933-W/12, an die Amtsvertretung weitergeleitet.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_145`)


Mit den Schreiben der die Bf. seit Jahren betreuenden und behandelnden Ärztin Dr. E. vom  16.12.2019 und 30.07.2020 ist der Amtsvertretung die Tatsache, dass die Bf. infolge der in den  Schreiben genannten Diagnosen und ihrem Alter im Jahr 2018 pflegebedürftig und ein Leben  ohne Unterstützung aufgrund der Erkrankungen an PNP und dem kombinierten Aortenvitium  unmöglich war, bestätigt worden.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_146`)


2. Beweiswürdigung  Die Sachverhaltsfeststellungen beruhen auf a) dem Bescheid, mit dem der Bf. Pflegegeld Stufe  1 zuerkannt worden ist, b) den Schreiben der langjährigen Hausärztin Dr. E. vom 16.12.2019  und 30.7.2020, c) dem Bericht des OA Dr. A., Herz Jesu-KH, vom 6.12.2001 über die Operation  an der Wirbelsäule vom Vortag (Beilage 2/a), d) dem Arztbrief des Prim. Univ.-Prof. DDr. B.,  Unfallabteilung, Landesklinikum Baden Mödling, betreffend die frakturbedingte Operation vom  6.05.2013, e) der Niederschrift des Prim. Univ.- Prof. Dr. C. , Evangelisches Krankenhaus, vom  9.04.2014 betreffend die Operation am Darm vom 8.04.2014, f) dem Röntgen-Befund der  Radiologischen Gruppenpraxis Baden OG vom 25.04.2017 (Wirbelsäule), g) dem Befundbericht  des Dr. Med. Univ.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation
- `Dr. A.` — no gold match — likely missing annotation
- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 11** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_150`)


Im Gegensatz zur steuerlichen Vertretung  vertritt die Amtsvertretung die Rechtsmeinung, dass die Bf. aufgrund der in der  Arztbestätigung der Dr. E. vom 16.12.2019 genannten Diagnosen und ihrem Alter zwar  pflegebedürftig sei, jedoch liege ein detailliertes Gutachten trotz Aufforderung nicht vor.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_214`)


Die  Verschlechterung des Gesundheitszustands wurde durch den nachfolgend abgelichteten  Befundbericht der Hausärztin Dr. E. vom 30.07.2020 bestätigt:   „

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_219`)


Angesichts der Eigenschaft der  Bf. als langjährige Patientin der Dr. E. war es der Allgemeinmedizinerin möglich, den  Befundbericht vom 30.07.2020 mit der Darstellung des Status und der Kontinuität der  Behandlung der Bf. zu erstellen und die Angaben durch Vorlage der der Krankengeschichte  beigelegten Beweismittel (a) OP-Bericht des OA Dr. A., Herz Jesu-KH, vom 6.12.2001,  b) Arztbrief des Prim. Univ.-Prof. DDr. B. vom 6.05.2013, c) Niederschrift des Prim. Univ.- Prof.  Dr. C., Evangelisches KH, vom 9.04.2014, d) Befundbericht des Dr. Med. Univ.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation
- `Dr. A.` — no gold match — likely missing annotation
- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 14** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_230`)


Den Bedenken der Amtsvertretung gegen den Befundbericht der Dr. E. war zu erwidern, dass  prinzipiell ein niedergelassener Arzt für Allgemeinmedizin der erste Ansprechpartner eines  Patienten ist, folglich dessen üblicherweise bei ihm die Dokumentation der ärztlichen  Leistungen betreffend den Patienten zusammenläuft.

**False Positives:**

- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/133679.1`) (sent_id: `deanon_BFG_TRAIN/133679.1_164`)


Zu der Zeit, als die Befragte im Labor des Bf tätig war, hätten  weitere immer unterschiedliche Ärzte in der Makroskopie gearbeitet, Dr. H, Dr. A (bis 2008  jeden Donnerstag), die angestellte Dr. C. Auf Grund der Haftung des Labors für falsche  Befundungen wären schwierige Fälle zB bei Tumoren von einer Fachärztin der Pathologie Dr. H  noch einmal begutachtet worden.

**False Positives:**

- `Dr. C.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_12`)


300,93  km: 2.497,76   4.956,70  Weiters wurden vorgelegt:   - eine Aufstellung der geltend gemachten Fahrtkosten in Form von km-Geldern   - Listen über den Therapieablauf im Gesundheitszentrum Bad Sauerbrunn für Physiotherapien  und Heilmassagen im Zeitraum 06.02.2019 - 14.03.2019   - Rechnung Impuls Hotel Tirol Bad Hofgastein vom 08.04.2019 (an den Bf.)   - Therapieplan vom 27.03.2019 zur Stollentherapie 2019 im Gasteiner Heilstollen über acht  Einfahrten in der Zeit von 09.09.2019 - 21.09.2019   - Behandlungsbeitragsvorschreibungen der Versicherungsanstalt öffentlich Bediensteter (BVA)  des Jahres 2019 (an den Bf.)   - Honorarnote des Facharztes für physikalische Medizin und Rheumatologie Dr. P. vom  07.01.2019 samt Zahlungsbeleg   - Honorarnote der Fachärztin für Innere Medizin und Rheumatologie Dr. K. vom 14.05.2019   - Honorarnote der Fachärztin für Haut- und Geschlechtskrankheiten Dr. M. vom 24.07.2019  - Honorarnote des Ambulatoriums für medizinische und chemische Labordiagnostik vom  2 von 17 Seite 3 von 17

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. K.` — no gold match — likely missing annotation
- `Dr. M.` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `M.`(person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_53`)


Anbei übermittle ich ihnen den Arztbrief  sowie die ausgefüllten Kuranträge von Dr. P. und Dr. N.-S. und ersuche um Anerkennung der  außergewöhnlichen Belastung.“

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_54`)


Mit Schreiben vom 05.03.2021 ersuchte das Finanzamt den Bf. um Übermittlung der  Unterlagen, die er im Vorlageantrag erwähnt hatte (Arztbrief sowie die ausgefüllten  Kuranträge von Dr. P. und Dr. N.-S.).

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 19** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_58`)


Ich übersende ihnen nochmals die Kopie  betreffend Kuraufenthalt von Dr. P., Arztbrief Dr. K. sowie Ärztliche Verordnung vom Gasteiner  Heilstollen.“

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation
- `Dr. K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_60`)


X ja   Wann 2016, 2017, 2018   Wo Bad Hofgastein)   - Ärztliche Stellungnahme zu (Bf., Geburtsjahr) des Dr. P., Facharzt für physikalische Medizin,  Rehabilitation und Rheumatologie vom 07.01.2019:   Aktuelle Vorgeschichte – soweit antragsrelevant   Seit Jahren bekannte M. Bechterew Erkrankung seit Nov.

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 21** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_66`)


Patient ist heimfähig x ja, kurfähig x ja, benötigt Diät x ja,   ist gehfähig x ja, mit Hilfsmittel x nein, Rollstuhl x nein,   benötigt Begleitperson x nein,   benötigt fremde Hilfe (waschen, anziehen usw.) x nein,   benötigt Transport x nein   - Ärztliche Verordnung des Dr. med. univ. O., Facharzt für Physikalische und Rehabilitative  Medizin, Krankenanstalt Gasteiner Heilstollen, vom 09.09.2019 (bereits mit der Beantwortung  des Vorhalteschreibens vom 03.09.2020 vorgelegt)   - Arztbrief der Dr. K., Fachärztin für Innere Medizin und Rheumatologie, vom 14.05.2019  (Diagnose: Morbus Bechterew, akuter Schub)

**False Positives:**

- `Dr. K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_147`)


Bezüglich der Kur in Bad Hofgastein März-April 2019 legte der Bf. mit Antwortschreiben vom  16.05.2021 zum Vorhalt vom 05.03.2021 nicht nur den Antrag auf Rehabilitations-, Kur- bzw.  Erholungsaufenthalt vom 10.01.2019 vor, sondern auch die ärztliche Stellungnahme des Dr. P.,  Facharzt für physikalische Medizin, Rehabilitation und Rheumatologie vom 07.01.2019 (oben in  Punkt I. im Wesentlichen wiedergegeben): In dieser wird als antragsrelevante Diagnose  Morbus Bechterew (Erkrankung seit Nov. 2017) genannt und die Rehabilitation bzw. das  Kurheilverfahren für den Bewegungs- und Stützapparat bzw. den rheumatologischen  Formenkreis ausdrücklich in Bad Hofgastein Impuls Hotel Tirol inkl. Stolleneinfahrten  vorgeschlagen (mit dem Hinweis, dass der vorgeschlagene Ort nach Möglichkeit berücksichtigt  werde) samt Begründung für die vorgeschlagene Maßnahme (Verbesserung des AZ und der  Beweglichkeit, Maximierung der Alltagsaktivitäten, Reduktion der Schmerzmittel und  Krankenstände).

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_150`)


Außerdem geht aus der ärztlichen Stellungnahme des Dr. P. vom 07.01.2019 hervor, dass der  Bf. keine Begleitperson benötigt (vgl. oben in Punkt I.).

**False Positives:**

- `Dr. P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/134975.1`) (sent_id: `deanon_BFG_TRAIN/134975.1_153`)


Weiters wurde ein Arztbrief der Dr. K., Fachärztin für Innere Medizin und Rheumatologie, vom  14.05.2019 vorgelegt.

**False Positives:**

- `Dr. K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_99`)


Von seinem Onkel, Herrn Dr. A. R., der ebenfalls in diesem Haus wohnt, sowie  seiner Schwester, Frau R. H., sei ihm mitgeteilt worden, dass der Autoschlüssel samt allen  Papieren seit Monaten verschwunden sei.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_148`)


Herr Dr. A. R., der Onkel des Bf, wohnhaft in Adresse hat im Schreiben vom 28. Dezember 2020  an das Bezirksgericht D iZm dem Verfahren über die Bestellung eines Erwachsenenvertreters  für Frau B. H. zum verfahrensgegenständlichen Fahrzeug ausgeführt:  „Mitunter setzt sich Frau B. H. in ihr in der K-Straße geparktes - offenbar unversperrtes - Kfz und  versucht dieses in Betrieb zu nehmen.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht D`(organisation)

**Example 27** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_157`)


Mit E-Mail vom 11. November 2024 hielt Herr Dr. A. R. gegenüber der belangten Behörde,  dieses Mal explizit im Zusammenhang mit dem Beschwerdeverfahren, fest:  „Über Ersuchen meines Neffen Antonia Adding  bestätige ich gerne die Richtigkeit meiner  seinerzeitigen Wahrnehmungen hinsichtlich des Kfz meiner Schwägerin B. H. (Alfa Romeo Grün,  an das Kennzeichen kann ich mich nicht mehr erinnern).

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Antonia Adding`(person)

**Example 28** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_185`)


In diesem Zusammenhang ist auch darauf hinzuweisen, dass dem Erwachsenenvertreter zum  Zeitpunkt seiner Eingabe vom 28. Jänner 2022 an die belangte Behörde die Angaben des Herrn  Dr. A. R. im Schreiben vom 28. Dezember 2020 (Fahrzeug zumindest 8 Monate lang nicht  bewegt;

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/147279.1`) (sent_id: `deanon_BFG_TRAIN/147279.1_189`)


In einer Gesamtbetrachtung der Umstände ist aufgrund der Aussagen der Auskunftspersonen  Dr. A. R. und R. H. sowie insbesondere der diesbezüglich übereinstimmenden Aufzeichnungen  der Meldungsleger der MA mit hoher Wahrscheinlichkeit davon auszugehen, dass das  Fahrzeug bereits im Februar 2020, dh Monate vor dem strittigen Vorschreibungszeitraum, an  der angegebenen Adresse abgestellt worden ist und in der Folge dort unverändert verblieben  ist.

**False Positives:**

- `Dr. A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_TRAIN/148044.1`) (sent_id: `deanon_BFG_TRAIN/148044.1_526`)


Ebenso konnte aus dem Belegmaterial (OZ. 77) entnommen werden, dass die Bf. zahlreiche  Facharztbesuche, Physiotherapeuten, Heilpraktiker, ärztliche Labors (Re v. 22.8.2014,  1.10.2014 Dr. M., 30.10.2014 Dr. Sch., 30.10.2014 Dr. Sz., 16.1.2015 Dr. E., 26.1.2015 Dr. W.,  4.3.2015 Diagnostik M., 28.8.2015 Heilpraktikerin H., 14.12.2015 Heilpraktikerin H., 17.12.2015  Labor Dres., 30.12.2015 Heilpraktikerin H., 29.11.2016 Dr. E., 10.2.2017 Zahnarzt 4 Sitzungen,  21.3.2017 Facharzt 4 Sitzungen, 11.8.2017 Zahnarzt, 12.10.2017 Dr. E., 27.12.2017 Dr. B. 2  Sitzungen, absolviert hat.

**False Positives:**

- `Dr. M.` — partial — gold is substring of pred: `M.`
- `Dr. E.` — no gold match — likely missing annotation
- `Dr. W.` — no gold match — likely missing annotation
- `Dr. E.` — no gold match — likely missing annotation
- `Dr. E.` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 4

**Gold Entities:**

- `M.`(person)
- `M.`(person)
- `Dr. B.`(person)

</details>

---

## `MedR Title Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fa663fdd`  
**Description:**
Specifically matches person names following the 'MedR' title, ensuring the full name is captured including preceding titles like 'RgR' or 'DDr'.

**Content:**
```
\b((?:RgR\s+|DDr\s+|Mag\.\s+|Dr\.\s+|Univ\.-Prof\.(?:in\s+)?\s+)?MedR\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s*,\s*[A-Z]{2,})?(?:\s+(?:MSc|MBA|LL\.M|LL\.B|B\.Sc|B\.A|B\.Ed|MA|LLB|B\.Sc|B\.A|B\.Ed|BEd|B\.Ed|Bakk\.\s+techn\.|Bakk\.\s+iur\.|Bakk\.\s+rer\.\s+\w+)*)(?=[\s,;\n]|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1501 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/133915.1`) (sent_id: `deanon_BFG_TRAIN/133915.1_22`)


Die  Beschwerdeführerin beantragte daher „die Aufhebung der angefochtenen Bescheide und  Erlassung geänderter Bescheide, in [welcher] meine Einkünfte aus meiner  Werksvertragstätigkeit für meinen Ehemann Dipl.-Ing. MedR Pascal Blochel  als solche aus selbstständiger Arbeit  ausgewiesen werden“.

**False Positives:**

- `MedR Pascal Blochel ` — positional overlap with gold: `Dipl.-Ing. MedR Pascal Blochel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. MedR Pascal Blochel`(person)

</details>

---

## `Name Born Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `633e173e`  
**Description:**
Matches person names following 'geboren am' or 'geb.' to capture names in birth contexts, ensuring the name follows the date context.

**Content:**
```
(?:geboren\s+am\s+|geb\.\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*)(?=[\s,;\n]|$|\s+KG|\s+Bf\.|\s+\.\s*$|\s+\(|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1871 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_4`)


Der Beschwerdeführer (Bf.), geboren am Dezember 1992, ist besachwaltet.

**False Positives:**

- `Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/132557.1`) (sent_id: `deanon_BFG_TRAIN/132557.1_32`)


Der Ehegatte der  Beschwerdeführerin, K, geboren am Datum, ist an dieser Adresse seit 2.1.2003 mit  Hauptwohnsitz gemeldet.

**False Positives:**

- `Datum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/132617.1`) (sent_id: `deanon_BFG_TRAIN/132617.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Konrad Schneidewendt (= Beschwerdeführerin, Bf), geb. Juni 1998, hatte mit Formular Beih100 im  September 2019 für sich die Zuerkennung der Familienbeihilfe (FB) wegen "Ausbildung" bzw.  "Lehre" mit einer voraussichtlichen Dauer bis 28.1.2022 beantragt.

**False Positives:**

- `Juni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Konrad Schneidewendt`(person)

</details>

---

## `Bf Parenthetical Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c15108ab`  
**Description:**
Captures person names following 'Bf.' or 'Bf' in parenthetical definitions (e.g., 'Bf. genannt) Name' or 'Bf) Name').

**Content:**
```
\b(?:Bf\.|Bf)\s*(?:genannt\s*)?\)?\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 295 | 0 | 295 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 295 | 2012 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/124843.1`) (sent_id: `deanon_BFG_TRAIN/124843.1_67`)


Der Text der Beschwerde lautet: „    Innerhalb offener Frist erheben wir im Namen von Herrn Bf Berufung gegen den „Bescheid   ü   ber die Festsetzung der Normverbrauchsabgabe f   ü   r den Zeitraum Seite 6 von 18 Mai 2012“  („N0VA-Beseheid“) vom 9.7.2012, der durch Bescheidbegr ü   ndung des Finanzamtes Bruck Eisenstadt Oberwart vom 13.7.2012 erg   ä   nzt und dessen Frist zur Berufung am 10.8.2012 auf den 30.9.2012 erstreckt wurde, und begehren die Herabsetzung der festgesetzten Normverbrauchsabgabe f   ü   r den Zeitraum Mai 2012 von EUR 19.131,60    um EUR 19.131,60 auf EUR 0,00.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/128975.1`) (sent_id: `deanon_BFG_TRAIN/128975.1_64`)


Tabelle der Bf  Die adaptierte Prognoserechnung weist einen kumulierten Überschuss von € + 13.576,00 aus.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/129005.1`) (sent_id: `deanon_BFG_TRAIN/129005.1_56`)


Desweiteren übermittelte der Bf. Zahlungsaufstellungen betreffend Strom, Miete, Gas, Telefon  und Internet.

**False Positives:**

- `Zahlungsaufstellungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/129033.1`) (sent_id: `deanon_BFG_TRAIN/129033.1_79`)


Diesem Schreiben fügte der Bf. Fotos der einzelnen aufgelisteten Ausstattungselemente bei.

**False Positives:**

- `Fotos` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/129086.1`) (sent_id: `deanon_BFG_TRAIN/129086.1_5`)


Dagegen hat die Bf. Beschwerde erhoben und ausgeführt, dass sie in Wien kein Grab gehabt  und es neu errichten habe lassen.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)
- `Mag. Wolfgang Freudelsperger`(person)
- `Finanzamtes Wien 1/23`(organisation)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_63`)


Im gegenständlichen Fall wurden durch die Bf. Betriebsausgaben iHv Euro 180.000,00 geltend  gemacht, denen in der Rechnung der M-GmbH (Rechnungsdatum 8.3.2008) angeführte  Leistungen zugrunde lagen.

**False Positives:**

- `Betriebsausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_8`)


Zusätzlich übermittelte der Bf Kopien von sechs Bankbelegen, aus  1 von 6 Seite 2 von 6

**False Positives:**

- `Kopien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_11`)


Mit Schriftsatz vom 28.08.2013 erhob die steuerliche Vertretung des Bf Berufung gegen den  Einkommensteuerbescheid 2012 vom 23.08.2013 und beantragte, die Rückzahlung der  Notstandshilfe in Höhe von 12.383,52 € ebenso wie die in der Erklärung noch nicht geltend  gemachten Kurkosten in Höhe von 338,27 € sowie die pauschalen Diätkosten für  Zuckerkrankheit in Höhe von 840 € als außergewöhnliche Belastungen gemäß § 34 EStG zu  berücksichtigen.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/129261.1`) (sent_id: `deanon_BFG_TRAIN/129261.1_25`)


Aufgrund seiner Zuckerkrankheit machte der Bf Mehraufwendungen wegen  Krankendiätverpflegung in Höhe des Pauschbetrages als außergewöhnliche Belastungen  geltend.

**False Positives:**

- `Mehraufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_60`)


Wichtig sei im vorliegenden Verfahren nur die korrekte Leistungserbringung durch die Firma T  an den Bf.  Betreffend die Firma C GmbH führte der Bf. aus, dass am 29.11.2012 der Konkurs über das  Vermögen dieser Firma eröffnet und mangels Masse abgelehnt worden sei.

**False Positives:**

- `Betreffend` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_69`)


Im Zuge des Verfahrens legte der Bf. Kopien von folgenden Unterlagen vor:  An ihn gelegten Rechnungen der Firma T:  1.)

**False Positives:**

- `Kopien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_74`)


Weiters legte der Bf. Ablichtungen der Kasseneingangsbelege  der Firma T gerichtet an den Bf.  vor:  1.)

**False Positives:**

- `Ablichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/129432.1`) (sent_id: `deanon_BFG_TRAIN/129432.1_89`)


Bezüglich der Fremdleistungen der Firma C GmbH an die Firma T legte der Bf. Ablichtungen  folgender Rechnungen und Kassenbelege der C GmbH an die Firma T vor:  A1) Rechnung 9.10.2012, Leistungszeitraum 24.9.12-9.10.12, € 17.508,73, Baustelle, Adresse1,  Kassaeingangsbeleg 9.10.12 über € 17.508,73  A2) Rechnung 24.4.2012, Leistungszeitraum 10.10.11 - 20.4.12, € 35.330,-, Baustelle Adresse2,  Kassaeingangsbeleg 24.4.12 über € 24.245,80

**False Positives:**

- `Ablichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/129533.1`) (sent_id: `deanon_BFG_TRAIN/129533.1_7`)


Während seiner Dienstverrichtung in Österreich wurden dem Bf Stock Options und Restricted  Stock Units (RSU) gewährt, die er im Jahr 2011 ausübte.

**False Positives:**

- `Stock Options` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/129533.1`) (sent_id: `deanon_BFG_TRAIN/129533.1_12`)


Mit Schreiben vom 21.12.2012 erhob die steuerliche Vertretung des Bf Berufung gegen den  Einkommensteuerbescheid 2011 vom 21.11.2012 und begründete diese im Wesentlichen  damit, dass der Vorteil aus der Ausübung der Stock Options bzw RSUs sonstige Bezüge gemäß  § 67 Abs 1 EStG 1988 darstellte, der innerhalb des Jahressechstels mit dem begünstigten  Steuersatz von 6 % zu versteuern sei und dass für die Berechnung des Jahressechstels auch die  laufenden Bezugsteile einzubeziehen seien, die in Österreich nicht steuerpflichtig seien.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_228`)


Bf. Diagramme, technische Zeichnungen sowie Fotos vorgelegt.

**False Positives:**

- `Diagramme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_334`)


- Probetrocknungen in der Pilotanlage WJ 2011  Die nachgereichten Unterlagen enthalten keine weiterreichenden Informationen zu  eigenbetrieblich durchgeführten F&E-Aktivitäten der Bf.   Trotz konkreter Rückfrage wird nicht ausreichend beschrieben, welche Probetrocknungen im  Detail mit welcher technologischen Zielsetzung durchgeführt wurden.

**False Positives:**

- `Trotz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_337`)


- Fortsetzung der Probetrocknungen in der Pilotanlage WJ 2012  Die nachgereichten Unterlagen enthalten keine weiterreichenden Informationen zu  eigenbetrieblich durchgeführten F&E-Aktivitäten der Bf.   Die von der FFG am 25. Oktober 2016 gestellten Fragen blieben inhaltlich unbeantwortet.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/129635.1`) (sent_id: `deanon_BFG_TRAIN/129635.1_349`)


- Probetrocknungen im Serien-Prototypen WJ 2012   Die nachgereichten Unterlagen enthalten keine weiterreichenden Informationen zu  eigenbetrieblich durchgeführten F&E-Aktivitäten der Bf.   Die von der FFG am 25. Oktober 2016 gestellten Fragen blieben inhaltlich unbeantwortet.

**False Positives:**

- `Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/129671.1`) (sent_id: `deanon_BFG_TRAIN/129671.1_161`)


Bescheid über die Festsetzung des Zuschlages zum DB (DZ) für das Jahr 2010 in Höhe  von 150,06 €  Am 28.7.2011 erstattete die Bf Berufung gegen acht der zehn Bescheide vom 29.6.2011 – alle  ausgenommen der Bescheide betreffend der Säumniszuschläge.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_75`)


Bezüglich der unbaren Erlöse der AGMbH wurden vom Bf. Rechnungen an die Auftragsfirma  gelegt und diese auch verbucht.

**False Positives:**

- `Rechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_10`)


Das Finanzamt folgte dieser Feststellung und erließ für 2014 einen Haftungsbescheid gemäß  § 99 EStG 1988 und schrieb der Bf Abzugssteuer in Höhe von 10.140,00 Euro vor.

**False Positives:**

- `Abzugssteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/130149.1`) (sent_id: `deanon_BFG_TRAIN/130149.1_77`)


A habe bei  seiner Einvernahme bestätigt, dass er für die Bf Eisenbeton-Montagen mit vier Angestellten  durchgeführt habe.

**False Positives:**

- `Eisenbeton` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_16`)


Weiters   - das Jahreszeugnis vom 01. Februar 2019, wonach der Sohn der Bf. Schüler der 3BSI (dritte  Fachklasse) für den Lehrberuf Informationstechnologie-Technik war und die 3. Klasse  (12. Schulstufe) mit gutem Erfolg abschloss und zum Aufsteigen in die 4. Klasse (13. Schulstufe)  berechtigt war.

**False Positives:**

- `Schüler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/130332.1`) (sent_id: `deanon_BFG_TRAIN/130332.1_75`)


Die Geschäftsführung des den Diplomlehrgang veranstaltenden Instituts bestätigte der Bf.  Folgendes:  Gerne bestätige ich, Dr. …, Begründerin und Eigentümerin des Instituts für Relationale  Beratung (IRBW) und langjährige Coaching-Expertin, dass (die Bf.) die Coaching-Ausbildung in  unserem Institut absolviert hat.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/130413.1`) (sent_id: `deanon_BFG_TRAIN/130413.1_46`)


Gegen die Strafverfügung wurde vom Bf. Einspruch erhoben (E-Mail vom 29. Juli 2019) und die  Strafverfügung dem Grunde und der Höhe nach bestritten.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/130413.1`) (sent_id: `deanon_BFG_TRAIN/130413.1_105`)


Die Protokollliste wurde dem BFG am 6. Februar übermittelt.  Aus der Protokollliste geht hervor, dass der Meldungsleger KO am 27. März 2020 in der Xstraße  folgende Beanstandungen durchgeführt hat:  Xstraße *2 10:21 Uhr  Xstraße *1 10:26 Uhr (= Fahrzeug des Bf.)  Xstraße *3 10:33 Uhr  Der Bf. wurde zu der am 21. Juli 2020 anberaumten mündlichen Verhandlung zeitgerecht und  ordnungsgemäß geladen.

**False Positives:**

- `Xstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130422.1`) (sent_id: `deanon_BFG_TRAIN/130422.1_131`)


Im Zuge des verwaltungsgerichtlichen Verfahrens wurde dem Bf Gelegenheit gegeben, dem  BFG ein fundiertes Sachverständigengutachten über den Wert der Liegenschaft  vorzulegen.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_10`)


Dagegen erhob die Bf. Beschwerde und brachte u.a. Folgendes vor:  "Der Sohn der Beschwerdeführerin, VN-Sohn NN, geboren am GEBURTSDATUM, hat im Jahr  2018 insgesamt einen Betrag von EUR 15.621,03 als Einkommen aus unselbstständiger  Erwerbstätigkeit bezogen;

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_147`)


Es ist nicht ersichtlich, dass der Bf. Grund dazu hätte, zu Lasten  seiner Dienst- und Unterkunftgeberin gegenüber der Abgabenbehörde unrichtige Angaben zu  tätigen.

**False Positives:**

- `Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_189`)


Umstände zweifelsohne die weitaus  umfassendere Verfügungsgewalt über den BMW zukommt („Wer immer das Auto verwenden  möchte, muss sich an … die Bf. wenden.) und die Bf. Herrn AN* die im Zusammenhang mit dem  Fahrzeugbetrieb anfallenden Kosten zur Gänze ersetzt, war es letztlich im Wege der  anzustellenden Ermessensübung jedenfalls sachgerecht, die Bf. als Halterin – und nicht etwa  ihren lediglich nutzungsberechtigten Arbeitnehmer – als Steuerschuldnerin heranzuziehen.

**False Positives:**

- `Herrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_64`)


Am Familienwohnsitz lebt die Ehegattin des Bf. Kinder sind nicht aktenkundig.

**False Positives:**

- `Kinder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_120`)


Da die Wohnung vom Bf. und drei weiteren Personen bewohnt wurde (Vierer- Wohngemeinschaft), entfielen auf den Bf. Kosten iHv [(€ 301,33 x 12 + € 140,40) : 4 =)]  € 939,09.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_TRAIN/130536.1`) (sent_id: `deanon_BFG_TRAIN/130536.1_35`)


„Zur Information“ schrieb der Bf. Folgendes:  3 von 16 Seite 4 von 16

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_TRAIN/130601.1`) (sent_id: `deanon_BFG_TRAIN/130601.1_91`)


Demgemäß war die Verwaltungs(straf)behörde iSd Grundsätze der Rechtsprechung des  Verwaltungsgerichtshofes berechtigt, nach Scheitern der Kontaktaufnahme mit dem vom Bf.  Genannten im Rahmen von dessen erhöhter Mitwirkungspflicht im Verwaltungsstrafverfahren  zweckdienliche Angaben zu verlangen (VwGH 04.06.1991, 90/18/0091, VwGH 2008/02/0030,  23.01.2009).

**False Positives:**

- `Genannten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 36** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_49`)


War amtsbekannt, dass der Ex-Ehepartner der Bf.  Einkünfte von über 6.000,00 € im Streitjahr bezogen hatte, so war die Überschreitung der  Einkunftsgrenze für M.M.A. - 6.000 € - im Jahr 2019 festzustellen.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_TRAIN/130685.1`) (sent_id: `deanon_BFG_TRAIN/130685.1_18`)


Gegen die Strafverfügung wurde vom Bf. Einspruch erhoben (E-Mail vom 10. August 2020) und  vorgebracht, dass er das Fahrzeug kurz abgestellt habe, um schnell etwas zu besorgen.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_103`)


Als weitere Werbungskosten wurden von der Bf. Ausgaben wie im  Vorjahr für Arbeitsmittel (Notebook mit EUR 99,39 nach Abzug von 40% Privatanteil durch die  Bf., Internetkosten von EUR 105,00 ohne erkennbarem Abzug eines Privatanteils) in der Höhe  von EUR 204,39 geltend gemacht, jedoch zusätzlich für Trainingsmittel (Thera-Bänder,  Türrecks, Redondo-Ball) einen Betrag von EUR 82,62 und für Arbeitsbekleidung (Pullover, T- Shirt) einen Betrag von EUR 52,42.

**False Positives:**

- `Ausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_TRAIN/131110.1`) (sent_id: `deanon_BFG_TRAIN/131110.1_7`)


Erst nach Ergehen der BVE bzw. im finanzgerichtlichen Ermittlungsverfahren übermittelte die  Bf Teile der angeforderten Unterlagen.

**False Positives:**

- `Teile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_TRAIN/131110.1`) (sent_id: `deanon_BFG_TRAIN/131110.1_53`)


Zudem beantragt die Bf Kosten des öffentlichen Verkehrsmittels für wöchentliche  Besuchsfahrten zum Gatten in das Pflegeheim (707,20 € p.a.).

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_TRAIN/131110.1`) (sent_id: `deanon_BFG_TRAIN/131110.1_120`)


Im Übrigen fanden die (angeblich) übernommenen Pflegheimkosten ohne Zweifel im späteren  Erbanteil der Bf Deckung, sodass der geltend gemachten Belastung eine spätere Bereicherung  des Bf gegenübersteht und damit keine endgültige Beeinträchtigung der wirtschaftlichen  Leistungsfähigkeit eintrat (VwGH 27.2.1009, 87/14/0004).

**False Positives:**

- `Deckung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_138`)


Zudem ist die Bf Eigentümerin eines Wohnhauses in Land3.

**False Positives:**

- `Eigentümerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_207`)


Daneben hat die Bf Urlaubsreisen unternommen und glaublich auch, als  gebürtige Land3, Fahrten zur dortigen Verwandtschaft und zu dem in ihrem Eigentum  stehenden Wohnhaus in Land3 unternommen, das sie wohl ebenso in gewissem Umfang zu  betreuen hatte.

**False Positives:**

- `Urlaubsreisen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_TRAIN/131343.1`) (sent_id: `deanon_BFG_TRAIN/131343.1_32`)


Im vorliegenden Fall wird dem Begehren des Bf. Folge gegeben, eine Rechtsfrage von  grundsätzlicher Bedeutung liegt nicht vor, weshalb die Revision nicht zuzulassen war.

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_33`)


Beweismittel:   Bescheide sowie Eingaben des Bf  Auskunft der OÖ GKK v. 20.08.2020  Lohnzettel über Nachzahlung  Ausdrucke der Veranlagungsjahre 2016 und 2017  Stellungnahme:   Gemäß § 19 Abs. 1 EStG 1988 sind Einnahmen in jenem Kalenderjahr bezogen, in dem sie dem  Steuerpflichtigen zugeflossen sind.

**False Positives:**

- `Auskunft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_63`)


Die - beschwerdegegenständliche - Rechnung wurde erstellt wie folgt:   D… GmbH [Schrift und Schriftgröße wie bei der Vollmacht]  (Anschrift) – Tel: … - Fax: … - Email: office…   (Name und Anschrift des Bf.)   Wien, am 20. März 2009   Rechnung: 005-2009   BVH: Wien ****, L…str..  Arbeiten: Diverses  Lzr: Februar März 2009   Für die ausgeführten Leistungen, o.a. Baustelle, verrechnen wir Ihnen lt. Vereinbarung wie  folgt:   Pos.1 Spanplatte € 1.028,72  Pos.2 Laminat € 1.249,16  Pos.3 Maler € 2.350,00  Pos.4 Einstreichen € 800,00  6 von 9 Seite 7 von 9

**False Positives:**

- `Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_66`)


20 % MwST € 1.129,58      € 6.777,46  Zahlungsmodalität: Prompt, nach Rechnungserhalt, Netto ohne Skonto   Bankverbindung: B… Konto-Nr. 0…2-930 BLZ 1…  HG-Wien, FN …  UID-Nr.: ATU...  Steuer-Nr.: …   [gesamte 2. Zeile: wie Vollmacht]    Ebenso wurde die beschwerdegegenständliche Rechnung Nr. 009 - 2009 für das Bauvorhaben  Wien 15, R….g. 15 (Gewerk: Fassade), Bruttosumme € 19.097,52, erstellt.  Die aktenkundige IZV-Auftragsliste beinhaltet Folgendes:  Konto: …  Absender: (HV Dr. Y – Bf.)  Verfüger: (X)  Vom Bankrechner am 06.04.2009 um 12:00 entgegengenommen Status: positiv  Durchführungsdatum: 06.04.2009 Dringende Durchführung   Nr Empfänger/Zahlungspflichtiger BLZ / Kontonr. Betrag WKZ  1 D… GmbH  (Anschrift laut Vollmacht u. Rechnung)  1… / ...2930 20.000,00 EUR  1 Eilüberweisung Gesamtsumme: 20.000,00 EUR

**False Positives:**

- `Verfüger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_69`)


Baumaterials auf die Baustelle und das Einteilen der Arbeiter umfassten, ausgeführt worden  sind, erfolgte sodann die Rechnungslegung durch die D. GmbH, ist nicht zu erkennen, dass bei  der Bf. Zweifel aufkommen mussten, die Leistungserbringung sei nicht von der D.GmbH  vorgenommen worden.

**False Positives:**

- `Zweifel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_TRAIN/131601.1`) (sent_id: `deanon_BFG_TRAIN/131601.1_58`)


Im vorliegenden Fall liegt diese Voraussetzung des eigenen Hausstandes in Polen nicht vor, da  der Bf. Räumlichkeiten innerhalb des Wohnungsverbandes mit seinen Eltern im Elternhaus  mitbewohnt.

**False Positives:**

- `Räumlichkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_TRAIN/131914.1`) (sent_id: `deanon_BFG_TRAIN/131914.1_5`)


Außergewöhnliche Belastungen wegen Behinderung Bf Gattin  Grad der Behinderung 70 % 60 %  Diät wegen Magenkrankheit  ja   Diät wegen Zuckerkrankheit  Ja  Unregelmäßige Ausgaben für Hilfsmittel (zB Rollstuhl, Hörgerät,  Blindenhilfsmittel) sowie Kosten der Heilbehandlung (zB ärztliche  Kosten, Medikamente) allfällige Kostenersätze bitte abziehen  1.374,00 3.938,87  Mit Schreiben vom 17. Juli 2019 forderte das Finanzamt Bf auf, seine zusätzlichen  Krankheitskosten in Höhe von 1.374,00 € und jene der Gattin von 3.938,87 € durch Vorlage  entsprechender Aufstellungen, Unterlagen und Belegen nachzuweisen.

**False Positives:**

- `Gattin  Grad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_TRAIN/131914.1`) (sent_id: `deanon_BFG_TRAIN/131914.1_7`)


Im Einkommensteuerbescheid 2018 vom 7. Oktober 2019 berücksichtigte das Finanzamt  folgende Beträge als Außergewöhnliche Belastungen:  Außergewöhnliche Belastungen Bf Gattin  Aufwendungen vor Abzug des Selbstbehaltes (§ 34 Abs. 4 EStG 1988  -3.356,40   Selbstbehalt 3.356,40   Außergewöhnliche Belastungen wegen Behinderung    Freibetrag wegen Behinderung § 35 Abs. 3 EStG 1988 -363,00 -294,00  Pauschbetrag nach VO über ao Belastungen wegen Behinderung -504,00 -840,00  Nachgewiesene Kosten aus Behinderung nach der VO -1.374,00 -515,56  Summen 2.241,00 1.649,56  Insgesamt für außergewöhnliche Belastungen berücksichtigt 3.890,56 €

**False Positives:**

- `Gattin  Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_TRAIN/131914.1`) (sent_id: `deanon_BFG_TRAIN/131914.1_12`)


Mit am 5. November 2019 persönlich beim Finanzamt eingebrachtem Schriftsatz vom 28.  Oktober 2019 erhob Bf Beschwerde gegen den Einkommensteuerbescheid 2018 und  beantragte sinngemäß mit folgender Begründung die Gebühren der Tagesklinik nicht um  Selbstkosten von 36,61 € und die Kosten für Kieferchirurgie und Zahnarzt im Zusammenhang  mit dem Implantatverlust um keinen Selbstbehalt zu kürzen:  1. Haushaltsersparnis für Aufenthalt der Gattin in Tagesklinik

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_15`)


Bisheriges Verwaltungsverfahren  Das Finanzamt machte mit einem Haftungsbescheid vom 27.4.2016 gegenüber der Bf  Kapitalertragsteuer iHv € 33.625,00 unter Angabe der maßgeblichen Gesetzesstellen und  Erläuterung des geübten Ermessens geltend.

**False Positives:**

- `Kapitalertragsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_134`)


4. Die Amtspartei wird ersucht, insbesondere zu den Renditedarstellungen der Bf Stellung  zu nehmen.

**False Positives:**

- `Stellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_TRAIN/132264.1`) (sent_id: `deanon_BFG_TRAIN/132264.1_18`)


Per E-Mail vom 9.11.2020 erhob der Bf. Beschwerde gegen die o.a. Vollstreckungsverfügungen  und brachte u.a. folgendes vor.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_TRAIN/132368.1`) (sent_id: `deanon_BFG_TRAIN/132368.1_16`)


3. Beschwerde  Fristgerecht wurde vom Bf Beschwerde erhoben und vorgebracht, dass es richtig ist, dass der  vom Bf getätigte Investitionsbetrag in der Vereinbarung mit € 130.000,00 angegeben wurde,  gemäß VP V. wurde jedoch der Geldwert mit € 40.000,00 festgelegt.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_34`)


Das im Dezember 1999 geborene Kind Priv.-Doz.in KommR Ida Sackerer, MBA  lebte seit August 2014 nicht mehr im  Haushalt ihrer Mutter, der Bf.   Diese Feststellung ist, soweit sie die Tochter Priv.-Doz.in KommR Ida Sackerer, MBA  betrifft, unstrittig.

**False Positives:**

- `Diese Feststellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in KommR Ida Sackerer, MBA`(person)
- `Priv.-Doz.in KommR Ida Sackerer, MBA`(person)

**Example 58** (doc_id: `deanon_BFG_TRAIN/132647.1`) (sent_id: `deanon_BFG_TRAIN/132647.1_171`)


Wie den vorgelegten  Einkommensteuererklärungen und späteren Berufungen/Beschwerden entnommen werden  kann, sind Herrn Bf. Einkünfte niemals unbesteuert geblieben: Österreich besteuert das  Welteinkommen, einerseits im Wege der Anrechnungsmethode, andererseits im Wege der  Befreiungsmethode.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_TRAIN/132794.1`) (sent_id: `deanon_BFG_TRAIN/132794.1_9`)


Letztgenannter ist seit 28.9.2012  Kommanditist der Bf. Die KomplementärGes m.b.H. (früher: alterFirmenwortlaut-GmbH) ist  seit Juli 2016 die (einzige) unbeschränkt haftende Gesellschafterin der Bf.

**False Positives:**

- `Die Komplementär` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_12`)


Der  Beschwerdeantrag wurde damit begründet, dass die Bf. wegen ihrer Krankheiten sowie ihrer  Pflege- und Betreuungsbedürftigkeit bereits seit mehreren Jahren nicht mehr in der Lage sei,  einen eigenen Haushalt zu führen (vgl. dazu Schreiben der Bf. It. Blg. 2).

**False Positives:**

- `It` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_TRAIN/132838.1`) (sent_id: `deanon_BFG_TRAIN/132838.1_146`)


2. Beweiswürdigung  Die Sachverhaltsfeststellungen beruhen auf a) dem Bescheid, mit dem der Bf. Pflegegeld Stufe  1 zuerkannt worden ist, b) den Schreiben der langjährigen Hausärztin Dr. E. vom 16.12.2019  und 30.7.2020, c) dem Bericht des OA Dr. A., Herz Jesu-KH, vom 6.12.2001 über die Operation  an der Wirbelsäule vom Vortag (Beilage 2/a), d) dem Arztbrief des Prim. Univ.-Prof. DDr. B.,  Unfallabteilung, Landesklinikum Baden Mödling, betreffend die frakturbedingte Operation vom  6.05.2013, e) der Niederschrift des Prim. Univ.- Prof. Dr. C. , Evangelisches Krankenhaus, vom  9.04.2014 betreffend die Operation am Darm vom 8.04.2014, f) dem Röntgen-Befund der  Radiologischen Gruppenpraxis Baden OG vom 25.04.2017 (Wirbelsäule), g) dem Befundbericht  des Dr. Med. Univ.

**False Positives:**

- `Pflegegeld Stufe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_TRAIN/132861.1`) (sent_id: `deanon_BFG_TRAIN/132861.1_65`)


„Beweis:  Einvernahme des Bf.  Einvernahme des Meldungslegers  Einvernahme des Zeugen A., p.A. Einsiedlergasse 2, 1050 Wien, Stadt Wien, MA 48  Zeuge/in: B., p.A. MA 67, Dresdner Straße 81-85, 1200 Wien,  weitere Beweis vorbehalten“  Sämtliche von ihm gestellten Beweisanträge würden aufrechterhalten.

**False Positives:**

- `Einvernahme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 63** (doc_id: `deanon_BFG_TRAIN/133136.1`) (sent_id: `deanon_BFG_TRAIN/133136.1_37`)


Aus dieser Tätigkeit erzielte der Bf Einkünfte aus nichtselbständiger Arbeit, die mangels einer in  Österreich gelegenen Betriebstätte des Arbeitsgebers nicht der inländischen Lohnsteuer  unterzogen wurden.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_TRAIN/133151.1`) (sent_id: `deanon_BFG_TRAIN/133151.1_7`)


25/481 Anteile verbunden mit Wohnungseigentum  an der Dachbodeneinheit Top 7 für die Bf.   Erwerbszweck ist der Dachbodenausbau durch die Bf auf ihre alleinigen Kosten (Pkt. III.2.i)  1 von 8 Seite 2 von 8

**False Positives:**

- `Erwerbszweck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_TRAIN/133151.1`) (sent_id: `deanon_BFG_TRAIN/133151.1_17`)


Gemäß Vertragspunkt III. übergibt die X-GmbH 92/573 Miteigentumsanteile aus ihren Anteilen  in das Eigentum der Bf.   Sämtliche mit der Vertragserrichtung verbundenen Kosten, insbesondere die daraus  resultierende Grunderwerbsteuer, sind von der Bf zu tragen (Pkt. V.).

**False Positives:**

- `Sämtliche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_TRAIN/133262.1`) (sent_id: `deanon_BFG_TRAIN/133262.1_85`)


In ihrem  Antrag auf Wiederaufnahme legt die Bf Nachweise vor, die Zahlungen an die Schule der  Tochter im März 2020 nachweisen.

**False Positives:**

- `Nachweise` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_TRAIN/133262.1`) (sent_id: `deanon_BFG_TRAIN/133262.1_102`)


Am 22. Juli 2019 erließ das Finanzamt den Abweisungsbescheid:  Ihr Antrag vom 21.5.2019 auf Familienbeihilfe wird abgewiesen für: (Tochter der Bf.)  Begründung  Zu (im Juli 2000 geborene Tochter der Bf.):  Gemäß § 2 Abs. 2 Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen Anspruch  auf Familienbeihilfe für ein Kind, zu deren Haushalt das Kind gehört.

**False Positives:**

- `Begründung  Zu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_TRAIN/133262.1`) (sent_id: `deanon_BFG_TRAIN/133262.1_153`)


In ihrem Antrag auf Wiederaufnahme legt die Bf Nachweise vor, die Zahlungen an  die Schule der Tochter im März 2020 nachweisen.

**False Positives:**

- `Nachweise` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_TRAIN/133459.1`) (sent_id: `deanon_BFG_TRAIN/133459.1_276`)


Sowohl die Einbuchung einer „Sonstigen Verbindlichkeit“ von 55.000,- € samt  Rechnungsabgrenzung (RAP) im Jahresabschluss 2008, als auch die Ausbuchung der  Verrechnungsverbindlichkeit gegen den Bf Ende April 2009 hätte sich dadurch erübrigt.

**False Positives:**

- `Ende April` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_TRAIN/133459.1`) (sent_id: `deanon_BFG_TRAIN/133459.1_281`)


Die gewinnneutrale Einbuchung einer „Sonstigen Verbindlichkeit“ im Jahresabschluss 2008 und  die Reduktion der Verrechnungsverbindlichkeiten gegen den Bf bei gleichzeitiger  Verminderung der Kassaeinlagen - doch unverändert belassenem Stand der  Kundenforderungen - nach Entdeckung des Buchungsfehlers im April 2009, bieten ebenfalls  keine Stütze für die Feststellung einer beabsichtigten Zuwendung der betreffenden  Geldbeträge an den Bf. Tragfähige Anhaltspunkte anderer Art, die auf einen derartigen  Verzicht der L-GmbH gegenüber dem Bf schließen lassen, waren im Verfahren nicht  feststellbar.

**False Positives:**

- `Tragfähige Anhaltspunkte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_TRAIN/133459.1`) (sent_id: `deanon_BFG_TRAIN/133459.1_323`)


Da das BFG, mangels auswertbarer Verfahrensunterlagen, zu keinem der lt. AP-Bericht Tz.4/2.)  im Jahr 2008 „auf Konto Schadensfälle“ verbuchten Vorgänge eine Vereinnahmung durch die  L-GmbH bzw. den Bf festzustellen vermag, fehlt es in Bezug auf den im AP-Bericht zu dieser  Textziffer erfassten Sachverhalt insgesamt an den Voraussetzungen für die Annahme einer  verdeckten Ausschüttung an den Bf.  Gemäß § 266 Abs. 4 BAO folgt das BFG unter diesen Umständen auch zu diesem Streitpunkt  dem Rechtsmittelvorbringen des Bf und geht davon aus, dass den im Rechenwerk 2008 der  L-GmbH als Schadensfälle verbuchten Beträgen tatsächlich Einnahmenausfälle zugrunde  liegen, welche die Annahme einer verdeckten Ausschüttung und Vorschreibung einer darauf  entfallenden KeSt an den Bf nicht rechtfertigen.

**False Positives:**

- `Gemäß` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)

**Example 72** (doc_id: `deanon_BFG_TRAIN/133588.1`) (sent_id: `deanon_BFG_TRAIN/133588.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) stellte am 10. April 2020 einen Antrag auf Zuerkennung der  Familienbeihilfe für seinen 1998 geborenen Sohn J. mit u.a. folgenden Angaben:   Für nachstehendes Kind beantrage ich die Familienbeihilfe:   x Zuerkennung  ab (TTMMJJJJ) 01042020   Grund: Beginn der Polizeischule   Derzeitige Wohnanschrift des Kindes: (Wohnanschrift des Bf.)   Kostentragung: Der Antragsteller trägt die Kosten für das Kind zu mehr als 50 %.

**False Positives:**

- `Kostentragung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_TRAIN/133721.1`) (sent_id: `deanon_BFG_TRAIN/133721.1_338`)


Der Vorwurf des Finanzamtes, dass sich die Bf. Scheinfirmen bedient habe, diese Finnen somit  keine Leistungen erbracht hätten, sei also auch physisch nicht haltbar.

**False Positives:**

- `Scheinfirmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_TRAIN/133721.1`) (sent_id: `deanon_BFG_TRAIN/133721.1_449`)


Als Beilagen zu einem Schreiben vom 29.11.2018 brachte die Bf. – vertreten von  zweiteSteuerberatungsgesellschaft – beim BFG ein:   Protokollsvermerk und gekürzte Urteilsausfertigung des Landesgerichtes für  Strafsachen Wien vom 2.9.2014 zu Zahl LGSzahl2:  enthaltend Freispruch des GesGf1 vom Vorwurf, er habe u.a. als handelsrechtlicher  Geschäftsführer, sohin als für die Wahrnehmung der abgabenrechtlichen Belange der  Bf. Verantwortlicher, einerseits bescheidmäßig festzusetzende Abgaben durch die  Abgabe u.a. unrichtiger Körperschaftsteuererklärungen für die Jahre 2005 bis 2009 und  andererseits selbst zu berechnende Abgaben, nämlich Kapitalertragsteuer durch die  Nichteinbehaltung und Nichtabfuhr jeweils eine Woche nach Zufluss der Kapitalerträge,  hinterzogen;

**False Positives:**

- `Verantwortlicher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 75** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_27`)


Abschließend sei dem Bf. Gelegenheit gegeben worden, einen Nachweis der  Gläubigergleichbehandlung zu übermitteln.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_TRAIN/133782.1`) (sent_id: `deanon_BFG_TRAIN/133782.1_35`)


Im konkreten Fall sei aber nicht die Bf  Steuerschuldnerin, sondern die B, die ihrer Verpflichtung aus dem Urteil des Obersten  Gerichtshofes sowie dem später vereinbarten Vergleich über die Zahlung der anteiligen  Lohnsteuer, nicht nachkomme.

**False Positives:**

- `Steuerschuldnerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_67`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Firma A als Gruppenträgerin ist, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_TRAIN/134371.1`) (sent_id: `deanon_BFG_TRAIN/134371.1_38`)


Seit dem Veranlagungsjahr 2009 ist die Bf. Gruppenträgerin einer Unternehmensgruppe (in der  Folge auch Konzern genannt) gemäß § 9 KStG 1988 als deren weitere Gruppenmitglieder die  Firma A (FN 111111), die Firma B (FN 222222), die Firma C (FN 333333), die Firma D (FN  444444), die Firma E (FN 555555) und die Firma F (FN 666666) agieren.

**False Positives:**

- `Gruppenträgerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_TRAIN/134371.1`) (sent_id: `deanon_BFG_TRAIN/134371.1_66`)


Dass die Bf. Teil einer Unternehmensgruppe als Gruppenträgerin mit den genannten weiteren  Gruppenmitgliedern ist, ergibt eine Einschau des Gerichtes in den elektronischen  Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_TRAIN/134395.1`) (sent_id: `deanon_BFG_TRAIN/134395.1_12`)


Dagegen wurde vom Bf Beschwerde erhoben und ausgeführt:  Der Bf war bis 2016 Wohnungseigentumspartner von Miteigentumsanteilen diverser  Liegenschaften.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_TRAIN/134395.1`) (sent_id: `deanon_BFG_TRAIN/134395.1_108`)


Durch die Tauschfiktion kommt es zur Aufdeckung von stillen Reserven bei den eingelegten  Wohnungen und hat zur Folge, dass beim Bf Erlöse in Höhe des gemeinen Wertes der in die  Kapitalgesellschaft eingebrachten Wohnungen anzusetzen sind (vgl. das hg.

**False Positives:**

- `Erlöse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_TRAIN/134424.1`) (sent_id: `deanon_BFG_TRAIN/134424.1_35`)


Mit Erklärung zur Arbeitnehmerveranlagung 2020 vom  21.01.2021 beantragte der Beschwerdeführer (Bf.) Aufwendungen für Personenversicherungen  (5.112,01 €) und Wohnraumschaffung (7.729,08 €) als Sonderausgaben sowie Reisekosten  (268,40 €) und außergewöhnliche Belastungen mit Selbstbehalt (insgesamt 3.296,09 €).

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_32`)


Jeder dieser, mit 29. November 2010 datierten „Bescheide“ zur St.Nr. 33 StNr2 enthält als  materiellen Bescheidadressaten die frühere Geschäftsherrin und die an ihr atypisch still  beteiligt Gewesenen, darunter den Bf. Weiters enthielten diese „Bescheide“ einen Hinweis auf  die Zustellfiktion gemäß § 101 BAO.

**False Positives:**

- `Weiters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_36`)


Jeder dieser, mit 29. November 2010 datierten „Bescheide“ zur St.Nr. 33 StNr1 enthält als  materiellen Bescheidadressaten die frühere Geschäftsherrin und die an ihr atypisch still  beteiligt Gewesenen, darunter den Bf. Weiters enhielten diese Bescheide einen Hinweis auf die  Zustellfiktion gemäß § 101 BAO.

**False Positives:**

- `Weiters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_66`)


„X_Zwei“: Mit Schreiben vom 15.12.2011 erhob der rechtsfreundlich vertretene  Bf. Berufung gegen den am 17.11.2011 zugestellten Zurückweisungsbescheid vom 8.11.2011 zu  Steuernummer StNr2 und begehrte dessen ersatzlose Behebung.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_74`)


„X_Eins“: Mit Schreiben vom 11.11.2011 erhob der rechtsfreundlich vertretene  Bf. Berufung gegen den am 13.10.2011 zugestellten Zurückweisungsbescheid vom 10.10.2011  zu Steuernummer StNr1 und begehrte dessen ersatzlose Behebung.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_TRAIN/134507.1`) (sent_id: `deanon_BFG_TRAIN/134507.1_35`)


In  der beim Finanzamt eingereichten Einkommensteuererklärung (Arbeitnehmerveranlagung) für  das Jahr 2013 machte der Bf. Werbungskosten und Sonderausgaben geltend und verwies  hinsichtlich der bei der ausländischen Arbeitgeberin erzielten Bezüge auf den Lohnausweis, in  welchem u.a. die laufenden Bezüge, die sonstigen Bezüge und unter „c) Zulagen und Zuschläge  (Angaben jeweils ohne Grundlohn):“ ein „Sonntags- und Feiertagszuschlag“ in Höhe von 419,00  CHF und ein „Nachtarbeitszuschlag (für zusammenhängende Arbeitszeiten von mind.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_TRAIN/134540.1`) (sent_id: `deanon_BFG_TRAIN/134540.1_70`)


An  dieser Adresse befinde sich seitdem auch der private Wohnsitz des Bf. Das Haus in Adr1,  bewohne die geschiedene Ehegattin sowie deren X Kinder.

**False Positives:**

- `Das Haus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_TRAIN/134540.1`) (sent_id: `deanon_BFG_TRAIN/134540.1_101`)


Es sei daher durchaus verständlich, dass der Bf Veranstaltungen als aktiver  Teilnehmer aufsuche, da dies durch Aufscheinen in der Startliste sowie durch intensiven  Kontakt mit dem restlichen Starterfeld eine hohe Publizitätswirkung bzw. direkten Zugang zu  potentiellen Kunden mit sich bringe.

**False Positives:**

- `Veranstaltungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_TRAIN/134540.1`) (sent_id: `deanon_BFG_TRAIN/134540.1_171`)


Bei den Teilnahmen an den Rallyeveranstaltungen handle es sich vielmehr um ein privates  Hobby bzw. eine Leidenschaft des Bf. Insgesamt betrachtet fehle der betriebliche  Veranlassungszusammenhang.

**False Positives:**

- `Insgesamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_TRAIN/134540.1`) (sent_id: `deanon_BFG_TRAIN/134540.1_264`)


1.2 „Dienstverhältnis“ zwischen dem Bf und seinem Sohn  Während des Streitzeitraumes 2010 bis 2014 stellte der Bf Lohnzettel für folgende Personen  aus:  Name Zeitraum Kz 210 (Bruttobezüge)   2010   F 01.01.2010 - 31.12.2010 15.127,00  S 01.01.2010 – 31.12.2010 4.620,00  To 01.01.2010 – 20.07.2010  10.09.2010 – 31.12.2010  1.701,28  907,02   2011   L 01.04.2011 – 31.12.2011 4.945,08  F 01.01.2011 – 15.07.2011 13.937,98  S 01.01.2011 – 31.12.2011 4.620,00  To 01.01.2011 – 30.06.2011 1.470,00   2012   L 01.01.2012 – 31.12.2012 5.250,00  S 01.01.2012 – 31.12.2012 4.620,00   2013   L 01.01.2013 – 31.12.2013 5.390,00  S 01.01.2013 – 15.07.2013  01.10.2013 – 31.12.2013  2.575,16  1.190,00   2014   L 01.01.2014 – 31.12.2014 5.530,00  S 01.01.2014 – 31.12.2014 4.900,00  16 von 30 Seite 17 von 30

**False Positives:**

- `Lohnzettel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_TRAIN/134630.1`) (sent_id: `deanon_BFG_TRAIN/134630.1_37`)


des Ermessens auf die wirtschaftliche Auswirkung für die Bf Rücksicht zu nehmen.

**False Positives:**

- `Rücksicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_TRAIN/134737.1`) (sent_id: `deanon_BFG_TRAIN/134737.1_30`)


Von 1.1.2016 bis 17.4.2016 habe der Bf Arbeitslosengeld bezogen.

**False Positives:**

- `Arbeitslosengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_TRAIN/134762.1`) (sent_id: `deanon_BFG_TRAIN/134762.1_28`)


Da damit dem – im Zuge des am 4.10.2021 abgehaltenen Erörterungstermines abgeänderten –  Beschwerdebegehren der Bf Rechnung getragen wurde, war die Beschwerde, die gemäß § 253  BAO auch als gegen die neuen Sachbescheide gerichtet gilt, gemäß § 261 Abs 1 lit a BAO  beschlussmäßig als gegenstandslos zu erklären.

**False Positives:**

- `Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_TRAIN/134786.1`) (sent_id: `deanon_BFG_TRAIN/134786.1_14`)


Zulassungskopie PKW Renault Megane lautend auf den Bf.  Formulare E9 für die Ehegattin des Bf. Y betreffend die Jahre 2015 bis 2017, die bestätigen,  dass diese Einkünfte von Null erzielt hat.

**False Positives:**

- `Formulare` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_TRAIN/134786.1`) (sent_id: `deanon_BFG_TRAIN/134786.1_128`)


Von einem Nachweis oder einer Glaubhaftmachung, dass den  Bf. Kosten für das Wohnen am Ort der Beschäftigung getroffen haben, kann aufgrund des  widersprüchlichen und durch keine aussagekräftigen Unterlagen belegten Vorbringens des Bf.  nicht ausgegangen werden.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_47`)


(seit 2007 mehrere Mieterwechsel) etc. vor Ort obliege der Bf.   Lt. vorgelegten dten.

**False Positives:**

- `Lt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_48`)


ESt-Bescheiden 2006-2010 hat die Bf Einkünfte aus Vermietung von  jährlich zw. ca. € 4.000 bis zuletzt ca. € 10.000 erzielt;

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `deanon_BFG_TRAIN/134926.1`) (sent_id: `deanon_BFG_TRAIN/134926.1_29`)


Neuerlich legte der Bf Wert auf die Feststellung, dass er seine private Lebensführung  vorwiegend durch Inanspruchnahme von Sachleistungen seines L+F-Betriebes bestreite  (Wohnversorgung, Heizung, Lebensmittel), hinsichtlich welcher er keiner Aufzeichnungspflicht  unterliege.

**False Positives:**

- `Wert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Herr Title Name Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fa0b9fa1`  
**Description:**
Captures person names following 'Herr', ensuring the full name is captured including suffixes and complex titles like 'Techn R OMedR'. Handles cases like 'Herr KindB'.

**Content:**
```
\bHerr\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+(?:di|de|der|von|zu|van|vanden|ter|ter\s+|da|della|del|des|dos|da\s+|di\s+|de\s+|der\s+|von\s+|zu\s+|van\s+|vanden\s+|ter\s+|ter\s+|da\s+|della\s+|del\s+|des\s+|dos\s+|da\s+))*[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s*,?\s*(?:LL\.B|LL\.M|LLB|MSc|MBA|B\.Sc|B\.A|B\.Ed|MA|BEd|Bakk\.\s+techn\.|Bakk\.\s+iur\.|Bakk\.\s+rer\.\s+\w+)*))(?=[\s,;\n]|$|\s+KG|\s+Bf\.|\s+\.\s*$|\s+\(|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1372 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/135338.1`) (sent_id: `deanon_BFG_TRAIN/135338.1_8`)


zuständige Herr Prokurist der Bank war auf Urlaub) konnte ich die Grunderwerbsteuer erst  etwas später überweisen.

**False Positives:**

- `Prokurist der Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/145175.1`) (sent_id: `deanon_BFG_TRAIN/145175.1_33`)


Herr Roberta de Francesco  hat in eigener Recherche noch herausgefunden, dass bei unbeschränkter  Schweizer Steuerpflicht nur ein sehr enger Kostenkatalog berücksichtigt werden könnte:  „Schuldzinsen, Beiträge in die Säule 2b und 3a, berufliche Weiterbildungskosten, bezahlte  Alimente, Unterstützungsbeiträge“ und bei beschränkter Steuerpflicht lediglich „Beiträge an  die Säule 2b und 3a sowie Wochenaufenthaltskosten“.

**False Positives:**

- `Roberta de Francesco ` — partial — gold is substring of pred: `Roberta de Francesco`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roberta de Francesco`(person)

</details>

---

## `Single Letter Name Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `391d7a7e`  
**Description:**
Captures anonymized single-letter names (e.g., 'M. Mayr') when preceded by titles or in specific contexts, ensuring the full title+initial is captured.

**Content:**
```
\b((?:Dr\.|Mag\.|KommR|StR|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|Ri\.|R\.\s+)([A-Z]\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+))(?=[\s,;\n]|$|\s+KG|\s+Bf\.|\s+\.\s*$|\s+\(|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 969 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/139927.1`) (sent_id: `deanon_BFG_TRAIN/139927.1_21`)


In der Begründung hielt die Behörde u.a. fest, dass Mag.M. Steuerberater, und als solcher,  Mitglied der Kammer der Steuerberater und Wirtschaftsprüfer, sei.

**False Positives:**

- `Mag.M. Steuerberater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Complainant Name Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66b7aa44`  
**Description:**
Captures person names following 'in der Beschwerdesache', handling multi-word names (e.g., 'di Francesco') and academic suffixes.

**Content:**
```
in\s+der\s+Beschwerdesache\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+(?:di|de|der|von|zu|van|vanden|ter|ter\s+|da|della|del|des|dos|da\s+|di\s+|de\s+|der\s+|von\s+|zu\s+|van\s+|vanden\s+|ter\s+|ter\s+|da\s+|della\s+|del\s+|des\s+|dos\s+|da\s+))*[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*(?:\s+(?:LL\.B\.\s+LL\.M\.|LL\.M\.\s+LL\.B\.|LL\.B\.\s+LLB|LLB|LL\.M\.|MSc|MBA|MAS|BA|B\.Sc|B\.A|B\.Ed|MA|BEd|Bakk\.\s+techn\.|Bakk\.\s+iur\.|Bakk\.\s+rer\.\s+\w+)*))(?=[\s,;\n]|$|\s+KG|\s+Bf\.|\s+\.\s*$|\s+\(|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Judge Name Context Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9f823d7f`  
**Description:**
Captures person names immediately following 'Richter' or 'Richterin', ensuring the full name including titles and suffixes is captured.

**Content:**
```
(?:Richter|Richterin)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00DC]+)*(?:\s*,\s*(?:BA|BSc|B\.Sc|B\.A\.|Bakk\. rer\. nat\.|Dipl\.|Ing\.|B\.Sc\.))?)(?=\s*,|\s+\d|\s+\.|\s+\)|\s+\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Organization Name as Person Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `20406141`  
**Description:**
Captures names following 'Fußballklub' or 'FC' which are misidentified as organizations but are person entities in this specific legal context (e.g., Verona Kemper).

**Content:**
```
(?:Fu\u00dfballklub|FC)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1988 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128894.1`) (sent_id: `deanon_BFG_TRAIN/128894.1_27`)


- Freiwillige Feuerwehr Ortsname-2 – Feuerwehrheurigen: handschriftlicher Vermerk durch die  Bf.: „Geschenkkorb EUR 30,-“  - FC Eigenname-3 – Einladung „Eigenname-1 5.0“ - Tombolaspende (via Mail): handschriftlicher  Vermerk durch die Bf.: „Bierkorb und Wurst“  - Männergesangsverein Ort-1 – Faschingsliedertafel: handschriftlicher Vermerk durch die Bf.:  „Erdbeer-Korb EUR 30,-, Geschenkkorb EUR 40,-“  - SC Ort-1 – Sportlerball: handschriftlicher Vermerk durch die Bf.: „Geschenkkorb“  - Kindermaskenball Ort-1: kein handschriftlicher Vermerk durch die Bf.

**False Positives:**

- `Eigenname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

