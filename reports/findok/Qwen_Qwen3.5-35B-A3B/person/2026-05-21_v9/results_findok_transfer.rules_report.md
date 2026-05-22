# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-21T23:33:19.106994

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-21_v9/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2549 |
| Validation documents | 639 |
| Test documents | 1247 |
| Train sentences | 4268 |
| Validation sentences | 968 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 200 |
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
| Batch size | 50 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | findok |
| Seed Rule Count | 10 |
| New Rules Added | 2 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 4080 |
| Phase1 Eval Sentences | 927 |
| Transfer Train Sentences | 188 |
| Transfer Eval Sentences | 41 |
| Best Batch Idx | 2 |
| Best Batch F1 | 0.27972027972027974 |
| Best Rules Serialized | [{'id': 'ec6abf56', 'name': 'extract_german_legal_person_mandantin', 'description': "Extracts person names following 'Mandantin, Frau' or 'Mandant, Herr' patterns common in legal letters.", 'format': 'regex', 'content': '(?:Mandantin,\\s+Frau\\s+|Mandant,\\s+Herr\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)*)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '76006b7f', 'name': 'extract_german_legal_person_nachname_wie_bf', 'description': "Extracts person names following the specific legal context marker '(Nachname wie Bf.)'. This handles cases where the name is explicitly listed after this marker.", 'format': 'regex', 'content': '\\(Nachname\\s+wie\\s+Bf\\.\\)\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)*)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'f0f54feb', 'name': 'extract_german_legal_person_children_context', 'description': "Extracts person names following 'für die Kinder' or 'Kinder' in a list context, capturing the full name without assuming a title.", 'format': 'regex', 'content': '(?:für\\s+die\\s+Kinder\\s+|Kinder\\s+)([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:,\\s*(?:geboren|und|und\\s+|\\))?)?)(?=\\s|,|\\(|\\)|$)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '44fe6684', 'name': 'extract_german_legal_person_direct_context', 'description': "Extracts person names directly following 'in der Beschwerdesache' or 'Beschwerde der/des'. Captures the full name including any title (e.g., OSR, Prof.in). Strictly stops at comma to avoid capturing addresses.", 'format': 'regex', 'content': "(?:in\\s+der\\s+Beschwerdesache\\s+(?:des\\s+|der\\s+)?|Beschwerde\\s+der\\s+|Beschwerde\\s+des\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)*(?:\\s+(?:di|van|von|del|de|la|le|da|d'|d\\s+)[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)*(?:\\s+(?:Dr\\.|Mag\\.|Mag\\.a|Hon\\.-Prof\\.|Hon\\.-Prof\\.in|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|KzlR|KommR|Ing\\.|RgR|PhD|LL\\.M|LL\\.B|Bakk\\.\\s+iur|BA|\\u00d6kR|Dipl\\.-Ing\\.|Richter|Richterin|Ri\\s|IBV|M\\.?|R\\.?|Prof\\.|St\\.?B\\.?|Stb\\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\\.-Doz\\.|DDr\\.|Dr\\.in|Dr\\.in\\s+Dr\\.in|Univ\\.-Prof\\.in|Priv\\.-Doz\\.in|Techn\\s+R|Techn\\.\\s+R|KommR\\s+VetR|VetR\\s+KommR)\\s+)?([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?:\\s*,\\s*(?:LL\\.M|LL\\.B|MSc|BEd|PhD|Dr\\.in|Mag\\.a|OMedR|MedR|Priv\\.-Doz\\.|Univ\\.-Prof\\.)?)?)\\s*(?=,|\\.|\\)|\\s|$)", 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '65de81ba', 'name': 'extract_german_legal_person_frau_herr', 'description': "Extracts full names following 'Frau' or 'Herr'. Captures first and last name, and optional suffixes. Stops at non-name words.", 'format': 'regex', 'content': '\\b(?:Frau(?:n)?\\s+|Herr(?:n|s)?\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)*(?:\\s*,\\s*(?:LL\\.M|LL\\.B|MSc|BEd|PhD|Dr\\.in|Mag\\.a|OMedR|MedR|Priv\\.-Doz\\.|Univ\\.-Prof\\.)?)?)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'cb54a318', 'name': 'extract_german_legal_person_kinship', 'description': "Extracts person names following kinship terms like 'Gattin' (wife) or 'Ehemann' (husband).", 'format': 'regex', 'content': "(?:Gattin|Ehemann|Sohn|Tochter|Vater|Mutter)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+(?:di|van|von|del|de|la|le|da|d'|d\\s+)[A-Z][a-zäöüß]+)+)(?=,|\\.|\\)|\\s|$)", 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '6b50df2b', 'name': 'extract_german_legal_person_role_context', 'description': "Extracts person names following specific legal roles like 'durch den Richter' or 'durch die Richterin'. Requires full name (first + last) to avoid partial title matches.", 'format': 'regex', 'content': '(?:durch\\s+(?:den\\s+|die\\s+)?(?:Richter|Richterin)\\s+)([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)+)(?:\\s+(?:LL\\.M|LL\\.B|MSc|BEd|PhD|Dr\\.in|Mag\\.a|OMedR|MedR|Priv\\.-Doz\\.|Univ\\.-Prof\\.)?)?', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'd18d5c6d', 'name': 'extract_german_legal_person_title_complex', 'description': 'Extracts person names with titles. Captures the full title sequence and name. Handles multiple titles (e.g., Univ.-Prof. Dr. Priv.-Doz.) and stops before commas or addresses.', 'format': 'regex', 'content': '\\b(?:Dr\\.|Mag\\.|Mag\\.a|Hon\\.-Prof\\.|Hon\\.-Prof\\.in|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|KzlR|KommR|Ing\\.|RgR|PhD|LL\\.M|LL\\.B|Bakk\\.\\s+iur|BA|\\u00d6kR|Dipl\\.-Ing\\.|Richter|Richterin|Ri\\s|IBV|M\\.?|R\\.?|Prof\\.|St\\.?B\\.?|Stb\\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\\.-Doz\\.|DDr\\.|Dr\\.in|Dr\\.in\\s+Dr\\.in|Univ\\.-Prof\\.in|Priv\\.-Doz\\.in|Techn\\s+R|Techn\\.\\s+R|KommR\\s+VetR|VetR\\s+KommR)(?:\\s+(?:Dr\\.|Mag\\.|Mag\\.a|Hon\\.-Prof\\.|Hon\\.-Prof\\.in|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|KzlR|KommR|Ing\\.|RgR|PhD|LL\\.M|LL\\.B|Bakk\\.\\s+iur|BA|\\u00d6kR|Dipl\\.-Ing\\.|Richter|Richterin|Ri\\s|IBV|M\\.?|R\\.?|Prof\\.|St\\.?B\\.?|Stb\\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\\.-Doz\\.|DDr\\.|Dr\\.in|Dr\\.in\\s+Dr\\.in|Univ\\.-Prof\\.in|Priv\\.-Doz\\.in|Techn\\s+R|Techn\\.\\s+R|KommR\\s+VetR|VetR\\s+KommR))*\\s+([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'f99b13f6', 'name': 'extract_german_legal_person_context', 'description': "Extracts person names following specific legal context markers. Excludes organization prefixes and 'Herr/Frau' from the capture. Handles 'bei der/den' context.", 'format': 'regex', 'content': '(?:von\\s+|gegen\\s+|in\\s+der\\s+Beschwerdesache\\s+(?:des\\s+|der\\s+)?|Beschwerde\\s+der\\s+|Beschwerde\\s+des\\s+|des\\s+Bf\\.|dem\\s+(?:Bf\\.|Bf\\.in)?|an\\s+Herrn\\s+|an\\s+Frau\\s+|des\\s+Beschwerdeführers\\s+|der\\s+Beschwerdeführerin\\s+|des\\s+Beschuldigten\\s+|der\\s+Beschuldigten\\s+|erhoben\\s+von\\s+|eingebracht\\s+von\\s+|im\\s+Zuge\\s+der\\s+|in\\s+der\\s+Revisionssache\\s+|in\\s+der\\s+Rechtssache\\s+|bei\\s+der\\s+|bei\\s+den\\s+|zur\\s+|durch\\s+die\\s+|durch\\s+den\\s+)(?:(?:Herr\\s+|Frau\\s+)?)(?!Verein\\s+|Klub\\s+|GmbH\\s+|AG\\s+|KG\\s+|mbH\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '11edda00', 'name': 'extract_german_legal_person_generic', 'description': "Extracts person names in generic legal contexts where no title is present, such as after 'Versicherungsnehmer' or 'Bf'.", 'format': 'regex', 'content': '(?:Versicherungsnehmer\\s+|Bf\\.\\s+|Bf\\.in\\s+|des\\s+Beschwerdeführers\\s+|der\\s+Beschwerdeführerin\\s+)([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)+)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '38a57ea3', 'name': 'extract_german_legal_person_prof_in', 'description': "Extracts person names starting with 'Prof.in' or 'Univ.-Prof.in'. Captures the full title and name.", 'format': 'regex', 'content': '\\b(?:Univ\\.-Prof\\.in|Prof\\.in)\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '5c6770d4', 'name': 'extract_german_legal_person_generic_no_context', 'description': "Extracts standalone person names (First Last) that appear in specific contexts like parentheses or after 'bei der' without titles, to catch cases like 'Hugo Buring'.", 'format': 'regex', 'content': '(?:\\(|bei\\s+der\\s+|bei\\s+den\\s+|und\\s+)([A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?:\\)|,|\\s|$)', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 94.5% |
| True Positives | 20 |
| False Positives | 33 |
| False Negatives | 70 |
| Total Gold Entities | 90 |
| Micro Precision | 37.7% |
| Micro Recall | 22.2% |
| Micro F1 | 28.0% |
| Macro F1 | 28.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `extract_german_legal_person_context` | 19.0% | 42.3% | 12.2% | 26 | 11 | 15 |
| `extract_german_legal_person_frau_herr` | 8.0% | 40.0% | 4.4% | 10 | 4 | 6 |
| `extract_german_legal_person_generic_no_context` | 9.4% | 31.2% | 5.6% | 16 | 5 | 11 |
| `extract_german_legal_person_title_complex` | 1.9% | 7.1% | 1.1% | 14 | 1 | 13 |
| `extract_german_legal_person_mandantin` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `extract_german_legal_person_nachname_wie_bf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `extract_german_legal_person_children_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `extract_german_legal_person_direct_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `extract_german_legal_person_kinship` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `extract_german_legal_person_role_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `extract_german_legal_person_generic` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `extract_german_legal_person_prof_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `extract_german_legal_person_context`

**F1:** 0.190 | **Precision:** 0.423 | **Recall:** 0.122  

**Format:** `regex`  
**Rule ID:** `f99b13f6`  
**Description:**
Extracts person names following specific legal context markers. Excludes organization prefixes and 'Herr/Frau' from the capture. Handles 'bei der/den' context.

**Content:**
```
(?:von\s+|gegen\s+|in\s+der\s+Beschwerdesache\s+(?:des\s+|der\s+)?|Beschwerde\s+der\s+|Beschwerde\s+des\s+|des\s+Bf\.|dem\s+(?:Bf\.|Bf\.in)?|an\s+Herrn\s+|an\s+Frau\s+|des\s+Beschwerdeführers\s+|der\s+Beschwerdeführerin\s+|des\s+Beschuldigten\s+|der\s+Beschuldigten\s+|erhoben\s+von\s+|eingebracht\s+von\s+|im\s+Zuge\s+der\s+|in\s+der\s+Revisionssache\s+|in\s+der\s+Rechtssache\s+|bei\s+der\s+|bei\s+den\s+|zur\s+|durch\s+die\s+|durch\s+den\s+)(?:(?:Herr\s+|Frau\s+)?)(?!Verein\s+|Klub\s+|GmbH\s+|AG\s+|KG\s+|mbH\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.122 | 0.190 | 26 | 11 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 15 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Frauke Stuhldreher` | `Frauke Stuhldreher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Patricia Jentz` | `Patricia Jentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Mathilda Eckholdt` | `Mathilda Eckholdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr` — positional overlap with gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Bezirksgericht Purkersdorf` — type mismatch — same span as gold: `Bezirksgericht Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `extract_german_legal_person_generic_no_context`

**F1:** 0.094 | **Precision:** 0.312 | **Recall:** 0.056  

**Format:** `regex`  
**Rule ID:** `5c6770d4`  
**Description:**
Extracts standalone person names (First Last) that appear in specific contexts like parentheses or after 'bei der' without titles, to catch cases like 'Hugo Buring'.

**Content:**
```
(?:\(|bei\s+der\s+|bei\s+den\s+|und\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\)|,|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.312 | 0.056 | 0.094 | 16 | 5 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 11 | 82 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `5966 230804` (social_security_number)
- `4740150943` (social_security_number)
- `RgR HR Reneé Schrammek` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `5966 230804` (social_security_number)
- `4740150943` (social_security_number)
- `RgR HR Reneé Schrammek` (person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_52`)


Davor wurde die  Familienbeihilfe schon mit 01/2021 eingestellt, da lt. Studiendatenübermittlungsauskunft das  Studium nur bis 14.12.2020 betrieben wurde und Viktoria Immohr  mit 01.01.2021 eine  Teilzeitbeschäftigung begann.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`
- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Bachelorstudium Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `extract_german_legal_person_title_complex`

**F1:** 0.019 | **Precision:** 0.071 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `d18d5c6d`  
**Description:**
Extracts person names with titles. Captures the full title sequence and name. Handles multiple titles (e.g., Univ.-Prof. Dr. Priv.-Doz.) and stops before commas or addresses.

**Content:**
```
\b(?:Dr\.|Mag\.|Mag\.a|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|KzlR|KommR|Ing\.|RgR|PhD|LL\.M|LL\.B|Bakk\.\s+iur|BA|\u00d6kR|Dipl\.-Ing\.|Richter|Richterin|Ri\s|IBV|M\.?|R\.?|Prof\.|St\.?B\.?|Stb\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\.-Doz\.|DDr\.|Dr\.in|Dr\.in\s+Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Techn\s+R|Techn\.\s+R|KommR\s+VetR|VetR\s+KommR)(?:\s+(?:Dr\.|Mag\.|Mag\.a|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|KzlR|KommR|Ing\.|RgR|PhD|LL\.M|LL\.B|Bakk\.\s+iur|BA|\u00d6kR|Dipl\.-Ing\.|Richter|Richterin|Ri\s|IBV|M\.?|R\.?|Prof\.|St\.?B\.?|Stb\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\.-Doz\.|DDr\.|Dr\.in|Dr\.in\s+Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Techn\s+R|Techn\.\s+R|KommR\s+VetR|VetR\s+KommR))*\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.071 | 0.011 | 0.019 | 14 | 1 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 13 | 89 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in OStR Tosca Knoller` | `Hon.-Prof.in OStR Tosca Knoller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Estelle Niederholz` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv.-Doz. Hon.-Prof. Gotthard Clement` — partial — gold is substring of pred: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr. Siegfried Fenz` — partial — gold is substring of pred: `Dr. Siegfried Fenz`
- `Dr. Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Richter Mag. Ashley Partenfelder` — partial — gold is substring of pred: `Mag. Ashley Partenfelder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Richterin Priv.-Doz.in Farina Kohlstrunk` — partial — gold is substring of pred: `Priv.-Doz.in Farina Kohlstrunk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Farina Kohlstrunk`(person)
- `Mathilda Eckholdt`(person)
- `Kleingassen 3, 4150 Reith, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`(address)
- `Bundesfinanzgericht`(organisation)
- `Finanzamt Österreich`(organisation)
- `69-575/0475`(tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Richter Priv.-Doz. Quirin Januszis` — partial — gold is substring of pred: `Priv.-Doz. Quirin Januszis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

</details>

---

## `extract_german_legal_person_frau_herr`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `65de81ba`  
**Description:**
Extracts full names following 'Frau' or 'Herr'. Captures first and last name, and optional suffixes. Stops at non-name words.

**Content:**
```
\b(?:Frau(?:n)?\s+|Herr(?:n|s)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:LL\.M|LL\.B|MSc|BEd|PhD|Dr\.in|Mag\.a|OMedR|MedR|Priv\.-Doz\.|Univ\.-Prof\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.044 | 0.080 | 10 | 4 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 6 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_53`)


Zwischen dem Bf. und Frau Delia Moebes  besteht unstrittig eine aufrechte eheliche  Gemeinschaft (vgl. Protokoll zur Verhandlung vom 1. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_93`)


Nach den unstrittigen Sachverhaltsfeststellungen besteht zwischen dem Bf. und Frau  Delia Moebes  eine aufrechte eheliche Gemeinschaft, wobei den Bf. gegenüber seiner Ehefrau  keine Unterhaltspflicht trifft.

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `extract_german_legal_person_mandantin`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ec6abf56`  
**Description:**
Extracts person names following 'Mandantin, Frau' or 'Mandant, Herr' patterns common in legal letters.

**Content:**
```
(?:Mandantin,\s+Frau\s+|Mandant,\s+Herr\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_nachname_wie_bf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `76006b7f`  
**Description:**
Extracts person names following the specific legal context marker '(Nachname wie Bf.)'. This handles cases where the name is explicitly listed after this marker.

**Content:**
```
\(Nachname\s+wie\s+Bf\.\)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_children_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f0f54feb`  
**Description:**
Extracts person names following 'für die Kinder' or 'Kinder' in a list context, capturing the full name without assuming a title.

**Content:**
```
(?:für\s+die\s+Kinder\s+|Kinder\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:,\s*(?:geboren|und|und\s+|\))?)?)(?=\s|,|\(|\)|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_direct_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `44fe6684`  
**Description:**
Extracts person names directly following 'in der Beschwerdesache' or 'Beschwerde der/des'. Captures the full name including any title (e.g., OSR, Prof.in). Strictly stops at comma to avoid capturing addresses.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+(?:des\s+|der\s+)?|Beschwerde\s+der\s+|Beschwerde\s+des\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:di|van|von|del|de|la|le|da|d'|d\s+)[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:Dr\.|Mag\.|Mag\.a|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|KzlR|KommR|Ing\.|RgR|PhD|LL\.M|LL\.B|Bakk\.\s+iur|BA|\u00d6kR|Dipl\.-Ing\.|Richter|Richterin|Ri\s|IBV|M\.?|R\.?|Prof\.|St\.?B\.?|Stb\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\.-Doz\.|DDr\.|Dr\.in|Dr\.in\s+Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Techn\s+R|Techn\.\s+R|KommR\s+VetR|VetR\s+KommR)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:LL\.M|LL\.B|MSc|BEd|PhD|Dr\.in|Mag\.a|OMedR|MedR|Priv\.-Doz\.|Univ\.-Prof\.)?)?)\s*(?=,|\.|\)|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_kinship`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cb54a318`  
**Description:**
Extracts person names following kinship terms like 'Gattin' (wife) or 'Ehemann' (husband).

**Content:**
```
(?:Gattin|Ehemann|Sohn|Tochter|Vater|Mutter)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:di|van|von|del|de|la|le|da|d'|d\s+)[A-Z][a-zäöüß]+)+)(?=,|\.|\)|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_role_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6b50df2b`  
**Description:**
Extracts person names following specific legal roles like 'durch den Richter' or 'durch die Richterin'. Requires full name (first + last) to avoid partial title matches.

**Content:**
```
(?:durch\s+(?:den\s+|die\s+)?(?:Richter|Richterin)\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+(?:LL\.M|LL\.B|MSc|BEd|PhD|Dr\.in|Mag\.a|OMedR|MedR|Priv\.-Doz\.|Univ\.-Prof\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_prof_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `38a57ea3`  
**Description:**
Extracts person names starting with 'Prof.in' or 'Univ.-Prof.in'. Captures the full title and name.

**Content:**
```
\b(?:Univ\.-Prof\.in|Prof\.in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+
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

## `extract_german_legal_person_context`

**F1:** 0.190 | **Precision:** 0.423 | **Recall:** 0.122  

**Format:** `regex`  
**Rule ID:** `f99b13f6`  
**Description:**
Extracts person names following specific legal context markers. Excludes organization prefixes and 'Herr/Frau' from the capture. Handles 'bei der/den' context.

**Content:**
```
(?:von\s+|gegen\s+|in\s+der\s+Beschwerdesache\s+(?:des\s+|der\s+)?|Beschwerde\s+der\s+|Beschwerde\s+des\s+|des\s+Bf\.|dem\s+(?:Bf\.|Bf\.in)?|an\s+Herrn\s+|an\s+Frau\s+|des\s+Beschwerdeführers\s+|der\s+Beschwerdeführerin\s+|des\s+Beschuldigten\s+|der\s+Beschuldigten\s+|erhoben\s+von\s+|eingebracht\s+von\s+|im\s+Zuge\s+der\s+|in\s+der\s+Revisionssache\s+|in\s+der\s+Rechtssache\s+|bei\s+der\s+|bei\s+den\s+|zur\s+|durch\s+die\s+|durch\s+den\s+)(?:(?:Herr\s+|Frau\s+)?)(?!Verein\s+|Klub\s+|GmbH\s+|AG\s+|KG\s+|mbH\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.423 | 0.122 | 0.190 | 26 | 11 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 15 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Frauke Stuhldreher` | `Frauke Stuhldreher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Patricia Jentz` | `Patricia Jentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Mathilda Eckholdt` | `Mathilda Eckholdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Wilhelm Konetzny` | `Wilhelm Konetzny` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Alma Springel` | `Alma Springel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Oleg Dell` | `Oleg Dell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `80-738/9953` (tax_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Ludger Weynand` | `Ludger Weynand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr` — positional overlap with gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Bezirksgericht Purkersdorf` — type mismatch — same span as gold: `Bezirksgericht Purkersdorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Richter Mag` — positional overlap with gold: `Mag. Ashley Partenfelder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Richterin Priv` — positional overlap with gold: `Priv.-Doz.in Farina Kohlstrunk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Farina Kohlstrunk`(person)
- `Mathilda Eckholdt`(person)
- `Kleingassen 3, 4150 Reith, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`(address)
- `Bundesfinanzgericht`(organisation)
- `Finanzamt Österreich`(organisation)
- `69-575/0475`(tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Quirin Januszis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Richterin Mag` — positional overlap with gold: `Mag. Gabriele Friedbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Richterin Priv` — positional overlap with gold: `Priv.-Doz.in Juliana Bartjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richterin Dr` — positional overlap with gold: `Dr.in Estelle Niederholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Richter Hon` — positional overlap with gold: `Hon.-Prof. Thassilo Averdiek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richterin Mag` — positional overlap with gold: `Mag.Dr. Katrin Allram`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr` — positional overlap with gold: `Dr. Dagobert Nordholt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Richter Mag` — positional overlap with gold: `Mag. Peter Bilger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `Ludger Weynand`(person)
- `Plestätten 139Y, 4923 Reintal, Österreich`(address)
- `27-924/8149`(tax_number)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `extract_german_legal_person_generic_no_context`

**F1:** 0.094 | **Precision:** 0.312 | **Recall:** 0.056  

**Format:** `regex`  
**Rule ID:** `5c6770d4`  
**Description:**
Extracts standalone person names (First Last) that appear in specific contexts like parentheses or after 'bei der' without titles, to catch cases like 'Hugo Buring'.

**Content:**
```
(?:\(|bei\s+der\s+|bei\s+den\s+|und\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\)|,|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.312 | 0.056 | 0.094 | 16 | 5 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 11 | 82 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `5966 230804` (social_security_number)
- `4740150943` (social_security_number)
- `RgR HR Reneé Schrammek` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `5966 230804` (social_security_number)
- `4740150943` (social_security_number)
- `RgR HR Reneé Schrammek` (person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_52`)


Davor wurde die  Familienbeihilfe schon mit 01/2021 eingestellt, da lt. Studiendatenübermittlungsauskunft das  Studium nur bis 14.12.2020 betrieben wurde und Viktoria Immohr  mit 01.01.2021 eine  Teilzeitbeschäftigung begann.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`
- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Bachelorstudium Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Nach Abschluss der Betriebsprüfung (BP-Bericht vom 13.5.2024) erging (erstmalig) der  Einkommensteuerbescheid 2021 am 22.5.2024.

**False Positives:**

- `Sachverhalt  Nach Abschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_47`)


Da der Einkommensteuerbescheid aufgrund der Beschwerde des Bf mit  Beschwerdevorentscheidung vom 12.03.2025 abgeändert wurde (zugunsten des Bf) erging am  12.03.2025 der neue (bzw. weitere) Bescheid über die Festsetzung von Anspruchszinsen 2021, in  dem diesem Umstand Rechnung getragen wurde (Gutschrift Anspruchszinsen in der Höhe von  Euro 7.963,60).

**False Positives:**

- `Gutschrift Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_84`)


Festgehalten wird, dass die vom Vertreter des Bf. genannte Beschwerdevorentscheidung vom  11.3.2025 nicht die Einkommensteuer für das Jahr 2021, sondern die Einkommensteuer für das  Jahr 2020 betrifft (Die Beschwerde gegen den Einkommensteuerbescheid 2020 wurde dem  BFG zur Entscheidung vorgelegt, die noch unerledigt ist, RV/5100771/2025).

**False Positives:**

- `Die Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_53`)


Zwischen dem Bf. und Frau Delia Moebes  besteht unstrittig eine aufrechte eheliche  Gemeinschaft (vgl. Protokoll zur Verhandlung vom 1. Oktober 2025).

**False Positives:**

- `Frau Delia Moebes` — partial — gold is substring of pred: `Delia Moebes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Delia Moebes`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_93`)


Nach den unstrittigen Sachverhaltsfeststellungen besteht zwischen dem Bf. und Frau  Delia Moebes  eine aufrechte eheliche Gemeinschaft, wobei den Bf. gegenüber seiner Ehefrau  keine Unterhaltspflicht trifft.

**False Positives:**

- `Frau  Delia Moebes` — partial — gold is substring of pred: `Delia Moebes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Delia Moebes`(person)

</details>

---

## `extract_german_legal_person_frau_herr`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `65de81ba`  
**Description:**
Extracts full names following 'Frau' or 'Herr'. Captures first and last name, and optional suffixes. Stops at non-name words.

**Content:**
```
\b(?:Frau(?:n)?\s+|Herr(?:n|s)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:LL\.M|LL\.B|MSc|BEd|PhD|Dr\.in|Mag\.a|OMedR|MedR|Priv\.-Doz\.|Univ\.-Prof\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.044 | 0.080 | 10 | 4 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 6 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_53`)


Zwischen dem Bf. und Frau Delia Moebes  besteht unstrittig eine aufrechte eheliche  Gemeinschaft (vgl. Protokoll zur Verhandlung vom 1. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_93`)


Nach den unstrittigen Sachverhaltsfeststellungen besteht zwischen dem Bf. und Frau  Delia Moebes  eine aufrechte eheliche Gemeinschaft, wobei den Bf. gegenüber seiner Ehefrau  keine Unterhaltspflicht trifft.

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `extract_german_legal_person_title_complex`

**F1:** 0.019 | **Precision:** 0.071 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `d18d5c6d`  
**Description:**
Extracts person names with titles. Captures the full title sequence and name. Handles multiple titles (e.g., Univ.-Prof. Dr. Priv.-Doz.) and stops before commas or addresses.

**Content:**
```
\b(?:Dr\.|Mag\.|Mag\.a|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|KzlR|KommR|Ing\.|RgR|PhD|LL\.M|LL\.B|Bakk\.\s+iur|BA|\u00d6kR|Dipl\.-Ing\.|Richter|Richterin|Ri\s|IBV|M\.?|R\.?|Prof\.|St\.?B\.?|Stb\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\.-Doz\.|DDr\.|Dr\.in|Dr\.in\s+Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Techn\s+R|Techn\.\s+R|KommR\s+VetR|VetR\s+KommR)(?:\s+(?:Dr\.|Mag\.|Mag\.a|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|KzlR|KommR|Ing\.|RgR|PhD|LL\.M|LL\.B|Bakk\.\s+iur|BA|\u00d6kR|Dipl\.-Ing\.|Richter|Richterin|Ri\s|IBV|M\.?|R\.?|Prof\.|St\.?B\.?|Stb\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\.-Doz\.|DDr\.|Dr\.in|Dr\.in\s+Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Techn\s+R|Techn\.\s+R|KommR\s+VetR|VetR\s+KommR))*\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.071 | 0.011 | 0.019 | 14 | 1 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 13 | 89 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in OStR Tosca Knoller` | `Hon.-Prof.in OStR Tosca Knoller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Estelle Niederholz` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv.-Doz. Hon.-Prof. Gotthard Clement` — partial — gold is substring of pred: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr. Siegfried Fenz` — partial — gold is substring of pred: `Dr. Siegfried Fenz`
- `Dr. Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Richter Mag. Ashley Partenfelder` — partial — gold is substring of pred: `Mag. Ashley Partenfelder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Richterin Priv.-Doz.in Farina Kohlstrunk` — partial — gold is substring of pred: `Priv.-Doz.in Farina Kohlstrunk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Farina Kohlstrunk`(person)
- `Mathilda Eckholdt`(person)
- `Kleingassen 3, 4150 Reith, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`(address)
- `Bundesfinanzgericht`(organisation)
- `Finanzamt Österreich`(organisation)
- `69-575/0475`(tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Richter Priv.-Doz. Quirin Januszis` — partial — gold is substring of pred: `Priv.-Doz. Quirin Januszis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Richterin Mag. Gabriele Friedbacher` — partial — gold is substring of pred: `Mag. Gabriele Friedbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Richterin Priv.-Doz.in Juliana Bartjen` — partial — gold is substring of pred: `Priv.-Doz.in Juliana Bartjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richterin Dr.in Estelle Niederholz` — partial — gold is substring of pred: `Dr.in Estelle Niederholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Richter Hon.-Prof. Thassilo Averdiek` — partial — gold is substring of pred: `Hon.-Prof. Thassilo Averdiek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr. Dagobert Nordholt` — partial — gold is substring of pred: `Dr. Dagobert Nordholt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Richter Mag. Peter Bilger` — partial — gold is substring of pred: `Mag. Peter Bilger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `Ludger Weynand`(person)
- `Plestätten 139Y, 4923 Reintal, Österreich`(address)
- `27-924/8149`(tax_number)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `extract_german_legal_person_mandantin`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ec6abf56`  
**Description:**
Extracts person names following 'Mandantin, Frau' or 'Mandant, Herr' patterns common in legal letters.

**Content:**
```
(?:Mandantin,\s+Frau\s+|Mandant,\s+Herr\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_nachname_wie_bf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `76006b7f`  
**Description:**
Extracts person names following the specific legal context marker '(Nachname wie Bf.)'. This handles cases where the name is explicitly listed after this marker.

**Content:**
```
\(Nachname\s+wie\s+Bf\.\)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_children_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f0f54feb`  
**Description:**
Extracts person names following 'für die Kinder' or 'Kinder' in a list context, capturing the full name without assuming a title.

**Content:**
```
(?:für\s+die\s+Kinder\s+|Kinder\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:,\s*(?:geboren|und|und\s+|\))?)?)(?=\s|,|\(|\)|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_direct_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `44fe6684`  
**Description:**
Extracts person names directly following 'in der Beschwerdesache' or 'Beschwerde der/des'. Captures the full name including any title (e.g., OSR, Prof.in). Strictly stops at comma to avoid capturing addresses.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+(?:des\s+|der\s+)?|Beschwerde\s+der\s+|Beschwerde\s+des\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:di|van|von|del|de|la|le|da|d'|d\s+)[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:Dr\.|Mag\.|Mag\.a|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|KzlR|KommR|Ing\.|RgR|PhD|LL\.M|LL\.B|Bakk\.\s+iur|BA|\u00d6kR|Dipl\.-Ing\.|Richter|Richterin|Ri\s|IBV|M\.?|R\.?|Prof\.|St\.?B\.?|Stb\.|VetR|OSR|EURAX|OStR|HR|OMedR|MedR|Priv\.-Doz\.|DDr\.|Dr\.in|Dr\.in\s+Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Techn\s+R|Techn\.\s+R|KommR\s+VetR|VetR\s+KommR)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:LL\.M|LL\.B|MSc|BEd|PhD|Dr\.in|Mag\.a|OMedR|MedR|Priv\.-Doz\.|Univ\.-Prof\.)?)?)\s*(?=,|\.|\)|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_kinship`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cb54a318`  
**Description:**
Extracts person names following kinship terms like 'Gattin' (wife) or 'Ehemann' (husband).

**Content:**
```
(?:Gattin|Ehemann|Sohn|Tochter|Vater|Mutter)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:di|van|von|del|de|la|le|da|d'|d\s+)[A-Z][a-zäöüß]+)+)(?=,|\.|\)|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_role_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6b50df2b`  
**Description:**
Extracts person names following specific legal roles like 'durch den Richter' or 'durch die Richterin'. Requires full name (first + last) to avoid partial title matches.

**Content:**
```
(?:durch\s+(?:den\s+|die\s+)?(?:Richter|Richterin)\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s+(?:LL\.M|LL\.B|MSc|BEd|PhD|Dr\.in|Mag\.a|OMedR|MedR|Priv\.-Doz\.|Univ\.-Prof\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `extract_german_legal_person_generic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `11edda00`  
**Description:**
Extracts person names in generic legal contexts where no title is present, such as after 'Versicherungsnehmer' or 'Bf'.

**Content:**
```
(?:Versicherungsnehmer\s+|Bf\.\s+|Bf\.in\s+|des\s+Beschwerdeführers\s+|der\s+Beschwerdeführerin\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 51 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `extract_german_legal_person_prof_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `38a57ea3`  
**Description:**
Extracts person names starting with 'Prof.in' or 'Univ.-Prof.in'. Captures the full title and name.

**Content:**
```
\b(?:Univ\.-Prof\.in|Prof\.in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+
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

