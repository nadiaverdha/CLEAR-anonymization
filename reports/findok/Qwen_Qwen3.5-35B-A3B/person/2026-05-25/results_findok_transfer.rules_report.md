# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (ris)

Generated on: 2026-05-25T15:13:23.856656

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
| Training documents | 1571 |
| Validation documents | 394 |
| Test documents | 21234 |
| Train sentences | 2935 |
| Validation sentences | 780 |
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
| Seeded From | findok |
| Seed Rule Count | 9 |
| New Rules Added | 7 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 185 |
| Phase1 Eval Sentences | 45 |
| Transfer Train Sentences | 2750 |
| Transfer Eval Sentences | 735 |
| Best Batch Idx | 8 |
| Best Batch F1 | 0.3276570757486788 |
| Best Rules Serialized | [{'id': 'cfc661f1', 'name': "Person after 'Schriftführer' (Court Clerk)", 'description': 'Captures the name of the court clerk mentioned after the title.', 'format': 'regex', 'content': '(?:Schriftführer)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*)', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '6e3cfc1d', 'name': "Person after 'fachkundiger Laienrichter'", 'description': 'Captures lay judges mentioned with their specific title.', 'format': 'regex', 'content': '(?:fachkundiger\\s+Laienrichter|fachkundige\\s+Laienrichterin)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*)', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '9b474dd4', 'name': 'Person after Judicial Role', 'description': 'Captures the full name (including title) appearing immediately after judicial role indicators, excluding the role text.', 'format': 'regex', 'content': '(?:die\\s+Richterin|der\\s+Richter|die\\s+Senatsvorsitzende)\\s+(?:Dr\\.(?:in)?|Mag\\.(?:Dr\\.)?|Univ\\.-Prof\\.(?:in)?|Priv\\.-Doz\\.(?:in)?|Hon\\.-Prof\\.(?:in)?|Ing\\.(?:Mag\\.)?|PhD|LL\\.M\\.|Bakk\\. rer\\. nat\\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR)?\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '79232d4e', 'name': "Person after 'Herrn' or 'Frau'", 'description': "Captures names preceded by 'Herrn' or 'Frau' in legal texts.", 'format': 'regex', 'content': '(?:Herrn|Frau)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 4, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '23bbc7f9', 'name': "Person after 'Gattin' or 'Kinder'", 'description': 'Captures names of spouses or children mentioned in legal contexts.', 'format': 'regex', 'content': '(?:und\\s+dessen\\s+Gattin|und\\s+deren\\s+Gattin|für\\s+seine\\s+Kinder|für\\s+das\\s+Kind|für\\s+ihre\\s+Tochter|für\\s+seinen\\s+Sohn)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4c8cbe8f', 'name': "Person after 'klagenden Partei' (Plaintiff)", 'description': "Captures the name of the plaintiff appearing after 'klagenden Partei', explicitly excluding company names and handling titles.", 'format': 'regex', 'content': 'klagenden\\s+Partei\\s+(?:[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*\\s+)?([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*(?:\\s*,\\s*[A-Z][a-z]+)*)(?!\\s+(?:GmbH|AG|Co\\.|Ltd|Inc|LLC|Rechtsanwalts?\\s+GmbH|Rechtsanwalts?\\s+AG))', 'priority': 12, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'e25ebe36', 'name': "Person in 'gegen' or 'von' context", 'description': "Captures names appearing after 'gegen' (against) or 'von' (of/from) in legal contexts, often without titles.", 'format': 'regex', 'content': '(?:gegen\\s+|von\\s+)([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '1fcb9e35', 'name': "Person after 'vertreten durch' (Refined)", 'description': "Captures names of legal representatives following 'vertreten durch', strictly excluding law firm names and ensuring the match ends before company suffixes or 'Rechtsanwalt'.", 'format': 'regex', 'content': 'vertreten\\s+durch\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)+)(?:\\s+Rechtsanwalt|\\s+Rechtsanwältin|\\s+GmbH|\\s+AG|\\s+KG|\\s+mbH|\\s+Co\\.?|\\s+Ltd|\\s+Inc|\\s+LLC|\\s+Stadtgemeinde|\\s+Gemeinde|\\s+Verein|\\s+Gesellschaft|\\s+Unternehmen|\\s+Firma|\\s+Werk|\\s+Bank|\\s+Pharma|\\s+Energie|\\s+Versand|\\s+Handel|\\s+Technik|\\s+Bau|\\s+Immobilien|\\s+Consulting|\\s+Management|\\s+Group|\\s+Holdings|\\s+Partners|\\s+&|\\.|$)', 'priority': 14, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'e45b5272', 'name': 'Person in List Context (Numbered)', 'description': 'Captures names in numbered lists (1., 2., 3.) or comma-separated lists where a name is followed by a number or comma, ensuring full name capture.', 'format': 'regex', 'content': '(?:^|,\\s+|\\d+\\.\\s+)([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)+)(?:,|\\s+\\d+\\.\\s+|\\s+und\\s+|\\s+und\\s+|\\s+\\.|$)', 'priority': 12, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '3e083246', 'name': "Person after 'gegen' or 'von' (Contextual)", 'description': "Captures names appearing after 'gegen' (against) or 'von' (of/from) in legal contexts, ensuring full name capture including 'von' prefixes and handling multi-word names.", 'format': 'regex', 'content': '(?:gegen\\s+|von\\s+)([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)+)(?:\\s+(?:von|vertreten\\s+durch))?\\s*(?!GmbH|AG|KG|mbH|Co\\.?|Ltd|Inc|LLC|\\s+GmbH|\\s+AG|\\s+KG|\\s+mbH|\\s+Co\\.?|\\s+Ltd|\\s+Inc|\\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\\.|$)', 'priority': 14, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '1182fd38', 'name': 'Person in Parenthetical Context', 'description': 'Captures names appearing within parentheses, often used for clarification or full names in legal texts.', 'format': 'regex', 'content': '\\(\\s*([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)*)\\s*\\)', 'priority': 11, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'ea02f06b', 'name': "Person after 'Partei' (Plaintiff/Defendant)", 'description': "Captures person names immediately following 'Partei' (party), explicitly excluding company names by checking for suffixes like GmbH, AG, KG, mbH, etc., and prefixes like Stadtgemeinde, Gemeinde, Verein. Requires at least two words or a known title pattern to avoid partial matches.", 'format': 'regex', 'content': '(?:der\\s+klagenden\\s+Partei\\s+|der\\s+beklagten\\s+Partei\\s+|der\\s+betreibenden\\s+Partei\\s+|der\\s+verpflichteten\\s+Partei\\s+|Partei\\s+|der\\s+Partei\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?:\\s+(?:von|vertreten\\s+durch))?\\s*(?!GmbH|AG|KG|mbH|Co\\.?|Ltd|Inc|LLC|\\s+GmbH|\\s+AG|\\s+KG|\\s+mbH|\\s+Co\\.?|\\s+Ltd|\\s+Inc|\\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\\.|$)', 'priority': 15, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'f96ee46b', 'name': 'Person with Complex Academic Titles', 'description': "Captures names preceded by complex German academic titles, ensuring the full name including the title is captured if it's a compound entity, or just the name if the title is separate. Handles specific complex suffixes like 'Bakk. rer. nat. Bakk. iur..net'.", 'format': 'regex', 'content': '(?:Dr\\.|Mag\\.|Prof\\.|Hon\\.-Prof\\.|Priv\\.-Doz\\.|Univ\\.-Prof\\.|Dipl\\.-Ing\\.|Ing\\.|Techn\\sR|StR|OStR|MR|\\u00d6kR|KommR|VetR|LLM|LLB|Bakk\\.\\s+rer\\.\\s+nat\\.|Bakk\\.\\s+techn\\.|Bakk\\.\\s+phil\\.|MSc|MA|BA|PhD|PhD\\s+OMedR|Mag\\.\\s+a|Dr\\.\\s+a|Hon\\.-Prof\\.\\s+in|Priv\\.-Doz\\.\\s+in|DDr\\.|RgR|MMM\\.?|MMM\\.\\s+a|DI\\.|MMag\\.|MMag\\.\\s+a|OSR\\.|KzlR\\.|MedR\\.|BEd\\.|Bakk\\.\\s+art\\.|Dr\\.\\s+in|Mag\\.\\s+in|Prof\\.\\s+in|Univ\\.-Prof\\.\\s+in|Priv\\.-Doz\\.\\s+in|Dipl\\.-Ing\\.\\s+in|Ing\\.\\s+in|Techn\\sR\\s+in|StR\\s+in|OStR\\s+in|MR\\s+in|\\u00d6kR\\s+in|KommR\\s+in|VetR\\s+in|LLM\\s+in|LLB\\s+in|Bakk\\.\\s+rer\\.\\s+nat\\.\\s+in|Bakk\\.\\s+techn\\.\\s+in|Bakk\\.\\s+phil\\.\\s+in|MSc\\s+in|MA\\s+in|BA\\s+in|PhD\\s+in|PhD\\s+OMedR\\s+in|Mag\\.\\s+a\\s+in|Dr\\.\\s+a\\s+in|Hon\\.-Prof\\.\\s+in\\s+in|Priv\\.-Doz\\.\\s+in\\s+in|DDr\\.\\s+in|RgR\\s+in|MMM\\.?\\s+in|MMM\\.\\s+a\\s+in|DI\\.\\s+in|MMag\\.\\s+in|MMag\\.\\s+a\\s+in|OSR\\.\\s+in|KzlR\\.\\s+in|MedR\\.\\s+in|BEd\\.\\s+in|Bakk\\.\\s+art\\.\\s+in)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)+)(?:\\s+von\\s+[A-Z][a-zäöüß]+)?(?:\\s+Bakk\\.\\s+rer\\.\\s+nat\\.\\s+Bakk\\.\\s+iur\\.\\.net)?\\s*(?!Inhaber|Bank|GmbH|AG|KG|mbH|Co\\.?|Ltd|Inc|LLC|\\s+Inhaber|\\s+Bank|\\s+GmbH|\\s+AG|\\s+KG|\\s+mbH|\\s+Co\\.?|\\s+Ltd|\\s+Inc|\\s+LLC|\\.|$)', 'priority': 15, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'd05f9629', 'name': "Person after 'geboren am' (Born On)", 'description': "Captures names appearing after 'geboren am' (born on) in legal texts, typically identifying the subject of the case. Excludes month names.", 'format': 'regex', 'content': 'geboren\\s+am\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?:\\s+in\\s+|\\s+zu\\s+|\\s+der\\s+|\\s+des\\s+|\\s+am\\s+|\\s+im\\s+|\\s+|\\.|$)', 'priority': 13, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '10c10e06', 'name': "Person after 'gegen' (Defendant)", 'description': "Captures person names appearing after 'gegen' (against) in legal contexts, ensuring full name capture and excluding company names. Prioritizes this for cases where the name follows 'gegen' directly.", 'format': 'regex', 'content': '(?:gegen\\s+|der\\s+gegen\\s+)(?:Herrn\\s+|Frau\\s+)?([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?:\\s+von\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)?\\s*(?!GmbH|AG|KG|mbH|Co\\.?|Ltd|Inc|LLC|\\s+GmbH|\\s+AG|\\s+KG|\\s+mbH|\\s+Co\\.?|\\s+Ltd|\\s+Inc|\\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\\.|$)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '0e41d831', 'name': 'Person in Legal Case Context', 'description': "Captures names appearing after 'Beschwerdesache', 'Strafsache', 'Rechtssache', or 'gegen' (against) in legal contexts, ensuring full name capture. Handles standalone surnames and multi-word names.", 'format': 'regex', 'content': '(?:in\\s+der\\s+(?:Beschwerdesache|Strafsache|Rechtssache|Verwaltungsstrafsache|Arbeitsrechtssache|Familienrechtssache)|der\\s+(?:Beschwerdesache|Strafsache|Rechtssache|Verwaltungsstrafsache|Arbeitsrechtssache|Familienrechtssache)|gegen\\s+)(?:Herrn\\s+|Frau\\s+)?([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?:\\s+von\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)?\\s*(?!GmbH|AG|KG|mbH|Co\\.?|Ltd|Inc|LLC|\\s+GmbH|\\s+AG|\\s+KG|\\s+mbH|\\s+Co\\.?|\\s+Ltd|\\s+Inc|\\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\\.|$)', 'priority': 12, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 94.4% |
| True Positives | 558 |
| False Positives | 1473 |
| False Negatives | 817 |
| Total Gold Entities | 1375 |
| Micro Precision | 27.5% |
| Micro Recall | 40.6% |
| Micro F1 | 32.8% |
| Macro F1 | 32.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Person after 'Partei' (Plaintiff/Defendant)` | 23.6% | 60.7% | 14.6% | 331 | 201 | 130 |
| `Person in List Context (Numbered)` | 19.2% | 37.8% | 12.9% | 468 | 177 | 291 |
| `Person with Complex Academic Titles` | 15.9% | 20.4% | 13.0% | 876 | 179 | 697 |
| `Person after 'klagenden Partei' (Plaintiff)` | 0.9% | 2.9% | 0.5% | 239 | 7 | 232 |
| `Person in Parenthetical Context` | 0.4% | 2.0% | 0.2% | 151 | 3 | 148 |
| `Person in 'gegen' or 'von' context` | 0.1% | 1.4% | 0.1% | 70 | 1 | 69 |
| `Person after 'gegen' or 'von' (Contextual)` | 0.1% | 1.3% | 0.1% | 79 | 1 | 78 |
| `Person after 'Schriftführer' (Court Clerk)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after 'fachkundiger Laienrichter'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after Judicial Role` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Person after 'Herrn' or 'Frau'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after 'Gattin' or 'Kinder'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after 'vertreten durch' (Refined)` | 0.0% | 0.0% | 0.0% | 84 | 0 | 84 |
| `Person after 'geboren am' (Born On)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after 'gegen' (Defendant)` | 0.0% | 0.0% | 0.0% | 61 | 0 | 61 |
| `Person in Legal Case Context` | 0.0% | 0.0% | 0.0% | 61 | 0 | 61 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Person after 'Partei' (Plaintiff/Defendant)`

**F1:** 0.236 | **Precision:** 0.607 | **Recall:** 0.146  

**Format:** `regex`  
**Rule ID:** `ea02f06b`  
**Description:**
Captures person names immediately following 'Partei' (party), explicitly excluding company names by checking for suffixes like GmbH, AG, KG, mbH, etc., and prefixes like Stadtgemeinde, Gemeinde, Verein. Requires at least two words or a known title pattern to avoid partial matches.

**Content:**
```
(?:der\s+klagenden\s+Partei\s+|der\s+beklagten\s+Partei\s+|der\s+betreibenden\s+Partei\s+|der\s+verpflichteten\s+Partei\s+|Partei\s+|der\s+Partei\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+(?:von|vertreten\s+durch))?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.607 | 0.146 | 0.236 | 331 | 201 | 130 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 201 | 130 | 1174 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karin Meiwaldt` | `Karin Meiwaldt` |

**Missed by this rule (FN):**

- `Katharina Tomandl, MA` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chen Mestwerdt` | `Chen Mestwerdt` |
| `Roman Eschenweck` | `Roman Eschenweck` |

**Example 2** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Ingolf Grimpe` | `Ingolf Grimpe` |

**Missed by this rule (FN):**

- `Dersudheim Digital GmbH` (organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ursula Antoniadis` | `Ursula Antoniadis` |

**Missed by this rule (FN):**

- `Skrzypczik + Duchscherer Digital AG` (organisation)
- `Adelheid Lochmaier` (person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Elina Woyte` | `Elina Woyte` |

**Missed by this rule (FN):**

- `DI Fabian Reifrath` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Katharina Tomandl` — partial — pred is substring of gold: `Katharina Tomandl, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

**False Positives:**

- `Juri Petraschk` — partial — pred is substring of gold: `Juri Petraschk, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Juri Petraschk, Bakk. iur.`(person)
- `Mag. Dominik Riewert`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Diethard Eisenlöffel` — partial — pred is substring of gold: `Diethard Eisenlöffel, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Mur Kraftalheim Holding Gmb` — partial — pred is substring of gold: `Mur Kraftalheim Holding GmbH`
- `Nexstein Textil Gmb` — partial — pred is substring of gold: `Nexstein Textil GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Alsteinost Gmb` — partial — pred is substring of gold: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

</details>

---

## `Person in List Context (Numbered)`

**F1:** 0.192 | **Precision:** 0.378 | **Recall:** 0.129  

**Format:** `regex`  
**Rule ID:** `e45b5272`  
**Description:**
Captures names in numbered lists (1., 2., 3.) or comma-separated lists where a name is followed by a number or comma, ensuring full name capture.

**Content:**
```
(?:^|,\s+|\d+\.\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:,|\s+\d+\.\s+|\s+und\s+|\s+und\s+|\s+\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.378 | 0.129 | 0.192 | 468 | 177 | 291 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 177 | 291 | 1183 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Gerald Zacharie` | `Gerald Zacharie` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)
- `Mur Kraftalheim Holding GmbH` (organisation)
- `Nexstein Textil GmbH` (organisation)
- `Dipl.-Ing. Lynn Forkarth` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Adelheid Lochmaier` | `Adelheid Lochmaier` |

**Missed by this rule (FN):**

- `Skrzypczik + Duchscherer Digital AG` (organisation)
- `Ursula Antoniadis` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `Isidor Janofske` | `Isidor Janofske` |

**Missed by this rule (FN):**

- `Wolfram Fritzsche` (person)
- `VetR Lukas Dickhaus` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Krentzel` | `Janis Krentzel` |
| `Julian Grebener` | `Julian Grebener` |

**Missed by this rule (FN):**

- `Kotschenreuther u. Abele Planung GmbH` (organisation)
- `Mittel Keltal GmbH` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Severin Simaitis` | `Severin Simaitis` |
| `Nepomuk Sprinzl` | `Nepomuk Sprinzl` |

**Missed by this rule (FN):**

- `20. November` (date)
- `8. Juli 1967` (date)
- `17. November` (date)
- `11. September` (date)
- `Mag. Miklos Stiening` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Zarin Steevens, geboren 26. Mai 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Dorothea Akkaya, und des Antragsgegners Mirko Hamidi, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.

**False Positives:**

- `Russische Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zarin Steevens`(person)
- `26. Mai`(date)
- `Dorothea Akkaya`(person)
- `Mirko Hamidi`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_6`)


Die Mutter und die Kinder sind Staatsangehörige der Russischen Föderation und als Asylwerber im Inland aufhältig.

**False Positives:**

- `Die Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Vereinigtes Königreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_15`)


Ihr Geschäftsführer und ein von ihr beantragter Zeuge seien in Linz wohnhaft;

**False Positives:**

- `Ihr Geschäftsführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_47`)


Das Objekt, auf das sich der Rechtsstreit bezieht, ist in Wien gelegen, sodass auch ein Ortsaugenschein sowie die Befundaufnahme durch Sachverständige in Wien durchzuführen sind.

**False Positives:**

- `Das Objekt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Person with Complex Academic Titles`

**F1:** 0.159 | **Precision:** 0.204 | **Recall:** 0.130  

**Format:** `regex`  
**Rule ID:** `f96ee46b`  
**Description:**
Captures names preceded by complex German academic titles, ensuring the full name including the title is captured if it's a compound entity, or just the name if the title is separate. Handles specific complex suffixes like 'Bakk. rer. nat. Bakk. iur..net'.

**Content:**
```
(?:Dr\.|Mag\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Dipl\.-Ing\.|Ing\.|Techn\sR|StR|OStR|MR|\u00d6kR|KommR|VetR|LLM|LLB|Bakk\.\s+rer\.\s+nat\.|Bakk\.\s+techn\.|Bakk\.\s+phil\.|MSc|MA|BA|PhD|PhD\s+OMedR|Mag\.\s+a|Dr\.\s+a|Hon\.-Prof\.\s+in|Priv\.-Doz\.\s+in|DDr\.|RgR|MMM\.?|MMM\.\s+a|DI\.|MMag\.|MMag\.\s+a|OSR\.|KzlR\.|MedR\.|BEd\.|Bakk\.\s+art\.|Dr\.\s+in|Mag\.\s+in|Prof\.\s+in|Univ\.-Prof\.\s+in|Priv\.-Doz\.\s+in|Dipl\.-Ing\.\s+in|Ing\.\s+in|Techn\sR\s+in|StR\s+in|OStR\s+in|MR\s+in|\u00d6kR\s+in|KommR\s+in|VetR\s+in|LLM\s+in|LLB\s+in|Bakk\.\s+rer\.\s+nat\.\s+in|Bakk\.\s+techn\.\s+in|Bakk\.\s+phil\.\s+in|MSc\s+in|MA\s+in|BA\s+in|PhD\s+in|PhD\s+OMedR\s+in|Mag\.\s+a\s+in|Dr\.\s+a\s+in|Hon\.-Prof\.\s+in\s+in|Priv\.-Doz\.\s+in\s+in|DDr\.\s+in|RgR\s+in|MMM\.?\s+in|MMM\.\s+a\s+in|DI\.\s+in|MMag\.\s+in|MMag\.\s+a\s+in|OSR\.\s+in|KzlR\.\s+in|MedR\.\s+in|BEd\.\s+in|Bakk\.\s+art\.\s+in)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+von\s+[A-Z][a-zäöüß]+)?(?:\s+Bakk\.\s+rer\.\s+nat\.\s+Bakk\.\s+iur\.\.net)?\s*(?!Inhaber|Bank|GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+Inhaber|\s+Bank|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.204 | 0.130 | 0.159 | 876 | 179 | 697 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 179 | 697 | 1196 |

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

**Example 1** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Gregor Ruemmel` | `OStR Gregor Ruemmel` |

**Missed by this rule (FN):**

- `Sten und Stöwer Wind GmbH` (organisation)
- `OMedR Torsten Münchmeyer` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `PhD Ignaz Nardelli` | `PhD Ignaz Nardelli` |

**Missed by this rule (FN):**

- `Diethard Eisenlöffel, Bakk. phil.` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Lynn Forkarth` | `Dipl.-Ing. Lynn Forkarth` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)
- `Mur Kraftalheim Holding GmbH` (organisation)
- `Gerald Zacharie` (person)
- `Nexstein Textil GmbH` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Adam Kratki` | `Mag. Adam Kratki` |

**Missed by this rule (FN):**

- `Alsteinost GmbH` (organisation)
- `Anna Kisaoglu, Bakk. iur.` (person)

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

**Example 2** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

**False Positives:**

- `Priv.-Doz. Sven Egerth` — partial — pred is substring of gold: `ÖkR Priv.-Doz. Sven Egerth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Priv.-Doz. Sven Egerth`(person)
- `3. Mai`(date)
- `Bezirksgericht Graz`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mag. Alexander Rimser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `OStR Gregor Ruemmel`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Dr. Carl Benkhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

</details>

---

## `Person after 'klagenden Partei' (Plaintiff)`

**F1:** 0.009 | **Precision:** 0.029 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `4c8cbe8f`  
**Description:**
Captures the name of the plaintiff appearing after 'klagenden Partei', explicitly excluding company names and handling titles.

**Content:**
```
klagenden\s+Partei\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s*,\s*[A-Z][a-z]+)*)(?!\s+(?:GmbH|AG|Co\.|Ltd|Inc|LLC|Rechtsanwalts?\s+GmbH|Rechtsanwalts?\s+AG))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.029 | 0.005 | 0.009 | 239 | 7 | 232 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 7 | 232 | 1368 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ostrovska` | `Ostrovska` |

**Example 1** (doc_id: `deanon_TRAIN/1Ob186_12b`) (sent_id: `deanon_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Pasqualini, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Denzlein, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Pasqualini` | `Pasqualini` |

**Missed by this rule (FN):**

- `Denzlein` (person)

**Example 2** (doc_id: `deanon_TRAIN/2Ob181_10x`) (sent_id: `deanon_TRAIN/2Ob181_10x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Gertrude Ptak, vertreten durch Dr. Bertram Broesigke und Dr. Wolfgang Broesigke, Rechtsanwälte in Wien, gegen die beklagte Partei Josef Schindelmeißer, vertreten durch den Sachwalter Dr. Helmut Heiger, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 15. Juni 2010, GZ 41 R 130/10m-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Ptak` | `Ptak` |

**Missed by this rule (FN):**

- `Schindelmeißer` (person)

**Example 3** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Thomas Papakonstantinou, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagten Parteien 1. Matthias Graafmann, und 2.

| Predicted | Gold |
|---|---|
| `Papakonstantinou` | `Papakonstantinou` |

**Missed by this rule (FN):**

- `Graafmann` (person)

**Example 4** (doc_id: `deanon_TRAIN/3Ob128_10k`) (sent_id: `deanon_TRAIN/3Ob128_10k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte und Hofrätinnen Hon.-Prof. Dr. Sailer, Dr. Lovrek, Dr. Jensik und Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Nadja Spangler, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagte Partei Sascha Heckert, vertreten durch Dr. Andreas König, Dr. Andreas Ermacora und Dr. Barbara Lässer, Rechtsanwälte in Innsbruck, wegen 137.146,60 EUR sA und Feststellung (Gesamtstreitwert 157.146,60 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2010, GZ 6 R 28/10w-44, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 30. Oktober 2009, GZ 7 Cg 117/07b-40, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Spangler` | `Spangler` |

**Missed by this rule (FN):**

- `Sascha Heckert` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Meiwaldt` — partial — pred is substring of gold: `Karin Meiwaldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

**False Positives:**

- `Mestwerdt, Slowenien` — positional overlap with gold: `Chen Mestwerdt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Chen Mestwerdt`(person)
- `Roman Eschenweck`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

**False Positives:**

- `Petraschk, Bakk` — partial — pred is substring of gold: `Juri Petraschk, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Juri Petraschk, Bakk. iur.`(person)
- `Mag. Dominik Riewert`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Sten` — partial — pred is substring of gold: `Sten und Stöwer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `OStR Gregor Ruemmel`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Ph` — partial — pred is substring of gold: `PhD Ignaz Nardelli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Person in Parenthetical Context`

**F1:** 0.004 | **Precision:** 0.020 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `1182fd38`  
**Description:**
Captures names appearing within parentheses, often used for clarification or full names in legal texts.

**Content:**
```
\(\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.020 | 0.002 | 0.004 | 151 | 3 | 148 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 148 | 1354 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_5`)


Die Entscheidungen der Vorinstanzen werden dahin abgeändert, dass der Beschluss des Erstgerichts lautet: „1. Dem minderjährigen Laurin Bihrenbrodt, und der minderjährigen Dominik Aldirmaz, wird vom 1. Jänner 2024 bis 31. Dezember 2028 gemäß §§ 3, 4 Z 1 UVG ein monatlicher Unterhaltsvorschuss in Höhe von 305 EUR ( Silvius Berwolf ) und 270 EUR ( Karlheinz Arntzen ), höchstens jedoch in der Höhe des jeweiligen Richtsatzes für pensionsberechtigte Halbwaisen gemäß § 293 Abs 1 lit c, sublit bb erster Fall, § 108f ASVG gewährt.

| Predicted | Gold |
|---|---|
| `Silvius Berwolf` | `Silvius Berwolf` |
| `Karlheinz Arntzen` | `Karlheinz Arntzen` |

**Missed by this rule (FN):**

- `Laurin Bihrenbrodt` (person)
- `Dominik Aldirmaz` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_17`)


[4] Mit Bescheiden vom 18. Jänner 2017 ( Silvia Balßuweit ) und 23. Juli 2018 ( OMedR Ilse Albertsernst ) wurde den Kindern ebenfalls der Status des Asylberechtigten als Familienangehörige (ihrer Mutter) zuerkannt.

| Predicted | Gold |
|---|---|
| `Silvia Balßuweit` | `Silvia Balßuweit` |

**Missed by this rule (FN):**

- `OMedR Ilse Albertsernst` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_7`)


Der Antragsgegner wohnt in der Russischen Förderation (Tschetschenien).

**False Positives:**

- `Tschetschenien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_46`)


Die weiteren acht Personen, deren Vernehmung beantragt wurde, haben ihren Wohnsitz in Wien bzw der Umgebung von Wien (Maria Enzersdorf).

**False Positives:**

- `Maria Enzersdorf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_104`)


Der Wegfall der Anmerkung (aus welchem Grund auch immer) führt demnach nicht zum Erlöschen des Eigentums, weil eine Anmerkung nicht zur Veränderung (Aufhebung) dinglicher Rechte führen kann.

**False Positives:**

- `Aufhebung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_62`)


Das Wohnsitzkriterium wirkt sich somit eher auf Wanderarbeitnehmer (Grenzgänger) als auf österreichische Arbeitnehmer und ihre Familienangehörigen, die ihren Wohnsitz meistens im Inland haben, benachteiligend aus, was den Tatbestand der mittelbaren Diskriminierung erfüllt (Felten/NeumayraaO iFamZ 2010, 169).

**False Positives:**

- `Grenzgänger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_73`)


4. Bei Berücksichtigung der dargelegten Erwägungen gelangt der erkennende Senat zu dem Ergebnis, dass die Beschränkung auf den gewöhnlichen Aufenthalt des Kindes im Inland gemäß § 2 Abs 1 UVG im vorliegenden Fall mit der Freizügigkeitsverordnung (EU) 492/2011 nicht vereinbar ist und die Minderjährigen daher aus der Rechtsstellung ihrer Mutter als Wanderarbeitnehmer (Grenzgängerin), die in Österreich einer Beschäftigung über der Geringfügigkeitsgrenze nachgeht und mit ihren beiden unterhaltsberechtigten Kindern in einem anderen Mitgliedstaat (Slowakei) lebt, mit Recht einen Anspruch auf Gewährung österreichischer Unterhaltsvorschüsse ableiten können.

**False Positives:**

- `Grenzgängerin` — no gold match — likely missing annotation
- `Slowakei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Person after 'vertreten durch' (Refined)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1fcb9e35`  
**Description:**
Captures names of legal representatives following 'vertreten durch', strictly excluding law firm names and ensuring the match ends before company suffixes or 'Rechtsanwalt'.

**Content:**
```
vertreten\s+durch\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+Rechtsanwalt|\s+Rechtsanwältin|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|\s+Stadtgemeinde|\s+Gemeinde|\s+Verein|\s+Gesellschaft|\s+Unternehmen|\s+Firma|\s+Werk|\s+Bank|\s+Pharma|\s+Energie|\s+Versand|\s+Handel|\s+Technik|\s+Bau|\s+Immobilien|\s+Consulting|\s+Management|\s+Group|\s+Holdings|\s+Partners|\s+&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 84 | 0 | 84 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 84 | 1357 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Skribe Rechtsanwälte` — no gold match — likely missing annotation

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

- `Lederer Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kotschenreuther u. Abele Planung GmbH`(organisation)
- `Janis Krentzel`(person)
- `Mittel Keltal GmbH`(organisation)
- `Julian Grebener`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts` — no gold match — likely missing annotation

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

## `Person after 'gegen' or 'von' (Contextual)`

**F1:** 0.001 | **Precision:** 0.013 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `3e083246`  
**Description:**
Captures names appearing after 'gegen' (against) or 'von' (of/from) in legal contexts, ensuring full name capture including 'von' prefixes and handling multi-word names.

**Content:**
```
(?:gegen\s+|von\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+(?:von|vertreten\s+durch))?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.013 | 0.001 | 0.001 | 79 | 1 | 78 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 78 | 1266 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_10`)


In dem vor dem Oberlandesgericht Köln geführten Pflegschaftsverfahren vereinbarten die Eltern am 8. Mai 2018 die Beibehaltung des gemeinsamen Obsorge- und Aufenthaltsbestimmungsrechts für beide Kinder, wobei der Lebensmittelpunkt von Heinrich Debbert beim Vater (der inzwischen ebenfalls nach Wien übersiedelt war) und für Ashley Frohnsdorfer eine wöchentlich abwechselnde Betreuung festgelegt wurde.

| Predicted | Gold |
|---|---|
| `Heinrich Debbert` | `Heinrich Debbert` |

**Missed by this rule (FN):**

- `Ashley Frohnsdorfer` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob30_19p`) (sent_id: `deanon_TRAIN/10Ob30_19p_54`)


Das Kind hätte in dieser besonderen Konstellation bereits in seinem Antrag auf Gewährung von Unterhaltsvorschüssen Tatsachen geltend machen müssen, die den Schluss auf die Anspannbarkeit des Unterhaltsschuldners zulassen, weil nach der Rückkehr der Mutter nach Rumänien das dem Titel zugrundegelegte Einkommen evidentermaßen nicht mehr erzielbar war (vgl 10 Ob 33/17a).

**False Positives:**

- `Unterhaltsvorschüssen Tatsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 2** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Szczech vertretenen Inn Triconal Holding GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Susanna Szczech` — partial — gold is substring of pred: `Szczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Szczech`(person)
- `Inn Triconal Holding GesmbH`(organisation)
- `Co KG`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 4** (doc_id: `deanon_TRAIN/11Os49_13k`) (sent_id: `deanon_TRAIN/11Os49_13k_3`)


Kopf Der Oberste Gerichtshof hat am 16. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Wancata als Schriftführer, in der Strafsache gegen Michael Dämering wegen des Verbrechens des schweren Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 4, 129 Z 1 StGB, AZ 13 Hv 23/13d des Landesgerichts Wels, über die von der Generalprokuratur gegen den gemäß § 494a StPO gefassten Beschluss dieses Gerichts vom 20. März 2012, ON 13 der Hv-Akten, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Michael Dämering` — partial — gold is substring of pred: `Dämering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dämering`(person)

</details>

---

## `Person in 'gegen' or 'von' context`

**F1:** 0.001 | **Precision:** 0.014 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `e25ebe36`  
**Description:**
Captures names appearing after 'gegen' (against) or 'von' (of/from) in legal contexts, often without titles.

**Content:**
```
(?:gegen\s+|von\s+)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.014 | 0.001 | 0.001 | 70 | 1 | 69 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 69 | 1218 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_10`)


In dem vor dem Oberlandesgericht Köln geführten Pflegschaftsverfahren vereinbarten die Eltern am 8. Mai 2018 die Beibehaltung des gemeinsamen Obsorge- und Aufenthaltsbestimmungsrechts für beide Kinder, wobei der Lebensmittelpunkt von Heinrich Debbert beim Vater (der inzwischen ebenfalls nach Wien übersiedelt war) und für Ashley Frohnsdorfer eine wöchentlich abwechselnde Betreuung festgelegt wurde.

| Predicted | Gold |
|---|---|
| `Heinrich Debbert` | `Heinrich Debbert` |

**Missed by this rule (FN):**

- `Ashley Frohnsdorfer` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 1** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Szczech vertretenen Inn Triconal Holding GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Susanna Szczech` — partial — gold is substring of pred: `Szczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Szczech`(person)
- `Inn Triconal Holding GesmbH`(organisation)
- `Co KG`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 3** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 4** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

</details>

---

## `Person after 'gegen' (Defendant)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `10c10e06`  
**Description:**
Captures person names appearing after 'gegen' (against) in legal contexts, ensuring full name capture and excluding company names. Prioritizes this for cases where the name follows 'gegen' directly.

**Content:**
```
(?:gegen\s+|der\s+gegen\s+)(?:Herrn\s+|Frau\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 61 | 0 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 61 | 1219 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 1** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 2** (doc_id: `deanon_TRAIN/11Os49_13k`) (sent_id: `deanon_TRAIN/11Os49_13k_3`)


Kopf Der Oberste Gerichtshof hat am 16. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Wancata als Schriftführer, in der Strafsache gegen Michael Dämering wegen des Verbrechens des schweren Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 4, 129 Z 1 StGB, AZ 13 Hv 23/13d des Landesgerichts Wels, über die von der Generalprokuratur gegen den gemäß § 494a StPO gefassten Beschluss dieses Gerichts vom 20. März 2012, ON 13 der Hv-Akten, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Michael Dämering` — partial — gold is substring of pred: `Dämering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dämering`(person)

**Example 3** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 4** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

</details>

---

## `Person in Legal Case Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0e41d831`  
**Description:**
Captures names appearing after 'Beschwerdesache', 'Strafsache', 'Rechtssache', or 'gegen' (against) in legal contexts, ensuring full name capture. Handles standalone surnames and multi-word names.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Strafsache|Rechtssache|Verwaltungsstrafsache|Arbeitsrechtssache|Familienrechtssache)|der\s+(?:Beschwerdesache|Strafsache|Rechtssache|Verwaltungsstrafsache|Arbeitsrechtssache|Familienrechtssache)|gegen\s+)(?:Herrn\s+|Frau\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 61 | 0 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 61 | 1219 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 1** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 2** (doc_id: `deanon_TRAIN/11Os49_13k`) (sent_id: `deanon_TRAIN/11Os49_13k_3`)


Kopf Der Oberste Gerichtshof hat am 16. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Wancata als Schriftführer, in der Strafsache gegen Michael Dämering wegen des Verbrechens des schweren Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 4, 129 Z 1 StGB, AZ 13 Hv 23/13d des Landesgerichts Wels, über die von der Generalprokuratur gegen den gemäß § 494a StPO gefassten Beschluss dieses Gerichts vom 20. März 2012, ON 13 der Hv-Akten, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Michael Dämering` — partial — gold is substring of pred: `Dämering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dämering`(person)

**Example 3** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 4** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

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

## `Person after 'geboren am' (Born On)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d05f9629`  
**Description:**
Captures names appearing after 'geboren am' (born on) in legal texts, typically identifying the subject of the case. Excludes month names.

**Content:**
```
geboren\s+am\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+in\s+|\s+zu\s+|\s+der\s+|\s+des\s+|\s+am\s+|\s+im\s+|\s+|\.|$)
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

## `Person after 'Partei' (Plaintiff/Defendant)`

**F1:** 0.236 | **Precision:** 0.607 | **Recall:** 0.146  

**Format:** `regex`  
**Rule ID:** `ea02f06b`  
**Description:**
Captures person names immediately following 'Partei' (party), explicitly excluding company names by checking for suffixes like GmbH, AG, KG, mbH, etc., and prefixes like Stadtgemeinde, Gemeinde, Verein. Requires at least two words or a known title pattern to avoid partial matches.

**Content:**
```
(?:der\s+klagenden\s+Partei\s+|der\s+beklagten\s+Partei\s+|der\s+betreibenden\s+Partei\s+|der\s+verpflichteten\s+Partei\s+|Partei\s+|der\s+Partei\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+(?:von|vertreten\s+durch))?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.607 | 0.146 | 0.236 | 331 | 201 | 130 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 201 | 130 | 1174 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karin Meiwaldt` | `Karin Meiwaldt` |

**Missed by this rule (FN):**

- `Katharina Tomandl, MA` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chen Mestwerdt` | `Chen Mestwerdt` |
| `Roman Eschenweck` | `Roman Eschenweck` |

**Example 2** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Ingolf Grimpe` | `Ingolf Grimpe` |

**Missed by this rule (FN):**

- `Dersudheim Digital GmbH` (organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ursula Antoniadis` | `Ursula Antoniadis` |

**Missed by this rule (FN):**

- `Skrzypczik + Duchscherer Digital AG` (organisation)
- `Adelheid Lochmaier` (person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Elina Woyte` | `Elina Woyte` |

**Missed by this rule (FN):**

- `DI Fabian Reifrath` (person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Corinna Elfe` | `Corinna Elfe` |

**Missed by this rule (FN):**

- `Jonasgasse 71, 4760 Weeg, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/10Ob11_15p`) (sent_id: `deanon_TRAIN/10Ob11_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte und Hofrätinnen Univ.-Prof. Dr. Neumayr, Dr. Schramm, Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Viktoria Hornburg, vertreten durch Dr. Walter Vasoll und Mag. Marion Vasoll, Rechtsanwälte in Hermagor, gegen die beklagte Partei Mercedes Jungschlaeger, vertreten durch Dr. Thomas Romauch, Rechtsanwalt in Wien, wegen Feststellung und Einwilligung (6.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 4. Dezember 2014, GZ 3 R 169/14h-14, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Hermagor vom 9. August 2014, GZ 1 C 563/13b-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Viktoria Hornburg` | `Viktoria Hornburg` |
| `Mercedes Jungschlaeger` | `Mercedes Jungschlaeger` |

**Example 7** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `Wolfram Fritzsche` | `Wolfram Fritzsche` |

**Missed by this rule (FN):**

- `Isidor Janofske` (person)
- `VetR Lukas Dickhaus` (person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Zoltan Alfermann, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei DonauFurtostBildung GmbH, KzlR Noah Christansen, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Zoltan Alfermann` | `Zoltan Alfermann` |

**Missed by this rule (FN):**

- `DonauFurtostBildung GmbH` (organisation)
- `KzlR Noah Christansen` (person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Miranda Klagemann` | `Miranda Klagemann` |

**Missed by this rule (FN):**

- `DI Adolf Kowallek` (person)
- `Ing. Janis Grottian` (person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Walter Gritzmacher` | `Walter Gritzmacher` |

**Missed by this rule (FN):**

- `Dr. Ariadne Graspointner` (person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob16_16z`) (sent_id: `deanon_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Josepha Mikolajetz, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Erhard Arslanboga, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Josepha Mikolajetz` | `Josepha Mikolajetz` |
| `Erhard Arslanboga` | `Erhard Arslanboga` |

**Example 12** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ernestine Feifel` | `Ernestine Feifel` |
| `Jean Kandziora` | `Jean Kandziora` |

**Missed by this rule (FN):**

- `Co KG` (organisation)

**Example 13** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `Ignaz Jungmichel` | `Ignaz Jungmichel` |

**Missed by this rule (FN):**

- `TalAlvalRobotik AG` (organisation)
- `Delila Leiteritz` (person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Calvin Amorelli` | `Calvin Amorelli` |

**Missed by this rule (FN):**

- `Strathewerd u. Niemetz Metall GmbH` (organisation)
- `Dolores Chatzakis` (person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Arielle Schallmair, gegen die beklagte Partei Dr. Daisy Nagelkrämer, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arielle Schallmair` | `Arielle Schallmair` |

**Missed by this rule (FN):**

- `Dr. Daisy Nagelkrämer` (person)

**Example 16** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_5`)


Dr. Torsten Classe, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Jaqueline Ratzenböck, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jaqueline Ratzenböck` | `Jaqueline Ratzenböck` |

**Missed by this rule (FN):**

- `Dr. Torsten Classe` (person)

**Example 17** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Samantha Neunteufl` | `Samantha Neunteufl` |

**Example 18** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Levi Adelwart` | `Levi Adelwart` |

**Missed by this rule (FN):**

- `Dr. Penelope Piephans` (person)
- `Valkraftfen-Analyse Aktiengesellschaft` (organisation)

**Example 19** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Laurin Aichhorn` | `Laurin Aichhorn` |

**Missed by this rule (FN):**

- `KommR Franz Kubank` (person)
- `Timothy Schulmeister` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 20** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Nordkamp, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Belohlawek KI Bank AG, Denis Nakonzer, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Manfred Nordkamp` | `Manfred Nordkamp` |

**Missed by this rule (FN):**

- `Belohlawek KI` (organisation)
- `Denis Nakonzer` (person)

**Example 21** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Prof. Virgil Pahlow, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Dominika Föcks, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Dominika Föcks` | `Dominika Föcks` |

**Missed by this rule (FN):**

- `Prof. Virgil Pahlow` (person)

**Example 22** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tamara Schweinfurth, vertreten durch Dr. Wolfgang Maurer, Rechtsanwalt in Golling, gegen die beklagte Partei Noah Vlatten, BEd, vertreten durch Dr. Peter Perner, Rechtsanwalt in Salzburg, wegen 10.895,18 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 19. Mai 2015, GZ 22 R 126/15f-21, mit dem das Urteil des Bezirksgerichts Salzburg vom 5. März 2015, GZ 32 C 407/14x-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Tamara Schweinfurth` | `Tamara Schweinfurth` |

**Missed by this rule (FN):**

- `Noah Vlatten, BEd` (person)

**Example 23** (doc_id: `deanon_TRAIN/1Ob186_16h`) (sent_id: `deanon_TRAIN/1Ob186_16h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Anton Luehne, Deutschland, vertreten durch die Dr. Paul Kreuzberger, Mag. Markus Stranimaier & Mag. Manuel Vogler – Rechtsanwälte & Strafverteidiger OG, Bischofshofen, gegen die beklagten Parteien 1. OMedR Angelina Badenius und 2. Hon.-Prof. Miroslav Roelle, vertreten durch Dr. Raimund Danner, Rechtsanwalt in Salzburg, wegen 18.383,81 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. August 2016, GZ 4 R 107/16g-45, mit dem das Teilzwischenurteil des Landesgerichts Salzburg vom 8. Juni 2016, GZ 5 Cg 125/14z-41, mit einer Maßgabe bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Anton Luehne` | `Anton Luehne` |

**Missed by this rule (FN):**

- `OMedR Angelina Badenius` (person)
- `Hon.-Prof. Miroslav Roelle` (person)

**Example 24** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Yelec Dangelmeier` | `Yelec Dangelmeier` |

**Missed by this rule (FN):**

- `Boothe u. Sandmeier IT GmbH` (organisation)
- `OberTelekom GmbH` (organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich` (address)

**Example 25** (doc_id: `deanon_TRAIN/1Ob22_24b`) (sent_id: `deanon_TRAIN/1Ob22_24b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der gefährdeten Partei Ida Theocharaki, vertreten durch Mag. Stefan Hotz, Rechtsanwalt in Wien, gegen den Gegner der gefährdeten Partei Mag. Bianca Orzegowski, vertreten durch Dr. Kristina Venturini, Rechtsanwältin in Wien, wegen Ehescheidung, hier wegen vorläufigen Unterhalts, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 13. Dezember 2023, GZ 44 R 314/23m-203, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionrekurs wird mangels der Voraussetzungen des § 528 Abs 1 ZPO (iVm §§ 78, 402 Abs 4 EO) zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Theocharaki` | `Ida Theocharaki` |

**Missed by this rule (FN):**

- `Mag. Bianca Orzegowski` (person)

**Example 26** (doc_id: `deanon_TRAIN/1Ob234_19x`) (sent_id: `deanon_TRAIN/1Ob234_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr in der Rechtssache der gefährdeten Partei VetR RgR Janet Wichtler, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdende Partei Charles Gutbrot, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 5. November 2019, GZ 1 R 191/19v-326, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 24. Juli 2019, GZ 23 Fam 27/15p-297, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß den §§ 402 Abs 4, 78 EO iVm § 526 Abs 2 erster Satz ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Charles Gutbrot` | `Charles Gutbrot` |

**Missed by this rule (FN):**

- `VetR RgR Janet Wichtler` (person)

**Example 27** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Elvira Nossal` | `Elvira Nossal` |

**Missed by this rule (FN):**

- `HR Janet Henken` (person)

**Example 28** (doc_id: `deanon_TRAIN/1Ob57_16p`) (sent_id: `deanon_TRAIN/1Ob57_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Familienrechtssache der Antragstellerin und gefährdeten Partei Tatjana Skowroneck, vertreten durch Mag. Nikolaus Vasak, Rechtsanwalt in Wien, gegen den Antragsgegner und Gegner der gefährdeten Partei Emmerich Smolin, vertreten durch Dr. Josef Lindlbauer, Rechtsanwalt in Enns, wegen (einstweiligen) Unterhalts, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 17. September 2015, GZ 16 R 271/15i-77, mit dem der Beschluss des Bezirksgerichts Mödling vom 29. Juni 2015, GZ 2 Fam 68/14f-58, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Tatjana Skowroneck` | `Tatjana Skowroneck` |
| `Emmerich Smolin` | `Emmerich Smolin` |

**Example 29** (doc_id: `deanon_TRAIN/1Ob84_13d`) (sent_id: `deanon_TRAIN/1Ob84_13d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Miklos Ostheim, vertreten durch Dr. Christoph Brandweiner und Dr. Gabriela Brandweiner-Reiter, Rechtsanwälte in Salzburg, gegen den Gegner der gefährdeten Partei Karim Markel DDr. Maximilian Damrau, vertreten durch Dr. Petra Patzelt, Rechtsanwältin in Salzburg, wegen Erlassung einer einstweiligen Verfügung, über den vom Gegner der gefährdeten Partei gestellten Antrag auf Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Erhebung eines außerordentlichen Revisionsrekurses gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 26. März 2013, GZ 21 R 359/12h-16, mit dem der Beschluss des Bezirksgerichts Salzburg vom 8. August 2012, GZ 20 C 11/12w-6, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Der Wiedereinsetzungsantrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Karim Markel` | `Karim Markel` |

**Missed by this rule (FN):**

- `Dr. Miklos Ostheim` (person)
- `DDr. Maximilian Damrau` (person)

**Example 30** (doc_id: `deanon_TRAIN/2Ob114_24i`) (sent_id: `deanon_TRAIN/2Ob114_24i_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Edith Wischnewsky, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei KzlR Techn R Quirin Erler, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Edith Wischnewsky` | `Edith Wischnewsky` |

**Missed by this rule (FN):**

- `KzlR Techn R Quirin Erler` (person)

**Example 31** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Edgar Arnts, vertreten durch Dr. Heinrich Oppitz, Rechtsanwalt in Wels, wider die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Edgar Arnts` | `Edgar Arnts` |

**Example 32** (doc_id: `deanon_TRAIN/2Ob175_21f`) (sent_id: `deanon_TRAIN/2Ob175_21f_4`)


Sloboda als weitere Richter in der Rechtssache der klagenden Partei Shoshana Etl, vertreten durch Mag. Axel Bauer, Rechtsanwalt in Wien, gegen die beklagte Partei Manuel van der Willik, vertreten durch Dr. Manfred Sommerbauer ua, Rechtsanwälte in Wiener Neustadt, wegen 44.903,84 EUR sA, über die Revision der beklagten Partei gegen das Zwischenurteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. Juni 2021, GZ 11 R 79/21z-66, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. März 2021, GZ 5 Cg 105/19a-50 in der Fassung des Berichtigungsbeschlusses vom 16. März 2021, GZ 5 Cg 105/19a-51, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Shoshana Etl` | `Shoshana Etl` |

**Missed by this rule (FN):**

- `Manuel van der Willik` (person)

**Example 33** (doc_id: `deanon_TRAIN/2Ob176_25h`) (sent_id: `deanon_TRAIN/2Ob176_25h_4`)


Sloboda, Dr. Thunhart und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richterin und weitere Richter in der Rechtssache der klagenden Partei Alva Wittwer, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, gegen die beklagte Partei Leopold Eggerichs, vertreten durch Grgic & Partneri Rechtsanwaltsgesellschaft mbH in Wien, wegen zuletzt 31.718 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 6. September 2025, GZ 11 R 40/25w-47, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Alva Wittwer` | `Alva Wittwer` |
| `Leopold Eggerichs` | `Leopold Eggerichs` |

**Example 34** (doc_id: `deanon_TRAIN/2Ob179_15k`) (sent_id: `deanon_TRAIN/2Ob179_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Franz Wagenschwanz, vertreten durch Dr. Klaus Estl, Rechtsanwalt in Salzburg, gegen die beklagten Parteien 1. Hartmut Willekes, und 2. KommR Roswitha Allgoewer, vertreten durch Dr. Roland Reichl, Rechtsanwalt in Salzburg, wegen 10.000 EUR sA und Feststellung (Streitinteresse 5.000 EUR), über den Rekurs der zweitbeklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 22. Juli 2015, GZ 22 R 169/15d-52, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Salzburg vom 2. April 2015, GZ 32 C 896/12f-47, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Franz Wagenschwanz` | `Franz Wagenschwanz` |

**Missed by this rule (FN):**

- `Hartmut Willekes` (person)
- `KommR Roswitha Allgoewer` (person)

**Example 35** (doc_id: `deanon_TRAIN/2Ob182_24i`) (sent_id: `deanon_TRAIN/2Ob182_24i_4`)


Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden und gefährdeten Partei Theresa Ziebold, vertreten durch Mag. Mahmut Sahinol, Rechtsanwalt in Wien, gegen die beklagten Parteien und Gegner der gefährdeten Parteien 1.

| Predicted | Gold |
|---|---|
| `Theresa Ziebold` | `Theresa Ziebold` |

**Example 36** (doc_id: `deanon_TRAIN/2Ob224_21m`) (sent_id: `deanon_TRAIN/2Ob224_21m_5`)


Dr. Konstantin Haas, Rechtsanwalt in Leonding, gegen die beklagte Partei Annette Provost, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, wegen 25.650,07 EUR sA sowie Herausgabe (Streitwert 1.000 EUR) über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Oktober 2021, GZ 2 R 119/21i-48, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 28. Juni 2021, GZ 5 Cg 60/18b-44, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Annette Provost` | `Annette Provost` |

**Example 37** (doc_id: `deanon_TRAIN/2Ob37_17f`) (sent_id: `deanon_TRAIN/2Ob37_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Florentin Uffenwasser, vertreten durch Dr. Armin Exner, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Stadtgemeinde Naomi Mertensmeyer, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, wegen 29.461,04 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 22.377,04 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 15. Dezember 2016, GZ 2 R 141/16a-47, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Uffenwasser` | `Florentin Uffenwasser` |

**Missed by this rule (FN):**

- `Naomi Mertensmeyer` (person)

**Example 38** (doc_id: `deanon_TRAIN/2Ob71_23i`) (sent_id: `deanon_TRAIN/2Ob71_23i_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Moses Malkomes, vertreten durch Klepp Nöbauer Hintringer Primetshofer Rechtsanwälte (GbR) in Linz, gegen die beklagte Partei Carmen Reinoldsmann, vertreten durch Dr. Christoph Arbeithuber, Rechtsanwalt in Linz, wegen 26.843,50 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Februar 2023, GZ 4 R 17/23g-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Moses Malkomes` | `Moses Malkomes` |
| `Carmen Reinoldsmann` | `Carmen Reinoldsmann` |

**Example 39** (doc_id: `deanon_TRAIN/2Ob73_15x`) (sent_id: `deanon_TRAIN/2Ob73_15x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dragan Karp, vertreten durch Mag. Bernd Trappmaier, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Marlene Diderichs, vertreten durch Mag. Claus Marchl, Rechtsanwalt in Wien, wegen 25.396,03 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. Jänner 2015, GZ 11 R 239/14v-26, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. September 2014, GZ 57 Cg 30/14x-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dragan Karp` | `Dragan Karp` |
| `Marlene Diderichs` | `Marlene Diderichs` |

**Example 40** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Luigi Neimeier` | `Luigi Neimeier` |

**Missed by this rule (FN):**

- `LNC KI Solutions GmbH` (organisation)
- `Kordelia Grauel` (person)

**Example 41** (doc_id: `deanon_TRAIN/2Ob89_17b`) (sent_id: `deanon_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Aron Dawideit, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. PhD Irvin Kindschuh, 2. Theodor Hermus, und 3.

| Predicted | Gold |
|---|---|
| `Aron Dawideit` | `Aron Dawideit` |

**Missed by this rule (FN):**

- `PhD Irvin Kindschuh` (person)
- `Theodor Hermus` (person)

**Example 42** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `Farina Dirker` | `Farina Dirker` |

**Missed by this rule (FN):**

- `Lüttge Chemie Limited` (organisation)
- `René Luidthard` (person)

**Example 43** (doc_id: `deanon_TRAIN/3Ob128_10k`) (sent_id: `deanon_TRAIN/3Ob128_10k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte und Hofrätinnen Hon.-Prof. Dr. Sailer, Dr. Lovrek, Dr. Jensik und Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Nadja Spangler, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagte Partei Sascha Heckert, vertreten durch Dr. Andreas König, Dr. Andreas Ermacora und Dr. Barbara Lässer, Rechtsanwälte in Innsbruck, wegen 137.146,60 EUR sA und Feststellung (Gesamtstreitwert 157.146,60 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2010, GZ 6 R 28/10w-44, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 30. Oktober 2009, GZ 7 Cg 117/07b-40, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Sascha Heckert` | `Sascha Heckert` |

**Missed by this rule (FN):**

- `Spangler` (person)

**Example 44** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Annette Fiss` | `Annette Fiss` |

**Missed by this rule (FN):**

- `Kraftnorost Wind GmbH` (organisation)
- `Roderich Holtze` (person)
- `Ing. Kirstin Movcan` (person)

**Example 45** (doc_id: `deanon_TRAIN/3Ob14_24s`) (sent_id: `deanon_TRAIN/3Ob14_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Daniela Sklenar SE, Kimberly Hurrelmeyer, vertreten durch Cerha Hempel Rechtsanwälte GmbH in Wien, gegen die verpflichtete Partei Staat Libyen, StR Violetta Stegemeyer, Libyen, vertreten durch Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 10 Mio EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Oktober 2023, GZ 47 R 228/23m-107, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Daniela Sklenar` | `Daniela Sklenar` |

**Missed by this rule (FN):**

- `Kimberly Hurrelmeyer` (person)
- `StR Violetta Stegemeyer` (person)

**Example 46** (doc_id: `deanon_TRAIN/3Ob152_10i`) (sent_id: `deanon_TRAIN/3Ob152_10i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei KMN Versicherung Werke AG, Corbinian Pichlmaier, vertreten durch Dr. Erich Kafka, Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die verpflichtete Partei Severin Wellenbrink, vertreten durch Dr. Philipp Jessich, Rechtsanwalt in Wien, wegen Aufschiebung einer Räumungsexekution, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. Mai 2010, GZ 39 R 44/10z-22, womit der Beschluss des Bezirksgerichts Fünfhaus vom 14. Jänner 2010, GZ 10 E 171/09d-6, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Severin Wellenbrink` | `Severin Wellenbrink` |

**Missed by this rule (FN):**

- `KMN Versicherung Werke AG` (organisation)
- `Corbinian Pichlmaier` (person)

**Example 47** (doc_id: `deanon_TRAIN/3Ob155_13k`) (sent_id: `deanon_TRAIN/3Ob155_13k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Ingolf Durur, vertreten durch Dr. Lucas Lorenz, Rechtsanwalt in Innsbruck, gegen die verpflichtete Partei Imre Viße, vertreten durch Dr. Robert Eiter, Rechtsanwalt in Landeck, wegen Einverleibung des Eigentumsrechts sowie Lastenfreistellung (§§ 350, 353 EO), über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 4. Juni 2013, GZ 1 R 10/13x-22, womit die Exekutionsbewilligung des Bezirksgerichts Imst vom 13. November 2012, GZ 5 E 2224/12y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Imre Viße` | `Imre Viße` |

**Missed by this rule (FN):**

- `Dr. Ingolf Durur` (person)

**Example 48** (doc_id: `deanon_TRAIN/3Ob156_12f`) (sent_id: `deanon_TRAIN/3Ob156_12f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Severin Ilek, vertreten durch die Sachwalterin Mag. Roswitha Ferl-Pailer, Rechtsanwältin in Hartberg, gegen die beklagte Partei Dipl.

| Predicted | Gold |
|---|---|
| `Severin Ilek` | `Severin Ilek` |

**Example 49** (doc_id: `deanon_TRAIN/3Ob178_15w`) (sent_id: `deanon_TRAIN/3Ob178_15w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Jensik als Vorsitzenden, die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Schwarzenbacher und Dr. Roch sowie die Hofrätin Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Nikolai Castelli, vertreten durch Divitschek Sieder Sauer Peter Rechtsanwälte GesBR in Deutschlandsberg, gegen die beklagte Partei Dohmgoergen Bau GmbH, Oswald Schubert, vertreten durch Dr. Johannes Liebmann, Rechtsanwalt in Gleisdorf, wegen 82.977,52 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. Juli 2015, GZ 3 R 54/15h-145, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Nikolai Castelli` | `Nikolai Castelli` |

**Missed by this rule (FN):**

- `Dohmgoergen Bau GmbH` (organisation)
- `Oswald Schubert` (person)

**Example 50** (doc_id: `deanon_TRAIN/3Ob19_20w`) (sent_id: `deanon_TRAIN/3Ob19_20w_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Rinaldo Isaac, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wider die beklagte Partei Felizia Mascheck, vertreten durch Dr. Alexandra Sedelmayer-Pammesberger, Rechtsanwältin in Wien, wegen Unterhaltsherabsetzung (AZ 8 C 22/16k) und Einwendungen gegen den Anspruch nach § 35 EO (AZ 8 C 4/18s), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 20. August 2019, GZ 44 R 338/19k-67, mit dem das Urteil des Bezirksgerichts Hernals vom 23. Mai 2019, GZ 8 C 22/16k-60, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden neuerlich dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Rinaldo Isaac` | `Rinaldo Isaac` |
| `Felizia Mascheck` | `Felizia Mascheck` |

**Example 51** (doc_id: `deanon_TRAIN/3Ob201_19h`) (sent_id: `deanon_TRAIN/3Ob201_19h_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Kimberly Mühlenstädt, vertreten durch Korn & Gärtner Rechtsanwälte OG in Salzburg, gegen die verpflichtete Partei Arabella Jorn, vertreten durch Dr. Wolfgang Lang, Rechtsanwalt in Salzburg, wegen 7.711,58 EUR sA, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 3. Juli 2019, GZ 22 R 171/19d-26, womit der Beschluss des Bezirksgerichts Salzburg vom 1. Februar 2019, GZ 5 E 2444/18x-7, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kimberly Mühlenstädt` | `Kimberly Mühlenstädt` |
| `Arabella Jorn` | `Arabella Jorn` |

**Example 52** (doc_id: `deanon_TRAIN/3Ob205_15s`) (sent_id: `deanon_TRAIN/3Ob205_15s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Laila Michot, vertreten durch Mag. Dr. Felix Sehorz, Rechtsanwalt in Wien, wider die verpflichtete Partei Jean Rehaag, wegen zwangsweiser Räumung (hier: Aufschiebung), aus Anlass des Revisionsrekurses der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 2. September 2015, GZ 39 R 260/15x-47, womit der Beschluss des Bezirksgerichts Liesing vom 27. Mai 2015, GZ 6 E 46/11k-43, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 16. Dezember 2015, AZ 3 Ob 205/15s, wird dahin berichtigt, dass das im ersten Absatz der Begründung genannte Datum der Einantwortung statt „6. März 2012“ richtig zu lauten hat „27. Juni 2013“.

| Predicted | Gold |
|---|---|
| `Laila Michot` | `Laila Michot` |
| `Jean Rehaag` | `Jean Rehaag` |

**Example 53** (doc_id: `deanon_TRAIN/3Ob220_14w`) (sent_id: `deanon_TRAIN/3Ob220_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Wendelin Mauroschat, Deutschland, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die verpflichtete Partei Quirin Eißelt, Deutschland, vertreten durch Dr. Josef Trenker, Rechtsanwalt in St. Johann im Pongau, wegen Erwirkung einer vertretbaren Handlung (§ 353 EO), über den „außerordentlichen Revisionsrekurs“ der betreibenden Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 23. Oktober 2014, GZ 4 R 312/14g-7, womit infolge Rekurses der verpflichteten Partei der Beschluss des Bezirksgerichts Kitzbühel vom 26. August 2014, GZ 1 E 3576/14g-2, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Quirin Eißelt` | `Quirin Eißelt` |

**Missed by this rule (FN):**

- `Dr. Wendelin Mauroschat` (person)

**Example 54** (doc_id: `deanon_TRAIN/3Ob236_17b`) (sent_id: `deanon_TRAIN/3Ob236_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Delila Englschall, vertreten durch Harb & Postl Rechtsanwälte OG in Graz, gegen die beklagte Partei Achmed Schnetzer, vertreten durch Dr. Paul Bauer, Dr. Anton Triendl, Rechtsanwälte in Innsbruck, wegen 32.173,22 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 23.653,60 EUR sA und Feststellung) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 29. November 2017, GZ 10 R 59/17b-27, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Delila Englschall` | `Delila Englschall` |
| `Achmed Schnetzer` | `Achmed Schnetzer` |

**Example 55** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH, Hubert Englmaier, vertreten durch Dr. Martin Holzer, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Florian Corvetti, vertreten durch Dr. Heimo Jilek, Rechtsanwalt in Leoben, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 3. November 2010, GZ 1 R 244/10i-34, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Leoben vom 9. Juni 2010, GZ 5 C 315/09y-28, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision der klagenden Partei wird Folge gegeben, das angefochtene Urteil aufgehoben und die Rechtssache zur neuerlichen Entscheidung an das Berufungsgericht zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Florian Corvetti` | `Florian Corvetti` |

**Missed by this rule (FN):**

- `Riecken Maschinenbau GmbH` (organisation)
- `Hubert Englmaier` (person)

**Example 56** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Florentin Rosskämmer, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde ÖkR Priv.-Doz. Björn Gustloff, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Florentin Rosskämmer` | `Florentin Rosskämmer` |

**Missed by this rule (FN):**

- `ÖkR Priv.-Doz. Björn Gustloff` (person)

**Example 57** (doc_id: `deanon_TRAIN/3Ob35_13p`) (sent_id: `deanon_TRAIN/3Ob35_13p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Mercedes Jungels, vertreten durch Dr. Peter Böck, Rechtsanwalt in Neusiedl am See, gegen die beklagte Partei Traude Ejsmond, vertreten durch Mag. Christian Kaiser, Rechtsanwalt in Wien, wegen Ehescheidung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Eisenstadt als Berufungsgericht vom 13. Dezember 2012, GZ 20 R 123/12f-15, womit infolge Berufungen der klagenden und beklagten Partei das Urteil des Bezirksgerichts Neusiedl am See vom 19. April 2012, GZ 10 C 10/12d-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Mercedes Jungels` | `Mercedes Jungels` |
| `Traude Ejsmond` | `Traude Ejsmond` |

**Example 58** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Andreas Clösges` | `Andreas Clösges` |

**Missed by this rule (FN):**

- `Chemie Valtri GmbH` (organisation)
- `Niels Niefeldt` (person)

**Example 59** (doc_id: `deanon_TRAIN/3Ob52_14i`) (sent_id: `deanon_TRAIN/3Ob52_14i_3`)


Kopf Der Oberste Gerichtshof hat durch die Hofrätin Dr. Lovrek als Vorsitzende sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Jensik, Dr. Musger und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Gabriel Domaß, vertreten durch Ehrlich-Rogner & Schlögl Rechtsanwalts-Partnerschaft in Wien, gegen die beklagte Partei KR Univ.-Prof.in Melina Thoele, vertreten durch Dr. Tassilo Wallentin, Rechtsanwalt in Wien, wegen Einwendungen gegen den Anspruch, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 6. Dezember 2012, GZ 47 R 275/12g-21, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Döbling vom 23. Mai 2012, GZ 6 C 223/10y-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Gabriel Domaß` | `Gabriel Domaß` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Melina Thoele` (person)

**Example 60** (doc_id: `deanon_TRAIN/4Ob112_24k`) (sent_id: `deanon_TRAIN/4Ob112_24k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Kersseboom Textil AG, Prof.in Juliette Große-Kleimann, Schweiz, vertreten durch die Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Benedikt Faath plc, DDr. Piedro Bielmeier, Malta, vertreten durch die Brandl Talos Rechtsanwälte GmbH in Wien, wegen 19.333,99 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz vom 14. März 2024, GZ 1 R 12/24a-46, mit dem das Urteil des Landesgerichts Wels vom 1. Dezember 2023, GZ 6 Cg 18/23p-41, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Benedikt Faath` | `Benedikt Faath` |

**Missed by this rule (FN):**

- `Kersseboom Textil AG` (organisation)
- `Prof.in Juliette Große-Kleimann` (person)
- `DDr. Piedro Bielmeier` (person)

**Example 61** (doc_id: `deanon_TRAIN/4Ob113_24g`) (sent_id: `deanon_TRAIN/4Ob113_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Vierziger u. Tewald Wind GmbH, Claire Lüdermann, Bakk. rer. nat., vertreten durch Grassner Rechtsanwalts GmbH in Linz, gegen die beklagte Partei Milena Buchmayr, vertreten durch Dr. Manfred Palkovits, Mag. Martin Sohm, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2024, GZ 38 R 247/23i-46, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Milena Buchmayr` | `Milena Buchmayr` |

**Missed by this rule (FN):**

- `Vierziger u. Tewald Wind GmbH` (organisation)
- `Claire Lüdermann, Bakk. rer. nat.` (person)

**Example 62** (doc_id: `deanon_TRAIN/4Ob13_24a`) (sent_id: `deanon_TRAIN/4Ob13_24a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Peter Nöhrnberg, LLM, vertreten durch Mag. Andrea Nobis, Rechtsanwältin in Wien, gegen die beklagte Partei Astrid Fesenmair, vertreten durch die Maraszto Milisits Rechtsanwälte OG in Wien, wegen 59.888,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. November 2023, GZ 5 R 154/23p-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Astrid Fesenmair` | `Astrid Fesenmair` |

**Missed by this rule (FN):**

- `Peter Nöhrnberg, LLM` (person)

**Example 63** (doc_id: `deanon_TRAIN/4Ob163_13v`) (sent_id: `deanon_TRAIN/4Ob163_13v_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Musger, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Miranda Bleckwehl, vertreten durch die Sachwalterin Dr. Tanja Sporrer, Rechtsanwältin, Innsbruck, Templstraße 22, gegen die beklagte Partei Oswald Wiechering, vertreten durch Dr. Ekkehard Erlacher und Dr. Renate Erlacher-Philadelphy, Rechtsanwälte in Innsbruck, wegen 56.626 EUR sA, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 8. Mai 2013, GZ 4 R 40/13h-125, womit der Antrag des Beklagten auf Berichtigung des Bewertungsausspruchs im Urteil vom 15. März 2013 abgewiesen wurde, folgenden Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Miranda Bleckwehl` | `Miranda Bleckwehl` |
| `Oswald Wiechering` | `Oswald Wiechering` |

**Example 64** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Christiane Rechenauer` | `Christiane Rechenauer` |

**Missed by this rule (FN):**

- `Bachkelwerk Pflege AG` (organisation)
- `Eva Selcuk` (person)
- `Dossenweg 6, 4924 Dundeck, Österreich` (address)

**Example 65** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jörg Drathschmidt` | `Jörg Drathschmidt` |

**Missed by this rule (FN):**

- `Wien Dorfsud GmbH` (organisation)
- `Gerlinde Balcerzak` (person)
- `Waldfen-Versand GmbH` (organisation)
- `Eva Boztas` (person)

**Example 66** (doc_id: `deanon_TRAIN/4Ob190_23d`) (sent_id: `deanon_TRAIN/4Ob190_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Jolanda Petschke, vertreten durch den Verfahrenshelfer Dr. Lukas Twardosz, Rechtsanwalt in Wien, gegen die beklagte Partei Ali Salwetter Verein Wilma Sahlmüller, vertreten durch die Verfahrenshelferin Mag. Ioana-Maria Vilau, Rechtsanwältin in Wien, wegen zuletzt 30.000 EUR sA, Unterlassung und Beseitigung (Gesamtstreitwert: 40.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Juli 2023, GZ 4 R 175/22t-62, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jolanda Petschke` | `Jolanda Petschke` |

**Missed by this rule (FN):**

- `Ali Salwetter` (person)
- `Wilma Sahlmüller` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Katharina Tomandl` — partial — pred is substring of gold: `Katharina Tomandl, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

**False Positives:**

- `Juri Petraschk` — partial — pred is substring of gold: `Juri Petraschk, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Juri Petraschk, Bakk. iur.`(person)
- `Mag. Dominik Riewert`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Diethard Eisenlöffel` — partial — pred is substring of gold: `Diethard Eisenlöffel, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Mur Kraftalheim Holding Gmb` — partial — pred is substring of gold: `Mur Kraftalheim Holding GmbH`
- `Nexstein Textil Gmb` — partial — pred is substring of gold: `Nexstein Textil GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Alsteinost Gmb` — partial — pred is substring of gold: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Agrargemeinschaft Jonasgasse` — positional overlap with gold: `Jonasgasse 71, 4760 Weeg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mittel Keltal Gmb` — partial — pred is substring of gold: `Mittel Keltal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kotschenreuther u. Abele Planung GmbH`(organisation)
- `Janis Krentzel`(person)
- `Mittel Keltal GmbH`(organisation)
- `Julian Grebener`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bruno Altevogt, BA MBA, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, gegen die beklagten Parteien 1.

**False Positives:**

- `Bruno Altevogt` — partial — pred is substring of gold: `Bruno Altevogt, BA MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruno Altevogt, BA MBA`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Enns Werkdonver Holding Gmb` — partial — pred is substring of gold: `Enns Werkdonver Holding GmbH`
- `Prausewetter Umwel` — partial — pred is substring of gold: `Prausewetter Umwelt AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Enns Werkdonver Holding GmbH`(organisation)
- `Mag.a DDr.in Lynn Rothwein`(person)
- `Prausewetter Umwelt AG`(organisation)
- `Valerius Gensmantel`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Helge Monhemius` — partial — pred is substring of gold: `Helge Monhemius, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Helge Monhemius, Bakk. techn.`(person)
- `Ing. Eugenia Welze`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob88_19t`) (sent_id: `deanon_TRAIN/10Ob88_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Fatima Berlin, BSc, vertreten durch Frysak & Frysak Rechtsanwalts-Partnerschaft in Wien, gegen die beklagte Partei Otto Cesar, MSc, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, wegen 18.800 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 14. Oktober 2019, GZ 11 R 145/19b-16, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Mai 2019, GZ 27 Cg 6/19d-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Fatima Berlin` — partial — pred is substring of gold: `Fatima Berlin, BSc`
- `Otto Cesar` — partial — pred is substring of gold: `Otto Cesar, MSc`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Fatima Berlin, BSc`(person)
- `Otto Cesar, MSc`(person)

**Example 11** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Gertrud Johanna Ostrovska` — partial — gold is substring of pred: `Ostrovska`
- `Steiermärkische Gebietskrankenkasse` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Ostrovska`(person)

**Example 12** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Vorarlberger Gebietskrankenkasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Samantha Neunteufl`(person)

**Example 13** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Laura Overbeeke` — partial — pred is substring of gold: `Laura Overbeeke, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

**Example 14** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Angelina Töpker In` — partial — gold is substring of pred: `Angelina Töpker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)

**Example 15** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Tracondon Aktiengesellschaft` — type mismatch — same span as gold: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tamara Schweinfurth, vertreten durch Dr. Wolfgang Maurer, Rechtsanwalt in Golling, gegen die beklagte Partei Noah Vlatten, BEd, vertreten durch Dr. Peter Perner, Rechtsanwalt in Salzburg, wegen 10.895,18 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 19. Mai 2015, GZ 22 R 126/15f-21, mit dem das Urteil des Bezirksgerichts Salzburg vom 5. März 2015, GZ 32 C 407/14x-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Noah Vlatten` — partial — pred is substring of gold: `Noah Vlatten, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tamara Schweinfurth`(person)
- `Noah Vlatten, BEd`(person)

**Example 17** (doc_id: `deanon_TRAIN/1Ob186_12b`) (sent_id: `deanon_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Pasqualini, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Denzlein, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Thomas Pasqualini` — partial — gold is substring of pred: `Pasqualini`
- `Patrick Denzlein` — partial — gold is substring of pred: `Denzlein`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Pasqualini`(person)
- `Denzlein`(person)

**Example 18** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hamberg Marine Limited` — type mismatch — same span as gold: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 19** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Roberta Reumschüssel` — partial — pred is substring of gold: `Roberta Reumschüssel, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 20** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Kurt Schwenckel, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Condon Planung GmbH, Corvin Heidtmeyer, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Condon Planung Gmb` — partial — pred is substring of gold: `Condon Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kurt Schwenckel`(person)
- `Condon Planung GmbH`(organisation)
- `Corvin Heidtmeyer`(person)

**Example 21** (doc_id: `deanon_TRAIN/1Ob95_21h`) (sent_id: `deanon_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Planung Berglanzfurt GmbH, Heiko Thieroff, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei InnGetränke GmbH, OMedR Rainer Witthoefft, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Planung Berglanzfurt Gmb` — partial — pred is substring of gold: `Planung Berglanzfurt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Planung Berglanzfurt GmbH`(organisation)
- `Heiko Thieroff`(person)
- `InnGetränke GmbH`(organisation)
- `OMedR Rainer Witthoefft`(person)

**Example 22** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. E. Solé als weitere Richter in der Rechtssache der klagenden Partei Thaddäus Gerzabek, LLM, vertreten durch Dr. Hanspeter Egger, Rechtsanwalt in Wien, gegen die beklagte Partei Pietruszak Recycling -AG, Rainer Chochola, vertreten durch Dr. Norbert Bergmüller, Rechtsanwalt in Schladming, wegen 1.505,25 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Hietzing das Bezirksgericht Irdning bestimmt.

**False Positives:**

- `Thaddäus Gerzabek` — partial — pred is substring of gold: `Thaddäus Gerzabek, LLM`
- `Pietruszak Recycling` — type mismatch — same span as gold: `Pietruszak Recycling`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Thaddäus Gerzabek, LLM`(person)
- `Pietruszak Recycling`(organisation)
- `Rainer Chochola`(person)
- `Bezirksgericht Irdning`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/2Ob177_20y`) (sent_id: `deanon_TRAIN/2Ob177_20y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Jörg von Bockel, vertreten durch Mag. Stefan Danzinger, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Gareise Energie AG, Ada Krol, vertreten durch Grgić & Partneri Rechtsanwaltsgesellschaft mbH, Zweigniederlassung Wien, wegen 11.266,39 EUR sA, über die Revision der beklagten Partei (Revisionsinteresse: 6.646,20 EUR) gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 17. Juli 2020, GZ 18 R 38/20x-32, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Wiener Neustadt vom 31. Jänner 2020, GZ 14 C 1015/18h-27, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gareise Energi` — partial — pred is substring of gold: `Gareise Energie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jörg von Bockel`(person)
- `Gareise Energie AG`(organisation)
- `Ada Krol`(person)

**Example 24** (doc_id: `deanon_TRAIN/2Ob178_18t`) (sent_id: `deanon_TRAIN/2Ob178_18t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Garttri Sicherheit -GesmbH, Alpendorfsiedlung 14, 4209 Linzerberg, Österreich, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, wider die beklagte Partei Vogelsanger Marine GmbH, Juri Büttgens, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen (restlich) 30.000 EUR sA, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juli 2018, GZ 4 R 79/18v-157, mit welchem das Endurteil des Handelsgerichts Wien vom 9. April 2018, GZ 40 Cg 12/11g-153, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Garttri Sicherheit` — type mismatch — same span as gold: `Garttri Sicherheit`
- `Vogelsanger Marine Gmb` — partial — pred is substring of gold: `Vogelsanger Marine GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Garttri Sicherheit`(organisation)
- `Alpendorfsiedlung 14, 4209 Linzerberg, Österreich`(address)
- `Vogelsanger Marine GmbH`(organisation)
- `Juri Büttgens`(person)

**Example 25** (doc_id: `deanon_TRAIN/2Ob181_10x`) (sent_id: `deanon_TRAIN/2Ob181_10x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Gertrude Ptak, vertreten durch Dr. Bertram Broesigke und Dr. Wolfgang Broesigke, Rechtsanwälte in Wien, gegen die beklagte Partei Josef Schindelmeißer, vertreten durch den Sachwalter Dr. Helmut Heiger, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 15. Juni 2010, GZ 41 R 130/10m-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Gertrude Ptak` — partial — gold is substring of pred: `Ptak`
- `Josef Schindelmeißer` — partial — gold is substring of pred: `Schindelmeißer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Ptak`(person)
- `Schindelmeißer`(person)

**Example 26** (doc_id: `deanon_TRAIN/2Ob216_18f`) (sent_id: `deanon_TRAIN/2Ob216_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof. Ewald Schwietale, vertreten durch Mag. Martin Paar und Mag. Hermann Zwanzger, Rechtsanwälte in Wien, gegen die beklagte Partei Lütkemöller Digital AG, Karl Deppermann, vertreten durch Dr. Helmut Weinzettl, Rechtsanwalt in Wiener Neustadt, wegen 14.817,50 EUR sA, über die Revisionen beider Parteien gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Juni 2018, GZ 18 R 11/18y-64, mit welchem das Urteil des Bezirksgerichts Baden vom 28. Dezember 2017, GZ 7 C 1010/15x-58, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Lütkemöller Digita` — partial — pred is substring of gold: `Lütkemöller Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Ewald Schwietale`(person)
- `Lütkemöller Digital AG`(organisation)
- `Karl Deppermann`(person)

**Example 27** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Stallbauer Telekom Aktiengesellschaft` — type mismatch — same span as gold: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 28** (doc_id: `deanon_TRAIN/2Ob37_17f`) (sent_id: `deanon_TRAIN/2Ob37_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Florentin Uffenwasser, vertreten durch Dr. Armin Exner, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Stadtgemeinde Naomi Mertensmeyer, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, wegen 29.461,04 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 22.377,04 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 15. Dezember 2016, GZ 2 R 141/16a-47, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stadtgemeinde Naomi Mertensmeyer` — partial — gold is substring of pred: `Naomi Mertensmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Uffenwasser`(person)
- `Naomi Mertensmeyer`(person)

**Example 29** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Thomas Papakonstantinou, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagten Parteien 1. Matthias Graafmann, und 2.

**False Positives:**

- `Thomas Papakonstantinou` — partial — gold is substring of pred: `Papakonstantinou`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Papakonstantinou`(person)
- `Graafmann`(person)

**Example 30** (doc_id: `deanon_TRAIN/2Ob86_12d`) (sent_id: `deanon_TRAIN/2Ob86_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Constanze Hoefelmann, MSc, vertreten durch Gruböck & Lentschig Rechtsanwälte OG in Baden, wider die beklagte Partei „ Herbert Sippert “ Ada Roselius, vertreten durch Themmer, Toth & Partner Rechtsanwälte OG in Wien, wegen 144.329,55 EUR sA (Revisionsinteresse 54.717 EUR sA), infolge der außerordentlichen Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Februar 2012, GZ 4 R 598/11g-25, den Beschluss gefasst:  Spruch Das Revisionsverfahren wird bis zur rechtskräftigen Erledigung des Verfahrens über den Ablehnungsantrag der beklagten Partei gegen die Erstrichterin unterbrochen.

**False Positives:**

- `Constanze Hoefelmann` — partial — pred is substring of gold: `Constanze Hoefelmann, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Constanze Hoefelmann, MSc`(person)
- `Herbert Sippert`(person)
- `Ada Roselius`(person)

**Example 31** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Lüttge Chemie Limited` — type mismatch — same span as gold: `Lüttge Chemie Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 32** (doc_id: `deanon_TRAIN/3Ob105_13g`) (sent_id: `deanon_TRAIN/3Ob105_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei ÖkR Malik Sutmöller OEG, Leila Nieboer, vertreten durch Dr. Heinz-Wilhelm Stenzl, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel Bachlemsee GmbH, Erwin Klefass, BSc, vertreten durch Dr. Johann Gelbmann, Rechtsanwalt in Wien, wegen (restlich) 12.536,14 EUR sA, über die Revision der beklagten Partei (Revisionsinteresse 6.909 EUR sA) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. Dezember 2012, GZ 38 R 173/12s-139, womit über die Berufungen beider Parteien das Urteil des Bezirksgerichts Fünfhaus vom 10. April 2012, GZ 12 C 1045/05m-131, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mittel Bachlemsee Gmb` — partial — pred is substring of gold: `Mittel Bachlemsee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Malik Sutmöller`(person)
- `Leila Nieboer`(person)
- `Mittel Bachlemsee GmbH`(organisation)
- `Erwin Klefass, BSc`(person)

**Example 33** (doc_id: `deanon_TRAIN/3Ob128_10k`) (sent_id: `deanon_TRAIN/3Ob128_10k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte und Hofrätinnen Hon.-Prof. Dr. Sailer, Dr. Lovrek, Dr. Jensik und Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Nadja Spangler, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagte Partei Sascha Heckert, vertreten durch Dr. Andreas König, Dr. Andreas Ermacora und Dr. Barbara Lässer, Rechtsanwälte in Innsbruck, wegen 137.146,60 EUR sA und Feststellung (Gesamtstreitwert 157.146,60 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2010, GZ 6 R 28/10w-44, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 30. Oktober 2009, GZ 7 Cg 117/07b-40, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nadja Spangler` — partial — gold is substring of pred: `Spangler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Spangler`(person)
- `Sascha Heckert`(person)

**Example 34** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kraftnorost Wind Gmb` — partial — pred is substring of gold: `Kraftnorost Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 35** (doc_id: `deanon_TRAIN/3Ob14_24s`) (sent_id: `deanon_TRAIN/3Ob14_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Daniela Sklenar SE, Kimberly Hurrelmeyer, vertreten durch Cerha Hempel Rechtsanwälte GmbH in Wien, gegen die verpflichtete Partei Staat Libyen, StR Violetta Stegemeyer, Libyen, vertreten durch Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 10 Mio EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Oktober 2023, GZ 47 R 228/23m-107, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Staat Libyen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daniela Sklenar`(person)
- `Kimberly Hurrelmeyer`(person)
- `StR Violetta Stegemeyer`(person)

**Example 36** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Bruckgartver Gmb` — partial — pred is substring of gold: `Bruckgartver GmbH`
- `Ofczarczik Planun` — partial — pred is substring of gold: `Ofczarczik Planung AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 37** (doc_id: `deanon_TRAIN/3Ob178_15w`) (sent_id: `deanon_TRAIN/3Ob178_15w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Jensik als Vorsitzenden, die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Schwarzenbacher und Dr. Roch sowie die Hofrätin Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Nikolai Castelli, vertreten durch Divitschek Sieder Sauer Peter Rechtsanwälte GesBR in Deutschlandsberg, gegen die beklagte Partei Dohmgoergen Bau GmbH, Oswald Schubert, vertreten durch Dr. Johannes Liebmann, Rechtsanwalt in Gleisdorf, wegen 82.977,52 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. Juli 2015, GZ 3 R 54/15h-145, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dohmgoergen Bau Gmb` — partial — pred is substring of gold: `Dohmgoergen Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nikolai Castelli`(person)
- `Dohmgoergen Bau GmbH`(organisation)
- `Oswald Schubert`(person)

**Example 38** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Heizung Werkuni Aktiengesellschaft` — type mismatch — same span as gold: `Heizung Werkuni Aktiengesellschaft`
- `Dorothea Eiken Bank` — partial — gold is substring of pred: `Dorothea Eiken`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)
- `LLP Co KG`(organisation)

**Example 39** (doc_id: `deanon_TRAIN/3Ob22_13a`) (sent_id: `deanon_TRAIN/3Ob22_13a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der betreibenden Partei Szymczak Software GmbH, Berthold Haendl, vertreten durch Mayrhofer & Rainer Rechtsanwälte OG in Wien, gegen die verpflichtete Partei Mag. Dr. Jennifer Meinard, wegen Räumung, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. November 2012, GZ 40 R 307/12m-99, womit der Rekurs der verpflichteten Partei gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. Juli 2012, GZ 48 C 363/10d = 48 E 70/11y-38, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Szymczak Software Gmb` — partial — pred is substring of gold: `Szymczak Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Szymczak Software GmbH`(organisation)
- `Berthold Haendl`(person)
- `Dr. Jennifer Meinard`(person)

**Example 40** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH, Hubert Englmaier, vertreten durch Dr. Martin Holzer, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Florian Corvetti, vertreten durch Dr. Heimo Jilek, Rechtsanwalt in Leoben, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 3. November 2010, GZ 1 R 244/10i-34, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Leoben vom 9. Juni 2010, GZ 5 C 315/09y-28, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision der klagenden Partei wird Folge gegeben, das angefochtene Urteil aufgehoben und die Rechtssache zur neuerlichen Entscheidung an das Berufungsgericht zurückverwiesen.

**False Positives:**

- `Riecken Maschinenbau Gmb` — partial — pred is substring of gold: `Riecken Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Riecken Maschinenbau GmbH`(organisation)
- `Hubert Englmaier`(person)
- `Florian Corvetti`(person)

**Example 41** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Chemie Valtri Gmb` — partial — pred is substring of gold: `Chemie Valtri GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Clösges`(person)
- `Chemie Valtri GmbH`(organisation)
- `Niels Niefeldt`(person)

**Example 42** (doc_id: `deanon_TRAIN/3Ob49_11v`) (sent_id: `deanon_TRAIN/3Ob49_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Julius Zimzick Verlag GmbH & Co KG, Terramaregasse 28, 8234 Rohrbachschlag, Österreich, vertreten durch Dr. Wolfgang Dartmann und andere Rechtsanwälte in Linz, wider die beklagten Parteien 1. Friedrich Schreinemachers und 2.

**False Positives:**

- `Julius Zimzick Verlag Gmb` — positional overlap with gold: `Zimzick Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zimzick Verlag GmbH`(organisation)
- `Co KG`(organisation)
- `Terramaregasse 28, 8234 Rohrbachschlag, Österreich`(address)
- `Schreinemachers`(person)

**Example 43** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Rudigkeit Finanzen Gmb` — partial — pred is substring of gold: `Rudigkeit Finanzen GmbH`
- `Suddorftra Manufaktur Gmb` — partial — pred is substring of gold: `Suddorftra Manufaktur GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)
- `Rudigkeit Finanzen GmbH`(organisation)
- `Ing. Sascha Rohkrämer`(person)
- `Suddorftra Manufaktur GmbH`(organisation)
- `Ludmilla Nottelmann`(person)
- `Landesgericht Wien`(organisation)

**Example 44** (doc_id: `deanon_TRAIN/4Ob100_13d`) (sent_id: `deanon_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Erwin Sieferer, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Lebensmittel Seeder -Aktiengesellschaft, Knechtswies 63, 4692 Niederau, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ StR Thobias Broß ” Viola Hüßkes, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Verein Erwin Sieferer` — partial — gold is substring of pred: `Erwin Sieferer`
- `Lebensmittel Seeder` — type mismatch — same span as gold: `Lebensmittel Seeder`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Erwin Sieferer`(person)
- `Lebensmittel Seeder`(organisation)
- `Knechtswies 63, 4692 Niederau, Österreich`(address)
- `StR Thobias Broß`(person)
- `Viola Hüßkes`(person)

**Example 45** (doc_id: `deanon_TRAIN/4Ob112_24k`) (sent_id: `deanon_TRAIN/4Ob112_24k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Kersseboom Textil AG, Prof.in Juliette Große-Kleimann, Schweiz, vertreten durch die Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Benedikt Faath plc, DDr. Piedro Bielmeier, Malta, vertreten durch die Brandl Talos Rechtsanwälte GmbH in Wien, wegen 19.333,99 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz vom 14. März 2024, GZ 1 R 12/24a-46, mit dem das Urteil des Landesgerichts Wels vom 1. Dezember 2023, GZ 6 Cg 18/23p-41, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Kersseboom Texti` — partial — pred is substring of gold: `Kersseboom Textil AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kersseboom Textil AG`(organisation)
- `Prof.in Juliette Große-Kleimann`(person)
- `Benedikt Faath`(person)
- `DDr. Piedro Bielmeier`(person)

**Example 46** (doc_id: `deanon_TRAIN/4Ob13_24a`) (sent_id: `deanon_TRAIN/4Ob13_24a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Peter Nöhrnberg, LLM, vertreten durch Mag. Andrea Nobis, Rechtsanwältin in Wien, gegen die beklagte Partei Astrid Fesenmair, vertreten durch die Maraszto Milisits Rechtsanwälte OG in Wien, wegen 59.888,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. November 2023, GZ 5 R 154/23p-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Peter Nöhrnberg` — partial — pred is substring of gold: `Peter Nöhrnberg, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Peter Nöhrnberg, LLM`(person)
- `Astrid Fesenmair`(person)

**Example 47** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Bachkelwerk Pfleg` — partial — pred is substring of gold: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 48** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Wien Dorfsud Gmb` — partial — pred is substring of gold: `Wien Dorfsud GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jörg Drathschmidt`(person)
- `Wien Dorfsud GmbH`(organisation)
- `Gerlinde Balcerzak`(person)
- `Waldfen-Versand GmbH`(organisation)
- `Eva Boztas`(person)

**Example 49** (doc_id: `deanon_TRAIN/4Ob190_23d`) (sent_id: `deanon_TRAIN/4Ob190_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Jolanda Petschke, vertreten durch den Verfahrenshelfer Dr. Lukas Twardosz, Rechtsanwalt in Wien, gegen die beklagte Partei Ali Salwetter Verein Wilma Sahlmüller, vertreten durch die Verfahrenshelferin Mag. Ioana-Maria Vilau, Rechtsanwältin in Wien, wegen zuletzt 30.000 EUR sA, Unterlassung und Beseitigung (Gesamtstreitwert: 40.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Juli 2023, GZ 4 R 175/22t-62, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ali Salwetter Verein Wilma Sahlmüller` — partial — gold is substring of pred: `Ali Salwetter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jolanda Petschke`(person)
- `Ali Salwetter`(person)
- `Wilma Sahlmüller`(person)

</details>

---

## `Person in List Context (Numbered)`

**F1:** 0.192 | **Precision:** 0.378 | **Recall:** 0.129  

**Format:** `regex`  
**Rule ID:** `e45b5272`  
**Description:**
Captures names in numbered lists (1., 2., 3.) or comma-separated lists where a name is followed by a number or comma, ensuring full name capture.

**Content:**
```
(?:^|,\s+|\d+\.\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:,|\s+\d+\.\s+|\s+und\s+|\s+und\s+|\s+\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.378 | 0.129 | 0.192 | 468 | 177 | 291 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 177 | 291 | 1183 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Gerald Zacharie` | `Gerald Zacharie` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)
- `Mur Kraftalheim Holding GmbH` (organisation)
- `Nexstein Textil GmbH` (organisation)
- `Dipl.-Ing. Lynn Forkarth` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Adelheid Lochmaier` | `Adelheid Lochmaier` |

**Missed by this rule (FN):**

- `Skrzypczik + Duchscherer Digital AG` (organisation)
- `Ursula Antoniadis` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `Isidor Janofske` | `Isidor Janofske` |

**Missed by this rule (FN):**

- `Wolfram Fritzsche` (person)
- `VetR Lukas Dickhaus` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Krentzel` | `Janis Krentzel` |
| `Julian Grebener` | `Julian Grebener` |

**Missed by this rule (FN):**

- `Kotschenreuther u. Abele Planung GmbH` (organisation)
- `Mittel Keltal GmbH` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Severin Simaitis` | `Severin Simaitis` |
| `Nepomuk Sprinzl` | `Nepomuk Sprinzl` |

**Missed by this rule (FN):**

- `20. November` (date)
- `8. Juli 1967` (date)
- `17. November` (date)
- `11. September` (date)
- `Mag. Miklos Stiening` (person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Mag. Schober und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Pflegschaftssache der Minderjährigen 1. Leonhard Brodskyy, und 2.

| Predicted | Gold |
|---|---|
| `Leonhard Brodskyy` | `Leonhard Brodskyy` |

**Example 6** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Valerius Gensmantel` | `Valerius Gensmantel` |

**Missed by this rule (FN):**

- `Enns Werkdonver Holding GmbH` (organisation)
- `Mag.a DDr.in Lynn Rothwein` (person)
- `Prausewetter Umwelt AG` (organisation)

**Example 7** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jaden Jurkutaitis` | `Jaden Jurkutaitis` |

**Missed by this rule (FN):**

- `Calvin Mützlaff` (person)
- `Volker Scheffski` (person)
- `8. Dezember 1982` (date)
- `PhD Karim Trieber` (person)
- `11. Januar 1975` (date)
- `StR Lara Jungnikl` (person)
- `RgR Dipl.-Ing. Quirin Bagemühl` (person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `Delila Leiteritz` | `Delila Leiteritz` |

**Missed by this rule (FN):**

- `Ignaz Jungmichel` (person)
- `TalAlvalRobotik AG` (organisation)

**Example 9** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dolores Chatzakis` | `Dolores Chatzakis` |

**Missed by this rule (FN):**

- `Calvin Amorelli` (person)
- `Strathewerd u. Niemetz Metall GmbH` (organisation)

**Example 10** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_4`)


Anselm Lamann, geboren am 29. Juni 2014, 2. MedR Samir Lorang, geboren am 28. März 1969, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Anselm Lamann` | `Anselm Lamann` |

**Missed by this rule (FN):**

- `29. Juni 2014` (date)
- `MedR Samir Lorang` (person)
- `28. März 1969` (date)

**Example 11** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Pablo Ebling, geboren am 9. August 1991, Hugo Stegemann, geboren am 30. September 1992, mj Delila Ringsdorff, geboren am 22. Dezember 1998 und mj Nigel Conrades, Bakk. techn. BEd, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Vivian Hadamzick, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hugo Stegemann` | `Hugo Stegemann` |

**Missed by this rule (FN):**

- `Pablo Ebling` (person)
- `Delila Ringsdorff` (person)
- `Nigel Conrades, Bakk. techn. BEd` (person)
- `Mag. Vivian Hadamzick` (person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_20`)


Aus dem Akt ergebe sich, das Edeltraud Suhrbeer, Achmed Rethage und Laetitia Chmielowska Unterhaltsvorschüsse gemäß § 4 Z 2 UVG mit Beschluss vom 7. 9. 2009 (ON U 319, 320 und 321) ab 1. 9. 2009 gewährt worden seien.

| Predicted | Gold |
|---|---|
| `Achmed Rethage` | `Achmed Rethage` |

**Missed by this rule (FN):**

- `Edeltraud Suhrbeer` (person)
- `Laetitia Chmielowska` (person)

**Example 13** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_5`)


Zeno Thulcke, 2. Christine Adomadt, erstklagende Partei vertreten durch die Erwachsenenvertreterin Mag. Elfriede Melichar, Rechtsanwältin in Mödling, wider die beklagte Partei Dr. Benjamin Görmar, wegen Schadenersatz, hier wegen Verfahrenshilfe, über den „Rekurs“ (richtig: Revisionsrekurs) der zweitklagenden Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 21. Juli 2023, GZ 18 R 96/23f, 97/23b, 98/23z-31, womit der Beschluss des Bezirksgerichts Mödling vom 10. Mai 2023, GZ 3 C 1057/21v-25, hinsichtlich der erstklagenden Partei bestätigt und der von der zweitklagenden Partei dagegen erhobene Rekurs zurückgewiesen wurde, sowie der Rekurs der klagenden Parteien gegen den Beschluss des Bezirksgerichts Mödling vom 28. März 2023, GZ 3 C 1057/21v-20, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Zeno Thulcke` | `Zeno Thulcke` |
| `Christine Adomadt` | `Christine Adomadt` |

**Missed by this rule (FN):**

- `Dr. Benjamin Görmar` (person)

**Example 14** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Robert Leis` | `Robert Leis` |

**Missed by this rule (FN):**

- `See-Versand Werke GmbH` (organisation)
- `Dargatz+Boedewig Telekom GmbH` (organisation)
- `ÖkR Nikolaus Buksbaum` (person)

**Example 15** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Waldemar Lokämper` | `Waldemar Lokämper` |

**Missed by this rule (FN):**

- `Landesgericht Wiener Neustadt` (organisation)
- `Herbes&Vißers Heizung GmbH` (organisation)
- `Traun-Luftfahrt GmbH` (organisation)
- `VetR DDr. Walter Stuehrmann` (person)
- `Landesgericht Feldkirch` (organisation)

**Example 16** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Timothy Schulmeister` | `Timothy Schulmeister` |

**Missed by this rule (FN):**

- `KommR Franz Kubank` (person)
- `Laurin Aichhorn` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 17** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

| Predicted | Gold |
|---|---|
| `Janis Marxmeyer` | `Janis Marxmeyer` |

**Missed by this rule (FN):**

- `Laura Overbeeke, BA` (person)

**Example 18** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_4`)


Chantal Maxein, vertreten durch Dr. Eric Agstner, Rechtsanwalt in Wien, wegen Unterlassung, Zahlung, Feststellung und Beseitigung, über die Revision der beklagten Parteien gegen das Teilurteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Februar 2017, GZ 58 R 128/16w-38a, in der Fassung des Berichtigungsbeschlusses vom 29. März 2017, GZ 58 R 128/16w-40, mit dem das Urteil des Bezirksgerichts Neunkirchen vom 18. November 2016, GZ 23 C 249/16x-33, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chantal Maxein` | `Chantal Maxein` |

**Example 19** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_4`)


Peter Gopfert, 2. OSR Gerald Huckebrinker, und 3.

| Predicted | Gold |
|---|---|
| `Peter Gopfert` | `Peter Gopfert` |

**Missed by this rule (FN):**

- `OSR Gerald Huckebrinker` (person)

**Example 20** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ronja Straßgschwandtner` | `Ronja Straßgschwandtner` |

**Missed by this rule (FN):**

- `Angelina Töpker` (person)
- `Mag. Lilia Anderßon` (person)
- `Vanek und Eloy Analyse GmbH` (organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich` (address)

**Example 21** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Nordkamp, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Belohlawek KI Bank AG, Denis Nakonzer, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Denis Nakonzer` | `Denis Nakonzer` |

**Missed by this rule (FN):**

- `Manfred Nordkamp` (person)
- `Belohlawek KI` (organisation)

**Example 22** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Tanja Thielike` | `Tanja Thielike` |

**Missed by this rule (FN):**

- `Synsynfurt-Finanzen GmbH` (organisation)
- `Roberta Reumschüssel, Bakk. phil.` (person)

**Example 23** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Kurt Schwenckel, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Condon Planung GmbH, Corvin Heidtmeyer, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Corvin Heidtmeyer` | `Corvin Heidtmeyer` |

**Missed by this rule (FN):**

- `Kurt Schwenckel` (person)
- `Condon Planung GmbH` (organisation)

**Example 24** (doc_id: `deanon_TRAIN/1Ob56_21y`) (sent_id: `deanon_TRAIN/1Ob56_21y_4`)


Ali Haarnacke und 2. Li Baselt, vertreten durch Dr. Serpil Dogan, Rechtsanwältin in Feldkirch, gegen die beklagte Partei Republik Österreich (Bund), vertreten durch die Finanzprokuratur in Wien, und den Nebenintervenienten auf Seite der beklagten Partei KzlR Florian Schlimm, vertreten durch Dr. Bertram Grass und Mag. Christoph Dorner, Rechtsanwälte in Bregenz, wegen 60.300 EUR sA und Feststellung (Erstklägerin) und 66.300 EUR sA und Feststellung (Zweitkläger), über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 27. Jänner 2021, GZ 4 R 171/20h-41, mit dem das Urteil des Landesgerichts Feldkirch vom 2. Oktober 2020, GZ 4 Cg 14/19k-35, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ali Haarnacke` | `Ali Haarnacke` |
| `Li Baselt` | `Li Baselt` |

**Missed by this rule (FN):**

- `KzlR Florian Schlimm` (person)

**Example 25** (doc_id: `deanon_TRAIN/1Ob95_21h`) (sent_id: `deanon_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Planung Berglanzfurt GmbH, Heiko Thieroff, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei InnGetränke GmbH, OMedR Rainer Witthoefft, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Heiko Thieroff` | `Heiko Thieroff` |

**Missed by this rule (FN):**

- `Planung Berglanzfurt GmbH` (organisation)
- `InnGetränke GmbH` (organisation)
- `OMedR Rainer Witthoefft` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Zarin Steevens, geboren 26. Mai 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Dorothea Akkaya, und des Antragsgegners Mirko Hamidi, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.

**False Positives:**

- `Russische Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zarin Steevens`(person)
- `26. Mai`(date)
- `Dorothea Akkaya`(person)
- `Mirko Hamidi`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_6`)


Die Mutter und die Kinder sind Staatsangehörige der Russischen Föderation und als Asylwerber im Inland aufhältig.

**False Positives:**

- `Die Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Vereinigtes Königreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_15`)


Ihr Geschäftsführer und ein von ihr beantragter Zeuge seien in Linz wohnhaft;

**False Positives:**

- `Ihr Geschäftsführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_47`)


Das Objekt, auf das sich der Rechtsstreit bezieht, ist in Wien gelegen, sodass auch ein Ortsaugenschein sowie die Befundaufnahme durch Sachverständige in Wien durchzuführen sind.

**False Positives:**

- `Das Objekt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_26`)


2. Der Rechtsfrage, ob es sich bei einem konkreten Verhalten um ein unleidliches Verhalten gemäß § 30 Abs 2 Z 3 MRG handelt, kommt keine erhebliche Bedeutung iSd § 502 ZPO zu (RIS-Justiz RS0042984), sofern das Berufungsgericht sich im Rahmen der von der Rechtsprechung herausgearbeiten Grundsätze gehalten hat.

**False Positives:**

- `Der Rechtsfrage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Anna Kisaoglu` — partial — pred is substring of gold: `Anna Kisaoglu, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_76`)


Das Löschungsgesuch, das eine genaue Bezeichnung der Liegenschaft zu enthalten hat, ist im Grundbuche durch eine Anmerkung ersichtlich zu machen.

**False Positives:**

- `Das Löschungsgesuch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_4`)


Vera Auer, Bakk. art. und 2.

**False Positives:**

- `Vera Auer` — partial — pred is substring of gold: `Vera Auer, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vera Auer, Bakk. art.`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_52`)


Die Frage, ob ein längeres Zuwarten mit der Verfolgung eines Anspruchs im Sinn des § 1497 ABGB noch hingenommen werden kann oder ob eine ungewöhnliche Untätigkeit vorliegt, aus der entnommen werden muss, dass es der Partei an dem erforderlichen Ernst zur Erreichung des Prozessziels fehlt, ist unter Berücksichtigung der Umstände des einzelnen Falls zu beantworten.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_16`)


Die Kinder, die ihren ständigen Aufenthalt in der Slowakei hätten, hätten daher Anspruch auf Unterhaltsvorschuss gemäß § 4 Z 3 UVG.

**False Positives:**

- `Die Kinder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_22`)


Der Bund, vertreten durch den Präsidenten des Oberlandesgerichts Wien, beantragt in seiner Revisionsrekursbeantwortung, den Revisionsrekurs zurückzuweisen bzw ihm keine Folge zu geben.

**False Positives:**

- `Der Bund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_35`)


2. Die Frage, ob bei Sachverhalten mit Unionsbezug österreichische Unterhaltsvorschüsse gebühren, ist daher seit 1. 5. 2010 wieder auf der Grundlage des § 2 UVG zu beurteilen, wobei allerdings bei der Anwendung dieser Bestimmung das europäische Primär- und Sekundärrecht nicht ausgeblendet werden darf (NeumayraaO § 1 UVG Rz 17 mwN).

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_24`)


Den Entschluss, den höheren Tarif einzustellen, habe die Beklagte erst nach dem Schreiben vom Juni 2023 gefasst, und eine unrichtige Information sei mit diesem Schreiben nicht erteilt worden.

**False Positives:**

- `Den Entschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10Ob23_14a`) (sent_id: `deanon_TRAIN/10Ob23_14a_38`)


Nach Lehre und Rechtsprechung wird diese Regelung über den Ausschluss einer anteiligen Rückzahlungspflicht auch auf den Eintritt sonstiger Endigungsgründe während des Monats - wie zB den Eintritt der Selbsterhaltungsfähigkeit - analog angewendet (vglStabentheinerinKletečka/Schauer, ABGB-ON1.02§ 1418 Rz 14;ReischauerinRummel, ABGB³ § 1418 Rz 3 jeweils mwN).

**False Positives:**

- `Nach Lehre` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_46`)


Der Umstand, dass der Vater nur geringe Einkommensteuern zahle, ändere nichts an der Anrechnung der Familienbeihilfe zu seinen Gunsten.

**False Positives:**

- `Der Umstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_105`)


Die Familienbeihilfe und der nach § 33 Abs 3 EStG gemeinsam ausgezahlte Kinderabsetzbetrag dienen bei gleichwertigen Betreuungsleistungen primär der Unterstützung der Betreuenden in finanzieller Sicht.

**False Positives:**

- `Die Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/10Ob26_10m`) (sent_id: `deanon_TRAIN/10Ob26_10m_4`)


Silvester Boetefuer, geboren am 12. Juli 1994, 2.) Annika Blumenstock, geboren am 28. Dezember 1998, und 3.) Lars Betschel, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Brockschnieder, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

**False Positives:**

- `Silvester Boetefuer` — partial — gold is substring of pred: `Boetefuer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boetefuer`(person)
- `Blumenstock`(person)
- `Betschel`(person)
- `Brockschnieder`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_8`)


Nach Punkt 5. dieses Vertrags ist er berechtigt, „gegen angemessene Bezahlung beliebig Trink- und Nutzwasser zu beziehen“.

**False Positives:**

- `Nach Punkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_41`)


Der Umstand, dass das Kind nicht im gemeinsamen Haushalt mit diesem Elternteil lebt, ist nicht relevant (10 Ob 18/22b mwN).

**False Positives:**

- `Der Umstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_45`)


Die Frage, ob die im Verwaltungsverfahren getroffene deklarative Feststellung der Flüchtlingseigenschaft des Kindes eine eigenständige Prüfung entbehrlich macht, hängt von zwei Faktoren ab, nämlich (primär) von der seither vergangenen Zeit aber auch davon, ob Anhaltspunkte für das Fortbestehen oder – aufgrund geänderter Verhältnisse – den Wegfall der Flüchtlingseigenschaft vorliegen.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_21`)


2. Der Gegenstand, über den das Rekursgericht in seinem Beschluss ON 76 entschieden hat, übersteigt im vorliegenden Fall hinsichtlich beider Unterhaltsberechtigter jeweils nicht 30.000 EUR: 2.1.

**False Positives:**

- `Der Gegenstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_41`)


Die Zweitklägerin und der Drittkläger haben in der Revisionsbeantwortung auf die Unzulässigkeit des gegnerischen Rechtsmittels hingewiesen.

**False Positives:**

- `Die Zweitklägerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_53`)


In Verfahren, die (auch) von Amts wegen eingeleitet werden können, ist das Rekursgericht an das Rekursbegehren nicht gebunden.

**False Positives:**

- `In Verfahren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_57`)


In Verfahren, die auch von Amts wegen eingeleitet werden können, gibt es jedoch keine Teilrechtskraft einer Entscheidung, weil das Rekursgericht (Revisionskursgericht) an das Antragsbegehren nicht gebunden ist und die Entscheidung auch zu Ungunsten des Rekurswerbers abgeändert werden kann (Fucik/Kloiber, AußStrG § 42 Rz 3, 4; siehe schon oben Pkt 1.1).

**False Positives:**

- `In Verfahren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_49`)


6. Die Frage, ob deutsches oder österreichisches Recht anwendbar sei, kann bei diesem Verständnis des § 5 Abs 2 KMG aF dahingestellt bleiben.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_46`)


6. Die Frage, ob deutsches oder österreichisches Recht anwendbar sei, kann bei diesem Verständnis des § 5 Abs 2 KMG aF dahingestellt bleiben.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

**False Positives:**

- `Fretzschner Medien` — type mismatch — same span as gold: `Fretzschner Medien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maschinenbau Heimfurtcon GmbH`(organisation)
- `Fretzschner Medien`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/10Ob88_19t`) (sent_id: `deanon_TRAIN/10Ob88_19t_9`)


Die Leine, an der der Hund festgebunden war, war ca ein Meter lang.

**False Positives:**

- `Die Leine` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/10Ob88_19t`) (sent_id: `deanon_TRAIN/10Ob88_19t_24`)


4. Welche Verwahrung und Beaufsichtigung durch den Tierhalter erforderlich ist, hängt von den Umständen des Einzelfalls ab (RS0030058).

**False Positives:**

- `Welche Verwahrung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_24`)


Dem Umstand, dass durch die Anstaltsunterbringung sein Lebensbedarf weitgehend gedeckt sei, werde dadurch Rechnung getragen, dass gemäß § 173 Abs 3 und Abs 4 BSVG 80 % seiner Pension inklusive Zuschlägen und Zulagen zur teilweisen Kostendeckung des Anstaltsaufenthalts herangezogen würden.

**False Positives:**

- `Dem Umstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_73`)


Der Erstattungskodex, der jene Heilmittel auflistet, die ohne die sonst notwendige chefärztliche Bewilligung verschrieben werden können, schränkt daher das Recht der Versicherten auf Krankenbehandlung mit Heilmitteln nicht ein.

**False Positives:**

- `Der Erstattungskodex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_125`)


Nr 1408/71 vorlagen (vgl auchNeumayr, Zum Klagebegehren und Urteilsspruch im sozialgerichtlichen Verfahren über Bescheidklagen, ÖJZ 2009, 1031 ff [1033]).

**False Positives:**

- `Zum Klagebegehren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_129`)


Auch in diesem Fall ist aber eine Feststellungsklage des Versicherten darüber, dass eine Leistungspflicht des Krankenversicherungsträgers (über den Gesamtvertrag und den Erstattungskodex hinaus) besteht, zulässig (vgl auchThaler/Plank, Heilmittel und Komplementärmedizin aaO 187;Rebhahn, Die Bereitstellung von Arzneimitteln, inGrillberger/Mosler[Hrsg], Europäisches Wirtschaftsrecht und soziale Krankenversicherung [2003] 209 ff [228]).

**False Positives:**

- `Europäisches Wirtschaftsrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_34`)


3. Die Frage, ob eine Versicherte Berufsschutz genießt, ist von Amts wegen zu prüfen.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Susanne Schueßler` — partial — gold is substring of pred: `Schueßler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Beinicke`(person)
- `Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Co KG`(organisation)
- `Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 36** (doc_id: `deanon_TRAIN/12Os40_19b`) (sent_id: `deanon_TRAIN/12Os40_19b_9`)


Die Konstatierung, wonach der Nichtigkeitswerber Emily Gerdsmann während der Gewaltanwendung wiederholt aufforderte, ihm Geld zu geben (US 3), hat das Erstgericht dem der Sache nach erhobenen Einwand der Unvollständigkeit (Z 5 zweiter Fall) zuwider unter Berücksichtigung der Verantwortung des Beschwerdeführers und der Angaben des Zeugen Tobias Kozel aus den Aussagen des Tatopfers vor der Polizei (ON 2 S 27) und in der Hauptverhandlung (ON 27 S 5) erschlossen.

**False Positives:**

- `Die Konstatierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gerdsmann`(person)
- `Kozel`(person)

**Example 37** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_7`)


Danach hat er in Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich und an anderen Orten 1) am 15. Februar 2014 Asli Davidsmeyer mit Gewalt zur Duldung des Analverkehrs genötigt, indem er sie auf ein Bett stieß, im Nacken festhielt und gegen ihren Willen seinen Penis in ihren After einführte, 2) durch im Urteil bezeichnete Handlungen und Äußerungen längere Zeit hindurch gegen andere Personen fortgesetzt Gewalt ausgeübt, und zwar a) ab dem 1. Juni 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014 gegen Asli Dagtekin, b) ab dem Jahr 2012 bis zum 19. November 2014, also länger als ein Jahr, gegen seine am 25. April 2008 geborene, somit unmündige, Tochter Berfin Krempl, sowie c) ab dem Jahr 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014, also länger als ein Jahr, gegen seinen am 18. Juni 2003 geborenen, somit unmündigen, Sohn Ilhan Kukolies, 3) Asli Dücking durch im Urteil bezeichnete Handlungen vorsätzlich am Körper verletzt, und zwar a) im September 2008, wodurch die Genannte Schwellungen und Hämatome erlitt, und b) zwischen September und November 2008, wodurch die Genannte das Bewusstsein verlor und eine Schwellung am Hinterkopf und Rötungen im Kniebereich erlitt, weiters Asli Dietzler durch im Urteil bezeichnete Äußerungen 4) zwischen September und November 2008 zu einer Unterlassung genötigt und 5) am 9. Februar 2017 zumindest mit einer Verletzung am Körper gefährlich bedroht, um sie in Furcht und Unruhe zu versetzen.

**False Positives:**

- `Tochter Berfin Krempl` — partial — gold is substring of pred: `Krempl`
- `Sohn Ilhan Kukolies` — partial — gold is substring of pred: `Kukolies`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich`(address)
- `Davidsmeyer`(person)
- `Dagtekin`(person)
- `Krempl`(person)
- `Kukolies`(person)
- `Dücking`(person)
- `Dietzler`(person)

**Example 38** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__12`)


Das Urteil und der Beschluss des Landesgerichts Innsbruck vom 10. Jänner 2012 erwuchsen sogleich in Rechtskraft (ON 49 S 4), wurden aber nicht (durch eine entsprechende Strafvollzugsanordnung) in Vollzug gesetzt.

**False Positives:**

- `Das Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__12`)


Der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts steht - wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend aufzeigt - mit den im Spruch genannten Bestimmungen der Kaiserlichen Verordnung nicht in Einklang: 1. Vorweg ist festzuhalten, dass sich diese - nach wie vor in Geltung stehende (vgl Anhang [Indexzahl 14.02.04] zum Ersten BundesrechtsbereinigungsG, BGBl I 1999/191) - Verordnung unmittelbar auf das Staatsgrundgesetz vom 21. Dezember 1867 RGBl 1867/141 stützt, es sich somit um eine verfassungsunmittelbare Verordnung handelt, die nach ausdrücklicher Anordnung des § 14 dieses Staatsgrundgesetzes Gesetzeskraft hat (zum Rang vergleichbarer Notverordnungen des Bundespräsidenten [Art 18 Abs 3 bis 5 B-VG] im Stufenbau der geltenden RechtsordnungRaschauerinKorinek/Holoubek, B-VG Art 18/3-5 Rz 1 und 10;Mayer, Die Verordnung, 39 f;Aichlreiter, Österreichisches Verordnungsrecht, 905 ff und 1151 f; vgl zum Gesetzesbegriff des § 23 StPORatz, WK-StPO § 292 Rz 12).

**False Positives:**

- `Die Verordnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__33`)


11. Sollten Staatsanwaltschaft und Angeklagter ihr Einverständnis im Sinn der genannten Bestimmungen erklären, wäre das (durch einen anderen Richter) ausgefertigte Urteil den Parteien neuerlich zuzustellen, wodurch die Frist zur Ausführung angemeldeter Rechtsmittel erneut in Gang gesetzt würde.

**False Positives:**

- `Sollten Staatsanwaltschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/14Os108_18s`) (sent_id: `deanon_TRAIN/14Os108_18s_21`)


Die Feststellungen, nach denen sich die vier Angeklagten mit weiteren unbekannten Tätern bewusst und gewollt zumindest für einige Wochen zusammenschlossen, um in Österreich – in wechselnder Besetzung – gemeinsam Einbruchsdiebstähle in Wohnstätten zu begehen, und auch der Beschwerdeführer die ihm zur Last gelegten beiden Taten mit darauf gerichtetem Vorsatz im Rahmen dieser kriminellen Vereinigung unter Mitwirkung anderer Mitglieder derselben beging (US 8, 11, 16), beruhen entgegen dem weiteren Vorwurf der Mängelrüge nicht auf bloßen „Spekulationen“ und „durch nichts untermauerten Annahmen“ (Z 5 vierter Fall).

**False Positives:**

- `Die Feststellungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/14Os121_19d`) (sent_id: `deanon_TRAIN/14Os121_19d_12`)


Der Beschwerdeeinwand, der Schöffensenat habe die Begründung der in der Hauptverhandlung getroffenen Entscheidung gesetzwidrig den Urteilsgründen vorbehalten, trifft zwar zu (ON 15 S 100, US 6).

**False Positives:**

- `Der Beschwerdeeinwand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_13`)


Die Kritik, die Feststellung, die Beschwerde-führerin habe dem Opfer – von diesem unbemerkt – unbekannte Mengen des Wirkstoffs „Prothipendyl“ (der später in einer „hochtoxischen Konzentration“ im Blut des Opfers nachgewiesen werden konnte) in dessen Getränk gemischt, sei offenbar unzureichend begründet (Z 5 vierter Fall), nimmt bloß eine einzige Urteilspassage (US 14 zweiter Absatz) ins Visier und verfehlt damit die gebotene Bezugnahme auf die Gesamtheit der Entscheidungsgründe (RIS-Justiz RS0119370).

**False Positives:**

- `Die Kritik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_15`)


Die Behauptung, es fehlten Feststellungen dazu, dass sich die (unterdrückten) Urkunden im Tatzeitpunkt in der Plastikhülle befunden hätten (der Sache nach Z 9 lit a), übergeht die genau dazu getroffenen Konstatierungen (US 7; RIS-Justiz RS0099810).

**False Positives:**

- `Die Behauptung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in Punkt A./2./ des Schuldspruchs sowie im Strafausspruch aufgehoben und es wird die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

**False Positives:**

- `Das Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_13`)


Im Urteilstenor, der im Fall einer gemäß § 270 Abs 4 StPO gekürzten Urteilsausfertigung die fehlenden Entscheidungsgründe als Bezugspunkt für die materiell-rechtliche Beurteilung ersetzt, ist sohin auszusprechen, welcher Tat der Angeklagte schuldig befunden worden ist, und zwar unter ausdrücklicher Bezeichnung der einen bestimmten Strafsatz bedingenden Tatumstände, worunter nichts anderes zu verstehen ist, als die für die Subsumtion entscheidenden Tatsachen (§ 260 Abs 1 Z 1 StPO; RIS-Justiz RS0125764).

**False Positives:**

- `Im Urteilstenor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_4`)


Das Urteil, das im Übrigen unberührt bleibt, wird im Schuldspruch A, demgemäß auch im Gerhard Oeste betreffenden Strafausspruch, aufgehoben und in diesem Umfang in der Sache selbst erkannt: Gerhard Opderbecke wird gemäß § 259 Z 3 StPO vom Vorwurf freigesprochen, er habe in Aichbach 59, 9131 Zapfendorf, Österreich A/ als Bürgermeister der Gemeinde Krautz, mithin als Beamter im strafrechtlichen Sinn, „mit dem Vorsatz, die Gemeinderäte der Gemeinde Kießlich an ihren Rechten gemäß §§ 28 Abs 1 und 2, 35 Abs 1, 78 Abs 1a K-AGO auf Einberufung des Gemeinderates und Behandlung von Erledigungen, die der Beschlussfassung durch den Gemeinderat vorbehalten waren, zu schädigen“, wiederholt seine Befugnis, im Namen der Gemeinde Klingenschmid als deren Organ in Vollziehung der Gesetze Amtsgeschäfte vorzunehmen, wissentlich missbraucht, indem er es unterließ, „Sitzungen des Gemeinderates zur Beschlussfassung über nachangeführte Geschäftsgänge und über die Adaptierung der Nebengebührenverordnung der Gemeinde einzuberufen, darüber einen Tagesordnungspunkt in einer Gemeinderatssitzung anzusetzen und hierfür Sitzungsvorträge nach § 78 K-AGO ausarbeiten zu lassen und indem er die entsprechenden Punkte mehrfach von der Tagesordnung der Gemeinderatssitzungen strich“, und zwar I/ zwischen 1. Juli 2010 und März 2015 über die Bestellung von Renate Dal zur Amtsleiterstellvertreterin und über die Gewährung einer monatlichen Mehrleistungszulage und Aufwandsent-schädigung für diese Funktion, „wodurch der Gemeinde Khatib ein Schaden im Gesamtbetrag von zumindest insgesamt 25.302,76 Euro inklusive Dienstgeberabgaben entstand“;

**False Positives:**

- `Das Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oeste`(person)
- `Opderbecke`(person)
- `Aichbach 59, 9131 Zapfendorf, Österreich`(address)
- `Krautz`(person)
- `Kießlich`(person)
- `Klingenschmid`(person)
- `Dal`(person)
- `Khatib`(person)

**Example 48** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_13`)


3/ von 1. Juli 2010 bis 31. Dezember 2012 der Finanzverwalterin der Gemeinde Kusznerus, Renate Heister, eine Finanzverwalterzulage von insgesamt 6.054,81 Euro brutto anweisen ließ, obwohl eine solche Zulage in den Nebengebührenverordnungen des Landes oder der Gemeinde nicht vorgesehen war und er keine Beschlussfassung des Gemeinderats eingeholt hatte, wodurch der Gemeinde Kestelyn ein Schaden von 7.522,50 Euro inklusive Dienstgeberabgaben entstand;

**False Positives:**

- `Renate Heister` — partial — gold is substring of pred: `Heister`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kusznerus`(person)
- `Heister`(person)
- `Kestelyn`(person)

**Example 49** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_20`)


Nach dem Urteilssachverhalt handelte es sich bei Mag. (FH) Nicole Kuechle, Renate Deudeloff und Renate Herbst um Vertragsbedienstete, ab 1. Jänner 2013 (teilweise) um Gemeindemitarbeiterinnen, deren Dienstverhältnis zur Gemeinde Klementz (im Tatzeitraum) also durchwegs privatrechtlicher Natur war.

**False Positives:**

- `Renate Deudeloff` — partial — gold is substring of pred: `Deudeloff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuechle`(person)
- `Deudeloff`(person)
- `Herbst`(person)
- `Klementz`(person)

**Example 50** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_9`)


Die Abwasserbeseitigung und Wasserversorgung sei im öffentlichen Interesse gelegen.

**False Positives:**

- `Die Abwasserbeseitigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_28`)


Ein Bescheid, der dem Kläger oder dessen Rechtsvorgängern eine Duldungspflicht nach dem Niederösterreichischen Kanalgesetz 1977 in der damals geltenden Fassung oder dem Wasserrechtsgesetz auferlegte, liegt nicht vor.

**False Positives:**

- `Ein Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_29`)


Der Fall, dass ein Scheidungsfolgenvergleich deswegen unvollständig blieb, weil ein Ehegatte an das Vorhandensein von ehelichen Ersparnissen nicht denken konnte (RIS-Justiz RS0008464) oder er in Bezug auf einzelne Vermögensbestandteile in Unkenntnis war (RIS-Justiz RS0008463), liegt hier nicht vor.

**False Positives:**

- `Der Fall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_5`)


Isidor Saurwein, BA, alle vertreten durch die Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH, Wien, wegen Feststellung und Räumung, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2020, GZ 2 R 122/20d-54, mit dem das Urteil des Landesgerichts Wels vom 27. Juli 2020, GZ 2 Cg 84/18g-47, in der Hauptsache bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Isidor Saurwein` — partial — pred is substring of gold: `Isidor Saurwein, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isidor Saurwein, BA`(person)

**Example 54** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_52`)


Die Auffassung, die festgestellten Handlungen ließen für diesen eingeschränkt nutzbaren Bereich objektiv die Ausübung des Vollrechts Eigentum erkennen, ist nicht korrekturbedürftig, kommt doch hier eine intensivere Nutzung kaum in Betracht.

**False Positives:**

- `Die Auffassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_69`)


Die Revision, die insgesamt keine erhebliche Rechtsfrage aufzeigt, ist damit zurückzuweisen.

**False Positives:**

- `Die Revision` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/1Ob142_19t`) (sent_id: `deanon_TRAIN/1Ob142_19t_94`)


Der Garten und sein Äquivalent (der klar abgrenzbare Verkaufserlös) wären damit nicht der Aufteilung unterlegen (§ 82 Abs 1 EheG; RS0057322).

**False Positives:**

- `Der Garten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hong Kong` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Amber Baraniak`(person)
- `Mag. Liliana Bößer`(person)

**Example 58** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_31`)


Der Umstand, dass die Klägerin ihr Rechtsmittel ausschließlich auf den Revisionsgrund der Mangelhaftigkeit (§ 503 Z 2 ZPO) stützt, schadet nicht, weil ihre Rechtsmittelausführungen auch eine Rechtsrüge nach § 503 Z 4 ZPO erkennen lassen (vgl RS0041851).

**False Positives:**

- `Der Umstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_38`)


[11] 2.2. Ein Vorbringen, dass die Rechnungslegung erforderlich gewesen wäre, weil der Kaufpreis bzw die Forderungen bei Ablieferung nicht feststanden, hat die Klägerin ebenso wenig erstattet wie ein Vorbringen zu einer abweichenden Vereinbarung über die Zahlungsfrist oder zum Vorliegen eines Kontokorrentverhältnisses (§ 355 UGB).

**False Positives:**

- `Ein Vorbringen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_33`)


Dem Argument, die Unwirksamkeit des gesamten Kreditvertrags ergebe sich daraus, dass ohne die erste der beanstandeten „Konvertierungsklauseln“ die genaue Kreditsumme nicht feststellbar sei, weil dazu bloß ein „Gegenwert“ in Euro vereinbart worden sei, ist entgegenzuhalten, dass im ursprünglichen Kreditvertrag ein fixer Wechselkurs individuell vereinbart wurde.

**False Positives:**

- `Dem Argument` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_35`)


Die Beurteilung, ob eine Klausel den Vertragspartner gröblich benachteiligt, hat sich am dispositiven Recht als dem Leitbild eines ausgewogenen und gerechten Interessenausgleichs zu orientieren (RS0014676 [T7, T13, T43]).

**False Positives:**

- `Die Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_112`)


Auch die hier von der Klägerin beanstandeten Klauseln verpflichten den Verbraucher nicht nur zur Zahlung einer Kreditbearbeitungsgebühr (Klausel 2), sondern sehen auch weitere Entgelte in Form von Erhebungsspesen (Klausel 20), Auslagenersatz Porti und Drucksorten (Klausel 21), Auslagenersatz Porti und Druckkosten (Ident.Brief) (Klausel 22) und Überweisungsspesen (Klausel 23) vor.

**False Positives:**

- `Auslagenersatz Porti` — no gold match — likely missing annotation
- `Auslagenersatz Porti` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 63** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_136`)


Die Gründe, die eine Änderung der AGB zulassen würden, seien in der Klausel taxativ und klar verständlich angeführt.

**False Positives:**

- `Die Gründe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_144`)


Die Parameter, die für eine Entgelterhöhung mittels Zustimmungsfiktion eine Rolle spielen, müssen aus der Klausel selbst hervorgehen, damit diese dem Transparenzgebot entspricht (RS0132022;

**False Positives:**

- `Die Parameter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_14`)


Der Beklagte, der von der Klägerin von diesem Termin verständigt worden war, nahm an der Verhandlung nicht teil.

**False Positives:**

- `Der Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/1Ob186_16h`) (sent_id: `deanon_TRAIN/1Ob186_16h_7`)


Der Erstbeklagte, der nur etwa eine Armlänge von ihr entfernt war, bemerkte aus dem Augenwinkel, dass im Nahbereich ein Schifahrer mit großen Tempo von oben kommend auf die beiden zufuhr.

**False Positives:**

- `Der Erstbeklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/1Ob234_19x`) (sent_id: `deanon_TRAIN/1Ob234_19x_25`)


Die Frage, welchen rechtlich erheblichen Inhalt eine gerichtliche Entscheidung hat, ist eine Rechtsfrage, die aufgrund des Wortlauts des Spruchs und der Gründe der Entscheidung in Verbindung mit dem dadurch angewandten Gesetz gelöst werden muss (1 Ob 74/19t mwN).

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_22`)


Die Beurteilung, dass er nach der Aufkündigung kein Verhalten setzte, dass bei einer im Einzelfall allenfalls gebotenen Gesamtwürdigung zu seinen Gunsten mitberücksichtigt werden hätte können (dazu RS0070378), zieht der Beklagte zu Recht ohnedies nicht in Zweifel.

**False Positives:**

- `Die Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_27`)


Die Beweiswürdigung und damit die Tatsachenfeststellungen können vom Obersten Gerichtshof, der ausschließlich Rechtsinstanz ist (vgl RS0123663), aber nicht überprüft werden.

**False Positives:**

- `Die Beweiswürdigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_55`)


Die Tatsache, dass der Mann seit Aufhebung der ehelichen Gemeinschaft aus danach erwirtschafteten Geldmitteln die Rückzahlungsraten beim Bauspardarlehen alleine getragen hatte, berücksichtigte das Rekursgericht nicht.

**False Positives:**

- `Die Tatsache` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_34`)


Die Frage, ob der Sicherungspflichtige die im Wesentlichen von der konkreten örtlichen Situation abhängigen zumutbaren Maßnahmen unterlassen hat, stellt wegen ihrer Einzelfallbezogenheit regelmäßig keine Rechtsfrage von erheblicher Bedeutung dar (1 Ob 41/00m) und kann daher - von Fällen krasser Fehlbeurteilung abgesehen - die Zulässigkeit der Revision nicht rechtfertigen (vgl RIS-Justiz RS0044088 [T35 und T42]).

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/1Ob57_16p`) (sent_id: `deanon_TRAIN/1Ob57_16p_4`)


Der Antragsgegner und Gegner der gefährdeten Partei ist schuldig, der Antragstellerin und gefährdeten Partei binnen 14 Tagen die mit 1.098 EUR (darin 183 EUR USt) bestimmten Kosten des Revisionsrekursverfahrens binnen 14 Tagen zu ersetzen.

**False Positives:**

- `Der Antragsgegner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_24`)


Wegen Punkt 1. des Kreditvertrags werde die Fremdwährungsschuld in Schweizer Franken erst auf Grundlage des von der Beklagten selbst gebildeten Devisengeldkurses errechnet.

**False Positives:**

- `Wegen Punkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Person with Complex Academic Titles`

**F1:** 0.159 | **Precision:** 0.204 | **Recall:** 0.130  

**Format:** `regex`  
**Rule ID:** `f96ee46b`  
**Description:**
Captures names preceded by complex German academic titles, ensuring the full name including the title is captured if it's a compound entity, or just the name if the title is separate. Handles specific complex suffixes like 'Bakk. rer. nat. Bakk. iur..net'.

**Content:**
```
(?:Dr\.|Mag\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Dipl\.-Ing\.|Ing\.|Techn\sR|StR|OStR|MR|\u00d6kR|KommR|VetR|LLM|LLB|Bakk\.\s+rer\.\s+nat\.|Bakk\.\s+techn\.|Bakk\.\s+phil\.|MSc|MA|BA|PhD|PhD\s+OMedR|Mag\.\s+a|Dr\.\s+a|Hon\.-Prof\.\s+in|Priv\.-Doz\.\s+in|DDr\.|RgR|MMM\.?|MMM\.\s+a|DI\.|MMag\.|MMag\.\s+a|OSR\.|KzlR\.|MedR\.|BEd\.|Bakk\.\s+art\.|Dr\.\s+in|Mag\.\s+in|Prof\.\s+in|Univ\.-Prof\.\s+in|Priv\.-Doz\.\s+in|Dipl\.-Ing\.\s+in|Ing\.\s+in|Techn\sR\s+in|StR\s+in|OStR\s+in|MR\s+in|\u00d6kR\s+in|KommR\s+in|VetR\s+in|LLM\s+in|LLB\s+in|Bakk\.\s+rer\.\s+nat\.\s+in|Bakk\.\s+techn\.\s+in|Bakk\.\s+phil\.\s+in|MSc\s+in|MA\s+in|BA\s+in|PhD\s+in|PhD\s+OMedR\s+in|Mag\.\s+a\s+in|Dr\.\s+a\s+in|Hon\.-Prof\.\s+in\s+in|Priv\.-Doz\.\s+in\s+in|DDr\.\s+in|RgR\s+in|MMM\.?\s+in|MMM\.\s+a\s+in|DI\.\s+in|MMag\.\s+in|MMag\.\s+a\s+in|OSR\.\s+in|KzlR\.\s+in|MedR\.\s+in|BEd\.\s+in|Bakk\.\s+art\.\s+in)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+von\s+[A-Z][a-zäöüß]+)?(?:\s+Bakk\.\s+rer\.\s+nat\.\s+Bakk\.\s+iur\.\.net)?\s*(?!Inhaber|Bank|GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+Inhaber|\s+Bank|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.204 | 0.130 | 0.159 | 876 | 179 | 697 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 179 | 697 | 1196 |

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

**Example 1** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Gregor Ruemmel` | `OStR Gregor Ruemmel` |

**Missed by this rule (FN):**

- `Sten und Stöwer Wind GmbH` (organisation)
- `OMedR Torsten Münchmeyer` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `PhD Ignaz Nardelli` | `PhD Ignaz Nardelli` |

**Missed by this rule (FN):**

- `Diethard Eisenlöffel, Bakk. phil.` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Lynn Forkarth` | `Dipl.-Ing. Lynn Forkarth` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)
- `Mur Kraftalheim Holding GmbH` (organisation)
- `Gerald Zacharie` (person)
- `Nexstein Textil GmbH` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Adam Kratki` | `Mag. Adam Kratki` |

**Missed by this rule (FN):**

- `Alsteinost GmbH` (organisation)
- `Anna Kisaoglu, Bakk. iur.` (person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Elmar Janaschek` | `Mag. Elmar Janaschek` |
| `VetR Charlotte Eissenmann` | `VetR Charlotte Eissenmann` |

**Example 6** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `VetR Lukas Dickhaus` | `VetR Lukas Dickhaus` |

**Missed by this rule (FN):**

- `Isidor Janofske` (person)
- `Wolfram Fritzsche` (person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Ing. Janis Grottian` | `Ing. Janis Grottian` |

**Missed by this rule (FN):**

- `Miranda Klagemann` (person)
- `DI Adolf Kowallek` (person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Egon Luckow, geboren am 1. August 2011, und des mj Priv.-Doz. Samuel Prestle, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Samuel Prestle` | `Priv.-Doz. Samuel Prestle` |

**Missed by this rule (FN):**

- `Egon Luckow` (person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Dr. Ariadne Graspointner` | `Dr. Ariadne Graspointner` |

**Missed by this rule (FN):**

- `Walter Gritzmacher` (person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `VetR Herbert Dedert` | `VetR Herbert Dedert` |

**Missed by this rule (FN):**

- `Monsud-Textil GmbH` (organisation)

**Example 11** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


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

**Example 12** (doc_id: `deanon_TRAIN/10Ob28_17s`) (sent_id: `deanon_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Jaroslaw Mlynarik, geboren am 1. Juli 2009, wegen Kontaktrechts des Vaters Dr. Eckard Tschernig, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Bettina Makswietat, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Dr. Eckard Tschernig` | `Dr. Eckard Tschernig` |
| `Dr. Bettina Makswietat` | `Dr. Bettina Makswietat` |

**Missed by this rule (FN):**

- `Jaroslaw Mlynarik` (person)
- `1. Juli 2009` (date)
- `Partner KG` (organisation)

**Example 13** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `PhD Karim Trieber` | `PhD Karim Trieber` |
| `StR Lara Jungnikl` | `StR Lara Jungnikl` |

**Missed by this rule (FN):**

- `Calvin Mützlaff` (person)
- `Volker Scheffski` (person)
- `Jaden Jurkutaitis` (person)
- `8. Dezember 1982` (date)
- `11. Januar 1975` (date)
- `RgR Dipl.-Ing. Quirin Bagemühl` (person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Arielle Schallmair, gegen die beklagte Partei Dr. Daisy Nagelkrämer, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Daisy Nagelkrämer` | `Dr. Daisy Nagelkrämer` |

**Missed by this rule (FN):**

- `Arielle Schallmair` (person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Eugenia Welze` | `Ing. Eugenia Welze` |

**Missed by this rule (FN):**

- `Helge Monhemius, Bakk. techn.` (person)

**Example 16** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Jakob Krägeloh, geboren am 9. Juli 2019, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1.

| Predicted | Gold |
|---|---|
| `Dr. Jakob Krägeloh` | `Dr. Jakob Krägeloh` |

**Missed by this rule (FN):**

- `9. Juli 2019` (date)

**Example 17** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_4`)


Dr. Emmerich Schrammen, Niederlande, und 3.)

| Predicted | Gold |
|---|---|
| `Dr. Emmerich Schrammen` | `Dr. Emmerich Schrammen` |

**Example 18** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_5`)


Dr. Torsten Classe, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Jaqueline Ratzenböck, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Torsten Classe` | `Dr. Torsten Classe` |

**Missed by this rule (FN):**

- `Jaqueline Ratzenböck` (person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_5`)


Text Begründung: Mit Beschluss vom 14. 3. 2013, GZ 3 Pu 61/12x-40, verpflichtete das Erstgericht den Vater der minderjährigen Mathias Weinschrod und des minderjährigen PhD Regina Milbradt, ab 1. 3. 2012 einen monatlichen Unterhaltsbeitrag von 75 EUR für Enrico Weffers und von 55 EUR für Veit Mazzei zu leisten;

| Predicted | Gold |
|---|---|
| `PhD Regina Milbradt` | `PhD Regina Milbradt` |

**Missed by this rule (FN):**

- `Mathias Weinschrod` (person)
- `Enrico Weffers` (person)
- `Veit Mazzei` (person)

**Example 20** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Pablo Ebling, geboren am 9. August 1991, Hugo Stegemann, geboren am 30. September 1992, mj Delila Ringsdorff, geboren am 22. Dezember 1998 und mj Nigel Conrades, Bakk. techn. BEd, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Vivian Hadamzick, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Vivian Hadamzick` | `Mag. Vivian Hadamzick` |

**Missed by this rule (FN):**

- `Pablo Ebling` (person)
- `Hugo Stegemann` (person)
- `Delila Ringsdorff` (person)
- `Nigel Conrades, Bakk. techn. BEd` (person)

**Example 21** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Marlon Richel` | `Dr. Marlon Richel` |

**Missed by this rule (FN):**

- `Freimut & Assenov Sicherheit GmbH` (organisation)
- `Spazgasse 41, 8524 Greim, Österreich` (address)

**Example 22** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Techn R Heidrun Imai, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Techn R Heidrun Imai` | `Techn R Heidrun Imai` |

**Example 23** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `OStR Esra Jakubait` | `OStR Esra Jakubait` |

**Example 24** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_5`)


Zeno Thulcke, 2. Christine Adomadt, erstklagende Partei vertreten durch die Erwachsenenvertreterin Mag. Elfriede Melichar, Rechtsanwältin in Mödling, wider die beklagte Partei Dr. Benjamin Görmar, wegen Schadenersatz, hier wegen Verfahrenshilfe, über den „Rekurs“ (richtig: Revisionsrekurs) der zweitklagenden Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 21. Juli 2023, GZ 18 R 96/23f, 97/23b, 98/23z-31, womit der Beschluss des Bezirksgerichts Mödling vom 10. Mai 2023, GZ 3 C 1057/21v-25, hinsichtlich der erstklagenden Partei bestätigt und der von der zweitklagenden Partei dagegen erhobene Rekurs zurückgewiesen wurde, sowie der Rekurs der klagenden Parteien gegen den Beschluss des Bezirksgerichts Mödling vom 28. März 2023, GZ 3 C 1057/21v-20, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Benjamin Görmar` | `Dr. Benjamin Görmar` |

**Missed by this rule (FN):**

- `Zeno Thulcke` (person)
- `Christine Adomadt` (person)

**Example 25** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

| Predicted | Gold |
|---|---|
| `ÖkR Nikolaus Buksbaum` | `ÖkR Nikolaus Buksbaum` |

**Missed by this rule (FN):**

- `See-Versand Werke GmbH` (organisation)
- `Robert Leis` (person)
- `Dargatz+Boedewig Telekom GmbH` (organisation)

**Example 26** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `KommR Franz Kubank` | `KommR Franz Kubank` |

**Missed by this rule (FN):**

- `Laurin Aichhorn` (person)
- `Timothy Schulmeister` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 27** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dr. Alice Wickertsheimer, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Dr. Alice Wickertsheimer` | `Dr. Alice Wickertsheimer` |

**Example 28** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralph Kreidenweiß` | `Dr. Ralph Kreidenweiß` |

**Missed by this rule (FN):**

- `Donau-Automotive GmbH` (organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 29** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Jeannette Scherl, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Selina Dorfmeyer, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Jeannette Scherl` | `Mag. Jeannette Scherl` |

**Missed by this rule (FN):**

- `Selina Dorfmeyer` (person)

**Example 30** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Franziska Gonschorek, vertreten durch die Huber & Partner Rechtsanwälte GmbH, Linz, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Franziska Gonschorek` | `Mag. Franziska Gonschorek` |

**Example 31** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Lilia Anderßon` | `Mag. Lilia Anderßon` |

**Missed by this rule (FN):**

- `Angelina Töpker` (person)
- `Ronja Straßgschwandtner` (person)
- `Vanek und Eloy Analyse GmbH` (organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich` (address)

**Example 32** (doc_id: `deanon_TRAIN/1Ob142_19t`) (sent_id: `deanon_TRAIN/1Ob142_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der Antragstellerin Mag. Liu Cingöz, vertreten Dr. Brigitte Birnbaum und Dr. Rainer Toperczer, Rechtsanwälte in Wien, gegen den Antragsgegner Dr. Torsten Erlautzki, vertreten durch die Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse gemäß §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 9. Juli 2019, GZ 45 R 554/18f-162, mit dem der Beschluss des Bezirksgerichts Fünfhaus vom 25. Oktober 2018, GZ 4 Fam 68/14k-156, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Der Revisionsrekurs des Antragsgegners wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Liu Cingöz` | `Mag. Liu Cingöz` |
| `Dr. Torsten Erlautzki` | `Dr. Torsten Erlautzki` |

**Example 33** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Amber Baraniak` | `VetR Amber Baraniak` |
| `Mag. Liliana Bößer` | `Mag. Liliana Bößer` |

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

**Example 2** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

**False Positives:**

- `Priv.-Doz. Sven Egerth` — partial — pred is substring of gold: `ÖkR Priv.-Doz. Sven Egerth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Priv.-Doz. Sven Egerth`(person)
- `3. Mai`(date)
- `Bezirksgericht Graz`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mag. Alexander Rimser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `OStR Gregor Ruemmel`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Dr. Carl Benkhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Tschiggfreystraße 46, 3240 Loitsdorf, Österreich, wohnhaft gewesenen Manfred Johann Pingert, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Czychy, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tschiggfreystraße 46, 3240 Loitsdorf, Österreich`(address)
- `Pingert`(person)
- `Czychy`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


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

**Example 7** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Franz Podovsovnik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Dr. Erich Kafka ` — no gold match — likely missing annotation
- `Dr. Manfred Palkovits` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Wilhelm Schlein Rechtsanwalt Gmb` — no gold match — likely missing annotation
- `Dr. Werner Goeritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `DI Fabian Reifrath`(person)
- `Elina Woyte`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Alois Schneider` — no gold match — likely missing annotation
- `Dr. Walter Hausberger` — no gold match — likely missing annotation
- `Dr. Katharina Moritz ` — no gold match — likely missing annotation
- `Dr. Alfred Schmidt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob11_15p`) (sent_id: `deanon_TRAIN/10Ob11_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte und Hofrätinnen Univ.-Prof. Dr. Neumayr, Dr. Schramm, Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Viktoria Hornburg, vertreten durch Dr. Walter Vasoll und Mag. Marion Vasoll, Rechtsanwälte in Hermagor, gegen die beklagte Partei Mercedes Jungschlaeger, vertreten durch Dr. Thomas Romauch, Rechtsanwalt in Wien, wegen Feststellung und Einwilligung (6.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 4. Dezember 2014, GZ 3 R 169/14h-14, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Hermagor vom 9. August 2014, GZ 1 C 563/13b-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Dr. Walter Vasoll ` — no gold match — likely missing annotation
- `Mag. Marion Vasoll` — no gold match — likely missing annotation
- `Dr. Thomas Romauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Viktoria Hornburg`(person)
- `Mercedes Jungschlaeger`(person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_6`)


Text Entscheidungsgründe: Über Vermittlung der Beklagten und nach Beratung durch deren Mitarbeiter Ing. Vivian Wenz erwarb die Klägerin im Mai 2007 um 20.000 EUR Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Ing. Vivian Wenz ` — partial — gold is substring of pred: `Ing. Vivian Wenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Vivian Wenz`(person)

**Example 13** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_7`)


Als sie einen Kursverfall dieser Aktien 2008/2009 zu einem nicht mehr näher feststellbaren Zeitpunkt wahrnahm, stellte sie erstmals fest, dass sie mit diesen Aktien ein Finanzprodukt erworben hatte, das weder dem Inhalt der Beratung des Ing. Dietrich Worell noch vom Risiko und der Risikostreuung im „Portfolio“ her dem entsprach, was sie 2007 hatte erwerben wollen.

**False Positives:**

- `Ing. Dietrich Worell ` — partial — gold is substring of pred: `Ing. Dietrich Worell`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Dietrich Worell`(person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Miklos Wiederaenders im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Ing. Miklos Wiederaenders ` — partial — gold is substring of pred: `Ing. Miklos Wiederaenders`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Miklos Wiederaenders`(person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Andreas Ladstätter` — no gold match — likely missing annotation
- `Dr. Walter Schuhmeister ` — no gold match — likely missing annotation
- `Mag. Franz Haydn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Miranda Klagemann`(person)
- `DI Adolf Kowallek`(person)
- `Ing. Janis Grottian`(person)

**Example 16** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Birgit Lajtai` — no gold match — likely missing annotation
- `Dr. Robert Kugler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Walter Gritzmacher`(person)
- `Dr. Ariadne Graspointner`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob16_16z`) (sent_id: `deanon_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Josepha Mikolajetz, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Erhard Arslanboga, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Clemens Lintschinger` — no gold match — likely missing annotation
- `Dr. Georg Backhausen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Josepha Mikolajetz`(person)
- `Erhard Arslanboga`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Walter Reichholf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Paul Vavrovsky ` — no gold match — likely missing annotation
- `Mag. Christian Schrott` — no gold match — likely missing annotation
- `Dr. Katharina Sedlazeck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Steintra Solar GmbH`(organisation)
- `Kospachstraße 35, 3162 Rainfeld, Österreich`(address)
- `Umwelt Dorfwald ges.m.b.H.`(organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich`(address)

**Example 20** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


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

**Example 21** (doc_id: `deanon_TRAIN/10Ob26_10m`) (sent_id: `deanon_TRAIN/10Ob26_10m_4`)


Silvester Boetefuer, geboren am 12. Juli 1994, 2.) Annika Blumenstock, geboren am 28. Dezember 1998, und 3.) Lars Betschel, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Brockschnieder, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

**False Positives:**

- `Mag. Anton Brockschnieder` — partial — gold is substring of pred: `Brockschnieder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boetefuer`(person)
- `Blumenstock`(person)
- `Betschel`(person)
- `Brockschnieder`(person)

**Example 22** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dipl.-Ing. Quirin Bagemühl` — partial — pred is substring of gold: `RgR Dipl.-Ing. Quirin Bagemühl`

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

**Example 23** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_83`)


Nach dem Unterhaltsherabsetzungsantrag des Vaters vom 20. 12. 2011 (Band I, ON 29 und ON 30) wurde mit der Vorschussgewährung ohnehin bereits teilweise innegehalten, sodass anstatt der ursprünglich gewährten 791,50 EUR monatlich pro Kind nunmehr - wie der Vater beantragte - nur noch monatliche Unterhaltsvorschüsse von 300 EUR für Cassandra Mustapha, 340 EUR für Jeannine Janowska und 330 EUR für PhD Zdenko Tomayer zur Auszahlung gelangen (Band I, ON 31, vgl auch Band II, ON 75, womit das Rekursgericht dem Erstgericht die Fortsetzung des Unterhaltsherabsetzungsverfahrens auftrug).

**False Positives:**

- `PhD Zdenko Tomayer ` — partial — gold is substring of pred: `PhD Zdenko Tomayer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cassandra Mustapha`(person)
- `Jeannine Janowska`(person)
- `PhD Zdenko Tomayer`(person)

**Example 24** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Martin Hembach` — no gold match — likely missing annotation
- `Mag. Martin Trapichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 25** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Arielle Schallmair, gegen die beklagte Partei Dr. Daisy Nagelkrämer, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr. Stefan Krall ` — no gold match — likely missing annotation
- `Dr. Oliver Kühnl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Arielle Schallmair`(person)
- `Dr. Daisy Nagelkrämer`(person)

**Example 26** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Georg Gorton ` — no gold match — likely missing annotation
- `DDr. Birgit Gorton` — no gold match — likely missing annotation
- `Dr. Gottfried Kassin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Helge Monhemius, Bakk. techn.`(person)
- `Ing. Eugenia Welze`(person)

**Example 27** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Jakob Krägeloh, geboren am 9. Juli 2019, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1.

**False Positives:**

- `Mag. Werner Thurner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Jakob Krägeloh`(person)
- `9. Juli 2019`(date)

**Example 28** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


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

**Example 29** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_10`)


8. 2009 zuerkannte, und zwar in Höhe von (jeweils) 80 EUR monatlich für MedR Ing. Anneliese Eberschulz und Tristan Swirbul, von 70 EUR monatlich für Wendy Remmy und von 60 EUR für Serena Christodoulidou.

**False Positives:**

- `Ing. Anneliese Eberschulz ` — positional overlap with gold: `MedR Ing. Anneliese Eberschulz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MedR Ing. Anneliese Eberschulz`(person)
- `Tristan Swirbul`(person)
- `Wendy Remmy`(person)
- `Serena Christodoulidou`(person)

**Example 30** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ing. Christian Stangl` — no gold match — likely missing annotation
- `Mag. Claudia Gründel ` — no gold match — likely missing annotation
- `Dr. Thomas Stampfer ` — no gold match — likely missing annotation
- `Dr. Christoph Orgler` — no gold match — likely missing annotation
- `Dr. Michael Stögerer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 5

**Gold Entities:**

- `OStR Esra Jakubait`(person)

**Example 31** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag. Irene Kienzl ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ostrovska`(person)

**Example 32** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_6`)


Sie suchte Dr. Thomas Poettgen, Facharzt für Orthopädie in Graz, auf, der ihr das Medikament Voltaren sowie eine Physiotherapie verschrieb.

**False Positives:**

- `Dr. Thomas Poettgen` — partial — gold is substring of pred: `Poettgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poettgen`(person)

**Example 33** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_11`)


2. 2009 von Dr. Thomas Pawlowitsch, Facharzt für Orthopädie in Graz, verordnete Präparat „Hyalgan SprAmp 2 ml 5 St“ habe.

**False Positives:**

- `Dr. Thomas Pawlowitsch` — partial — gold is substring of pred: `Pawlowitsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pawlowitsch`(person)

**Example 34** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_137`)


2. 2009 von Dr. Thomas Pavelec, Facharzt für Orthopädie in Graz, verordnete Präparat „Hyalgan SprAmp 2 ml 5 St“ zu Recht bestehe.

**False Positives:**

- `Dr. Thomas Pavelec` — partial — gold is substring of pred: `Pavelec`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pavelec`(person)

**Example 35** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr. Gabriele Griehsel ` — no gold match — likely missing annotation
- `Dr. Wolfgang Kozak ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

**Example 36** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_28`)


11. 2015 im Herz Jesu Heim in Dr. Rudolf Haberleitner-Straße 13, 4230 Pregarten, Österreich als „Hilfsarbeiterin“ beschäftigt gewesen sei, sei Ergebnis einer unbedenklichen Beweiswürdigung.

**False Positives:**

- `Dr. Rudolf Haberleitner` — partial — pred is substring of gold: `Dr. Rudolf Haberleitner-Straße 13, 4230 Pregarten, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Rudolf Haberleitner-Straße 13, 4230 Pregarten, Österreich`(address)

**Example 37** (doc_id: `deanon_TRAIN/11Ns41_20y`) (sent_id: `deanon_TRAIN/11Ns41_20y_3`)


Kopf Der Oberste Gerichtshof hat am 24. Februar 2021 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer, die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter im Verfahren zur Unterbringung des Mag. Herwig Beerbohm in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über den Antrag des Genannten auf Gewährung von Verfahrenshilfe nach Einsichtnahme der Generalprokuratur in die Akten nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Mag. Herwig Beerbohm ` — partial — gold is substring of pred: `Beerbohm`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Beerbohm`(person)

**Example 38** (doc_id: `deanon_TRAIN/11Ns41_20y`) (sent_id: `deanon_TRAIN/11Ns41_20y_4`)


Text Gründe: [1] Mit Beschluss des Obersten Gerichtshofs vom 8. Mai 2020, AZ 11 Os 18/20m, wurde ein auf das Verfahren AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien bezogener Antrag des Mag. Herwig Balnuß auf Erneuerung des Strafverfahrens zurückgewiesen.

**False Positives:**

- `Mag. Herwig Balnuß ` — partial — gold is substring of pred: `Balnuß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Balnuß`(person)

**Example 39** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Mag. Johann Klössel` — partial — gold is substring of pred: `Klössel`
- `Mag. Kurt Stoliarov ` — partial — gold is substring of pred: `Stoliarov`
- `Dr. Bernhard Holtzhäuser ` — partial — gold is substring of pred: `Holtzhäuser`
- `Mag. Kurt Schromm ` — partial — gold is substring of pred: `Schromm`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

**Example 40** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_4`)


Text Gründe: Der Oberste Gerichtshof hat zu AZ 12 Os 117/12s, 12 Os 118/12p über den Antrag des Angeklagten Mag. Kurt Schelm auf Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Ausführung eines Rechtsmittels sowie über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rogger, Mag. Johann Kiesler, Mag. Kurt Schwamm und Dr. Bernhard Havkost gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 21. Juni 2011, GZ 49 Hv 69/09f-938, zu entscheiden.

**False Positives:**

- `Mag. Kurt Schelm ` — partial — gold is substring of pred: `Schelm`
- `Mag. Johann Kiesler` — partial — gold is substring of pred: `Kiesler`
- `Mag. Kurt Schwamm ` — partial — gold is substring of pred: `Schwamm`
- `Dr. Bernhard Havkost ` — partial — gold is substring of pred: `Havkost`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Schelm`(person)
- `Rogger`(person)
- `Kiesler`(person)
- `Schwamm`(person)
- `Havkost`(person)

**Example 41** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_7`)


Diese zeigte ihre allfällige Ausgeschlossenheit an, weil sie mit dem (nach Einstellung des gegen ihn geführten Ermittlungsverfahrens) in der Hauptverhandlung als Zeugen vernommenen Dr. Gottwald Kr Valerian Hrabal eng befreundet sei.

**False Positives:**

- `Dr. Gottwald Kr Valerian Hrabal ` — partial — gold is substring of pred: `Valerian Hrabal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerian Hrabal`(person)

**Example 42** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_9`)


Zwar können aus dieser Generalklausel persönliche Beziehungen des Richters zu einer Beweisperson beachtlich sein, doch ist vom Obersten Gerichtshof die Glaubwürdigkeit des Zeugen Dr. Kr Svenja Siliacks nicht zu beurteilen, weshalb die Freundschaft der Hofrätin des Obersten Gerichtshofs Mag. Michel mit dem Zeugen nicht geeignet ist, bei einem verständig würdigenden objektiven Beurteiler naheliegende Zweifel an der unvoreingenommenen und unparteilichen Dienstverrichtung zu wecken (vglLässig, WK-StPO § 43 Rz 10 f; RIS-Justiz RS0045935).

**False Positives:**

- `Dr. Kr Svenja Siliacks ` — partial — gold is substring of pred: `Svenja Siliacks`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Svenja Siliacks`(person)

**Example 43** (doc_id: `deanon_TRAIN/12Ns18_20y`) (sent_id: `deanon_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bellingrath in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Birnstiel auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Mag. Herwig Bellingrath ` — partial — gold is substring of pred: `Bellingrath`
- `Mag. Herwig Birnstiel ` — partial — gold is substring of pred: `Birnstiel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bellingrath`(person)
- `Birnstiel`(person)

**Example 44** (doc_id: `deanon_TRAIN/12Ns18_20y`) (sent_id: `deanon_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Busskamp bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

**False Positives:**

- `Mag. Herwig Busskamp ` — partial — gold is substring of pred: `Busskamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Busskamp`(person)

**Example 45** (doc_id: `deanon_TRAIN/12Ns22_16f`) (sent_id: `deanon_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

**False Positives:**

- `Dr. Christine Schwab ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_4`)


2005 den Beschluss gefasst:  Spruch Vizepräsidentin des Obersten Gerichtshofs Mag. Marek ist von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Dr. Tilo Bräutigam sowie über die Berufungen der Staatsanwaltschaft und der Privatbeteiligten Hoch Seefurtlem GmbH gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 30. Juni 2017, GZ 72 Hv 8/17g-80, ausgeschlossen.

**False Positives:**

- `Dr. Tilo Bräutigam ` — partial — gold is substring of pred: `Bräutigam`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bräutigam`(person)
- `Hoch Seefurtlem GmbH`(organisation)

**Example 47** (doc_id: `deanon_TRAIN/12Ns4_15g`) (sent_id: `deanon_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

**False Positives:**

- `Dr. Christine Schwab` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/12Ns61_19w`) (sent_id: `deanon_TRAIN/12Ns61_19w_3`)


Kopf Der Oberste Gerichtshof hat am 24. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Dr. Harald Weichard und einen anderen Angeklagten wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB, AZ 121 Hv 19/16z des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Vizepräsidentin des Obersten Gerichtshofs Mag. Marek gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Dr. Harald Weichard ` — partial — gold is substring of pred: `Weichard`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weichard`(person)

**Example 49** (doc_id: `deanon_TRAIN/12Ns61_19w`) (sent_id: `deanon_TRAIN/12Ns61_19w_4`)


2005 den Beschluss gefasst:  Spruch Vizepräsidentin des Obersten Gerichtshofs Mag. Marek ist von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Dr. Harald Wallbrecht gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 1. August 2018, GZ 121 Hv 19/16z-857, ausgeschlossen.

**False Positives:**

- `Dr. Harald Wallbrecht ` — partial — gold is substring of pred: `Wallbrecht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wallbrecht`(person)

**Example 50** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_3`)


Kopf Der Oberste Gerichtshof hat am 3. Februar 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Bergmann als Schriftführerin in der Strafsache gegen Mag. Herwig Botzong wegen der Verbrechen der Verleumdung nach § 297 Abs 1 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 24 Hv 46/10k des Landesgerichts Linz, über die Grundrechtsbeschwerden des Genannten gegen den Beschluss des Oberlandesgerichts Linz vom 29. November 2010, AZ 8 Bs 402/10i, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerden werden zurückgewiesen.

**False Positives:**

- `Mag. Herwig Botzong ` — partial — gold is substring of pred: `Botzong`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Botzong`(person)

**Example 51** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_4`)


Text Gründe: In dem gegen Mag. Herwig Booth wegen der Verbrechen der Verleumdung nach § 297 Abs 1 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 24 Hv 46/10k des Landesgerichts Linz, geführten Strafverfahren befindet sich der Genannte seit 5. November 2009 in Untersuchungshaft.

**False Positives:**

- `Mag. Herwig Booth ` — partial — gold is substring of pred: `Booth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Booth`(person)

**Example 52** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_6`)


Mit dem angefochtenen Beschluss gab das Oberlandesgericht Linz einer Beschwerde von Mag. Herwig Brückbauer gegen die am 11. November 2010 beschlossene Fortsetzung (ON 1134) der Untersuchungshaft nicht Folge und setzte diese aus dem Haftgrund der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit a, lit b und lit c StPO fort.

**False Positives:**

- `Mag. Herwig Brückbauer ` — partial — gold is substring of pred: `Brückbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brückbauer`(person)

**Example 53** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_7`)


Rechtliche Beurteilung Gegen diese Entscheidung richten sich die rechtzeitig erhobenen, von Mag. Thobias Boßer handschriftlich in überwiegend grob unsachlicher Diktion verfassten Grundrechtsbeschwerden vom 15. Dezember 2010, die fristgerecht mit Schriftsatz seines Verteidigers gemeinsam eingebracht wurden.

**False Positives:**

- `Mag. Thobias Boßer ` — partial — gold is substring of pred: `Mag. Thobias Boßer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Thobias Boßer`(person)

**Example 54** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Mattheiß und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Tiepoldt auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr. Stefan Tiepoldt ` — partial — gold is substring of pred: `Tiepoldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mattheiß`(person)
- `Tiepoldt`(person)

**Example 55** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Dr. Stefan Tolmin ` — partial — gold is substring of pred: `Tolmin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 56** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_6`)


Rechtliche Beurteilung Gegen diesen Beschluss des Oberlandesgerichts Wien richtet sich der – nicht auf ein Erkenntnis des Europäischen Gerichtshofs für Menschenrechte (EGMR) gestützte – (rechtzeitige) Antrag des Beschuldigten Dr. Stefan Tokarski auf Erneuerung des Strafverfahrens gemäß § 363a StPO per analogiam, mit welchem dieser einen „Verstoß gegen Art 6 und 8 EMRK, Art 1 1.

**False Positives:**

- `Dr. Stefan Tokarski ` — partial — gold is substring of pred: `Tokarski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tokarski`(person)

**Example 57** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_17`)


Indem sich der Antrag des Dr. Stefan Töpker in einer bloßen (im Wesentlichen sogar wortgleichen) Wiederholung des Beschwerdevorbringens erschöpft und nicht einmal der Versuch einer argumentativen Bezugnahme zur angefochtenen Beschwerdeentscheidung insbesondere zu der nach seiner Vernehmung und nach der Übersetzung von ihm vorgelegter Urkunden bestehenden Verdachtslage (BS 2 ff) unternommen wird, wird er diesen Erfordernissen nicht gerecht.

**False Positives:**

- `Dr. Stefan Töpker ` — partial — gold is substring of pred: `Töpker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Töpker`(person)

**Example 58** (doc_id: `deanon_TRAIN/13Fss3_19y`) (sent_id: `deanon_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Nedler im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Ing. Sebastian Nedler ` — partial — gold is substring of pred: `Nedler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nedler`(person)

**Example 59** (doc_id: `deanon_TRAIN/13Fss3_19y`) (sent_id: `deanon_TRAIN/13Fss3_19y_4`)


Gründe:  Rechtliche Beurteilung Mit seinem Fristsetzungsantrag vom 23. Dezember 2019 behauptet Ing. Sebastian Nattler Säumnis des Obersten Gerichtshofs mit „der Vornahme einer Verfahrenshandlung und Ausfertigung einer Entscheidung“ in Ansehung seines am 20. August 2019 beim Obersten Gerichtshof eingebrachten, gegen den Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v gerichteten Antrags auf Erneuerung des Strafverfahrens.

**False Positives:**

- `Ing. Sebastian Nattler Säumnis ` — partial — gold is substring of pred: `Nattler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nattler`(person)

**Example 60** (doc_id: `deanon_TRAIN/13Fss3_19y`) (sent_id: `deanon_TRAIN/13Fss3_19y_7`)


Eine Ausfertigung dieser Entscheidung wurde der Vertreterin des Ing. Sebastian Naesemann am 18. Oktober 2019 zugestellt.

**False Positives:**

- `Ing. Sebastian Naesemann ` — partial — gold is substring of pred: `Naesemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Naesemann`(person)

**Example 61** (doc_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z__4`)


Linzner als Schriftführerin im Verfahren zur Unterbringung der Mag. Türkan Erika Böld in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 33 Hv 24/12g des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde der Betroffenen nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mag. Türkan Erika Böld ` — partial — gold is substring of pred: `Erika Böld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Erika Böld`(person)

**Example 62** (doc_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z__5`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Laurin Bickmann die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

**False Positives:**

- `Mag. Türkan Laurin Bickmann ` — partial — gold is substring of pred: `Laurin Bickmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laurin Bickmann`(person)

**Example 63** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__4`)


Abs 1 fünfter Fall, Abs 2 Z 1 SMG und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 20. Jänner 2012, GZ 8 Hv 83/11m-49, sowie die von der Generalprokuratur gegen den Vorgang der schriftlichen Ausfertigung dieses Urteils erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Brenner, sowie des Angeklagten und seines Verteidigers Mag. Heinz Russold nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Mag. Heinz Russold ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/14Os121_19d`) (sent_id: `deanon_TRAIN/14Os121_19d_17`)


Denn der Beschwerdeführer legte nicht dar, inwiefern die Aussagen der Zeugen Yelec Telci und StR Richard Ruzitschka zum Tatort und zum Tathergang – auch in Zusammenhalt mit den in der Hauptverhandlung vorgekommenen Lichtbildern vom Tatort (ON 15 Beilagen 1 bis 4) – mit den tatsächlichen örtlichen Gegebenheiten nicht übereinstimmen sollten und daher die Notwendigkeit bestünde, die Angaben der Zeugen an Ort und Stelle einer Überprüfung zu unterziehen.

**False Positives:**

- `StR Richard Ruzitschka ` — partial — gold is substring of pred: `StR Richard Ruzitschka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Yelec Telci`(person)
- `StR Richard Ruzitschka`(person)

**Example 65** (doc_id: `deanon_TRAIN/14Os16_15g`) (sent_id: `deanon_TRAIN/14Os16_15g_9`)


Dem Einwand der Verfahrensrüge (Z 5) zuwider wurden durch die Abweisung des - zum Beweis dafür, dass beim Angeklagten zum Tatzeitpunkt ein die Zurechnungsfähigkeit ausschließender Rauschzustand bestanden hat, gestellten - Antrags auf „Einholung eines weiteren Gutachtens aus dem Fachbereich der Medizin“ (ON 35 S 14) wegen behaupteter unvollständiger Befundaufnahme und inhaltlicher Mangelhaftigkeit der Expertise des psychiatrischen und neurologischen Sachverständigen Dr. Bertha Westerhoven Verteidigungsrechte nicht verletzt.

**False Positives:**

- `Dr. Bertha Westerhoven Verteidigungsrechte ` — partial — gold is substring of pred: `Dr. Bertha Westerhoven`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Bertha Westerhoven`(person)

**Example 66** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_3`)


Kopf Der Oberste Gerichtshof hat am 19. Februar 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Ent als Schriftführer in der Strafsache gegen Christian Poethke und einen anderen Angeklagten wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer anderen strafbaren Handlung, (zuletzt) AZ 33 Hv 70/12x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Rakhart Jörg Andrich auf Erneuerung des Strafverfahrens gemäß § 363a Abs 1 StPO nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr. Rakhart Jörg Andrich ` — partial — gold is substring of pred: `Jörg Andrich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poethke`(person)
- `Jörg Andrich`(person)

**Example 67** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_7`)


Mit Beschluss der Vorsitzenden des Schöffengerichts vom 22. Februar 2013, GZ 33 Hv 70/12x-220, wurden der Antrag des Dr. Rakhart Kirstin Achard auf Zuerkennung der Stellung als Opfer gemäß § 65 Abs 1 lit c StPO in diesem Verfahren zurückgewiesen und der Antrag auf Akteneinsicht abgewiesen.

**False Positives:**

- `Dr. Rakhart Kirstin Achard ` — partial — gold is substring of pred: `Kirstin Achard`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirstin Achard`(person)

**Example 68** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_10`)


Dagegen richtet sich der nicht auf eine Entscheidung des EGMR gestützte Antrag auf Erneuerung des Verfahrens gemäß § 363a StPO (RIS-Justiz RS0122228) des Dr. Rakhart Karsten Abbas.

**False Positives:**

- `Dr. Rakhart Karsten Abba` — positional overlap with gold: `Karsten Abbas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karsten Abbas`(person)

**Example 69** (doc_id: `deanon_TRAIN/15Os178_15p`) (sent_id: `deanon_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Korsmeier gegen Martin Rühmekorb wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klingspohr vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

**False Positives:**

- `Mag. Ralph Korsmeier ` — partial — gold is substring of pred: `Korsmeier`
- `Mag. Ralph Klingspohr ` — partial — gold is substring of pred: `Klingspohr`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Korsmeier`(person)
- `Rühmekorb`(person)
- `Klingspohr`(person)

**Example 70** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Penelope Piephans ` — partial — gold is substring of pred: `Dr. Penelope Piephans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 71** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_5`)


Zeno Thulcke, 2. Christine Adomadt, erstklagende Partei vertreten durch die Erwachsenenvertreterin Mag. Elfriede Melichar, Rechtsanwältin in Mödling, wider die beklagte Partei Dr. Benjamin Görmar, wegen Schadenersatz, hier wegen Verfahrenshilfe, über den „Rekurs“ (richtig: Revisionsrekurs) der zweitklagenden Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 21. Juli 2023, GZ 18 R 96/23f, 97/23b, 98/23z-31, womit der Beschluss des Bezirksgerichts Mödling vom 10. Mai 2023, GZ 3 C 1057/21v-25, hinsichtlich der erstklagenden Partei bestätigt und der von der zweitklagenden Partei dagegen erhobene Rekurs zurückgewiesen wurde, sowie der Rekurs der klagenden Parteien gegen den Beschluss des Bezirksgerichts Mödling vom 28. März 2023, GZ 3 C 1057/21v-20, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Elfriede Melichar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zeno Thulcke`(person)
- `Christine Adomadt`(person)
- `Dr. Benjamin Görmar`(person)

**Example 72** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

**False Positives:**

- `Dr. Horst Pechar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `See-Versand Werke GmbH`(organisation)
- `Robert Leis`(person)
- `Dargatz+Boedewig Telekom GmbH`(organisation)
- `ÖkR Nikolaus Buksbaum`(person)

**Example 73** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_4`)


Text Begründung: [1] Zwischen den Streitteilen ist seit Juni 2019 ein Schiedsverfahren anhängig, wobei der Senat gemäß § 587 ZPO mit Beschluss vom 20. Dezember 2019 zu GZ 18 ONc 3/19i-5, Univ.-Prof. Dr. Ernestine Mörtenhuber zum Schiedsrichter bestellte.

**False Positives:**

- `Dr. Ernestine Mörtenhuber ` — partial — gold is substring of pred: `Dr. Ernestine Mörtenhuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ernestine Mörtenhuber`(person)

**Example 74** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_5`)


Daneben besteht das Schiedsgericht aus Mag. Verena Mikolassek als Vorsitzendem und Dr. Ingrid Enzensperger als weiterer Schiedsrichterin.

**False Positives:**

- `Mag. Verena Mikolassek ` — partial — gold is substring of pred: `Mag. Verena Mikolassek`
- `Dr. Ingrid Enzensperger ` — partial — gold is substring of pred: `Dr. Ingrid Enzensperger`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Verena Mikolassek`(person)
- `Dr. Ingrid Enzensperger`(person)

**Example 75** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Dr. Andreas Oberbichler ` — no gold match — likely missing annotation
- `Dr. Michael Kramer` — no gold match — likely missing annotation
- `DDr. Walter Stuehrmann` — partial — pred is substring of gold: `VetR DDr. Walter Stuehrmann`
- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 3

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 76** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Dr. Michael Wukoschitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 77** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Dr. Gerhard Ebenbichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

**Example 78** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_4`)


Chantal Maxein, vertreten durch Dr. Eric Agstner, Rechtsanwalt in Wien, wegen Unterlassung, Zahlung, Feststellung und Beseitigung, über die Revision der beklagten Parteien gegen das Teilurteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Februar 2017, GZ 58 R 128/16w-38a, in der Fassung des Berichtigungsbeschlusses vom 29. März 2017, GZ 58 R 128/16w-40, mit dem das Urteil des Bezirksgerichts Neunkirchen vom 18. November 2016, GZ 23 C 249/16x-33, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Eric Agstner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Chantal Maxein`(person)

**Example 79** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Hubert Simon` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 80** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Jeannette Scherl, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Selina Dorfmeyer, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Helene Klaar ` — no gold match — likely missing annotation
- `Dr. Norbert Marschall Rechtsanwälte ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Mag. Jeannette Scherl`(person)
- `Selina Dorfmeyer`(person)

**Example 81** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


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

**Example 82** (doc_id: `deanon_TRAIN/1Ob142_19t`) (sent_id: `deanon_TRAIN/1Ob142_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der Antragstellerin Mag. Liu Cingöz, vertreten Dr. Brigitte Birnbaum und Dr. Rainer Toperczer, Rechtsanwälte in Wien, gegen den Antragsgegner Dr. Torsten Erlautzki, vertreten durch die Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse gemäß §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 9. Juli 2019, GZ 45 R 554/18f-162, mit dem der Beschluss des Bezirksgerichts Fünfhaus vom 25. Oktober 2018, GZ 4 Fam 68/14k-156, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Der Revisionsrekurs des Antragsgegners wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Dr. Brigitte Birnbaum ` — no gold match — likely missing annotation
- `Dr. Rainer Toperczer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Mag. Liu Cingöz`(person)
- `Dr. Torsten Erlautzki`(person)

**Example 83** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Karl Heinz Kramer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Amber Baraniak`(person)
- `Mag. Liliana Bößer`(person)

**Example 84** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `VetR Volkmar Aca` — partial — pred is substring of gold: `VetR Volkmar Acar`
- `Dr. Christian Bachmann` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Volkmar Acar`(person)
- `FN823951l`(business_register_number)
- `Nemtschok Touristik`(organisation)
- `Wilnorlex Werke gmbH`(organisation)
- `FN545761v`(business_register_number)

**Example 85** (doc_id: `deanon_TRAIN/1Ob160_12d`) (sent_id: `deanon_TRAIN/1Ob160_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Svenja Meierarnd, vertreten durch Dr. Karl-Peter Hasch, Rechtsanwalt in Villach, gegen den Antragsgegner Othmar Eidenmueller, vertreten durch Mag. Hanno Stromberger, Rechtsanwalt in Villach, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 31. Mai 2012, GZ 2 R 85/12w-11, mit dem der Beschluss des Bezirksgerichts Villach vom 13. März 2012, GZ 38 Fam 98/11s-7, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag. Hanno Stromberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Svenja Meierarnd`(person)
- `Othmar Eidenmueller`(person)

**Example 86** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Nordkamp, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Belohlawek KI Bank AG, Denis Nakonzer, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Dieter Koch ` — no gold match — likely missing annotation
- `Mag. Natascha Jilek` — no gold match — likely missing annotation
- `Mag. Martina Hosp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Manfred Nordkamp`(person)
- `Belohlawek KI`(organisation)
- `Denis Nakonzer`(person)

</details>

---

## `Person after 'klagenden Partei' (Plaintiff)`

**F1:** 0.009 | **Precision:** 0.029 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `4c8cbe8f`  
**Description:**
Captures the name of the plaintiff appearing after 'klagenden Partei', explicitly excluding company names and handling titles.

**Content:**
```
klagenden\s+Partei\s+(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s*,\s*[A-Z][a-z]+)*)(?!\s+(?:GmbH|AG|Co\.|Ltd|Inc|LLC|Rechtsanwalts?\s+GmbH|Rechtsanwalts?\s+AG))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.029 | 0.005 | 0.009 | 239 | 7 | 232 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 7 | 232 | 1368 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ostrovska` | `Ostrovska` |

**Example 1** (doc_id: `deanon_TRAIN/1Ob186_12b`) (sent_id: `deanon_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Pasqualini, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Denzlein, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Pasqualini` | `Pasqualini` |

**Missed by this rule (FN):**

- `Denzlein` (person)

**Example 2** (doc_id: `deanon_TRAIN/2Ob181_10x`) (sent_id: `deanon_TRAIN/2Ob181_10x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Gertrude Ptak, vertreten durch Dr. Bertram Broesigke und Dr. Wolfgang Broesigke, Rechtsanwälte in Wien, gegen die beklagte Partei Josef Schindelmeißer, vertreten durch den Sachwalter Dr. Helmut Heiger, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 15. Juni 2010, GZ 41 R 130/10m-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Ptak` | `Ptak` |

**Missed by this rule (FN):**

- `Schindelmeißer` (person)

**Example 3** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Thomas Papakonstantinou, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagten Parteien 1. Matthias Graafmann, und 2.

| Predicted | Gold |
|---|---|
| `Papakonstantinou` | `Papakonstantinou` |

**Missed by this rule (FN):**

- `Graafmann` (person)

**Example 4** (doc_id: `deanon_TRAIN/3Ob128_10k`) (sent_id: `deanon_TRAIN/3Ob128_10k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte und Hofrätinnen Hon.-Prof. Dr. Sailer, Dr. Lovrek, Dr. Jensik und Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Nadja Spangler, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagte Partei Sascha Heckert, vertreten durch Dr. Andreas König, Dr. Andreas Ermacora und Dr. Barbara Lässer, Rechtsanwälte in Innsbruck, wegen 137.146,60 EUR sA und Feststellung (Gesamtstreitwert 157.146,60 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2010, GZ 6 R 28/10w-44, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 30. Oktober 2009, GZ 7 Cg 117/07b-40, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Spangler` | `Spangler` |

**Missed by this rule (FN):**

- `Sascha Heckert` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Meiwaldt` — partial — pred is substring of gold: `Karin Meiwaldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

**False Positives:**

- `Mestwerdt, Slowenien` — positional overlap with gold: `Chen Mestwerdt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Chen Mestwerdt`(person)
- `Roman Eschenweck`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

**False Positives:**

- `Petraschk, Bakk` — partial — pred is substring of gold: `Juri Petraschk, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Juri Petraschk, Bakk. iur.`(person)
- `Mag. Dominik Riewert`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Sten` — partial — pred is substring of gold: `Sten und Stöwer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `OStR Gregor Ruemmel`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Ph` — partial — pred is substring of gold: `PhD Ignaz Nardelli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Mur Kraftalheim Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Skrzypczik` — partial — pred is substring of gold: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Jonasgasse` — partial — pred is substring of gold: `Jonasgasse 71, 4760 Weeg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob11_15p`) (sent_id: `deanon_TRAIN/10Ob11_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte und Hofrätinnen Univ.-Prof. Dr. Neumayr, Dr. Schramm, Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Viktoria Hornburg, vertreten durch Dr. Walter Vasoll und Mag. Marion Vasoll, Rechtsanwälte in Hermagor, gegen die beklagte Partei Mercedes Jungschlaeger, vertreten durch Dr. Thomas Romauch, Rechtsanwalt in Wien, wegen Feststellung und Einwilligung (6.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 4. Dezember 2014, GZ 3 R 169/14h-14, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Hermagor vom 9. August 2014, GZ 1 C 563/13b-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Hornburg` — partial — pred is substring of gold: `Viktoria Hornburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktoria Hornburg`(person)
- `Mercedes Jungschlaeger`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Zoltan Alfermann, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei DonauFurtostBildung GmbH, KzlR Noah Christansen, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Alfermann` — partial — pred is substring of gold: `Zoltan Alfermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Klagemann` — partial — pred is substring of gold: `Miranda Klagemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Miranda Klagemann`(person)
- `DI Adolf Kowallek`(person)
- `Ing. Janis Grottian`(person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Gritzmacher` — partial — pred is substring of gold: `Walter Gritzmacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Walter Gritzmacher`(person)
- `Dr. Ariadne Graspointner`(person)

**Example 13** (doc_id: `deanon_TRAIN/10Ob16_16z`) (sent_id: `deanon_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Josepha Mikolajetz, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Erhard Arslanboga, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mikolajetz` — partial — pred is substring of gold: `Josepha Mikolajetz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Josepha Mikolajetz`(person)
- `Erhard Arslanboga`(person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Verein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Feifel` — partial — pred is substring of gold: `Ernestine Feifel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)
- `Co KG`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kotschenreuther` — partial — pred is substring of gold: `Kotschenreuther u. Abele Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kotschenreuther u. Abele Planung GmbH`(organisation)
- `Janis Krentzel`(person)
- `Mittel Keltal GmbH`(organisation)
- `Julian Grebener`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bruno Altevogt, BA MBA, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, gegen die beklagten Parteien 1.

**False Positives:**

- `Altevogt` — partial — pred is substring of gold: `Bruno Altevogt, BA MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruno Altevogt, BA MBA`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Enns Werkdonver Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns Werkdonver Holding GmbH`(organisation)
- `Mag.a DDr.in Lynn Rothwein`(person)
- `Prausewetter Umwelt AG`(organisation)
- `Valerius Gensmantel`(person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Jungmichel` — partial — pred is substring of gold: `Ignaz Jungmichel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 20** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Amorelli` — partial — pred is substring of gold: `Calvin Amorelli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 21** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Arielle Schallmair, gegen die beklagte Partei Dr. Daisy Nagelkrämer, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Schallmair` — partial — pred is substring of gold: `Arielle Schallmair`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arielle Schallmair`(person)
- `Dr. Daisy Nagelkrämer`(person)

**Example 22** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Monhemius, Bakk` — partial — pred is substring of gold: `Helge Monhemius, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Helge Monhemius, Bakk. techn.`(person)
- `Ing. Eugenia Welze`(person)

**Example 23** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Marlon Richel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 24** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Techn R Heidrun Imai, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R Heidrun Imai`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Heidrun Imai`(person)

**Example 25** (doc_id: `deanon_TRAIN/10Ob88_19t`) (sent_id: `deanon_TRAIN/10Ob88_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Fatima Berlin, BSc, vertreten durch Frysak & Frysak Rechtsanwalts-Partnerschaft in Wien, gegen die beklagte Partei Otto Cesar, MSc, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, wegen 18.800 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 14. Oktober 2019, GZ 11 R 145/19b-16, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Mai 2019, GZ 27 Cg 6/19d-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Berlin` — partial — pred is substring of gold: `Fatima Berlin, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fatima Berlin, BSc`(person)
- `Otto Cesar, MSc`(person)

**Example 26** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Neunteufl, Deutschland` — positional overlap with gold: `Samantha Neunteufl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Samantha Neunteufl`(person)

**Example 27** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr.in Gerlinde Saltzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

**Example 28** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Adelwart` — partial — pred is substring of gold: `Levi Adelwart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Herbes` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 30** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Komm` — partial — pred is substring of gold: `KommR Franz Kubank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 31** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Overbeeke` — partial — pred is substring of gold: `Laura Overbeeke, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

**Example 32** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dr. Alice Wickertsheimer, gegen die beklagten Parteien 1.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Alice Wickertsheimer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Alice Wickertsheimer`(person)

**Example 33** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Franziska Gonschorek, vertreten durch die Huber & Partner Rechtsanwälte GmbH, Linz, gegen die beklagten Parteien 1.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Franziska Gonschorek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Franziska Gonschorek`(person)

**Example 34** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Angelina` — partial — pred is substring of gold: `Angelina Töpker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)

**Example 35** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Aktiengesellschaft, Meidlinger` — positional overlap with gold: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 36** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Amber Baraniak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Amber Baraniak`(person)
- `Mag. Liliana Bößer`(person)

**Example 37** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Volkmar Acar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Volkmar Acar`(person)
- `FN823951l`(business_register_number)
- `Nemtschok Touristik`(organisation)
- `Wilnorlex Werke gmbH`(organisation)
- `FN545761v`(business_register_number)

**Example 38** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Nordkamp, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Belohlawek KI Bank AG, Denis Nakonzer, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nordkamp` — partial — pred is substring of gold: `Manfred Nordkamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manfred Nordkamp`(person)
- `Belohlawek KI`(organisation)
- `Denis Nakonzer`(person)

**Example 39** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Bundeskammer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 40** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tamara Schweinfurth, vertreten durch Dr. Wolfgang Maurer, Rechtsanwalt in Golling, gegen die beklagte Partei Noah Vlatten, BEd, vertreten durch Dr. Peter Perner, Rechtsanwalt in Salzburg, wegen 10.895,18 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 19. Mai 2015, GZ 22 R 126/15f-21, mit dem das Urteil des Bezirksgerichts Salzburg vom 5. März 2015, GZ 32 C 407/14x-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Schweinfurth` — partial — pred is substring of gold: `Tamara Schweinfurth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tamara Schweinfurth`(person)
- `Noah Vlatten, BEd`(person)

**Example 41** (doc_id: `deanon_TRAIN/1Ob186_16h`) (sent_id: `deanon_TRAIN/1Ob186_16h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Anton Luehne, Deutschland, vertreten durch die Dr. Paul Kreuzberger, Mag. Markus Stranimaier & Mag. Manuel Vogler – Rechtsanwälte & Strafverteidiger OG, Bischofshofen, gegen die beklagten Parteien 1. OMedR Angelina Badenius und 2. Hon.-Prof. Miroslav Roelle, vertreten durch Dr. Raimund Danner, Rechtsanwalt in Salzburg, wegen 18.383,81 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. August 2016, GZ 4 R 107/16g-45, mit dem das Teilzwischenurteil des Landesgerichts Salzburg vom 8. Juni 2016, GZ 5 Cg 125/14z-41, mit einer Maßgabe bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Luehne, Deutschland` — positional overlap with gold: `Anton Luehne`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Anton Luehne`(person)
- `OMedR Angelina Badenius`(person)
- `Hon.-Prof. Miroslav Roelle`(person)

**Example 42** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Limited, London, Kapellergasse` — positional overlap with gold: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 43** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Boothe` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 44** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Synsynfurt` — partial — pred is substring of gold: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 45** (doc_id: `deanon_TRAIN/1Ob95_21h`) (sent_id: `deanon_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Planung Berglanzfurt GmbH, Heiko Thieroff, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei InnGetränke GmbH, OMedR Rainer Witthoefft, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Planung Berglanzfurt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Planung Berglanzfurt GmbH`(organisation)
- `Heiko Thieroff`(person)
- `InnGetränke GmbH`(organisation)
- `OMedR Rainer Witthoefft`(person)

**Example 46** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. Musger als weitere Richter in der Rechtssache der klagenden Partei Glanzbruckkraft-Recycling -Aktiengesellschaft, Steindläcker 26, 4183 Obertraberg, Österreich, vertreten durch THUM WEINREICH SCHWARZ CHYBA REITER Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Verband der Versicherungsunternehmen Österreichs, Schwarzenbergplatz 7, 1030 Wien, vertreten durch Mag. Georg E. Thalhammer, Rechtsanwalt in Wien, wegen 11.550 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Innere Stadt Wien das Bezirksgericht Kitzbühel bestimmt.

**False Positives:**

- `Glanzbruckkraft` — partial — pred is substring of gold: `Glanzbruckkraft-Recycling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Glanzbruckkraft-Recycling`(organisation)
- `Steindläcker 26, 4183 Obertraberg, Österreich`(address)
- `Bezirksgericht Kitzbühel`(organisation)

**Example 47** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. E. Solé als weitere Richter in der Rechtssache der klagenden Partei Thaddäus Gerzabek, LLM, vertreten durch Dr. Hanspeter Egger, Rechtsanwalt in Wien, gegen die beklagte Partei Pietruszak Recycling -AG, Rainer Chochola, vertreten durch Dr. Norbert Bergmüller, Rechtsanwalt in Schladming, wegen 1.505,25 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Hietzing das Bezirksgericht Irdning bestimmt.

**False Positives:**

- `Thadd` — partial — pred is substring of gold: `Thaddäus Gerzabek, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thaddäus Gerzabek, LLM`(person)
- `Pietruszak Recycling`(organisation)
- `Rainer Chochola`(person)
- `Bezirksgericht Irdning`(organisation)

**Example 48** (doc_id: `deanon_TRAIN/2Ob114_24i`) (sent_id: `deanon_TRAIN/2Ob114_24i_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Edith Wischnewsky, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei KzlR Techn R Quirin Erler, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Wischnewsky` — partial — pred is substring of gold: `Edith Wischnewsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edith Wischnewsky`(person)
- `KzlR Techn R Quirin Erler`(person)

**Example 49** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Edgar Arnts, vertreten durch Dr. Heinrich Oppitz, Rechtsanwalt in Wels, wider die beklagten Parteien 1.

**False Positives:**

- `Arnts` — partial — pred is substring of gold: `Edgar Arnts`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edgar Arnts`(person)

**Example 50** (doc_id: `deanon_TRAIN/2Ob175_21f`) (sent_id: `deanon_TRAIN/2Ob175_21f_4`)


Sloboda als weitere Richter in der Rechtssache der klagenden Partei Shoshana Etl, vertreten durch Mag. Axel Bauer, Rechtsanwalt in Wien, gegen die beklagte Partei Manuel van der Willik, vertreten durch Dr. Manfred Sommerbauer ua, Rechtsanwälte in Wiener Neustadt, wegen 44.903,84 EUR sA, über die Revision der beklagten Partei gegen das Zwischenurteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. Juni 2021, GZ 11 R 79/21z-66, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. März 2021, GZ 5 Cg 105/19a-50 in der Fassung des Berichtigungsbeschlusses vom 16. März 2021, GZ 5 Cg 105/19a-51, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Etl` — partial — pred is substring of gold: `Shoshana Etl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Shoshana Etl`(person)
- `Manuel van der Willik`(person)

**Example 51** (doc_id: `deanon_TRAIN/2Ob176_25h`) (sent_id: `deanon_TRAIN/2Ob176_25h_4`)


Sloboda, Dr. Thunhart und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richterin und weitere Richter in der Rechtssache der klagenden Partei Alva Wittwer, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, gegen die beklagte Partei Leopold Eggerichs, vertreten durch Grgic & Partneri Rechtsanwaltsgesellschaft mbH in Wien, wegen zuletzt 31.718 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 6. September 2025, GZ 11 R 40/25w-47, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wittwer` — partial — pred is substring of gold: `Alva Wittwer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alva Wittwer`(person)
- `Leopold Eggerichs`(person)

**Example 52** (doc_id: `deanon_TRAIN/2Ob178_18t`) (sent_id: `deanon_TRAIN/2Ob178_18t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Garttri Sicherheit -GesmbH, Alpendorfsiedlung 14, 4209 Linzerberg, Österreich, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, wider die beklagte Partei Vogelsanger Marine GmbH, Juri Büttgens, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen (restlich) 30.000 EUR sA, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juli 2018, GZ 4 R 79/18v-157, mit welchem das Endurteil des Handelsgerichts Wien vom 9. April 2018, GZ 40 Cg 12/11g-153, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Sicherheit` — partial — pred is substring of gold: `Garttri Sicherheit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Garttri Sicherheit`(organisation)
- `Alpendorfsiedlung 14, 4209 Linzerberg, Österreich`(address)
- `Vogelsanger Marine GmbH`(organisation)
- `Juri Büttgens`(person)

**Example 53** (doc_id: `deanon_TRAIN/2Ob179_15k`) (sent_id: `deanon_TRAIN/2Ob179_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Franz Wagenschwanz, vertreten durch Dr. Klaus Estl, Rechtsanwalt in Salzburg, gegen die beklagten Parteien 1. Hartmut Willekes, und 2. KommR Roswitha Allgoewer, vertreten durch Dr. Roland Reichl, Rechtsanwalt in Salzburg, wegen 10.000 EUR sA und Feststellung (Streitinteresse 5.000 EUR), über den Rekurs der zweitbeklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 22. Juli 2015, GZ 22 R 169/15d-52, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Salzburg vom 2. April 2015, GZ 32 C 896/12f-47, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Wagenschwanz` — partial — pred is substring of gold: `Franz Wagenschwanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Franz Wagenschwanz`(person)
- `Hartmut Willekes`(person)
- `KommR Roswitha Allgoewer`(person)

**Example 54** (doc_id: `deanon_TRAIN/2Ob180_21s`) (sent_id: `deanon_TRAIN/2Ob180_21s_4`)


Sloboda als weitere Richter in der Rechtssache der klagenden Partei Ing. Constanze Kronawitt, vertreten durch Dr. Alexander Bosio, Rechtsanwalt in Zell am See, gegen die beklagten Parteien 1. DDr. Leif Eralp, und 2. Lothar Schwänke, beide vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, wegen 21.376,95 EUR sA und Feststellung (Streitwert: 10.000 EUR), über die Revisionen der klagenden und der zweitbeklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 6. August 2021, GZ 53 R 110/21i-23, womit das Teil- und Teilzwischenurteil des Bezirksgerichts Zell am See vom 6. April 2021, GZ 18 C 892/20z-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen der klagenden und der zweitbeklagten Partei werden zurückgewiesen.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Constanze Kronawitt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Constanze Kronawitt`(person)
- `DDr. Leif Eralp`(person)
- `Lothar Schwänke`(person)

**Example 55** (doc_id: `deanon_TRAIN/2Ob216_18f`) (sent_id: `deanon_TRAIN/2Ob216_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof. Ewald Schwietale, vertreten durch Mag. Martin Paar und Mag. Hermann Zwanzger, Rechtsanwälte in Wien, gegen die beklagte Partei Lütkemöller Digital AG, Karl Deppermann, vertreten durch Dr. Helmut Weinzettl, Rechtsanwalt in Wiener Neustadt, wegen 14.817,50 EUR sA, über die Revisionen beider Parteien gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Juni 2018, GZ 18 R 11/18y-64, mit welchem das Urteil des Bezirksgerichts Baden vom 28. Dezember 2017, GZ 7 C 1010/15x-58, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. Ewald Schwietale`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Ewald Schwietale`(person)
- `Lütkemöller Digital AG`(organisation)
- `Karl Deppermann`(person)

**Example 56** (doc_id: `deanon_TRAIN/2Ob224_21m`) (sent_id: `deanon_TRAIN/2Ob224_21m_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Igor Arnoldußen, vertreten durch MMMMag.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Igor Arnoldußen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Igor Arnoldußen`(person)

**Example 57** (doc_id: `deanon_TRAIN/2Ob226_19b`) (sent_id: `deanon_TRAIN/2Ob226_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Paul Wienhölter, vertreten durch Beck & Dörnhöfer & Partner Rechtsanwälte in Eisenstadt, wider die beklagten Parteien 1. Florian Michalik und 2.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Paul Wienhölter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Paul Wienhölter`(person)
- `Florian Michalik`(person)

**Example 58** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Aktiengesellschaft, Poysdorfer` — positional overlap with gold: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 59** (doc_id: `deanon_TRAIN/2Ob37_17f`) (sent_id: `deanon_TRAIN/2Ob37_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Florentin Uffenwasser, vertreten durch Dr. Armin Exner, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Stadtgemeinde Naomi Mertensmeyer, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, wegen 29.461,04 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 22.377,04 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 15. Dezember 2016, GZ 2 R 141/16a-47, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Uffenwasser` — partial — pred is substring of gold: `Florentin Uffenwasser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Uffenwasser`(person)
- `Naomi Mertensmeyer`(person)

**Example 60** (doc_id: `deanon_TRAIN/2Ob71_23i`) (sent_id: `deanon_TRAIN/2Ob71_23i_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Moses Malkomes, vertreten durch Klepp Nöbauer Hintringer Primetshofer Rechtsanwälte (GbR) in Linz, gegen die beklagte Partei Carmen Reinoldsmann, vertreten durch Dr. Christoph Arbeithuber, Rechtsanwalt in Linz, wegen 26.843,50 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Februar 2023, GZ 4 R 17/23g-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Malkomes` — partial — pred is substring of gold: `Moses Malkomes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Moses Malkomes`(person)
- `Carmen Reinoldsmann`(person)

**Example 61** (doc_id: `deanon_TRAIN/2Ob73_15x`) (sent_id: `deanon_TRAIN/2Ob73_15x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dragan Karp, vertreten durch Mag. Bernd Trappmaier, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Marlene Diderichs, vertreten durch Mag. Claus Marchl, Rechtsanwalt in Wien, wegen 25.396,03 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. Jänner 2015, GZ 11 R 239/14v-26, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. September 2014, GZ 57 Cg 30/14x-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Karp` — partial — pred is substring of gold: `Dragan Karp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dragan Karp`(person)
- `Marlene Diderichs`(person)

**Example 62** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Neimeier` — partial — pred is substring of gold: `Luigi Neimeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Luigi Neimeier`(person)
- `LNC KI Solutions GmbH`(organisation)
- `Kordelia Grauel`(person)

**Example 63** (doc_id: `deanon_TRAIN/2Ob86_12d`) (sent_id: `deanon_TRAIN/2Ob86_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Constanze Hoefelmann, MSc, vertreten durch Gruböck & Lentschig Rechtsanwälte OG in Baden, wider die beklagte Partei „ Herbert Sippert “ Ada Roselius, vertreten durch Themmer, Toth & Partner Rechtsanwälte OG in Wien, wegen 144.329,55 EUR sA (Revisionsinteresse 54.717 EUR sA), infolge der außerordentlichen Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Februar 2012, GZ 4 R 598/11g-25, den Beschluss gefasst:  Spruch Das Revisionsverfahren wird bis zur rechtskräftigen Erledigung des Verfahrens über den Ablehnungsantrag der beklagten Partei gegen die Erstrichterin unterbrochen.

**False Positives:**

- `Hoefelmann` — partial — pred is substring of gold: `Constanze Hoefelmann, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Constanze Hoefelmann, MSc`(person)
- `Herbert Sippert`(person)
- `Ada Roselius`(person)

**Example 64** (doc_id: `deanon_TRAIN/2Ob89_17b`) (sent_id: `deanon_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Aron Dawideit, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. PhD Irvin Kindschuh, 2. Theodor Hermus, und 3.

**False Positives:**

- `Dawideit` — partial — pred is substring of gold: `Aron Dawideit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Aron Dawideit`(person)
- `PhD Irvin Kindschuh`(person)
- `Theodor Hermus`(person)

**Example 65** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Dirker` — partial — pred is substring of gold: `Farina Dirker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 66** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Stadt` — partial — pred is substring of gold: `Stadt-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Co KG`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 67** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Kraftnorost Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 68** (doc_id: `deanon_TRAIN/3Ob156_12f`) (sent_id: `deanon_TRAIN/3Ob156_12f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Severin Ilek, vertreten durch die Sachwalterin Mag. Roswitha Ferl-Pailer, Rechtsanwältin in Hartberg, gegen die beklagte Partei Dipl.

**False Positives:**

- `Ilek` — partial — pred is substring of gold: `Severin Ilek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Severin Ilek`(person)

**Example 69** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Bruckgartver GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 70** (doc_id: `deanon_TRAIN/3Ob178_15w`) (sent_id: `deanon_TRAIN/3Ob178_15w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Jensik als Vorsitzenden, die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Schwarzenbacher und Dr. Roch sowie die Hofrätin Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Nikolai Castelli, vertreten durch Divitschek Sieder Sauer Peter Rechtsanwälte GesBR in Deutschlandsberg, gegen die beklagte Partei Dohmgoergen Bau GmbH, Oswald Schubert, vertreten durch Dr. Johannes Liebmann, Rechtsanwalt in Gleisdorf, wegen 82.977,52 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. Juli 2015, GZ 3 R 54/15h-145, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Castelli` — partial — pred is substring of gold: `Nikolai Castelli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nikolai Castelli`(person)
- `Dohmgoergen Bau GmbH`(organisation)
- `Oswald Schubert`(person)

**Example 71** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Dr. Bartholomäus Nijboer, vertreten durch Hochsteger, Perz, Wallner & Warga Rechtsanwälte in Hallein, gegen die beklagte Partei Hon.-Prof. Dirk Edlich, vertreten durch Mag. Johann Meisthuber, Rechtsanwalt in Salzburg, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 26. August 2011, GZ 21 R 31/11x-32, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Salzburg vom 25. November 2010, GZ 31 C 86/09a-24, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Bartholomäus Nijboer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Bartholomäus Nijboer`(person)
- `Hon.-Prof. Dirk Edlich`(person)

**Example 72** (doc_id: `deanon_TRAIN/3Ob19_20w`) (sent_id: `deanon_TRAIN/3Ob19_20w_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Rinaldo Isaac, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wider die beklagte Partei Felizia Mascheck, vertreten durch Dr. Alexandra Sedelmayer-Pammesberger, Rechtsanwältin in Wien, wegen Unterhaltsherabsetzung (AZ 8 C 22/16k) und Einwendungen gegen den Anspruch nach § 35 EO (AZ 8 C 4/18s), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 20. August 2019, GZ 44 R 338/19k-67, mit dem das Urteil des Bezirksgerichts Hernals vom 23. Mai 2019, GZ 8 C 22/16k-60, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden neuerlich dem Erstgericht zurückgestellt.

**False Positives:**

- `Isaac` — partial — pred is substring of gold: `Rinaldo Isaac`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rinaldo Isaac`(person)
- `Felizia Mascheck`(person)

**Example 73** (doc_id: `deanon_TRAIN/3Ob236_17b`) (sent_id: `deanon_TRAIN/3Ob236_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Delila Englschall, vertreten durch Harb & Postl Rechtsanwälte OG in Graz, gegen die beklagte Partei Achmed Schnetzer, vertreten durch Dr. Paul Bauer, Dr. Anton Triendl, Rechtsanwälte in Innsbruck, wegen 32.173,22 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 23.653,60 EUR sA und Feststellung) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 29. November 2017, GZ 10 R 59/17b-27, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Englschall` — partial — pred is substring of gold: `Delila Englschall`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Delila Englschall`(person)
- `Achmed Schnetzer`(person)

**Example 74** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH, Hubert Englmaier, vertreten durch Dr. Martin Holzer, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Florian Corvetti, vertreten durch Dr. Heimo Jilek, Rechtsanwalt in Leoben, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 3. November 2010, GZ 1 R 244/10i-34, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Leoben vom 9. Juni 2010, GZ 5 C 315/09y-28, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision der klagenden Partei wird Folge gegeben, das angefochtene Urteil aufgehoben und die Rechtssache zur neuerlichen Entscheidung an das Berufungsgericht zurückverwiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Riecken Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Riecken Maschinenbau GmbH`(organisation)
- `Hubert Englmaier`(person)
- `Florian Corvetti`(person)

**Example 75** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Florentin Rosskämmer, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde ÖkR Priv.-Doz. Björn Gustloff, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Rossk` — partial — pred is substring of gold: `Florentin Rosskämmer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Rosskämmer`(person)
- `ÖkR Priv.-Doz. Björn Gustloff`(person)

**Example 76** (doc_id: `deanon_TRAIN/3Ob35_13p`) (sent_id: `deanon_TRAIN/3Ob35_13p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Mercedes Jungels, vertreten durch Dr. Peter Böck, Rechtsanwalt in Neusiedl am See, gegen die beklagte Partei Traude Ejsmond, vertreten durch Mag. Christian Kaiser, Rechtsanwalt in Wien, wegen Ehescheidung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Eisenstadt als Berufungsgericht vom 13. Dezember 2012, GZ 20 R 123/12f-15, womit infolge Berufungen der klagenden und beklagten Partei das Urteil des Bezirksgerichts Neusiedl am See vom 19. April 2012, GZ 10 C 10/12d-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Jungels` — partial — pred is substring of gold: `Mercedes Jungels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mercedes Jungels`(person)
- `Traude Ejsmond`(person)

**Example 77** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Cl` — partial — pred is substring of gold: `Andreas Clösges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Clösges`(person)
- `Chemie Valtri GmbH`(organisation)
- `Niels Niefeldt`(person)

**Example 78** (doc_id: `deanon_TRAIN/3Ob49_11v`) (sent_id: `deanon_TRAIN/3Ob49_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Julius Zimzick Verlag GmbH & Co KG, Terramaregasse 28, 8234 Rohrbachschlag, Österreich, vertreten durch Dr. Wolfgang Dartmann und andere Rechtsanwälte in Linz, wider die beklagten Parteien 1. Friedrich Schreinemachers und 2.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Zimzick Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zimzick Verlag GmbH`(organisation)
- `Co KG`(organisation)
- `Terramaregasse 28, 8234 Rohrbachschlag, Österreich`(address)
- `Schreinemachers`(person)

**Example 79** (doc_id: `deanon_TRAIN/3Ob52_14i`) (sent_id: `deanon_TRAIN/3Ob52_14i_3`)


Kopf Der Oberste Gerichtshof hat durch die Hofrätin Dr. Lovrek als Vorsitzende sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Jensik, Dr. Musger und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Gabriel Domaß, vertreten durch Ehrlich-Rogner & Schlögl Rechtsanwalts-Partnerschaft in Wien, gegen die beklagte Partei KR Univ.-Prof.in Melina Thoele, vertreten durch Dr. Tassilo Wallentin, Rechtsanwalt in Wien, wegen Einwendungen gegen den Anspruch, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 6. Dezember 2012, GZ 47 R 275/12g-21, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Döbling vom 23. Mai 2012, GZ 6 C 223/10y-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird zurückgewiesen.

**False Positives:**

- `Doma` — partial — pred is substring of gold: `Gabriel Domaß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gabriel Domaß`(person)
- `Univ.-Prof.in Melina Thoele`(person)

**Example 80** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Lexglanzfen-Garten AG, Pia Özbek, vertreten durch Dr. Hartmut Mayer, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Esra Waitkat, vertreten durch Mag. Gerhard Pilz, Rechtsanwalt, als Verfahrenshelfer, wegen 3.330,19 EUR sA (AZ 35 R 24/09b des Landesgerichts für Zivilrechtssachen Wien), zum Fristsetzungsantrag der beklagten Partei vom 28. Oktober 2009 an den Obersten Gerichtshof im Ablehnungsverfahren den Beschluss gefasst:  Spruch Der Fristsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Lexglanzfen` — partial — pred is substring of gold: `Lexglanzfen-Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexglanzfen-Garten AG`(organisation)
- `Pia Özbek`(person)
- `Mag. Esra Waitkat`(person)

**Example 81** (doc_id: `deanon_TRAIN/4Nc18_11a`) (sent_id: `deanon_TRAIN/4Nc18_11a_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei HochCloud GmbH, Piedro Temur, vertreten durch Dr. Christian Fuchshuber LL.M., Rechtsanwalt in Innsbruck, gegen die beklagte Partei SUI Pharma Consulting GmbH, Nancy Herz, vertreten durch Dr. Gerhard Strobich, Rechtsanwalt in Trofaiach, wegen 5.873,18 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag, zur Verhandlung und Entscheidung in dieser Rechtssache anstelle des Bezirksgerichts Innsbruck das Bezirksgericht Leoben zu bestimmen, wird abgewiesen.

**False Positives:**

- `Hoch` — partial — pred is substring of gold: `HochCloud GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HochCloud GmbH`(organisation)
- `Piedro Temur`(person)
- `SUI Pharma Consulting GmbH`(organisation)
- `Nancy Herz`(person)
- `Bezirksgericht Leoben`(organisation)

**Example 82** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Rudigkeit Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Innsbruck`(organisation)
- `Rudigkeit Finanzen GmbH`(organisation)
- `Ing. Sascha Rohkrämer`(person)
- `Suddorftra Manufaktur GmbH`(organisation)
- `Ludmilla Nottelmann`(person)
- `Landesgericht Wien`(organisation)

**Example 83** (doc_id: `deanon_TRAIN/4Ob100_13d`) (sent_id: `deanon_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Erwin Sieferer, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Lebensmittel Seeder -Aktiengesellschaft, Knechtswies 63, 4692 Niederau, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ StR Thobias Broß ” Viola Hüßkes, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Sieferer` — partial — pred is substring of gold: `Erwin Sieferer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Erwin Sieferer`(person)
- `Lebensmittel Seeder`(organisation)
- `Knechtswies 63, 4692 Niederau, Österreich`(address)
- `StR Thobias Broß`(person)
- `Viola Hüßkes`(person)

**Example 84** (doc_id: `deanon_TRAIN/4Ob112_24k`) (sent_id: `deanon_TRAIN/4Ob112_24k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Kersseboom Textil AG, Prof.in Juliette Große-Kleimann, Schweiz, vertreten durch die Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Benedikt Faath plc, DDr. Piedro Bielmeier, Malta, vertreten durch die Brandl Talos Rechtsanwälte GmbH in Wien, wegen 19.333,99 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz vom 14. März 2024, GZ 1 R 12/24a-46, mit dem das Urteil des Landesgerichts Wels vom 1. Dezember 2023, GZ 6 Cg 18/23p-41, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Texti` — partial — pred is substring of gold: `Kersseboom Textil AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kersseboom Textil AG`(organisation)
- `Prof.in Juliette Große-Kleimann`(person)
- `Benedikt Faath`(person)
- `DDr. Piedro Bielmeier`(person)

**Example 85** (doc_id: `deanon_TRAIN/4Ob113_24g`) (sent_id: `deanon_TRAIN/4Ob113_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Vierziger u. Tewald Wind GmbH, Claire Lüdermann, Bakk. rer. nat., vertreten durch Grassner Rechtsanwalts GmbH in Linz, gegen die beklagte Partei Milena Buchmayr, vertreten durch Dr. Manfred Palkovits, Mag. Martin Sohm, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2024, GZ 38 R 247/23i-46, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vierziger` — partial — pred is substring of gold: `Vierziger u. Tewald Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vierziger u. Tewald Wind GmbH`(organisation)
- `Claire Lüdermann, Bakk. rer. nat.`(person)
- `Milena Buchmayr`(person)

**Example 86** (doc_id: `deanon_TRAIN/4Ob13_24a`) (sent_id: `deanon_TRAIN/4Ob13_24a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Peter Nöhrnberg, LLM, vertreten durch Mag. Andrea Nobis, Rechtsanwältin in Wien, gegen die beklagte Partei Astrid Fesenmair, vertreten durch die Maraszto Milisits Rechtsanwälte OG in Wien, wegen 59.888,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. November 2023, GZ 5 R 154/23p-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Peter` — partial — pred is substring of gold: `Peter Nöhrnberg, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Peter Nöhrnberg, LLM`(person)
- `Astrid Fesenmair`(person)

**Example 87** (doc_id: `deanon_TRAIN/4Ob163_13v`) (sent_id: `deanon_TRAIN/4Ob163_13v_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Musger, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Miranda Bleckwehl, vertreten durch die Sachwalterin Dr. Tanja Sporrer, Rechtsanwältin, Innsbruck, Templstraße 22, gegen die beklagte Partei Oswald Wiechering, vertreten durch Dr. Ekkehard Erlacher und Dr. Renate Erlacher-Philadelphy, Rechtsanwälte in Innsbruck, wegen 56.626 EUR sA, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 8. Mai 2013, GZ 4 R 40/13h-125, womit der Antrag des Beklagten auf Berichtigung des Bewertungsausspruchs im Urteil vom 15. März 2013 abgewiesen wurde, folgenden Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Bleckwehl` — partial — pred is substring of gold: `Miranda Bleckwehl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Miranda Bleckwehl`(person)
- `Oswald Wiechering`(person)

**Example 88** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Pfleg` — partial — pred is substring of gold: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 89** (doc_id: `deanon_TRAIN/4Ob190_23d`) (sent_id: `deanon_TRAIN/4Ob190_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Jolanda Petschke, vertreten durch den Verfahrenshelfer Dr. Lukas Twardosz, Rechtsanwalt in Wien, gegen die beklagte Partei Ali Salwetter Verein Wilma Sahlmüller, vertreten durch die Verfahrenshelferin Mag. Ioana-Maria Vilau, Rechtsanwältin in Wien, wegen zuletzt 30.000 EUR sA, Unterlassung und Beseitigung (Gesamtstreitwert: 40.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Juli 2023, GZ 4 R 175/22t-62, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Petschke` — partial — pred is substring of gold: `Jolanda Petschke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jolanda Petschke`(person)
- `Ali Salwetter`(person)
- `Wilma Sahlmüller`(person)

**Example 90** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Dueckers Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 91** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Kraftheimglanz` — partial — pred is substring of gold: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 92** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Traun` — partial — pred is substring of gold: `Traun-Sanitär gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 93** (doc_id: `deanon_TRAIN/4Ob201_10b`) (sent_id: `deanon_TRAIN/4Ob201_10b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Wendelin Wetekamp OEG, KzlR Ibrahim Kocaslan, vertreten durch Dr. Martin Leitner und Dr. Ralph Trischler, Rechtsanwälte in Wien, gegen die beklagte Partei Feddes KI GmbH, KommR Waldemar Holzhaider, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung, Rechnungslegung, Schadenersatz und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. September 2010, GZ 1 R 192/10b-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß Der Antrag auf Zuspruch der Kosten der Revisionsrekursbeantwortung wird gemäß § 508a Abs 2 Satz 2 und § 521a Abs 2 ZPO abgewiesen.

**False Positives:**

- `Wetekamp` — partial — pred is substring of gold: `Wendelin Wetekamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendelin Wetekamp`(person)
- `KzlR Ibrahim Kocaslan`(person)
- `Feddes KI GmbH`(organisation)
- `KommR Waldemar Holzhaider`(person)

**Example 94** (doc_id: `deanon_TRAIN/4Ob204_15a`) (sent_id: `deanon_TRAIN/4Ob204_15a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Severin Vollersen, MSc kammer, Miranda Ranfft, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, gegen die beklagte Partei Silvia Markfort, vertreten durch Mag. Romi Andrea Panner, Rechtsanwältin in Rudersdorf, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 34.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. September 2015, GZ 2 R 101/15k-35, womit das Urteil des Landesgerichts Eisenstadt vom 6. Mai 2015, GZ 18 Cg 18/14w-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vollersen` — partial — pred is substring of gold: `Severin Vollersen, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Severin Vollersen, MSc`(person)
- `Miranda Ranfft`(person)
- `Silvia Markfort`(person)

</details>

---

## `Person in Parenthetical Context`

**F1:** 0.004 | **Precision:** 0.020 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `1182fd38`  
**Description:**
Captures names appearing within parentheses, often used for clarification or full names in legal texts.

**Content:**
```
\(\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.020 | 0.002 | 0.004 | 151 | 3 | 148 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 148 | 1354 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_5`)


Die Entscheidungen der Vorinstanzen werden dahin abgeändert, dass der Beschluss des Erstgerichts lautet: „1. Dem minderjährigen Laurin Bihrenbrodt, und der minderjährigen Dominik Aldirmaz, wird vom 1. Jänner 2024 bis 31. Dezember 2028 gemäß §§ 3, 4 Z 1 UVG ein monatlicher Unterhaltsvorschuss in Höhe von 305 EUR ( Silvius Berwolf ) und 270 EUR ( Karlheinz Arntzen ), höchstens jedoch in der Höhe des jeweiligen Richtsatzes für pensionsberechtigte Halbwaisen gemäß § 293 Abs 1 lit c, sublit bb erster Fall, § 108f ASVG gewährt.

| Predicted | Gold |
|---|---|
| `Silvius Berwolf` | `Silvius Berwolf` |
| `Karlheinz Arntzen` | `Karlheinz Arntzen` |

**Missed by this rule (FN):**

- `Laurin Bihrenbrodt` (person)
- `Dominik Aldirmaz` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_17`)


[4] Mit Bescheiden vom 18. Jänner 2017 ( Silvia Balßuweit ) und 23. Juli 2018 ( OMedR Ilse Albertsernst ) wurde den Kindern ebenfalls der Status des Asylberechtigten als Familienangehörige (ihrer Mutter) zuerkannt.

| Predicted | Gold |
|---|---|
| `Silvia Balßuweit` | `Silvia Balßuweit` |

**Missed by this rule (FN):**

- `OMedR Ilse Albertsernst` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_7`)


Der Antragsgegner wohnt in der Russischen Förderation (Tschetschenien).

**False Positives:**

- `Tschetschenien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_46`)


Die weiteren acht Personen, deren Vernehmung beantragt wurde, haben ihren Wohnsitz in Wien bzw der Umgebung von Wien (Maria Enzersdorf).

**False Positives:**

- `Maria Enzersdorf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_104`)


Der Wegfall der Anmerkung (aus welchem Grund auch immer) führt demnach nicht zum Erlöschen des Eigentums, weil eine Anmerkung nicht zur Veränderung (Aufhebung) dinglicher Rechte führen kann.

**False Positives:**

- `Aufhebung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_62`)


Das Wohnsitzkriterium wirkt sich somit eher auf Wanderarbeitnehmer (Grenzgänger) als auf österreichische Arbeitnehmer und ihre Familienangehörigen, die ihren Wohnsitz meistens im Inland haben, benachteiligend aus, was den Tatbestand der mittelbaren Diskriminierung erfüllt (Felten/NeumayraaO iFamZ 2010, 169).

**False Positives:**

- `Grenzgänger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_73`)


4. Bei Berücksichtigung der dargelegten Erwägungen gelangt der erkennende Senat zu dem Ergebnis, dass die Beschränkung auf den gewöhnlichen Aufenthalt des Kindes im Inland gemäß § 2 Abs 1 UVG im vorliegenden Fall mit der Freizügigkeitsverordnung (EU) 492/2011 nicht vereinbar ist und die Minderjährigen daher aus der Rechtsstellung ihrer Mutter als Wanderarbeitnehmer (Grenzgängerin), die in Österreich einer Beschäftigung über der Geringfügigkeitsgrenze nachgeht und mit ihren beiden unterhaltsberechtigten Kindern in einem anderen Mitgliedstaat (Slowakei) lebt, mit Recht einen Anspruch auf Gewährung österreichischer Unterhaltsvorschüsse ableiten können.

**False Positives:**

- `Grenzgängerin` — no gold match — likely missing annotation
- `Slowakei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 5** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_60`)


Beides trifft hier nicht zu, weshalb den Kindern nach der jüngeren, mittlerweile gefestigten Rechtsprechung ein Restgeldunterhaltsanspruch (Differenzunterhalt) gegen den besserverdienenden Vater zusteht (1 Ob 158/15i;

**False Positives:**

- `Differenzunterhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_7`)


Die beklagte Partei ist schuldig, der klagenden Partei die mit 259,42 EUR (Barauslagen) bestimmten Kosten des Revisionsverfahrens binnen 14 Tagen zu ersetzen.

**False Positives:**

- `Barauslagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_25`)


Das Klagebegehren laute jedoch darauf, der Klägerin (Leasingnehmerin) einen Teil des Kaufpreises zu erstatten.

**False Positives:**

- `Leasingnehmerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_85`)


Die Abtretung als kausales Verfügungsgeschäft ist nur dann wirksam, wenn sie auf einem gültigen Grundgeschäft (Rechtstitel) beruht (RS0032510).

**False Positives:**

- `Rechtstitel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_93`)


Einwendungen aus dem Valutaverhältnis zwischen Zedentin (Leasinggeberin) und Zessionarin (Klägerin) kann die Schuldnerin (Beklagte) nur so weit geltend machen, als damit die Gläubigerstellung der Zessionarin, beispielsweise wegen Nichtigkeit oder Unwirksamkeit des Zessionsgeschäfts, in Frage gestellt wird (RS0032781;

**False Positives:**

- `Leasinggeberin` — no gold match — likely missing annotation
- `Klägerin` — no gold match — likely missing annotation
- `Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 10** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_39`)


2. Aus Art 87 und 87a B-VG ergibt sich, dass die Gerichtsbarkeit grundsätzlich von Richtern auszuüben ist, wobei die Besorgung einzelner und genau zu bezeichnender Arten von Geschäften der Gerichtsbarkeit erster Instanz in Zivilrechtssachen besonders ausgebildeten nichtrichterlichen Bundesbediensteten (Rechtspfleger) übertragen werden kann.

**False Positives:**

- `Rechtspfleger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_76`)


Im vorliegenden Fall hat die Mutter ihren gewöhnlichen Aufenthalt gemeinsam mit den minderjährigen Kindern in Österreich, wobei sowohl die Mutter als auch die Kinder Staatsbürger eines EU-Mitgliedstaats (Frankreich) sind.

**False Positives:**

- `Frankreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_9`)


Zwischen den Parteien ist strittig, ob der angemessene Wasserzins 1,30 EUR (Kläger) oder 1,10 EUR (Beklagter) pro m³ Wasser beträgt.

**False Positives:**

- `Kläger` — no gold match — likely missing annotation
- `Beklagter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 13** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_20`)


Im Anlassfall lägen mit den Bescheiden des BFA aus den Jahren 2020 (Vater) und 2021 (Kind und Mutter) hinsichtlich aller Familienmitglieder rezente Asylentscheidungen vor, weshalb sich das Erstgericht zu Recht weder mit der Flüchtlingseigenschaft des Kindes noch der konkreten Situation der Familie näher befasst habe.

**False Positives:**

- `Vater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_26`)


3. Wenn der Wert des Entscheidungsgegenstands des Rekursgerichts nicht 30.000 EUR übersteigt, steht einer Partei nach § 63 Abs 1 und 2 AußStrG nur ein Antrag an das Rekursgericht offen, den Ausspruch dahin abzuändern, dass der ordentliche Revisionsrekurs doch für zulässig erklärt werde (Zulassungsvorstellung).

**False Positives:**

- `Zulassungsvorstellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_57`)


In Verfahren, die auch von Amts wegen eingeleitet werden können, gibt es jedoch keine Teilrechtskraft einer Entscheidung, weil das Rekursgericht (Revisionskursgericht) an das Antragsbegehren nicht gebunden ist und die Entscheidung auch zu Ungunsten des Rekurswerbers abgeändert werden kann (Fucik/Kloiber, AußStrG § 42 Rz 3, 4; siehe schon oben Pkt 1.1).

**False Positives:**

- `Revisionskursgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_64`)


2.2 Der Zweck der Legalzession nach § 173 Abs 4 BSVG liegt darin, zu vermeiden, dass der untergebrachte Bezieher einer Pension oder Rente seinen Unterhalt doppelt, nämlich einmal auf Kosten des Bundes in natura und ein zweites Mal in Form einer Pension (Rente) auf Kosten des Sozialversicherungsträgers erhält.

**False Positives:**

- `Rente` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_89`)


Der Bund ist damit in die Rechte des Klägers eingetreten und könnte die Zuerkennung (Erhöhung) von Leistungen im Verfahren in Leistungssachen beantragen (RIS-Justiz RS0109546).

**False Positives:**

- `Erhöhung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_18`)


Werden die gesetzlichen Kriterien für die Ermessensentscheidung (Gefährlichkeitsprognose) verkannt oder wird die Prognosetat verfehlt als solche mit schweren Folgen beurteilt, so kommt auch eine Anfechtung aus § 281 Abs 1 Z 11 zweiter Fall StPO in Betracht (vgl zum GanzenRatzin WK² StGB Vor §§ 21 bis 25 Rz 8 ff mwN).

**False Positives:**

- `Gefährlichkeitsprognose` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/12Os80_15d`) (sent_id: `deanon_TRAIN/12Os80_15d_11`)


Das isoliert herausgegriffene, offensichtlich ganz allgemein gehaltene Aussagedetail, er (Veroljub Closhen ) habe nicht gewusst, ob es sich bei den Schmuggelfahrten im September und im Oktober 2011 um echte Drogen gehandelt habe oder nur um andere Stoffe (ON 46 S 7), bringt lediglich dessen fehlende Kenntnis mangels eigener Überprüfung zum Ausdruck und tangiert daher keine entscheidende oder erhebliche und nur solcherart erörterungsbedürftige Tatsache (zu den Begriffen:Ratz, WK-StPO § 281 Rz 399 ff, 409 ff).

**False Positives:**

- `Veroljub Closhen` — partial — gold is substring of pred: `Closhen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Closhen`(person)

**Example 20** (doc_id: `deanon_TRAIN/15Os53_16g`) (sent_id: `deanon_TRAIN/15Os53_16g_7`)


Danach hat er am 21. Juni 2015 in Osterkogel 186, 4880 Eggenberg, Österreich Sieglinde Kutschorra mit Gewalt und durch Drohung mit gegenwärtiger Gefahr für Leib oder Leben (§ 89 StGB) zur Duldung einer dem Beischlaf gleichzusetzenden geschlechtlichen Handlung, nämlich des Analverkehrs genötigt, indem er „sie auf das Bett warf, auf den Bauch drehte, ihr Hose und Unterhose herunterriss und sie gewaltsam am Bett niederdrückte, während er den Analverkehr an ihr vollzog, wobei er androhte, er werde einen mitgebrachten Gegenstand in ihren Anus einführen und sie 'ausdehnen', wenn sie nicht 'herhalte', und ihr unter der weiteren Androhung, diese zuzuziehen, wenn sie nicht aufhöre zu schreien, eine Eisenkette mit großen Gliedern um den Hals schlang“, wobei die Tat eine länger als 24 Tage dauernde Gesundheitsschädigung (Anpassungsstörung) der Sieglinde Koepke zur Folge hatte.

**False Positives:**

- `Anpassungsstörung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Osterkogel 186, 4880 Eggenberg, Österreich`(address)
- `Kutschorra`(person)
- `Koepke`(person)

**Example 21** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_17`)


Gegen die Rekursentscheidung, soweit sie den Unterbrechungsbeschluss betrifft, richtet sich der „Rekurs“ (Revisionsrekurs) des Zweitklägers.

**False Positives:**

- `Revisionsrekurs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_10`)


2. Der Oberste Gerichtshof hat bereits in anderen gleichgelagerten Fällen der Durchsetzung von Ansprüchen nach der EU-Fluggastrechte-VO gegen das auch hier beklagte Flugunternehmen mit Sitz in Hirschmühle 31, 8221 Hofing, Österreich (Serbien) die Ordination bewilligt und das Bezirksgericht Schwechat, in dessen Sprengel der Abflughafen liegt, als zuständiges Gericht bestimmt (6 Nc 1/19b = ZVR 2019/114, 259 [zustMayr];

**False Positives:**

- `Serbien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hirschmühle 31, 8221 Hofing, Österreich`(address)
- `Bezirksgericht Schwechat`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_6`)


Text Begründung: Gegenstand des Revisionsverfahrens ist allein das Begehren des Klägers auf Beseitigung der auf seiner Liegenschaft errichteten Abwasserbeseitigungsanlage (Hauskanal) der Beklagten.

**False Positives:**

- `Hauskanal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_38`)


Hat die Klägerin bzw haben ihre Rechtsvorgänger innerhalb der im (integrierten) Plan ausgewiesenen Fläche Handlungen gesetzt, die nach außen hin die volle Zugehörigkeit der Sache zum Ausübenden (während einer dreißigjährigen Dauer) sichtbar zum Ausdruck brachten (und damit die Voraussetzungen einer Eigentumsersitzung erfüllt), kommt der „wahren“ Grenze (Naturgrenze) zwischen ihren jeweiligen Grundstücken (und damit der Frage, ob die Klägerin und ihre Rechtsvorgänger „schon immer“ Eigentümer genau dieser Fläche waren) keine entscheidungserhebliche Bedeutung zu.

**False Positives:**

- `Naturgrenze` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/1Ob142_19t`) (sent_id: `deanon_TRAIN/1Ob142_19t_89`)


Das Vorbringen des Mannes dazu, dass er 764.322 ATS für den Dachgeschossausbau (Holzbau) und 570.048 ATS für den Wintergarten vom „Firmenkonto“ bezahlt habe, und dass Dachgeschossausbau und Wintergarten Investitionen betroffen hätten, die „erst Jahre später erfolgt“ seien, gestand die Frau im Übrigen als richtig zu und räumte ausdrücklich ein, dass Dachbodenausbau und Wintergarten aus dem (ehelichen) Einkommen des Mannes finanziert wurden.

**False Positives:**

- `Holzbau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_248`)


Jedenfalls dann, wenn die Ausstellung der Restschuldbestätigung im unmittelbaren Zusammenhang mit der vorzeitigen Kreditrückzahlung steht, könnte die beanstandete Entgeltvereinbarung den zwingenden gesetzlichen Anordnungen (Entgeltbeschränkungen) des § 16 VKrG widersprechen.

**False Positives:**

- `Entgeltbeschränkungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_33`)


Jedenfalls als Teile der Aufteilungsmasse vorhanden sind derzeit eine im gemeinsamen Eigentum (je 50 %) stehende Liegenschaft mit der früheren Ehewohnung in Oberbreitsach 106, 4274 Almblick, Österreich, eine im gemeinsamen Eigentum der Streitteile stehende Eigentumswohnung in Gustav Mahler-Promenade 27, 5212 Obererb, Österreich, ein im gemeinsamen Eigentum stehendes Baugrundstück in Wißgrillgasse 113, 5273 Edt, Österreich, eine Eigentumswohnung des Antragsgegners in Alva Gangloff ( Altes Mühlbachbett 1, 2534 Windhaag, Österreich gasse), Gesellschaftsanteile (je 10 %) des Antragsgegners an zwei Kommanditgesellschaften (Verlustbeteiligungen) sowie eine Forderung des Antragsgegners gegen eine GmbH, deren Alleingesellschafter er ist, in Höhe von 341.500 EUR.

**False Positives:**

- `Verlustbeteiligungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberbreitsach 106, 4274 Almblick, Österreich`(address)
- `Gustav Mahler-Promenade 27, 5212 Obererb, Österreich`(address)
- `Wißgrillgasse 113, 5273 Edt, Österreich`(address)
- `Alva Gangloff`(person)
- `Altes Mühlbachbett 1, 2534 Windhaag, Österreich`(address)

**Example 28** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_39`)


Im Zusammenhang mit ihrer Berufung auf § 91 Abs 2 EheG unterlässt sie insbesondere jede Erörterung darüber, in welchem Ausmaß die vom Antragsgegner überwiegend aus Unternehmenserträgnissen (Gewinnausschüttungen) finanzierten Vermögensgegenstände wertmäßig unter Berücksichtigung der in Satz 2 angeführten Kriterien bei der Aufteilung – zumindest größenordnungsmäßig – zu veranschlagen wären.

**False Positives:**

- `Gewinnausschüttungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_13`)


[3] Zum wesentlichen Vermögensgut, der Liegenschaft mit der Ehewohnung (Haus), stellte das Erstgericht fest, dass der Verkehrswert am 7. 12. 2018 315.500 EUR betrug.

**False Positives:**

- `Haus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_102`)


Da es nicht Aufgabe des Aufteilungsverfahrens ist, die wirtschaftliche Gebarung während der Ehe im Nachhinein zu korrigieren, kommt es im Aufteilungsverfahren nur darauf an, dass dieser gewährte Kredit während der ehelichen Lebensgemeinschaft im Ausmaß von 6.500 EUR für die Ehewohnung (Terrasse) verwendet wurde, er aber nun mit außerhalb der Ehe erwirtschafteten Mitteln allein von der Frau „abbezahlt“ wird.

**False Positives:**

- `Terrasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_61`)


8. 2009 (Unfallstag) in Gang gesetzt wurde und grundsätzlich am 19.

**False Positives:**

- `Unfallstag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/1Ob56_21y`) (sent_id: `deanon_TRAIN/1Ob56_21y_4`)


Ali Haarnacke und 2. Li Baselt, vertreten durch Dr. Serpil Dogan, Rechtsanwältin in Feldkirch, gegen die beklagte Partei Republik Österreich (Bund), vertreten durch die Finanzprokuratur in Wien, und den Nebenintervenienten auf Seite der beklagten Partei KzlR Florian Schlimm, vertreten durch Dr. Bertram Grass und Mag. Christoph Dorner, Rechtsanwälte in Bregenz, wegen 60.300 EUR sA und Feststellung (Erstklägerin) und 66.300 EUR sA und Feststellung (Zweitkläger), über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 27. Jänner 2021, GZ 4 R 171/20h-41, mit dem das Urteil des Landesgerichts Feldkirch vom 2. Oktober 2020, GZ 4 Cg 14/19k-35, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Bund` — no gold match — likely missing annotation
- `Erstklägerin` — no gold match — likely missing annotation
- `Zweitkläger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Ali Haarnacke`(person)
- `Li Baselt`(person)
- `KzlR Florian Schlimm`(person)

**Example 33** (doc_id: `deanon_TRAIN/1Ob57_16p`) (sent_id: `deanon_TRAIN/1Ob57_16p_27`)


Die Vorinstanzen legten auf der Sachverhaltsebene zum Studienwechsel zu Grunde, dass die Antragstellerin im Oktober 2012 an die Kunstuniversität Graz wechselte, wo sie bis heute zielstrebig, innerhalb der vorgeschriebenen Zeit liegend und erfolgreich die Studienrichtung »Instrumental(Gesangs)Pädagogik - Klassik (Harfe - Klassik)« studiert, sowie dass der Antragsgegner die vorbehaltlos geleisteten Unterhaltszahlungen bis Juli 2013 in Kenntnis aller Umstände leistete.

**False Positives:**

- `Gesangs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/2Ob41_16t`) (sent_id: `deanon_TRAIN/2Ob41_16t_6`)


Die ausgebende Fondsgesellschaft wurde nach dem Recht der Cayman Islands gegründet, als ihre Depotbank wurde im Emissionsprospekt die Bank of Bermuda (Luxembourg) angeführt und als ihre inländische Repräsentantin, Prospektkontrollorin und Zahlstelle im Sinne des InvFG 1993 schien die Beklagte auf.

**False Positives:**

- `Luxembourg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/2Ob41_16t`) (sent_id: `deanon_TRAIN/2Ob41_16t_17`)


Weiters erblickt die Klägerin einen grundlegenden Rechtsirrtum des Berufungsgerichts darin, dass zur Beurteilung der Vollständigkeit und Richtigkeit des Prospekts des tatsächlich veranlagten Wertpapiers (Herald Fund) ein Prospekt eines anderen Wertpapiers, nämlich des Primeo Funds herangezogen worden sei.

**False Positives:**

- `Herald Fund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_6`)


Dabei waren auch Arbeiten in Nassräumen (Duschbereich) eines als Fitnessstudio genutzten Gebäudeteils vorzunehmen.

**False Positives:**

- `Duschbereich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_10`)


Soweit in dritter Instanz noch relevant ging das Berufungsgericht – in teilweiser Abänderung des der Klage zur Gänze stattgebenden Urteils des Erstgerichts – davon aus, dass die Klägerin durch einen gänzlichen Ersatz ihrer zur Mängelbehebung aufgewendeten Kosten bereichert wäre, weil die Sanierung des mangelhaften Teils des Gebäudes (Duschbereich) nach rund der Hälfte seiner Lebensdauer erfolgte.

**False Positives:**

- `Duschbereich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/3Ob14_24s`) (sent_id: `deanon_TRAIN/3Ob14_24s_9`)


Auf den zugesprochenen Betrag entfallen 6.204.600 EUR an Schadenersatz gemäß Art 5 Abs 2 BIT (Beschlagnahme von Fahrzeugen und sonstigen beweglichen Sachen) sowie (richtig) 68.732.403,60 EUR an Schadenersatz gemäß Art 8 Abs 1 BIT (Schirmklausel) wegen Verletzung der mit drei libyschen Agenturen abgeschlossenen Projektverträge.

**False Positives:**

- `Schirmklausel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_11`)


[2] DieBeklagteist für die Ökostromförderabwicklung nach dem Ökostromgesetz verantwortlich und zahlt die durch Verordnung festgelegten Vergütungen (Einspeisetarife) an die Erzeuger von Ökostrom aus.

**False Positives:**

- `Einspeisetarife` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_59`)


Als Preise für die Abnahme elektrischer Energie aus Stromerzeugungsanlagen (Neuanlagen), die unter ausschließlicher Verwendung des Energieträgers feste Biomasse (zB Waldhackgut) betrieben werden, werden folgende Beträge festgesetzt: ... (2)

**False Positives:**

- `Neuanlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_60`)


Als Preise für die Abnahme elektrischer Energie aus Stromerzeugungsanlagen (Neuanlagen), die unter ausschließlicher Verwendung des Energieträgers Abfälle mit hohem biogenen Anteil betrieben werden, werden folgende Beträge festgesetzt: 1.

**False Positives:**

- `Neuanlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/3Ob1_20y`) (sent_id: `deanon_TRAIN/3Ob1_20y_58`)


Der – dem (von den Klägern mehrfach geänderten) Urteilsbegehren im Vorverfahren zur Gänze stattgebende – Titel ist nicht bloß unbestimmt, sondern vielmehr in sich widersprüchlich, weil er in seinem Punkt 1. (Feststellungsbegehren) zum Verlauf des Servitutswegs auf die in Wahrheit nicht deckungsgleichen Einzeichnungen in Beilage ./B1 und ON 71 verweist, sodass ausgehend vom Spruch völlig offen bleibt, welcher der beiden Wegverläufe nun tatsächlich festgestellt werden sollte.

**False Positives:**

- `Feststellungsbegehren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/3Ob236_17b`) (sent_id: `deanon_TRAIN/3Ob236_17b_10`)


Den Vorinstanzen ist bei der Annahme, der Beklagte habe in sorgloser Weise gefährlich gehandelt, indem er (als „Klaubauf“ verkleidet) die Klägerin unsanft seitlich zu Boden riss, und daher schadenersatzrechtlich für die Gesundheitsschäden (Schlüsselbeinbruch) einzustehen, die sie beim Aufschlagen auf dem „erkennbar hart gefrorenen“ Boden erlitt, keine Fehlbeurteilung unterlaufen.

**False Positives:**

- `Schlüsselbeinbruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/3Ob242_19p`) (sent_id: `deanon_TRAIN/3Ob242_19p_54`)


Die genannte Bestimmung bezieht sich also ausschließlich auf die Kommunikation des Betroffenen mit dem Gericht, sei es in oder außerhalb einer Verhandlung (Tagsatzung), sodass ihre Anwendung auf die hier relevante Kommunikation des Betroffenen mit seinem gesetzlichen Vertreter keinesfalls in Betracht kommt.

**False Positives:**

- `Tagsatzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_28`)


Ein solcher liege hier, wie das Erstgericht zutreffend erkannt habe, in dem in der Sitzung der Gemeindevertretung gefassten Beschluss über die Genehmigung des Kaufvertrags, komme doch im Sitzungsprotokoll ausreichend zum Ausdruck, dass das Grundstück als öffentliche Verkehrsanlage (Marktplatz) gewidmet werden solle.

**False Positives:**

- `Marktplatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_42`)


[12] 3. Gemäß § 27 Abs 2 Sbg LStG 1966 erfolgte der Bau neuer Gemeindestraßen und die Übernahme von Straßen als Gemeindestraßen sowie die Bestimmung (Umwandlung) als Gemeindestraße I. oder II. Klasse aufgrund von Beschlüssen der Gemeindevertretung.

**False Positives:**

- `Umwandlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_15`)


Das Erstgericht beendete daraufhin die Beweisaufnahme (Einvernahme des ausständigen Zeugen), schloss das Verfahren unter Abstandnahme von weiterer Beweisaufnahme (Lokalaugenschein) und legte den Akt mit der Stellungnahme zur Entscheidung über den Delegierungsantrag dem Obersten Gerichtshof vor, ein Grund für eine Delegierung habe von Anfang an nicht vorgelegen, der einzuvernehmende Zeuge wohne in Tirol, die Beklagte habe ihren Sitz im Sprengel des Landesgerichts Innsbruck und die beanstandeten Rechteverletzungen hätten in Tirol stattgefunden.

**False Positives:**

- `Lokalaugenschein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_21`)


Zweckmäßigkeitsgründe sind vor allem der Wohnort (Sitz) der Parteien und der zu vernehmenden Zeugen (zuletzt 4 Nc 21/11t mwN).

**False Positives:**

- `Sitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_TRAIN/4Ob13_24a`) (sent_id: `deanon_TRAIN/4Ob13_24a_5`)


[2] DasErstgerichtwies die Klage ab, weil die Behandlung und insbesondere der chirurgische Eingriff, der auch medizinisch indiziert gewesen sei, lege artis erfolgt sei; eine Alternative im Sinne einer gleichwertigen „Lösung“ (Behandlungsmethode) habe nicht bestanden.

**False Positives:**

- `Behandlungsmethode` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_12`)


Dafür stellt die Beklagte ein Vermittlungssystem mittels einer Technologie bereit, mit deren Hilfe die Anfrage eines Kunden um eine Beförderungsleistung an registrierte Partner (Mietwagenunternehmer) übermittelt wird, wobei Mietwagenunternehmer und Fahrer gleichzeitig elektronisch über den Eingang einer Bestellung informiert werden;

**False Positives:**

- `Mietwagenunternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_96`)


4.1Im Anlassfall wird nach der Bestellung (Fahrtanfrage) durch den Nutzer vom Vermittlungssystem der Beklagten ein Fahrer ausgewählt, der – über das Vermittlungssystem – über die Anfrage informiert wird und den Auftrag bestätigt.

**False Positives:**

- `Fahrtanfrage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Verein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 53** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_4`)


Begründung:  Rechtliche Beurteilung Die Vorinstanzen haben den wegen Verstoßes der beklagten Parteien gegen § 225 UGB auf § 1 Abs 1 Z 1 UWG (Fallgruppe Rechtsbruch) gestützten Unterlassungsanspruch abgewiesen, wobei das Berufungsgericht den Anspruch wegen der von ihm als vertretbar qualifizierten Rechtsansicht der beklagten Parteien verneint hat.

**False Positives:**

- `Fallgruppe Rechtsbruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_27`)


Die Umbauarbeiten (Dachbodenausbau) standen in keinem Zusammenhang mit dem (späteren) Kaufvertrag zwischen den Streitteilen.

**False Positives:**

- `Dachbodenausbau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_9`)


Das Fahrzeug war mit einer Abschalteinrichtung (Abgasmanipulationssoftware) ausgestattet.

**False Positives:**

- `Abgasmanipulationssoftware` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/5Ob177_20w`) (sent_id: `deanon_TRAIN/5Ob177_20w_13`)


Vor etwa 20 bis 25 Jahren begannen die Antragsgegner mit dem Ausbau des Obergeschosses (Dachbodens), in dem sie zunächst Dachflächenfenster einbauten und ein Bad und WC sowie eine Doppeleingangstür errichteten und diese Räume vom restlichen Dachboden abtrennten.

**False Positives:**

- `Dachbodens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/5Ob177_20w`) (sent_id: `deanon_TRAIN/5Ob177_20w_137`)


Relevant ist im vorliegenden Fall die Neuschaffung einer Wohnung durch den Ausbau des Obergeschosses (Dachbodens) in dem ehemaligen Wirtschafts- und Stallgebäude der Antragsgegner.

**False Positives:**

- `Dachbodens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/5Ob177_20w`) (sent_id: `deanon_TRAIN/5Ob177_20w_142`)


[29] 4.2.2 Während der Ausnahmetatbestand des § 1 Abs 4 Z 1 MRG die Neuerrichtung eines Gebäudes voraussetzt und es nicht darauf ankommt, wie viele Bestandobjekte in diesem neuen Gebäude vorhanden sind, zielt etwa § 16 Abs 1 Z 2 zweiter Fall MRG auf die Neuschaffung eines Mietgegenstands durch Umbau, Einbau oder Zubau als Erweiterung eines schon bestehenden Gebäudes ab (RS0117872) und setzt damit voraus, dass weitere Räumlichkeiten (Mietgegenstände) hinzukommen (vglWürth/Zingher/KovanyiaaO § 16 MRG Rz 14).

**False Positives:**

- `Mietgegenstände` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/5Ob182_20f`) (sent_id: `deanon_TRAIN/5Ob182_20f_14`)


[4] Gegenstand des Revisionsverfahrens ist (nur mehr) das Begehren der Klägerin, den Beklagten zu verpflichten, diese Rampe zu entfernen und den vorigen Zustand (Asphaltfläche) wieder herzustellen.

**False Positives:**

- `Asphaltfläche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/5Ob184_21a`) (sent_id: `deanon_TRAIN/5Ob184_21a_13`)


Die Vertragsparteien stellten im Vertrag fest, dass für das Mietverhältnis – unbeschadet der Geltung zwingender Rechtsvorschriften – ausschließlich die Bestimmungen dieses Vertrags und subsidiär die Bestimmungen des ABGB rechtswirksam seien und die Bestimmungen des MRG nur in dem in § 1 Abs 4 MRG (Einleitungssatz) normierten Umfang zur Anwendung kommen sollten.

**False Positives:**

- `Einleitungssatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_63`)


Nach ständiger Rechtsprechung des Fachsenats (RS0102514) hat der Mieter im Bereich der Hauptmietzinsüberprüfung nach § 37 Abs 1 Z 8 MRG die Möglichkeit, die Feststellung der zulässigen Höhe des Hauptmietzinses pro futuro oder zu bestimmten Zinsterminen zu begehren, er kann sich aber auch mit der bloßen Feststellung, dass der Hauptmietzins nach § 16 Abs 1 MRG (Angemessenheit) oder nach § 16 Abs 2 MRG (Kategorie) zu bilden ist, begnügen.

**False Positives:**

- `Angemessenheit` — no gold match — likely missing annotation
- `Kategorie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 62** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_12`)


(Nur) in Bezug auf die Zurückweisung der Rekurse tätigte es einen Bewertungs- und Zulässigkeitsausspruch.

**False Positives:**

- `Nur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/5Ob71_24p`) (sent_id: `deanon_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ignaz Schaufel, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Mur Waldbach GmbH, StR Martin Leitenbauer, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

**False Positives:**

- `Deutschland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ignaz Schaufel`(person)
- `Mur Waldbach GmbH`(organisation)
- `StR Martin Leitenbauer`(person)
- `Co KG`(organisation)

**Example 64** (doc_id: `deanon_TRAIN/5Ob71_24p`) (sent_id: `deanon_TRAIN/5Ob71_24p_23`)


Das Landgericht Ravensburg (Deutschland) hat dem Gerichtshof der Europäischen Union am 9.

**False Positives:**

- `Deutschland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/5Ob93_15k`) (sent_id: `deanon_TRAIN/5Ob93_15k_8`)


Weiters liege - soweit überschaubar - keine höchstgerichtliche Rechtsprechung zur Frage vor, ob durch eine hier vorliegende Vereinbarung zwischen dem Bauträger und den Käufern bzw Wohnungseigentümern über eine bestimmte Art der Bepflanzung in das Zubehör (Garten) eines anderen Wohnungseigentümers eingegriffen werden könne.

**False Positives:**

- `Garten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_30`)


Der Beklagte habe ihn nicht darüber aufgeklärt, dass die Ausschüttungen keine Gewinne seien, sondern Rückzahlungen des eigenen investierten Kapitals, und von den Gesellschaftsgläubigern auch wieder zurückverlangt werden könnten, das (Total-)Verlustrisiko (Insolvenzrisiko) infolge der hohen Fremdkapitalquote (Fremdfinanzierung durch Banken) besonders hoch sei, der Beklagte für die Vermittlung über das jeweilige Agio von anteilig 2,5 bis 5 % hinaus auch noch Provisionszahlungen (= Innenprovision/Retrozession/Kick-Back-Zahlungen) von 5 bis 6 % und daher 7,5 bis 11 % des investierten Kapitals erhalten habe und das eingezahlte Kapital exzessiv – nämlich mit rund 20 bis 29 % – mit „Weichkosten“ (Vertriebsspesen) belastet sei.

**False Positives:**

- `Insolvenzrisiko` — no gold match — likely missing annotation
- `Vertriebsspesen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 67** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_104`)


Mit „Weichkosten“ (Vertriebskosten) muss ein Anleger grundsätzlich rechnen.

**False Positives:**

- `Vertriebskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_22`)


eine Untersuchung auf andere Schadstoffe (Vollanalyse) sei nicht erforderlich gewesen.

**False Positives:**

- `Vollanalyse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_71`)


Für Schadenersatzansprüche gegen einen Kaufmann (Unternehmer) gilt, dass diese nur dann vor die Handelsgerichte gehören, wenn sie aus der Erfüllung, Schlechterfüllung oder Nichterfüllung eines Handelsgeschäfts (unternehmensbezogenen Geschäfts) abgeleitet werden (RS0113977; RS0046419).

**False Positives:**

- `Unternehmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_140`)


Die Klägerin behauptet überdies Arglist der Beklagten: Der listig Irreführende kann dem Begehren des Vertragspartners auf angemessene Vergütung nach § 872 ABGB (Vertragsanpassung) die Einwendung, dass er den Vertrag anders nicht geschlossen hätte, nur entgegensetzen, wenn durch die begehrte Anpassung wesentliche Interessen auf seiner Seite beeinträchtigt würden (nicht aber schon, weil er den betrügerisch herausgelockten Vorteil auf jeden Fall behalten will) (RS0014780).

**False Positives:**

- `Vertragsanpassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/6Ob22_20h`) (sent_id: `deanon_TRAIN/6Ob22_20h_20`)


Zur Ermittlung des Umfangs der betroffenen Flächen (Trennstücke) wäre aber die Anführung auch der „ursprünglichen“ Grenze erforderlich, die in derartigen Fällen vielfach nicht bekannt oder gerade strittig sein werde.

**False Positives:**

- `Trennstücke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_122`)


Es könnten also „Befugnisträger“ (Kammermitglied) und Unternehmensträger (Gesellschaft) unter Umständen auseinanderfallen.

**False Positives:**

- `Kammermitglied` — no gold match — likely missing annotation
- `Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 73** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_123`)


In solchen Fällen könne es daher nicht darauf ankommen, dass der im Firmenbuch eingetragene bzw einzutragende Rechtsträger (Gesellschaft) der jeweiligen Kammer angehöre (dies sei ja gar nicht möglich), sondern es sei auf die dahinter stehenden Befugnisträger abzustellen, von denen der Rechtsträger (Unternehmensträger) die Berechtigung zur Berufsausübung in der Rechtsform einer Gesellschaft ableiten könne.

**False Positives:**

- `Gesellschaft` — no gold match — likely missing annotation
- `Unternehmensträger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 74** (doc_id: `deanon_TRAIN/7Ob113_14i`) (sent_id: `deanon_TRAIN/7Ob113_14i_203`)


3.3. Bestimmungen, die die Zulässigkeit von Obduktionen (Leichenöffnungen) oder Exhumierungen (Enterdigungen) regeln, finden sich verstreut sowohl in verschiedenen Bundesgesetzen als auch in Landesgesetzen.

**False Positives:**

- `Leichenöffnungen` — no gold match — likely missing annotation
- `Enterdigungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 75** (doc_id: `deanon_TRAIN/7Ob14_24w`) (sent_id: `deanon_TRAIN/7Ob14_24w_19`)


sofern und solange die tatsächlichen oder behaupteten Forderungen und Gegenforderungen der Vertragsparteien (Gesamtansprüche) aufgrund desselben Versicherungsfalles im Sinne des Artikel 2.3.

**False Positives:**

- `Gesamtansprüche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/7Ob14_24w`) (sent_id: `deanon_TRAIN/7Ob14_24w_76`)


Auch § 43 Abs 5 IO verweist – wie auch bereits die Vorgängerbestimmung der KO – Anfechtungsklagen des Insolvenzverwalters (Masseverwalters) in die Zuständigkeit des Insolvenzgerichts, was diese Sichtweise bestärkt.

**False Positives:**

- `Masseverwalters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/7Ob165_18t`) (sent_id: `deanon_TRAIN/7Ob165_18t_14`)


9. 2016 (Postaufgabe) einen Antrag auf Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Rekursfrist und führte in einem den Rekurs aus.

**False Positives:**

- `Postaufgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/7Ob17_13w`) (sent_id: `deanon_TRAIN/7Ob17_13w_20`)


(Zeitlicher Geltungsbereich) 1.

**False Positives:**

- `Zeitlicher Geltungsbereich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/7Ob17_13w`) (sent_id: `deanon_TRAIN/7Ob17_13w_59`)


Die Klägerin habe als Unterhaltsschuldnerin gegen den Vater aus dieser Vereinbarung primär einen Befreiungs- oder „Freistellungsanspruch“, der sich erst im Fall der Nichterfüllung dieser „Freistellung“ durch den Erfüllungsübernehmer (Vater) und einer Unterhaltszahlung durch die Klägerin selbst zu einem (auf Geldleistung lautenden) Schadenersatzanspruch wandle.

**False Positives:**

- `Vater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/7Ob17_13w`) (sent_id: `deanon_TRAIN/7Ob17_13w_98`)


Erfüllt der Übernehmer (Vater) seine Verpflichtung zur Leistung an den Gläubiger nicht, muss der Schuldner nicht unbedingt selbst leisten, sondern kann seinen Befreiungsanspruch durch eine auf Leistung unmittelbar an den Gläubiger gerichtete Klage gegen den Übernehmer geltend machen.

**False Positives:**

- `Vater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_6`)


2.Teilurteil: Der Revision wird hinsichtlich der Punkte II 1. bis 5. des Urteils des Berufungsgerichts (Klauseln) nicht Folge gegeben.

**False Positives:**

- `Klauseln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_8`)


3. Das Revisionsverfahren hinsichtlich des Punktes I. des Urteils des Berufungsgerichts (Zahlscheingebühr) wird bis zur Entscheidung des Gerichtshofs der Europäischen Union über den vom Obersten Gerichtshof am 8. November 2011 in der Rechtssache 10 Ob 31/11y gestellten Antrag auf Vorabentscheidung unterbrochen.

**False Positives:**

- `Zahlscheingebühr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_27`)


Zu 2.: DieRevision gegen Punkt II. der Entscheidung des Berufungsgerichts(Klauseln) ist zulässig, sie ist aber nicht berechtigt.

**False Positives:**

- `Klauseln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_144`)


Der Versicherer ist berechtigt, die für die längere Vertragsdauer eingeräumten Prämiennachlässe (Dauerrabatt) nachzuverrechnen.“

**False Positives:**

- `Dauerrabatt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_293`)


11. 2007 über Zahlungsdienste im Binnenmarkt dahin auszulegen, dass er auch auf das Vertragsverhältnis zwischen einem Mobilfunkbetreiber als Zahlungsempfänger und seinen Privatkunden (Verbraucher) als Zahler Anwendung zu finden hat?

**False Positives:**

- `Verbraucher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_294`)


2. Sind ein vom Zahler eigenhändig unterschriebener Zahlschein bzw das auf einem unterschriebenen Zahlschein beruhende Verfahren zur Erteilung von Überweisungsaufträgen sowie das zur Erteilung von Überweisungsaufträgen im Online-Banking (Telebanking) vereinbarte Verfahren als 'Zahlungsinstrumente' im Sinn von Art 4 Z 23 und des Art 52 Abs 3 der RL 2007/64/EG anzusehen?

**False Positives:**

- `Telebanking` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_TRAIN/7Ob202_19k`) (sent_id: `deanon_TRAIN/7Ob202_19k_21`)


Im vorliegenden Fall wurden mit der Zurückweisung des Widerspruchs des Antragsgegners aus formellen Gründen (Verspätung) und deren Bestätigung keine Sachentscheidungen über den Widerspruch getroffen;

**False Positives:**

- `Verspätung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_TRAIN/7Ob205_19a`) (sent_id: `deanon_TRAIN/7Ob205_19a_63`)


Dem gegenüber ist ein deklaratives Anerkenntnis (Rechtsgeständnis) kein Leistungsversprechen, sondern eine durch Gegenbeweis widerlegbare Wissenserklärung (RS0032784 [T10]).

**False Positives:**

- `Rechtsgeständnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_22`)


[…] Artikel 8 Welche Pflichten hat der Versicherungsnehmer zur Sicherung seines Deckungsanspruches zu beachten (Allgemeine Obliegenheiten) 1.

**False Positives:**

- `Allgemeine Obliegenheiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_245`)


Zwar muss eine gewisse Verdienstlichkeit der Tätigkeit des Rechtsanwalts für den als Erfolg aufgefassten Ausgang eines Verfahrens jedenfalls vorliegen, wäre doch sonst ein Zuschlag von 50 % allein aufgrund des Verfahrensausgangs (Freispruch), der ohne jegliche Mitwirkung des Verteidigers zustande kam (etwa aufgrund Verjährung der Strafbarkeit, die dem Verteidiger nicht bewusst war, sodass er dazu nichts ausgeführt hat), nach Angemessenheitskriterien nicht zu rechtfertigen.

**False Positives:**

- `Freispruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_TRAIN/7Ob6_20p`) (sent_id: `deanon_TRAIN/7Ob6_20p_29`)


1.2.Diese Vorlagefrage 1 hat der EuGH wie folgt beantwortet: „1. Art. 15 Abs. 1 der Zweiten Richtlinie 90/619/EWG des Rates vom 8. November 1990 zur Koordinierung der Rechts- und Verwaltungsvorschriften für die Direktversicherung (Lebensversicherung) und zur Erleichterung der tatsächlichen Ausübung des freien Dienstleistungsverkehrs sowie zur Änderung der Richtlinie 79/267/EWG in der durch die Richtlinie 92/96/EWG des Rates vom 10. November 1992 geänderten Fassung in Verbindung mit Art. 31 der Richtlinie 92/96/EWG des Rates vom 10. November 1992 zur Koordinierung der Rechts- und Verwaltungsvorschriften für die Direktversicherung (Lebensversicherung) sowie zur Änderung der Richtlinien 79/267/EWG und 90/619/EWG (Dritte Richtlinie Lebensversicherung), Art. 35 Abs. 1 der Richtlinie 2002/83/EG des Europäischen Parlaments und des Rates vom 5. November 2002 über Lebensversicherungen in Verbindung mit deren Art. 36 Abs. 1 und Art. 185 Abs. 1 der Richtlinie 2009/138/EG des Europäischen Parlaments und des Rates vom 25. November 2009 betreffend die Aufnahme und Ausübung der Versicherungs- und der Rückversicherungstätigkeit (Solvabilität II) in Verbindung mit deren Art. 186 Abs. 1 sind dahin auszulegen, dass die Rücktrittsfrist bei einem Lebensversicherungsvertrag auch dann ab dem Zeitpunkt zu laufen beginnt, zu dem der Versicherungsnehmer davon in Kenntnis gesetzt wird, dass der Vertrag geschlossen ist, wenn in den Informationen, die der Versicherer dem Versicherungsnehmer mitteilt, – nicht angegeben ist, dass die Erklärung des Rücktritts nach dem auf den Vertrag anwendbaren nationalen Recht keiner besonderen Form bedarf, oder – eine Form verlangt wird, die nach dem auf den Vertrag anwendbaren nationalen Recht oder den Bestimmungen des Vertrags nicht vorgeschrieben ist, solange dem Versicherungsnehmer durch die Informationen nicht die Möglichkeit genommen wird, sein Rücktrittsrecht im Wesentlichen unter denselben Bedingungen wie bei Mitteilung zutreffender Informationen auszuüben.

**False Positives:**

- `Lebensversicherung` — no gold match — likely missing annotation
- `Lebensversicherung` — no gold match — likely missing annotation
- `Dritte Richtlinie Lebensversicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 92** (doc_id: `deanon_TRAIN/7Ob6_20p`) (sent_id: `deanon_TRAIN/7Ob6_20p_82`)


4.3.Im Alltag ist für eine Vielzahl von (rechtsgeschäftlichen) Erklärungen die Schriftform auch bei Privaten (Verbrauchern) eine geradezu typische und faktisch regelmäßig praktizierte Mitteilungsform, die für jedermann einfach und ohne besonderen Aufwand durchzuführen ist, sodass keine für ihre Effektivität relevanten Hürden entgegenstehen.

**False Positives:**

- `Verbrauchern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/7Ob6_20p`) (sent_id: `deanon_TRAIN/7Ob6_20p_89`)


Die Schriftform steht im gegebenen Kontext nicht mit europarechtlichen Vorgaben im Widerspruch, ist eine auch für Private (Verbraucher) ohne praktische Hürden wahrnehmbare und faktisch regelmäßig praktizierte Mitteilungsform und dient im vorliegenden Zusammenhang dem Schutz des Versicherungsnehmers bei der Wahrnehmung seiner Beweispflicht.

**False Positives:**

- `Verbraucher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_23`)


Die Parteien beabsichtigen, zur Gestaltung von Zinsänderungs-, Währungskurs- und sonstigen Kursrisiken im Rahmen ihrer Geschäftstätigkeit Finanztermingeschäfte abzuschließen, die den Austausch von Geldbeträgen in verschiedenen Währungen oder von Geldbeträgen, die auf der Grundlage von variablen oder festen Zinssätzen, Kursen, Preisen oder sonstigen Wertmessern, einschließlich diesbezüglicher Durchschnittswerte (Indizes), ermittelt werden oder die Lieferung oder Übertragung von Wertpapieren, anderen Finanzinstrumenten oder Edelmetallen oder ähnlichen Leistungen zum Gegenstand haben.

**False Positives:**

- `Indizes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_TRAIN/8Ob19_24p`) (sent_id: `deanon_TRAIN/8Ob19_24p_8`)


3. 2017 erstmals zugelassenen Personenkraftwagen der Marke Audi Q5 2.0 TDI ultra quattro Sport mit einem Kilometerstand von damals 200 km (Klagsfahrzeug), in dem ein von der Beklagten hergestellter 2,0 1–4 Zylinder-Dieselmotor der Baureihe EA288 mit einer Leistung von 140 kW verbaut ist.

**False Positives:**

- `Klagsfahrzeug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_TRAIN/8Ob19_24p`) (sent_id: `deanon_TRAIN/8Ob19_24p_27`)


Das Berufungsgericht ließ den Rekurs gegen diese Entscheidung zu, weil höchstgerichtliche Rechtsprechung zur Frage fehle, ob und unter welchen Voraussetzungen ein Komponentenzulieferer (Motorhersteller) hafte, und weiters zu den Fragen, ob eine Abschalteinrichtung gemäß Art 3 Z 10 VO 715/2007/EG auch dann unzulässig sein könne, wenn sie aufgrund der vorherrschenden Außentemperaturen zwar nicht den überwiegenden Teil, aber doch einen erheblichen Teil eines Jahres funktionieren müsste, um den Motor vor Beschädigung oder Unfall zu schützen und den sicheren Betrieb des Fahrzeugs zu gewährleisten;

**False Positives:**

- `Motorhersteller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_TRAIN/8Ob33_23w`) (sent_id: `deanon_TRAIN/8Ob33_23w_8`)


Damit strebte er erkennbar eine Unterhaltserhöhung an (Unterhaltserhöhungsantrag).

**False Positives:**

- `Unterhaltserhöhungsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Person in 'gegen' or 'von' context`

**F1:** 0.001 | **Precision:** 0.014 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `e25ebe36`  
**Description:**
Captures names appearing after 'gegen' (against) or 'von' (of/from) in legal contexts, often without titles.

**Content:**
```
(?:gegen\s+|von\s+)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.014 | 0.001 | 0.001 | 70 | 1 | 69 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 69 | 1218 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_10`)


In dem vor dem Oberlandesgericht Köln geführten Pflegschaftsverfahren vereinbarten die Eltern am 8. Mai 2018 die Beibehaltung des gemeinsamen Obsorge- und Aufenthaltsbestimmungsrechts für beide Kinder, wobei der Lebensmittelpunkt von Heinrich Debbert beim Vater (der inzwischen ebenfalls nach Wien übersiedelt war) und für Ashley Frohnsdorfer eine wöchentlich abwechselnde Betreuung festgelegt wurde.

| Predicted | Gold |
|---|---|
| `Heinrich Debbert` | `Heinrich Debbert` |

**Missed by this rule (FN):**

- `Ashley Frohnsdorfer` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 1** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Szczech vertretenen Inn Triconal Holding GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Susanna Szczech` — partial — gold is substring of pred: `Szczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Szczech`(person)
- `Inn Triconal Holding GesmbH`(organisation)
- `Co KG`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 3** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 4** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

**Example 5** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_3`)


Kopf Der Oberste Gerichtshof hat am 8. August 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Josef Klös und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1, Abs 3 StGB, AZ 72 Hv 8/17g des Landesgerichts Klagenfurt, über die Anzeige der Ausgeschlossenheit der Vizepräsidentin des Obersten Gerichtshofs Mag. Marek gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Josef Kl` — positional overlap with gold: `Klös`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klös`(person)

**Example 6** (doc_id: `deanon_TRAIN/12Ns4_15g`) (sent_id: `deanon_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bachel wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Gerhard Bachel` — partial — gold is substring of pred: `Bachel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachel`(person)

**Example 7** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_3`)


Kopf Der Oberste Gerichtshof hat am 18. Oktober 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Bilinska als Schriftführerin in der Strafsache gegen Gerfried Hundgeburth und eine Angeklagte wegen des Verbrechens der betrügerischen Krida nach §§ 156 Abs 1, 161 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten Renata Holzhey gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 11. April 2011, GZ 602 Hv 4/10m-58, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gerfried Hundgeburth` — partial — gold is substring of pred: `Hundgeburth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hundgeburth`(person)
- `Holzhey`(person)

**Example 8** (doc_id: `deanon_TRAIN/12Os11_19p`) (sent_id: `deanon_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Margardt wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Thomas Margardt` — partial — gold is substring of pred: `Margardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Margardt`(person)

**Example 9** (doc_id: `deanon_TRAIN/12Os164_12b`) (sent_id: `deanon_TRAIN/12Os164_12b_3`)


Kopf Der Oberste Gerichtshof hat am 31. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Dr. Pausa als Schriftführerin in der Strafsache gegen Giorgi Standtke wegen des Verbrechens des gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 129 Z 1, 130 vierter Fall und 15 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien vom 17. Oktober 2012, GZ 95 Hv 92/12p-26, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Giorgi Standtke` — partial — gold is substring of pred: `Standtke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Standtke`(person)

**Example 10** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pitzenbauer wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Nenad Pitzenbauer` — partial — gold is substring of pred: `Pitzenbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pitzenbauer`(person)

**Example 11** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Mattheiß und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Tiepoldt auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Viktor Matthei` — positional overlap with gold: `Mattheiß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mattheiß`(person)
- `Tiepoldt`(person)

**Example 12** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Viktor Mittermair` — partial — gold is substring of pred: `Mittermair`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 13** (doc_id: `deanon_TRAIN/12Os40_19b`) (sent_id: `deanon_TRAIN/12Os40_19b_3`)


Kopf Der Oberste Gerichtshof hat am 27. Februar 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden sowie durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Schriftführerin Maurer in der Strafsache gegen Alexander Jastrzemsky wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Jugendschöffengericht vom 8. Jänner 2019, GZ 23 Hv 29/18y-28, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alexander Jastrzemsky` — partial — gold is substring of pred: `Jastrzemsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jastrzemsky`(person)

**Example 14** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_3`)


Kopf Der Oberste Gerichtshof hat am 18. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Adamowitsch als Schriftführerin in der Strafsache gegen Norbert Noelker wegen Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB, AZ 16 Hv 32/15g des Landesgerichts Krems an der Donau, über die Beschwerde des Verurteilten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 7. März 2017, AZ 20 Bs 59/17y, nach Einsichtnahme durch die Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Norbert Noelker` — partial — gold is substring of pred: `Noelker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noelker`(person)

**Example 15** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__14`)


Am 3. Mai 2010 brachte die Staatsanwaltschaft Wiener Neustadt beim Bezirksgericht Baden erneut einen Strafantrag gegen Christian Kowalzyk wegen des Verdachts der (während der Probezeit begangenen) Vergehen des unbefugten Gebrauchs von Fahrzeugen nach § 136 Abs 1 StGB sowie der Urkundenunterdrückung nach § 229 Abs 1 StGB ein und beantragte zugleich die „Straffestsetzung zu AZ 12 U 86/07z des Bezirksgerichtes Baden“ (ON 3 im Akt AZ 12 U 105/10y).

**False Positives:**

- `Christian Kowalzyk` — partial — gold is substring of pred: `Kowalzyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Baden`(organisation)
- `Kowalzyk`(person)

**Example 16** (doc_id: `deanon_TRAIN/12Os80_15d`) (sent_id: `deanon_TRAIN/12Os80_15d_3`)


Kopf Der Oberste Gerichtshof hat am 28. Jänner 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Jukic als Schriftführerin in der Strafsache gegen Arben Dietlof wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 17. April 2015, GZ 39 Hv 127/14v-47, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Arben Dietlof` — partial — gold is substring of pred: `Dietlof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dietlof`(person)

**Example 17** (doc_id: `deanon_TRAIN/13Os100_16d`) (sent_id: `deanon_TRAIN/13Os100_16d_3`)


Kopf Der Oberste Gerichtshof hat am 12. Oktober 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Krenn als Schriftführerin in der Strafsache gegen Richard Berzine und einen anderen Angeklagten wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Clemens Feidel sowie die Berufungen des Angeklagten Richard Boudewijn und der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 30. Mai 2016, GZ 61 Hv 45/16w-98, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Richard Berzine` — partial — gold is substring of pred: `Berzine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Berzine`(person)
- `Feidel`(person)
- `Boudewijn`(person)

**Example 18** (doc_id: `deanon_TRAIN/13Os100_16d`) (sent_id: `deanon_TRAIN/13Os100_16d_7`)


Danach hat er in Untertweng-Eichenweg 7, 9071 Plöschenberg, Österreich (1) am 11. Jänner 2016 mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz (US 8) zur Ausführung eines von Richard Bradley unter Verwendung einer Waffe begangenen Raubes beigetragen (§ 12 dritter Fall StGB), indem er den unmittelbaren Täter zum und vom Tatort chauffierte, (2) am 21. Jänner 2016 mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz (US 9) zu einem von Richard Birkenberg unter Verwendung einer Waffe begangenen Raub beigetragen (§ 12 dritter Fall StGB), indem er den unmittelbaren Täter zum Tatort chauffierte, dort Aufpasserdienste leistete, dem unmittelbaren Täter telefonisch einen günstigen Ausführungszeitpunkt nannte und das Fluchtfahrzeug vom Tatort lenkte, (3) vom 22. Jänner 2016 bis zum 3. Februar 2016, wenn auch nur fahrlässig, eine Gaspistole samt Munition besessen, obwohl ihm dies gemäß § 12 WaffG verboten war, und (4) bis zum 3. Februar 2016, wenn auch nur fahrlässig, eine gemäß § 17 Abs 1 Z 6 WaffG verbotene Waffe, nämlich einen Teleskopschlagstock, unbefugt besessen.

**False Positives:**

- `Richard Bradley` — partial — gold is substring of pred: `Bradley`
- `Richard Birkenberg` — partial — gold is substring of pred: `Birkenberg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Untertweng-Eichenweg 7, 9071 Plöschenberg, Österreich`(address)
- `Bradley`(person)
- `Birkenberg`(person)

**Example 19** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Abdullah Klingfuss wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. Juli 2019, GZ 41 Hv 18/18i-55, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Abdullah Klingfuss` — partial — gold is substring of pred: `Klingfuss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingfuss`(person)

**Example 20** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_7`)


Danach hat er in Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich und an anderen Orten 1) am 15. Februar 2014 Asli Davidsmeyer mit Gewalt zur Duldung des Analverkehrs genötigt, indem er sie auf ein Bett stieß, im Nacken festhielt und gegen ihren Willen seinen Penis in ihren After einführte, 2) durch im Urteil bezeichnete Handlungen und Äußerungen längere Zeit hindurch gegen andere Personen fortgesetzt Gewalt ausgeübt, und zwar a) ab dem 1. Juni 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014 gegen Asli Dagtekin, b) ab dem Jahr 2012 bis zum 19. November 2014, also länger als ein Jahr, gegen seine am 25. April 2008 geborene, somit unmündige, Tochter Berfin Krempl, sowie c) ab dem Jahr 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014, also länger als ein Jahr, gegen seinen am 18. Juni 2003 geborenen, somit unmündigen, Sohn Ilhan Kukolies, 3) Asli Dücking durch im Urteil bezeichnete Handlungen vorsätzlich am Körper verletzt, und zwar a) im September 2008, wodurch die Genannte Schwellungen und Hämatome erlitt, und b) zwischen September und November 2008, wodurch die Genannte das Bewusstsein verlor und eine Schwellung am Hinterkopf und Rötungen im Kniebereich erlitt, weiters Asli Dietzler durch im Urteil bezeichnete Äußerungen 4) zwischen September und November 2008 zu einer Unterlassung genötigt und 5) am 9. Februar 2017 zumindest mit einer Verletzung am Körper gefährlich bedroht, um sie in Furcht und Unruhe zu versetzen.

**False Positives:**

- `Asli Dagtekin` — partial — gold is substring of pred: `Dagtekin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich`(address)
- `Davidsmeyer`(person)
- `Dagtekin`(person)
- `Krempl`(person)
- `Kukolies`(person)
- `Dücking`(person)
- `Dietzler`(person)

**Example 21** (doc_id: `deanon_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Stelzl wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

**False Positives:**

- `Zoltan Stelzl` — partial — gold is substring of pred: `Stelzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stelzl`(person)

**Example 22** (doc_id: `deanon_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Mitzkait wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag.

**False Positives:**

- `Nikola Mitzkait` — partial — gold is substring of pred: `Mitzkait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mitzkait`(person)

**Example 23** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__3`)


Kopf Der Oberste Gerichtshof hat am 22. November 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Krausam als Schriftführerin in der Strafsache gegen Jasmin Fejfar wegen Vergehen der Erschleichung einer Leistung nach § 149 Abs 1 StGB, AZ 36 Hv 160/11y des Landesgerichts Innsbruck, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 10. Jänner 2012 (ON 49) und andere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Jasmin Fejfar` — partial — gold is substring of pred: `Fejfar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fejfar`(person)

**Example 24** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Lässig und Dr. Oberressl in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mario Speer und andere Angeklagte wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 3, 148 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 12 Hv 110/16x des Landesgerichts Wels, über die Grundrechtsbeschwerde des genannten Angeklagten gegen die Verfügung des Vorsitzenden vom 15. November 2016 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mario Speer` — partial — gold is substring of pred: `Speer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Speer`(person)

**Example 25** (doc_id: `deanon_TRAIN/13Os22_20i`) (sent_id: `deanon_TRAIN/13Os22_20i_3`)


Kopf Der Oberste Gerichtshof hat am 27. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in der Strafsache gegen Erwin Waegert wegen des Verbrechens des Mordes nach §§ 15, 75 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Geschworenengericht vom 19. Dezember 2019, GZ 19 Hv 72/19m-46, nach Anhörung der Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung werden zurückgewiesen.

**False Positives:**

- `Erwin Waegert` — partial — gold is substring of pred: `Waegert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waegert`(person)

**Example 26** (doc_id: `deanon_TRAIN/13Os23_15d`) (sent_id: `deanon_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wissink wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Karl Wissink` — partial — gold is substring of pred: `Wissink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wissink`(person)

**Example 27** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Junghuber wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Erik Junghuber` — partial — gold is substring of pred: `Junghuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Junghuber`(person)

**Example 28** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jerzenbek, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

**False Positives:**

- `Erik Jerzenbek` — partial — gold is substring of pred: `Jerzenbek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jerzenbek`(person)

**Example 29** (doc_id: `deanon_TRAIN/13Os34_19b`) (sent_id: `deanon_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weigenannt wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Wolfgang Weigenannt` — partial — gold is substring of pred: `Weigenannt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weigenannt`(person)

**Example 30** (doc_id: `deanon_TRAIN/13Os37_12h`) (sent_id: `deanon_TRAIN/13Os37_12h_3`)


Kopf Der Oberste Gerichtshof hat am 10. Mai 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Wohlmuth als Schriftführerin in der Strafsache gegen Michael Liebhold und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Waßmann und des DI Georg Lu Babette Prusak gegen den Beschluss des Oberlandesgerichts Innsbruck vom 20. März 2012, AZ 6 Bs 130/12m, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Liebhold` — partial — gold is substring of pred: `Liebhold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Liebhold`(person)
- `Waßmann`(person)
- `Babette Prusak`(person)

**Example 31** (doc_id: `deanon_TRAIN/13Os68_18a`) (sent_id: `deanon_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Coolhaas wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Mihai Coolhaas` — partial — gold is substring of pred: `Coolhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Coolhaas`(person)

**Example 32** (doc_id: `deanon_TRAIN/13Os6_14b`) (sent_id: `deanon_TRAIN/13Os6_14b_3`)


Kopf Der Oberste Gerichtshof hat am 14. März 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Gansterer als Schriftführerin in der Strafsache gegen Valentino Thünissen wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 9. Dezember 2013, GZ 52 Hv 65/13b-21, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Valentino Th` — positional overlap with gold: `Thünissen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thünissen`(person)

**Example 33** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Urbansky wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Robert Urbansky` — partial — gold is substring of pred: `Urbansky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Urbansky`(person)

**Example 34** (doc_id: `deanon_TRAIN/13Os8_11t`) (sent_id: `deanon_TRAIN/13Os8_11t_3`)


Kopf Der Oberste Gerichtshof hat am 17. Februar 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Kirnbauer als Schriftführerin in der Strafsache gegen Delroy Dambrowsky wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 16. November 2010, GZ 031 Hv 125/10t-58, sowie die Beschwerde des Angeklagten gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Delroy Dambrowsky` — partial — gold is substring of pred: `Dambrowsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dambrowsky`(person)

**Example 35** (doc_id: `deanon_TRAIN/13Os97_11f`) (sent_id: `deanon_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Gehler wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

**False Positives:**

- `Ernst Gehler` — partial — gold is substring of pred: `Gehler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gehler`(person)

**Example 36** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Hermanni wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

**False Positives:**

- `Christoph Hermanni` — partial — gold is substring of pred: `Hermanni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermanni`(person)

**Example 37** (doc_id: `deanon_TRAIN/14Os108_18s`) (sent_id: `deanon_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Reichenbach und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kulaksiz gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Misha Reichenbach` — partial — gold is substring of pred: `Reichenbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reichenbach`(person)
- `Kulaksiz`(person)

**Example 38** (doc_id: `deanon_TRAIN/14Os121_19d`) (sent_id: `deanon_TRAIN/14Os121_19d_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Emir Kles wegen Verbrechen der schweren Körperverletzung nach §§ 15, 84 Abs 4 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 22. August 2019, GZ 52 Hv 23/19b-16, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Emir Kles` — partial — gold is substring of pred: `Kles`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kles`(person)

**Example 39** (doc_id: `deanon_TRAIN/14Os132_10h`) (sent_id: `deanon_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahner wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Tomislav Ahner` — partial — gold is substring of pred: `Ahner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ahner`(person)

**Example 40** (doc_id: `deanon_TRAIN/14Os136_19k`) (sent_id: `deanon_TRAIN/14Os136_19k_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Dimitri Thomassin wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 vierter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 30. September 2019, GZ 632 Hv 2/19a-138, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dimitri Thomassin` — partial — gold is substring of pred: `Thomassin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomassin`(person)

**Example 41** (doc_id: `deanon_TRAIN/14Os16_15g`) (sent_id: `deanon_TRAIN/14Os16_15g_3`)


Kopf Der Oberste Gerichtshof hat am 28. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Moelle als Schriftführerin in der Strafsache gegen Alessandro Braunmiller wegen des Verbrechens nach § 3g VerbotsG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Klagenfurt als Geschworenengericht vom 26. November 2014, GZ 38 Hv 50/14d-36, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alessandro Braunmiller` — partial — gold is substring of pred: `Braunmiller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Braunmiller`(person)

**Example 42** (doc_id: `deanon_TRAIN/14Os63_12i`) (sent_id: `deanon_TRAIN/14Os63_12i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart des Richteramtsanwärters Mag. Lindenbauer als Schriftführer in der Strafsache gegen Johann Haugk wegen des Verbrechens des Suchtgifthandels nach §§ 12 dritter Fall, 15 StGB, 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 29. Februar 2012, GZ 35 Hv 150/11z-93, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Johann Haugk` — partial — gold is substring of pred: `Haugk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Haugk`(person)

**Example 43** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_3`)


Kopf Der Oberste Gerichtshof hat am 5. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Draginja Nielson und einen Angeklagten wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 30. März 2017, GZ 26 Hv 117/16h-55, sowie ihre Beschwerde gegen den zugleich gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Draginja Nielson` — partial — gold is substring of pred: `Nielson`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nielson`(person)

**Example 44** (doc_id: `deanon_TRAIN/14Os71_17y`) (sent_id: `deanon_TRAIN/14Os71_17y_3`)


Kopf Der Oberste Gerichtshof hat am 3. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Adam Albanesi wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Geschworenengericht vom 5. Mai 2017, GZ 35 Hv 15/17a-83, sowie über die Beschwerde des Angeklagten gegen den Beschluss auf Widerruf einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Adam Albanesi` — partial — gold is substring of pred: `Albanesi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albanesi`(person)

**Example 45** (doc_id: `deanon_TRAIN/15Os110_17s`) (sent_id: `deanon_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Valerius Niesse, MA und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Laila Niezoldi gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Shafiqullah Valerius Niesse` — positional overlap with gold: `Valerius Niesse, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerius Niesse, MA`(person)
- `Laila Niezoldi`(person)

**Example 46** (doc_id: `deanon_TRAIN/15Os114_10v`) (sent_id: `deanon_TRAIN/15Os114_10v_3`)


Kopf Der Oberste Gerichtshof hat am 15. September 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger als weitere Richter, in Gegenwart der Rechtspraktikantin Mag. Reich als Schriftführerin, in der Strafsache gegen Marek Dirksmeyer wegen des Verbrechens des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. April 2010, GZ 40 Hv 1/10w-32, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung des Angeklagten „wegen Schuld“ werden zurückgewiesen.

**False Positives:**

- `Marek Dirksmeyer` — partial — gold is substring of pred: `Dirksmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dirksmeyer`(person)

**Example 47** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_3`)


Kopf Der Oberste Gerichtshof hat am 19. Februar 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Ent als Schriftführer in der Strafsache gegen Christian Poethke und einen anderen Angeklagten wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer anderen strafbaren Handlung, (zuletzt) AZ 33 Hv 70/12x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Rakhart Jörg Andrich auf Erneuerung des Strafverfahrens gemäß § 363a Abs 1 StPO nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Christian Poethke` — partial — gold is substring of pred: `Poethke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poethke`(person)
- `Jörg Andrich`(person)

**Example 48** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Bahar wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Manfred Bahar` — partial — gold is substring of pred: `Bahar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bahar`(person)

**Example 49** (doc_id: `deanon_TRAIN/15Os53_16g`) (sent_id: `deanon_TRAIN/15Os53_16g_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Janisch als Schriftführerin in der Strafsache gegen Eduard Meisslein wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 erster Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 21. Dezember 2015, GZ 181 Hv 4/15x-46, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Eduard Meisslein` — partial — gold is substring of pred: `Meisslein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Meisslein`(person)

**Example 50** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Rauhe und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Johann Rauhe` — partial — gold is substring of pred: `Rauhe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rauhe`(person)

**Example 51** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_8`)


Text Gründe: Die Staatsanwaltschaft Wels führt zu AZ 17 St 77/19g ein Ermittlungsverfahren gegen Johann Remppel wegen des Verdachts des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG und weiterer strafbarer Handlungen.

**False Positives:**

- `Johann Remppel` — partial — gold is substring of pred: `Remppel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Remppel`(person)

**Example 52** (doc_id: `deanon_TRAIN/15Os72_12w`) (sent_id: `deanon_TRAIN/15Os72_12w_4`)


Karlicek als Schriftführerin in der Strafsache gegen Rudolf Czaya wegen Verbrechen der Vergewaltigung nach §§ 201 Abs 1, 15 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 23. März 2012, GZ 631 Hv 2/12h-28, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Rudolf Czaya` — partial — gold is substring of pred: `Czaya`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Czaya`(person)

**Example 53** (doc_id: `deanon_TRAIN/15Os96_17g`) (sent_id: `deanon_TRAIN/15Os96_17g_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Roman Abbold wegen des Verbrechens der terroristischen Vereinigung nach § 278b Abs 2 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 16. Mai 2017, GZ 39 Hv 6/17h-37, sowie über dessen Beschwerde gegen den Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Roman Abbold` — partial — gold is substring of pred: `Abbold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Abbold`(person)

**Example 54** (doc_id: `deanon_TRAIN/15Os96_17g`) (sent_id: `deanon_TRAIN/15Os96_17g_22`)


Nach dieser Schießübung wurde der Angeklagte von Umar Mergele besucht, welcher ihm erklärte, der Angeklagte werde bald zu ihm kommen, womit er meinte, dass dann dessen Ausbildung vorbei wäre.

**False Positives:**

- `Umar Mergele` — partial — gold is substring of pred: `Mergele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mergele`(person)

**Example 55** (doc_id: `deanon_TRAIN/15Os98_15y`) (sent_id: `deanon_TRAIN/15Os98_15y_3`)


Kopf Der Oberste Gerichtshof hat am 26. August 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Leisser als Schriftführerin in der Strafsache gegen Gottlieb Zekalla wegen des Verbrechens des Diebstahls durch Einbruch nach §§ 127, 129 Z 1 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 19. Mai 2015, GZ 39 Hv 105/13k-91, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur Dr. Ulrich, des Angeklagten und seines Verteidigers Dr. Pohle zu Recht erkannt:  Spruch

**False Positives:**

- `Gottlieb Zekalla` — partial — gold is substring of pred: `Zekalla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zekalla`(person)

**Example 56** (doc_id: `deanon_TRAIN/15Os9_12f`) (sent_id: `deanon_TRAIN/15Os9_12f_4`)


Linzner als Schriftführerin in der Strafsache gegen Georg Henckens wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

**False Positives:**

- `Georg Henckens` — partial — gold is substring of pred: `Henckens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Henckens`(person)

**Example 57** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Juni 2018 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Gerhard Obeser und eine Angeklagte wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und weiterer strafbarer Handlungen aus Anlass der Nichtigkeitsbeschwerde der Angeklagten Mag. (FH) Nicole Kochem gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 31. Oktober 2017, GZ 78 Hv 76/17a-76,nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Stani, des Angeklagten Gerhard Oravec und seines Verteidigers Dr. Gärtner zu Recht erkannt:  Spruch

**False Positives:**

- `Gerhard Obeser` — partial — gold is substring of pred: `Obeser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obeser`(person)
- `Kochem`(person)
- `Oravec`(person)

**Example 58** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_4`)


Das Urteil, das im Übrigen unberührt bleibt, wird im Schuldspruch A, demgemäß auch im Gerhard Oeste betreffenden Strafausspruch, aufgehoben und in diesem Umfang in der Sache selbst erkannt: Gerhard Opderbecke wird gemäß § 259 Z 3 StPO vom Vorwurf freigesprochen, er habe in Aichbach 59, 9131 Zapfendorf, Österreich A/ als Bürgermeister der Gemeinde Krautz, mithin als Beamter im strafrechtlichen Sinn, „mit dem Vorsatz, die Gemeinderäte der Gemeinde Kießlich an ihren Rechten gemäß §§ 28 Abs 1 und 2, 35 Abs 1, 78 Abs 1a K-AGO auf Einberufung des Gemeinderates und Behandlung von Erledigungen, die der Beschlussfassung durch den Gemeinderat vorbehalten waren, zu schädigen“, wiederholt seine Befugnis, im Namen der Gemeinde Klingenschmid als deren Organ in Vollziehung der Gesetze Amtsgeschäfte vorzunehmen, wissentlich missbraucht, indem er es unterließ, „Sitzungen des Gemeinderates zur Beschlussfassung über nachangeführte Geschäftsgänge und über die Adaptierung der Nebengebührenverordnung der Gemeinde einzuberufen, darüber einen Tagesordnungspunkt in einer Gemeinderatssitzung anzusetzen und hierfür Sitzungsvorträge nach § 78 K-AGO ausarbeiten zu lassen und indem er die entsprechenden Punkte mehrfach von der Tagesordnung der Gemeinderatssitzungen strich“, und zwar I/ zwischen 1. Juli 2010 und März 2015 über die Bestellung von Renate Dal zur Amtsleiterstellvertreterin und über die Gewährung einer monatlichen Mehrleistungszulage und Aufwandsent-schädigung für diese Funktion, „wodurch der Gemeinde Khatib ein Schaden im Gesamtbetrag von zumindest insgesamt 25.302,76 Euro inklusive Dienstgeberabgaben entstand“;

**False Positives:**

- `Renate Dal` — partial — gold is substring of pred: `Dal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oeste`(person)
- `Opderbecke`(person)
- `Aichbach 59, 9131 Zapfendorf, Österreich`(address)
- `Krautz`(person)
- `Kießlich`(person)
- `Klingenschmid`(person)
- `Dal`(person)
- `Khatib`(person)

**Example 59** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_118`)


Haben gemeinsame Kinder das Haus mit der Mutter bewohnt und hat diese die Kinder überwiegend betreut, wird (jedenfalls im Verhältnis zu den Kindern) in der Zurverfügungstellung von Wohnraum Naturalunterhalt liegen.

**False Positives:**

- `Wohnraum Naturalunterhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Roman Janis` — partial — gold is substring of pred: `Janis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Landesgericht Linz`(organisation)
- `Bezirksgericht Amstetten`(organisation)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 61** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_28`)


Dem stehe die Gewährleistung für die Lastenfreiheit und Freiheit von Nutzungsrechten Dritter nicht entgegen, weil damit die Löschung der Pfandrechte angesprochen worden sei und weil die Erwerber von der Überlassung einer Wohnung an die Klägerin durch ihre frühere Dienstgeberin gewusst hätten.

**False Positives:**

- `Nutzungsrechten Dritter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_69`)


Er konnte daher die Zusicherung der Verkäuferinnen, die Liegenschaft sei frei von Nutzungsrechten Dritter, nur so verstehen, dass damit andere Nutzungsrechte als jenes der Klägerin gemeint waren.

**False Positives:**

- `Nutzungsrechten Dritter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_165`)


[41]4.2.Dem für gemeinnützige Bauvereinigungen zuständigen Revisionsverband kommt überdies im Firmenbuchverfahren von Gesellschaften Parteistellung nach § 14 Abs 3 FBG soweit zu, als es Firmenbucheintragungen von Gesellschaftern dieser Gesellschaften betrifft, wenn der wirksame Erwerb der Gesellschafterstellung von der Zustimmung der Landesregierung nach § 10a Abs 1a WGG abhängig ist.

**False Positives:**

- `Gesellschaften Parteistellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/7Nc5_13i`) (sent_id: `deanon_TRAIN/7Nc5_13i_9`)


Die vorliegende Fallkonstellation ist geeignet, die Unbefangenheit von Hofrat Dr. Bertha Klefeldt in dieser Rechtssache in Zweifel zu ziehen.

**False Positives:**

- `Hofrat Dr` — positional overlap with gold: `Dr. Bertha Klefeldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Bertha Klefeldt`(person)

**Example 65** (doc_id: `deanon_TRAIN/7Ob150_17k`) (sent_id: `deanon_TRAIN/7Ob150_17k_32`)


2.Der Oberste Gerichtshof ist zur Auslegung von Allgemeinen Versicherungsbedingungen (AVB) nicht „jedenfalls“, sondern nur dann berufen, wenn das Berufungsgericht höchstgerichtliche Rechtsprechung missachtet hat oder für die Rechtseinheit oder Rechtsentwicklung bedeutsame Fragen zu lösen sind (RIS-Justiz RS0121516).

**False Positives:**

- `Allgemeinen Versicherungsbedingungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/7Ob79_10h`) (sent_id: `deanon_TRAIN/7Ob79_10h_10`)


Damit vermag der Kläger einen tauglichen Grund für die Zulassung seines außerordentlichen Rechtsmittels nicht aufzuzeigen:  Rechtliche Beurteilung Die Auslegung von Allgemeinen Versicherungsbedingungen hat sich am Maßstab des durchschnittlich verständigen Versicherungsnehmers zu orientieren (RIS-Justiz RS0050063).

**False Positives:**

- `Allgemeinen Versicherungsbedingungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_22`)


[6] Wie vom EuGH insbesondere in der Rechtssache Löber (C-304/17 [Rz 31]) ausgesprochen, müssen kurz gesagt „spezifischen Gegebenheiten [...] insgesamt zur Zuweisung der Zuständigkeit an die österreichischen Gerichte beitragen“, um die in Rede stehende internationale Zuständigkeit Österreichs zu begründen (iglS – zu einer Klage eines anderen Erwerbers von Norder Maschinenbau -Aktien gegen die auch hier beklagte Wirtschaftsprüferin – 2 Ob 154/21t [Rz 2]).

**False Positives:**

- `Norder Maschinenbau` — type mismatch — same span as gold: `Norder Maschinenbau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Norder Maschinenbau`(organisation)

</details>

---

## `Person after 'gegen' or 'von' (Contextual)`

**F1:** 0.001 | **Precision:** 0.013 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `3e083246`  
**Description:**
Captures names appearing after 'gegen' (against) or 'von' (of/from) in legal contexts, ensuring full name capture including 'von' prefixes and handling multi-word names.

**Content:**
```
(?:gegen\s+|von\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+(?:von|vertreten\s+durch))?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.013 | 0.001 | 0.001 | 79 | 1 | 78 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 78 | 1266 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_10`)


In dem vor dem Oberlandesgericht Köln geführten Pflegschaftsverfahren vereinbarten die Eltern am 8. Mai 2018 die Beibehaltung des gemeinsamen Obsorge- und Aufenthaltsbestimmungsrechts für beide Kinder, wobei der Lebensmittelpunkt von Heinrich Debbert beim Vater (der inzwischen ebenfalls nach Wien übersiedelt war) und für Ashley Frohnsdorfer eine wöchentlich abwechselnde Betreuung festgelegt wurde.

| Predicted | Gold |
|---|---|
| `Heinrich Debbert` | `Heinrich Debbert` |

**Missed by this rule (FN):**

- `Ashley Frohnsdorfer` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob30_19p`) (sent_id: `deanon_TRAIN/10Ob30_19p_54`)


Das Kind hätte in dieser besonderen Konstellation bereits in seinem Antrag auf Gewährung von Unterhaltsvorschüssen Tatsachen geltend machen müssen, die den Schluss auf die Anspannbarkeit des Unterhaltsschuldners zulassen, weil nach der Rückkehr der Mutter nach Rumänien das dem Titel zugrundegelegte Einkommen evidentermaßen nicht mehr erzielbar war (vgl 10 Ob 33/17a).

**False Positives:**

- `Unterhaltsvorschüssen Tatsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 2** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Szczech vertretenen Inn Triconal Holding GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Susanna Szczech` — partial — gold is substring of pred: `Szczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Szczech`(person)
- `Inn Triconal Holding GesmbH`(organisation)
- `Co KG`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 4** (doc_id: `deanon_TRAIN/11Os49_13k`) (sent_id: `deanon_TRAIN/11Os49_13k_3`)


Kopf Der Oberste Gerichtshof hat am 16. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Wancata als Schriftführer, in der Strafsache gegen Michael Dämering wegen des Verbrechens des schweren Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 4, 129 Z 1 StGB, AZ 13 Hv 23/13d des Landesgerichts Wels, über die von der Generalprokuratur gegen den gemäß § 494a StPO gefassten Beschluss dieses Gerichts vom 20. März 2012, ON 13 der Hv-Akten, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Michael Dämering` — partial — gold is substring of pred: `Dämering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dämering`(person)

**Example 5** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 6** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

**Example 7** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_3`)


Kopf Der Oberste Gerichtshof hat am 8. August 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Josef Klös und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1, Abs 3 StGB, AZ 72 Hv 8/17g des Landesgerichts Klagenfurt, über die Anzeige der Ausgeschlossenheit der Vizepräsidentin des Obersten Gerichtshofs Mag. Marek gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Josef Klös` — partial — gold is substring of pred: `Klös`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klös`(person)

**Example 8** (doc_id: `deanon_TRAIN/12Ns4_15g`) (sent_id: `deanon_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bachel wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Gerhard Bachel` — partial — gold is substring of pred: `Bachel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachel`(person)

**Example 9** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_3`)


Kopf Der Oberste Gerichtshof hat am 18. Oktober 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Bilinska als Schriftführerin in der Strafsache gegen Gerfried Hundgeburth und eine Angeklagte wegen des Verbrechens der betrügerischen Krida nach §§ 156 Abs 1, 161 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten Renata Holzhey gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 11. April 2011, GZ 602 Hv 4/10m-58, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gerfried Hundgeburth` — partial — gold is substring of pred: `Hundgeburth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hundgeburth`(person)
- `Holzhey`(person)

**Example 10** (doc_id: `deanon_TRAIN/12Os11_19p`) (sent_id: `deanon_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Margardt wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Thomas Margardt` — partial — gold is substring of pred: `Margardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Margardt`(person)

**Example 11** (doc_id: `deanon_TRAIN/12Os164_12b`) (sent_id: `deanon_TRAIN/12Os164_12b_3`)


Kopf Der Oberste Gerichtshof hat am 31. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Dr. Pausa als Schriftführerin in der Strafsache gegen Giorgi Standtke wegen des Verbrechens des gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 129 Z 1, 130 vierter Fall und 15 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien vom 17. Oktober 2012, GZ 95 Hv 92/12p-26, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Giorgi Standtke` — partial — gold is substring of pred: `Standtke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Standtke`(person)

**Example 12** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pitzenbauer wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Nenad Pitzenbauer` — partial — gold is substring of pred: `Pitzenbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pitzenbauer`(person)

**Example 13** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Mattheiß und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Tiepoldt auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Viktor Mattheiß` — partial — gold is substring of pred: `Mattheiß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mattheiß`(person)
- `Tiepoldt`(person)

**Example 14** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Viktor Mittermair` — partial — gold is substring of pred: `Mittermair`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 15** (doc_id: `deanon_TRAIN/12Os40_19b`) (sent_id: `deanon_TRAIN/12Os40_19b_3`)


Kopf Der Oberste Gerichtshof hat am 27. Februar 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden sowie durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Schriftführerin Maurer in der Strafsache gegen Alexander Jastrzemsky wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Jugendschöffengericht vom 8. Jänner 2019, GZ 23 Hv 29/18y-28, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alexander Jastrzemsky` — partial — gold is substring of pred: `Jastrzemsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jastrzemsky`(person)

**Example 16** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_3`)


Kopf Der Oberste Gerichtshof hat am 18. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Adamowitsch als Schriftführerin in der Strafsache gegen Norbert Noelker wegen Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB, AZ 16 Hv 32/15g des Landesgerichts Krems an der Donau, über die Beschwerde des Verurteilten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 7. März 2017, AZ 20 Bs 59/17y, nach Einsichtnahme durch die Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Norbert Noelker` — partial — gold is substring of pred: `Noelker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noelker`(person)

**Example 17** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__4`)


In der Strafsache gegen Christian Köbbel, AZ 12 U 86/07z des Bezirksgerichts Baden, verletzt die Abfassung des Protokolls- und Urteilsvermerks vom 25. Juli 2007 (ON 5) das Gesetz in § 32 Abs 2 JGG und in § 458 Abs 3 Z 1 StPO idF BGBl I 2004/164 iVm § 270 Abs 2 Z 2 StPO.

**False Positives:**

- `Christian Köbbel` — partial — gold is substring of pred: `Köbbel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Köbbel`(person)

**Example 18** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__14`)


Am 3. Mai 2010 brachte die Staatsanwaltschaft Wiener Neustadt beim Bezirksgericht Baden erneut einen Strafantrag gegen Christian Kowalzyk wegen des Verdachts der (während der Probezeit begangenen) Vergehen des unbefugten Gebrauchs von Fahrzeugen nach § 136 Abs 1 StGB sowie der Urkundenunterdrückung nach § 229 Abs 1 StGB ein und beantragte zugleich die „Straffestsetzung zu AZ 12 U 86/07z des Bezirksgerichtes Baden“ (ON 3 im Akt AZ 12 U 105/10y).

**False Positives:**

- `Christian Kowalzyk` — partial — gold is substring of pred: `Kowalzyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Baden`(organisation)
- `Kowalzyk`(person)

**Example 19** (doc_id: `deanon_TRAIN/12Os80_15d`) (sent_id: `deanon_TRAIN/12Os80_15d_3`)


Kopf Der Oberste Gerichtshof hat am 28. Jänner 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Jukic als Schriftführerin in der Strafsache gegen Arben Dietlof wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 17. April 2015, GZ 39 Hv 127/14v-47, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Arben Dietlof` — partial — gold is substring of pred: `Dietlof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dietlof`(person)

**Example 20** (doc_id: `deanon_TRAIN/13Os100_16d`) (sent_id: `deanon_TRAIN/13Os100_16d_3`)


Kopf Der Oberste Gerichtshof hat am 12. Oktober 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Krenn als Schriftführerin in der Strafsache gegen Richard Berzine und einen anderen Angeklagten wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Clemens Feidel sowie die Berufungen des Angeklagten Richard Boudewijn und der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 30. Mai 2016, GZ 61 Hv 45/16w-98, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Richard Berzine` — partial — gold is substring of pred: `Berzine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Berzine`(person)
- `Feidel`(person)
- `Boudewijn`(person)

**Example 21** (doc_id: `deanon_TRAIN/13Os100_16d`) (sent_id: `deanon_TRAIN/13Os100_16d_7`)


Danach hat er in Untertweng-Eichenweg 7, 9071 Plöschenberg, Österreich (1) am 11. Jänner 2016 mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz (US 8) zur Ausführung eines von Richard Bradley unter Verwendung einer Waffe begangenen Raubes beigetragen (§ 12 dritter Fall StGB), indem er den unmittelbaren Täter zum und vom Tatort chauffierte, (2) am 21. Jänner 2016 mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz (US 9) zu einem von Richard Birkenberg unter Verwendung einer Waffe begangenen Raub beigetragen (§ 12 dritter Fall StGB), indem er den unmittelbaren Täter zum Tatort chauffierte, dort Aufpasserdienste leistete, dem unmittelbaren Täter telefonisch einen günstigen Ausführungszeitpunkt nannte und das Fluchtfahrzeug vom Tatort lenkte, (3) vom 22. Jänner 2016 bis zum 3. Februar 2016, wenn auch nur fahrlässig, eine Gaspistole samt Munition besessen, obwohl ihm dies gemäß § 12 WaffG verboten war, und (4) bis zum 3. Februar 2016, wenn auch nur fahrlässig, eine gemäß § 17 Abs 1 Z 6 WaffG verbotene Waffe, nämlich einen Teleskopschlagstock, unbefugt besessen.

**False Positives:**

- `Richard Bradley` — partial — gold is substring of pred: `Bradley`
- `Richard Birkenberg` — partial — gold is substring of pred: `Birkenberg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Untertweng-Eichenweg 7, 9071 Plöschenberg, Österreich`(address)
- `Bradley`(person)
- `Birkenberg`(person)

**Example 22** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Abdullah Klingfuss wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. Juli 2019, GZ 41 Hv 18/18i-55, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Abdullah Klingfuss` — partial — gold is substring of pred: `Klingfuss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingfuss`(person)

**Example 23** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_7`)


Danach hat er in Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich und an anderen Orten 1) am 15. Februar 2014 Asli Davidsmeyer mit Gewalt zur Duldung des Analverkehrs genötigt, indem er sie auf ein Bett stieß, im Nacken festhielt und gegen ihren Willen seinen Penis in ihren After einführte, 2) durch im Urteil bezeichnete Handlungen und Äußerungen längere Zeit hindurch gegen andere Personen fortgesetzt Gewalt ausgeübt, und zwar a) ab dem 1. Juni 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014 gegen Asli Dagtekin, b) ab dem Jahr 2012 bis zum 19. November 2014, also länger als ein Jahr, gegen seine am 25. April 2008 geborene, somit unmündige, Tochter Berfin Krempl, sowie c) ab dem Jahr 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014, also länger als ein Jahr, gegen seinen am 18. Juni 2003 geborenen, somit unmündigen, Sohn Ilhan Kukolies, 3) Asli Dücking durch im Urteil bezeichnete Handlungen vorsätzlich am Körper verletzt, und zwar a) im September 2008, wodurch die Genannte Schwellungen und Hämatome erlitt, und b) zwischen September und November 2008, wodurch die Genannte das Bewusstsein verlor und eine Schwellung am Hinterkopf und Rötungen im Kniebereich erlitt, weiters Asli Dietzler durch im Urteil bezeichnete Äußerungen 4) zwischen September und November 2008 zu einer Unterlassung genötigt und 5) am 9. Februar 2017 zumindest mit einer Verletzung am Körper gefährlich bedroht, um sie in Furcht und Unruhe zu versetzen.

**False Positives:**

- `Asli Dagtekin` — partial — gold is substring of pred: `Dagtekin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich`(address)
- `Davidsmeyer`(person)
- `Dagtekin`(person)
- `Krempl`(person)
- `Kukolies`(person)
- `Dücking`(person)
- `Dietzler`(person)

**Example 24** (doc_id: `deanon_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Stelzl wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

**False Positives:**

- `Zoltan Stelzl` — partial — gold is substring of pred: `Stelzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stelzl`(person)

**Example 25** (doc_id: `deanon_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Mitzkait wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag.

**False Positives:**

- `Nikola Mitzkait` — partial — gold is substring of pred: `Mitzkait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mitzkait`(person)

**Example 26** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__3`)


Kopf Der Oberste Gerichtshof hat am 22. November 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Krausam als Schriftführerin in der Strafsache gegen Jasmin Fejfar wegen Vergehen der Erschleichung einer Leistung nach § 149 Abs 1 StGB, AZ 36 Hv 160/11y des Landesgerichts Innsbruck, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 10. Jänner 2012 (ON 49) und andere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Jasmin Fejfar` — partial — gold is substring of pred: `Fejfar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fejfar`(person)

**Example 27** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Lässig und Dr. Oberressl in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mario Speer und andere Angeklagte wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 3, 148 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 12 Hv 110/16x des Landesgerichts Wels, über die Grundrechtsbeschwerde des genannten Angeklagten gegen die Verfügung des Vorsitzenden vom 15. November 2016 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mario Speer` — partial — gold is substring of pred: `Speer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Speer`(person)

**Example 28** (doc_id: `deanon_TRAIN/13Os22_20i`) (sent_id: `deanon_TRAIN/13Os22_20i_3`)


Kopf Der Oberste Gerichtshof hat am 27. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in der Strafsache gegen Erwin Waegert wegen des Verbrechens des Mordes nach §§ 15, 75 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Geschworenengericht vom 19. Dezember 2019, GZ 19 Hv 72/19m-46, nach Anhörung der Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung werden zurückgewiesen.

**False Positives:**

- `Erwin Waegert` — partial — gold is substring of pred: `Waegert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waegert`(person)

**Example 29** (doc_id: `deanon_TRAIN/13Os23_15d`) (sent_id: `deanon_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wissink wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Karl Wissink` — partial — gold is substring of pred: `Wissink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wissink`(person)

**Example 30** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Junghuber wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Erik Junghuber` — partial — gold is substring of pred: `Junghuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Junghuber`(person)

**Example 31** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jerzenbek, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

**False Positives:**

- `Erik Jerzenbek` — partial — gold is substring of pred: `Jerzenbek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jerzenbek`(person)

**Example 32** (doc_id: `deanon_TRAIN/13Os34_19b`) (sent_id: `deanon_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weigenannt wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Wolfgang Weigenannt` — partial — gold is substring of pred: `Weigenannt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weigenannt`(person)

**Example 33** (doc_id: `deanon_TRAIN/13Os37_12h`) (sent_id: `deanon_TRAIN/13Os37_12h_3`)


Kopf Der Oberste Gerichtshof hat am 10. Mai 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Wohlmuth als Schriftführerin in der Strafsache gegen Michael Liebhold und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Waßmann und des DI Georg Lu Babette Prusak gegen den Beschluss des Oberlandesgerichts Innsbruck vom 20. März 2012, AZ 6 Bs 130/12m, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Liebhold` — partial — gold is substring of pred: `Liebhold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Liebhold`(person)
- `Waßmann`(person)
- `Babette Prusak`(person)

**Example 34** (doc_id: `deanon_TRAIN/13Os68_18a`) (sent_id: `deanon_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Coolhaas wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Mihai Coolhaas` — partial — gold is substring of pred: `Coolhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Coolhaas`(person)

**Example 35** (doc_id: `deanon_TRAIN/13Os6_14b`) (sent_id: `deanon_TRAIN/13Os6_14b_3`)


Kopf Der Oberste Gerichtshof hat am 14. März 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Gansterer als Schriftführerin in der Strafsache gegen Valentino Thünissen wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 9. Dezember 2013, GZ 52 Hv 65/13b-21, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Valentino Thünissen` — partial — gold is substring of pred: `Thünissen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thünissen`(person)

**Example 36** (doc_id: `deanon_TRAIN/13Os78_12p`) (sent_id: `deanon_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Längefeld und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wissing und des DI Georg Lu Jeannine Flemmig gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Längefeld` — partial — gold is substring of pred: `Längefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Längefeld`(person)
- `Wissing`(person)
- `Jeannine Flemmig`(person)

**Example 37** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Urbansky wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Robert Urbansky` — partial — gold is substring of pred: `Urbansky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Urbansky`(person)

**Example 38** (doc_id: `deanon_TRAIN/13Os8_11t`) (sent_id: `deanon_TRAIN/13Os8_11t_3`)


Kopf Der Oberste Gerichtshof hat am 17. Februar 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Kirnbauer als Schriftführerin in der Strafsache gegen Delroy Dambrowsky wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 16. November 2010, GZ 031 Hv 125/10t-58, sowie die Beschwerde des Angeklagten gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Delroy Dambrowsky` — partial — gold is substring of pred: `Dambrowsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dambrowsky`(person)

**Example 39** (doc_id: `deanon_TRAIN/13Os97_11f`) (sent_id: `deanon_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Gehler wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

**False Positives:**

- `Ernst Gehler` — partial — gold is substring of pred: `Gehler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gehler`(person)

**Example 40** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Hermanni wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

**False Positives:**

- `Christoph Hermanni` — partial — gold is substring of pred: `Hermanni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermanni`(person)

**Example 41** (doc_id: `deanon_TRAIN/14Os108_18s`) (sent_id: `deanon_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Reichenbach und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kulaksiz gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Misha Reichenbach` — partial — gold is substring of pred: `Reichenbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reichenbach`(person)
- `Kulaksiz`(person)

**Example 42** (doc_id: `deanon_TRAIN/14Os113_12t`) (sent_id: `deanon_TRAIN/14Os113_12t_3`)


Kopf Der Oberste Gerichtshof hat am 18. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen Astrit Börgers wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Geschworenengericht vom 23. August 2012, GZ 24 Hv 38/12m-61, sowie über dessen Beschwerde gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf bedingter Strafnachsichten und einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Astrit Börgers` — partial — gold is substring of pred: `Börgers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Börgers`(person)

**Example 43** (doc_id: `deanon_TRAIN/14Os121_19d`) (sent_id: `deanon_TRAIN/14Os121_19d_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Emir Kles wegen Verbrechen der schweren Körperverletzung nach §§ 15, 84 Abs 4 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 22. August 2019, GZ 52 Hv 23/19b-16, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Emir Kles` — partial — gold is substring of pred: `Kles`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kles`(person)

**Example 44** (doc_id: `deanon_TRAIN/14Os132_10h`) (sent_id: `deanon_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahner wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Tomislav Ahner` — partial — gold is substring of pred: `Ahner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ahner`(person)

**Example 45** (doc_id: `deanon_TRAIN/14Os136_19k`) (sent_id: `deanon_TRAIN/14Os136_19k_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Dimitri Thomassin wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 vierter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 30. September 2019, GZ 632 Hv 2/19a-138, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dimitri Thomassin` — partial — gold is substring of pred: `Thomassin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomassin`(person)

**Example 46** (doc_id: `deanon_TRAIN/14Os16_15g`) (sent_id: `deanon_TRAIN/14Os16_15g_3`)


Kopf Der Oberste Gerichtshof hat am 28. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Moelle als Schriftführerin in der Strafsache gegen Alessandro Braunmiller wegen des Verbrechens nach § 3g VerbotsG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Klagenfurt als Geschworenengericht vom 26. November 2014, GZ 38 Hv 50/14d-36, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alessandro Braunmiller` — partial — gold is substring of pred: `Braunmiller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Braunmiller`(person)

**Example 47** (doc_id: `deanon_TRAIN/14Os63_12i`) (sent_id: `deanon_TRAIN/14Os63_12i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart des Richteramtsanwärters Mag. Lindenbauer als Schriftführer in der Strafsache gegen Johann Haugk wegen des Verbrechens des Suchtgifthandels nach §§ 12 dritter Fall, 15 StGB, 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 29. Februar 2012, GZ 35 Hv 150/11z-93, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Johann Haugk` — partial — gold is substring of pred: `Haugk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Haugk`(person)

**Example 48** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_3`)


Kopf Der Oberste Gerichtshof hat am 5. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Draginja Nielson und einen Angeklagten wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 30. März 2017, GZ 26 Hv 117/16h-55, sowie ihre Beschwerde gegen den zugleich gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Draginja Nielson` — partial — gold is substring of pred: `Nielson`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nielson`(person)

**Example 49** (doc_id: `deanon_TRAIN/14Os71_17y`) (sent_id: `deanon_TRAIN/14Os71_17y_3`)


Kopf Der Oberste Gerichtshof hat am 3. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Adam Albanesi wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Geschworenengericht vom 5. Mai 2017, GZ 35 Hv 15/17a-83, sowie über die Beschwerde des Angeklagten gegen den Beschluss auf Widerruf einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Adam Albanesi` — partial — gold is substring of pred: `Albanesi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albanesi`(person)

**Example 50** (doc_id: `deanon_TRAIN/15Ns104_16m`) (sent_id: `deanon_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Höferth wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Markus Höferth` — partial — gold is substring of pred: `Höferth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Höferth`(person)

**Example 51** (doc_id: `deanon_TRAIN/15Os110_17s`) (sent_id: `deanon_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Valerius Niesse, MA und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Laila Niezoldi gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Shafiqullah Valerius Niesse` — positional overlap with gold: `Valerius Niesse, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerius Niesse, MA`(person)
- `Laila Niezoldi`(person)

**Example 52** (doc_id: `deanon_TRAIN/15Os114_10v`) (sent_id: `deanon_TRAIN/15Os114_10v_3`)


Kopf Der Oberste Gerichtshof hat am 15. September 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger als weitere Richter, in Gegenwart der Rechtspraktikantin Mag. Reich als Schriftführerin, in der Strafsache gegen Marek Dirksmeyer wegen des Verbrechens des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. April 2010, GZ 40 Hv 1/10w-32, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung des Angeklagten „wegen Schuld“ werden zurückgewiesen.

**False Positives:**

- `Marek Dirksmeyer` — partial — gold is substring of pred: `Dirksmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dirksmeyer`(person)

**Example 53** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_3`)


Kopf Der Oberste Gerichtshof hat am 19. Februar 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Ent als Schriftführer in der Strafsache gegen Christian Poethke und einen anderen Angeklagten wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer anderen strafbaren Handlung, (zuletzt) AZ 33 Hv 70/12x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Rakhart Jörg Andrich auf Erneuerung des Strafverfahrens gemäß § 363a Abs 1 StPO nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Christian Poethke` — partial — gold is substring of pred: `Poethke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poethke`(person)
- `Jörg Andrich`(person)

**Example 54** (doc_id: `deanon_TRAIN/15Os178_15p`) (sent_id: `deanon_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Korsmeier gegen Martin Rühmekorb wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klingspohr vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

**False Positives:**

- `Martin Rühmekorb` — partial — gold is substring of pred: `Rühmekorb`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Korsmeier`(person)
- `Rühmekorb`(person)
- `Klingspohr`(person)

**Example 55** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Bahar wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Manfred Bahar` — partial — gold is substring of pred: `Bahar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bahar`(person)

**Example 56** (doc_id: `deanon_TRAIN/15Os53_16g`) (sent_id: `deanon_TRAIN/15Os53_16g_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Janisch als Schriftführerin in der Strafsache gegen Eduard Meisslein wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 erster Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 21. Dezember 2015, GZ 181 Hv 4/15x-46, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Eduard Meisslein` — partial — gold is substring of pred: `Meisslein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Meisslein`(person)

**Example 57** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Rauhe und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Johann Rauhe` — partial — gold is substring of pred: `Rauhe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rauhe`(person)

**Example 58** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_8`)


Text Gründe: Die Staatsanwaltschaft Wels führt zu AZ 17 St 77/19g ein Ermittlungsverfahren gegen Johann Remppel wegen des Verdachts des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG und weiterer strafbarer Handlungen.

**False Positives:**

- `Johann Remppel` — partial — gold is substring of pred: `Remppel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Remppel`(person)

**Example 59** (doc_id: `deanon_TRAIN/15Os72_12w`) (sent_id: `deanon_TRAIN/15Os72_12w_4`)


Karlicek als Schriftführerin in der Strafsache gegen Rudolf Czaya wegen Verbrechen der Vergewaltigung nach §§ 201 Abs 1, 15 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 23. März 2012, GZ 631 Hv 2/12h-28, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Rudolf Czaya` — partial — gold is substring of pred: `Czaya`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Czaya`(person)

**Example 60** (doc_id: `deanon_TRAIN/15Os96_17g`) (sent_id: `deanon_TRAIN/15Os96_17g_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Roman Abbold wegen des Verbrechens der terroristischen Vereinigung nach § 278b Abs 2 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 16. Mai 2017, GZ 39 Hv 6/17h-37, sowie über dessen Beschwerde gegen den Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Roman Abbold` — partial — gold is substring of pred: `Abbold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Abbold`(person)

**Example 61** (doc_id: `deanon_TRAIN/15Os96_17g`) (sent_id: `deanon_TRAIN/15Os96_17g_22`)


Nach dieser Schießübung wurde der Angeklagte von Umar Mergele besucht, welcher ihm erklärte, der Angeklagte werde bald zu ihm kommen, womit er meinte, dass dann dessen Ausbildung vorbei wäre.

**False Positives:**

- `Umar Mergele` — partial — gold is substring of pred: `Mergele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mergele`(person)

**Example 62** (doc_id: `deanon_TRAIN/15Os98_15y`) (sent_id: `deanon_TRAIN/15Os98_15y_3`)


Kopf Der Oberste Gerichtshof hat am 26. August 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Leisser als Schriftführerin in der Strafsache gegen Gottlieb Zekalla wegen des Verbrechens des Diebstahls durch Einbruch nach §§ 127, 129 Z 1 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 19. Mai 2015, GZ 39 Hv 105/13k-91, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur Dr. Ulrich, des Angeklagten und seines Verteidigers Dr. Pohle zu Recht erkannt:  Spruch

**False Positives:**

- `Gottlieb Zekalla` — partial — gold is substring of pred: `Zekalla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zekalla`(person)

**Example 63** (doc_id: `deanon_TRAIN/15Os9_12f`) (sent_id: `deanon_TRAIN/15Os9_12f_4`)


Linzner als Schriftführerin in der Strafsache gegen Georg Henckens wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

**False Positives:**

- `Georg Henckens` — partial — gold is substring of pred: `Henckens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Henckens`(person)

**Example 64** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Juni 2018 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Gerhard Obeser und eine Angeklagte wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und weiterer strafbarer Handlungen aus Anlass der Nichtigkeitsbeschwerde der Angeklagten Mag. (FH) Nicole Kochem gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 31. Oktober 2017, GZ 78 Hv 76/17a-76,nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Stani, des Angeklagten Gerhard Oravec und seines Verteidigers Dr. Gärtner zu Recht erkannt:  Spruch

**False Positives:**

- `Gerhard Obeser` — partial — gold is substring of pred: `Obeser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obeser`(person)
- `Kochem`(person)
- `Oravec`(person)

**Example 65** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_4`)


Das Urteil, das im Übrigen unberührt bleibt, wird im Schuldspruch A, demgemäß auch im Gerhard Oeste betreffenden Strafausspruch, aufgehoben und in diesem Umfang in der Sache selbst erkannt: Gerhard Opderbecke wird gemäß § 259 Z 3 StPO vom Vorwurf freigesprochen, er habe in Aichbach 59, 9131 Zapfendorf, Österreich A/ als Bürgermeister der Gemeinde Krautz, mithin als Beamter im strafrechtlichen Sinn, „mit dem Vorsatz, die Gemeinderäte der Gemeinde Kießlich an ihren Rechten gemäß §§ 28 Abs 1 und 2, 35 Abs 1, 78 Abs 1a K-AGO auf Einberufung des Gemeinderates und Behandlung von Erledigungen, die der Beschlussfassung durch den Gemeinderat vorbehalten waren, zu schädigen“, wiederholt seine Befugnis, im Namen der Gemeinde Klingenschmid als deren Organ in Vollziehung der Gesetze Amtsgeschäfte vorzunehmen, wissentlich missbraucht, indem er es unterließ, „Sitzungen des Gemeinderates zur Beschlussfassung über nachangeführte Geschäftsgänge und über die Adaptierung der Nebengebührenverordnung der Gemeinde einzuberufen, darüber einen Tagesordnungspunkt in einer Gemeinderatssitzung anzusetzen und hierfür Sitzungsvorträge nach § 78 K-AGO ausarbeiten zu lassen und indem er die entsprechenden Punkte mehrfach von der Tagesordnung der Gemeinderatssitzungen strich“, und zwar I/ zwischen 1. Juli 2010 und März 2015 über die Bestellung von Renate Dal zur Amtsleiterstellvertreterin und über die Gewährung einer monatlichen Mehrleistungszulage und Aufwandsent-schädigung für diese Funktion, „wodurch der Gemeinde Khatib ein Schaden im Gesamtbetrag von zumindest insgesamt 25.302,76 Euro inklusive Dienstgeberabgaben entstand“;

**False Positives:**

- `Renate Dal` — partial — gold is substring of pred: `Dal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oeste`(person)
- `Opderbecke`(person)
- `Aichbach 59, 9131 Zapfendorf, Österreich`(address)
- `Krautz`(person)
- `Kießlich`(person)
- `Klingenschmid`(person)
- `Dal`(person)
- `Khatib`(person)

**Example 66** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_118`)


Haben gemeinsame Kinder das Haus mit der Mutter bewohnt und hat diese die Kinder überwiegend betreut, wird (jedenfalls im Verhältnis zu den Kindern) in der Zurverfügungstellung von Wohnraum Naturalunterhalt liegen.

**False Positives:**

- `Wohnraum Naturalunterhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Roman Janis` — partial — gold is substring of pred: `Janis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Landesgericht Linz`(organisation)
- `Bezirksgericht Amstetten`(organisation)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 68** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_28`)


Dem stehe die Gewährleistung für die Lastenfreiheit und Freiheit von Nutzungsrechten Dritter nicht entgegen, weil damit die Löschung der Pfandrechte angesprochen worden sei und weil die Erwerber von der Überlassung einer Wohnung an die Klägerin durch ihre frühere Dienstgeberin gewusst hätten.

**False Positives:**

- `Nutzungsrechten Dritter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_69`)


Er konnte daher die Zusicherung der Verkäuferinnen, die Liegenschaft sei frei von Nutzungsrechten Dritter, nur so verstehen, dass damit andere Nutzungsrechte als jenes der Klägerin gemeint waren.

**False Positives:**

- `Nutzungsrechten Dritter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_165`)


[41]4.2.Dem für gemeinnützige Bauvereinigungen zuständigen Revisionsverband kommt überdies im Firmenbuchverfahren von Gesellschaften Parteistellung nach § 14 Abs 3 FBG soweit zu, als es Firmenbucheintragungen von Gesellschaftern dieser Gesellschaften betrifft, wenn der wirksame Erwerb der Gesellschafterstellung von der Zustimmung der Landesregierung nach § 10a Abs 1a WGG abhängig ist.

**False Positives:**

- `Gesellschaften Parteistellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/7Ob150_17k`) (sent_id: `deanon_TRAIN/7Ob150_17k_32`)


2.Der Oberste Gerichtshof ist zur Auslegung von Allgemeinen Versicherungsbedingungen (AVB) nicht „jedenfalls“, sondern nur dann berufen, wenn das Berufungsgericht höchstgerichtliche Rechtsprechung missachtet hat oder für die Rechtseinheit oder Rechtsentwicklung bedeutsame Fragen zu lösen sind (RIS-Justiz RS0121516).

**False Positives:**

- `Allgemeinen Versicherungsbedingungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/7Ob79_10h`) (sent_id: `deanon_TRAIN/7Ob79_10h_8`)


Der Revisionswerber wendet dagegen ein, es sei anzunehmen, dass die Klausel in einer Vielzahl von Versicherungsverträgen Verwendung finde.

**False Positives:**

- `Versicherungsverträgen Verwendung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/7Ob79_10h`) (sent_id: `deanon_TRAIN/7Ob79_10h_10`)


Damit vermag der Kläger einen tauglichen Grund für die Zulassung seines außerordentlichen Rechtsmittels nicht aufzuzeigen:  Rechtliche Beurteilung Die Auslegung von Allgemeinen Versicherungsbedingungen hat sich am Maßstab des durchschnittlich verständigen Versicherungsnehmers zu orientieren (RIS-Justiz RS0050063).

**False Positives:**

- `Allgemeinen Versicherungsbedingungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_197`)


Schon allein aufgrund der Zielsetzung ihrer handelnden Organe, mit der in Aussicht genommenen Art von Geschäften Spekulationsgewinne zu erzielen, hätte die Beklagte selbst das Erfordernis einer ministeriellen Genehmigung nach § 446 Abs 3 ASVG erkennen müssen.

**False Positives:**

- `Geschäften Spekulationsgewinne` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_22`)


[6] Wie vom EuGH insbesondere in der Rechtssache Löber (C-304/17 [Rz 31]) ausgesprochen, müssen kurz gesagt „spezifischen Gegebenheiten [...] insgesamt zur Zuweisung der Zuständigkeit an die österreichischen Gerichte beitragen“, um die in Rede stehende internationale Zuständigkeit Österreichs zu begründen (iglS – zu einer Klage eines anderen Erwerbers von Norder Maschinenbau -Aktien gegen die auch hier beklagte Wirtschaftsprüferin – 2 Ob 154/21t [Rz 2]).

**False Positives:**

- `Norder Maschinenbau` — type mismatch — same span as gold: `Norder Maschinenbau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Norder Maschinenbau`(organisation)

**Example 76** (doc_id: `deanon_TRAIN/8Ob41_17p`) (sent_id: `deanon_TRAIN/8Ob41_17p_64`)


Daraus folgt, dass eine dem Gläubiger vorwerfbare eigene Nachlässigkeit im Sinn des § 1356 ABGB nicht in der Unterlassung von Eintreibungsmaßnahmennachder Verwirklichung eines der in Rede stehenden Ausnahmetatbestände liegen kann (2 Ob 78/11a).

**False Positives:**

- `Eintreibungsmaßnahmennachder Verwirklichung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Person after 'vertreten durch' (Refined)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1fcb9e35`  
**Description:**
Captures names of legal representatives following 'vertreten durch', strictly excluding law firm names and ensuring the match ends before company suffixes or 'Rechtsanwalt'.

**Content:**
```
vertreten\s+durch\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+Rechtsanwalt|\s+Rechtsanwältin|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|\s+Stadtgemeinde|\s+Gemeinde|\s+Verein|\s+Gesellschaft|\s+Unternehmen|\s+Firma|\s+Werk|\s+Bank|\s+Pharma|\s+Energie|\s+Versand|\s+Handel|\s+Technik|\s+Bau|\s+Immobilien|\s+Consulting|\s+Management|\s+Group|\s+Holdings|\s+Partners|\s+&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 84 | 0 | 84 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 84 | 1357 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Skribe Rechtsanwälte` — no gold match — likely missing annotation

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

- `Lederer Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kotschenreuther u. Abele Planung GmbH`(organisation)
- `Janis Krentzel`(person)
- `Mittel Keltal GmbH`(organisation)
- `Julian Grebener`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob28_17s`) (sent_id: `deanon_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Jaroslaw Mlynarik, geboren am 1. Juli 2009, wegen Kontaktrechts des Vaters Dr. Eckard Tschernig, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Bettina Makswietat, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Rechtsanwälte Pieler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jaroslaw Mlynarik`(person)
- `1. Juli 2009`(date)
- `Dr. Eckard Tschernig`(person)
- `Partner KG`(organisation)
- `Dr. Bettina Makswietat`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_5`)


Dr. Torsten Classe, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Jaqueline Ratzenböck, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `König Ermacora Klotz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Torsten Classe`(person)
- `Jaqueline Ratzenböck`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt` — no gold match — likely missing annotation
- `Wess Kux Kispert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 9** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt` — no gold match — likely missing annotation
- `Wess Kux Kispert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Techn R Heidrun Imai, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Techn R Heidrun Imai`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OberTratraSoftware Dienstleistungen AG`(organisation)
- `Prägrader Weg 43, 8616 Gasen, Österreich`(address)

**Example 12** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Stephan Briem Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Rechtsanwälte Estermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Luigi Neimeier`(person)
- `LNC KI Solutions GmbH`(organisation)
- `Kordelia Grauel`(person)

**Example 14** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Brandl Talos Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 15** (doc_id: `deanon_TRAIN/3Ob14_24s`) (sent_id: `deanon_TRAIN/3Ob14_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Daniela Sklenar SE, Kimberly Hurrelmeyer, vertreten durch Cerha Hempel Rechtsanwälte GmbH in Wien, gegen die verpflichtete Partei Staat Libyen, StR Violetta Stegemeyer, Libyen, vertreten durch Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 10 Mio EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Oktober 2023, GZ 47 R 228/23m-107, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Cerha Hempel Rechtsanwälte` — no gold match — likely missing annotation
- `Binder Grösswang Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Daniela Sklenar`(person)
- `Kimberly Hurrelmeyer`(person)
- `StR Violetta Stegemeyer`(person)

**Example 16** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Florentin Rosskämmer, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde ÖkR Priv.-Doz. Björn Gustloff, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ebner Aichinger Guggenberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Florentin Rosskämmer`(person)
- `ÖkR Priv.-Doz. Björn Gustloff`(person)

**Example 17** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei HR Dr.in RgR Johanna Drestomark, Italien, vertreten durch Oberhammer Rechtsanwälte GmbH in Wien, wider die verpflichtete Partei Prosten und Kreutzinger Bau gesellschaft mbH, Dr.Viktor-Kaplan-Straße 8, 4920 Weiketsedt, Österreich, vertreten durch Dr. Daniel Charim und Mag. Jakob Charim, Rechtsanwälte in Wien, wegen (restlich) 347.093,53 EUR sA über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Dezember 2016, GZ 46 R 323/16i-61, womit der Beschluss des Bezirksgerichts Josefstadt vom 24. Juni 2016, GZ 11 E 2966/11p-56, bestätigt wurde, den Beschluss gefasst:  Spruch I.Der Revisionsrekurs der verpflichteten Partei wird, soweit er die Bestätigung der Exekutionsbewilligung bekämpft, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Oberhammer Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Dr.in RgR Johanna Drestomark`(person)
- `Prosten und Kreutzinger Bau gesellschaft mbH`(organisation)
- `Dr.Viktor-Kaplan-Straße 8, 4920 Weiketsedt, Österreich`(address)

**Example 18** (doc_id: `deanon_TRAIN/4Ob100_13d`) (sent_id: `deanon_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Erwin Sieferer, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Lebensmittel Seeder -Aktiengesellschaft, Knechtswies 63, 4692 Niederau, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ StR Thobias Broß ” Viola Hüßkes, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Raits Bleiziffer Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erwin Sieferer`(person)
- `Lebensmittel Seeder`(organisation)
- `Knechtswies 63, 4692 Niederau, Österreich`(address)
- `StR Thobias Broß`(person)
- `Viola Hüßkes`(person)

**Example 19** (doc_id: `deanon_TRAIN/4Ob113_24g`) (sent_id: `deanon_TRAIN/4Ob113_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Vierziger u. Tewald Wind GmbH, Claire Lüdermann, Bakk. rer. nat., vertreten durch Grassner Rechtsanwalts GmbH in Linz, gegen die beklagte Partei Milena Buchmayr, vertreten durch Dr. Manfred Palkovits, Mag. Martin Sohm, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2024, GZ 38 R 247/23i-46, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Grassner Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vierziger u. Tewald Wind GmbH`(organisation)
- `Claire Lüdermann, Bakk. rer. nat.`(person)
- `Milena Buchmayr`(person)

**Example 20** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanwälte` — no gold match — likely missing annotation
- `Schönherr Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 21** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ebert Huber Swoboda Oswald` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 22** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Schönherr Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 23** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ruggenthaler Rechtsanwalts` — partial — pred is substring of gold: `Ruggenthaler Rechtsanwalts KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `JQV Finanzen Gruppe GmbH`(organisation)
- `Innovationsplatz 79, 9751 Nigglai, Österreich`(address)
- `Ruggenthaler Rechtsanwalts KG`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwälte Konrad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/4Ob201_10b`) (sent_id: `deanon_TRAIN/4Ob201_10b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Wendelin Wetekamp OEG, KzlR Ibrahim Kocaslan, vertreten durch Dr. Martin Leitner und Dr. Ralph Trischler, Rechtsanwälte in Wien, gegen die beklagte Partei Feddes KI GmbH, KommR Waldemar Holzhaider, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung, Rechnungslegung, Schadenersatz und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. September 2010, GZ 1 R 192/10b-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß Der Antrag auf Zuspruch der Kosten der Revisionsrekursbeantwortung wird gemäß § 508a Abs 2 Satz 2 und § 521a Abs 2 ZPO abgewiesen.

**False Positives:**

- `Bichler Zrzavy Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendelin Wetekamp`(person)
- `KzlR Ibrahim Kocaslan`(person)
- `Feddes KI GmbH`(organisation)
- `KommR Waldemar Holzhaider`(person)

**Example 26** (doc_id: `deanon_TRAIN/4Ob24_11z`) (sent_id: `deanon_TRAIN/4Ob24_11z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei DI Gundula Vielmäder, vertreten durch Proksch & Fritzsche Rechtsanwälte OG in Wien, gegen die beklagte Partei Dr. Theodor Huetter, vertreten durch Ploil Krepp & Partner Rechtsanwälte GmbH in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 24. November 2010, GZ 39 R 292/10w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Ploil Krepp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Gundula Vielmäder`(person)
- `Dr. Theodor Huetter`(person)

**Example 27** (doc_id: `deanon_TRAIN/4Ob69_14x`) (sent_id: `deanon_TRAIN/4Ob69_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Univ.-Prof. Dr. Anita Christöphler, vertreten durch Riesemann Rechtsanwalts GmbH in Graz, gegen die beklagte Partei Husein E‑Commerce GmbH, Dolores Linse, Deutschland, vertreten durch Dr. Peter Schlösser, Rechtsanwalt in Graz, wegen Unterlassung, Beseitigung, Urteilsveröffentlichung, Rechnungslegung und Zahlung (Streitwert im Sicherungsverfahren 50.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz vom 5. März 2014, GZ 5 R 20/14x-21, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Riesemann Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Anita Christöphler`(person)
- `Husein E‑Commerce GmbH`(organisation)
- `Dolores Linse`(person)

**Example 28** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


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

**Example 29** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_4`)


Matzka als weitere Richter in der Rechtssache der Klägerin Dr. Imre Grosse-Budde, vertreten durch Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die Beklagte IFS Telekom Technologien GmbH, Großtaxen 13, 6345 Kössen, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Wien, und die Nebenintervenienten auf Seiten der Beklagten 1.

**False Positives:**

- `Huber Swoboda Oswald Aixberger Rechtsanwälte` — no gold match — likely missing annotation
- `Wiedenbauer Mutz Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Imre Grosse-Budde`(person)
- `IFS Telekom Technologien GmbH`(organisation)
- `Großtaxen 13, 6345 Kössen, Österreich`(address)

**Example 30** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. KzlR MedR Brunhild Syndikus`(person)
- `Böhnstedt+Bittlmeier Verlag GmbH`(organisation)
- `Wien Traalmon Betriebe`(organisation)
- `TraunBau AG`(organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich`(address)

**Example 31** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Weishaupt Horak Georgiev Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)
- `Co KG`(organisation)

**Example 32** (doc_id: `deanon_TRAIN/5Ob93_24y`) (sent_id: `deanon_TRAIN/5Ob93_24y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH, Florenzia Lohmöller, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dipl.-Ing. Juliana Maurice, wegen Unterfertigung eines Wohnungseigentumsvertrags und Feststellung, hier: Anmerkung der Klage, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 26. April 2024, GZ 15 R 41/24w-18, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 126 Abs 1 GBG iVm § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Rechtsanwälte Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jozwiak Robotik GmbH`(organisation)
- `Florenzia Lohmöller`(person)
- `Dipl.-Ing. Juliana Maurice`(person)

**Example 33** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Musey Rechtsanwalt` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 34** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden und durch die Hofräte Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Ing. Melinda Jastrembski, vertreten durch Dr. Wolfgang Leitner, Priv.-Doz. Dr. Max Leitner, Dr. Mara-Sophie Häusler, Rechtsanwälte in Wien, gegen die beklagte Partei Heiko Radziwil, vertreten durch Lederer Rechtsanwalt GmbH in Wien, und der Nebenintervenienten auf Seite der beklagten Partei 1.

**False Positives:**

- `Lederer Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Melinda Jastrembski`(person)
- `Heiko Radziwil`(person)

**Example 35** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_4`)


SeeAlheimsudMedien Institut GmbH in Liquidation, LNMT Cloud, 2. WEA Robotik GmbH, Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich, Deutschland, beide vertreten durch Wess Kispert Rechtsanwalts GmbH in Wien, wegen 103.578,16 EUR sA und Feststellung, über die Rekurse der beklagten Partei und der Nebenintervenienten gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 13. April 2016, GZ 14 R 173/16m-39, womit das Urteil des Landesgerichts Eisenstadt vom 31. August 2015, GZ 3 Cg 166/13y-34, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Den Rekursen wird nicht Folge gegeben.

**False Positives:**

- `Wess Kispert Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `SeeAlheimsudMedien Institut GmbH`(organisation)
- `LNMT Cloud`(organisation)
- `WEA Robotik GmbH`(organisation)
- `Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich`(address)

**Example 36** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_5`)


Li Krautsch, alle vertreten durch Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. März 2019, GZ 11 R 28/19x-17, womit über Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. Dezember 2018, GZ 58 Cg 33/18a-13, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Saxinger Chalupsky` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Li Krautsch`(person)

**Example 37** (doc_id: `deanon_TRAIN/6Ob139_19p`) (sent_id: `deanon_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Priv.-Doz. Florian Thiesbonenkamp, LLM, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Maximiliane Cekal, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brauneis Klauser Prändl Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Florian Thiesbonenkamp, LLM`(person)
- `Co KG`(organisation)
- `Dr. Maximiliane Cekal`(person)

**Example 38** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_5`)


Nigel Frömmke, vertreten durch Dr. Josef Olischar und Dr. Johannes Olischar, Rechtsanwälte in Wien, gegen die Antragsgegnerin Republik Österreich, vertreten durch WienEvent GmbH, Oweges C 64, 4115 Apfelsbach, Österreich, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen Festsetzung einer Enteignungsentschädigung, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. Mai 2010, GZ 14 R 59/10i-54, womit der Beschluss des Landesgerichts Korneuburg vom 2. Februar 2010, GZ 26 Nc 3/08x-44, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Fellner Wratzfeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nigel Frömmke`(person)
- `WienEvent GmbH`(organisation)
- `Oweges C 64, 4115 Apfelsbach, Österreich`(address)

**Example 39** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `List Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

**Example 40** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des Minderjährigen HR Estelle de Clerck, geboren am 18. Juni 2007, 1. Juli 2016, vertreten durch das Land Wien (Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung Bezirk 22, 1220 Wien, Simone-de-Beauvoir-Platz 6) als Kinder- und Jugendhilfeträger, über den Revisionsrekurs des Vaters Mag. Liu Mertoglu, vertreten durch Anwaltssocietät Sattlegger Dorninger Steiner & Partner in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 25. Juni 2020, GZ 43 R 237/20a-31, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 21. April 2020, GZ 1 P 135/18y-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wirdzurückgewiesen.

**False Positives:**

- `Anwaltssocietät Sattlegger Dorninger Steiner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Estelle de Clerck`(person)
- `18. Juni`(date)
- `1. Juli 2016`(date)
- `Mag. Liu Mertoglu`(person)

**Example 41** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie durch die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Nepomuk Birkenmeier, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wider die beklagte Partei Dr. Flora Lyttwin, vertreten durch Dr. Thomas Weber, Rechtsanwalt in Baden, und den Nebenintervenienten auf Seiten der beklagten Partei Dr. Lukas Riemenschneider, vertreten durch Prettenhofer Raimann Pérez Rechtsanwaltspartnerschaft in Wien, wegen Löschung und Unterlassung, über die außerordentlichen Revisionen der beklagten Partei und des Nebenintervenienten gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 19. November 2019, GZ 58 R 58/19f-36, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dorda Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nepomuk Birkenmeier`(person)
- `Dr. Flora Lyttwin`(person)
- `Dr. Lukas Riemenschneider`(person)

**Example 42** (doc_id: `deanon_TRAIN/6Ob86_20w`) (sent_id: `deanon_TRAIN/6Ob86_20w_5`)


Juri Schlösiger, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Juri Schlösiger`(person)

**Example 43** (doc_id: `deanon_TRAIN/6Ob86_20w`) (sent_id: `deanon_TRAIN/6Ob86_20w_6`)


Solar Bruckstein GmbH, Scherrers Getränke, 2. SüdDerveruniMaschinenbau AG, Untere Hofäcker 14, 5771 Sinning, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 27.758,24 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 5. März 2020, GZ 1 R 4/20w-44, mit dem das Urteil des Landesgerichts St. Pölten vom 28. Oktober 2019, GZ 3 Cg 62/17m-40, bestätigt wurde, den Beschluss gefasst:  Spruch Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Solar Bruckstein GmbH`(organisation)
- `Scherrers Getränke`(organisation)
- `SüdDerveruniMaschinenbau AG`(organisation)
- `Untere Hofäcker 14, 5771 Sinning, Österreich`(address)

**Example 44** (doc_id: `deanon_TRAIN/7Ob113_14i`) (sent_id: `deanon_TRAIN/7Ob113_14i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei KzlR Evamaria Zemlitschka Versicherungs-Aktiengesellschaft, Johann Hofbauer - Weg 21, 3242 Hinterberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Februar 2014, GZ 2 R 212/13f-14, mit dem das Urteil des Handelsgerichts Wien vom 2. Juli 2013, GZ 39 Cg 41/12s-8, teilweise bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Schönherr Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KzlR Evamaria Zemlitschka`(person)
- `Johann Hofbauer - Weg 21, 3242 Hinterberg, Österreich`(address)

**Example 45** (doc_id: `deanon_TRAIN/7Ob201_12b`) (sent_id: `deanon_TRAIN/7Ob201_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, 1041 Wien, Prinz-Eugen-Straße 20-22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei DrauGastronomie AG, Fridolin Podszius, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2011, GZ 2 R 203/11d-11, womit das Urteil des Handelsgerichts Wien vom 26. Juni 2011, GZ 19 Cg 49/11v-5, teilweise abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Schönherr Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DrauGastronomie AG`(organisation)
- `Fridolin Podszius`(person)

**Example 46** (doc_id: `deanon_TRAIN/7Ob205_19a`) (sent_id: `deanon_TRAIN/7Ob205_19a_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Florentin Herboldt, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Wolenk und Ukininks Planung -Aktiengesellschaft, Mayr-Melnhof-Weg 66, 9842 Auen, Österreich, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 11. September 2019, GZ 22 R 243/19t-11, womit das Urteil des Bezirksgerichts Salzburg vom 29. Mai 2019, GZ 16 C 627/18p-7, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Florentin Herboldt`(person)
- `Wolenk und Ukininks Planung`(organisation)
- `Mayr-Melnhof-Weg 66, 9842 Auen, Österreich`(address)

**Example 47** (doc_id: `deanon_TRAIN/7Ob254_18f`) (sent_id: `deanon_TRAIN/7Ob254_18f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Svenja Nareyek, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Ost-Pflege AG, Lorena Blanknagel, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2018, GZ 50 R 131/17x-10, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2017, GZ 18 C 304/17p-6, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Svenja Nareyek`(person)
- `Ost-Pflege AG`(organisation)
- `Lorena Blanknagel`(person)

**Example 48** (doc_id: `deanon_TRAIN/7Ob48_17k`) (sent_id: `deanon_TRAIN/7Ob48_17k_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Vertra-Elektro GmbH, Camilla Niemetschek, vertreten durch Aigner Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Schmerschneider Transport AG, René Weisspfenning, vertreten durch Dr. Josef Milchram, Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen 1.373.171,48 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 20. Jänner 2017, GZ 1 R 160/16d-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Aigner Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vertra-Elektro GmbH`(organisation)
- `Camilla Niemetschek`(person)
- `Schmerschneider Transport AG`(organisation)
- `René Weisspfenning`(person)

**Example 49** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_5`)


Schefuss Forschung GmbH, beide Raidenstraße 62, 8354 Aigen, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dorda Brugger Jordis Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schefuss Forschung GmbH`(organisation)
- `Raidenstraße 62, 8354 Aigen, Österreich`(address)

**Example 50** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

**False Positives:**

- `Plankel Mayrhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Salzburg`(organisation)
- `Buth Analyse GmbH`(organisation)
- `Anabel Traudtmann`(person)
- `Christine Schwemmer`(person)

**Example 51** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


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

**Example 52** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Czernich Hofstädter Guggenberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

**Example 53** (doc_id: `deanon_TRAIN/8Ob29_19a`) (sent_id: `deanon_TRAIN/8Ob29_19a_5`)


Wald Lemwald - Lemlogber Metall GmbH, Argenotstraße 81, 4871 Tiefenbach, Österreich, vertreten durch Dr. Wilfried Plattner, Rechtsanwalt in Innsbruck, 4. Bachconval-Automotive GmbH in Liqu., Förolach 3, 4952 Appersting, Österreich, vertreten durch Mag. Martin Corazza, Rechtsanwalt in Innsbruck, 5. Waltemathe KI GmbH & Co OG, Springsfield 4, 9112 Untergreutschach, Österreich, vertreten durch Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien und Prader, Ortner, Fuchs, Wenzel Rechtsanwälte GesbR in Innsbruck, wegen Hinterlegung nach § 1425 ABGB, über den außerordentlichen Revisionsrekurs der Fünfterlagsgegnerin gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 2. Oktober 2018, GZ 52 R 50/18m-30, den Beschluss gefasst:  Spruch I. Die Bezeichnung der Fünfterlagsgegnerin wird berichtigt auf: „ Lexder-Finanzen GmbH & Co OG“.

**False Positives:**

- `Wolf Theiss Rechtsanwälte` — no gold match — likely missing annotation

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

**Example 54** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Co KG`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 55** (doc_id: `deanon_TRAIN/8Ob7_10b`) (sent_id: `deanon_TRAIN/8Ob7_10b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, durch den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei DI Dr. Valerie Haesevoets, vertreten durch Kaan Cronenberg & Partner, Rechtsanwälte in Graz, gegen die beklagten Parteien 1. Ashley Völkmer, 2. Marlene Fritzer und 3. Karsten Dalkiran, alle vertreten durch Dr. Thomas Stampfer, Dr. Christoph Orgler, Rechtsanwälte in Graz, wegen 49.620 EUR sA und Feststellung (Streitwert 15.000 EUR), über die Revision der beklagten Parteien (Revisionsinteresse: 49.620 EUR) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 19. November 2009, GZ 4 R 142/09y-38, womit über Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 19. Juni 2009, GZ 39 Cg 102/08m-32 teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Kaan Cronenberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Valerie Haesevoets`(person)
- `Ashley Völkmer`(person)
- `Marlene Fritzer`(person)
- `Karsten Dalkiran`(person)

**Example 56** (doc_id: `deanon_TRAIN/8Ob97_16x`) (sent_id: `deanon_TRAIN/8Ob97_16x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn sowie die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei VetR Dr.in Zarin Österhellweg, vertreten durch Wiedenbauer Mutz Winkler Pramberger Rechtsanwälte GmbH in Klagenfurt, gegen die beklagte Partei APEA Solar Systeme Aktiengesellschaft, Vorderer Sonnberg 7, 2752 Wöllersdorf, Österreich, vertreten durch Dr. Ludwig Beurle, Dr. Rudolf Mitterlehner und andere, Rechtsanwälte in Linz, wegen 6.073,15 EUR sA, über die Revison der klagenden Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 10. Mai 2016, GZ 32 R 127/15z-56, mit dem das Urteil des Bezirksgerichts Linz vom 7. August 2015, GZ 8 C 1185/13y-50, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Wiedenbauer Mutz Winkler Pramberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Dr.in Zarin Österhellweg`(person)
- `APEA Solar Systeme Aktiengesellschaft`(organisation)
- `Vorderer Sonnberg 7, 2752 Wöllersdorf, Österreich`(address)

**Example 57** (doc_id: `deanon_TRAIN/8Ob99_16s`) (sent_id: `deanon_TRAIN/8Ob99_16s_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn sowie die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei Wien Wilzor AG, Chiara Hellfritsch, vertreten durch Dr. Amhof & Dr. Damian GmbH Rechtsanwälte in Wien, gegen die beklagte Partei Ostfurttal-Touristik GmbH, Elias Stellmaszyk, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen 6.396.663,36 EUR sA, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. August 2016, GZ 1 R 60/16z-14, mit dem festgestellt wurde, dass das Urteil des Landesgerichts Eisenstadt vom 18. Jänner 2014, GZ 27 Cg 47/15b-10, als nicht gefällt anzusehen sei und die Berufung sowie die Berufungsbeantwortung zurückgewiesen wurden, den Beschluss gefasst:  Spruch Der angefochtene Beschluss wird aufgehoben, die Rechtssache an das Berufungsgericht zurückverwiesen und diesem die Fortsetzung des Berufungsverfahrens aufgetragen.

**False Positives:**

- `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien Wilzor AG`(organisation)
- `Chiara Hellfritsch`(person)
- `Ostfurttal-Touristik GmbH`(organisation)
- `Elias Stellmaszyk`(person)

**Example 58** (doc_id: `deanon_TRAIN/8ObA31_23a`) (sent_id: `deanon_TRAIN/8ObA31_23a_4`)


Dr. Andreas Schlegel (aus dem Kreis der Arbeitgeber) und Anton Starecek (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Ing. Zacharias Kloße, vertreten durch Doschek Rechtsanwalts GmbH in Wien, gegen die beklagte Partei EEH Landwirtschaft GmbH Gwendolin Raffelsiefer, vertreten durch Barnert Egermann Illigasch Rechtsanwälte GmbH in Wien, wegen Entlassungsanfechtung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. März 2023, GZ 8 Ra 61/22g-97, mit dem das Urteil des Landesgerichts Korneuburg vom 30. März 2022, GZ 9 Cga 43/19z-88, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Doschek Rechtsanwalts` — no gold match — likely missing annotation
- `Barnert Egermann Illigasch Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. Zacharias Kloße`(person)
- `EEH Landwirtschaft GmbH`(organisation)
- `Gwendolin Raffelsiefer`(person)

**Example 59** (doc_id: `deanon_TRAIN/8ObA56_10h`) (sent_id: `deanon_TRAIN/8ObA56_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras und die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Prof. Mag. Dr. Thomas Keppert und Franz Kisling als weitere Richter in der Arbeitsrechtssache der klagenden Partei Ing. Francois Zindl, vertreten durch Achammer und Mennel Rechtsanwälte OG in Feldkirch, wider die beklagte Partei Marktgemeinde Tatjana Nußhardt, vertreten durch Amman Jehle Juen Rechtsanwälte GmbH in Rankweil, wegen Feststellung des aufrechten Dienstverhältnisses, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. Juni 2010, GZ 15 Ra 2/10x-43, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Amman Jehle Juen Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Francois Zindl`(person)
- `Tatjana Nußhardt`(person)

**Example 60** (doc_id: `deanon_TRAIN/9Ob10_19i`) (sent_id: `deanon_TRAIN/9Ob10_19i_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei See-Automotive Entwicklung GmbH, Alva Scherper, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, gegen die beklagte Partei DrauSuddonPharma GmbH, Gloria Rennicke, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, wegen 6.265 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 29. November 2018, GZ 53 R 212/18k-19, mit dem der Berufung der klagenden Partei gegen das Urteil des Bezirksgerichts Salzburg vom 25. Juni 2018, GZ 17 C 965/17a-15, Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partnerschaft Schuppich Sporn` — no gold match — likely missing annotation
- `Vavrovsky Heine Marth Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `See-Automotive Entwicklung GmbH`(organisation)
- `Alva Scherper`(person)
- `DrauSuddonPharma GmbH`(organisation)
- `Gloria Rennicke`(person)

**Example 61** (doc_id: `deanon_TRAIN/9Ob10_21t`) (sent_id: `deanon_TRAIN/9Ob10_21t_3`)


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

**Example 62** (doc_id: `deanon_TRAIN/9Ob28_23t`) (sent_id: `deanon_TRAIN/9Ob28_23t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Annerl in der Rechtssache der klagenden Partei Dr. Alessia Anwar, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr.inM Li Mavromatidis, vertreten durch Mag. Markus Lechner, Rechtsanwalt in Lochau, wegen 247.483,60 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. Mai 2023, GZ 4 R 28/23d-16, mit dem aus Anlass der Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 16. Dezember 2022, GZ 20 Cg 86/22i-10, und das vorangegangene Verfahren als nichtig aufgehoben und die Klage wegen Unzulässigkeit des Rechtswegs zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 26. Juli 2023 wird in seinem Spruch wie folgt berichtigt: Die Kostenentscheidung hat anstelle der Wortfolge „Die klagende Partei ist schuldig, der beklagten Partei ...“ richtig mit den Worten „DiebeklagtePartei ist schuldig, derklagendenPartei ...“ zu beginnen.

**False Positives:**

- `Held Berdnik Astner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alessia Anwar`(person)
- `Li Mavromatidis`(person)

**Example 63** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_4`)


Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Angelika Blochinger, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Laurence Klüs Gesellschaft m.b.H. (FN FN026367d ), FN434768w, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

**False Positives:**

- `Neubauer Fähnrich Rechtsanwälte` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Angelika Blochinger`(person)
- `Co KG`(organisation)
- `Laurence Klüs`(person)
- `FN026367d`(business_register_number)
- `FN434768w`(business_register_number)

**Example 64** (doc_id: `deanon_TRAIN/9Ob72_18f`) (sent_id: `deanon_TRAIN/9Ob72_18f_3`)


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

**Example 65** (doc_id: `deanon_TRAIN/9ObA109_13i`) (sent_id: `deanon_TRAIN/9ObA109_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Thomas Kallab als weitere Richter in der Arbeitsrechtssache der klagenden Partei Klaus Sowacki, gegen die beklagte Partei Mag. Gerlinde Klobucar, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, wegen 3.674,41 EUR brutto abzüglich 181,96 EUR netto sA (Revisionsinteresse 1.572,49 EUR brutto sA), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Mai 2013, GZ 8 Ra 36/13t-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Hochleitner Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Klaus Sowacki`(person)
- `Mag. Gerlinde Klobucar`(person)

**Example 66** (doc_id: `deanon_TRAIN/9ObA118_19x`) (sent_id: `deanon_TRAIN/9ObA118_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner (Senat nach § 11a ASGG) in der Arbeitsrechtssache der klagenden Partei Thilo Weijer, gegen die beklagte Partei UWK Chemie GmbH, Emma Finzel, vertreten durch Dumfarth Klausberger Rechtsanwälte GmbH & CO KG in Linz, wegen Nichtigkeit und Wiederaufnahme des Verfahrens zu 9 ObA 41/19y, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das beim Obersten Gerichtshof anhängige Verfahren 9 ObA 118/19x wird bis zur Mitteilung des Pflegschaftsgerichts, ob für den Kläger ein (einstweiliger) Erwachsenenvertreter bestellt oder eine sonstige Maßnahme getroffen wird, unterbrochen.

**False Positives:**

- `Dumfarth Klausberger Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Thilo Weijer`(person)
- `UWK Chemie GmbH`(organisation)
- `Emma Finzel`(person)
- `CO KG`(organisation)

**Example 67** (doc_id: `deanon_TRAIN/9ObA129_19i`) (sent_id: `deanon_TRAIN/9ObA129_19i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau, den Hofrat des Obersten Gerichtshofs Dr. Stefula und die fachkundigen Laienrichter KR Mag. Paul Kunsky (aus dem Kreis der Arbeitgeber) und Harald Kohlruss (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Regina Drahtschmidt, LLB, vertreten durch Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Anselm Staeblein, vertreten durch Leitner Hirth Rechtsanwälte GmbH in Graz, wegen 3.461,72 EUR brutto sA (Revisionsinteresse 971,31 EUR brutto sA), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. September 2019, GZ 6 Ra 57/19b-13, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Leitner Hirth Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Regina Drahtschmidt, LLB`(person)
- `Anselm Staeblein`(person)

**Example 68** (doc_id: `deanon_TRAIN/9ObA33_20y`) (sent_id: `deanon_TRAIN/9ObA33_20y_4`)


Gabriele Svirak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Jürgen Fußgänger, vertreten durch Dr. Herbert Holzinger, Rechtsanwalt in Wien, gegen die beklagte Partei UnterImmobilien GmbH, Ing. Virgil Feketics, vertreten durch Salzborn Rechtsanwaltsgesellschaft mbH in Wien, wegen 1.152,44 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2020, GZ 7 Ra 7/20f-23, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Salzborn Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jürgen Fußgänger`(person)
- `UnterImmobilien GmbH`(organisation)
- `Ing. Virgil Feketics`(person)

**Example 69** (doc_id: `deanon_TRAIN/9ObA4_13y`) (sent_id: `deanon_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Maria Maritz, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei PHG Möbel Dienstleistungen GmbH, Zeno Speckl, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Fellner Wratzfeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maria Maritz`(person)
- `PHG Möbel Dienstleistungen GmbH`(organisation)
- `Zeno Speckl`(person)

**Example 70** (doc_id: `deanon_TRAIN/9ObA8_20x`) (sent_id: `deanon_TRAIN/9ObA8_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Werner Pletzenauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Dr. Cornelius Jannes, vertreten durch Moser Mutz Rechtsanwälte GesbR in Klagenfurt am Wörthersee, gegen die beklagte Partei Stubertz & Fortschnieder Daten AG, VetR Zeno Dornedden, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Klagenfurt am Wörthersee, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2019, GZ 7 Ra 70/19x-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wiedenbauer Mutz Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Cornelius Jannes`(person)
- `Stubertz & Fortschnieder Daten AG`(organisation)
- `VetR Zeno Dornedden`(person)

</details>

---

## `Person after 'geboren am' (Born On)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d05f9629`  
**Description:**
Captures names appearing after 'geboren am' (born on) in legal texts, typically identifying the subject of the case. Excludes month names.

**Content:**
```
geboren\s+am\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+in\s+|\s+zu\s+|\s+der\s+|\s+des\s+|\s+am\s+|\s+im\s+|\s+|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after 'gegen' (Defendant)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `10c10e06`  
**Description:**
Captures person names appearing after 'gegen' (against) in legal contexts, ensuring full name capture and excluding company names. Prioritizes this for cases where the name follows 'gegen' directly.

**Content:**
```
(?:gegen\s+|der\s+gegen\s+)(?:Herrn\s+|Frau\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 61 | 0 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 61 | 1219 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 1** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 2** (doc_id: `deanon_TRAIN/11Os49_13k`) (sent_id: `deanon_TRAIN/11Os49_13k_3`)


Kopf Der Oberste Gerichtshof hat am 16. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Wancata als Schriftführer, in der Strafsache gegen Michael Dämering wegen des Verbrechens des schweren Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 4, 129 Z 1 StGB, AZ 13 Hv 23/13d des Landesgerichts Wels, über die von der Generalprokuratur gegen den gemäß § 494a StPO gefassten Beschluss dieses Gerichts vom 20. März 2012, ON 13 der Hv-Akten, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Michael Dämering` — partial — gold is substring of pred: `Dämering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dämering`(person)

**Example 3** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 4** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

**Example 5** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_3`)


Kopf Der Oberste Gerichtshof hat am 8. August 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Josef Klös und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1, Abs 3 StGB, AZ 72 Hv 8/17g des Landesgerichts Klagenfurt, über die Anzeige der Ausgeschlossenheit der Vizepräsidentin des Obersten Gerichtshofs Mag. Marek gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Josef Klös` — partial — gold is substring of pred: `Klös`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klös`(person)

**Example 6** (doc_id: `deanon_TRAIN/12Ns4_15g`) (sent_id: `deanon_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bachel wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Gerhard Bachel` — partial — gold is substring of pred: `Bachel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachel`(person)

**Example 7** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_3`)


Kopf Der Oberste Gerichtshof hat am 18. Oktober 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Bilinska als Schriftführerin in der Strafsache gegen Gerfried Hundgeburth und eine Angeklagte wegen des Verbrechens der betrügerischen Krida nach §§ 156 Abs 1, 161 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten Renata Holzhey gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 11. April 2011, GZ 602 Hv 4/10m-58, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gerfried Hundgeburth` — partial — gold is substring of pred: `Hundgeburth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hundgeburth`(person)
- `Holzhey`(person)

**Example 8** (doc_id: `deanon_TRAIN/12Os11_19p`) (sent_id: `deanon_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Margardt wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Thomas Margardt` — partial — gold is substring of pred: `Margardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Margardt`(person)

**Example 9** (doc_id: `deanon_TRAIN/12Os164_12b`) (sent_id: `deanon_TRAIN/12Os164_12b_3`)


Kopf Der Oberste Gerichtshof hat am 31. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Dr. Pausa als Schriftführerin in der Strafsache gegen Giorgi Standtke wegen des Verbrechens des gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 129 Z 1, 130 vierter Fall und 15 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien vom 17. Oktober 2012, GZ 95 Hv 92/12p-26, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Giorgi Standtke` — partial — gold is substring of pred: `Standtke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Standtke`(person)

**Example 10** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pitzenbauer wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Nenad Pitzenbauer` — partial — gold is substring of pred: `Pitzenbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pitzenbauer`(person)

**Example 11** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Mattheiß und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Tiepoldt auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Viktor Mattheiß` — partial — gold is substring of pred: `Mattheiß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mattheiß`(person)
- `Tiepoldt`(person)

**Example 12** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Viktor Mittermair` — partial — gold is substring of pred: `Mittermair`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 13** (doc_id: `deanon_TRAIN/12Os40_19b`) (sent_id: `deanon_TRAIN/12Os40_19b_3`)


Kopf Der Oberste Gerichtshof hat am 27. Februar 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden sowie durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Schriftführerin Maurer in der Strafsache gegen Alexander Jastrzemsky wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Jugendschöffengericht vom 8. Jänner 2019, GZ 23 Hv 29/18y-28, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alexander Jastrzemsky` — partial — gold is substring of pred: `Jastrzemsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jastrzemsky`(person)

**Example 14** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_3`)


Kopf Der Oberste Gerichtshof hat am 18. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Adamowitsch als Schriftführerin in der Strafsache gegen Norbert Noelker wegen Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB, AZ 16 Hv 32/15g des Landesgerichts Krems an der Donau, über die Beschwerde des Verurteilten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 7. März 2017, AZ 20 Bs 59/17y, nach Einsichtnahme durch die Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Norbert Noelker` — partial — gold is substring of pred: `Noelker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noelker`(person)

**Example 15** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__4`)


In der Strafsache gegen Christian Köbbel, AZ 12 U 86/07z des Bezirksgerichts Baden, verletzt die Abfassung des Protokolls- und Urteilsvermerks vom 25. Juli 2007 (ON 5) das Gesetz in § 32 Abs 2 JGG und in § 458 Abs 3 Z 1 StPO idF BGBl I 2004/164 iVm § 270 Abs 2 Z 2 StPO.

**False Positives:**

- `Christian Köbbel` — partial — gold is substring of pred: `Köbbel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Köbbel`(person)

**Example 16** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__14`)


Am 3. Mai 2010 brachte die Staatsanwaltschaft Wiener Neustadt beim Bezirksgericht Baden erneut einen Strafantrag gegen Christian Kowalzyk wegen des Verdachts der (während der Probezeit begangenen) Vergehen des unbefugten Gebrauchs von Fahrzeugen nach § 136 Abs 1 StGB sowie der Urkundenunterdrückung nach § 229 Abs 1 StGB ein und beantragte zugleich die „Straffestsetzung zu AZ 12 U 86/07z des Bezirksgerichtes Baden“ (ON 3 im Akt AZ 12 U 105/10y).

**False Positives:**

- `Christian Kowalzyk` — partial — gold is substring of pred: `Kowalzyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Baden`(organisation)
- `Kowalzyk`(person)

**Example 17** (doc_id: `deanon_TRAIN/12Os80_15d`) (sent_id: `deanon_TRAIN/12Os80_15d_3`)


Kopf Der Oberste Gerichtshof hat am 28. Jänner 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Jukic als Schriftführerin in der Strafsache gegen Arben Dietlof wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 17. April 2015, GZ 39 Hv 127/14v-47, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Arben Dietlof` — partial — gold is substring of pred: `Dietlof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dietlof`(person)

**Example 18** (doc_id: `deanon_TRAIN/13Os100_16d`) (sent_id: `deanon_TRAIN/13Os100_16d_3`)


Kopf Der Oberste Gerichtshof hat am 12. Oktober 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Krenn als Schriftführerin in der Strafsache gegen Richard Berzine und einen anderen Angeklagten wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Clemens Feidel sowie die Berufungen des Angeklagten Richard Boudewijn und der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 30. Mai 2016, GZ 61 Hv 45/16w-98, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Richard Berzine` — partial — gold is substring of pred: `Berzine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Berzine`(person)
- `Feidel`(person)
- `Boudewijn`(person)

**Example 19** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Abdullah Klingfuss wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. Juli 2019, GZ 41 Hv 18/18i-55, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Abdullah Klingfuss` — partial — gold is substring of pred: `Klingfuss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingfuss`(person)

**Example 20** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_7`)


Danach hat er in Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich und an anderen Orten 1) am 15. Februar 2014 Asli Davidsmeyer mit Gewalt zur Duldung des Analverkehrs genötigt, indem er sie auf ein Bett stieß, im Nacken festhielt und gegen ihren Willen seinen Penis in ihren After einführte, 2) durch im Urteil bezeichnete Handlungen und Äußerungen längere Zeit hindurch gegen andere Personen fortgesetzt Gewalt ausgeübt, und zwar a) ab dem 1. Juni 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014 gegen Asli Dagtekin, b) ab dem Jahr 2012 bis zum 19. November 2014, also länger als ein Jahr, gegen seine am 25. April 2008 geborene, somit unmündige, Tochter Berfin Krempl, sowie c) ab dem Jahr 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014, also länger als ein Jahr, gegen seinen am 18. Juni 2003 geborenen, somit unmündigen, Sohn Ilhan Kukolies, 3) Asli Dücking durch im Urteil bezeichnete Handlungen vorsätzlich am Körper verletzt, und zwar a) im September 2008, wodurch die Genannte Schwellungen und Hämatome erlitt, und b) zwischen September und November 2008, wodurch die Genannte das Bewusstsein verlor und eine Schwellung am Hinterkopf und Rötungen im Kniebereich erlitt, weiters Asli Dietzler durch im Urteil bezeichnete Äußerungen 4) zwischen September und November 2008 zu einer Unterlassung genötigt und 5) am 9. Februar 2017 zumindest mit einer Verletzung am Körper gefährlich bedroht, um sie in Furcht und Unruhe zu versetzen.

**False Positives:**

- `Asli Dagtekin` — partial — gold is substring of pred: `Dagtekin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich`(address)
- `Davidsmeyer`(person)
- `Dagtekin`(person)
- `Krempl`(person)
- `Kukolies`(person)
- `Dücking`(person)
- `Dietzler`(person)

**Example 21** (doc_id: `deanon_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Stelzl wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

**False Positives:**

- `Zoltan Stelzl` — partial — gold is substring of pred: `Stelzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stelzl`(person)

**Example 22** (doc_id: `deanon_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Mitzkait wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag.

**False Positives:**

- `Nikola Mitzkait` — partial — gold is substring of pred: `Mitzkait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mitzkait`(person)

**Example 23** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__3`)


Kopf Der Oberste Gerichtshof hat am 22. November 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Krausam als Schriftführerin in der Strafsache gegen Jasmin Fejfar wegen Vergehen der Erschleichung einer Leistung nach § 149 Abs 1 StGB, AZ 36 Hv 160/11y des Landesgerichts Innsbruck, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 10. Jänner 2012 (ON 49) und andere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Jasmin Fejfar` — partial — gold is substring of pred: `Fejfar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fejfar`(person)

**Example 24** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Lässig und Dr. Oberressl in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mario Speer und andere Angeklagte wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 3, 148 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 12 Hv 110/16x des Landesgerichts Wels, über die Grundrechtsbeschwerde des genannten Angeklagten gegen die Verfügung des Vorsitzenden vom 15. November 2016 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mario Speer` — partial — gold is substring of pred: `Speer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Speer`(person)

**Example 25** (doc_id: `deanon_TRAIN/13Os22_20i`) (sent_id: `deanon_TRAIN/13Os22_20i_3`)


Kopf Der Oberste Gerichtshof hat am 27. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in der Strafsache gegen Erwin Waegert wegen des Verbrechens des Mordes nach §§ 15, 75 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Geschworenengericht vom 19. Dezember 2019, GZ 19 Hv 72/19m-46, nach Anhörung der Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung werden zurückgewiesen.

**False Positives:**

- `Erwin Waegert` — partial — gold is substring of pred: `Waegert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waegert`(person)

**Example 26** (doc_id: `deanon_TRAIN/13Os23_15d`) (sent_id: `deanon_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wissink wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Karl Wissink` — partial — gold is substring of pred: `Wissink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wissink`(person)

**Example 27** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Junghuber wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Erik Junghuber` — partial — gold is substring of pred: `Junghuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Junghuber`(person)

**Example 28** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jerzenbek, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

**False Positives:**

- `Erik Jerzenbek` — partial — gold is substring of pred: `Jerzenbek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jerzenbek`(person)

**Example 29** (doc_id: `deanon_TRAIN/13Os34_19b`) (sent_id: `deanon_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weigenannt wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Wolfgang Weigenannt` — partial — gold is substring of pred: `Weigenannt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weigenannt`(person)

**Example 30** (doc_id: `deanon_TRAIN/13Os37_12h`) (sent_id: `deanon_TRAIN/13Os37_12h_3`)


Kopf Der Oberste Gerichtshof hat am 10. Mai 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Wohlmuth als Schriftführerin in der Strafsache gegen Michael Liebhold und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Waßmann und des DI Georg Lu Babette Prusak gegen den Beschluss des Oberlandesgerichts Innsbruck vom 20. März 2012, AZ 6 Bs 130/12m, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Liebhold` — partial — gold is substring of pred: `Liebhold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Liebhold`(person)
- `Waßmann`(person)
- `Babette Prusak`(person)

**Example 31** (doc_id: `deanon_TRAIN/13Os68_18a`) (sent_id: `deanon_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Coolhaas wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Mihai Coolhaas` — partial — gold is substring of pred: `Coolhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Coolhaas`(person)

**Example 32** (doc_id: `deanon_TRAIN/13Os6_14b`) (sent_id: `deanon_TRAIN/13Os6_14b_3`)


Kopf Der Oberste Gerichtshof hat am 14. März 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Gansterer als Schriftführerin in der Strafsache gegen Valentino Thünissen wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 9. Dezember 2013, GZ 52 Hv 65/13b-21, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Valentino Thünissen` — partial — gold is substring of pred: `Thünissen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thünissen`(person)

**Example 33** (doc_id: `deanon_TRAIN/13Os78_12p`) (sent_id: `deanon_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Längefeld und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wissing und des DI Georg Lu Jeannine Flemmig gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Längefeld` — partial — gold is substring of pred: `Längefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Längefeld`(person)
- `Wissing`(person)
- `Jeannine Flemmig`(person)

**Example 34** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Urbansky wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Robert Urbansky` — partial — gold is substring of pred: `Urbansky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Urbansky`(person)

**Example 35** (doc_id: `deanon_TRAIN/13Os8_11t`) (sent_id: `deanon_TRAIN/13Os8_11t_3`)


Kopf Der Oberste Gerichtshof hat am 17. Februar 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Kirnbauer als Schriftführerin in der Strafsache gegen Delroy Dambrowsky wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 16. November 2010, GZ 031 Hv 125/10t-58, sowie die Beschwerde des Angeklagten gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Delroy Dambrowsky` — partial — gold is substring of pred: `Dambrowsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dambrowsky`(person)

**Example 36** (doc_id: `deanon_TRAIN/13Os97_11f`) (sent_id: `deanon_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Gehler wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

**False Positives:**

- `Ernst Gehler` — partial — gold is substring of pred: `Gehler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gehler`(person)

**Example 37** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Hermanni wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

**False Positives:**

- `Christoph Hermanni` — partial — gold is substring of pred: `Hermanni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermanni`(person)

**Example 38** (doc_id: `deanon_TRAIN/14Os108_18s`) (sent_id: `deanon_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Reichenbach und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kulaksiz gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Misha Reichenbach` — partial — gold is substring of pred: `Reichenbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reichenbach`(person)
- `Kulaksiz`(person)

**Example 39** (doc_id: `deanon_TRAIN/14Os113_12t`) (sent_id: `deanon_TRAIN/14Os113_12t_3`)


Kopf Der Oberste Gerichtshof hat am 18. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen Astrit Börgers wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Geschworenengericht vom 23. August 2012, GZ 24 Hv 38/12m-61, sowie über dessen Beschwerde gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf bedingter Strafnachsichten und einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Astrit Börgers` — partial — gold is substring of pred: `Börgers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Börgers`(person)

**Example 40** (doc_id: `deanon_TRAIN/14Os121_19d`) (sent_id: `deanon_TRAIN/14Os121_19d_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Emir Kles wegen Verbrechen der schweren Körperverletzung nach §§ 15, 84 Abs 4 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 22. August 2019, GZ 52 Hv 23/19b-16, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Emir Kles` — partial — gold is substring of pred: `Kles`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kles`(person)

**Example 41** (doc_id: `deanon_TRAIN/14Os132_10h`) (sent_id: `deanon_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahner wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Tomislav Ahner` — partial — gold is substring of pred: `Ahner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ahner`(person)

**Example 42** (doc_id: `deanon_TRAIN/14Os136_19k`) (sent_id: `deanon_TRAIN/14Os136_19k_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Dimitri Thomassin wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 vierter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 30. September 2019, GZ 632 Hv 2/19a-138, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dimitri Thomassin` — partial — gold is substring of pred: `Thomassin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomassin`(person)

**Example 43** (doc_id: `deanon_TRAIN/14Os16_15g`) (sent_id: `deanon_TRAIN/14Os16_15g_3`)


Kopf Der Oberste Gerichtshof hat am 28. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Moelle als Schriftführerin in der Strafsache gegen Alessandro Braunmiller wegen des Verbrechens nach § 3g VerbotsG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Klagenfurt als Geschworenengericht vom 26. November 2014, GZ 38 Hv 50/14d-36, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alessandro Braunmiller` — partial — gold is substring of pred: `Braunmiller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Braunmiller`(person)

**Example 44** (doc_id: `deanon_TRAIN/14Os63_12i`) (sent_id: `deanon_TRAIN/14Os63_12i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart des Richteramtsanwärters Mag. Lindenbauer als Schriftführer in der Strafsache gegen Johann Haugk wegen des Verbrechens des Suchtgifthandels nach §§ 12 dritter Fall, 15 StGB, 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 29. Februar 2012, GZ 35 Hv 150/11z-93, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Johann Haugk` — partial — gold is substring of pred: `Haugk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Haugk`(person)

**Example 45** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_3`)


Kopf Der Oberste Gerichtshof hat am 5. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Draginja Nielson und einen Angeklagten wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 30. März 2017, GZ 26 Hv 117/16h-55, sowie ihre Beschwerde gegen den zugleich gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Draginja Nielson` — partial — gold is substring of pred: `Nielson`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nielson`(person)

**Example 46** (doc_id: `deanon_TRAIN/14Os71_17y`) (sent_id: `deanon_TRAIN/14Os71_17y_3`)


Kopf Der Oberste Gerichtshof hat am 3. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Adam Albanesi wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Geschworenengericht vom 5. Mai 2017, GZ 35 Hv 15/17a-83, sowie über die Beschwerde des Angeklagten gegen den Beschluss auf Widerruf einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Adam Albanesi` — partial — gold is substring of pred: `Albanesi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albanesi`(person)

**Example 47** (doc_id: `deanon_TRAIN/15Ns104_16m`) (sent_id: `deanon_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Höferth wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Markus Höferth` — partial — gold is substring of pred: `Höferth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Höferth`(person)

**Example 48** (doc_id: `deanon_TRAIN/15Os110_17s`) (sent_id: `deanon_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Valerius Niesse, MA und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Laila Niezoldi gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Shafiqullah Valerius Niesse` — positional overlap with gold: `Valerius Niesse, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerius Niesse, MA`(person)
- `Laila Niezoldi`(person)

**Example 49** (doc_id: `deanon_TRAIN/15Os114_10v`) (sent_id: `deanon_TRAIN/15Os114_10v_3`)


Kopf Der Oberste Gerichtshof hat am 15. September 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger als weitere Richter, in Gegenwart der Rechtspraktikantin Mag. Reich als Schriftführerin, in der Strafsache gegen Marek Dirksmeyer wegen des Verbrechens des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. April 2010, GZ 40 Hv 1/10w-32, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung des Angeklagten „wegen Schuld“ werden zurückgewiesen.

**False Positives:**

- `Marek Dirksmeyer` — partial — gold is substring of pred: `Dirksmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dirksmeyer`(person)

**Example 50** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_3`)


Kopf Der Oberste Gerichtshof hat am 19. Februar 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Ent als Schriftführer in der Strafsache gegen Christian Poethke und einen anderen Angeklagten wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer anderen strafbaren Handlung, (zuletzt) AZ 33 Hv 70/12x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Rakhart Jörg Andrich auf Erneuerung des Strafverfahrens gemäß § 363a Abs 1 StPO nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Christian Poethke` — partial — gold is substring of pred: `Poethke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poethke`(person)
- `Jörg Andrich`(person)

**Example 51** (doc_id: `deanon_TRAIN/15Os178_15p`) (sent_id: `deanon_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Korsmeier gegen Martin Rühmekorb wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klingspohr vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

**False Positives:**

- `Martin Rühmekorb` — partial — gold is substring of pred: `Rühmekorb`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Korsmeier`(person)
- `Rühmekorb`(person)
- `Klingspohr`(person)

**Example 52** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Bahar wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Manfred Bahar` — partial — gold is substring of pred: `Bahar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bahar`(person)

**Example 53** (doc_id: `deanon_TRAIN/15Os53_16g`) (sent_id: `deanon_TRAIN/15Os53_16g_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Janisch als Schriftführerin in der Strafsache gegen Eduard Meisslein wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 erster Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 21. Dezember 2015, GZ 181 Hv 4/15x-46, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Eduard Meisslein` — partial — gold is substring of pred: `Meisslein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Meisslein`(person)

**Example 54** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Rauhe und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Johann Rauhe` — partial — gold is substring of pred: `Rauhe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rauhe`(person)

**Example 55** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_8`)


Text Gründe: Die Staatsanwaltschaft Wels führt zu AZ 17 St 77/19g ein Ermittlungsverfahren gegen Johann Remppel wegen des Verdachts des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG und weiterer strafbarer Handlungen.

**False Positives:**

- `Johann Remppel` — partial — gold is substring of pred: `Remppel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Remppel`(person)

**Example 56** (doc_id: `deanon_TRAIN/15Os72_12w`) (sent_id: `deanon_TRAIN/15Os72_12w_4`)


Karlicek als Schriftführerin in der Strafsache gegen Rudolf Czaya wegen Verbrechen der Vergewaltigung nach §§ 201 Abs 1, 15 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 23. März 2012, GZ 631 Hv 2/12h-28, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Rudolf Czaya` — partial — gold is substring of pred: `Czaya`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Czaya`(person)

**Example 57** (doc_id: `deanon_TRAIN/15Os96_17g`) (sent_id: `deanon_TRAIN/15Os96_17g_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Roman Abbold wegen des Verbrechens der terroristischen Vereinigung nach § 278b Abs 2 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 16. Mai 2017, GZ 39 Hv 6/17h-37, sowie über dessen Beschwerde gegen den Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Roman Abbold` — partial — gold is substring of pred: `Abbold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Abbold`(person)

**Example 58** (doc_id: `deanon_TRAIN/15Os98_15y`) (sent_id: `deanon_TRAIN/15Os98_15y_3`)


Kopf Der Oberste Gerichtshof hat am 26. August 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Leisser als Schriftführerin in der Strafsache gegen Gottlieb Zekalla wegen des Verbrechens des Diebstahls durch Einbruch nach §§ 127, 129 Z 1 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 19. Mai 2015, GZ 39 Hv 105/13k-91, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur Dr. Ulrich, des Angeklagten und seines Verteidigers Dr. Pohle zu Recht erkannt:  Spruch

**False Positives:**

- `Gottlieb Zekalla` — partial — gold is substring of pred: `Zekalla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zekalla`(person)

**Example 59** (doc_id: `deanon_TRAIN/15Os9_12f`) (sent_id: `deanon_TRAIN/15Os9_12f_4`)


Linzner als Schriftführerin in der Strafsache gegen Georg Henckens wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

**False Positives:**

- `Georg Henckens` — partial — gold is substring of pred: `Henckens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Henckens`(person)

**Example 60** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Juni 2018 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Gerhard Obeser und eine Angeklagte wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und weiterer strafbarer Handlungen aus Anlass der Nichtigkeitsbeschwerde der Angeklagten Mag. (FH) Nicole Kochem gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 31. Oktober 2017, GZ 78 Hv 76/17a-76,nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Stani, des Angeklagten Gerhard Oravec und seines Verteidigers Dr. Gärtner zu Recht erkannt:  Spruch

**False Positives:**

- `Gerhard Obeser` — partial — gold is substring of pred: `Obeser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obeser`(person)
- `Kochem`(person)
- `Oravec`(person)

</details>

---

## `Person in Legal Case Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0e41d831`  
**Description:**
Captures names appearing after 'Beschwerdesache', 'Strafsache', 'Rechtssache', or 'gegen' (against) in legal contexts, ensuring full name capture. Handles standalone surnames and multi-word names.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Strafsache|Rechtssache|Verwaltungsstrafsache|Arbeitsrechtssache|Familienrechtssache)|der\s+(?:Beschwerdesache|Strafsache|Rechtssache|Verwaltungsstrafsache|Arbeitsrechtssache|Familienrechtssache)|gegen\s+)(?:Herrn\s+|Frau\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?\s*(?!GmbH|AG|KG|mbH|Co\.?|Ltd|Inc|LLC|\s+GmbH|\s+AG|\s+KG|\s+mbH|\s+Co\.?|\s+Ltd|\s+Inc|\s+LLC|Stadtgemeinde|Gemeinde|Verein|Gesellschaft|Unternehmen|Firma|Werk|Bank|Pharma|Energie|Versand|Handel|Technik|Bau|Immobilien|Consulting|Management|Group|Holdings|Partners|&|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 61 | 0 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 61 | 1219 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Bekar und Norbert Weib wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Bernhard Bekar` — partial — gold is substring of pred: `Bekar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bekar`(person)
- `Weib`(person)

**Example 1** (doc_id: `deanon_TRAIN/11Os175_10k`) (sent_id: `deanon_TRAIN/11Os175_10k_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Koller als Schriftführer, in der Strafsache gegen Alfred Simonbauer wegen des Verbrechens des Mordes nach § 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Geschworenengericht vom 13. September 2010, GZ 37 Hv 86/10v-102, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alfred Simonbauer` — partial — gold is substring of pred: `Simonbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Simonbauer`(person)

**Example 2** (doc_id: `deanon_TRAIN/11Os49_13k`) (sent_id: `deanon_TRAIN/11Os49_13k_3`)


Kopf Der Oberste Gerichtshof hat am 16. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Wancata als Schriftführer, in der Strafsache gegen Michael Dämering wegen des Verbrechens des schweren Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 4, 129 Z 1 StGB, AZ 13 Hv 23/13d des Landesgerichts Wels, über die von der Generalprokuratur gegen den gemäß § 494a StPO gefassten Beschluss dieses Gerichts vom 20. März 2012, ON 13 der Hv-Akten, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Michael Dämering` — partial — gold is substring of pred: `Dämering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dämering`(person)

**Example 3** (doc_id: `deanon_TRAIN/11Os67_16m`) (sent_id: `deanon_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kleefeld wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Daniel Kleefeld` — partial — gold is substring of pred: `Kleefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kleefeld`(person)

**Example 4** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Andre Raszka` — partial — gold is substring of pred: `Raszka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

**Example 5** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_3`)


Kopf Der Oberste Gerichtshof hat am 8. August 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Josef Klös und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1, Abs 3 StGB, AZ 72 Hv 8/17g des Landesgerichts Klagenfurt, über die Anzeige der Ausgeschlossenheit der Vizepräsidentin des Obersten Gerichtshofs Mag. Marek gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Josef Klös` — partial — gold is substring of pred: `Klös`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klös`(person)

**Example 6** (doc_id: `deanon_TRAIN/12Ns4_15g`) (sent_id: `deanon_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bachel wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Gerhard Bachel` — partial — gold is substring of pred: `Bachel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachel`(person)

**Example 7** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_3`)


Kopf Der Oberste Gerichtshof hat am 18. Oktober 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Bilinska als Schriftführerin in der Strafsache gegen Gerfried Hundgeburth und eine Angeklagte wegen des Verbrechens der betrügerischen Krida nach §§ 156 Abs 1, 161 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten Renata Holzhey gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 11. April 2011, GZ 602 Hv 4/10m-58, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gerfried Hundgeburth` — partial — gold is substring of pred: `Hundgeburth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hundgeburth`(person)
- `Holzhey`(person)

**Example 8** (doc_id: `deanon_TRAIN/12Os11_19p`) (sent_id: `deanon_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Margardt wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Thomas Margardt` — partial — gold is substring of pred: `Margardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Margardt`(person)

**Example 9** (doc_id: `deanon_TRAIN/12Os164_12b`) (sent_id: `deanon_TRAIN/12Os164_12b_3`)


Kopf Der Oberste Gerichtshof hat am 31. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Dr. Pausa als Schriftführerin in der Strafsache gegen Giorgi Standtke wegen des Verbrechens des gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 129 Z 1, 130 vierter Fall und 15 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien vom 17. Oktober 2012, GZ 95 Hv 92/12p-26, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Giorgi Standtke` — partial — gold is substring of pred: `Standtke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Standtke`(person)

**Example 10** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pitzenbauer wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

**False Positives:**

- `Nenad Pitzenbauer` — partial — gold is substring of pred: `Pitzenbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pitzenbauer`(person)

**Example 11** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Mattheiß und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Tiepoldt auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Viktor Mattheiß` — partial — gold is substring of pred: `Mattheiß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mattheiß`(person)
- `Tiepoldt`(person)

**Example 12** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Viktor Mittermair` — partial — gold is substring of pred: `Mittermair`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 13** (doc_id: `deanon_TRAIN/12Os40_19b`) (sent_id: `deanon_TRAIN/12Os40_19b_3`)


Kopf Der Oberste Gerichtshof hat am 27. Februar 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden sowie durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Schriftführerin Maurer in der Strafsache gegen Alexander Jastrzemsky wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Jugendschöffengericht vom 8. Jänner 2019, GZ 23 Hv 29/18y-28, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alexander Jastrzemsky` — partial — gold is substring of pred: `Jastrzemsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jastrzemsky`(person)

**Example 14** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_3`)


Kopf Der Oberste Gerichtshof hat am 18. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Adamowitsch als Schriftführerin in der Strafsache gegen Norbert Noelker wegen Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB, AZ 16 Hv 32/15g des Landesgerichts Krems an der Donau, über die Beschwerde des Verurteilten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 7. März 2017, AZ 20 Bs 59/17y, nach Einsichtnahme durch die Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Norbert Noelker` — partial — gold is substring of pred: `Noelker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noelker`(person)

**Example 15** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__4`)


In der Strafsache gegen Christian Köbbel, AZ 12 U 86/07z des Bezirksgerichts Baden, verletzt die Abfassung des Protokolls- und Urteilsvermerks vom 25. Juli 2007 (ON 5) das Gesetz in § 32 Abs 2 JGG und in § 458 Abs 3 Z 1 StPO idF BGBl I 2004/164 iVm § 270 Abs 2 Z 2 StPO.

**False Positives:**

- `Christian Köbbel` — partial — gold is substring of pred: `Köbbel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Köbbel`(person)

**Example 16** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__14`)


Am 3. Mai 2010 brachte die Staatsanwaltschaft Wiener Neustadt beim Bezirksgericht Baden erneut einen Strafantrag gegen Christian Kowalzyk wegen des Verdachts der (während der Probezeit begangenen) Vergehen des unbefugten Gebrauchs von Fahrzeugen nach § 136 Abs 1 StGB sowie der Urkundenunterdrückung nach § 229 Abs 1 StGB ein und beantragte zugleich die „Straffestsetzung zu AZ 12 U 86/07z des Bezirksgerichtes Baden“ (ON 3 im Akt AZ 12 U 105/10y).

**False Positives:**

- `Christian Kowalzyk` — partial — gold is substring of pred: `Kowalzyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Baden`(organisation)
- `Kowalzyk`(person)

**Example 17** (doc_id: `deanon_TRAIN/12Os80_15d`) (sent_id: `deanon_TRAIN/12Os80_15d_3`)


Kopf Der Oberste Gerichtshof hat am 28. Jänner 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Jukic als Schriftführerin in der Strafsache gegen Arben Dietlof wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 17. April 2015, GZ 39 Hv 127/14v-47, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Arben Dietlof` — partial — gold is substring of pred: `Dietlof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dietlof`(person)

**Example 18** (doc_id: `deanon_TRAIN/13Os100_16d`) (sent_id: `deanon_TRAIN/13Os100_16d_3`)


Kopf Der Oberste Gerichtshof hat am 12. Oktober 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Krenn als Schriftführerin in der Strafsache gegen Richard Berzine und einen anderen Angeklagten wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Clemens Feidel sowie die Berufungen des Angeklagten Richard Boudewijn und der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 30. Mai 2016, GZ 61 Hv 45/16w-98, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Richard Berzine` — partial — gold is substring of pred: `Berzine`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Berzine`(person)
- `Feidel`(person)
- `Boudewijn`(person)

**Example 19** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Abdullah Klingfuss wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. Juli 2019, GZ 41 Hv 18/18i-55, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Abdullah Klingfuss` — partial — gold is substring of pred: `Klingfuss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingfuss`(person)

**Example 20** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_7`)


Danach hat er in Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich und an anderen Orten 1) am 15. Februar 2014 Asli Davidsmeyer mit Gewalt zur Duldung des Analverkehrs genötigt, indem er sie auf ein Bett stieß, im Nacken festhielt und gegen ihren Willen seinen Penis in ihren After einführte, 2) durch im Urteil bezeichnete Handlungen und Äußerungen längere Zeit hindurch gegen andere Personen fortgesetzt Gewalt ausgeübt, und zwar a) ab dem 1. Juni 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014 gegen Asli Dagtekin, b) ab dem Jahr 2012 bis zum 19. November 2014, also länger als ein Jahr, gegen seine am 25. April 2008 geborene, somit unmündige, Tochter Berfin Krempl, sowie c) ab dem Jahr 2009 bis zum Februar 2010 und vom Juli 2011 bis zum 19. November 2014, also länger als ein Jahr, gegen seinen am 18. Juni 2003 geborenen, somit unmündigen, Sohn Ilhan Kukolies, 3) Asli Dücking durch im Urteil bezeichnete Handlungen vorsätzlich am Körper verletzt, und zwar a) im September 2008, wodurch die Genannte Schwellungen und Hämatome erlitt, und b) zwischen September und November 2008, wodurch die Genannte das Bewusstsein verlor und eine Schwellung am Hinterkopf und Rötungen im Kniebereich erlitt, weiters Asli Dietzler durch im Urteil bezeichnete Äußerungen 4) zwischen September und November 2008 zu einer Unterlassung genötigt und 5) am 9. Februar 2017 zumindest mit einer Verletzung am Körper gefährlich bedroht, um sie in Furcht und Unruhe zu versetzen.

**False Positives:**

- `Asli Dagtekin` — partial — gold is substring of pred: `Dagtekin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert-Zumpf-Gasse 13, 9321 Krasta, Österreich`(address)
- `Davidsmeyer`(person)
- `Dagtekin`(person)
- `Krempl`(person)
- `Kukolies`(person)
- `Dücking`(person)
- `Dietzler`(person)

**Example 21** (doc_id: `deanon_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Stelzl wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

**False Positives:**

- `Zoltan Stelzl` — partial — gold is substring of pred: `Stelzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stelzl`(person)

**Example 22** (doc_id: `deanon_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Mitzkait wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag.

**False Positives:**

- `Nikola Mitzkait` — partial — gold is substring of pred: `Mitzkait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mitzkait`(person)

**Example 23** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__3`)


Kopf Der Oberste Gerichtshof hat am 22. November 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Krausam als Schriftführerin in der Strafsache gegen Jasmin Fejfar wegen Vergehen der Erschleichung einer Leistung nach § 149 Abs 1 StGB, AZ 36 Hv 160/11y des Landesgerichts Innsbruck, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 10. Jänner 2012 (ON 49) und andere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Geymayer, zu Recht erkannt:  Spruch

**False Positives:**

- `Jasmin Fejfar` — partial — gold is substring of pred: `Fejfar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fejfar`(person)

**Example 24** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Lässig und Dr. Oberressl in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mario Speer und andere Angeklagte wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 3, 148 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 12 Hv 110/16x des Landesgerichts Wels, über die Grundrechtsbeschwerde des genannten Angeklagten gegen die Verfügung des Vorsitzenden vom 15. November 2016 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Mario Speer` — partial — gold is substring of pred: `Speer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Speer`(person)

**Example 25** (doc_id: `deanon_TRAIN/13Os22_20i`) (sent_id: `deanon_TRAIN/13Os22_20i_3`)


Kopf Der Oberste Gerichtshof hat am 27. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in der Strafsache gegen Erwin Waegert wegen des Verbrechens des Mordes nach §§ 15, 75 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Geschworenengericht vom 19. Dezember 2019, GZ 19 Hv 72/19m-46, nach Anhörung der Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung werden zurückgewiesen.

**False Positives:**

- `Erwin Waegert` — partial — gold is substring of pred: `Waegert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waegert`(person)

**Example 26** (doc_id: `deanon_TRAIN/13Os23_15d`) (sent_id: `deanon_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wissink wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Karl Wissink` — partial — gold is substring of pred: `Wissink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wissink`(person)

**Example 27** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Junghuber wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Erik Junghuber` — partial — gold is substring of pred: `Junghuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Junghuber`(person)

**Example 28** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jerzenbek, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

**False Positives:**

- `Erik Jerzenbek` — partial — gold is substring of pred: `Jerzenbek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jerzenbek`(person)

**Example 29** (doc_id: `deanon_TRAIN/13Os34_19b`) (sent_id: `deanon_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weigenannt wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Wolfgang Weigenannt` — partial — gold is substring of pred: `Weigenannt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weigenannt`(person)

**Example 30** (doc_id: `deanon_TRAIN/13Os37_12h`) (sent_id: `deanon_TRAIN/13Os37_12h_3`)


Kopf Der Oberste Gerichtshof hat am 10. Mai 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Wohlmuth als Schriftführerin in der Strafsache gegen Michael Liebhold und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Waßmann und des DI Georg Lu Babette Prusak gegen den Beschluss des Oberlandesgerichts Innsbruck vom 20. März 2012, AZ 6 Bs 130/12m, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Liebhold` — partial — gold is substring of pred: `Liebhold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Liebhold`(person)
- `Waßmann`(person)
- `Babette Prusak`(person)

**Example 31** (doc_id: `deanon_TRAIN/13Os68_18a`) (sent_id: `deanon_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Coolhaas wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Mihai Coolhaas` — partial — gold is substring of pred: `Coolhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Coolhaas`(person)

**Example 32** (doc_id: `deanon_TRAIN/13Os6_14b`) (sent_id: `deanon_TRAIN/13Os6_14b_3`)


Kopf Der Oberste Gerichtshof hat am 14. März 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Gansterer als Schriftführerin in der Strafsache gegen Valentino Thünissen wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 9. Dezember 2013, GZ 52 Hv 65/13b-21, sowie über die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Valentino Thünissen` — partial — gold is substring of pred: `Thünissen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thünissen`(person)

**Example 33** (doc_id: `deanon_TRAIN/13Os78_12p`) (sent_id: `deanon_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Längefeld und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wissing und des DI Georg Lu Jeannine Flemmig gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

**False Positives:**

- `Michael Längefeld` — partial — gold is substring of pred: `Längefeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Längefeld`(person)
- `Wissing`(person)
- `Jeannine Flemmig`(person)

**Example 34** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Urbansky wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Robert Urbansky` — partial — gold is substring of pred: `Urbansky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Urbansky`(person)

**Example 35** (doc_id: `deanon_TRAIN/13Os8_11t`) (sent_id: `deanon_TRAIN/13Os8_11t_3`)


Kopf Der Oberste Gerichtshof hat am 17. Februar 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Kirnbauer als Schriftführerin in der Strafsache gegen Delroy Dambrowsky wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 16. November 2010, GZ 031 Hv 125/10t-58, sowie die Beschwerde des Angeklagten gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Delroy Dambrowsky` — partial — gold is substring of pred: `Dambrowsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dambrowsky`(person)

**Example 36** (doc_id: `deanon_TRAIN/13Os97_11f`) (sent_id: `deanon_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Gehler wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

**False Positives:**

- `Ernst Gehler` — partial — gold is substring of pred: `Gehler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gehler`(person)

**Example 37** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Hermanni wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

**False Positives:**

- `Christoph Hermanni` — partial — gold is substring of pred: `Hermanni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermanni`(person)

**Example 38** (doc_id: `deanon_TRAIN/14Os108_18s`) (sent_id: `deanon_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Reichenbach und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kulaksiz gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Misha Reichenbach` — partial — gold is substring of pred: `Reichenbach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reichenbach`(person)
- `Kulaksiz`(person)

**Example 39** (doc_id: `deanon_TRAIN/14Os113_12t`) (sent_id: `deanon_TRAIN/14Os113_12t_3`)


Kopf Der Oberste Gerichtshof hat am 18. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen Astrit Börgers wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Geschworenengericht vom 23. August 2012, GZ 24 Hv 38/12m-61, sowie über dessen Beschwerde gegen den gemeinsam mit dem Urteil gefassten Beschluss auf Widerruf bedingter Strafnachsichten und einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Astrit Börgers` — partial — gold is substring of pred: `Börgers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Börgers`(person)

**Example 40** (doc_id: `deanon_TRAIN/14Os121_19d`) (sent_id: `deanon_TRAIN/14Os121_19d_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Emir Kles wegen Verbrechen der schweren Körperverletzung nach §§ 15, 84 Abs 4 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 22. August 2019, GZ 52 Hv 23/19b-16, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Emir Kles` — partial — gold is substring of pred: `Kles`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kles`(person)

**Example 41** (doc_id: `deanon_TRAIN/14Os132_10h`) (sent_id: `deanon_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahner wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Tomislav Ahner` — partial — gold is substring of pred: `Ahner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ahner`(person)

**Example 42** (doc_id: `deanon_TRAIN/14Os136_19k`) (sent_id: `deanon_TRAIN/14Os136_19k_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Dimitri Thomassin wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 vierter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 30. September 2019, GZ 632 Hv 2/19a-138, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dimitri Thomassin` — partial — gold is substring of pred: `Thomassin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomassin`(person)

**Example 43** (doc_id: `deanon_TRAIN/14Os16_15g`) (sent_id: `deanon_TRAIN/14Os16_15g_3`)


Kopf Der Oberste Gerichtshof hat am 28. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Moelle als Schriftführerin in der Strafsache gegen Alessandro Braunmiller wegen des Verbrechens nach § 3g VerbotsG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Klagenfurt als Geschworenengericht vom 26. November 2014, GZ 38 Hv 50/14d-36, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Alessandro Braunmiller` — partial — gold is substring of pred: `Braunmiller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Braunmiller`(person)

**Example 44** (doc_id: `deanon_TRAIN/14Os63_12i`) (sent_id: `deanon_TRAIN/14Os63_12i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätin des Obersten Gerichtshofs Mag. Fürnkranz in Gegenwart des Richteramtsanwärters Mag. Lindenbauer als Schriftführer in der Strafsache gegen Johann Haugk wegen des Verbrechens des Suchtgifthandels nach §§ 12 dritter Fall, 15 StGB, 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 29. Februar 2012, GZ 35 Hv 150/11z-93, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Johann Haugk` — partial — gold is substring of pred: `Haugk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Haugk`(person)

**Example 45** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_3`)


Kopf Der Oberste Gerichtshof hat am 5. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Draginja Nielson und einen Angeklagten wegen des Verbrechens des Raubes nach § 142 Abs 1 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung der Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 30. März 2017, GZ 26 Hv 117/16h-55, sowie ihre Beschwerde gegen den zugleich gefassten Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Draginja Nielson` — partial — gold is substring of pred: `Nielson`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nielson`(person)

**Example 46** (doc_id: `deanon_TRAIN/14Os71_17y`) (sent_id: `deanon_TRAIN/14Os71_17y_3`)


Kopf Der Oberste Gerichtshof hat am 3. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Wukovits, LL.M., als Schriftführerin in der Strafsache gegen Adam Albanesi wegen des Verbrechens des Mordes nach §§ 15, 75 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Geschworenengericht vom 5. Mai 2017, GZ 35 Hv 15/17a-83, sowie über die Beschwerde des Angeklagten gegen den Beschluss auf Widerruf einer bedingten Entlassung nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Adam Albanesi` — partial — gold is substring of pred: `Albanesi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albanesi`(person)

**Example 47** (doc_id: `deanon_TRAIN/15Ns104_16m`) (sent_id: `deanon_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Höferth wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Markus Höferth` — partial — gold is substring of pred: `Höferth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Höferth`(person)

**Example 48** (doc_id: `deanon_TRAIN/15Os110_17s`) (sent_id: `deanon_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Valerius Niesse, MA und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Laila Niezoldi gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Shafiqullah Valerius Niesse` — positional overlap with gold: `Valerius Niesse, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerius Niesse, MA`(person)
- `Laila Niezoldi`(person)

**Example 49** (doc_id: `deanon_TRAIN/15Os114_10v`) (sent_id: `deanon_TRAIN/15Os114_10v_3`)


Kopf Der Oberste Gerichtshof hat am 15. September 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger als weitere Richter, in Gegenwart der Rechtspraktikantin Mag. Reich als Schriftführerin, in der Strafsache gegen Marek Dirksmeyer wegen des Verbrechens des sexuellen Missbrauchs von Unmündigen nach § 207 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 8. April 2010, GZ 40 Hv 1/10w-32, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung des Angeklagten „wegen Schuld“ werden zurückgewiesen.

**False Positives:**

- `Marek Dirksmeyer` — partial — gold is substring of pred: `Dirksmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dirksmeyer`(person)

**Example 50** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_3`)


Kopf Der Oberste Gerichtshof hat am 19. Februar 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Ent als Schriftführer in der Strafsache gegen Christian Poethke und einen anderen Angeklagten wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer anderen strafbaren Handlung, (zuletzt) AZ 33 Hv 70/12x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Rakhart Jörg Andrich auf Erneuerung des Strafverfahrens gemäß § 363a Abs 1 StPO nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Christian Poethke` — partial — gold is substring of pred: `Poethke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poethke`(person)
- `Jörg Andrich`(person)

**Example 51** (doc_id: `deanon_TRAIN/15Os178_15p`) (sent_id: `deanon_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Korsmeier gegen Martin Rühmekorb wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klingspohr vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

**False Positives:**

- `Martin Rühmekorb` — partial — gold is substring of pred: `Rühmekorb`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Korsmeier`(person)
- `Rühmekorb`(person)
- `Klingspohr`(person)

**Example 52** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Bahar wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

**False Positives:**

- `Manfred Bahar` — partial — gold is substring of pred: `Bahar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bahar`(person)

**Example 53** (doc_id: `deanon_TRAIN/15Os53_16g`) (sent_id: `deanon_TRAIN/15Os53_16g_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Janisch als Schriftführerin in der Strafsache gegen Eduard Meisslein wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 und Abs 2 erster Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 21. Dezember 2015, GZ 181 Hv 4/15x-46, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Eduard Meisslein` — partial — gold is substring of pred: `Meisslein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Meisslein`(person)

**Example 54** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Rauhe und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

**False Positives:**

- `Johann Rauhe` — partial — gold is substring of pred: `Rauhe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rauhe`(person)

**Example 55** (doc_id: `deanon_TRAIN/15Os61_20i`) (sent_id: `deanon_TRAIN/15Os61_20i_8`)


Text Gründe: Die Staatsanwaltschaft Wels führt zu AZ 17 St 77/19g ein Ermittlungsverfahren gegen Johann Remppel wegen des Verdachts des Verbrechens des Suchtgifthandels nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG und weiterer strafbarer Handlungen.

**False Positives:**

- `Johann Remppel` — partial — gold is substring of pred: `Remppel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Remppel`(person)

**Example 56** (doc_id: `deanon_TRAIN/15Os72_12w`) (sent_id: `deanon_TRAIN/15Os72_12w_4`)


Karlicek als Schriftführerin in der Strafsache gegen Rudolf Czaya wegen Verbrechen der Vergewaltigung nach §§ 201 Abs 1, 15 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Korneuburg als Schöffengericht vom 23. März 2012, GZ 631 Hv 2/12h-28, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Rudolf Czaya` — partial — gold is substring of pred: `Czaya`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Czaya`(person)

**Example 57** (doc_id: `deanon_TRAIN/15Os96_17g`) (sent_id: `deanon_TRAIN/15Os96_17g_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Roman Abbold wegen des Verbrechens der terroristischen Vereinigung nach § 278b Abs 2 StGB und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 16. Mai 2017, GZ 39 Hv 6/17h-37, sowie über dessen Beschwerde gegen den Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Roman Abbold` — partial — gold is substring of pred: `Abbold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Abbold`(person)

**Example 58** (doc_id: `deanon_TRAIN/15Os98_15y`) (sent_id: `deanon_TRAIN/15Os98_15y_3`)


Kopf Der Oberste Gerichtshof hat am 26. August 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Leisser als Schriftführerin in der Strafsache gegen Gottlieb Zekalla wegen des Verbrechens des Diebstahls durch Einbruch nach §§ 127, 129 Z 1 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 19. Mai 2015, GZ 39 Hv 105/13k-91, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur Dr. Ulrich, des Angeklagten und seines Verteidigers Dr. Pohle zu Recht erkannt:  Spruch

**False Positives:**

- `Gottlieb Zekalla` — partial — gold is substring of pred: `Zekalla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zekalla`(person)

**Example 59** (doc_id: `deanon_TRAIN/15Os9_12f`) (sent_id: `deanon_TRAIN/15Os9_12f_4`)


Linzner als Schriftführerin in der Strafsache gegen Georg Henckens wegen des Vergehens des Betrugs nach § 146 StGB, AZ 24 Hv 84/11k des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Sperker, zu Recht erkannt:  Spruch

**False Positives:**

- `Georg Henckens` — partial — gold is substring of pred: `Henckens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Henckens`(person)

**Example 60** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Juni 2018 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Gerhard Obeser und eine Angeklagte wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und weiterer strafbarer Handlungen aus Anlass der Nichtigkeitsbeschwerde der Angeklagten Mag. (FH) Nicole Kochem gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 31. Oktober 2017, GZ 78 Hv 76/17a-76,nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Stani, des Angeklagten Gerhard Oravec und seines Verteidigers Dr. Gärtner zu Recht erkannt:  Spruch

**False Positives:**

- `Gerhard Obeser` — partial — gold is substring of pred: `Obeser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obeser`(person)
- `Kochem`(person)
- `Oravec`(person)

</details>

---

</details>

---

