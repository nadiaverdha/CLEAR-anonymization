# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-28T10:23:07.770469

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-28/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2549 |
| Validation documents | 639 |
| Test documents | 91453 |
| Train sentences | 4081 |
| Validation sentences | 1192 |
| Test sentences | 91453 |
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
| Seeded From | findok |
| Seed Rule Count | 6 |
| New Rules Added | 4 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 3896 |
| Phase1 Eval Sentences | 1147 |
| Transfer Train Sentences | 185 |
| Transfer Eval Sentences | 45 |
| Best Batch Idx | 0 |
| Best Batch F1 | 0.24195121951219514 |
| Best Rules Serialized | [{'id': 'dc682d4a', 'name': 'Judge_Richter', 'description': 'Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles, ensuring no trailing whitespace and excluding single-letter abbreviations.', 'format': 'regex', 'content': '(?:durch\\s+(?:den\\s+)?(?:Richter|Richterin|Vorsitzende)\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|Dr\\.\\s+Univ\\.-Prof\\.in?|Univ\\.-Prof\\.in?|Priv\\.-Doz\\.in?|Hon\\.-Prof\\.in?)?)?)(?=\\s+(?:in der|\\u00fcber die|in der Verwaltungsstrafsache|\\(|,|$))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'af12a153', 'name': 'Party_Beschwerdesache', 'description': "Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.", 'format': 'regex', 'content': '(?:in der\\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\\s+(?:der\\s+|des\\s+)?)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.)?)?)(?=,\\s+[A-Z]|\\s+vertreten|\\s+\\(|\\s+\\)|$|\\s+\\d{4}\\s+\\w+|\\s+Gattin|\\s+und\\s+der)', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'aca7d129', 'name': 'Representative_vertreten_durch', 'description': "Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.", 'format': 'regex', 'content': '(?:vertreten\\s+durch\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|DDr\\.|R\\.in?|R\\.)?)?)(?=,\\s+[A-Z]|\\s+GmbH|\\s+Steuerberatung|\\s+OG|\\s+KG|\\s+Rechtsanwalts|\\s+PartG|\\s+StbG|\\s+\\(|$)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'b07361b5', 'name': 'Frau_Name', 'description': "Captures full names following 'Frau'.", 'format': 'regex', 'content': '(?:Frau|Frauen)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d))', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '98f92f79', 'name': 'Herr_Name_Corrected', 'description': "Captures full names following 'Herr' or 'Herrn', ensuring it matches a name (not a title) and handles German characters.", 'format': 'regex', 'content': '(?:Herr|Herrn)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d))', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '94942c84', 'name': 'Name_Herrn', 'description': "Captures full names following 'Herrn' (accusative/dative), ensuring the full name including suffixes is extracted.", 'format': 'regex', 'content': '(?:Herrn|Herr)\\s+([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.)?)?)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d|Gattin|und))', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '789ef8cf', 'name': 'Name_Gegen', 'description': "Captures names following 'gegen' (against) in legal proceedings.", 'format': 'regex', 'content': '(?:gegen\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.)?)?)(?=,\\s+[A-Z]|\\s+\\(|$|\\s+\\d{4}|\\s+Gattin|\\s+und)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4031b52e', 'name': 'Name_Von', 'description': "Captures names following 'von' (of/from) in contexts like 'Gutachten von'.", 'format': 'regex', 'content': '(?:von\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.)?)?)(?=,\\s+[A-Z]|\\s+\\(|$|\\s+\\d{4}|\\s+Gattin|\\s+und|\\s+Vermietung|\\s+Zimmer)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '90e1f5a6', 'name': 'Name_Representative', 'description': "Captures names following 'vertreten durch' (represented by).", 'format': 'regex', 'content': '(?:vertreten\\s+durch\\s+)([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)*(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.)?)?)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '6a54d072', 'name': 'Name_Bei', 'description': "Captures names following 'bei' (at/with) in contexts like 'bei der Hugo Buring'.", 'format': 'regex', 'content': '(?:bei\\s+(?:der|die|den)\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.)?)?)(?=,\\s+[A-Z]|\\s+\\(|$|\\s+\\d{4}|\\s+Gattin|\\s+und)', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 96.4% |
| True Positives | 620 |
| False Positives | 2867 |
| False Negatives | 1018 |
| Total Gold Entities | 1638 |
| Micro Precision | 17.8% |
| Micro Recall | 37.9% |
| Micro F1 | 24.2% |
| Macro F1 | 24.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Herr_Name_Corrected` | 1.2% | 100.0% | 0.6% | 10 | 10 | 0 |
| `Party_Beschwerdesache` | 39.8% | 86.2% | 25.9% | 492 | 424 | 68 |
| `Frau_Name` | 0.5% | 80.0% | 0.2% | 5 | 4 | 1 |
| `Judge_Richter` | 15.7% | 70.0% | 8.9% | 207 | 145 | 62 |
| `Name_Gegen` | 2.6% | 28.2% | 1.3% | 78 | 22 | 56 |
| `Name_Herrn` | 1.0% | 6.0% | 0.5% | 150 | 9 | 141 |
| `Representative_vertreten_durch` | 0.8% | 5.2% | 0.4% | 134 | 7 | 127 |
| `Name_Representative` | 1.2% | 3.9% | 0.7% | 304 | 12 | 292 |
| `Name_Bei` | 0.1% | 0.2% | 0.1% | 447 | 1 | 446 |
| `Name_Von` | 0.1% | 0.1% | 0.1% | 1846 | 2 | 1844 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Herr_Name_Corrected`

**F1:** 0.012 | **Precision:** 1.000 | **Recall:** 0.006  

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
| 1.000 | 0.006 | 0.012 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 0 | 1315 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Stanislaus Calisir (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Cynthia Neureuter  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Natascha Daschmann (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_8`)


Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der  Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische  Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur  Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit  1 von 20 Seite 2 von 20

| Predicted | Gold |
|---|---|
| `Brunhild Hoffschulz` | `Brunhild Hoffschulz` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/141435.1`) (sent_id: `deanon_BFG_TRAIN/141435.1_4`)


Begründung  Verfahrensgang:  MA67/226701281451/2022:  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner  2023, Zahl: MA67/226701281451/2022, wurde Herr Robert Grentzmann (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von einem 14 Stunden verhängt sowie ein  Verfahrenskostenbeitrag von € 10,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Robert Grentzmann` | `Robert Grentzmann` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/142976.1`) (sent_id: `deanon_BFG_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Nikolaus Thulke (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Nikolaus Thulke` | `Nikolaus Thulke` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_6`)


Entscheidungsgründe  Mit Straferkenntnis vom 16. April 2024, Zahl: MA67/246700162299/2024, hat der Magistrat  der Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Leonhard Facci (in weiterer  Folge: Beschwerdeführer – Bf) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt  indem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen I-57 VS  am  2. Februar 2024 um 09:20 Uhr in einer gebührenpflichtigen Kurzparkzone in 1210 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `I-57 VS` (vehicle_license)

**Example 7** (doc_id: `deanon_BFG_TRAIN/146476.1`) (sent_id: `deanon_BFG_TRAIN/146476.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Herr MedR Florentine Wägemann (in der Folge kurz: Bf.) brachte am 19.2.2024 den Antrag auf  Arbeitnehmerveranlagung für das Jahr 2023 per Finanzonline ein.

| Predicted | Gold |
|---|---|
| `MedR Florentine Wägemann` | `MedR Florentine Wägemann` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/147143.1`) (sent_id: `deanon_BFG_TRAIN/147143.1_5`)


Im Zuge einer Anhaltung durch die Finanzpolizei am 10.7.2015, 22:55 Uhr, in A-Ort1,XStr, hat  der Lenker des Fahrzeuges VW Touareg mit dem ausländischen Kennzeichen XX1, FIN Nr123,  Herr Kirstin Lünebach (= Beschwerdeführer, Bf) angegeben, dass Zulassungsbesitzerin des Fahrzeuges  die Fa. A-GmbH in D-Ort2 ist und er sich auf der Fahrt nach Hause befindet.

| Predicted | Gold |
|---|---|
| `Kirstin Lünebach` | `Kirstin Lünebach` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Einkommensteuerbescheid (Arbeitnehmerveranlagung) vom 1. März 2024 wurde die  Einkommensteuer von Herrn Bernhard Siegmundt (im Folgenden auch Beschwerdeführer oder Bf.) für das  Jahr 2023 mit einer Gutschrift in Höhe von EUR 29,- festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

</details>

---

## `Party_Beschwerdesache`

**F1:** 0.398 | **Precision:** 0.862 | **Recall:** 0.259  

**Format:** `regex`  
**Rule ID:** `af12a153`  
**Description:**
Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.

**Content:**
```
(?:in der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\s+(?:der\s+|des\s+)?)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+vertreten|\s+\(|\s+\)|$|\s+\d{4}\s+\w+|\s+Gattin|\s+und\s+der)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.862 | 0.259 | 0.398 | 492 | 424 | 68 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 424 | 68 | 1212 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Erika Zajcenko, Volksheimstraße 9, 8784 Trieben, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erika Zajcenko` | `Erika Zajcenko` |

**Missed by this rule (FN):**

- `Volksheimstraße 9, 8784 Trieben, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Catharina Moewis,  Im Klosterhof 21N, 5241 Großenaich, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Catharina Moewis` | `Catharina Moewis` |

**Missed by this rule (FN):**

- `Im Klosterhof 21N, 5241 Großenaich, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Konrad Conrady  in der Beschwerdesache  Prof.  Ashley Lauterwasser, Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich, über die Beschwerde vom 23. September 2016 gegen den Bescheid  des Finanzamtes Linz vom 25. August 2016 betreffend Einkommensteuer 2014 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Prof.  Ashley Lauterwasser` | `Prof.  Ashley Lauterwasser` |

**Missed by this rule (FN):**

- `Univ.-Prof. Konrad Conrady` (person)
- `Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128731.1`) (sent_id: `deanon_BFG_TRAIN/128731.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Mag. Gerald Leverenz, Hansl-Schmid-Weg 54, 4623 Sirfling, Österreich, über die Beschwerde vom 17. Juli 2013 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 3. Juli 2013 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 Steuernummer zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerald Leverenz` | `Mag. Gerald Leverenz` |

**Missed by this rule (FN):**

- `Hansl-Schmid-Weg 54, 4623 Sirfling, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Klara Vondenhoff  in der Beschwerdesache  Vitus Hepprich, Singerweg 36, 9581 Unterferlach, Österreich  über die Beschwerde vom 28. Februar 2019 gegen die Bescheide  des FA Vorarlberg  vom 30. Jänner 2019, 20-231/9124, betreffend Umsatz- und  Einkommensteuer 2017  zu Recht erkannt:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Vitus Hepprich` | `Vitus Hepprich` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Klara Vondenhoff` (person)
- `Singerweg 36, 9581 Unterferlach, Österreich` (address)
- `FA Vorarlberg` (organisation)
- `20-231/9124` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128762.1`) (sent_id: `deanon_BFG_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Daniel Baake,  Zollfeldstraße 85, 4731 Unterbruck, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-63-948/2501 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Baake` | `Daniel Baake` |

**Missed by this rule (FN):**

- `Zollfeldstraße 85, 4731 Unterbruck, Österreich` (address)
- `10-63-948/2501` (tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Alvin Luczak, Kudlichstraße 14, 5282 Brunn im Gries, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Bruck Eisenstadt Oberwart  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 67-340/8452  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alvin Luczak` | `Alvin Luczak` |

**Missed by this rule (FN):**

- `Kudlichstraße 14, 5282 Brunn im Gries, Österreich` (address)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)
- `67-340/8452` (tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Serge Anhalt, Ebenfeld 7, 4776 Mitterndorf, Österreich,  vertreten durch WP_GmbH, WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  44-050/5905  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Serge Anhalt` | `Serge Anhalt` |

**Missed by this rule (FN):**

- `Ebenfeld 7, 4776 Mitterndorf, Österreich` (address)
- `44-050/5905` (tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/128893.1`) (sent_id: `deanon_BFG_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Horst de Keyser, Heinrich-Ruff-Weg 8, 8523 Laßnitz, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Horst de Keyser` | `Horst de Keyser` |

**Missed by this rule (FN):**

- `Heinrich-Ruff-Weg 8, 8523 Laßnitz, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache KzlR Livia Vasold, Statzenbachgasse 8, 9654 Tuffbad, Österreich, über die Beschwerde vom 10. Juni 2016 gegen den Bescheid des FA vom 3. Juni 2016  betreffend Einkommensteuer 2014 Steuernummer 94-176/6276  zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `KzlR Livia Vasold` | `KzlR Livia Vasold` |

**Missed by this rule (FN):**

- `Statzenbachgasse 8, 9654 Tuffbad, Österreich` (address)
- `94-176/6276` (tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Mehmet Bildstein, Josef Glanner-Gasse 168, 3142 Obermoos, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 72-182/5875  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mehmet Bildstein` | `Mehmet Bildstein` |

**Missed by this rule (FN):**

- `Dr. Alois Pichler` (person)
- `Josef Glanner-Gasse 168, 3142 Obermoos, Österreich` (address)
- `72-182/5875` (tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129103.1`) (sent_id: `deanon_BFG_TRAIN/129103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache DDr. Rocco Bernhards, Obere Festwiese 8, 4863 Steindorf, Österreich, über die Beschwerde vom 18. Juli 2013 gegen den Bescheid des Zollamtes Linz Wels  vom 18. Juni 2013 betreffend Vorschreibung eines Altlastenbeitrag für die Quartale 2-4 des  Jahres 2003 zu Recht erkannt:   Der angefochtene Bescheid wird hinsichtlich des Altlastenbeitrags - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `DDr. Rocco Bernhards` | `DDr. Rocco Bernhards` |

**Missed by this rule (FN):**

- `Obere Festwiese 8, 4863 Steindorf, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129137.1`) (sent_id: `deanon_BFG_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Lara Emhart, Steinwiese 39, 6060 Heiligkreuz, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Steinparztal 60, 9472 Krottendorf, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lara Emhart` | `Lara Emhart` |

**Missed by this rule (FN):**

- `Steinwiese 39, 6060 Heiligkreuz, Österreich` (address)
- `Steinparztal 60, 9472 Krottendorf, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Missed by this rule (FN):**

- `Mag. Markus Knechtl LL.M.` (person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich` (address)
- `84-986/6948` (tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129188.1`) (sent_id: `deanon_BFG_TRAIN/129188.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Volker Fatheuer, Voirans 4, 8503 Blumegg, Österreich, betreffend Beschwerde vom 11. Juni 2016 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart vom 13. Mai 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 beschlossen:  Der Vorlageantrag vom 9.2.2020 wird gemäß § 278 Abs. 1 lit. a i.V.m. den §§ 260 Abs. 1 lit. b,  264 Abs. 4 lit. e und 264 Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Volker Fatheuer` | `Volker Fatheuer` |

**Missed by this rule (FN):**

- `Voirans 4, 8503 Blumegg, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129205.1`) (sent_id: `deanon_BFG_TRAIN/129205.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Vivian Agnesen,  Kafkasee I 2G, 4693 Viecht, Österreich, über die Beschwerde vom 10. April 2019 gegen den Bescheid über den Antrag  vom 06.03.2019 auf Mehrkindzuschlag für 2019 aufgrund der Verhältnisse des Jahres 2018  des  Finanzamtes vom 1. April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vivian Agnesen` | `Vivian Agnesen` |

**Missed by this rule (FN):**

- `Kafkasee I 2G, 4693 Viecht, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Elena Zilinski, Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Elena Zilinski` | `Elena Zilinski` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe,  Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

| Predicted | Gold |
|---|---|
| `Kordelia van Clewe` | `Kordelia van Clewe` |

**Missed by this rule (FN):**

- `Mag.a Irene van der Hoven` (person)
- `Piettegasse 15, 3341 Oberamt, Österreich` (address)
- `FA Tirol Ost` (organisation)
- `20-364/1486` (tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129421.1`) (sent_id: `deanon_BFG_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Konepatzki  in der Beschwerdesache KommR MedR Jeannine Wegerhoff,  Burleiten 563, 9423 Matschenbloch, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KommR MedR Jeannine Wegerhoff` | `KommR MedR Jeannine Wegerhoff` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Jacqueline Konepatzki` (person)
- `Burleiten 563, 9423 Matschenbloch, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Vivian Wenk` | `Vivian Wenk` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Cedric Leutheusser, Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Cedric Leutheusser` | `Mag. Cedric Leutheusser` |

**Missed by this rule (FN):**

- `Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Shoshana Schweinforth, Brenggenalm 15, 8551 Gieselegg, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 78-461/2049  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shoshana Schweinforth` | `Shoshana Schweinforth` |

**Missed by this rule (FN):**

- `Brenggenalm 15, 8551 Gieselegg, Österreich` (address)
- `78-461/2049` (tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/129950.1`) (sent_id: `deanon_BFG_TRAIN/129950.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Denise Adamske, Adresse1,  Ungarn, über die Beschwerde vom 26. März 2019 gegen den Bescheid des Finanzamtes A vom  27. Februar 2019, Steuernummer 85-962/6181, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Denise Adamske` | `Denise Adamske` |

**Missed by this rule (FN):**

- `85-962/6181` (tax_number)

**Example 23** (doc_id: `deanon_BFG_TRAIN/129969.1`) (sent_id: `deanon_BFG_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hilde Heinsohn, Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `Hilde Heinsohn` | `Hilde Heinsohn` |

**Missed by this rule (FN):**

- `Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/130024.1`) (sent_id: `deanon_BFG_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Marlon William, J. Ranzoni-Straße 1L, 9554 Reggen, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlon William` | `Marlon William` |

**Missed by this rule (FN):**

- `J. Ranzoni-Straße 1L, 9554 Reggen, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130034.1`) (sent_id: `deanon_BFG_TRAIN/130034.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache des Karina Wissmann, Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich, betreffend eine  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, über die Beschwerde vom 16. Juli 2020 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 –  Parkraumüberwachung, als Abgabenstrafbehörde vom 18. Juni 2020, Zahl MA67/Zahlzu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde vom  16. Juli 2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  – Parkraumüberwachung, MA67/Zahl, vom 18. Juni 2020 als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Karina Wissmann` | `Karina Wissmann` |

**Missed by this rule (FN):**

- `Mag. Andreas Stanek` (person)
- `Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130057.1`) (sent_id: `deanon_BFG_TRAIN/130057.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Rachel Thurm  in der Beschwerdesache des  Arnold Kopman, Schiexlgasse 96, 4582 Seebach, Österreich, über die Beschwerde vom 6. März 2017 gegen den Bescheid des  Finanzamt Gmunden Vöcklabruck  vom 30. Jänner 2017 betreffend Grunderwerbsteuer 2017 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arnold Kopman` | `Arnold Kopman` |

**Missed by this rule (FN):**

- `Dr.in Rachel Thurm` (person)
- `Schiexlgasse 96, 4582 Seebach, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)

**Example 27** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Christoph Mehlbeer` | `Christoph Mehlbeer` |

**Missed by this rule (FN):**

- `Schötz Gasse 45, 7434 Holzschlag, Österreich` (address)
- `Margarete Wiepking` (person)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Missed by this rule (FN):**

- `Schulwiesen 13, 4203 Stratreith, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130442.1`) (sent_id: `deanon_BFG_TRAIN/130442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Armin Lieffering, Fuchsleitenweg 4, 4143 Neustift im Mühlkreis, Österreich, über die Beschwerden vom 27. November 2018 gegen die Bescheide des Finanzamtes  Baden Mödling vom 12. November 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017, Steuernummer , zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Armin Lieffering` | `Armin Lieffering` |

**Missed by this rule (FN):**

- `Fuchsleitenweg 4, 4143 Neustift im Mühlkreis, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_1`)


Gerald Erwin Ehgartner in der Beschwerdesache Janis Forch, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Janis Forch,` — partial — gold is substring of pred: `Janis Forch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Janis Forch`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl.

**False Positives:**

- `Dipl.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Emmerich Bleekmann`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenV, die RichterinR sowie die  fachkundigen Laienrichter LR1 und LR2 in der Beschwerdesache Bf, Wilhelmsederstraße 93, 9112 Gönitz, Österreich, vertreten  durch Stb, über die Beschwerde vom 27. April 2015 gegen die Bescheide des Finanzamtes St.  Johann Tamsweg Zell am See vom 27. März 2015 betreffend Umsatzsteuer 2012 und  Umsatzsteuer 2013, Steuernummer 91-666/8239, nach Durchführung einer mündlichen  Verhandlung am 10. Juni 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wilhelmsederstraße 93, 9112 Gönitz, Österreich`(address)
- `91-666/8239`(tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Dr.in Ulrike Kusnierz  in der Beschwerdesache K GmbH,  Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `K GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dr.in Ulrike Kusnierz`(person)
- `Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf. Name vormals nunmehr Janis Dollnig` — partial — gold is substring of pred: `Janis Dollnig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129503.1`) (sent_id: `deanon_BFG_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache Gabriele Lemmon, Bakk. rer. nat., Graf-Egger-Straße 4, 4712 Armau, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 49-573/3569  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `Gabriele Lemmon` — partial — pred is substring of gold: `Gabriele Lemmon, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gabriele Lemmon, Bakk. rer. nat.`(person)
- `Graf-Egger-Straße 4, 4712 Armau, Österreich`(address)
- `49-573/3569`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/130424.1`) (sent_id: `deanon_BFG_TRAIN/130424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Vivian Classens, Bakk. iur. BEd, Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich  vertreten durch Vertreter, gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 24. November 2015, betreffend Grunderwerbsteuer  aufgrund des Übergabsvertrages mit N.N. (Erf. Nr., Steuernummer), zu Recht erkannt:   Der eingeschränkten Beschwerde wird Folge gegeben.

**False Positives:**

- `Vivian Classens` — partial — pred is substring of gold: `Vivian Classens, Bakk. iur. BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vivian Classens, Bakk. iur. BEd`(person)
- `Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Cevik  in der Beschwerdesache der Bf., (im  Beschwerdeverfahren) vertreten durch Rechtsanwälte Lehofer & Lehofer,  Kalchberggasse 6/1.

**False Positives:**

- `Bf.,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Lubomir Cevik`(person)

**Example 8** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Marlies Danzfuss` — partial — pred is substring of gold: `Marlies Danzfuss, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Siegfried Fenz`(person)
- `Marlies Danzfuss, BSc`(person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/131091.1`) (sent_id: `deanon_BFG_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Raimund Grünstäudl  in der Beschwerdesache der Frau  Manfred Bernatik, Reisgasse 13, 8402 Werndorf, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Frau  Manfred Bernatik` — partial — gold is substring of pred: `Manfred Bernatik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Raimund Grünstäudl`(person)
- `Manfred Bernatik`(person)
- `Reisgasse 13, 8402 Werndorf, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/131772.1`) (sent_id: `deanon_BFG_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Dipl.

**False Positives:**

- `Dipl.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/132063.1`) (sent_id: `deanon_BFG_TRAIN/132063.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Gindert  in der Beschwerdesache Prof.in Henriette Oldvader, LLB,  Anton-Proksch-Siedlung 23, 3203 Steinklamm, Österreich, über die Säumnisbeschwerden vom 29. Jänner 2021, eingebracht am 8.  Februar 2021, wegen behaupteter Verletzung der Entscheidungspflicht des Finanzamt Innsbruck  betreffend   1. Antrag an das FA Innsbruck  vom 26.05.2020 auf Wiederaufnahme des mit  Einstellungsbeschluss des BFG vom 16.04.2020 abgeschlossenen Abgabenverfahrens  2. Antrag an das FA Innsbruck  vom 02.06.2020 auf Aufhebung des Einstellungsbeschlusses  des BFG vom 16.04.2020 nach § 299 BAO   beschlossen:  Die Säumnisbeschwerden werden gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Prof.in Henriette Oldvader` — partial — pred is substring of gold: `Prof.in Henriette Oldvader, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Jeannine Gindert`(person)
- `Prof.in Henriette Oldvader, LLB`(person)
- `Anton-Proksch-Siedlung 23, 3203 Steinklamm, Österreich`(address)
- `Finanzamt Innsbruck`(organisation)
- `FA Innsbruck`(organisation)
- `FA Innsbruck`(organisation)

**Example 12** (doc_id: `deanon_BFG_TRAIN/132142.1`) (sent_id: `deanon_BFG_TRAIN/132142.1_91`)


Als Beispiel darf auf das Urteil des EuGH in der Rechtssache Schumacker verwiesen werden.

**False Positives:**

- `Schumacker verwiesen werden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/132197.1`) (sent_id: `deanon_BFG_TRAIN/132197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Horst Widera, Bakk. rer. nat., Edergasse 43, 3713 Harmannsdorf, Österreich, über die Beschwerde vom 10. September 2019 gegen den  Bescheid des Finanzamtes Österreich vom 13. August 2019 betreffend Abweisung eines  Antrages auf Wiederaufnahme § 303 BAO /  ESt 2017 Steuernummer 56-074/9687  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Horst Widera` — partial — pred is substring of gold: `Horst Widera, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Horst Widera, Bakk. rer. nat.`(person)
- `Edergasse 43, 3713 Harmannsdorf, Österreich`(address)
- `56-074/9687`(tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf., Farchern 45, 4362 Kühweid, Österreich, über die Beschwerde vom 27. Mai 2016 gegen den  Bescheid des Finanzamtes KirchdorfPerg Steyr vom 27. April 2016 betreffend  Kapitalertragsteuer 2012 und die Bescheide vom 3. Mai 2016 betreffend Körperschaftssteuer  2012, 2013 und 2014, Steuernummer 77-859/7031, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Farchern 45, 4362 Kühweid, Österreich`(address)
- `77-859/7031`(tax_number)

**Example 15** (doc_id: `deanon_BFG_TRAIN/132255.1`) (sent_id: `deanon_BFG_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Chen Helwig  in der Beschwerdesache Roxana Gehrbrandt,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Roxana Gehrbrandt, ` — partial — gold is substring of pred: `Roxana Gehrbrandt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Chen Helwig`(person)
- `Roxana Gehrbrandt`(person)

**Example 16** (doc_id: `deanon_BFG_TRAIN/132412.1`) (sent_id: `deanon_BFG_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Erwin Mittenreiter  in der Beschwerdesache Rita Ratfeld  in  Liquidation, Kujanikgasse 28, 5123 Weng, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  FA Innsbruck  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rita Ratfeld  in  Liquidation` — partial — gold is substring of pred: `Rita Ratfeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Erwin Mittenreiter`(person)
- `Rita Ratfeld`(person)
- `Kujanikgasse 28, 5123 Weng, Österreich`(address)
- `FA Innsbruck`(organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/132557.1`) (sent_id: `deanon_BFG_TRAIN/132557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Emilia Nüßgens  in der Beschwerdesache der  Hinklein, Stadlweg 3, 8160 Haselbach bei Weiz, Österreich, vertreten durch Ort, über die Beschwerde vom 6.9.2017 gegen die  Bescheide des Finanzamtes Innsbruck vom 2. August 2017 betreffend Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 und Festsetzung der  Kraftfahrzeugsteuer für die Zeiträume Juli bis Dezember 2014 und Jänner bis Juni 2015 zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 wird abgewiesen.

**False Positives:**

- `Hinklein` — type mismatch — same span as gold: `Hinklein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Emilia Nüßgens`(person)
- `Hinklein`(organisation)
- `Stadlweg 3, 8160 Haselbach bei Weiz, Österreich`(address)

</details>

---

## `Judge_Richter`

**F1:** 0.157 | **Precision:** 0.700 | **Recall:** 0.089  

**Format:** `regex`  
**Rule ID:** `dc682d4a`  
**Description:**
Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles, ensuring no trailing whitespace and excluding single-letter abbreviations.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Vorsitzende)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|Dr\.\s+Univ\.-Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?)?)?)(?=\s+(?:in der|\u00fcber die|in der Verwaltungsstrafsache|\(|,|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.700 | 0.089 | 0.157 | 207 | 145 | 62 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 145 | 62 | 1488 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christoph Kordik in der Beschwerdesache  Prof. Hon.-Prof. ÖkR Detlev Leudert, Bungalowweg 8, 6741 Plazera, Österreich, über die Beschwerde vom 13.03.2015 gegen die Bescheide des  Finanzamtes Linz vom 17. Februar 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2009 und 2010 ,Steuernummer [...] ,zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christoph Kordik` | `Mag. Christoph Kordik` |

**Missed by this rule (FN):**

- `Prof. Hon.-Prof. ÖkR Detlev Leudert` (person)
- `Bungalowweg 8, 6741 Plazera, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Raphael Skowroneck, MBA` (person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Mehmet Bildstein, Josef Glanner-Gasse 168, 3142 Obermoos, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 72-182/5875  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Mehmet Bildstein` (person)
- `Josef Glanner-Gasse 168, 3142 Obermoos, Österreich` (address)
- `72-182/5875` (tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Lubomir Baltßun` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |

**Missed by this rule (FN):**

- `OStR Karl Ostendarp` (person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich` (address)
- `84-986/6948` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129254.1`) (sent_id: `deanon_BFG_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache StR VetR Corbinian Drügemöller, Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Thomas Leitner` | `Mag.Dr. Thomas Leitner` |

**Missed by this rule (FN):**

- `StR VetR Corbinian Drügemöller` (person)
- `Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Vivian Wenk` (person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129872.1`) (sent_id: `deanon_BFG_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache James Loratis, Platzerweg 28, 4673 Baumgarting, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `James Loratis` (person)
- `Platzerweg 28, 4673 Baumgarting, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129937.1`) (sent_id: `deanon_BFG_TRAIN/129937.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Paulina Steg, Weiterndorf 9, 4650 Oberzeiling, Österreich, vom 25. Juni 2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 28. Mai 2020, Zahl: MA67/Zahl, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Abweisung  I. Der Beschwerde wird teilweise Folge gegeben und die Entscheidung des Magistrats der Stadt  Wien in ihrem Ausspruch über die Strafe dahingehend abgeändert, dass die gemäß § 4 Abs. 1  Parkometergesetz 2006 verhängte Geldstrafe von € 140,00 auf € 90,00 und die gemäß § 16  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) verhängte Ersatzfreiheitsstrafe von 1 Tag 9 Stunden  auf 21 Stunden verringert werden.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Paulina Steg` (person)
- `Weiterndorf 9, 4650 Oberzeiling, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/130034.1`) (sent_id: `deanon_BFG_TRAIN/130034.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache des Karina Wissmann, Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich, betreffend eine  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, über die Beschwerde vom 16. Juli 2020 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 –  Parkraumüberwachung, als Abgabenstrafbehörde vom 18. Juni 2020, Zahl MA67/Zahlzu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde vom  16. Juli 2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  – Parkraumüberwachung, MA67/Zahl, vom 18. Juni 2020 als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Karina Wissmann` (person)
- `Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Marlies Danzfuss, BSc` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Paula Jagiella, Medienpark 18, 3384 Eidletzberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Paula Jagiella` (person)
- `Medienpark 18, 3384 Eidletzberg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Wladimir Nüssli` (person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/130686.1`) (sent_id: `deanon_BFG_TRAIN/130686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde der  Alana Single, Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich, vom 19. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 17. August 2020, Zahl MA67/Zahl/2019, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Alana Single` (person)
- `Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Matthäus Buskens` (person)
- `Edlach 19, 3141 Oberkilling, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/130909.1`) (sent_id: `deanon_BFG_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Miriam Kloeppel, Hollehnerweg 19, 9061 Nußberg, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Miriam Kloeppel` (person)
- `Hollehnerweg 19, 9061 Nußberg, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Jean Wohlrap, Weyprechtgasse 44M, 9701 Nußdorf, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Jean Wohlrap` (person)
- `Weyprechtgasse 44M, 9701 Nußdorf, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Gregor Fraunlob, Brantmannstraße 9, 3595 Frankenreith, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Gregor Fraunlob` (person)
- `Brantmannstraße 9, 3595 Frankenreith, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/131361.1`) (sent_id: `deanon_BFG_TRAIN/131361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Kordula Zeitler, Auhäuseln 22, 7540 Inzenhof, Österreich, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, MA 67, als Abgabenstrafbehörde vom 20. März 2020, MA67/GZ, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Kordula Zeitler` (person)
- `Auhäuseln 22, 7540 Inzenhof, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/131365.1`) (sent_id: `deanon_BFG_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Mario Gajewska, Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Mario Gajewska` (person)
- `Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Prof. Gernot Woortmann, Spitzbergweg 116, 3204 Tradigistgegend, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 16-817/8793  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Prof. Gernot Woortmann` (person)
- `Spitzbergweg 116, 3204 Tradigistgegend, Österreich` (address)
- `16-817/8793` (tax_number)

**Example 21** (doc_id: `deanon_BFG_TRAIN/132162.1`) (sent_id: `deanon_BFG_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Liu Werbicki, Elisabetha 26n, 3383 Pöttendorf, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 58-661/8152, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Liu Werbicki` (person)
- `Elisabetha 26n, 3383 Pöttendorf, Österreich` (address)
- `58-661/8152` (tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf., Farchern 45, 4362 Kühweid, Österreich, über die Beschwerde vom 27. Mai 2016 gegen den  Bescheid des Finanzamtes KirchdorfPerg Steyr vom 27. April 2016 betreffend  Kapitalertragsteuer 2012 und die Bescheide vom 3. Mai 2016 betreffend Körperschaftssteuer  2012, 2013 und 2014, Steuernummer 77-859/7031, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Farchern 45, 4362 Kühweid, Österreich` (address)
- `77-859/7031` (tax_number)

**Example 23** (doc_id: `deanon_BFG_TRAIN/132372.1`) (sent_id: `deanon_BFG_TRAIN/132372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die zwei  (gleichlautenden) Beschwerden des Siegmund Prokopiev, Seibersdorf bei Sankt Veit 10, 5242 Straß, Österreich, vom 21. Jänner 2021 gegen die  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67, Zahl 1) MA67/Zahl1  und 2) MA67/Zahl2/2020, beide vom 08. Jänner 2021, beide wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) werden die Beschwerden als  unbegründet abgewiesen und die angefochtenen Straferkenntnisse bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Siegmund Prokopiev` (person)
- `Seibersdorf bei Sankt Veit 10, 5242 Straß, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/132477.1`) (sent_id: `deanon_BFG_TRAIN/132477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Yelec Nitzge, Gasteigergasse 68, 3261 Oberstampfing, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 19. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Yelec Nitzge` (person)
- `Gasteigergasse 68, 3261 Oberstampfing, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_TRAIN/132482.1`) (sent_id: `deanon_BFG_TRAIN/132482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  MedR Roland Ruschemeier, Schöferhof 401, 9832 Untersteinwand, Österreich, über die Beschwerde vom 30. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 9. März 2020 betreffend Einkommensteuer  2018, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `MedR Roland Ruschemeier` (person)
- `Schöferhof 401, 9832 Untersteinwand, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/132501.1`) (sent_id: `deanon_BFG_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Huberta Petratschek, Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Huberta Petratschek` (person)
- `Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/132578.1`) (sent_id: `deanon_BFG_TRAIN/132578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Aloisa Füchsel, Wimhub 18, 3443 Henzing, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 6.3.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Aloisa Füchsel` (person)
- `Wimhub 18, 3443 Henzing, Österreich` (address)

**Example 28** (doc_id: `deanon_BFG_TRAIN/132660.1`) (sent_id: `deanon_BFG_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Nancy Kärgling, Küng 27, 2133 Ungerndorf, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Nancy Kärgling` (person)
- `Küng 27, 2133 Ungerndorf, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ernestine Schittenhelm, Clementinengasse 29, 8692 Krampen, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Ernestine Schittenhelm` (person)
- `Clementinengasse 29, 8692 Krampen, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128877.1`) (sent_id: `deanon_BFG_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers OSR DDr. Heiko Lehwaldt, Point 6, 3232 Zauching, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR DDr. Heiko Lehwaldt`(person)
- `Point 6, 3232 Zauching, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl.

**False Positives:**

- `Mag. Emmerich Bleekmann ` — partial — gold is substring of pred: `Mag. Emmerich Bleekmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Emmerich Bleekmann`(person)

**Example 3** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christoph Mehlbeer`(person)
- `Schötz Gasse 45, 7434 Holzschlag, Österreich`(address)
- `Margarete Wiepking`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/131051.1`) (sent_id: `deanon_BFG_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Kirsten Öllrich, Grundemanngasse 2, 4755 Hub, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Öllrich`(person)
- `Grundemanngasse 2, 4755 Hub, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Ottfried Bremermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottfried Bremermann`(person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich`(address)
- `Samuel Rehnke, BSc`(person)
- `Planetengasse 30, 8455 Bischofegg, Österreich`(address)
- `14-141/9449`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/131772.1`) (sent_id: `deanon_BFG_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Dipl.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/131922.1`) (sent_id: `deanon_BFG_TRAIN/131922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Bodo Ibel  in der Verwaltungsstrafsache  Fridolin Jodeleid, Stiftergasse 75z, 2262 Stillfried, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in  Verbindung mit § 16 Abs. 1 und Tarifpost B 8 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli  1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl.

**False Positives:**

- `Mag. Mag. Bodo Ibel ` — partial — gold is substring of pred: `Mag. Mag. Bodo Ibel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Mag. Bodo Ibel`(person)
- `Fridolin Jodeleid`(person)
- `Stiftergasse 75z, 2262 Stillfried, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Karola Birkenzeller, Reifnitz 2, 4532 Rohr im Kremstal, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Pascal Tiessen, Dipl.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karola Birkenzeller`(person)
- `Reifnitz 2, 4532 Rohr im Kremstal, Österreich`(address)
- `Pascal Tiessen`(person)

**Example 9** (doc_id: `deanon_BFG_TRAIN/133042.1`) (sent_id: `deanon_BFG_TRAIN/133042.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Siegfried Borneleit  in der Beschwerdesache Ashley Kutluca,  Pabensteinstraße 20, 5132 Reith, Österreich, über die Beschwerden vom 20. Februar 2020 gegen die Bescheide des  Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 24. Jänner 2020 betreffend   1. Zurückweisung des Antrages vom 2.1.2020 auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2014 und   2.

**False Positives:**

- `Dr. Dr. Siegfried Borneleit ` — partial — gold is substring of pred: `Dr. Dr. Siegfried Borneleit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Siegfried Borneleit`(person)
- `Ashley Kutluca`(person)
- `Pabensteinstraße 20, 5132 Reith, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Lorenz Lohkampff ` — partial — gold is substring of pred: `Mag. Lorenz Lohkampff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/133768.1`) (sent_id: `deanon_BFG_TRAIN/133768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Daphne Heinzlmeir, Holzwiesengasse 15, 4723 Natternbach, Österreich, über die Beschwerde vom 20. Mai 2021 gegen den Bescheid des Finanzamtes  Österreich vom 26. April 2021 betreffend Zwangsstrafen 2021 zu Steuernummer  68-502/3247  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daphne Heinzlmeir`(person)
- `Holzwiesengasse 15, 4723 Natternbach, Österreich`(address)
- `68-502/3247`(tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/134729.1`) (sent_id: `deanon_BFG_TRAIN/134729.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Philipp Dahlhues  in der Beschwerdesache August Combach,  Damweg 1, 7501 Spitzzicken, Österreich, gegen die Bescheide des Finanzamtes Österreich vom   - 11. Juli 2017 betreffend Einkommensteuer 2014 sowie  - 06. Juni 2018 betreffend Einkommensteuer 2016 und 2017  den Beschluss:  I. Die Beschwerde betreffend Einkommensteuer 2014 wird gemäß  § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Philipp Dahlhues ` — partial — gold is substring of pred: `Mag. Philipp Dahlhues`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Philipp Dahlhues`(person)
- `August Combach`(person)
- `Damweg 1, 7501 Spitzzicken, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/134866.1`) (sent_id: `deanon_BFG_TRAIN/134866.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Daniel Priskorn  in der Beschwerdesache Felix Kerling,  Rassbergstraße 13, 3742 Passendorf, Österreich, wegen behaupteter Verletzung der Entscheidungspflicht des FA St. Johann Tamsweg Zell am See  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 beschlossen:   Die Säumnisbeschwerde wird als unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Daniel Priskorn ` — partial — gold is substring of pred: `Dr. Daniel Priskorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Daniel Priskorn`(person)
- `Felix Kerling`(person)
- `Rassbergstraße 13, 3742 Passendorf, Österreich`(address)
- `FA St. Johann Tamsweg Zell am See`(organisation)

**Example 14** (doc_id: `deanon_BFG_TRAIN/135112.1`) (sent_id: `deanon_BFG_TRAIN/135112.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Zlatan Deisen  in der Beschwerdesache des  Prof. Richard Paulick, Scharmühlwinkel 13, 3144 Baumgarten, Österreich, über 1) die Beschwerde vom 27.9.2017 gegen den Bescheid des  Finanzamtes Bruck Leoben Mürzzuschlag (nunmehr Finanzamt Österreich) vom 4.9.2017  betreffend Umsatzsteuer 2015 sowie über 2) die Beschwerde vom 7.9.2018 gegen den  Bescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 21.8.2018 betreffend Abweisung  von Anträgen auf Aufhebung der Bescheide hinsichtlich Umsatzsteuer 2011 bis 2014 nach  Durchführung einer mündlichen Verhandlung am 2.12.2021 zu Recht erkannt:   I. Den Beschwerden wird Folge gegeben.

**False Positives:**

- `Dr. Dr. Zlatan Deisen ` — partial — gold is substring of pred: `Dr. Dr. Zlatan Deisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Zlatan Deisen`(person)
- `Prof. Richard Paulick`(person)
- `Scharmühlwinkel 13, 3144 Baumgarten, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/135347.1`) (sent_id: `deanon_BFG_TRAIN/135347.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache DDr. DDr. Björn Wöber, Bisamgasse 3i, 9433 Tschrietes, Österreich, betreffend Beschwerde vom 27. Oktober 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 9. Oktober 2020 zu Steuernummer  60-281/1996  betreffend Abweisung des Antrages auf Zuerkennung der Familienbeihilfe für  KommR Hugo Vollpracht  ab Oktober 2019 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `R.` — similar text (different position): `DDr. DDr. Björn Wöber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. DDr. Björn Wöber`(person)
- `Bisamgasse 3i, 9433 Tschrietes, Österreich`(address)
- `60-281/1996`(tax_number)
- `KommR Hugo Vollpracht`(person)

**Example 16** (doc_id: `deanon_BFG_TRAIN/135585.1`) (sent_id: `deanon_BFG_TRAIN/135585.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Charles Schindele  in der Beschwerdesache Gregor Branz,  Tandlerstraße 7, 9341 Herd, Österreich, vertreten durch die Germuth Steuerberatungs GmbH, Johannesgasse 16/5,  1010 Wien, über die Beschwerde vom 17. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 14. Juli 2021 betreffend Nachsicht gemäß § 236 BAO, Steuernummer  79-519/7411  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Charles Schindele ` — partial — gold is substring of pred: `Mag. Charles Schindele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Charles Schindele`(person)
- `Gregor Branz`(person)
- `Tandlerstraße 7, 9341 Herd, Österreich`(address)
- `79-519/7411`(tax_number)

**Example 17** (doc_id: `deanon_BFG_TRAIN/135774.1`) (sent_id: `deanon_BFG_TRAIN/135774.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache MedR Uwe Preikschas, Marika Rökk-Straße 67, 3131 Anzenberg, Österreich, über die Beschwerde vom 19. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019, Steuernummer 19-302/7367, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO – wie mit Beschwerdevorentscheidung vom 26. April  2021 – teilweise Folge gegeben und der angefochtene Bescheid in diesem Sinne abgeändert.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MedR Uwe Preikschas`(person)
- `Marika Rökk-Straße 67, 3131 Anzenberg, Österreich`(address)
- `19-302/7367`(tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/136313.1`) (sent_id: `deanon_BFG_TRAIN/136313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger im  Beschwerdeverfahren über die Beschwerde der Verl nach XY, vertreten durch Laurence Krekemeyer,  Steyersberg 2, 8481 Priebing, Österreich  vom 20. Juli 2021 gegen den Zurückweisungsbescheid des Finanzamtes  Österreich vom 7. Juli 2021 betreffend Antrag auf Durchführung einer  Arbeitnehmerveranlagung, beschlossen:  Der Vorlageantrag der Beschwerdeführerin Verl nach XY vom 10.9.2021 wird gemäß § 260 Abs.  1 BAO iVm § 264 BAO (insbesondere Abs. 4 lit e und Abs. 5) als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr. Ansgar Unterberger im  Beschwerdeverfahren` — partial — gold is substring of pred: `Dr. Ansgar Unterberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Laurence Krekemeyer`(person)
- `Steyersberg 2, 8481 Priebing, Österreich`(address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/137032.1`) (sent_id: `deanon_BFG_TRAIN/137032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dirk Kreutel  in der Beschwerdesache   Samir Hentzsch, Strattnerstraße 101, 8341 Saaz, Österreich, vertreten durch Steuerberater Lynn Meinertshagen, über die  Beschwerde vom 19. Mai 2014 gegen die Bescheide des FA Klosterneuburg (jetzt Finanzamt Österreich  vom 22. April 2014 betreffend Umsatzsteuer und Körperschaftsteuer 2009-2011 und die  Bescheide über die Wiederaufnahme der jeweiligen Verfahren,   Steuernummer 10-189/1227,   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Dirk Kreutel ` — partial — gold is substring of pred: `Dr. Dirk Kreutel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dirk Kreutel`(person)
- `Samir Hentzsch`(person)
- `Strattnerstraße 101, 8341 Saaz, Österreich`(address)
- `Lynn Meinertshagen`(person)
- `FA Klosterneuburg`(organisation)
- `10-189/1227`(tax_number)

**Example 20** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Dr. Theobald Korschinek ` — partial — gold is substring of pred: `Dr. Theobald Korschinek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Theobald Korschinek`(person)
- `Dieter Papakiriakou`(person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich`(address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/137493.1`) (sent_id: `deanon_BFG_TRAIN/137493.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Herbert Kramp, Kinkstraße 6, 3541 Senftenberg, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Waldviertel, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend Abweisung des  Antrages auf Gewährung der vollen nichtindexierten Familienbeihilfe ab Jänner 2019,  Steuernummer 15-114/2120, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Herbert Kramp`(person)
- `Kinkstraße 6, 3541 Senftenberg, Österreich`(address)
- `15-114/2120`(tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/137516.1`) (sent_id: `deanon_BFG_TRAIN/137516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Friedhelm Servais, Ölbrennerweg 38, 5231 Wiesing, Österreich, über die Beschwerde vom 15. Oktober 2020 gegen den Bescheid des Finanzamtes  Österreich vom 1. Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 86-385/7500  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Friedhelm Servais`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Friedhelm Servais`(person)
- `Ölbrennerweg 38, 5231 Wiesing, Österreich`(address)
- `86-385/7500`(tax_number)

**Example 23** (doc_id: `deanon_BFG_TRAIN/137596.1`) (sent_id: `deanon_BFG_TRAIN/137596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Egon Hintenberg  in der Beschwerdesache des  OMedR Rafaela Balcius, Hoferweg 3, 3033 Manzing, Österreich, über die Beschwerde vom 11. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Egon Hintenberg ` — partial — gold is substring of pred: `Mag. Egon Hintenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Egon Hintenberg`(person)
- `OMedR Rafaela Balcius`(person)
- `Hoferweg 3, 3033 Manzing, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/137664.1`) (sent_id: `deanon_BFG_TRAIN/137664.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Dr. Emanuel Rauschmeir  in der Beschwerdesache Bertha Hueber,  Schirnes 10, 9871 Kötzing, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, betreffend Beschwerden vom 11. Februar 2020 und 27. Februar 2020  gegen die Bescheide betreffend Feststellungsbescheid Gruppenmitglied 2014 vom 11. Februar  2020 sowie vom 13. Jänner 2020 betreffend Feststellungsbescheid Gruppenmitglied 2015 und  2016 jeweils des Finanzamtes Wien 1/23 den Beschluss:   I. Die Beschwerden werden gemäß § 278 Abs. 1 lit b iVm § 256 Abs. 3 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Dr. Emanuel Rauschmeir ` — partial — gold is substring of pred: `Dr. Emanuel Rauschmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Emanuel Rauschmeir`(person)
- `Bertha Hueber`(person)
- `Schirnes 10, 9871 Kötzing, Österreich`(address)

**Example 25** (doc_id: `deanon_BFG_TRAIN/138011.1`) (sent_id: `deanon_BFG_TRAIN/138011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Sascha Grosan  in der Beschwerdesache Carla Kurrek,  Moosacker 29, 4724 Stocket, Österreich, über die Beschwerde vom 30. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Kirchdorf Perg Steyr)vom 30. November 2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 92-841/4978  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Sascha Grosan ` — partial — gold is substring of pred: `Dr. Sascha Grosan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sascha Grosan`(person)
- `Carla Kurrek`(person)
- `Moosacker 29, 4724 Stocket, Österreich`(address)
- `92-841/4978`(tax_number)

**Example 26** (doc_id: `deanon_BFG_TRAIN/138321.1`) (sent_id: `deanon_BFG_TRAIN/138321.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Miroslav Rolleder  in der Beschwerdesache Adelheid Loefflad,  Sonndorf 5, 5145 Gsotthub, Österreich, gegen die von der belangten Behörde Finanzamt Österreich am 12. Juli 2022 zu  Steuernummer 92-210/3587  ausgefertigten Bescheide über die Zurückweisung der Anträge  auf Aufhebung der Einkommensteuerbescheide für die Jahre 2017, 2018 und 2019 sowie die  am selben Tag  von der  gleichen belangten Behörde ausgefertigten Bescheide über die  Abweisung der Anträge auf Aufhebung der Einkommensteuerbescheide für die Jahre 2020 und  2021 zu Recht erkannt:   I. Die Beschwerde gegen die Bescheide über die Zurückweisung der Anträge auf Aufhebung  der Einkommensteuerbescheide für die Jahre 2017, 2018 und 2019 und gegen den Bescheid  über die Abweisung des Antrags auf Aufhebung des Einkommensteuerbescheides für das  Jahr 2021 wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Miroslav Rolleder ` — partial — gold is substring of pred: `Mag. Miroslav Rolleder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Miroslav Rolleder`(person)
- `Adelheid Loefflad`(person)
- `Sonndorf 5, 5145 Gsotthub, Österreich`(address)
- `92-210/3587`(tax_number)

</details>

---

## `Name_Gegen`

**F1:** 0.026 | **Precision:** 0.282 | **Recall:** 0.013  

**Format:** `regex`  
**Rule ID:** `789ef8cf`  
**Description:**
Captures names following 'gegen' (against) in legal proceedings.

**Content:**
```
(?:gegen\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+\(|$|\s+\d{4}|\s+Gattin|\s+und)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.282 | 0.013 | 0.026 | 78 | 22 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 22 | 56 | 1614 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129896.1`) (sent_id: `deanon_BFG_TRAIN/129896.1_2`)


in der Verwaltungsstrafsache gegen  Elina Jonethal, Steinkamperl 3, 4204 Zeil, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006 über die  zwei gleichlautenden Beschwerden der Beschuldigten vom 24. März 2020 gegen die zwei  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 25. Februar  2020, Zahl: a) MA67/xxxxx/2019 und b) MA67/yyyyy/2019, zu Recht erkannt:  I) Die zwei Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elina Jonethal` | `Elina Jonethal` |

**Missed by this rule (FN):**

- `Steinkamperl 3, 4204 Zeil, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131148.1`) (sent_id: `deanon_BFG_TRAIN/131148.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der  Verwaltungsstrafsache gegen Ronja Hertwick, Lainach 22, 9564 Mitterdorf, Österreich, über die Beschwerde vom 20.  November 2020, gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der  Stadt Wien, Magistratsabteilung 6, vom 09. November 2020, Zahl MA67/Zahl/2019, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 08. Mai 2019, Zahl MA67/Zahl/2019, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ronja Hertwick` | `Ronja Hertwick` |

**Missed by this rule (FN):**

- `Lainach 22, 9564 Mitterdorf, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/134195.1`) (sent_id: `deanon_BFG_TRAIN/134195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der  Verwaltungsstrafsache gegen Christian Nowikov, Schildlehen 2, 3512 Mautern an der Donau, Österreich, über die Beschwerde vom 02. März  2021 gegen die zwei Vollstreckungsverfügungen des Magistrates der Stadt Wien,  Magistratsabteilung 6 – BA 32, beide vom 25. Februar 2021, Zahlen A) MA67/ZahlA/2020 und  B) MA67/ZahlB/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und werden die angefochtenen Vollstreckungsverfügungen bestätigt.

| Predicted | Gold |
|---|---|
| `Christian Nowikov` | `Christian Nowikov` |

**Missed by this rule (FN):**

- `Schildlehen 2, 3512 Mautern an der Donau, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/134689.1`) (sent_id: `deanon_BFG_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Brunhild Katschmareck` | `Brunhild Katschmareck` |

**Missed by this rule (FN):**

- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen Mag. Willibald Giesser, Eichingerweg 67, 4931 Neulendt, Österreich, vertreten durch HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft, Landstraßer Hauptstraße 27,  1030 Wien, über die Beschwerde des Beschuldigten vom 1. April 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 6,  Abgabenstrafen vom 2. März 2021, Zahl: MA6/206000002559/2020, in Anwesenheit des  Verteidigers und der Behördenvertreterin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der Zurückweisungsbescheid des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Willibald Giesser` | `Mag. Willibald Giesser` |

**Missed by this rule (FN):**

- `Eichingerweg 67, 4931 Neulendt, Österreich` (address)
- `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/137220.1`) (sent_id: `deanon_BFG_TRAIN/137220.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Ottfried Weicke, Siebenbürger Straße 6, 6135 Stans, Österreich, vertreten durch Singer-Musil Singer  RA OG, Döblinger Hauptstraße 68, 1190 Wien, wegen Verwaltungsübertretungen gem. § 1 Abs.  1 iVm § 16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966,  LGBl. für Wien Nr. 20 idF des LGBl.

| Predicted | Gold |
|---|---|
| `Ottfried Weicke` | `Ottfried Weicke` |

**Missed by this rule (FN):**

- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Siebenbürger Straße 6, 6135 Stans, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter in der Verwaltungsstrafsache gegen Natascha Daschmann,  Gillhofstraße 7, 8990 Lerchenreith, Österreich, Deutschland, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 5. Mai  2022, gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  21. April 2022, Zahl MA67/Zahl/2021, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Missed by this rule (FN):**

- `Gillhofstraße 7, 8990 Lerchenreith, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138030.1`) (sent_id: `deanon_BFG_TRAIN/138030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der  Verwaltungsstrafsache gegen Kirsten Fibich, Voitsbergerweg 7, 5211 Schwöll, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF.  ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, über die Beschwerde der  beschwerdeführenden Partei vom 7. April 2022 gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom  28. März 2022, Zahl MA67/Zahl/2021, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Kirsten Fibich` | `Kirsten Fibich` |

**Missed by this rule (FN):**

- `Voitsbergerweg 7, 5211 Schwöll, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/138484.1`) (sent_id: `deanon_BFG_TRAIN/138484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Verwaltungsstrafsache gegen Ruprecht Seebode, Ursulinenplatz 11, 4861 Hainbach, Österreich, über die Beschwerde des  Beschuldigten vom 23. September 2022, gegen die Vollstreckungsverfügung des Magistrates  der Stadt Wien, Magistratsabteilung 6, BA 32, vom 20. September 2022, Zahl MA67/Zahl/2022,  betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen Strafe samt  Mahngebühr auf Grund der Strafverfügung vom 3. August 2022, Zahl MA67/Zahl/2022, zu  Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung des Magistrates der  Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Ruprecht Seebode` | `Ruprecht Seebode` |

**Missed by this rule (FN):**

- `Mag. Daniel Philip Pfau` (person)
- `Ursulinenplatz 11, 4861 Hainbach, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/140707.1`) (sent_id: `deanon_BFG_TRAIN/140707.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der Verwal- tungsstrafsache gegen Wendelin Kohr, Fritz-Engel-Straße 17, 4692 Penetzdorf, Österreich, wegen der Verwaltungsübertretung gemäß  § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde des Beschuldigten vom 10. März 2023 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. März 2023, GZ.  MA67/Zahl/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Wendelin Kohr` | `Wendelin Kohr` |

**Missed by this rule (FN):**

- `Fritz-Engel-Straße 17, 4692 Penetzdorf, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/140876.1`) (sent_id: `deanon_BFG_TRAIN/140876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Birgitt Koran in der  Verwaltungsstrafsache gegen Traude von der Laaken, Am Sägebach 49, 5124 Marktl, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 21. November 2022  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  7. November 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Traude von der Laaken` | `Traude von der Laaken` |

**Missed by this rule (FN):**

- `Am Sägebach 49, 5124 Marktl, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/141220.1`) (sent_id: `deanon_BFG_TRAIN/141220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Julia Nellen, Siemensweg 11, 4322 Altenburg, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde der Beschuldigten vom 20. Februar 2023 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 17. Jänner 2023, GZ.  MA67/Zahl/2022, nach Durchführung einer mündlichen Ver¬handlung am 5. Juni 2023 in  Anwesenheit der Beschuldigten und der Schriftführerin zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis aufge- hoben und das Verfahren nach § 45 Abs. 1 Z. 2. VStG eingestellt.

| Predicted | Gold |
|---|---|
| `Julia Nellen` | `Julia Nellen` |

**Missed by this rule (FN):**

- `Siemensweg 11, 4322 Altenburg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/142771.1`) (sent_id: `deanon_BFG_TRAIN/142771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der  Verwaltungsstrafsache gegen Ernst Skrzyppek, Südrandstraße 14, 9816 Litzldorf, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 11. Oktober 2023 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  15. September 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Ernst Skrzyppek` | `Ernst Skrzyppek` |

**Missed by this rule (FN):**

- `Mag. Gerhard Konrad` (person)
- `Südrandstraße 14, 9816 Litzldorf, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/143463.1`) (sent_id: `deanon_BFG_TRAIN/143463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Corinna Zimmerninks, Johann-Rössler-Gasse 55, 4152 Obernreith, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde des Beschuldigten vom 9. Jänner 2024 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2024, GZ. MA67/Zahl/2023, zu Recht  erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Corinna Zimmerninks` | `Corinna Zimmerninks` |

**Missed by this rule (FN):**

- `Johann-Rössler-Gasse 55, 4152 Obernreith, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/144489.1`) (sent_id: `deanon_BFG_TRAIN/144489.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler in der  Verwaltungsstrafsache gegen Claire Madelung, A.-Schuricht-Straße 1292, 8934 Wolfsbachau, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 11. April 2024 gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. März 2024,  GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Claire Madelung` | `Claire Madelung` |

**Missed by this rule (FN):**

- `A.-Schuricht-Straße 1292, 8934 Wolfsbachau, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Verwaltungsstrafsache  gegen Leonhard Facci, Am Aigen 26, 3214 Brandgegend, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idgF. in Verbindung mit § 4  Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF. über die Beschwerde des  Beschuldigten vom 20. April 2024 gegen das Erkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 16. April 2024, Zahl: MA67/246700162299/2024, nach mündlicher  Verhandlung am 18.6.2024 in Anwesenheit des Beschuldigten zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als die  Verhängung der Geldstrafe und der Ersatzfreiheitsstrafe aufgehoben werden sowie  gemäß § 45 Abs. 1 Z 4 und Abs. 1 letzter Satz VStG von der Verhängung einer Strafe  abgesehen und den Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Am Aigen 26, 3214 Brandgegend, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/146760.1`) (sent_id: `deanon_BFG_TRAIN/146760.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Lorenz Wilim, Feinfeld 31, 9113 Lippitzbach, Österreich, über die Beschwerde vom 30. April  2024 gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien vom 24. April 2024,  Zahl: MA67/236701487597/2023, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  die angefochtene Vollstreckungsverfügung bestätigt.

| Predicted | Gold |
|---|---|
| `Lorenz Wilim` | `Lorenz Wilim` |

**Missed by this rule (FN):**

- `Feinfeld 31, 9113 Lippitzbach, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Madeleine Klingner  in der Verwaltungsstrafsache  gegen Christine Stepanek, Haidsiedlung 2, 9431 Paildorf, Österreich, über die Beschwerde vom 18. Jänner 2025 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 9. Jänner 2025, Zahl:  MA67/246700179244/2024, mit dem der Einspruch vom 13. Oktober 2024 gegen die  Strafverfügung vom 16. September 2024 mit derselben Geschäftszahl gemäß § 49 Abs. 1  VStG als verspätet zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Christine Stepanek` | `Christine Stepanek` |

**Missed by this rule (FN):**

- `Dr.in Madeleine Klingner` (person)
- `Haidsiedlung 2, 9431 Paildorf, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_5`)


B. Das Bundesfinanzgericht hat durch die Richterin Dr.in Madeleine Klingner  in der Verwaltungsstrafsache  gegen Christine Stepanek, Haidsiedlung 2, 9431 Paildorf, Österreich  über den Antrag vom 18. Jänner 2025 auf Aufhebung der  Strafverfügung vom 16. September 2024, Zahl: MA67/246700179244/2024, den Beschluss  gefasst:    I. Gemäß § 28 und 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Antrag als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Stepanek` | `Christine Stepanek` |

**Missed by this rule (FN):**

- `Dr.in Madeleine Klingner` (person)
- `Haidsiedlung 2, 9431 Paildorf, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_9`)


C. Das Bundesfinanzgericht hat durch die Richterin Dr.in Madeleine Klingner  in der Verwaltungsstrafsache  gegen Christine Stepanek, Haidsiedlung 2, 9431 Paildorf, Österreich  über den Antrag vom 18. Jänner 2025 auf  Wiederaufnahme des Verfahrens nach § 69 AVG zum Bescheid vom 9. Jänner 2025, Zahl:  MA67/246700179244/2024, mit dem der Antrag vom 15. Dezember 2024 auf  Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Einbringung  eines Rechtsmittels gegen die Strafverfügung vom 16. September 2024 mit derselben  Geschäftszahl gemäß § 71 Abs. 1 AVG in Verbindung mit § 24 VStG als unzulässig  zurückgewiesen wurde, den Beschluss gefasst:    I. Gemäß § 28 und 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Antrag als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Stepanek` | `Christine Stepanek` |

**Missed by this rule (FN):**

- `Dr.in Madeleine Klingner` (person)
- `Haidsiedlung 2, 9431 Paildorf, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/149029.1`) (sent_id: `deanon_BFG_TRAIN/149029.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Verwaltungsstrafsache gegen Constantin Stein, Anton-Gassner-Weg 6N, 4924 Baumgarten, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl.

| Predicted | Gold |
|---|---|
| `Constantin Stein` | `Constantin Stein` |

**Missed by this rule (FN):**

- `Anton-Gassner-Weg 6N, 4924 Baumgarten, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/149205.1`) (sent_id: `deanon_BFG_TRAIN/149205.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Alva Jakuszeit, Leopold-Figl-Weg 7, 2032 Enzersdorf im Thale, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  Abl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl.

| Predicted | Gold |
|---|---|
| `Alva Jakuszeit` | `Alva Jakuszeit` |

**Missed by this rule (FN):**

- `Dr. Sebastian Pfeiffer LL.M.` (person)
- `Leopold-Figl-Weg 7, 2032 Enzersdorf im Thale, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_0`)


GZ. RV/7300048/2016 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen Herrn J., geb., Wien, vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/10, 1060 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten gemäß §§ 33 Abs. 1 und Abs. 2 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom 1. August 2016 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  8. Juni 2016 , SpS 16, nach Durchführung einer mündlichen Verhandlung  am 10. Jänner 2017 in Anwesenheit des Beschuldigten, seines Verteidigers, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt: Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des Spruchsenates vom 8. Juni 2016, SpS 16, wie folgt abgeändert: I. Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer 002 anhängige Finanzstrafverfahren wird hinsichtlich des Verdachts, Herr J. hätte  vorsätzlich a) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von€ 2.403,50  zu verkürzen versucht und dadurch eine versuchte Abgabenhinterziehung gemäß §§ 13, 33 Abs. 1 FinStrG begangen, b) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden Voranmeldungen die Vorauszahlung von Umsatzsteuer für 4/2015 in Höhe von € 900,00 bewirkt und  dadurch eine Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a FinStrG begangen, c) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

**False Positives:**

- `Herrn J., geb.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_79`)


Von diesem Betrag  werden die bereits bar kassierten Beträge abgezogen und der Rest dem Subunternehmer  gegen Rechnung ausbezahlt.

**False Positives:**

- `Rechnung ausbezahlt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/130475.1`) (sent_id: `deanon_BFG_TRAIN/130475.1_42`)


Andere offenbar auf einem ähnlichen Versehen beruhende Unrichtigkeiten sind Fehler, die  Schreib- und Rechenfehler sehr nahekommen, also Fehler in der Ausdrucksweise, nicht  hingegen Fehler im Bereich des Zustandekommens und der Gestaltung des Bescheidwillens.

**False Positives:**

- `Fehler im Bereich des Zustandekommens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/130727.1`) (sent_id: `deanon_BFG_TRAIN/130727.1_70`)


Innerhalb offener Frist erhob sie dagegen Beschwerde  sowie nach Ergehen einer abweisenden Beschwerdevorentscheidung fristgerecht den Antrag  auf Vorlage der Beschwerde an das Bundesfinanzgericht.

**False Positives:**

- `Beschwerde  sowie nach Ergehen einer abweisenden Beschwerdevorentscheidung fristgerecht den Antrag  auf Vorlage der Beschwerde an das Bundesfinanzgericht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Ronald Kleile, Bakk. rer. nat., Fischteichweg 49, 4924 Hartlberg, Österreich, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 15. März 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 20. Februar 2019, Strafnummer 007, in Anwesenheit des  Beschuldigten, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Über Ronald Kleile, Bakk. rer. nat.  wird gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 17.600,00  verhängt.

**False Positives:**

- `Herrn Ronald Kleile` — positional overlap with gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)
- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/132704.1`) (sent_id: `deanon_BFG_TRAIN/132704.1_5`)


III. Der Beschwerde gegen Vorauszahlungsbescheid 2018 wird teilweise Folge gegeben.

**False Positives:**

- `Vorauszahlungsbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/132991.1`) (sent_id: `deanon_BFG_TRAIN/132991.1_34`)


I.2. Beschwerde  Mit Schreiben vom 24. Mai 2017 brachte die anwaltliche Vertretung der beschwerdeführenden  Gesellschaft dagegen Beschwerde ein und führte zunächst aus, dass der Bescheid mangelhaft  begründet sei.

**False Positives:**

- `Beschwerde ein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_161`)


Die bei Beendigung der  Personenvereinigung (Personengemeinschaft) bestehende Vertretungsbefugnis bleibt, sofern  dem nicht andere Rechtsvorschriften entgegenstehen, insoweit und solange aufrecht, als nicht  von einem der zuletzt beteiligt gewesenen Gesellschafter (Mitglieder) oder der  vertretungsbefugten Person dagegen Widerspruch erhoben wird.

**False Positives:**

- `Widerspruch erhoben wird.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_113`)


IV. Rechtslage  1. Gesetzliche Bestimmungen:  Gemäß Art. 1 Abs. 1 UStG 1994 (= Binnenmarktregelung/BMR als Anhang zu § 29 Abs. 8 UStG  1994) unterliegt auch der innergemeinschaftliche Erwerb im Inland gegen Entgelt der  Umsatzsteuer.

**False Positives:**

- `Entgelt der  Umsatzsteuer.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_114`)


Nach Art. 1 Abs. 2 UStG 1994 liegt ein innergemeinschaftlicher Erwerb gegen Entgelt vor, wenn  (Z 1) ein Gegenstand bei einer Lieferung an den Abnehmer (Erwerber) aus dem Gebiet eines  Mitgliedstaates in das Gebiet eines anderen Mitgliedstaates gelangt, auch wenn der Lieferer  den Gegenstand in das Gemeinschaftsgebiet eingeführt hat und (Z 2) der Erwerber ein  Unternehmer, der den Gegenstand für sein Unternehmen erwirbt, oder eine juristische Person  ist, die nicht Unternehmer ist oder die den Gegenstand nicht für ihr Unternehmen erwirbt.

**False Positives:**

- `Entgelt vor, wenn ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/134926.1`) (sent_id: `deanon_BFG_TRAIN/134926.1_14`)


In der Folge listete der Bf seine, aufgrund seiner „besonderen beruflichen und privaten  Konstellation“, mit nur etwa 15%-20% vom „Warenkorb 2019 der Statistik Austria“ deutlich  unterdurchschnittlichen Kosten der privaten Lebensführung auf (3 Betriebe, darunter L+F mit  wesentlichen Beiträgen zur Eigenversorgung (Wohnversorgung, Holzheizung, Lebensmittel),  Zweipersonenhaushalt mit Versorgung der pflegebedürftigen Mutter gegen Kostenbeteiligung  (Pflegegeldbezug Stufe 6).

**False Positives:**

- `Kostenbeteiligung ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/135372.1`) (sent_id: `deanon_BFG_TRAIN/135372.1_50`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Unstrittig hat der Bf mit einem gerichtlichen Vergleich vom 26.3.2002 gegen Zusicherung einer  lebenslangen monatlichen Leibrente (in Form einer angemessenen Kaupreisrente) iHv €  4 von 17 Seite 5 von 17

**False Positives:**

- `Zusicherung einer  lebenslangen monatlichen Leibrente` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_42`)


§ 11 WTFG: Wer im Gebiet der Stadt Wien in einem Beherbergungsbetrieb oder in einer  Privatunterkunft gegen Entgelt Aufenthalt nimmt (Beherbergung), hat die Ortstaxe zu  entrichten.

**False Positives:**

- `Entgelt Aufenthalt nimmt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/135628.1`) (sent_id: `deanon_BFG_TRAIN/135628.1_9`)


Am 11. Februar 2014, bei der belangten Behörde am eingelangt am 13. Februar 2014 brachte  die Bf dagegen Beschwerde ein.

**False Positives:**

- `Beschwerde ein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/136061.1`) (sent_id: `deanon_BFG_TRAIN/136061.1_230`)


Das Vorbringen, wonach das Nominalwertprinzip über lange Zeiträume zu immer größerer  Besteuerung von Scheingewinnen führe, der Nominalwert über lange Zeiträume gegen Null  gehe und es umso mehr zu einer Besteuerung von Substanz und nicht von Gewinn komme,  beruht auf der von der Bf. mutwillig herbeigeführten Einkünfteermittlung gemäß § 30 Abs. 3  EStG 1988, wo doch die reguläre Besteuerung für das gegenständlich betroffene Altvermögen  gemäß § 30 Abs. 4 Z 2 EStG 1988 wesentlich günstiger wäre.

**False Positives:**

- `Null  gehe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/136261.1`) (sent_id: `deanon_BFG_TRAIN/136261.1_37`)


Da aber die Wertsteigerung von 2009 auf 2015 die durch Professionisten gegen Rechnung und  Gewährleistung erbrachte Arbeitsleistung beinhaltet, erscheint es sachgerecht, als Ausgaben  im Rahmen der Eigenleistung nur die Hälfte dieses Betrages zum Ansatz zu bringen.

**False Positives:**

- `Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/136471.1`) (sent_id: `deanon_BFG_TRAIN/136471.1_6`)


Mit Schriftsatz vom 15.06.2021 brachte die Beschwerdeführerin durch die  Erwachsenenvertretung Salzburg dagegen Beschwerde ein.

**False Positives:**

- `Beschwerde ein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/136516.1`) (sent_id: `deanon_BFG_TRAIN/136516.1_5`)


Mit Schreiben vom 21. April 2021 erhob die steuerliche Vertretung der Beschwerdeführerin  dagegen Beschwerde.

**False Positives:**

- `Beschwerde.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/137355.1`) (sent_id: `deanon_BFG_TRAIN/137355.1_136`)


Punkt 2.5.8.2 der AGB 2006 sowie Punkt 2.12.2 der AGB 2011 lauten wörtlich:  „Der Kunde tritt bereits hiermit seine Rechte aus den für das Leasingfahrzeug abgeschlossenen  Versicherungen (unabhängig davon, wer den Versicherungsschutz eingedeckt hat) sowie alle  Ansprüche wegen Beschädigung des Leasingfahrzeuges gegen Dritte und deren  Haftpflichtversicherungen an Ronald Leinberger  ab, die die Abtretungen annimmt.

**False Positives:**

- `Dritte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Leinberger`(person)

**Example 19** (doc_id: `deanon_BFG_TRAIN/137506.1`) (sent_id: `deanon_BFG_TRAIN/137506.1_23`)


Auch der Verstoß u.a. gegen Verordnungen der  EU ist eine Vertragsverletzung (vgl. aaO, § 258 Rn. 4 f.).   Art. 260 Abs. 1 AEUV bestimmt: „Stellt der Gerichtshof der Europäischen Union fest,  dass ein Mitgliedstaat gegen eine Verpflichtung aus den Verträgen verstoßen hat, so  hat dieser Staat die Maßnahmen zu ergreifen, die sich aus dem Urteil des Gerichtshofs  ergeben.“

**False Positives:**

- `Verordnungen der  EU ist eine Vertragsverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/137514.1`) (sent_id: `deanon_BFG_TRAIN/137514.1_11`)


Mit Schreiben vom 22.03.2022 erhob der Bf. dagegen Beschwerde und führte dazu aus, dass er  seine Beschwerde nachweislich am 09.12.2021 an die Poststelle der Justizanstalt übergeben  habe und daher Rechtzeitigkeit gegeben sei.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/137693.1`) (sent_id: `deanon_BFG_TRAIN/137693.1_53`)


Mit der Äußerung wurde die  Kopie einer gekürzten Urteilsausfertigung des Landesgerichts Innsbruck im Verfahren der P  GmbH gegen T vorgelegt.

**False Positives:**

- `T vorgelegt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/138506.1`) (sent_id: `deanon_BFG_TRAIN/138506.1_31`)


Da jeder dieser Bescheide gesondert anfechtbar ist (§ 243 BAO), muss jede Beschwerde für sich  den Formalerfordernissen der BAO für Rechtsbehelfe gegen Bescheide entsprechen.

**False Positives:**

- `Bescheide entsprechen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/138984.1`) (sent_id: `deanon_BFG_TRAIN/138984.1_16`)


Ein unehrliches steuerliches Verhalten des Bf. dokumentiere auch der gegen Jahresende 2010  erhobene Umstand, dass der Bf. einen PKW mit ausländischem (italienischem) Kennzeichen in  Österreich benutzte, weswegen er als steuerliche Konsequenz im Bereich NOVA und KFZ-

**False Positives:**

- `Jahresende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/138984.1`) (sent_id: `deanon_BFG_TRAIN/138984.1_126`)


17. Allein der nach Ansicht der Amtspartei ein unehrliches steuerliches Verhalten des Bf.  dokumentierende gegen Jahresende 2010 erhobene Umstand, dass der Bf. einen PKW mit  ausländischem (italienischen) Kennzeichen in Österreich nutzte, weswegen er als steuerliche  9 von 11 Seite 10 von 11

**False Positives:**

- `Jahresende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/140025.1`) (sent_id: `deanon_BFG_TRAIN/140025.1_14`)


Die ausständigen Erklärungen und Daten bezüglich der Mängelbescheide und diverser  eingebrachter Beschwerden (gegen Einkommensteuer 2019 und 2020, Umsatzsteuer 2019 und  2020, Verspätungszuschlag 2019 und 2020) würden bis 25. Oktober 2022 ganz sicher  nachgereicht werden.

**False Positives:**

- `Einkommensteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/140298.1`) (sent_id: `deanon_BFG_TRAIN/140298.1_5`)


Mit Schreiben vom 19. November 2022 brachte die Beschwerdeführerin über Finanzonline  dagegen Beschwerde ein.

**False Positives:**

- `Beschwerde ein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_65`)


10. Wohnraumvermieter überlassen Wohnraum zur in der Regel ausschließlichen Nutzung  durch ihre Mieter auf eine bestimmte Zeit gegen Entgelt.

**False Positives:**

- `Entgelt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_178`)


In Bezug auf die Frage der Ansässigkeit gemäß MwStSystRL bei einer Wohnungsvermietung  ist zudem darauf zu verweisen, dass Generalanwältin Kokott im EuGH-Verfahren Ingrid  Schmelz gegen Finanzamt Waldviertel, Rechtssache C-97/09, erklärte, Frau Schmelz, eine  deutsche Staatsbürgerin mit Wohnsitz in Deutschland, welche in Ostösterreich eine Wohnung  vermietet hatte, habe gemäß der Mehrwertsteuersystemrichtlinie als in Österreich ansässige  Person zu gelten (vgl. Endfellner, FJ 2010, 270, zweitletzter Aufzählungspunkt).

**False Positives:**

- `Finanzamt Waldviertel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/141765.1`) (sent_id: `deanon_BFG_TRAIN/141765.1_34`)


7. Das Bundesfinanzgericht (BFG) hatte – nach Direktvorlage - mit Erkenntnis vom 13.12.2016,  RV/3101114/2016, die Beschwerde als unbegründet abgewiesen und im Wesentlichen dahin  begründet:  Wird ein Baurecht an einem unbebauten Grundstück gegen Entgelt (hier die Leistung eines  jährlichen Bauzinses) auf 50 Jahre begründet, dann bemißt sich die Grunderwerbsteuer  ausgehend von der Gegenleistung, di. vom Wert der Bauzinsverpflichtung gemäß § 15 BewG (=  18facher Jahreswert des Entgelts; vgl.

**False Positives:**

- `Entgelt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_Herrn`

**F1:** 0.010 | **Precision:** 0.060 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `94942c84`  
**Description:**
Captures full names following 'Herrn' (accusative/dative), ensuring the full name including suffixes is extracted.

**Content:**
```
(?:Herrn|Herr)\s+([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=\s+(?:in|von|der|des|\(|$|\d{4}|\s+\d|Gattin|und))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.060 | 0.005 | 0.010 | 150 | 9 | 141 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 141 | 1627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Stanislaus Calisir (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Cynthia Neureuter  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Natascha Daschmann (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/138498.1`) (sent_id: `deanon_BFG_TRAIN/138498.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Im Rahmen der am 17.02.2020 eingereichten Erklärung zur Arbeitnehmerveranlagung 2019  wurde durch Herrn Zacharias Arhelger, BA (in der Folge „Bf“ oder „Beschwerdeführer“) die Gewährung des  (ganzen) Familienbonus Plus für 12 Monate beantragt.

| Predicted | Gold |
|---|---|
| `Zacharias Arhelger, BA` | `Zacharias Arhelger, BA` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_8`)


Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der  Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische  Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur  Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit  1 von 20 Seite 2 von 20

| Predicted | Gold |
|---|---|
| `Brunhild Hoffschulz` | `Brunhild Hoffschulz` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/141435.1`) (sent_id: `deanon_BFG_TRAIN/141435.1_4`)


Begründung  Verfahrensgang:  MA67/226701281451/2022:  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner  2023, Zahl: MA67/226701281451/2022, wurde Herr Robert Grentzmann (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von einem 14 Stunden verhängt sowie ein  Verfahrenskostenbeitrag von € 10,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Robert Grentzmann` | `Robert Grentzmann` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/142976.1`) (sent_id: `deanon_BFG_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Nikolaus Thulke (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Nikolaus Thulke` | `Nikolaus Thulke` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_6`)


Entscheidungsgründe  Mit Straferkenntnis vom 16. April 2024, Zahl: MA67/246700162299/2024, hat der Magistrat  der Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Leonhard Facci (in weiterer  Folge: Beschwerdeführer – Bf) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt  indem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen I-57 VS  am  2. Februar 2024 um 09:20 Uhr in einer gebührenpflichtigen Kurzparkzone in 1210 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `I-57 VS` (vehicle_license)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_5`)


III. Gemäß § 185 Abs.1 lit. a und b FinStrG hat Herrn J. die Kosten des verwaltungsbehördlichen und verwaltungsgerichtlichen Finanzstrafverfahrens in unveränderter Höhe von € 500,00 zu tragen.

**False Positives:**

- `J. die Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_9`)


Entscheidungsgründe Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg vom 8. Juni 2016, SpS 16, wurde Herr J. (in weiterer Folge: Beschuldigter), geb., österreichischer Staatsbürger, Geschäftsführer, aufhältig in Dohnalstraße 26, 8294 Steinbüchl, Österreich, in Abwesenheit schuldig erkannt, er habe im Bereich des Finanzamtes Wien 1/23 als für die Wahrnehmung der abgabenrechtlichen Obliegenheiten der A-GmbH vorsätzlich a) durch die verspätete Abgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Anzeige- ‚ Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von € 2.403,50 zu verkürzen versucht, b) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2014, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2014 in Höhe von € 11.919,91 zu verkürzen versucht, c) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG entsprechenden Voranmeldungen Verkürzungen von Vorauszahlungen an Umsatzsteuer für 02/2015 in Höhe von € 520,51, 04 – 05 /2015 in Höhe von € 3.814,30 bewirkt, wobei er den Eintritt der Verkürzungen nicht nur für möglich, sondern für gewiss gehalten habe, d) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

**False Positives:**

- `J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dohnalstraße 26, 8294 Steinbüchl, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_73`)


Dazu können die Herrn Mag. Y. und der Steuerberater, die in der Zeit vor Konkurseröffnung mit der Finanz Gespräche zur Verhinderung geführt haben, als Zeugen berichten.

**False Positives:**

- `Mag. Y.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/128762.1`) (sent_id: `deanon_BFG_TRAIN/128762.1_11`)


(Vertragsabwicklung) ist festgehalten, dass die Käufer Herrn RA mit der  Errichtung, treuhändigen Abwicklung und grundbücherlichen Durchführung dieses Vertrages  beauftragen.

**False Positives:**

- `RA mit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_25`)


Laut eigenen Aussagen ist Herr AB ein begeisterter Motorradfahrer und  nützt jede Gelegenheit, diesem Hobby nachzugehen.

**False Positives:**

- `AB ein begeisterter Motorradfahrer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_25`)


Die Bf. nannte der AP als Ansprechperson bei der M-GmbH einen Herr K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion und war weder bei der M-GmbH noch deren  Vorgängerin, der P-GmbH angestellt.

**False Positives:**

- `K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_45`)


Es lasse  sich nicht ableiten, wie Herr K. in den Genuss der „Vorteilszuwendung“ gekommen sei, da die  Rechnung durch die M-GmbH ausgestellt und der Betrag an diese überwiesen worden sei.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_71`)


Herr K. war weder im Jahr 2007, vor dem  Gesellschafterwechsel, noch im Jahr 2008 beim genannten Unternehmen angestellt oder  4 von 6 Seite 5 von 6

**False Positives:**

- `K. war weder im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/130697.1`) (sent_id: `deanon_BFG_TRAIN/130697.1_75`)


In der Verhandlung vor dem BFG wurde nach dem überwiegend wiederholenden Vorbringen  des Bf., Herr Z, Kontrollorgan der MA 67 der Landespolizeidirektion Wien, als Zeuge und zwar  zu folgendem Beweisthema vernommen:   Abstellen des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna am 12.  Dezember 2019 um 14:52 Uhr in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Simmeringer Hauptstraße 59 - 61.

**False Positives:**

- `Z, Kontrollorgan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_117`)


Herr C ist 1985  nach Österreich zurückgekehrt, Frau Bf hat ihren deutschen Hauptwohnsitz hingegen  beibehalten.

**False Positives:**

- `C ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_130`)


Die Befragung durch die FinPol und auch die Kontakte mit dem für Strafverfügungen  zuständigen Referenten bei der BH xxx, Herrn G, hat sie als sehr belastend empfunden, weshalb  es zu inhaltlich unrichtigen Protokoll-Textierungen gekommen ist.

**False Positives:**

- `G, hat sie als sehr belastend empfunden, weshalb  es zu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_6`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 20. Februar 2019,  Strafnummer 007, wurde Herr Ronald Kleile, Bakk. rer. nat., geb. 1989, Geschäftsführer, wohnhaft in Fischteichweg 49, 4924 Hartlberg, Österreich  in Abwesenheit schuldig erkannt,   „A.) er hat in Wien vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von  1 von 18 Seite 2 von 18

**False Positives:**

- `Ronald Kleile, Bakk. rer. nat., geb.` — partial — gold is substring of pred: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_152`)


In den  Mietverträgen aller vier im Jahr 2017 von der H- GmbH betriebenen Geschäftslokale scheint  nicht die Gesellschaft, sondern Hr. S. als Mieter auf, obwohl die GmbH bereits existierte und  Herr S. im Zeitpunkt der Vertragsabschlüsse seine Tätigkeit im Textilhandel durch Zurücklegung  der Gewerbeberechtigung bereits beendet hatte.

**False Positives:**

- `S. im Zeitpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_158`)


Herr S. leistet seit 2015 weder USt-Vorauszahlungen noch reicht  er UVAs und Jahreserklärungen ein.

**False Positives:**

- `S. leistet seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_161`)


Zwischen Herrn Ronald Kleile, Bakk. rer. nat., Alleingesellschafter und einziger Geschäftsführer der H- GmbH und  Herrn S., seinem Vater, bestand und besteht nicht nur eine persönliche, sondern auch eine  wirtschaftliche Nahebeziehung.

**False Positives:**

- `Ronald Kleile, Bakk. rer. nat., Alleingesellschafter` — partial — gold is substring of pred: `Ronald Kleile, Bakk. rer. nat.`
- `S., seinem Vater, bestand` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 15** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_174`)


Gemäß § 12 Abs. 14 UStG werden daher folgende Vorsteuern nicht zum Abzug zugelassen:   2017: 24.338,38  2018: 2.557,16  Darüber hinaus ist das behauptete Mietverhältnis zwischen Herrn S. und der H- GmbH, deren  Alleingesellschafter und -geschäftsführer der Beschuldigte ist, auch unter dem Gesichtspunkt,  dass es sich um vertragliche Beziehungen zwischen nahen Angehörigen handelt, zu prüfen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_19`)


2 Erbrachte Leistungen  J.N.  Da jedoch, wie oben erwähnt, die Leistungen von Herrn J.N. erbracht wurden, ist der bezahlte  Bruttoaufwand i.H.v. 20.000,-- als Betriebsausgabe zu berücksichtigen.

**False Positives:**

- `J.N. erbracht wurden, ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_42`)


Aufgrund von Erhebungen konnte festgestellt werden, dass durch Herrn J.N. von X beauftragte  Leistungen, wie Malerarbeiten und Räumungen erbracht wurden.

**False Positives:**

- `J.N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_10`)


In der angeführten Bestätigung des Arbeitgebers des Bf. (X) vom 19.10.2015 wird wie folgt  ausgeführt:  "Wir bestätigen, dass Herr Bf. , wohnhaft in AdrBf  von 11.3.2013 bis 30.9.2015 in unserem Unternehmen im Bereich Energieberatung tätig war.

**False Positives:**

- `Bf. , wohnhaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_21`)


Das Schreiben des Dienstgebers des Bf. vom 9.2.2016 lautete wie folgt:  „Ergänzend zu unserem Schreiben von 1.12.2015 können wir bestätigen, dass der maßgebliche  Bestandteil der Tätigkeit von Herrn Bf. die Abwicklung von Geschäftsabschlüssen ist.

**False Positives:**

- `Bf. die Abwicklung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_22`)


Herr Bf. unterliegt einer Zielvereinbarung, welche im Wesentlichen auf die Abwicklung von  Geschäftsabschlüssen basiert.“

**False Positives:**

- `Bf. unterliegt einer Zielvereinbarung, welche im Wesentlichen auf die Abwicklung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_75`)


Als Beispiel ist das bereits zweimal  stattgefundene Verkaufstraining mit Herrn Hubert Mann zu nennen (siehe Beilagen).

**False Positives:**

- `Hubert Mann zu nennen` — partial — gold is substring of pred: `Hubert Mann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert Mann`(person)

**Example 22** (doc_id: `deanon_BFG_TRAIN/132647.1`) (sent_id: `deanon_BFG_TRAIN/132647.1_17`)


1) Höhe der 2014 in Österreich Steuerpflichtigen Bezüge aus nicht selbständiger Arbeit   Herr Bf. erzielte auch in 2014 Einkünfte aus nichtselbständiger Arbeit als angestellter  Staatsanwalt aus Dienstverhältnissen zu zwei Schweizer Körperschaften öffentlichen Rechtes  (Kanton Nidwalden und Bund).

**False Positives:**

- `Bf. erzielte auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/132870.1`) (sent_id: `deanon_BFG_TRAIN/132870.1_16`)


Im Zeitraum September 2008 bis Jänner 2009 habe der Gesellschafter  Herr EK insgesamt € 205.000,- in vier Teilbeträgen auf das Konto der Bf einbezahlt, da die  Gesellschaft nicht über die entsprechenden Mittel verfügt hätte, den Umbau zu finanzieren.

**False Positives:**

- `EK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/132996.1`) (sent_id: `deanon_BFG_TRAIN/132996.1_21`)


In diesem Antrag führte der Bf. aus, dass er in den Zeiträumen 2009 bis 2012 durch den WTH  Herrn M steuerlich vertreten gewesen sei, der gemäß Auftrag die monatliche Buchhaltung, den  Jahresabschluss und die Steuerklärungen erstellen sollte.

**False Positives:**

- `M steuerlich vertreten gewesen sei,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_35`)


Herr A und Herr B fungierten im Beschwerdezeitraum weiters als deren handelsrechtliche  Geschäftsführer.

**False Positives:**

- `A und Herr B fungierten im Beschwerdezeitraum weiters als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_43`)


Herr C schied in der Folge per xx.2012 als unbeschränkt haftender  Gesellschafter aus, welche Funktion er jedoch per xx.2016 wieder aufnahm.

**False Positives:**

- `C schied` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_88`)


Wie Herr B im Zuge der mündlichen Verhandlung vom 06.07.2021  (ho Verfahren zu RV/4100093/2018 und RV/4100775/2018) dazu anmerkte, habe er bei seiner  Tätigkeit iZm der Managementvereinbarung einzig den „Konzern Hut“ getragen.

**False Positives:**

- `B im Zuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_95`)


Die festgestellte Leistungserbringung geht aus den Ausführungen des Herr B hervor, der auf  Frage des Gerichtes in der bezeichneten Verhandlung in den Parallelverfahren glaubwürdig  und nachvollziehbar den Arbeitsablauf und die Aufteilung darlegte.

**False Positives:**

- `B hervor,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_104`)


All diese Prämissen vorausgeschickt, bestand aufgrund des durchgeführten  Beweisverfahrens keinerlei Veranlassung, an den diesbezüglichen Ausführungen der Bf. zu  zweifeln: Herr B schilderte sein enormes Arbeitspensum vor der Umstrukturierungsphase in  einen Konzern (vgl. dazu VH Protokoll vom 06.07.2021 zu RV/4100093/2018 und  RV/4100775/2018, S. 5, wonach er wörtlich „herumgeflogen [sei], wie ein Depperter“).

**False Positives:**

- `B schilderte sein enormes Arbeitspensum vor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Representative_vertreten_durch`

**F1:** 0.008 | **Precision:** 0.052 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `aca7d129`  
**Description:**
Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+GmbH|\s+Steuerberatung|\s+OG|\s+KG|\s+Rechtsanwalts|\s+PartG|\s+StbG|\s+\(|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.052 | 0.004 | 0.008 | 134 | 7 | 127 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 7 | 127 | 1627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/133177.1`) (sent_id: `deanon_BFG_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Podzus  in der Beschwerdesache der  Planung Monuniost, Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich, vertreten durch Ilona Christahl,  Beschlingerstraße 66, 3233 Schlögelsbach, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ilona Christahl` | `Ilona Christahl` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Juliana Podzus` (person)
- `Planung Monuniost` (organisation)
- `Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich` (address)
- `Beschlingerstraße 66, 3233 Schlögelsbach, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/133706.1`) (sent_id: `deanon_BFG_TRAIN/133706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gloria Andres, Fuchshub 19, 4204 Aigen, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die Beschwerde vom  3. Juli 2015 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 29. Mai 2015  betreffend Anspruchszinsen (§ 205 BAO) 2003, 2004, 2005 und 2006 zu Steuernummer  06-338/7966  zu Recht erkannt:   I. Die angefochtenen Bescheide werden - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Gloria Andres` (person)
- `Fuchshub 19, 4204 Aigen, Österreich` (address)
- `06-338/7966` (tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/136313.1`) (sent_id: `deanon_BFG_TRAIN/136313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger im  Beschwerdeverfahren über die Beschwerde der Verl nach XY, vertreten durch Laurence Krekemeyer,  Steyersberg 2, 8481 Priebing, Österreich  vom 20. Juli 2021 gegen den Zurückweisungsbescheid des Finanzamtes  Österreich vom 7. Juli 2021 betreffend Antrag auf Durchführung einer  Arbeitnehmerveranlagung, beschlossen:  Der Vorlageantrag der Beschwerdeführerin Verl nach XY vom 10.9.2021 wird gemäß § 260 Abs.  1 BAO iVm § 264 BAO (insbesondere Abs. 4 lit e und Abs. 5) als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Laurence Krekemeyer` | `Laurence Krekemeyer` |

**Missed by this rule (FN):**

- `Dr. Ansgar Unterberger` (person)
- `Steyersberg 2, 8481 Priebing, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/137275.1`) (sent_id: `deanon_BFG_TRAIN/137275.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Carla Schweykart, Saaz 45, 8413 Stiefing, Österreich, vertreten durch Dr. Elmar Kresbach LL.M., Rechtsanwalt,  Wipplingerstraße 29/9, 1010 Wien, vom 7. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. April 2022, Zl. Zahl, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Elmar Kresbach LL.M.` | `Dr. Elmar Kresbach LL.M.` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Carla Schweykart` (person)
- `Saaz 45, 8413 Stiefing, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/141417.1`) (sent_id: `deanon_BFG_TRAIN/141417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Louisa Luppert  in der Beschwerdesache Vera Hempel,  Schnepfengasse 38, 9161 Ehrensdorf, Österreich  vertreten durch Elvira Postel, Waldpark 180, 3214 Wohlfahrtsschlag, Österreich, über die Beschwerde vom  4. Jänner 2023 gegen den Bescheid des Finanzamtes Österreich vom 5. Dezember 2022  betreffend Abweisung eines Aussetzungsantrages gem. § 212a BAO betreffend  Säumniszuschlag, Steuernummer 36-933/4246, nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elvira Postel` | `Elvira Postel` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Louisa Luppert` (person)
- `Vera Hempel` (person)
- `Schnepfengasse 38, 9161 Ehrensdorf, Österreich` (address)
- `Waldpark 180, 3214 Wohlfahrtsschlag, Österreich` (address)
- `36-933/4246` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/145403.1`) (sent_id: `deanon_BFG_TRAIN/145403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Sven Siemglüß  in der Beschwerdesache Josefine Schrörs,  Niesenbergergasse 8, 9831 Innerfragant, Österreich, vertreten durch Dr.in Rita Leinhos, Gladiolengasse 40, 4864 Breitenröth, Österreich, über die Beschwerde vom  13. Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 8. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2022 Steuernummer 03-666/4395  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Rita Leinhos` | `Dr.in Rita Leinhos` |

**Missed by this rule (FN):**

- `Mag. Sven Siemglüß` (person)
- `Josefine Schrörs` (person)
- `Niesenbergergasse 8, 9831 Innerfragant, Österreich` (address)
- `Gladiolengasse 40, 4864 Breitenröth, Österreich` (address)
- `03-666/4395` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Catharina Moewis,  Im Klosterhof 21N, 5241 Großenaich, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Moewis`(person)
- `Im Klosterhof 21N, 5241 Großenaich, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Mercuria Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Lubomir Baltßun`(person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Wolfgang Freudelsperger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129254.1`) (sent_id: `deanon_BFG_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache StR VetR Corbinian Drügemöller, Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grant Thornton Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.Dr. Thomas Leitner`(person)
- `StR VetR Corbinian Drügemöller`(person)
- `Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe,  Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

**False Positives:**

- `Johann Putzer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Irene van der Hoven`(person)
- `Kordelia van Clewe`(person)
- `Piettegasse 15, 3341 Oberamt, Österreich`(address)
- `FA Tirol Ost`(organisation)
- `20-364/1486`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `ICON Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Vivian Wenk`(person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Westra ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pastel Pharma`(organisation)
- `Retzenegg 222, 3242 Ramsau, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129872.1`) (sent_id: `deanon_BFG_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache James Loratis, Platzerweg 28, 4673 Baumgarting, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Gugenberger Barbara` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang Freilinger`(person)
- `James Loratis`(person)
- `Platzerweg 28, 4673 Baumgarting, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Margot Artner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daisy Mikoleizik`(person)
- `Schulwiesen 13, 4203 Stratreith, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Elke Hager` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang Aigner`(person)
- `Wladimir Nüssli`(person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

**False Positives:**

- `Helmut Binder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alfred Klaming`(person)
- `Matthäus Buskens`(person)
- `Edlach 19, 3141 Oberkilling, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/130834.1`) (sent_id: `deanon_BFG_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `BKS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/130839.1`) (sent_id: `deanon_BFG_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Zarin Finke,  Brauhausplatz 29, 9422 Untereberndorf, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Rupert Karl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zarin Finke`(person)
- `Brauhausplatz 29, 9422 Untereberndorf, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/130895.1`) (sent_id: `deanon_BFG_TRAIN/130895.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Priv.-Doz. Univ.-Prof. Ernst Uckermarck  über die Vorlageerinnerung der  Erich Ennulat, Leumühle 11, 4680 Leiten, Österreich  vertreten durch Hedwig Weber, Ausseer Straße 32, 8940 Liezen, vom  22.10.2020 zur Beschwerde vom 06.05.2020 gegen den Bescheid des Finanzamtes Judenburg  Liezen vom 01.04.2020 betreffend Sicherstellung gemäß § 232 BAO beschlossen:  Die Vorlageerinnerung wird als unzulässig zurückgewiesen.

**False Positives:**

- `Hedwig Weber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Univ.-Prof. Ernst Uckermarck`(person)
- `Erich Ennulat`(person)
- `Leumühle 11, 4680 Leiten, Österreich`(address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Jean Wohlrap, Weyprechtgasse 44M, 9701 Nußdorf, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Astoria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Jean Wohlrap`(person)
- `Weyprechtgasse 44M, 9701 Nußdorf, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Samuel Rehnke` — partial — pred is substring of gold: `Samuel Rehnke, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottfried Bremermann`(person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich`(address)
- `Samuel Rehnke, BSc`(person)
- `Planetengasse 30, 8455 Bischofegg, Österreich`(address)
- `14-141/9449`(tax_number)

**Example 16** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Jeanne von Fritz  in der Beschwerdesache Martha Michenfelder,  Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Dkfm.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Univ.-Prof.in Jeanne von Fritz`(person)
- `Martha Michenfelder`(person)
- `Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich`(address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/131368.1`) (sent_id: `deanon_BFG_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Dr. Zlatan Kappelsberger, Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `LeitnerLeitner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Zlatan Kappelsberger`(person)
- `Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich`(address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Intercura Teuhand Revisions ` — partial — pred is substring of gold: `Intercura Teuhand Revisions  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karen Vennemeyer`(person)
- `Neu-Reinbach 11, 4693 Fallholz, Österreich`(address)
- `Intercura Teuhand Revisions  GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_TRAIN/131567.1`) (sent_id: `deanon_BFG_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Severin Wöllecke  in der Finanzstrafsache gegen die  Beschuldigte Nicole Schlemper, Uteweg 12, 9624 Latschach, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

**False Positives:**

- `Mag. Heinz Wolfbauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Severin Wöllecke`(person)
- `Nicole Schlemper`(person)
- `Uteweg 12, 9624 Latschach, Österreich`(address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/132255.1`) (sent_id: `deanon_BFG_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Chen Helwig  in der Beschwerdesache Roxana Gehrbrandt,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr Christian Leskoschek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Chen Helwig`(person)
- `Roxana Gehrbrandt`(person)

**Example 21** (doc_id: `deanon_BFG_TRAIN/132752.1`) (sent_id: `deanon_BFG_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Manuel de Keijzer, Schmieddorf 5, 6215 Achenkirch, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Maria Brandstetter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manuel de Keijzer`(person)
- `Schmieddorf 5, 6215 Achenkirch, Österreich`(address)

**Example 22** (doc_id: `deanon_BFG_TRAIN/132794.1`) (sent_id: `deanon_BFG_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Edwin Uebel, Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Dkfm.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Edwin Uebel`(person)
- `Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/132893.1`) (sent_id: `deanon_BFG_TRAIN/132893.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Ute Höltje, Burghof 44, 5222 Spreitzenberg, Österreich, vertreten durch KAPAS Steuerberatung GmbH, Birkfelder Straße 25, 8160 Weiz, über  die Beschwerde vom 19.12.2019 gegen den Bescheid des Finanzamtes FA vom 13.05.2020  betreffend Feststellung von Einkünften gemäß § 188 BAO 2018 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `KAPAS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ute Höltje`(person)
- `Burghof 44, 5222 Spreitzenberg, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/133172.1`) (sent_id: `deanon_BFG_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Hon.-Prof.in Lena Ünlüer, Modsiedl 8, 4150 Katzing, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 51-253/7194  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Uniconsult` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Lena Ünlüer`(person)
- `Modsiedl 8, 4150 Katzing, Österreich`(address)
- `51-253/7194`(tax_number)

**Example 25** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Huberta Schwandt, Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 30-672/6934  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Commendatio Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Huberta Schwandt`(person)
- `Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich`(address)
- `30-672/6934`(tax_number)

**Example 26** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwalt Mag. Wolfgang Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/133873.1`) (sent_id: `deanon_BFG_TRAIN/133873.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die als  Bescheidbeschwerde zu erledigende Berufung vom 21.02.2011 der Xy, Emil Zöchling-Gasse 149, 9063 Rosendorf, Österreich  vertreten durch Dr. Hans Bodendorfer Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010  Wien, gegen den Einkommensteuerbescheid für das Jahr 2005 des Finanzamtes Bruck  Eisenstadt Oberwart vom 29.11.2010, Steuernummer 66-205/7303   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hans Bodendorfer` — partial — pred is substring of gold: `Dr. Hans Bodendorfer Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Emil Zöchling-Gasse 149, 9063 Rosendorf, Österreich`(address)
- `Dr. Hans Bodendorfer Steuerberatungsges.m.b.H.`(organisation)
- `66-205/7303`(tax_number)

**Example 28** (doc_id: `deanon_BFG_TRAIN/134099.1`) (sent_id: `deanon_BFG_TRAIN/134099.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lea Capoluongo  in der Beschwerdesache Rupert Lübbersmeyer,  Peter-Tunner-Straße 84, 3601 Oberloiben, Österreich, vertreten durch Stb Gerhard Obrist, Hans-Schrott-Fiechtl-Straße 30, 6134  Vomp, über die Beschwerde vom 14.1.2011 gegen den Bescheid des FA Kufstein Schwaz  (nunmehr FA Österreich) vom 15.12.2010, StrNr, betreffend 1. Festsetzung der  Normverbrauchsabgabe für den Zeitraum Oktober 2008 und   2.

**False Positives:**

- `Stb Gerhard Obrist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Lea Capoluongo`(person)
- `Rupert Lübbersmeyer`(person)
- `Peter-Tunner-Straße 84, 3601 Oberloiben, Österreich`(address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/134507.1`) (sent_id: `deanon_BFG_TRAIN/134507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Dipl.-Ing. Xaver Kühlwetter, Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich, vertreten durch Dr. Ferdinand Jenni, Jahngasse 18, 6850  Dornbirn, über die Beschwerde vom 10. November 2014 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Oktober 2014 betreffend Einkommensteuer 2013, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Ferdinand Jenni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Josef Ungericht`(person)
- `Dipl.-Ing. Xaver Kühlwetter`(person)
- `Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich`(address)

</details>

---

## `Name_Representative`

**F1:** 0.012 | **Precision:** 0.039 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `90e1f5a6`  
**Description:**
Captures names following 'vertreten durch' (represented by).

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.039 | 0.007 | 0.012 | 304 | 12 | 292 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 12 | 292 | 1624 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/133177.1`) (sent_id: `deanon_BFG_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Podzus  in der Beschwerdesache der  Planung Monuniost, Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich, vertreten durch Ilona Christahl,  Beschlingerstraße 66, 3233 Schlögelsbach, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ilona Christahl` | `Ilona Christahl` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Juliana Podzus` (person)
- `Planung Monuniost` (organisation)
- `Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich` (address)
- `Beschlingerstraße 66, 3233 Schlögelsbach, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/133706.1`) (sent_id: `deanon_BFG_TRAIN/133706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gloria Andres, Fuchshub 19, 4204 Aigen, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die Beschwerde vom  3. Juli 2015 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 29. Mai 2015  betreffend Anspruchszinsen (§ 205 BAO) 2003, 2004, 2005 und 2006 zu Steuernummer  06-338/7966  zu Recht erkannt:   I. Die angefochtenen Bescheide werden - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Gloria Andres` (person)
- `Fuchshub 19, 4204 Aigen, Österreich` (address)
- `06-338/7966` (tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/135177.1`) (sent_id: `deanon_BFG_TRAIN/135177.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Rüdiger Piotrowska  in der Beschwerdesache Ilhan Bartenschläger,  Bärngarten 834, 4212 Zissingdorf, Österreich, vertreten durch Egon Kohlschmied, betreffend die Beschwerde vom  4. Dezember 2015 gegen die Bescheide des Finanzamt Grieskirchen Wels (jetzt Finanzamt Österreich) vom  6. November 2015 zu Steuernummer 64-279/2417  betreffend Anspruchszinsen (§ 205  BAO) 2009, Anspruchszinsen (§ 205 BAO) 2013, Wiederaufnahme § 303 BAO /  ESt 2009,  Wiederaufnahme § 303 BAO /  ESt 2010, Wiederaufnahme § 303 BAO /  ESt 2011,  Wiederaufnahme § 303 BAO /  ESt 2012, Wiederaufnahme § 303 BAO /  USt 2009,  Wiederaufnahme § 303 BAO /  USt 2010, Wiederaufnahme § 303 BAO /  USt 2011 und  Wiederaufnahme § 303 BAO /  USt 2012   beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Egon Kohlschmied` | `Egon Kohlschmied` |

**Missed by this rule (FN):**

- `Mag. Rüdiger Piotrowska` (person)
- `Ilhan Bartenschläger` (person)
- `Bärngarten 834, 4212 Zissingdorf, Österreich` (address)
- `Finanzamt Grieskirchen Wels` (organisation)
- `64-279/2417` (tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/135479.1`) (sent_id: `deanon_BFG_TRAIN/135479.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Ali Dill, Hauswiesenweg 8, 4702 Bergern, Österreich, vertreten durch Wendelin Spätling,  Wasserturmstraße 114, 6791 Gortipohl, Österreich, betreffend die Beschwerde vom 6. Mai 2020 gegen den Bescheid  des Finanzamtes Neunkirchen Wr. Neustadt vom 26. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zur Steuernummer 81-336/9133  beschlossen:  I. Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) vom 28. Dezember 2020 wird gemäß § 264 Abs. 4 lit. e iVm § 260 Abs. 1 lit. b  iVm § 264 Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wendelin Spätling` | `Wendelin Spätling` |

**Missed by this rule (FN):**

- `Mag. Markus Knechtl LL.M.` (person)
- `Ali Dill` (person)
- `Hauswiesenweg 8, 4702 Bergern, Österreich` (address)
- `Wasserturmstraße 114, 6791 Gortipohl, Österreich` (address)
- `81-336/9133` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_0`)


GZ. RV/7300048/2016 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen Herrn J., geb., Wien, vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/10, 1060 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten gemäß §§ 33 Abs. 1 und Abs. 2 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom 1. August 2016 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  8. Juni 2016 , SpS 16, nach Durchführung einer mündlichen Verhandlung  am 10. Jänner 2017 in Anwesenheit des Beschuldigten, seines Verteidigers, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt: Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des Spruchsenates vom 8. Juni 2016, SpS 16, wie folgt abgeändert: I. Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer 002 anhängige Finanzstrafverfahren wird hinsichtlich des Verdachts, Herr J. hätte  vorsätzlich a) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von€ 2.403,50  zu verkürzen versucht und dadurch eine versuchte Abgabenhinterziehung gemäß §§ 13, 33 Abs. 1 FinStrG begangen, b) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden Voranmeldungen die Vorauszahlung von Umsatzsteuer für 4/2015 in Höhe von € 900,00 bewirkt und  dadurch eine Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a FinStrG begangen, c) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

**False Positives:**

- `Brehm ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_1`)


Gerald Erwin Ehgartner in der Beschwerdesache Janis Forch, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Jank Weiler Operenyi Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janis Forch`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Erika Zajcenko, Volksheimstraße 9, 8784 Trieben, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Monika Pfundner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erika Zajcenko`(person)
- `Volksheimstraße 9, 8784 Trieben, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Catharina Moewis,  Im Klosterhof 21N, 5241 Großenaich, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Moewis`(person)
- `Im Klosterhof 21N, 5241 Großenaich, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128762.1`) (sent_id: `deanon_BFG_TRAIN/128762.1_43`)


Mit Beschluss  vom 4. Dezember 2019, dem Bundesfinanzgericht zugestellt am 19. Dezember 2019, hatte  der Verwaltungsgerichtshof die außerordentliche Revision des betreffenden  Abgabepflichtigen, wie der Bf vertreten durch RA, zurückgewiesen.

**False Positives:**

- `RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_2`)


Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Elisabeth Tombült,  Landschacher Gasse 33, 3925 Neumelon, Österreich, vertreten durch Dr. Edelsbacher & Partner Wirtschaftsprüfungs- und Steuer-  beratungsgesellschaft mbH, Ernst-Grein-Straße 14A, 5026 Salzburg, betreffend Beschwerde  vom 17. Juli 2019 gegen den Bescheid des Finanzamtes vom 18. Juni 2019 über die Festsetzung  von Anspruchszinsen (§ 205 BAO) 2016 beschlossen:  Der Vorlageantrag vom 15.06.2020 wird gemäß § 260 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e  BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Elisabeth Tombült`(person)
- `Landschacher Gasse 33, 3925 Neumelon, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Serge Anhalt, Ebenfeld 7, 4776 Mitterndorf, Österreich,  vertreten durch WP_GmbH, WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  44-050/5905  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `WP` — no gold match — likely missing annotation
- `Mag` — no gold match — likely missing annotation
- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Serge Anhalt`(person)
- `Ebenfeld 7, 4776 Mitterndorf, Österreich`(address)
- `44-050/5905`(tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_2`)


Kff. Gwendolin Ziehr,  Reebokplatz 60, 4083 Gemersdorf, Österreich, vertreten durch BG&P Binder Grossek & Partner Steuerberatung und  Wirtschafts- prüfung GmbH, Neufeldweg 93, 8010 Graz, über die Beschwerden vom 10. Juni  2015 gegen die Bescheide des Finanzamtes Graz-Umgebung vom 14. April 2015 betreffend  Festsetzung des Dienstgeberbeitrages (DB) und des Zuschlages zum Dienstgeberbeitrag (DZ)  für die Jahre 2009, 2010, 2011, 2012 und 2013, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `BG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Reebokplatz 60, 4083 Gemersdorf, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Raphael Skowroneck, MBA`(person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Mehmet Bildstein, Josef Glanner-Gasse 168, 3142 Obermoos, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 72-182/5875  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Imre ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alois Pichler`(person)
- `Mehmet Bildstein`(person)
- `Josef Glanner-Gasse 168, 3142 Obermoos, Österreich`(address)
- `72-182/5875`(tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Mercuria Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Lubomir Baltßun`(person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Eva Maria Koller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Markus Knechtl LL.M.`(person)
- `OStR Karl Ostendarp`(person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich`(address)
- `84-986/6948`(tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenV, die RichterinR sowie die  fachkundigen Laienrichter LR1 und LR2 in der Beschwerdesache Bf, Wilhelmsederstraße 93, 9112 Gönitz, Österreich, vertreten  durch Stb, über die Beschwerde vom 27. April 2015 gegen die Bescheide des Finanzamtes St.  Johann Tamsweg Zell am See vom 27. März 2015 betreffend Umsatzsteuer 2012 und  Umsatzsteuer 2013, Steuernummer 91-666/8239, nach Durchführung einer mündlichen  Verhandlung am 10. Juni 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wilhelmsederstraße 93, 9112 Gönitz, Österreich`(address)
- `91-666/8239`(tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129231.1`) (sent_id: `deanon_BFG_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Bartholomäus Malcharzik, Ogugasse 8, 4483 Pirchhorn, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `EWT Schuster ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bartholomäus Malcharzik`(person)
- `Ogugasse 8, 4483 Pirchhorn, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Elena Zilinski, Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Treuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Elena Zilinski`(person)
- `Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich`(address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129254.1`) (sent_id: `deanon_BFG_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache StR VetR Corbinian Drügemöller, Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grant Thornton Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.Dr. Thomas Leitner`(person)
- `StR VetR Corbinian Drügemöller`(person)
- `Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich`(address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe,  Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

**False Positives:**

- `Johann Putzer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Irene van der Hoven`(person)
- `Kordelia van Clewe`(person)
- `Piettegasse 15, 3341 Oberamt, Österreich`(address)
- `FA Tirol Ost`(organisation)
- `20-364/1486`(tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `ICON Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Vivian Wenk`(person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich`(address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Westra  GmbH Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pastel Pharma`(organisation)
- `Retzenegg 222, 3242 Ramsau, Österreich`(address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/129503.1`) (sent_id: `deanon_BFG_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache Gabriele Lemmon, Bakk. rer. nat., Graf-Egger-Straße 4, 4712 Armau, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 49-573/3569  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `Halpern ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gabriele Lemmon, Bakk. rer. nat.`(person)
- `Graf-Egger-Straße 4, 4712 Armau, Österreich`(address)
- `49-573/3569`(tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/129571.1`) (sent_id: `deanon_BFG_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Annemarie Cünzer, Kothbauerstraße 39, 4152 Mühel, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Annemarie Cünzer`(person)
- `Kothbauerstraße 39, 4152 Mühel, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/129872.1`) (sent_id: `deanon_BFG_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache James Loratis, Platzerweg 28, 4673 Baumgarting, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang Freilinger`(person)
- `James Loratis`(person)
- `Platzerweg 28, 4673 Baumgarting, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Shoshana Schweinforth, Brenggenalm 15, 8551 Gieselegg, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 78-461/2049  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vertreter ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Shoshana Schweinforth`(person)
- `Brenggenalm 15, 8551 Gieselegg, Österreich`(address)
- `78-461/2049`(tax_number)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daisy Mikoleizik`(person)
- `Schulwiesen 13, 4203 Stratreith, Österreich`(address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_188`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/130424.1`) (sent_id: `deanon_BFG_TRAIN/130424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Vivian Classens, Bakk. iur. BEd, Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich  vertreten durch Vertreter, gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 24. November 2015, betreffend Grunderwerbsteuer  aufgrund des Übergabsvertrages mit N.N. (Erf. Nr., Steuernummer), zu Recht erkannt:   Der eingeschränkten Beschwerde wird Folge gegeben.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vivian Classens, Bakk. iur. BEd`(person)
- `Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130444.1`) (sent_id: `deanon_BFG_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Lars Hoerl  in der Beschwerdesache VetR Christina Schlotfeldt,  Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Vedat Gökdemir` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof. Lars Hoerl`(person)
- `VetR Christina Schlotfeldt`(person)
- `Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich`(address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Cevik  in der Beschwerdesache der Bf., (im  Beschwerdeverfahren) vertreten durch Rechtsanwälte Lehofer & Lehofer,  Kalchberggasse 6/1.

**False Positives:**

- `Rechtsanwälte Lehofer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Lubomir Cevik`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Name_Von`

**F1:** 0.001 | **Precision:** 0.001 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `4031b52e`  
**Description:**
Captures names following 'von' (of/from) in contexts like 'Gutachten von'.

**Content:**
```
(?:von\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+\(|$|\s+\d{4}|\s+Gattin|\s+und|\s+Vermietung|\s+Zimmer)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.001 | 0.001 | 0.001 | 1846 | 2 | 1844 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 1844 | 1634 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/102855.1`) (sent_id: `deanon_BFG_TRAIN/102855.1_69`)


Nach dem klaren Gesetzeswortlaut steht jede Art von Unterhaltsleistung einem Eigenanspruch auf Familienbeihilfe entgegen.

**False Positives:**

- `Unterhaltsleistung einem Eigenanspruch auf Familienbeihilfe entgegen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_83`)


Gemäß § 33 Abs. 2 lit. a FinStrG macht sich einer Abgabenhinterziehung schuldig, wer vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von Umsatzsteuer (Vorauszahlungen oder Gutschriften) bewirkt und dies nicht nur für möglich, sondern für gewiß hält.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_140`)


Wesentliche Tatbestandmerkmale einer Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG sind in subjektiver Hinsicht das Vorliegen von zumindest Eventualvorsatz hinsichtlich der Unterlassung der Abgabe von dem § 21 UStG entsprechenden (rechtzeitigen, richtigen, vollständigen) Voranmeldungen und von Wissentlichkeit in Bezug auf die nicht zeitgerechte Entrichtung der Umsatzsteuervorauszahlungen.

**False Positives:**

- `Wissentlichkeit in Bezug auf die nicht zeitgerechte Entrichtung der Umsatzsteuervorauszahlungen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_143`)


Auch wenn der Beschuldigte angesichts der vorgehaltenen zahlreichen finanzstrafbehördlichen Vorstrafen von sich behauptet, kein Serientäter zu sein, sind dem Beschuldigten aufgrund seiner Tätigkeit als Sanierer seit Jahren die abgabenrechtlichen Pflichten zu den Fälligkeitstagen ebenso bekannt wie die Verpflichtung zur fristgerechten Einreichung von Umsatzsteuervoranmeldungen bzw. die Entrichtung von Umsatzsteuervorauszahlungen.

**False Positives:**

- `Umsatzsteuervoranmeldungen bzw. die Entrichtung von Umsatzsteuervorauszahlungen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_170`)


Angesichts des über Jahre gezeigten steuerunehrlichen Verhaltens darf der Beschuldigte auf die Bestimmung des § 15 Abs. 2 FinStrG aufmerksam gemacht werden, wonach bei Finanzvergehen, die nicht mit einer zwingend zu verhängenden Freiheitsstrafe bedroht sind, auf eine solche nur erkannt werden darf, wenn es ihrer bedarf, um den Täter von weiteren Finanzvergehen abzuhalten oder der Begehung von Finanzvergehen durch andere entgegenzuwirken.

**False Positives:**

- `Finanzvergehen durch andere entgegenzuwirken.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_51`)


Dem Einwand der Beschwerdeführerin, dass bloß ein nicht der Bestandvertragsgebühr unterliegender Vorvertrag vorliege, kann von Seiten des Bundesfinanzgerichtes nicht gefolgt werden.

**False Positives:**

- `Seiten des Bundesfinanzgerichtes nicht gefolgt werden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_104`)


Im Sinne des § 93 Abs. 3 lit a BAO hat ein Bescheid eine Begründung zu enthalten, wenn dieser  von Amts wegen erlassen worden ist.

**False Positives:**

- `Amts wegen erlassen worden ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_105`)


Der angefochtene Bescheid vom 19.3.2014 wurde von Amts wegen erlassen und u.a. damit  7 von 12 Seite 8 von 12

**False Positives:**

- `Amts wegen erlassen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_119`)


Gewerblich oder beruflich ist jede nachhaltige Tätigkeit zur Erzielung von  Einnahmen, auch wenn die Absicht, Gewinn (Überschuss) zu erzielen, fehlt oder eine  Personenvereinigung nur gegenüber ihren Mitgliedern tätig wird.

**False Positives:**

- `Einnahmen, auch wenn die Absicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_168`)


Es lag eine nachhaltige, selbständige Tätigkeit zur Erzielung von Einnahmen vor,  auch wenn die Absicht, Gewinn zu erzielen, fehlte.

**False Positives:**

- `Einnahmen vor,  auch wenn die Absicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_35`)


Eine Abänderung nach § 295 Abs 1 BAO ist nur jedoch nur zulässig, wenn die Bescheide  betreffend Einkommensteuer für die Streitjahre von Feststellungsbescheiden abzuleiten sind.

**False Positives:**

- `Feststellungsbescheiden abzuleiten sind.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_50`)


Der Transport von Unterlagen zur Schule sei nicht maßgeblich, denn es käme  lediglich auf die mögliche Benutzung von Verkehrsmitteln an.

**False Positives:**

- `Verkehrsmitteln an.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_86`)


Wie der Verwaltungsgerichtshof in seinem Erkenntnis vom 20.1.1999, 98/13/0132, ist der  Mittelpunkt einer Lehrtätigkeit nach der Verkehrsauffassung zweifellos jener Ort, an dem die  Vermittlung von Wissen und technischem Können selbst erfolgt.

**False Positives:**

- `Wissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_89`)


Auch wenn für  die Lehrtätigkeit eine Vorbereitungszeit sowie eine Zeit für die Beurteilung vorzulegender  schriftlicher Arbeiten der Schüler erforderlich ist, so stellt die Ausübung dieser Tätigkeit - wie  immer sie auch vorgenommen wird - nicht den Mittelpunkt der Lehrtätigkeit, also die  unmittelbare Vermittlung von Wissen und Können an den Schüler, dar (vgl. VwGH 26.5.1999,  98/13/0138).

**False Positives:**

- `Wissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_19`)


Primäres Ziel von  Behindertenhilfen sei, Behinderten größtmögliche Selbstversorgung zu ermöglichen.

**False Positives:**

- `Behindertenhilfen sei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_31`)


Bei dem gegenständlichen Dusch-WC des Typs Geberit AquaClean 8000plus handelt es sich um  keine nur für Behinderte geeignete Anlage, sondern ist dieses auf Grund seiner Beschaffenheit  für jedermann nutzbar und auch für körperlich nicht einges chränkte Personen von Wert.

**False Positives:**

- `Wert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_69`)


Den vom Bundesfinanzgericht getroffenen Feststellungen zufolge (siehe dazu oben unter Punkt  1) handelt es sich bei dem vom Beschwerdeführer angeschafften Dusch-WC um keine spezifisch  nur für Behinderte geeignete Anlage, sondern ist dieses auf Grund seiner Beschaffenheit für  jedermann nutzbar und auch für körperlich nicht eingeschränkte Personen von Wert.

**False Positives:**

- `Wert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_23`)


Beschwerdeerwägungen:  Dem angefochtenen Bescheid über die Festsetzung von Anspruchszinsen 2007 liegt der im  Einkommensteuerbescheid 2007 des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013  ausgewiesene Differenzbetrag von € 254.913,99 zugrunde.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_24`)


Der Bf. bekämpft den Bescheid  über die Festsetzung von Anspruchszinsen 2007 ausschließlich mit der Begründung, dass der  zugrundeliegende Einkommensteuerbescheid unrichtig wäre bzw. nicht erlassen werden hätte  dürfen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_35`)


Eine  Abänderung von Zinsenbescheiden (anlässlich einer Abänderung bzw. Aufhebung des  Stammabgabenbescheides) ist im Gesetz nicht vorgesehen.

**False Positives:**

- `Zinsenbescheiden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_54`)


Auch das Bundesfinanzgericht kam in freier Beweiswürdigung aufgrund der nunmehr  vorliegenden Aktenlage zum Schluss, dass der Bf im Jahr 2017 keine Einnahmen bzw. Einkünfte  aus gewerblicher bzw. unternehmerischer Tätigkeit zugeflossen sind, die zu einer Festsetzung  von Umsatzsteuer und einer zusätzlichen Einkommensteuerbelastung für die Bf führen  konnten.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_65`)


Dabei sind alle Umstände zu berücksichtigen, die für  die Schätzung von Bedeutung sind.

**False Positives:**

- `Bedeutung sind.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_126`)


Bei der Schätzung von Besteuerungsgrundlagen handelt es sich um ein Beweisverfahren, bei  dem der Sachverhalt bezogen auf das im Einzelfall konkret vorliegende sachliche Geschehen  unter Zuhilfenahme mittelbarer Beweise ermittelt wird (VwGH 18.12.1997, 96/16/0143).

**False Positives:**

- `Besteuerungsgrundlagen handelt es sich um ein Beweisverfahren, bei  dem der Sachverhalt bezogen auf das im Einzelfall konkret vorliegende sachliche Geschehen  unter Zuhilfenahme mittelbarer Beweise ermittelt wird` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_39`)


 Rechtliche Erwägungen  Strittig ist die Abzugsfähigkeit von Fortbildungskosten als Werbungskosten.

**False Positives:**

- `Fortbildungskosten als Werbungskosten.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_55`)


Ferner sind idR nicht abzugsfähig Aufwendungen für den Besuch von Kursen  für neuro-linguistisches Programmieren (NLP), da diese im Regelfall Kenntnisse und  Fähigkeiten vermitteln, die auch für den Bereich der privaten Lebensführung von Bedeutung  sind (VwGH 28.5.2008, 2006/15/0237).

**False Positives:**

- `Bedeutung  sind` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_70`)


Dass der  Besuch von Seminaren für neurolinguistisches Programmieren (NLP) oder für Schauspiel und  Performance aber auch im Regelfall Kenntnisse und Fertigkeiten vermitteln, die für den Bereich  der privaten Lebensführung von Bedeutung sind, hat der Verwaltungsgerichtshof wiederholt  bejaht (zB VwGH 29.1.2004, 2000/15/0009;

**False Positives:**

- `Bedeutung sind, hat der Verwaltungsgerichtshof wiederholt  bejaht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_2`)


Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Elisabeth Tombült,  Landschacher Gasse 33, 3925 Neumelon, Österreich, vertreten durch Dr. Edelsbacher & Partner Wirtschaftsprüfungs- und Steuer-  beratungsgesellschaft mbH, Ernst-Grein-Straße 14A, 5026 Salzburg, betreffend Beschwerde  vom 17. Juli 2019 gegen den Bescheid des Finanzamtes vom 18. Juni 2019 über die Festsetzung  von Anspruchszinsen (§ 205 BAO) 2016 beschlossen:  Der Vorlageantrag vom 15.06.2020 wird gemäß § 260 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e  BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Elisabeth Tombült`(person)
- `Landschacher Gasse 33, 3925 Neumelon, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_4`)


Begründung  Gleichzeitig mit der Erlassung des Einkommensteuerbescheides 2016 erließ das Finanzamt am  18.06.2019 einen Bescheid über die Festsetzung von Anspruchszinsen 2016 gegenüber der  Beschwerdeführerin (kurz: Bf).

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_5`)


Mit Schriftsatz vom 17.07.2019 brachte die steuerliche Vertretung der Bf Beschwerde gegen  den Einkommensteuerbescheid 2016 und gegen den Bescheid über die Festsetzung von  Anspruchszinsen 2016 ein.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_Bei`

**F1:** 0.001 | **Precision:** 0.002 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `6a54d072`  
**Description:**
Captures names following 'bei' (at/with) in contexts like 'bei der Hugo Buring'.

**Content:**
```
(?:bei\s+(?:der|die|den)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+\(|$|\s+\d{4}|\s+Gattin|\s+und)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.002 | 0.001 | 0.001 | 447 | 1 | 446 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 446 | 1635 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_162`)


Seite 13 von 15 Bedenkt man, dass der Verwaltungsgerichtshof bei drei einschlägigen Vorstrafen eine Geldstrafe im Ausmaß von 45 % der möglichen Höchststrafe für zulässig erklärt hat (VwGH 8.2.2007, 2006/15/0293) oder bei zwei Vorstrafen wegen Abgabenhinterziehung bei geringem Einkommen des Bestraften eine Geldstrafe von 34% des Strafrahmens und eine zusätzliche primäre Freiheitsstrafe von zwei Wochen als angemessen erklärt (VwGH 25.6.1998, 96/15/0041), so kann man erkennen, wie moderat die Bemessung der Geldstrafe bei den Vorstrafen des Beschuldigten ausgefallen ist.

**False Positives:**

- `Vorstrafen des Beschuldigten ausgefallen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_66`)


Ausgaben für den Erwerb eines Wirtschaftsgutes sind nach ständiger Rechtsprechung des  Verwaltungsgerichtshofes in der Regel von einer Berücksichtigung als außergewöhn liche  Belastung ausgeschlossen, da bei der Ans chaffung eines Wirtschaftsgutes in der Regel ein  entsprechender Gegenwert erlangt wird (vgl zB VwGH 27.6.2018, Ra 2017/15/0006, mwN).

**False Positives:**

- `Ans chaffung eines Wirtschaftsgutes in der Regel ein  entsprechender Gegenwert erlangt wird` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_13`)


Bedauerlicher Weise wurde weder innerhalb des Bundesfinanzgerichtes eine Information über  die bereits erfolgte Entscheidung im zugrundeliegenden Abgabenverfahren noch von der  belangten Behörde eine Information über die Erlassung eines Gutschriftszinsenbescheides für  dieses Beschwerdeverfahren weitergeleitet, sodass es zu dieser weiteren – wenn auch  kurzfristigen – Verzögerung bei der Entscheidung gekommen ist.

**False Positives:**

- `Entscheidung gekommen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/128731.1`) (sent_id: `deanon_BFG_TRAIN/128731.1_65`)


Eine unzumutbare Verlegung des Familienwohnsitzes zum Dienstort liegt jedoch bei Einkünften  der Ehefrau nur vor, wenn es sich diesfalls um steuerlich relevante Erwerbseinkünfte handelt,  die bei der Verlegung des Familienwohnsitzes verloren gingen (vgl VwGH 8. Februar 2007,  2004/15/0102 und VwGH 17. Februar 1999, 95/14/0059).

**False Positives:**

- `Verlegung des Familienwohnsitzes verloren gingen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_62`)


Der BF war im Zeitraum 09/2008 - 04/2011 als Lkw-Fahrer bei der GmbH (in der Folge GmbH)  beschäftigt.

**False Positives:**

- `GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_130`)


Die verfahrensgegenständlichen Abgaben waren – wie oben dargestellt - bei der GmbH nicht  einbringlich, da das Insolvenzverfahren im Oktober 2011 mangels eines die Kosten des  Verfahrens deckenden Vermögens nicht eröffnet wurde.

**False Positives:**

- `GmbH nicht  einbringlich, da das Insolvenzverfahren im Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_8`)


Nach  einem Ergänzungsersuchen des FA in dem der BF seine Werbungskosten aufgliederte,  veranlagte das FA den BF mit Bescheid vom 03.06.2016 zur Einkommensteuer 2014, kürzte  dabei die Werbungskosten und setzte die Ausgaben bei den Funktionsgebühren nicht an.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_22`)


Dies umfasse auch öffentlich-rechtliche Rechtsträger und  somit auch die beiden Funktionen bei der Arbeiterkammer und der Gebietskrankenkasse.

**False Positives:**

- `Arbeiterkammer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_16`)


4. Die genannten Beträge sind bei der GmbH als uneinbringlich anzusehen.

**False Positives:**

- `GmbH als uneinbringlich anzusehen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_25`)


Im Fall  der Nichterbringung dieser Nachweise muss das Finanzamt davon ausgehen, dass Sie die Ihnen  obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwalteten Mitteln zu  entrichten, schuldhaft verletzt haben, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH ist.

**False Positives:**

- `GmbH ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/129101.1`) (sent_id: `deanon_BFG_TRAIN/129101.1_19`)


Eventuell zu erhaltende Quoten seien bei der Auflistung noch nicht  abgezogen worden.

**False Positives:**

- `Auflistung noch nicht  abgezogen worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/129137.1`) (sent_id: `deanon_BFG_TRAIN/129137.1_43`)


2. Liegenschaften, deren Benützung auf Grund der Notwendigkeit umfangreicher Bauarbeiten  (zB Generalsanierungen) unmöglich ist, sodass kein Müll anfallen kann, wobei die Ausnahme  auf die Dauer der Unbenutzbarkeit zu befristen ist.

**False Positives:**

- `Ausnahme  auf die Dauer der Unbenutzbarkeit zu befristen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_26`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes komme es bei der Beurteilung  darauf an, zu welcher Verwendung das Fahrzeug werkseitig bestimmt sei und entscheidend sei  die wirtschaftliche Zweckbestimmung des Fahrzeuges nach seiner werkseitigen Bauart und  Beschaffenheit (VwGH 82/14/0005).

**False Positives:**

- `Beurteilung  darauf an, zu welcher Verwendung das Fahrzeug werkseitig bestimmt sei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_191`)


sowie der  gewerblichen und technischen Erfahrungen des Franchisegebers und unter Beachtung des von  diesem entwickelten Organisations- und Werbesystems zu vertreiben, wobei der  Franchisegeber Beistand, Rat und Schulung in technischer und verkaufstechnischer Hinsicht  gewährt und eine Kontrolle über die Geschäftstätigkeit des Franchisenehmers ausübt.

**False Positives:**

- `Franchisegeber Beistand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_15`)


(2) Bereits in der Vorprüfung (BP 2006 bis 2009, Nachschauzeitraum bis 7/2010) sei die  Anwendung der Differenzbesteuerung bei den Fahrzeugen der Firma MH hinterfragt worden.

**False Positives:**

- `Fahrzeugen der Firma MH hinterfragt worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_128`)


Zur Liste der 21 Fahrzeuge aus 2009 und 2010 wird ausgeführt:  „Hiermit bestätige ich, dass die 21 oben angeführten Fahrzeuge unter Anwendung der  Differenzbesteuerung angeschafft worden sind, weil diese   - entweder von einer Person erworben wurden, die nicht zum Ausweis einer Vorsteuer  berechtigt ist  - oder von einem anderen Wiederverkäufer, der seinerseits bei der Lieferung die  Differenzbesteuerung angewendet hat.

**False Positives:**

- `Lieferung die  Differenzbesteuerung angewendet hat.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_552`)


Stb: Die Außenprüfung hat damals festgestellt, dass bei der Firma MH etwas nicht in Ordnung  war.

**False Positives:**

- `Firma MH etwas nicht in Ordnung  war.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_595`)


In einem Dekret des Staatsrates sind die spezifischen Verfahren für die Anwendung des ersten  Absatzes festgelegt, wenn der Vertreter in einem Land niedergelassen ist, in dem es kein  Rechtsinstrument für die gegenseitige Unterstützung mit einem ähnlichen Umfang wie in der  Richtlinie gibt (2010/24 EU des Rates vom 16. März 2010 über die gegenseitige Unterstützung  bei der Beitreibung von Schulden in Bezug auf Steuern, Abgaben und andere Maßnahmen sowie  durch die Verordnung (EU) Nr. 904/2010 des Rates vom 7. Oktober 2010 über die  administrative Zusammenarbeit und die Betrugsbekämpfung im Bereich der Mehrwertsteuer).

**False Positives:**

- `Beitreibung von Schulden in Bezug auf Steuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_627`)


Bei Weiterverkauf kann der österreichische KFZ-Händler die  Differenzbesteuerung anwenden, wenn bei der Lieferung an ihn keine USt geschuldet oder  erhoben worden ist.

**False Positives:**

- `Lieferung an ihn keine USt geschuldet oder  erhoben worden ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_674`)


Zunächst ist festzuhalten, dass schon anlässlich der vorangegangenen BP (Prüfungsauftrag  19.10.2010, Prüfungsjahre 2006 bis 2008, in der Folge ausgedehnt auf 2009) die  beschwerdegegenständliche Thematik angesprochen wurde (Einkauf Fahrzeuge bei MH ab  2009) und damit bereits zu diesem Zeitpunkt bekannt war:   (1) So wird in Pkt vier der Niederschrift vom 1. März 2012 (Bericht vom 20. März 2012 zu den  Veranlagungsjahren 2006 bis 2009 und Nachschau 1-7/2010) ausgeführt, „im Jahr 2009 und  2010 wurden vom Bf. Fahrzeuge bei der Firma MH ohne Angabe der eigenen UID angekauft.

**False Positives:**

- `Firma MH ohne Angabe der eigenen UID angekauft.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_703`)


In der Besprechung vom 6. Dezember 2010 habe der Bf. bestätigt,  dass es sich bei den Fahrzeugen um endbesteuerte Fahrzeuge handle und zugesagt, sich von  MH Bestätigungen für die einzelnen Differenzbesteuerungen zu besorgen.

**False Positives:**

- `Fahrzeugen um endbesteuerte Fahrzeuge handle` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_6`)


Durch die zuständige Abgabenbehörde wurde bei der Bf., beginnend im Jahr 2009, eine  Außenprüfung (AP) durchgeführt, die neben Körperschaft- und Umsatzsteuer für das Jahr 2008  auch die Kapitalertragsteuer zum Prüfungsgegenstand hatte.

**False Positives:**

- `Bf., beginnend im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_9`)


Im Zuge einer Außenprüfung bei der Bf. wurde festgestellt, dass im Jahr 2013  Rechtsanwaltskosten in Höhe von 30.158,94 Euro plus 20% Umsatzsteuer in Höhe von  6.031,79 Euro auf dem Konto 775 "Rechtsberatung" verbucht waren.

**False Positives:**

- `Bf. wurde festgestellt, dass im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_90`)


Die betriebliche Veranlassung von Aufwendungen ist grundsätzlich von Amts wegen  festzustellen, wobei den Steuerpflichtigen eine Mitwirkungspflicht trifft.

**False Positives:**

- `Steuerpflichtigen eine Mitwirkungspflicht trifft.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_164`)


Die betriebliche Veranlassung von Aufwendungen ist grundsätzlich von Amts wegen  festzustellen, wobei den Steuerpflichtigen eine Mitwirkungspflicht trifft.

**False Positives:**

- `Steuerpflichtigen eine Mitwirkungspflicht trifft.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_191`)


Die Beweislast liegt daher im Beschwerdefall eindeutig bei der Bf.

**False Positives:**

- `Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_115`)


Ein X scheint im  österreichischen Firmenbuch bei der Bf. aber mit keiner Funktion auf.

**False Positives:**

- `Bf. aber mit keiner Funktion auf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/129503.1`) (sent_id: `deanon_BFG_TRAIN/129503.1_9`)


Im gegenständlichen Fall sei zwar am 15. Juli 2019 bei der Firma C. GmbH ein  Umbuchungsantrag eingebracht worden.

**False Positives:**

- `Firma C. GmbH ein  Umbuchungsantrag eingebracht worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_61`)


Der Bf. erklärte, dass er bei den Bareinzahlungen der Erlöse aus den AGMbH Fahrten keinen  Text auf den Einzahlungsbeleg geschrieben habe, bei den Zahlungen betreffend die  Auftraggeber MT und J hingegen auf den Bankbelegen immer die Namen der Auftraggeber  vermerkt waren.

**False Positives:**

- `Zahlungen betreffend die  Auftraggeber MT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_80`)


Die Bf. gab folgende Stellungnahme ab:  "1  Das Gericht hält richtigerweise fest, dass es sich nach der Jud des VwGH bei der Gerichtspraxis  um eine Ausbildung im Sinne des FLAG handelt (VwGH 18.11.2009, 2008/13/0015) und die  Einkommensgrenze im vorliegenden Fall somit nicht überschritten wurde.

**False Positives:**

- `Gerichtspraxis  um eine Ausbildung im Sinne des FLAG handelt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Party_Beschwerdesache`

**F1:** 0.398 | **Precision:** 0.862 | **Recall:** 0.259  

**Format:** `regex`  
**Rule ID:** `af12a153`  
**Description:**
Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.

**Content:**
```
(?:in der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\s+(?:der\s+|des\s+)?)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+vertreten|\s+\(|\s+\)|$|\s+\d{4}\s+\w+|\s+Gattin|\s+und\s+der)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.862 | 0.259 | 0.398 | 492 | 424 | 68 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 424 | 68 | 1212 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Erika Zajcenko, Volksheimstraße 9, 8784 Trieben, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erika Zajcenko` | `Erika Zajcenko` |

**Missed by this rule (FN):**

- `Volksheimstraße 9, 8784 Trieben, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Catharina Moewis,  Im Klosterhof 21N, 5241 Großenaich, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Catharina Moewis` | `Catharina Moewis` |

**Missed by this rule (FN):**

- `Im Klosterhof 21N, 5241 Großenaich, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Konrad Conrady  in der Beschwerdesache  Prof.  Ashley Lauterwasser, Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich, über die Beschwerde vom 23. September 2016 gegen den Bescheid  des Finanzamtes Linz vom 25. August 2016 betreffend Einkommensteuer 2014 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Prof.  Ashley Lauterwasser` | `Prof.  Ashley Lauterwasser` |

**Missed by this rule (FN):**

- `Univ.-Prof. Konrad Conrady` (person)
- `Josefine-Wessely-Weg 4U, 5204 Eingarten, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128731.1`) (sent_id: `deanon_BFG_TRAIN/128731.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Mag. Gerald Leverenz, Hansl-Schmid-Weg 54, 4623 Sirfling, Österreich, über die Beschwerde vom 17. Juli 2013 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 3. Juli 2013 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 Steuernummer zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerald Leverenz` | `Mag. Gerald Leverenz` |

**Missed by this rule (FN):**

- `Hansl-Schmid-Weg 54, 4623 Sirfling, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Klara Vondenhoff  in der Beschwerdesache  Vitus Hepprich, Singerweg 36, 9581 Unterferlach, Österreich  über die Beschwerde vom 28. Februar 2019 gegen die Bescheide  des FA Vorarlberg  vom 30. Jänner 2019, 20-231/9124, betreffend Umsatz- und  Einkommensteuer 2017  zu Recht erkannt:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Vitus Hepprich` | `Vitus Hepprich` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Klara Vondenhoff` (person)
- `Singerweg 36, 9581 Unterferlach, Österreich` (address)
- `FA Vorarlberg` (organisation)
- `20-231/9124` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128762.1`) (sent_id: `deanon_BFG_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Daniel Baake,  Zollfeldstraße 85, 4731 Unterbruck, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-63-948/2501 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Baake` | `Daniel Baake` |

**Missed by this rule (FN):**

- `Zollfeldstraße 85, 4731 Unterbruck, Österreich` (address)
- `10-63-948/2501` (tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Alvin Luczak, Kudlichstraße 14, 5282 Brunn im Gries, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Bruck Eisenstadt Oberwart  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 67-340/8452  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alvin Luczak` | `Alvin Luczak` |

**Missed by this rule (FN):**

- `Kudlichstraße 14, 5282 Brunn im Gries, Österreich` (address)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)
- `67-340/8452` (tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Serge Anhalt, Ebenfeld 7, 4776 Mitterndorf, Österreich,  vertreten durch WP_GmbH, WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  44-050/5905  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Serge Anhalt` | `Serge Anhalt` |

**Missed by this rule (FN):**

- `Ebenfeld 7, 4776 Mitterndorf, Österreich` (address)
- `44-050/5905` (tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/128893.1`) (sent_id: `deanon_BFG_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Horst de Keyser, Heinrich-Ruff-Weg 8, 8523 Laßnitz, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Horst de Keyser` | `Horst de Keyser` |

**Missed by this rule (FN):**

- `Heinrich-Ruff-Weg 8, 8523 Laßnitz, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache KzlR Livia Vasold, Statzenbachgasse 8, 9654 Tuffbad, Österreich, über die Beschwerde vom 10. Juni 2016 gegen den Bescheid des FA vom 3. Juni 2016  betreffend Einkommensteuer 2014 Steuernummer 94-176/6276  zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `KzlR Livia Vasold` | `KzlR Livia Vasold` |

**Missed by this rule (FN):**

- `Statzenbachgasse 8, 9654 Tuffbad, Österreich` (address)
- `94-176/6276` (tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Mehmet Bildstein, Josef Glanner-Gasse 168, 3142 Obermoos, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 72-182/5875  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mehmet Bildstein` | `Mehmet Bildstein` |

**Missed by this rule (FN):**

- `Dr. Alois Pichler` (person)
- `Josef Glanner-Gasse 168, 3142 Obermoos, Österreich` (address)
- `72-182/5875` (tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129103.1`) (sent_id: `deanon_BFG_TRAIN/129103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache DDr. Rocco Bernhards, Obere Festwiese 8, 4863 Steindorf, Österreich, über die Beschwerde vom 18. Juli 2013 gegen den Bescheid des Zollamtes Linz Wels  vom 18. Juni 2013 betreffend Vorschreibung eines Altlastenbeitrag für die Quartale 2-4 des  Jahres 2003 zu Recht erkannt:   Der angefochtene Bescheid wird hinsichtlich des Altlastenbeitrags - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `DDr. Rocco Bernhards` | `DDr. Rocco Bernhards` |

**Missed by this rule (FN):**

- `Obere Festwiese 8, 4863 Steindorf, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129137.1`) (sent_id: `deanon_BFG_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Lara Emhart, Steinwiese 39, 6060 Heiligkreuz, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Steinparztal 60, 9472 Krottendorf, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lara Emhart` | `Lara Emhart` |

**Missed by this rule (FN):**

- `Steinwiese 39, 6060 Heiligkreuz, Österreich` (address)
- `Steinparztal 60, 9472 Krottendorf, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Missed by this rule (FN):**

- `Mag. Markus Knechtl LL.M.` (person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich` (address)
- `84-986/6948` (tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129188.1`) (sent_id: `deanon_BFG_TRAIN/129188.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Volker Fatheuer, Voirans 4, 8503 Blumegg, Österreich, betreffend Beschwerde vom 11. Juni 2016 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart vom 13. Mai 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 beschlossen:  Der Vorlageantrag vom 9.2.2020 wird gemäß § 278 Abs. 1 lit. a i.V.m. den §§ 260 Abs. 1 lit. b,  264 Abs. 4 lit. e und 264 Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Volker Fatheuer` | `Volker Fatheuer` |

**Missed by this rule (FN):**

- `Voirans 4, 8503 Blumegg, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129205.1`) (sent_id: `deanon_BFG_TRAIN/129205.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Vivian Agnesen,  Kafkasee I 2G, 4693 Viecht, Österreich, über die Beschwerde vom 10. April 2019 gegen den Bescheid über den Antrag  vom 06.03.2019 auf Mehrkindzuschlag für 2019 aufgrund der Verhältnisse des Jahres 2018  des  Finanzamtes vom 1. April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vivian Agnesen` | `Vivian Agnesen` |

**Missed by this rule (FN):**

- `Kafkasee I 2G, 4693 Viecht, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Elena Zilinski, Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Elena Zilinski` | `Elena Zilinski` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe,  Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

| Predicted | Gold |
|---|---|
| `Kordelia van Clewe` | `Kordelia van Clewe` |

**Missed by this rule (FN):**

- `Mag.a Irene van der Hoven` (person)
- `Piettegasse 15, 3341 Oberamt, Österreich` (address)
- `FA Tirol Ost` (organisation)
- `20-364/1486` (tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129421.1`) (sent_id: `deanon_BFG_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Konepatzki  in der Beschwerdesache KommR MedR Jeannine Wegerhoff,  Burleiten 563, 9423 Matschenbloch, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KommR MedR Jeannine Wegerhoff` | `KommR MedR Jeannine Wegerhoff` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Jacqueline Konepatzki` (person)
- `Burleiten 563, 9423 Matschenbloch, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Vivian Wenk` | `Vivian Wenk` |

**Missed by this rule (FN):**

- `Mag. Marco Laudacher` (person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/129876.1`) (sent_id: `deanon_BFG_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Cedric Leutheusser, Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Cedric Leutheusser` | `Mag. Cedric Leutheusser` |

**Missed by this rule (FN):**

- `Edmund-Hofbauer-Straße 11, 4084 Bräuleiten, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Shoshana Schweinforth, Brenggenalm 15, 8551 Gieselegg, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 78-461/2049  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Shoshana Schweinforth` | `Shoshana Schweinforth` |

**Missed by this rule (FN):**

- `Brenggenalm 15, 8551 Gieselegg, Österreich` (address)
- `78-461/2049` (tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/129950.1`) (sent_id: `deanon_BFG_TRAIN/129950.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Denise Adamske, Adresse1,  Ungarn, über die Beschwerde vom 26. März 2019 gegen den Bescheid des Finanzamtes A vom  27. Februar 2019, Steuernummer 85-962/6181, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Denise Adamske` | `Denise Adamske` |

**Missed by this rule (FN):**

- `85-962/6181` (tax_number)

**Example 23** (doc_id: `deanon_BFG_TRAIN/129969.1`) (sent_id: `deanon_BFG_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hilde Heinsohn, Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `Hilde Heinsohn` | `Hilde Heinsohn` |

**Missed by this rule (FN):**

- `Krautäckerstraße 46, 4623 Au bei Hischmannsberg, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/130024.1`) (sent_id: `deanon_BFG_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Marlon William, J. Ranzoni-Straße 1L, 9554 Reggen, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlon William` | `Marlon William` |

**Missed by this rule (FN):**

- `J. Ranzoni-Straße 1L, 9554 Reggen, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130034.1`) (sent_id: `deanon_BFG_TRAIN/130034.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache des Karina Wissmann, Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich, betreffend eine  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, über die Beschwerde vom 16. Juli 2020 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 –  Parkraumüberwachung, als Abgabenstrafbehörde vom 18. Juni 2020, Zahl MA67/Zahlzu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde vom  16. Juli 2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  – Parkraumüberwachung, MA67/Zahl, vom 18. Juni 2020 als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Karina Wissmann` | `Karina Wissmann` |

**Missed by this rule (FN):**

- `Mag. Andreas Stanek` (person)
- `Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130057.1`) (sent_id: `deanon_BFG_TRAIN/130057.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Rachel Thurm  in der Beschwerdesache des  Arnold Kopman, Schiexlgasse 96, 4582 Seebach, Österreich, über die Beschwerde vom 6. März 2017 gegen den Bescheid des  Finanzamt Gmunden Vöcklabruck  vom 30. Jänner 2017 betreffend Grunderwerbsteuer 2017 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arnold Kopman` | `Arnold Kopman` |

**Missed by this rule (FN):**

- `Dr.in Rachel Thurm` (person)
- `Schiexlgasse 96, 4582 Seebach, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)

**Example 27** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Christoph Mehlbeer` | `Christoph Mehlbeer` |

**Missed by this rule (FN):**

- `Schötz Gasse 45, 7434 Holzschlag, Österreich` (address)
- `Margarete Wiepking` (person)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Missed by this rule (FN):**

- `Schulwiesen 13, 4203 Stratreith, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130442.1`) (sent_id: `deanon_BFG_TRAIN/130442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Armin Lieffering, Fuchsleitenweg 4, 4143 Neustift im Mühlkreis, Österreich, über die Beschwerden vom 27. November 2018 gegen die Bescheide des Finanzamtes  Baden Mödling vom 12. November 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017, Steuernummer , zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Armin Lieffering` | `Armin Lieffering` |

**Missed by this rule (FN):**

- `Fuchsleitenweg 4, 4143 Neustift im Mühlkreis, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_TRAIN/130444.1`) (sent_id: `deanon_BFG_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Lars Hoerl  in der Beschwerdesache VetR Christina Schlotfeldt,  Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Christina Schlotfeldt` | `VetR Christina Schlotfeldt` |

**Missed by this rule (FN):**

- `Hon.-Prof. Lars Hoerl` (person)
- `Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich` (address)

**Example 31** (doc_id: `deanon_BFG_TRAIN/130450.1`) (sent_id: `deanon_BFG_TRAIN/130450.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Lorena Biedenbender, Gitzen 41, 4812 Reindlmühl, Österreich,  über die Beschwerde vom 20. April 2018 gegen die Bescheide des Finanzamtes Klagenfurt, zu  Steuernummer 09-249/9464, vom 23. März 2018, mittels welchen der Antrag auf  Aufhebung der Einkommensteuerbescheide für 2015 und 2016 gemäß § 299 BAO abgewiesen  wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lorena Biedenbender` | `Lorena Biedenbender` |

**Missed by this rule (FN):**

- `Gitzen 41, 4812 Reindlmühl, Österreich` (address)
- `09-249/9464` (tax_number)

**Example 32** (doc_id: `deanon_BFG_TRAIN/130475.1`) (sent_id: `deanon_BFG_TRAIN/130475.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache OMedR Hermann Voigtlander, Martha-Wölger-Weg 27, 2292 Stopfenreuth, Österreich, über die Beschwerden vom 22.12.2018  (hinsichtlich des Jahres 2014) und vom 13.01.2019 (hinsichtlich der Jahre 2015 und 2016)  gegen die Berichtigungsbescheide gemäß § 293 BAO zu den Einkommensteuerbescheiden für  die Jahre 2014 bis 2016 jeweils vom 18.12.2018 des Finanzamtes Wien 2/20/21/22   zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `OMedR Hermann Voigtlander` | `OMedR Hermann Voigtlander` |

**Missed by this rule (FN):**

- `Martha-Wölger-Weg 27, 2292 Stopfenreuth, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_TRAIN/130696.1`) (sent_id: `deanon_BFG_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Axel Winandt  in der Beschwerdesache Rafaela Coolens,  Murbergstraße 3, 9155 Bach, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  FA Schwechat Gerasdorf  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rafaela Coolens` | `Rafaela Coolens` |

**Missed by this rule (FN):**

- `Univ.-Prof. Axel Winandt` (person)
- `Murbergstraße 3, 9155 Bach, Österreich` (address)
- `FA Schwechat Gerasdorf` (organisation)

**Example 34** (doc_id: `deanon_BFG_TRAIN/130723.1`) (sent_id: `deanon_BFG_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Laura Koterba   in der Beschwerdesache des Eugenia Diamantoglou, Schirmleitenstraße 26, 3250 Marbach an der Kleinen Erlauf, Österreich,   betreffend die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 05-101/2290,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Eugenia Diamantoglou` | `Eugenia Diamantoglou` |

**Missed by this rule (FN):**

- `Dr.in Laura Koterba` (person)
- `Schirmleitenstraße 26, 3250 Marbach an der Kleinen Erlauf, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `05-101/2290` (tax_number)

**Example 35** (doc_id: `deanon_BFG_TRAIN/130754.1`) (sent_id: `deanon_BFG_TRAIN/130754.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Madeleine Uhlmer  in der Verwaltungsstrafsache  Waldemar Beimfohr, Ried Zephirau 9, 4894 Obernberg, Österreich, 1.) über die Beschwerde vom 19.06.2020 gegen die Strafverfügung  des Magistrats der Stadt Wien vom 30.12.2019, zugestellt am 27.02.2020, Geschäftszahl  MA67/196701166656/2019, und 2.) über die Beschwerde vom 19.06.2020 gegen die Strafver- fügung des Magistrats der Stadt Wien vom 20.01.2020, zugestellt am 03.03.2020, Geschäfts- zahl MA67/196701283117/2019, beschlossen:    Die Beschwerden werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Waldemar Beimfohr` | `Waldemar Beimfohr` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Madeleine Uhlmer` (person)
- `Ried Zephirau 9, 4894 Obernberg, Österreich` (address)

**Example 36** (doc_id: `deanon_BFG_TRAIN/130768.1`) (sent_id: `deanon_BFG_TRAIN/130768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Benedikt Muschalek, Latschacher Weg 44, 3644 Fahnsdorf, Österreich, über die Beschwerde vom 26. Mai 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 15. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Benedikt Muschalek` | `Benedikt Muschalek` |

**Missed by this rule (FN):**

- `Latschacher Weg 44, 3644 Fahnsdorf, Österreich` (address)

**Example 37** (doc_id: `deanon_BFG_TRAIN/130839.1`) (sent_id: `deanon_BFG_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Zarin Finke,  Brauhausplatz 29, 9422 Untereberndorf, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Zarin Finke` | `Zarin Finke` |

**Missed by this rule (FN):**

- `Brauhausplatz 29, 9422 Untereberndorf, Österreich` (address)

**Example 38** (doc_id: `deanon_BFG_TRAIN/130909.1`) (sent_id: `deanon_BFG_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Miriam Kloeppel, Hollehnerweg 19, 9061 Nußberg, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Miriam Kloeppel` | `Miriam Kloeppel` |

**Missed by this rule (FN):**

- `Dr. Wolfgang Freilinger` (person)
- `Hollehnerweg 19, 9061 Nußberg, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_TRAIN/130963.1`) (sent_id: `deanon_BFG_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rafaela Hennermann  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Gerhard Woehrlin, Lohwaggasse 88, 3004 Weinzierl, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 94-750/9977  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gerhard Woehrlin` | `Gerhard Woehrlin` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Rafaela Hennermann` (person)
- `Lohwaggasse 88, 3004 Weinzierl, Österreich` (address)
- `94-750/9977` (tax_number)

**Example 40** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Jean Wohlrap, Weyprechtgasse 44M, 9701 Nußdorf, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jean Wohlrap` | `Jean Wohlrap` |

**Missed by this rule (FN):**

- `Dr. Peter Unger` (person)
- `Weyprechtgasse 44M, 9701 Nußdorf, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Gregor Fraunlob, Brantmannstraße 9, 3595 Frankenreith, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Fraunlob` | `Gregor Fraunlob` |

**Missed by this rule (FN):**

- `Mag. Stefan Pipal` (person)
- `Brantmannstraße 9, 3595 Frankenreith, Österreich` (address)

**Example 42** (doc_id: `deanon_BFG_TRAIN/131046.1`) (sent_id: `deanon_BFG_TRAIN/131046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Hugo Moewius, Studenygasse 11, 4623 Buchleiten, Österreich, vertreten durch SCHIETZ + MAUREDER Steuerberatung GmbH,  Veldner Straße 29, 4120 Neufelden, über die Beschwerde vom 20. Juni 2017 gegen den  Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 9. Juni 2017 betreffend  Einkommensteuer 2015 Steuernummer 03-874/1042  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hugo Moewius` | `Hugo Moewius` |

**Missed by this rule (FN):**

- `Studenygasse 11, 4623 Buchleiten, Österreich` (address)
- `03-874/1042` (tax_number)

**Example 43** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Silvia Geidies, Schönengrund 34, 4209 Innertreffling, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 17-823/0942  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Silvia Geidies` | `Silvia Geidies` |

**Missed by this rule (FN):**

- `Schönengrund 34, 4209 Innertreffling, Österreich` (address)
- `17-823/0942` (tax_number)

**Example 44** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Endrowait` | `Willibald Endrowait` |

**Missed by this rule (FN):**

- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 45** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ottfried Bremermann` | `Ottfried Bremermann` |

**Missed by this rule (FN):**

- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich` (address)
- `Samuel Rehnke, BSc` (person)
- `Planetengasse 30, 8455 Bischofegg, Österreich` (address)
- `14-141/9449` (tax_number)

**Example 46** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Jeanne von Fritz  in der Beschwerdesache Martha Michenfelder,  Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich, vertreten durch Dkfm.

| Predicted | Gold |
|---|---|
| `Martha Michenfelder` | `Martha Michenfelder` |

**Missed by this rule (FN):**

- `Mag.a Univ.-Prof.in Jeanne von Fritz` (person)
- `Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich` (address)

**Example 47** (doc_id: `deanon_BFG_TRAIN/131313.1`) (sent_id: `deanon_BFG_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Laurentia Abatzidou  in der Beschwerdesache Jasper Kochzius,  Franz Hofbauer-Straße 64, 2640 Liesling, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-19-605/7001  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jasper Kochzius` | `Jasper Kochzius` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Laurentia Abatzidou` (person)
- `Franz Hofbauer-Straße 64, 2640 Liesling, Österreich` (address)
- `41-19-605/7001` (tax_number)

**Example 48** (doc_id: `deanon_BFG_TRAIN/131327.1`) (sent_id: `deanon_BFG_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Urs Grennigloh, Weitenfeld 26, 5273 Schwathof, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Urs Grennigloh` | `Urs Grennigloh` |

**Missed by this rule (FN):**

- `Weitenfeld 26, 5273 Schwathof, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_TRAIN/131343.1`) (sent_id: `deanon_BFG_TRAIN/131343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Techn R Damian Weida, Maierniggalpe 210, 4712 Niederwödling, Österreich, über die Beschwerde vom 21. August 2018 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 2. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Techn R Damian Weida` | `Techn R Damian Weida` |

**Missed by this rule (FN):**

- `Maierniggalpe 210, 4712 Niederwödling, Österreich` (address)

**Example 50** (doc_id: `deanon_BFG_TRAIN/131366.1`) (sent_id: `deanon_BFG_TRAIN/131366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Dagobert Wesserle,  Mahd 7r, 4690 Edt, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des Finanzamtes XY  vom 10.2.2020 betreffend Festsetzung einer Zwangsstrafe zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dagobert Wesserle` | `Dagobert Wesserle` |

**Missed by this rule (FN):**

- `Mahd 7r, 4690 Edt, Österreich` (address)

**Example 51** (doc_id: `deanon_BFG_TRAIN/131368.1`) (sent_id: `deanon_BFG_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Dr. Zlatan Kappelsberger, Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

| Predicted | Gold |
|---|---|
| `Dr. Zlatan Kappelsberger` | `Dr. Zlatan Kappelsberger` |

**Missed by this rule (FN):**

- `Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich` (address)

**Example 52** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Prof. Gernot Woortmann, Spitzbergweg 116, 3204 Tradigistgegend, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 16-817/8793  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Prof. Gernot Woortmann` | `Prof. Gernot Woortmann` |

**Missed by this rule (FN):**

- `Dr. Michael Mandlmayr` (person)
- `Spitzbergweg 116, 3204 Tradigistgegend, Österreich` (address)
- `16-817/8793` (tax_number)

**Example 53** (doc_id: `deanon_BFG_TRAIN/131450.1`) (sent_id: `deanon_BFG_TRAIN/131450.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Carmen Wielander  in der Beschwerdesache Ulrich Hecktor,  St. Nikolaus Straße 16, 4904 Reichering, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 26. Februar 2020,  betreffend Rückforderung von Familienbeihilfe und Kinderabsetzbeträge für die Zeiträume  Oktober 2017 bis Juni 2019, zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ulrich Hecktor` | `Ulrich Hecktor` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Carmen Wielander` (person)
- `St. Nikolaus Straße 16, 4904 Reichering, Österreich` (address)

**Example 54** (doc_id: `deanon_BFG_TRAIN/131451.1`) (sent_id: `deanon_BFG_TRAIN/131451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Janis Schmüser  in der Beschwerdesache Massimo Oechslin,  Alte Sulzer Straße 11v, 9102 Kulm, Österreich, vertreten durch die Erwachsenenvertreterin RA, gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 23. Juli 2018, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016 und Anspruchszinsen 2015, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Massimo Oechslin` | `Massimo Oechslin` |

**Missed by this rule (FN):**

- `Dr.in Mag.a Janis Schmüser` (person)
- `Alte Sulzer Straße 11v, 9102 Kulm, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

| Predicted | Gold |
|---|---|
| `Karen Vennemeyer` | `Karen Vennemeyer` |

**Missed by this rule (FN):**

- `Neu-Reinbach 11, 4693 Fallholz, Österreich` (address)
- `Intercura Teuhand Revisions  GmbH` (organisation)

**Example 56** (doc_id: `deanon_BFG_TRAIN/131524.1`) (sent_id: `deanon_BFG_TRAIN/131524.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterC in der Beschwerdesache Raimund Brand, Fagerstraße 3, 4671 Hofern, Österreich, über die Beschwerde vom 17. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 19. Dezember 2019 betreffend Rückforderung  Differenzzahlung/Familienbeihilfe und Kindergeld Juli bis Dezember 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Raimund Brand` | `Raimund Brand` |

**Missed by this rule (FN):**

- `Fagerstraße 3, 4671 Hofern, Österreich` (address)

**Example 57** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Mike Kuruoglu, Kronbergstraße 11, 9341 Wattein, Österreich, über die Beschwerden vom 2. November 2015 und vom 10. Februar 2016 gegen die  Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 15. Oktober 2015 und vom  26.1.2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 und 2014,  Steuernummer 38-811/5980, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mike Kuruoglu` | `Mike Kuruoglu` |

**Missed by this rule (FN):**

- `Kronbergstraße 11, 9341 Wattein, Österreich` (address)
- `38-811/5980` (tax_number)

**Example 58** (doc_id: `deanon_BFG_TRAIN/131581.1`) (sent_id: `deanon_BFG_TRAIN/131581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Juliana Benneker, Raudaschlmühle 59, 4810 Gmunden, Österreich, über die Beschwerde vom 27.8,2015 gegen den  Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser vom 28.

| Predicted | Gold |
|---|---|
| `Juliana Benneker` | `Juliana Benneker` |

**Missed by this rule (FN):**

- `Raudaschlmühle 59, 4810 Gmunden, Österreich` (address)

**Example 59** (doc_id: `deanon_BFG_TRAIN/131601.1`) (sent_id: `deanon_BFG_TRAIN/131601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Jana Maquard, Eberdorf 1, 4633 Kematen am Innbach, Österreich, über die Beschwerde vom 3. Oktober 2018 gegen die Bescheide des Finanzamtes Wien  1/23 vom 30. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 und  2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jana Maquard` | `Jana Maquard` |

**Missed by this rule (FN):**

- `Eberdorf 1, 4633 Kematen am Innbach, Österreich` (address)

**Example 60** (doc_id: `deanon_BFG_TRAIN/131705.1`) (sent_id: `deanon_BFG_TRAIN/131705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Abigail Jakobik,  Kaspar-Öhe-Weg 34, 4723 Moos, Österreich, über die Beschwerde vom 6. August 2019 gegen den Bescheid des Finanzamtes  Österreich vom 24. Juli 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018,  Steuernummer 32-528/0429, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Abigail Jakobik` | `Abigail Jakobik` |

**Missed by this rule (FN):**

- `Kaspar-Öhe-Weg 34, 4723 Moos, Österreich` (address)
- `32-528/0429` (tax_number)

**Example 61** (doc_id: `deanon_BFG_TRAIN/131716.1`) (sent_id: `deanon_BFG_TRAIN/131716.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Hartmut Veicht, Franz-Ressl-Straße 35, 5251 Thannstraß, Österreich, über die Beschwerde vom 30. Juni 2020 gegen die Bescheide des Finanzamtes Bruck  Eisenstadt Oberwart vom 27. Mai 2020 betreffend Abweisung eines Antrages auf  Wideraufnahme des Verfahrens hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung)  2015, 2016 und 2017 Steuernummer 98-900/9369  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hartmut Veicht` | `Hartmut Veicht` |

**Missed by this rule (FN):**

- `Franz-Ressl-Straße 35, 5251 Thannstraß, Österreich` (address)
- `98-900/9369` (tax_number)

**Example 62** (doc_id: `deanon_BFG_TRAIN/131773.1`) (sent_id: `deanon_BFG_TRAIN/131773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melinda Endele  in der Beschwerdesache Constantin Oberboersch,  Eidendorfer Straße 3, 8441 Höch, Österreich ,EU-Land, über die Beschwerde vom 19. Dezember 2017 gegen den  Abweisungsbescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 11. Dezember 2017  betreffend Ausgleichszahlung (Familienbeihilfe) für Kind1, geb. xx.xx..1994, Kind2, geb.  yy.yy..2002 und Kind3, geb. zz.zz..2000, je für den Zeitraum Jänner 2016 bis Dezember 2016 zu  Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Constantin Oberboersch` | `Constantin Oberboersch` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Melinda Endele` (person)
- `Eidendorfer Straße 3, 8441 Höch, Österreich` (address)

**Example 63** (doc_id: `deanon_BFG_TRAIN/131804.1`) (sent_id: `deanon_BFG_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Gerda Mauder, Exerzierplatz 16, 4962 Mining, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Gerda Mauder` | `Gerda Mauder` |

**Missed by this rule (FN):**

- `Exerzierplatz 16, 4962 Mining, Österreich` (address)

**Example 64** (doc_id: `deanon_BFG_TRAIN/131922.1`) (sent_id: `deanon_BFG_TRAIN/131922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Bodo Ibel  in der Verwaltungsstrafsache  Fridolin Jodeleid, Stiftergasse 75z, 2262 Stillfried, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in  Verbindung mit § 16 Abs. 1 und Tarifpost B 8 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli  1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl.

| Predicted | Gold |
|---|---|
| `Fridolin Jodeleid` | `Fridolin Jodeleid` |

**Missed by this rule (FN):**

- `Mag. Mag. Bodo Ibel` (person)
- `Stiftergasse 75z, 2262 Stillfried, Österreich` (address)

**Example 65** (doc_id: `deanon_BFG_TRAIN/132000.1`) (sent_id: `deanon_BFG_TRAIN/132000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Hon.-Prof.in Priv.-Doz.in Lukas Voigtlaender  in der Beschwerdesache Liu Stelmaszyk,  Laberlweg 104, 4382 Waldhausen im Strudengau, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und Jugendhilfe,  Karl-Borromäus-Platz 3, 1030 Wien, über die Beschwerde vom 14. August 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 (nunmehr Finanzamtes Österreich ) vom 30. Juli  2020 betreffend Abweisung des Antrages auf Familienbeihilfe für 01/2016 bis 06/2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Liu Stelmaszyk` | `Liu Stelmaszyk` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Hon.-Prof.in Priv.-Doz.in Lukas Voigtlaender` (person)
- `Laberlweg 104, 4382 Waldhausen im Strudengau, Österreich` (address)

**Example 66** (doc_id: `deanon_BFG_TRAIN/132030.1`) (sent_id: `deanon_BFG_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Bernadette Birkfeld, Pipitzhof 7, 3388 Knetzersdorf, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernadette Birkfeld` | `Bernadette Birkfeld` |

**Missed by this rule (FN):**

- `Pipitzhof 7, 3388 Knetzersdorf, Österreich` (address)

**Example 67** (doc_id: `deanon_BFG_TRAIN/132065.1`) (sent_id: `deanon_BFG_TRAIN/132065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Jason Wiegboldt, Oisreitl 3, 8850 Frojach, Österreich, gegen die Bescheide des Finanzamtes Wien 4/5/10 vom 21. Februar 2014 betreffend  die auf § 303 Abs. 1 BAO basierende Verfügung der Wiederaufnahme der Verfahren zur  Umsatzsteuer für das Jahr 2010 und zur Einkommensteuer für die Jahre 2010 und 2011 sowie  die auf § 205 Abs. 1 BAO basierende Festsetzung von Anspruchszinsen für die Jahre 2010 bis  2012 beschlossen:  Der Vorlageantrag vom 26.9.2014 wird - betreffend vorgenannter Bescheide - gemäß § 264  Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jason Wiegboldt` | `Jason Wiegboldt` |

**Missed by this rule (FN):**

- `Oisreitl 3, 8850 Frojach, Österreich` (address)

**Example 68** (doc_id: `deanon_BFG_TRAIN/132162.1`) (sent_id: `deanon_BFG_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Liu Werbicki, Elisabetha 26n, 3383 Pöttendorf, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 58-661/8152, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Liu Werbicki` | `Liu Werbicki` |

**Missed by this rule (FN):**

- `Dr. Ansgar Unterberger` (person)
- `Elisabetha 26n, 3383 Pöttendorf, Österreich` (address)
- `58-661/8152` (tax_number)

**Example 69** (doc_id: `deanon_BFG_TRAIN/132165.1`) (sent_id: `deanon_BFG_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Ingrid Raemaekers,  Am Lindenkreuz 6, 2620 Lindgrub, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Ingrid Raemaekers` | `Ingrid Raemaekers` |

**Missed by this rule (FN):**

- `Am Lindenkreuz 6, 2620 Lindgrub, Österreich` (address)

**Example 70** (doc_id: `deanon_BFG_TRAIN/132303.1`) (sent_id: `deanon_BFG_TRAIN/132303.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elvira Schaffranek  in der Beschwerdesache Judith Kuhr,  Unterm Kirchenberg 337, 4064 Hausleiten, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 07. April 2020,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Judith Kuhr` | `Judith Kuhr` |

**Missed by this rule (FN):**

- `Dr.in Elvira Schaffranek` (person)
- `Unterm Kirchenberg 337, 4064 Hausleiten, Österreich` (address)

**Example 71** (doc_id: `deanon_BFG_TRAIN/132328.1`) (sent_id: `deanon_BFG_TRAIN/132328.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Ivan Hovemeyer, Khevenhüllerstraße 36, 4272 Wienau, Österreich, betreffend Beschwerde vom 17. Jänner 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 18. Dezember 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 Steuernummer 88-222/2026  beschlossen:   Der Vorlageantrag vom 5.6.2020 wird gemäß § 260 Abs. 1 lit.b BAO in Verbindung mit § 264  Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ivan Hovemeyer` | `Ivan Hovemeyer` |

**Missed by this rule (FN):**

- `Khevenhüllerstraße 36, 4272 Wienau, Österreich` (address)
- `88-222/2026` (tax_number)

**Example 72** (doc_id: `deanon_BFG_TRAIN/132361.1`) (sent_id: `deanon_BFG_TRAIN/132361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dora Streb, Rosemarie-Preh-Allee 19, 9113 Grutschen, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1/Freyung, 1010  Wien, über die Beschwerde vom 13. Juni 2014 gegen den Bescheid des Finanzamtes Wien 1/23  vom 11. August 2010 betreffend Berichtigung gemäß § 293b BAO des Bescheides vom 1. Juni  2007 betreffend Umsatzsteuer 2005 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dora Streb` | `Dora Streb` |

**Missed by this rule (FN):**

- `Rosemarie-Preh-Allee 19, 9113 Grutschen, Österreich` (address)

**Example 73** (doc_id: `deanon_BFG_TRAIN/132368.1`) (sent_id: `deanon_BFG_TRAIN/132368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Hugo Denhart, Eichhorn 8, 9413 Hinterwölch, Österreich, vertreten durch Dr. Peter Eisele, Öffentlicher Notar, 7540 Güssing, Hauptplatz 1, über  die Beschwerde vom 18. Dezember 2017 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 11. Dezember 2017 betreffend Rechtsgebühr,  Steuernummer 10- 90-207/0668, Erf.Nr. 10- 2017, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hugo Denhart` | `Hugo Denhart` |

**Missed by this rule (FN):**

- `Eichhorn 8, 9413 Hinterwölch, Österreich` (address)
- `90-207/0668` (tax_number)

**Example 74** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Karola Birkenzeller, Reifnitz 2, 4532 Rohr im Kremstal, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Pascal Tiessen, Dipl.

| Predicted | Gold |
|---|---|
| `Karola Birkenzeller` | `Karola Birkenzeller` |

**Missed by this rule (FN):**

- `Reifnitz 2, 4532 Rohr im Kremstal, Österreich` (address)
- `Pascal Tiessen` (person)

**Example 75** (doc_id: `deanon_BFG_TRAIN/132477.1`) (sent_id: `deanon_BFG_TRAIN/132477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Yelec Nitzge, Gasteigergasse 68, 3261 Oberstampfing, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 19. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Yelec Nitzge` | `Yelec Nitzge` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Gasteigergasse 68, 3261 Oberstampfing, Österreich` (address)

**Example 76** (doc_id: `deanon_BFG_TRAIN/132482.1`) (sent_id: `deanon_BFG_TRAIN/132482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  MedR Roland Ruschemeier, Schöferhof 401, 9832 Untersteinwand, Österreich, über die Beschwerde vom 30. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 9. März 2020 betreffend Einkommensteuer  2018, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MedR Roland Ruschemeier` | `MedR Roland Ruschemeier` |

**Missed by this rule (FN):**

- `Dr. Peter Unger` (person)
- `Schöferhof 401, 9832 Untersteinwand, Österreich` (address)

**Example 77** (doc_id: `deanon_BFG_TRAIN/132501.1`) (sent_id: `deanon_BFG_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Huberta Petratschek, Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Huberta Petratschek` | `Huberta Petratschek` |

**Missed by this rule (FN):**

- `Dr. Peter Unger` (person)
- `Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich` (address)

**Example 78** (doc_id: `deanon_BFG_TRAIN/132524.1`) (sent_id: `deanon_BFG_TRAIN/132524.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Karola Kampschnieder  in der Beschwerdesache Astrid Schippmann,  Tostner Burgweg 7, 2801 Katzelsdorf, Österreich, betreffend Beschwerde vom 1. Mai 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 12. April 2019 hinsichtlich Wiederaufnahme § 303 BAO /  ESt 2016,  Steuernummer 82-640/4796  den Beschluss gefasst:  I.  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Astrid Schippmann` | `Astrid Schippmann` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Karola Kampschnieder` (person)
- `Tostner Burgweg 7, 2801 Katzelsdorf, Österreich` (address)
- `82-640/4796` (tax_number)

**Example 79** (doc_id: `deanon_BFG_TRAIN/132589.1`) (sent_id: `deanon_BFG_TRAIN/132589.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Rinaldo von Konrad,  Lebzelterweg 7, 9560 Pernegg, Österreich, über die Beschwerde vom 7. Jänner 2016  gegen den Bescheid des  Finanzamtes Österreich vom 9. Dezember 2015 betreffend Abweisung des Antrags auf  Ausgleichszahlung (Familienbeihilfe 01.2010-12.2015 ) zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 9. Dezember 2015 wird gemäß § 279 Abs. 1 BAO  abgewiesen.

| Predicted | Gold |
|---|---|
| `Rinaldo von Konrad` | `Rinaldo von Konrad` |

**Missed by this rule (FN):**

- `Lebzelterweg 7, 9560 Pernegg, Österreich` (address)

**Example 80** (doc_id: `deanon_BFG_TRAIN/132601.1`) (sent_id: `deanon_BFG_TRAIN/132601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Elena Scheidlin  in der Beschwerdesache Martin Chalupny,  Anton Gotsch-Gasse 26, 8492 Klöchberg, Österreich, vertreten durch StB, über die Beschwerde vom 23. Juli 2018 gegen den  Bescheid des Finanzamtes vom 25. Juni 2018 betreffend Einkommensteuervorauszahlungen  2018 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Martin Chalupny` | `Martin Chalupny` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Elena Scheidlin` (person)
- `Anton Gotsch-Gasse 26, 8492 Klöchberg, Österreich` (address)

**Example 81** (doc_id: `deanon_BFG_TRAIN/132647.1`) (sent_id: `deanon_BFG_TRAIN/132647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Janet Spatzl,  Alois-Jenewein-Weg 17, 5124 Weyer, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH, Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 23. Februar 2017 gegen den  Bescheid des Finanzamtes Gänserndorf Mistelbach vom 21. Dezember 2016 betreffend  Einkommensteuer 2014, Steuernummer 30-739/8407, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Janet Spatzl` | `Janet Spatzl` |

**Missed by this rule (FN):**

- `Alois-Jenewein-Weg 17, 5124 Weyer, Österreich` (address)
- `30-739/8407` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_1`)


Gerald Erwin Ehgartner in der Beschwerdesache Janis Forch, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Janis Forch,` — partial — gold is substring of pred: `Janis Forch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Janis Forch`(person)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl.

**False Positives:**

- `Dipl.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Emmerich Bleekmann`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenV, die RichterinR sowie die  fachkundigen Laienrichter LR1 und LR2 in der Beschwerdesache Bf, Wilhelmsederstraße 93, 9112 Gönitz, Österreich, vertreten  durch Stb, über die Beschwerde vom 27. April 2015 gegen die Bescheide des Finanzamtes St.  Johann Tamsweg Zell am See vom 27. März 2015 betreffend Umsatzsteuer 2012 und  Umsatzsteuer 2013, Steuernummer 91-666/8239, nach Durchführung einer mündlichen  Verhandlung am 10. Juni 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wilhelmsederstraße 93, 9112 Gönitz, Österreich`(address)
- `91-666/8239`(tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Dr.in Ulrike Kusnierz  in der Beschwerdesache K GmbH,  Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `K GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dr.in Ulrike Kusnierz`(person)
- `Maria-Platzer-Straße 69, 4755 Aiglbrechting, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf. Name vormals nunmehr Janis Dollnig` — partial — gold is substring of pred: `Janis Dollnig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129503.1`) (sent_id: `deanon_BFG_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache Gabriele Lemmon, Bakk. rer. nat., Graf-Egger-Straße 4, 4712 Armau, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 49-573/3569  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `Gabriele Lemmon` — partial — pred is substring of gold: `Gabriele Lemmon, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gabriele Lemmon, Bakk. rer. nat.`(person)
- `Graf-Egger-Straße 4, 4712 Armau, Österreich`(address)
- `49-573/3569`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/130424.1`) (sent_id: `deanon_BFG_TRAIN/130424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Vivian Classens, Bakk. iur. BEd, Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich  vertreten durch Vertreter, gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 24. November 2015, betreffend Grunderwerbsteuer  aufgrund des Übergabsvertrages mit N.N. (Erf. Nr., Steuernummer), zu Recht erkannt:   Der eingeschränkten Beschwerde wird Folge gegeben.

**False Positives:**

- `Vivian Classens` — partial — pred is substring of gold: `Vivian Classens, Bakk. iur. BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vivian Classens, Bakk. iur. BEd`(person)
- `Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Cevik  in der Beschwerdesache der Bf., (im  Beschwerdeverfahren) vertreten durch Rechtsanwälte Lehofer & Lehofer,  Kalchberggasse 6/1.

**False Positives:**

- `Bf.,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Lubomir Cevik`(person)

**Example 8** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Marlies Danzfuss` — partial — pred is substring of gold: `Marlies Danzfuss, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Siegfried Fenz`(person)
- `Marlies Danzfuss, BSc`(person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/131091.1`) (sent_id: `deanon_BFG_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Raimund Grünstäudl  in der Beschwerdesache der Frau  Manfred Bernatik, Reisgasse 13, 8402 Werndorf, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Frau  Manfred Bernatik` — partial — gold is substring of pred: `Manfred Bernatik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Raimund Grünstäudl`(person)
- `Manfred Bernatik`(person)
- `Reisgasse 13, 8402 Werndorf, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/131772.1`) (sent_id: `deanon_BFG_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Dipl.

**False Positives:**

- `Dipl.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/132063.1`) (sent_id: `deanon_BFG_TRAIN/132063.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Gindert  in der Beschwerdesache Prof.in Henriette Oldvader, LLB,  Anton-Proksch-Siedlung 23, 3203 Steinklamm, Österreich, über die Säumnisbeschwerden vom 29. Jänner 2021, eingebracht am 8.  Februar 2021, wegen behaupteter Verletzung der Entscheidungspflicht des Finanzamt Innsbruck  betreffend   1. Antrag an das FA Innsbruck  vom 26.05.2020 auf Wiederaufnahme des mit  Einstellungsbeschluss des BFG vom 16.04.2020 abgeschlossenen Abgabenverfahrens  2. Antrag an das FA Innsbruck  vom 02.06.2020 auf Aufhebung des Einstellungsbeschlusses  des BFG vom 16.04.2020 nach § 299 BAO   beschlossen:  Die Säumnisbeschwerden werden gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Prof.in Henriette Oldvader` — partial — pred is substring of gold: `Prof.in Henriette Oldvader, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Jeannine Gindert`(person)
- `Prof.in Henriette Oldvader, LLB`(person)
- `Anton-Proksch-Siedlung 23, 3203 Steinklamm, Österreich`(address)
- `Finanzamt Innsbruck`(organisation)
- `FA Innsbruck`(organisation)
- `FA Innsbruck`(organisation)

**Example 12** (doc_id: `deanon_BFG_TRAIN/132142.1`) (sent_id: `deanon_BFG_TRAIN/132142.1_91`)


Als Beispiel darf auf das Urteil des EuGH in der Rechtssache Schumacker verwiesen werden.

**False Positives:**

- `Schumacker verwiesen werden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/132197.1`) (sent_id: `deanon_BFG_TRAIN/132197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Horst Widera, Bakk. rer. nat., Edergasse 43, 3713 Harmannsdorf, Österreich, über die Beschwerde vom 10. September 2019 gegen den  Bescheid des Finanzamtes Österreich vom 13. August 2019 betreffend Abweisung eines  Antrages auf Wiederaufnahme § 303 BAO /  ESt 2017 Steuernummer 56-074/9687  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Horst Widera` — partial — pred is substring of gold: `Horst Widera, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Horst Widera, Bakk. rer. nat.`(person)
- `Edergasse 43, 3713 Harmannsdorf, Österreich`(address)
- `56-074/9687`(tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf., Farchern 45, 4362 Kühweid, Österreich, über die Beschwerde vom 27. Mai 2016 gegen den  Bescheid des Finanzamtes KirchdorfPerg Steyr vom 27. April 2016 betreffend  Kapitalertragsteuer 2012 und die Bescheide vom 3. Mai 2016 betreffend Körperschaftssteuer  2012, 2013 und 2014, Steuernummer 77-859/7031, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Farchern 45, 4362 Kühweid, Österreich`(address)
- `77-859/7031`(tax_number)

**Example 15** (doc_id: `deanon_BFG_TRAIN/132255.1`) (sent_id: `deanon_BFG_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Chen Helwig  in der Beschwerdesache Roxana Gehrbrandt,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Roxana Gehrbrandt, ` — partial — gold is substring of pred: `Roxana Gehrbrandt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Chen Helwig`(person)
- `Roxana Gehrbrandt`(person)

**Example 16** (doc_id: `deanon_BFG_TRAIN/132412.1`) (sent_id: `deanon_BFG_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Erwin Mittenreiter  in der Beschwerdesache Rita Ratfeld  in  Liquidation, Kujanikgasse 28, 5123 Weng, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  FA Innsbruck  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rita Ratfeld  in  Liquidation` — partial — gold is substring of pred: `Rita Ratfeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Erwin Mittenreiter`(person)
- `Rita Ratfeld`(person)
- `Kujanikgasse 28, 5123 Weng, Österreich`(address)
- `FA Innsbruck`(organisation)

**Example 17** (doc_id: `deanon_BFG_TRAIN/132557.1`) (sent_id: `deanon_BFG_TRAIN/132557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Emilia Nüßgens  in der Beschwerdesache der  Hinklein, Stadlweg 3, 8160 Haselbach bei Weiz, Österreich, vertreten durch Ort, über die Beschwerde vom 6.9.2017 gegen die  Bescheide des Finanzamtes Innsbruck vom 2. August 2017 betreffend Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 und Festsetzung der  Kraftfahrzeugsteuer für die Zeiträume Juli bis Dezember 2014 und Jänner bis Juni 2015 zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 wird abgewiesen.

**False Positives:**

- `Hinklein` — type mismatch — same span as gold: `Hinklein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag.a Emilia Nüßgens`(person)
- `Hinklein`(organisation)
- `Stadlweg 3, 8160 Haselbach bei Weiz, Österreich`(address)

</details>

---

## `Judge_Richter`

**F1:** 0.157 | **Precision:** 0.700 | **Recall:** 0.089  

**Format:** `regex`  
**Rule ID:** `dc682d4a`  
**Description:**
Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles, ensuring no trailing whitespace and excluding single-letter abbreviations.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Vorsitzende)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|Dr\.\s+Univ\.-Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?)?)?)(?=\s+(?:in der|\u00fcber die|in der Verwaltungsstrafsache|\(|,|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.700 | 0.089 | 0.157 | 207 | 145 | 62 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 145 | 62 | 1488 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christoph Kordik in der Beschwerdesache  Prof. Hon.-Prof. ÖkR Detlev Leudert, Bungalowweg 8, 6741 Plazera, Österreich, über die Beschwerde vom 13.03.2015 gegen die Bescheide des  Finanzamtes Linz vom 17. Februar 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2009 und 2010 ,Steuernummer [...] ,zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christoph Kordik` | `Mag. Christoph Kordik` |

**Missed by this rule (FN):**

- `Prof. Hon.-Prof. ÖkR Detlev Leudert` (person)
- `Bungalowweg 8, 6741 Plazera, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Raphael Skowroneck, MBA` (person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Mehmet Bildstein, Josef Glanner-Gasse 168, 3142 Obermoos, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 72-182/5875  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Mehmet Bildstein` (person)
- `Josef Glanner-Gasse 168, 3142 Obermoos, Österreich` (address)
- `72-182/5875` (tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Lubomir Baltßun` (person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |

**Missed by this rule (FN):**

- `OStR Karl Ostendarp` (person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich` (address)
- `84-986/6948` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129254.1`) (sent_id: `deanon_BFG_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache StR VetR Corbinian Drügemöller, Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Thomas Leitner` | `Mag.Dr. Thomas Leitner` |

**Missed by this rule (FN):**

- `StR VetR Corbinian Drügemöller` (person)
- `Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Vivian Wenk` (person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129872.1`) (sent_id: `deanon_BFG_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache James Loratis, Platzerweg 28, 4673 Baumgarting, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `James Loratis` (person)
- `Platzerweg 28, 4673 Baumgarting, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/129937.1`) (sent_id: `deanon_BFG_TRAIN/129937.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Paulina Steg, Weiterndorf 9, 4650 Oberzeiling, Österreich, vom 25. Juni 2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 28. Mai 2020, Zahl: MA67/Zahl, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Abweisung  I. Der Beschwerde wird teilweise Folge gegeben und die Entscheidung des Magistrats der Stadt  Wien in ihrem Ausspruch über die Strafe dahingehend abgeändert, dass die gemäß § 4 Abs. 1  Parkometergesetz 2006 verhängte Geldstrafe von € 140,00 auf € 90,00 und die gemäß § 16  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) verhängte Ersatzfreiheitsstrafe von 1 Tag 9 Stunden  auf 21 Stunden verringert werden.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Paulina Steg` (person)
- `Weiterndorf 9, 4650 Oberzeiling, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/130034.1`) (sent_id: `deanon_BFG_TRAIN/130034.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache des Karina Wissmann, Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich, betreffend eine  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, über die Beschwerde vom 16. Juli 2020 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 –  Parkraumüberwachung, als Abgabenstrafbehörde vom 18. Juni 2020, Zahl MA67/Zahlzu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde vom  16. Juli 2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67  – Parkraumüberwachung, MA67/Zahl, vom 18. Juni 2020 als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Karina Wissmann` (person)
- `Peter-Rosegger-Straße 8, 3462 Bierbaum am Kleebühel, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Marlies Danzfuss, BSc, Ober Bregarten 10, 4142 Hötzendorf, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Marlies Danzfuss, BSc` (person)
- `Ober Bregarten 10, 4142 Hötzendorf, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Paula Jagiella, Medienpark 18, 3384 Eidletzberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Paula Jagiella` (person)
- `Medienpark 18, 3384 Eidletzberg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Wladimir Nüssli` (person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/130686.1`) (sent_id: `deanon_BFG_TRAIN/130686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde der  Alana Single, Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich, vom 19. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 17. August 2020, Zahl MA67/Zahl/2019, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  stattgegeben, als die Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Alana Single` (person)
- `Franz-Xaver-Müller-Weg 40, 9413 Kaltstuben, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Matthäus Buskens` (person)
- `Edlach 19, 3141 Oberkilling, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/130909.1`) (sent_id: `deanon_BFG_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Miriam Kloeppel, Hollehnerweg 19, 9061 Nußberg, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Miriam Kloeppel` (person)
- `Hollehnerweg 19, 9061 Nußberg, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Jean Wohlrap, Weyprechtgasse 44M, 9701 Nußdorf, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Jean Wohlrap` (person)
- `Weyprechtgasse 44M, 9701 Nußdorf, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Gregor Fraunlob, Brantmannstraße 9, 3595 Frankenreith, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Gregor Fraunlob` (person)
- `Brantmannstraße 9, 3595 Frankenreith, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/131361.1`) (sent_id: `deanon_BFG_TRAIN/131361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Kordula Zeitler, Auhäuseln 22, 7540 Inzenhof, Österreich, gegen das Straferkenntnis der belangten Behörde, Magistrat der  Stadt Wien, MA 67, als Abgabenstrafbehörde vom 20. März 2020, MA67/GZ, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe von € 60,00 auf € 48,00 herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Kordula Zeitler` (person)
- `Auhäuseln 22, 7540 Inzenhof, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/131365.1`) (sent_id: `deanon_BFG_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Mario Gajewska, Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Mario Gajewska` (person)
- `Gärtnereistraße 115, 8720 Sankt Margarethen bei Knittelfeld, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Prof. Gernot Woortmann, Spitzbergweg 116, 3204 Tradigistgegend, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 16-817/8793  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Prof. Gernot Woortmann` (person)
- `Spitzbergweg 116, 3204 Tradigistgegend, Österreich` (address)
- `16-817/8793` (tax_number)

**Example 21** (doc_id: `deanon_BFG_TRAIN/132162.1`) (sent_id: `deanon_BFG_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Liu Werbicki, Elisabetha 26n, 3383 Pöttendorf, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 58-661/8152, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Liu Werbicki` (person)
- `Elisabetha 26n, 3383 Pöttendorf, Österreich` (address)
- `58-661/8152` (tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf., Farchern 45, 4362 Kühweid, Österreich, über die Beschwerde vom 27. Mai 2016 gegen den  Bescheid des Finanzamtes KirchdorfPerg Steyr vom 27. April 2016 betreffend  Kapitalertragsteuer 2012 und die Bescheide vom 3. Mai 2016 betreffend Körperschaftssteuer  2012, 2013 und 2014, Steuernummer 77-859/7031, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Farchern 45, 4362 Kühweid, Österreich` (address)
- `77-859/7031` (tax_number)

**Example 23** (doc_id: `deanon_BFG_TRAIN/132372.1`) (sent_id: `deanon_BFG_TRAIN/132372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die zwei  (gleichlautenden) Beschwerden des Siegmund Prokopiev, Seibersdorf bei Sankt Veit 10, 5242 Straß, Österreich, vom 21. Jänner 2021 gegen die  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67, Zahl 1) MA67/Zahl1  und 2) MA67/Zahl2/2020, beide vom 08. Jänner 2021, beide wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) werden die Beschwerden als  unbegründet abgewiesen und die angefochtenen Straferkenntnisse bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Siegmund Prokopiev` (person)
- `Seibersdorf bei Sankt Veit 10, 5242 Straß, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/132477.1`) (sent_id: `deanon_BFG_TRAIN/132477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Yelec Nitzge, Gasteigergasse 68, 3261 Oberstampfing, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 19. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Yelec Nitzge` (person)
- `Gasteigergasse 68, 3261 Oberstampfing, Österreich` (address)

**Example 25** (doc_id: `deanon_BFG_TRAIN/132482.1`) (sent_id: `deanon_BFG_TRAIN/132482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  MedR Roland Ruschemeier, Schöferhof 401, 9832 Untersteinwand, Österreich, über die Beschwerde vom 30. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 9. März 2020 betreffend Einkommensteuer  2018, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `MedR Roland Ruschemeier` (person)
- `Schöferhof 401, 9832 Untersteinwand, Österreich` (address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/132501.1`) (sent_id: `deanon_BFG_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Huberta Petratschek, Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Huberta Petratschek` (person)
- `Graf-Starhemberg-Gasse 11, 3170 Hainfeld, Österreich` (address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/132578.1`) (sent_id: `deanon_BFG_TRAIN/132578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Aloisa Füchsel, Wimhub 18, 3443 Henzing, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 6.3.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Aloisa Füchsel` (person)
- `Wimhub 18, 3443 Henzing, Österreich` (address)

**Example 28** (doc_id: `deanon_BFG_TRAIN/132660.1`) (sent_id: `deanon_BFG_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Nancy Kärgling, Küng 27, 2133 Ungerndorf, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Nancy Kärgling` (person)
- `Küng 27, 2133 Ungerndorf, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Ernestine Schittenhelm, Clementinengasse 29, 8692 Krampen, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Ernestine Schittenhelm` (person)
- `Clementinengasse 29, 8692 Krampen, Österreich` (address)

**Example 30** (doc_id: `deanon_BFG_TRAIN/132953.1`) (sent_id: `deanon_BFG_TRAIN/132953.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Vitalis Wienerth, Gewerbestraße Mitte 7, 4783 Stöbichen, Österreich, über die Beschwerde vom 28. Mai 2020 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 04-302/6040  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Vitalis Wienerth` (person)
- `Gewerbestraße Mitte 7, 4783 Stöbichen, Österreich` (address)
- `04-302/6040` (tax_number)

**Example 31** (doc_id: `deanon_BFG_TRAIN/133297.1`) (sent_id: `deanon_BFG_TRAIN/133297.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Reinhold Dengler, Königleiten 4, 2632 Altendorf, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 10. Februar 2017 betreffend Einkommensteuer 2015 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Reinhold Dengler` (person)
- `Königleiten 4, 2632 Altendorf, Österreich` (address)

**Example 32** (doc_id: `deanon_BFG_TRAIN/133301.1`) (sent_id: `deanon_BFG_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Francois Stürnkorb, Lobisser Straße 37, 4153 Schönberg, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Francois Stürnkorb` (person)
- `Lobisser Straße 37, 4153 Schönberg, Österreich` (address)

**Example 33** (doc_id: `deanon_BFG_TRAIN/133823.1`) (sent_id: `deanon_BFG_TRAIN/133823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Penelope Wohler, Dietlergraben 11, 4681 Schachet, Österreich, über die Beschwerde vom 30. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 3. Oktober 2019 betreffend Familienbeihilfe ab  September 2019 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Penelope Wohler` (person)
- `Dietlergraben 11, 4681 Schachet, Österreich` (address)

**Example 34** (doc_id: `deanon_BFG_TRAIN/133856.1`) (sent_id: `deanon_BFG_TRAIN/133856.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Ramon Häußlein, Julbach 63, 3713 Buttendorf, Österreich, über die Beschwerde vom 24. Dezember 2019  gegen den Bescheid des Finanzamtes für Gebühren Verkehrsteuern und Glücksspiel vom  22. November 2019, Steuernummer 54-489/6916, betreffend Grunderwerbsteuer 2019 zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Ramon Häußlein` (person)
- `Julbach 63, 3713 Buttendorf, Österreich` (address)
- `54-489/6916` (tax_number)

**Example 35** (doc_id: `deanon_BFG_TRAIN/134107.1`) (sent_id: `deanon_BFG_TRAIN/134107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. PhD Bruno Kastmann, Kirchbühelgasse 8u, 8524 Rassach, Österreich, über die Beschwerden vom 16. Februar 2018 und 24. Jänner 2019  gegen die Bescheide des Finanzamtes Landeck Reutte (nunmehr: Finanzamt Österreich) vom  8. Februar 2018 betreffend Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher  Behinderung und vom 10. Jänner 2019 betreffend Familienbeihilfe, jeweils ab Jänner 2018,  nach am 12. August 2021 in Innsbruck durchgeführter mündlicher Verhandlung  zu Recht erkannt:  I.  Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Kuprian` | `Mag. Martin Kuprian` |

**Missed by this rule (FN):**

- `Ing. PhD Bruno Kastmann` (person)
- `Kirchbühelgasse 8u, 8524 Rassach, Österreich` (address)

**Example 36** (doc_id: `deanon_BFG_TRAIN/134384.1`) (sent_id: `deanon_BFG_TRAIN/134384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Torsten Jokuschies, Taxerweg 19, 4952 Appersting, Österreich, vertreten durch Gstöttner & Partner  Steuerberatung Gesellschaft m.b.H. & Co. KG, Linzerstraße 10, 4320 Perg, über die Beschwerde  vom 26. Februar 2018 gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom  22. Jänner 2018 betreffend Feststellung der Einkünfte § 188 BAO 2011 Steuernummer  04-517/2751  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Torsten Jokuschies` (person)
- `Taxerweg 19, 4952 Appersting, Österreich` (address)
- `04-517/2751` (tax_number)

**Example 37** (doc_id: `deanon_BFG_TRAIN/134421.1`) (sent_id: `deanon_BFG_TRAIN/134421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Mercedes Markmeier, Ferdinand Raimund-Straße 243m, 3814 Schweinburg, Österreich, über die Beschwerde vom 21. August 2019 gegen den Bescheid des  Finanzamtes Gänserndorf Mistelbach vom 9. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 98-953/6162, zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne der Beschwerdevorentscheidung  abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Mercedes Markmeier` (person)
- `Ferdinand Raimund-Straße 243m, 3814 Schweinburg, Österreich` (address)
- `98-953/6162` (tax_number)

**Example 38** (doc_id: `deanon_BFG_TRAIN/134424.1`) (sent_id: `deanon_BFG_TRAIN/134424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Quirin Doster, Zunigalm 34, 4743 Osternach, Österreich, über die Beschwerde vom 31. März 2021 gegen den Bescheid des  Finanzamtes Österreich vom 24. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 55-758/2357  zu Recht erkannt:  I. Der angefochtene Bescheid wird wie mit Beschwerdevorentscheidung abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Quirin Doster` (person)
- `Zunigalm 34, 4743 Osternach, Österreich` (address)
- `55-758/2357` (tax_number)

**Example 39** (doc_id: `deanon_BFG_TRAIN/134507.1`) (sent_id: `deanon_BFG_TRAIN/134507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Dipl.-Ing. Xaver Kühlwetter, Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich, vertreten durch Dr. Ferdinand Jenni, Jahngasse 18, 6850  Dornbirn, über die Beschwerde vom 10. November 2014 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Oktober 2014 betreffend Einkommensteuer 2013, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Dipl.-Ing. Xaver Kühlwetter` (person)
- `Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich` (address)

**Example 40** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Sebastian Pfeiffer LL.M. über die  Beschwerde des Cynthia Neureuter, U-Bahn Station Praterstern 5, 4081 Gstaltenhof, Österreich, vom 3. September 2021 gegen die zwei an Frau  erlassenen Zurückweisungsbescheide der belangten Behörde, Magistrat der Stadt Wien, MA  67, als Abgabenstrafbehörde, beide vom 25. Juni 2021, Zahlen 1) MA67/Zahl1/2021 und 2)  MA67/Zahl2/2021, den Beschluss:  Die Beschwerde wird gemäß § 50 VwGVG iVm § 28 Abs. 1 VwGVG als unzulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Sebastian Pfeiffer LL.M.` | `Dr. Sebastian Pfeiffer LL.M.` |

**Missed by this rule (FN):**

- `Cynthia Neureuter` (person)
- `U-Bahn Station Praterstern 5, 4081 Gstaltenhof, Österreich` (address)

**Example 41** (doc_id: `deanon_BFG_TRAIN/134689.1`) (sent_id: `deanon_BFG_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Mag.Dr. Wolfgang Pagitsch` | `Mag.Dr. Wolfgang Pagitsch` |

**Missed by this rule (FN):**

- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)

**Example 42** (doc_id: `deanon_BFG_TRAIN/134907.1`) (sent_id: `deanon_BFG_TRAIN/134907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Konstanze Mockels, Ibm 10, 8160 Hafning, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz -  Erwachsenenvertretung, Bewohnervertretung, Schloßstraße 1, 3680 Persenbeug-Gottsdorf,  über die Beschwerde vom 20. Jänner 2021 gegen den Bescheid des Finanzamtes Österreich  vom 14. Dezember 2020 betreffend Familienbeihilfe ab Juni 2015 Steuernummer  41-950/9630  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Konstanze Mockels` (person)
- `Ibm 10, 8160 Hafning, Österreich` (address)
- `41-950/9630` (tax_number)

**Example 43** (doc_id: `deanon_BFG_TRAIN/135141.1`) (sent_id: `deanon_BFG_TRAIN/135141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  OMedR Bruno Kibar, Weissach 4, 5071 Walserfeld, Österreich, vertreten durch Dr. Martin Riedl, Franz-Josefs-Kai 5/DG, 1010  Wien, über die Beschwerde vom 3. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 26. August 2019  betreffend Gewährung von Familienbeihilfe ab März 2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `OMedR Bruno Kibar` (person)
- `Weissach 4, 5071 Walserfeld, Österreich` (address)

**Example 44** (doc_id: `deanon_BFG_TRAIN/135372.1`) (sent_id: `deanon_BFG_TRAIN/135372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Jelena Priesterrath, Flohleiten 13, 5123 Kreuzlinden, Österreich, über die Beschwerde vom 17. September 2018  gegen den Bescheid des Finanzamtes Linz vom 23.August 2018 betreffend Einkommensteuer  2015 und 2016, Steuernummer 97-678/1705, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Jelena Priesterrath` (person)
- `Flohleiten 13, 5123 Kreuzlinden, Österreich` (address)
- `97-678/1705` (tax_number)

**Example 45** (doc_id: `deanon_BFG_TRAIN/135479.1`) (sent_id: `deanon_BFG_TRAIN/135479.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Ali Dill, Hauswiesenweg 8, 4702 Bergern, Österreich, vertreten durch Wendelin Spätling,  Wasserturmstraße 114, 6791 Gortipohl, Österreich, betreffend die Beschwerde vom 6. Mai 2020 gegen den Bescheid  des Finanzamtes Neunkirchen Wr. Neustadt vom 26. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zur Steuernummer 81-336/9133  beschlossen:  I. Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) vom 28. Dezember 2020 wird gemäß § 264 Abs. 4 lit. e iVm § 260 Abs. 1 lit. b  iVm § 264 Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |

**Missed by this rule (FN):**

- `Ali Dill` (person)
- `Hauswiesenweg 8, 4702 Bergern, Österreich` (address)
- `Wendelin Spätling` (person)
- `Wasserturmstraße 114, 6791 Gortipohl, Österreich` (address)
- `81-336/9133` (tax_number)

**Example 46** (doc_id: `deanon_BFG_TRAIN/135536.1`) (sent_id: `deanon_BFG_TRAIN/135536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Florentine Beumers, Krischgasse 309, 4113 Windischberg, Österreich, über die Beschwerde vom 20. Februar 2020 gegen den Bescheid  des Finanzamtes Österreich vom 16. Jänner 2020 betreffend Familienbeihilfe 01.2020  Steuernummer 58-742/0765, SVNR 8800 110262, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Florentine Beumers` (person)
- `Krischgasse 309, 4113 Windischberg, Österreich` (address)
- `58-742/0765` (tax_number)
- `8800 110262` (social_security_number)

**Example 47** (doc_id: `deanon_BFG_TRAIN/135592.1`) (sent_id: `deanon_BFG_TRAIN/135592.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Theodora Corneille, Untere Brühlgasse 67, 4092 Kösslarn, Österreich, vom 17. Dezember 2021, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 1. Dezember 2021, GZ.  MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parko- meterabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Theodora Corneille` (person)
- `Untere Brühlgasse 67, 4092 Kösslarn, Österreich` (address)

**Example 48** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Reinhold Moellenkamp` (person)
- `Höllererweg 4, 2852 Maltern, Österreich` (address)

**Example 49** (doc_id: `deanon_BFG_TRAIN/135713.1`) (sent_id: `deanon_BFG_TRAIN/135713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Leonie Charalampidis, Heinrich-Hies-Hof 40, 2565 Schwarzensee, Österreich  vom 3. Oktober 2019, über die Beschwerde gegen die Bescheide  des Finanzamtes Braunau Ried Schärding vom 2. September 2019 betreffend  Kraftfahrzeugsteuer 4-12/2017 und 1-12/2018 sowie Normverbrauchsabgabe 6/2017

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Leonie Charalampidis` (person)
- `Heinrich-Hies-Hof 40, 2565 Schwarzensee, Österreich` (address)

**Example 50** (doc_id: `deanon_BFG_TRAIN/135883.1`) (sent_id: `deanon_BFG_TRAIN/135883.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Hermann Walraevens, Am Sonnwendstein 8, 2022 Immendorf, Österreich, vertreten durch MOORE STEPHENS City  Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Hafnerplatz 12, 3500  Krems an der Donau, über die Beschwerde vom 23. August 2018 gegen den Bescheid des  Finanzamtes Waldviertel vom 1. August 2018, Steuernummer 14-863/6378, betreffend  Einkommensteuer 2017 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Hermann Walraevens` (person)
- `Am Sonnwendstein 8, 2022 Immendorf, Österreich` (address)
- `14-863/6378` (tax_number)

**Example 51** (doc_id: `deanon_BFG_TRAIN/135931.1`) (sent_id: `deanon_BFG_TRAIN/135931.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Daniel Schmidtjörg, Grins 129, 4292 Kefermarkt, Österreich, über die Beschwerde vom 4. Februar 2021 gegen den Bescheid des  Finanzamtes Österreich vom 22. Jänner 2021 betreffend Familienbeihilfe 11.2019-06.2020  Steuernummer 03-2444093, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Daniel Schmidtjörg` (person)
- `Grins 129, 4292 Kefermarkt, Österreich` (address)

**Example 52** (doc_id: `deanon_BFG_TRAIN/136174.1`) (sent_id: `deanon_BFG_TRAIN/136174.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Natalie Armknecht, Ahornergasse 14, 8102 Windhof, Österreich, über die Beschwerde vom 26. Juni 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 12. Juni 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 90-423/2046  zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Natalie Armknecht` (person)
- `Ahornergasse 14, 8102 Windhof, Österreich` (address)
- `90-423/2046` (tax_number)

**Example 53** (doc_id: `deanon_BFG_TRAIN/136201.1`) (sent_id: `deanon_BFG_TRAIN/136201.1_1`)


IM NAMEN DER REPUBLI K  A.  Erkenntnis  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Karin Iosifescu, Bakk. iur., Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich, vertreten durch BDO Audit Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Am Belvedere 4, 1100 Wien, über die Beschwerde vom 17. Februar  2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom 6. Februar 2017 betreffend  1. Wiederaufnahme des Verfahrens der Vorsteuererstattung für 1-12/2012  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Karin Iosifescu, Bakk. iur.` (person)
- `Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich` (address)

**Example 54** (doc_id: `deanon_BFG_TRAIN/136201.1`) (sent_id: `deanon_BFG_TRAIN/136201.1_6`)


B.  Beschluss  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Karin Iosifescu, Bakk. iur., Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich  vertreten durch BDO Audit Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Am Belvedere 4, 1100 Wien, über die Beschwerden vom 17. Februar  2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom 6. Februar 2017 betreffend die  (Sach-) Bescheide im  1. wiederaufgenommenen Verfahren der Vorsteuererstattung für 1-12/2012  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Karin Iosifescu, Bakk. iur.` (person)
- `Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_TRAIN/136261.1`) (sent_id: `deanon_BFG_TRAIN/136261.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Jeremias Konetschnigg, Kraubathgraben 31x, 3944 Kurzschwarza, Österreich, über die Beschwerde vom 31. Dezember 2019 bzw vom 20.1.2020  gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln (nunmehr Finanzamt  Österreich, § 323b BAO) vom 17. Dezember 2019 betreffend Einkommensteuer 2009 sowie  vom 9.1.2020 betreffend Einkommensteuer 2012 und 2013 und vom 20.1.2020 betreffend  Einkommensteuer 2010, 2011, 2014-2018, Steuernummer 02-482/1394  zu Recht erkannt:   I. 1.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Jeremias Konetschnigg` (person)
- `Kraubathgraben 31x, 3944 Kurzschwarza, Österreich` (address)
- `02-482/1394` (tax_number)

**Example 56** (doc_id: `deanon_BFG_TRAIN/136497.1`) (sent_id: `deanon_BFG_TRAIN/136497.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Baumgartner über die Berufung,  nunmehr Beschwerde der Traude Kleinhuber, Bergglanzweg 29, 8103 Rein, Österreich, vertreten durch die CONSULTATIO  Wirtschaftsprüfung GmbH & Co KG, Karl-Waldbrunner-Platz 1, 1210 Wien, vom 30. November  2013 gegen den Bescheid des Finanzamtes Österreich vom 3. August 2012 betreffend  Abweisung des Antrages vom 23. April 2012 auf Vergütung von Energieabgaben für das  Wirtschaftsjahr 06/2010 bis 05/2011, Steuernummer 61-472/7721, zu Recht erkannt:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Christian Baumgartner` | `Mag. Christian Baumgartner` |

**Missed by this rule (FN):**

- `Traude Kleinhuber` (person)
- `Bergglanzweg 29, 8103 Rein, Österreich` (address)
- `61-472/7721` (tax_number)

**Example 57** (doc_id: `deanon_BFG_TRAIN/136760.1`) (sent_id: `deanon_BFG_TRAIN/136760.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Waldemar Gajdzis, Pojedl 10, 2201 Kapellerfeld, Österreich, über die Beschwerde vom 28.10.2021 gegen den  Körperschaftsteuerbescheid des Finanzamtes Österreich vom 5.10.2021 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Waldemar Gajdzis` (person)
- `Pojedl 10, 2201 Kapellerfeld, Österreich` (address)

**Example 58** (doc_id: `deanon_BFG_TRAIN/136857.1`) (sent_id: `deanon_BFG_TRAIN/136857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde des  Erhard Ptaczek, Lettengasse 56, 9314 Hochosterwitz, Österreich, vertreten durch Bezirkshauptmannschaft Mistelbach, Hauptplatz 4,  2130 Mistelbach, vom 28. September 2020, gegen den Bescheid des Finanzamtes Waldviertel  vom 14. September 2020, betreffend Zurückweisung des Antrages auf Familienbeihilfe und den  Erhöhungsbetrag für die Monate März 2020 bis Juli 2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Christian Doktor` | `Mag. Christian Doktor` |

**Missed by this rule (FN):**

- `Erhard Ptaczek` (person)
- `Lettengasse 56, 9314 Hochosterwitz, Österreich` (address)

**Example 59** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Jennifer Wildfang, Kirchbrücke 7, 3352 St. Peter in der Au-Markt, Österreich, über die Beschwerde vom 20. August 2013 gegen den Bescheid des  FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Körperschaftsteuer 2008 bis 2010,  Steuernummer 24-852/6682  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Jennifer Wildfang` (person)
- `Kirchbrücke 7, 3352 St. Peter in der Au-Markt, Österreich` (address)
- `24-852/6682` (tax_number)

**Example 60** (doc_id: `deanon_BFG_TRAIN/137220.1`) (sent_id: `deanon_BFG_TRAIN/137220.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Ottfried Weicke, Siebenbürger Straße 6, 6135 Stans, Österreich, vertreten durch Singer-Musil Singer  RA OG, Döblinger Hauptstraße 68, 1190 Wien, wegen Verwaltungsübertretungen gem. § 1 Abs.  1 iVm § 16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966,  LGBl. für Wien Nr. 20 idF des LGBl.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Wolfgang Pagitsch` | `Mag.Dr. Wolfgang Pagitsch` |

**Missed by this rule (FN):**

- `Ottfried Weicke` (person)
- `Siebenbürger Straße 6, 6135 Stans, Österreich` (address)

**Example 61** (doc_id: `deanon_BFG_TRAIN/137227.1`) (sent_id: `deanon_BFG_TRAIN/137227.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerde des  Milena Ehebauer, Roiderweg 40, 6241 Radfeld, Österreich, gegen die Bescheide des Finanzamtes Feldkirch vom 29. Mai 2015  betreffend Einkommensteuer für die Jahre 2010 bis 2013, zu Recht erkannt:   a)

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Milena Ehebauer` (person)
- `Roiderweg 40, 6241 Radfeld, Österreich` (address)

**Example 62** (doc_id: `deanon_BFG_TRAIN/137264.1`) (sent_id: `deanon_BFG_TRAIN/137264.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Jaroslaw Makarewitsch, Dorf, Oberau 474, 6262 Schlitters, Österreich, vertreten durch NWT Wirtschaftsprüfung &  Steuerberatung GmbH, Döblinger Hauptstraße 37, 1190 Wien, betreffend Beschwerde vom  25. April 2014 gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln vom  29. Jänner 2014 betreffend Anspruchszinsen (§ 205 BAO) 2009 und 2011 zur Steuernummer  77-556/9695  beschlossen:   I. Die Beschwerde vom 25. April 2014 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |

**Missed by this rule (FN):**

- `Jaroslaw Makarewitsch` (person)
- `Dorf, Oberau 474, 6262 Schlitters, Österreich` (address)
- `77-556/9695` (tax_number)

**Example 63** (doc_id: `deanon_BFG_TRAIN/137275.1`) (sent_id: `deanon_BFG_TRAIN/137275.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Carla Schweykart, Saaz 45, 8413 Stiefing, Österreich, vertreten durch Dr. Elmar Kresbach LL.M., Rechtsanwalt,  Wipplingerstraße 29/9, 1010 Wien, vom 7. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. April 2022, Zl. Zahl, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Carla Schweykart` (person)
- `Saaz 45, 8413 Stiefing, Österreich` (address)
- `Dr. Elmar Kresbach LL.M.` (person)

**Example 64** (doc_id: `deanon_BFG_TRAIN/137294.1`) (sent_id: `deanon_BFG_TRAIN/137294.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Dr.in ÖkR Wendy Nikolaiczik, Schupfen 27, 8330 Krennach, Österreich, vom 31. Mai 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 29. April 2022, Zl. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 36,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 8 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Dr.in ÖkR Wendy Nikolaiczik` (person)
- `Schupfen 27, 8330 Krennach, Österreich` (address)

**Example 65** (doc_id: `deanon_BFG_TRAIN/137432.1`) (sent_id: `deanon_BFG_TRAIN/137432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Prof. Gerhard Eibert, Treffelsdorf/Siebenbrünnerweg 5, 5360 Rußbach, Österreich, vertreten durch Mag. Nikolaus Vasak,  Ditscheinergasse 3/10, 1030 Wien, über die Beschwerde vom 2. Dezember 2020 gegen den  Bescheid des Magistrats der Stadt Wien MA 46 Verkehrsorganisation und technische  Verkehrsangelegenheiten vom 6. November 2020 betreffend Gebrauch des Luftraumes über  dem öffentlichen Grund vor der Liegenschaft Adresse durch sieben Lampen ohne  Gebrauchserlaubnis für den Zeitraum 1.1.2017 bis 31.12.2020, nach Durchführung der  beantragten mündlichen Verhandlung am 3. August 2022 in Anwesenheit des Schriftführers Sf,  zu Recht erkannt:  Gemäß § 279 Abs. 1 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Prof. Gerhard Eibert` (person)
- `Treffelsdorf/Siebenbrünnerweg 5, 5360 Rußbach, Österreich` (address)

**Example 66** (doc_id: `deanon_BFG_TRAIN/137506.1`) (sent_id: `deanon_BFG_TRAIN/137506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Claudia Stempin, Dombaugasse 18, 3100 Nadelbach, Österreich, über die Beschwerde vom 28. April 2021 gegen die Bescheide des  Finanzamtes Österreich vom 19. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 und 2020 Steuernummer 01-623/1653  zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Claudia Stempin` (person)
- `Dombaugasse 18, 3100 Nadelbach, Österreich` (address)
- `01-623/1653` (tax_number)

**Example 67** (doc_id: `deanon_BFG_TRAIN/137554.1`) (sent_id: `deanon_BFG_TRAIN/137554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Rebecca Blaschke, Zauchensee 25, 9342 Glanz, Österreich, vom 8. Juni 2020, gegen den Bescheid des Finanzamtes Österreich  vom 27. Mai 2020, betreffend Abweisung des Antrages auf Gewährung der erhöhten  Familienbeihilfe von November 2018 bis Februar 2022, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Rebecca Blaschke` (person)
- `Zauchensee 25, 9342 Glanz, Österreich` (address)

**Example 68** (doc_id: `deanon_BFG_TRAIN/137690.1`) (sent_id: `deanon_BFG_TRAIN/137690.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  KommR Zeno Henricy, Kaplan Herzlik Straße 2, 4962 Gundholling, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 13. August 2015 gegen die Bescheide des Finanzamtes Österreich vom  14. Juli 2015 betreffend  1. Wiederaufnahme des Verfahrens der Vorsteuererstattung für 01-03/2008  2.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `KommR Zeno Henricy` (person)
- `Kaplan Herzlik Straße 2, 4962 Gundholling, Österreich` (address)

**Example 69** (doc_id: `deanon_BFG_TRAIN/138484.1`) (sent_id: `deanon_BFG_TRAIN/138484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Verwaltungsstrafsache gegen Ruprecht Seebode, Ursulinenplatz 11, 4861 Hainbach, Österreich, über die Beschwerde des  Beschuldigten vom 23. September 2022, gegen die Vollstreckungsverfügung des Magistrates  der Stadt Wien, Magistratsabteilung 6, BA 32, vom 20. September 2022, Zahl MA67/Zahl/2022,  betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen Strafe samt  Mahngebühr auf Grund der Strafverfügung vom 3. August 2022, Zahl MA67/Zahl/2022, zu  Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung des Magistrates der  Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Daniel Philip Pfau` | `Mag. Daniel Philip Pfau` |

**Missed by this rule (FN):**

- `Ruprecht Seebode` (person)
- `Ursulinenplatz 11, 4861 Hainbach, Österreich` (address)

**Example 70** (doc_id: `deanon_BFG_TRAIN/138806.1`) (sent_id: `deanon_BFG_TRAIN/138806.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Birgit Dauth, Kraschach 35, 3110 Pultendorf, Österreich, betreffend Beschwerde vom 12. März 2021 gegen den Bescheid  des Finanzamtes Österreich vom 12. Oktober 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 61-224/5753  beschlossen:  I. Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e iVm § 260 Abs. 1 lit. a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Birgit Dauth` (person)
- `Kraschach 35, 3110 Pultendorf, Österreich` (address)
- `61-224/5753` (tax_number)

**Example 71** (doc_id: `deanon_BFG_TRAIN/138927.1`) (sent_id: `deanon_BFG_TRAIN/138927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  KzlR Petra Bisdorff, Simon Mayer-Straße 6, 3800 Weinpolz, Österreich, über die Beschwerde vom 28. November 2019 gegen den Bescheid  des Finanzamtes Salzburg-Stadt (nunmehr Finanzamtes Österreich ) vom 14. November 2019  betreffend die Wiederaufnahme des Einkommensteuerverfahrens 2013 zu Recht erkannt:  I)  Der Wiederaufnahmebescheid wird aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `KzlR Petra Bisdorff` (person)
- `Simon Mayer-Straße 6, 3800 Weinpolz, Österreich` (address)

**Example 72** (doc_id: `deanon_BFG_TRAIN/139043.1`) (sent_id: `deanon_BFG_TRAIN/139043.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Nicolaus Pomaroli MAS in der  Beschwerdesache Lee Guthe, Olympiastraße 16, 3800 Scheideldorf, Österreich, im fortgesetzten Verfahren nach dem Erkenntnis  des Verwaltungsgerichtshofes vom 14. Juni 2022 zu Ra 2020/15/0085-10 über die  Beschwerden gegen die Bescheide des FA Landeck Reutte vom 24. November 2008 betreffend  Umsatzsteuer 2007, vom 21. April 2010 betreffend Umsatzsteuer 2008 sowie vom 16. August  2010 betreffend Umsatzsteuer 2009 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Nicolaus Pomaroli MAS` | `Dr. Nicolaus Pomaroli MAS` |

**Missed by this rule (FN):**

- `Lee Guthe` (person)
- `Olympiastraße 16, 3800 Scheideldorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/128877.1`) (sent_id: `deanon_BFG_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers OSR DDr. Heiko Lehwaldt, Point 6, 3232 Zauching, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR DDr. Heiko Lehwaldt`(person)
- `Point 6, 3232 Zauching, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl.

**False Positives:**

- `Mag. Emmerich Bleekmann ` — partial — gold is substring of pred: `Mag. Emmerich Bleekmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Emmerich Bleekmann`(person)

**Example 3** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christoph Mehlbeer`(person)
- `Schötz Gasse 45, 7434 Holzschlag, Österreich`(address)
- `Margarete Wiepking`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/131051.1`) (sent_id: `deanon_BFG_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Kirsten Öllrich, Grundemanngasse 2, 4755 Hub, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Öllrich`(person)
- `Grundemanngasse 2, 4755 Hub, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Ottfried Bremermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottfried Bremermann`(person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich`(address)
- `Samuel Rehnke, BSc`(person)
- `Planetengasse 30, 8455 Bischofegg, Österreich`(address)
- `14-141/9449`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/131772.1`) (sent_id: `deanon_BFG_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Dipl.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/131922.1`) (sent_id: `deanon_BFG_TRAIN/131922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Bodo Ibel  in der Verwaltungsstrafsache  Fridolin Jodeleid, Stiftergasse 75z, 2262 Stillfried, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in  Verbindung mit § 16 Abs. 1 und Tarifpost B 8 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli  1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl.

**False Positives:**

- `Mag. Mag. Bodo Ibel ` — partial — gold is substring of pred: `Mag. Mag. Bodo Ibel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Mag. Bodo Ibel`(person)
- `Fridolin Jodeleid`(person)
- `Stiftergasse 75z, 2262 Stillfried, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Karola Birkenzeller, Reifnitz 2, 4532 Rohr im Kremstal, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Pascal Tiessen, Dipl.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karola Birkenzeller`(person)
- `Reifnitz 2, 4532 Rohr im Kremstal, Österreich`(address)
- `Pascal Tiessen`(person)

**Example 9** (doc_id: `deanon_BFG_TRAIN/133042.1`) (sent_id: `deanon_BFG_TRAIN/133042.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Siegfried Borneleit  in der Beschwerdesache Ashley Kutluca,  Pabensteinstraße 20, 5132 Reith, Österreich, über die Beschwerden vom 20. Februar 2020 gegen die Bescheide des  Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 24. Jänner 2020 betreffend   1. Zurückweisung des Antrages vom 2.1.2020 auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2014 und   2.

**False Positives:**

- `Dr. Dr. Siegfried Borneleit ` — partial — gold is substring of pred: `Dr. Dr. Siegfried Borneleit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Siegfried Borneleit`(person)
- `Ashley Kutluca`(person)
- `Pabensteinstraße 20, 5132 Reith, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Lorenz Lohkampff ` — partial — gold is substring of pred: `Mag. Lorenz Lohkampff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/133768.1`) (sent_id: `deanon_BFG_TRAIN/133768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Daphne Heinzlmeir, Holzwiesengasse 15, 4723 Natternbach, Österreich, über die Beschwerde vom 20. Mai 2021 gegen den Bescheid des Finanzamtes  Österreich vom 26. April 2021 betreffend Zwangsstrafen 2021 zu Steuernummer  68-502/3247  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daphne Heinzlmeir`(person)
- `Holzwiesengasse 15, 4723 Natternbach, Österreich`(address)
- `68-502/3247`(tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/134729.1`) (sent_id: `deanon_BFG_TRAIN/134729.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Philipp Dahlhues  in der Beschwerdesache August Combach,  Damweg 1, 7501 Spitzzicken, Österreich, gegen die Bescheide des Finanzamtes Österreich vom   - 11. Juli 2017 betreffend Einkommensteuer 2014 sowie  - 06. Juni 2018 betreffend Einkommensteuer 2016 und 2017  den Beschluss:  I. Die Beschwerde betreffend Einkommensteuer 2014 wird gemäß  § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Philipp Dahlhues ` — partial — gold is substring of pred: `Mag. Philipp Dahlhues`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Philipp Dahlhues`(person)
- `August Combach`(person)
- `Damweg 1, 7501 Spitzzicken, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/134866.1`) (sent_id: `deanon_BFG_TRAIN/134866.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Daniel Priskorn  in der Beschwerdesache Felix Kerling,  Rassbergstraße 13, 3742 Passendorf, Österreich, wegen behaupteter Verletzung der Entscheidungspflicht des FA St. Johann Tamsweg Zell am See  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 beschlossen:   Die Säumnisbeschwerde wird als unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Daniel Priskorn ` — partial — gold is substring of pred: `Dr. Daniel Priskorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Daniel Priskorn`(person)
- `Felix Kerling`(person)
- `Rassbergstraße 13, 3742 Passendorf, Österreich`(address)
- `FA St. Johann Tamsweg Zell am See`(organisation)

**Example 14** (doc_id: `deanon_BFG_TRAIN/135112.1`) (sent_id: `deanon_BFG_TRAIN/135112.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Zlatan Deisen  in der Beschwerdesache des  Prof. Richard Paulick, Scharmühlwinkel 13, 3144 Baumgarten, Österreich, über 1) die Beschwerde vom 27.9.2017 gegen den Bescheid des  Finanzamtes Bruck Leoben Mürzzuschlag (nunmehr Finanzamt Österreich) vom 4.9.2017  betreffend Umsatzsteuer 2015 sowie über 2) die Beschwerde vom 7.9.2018 gegen den  Bescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 21.8.2018 betreffend Abweisung  von Anträgen auf Aufhebung der Bescheide hinsichtlich Umsatzsteuer 2011 bis 2014 nach  Durchführung einer mündlichen Verhandlung am 2.12.2021 zu Recht erkannt:   I. Den Beschwerden wird Folge gegeben.

**False Positives:**

- `Dr. Dr. Zlatan Deisen ` — partial — gold is substring of pred: `Dr. Dr. Zlatan Deisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Zlatan Deisen`(person)
- `Prof. Richard Paulick`(person)
- `Scharmühlwinkel 13, 3144 Baumgarten, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/135347.1`) (sent_id: `deanon_BFG_TRAIN/135347.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache DDr. DDr. Björn Wöber, Bisamgasse 3i, 9433 Tschrietes, Österreich, betreffend Beschwerde vom 27. Oktober 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 9. Oktober 2020 zu Steuernummer  60-281/1996  betreffend Abweisung des Antrages auf Zuerkennung der Familienbeihilfe für  KommR Hugo Vollpracht  ab Oktober 2019 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `R.` — similar text (different position): `DDr. DDr. Björn Wöber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. DDr. Björn Wöber`(person)
- `Bisamgasse 3i, 9433 Tschrietes, Österreich`(address)
- `60-281/1996`(tax_number)
- `KommR Hugo Vollpracht`(person)

**Example 16** (doc_id: `deanon_BFG_TRAIN/135585.1`) (sent_id: `deanon_BFG_TRAIN/135585.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Charles Schindele  in der Beschwerdesache Gregor Branz,  Tandlerstraße 7, 9341 Herd, Österreich, vertreten durch die Germuth Steuerberatungs GmbH, Johannesgasse 16/5,  1010 Wien, über die Beschwerde vom 17. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 14. Juli 2021 betreffend Nachsicht gemäß § 236 BAO, Steuernummer  79-519/7411  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Charles Schindele ` — partial — gold is substring of pred: `Mag. Charles Schindele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Charles Schindele`(person)
- `Gregor Branz`(person)
- `Tandlerstraße 7, 9341 Herd, Österreich`(address)
- `79-519/7411`(tax_number)

**Example 17** (doc_id: `deanon_BFG_TRAIN/135774.1`) (sent_id: `deanon_BFG_TRAIN/135774.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache MedR Uwe Preikschas, Marika Rökk-Straße 67, 3131 Anzenberg, Österreich, über die Beschwerde vom 19. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019, Steuernummer 19-302/7367, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO – wie mit Beschwerdevorentscheidung vom 26. April  2021 – teilweise Folge gegeben und der angefochtene Bescheid in diesem Sinne abgeändert.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MedR Uwe Preikschas`(person)
- `Marika Rökk-Straße 67, 3131 Anzenberg, Österreich`(address)
- `19-302/7367`(tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/136313.1`) (sent_id: `deanon_BFG_TRAIN/136313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger im  Beschwerdeverfahren über die Beschwerde der Verl nach XY, vertreten durch Laurence Krekemeyer,  Steyersberg 2, 8481 Priebing, Österreich  vom 20. Juli 2021 gegen den Zurückweisungsbescheid des Finanzamtes  Österreich vom 7. Juli 2021 betreffend Antrag auf Durchführung einer  Arbeitnehmerveranlagung, beschlossen:  Der Vorlageantrag der Beschwerdeführerin Verl nach XY vom 10.9.2021 wird gemäß § 260 Abs.  1 BAO iVm § 264 BAO (insbesondere Abs. 4 lit e und Abs. 5) als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr. Ansgar Unterberger im  Beschwerdeverfahren` — partial — gold is substring of pred: `Dr. Ansgar Unterberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Laurence Krekemeyer`(person)
- `Steyersberg 2, 8481 Priebing, Österreich`(address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/137032.1`) (sent_id: `deanon_BFG_TRAIN/137032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dirk Kreutel  in der Beschwerdesache   Samir Hentzsch, Strattnerstraße 101, 8341 Saaz, Österreich, vertreten durch Steuerberater Lynn Meinertshagen, über die  Beschwerde vom 19. Mai 2014 gegen die Bescheide des FA Klosterneuburg (jetzt Finanzamt Österreich  vom 22. April 2014 betreffend Umsatzsteuer und Körperschaftsteuer 2009-2011 und die  Bescheide über die Wiederaufnahme der jeweiligen Verfahren,   Steuernummer 10-189/1227,   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Dirk Kreutel ` — partial — gold is substring of pred: `Dr. Dirk Kreutel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dirk Kreutel`(person)
- `Samir Hentzsch`(person)
- `Strattnerstraße 101, 8341 Saaz, Österreich`(address)
- `Lynn Meinertshagen`(person)
- `FA Klosterneuburg`(organisation)
- `10-189/1227`(tax_number)

**Example 20** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Dr. Theobald Korschinek ` — partial — gold is substring of pred: `Dr. Theobald Korschinek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Theobald Korschinek`(person)
- `Dieter Papakiriakou`(person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich`(address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/137493.1`) (sent_id: `deanon_BFG_TRAIN/137493.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Herbert Kramp, Kinkstraße 6, 3541 Senftenberg, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Waldviertel, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend Abweisung des  Antrages auf Gewährung der vollen nichtindexierten Familienbeihilfe ab Jänner 2019,  Steuernummer 15-114/2120, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Herbert Kramp`(person)
- `Kinkstraße 6, 3541 Senftenberg, Österreich`(address)
- `15-114/2120`(tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/137516.1`) (sent_id: `deanon_BFG_TRAIN/137516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Friedhelm Servais, Ölbrennerweg 38, 5231 Wiesing, Österreich, über die Beschwerde vom 15. Oktober 2020 gegen den Bescheid des Finanzamtes  Österreich vom 1. Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 86-385/7500  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Friedhelm Servais`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Friedhelm Servais`(person)
- `Ölbrennerweg 38, 5231 Wiesing, Österreich`(address)
- `86-385/7500`(tax_number)

**Example 23** (doc_id: `deanon_BFG_TRAIN/137596.1`) (sent_id: `deanon_BFG_TRAIN/137596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Egon Hintenberg  in der Beschwerdesache des  OMedR Rafaela Balcius, Hoferweg 3, 3033 Manzing, Österreich, über die Beschwerde vom 11. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Egon Hintenberg ` — partial — gold is substring of pred: `Mag. Egon Hintenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Egon Hintenberg`(person)
- `OMedR Rafaela Balcius`(person)
- `Hoferweg 3, 3033 Manzing, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/137664.1`) (sent_id: `deanon_BFG_TRAIN/137664.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Dr. Emanuel Rauschmeir  in der Beschwerdesache Bertha Hueber,  Schirnes 10, 9871 Kötzing, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, betreffend Beschwerden vom 11. Februar 2020 und 27. Februar 2020  gegen die Bescheide betreffend Feststellungsbescheid Gruppenmitglied 2014 vom 11. Februar  2020 sowie vom 13. Jänner 2020 betreffend Feststellungsbescheid Gruppenmitglied 2015 und  2016 jeweils des Finanzamtes Wien 1/23 den Beschluss:   I. Die Beschwerden werden gemäß § 278 Abs. 1 lit b iVm § 256 Abs. 3 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Dr. Emanuel Rauschmeir ` — partial — gold is substring of pred: `Dr. Emanuel Rauschmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Emanuel Rauschmeir`(person)
- `Bertha Hueber`(person)
- `Schirnes 10, 9871 Kötzing, Österreich`(address)

**Example 25** (doc_id: `deanon_BFG_TRAIN/138011.1`) (sent_id: `deanon_BFG_TRAIN/138011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Sascha Grosan  in der Beschwerdesache Carla Kurrek,  Moosacker 29, 4724 Stocket, Österreich, über die Beschwerde vom 30. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Kirchdorf Perg Steyr)vom 30. November 2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 92-841/4978  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Sascha Grosan ` — partial — gold is substring of pred: `Dr. Sascha Grosan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sascha Grosan`(person)
- `Carla Kurrek`(person)
- `Moosacker 29, 4724 Stocket, Österreich`(address)
- `92-841/4978`(tax_number)

**Example 26** (doc_id: `deanon_BFG_TRAIN/138321.1`) (sent_id: `deanon_BFG_TRAIN/138321.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Miroslav Rolleder  in der Beschwerdesache Adelheid Loefflad,  Sonndorf 5, 5145 Gsotthub, Österreich, gegen die von der belangten Behörde Finanzamt Österreich am 12. Juli 2022 zu  Steuernummer 92-210/3587  ausgefertigten Bescheide über die Zurückweisung der Anträge  auf Aufhebung der Einkommensteuerbescheide für die Jahre 2017, 2018 und 2019 sowie die  am selben Tag  von der  gleichen belangten Behörde ausgefertigten Bescheide über die  Abweisung der Anträge auf Aufhebung der Einkommensteuerbescheide für die Jahre 2020 und  2021 zu Recht erkannt:   I. Die Beschwerde gegen die Bescheide über die Zurückweisung der Anträge auf Aufhebung  der Einkommensteuerbescheide für die Jahre 2017, 2018 und 2019 und gegen den Bescheid  über die Abweisung des Antrags auf Aufhebung des Einkommensteuerbescheides für das  Jahr 2021 wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Miroslav Rolleder ` — partial — gold is substring of pred: `Mag. Miroslav Rolleder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Miroslav Rolleder`(person)
- `Adelheid Loefflad`(person)
- `Sonndorf 5, 5145 Gsotthub, Österreich`(address)
- `92-210/3587`(tax_number)

</details>

---

## `Name_Gegen`

**F1:** 0.026 | **Precision:** 0.282 | **Recall:** 0.013  

**Format:** `regex`  
**Rule ID:** `789ef8cf`  
**Description:**
Captures names following 'gegen' (against) in legal proceedings.

**Content:**
```
(?:gegen\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+\(|$|\s+\d{4}|\s+Gattin|\s+und)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.282 | 0.013 | 0.026 | 78 | 22 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 22 | 56 | 1614 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129896.1`) (sent_id: `deanon_BFG_TRAIN/129896.1_2`)


in der Verwaltungsstrafsache gegen  Elina Jonethal, Steinkamperl 3, 4204 Zeil, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006 über die  zwei gleichlautenden Beschwerden der Beschuldigten vom 24. März 2020 gegen die zwei  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 25. Februar  2020, Zahl: a) MA67/xxxxx/2019 und b) MA67/yyyyy/2019, zu Recht erkannt:  I) Die zwei Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elina Jonethal` | `Elina Jonethal` |

**Missed by this rule (FN):**

- `Steinkamperl 3, 4204 Zeil, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131148.1`) (sent_id: `deanon_BFG_TRAIN/131148.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der  Verwaltungsstrafsache gegen Ronja Hertwick, Lainach 22, 9564 Mitterdorf, Österreich, über die Beschwerde vom 20.  November 2020, gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der  Stadt Wien, Magistratsabteilung 6, vom 09. November 2020, Zahl MA67/Zahl/2019, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 08. Mai 2019, Zahl MA67/Zahl/2019, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ronja Hertwick` | `Ronja Hertwick` |

**Missed by this rule (FN):**

- `Lainach 22, 9564 Mitterdorf, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/134195.1`) (sent_id: `deanon_BFG_TRAIN/134195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der  Verwaltungsstrafsache gegen Christian Nowikov, Schildlehen 2, 3512 Mautern an der Donau, Österreich, über die Beschwerde vom 02. März  2021 gegen die zwei Vollstreckungsverfügungen des Magistrates der Stadt Wien,  Magistratsabteilung 6 – BA 32, beide vom 25. Februar 2021, Zahlen A) MA67/ZahlA/2020 und  B) MA67/ZahlB/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und werden die angefochtenen Vollstreckungsverfügungen bestätigt.

| Predicted | Gold |
|---|---|
| `Christian Nowikov` | `Christian Nowikov` |

**Missed by this rule (FN):**

- `Schildlehen 2, 3512 Mautern an der Donau, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/134689.1`) (sent_id: `deanon_BFG_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Brunhild Katschmareck` | `Brunhild Katschmareck` |

**Missed by this rule (FN):**

- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen Mag. Willibald Giesser, Eichingerweg 67, 4931 Neulendt, Österreich, vertreten durch HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft, Landstraßer Hauptstraße 27,  1030 Wien, über die Beschwerde des Beschuldigten vom 1. April 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 6,  Abgabenstrafen vom 2. März 2021, Zahl: MA6/206000002559/2020, in Anwesenheit des  Verteidigers und der Behördenvertreterin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der Zurückweisungsbescheid des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Willibald Giesser` | `Mag. Willibald Giesser` |

**Missed by this rule (FN):**

- `Eichingerweg 67, 4931 Neulendt, Österreich` (address)
- `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft` (organisation)

**Example 5** (doc_id: `deanon_BFG_TRAIN/137220.1`) (sent_id: `deanon_BFG_TRAIN/137220.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Ottfried Weicke, Siebenbürger Straße 6, 6135 Stans, Österreich, vertreten durch Singer-Musil Singer  RA OG, Döblinger Hauptstraße 68, 1190 Wien, wegen Verwaltungsübertretungen gem. § 1 Abs.  1 iVm § 16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966,  LGBl. für Wien Nr. 20 idF des LGBl.

| Predicted | Gold |
|---|---|
| `Ottfried Weicke` | `Ottfried Weicke` |

**Missed by this rule (FN):**

- `Mag.Dr. Wolfgang Pagitsch` (person)
- `Siebenbürger Straße 6, 6135 Stans, Österreich` (address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter in der Verwaltungsstrafsache gegen Natascha Daschmann,  Gillhofstraße 7, 8990 Lerchenreith, Österreich, Deutschland, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 5. Mai  2022, gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  21. April 2022, Zahl MA67/Zahl/2021, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Missed by this rule (FN):**

- `Gillhofstraße 7, 8990 Lerchenreith, Österreich` (address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138030.1`) (sent_id: `deanon_BFG_TRAIN/138030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der  Verwaltungsstrafsache gegen Kirsten Fibich, Voitsbergerweg 7, 5211 Schwöll, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF.  ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, über die Beschwerde der  beschwerdeführenden Partei vom 7. April 2022 gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom  28. März 2022, Zahl MA67/Zahl/2021, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Kirsten Fibich` | `Kirsten Fibich` |

**Missed by this rule (FN):**

- `Voitsbergerweg 7, 5211 Schwöll, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/138484.1`) (sent_id: `deanon_BFG_TRAIN/138484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Verwaltungsstrafsache gegen Ruprecht Seebode, Ursulinenplatz 11, 4861 Hainbach, Österreich, über die Beschwerde des  Beschuldigten vom 23. September 2022, gegen die Vollstreckungsverfügung des Magistrates  der Stadt Wien, Magistratsabteilung 6, BA 32, vom 20. September 2022, Zahl MA67/Zahl/2022,  betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen Strafe samt  Mahngebühr auf Grund der Strafverfügung vom 3. August 2022, Zahl MA67/Zahl/2022, zu  Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und die angefochtene Vollstreckungsverfügung des Magistrates der  Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Ruprecht Seebode` | `Ruprecht Seebode` |

**Missed by this rule (FN):**

- `Mag. Daniel Philip Pfau` (person)
- `Ursulinenplatz 11, 4861 Hainbach, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/140707.1`) (sent_id: `deanon_BFG_TRAIN/140707.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der Verwal- tungsstrafsache gegen Wendelin Kohr, Fritz-Engel-Straße 17, 4692 Penetzdorf, Österreich, wegen der Verwaltungsübertretung gemäß  § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde des Beschuldigten vom 10. März 2023 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. März 2023, GZ.  MA67/Zahl/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Wendelin Kohr` | `Wendelin Kohr` |

**Missed by this rule (FN):**

- `Fritz-Engel-Straße 17, 4692 Penetzdorf, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/140876.1`) (sent_id: `deanon_BFG_TRAIN/140876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Birgitt Koran in der  Verwaltungsstrafsache gegen Traude von der Laaken, Am Sägebach 49, 5124 Marktl, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 21. November 2022  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  7. November 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Traude von der Laaken` | `Traude von der Laaken` |

**Missed by this rule (FN):**

- `Am Sägebach 49, 5124 Marktl, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/141220.1`) (sent_id: `deanon_BFG_TRAIN/141220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Julia Nellen, Siemensweg 11, 4322 Altenburg, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde der Beschuldigten vom 20. Februar 2023 gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 17. Jänner 2023, GZ.  MA67/Zahl/2022, nach Durchführung einer mündlichen Ver¬handlung am 5. Juni 2023 in  Anwesenheit der Beschuldigten und der Schriftführerin zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis aufge- hoben und das Verfahren nach § 45 Abs. 1 Z. 2. VStG eingestellt.

| Predicted | Gold |
|---|---|
| `Julia Nellen` | `Julia Nellen` |

**Missed by this rule (FN):**

- `Siemensweg 11, 4322 Altenburg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/142771.1`) (sent_id: `deanon_BFG_TRAIN/142771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der  Verwaltungsstrafsache gegen Ernst Skrzyppek, Südrandstraße 14, 9816 Litzldorf, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 11. Oktober 2023 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  15. September 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Ernst Skrzyppek` | `Ernst Skrzyppek` |

**Missed by this rule (FN):**

- `Mag. Gerhard Konrad` (person)
- `Südrandstraße 14, 9816 Litzldorf, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/143463.1`) (sent_id: `deanon_BFG_TRAIN/143463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache gegen  Corinna Zimmerninks, Johann-Rössler-Gasse 55, 4152 Obernreith, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde des Beschuldigten vom 9. Jänner 2024 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2024, GZ. MA67/Zahl/2023, zu Recht  erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Corinna Zimmerninks` | `Corinna Zimmerninks` |

**Missed by this rule (FN):**

- `Johann-Rössler-Gasse 55, 4152 Obernreith, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/144489.1`) (sent_id: `deanon_BFG_TRAIN/144489.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler in der  Verwaltungsstrafsache gegen Claire Madelung, A.-Schuricht-Straße 1292, 8934 Wolfsbachau, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 11. April 2024 gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. März 2024,  GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Claire Madelung` | `Claire Madelung` |

**Missed by this rule (FN):**

- `A.-Schuricht-Straße 1292, 8934 Wolfsbachau, Österreich` (address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Verwaltungsstrafsache  gegen Leonhard Facci, Am Aigen 26, 3214 Brandgegend, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idgF. in Verbindung mit § 4  Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF. über die Beschwerde des  Beschuldigten vom 20. April 2024 gegen das Erkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 16. April 2024, Zahl: MA67/246700162299/2024, nach mündlicher  Verhandlung am 18.6.2024 in Anwesenheit des Beschuldigten zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als die  Verhängung der Geldstrafe und der Ersatzfreiheitsstrafe aufgehoben werden sowie  gemäß § 45 Abs. 1 Z 4 und Abs. 1 letzter Satz VStG von der Verhängung einer Strafe  abgesehen und den Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Am Aigen 26, 3214 Brandgegend, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/146760.1`) (sent_id: `deanon_BFG_TRAIN/146760.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Lorenz Wilim, Feinfeld 31, 9113 Lippitzbach, Österreich, über die Beschwerde vom 30. April  2024 gegen die Vollstreckungsverfügung des Magistrates der Stadt Wien vom 24. April 2024,  Zahl: MA67/236701487597/2023, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  die angefochtene Vollstreckungsverfügung bestätigt.

| Predicted | Gold |
|---|---|
| `Lorenz Wilim` | `Lorenz Wilim` |

**Missed by this rule (FN):**

- `Feinfeld 31, 9113 Lippitzbach, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Madeleine Klingner  in der Verwaltungsstrafsache  gegen Christine Stepanek, Haidsiedlung 2, 9431 Paildorf, Österreich, über die Beschwerde vom 18. Jänner 2025 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 9. Jänner 2025, Zahl:  MA67/246700179244/2024, mit dem der Einspruch vom 13. Oktober 2024 gegen die  Strafverfügung vom 16. September 2024 mit derselben Geschäftszahl gemäß § 49 Abs. 1  VStG als verspätet zurückgewiesen wurde, zu Recht erkannt:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Christine Stepanek` | `Christine Stepanek` |

**Missed by this rule (FN):**

- `Dr.in Madeleine Klingner` (person)
- `Haidsiedlung 2, 9431 Paildorf, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_5`)


B. Das Bundesfinanzgericht hat durch die Richterin Dr.in Madeleine Klingner  in der Verwaltungsstrafsache  gegen Christine Stepanek, Haidsiedlung 2, 9431 Paildorf, Österreich  über den Antrag vom 18. Jänner 2025 auf Aufhebung der  Strafverfügung vom 16. September 2024, Zahl: MA67/246700179244/2024, den Beschluss  gefasst:    I. Gemäß § 28 und 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Antrag als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Stepanek` | `Christine Stepanek` |

**Missed by this rule (FN):**

- `Dr.in Madeleine Klingner` (person)
- `Haidsiedlung 2, 9431 Paildorf, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_9`)


C. Das Bundesfinanzgericht hat durch die Richterin Dr.in Madeleine Klingner  in der Verwaltungsstrafsache  gegen Christine Stepanek, Haidsiedlung 2, 9431 Paildorf, Österreich  über den Antrag vom 18. Jänner 2025 auf  Wiederaufnahme des Verfahrens nach § 69 AVG zum Bescheid vom 9. Jänner 2025, Zahl:  MA67/246700179244/2024, mit dem der Antrag vom 15. Dezember 2024 auf  Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Einbringung  eines Rechtsmittels gegen die Strafverfügung vom 16. September 2024 mit derselben  Geschäftszahl gemäß § 71 Abs. 1 AVG in Verbindung mit § 24 VStG als unzulässig  zurückgewiesen wurde, den Beschluss gefasst:    I. Gemäß § 28 und 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Antrag als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Stepanek` | `Christine Stepanek` |

**Missed by this rule (FN):**

- `Dr.in Madeleine Klingner` (person)
- `Haidsiedlung 2, 9431 Paildorf, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/149029.1`) (sent_id: `deanon_BFG_TRAIN/149029.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Verwaltungsstrafsache gegen Constantin Stein, Anton-Gassner-Weg 6N, 4924 Baumgarten, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl.

| Predicted | Gold |
|---|---|
| `Constantin Stein` | `Constantin Stein` |

**Missed by this rule (FN):**

- `Anton-Gassner-Weg 6N, 4924 Baumgarten, Österreich` (address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/149205.1`) (sent_id: `deanon_BFG_TRAIN/149205.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Alva Jakuszeit, Leopold-Figl-Weg 7, 2032 Enzersdorf im Thale, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  Abl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl.

| Predicted | Gold |
|---|---|
| `Alva Jakuszeit` | `Alva Jakuszeit` |

**Missed by this rule (FN):**

- `Dr. Sebastian Pfeiffer LL.M.` (person)
- `Leopold-Figl-Weg 7, 2032 Enzersdorf im Thale, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_0`)


GZ. RV/7300048/2016 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen Herrn J., geb., Wien, vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/10, 1060 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten gemäß §§ 33 Abs. 1 und Abs. 2 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom 1. August 2016 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  8. Juni 2016 , SpS 16, nach Durchführung einer mündlichen Verhandlung  am 10. Jänner 2017 in Anwesenheit des Beschuldigten, seines Verteidigers, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt: Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des Spruchsenates vom 8. Juni 2016, SpS 16, wie folgt abgeändert: I. Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer 002 anhängige Finanzstrafverfahren wird hinsichtlich des Verdachts, Herr J. hätte  vorsätzlich a) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von€ 2.403,50  zu verkürzen versucht und dadurch eine versuchte Abgabenhinterziehung gemäß §§ 13, 33 Abs. 1 FinStrG begangen, b) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden Voranmeldungen die Vorauszahlung von Umsatzsteuer für 4/2015 in Höhe von € 900,00 bewirkt und  dadurch eine Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a FinStrG begangen, c) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

**False Positives:**

- `Herrn J., geb.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_79`)


Von diesem Betrag  werden die bereits bar kassierten Beträge abgezogen und der Rest dem Subunternehmer  gegen Rechnung ausbezahlt.

**False Positives:**

- `Rechnung ausbezahlt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/130475.1`) (sent_id: `deanon_BFG_TRAIN/130475.1_42`)


Andere offenbar auf einem ähnlichen Versehen beruhende Unrichtigkeiten sind Fehler, die  Schreib- und Rechenfehler sehr nahekommen, also Fehler in der Ausdrucksweise, nicht  hingegen Fehler im Bereich des Zustandekommens und der Gestaltung des Bescheidwillens.

**False Positives:**

- `Fehler im Bereich des Zustandekommens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/130727.1`) (sent_id: `deanon_BFG_TRAIN/130727.1_70`)


Innerhalb offener Frist erhob sie dagegen Beschwerde  sowie nach Ergehen einer abweisenden Beschwerdevorentscheidung fristgerecht den Antrag  auf Vorlage der Beschwerde an das Bundesfinanzgericht.

**False Positives:**

- `Beschwerde  sowie nach Ergehen einer abweisenden Beschwerdevorentscheidung fristgerecht den Antrag  auf Vorlage der Beschwerde an das Bundesfinanzgericht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Ronald Kleile, Bakk. rer. nat., Fischteichweg 49, 4924 Hartlberg, Österreich, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 15. März 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 20. Februar 2019, Strafnummer 007, in Anwesenheit des  Beschuldigten, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Über Ronald Kleile, Bakk. rer. nat.  wird gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 17.600,00  verhängt.

**False Positives:**

- `Herrn Ronald Kleile` — positional overlap with gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)
- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/132704.1`) (sent_id: `deanon_BFG_TRAIN/132704.1_5`)


III. Der Beschwerde gegen Vorauszahlungsbescheid 2018 wird teilweise Folge gegeben.

**False Positives:**

- `Vorauszahlungsbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/132991.1`) (sent_id: `deanon_BFG_TRAIN/132991.1_34`)


I.2. Beschwerde  Mit Schreiben vom 24. Mai 2017 brachte die anwaltliche Vertretung der beschwerdeführenden  Gesellschaft dagegen Beschwerde ein und führte zunächst aus, dass der Bescheid mangelhaft  begründet sei.

**False Positives:**

- `Beschwerde ein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_161`)


Die bei Beendigung der  Personenvereinigung (Personengemeinschaft) bestehende Vertretungsbefugnis bleibt, sofern  dem nicht andere Rechtsvorschriften entgegenstehen, insoweit und solange aufrecht, als nicht  von einem der zuletzt beteiligt gewesenen Gesellschafter (Mitglieder) oder der  vertretungsbefugten Person dagegen Widerspruch erhoben wird.

**False Positives:**

- `Widerspruch erhoben wird.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_113`)


IV. Rechtslage  1. Gesetzliche Bestimmungen:  Gemäß Art. 1 Abs. 1 UStG 1994 (= Binnenmarktregelung/BMR als Anhang zu § 29 Abs. 8 UStG  1994) unterliegt auch der innergemeinschaftliche Erwerb im Inland gegen Entgelt der  Umsatzsteuer.

**False Positives:**

- `Entgelt der  Umsatzsteuer.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_114`)


Nach Art. 1 Abs. 2 UStG 1994 liegt ein innergemeinschaftlicher Erwerb gegen Entgelt vor, wenn  (Z 1) ein Gegenstand bei einer Lieferung an den Abnehmer (Erwerber) aus dem Gebiet eines  Mitgliedstaates in das Gebiet eines anderen Mitgliedstaates gelangt, auch wenn der Lieferer  den Gegenstand in das Gemeinschaftsgebiet eingeführt hat und (Z 2) der Erwerber ein  Unternehmer, der den Gegenstand für sein Unternehmen erwirbt, oder eine juristische Person  ist, die nicht Unternehmer ist oder die den Gegenstand nicht für ihr Unternehmen erwirbt.

**False Positives:**

- `Entgelt vor, wenn ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/134926.1`) (sent_id: `deanon_BFG_TRAIN/134926.1_14`)


In der Folge listete der Bf seine, aufgrund seiner „besonderen beruflichen und privaten  Konstellation“, mit nur etwa 15%-20% vom „Warenkorb 2019 der Statistik Austria“ deutlich  unterdurchschnittlichen Kosten der privaten Lebensführung auf (3 Betriebe, darunter L+F mit  wesentlichen Beiträgen zur Eigenversorgung (Wohnversorgung, Holzheizung, Lebensmittel),  Zweipersonenhaushalt mit Versorgung der pflegebedürftigen Mutter gegen Kostenbeteiligung  (Pflegegeldbezug Stufe 6).

**False Positives:**

- `Kostenbeteiligung ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/135372.1`) (sent_id: `deanon_BFG_TRAIN/135372.1_50`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Unstrittig hat der Bf mit einem gerichtlichen Vergleich vom 26.3.2002 gegen Zusicherung einer  lebenslangen monatlichen Leibrente (in Form einer angemessenen Kaupreisrente) iHv €  4 von 17 Seite 5 von 17

**False Positives:**

- `Zusicherung einer  lebenslangen monatlichen Leibrente` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_42`)


§ 11 WTFG: Wer im Gebiet der Stadt Wien in einem Beherbergungsbetrieb oder in einer  Privatunterkunft gegen Entgelt Aufenthalt nimmt (Beherbergung), hat die Ortstaxe zu  entrichten.

**False Positives:**

- `Entgelt Aufenthalt nimmt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/135628.1`) (sent_id: `deanon_BFG_TRAIN/135628.1_9`)


Am 11. Februar 2014, bei der belangten Behörde am eingelangt am 13. Februar 2014 brachte  die Bf dagegen Beschwerde ein.

**False Positives:**

- `Beschwerde ein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/136061.1`) (sent_id: `deanon_BFG_TRAIN/136061.1_230`)


Das Vorbringen, wonach das Nominalwertprinzip über lange Zeiträume zu immer größerer  Besteuerung von Scheingewinnen führe, der Nominalwert über lange Zeiträume gegen Null  gehe und es umso mehr zu einer Besteuerung von Substanz und nicht von Gewinn komme,  beruht auf der von der Bf. mutwillig herbeigeführten Einkünfteermittlung gemäß § 30 Abs. 3  EStG 1988, wo doch die reguläre Besteuerung für das gegenständlich betroffene Altvermögen  gemäß § 30 Abs. 4 Z 2 EStG 1988 wesentlich günstiger wäre.

**False Positives:**

- `Null  gehe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/136261.1`) (sent_id: `deanon_BFG_TRAIN/136261.1_37`)


Da aber die Wertsteigerung von 2009 auf 2015 die durch Professionisten gegen Rechnung und  Gewährleistung erbrachte Arbeitsleistung beinhaltet, erscheint es sachgerecht, als Ausgaben  im Rahmen der Eigenleistung nur die Hälfte dieses Betrages zum Ansatz zu bringen.

**False Positives:**

- `Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/136471.1`) (sent_id: `deanon_BFG_TRAIN/136471.1_6`)


Mit Schriftsatz vom 15.06.2021 brachte die Beschwerdeführerin durch die  Erwachsenenvertretung Salzburg dagegen Beschwerde ein.

**False Positives:**

- `Beschwerde ein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/136516.1`) (sent_id: `deanon_BFG_TRAIN/136516.1_5`)


Mit Schreiben vom 21. April 2021 erhob die steuerliche Vertretung der Beschwerdeführerin  dagegen Beschwerde.

**False Positives:**

- `Beschwerde.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/137355.1`) (sent_id: `deanon_BFG_TRAIN/137355.1_136`)


Punkt 2.5.8.2 der AGB 2006 sowie Punkt 2.12.2 der AGB 2011 lauten wörtlich:  „Der Kunde tritt bereits hiermit seine Rechte aus den für das Leasingfahrzeug abgeschlossenen  Versicherungen (unabhängig davon, wer den Versicherungsschutz eingedeckt hat) sowie alle  Ansprüche wegen Beschädigung des Leasingfahrzeuges gegen Dritte und deren  Haftpflichtversicherungen an Ronald Leinberger  ab, die die Abtretungen annimmt.

**False Positives:**

- `Dritte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Leinberger`(person)

**Example 19** (doc_id: `deanon_BFG_TRAIN/137506.1`) (sent_id: `deanon_BFG_TRAIN/137506.1_23`)


Auch der Verstoß u.a. gegen Verordnungen der  EU ist eine Vertragsverletzung (vgl. aaO, § 258 Rn. 4 f.).   Art. 260 Abs. 1 AEUV bestimmt: „Stellt der Gerichtshof der Europäischen Union fest,  dass ein Mitgliedstaat gegen eine Verpflichtung aus den Verträgen verstoßen hat, so  hat dieser Staat die Maßnahmen zu ergreifen, die sich aus dem Urteil des Gerichtshofs  ergeben.“

**False Positives:**

- `Verordnungen der  EU ist eine Vertragsverletzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/137514.1`) (sent_id: `deanon_BFG_TRAIN/137514.1_11`)


Mit Schreiben vom 22.03.2022 erhob der Bf. dagegen Beschwerde und führte dazu aus, dass er  seine Beschwerde nachweislich am 09.12.2021 an die Poststelle der Justizanstalt übergeben  habe und daher Rechtzeitigkeit gegeben sei.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/137693.1`) (sent_id: `deanon_BFG_TRAIN/137693.1_53`)


Mit der Äußerung wurde die  Kopie einer gekürzten Urteilsausfertigung des Landesgerichts Innsbruck im Verfahren der P  GmbH gegen T vorgelegt.

**False Positives:**

- `T vorgelegt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/138506.1`) (sent_id: `deanon_BFG_TRAIN/138506.1_31`)


Da jeder dieser Bescheide gesondert anfechtbar ist (§ 243 BAO), muss jede Beschwerde für sich  den Formalerfordernissen der BAO für Rechtsbehelfe gegen Bescheide entsprechen.

**False Positives:**

- `Bescheide entsprechen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/138984.1`) (sent_id: `deanon_BFG_TRAIN/138984.1_16`)


Ein unehrliches steuerliches Verhalten des Bf. dokumentiere auch der gegen Jahresende 2010  erhobene Umstand, dass der Bf. einen PKW mit ausländischem (italienischem) Kennzeichen in  Österreich benutzte, weswegen er als steuerliche Konsequenz im Bereich NOVA und KFZ-

**False Positives:**

- `Jahresende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/138984.1`) (sent_id: `deanon_BFG_TRAIN/138984.1_126`)


17. Allein der nach Ansicht der Amtspartei ein unehrliches steuerliches Verhalten des Bf.  dokumentierende gegen Jahresende 2010 erhobene Umstand, dass der Bf. einen PKW mit  ausländischem (italienischen) Kennzeichen in Österreich nutzte, weswegen er als steuerliche  9 von 11 Seite 10 von 11

**False Positives:**

- `Jahresende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/140025.1`) (sent_id: `deanon_BFG_TRAIN/140025.1_14`)


Die ausständigen Erklärungen und Daten bezüglich der Mängelbescheide und diverser  eingebrachter Beschwerden (gegen Einkommensteuer 2019 und 2020, Umsatzsteuer 2019 und  2020, Verspätungszuschlag 2019 und 2020) würden bis 25. Oktober 2022 ganz sicher  nachgereicht werden.

**False Positives:**

- `Einkommensteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/140298.1`) (sent_id: `deanon_BFG_TRAIN/140298.1_5`)


Mit Schreiben vom 19. November 2022 brachte die Beschwerdeführerin über Finanzonline  dagegen Beschwerde ein.

**False Positives:**

- `Beschwerde ein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_65`)


10. Wohnraumvermieter überlassen Wohnraum zur in der Regel ausschließlichen Nutzung  durch ihre Mieter auf eine bestimmte Zeit gegen Entgelt.

**False Positives:**

- `Entgelt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/140445.1`) (sent_id: `deanon_BFG_TRAIN/140445.1_178`)


In Bezug auf die Frage der Ansässigkeit gemäß MwStSystRL bei einer Wohnungsvermietung  ist zudem darauf zu verweisen, dass Generalanwältin Kokott im EuGH-Verfahren Ingrid  Schmelz gegen Finanzamt Waldviertel, Rechtssache C-97/09, erklärte, Frau Schmelz, eine  deutsche Staatsbürgerin mit Wohnsitz in Deutschland, welche in Ostösterreich eine Wohnung  vermietet hatte, habe gemäß der Mehrwertsteuersystemrichtlinie als in Österreich ansässige  Person zu gelten (vgl. Endfellner, FJ 2010, 270, zweitletzter Aufzählungspunkt).

**False Positives:**

- `Finanzamt Waldviertel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/141765.1`) (sent_id: `deanon_BFG_TRAIN/141765.1_34`)


7. Das Bundesfinanzgericht (BFG) hatte – nach Direktvorlage - mit Erkenntnis vom 13.12.2016,  RV/3101114/2016, die Beschwerde als unbegründet abgewiesen und im Wesentlichen dahin  begründet:  Wird ein Baurecht an einem unbebauten Grundstück gegen Entgelt (hier die Leistung eines  jährlichen Bauzinses) auf 50 Jahre begründet, dann bemißt sich die Grunderwerbsteuer  ausgehend von der Gegenleistung, di. vom Wert der Bauzinsverpflichtung gemäß § 15 BewG (=  18facher Jahreswert des Entgelts; vgl.

**False Positives:**

- `Entgelt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_TRAIN/141768.1`) (sent_id: `deanon_BFG_TRAIN/141768.1_33`)


Einlangen der Zwangsstrafe erledigt worden sei und nicht erst gegen Ende der Nachfrist.

**False Positives:**

- `Ende der Nachfrist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_TRAIN/142369.1`) (sent_id: `deanon_BFG_TRAIN/142369.1_21`)


Die Verluste der Gesellschaft wurden ebenso wenig anerkannt wie die beantragten  Vorsteuerbeträge, die Umsätze der Jahre 2013 bis 2015 würden dagegen Kraft Rechnung  geschuldet.

**False Positives:**

- `Kraft Rechnung  geschuldet.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_TRAIN/142418.1`) (sent_id: `deanon_BFG_TRAIN/142418.1_40`)


Ferner stehe die Erbringung von weiteren Dolmetschleistungen an Privatpersonen oder andere  Auftraggeber gegen Barzahlung nicht im Widerspruch zur allgemeinen Lebenserfahrung.

**False Positives:**

- `Barzahlung nicht im Widerspruch zur allgemeinen Lebenserfahrung.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_TRAIN/142862.1`) (sent_id: `deanon_BFG_TRAIN/142862.1_139`)


Tatsächlich sollen die Kosten vom Bf jeweils „bedarfsgerecht“ gegen Vorlage entsprechender  Einzelbelege („z.B. für Benzin, Fahrzeugbereifung, Versicherung etc.“) vergütet worden sein.

**False Positives:**

- `Vorlage entsprechender  Einzelbelege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_TRAIN/143456.1`) (sent_id: `deanon_BFG_TRAIN/143456.1_15`)


Im Vorlageantrag vom 2.3.2021 wandte der Bf ein, das Finanzamt habe in den Vorjahren  sämtliche Wohnungsvermietungen als Liebhaberei beurteilt, wogegen Beschwerde eingelegt  worden sei.

**False Positives:**

- `Beschwerde eingelegt  worden sei.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_TRAIN/143456.1`) (sent_id: `deanon_BFG_TRAIN/143456.1_100`)


Keine der  Parteien erhob dagegen Einwendungen.

**False Positives:**

- `Einwendungen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_TRAIN/144196.1`) (sent_id: `deanon_BFG_TRAIN/144196.1_9`)


Mit Eingabe vom 03.11.2023 erhob die Beschwerdeführerin (Bf.) rechtzeitig dagegen  Beschwerde und stellte einen Antrag gem. § 299 BAO auf Nichtigerklärung des  Vorauszahlungsbescheides 2024 und Folgejahre.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_TRAIN/144505.1`) (sent_id: `deanon_BFG_TRAIN/144505.1_169`)


Obwohl die Mitgliedstaaten gemäß Art. 10 Abs. 1 dazu verpflichtet  gewesen seien, alle Überschusserlöse, die sich aus der Anwendung der Obergrenze für die  Markterlöse ergeben, gezielt zur Finanzierung von Maßnahmen zu verwenden, mit denen  Stromendkunden unterstützt werden, um die Auswirkungen der hohen Strompreise auf diese  Kunden abzumildern, und die Wichtigkeit dieser Maßnahme sogar noch durch die beispielhafte  Aufzählung in Abs. 2 verdeutlicht werde, finde sich im EKBSG, direkt verstoßend gegen EU  Recht, keinerlei derartige Bestimmung.

**False Positives:**

- `EU  Recht, keinerlei derartige Bestimmung.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_TRAIN/144625.1`) (sent_id: `deanon_BFG_TRAIN/144625.1_86`)


Im konkreten Fall erfolgte jeweils der Tausch eines Grundstücksanteiles gegen Anteile an der  Agrargemeinschaft A Waldgenossenschaft, die aus der Liegenschaft EZ KG besteht.

**False Positives:**

- `Anteile an der  Agrargemeinschaft A Waldgenossenschaft, die aus der Liegenschaft EZ KG besteht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_TRAIN/144887.1`) (sent_id: `deanon_BFG_TRAIN/144887.1_177`)


Ausländische Einkünfte sind dagegen Teil der Bemessungsgrundlage, auch wenn sie durch  DBA steuerbefreit sind (EStR 7598 und LStR 834 auf Grund von VwGH 24.5.07, 2004/15/0051  und BFG 30.6.14, RV/4100587/2013;

**False Positives:**

- `Teil der Bemessungsgrundlage, auch wenn sie durch  DBA steuerbefreit sind` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_TRAIN/145241.1`) (sent_id: `deanon_BFG_TRAIN/145241.1_35`)


Familienheimfahrten sind hingegen Fahrten zwischen Wohnsitz am Arbeitsort und  Familienwohnsitz, also zwischen zwei Wohnungen.

**False Positives:**

- `Fahrten zwischen Wohnsitz am Arbeitsort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_TRAIN/145791.1`) (sent_id: `deanon_BFG_TRAIN/145791.1_25`)


[Anmerkung Richter: Der „erste“ Vorlagenantrag hat auch die Anspruchszinsen umfasst, der  „zweite“ Vorlageantrag war demnach entbehrlich, der Vorlageantrag ist jedenfalls rechtzeitig]  „Die ggst.BSV weist eine angebliche Beschwerde dat.20240326 gegen Bescheide Zinsen 2016  angebl.dat.20240111 und 2017 dat.2024018 ab.

**False Positives:**

- `Bescheide Zinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_280`)


Ebenso habe das LG L in seinem Strafverfahren gegen Hrn.

**False Positives:**

- `Hrn.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_313`)


Das Bundesfinanzgericht wies die Beschwerde mit Erkenntnis vom 04.04.2017 zu  RV/2100778/2014 als unbegründet ab, wogegen Revision an den VwGH erhoben wurde.

**False Positives:**

- `Revision an den VwGH erhoben wurde.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_TRAIN/145979.1`) (sent_id: `deanon_BFG_TRAIN/145979.1_27`)


Der Einschreiter legt in seinem Antrag in keiner Weise einen qualifizierten Verstoß gegen  Unionsrecht dar.

**False Positives:**

- `Unionsrecht dar.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_TRAIN/146327.1`) (sent_id: `deanon_BFG_TRAIN/146327.1_36`)


Bereits daraus ergebe sich die  Zurückweisung der vorliegenden Beschwerde, da sie sich gegen Nichtbescheide richte.

**False Positives:**

- `Nichtbescheide richte.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_TRAIN/146476.1`) (sent_id: `deanon_BFG_TRAIN/146476.1_56`)


Allerdings stellt sich für das Bundesfinanzgericht die Frage, ob der Bf. mit seiner Eingabe vom  4.8.2024 tatsächlich Beschwerde gegen Einkommensteuerbescheid 2023 erheben wollte.

**False Positives:**

- `Einkommensteuerbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_TRAIN/146508.1`) (sent_id: `deanon_BFG_TRAIN/146508.1_8`)


Mit Schreiben vom 7. Jänner 2021 erhob die beschwerdeführende Gesellschaft dagegen  Beschwerde und führte aus, dass die belangte Behörde den § 176 Abs. 2 BAO in unrichtiger  Weise auf den gegenständlichen Fall angewendet habe.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_TRAIN/146845.1`) (sent_id: `deanon_BFG_TRAIN/146845.1_61`)


Am 21.08.2020 wurde dagegen Beschwerde erhoben und diese am 22.01.2021 mit  Beschwerdevorentscheidung abgewiesen, da Rechtsirrtümer und rechtliche Fehlbeurteilungen  keine neuen Tatsachen im Sinne des § 303 BAO seien.

**False Positives:**

- `Beschwerde erhoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_TRAIN/147029.1`) (sent_id: `deanon_BFG_TRAIN/147029.1_77`)


Sonstige Einlagen sind täglich fällige Gelder des Zahlungsverkehrs  (Sichteinlagen), alle Kündigungs- und Festgelder sowie die Einlagen gegen Ausgabe von  Kassenscheinen.

**False Positives:**

- `Ausgabe von  Kassenscheinen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_TRAIN/147238.1`) (sent_id: `deanon_BFG_TRAIN/147238.1_19`)


Mit Schreiben vom 25. September 2023 erhob der Beschwerdeführer dagegen Beschwerde  und verwies insbesondere auf den bereits vorgelegten Arbeitsvertrag beim FH, wo auf Seite 2,  Absatz 1 festgelegt werde, dass der Arbeitnehmer in Bereichen, die dieser als wissenschaftlich  ansehe, mitzuarbeiten habe.

**False Positives:**

- `Beschwerde ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_TRAIN/147328.1`) (sent_id: `deanon_BFG_TRAIN/147328.1_4`)


Mit FinanzOnline-Eingabe vom 17.7.2024 erhob der Bf dagegen Beschwerde.

**False Positives:**

- `Beschwerde.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_TRAIN/147760.1`) (sent_id: `deanon_BFG_TRAIN/147760.1_44`)


Obwohl ich nicht in Österreich war, wurde mir die Strafverfügung zugestellt und  auch hatte ich keine Möglichkeit, fristgerecht dagegen Beschwerde einzulegen.

**False Positives:**

- `Beschwerde einzulegen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_TRAIN/148041.1`) (sent_id: `deanon_BFG_TRAIN/148041.1_219`)


Es werden nur Aufwendungen berücksichtigt, die der  Steuerpflichtige getragen hat, nicht hingegen Aufwendungen anderer Personen.

**False Positives:**

- `Aufwendungen anderer Personen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_TRAIN/149265.1`) (sent_id: `deanon_BFG_TRAIN/149265.1_5`)


Mit Schreiben vom 26. August 2020 erhob der Beschwerdeführer dagegen Beschwerde und  brachte vor, dass der halbe Familienbonus plus und der Unterhaltsabsetzbetrag für volle 12  Monate nicht berücksichtigt worden seien.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_TRAIN/149834.1`) (sent_id: `deanon_BFG_TRAIN/149834.1_146`)


Eine  Vereinbarung über die Überlassung des Raums – laut Planung – von etwa 103m² an Bf1 gegen  Entgelt fehlt.

**False Positives:**

- `Entgelt fehlt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_Representative`

**F1:** 0.012 | **Precision:** 0.039 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `90e1f5a6`  
**Description:**
Captures names following 'vertreten durch' (represented by).

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.039 | 0.007 | 0.012 | 304 | 12 | 292 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 12 | 292 | 1624 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/133177.1`) (sent_id: `deanon_BFG_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Podzus  in der Beschwerdesache der  Planung Monuniost, Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich, vertreten durch Ilona Christahl,  Beschlingerstraße 66, 3233 Schlögelsbach, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ilona Christahl` | `Ilona Christahl` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Juliana Podzus` (person)
- `Planung Monuniost` (organisation)
- `Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich` (address)
- `Beschlingerstraße 66, 3233 Schlögelsbach, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/133706.1`) (sent_id: `deanon_BFG_TRAIN/133706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gloria Andres, Fuchshub 19, 4204 Aigen, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die Beschwerde vom  3. Juli 2015 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 29. Mai 2015  betreffend Anspruchszinsen (§ 205 BAO) 2003, 2004, 2005 und 2006 zu Steuernummer  06-338/7966  zu Recht erkannt:   I. Die angefochtenen Bescheide werden - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Gloria Andres` (person)
- `Fuchshub 19, 4204 Aigen, Österreich` (address)
- `06-338/7966` (tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/135177.1`) (sent_id: `deanon_BFG_TRAIN/135177.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Rüdiger Piotrowska  in der Beschwerdesache Ilhan Bartenschläger,  Bärngarten 834, 4212 Zissingdorf, Österreich, vertreten durch Egon Kohlschmied, betreffend die Beschwerde vom  4. Dezember 2015 gegen die Bescheide des Finanzamt Grieskirchen Wels (jetzt Finanzamt Österreich) vom  6. November 2015 zu Steuernummer 64-279/2417  betreffend Anspruchszinsen (§ 205  BAO) 2009, Anspruchszinsen (§ 205 BAO) 2013, Wiederaufnahme § 303 BAO /  ESt 2009,  Wiederaufnahme § 303 BAO /  ESt 2010, Wiederaufnahme § 303 BAO /  ESt 2011,  Wiederaufnahme § 303 BAO /  ESt 2012, Wiederaufnahme § 303 BAO /  USt 2009,  Wiederaufnahme § 303 BAO /  USt 2010, Wiederaufnahme § 303 BAO /  USt 2011 und  Wiederaufnahme § 303 BAO /  USt 2012   beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Egon Kohlschmied` | `Egon Kohlschmied` |

**Missed by this rule (FN):**

- `Mag. Rüdiger Piotrowska` (person)
- `Ilhan Bartenschläger` (person)
- `Bärngarten 834, 4212 Zissingdorf, Österreich` (address)
- `Finanzamt Grieskirchen Wels` (organisation)
- `64-279/2417` (tax_number)

**Example 3** (doc_id: `deanon_BFG_TRAIN/135479.1`) (sent_id: `deanon_BFG_TRAIN/135479.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Ali Dill, Hauswiesenweg 8, 4702 Bergern, Österreich, vertreten durch Wendelin Spätling,  Wasserturmstraße 114, 6791 Gortipohl, Österreich, betreffend die Beschwerde vom 6. Mai 2020 gegen den Bescheid  des Finanzamtes Neunkirchen Wr. Neustadt vom 26. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zur Steuernummer 81-336/9133  beschlossen:  I. Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) vom 28. Dezember 2020 wird gemäß § 264 Abs. 4 lit. e iVm § 260 Abs. 1 lit. b  iVm § 264 Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wendelin Spätling` | `Wendelin Spätling` |

**Missed by this rule (FN):**

- `Mag. Markus Knechtl LL.M.` (person)
- `Ali Dill` (person)
- `Hauswiesenweg 8, 4702 Bergern, Österreich` (address)
- `Wasserturmstraße 114, 6791 Gortipohl, Österreich` (address)
- `81-336/9133` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_0`)


GZ. RV/7300048/2016 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen Herrn J., geb., Wien, vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/10, 1060 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten gemäß §§ 33 Abs. 1 und Abs. 2 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom 1. August 2016 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  8. Juni 2016 , SpS 16, nach Durchführung einer mündlichen Verhandlung  am 10. Jänner 2017 in Anwesenheit des Beschuldigten, seines Verteidigers, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt: Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des Spruchsenates vom 8. Juni 2016, SpS 16, wie folgt abgeändert: I. Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer 002 anhängige Finanzstrafverfahren wird hinsichtlich des Verdachts, Herr J. hätte  vorsätzlich a) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von€ 2.403,50  zu verkürzen versucht und dadurch eine versuchte Abgabenhinterziehung gemäß §§ 13, 33 Abs. 1 FinStrG begangen, b) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden Voranmeldungen die Vorauszahlung von Umsatzsteuer für 4/2015 in Höhe von € 900,00 bewirkt und  dadurch eine Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a FinStrG begangen, c) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

**False Positives:**

- `Brehm ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_1`)


Gerald Erwin Ehgartner in der Beschwerdesache Janis Forch, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Jank Weiler Operenyi Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janis Forch`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Erika Zajcenko, Volksheimstraße 9, 8784 Trieben, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Monika Pfundner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erika Zajcenko`(person)
- `Volksheimstraße 9, 8784 Trieben, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Catharina Moewis,  Im Klosterhof 21N, 5241 Großenaich, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Moewis`(person)
- `Im Klosterhof 21N, 5241 Großenaich, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/128762.1`) (sent_id: `deanon_BFG_TRAIN/128762.1_43`)


Mit Beschluss  vom 4. Dezember 2019, dem Bundesfinanzgericht zugestellt am 19. Dezember 2019, hatte  der Verwaltungsgerichtshof die außerordentliche Revision des betreffenden  Abgabepflichtigen, wie der Bf vertreten durch RA, zurückgewiesen.

**False Positives:**

- `RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_2`)


Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Elisabeth Tombült,  Landschacher Gasse 33, 3925 Neumelon, Österreich, vertreten durch Dr. Edelsbacher & Partner Wirtschaftsprüfungs- und Steuer-  beratungsgesellschaft mbH, Ernst-Grein-Straße 14A, 5026 Salzburg, betreffend Beschwerde  vom 17. Juli 2019 gegen den Bescheid des Finanzamtes vom 18. Juni 2019 über die Festsetzung  von Anspruchszinsen (§ 205 BAO) 2016 beschlossen:  Der Vorlageantrag vom 15.06.2020 wird gemäß § 260 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e  BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Elisabeth Tombült`(person)
- `Landschacher Gasse 33, 3925 Neumelon, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Serge Anhalt, Ebenfeld 7, 4776 Mitterndorf, Österreich,  vertreten durch WP_GmbH, WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  44-050/5905  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `WP` — no gold match — likely missing annotation
- `Mag` — no gold match — likely missing annotation
- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Serge Anhalt`(person)
- `Ebenfeld 7, 4776 Mitterndorf, Österreich`(address)
- `44-050/5905`(tax_number)

**Example 8** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_2`)


Kff. Gwendolin Ziehr,  Reebokplatz 60, 4083 Gemersdorf, Österreich, vertreten durch BG&P Binder Grossek & Partner Steuerberatung und  Wirtschafts- prüfung GmbH, Neufeldweg 93, 8010 Graz, über die Beschwerden vom 10. Juni  2015 gegen die Bescheide des Finanzamtes Graz-Umgebung vom 14. April 2015 betreffend  Festsetzung des Dienstgeberbeitrages (DB) und des Zuschlages zum Dienstgeberbeitrag (DZ)  für die Jahre 2009, 2010, 2011, 2012 und 2013, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `BG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Reebokplatz 60, 4083 Gemersdorf, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Raphael Skowroneck, MBA, Herbert-Wochinz-Passage 77, 4712 Armau, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Erich Schwaiger`(person)
- `Raphael Skowroneck, MBA`(person)
- `Herbert-Wochinz-Passage 77, 4712 Armau, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Mehmet Bildstein, Josef Glanner-Gasse 168, 3142 Obermoos, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 72-182/5875  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Imre ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alois Pichler`(person)
- `Mehmet Bildstein`(person)
- `Josef Glanner-Gasse 168, 3142 Obermoos, Österreich`(address)
- `72-182/5875`(tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Mercuria Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Lubomir Baltßun`(person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache OStR Karl Ostendarp, Am Tremmel 13, 5742 Vorderkrimml, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 84-986/6948  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Eva Maria Koller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Markus Knechtl LL.M.`(person)
- `OStR Karl Ostendarp`(person)
- `Am Tremmel 13, 5742 Vorderkrimml, Österreich`(address)
- `84-986/6948`(tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenV, die RichterinR sowie die  fachkundigen Laienrichter LR1 und LR2 in der Beschwerdesache Bf, Wilhelmsederstraße 93, 9112 Gönitz, Österreich, vertreten  durch Stb, über die Beschwerde vom 27. April 2015 gegen die Bescheide des Finanzamtes St.  Johann Tamsweg Zell am See vom 27. März 2015 betreffend Umsatzsteuer 2012 und  Umsatzsteuer 2013, Steuernummer 91-666/8239, nach Durchführung einer mündlichen  Verhandlung am 10. Juni 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wilhelmsederstraße 93, 9112 Gönitz, Österreich`(address)
- `91-666/8239`(tax_number)

**Example 14** (doc_id: `deanon_BFG_TRAIN/129231.1`) (sent_id: `deanon_BFG_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Bartholomäus Malcharzik, Ogugasse 8, 4483 Pirchhorn, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `EWT Schuster ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bartholomäus Malcharzik`(person)
- `Ogugasse 8, 4483 Pirchhorn, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Elena Zilinski, Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Treuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Elena Zilinski`(person)
- `Alice-Harnoncourt-Platz 120, 5222 Parz, Österreich`(address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/129254.1`) (sent_id: `deanon_BFG_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache StR VetR Corbinian Drügemöller, Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grant Thornton Austria GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.Dr. Thomas Leitner`(person)
- `StR VetR Corbinian Drügemöller`(person)
- `Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich`(address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe,  Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

**False Positives:**

- `Johann Putzer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Irene van der Hoven`(person)
- `Kordelia van Clewe`(person)
- `Piettegasse 15, 3341 Oberamt, Österreich`(address)
- `FA Tirol Ost`(organisation)
- `20-364/1486`(tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `ICON Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Vivian Wenk`(person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich`(address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Westra  GmbH Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pastel Pharma`(organisation)
- `Retzenegg 222, 3242 Ramsau, Österreich`(address)

**Example 21** (doc_id: `deanon_BFG_TRAIN/129503.1`) (sent_id: `deanon_BFG_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache Gabriele Lemmon, Bakk. rer. nat., Graf-Egger-Straße 4, 4712 Armau, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 49-573/3569  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `Halpern ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gabriele Lemmon, Bakk. rer. nat.`(person)
- `Graf-Egger-Straße 4, 4712 Armau, Österreich`(address)
- `49-573/3569`(tax_number)

**Example 22** (doc_id: `deanon_BFG_TRAIN/129571.1`) (sent_id: `deanon_BFG_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Annemarie Cünzer, Kothbauerstraße 39, 4152 Mühel, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Annemarie Cünzer`(person)
- `Kothbauerstraße 39, 4152 Mühel, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/129872.1`) (sent_id: `deanon_BFG_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache James Loratis, Platzerweg 28, 4673 Baumgarting, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang Freilinger`(person)
- `James Loratis`(person)
- `Platzerweg 28, 4673 Baumgarting, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Shoshana Schweinforth, Brenggenalm 15, 8551 Gieselegg, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 78-461/2049  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vertreter ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Shoshana Schweinforth`(person)
- `Brenggenalm 15, 8551 Gieselegg, Österreich`(address)
- `78-461/2049`(tax_number)

**Example 25** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daisy Mikoleizik`(person)
- `Schulwiesen 13, 4203 Stratreith, Österreich`(address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_188`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/130424.1`) (sent_id: `deanon_BFG_TRAIN/130424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Vivian Classens, Bakk. iur. BEd, Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich  vertreten durch Vertreter, gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 24. November 2015, betreffend Grunderwerbsteuer  aufgrund des Übergabsvertrages mit N.N. (Erf. Nr., Steuernummer), zu Recht erkannt:   Der eingeschränkten Beschwerde wird Folge gegeben.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vivian Classens, Bakk. iur. BEd`(person)
- `Vogel & Noot-Straße 20, 3644 St. Georgen, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_TRAIN/130444.1`) (sent_id: `deanon_BFG_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Lars Hoerl  in der Beschwerdesache VetR Christina Schlotfeldt,  Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Vedat Gökdemir` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof. Lars Hoerl`(person)
- `VetR Christina Schlotfeldt`(person)
- `Weinzierl-Roßgrabenstraße 783, 4732 Kirnwies, Österreich`(address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Cevik  in der Beschwerdesache der Bf., (im  Beschwerdeverfahren) vertreten durch Rechtsanwälte Lehofer & Lehofer,  Kalchberggasse 6/1.

**False Positives:**

- `Rechtsanwälte Lehofer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Lubomir Cevik`(person)

**Example 30** (doc_id: `deanon_BFG_TRAIN/130559.1`) (sent_id: `deanon_BFG_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Julia Nöllecke  in der Beschwerdesache Esra Leßnick, LLB,  Hackermillerstraße 133, 8940 Döllach, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  06-833/3820, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Julia Nöllecke`(person)
- `Esra Leßnick, LLB`(person)
- `Hackermillerstraße 133, 8940 Döllach, Österreich`(address)
- `06-833/3820`(tax_number)

**Example 31** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Wolfgang Aigner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wolfgang Aigner`(person)
- `Wladimir Nüssli`(person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich`(address)

**Example 32** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

**False Positives:**

- `Helmut Binder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alfred Klaming`(person)
- `Matthäus Buskens`(person)
- `Edlach 19, 3141 Oberkilling, Österreich`(address)

**Example 33** (doc_id: `deanon_BFG_TRAIN/130834.1`) (sent_id: `deanon_BFG_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `BKS Steuerberatungs GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)

**Example 34** (doc_id: `deanon_BFG_TRAIN/130839.1`) (sent_id: `deanon_BFG_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Zarin Finke,  Brauhausplatz 29, 9422 Untereberndorf, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zarin Finke`(person)
- `Brauhausplatz 29, 9422 Untereberndorf, Österreich`(address)

**Example 35** (doc_id: `deanon_BFG_TRAIN/130895.1`) (sent_id: `deanon_BFG_TRAIN/130895.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Priv.-Doz. Univ.-Prof. Ernst Uckermarck  über die Vorlageerinnerung der  Erich Ennulat, Leumühle 11, 4680 Leiten, Österreich  vertreten durch Hedwig Weber, Ausseer Straße 32, 8940 Liezen, vom  22.10.2020 zur Beschwerde vom 06.05.2020 gegen den Bescheid des Finanzamtes Judenburg  Liezen vom 01.04.2020 betreffend Sicherstellung gemäß § 232 BAO beschlossen:  Die Vorlageerinnerung wird als unzulässig zurückgewiesen.

**False Positives:**

- `Hedwig Weber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Univ.-Prof. Ernst Uckermarck`(person)
- `Erich Ennulat`(person)
- `Leumühle 11, 4680 Leiten, Österreich`(address)

**Example 36** (doc_id: `deanon_BFG_TRAIN/130909.1`) (sent_id: `deanon_BFG_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Miriam Kloeppel, Hollehnerweg 19, 9061 Nußberg, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Wolfgang Freilinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wolfgang Freilinger`(person)
- `Miriam Kloeppel`(person)
- `Hollehnerweg 19, 9061 Nußberg, Österreich`(address)

**Example 37** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Jean Wohlrap, Weyprechtgasse 44M, 9701 Nußdorf, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Astoria Steuerberatung GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Jean Wohlrap`(person)
- `Weyprechtgasse 44M, 9701 Nußdorf, Österreich`(address)

**Example 38** (doc_id: `deanon_BFG_TRAIN/131046.1`) (sent_id: `deanon_BFG_TRAIN/131046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Hugo Moewius, Studenygasse 11, 4623 Buchleiten, Österreich, vertreten durch SCHIETZ + MAUREDER Steuerberatung GmbH,  Veldner Straße 29, 4120 Neufelden, über die Beschwerde vom 20. Juni 2017 gegen den  Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 9. Juni 2017 betreffend  Einkommensteuer 2015 Steuernummer 03-874/1042  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `SCHIETZ ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hugo Moewius`(person)
- `Studenygasse 11, 4623 Buchleiten, Österreich`(address)
- `03-874/1042`(tax_number)

**Example 39** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Samuel Rehnke` — partial — pred is substring of gold: `Samuel Rehnke, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottfried Bremermann`(person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich`(address)
- `Samuel Rehnke, BSc`(person)
- `Planetengasse 30, 8455 Bischofegg, Österreich`(address)
- `14-141/9449`(tax_number)

**Example 40** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Jeanne von Fritz  in der Beschwerdesache Martha Michenfelder,  Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Dkfm` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Univ.-Prof.in Jeanne von Fritz`(person)
- `Martha Michenfelder`(person)
- `Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich`(address)

**Example 41** (doc_id: `deanon_BFG_TRAIN/131327.1`) (sent_id: `deanon_BFG_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Urs Grennigloh, Weitenfeld 26, 5273 Schwathof, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Urs Grennigloh`(person)
- `Weitenfeld 26, 5273 Schwathof, Österreich`(address)

**Example 42** (doc_id: `deanon_BFG_TRAIN/131368.1`) (sent_id: `deanon_BFG_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Dr. Zlatan Kappelsberger, Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `LeitnerLeitner GmbH Wirtschaftsprüfer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Zlatan Kappelsberger`(person)
- `Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich`(address)

**Example 43** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Intercura Teuhand Revisions  GmbH` — type mismatch — same span as gold: `Intercura Teuhand Revisions  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karen Vennemeyer`(person)
- `Neu-Reinbach 11, 4693 Fallholz, Österreich`(address)
- `Intercura Teuhand Revisions  GmbH`(organisation)

**Example 44** (doc_id: `deanon_BFG_TRAIN/131567.1`) (sent_id: `deanon_BFG_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Severin Wöllecke  in der Finanzstrafsache gegen die  Beschuldigte Nicole Schlemper, Uteweg 12, 9624 Latschach, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Severin Wöllecke`(person)
- `Nicole Schlemper`(person)
- `Uteweg 12, 9624 Latschach, Österreich`(address)

**Example 45** (doc_id: `deanon_BFG_TRAIN/131638.1`) (sent_id: `deanon_BFG_TRAIN/131638.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck in der Beschwerdesache  Priv.-Doz. ÖkR Charles Splittstösser, An der Bundesstraße 10 4, 4364 Kleinmaseldorf, Österreich, vertreten durch LBG Niederösterreich Steuerberatung GmbH, Wie- ner Straße 2, 2640 Gloggnitz, über die Beschwerden vom 29. Dezember 2017 und 31. Jänner  2018 gegen die Bescheide des Finanzamtes Neunkirchen Wiener Neustadt vom 6. Dezember  2017 und 10. Jänner 2018 betreffend Einkommensteuer 2007 bis 2011, St.Nr. 33- 98-658/9399, zu Recht erkannt:    Der Beschwerde gegen den Einkommensteuerbescheid 2007 wird teilweise Folge gegeben.

**False Positives:**

- `LBG Niederösterreich Steuerberatung GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. ÖkR Charles Splittstösser`(person)
- `An der Bundesstraße 10 4, 4364 Kleinmaseldorf, Österreich`(address)
- `98-658/9399`(tax_number)

**Example 46** (doc_id: `deanon_BFG_TRAIN/132000.1`) (sent_id: `deanon_BFG_TRAIN/132000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Hon.-Prof.in Priv.-Doz.in Lukas Voigtlaender  in der Beschwerdesache Liu Stelmaszyk,  Laberlweg 104, 4382 Waldhausen im Strudengau, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und Jugendhilfe,  Karl-Borromäus-Platz 3, 1030 Wien, über die Beschwerde vom 14. August 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 (nunmehr Finanzamtes Österreich ) vom 30. Juli  2020 betreffend Abweisung des Antrages auf Familienbeihilfe für 01/2016 bis 06/2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Magistrat ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Hon.-Prof.in Priv.-Doz.in Lukas Voigtlaender`(person)
- `Liu Stelmaszyk`(person)
- `Laberlweg 104, 4382 Waldhausen im Strudengau, Österreich`(address)

**Example 47** (doc_id: `deanon_BFG_TRAIN/132255.1`) (sent_id: `deanon_BFG_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Chen Helwig  in der Beschwerdesache Roxana Gehrbrandt,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr Christian Leskoschek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Chen Helwig`(person)
- `Roxana Gehrbrandt`(person)

**Example 48** (doc_id: `deanon_BFG_TRAIN/132294.1`) (sent_id: `deanon_BFG_TRAIN/132294.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Frau Balthasar Jamrus, Ameisbühel 21, 8673 Landau, Österreich  damals vertreten durch WT, über die  Beschwerden der Abgabepflichtigen   1. vom 15. Dezember 2014 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf (nunmehr Finanzamt Österreich) vom 22. Oktober 2014 über die  Abweisung ihres Antrages auf Bewilligung von Aussetzungen der Einhebung vom 30. Juli  2014 betreffend die Einkommens- und Umsatzsteuer 2005-2011  2.

**False Positives:**

- `WT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Balthasar Jamrus`(person)
- `Ameisbühel 21, 8673 Landau, Österreich`(address)

**Example 49** (doc_id: `deanon_BFG_TRAIN/132361.1`) (sent_id: `deanon_BFG_TRAIN/132361.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dora Streb, Rosemarie-Preh-Allee 19, 9113 Grutschen, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1/Freyung, 1010  Wien, über die Beschwerde vom 13. Juni 2014 gegen den Bescheid des Finanzamtes Wien 1/23  vom 11. August 2010 betreffend Berichtigung gemäß § 293b BAO des Bescheides vom 1. Juni  2007 betreffend Umsatzsteuer 2005 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Deloitte Tax Wirtschaftsprüfungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dora Streb`(person)
- `Rosemarie-Preh-Allee 19, 9113 Grutschen, Österreich`(address)

**Example 50** (doc_id: `deanon_BFG_TRAIN/132368.1`) (sent_id: `deanon_BFG_TRAIN/132368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Hugo Denhart, Eichhorn 8, 9413 Hinterwölch, Österreich, vertreten durch Dr. Peter Eisele, Öffentlicher Notar, 7540 Güssing, Hauptplatz 1, über  die Beschwerde vom 18. Dezember 2017 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 11. Dezember 2017 betreffend Rechtsgebühr,  Steuernummer 10- 90-207/0668, Erf.Nr. 10- 2017, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hugo Denhart`(person)
- `Eichhorn 8, 9413 Hinterwölch, Österreich`(address)
- `90-207/0668`(tax_number)

**Example 51** (doc_id: `deanon_BFG_TRAIN/132394.1`) (sent_id: `deanon_BFG_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache OStR Georgette Köbele, MA, Gsteig 13, 4722 Ranna, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

**False Positives:**

- `Kleiner Eberl Brandstätter  Steuerberatung GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Georgette Köbele, MA`(person)
- `Gsteig 13, 4722 Ranna, Österreich`(address)

**Example 52** (doc_id: `deanon_BFG_TRAIN/132557.1`) (sent_id: `deanon_BFG_TRAIN/132557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Emilia Nüßgens  in der Beschwerdesache der  Hinklein, Stadlweg 3, 8160 Haselbach bei Weiz, Österreich, vertreten durch Ort, über die Beschwerde vom 6.9.2017 gegen die  Bescheide des Finanzamtes Innsbruck vom 2. August 2017 betreffend Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 und Festsetzung der  Kraftfahrzeugsteuer für die Zeiträume Juli bis Dezember 2014 und Jänner bis Juni 2015 zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 wird abgewiesen.

**False Positives:**

- `Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Emilia Nüßgens`(person)
- `Hinklein`(organisation)
- `Stadlweg 3, 8160 Haselbach bei Weiz, Österreich`(address)

**Example 53** (doc_id: `deanon_BFG_TRAIN/132601.1`) (sent_id: `deanon_BFG_TRAIN/132601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Elena Scheidlin  in der Beschwerdesache Martin Chalupny,  Anton Gotsch-Gasse 26, 8492 Klöchberg, Österreich, vertreten durch StB, über die Beschwerde vom 23. Juli 2018 gegen den  Bescheid des Finanzamtes vom 25. Juni 2018 betreffend Einkommensteuervorauszahlungen  2018 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `StB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Elena Scheidlin`(person)
- `Martin Chalupny`(person)
- `Anton Gotsch-Gasse 26, 8492 Klöchberg, Österreich`(address)

**Example 54** (doc_id: `deanon_BFG_TRAIN/132704.1`) (sent_id: `deanon_BFG_TRAIN/132704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Corinna Bastgen  in der Beschwerdesache Ernestine Josef,  Claretinergasse 28, 8530 Garanas, Österreich, vertreten durch König, Ermacora, Klotz & Partner Rechtsanwälte, Erlerstraße  4/3, 6020 Innsbruck, über die Beschwerde vom 6. Februar 2018 gegen die Bescheide des  Finanzamt Salzburg-Land  vom 23. Jänner 2018 betreffend Einkommensteuer 2014, Einkommensteuer 2015  und Einkommensteuervorauszahlungen 2018 zu Recht erkannt:   I. Der Beschwerde gegen den Einkommensteuerbescheid 2014 wird teilweise Folge  gegeben.

**False Positives:**

- `König` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Corinna Bastgen`(person)
- `Ernestine Josef`(person)
- `Claretinergasse 28, 8530 Garanas, Österreich`(address)
- `Finanzamt Salzburg-Land`(organisation)

**Example 55** (doc_id: `deanon_BFG_TRAIN/132752.1`) (sent_id: `deanon_BFG_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Manuel de Keijzer, Schmieddorf 5, 6215 Achenkirch, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manuel de Keijzer`(person)
- `Schmieddorf 5, 6215 Achenkirch, Österreich`(address)

**Example 56** (doc_id: `deanon_BFG_TRAIN/132770.1`) (sent_id: `deanon_BFG_TRAIN/132770.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache OMedR Edgar Petkof, Gemüseweg 8-19, 2011 Sierndorf, Österreich, vertreten durch DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger Straße 2-4,  1090 Wien, über die Beschwerde vom 11. Mai 2012 gegen den Bescheid des Zollamtes  Feldkirch Wolfurt vom 5. April 2012 betreffend Erstattung/Erlass von Einfuhrabgaben zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `DSC Doralt Seist Csoklich Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Edgar Petkof`(person)
- `Gemüseweg 8-19, 2011 Sierndorf, Österreich`(address)

**Example 57** (doc_id: `deanon_BFG_TRAIN/132794.1`) (sent_id: `deanon_BFG_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Edwin Uebel, Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Dkfm` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Edwin Uebel`(person)
- `Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich`(address)

**Example 58** (doc_id: `deanon_BFG_TRAIN/132870.1`) (sent_id: `deanon_BFG_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Lena Gualtiero  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 33-625/1773, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lena Gualtiero`(person)
- `33-625/1773`(tax_number)

**Example 59** (doc_id: `deanon_BFG_TRAIN/132893.1`) (sent_id: `deanon_BFG_TRAIN/132893.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Ute Höltje, Burghof 44, 5222 Spreitzenberg, Österreich, vertreten durch KAPAS Steuerberatung GmbH, Birkfelder Straße 25, 8160 Weiz, über  die Beschwerde vom 19.12.2019 gegen den Bescheid des Finanzamtes FA vom 13.05.2020  betreffend Feststellung von Einkünften gemäß § 188 BAO 2018 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `KAPAS Steuerberatung GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ute Höltje`(person)
- `Burghof 44, 5222 Spreitzenberg, Österreich`(address)

**Example 60** (doc_id: `deanon_BFG_TRAIN/133151.1`) (sent_id: `deanon_BFG_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Leila Togan  in der   Beschwerdesache Pia Minarsch, Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Leila Togan`(person)
- `Pia Minarsch`(person)
- `Camillo Kronich-Straße 5, 8243 Haideggendorf, Österreich`(address)

**Example 61** (doc_id: `deanon_BFG_TRAIN/133172.1`) (sent_id: `deanon_BFG_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Hon.-Prof.in Lena Ünlüer, Modsiedl 8, 4150 Katzing, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 51-253/7194  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Uniconsult Steuerberatungs GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Lena Ünlüer`(person)
- `Modsiedl 8, 4150 Katzing, Österreich`(address)
- `51-253/7194`(tax_number)

**Example 62** (doc_id: `deanon_BFG_TRAIN/133241.1`) (sent_id: `deanon_BFG_TRAIN/133241.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Kirstin Strohmeier  in der Beschwerdesache Quentin Diller, Bakk. rer. nat. LLM,  Udo Maz-Straße 2, 2122 Ulrichskirchen, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, über die Beschwerde vom 28. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 26. November 2020 betreffend Gebühren 29.04.2014  Steuernummer 50-265/2632  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Deloitte Tax Wirtschaftsprüfungs GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Kirstin Strohmeier`(person)
- `Quentin Diller, Bakk. rer. nat. LLM`(person)
- `Udo Maz-Straße 2, 2122 Ulrichskirchen, Österreich`(address)
- `50-265/2632`(tax_number)

**Example 63** (doc_id: `deanon_BFG_TRAIN/133292.1`) (sent_id: `deanon_BFG_TRAIN/133292.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Gustav Luther  in der Beschwerdesache Richarda Linnenkugel,  Palmsdorf 57, 3972 Seifritz, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, gegen den Bescheid des Finanzamtes Wien 1/23 vom  8. Jänner 2019 betreffend Forschungsprämie § 108c EStG 1988 2015 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Ernst ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof. Gustav Luther`(person)
- `Richarda Linnenkugel`(person)
- `Palmsdorf 57, 3972 Seifritz, Österreich`(address)

**Example 64** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Huberta Schwandt, Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 30-672/6934  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Commendatio Wirtschaftstreuhand GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Huberta Schwandt`(person)
- `Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich`(address)
- `30-672/6934`(tax_number)

**Example 65** (doc_id: `deanon_BFG_TRAIN/133679.1`) (sent_id: `deanon_BFG_TRAIN/133679.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Priv.-Doz.in Edeltraud Turbanski  in der Beschwerdesache Bernarda Metze,  Neubäckweg 48, 2534 Schwechatbach, Österreich, vertreten durch Glocknitzer Hollenthoner Stb.GmbH & Co KG,1050 Wien,  Bräuhausgasse 37/4, 1150 Wien, über die Beschwerde vom 10. April 2012 gegen den Bescheid  des FA Wien 9/18/19 Klosterneuburg vom 14. März 2012 betreffend Festsetzung des  Dienstgeberbeitrages 2006 bis 2009 Steuernummer abc zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben:  I. Die Beschwerde hinsichtlich Dienstgeberbeitrag für die Ärztinnen Dr. U und Dr. S wird  abgewiesen.

**False Positives:**

- `Glocknitzer Hollenthoner Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Priv.-Doz.in Priv.-Doz.in Edeltraud Turbanski`(person)
- `Bernarda Metze`(person)
- `Neubäckweg 48, 2534 Schwechatbach, Österreich`(address)

**Example 66** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwalt Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 67** (doc_id: `deanon_BFG_TRAIN/133873.1`) (sent_id: `deanon_BFG_TRAIN/133873.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die als  Bescheidbeschwerde zu erledigende Berufung vom 21.02.2011 der Xy, Emil Zöchling-Gasse 149, 9063 Rosendorf, Österreich  vertreten durch Dr. Hans Bodendorfer Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010  Wien, gegen den Einkommensteuerbescheid für das Jahr 2005 des Finanzamtes Bruck  Eisenstadt Oberwart vom 29.11.2010, Steuernummer 66-205/7303   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Hans Bodendorfer Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Emil Zöchling-Gasse 149, 9063 Rosendorf, Österreich`(address)
- `Dr. Hans Bodendorfer Steuerberatungsges.m.b.H.`(organisation)
- `66-205/7303`(tax_number)

**Example 68** (doc_id: `deanon_BFG_TRAIN/134032.1`) (sent_id: `deanon_BFG_TRAIN/134032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hubert Eitemüller, Kreuzberglweg 88h, 4920 Litzlham, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder-und  Jugendhilfe, Karl-Borromäus-Platz 3, 1030 Wien, über die Beschwerde vom 24. Juli 2019 gegen  den Bescheid des Finanzamtes Österreich vom 27. Juni 2019 betreffend Abweisung des  Antrages auf Gewährung von Familienbeihilfe für den Zeitraum Jänner 2017 bis Juni 2019 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Magistrat ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hubert Eitemüller`(person)
- `Kreuzberglweg 88h, 4920 Litzlham, Österreich`(address)

**Example 69** (doc_id: `deanon_BFG_TRAIN/134045.1`) (sent_id: `deanon_BFG_TRAIN/134045.1_2`)


Elisabeth in der Beschwerdesache  des Alana Urbanzyk, Schönrain 32u, 3334 Pettendorf, Österreich, vertreten durch Krebs & Rudorfer Wirtschafts- und  Steuerberatungs GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, betreffend die Bescheide des  Finanzamtes Gänserndorf Mistelbach vom 5. Dezember 2014 betreffend Einkommensteuer  2011, Einkommensteuer 2012 und Einkommensteuer 2013 den Beschluss:  Der Vorlageantrag wird als gegenstandslos erklärt.

**False Positives:**

- `Krebs ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alana Urbanzyk`(person)
- `Schönrain 32u, 3334 Pettendorf, Österreich`(address)

**Example 70** (doc_id: `deanon_BFG_TRAIN/134099.1`) (sent_id: `deanon_BFG_TRAIN/134099.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lea Capoluongo  in der Beschwerdesache Rupert Lübbersmeyer,  Peter-Tunner-Straße 84, 3601 Oberloiben, Österreich, vertreten durch Stb Gerhard Obrist, Hans-Schrott-Fiechtl-Straße 30, 6134  Vomp, über die Beschwerde vom 14.1.2011 gegen den Bescheid des FA Kufstein Schwaz  (nunmehr FA Österreich) vom 15.12.2010, StrNr, betreffend 1. Festsetzung der  Normverbrauchsabgabe für den Zeitraum Oktober 2008 und   2.

**False Positives:**

- `Stb Gerhard Obrist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Lea Capoluongo`(person)
- `Rupert Lübbersmeyer`(person)
- `Peter-Tunner-Straße 84, 3601 Oberloiben, Österreich`(address)

**Example 71** (doc_id: `deanon_BFG_TRAIN/134146.1`) (sent_id: `deanon_BFG_TRAIN/134146.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Kerstin Feuerhaak  in der Beschwerdesache Cassandra Mertel,  Pfeifferhofstraße 6, 6335 Vorderthiersee, Österreich, vertreten durch Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Eduard-Wallnöfer-Platz 1, 6460 Imst, über die Beschwerde vom  10. Juni 2013 gegen den Bescheid des FA Landeck Reutte (nunmehr FA Österreich) vom 15. Mai  2013, StrNr, betreffend Festsetzung der Normverbrauchsabgabe für den Zeitraum März 2012  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Kapferer Frei ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Mag.a Kerstin Feuerhaak`(person)
- `Cassandra Mertel`(person)
- `Pfeifferhofstraße 6, 6335 Vorderthiersee, Österreich`(address)

**Example 72** (doc_id: `deanon_BFG_TRAIN/134157.1`) (sent_id: `deanon_BFG_TRAIN/134157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Adriana Guretzky  in der Beschwerdesache der Bf,  vertreten durch StB, über die Beschwerden vom 27. Oktober 2017 gegen die Bescheide des  Finanzamtes vom 25. September 2017 betreffend die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2013 und Körperschaftsteuer 2013 zu Steuernummer  61-332/0449    I. zu Recht erkannt: Der Beschwerde gegen den Bescheid über die Wiederaufnahme des  Verfahrens hinsichtlich Körperschaftsteuer 2013 wird Folge gegeben.

**False Positives:**

- `StB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Adriana Guretzky`(person)
- `61-332/0449`(tax_number)

**Example 73** (doc_id: `deanon_BFG_TRAIN/134193.1`) (sent_id: `deanon_BFG_TRAIN/134193.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Violetta Bornmüller  in der Beschwerdesache HR Florentine Eckmaier,  Gaitenschlag 9, 3282 Mitteröd, Österreich, vertreten durch Dr. Heinz Häupl Rechtsanwalts GmbH, Stockwinkl 18, 4865  Nußdorf am Attersee, über die Beschwerde vom 12. November 2019 gegen den Bescheid des  FA Schwechat Gerasdorf  vom 9. Oktober 2019 betreffend die Festsetzung von ersten Säumniszuschlägen,  Steuernummer 79-881/2529, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr.in Violetta Bornmüller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Violetta Bornmüller`(person)
- `HR Florentine Eckmaier`(person)
- `Gaitenschlag 9, 3282 Mitteröd, Österreich`(address)
- `FA Schwechat Gerasdorf`(organisation)
- `79-881/2529`(tax_number)

**Example 74** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Laurence Mehlstaeubler, Laimerstraße 12, 6973 Höchst, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31.03.2014 gegen die Bescheide des Finanzamtes für Großbetriebe vom  23.01.2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2010 bis 2012  (Steuernummer 18-900/5712 ) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Glatzhofer ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laurence Mehlstaeubler`(person)
- `Laimerstraße 12, 6973 Höchst, Österreich`(address)
- `18-900/5712`(tax_number)

**Example 75** (doc_id: `deanon_BFG_TRAIN/134384.1`) (sent_id: `deanon_BFG_TRAIN/134384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Torsten Jokuschies, Taxerweg 19, 4952 Appersting, Österreich, vertreten durch Gstöttner & Partner  Steuerberatung Gesellschaft m.b.H. & Co. KG, Linzerstraße 10, 4320 Perg, über die Beschwerde  vom 26. Februar 2018 gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom  22. Jänner 2018 betreffend Feststellung der Einkünfte § 188 BAO 2011 Steuernummer  04-517/2751  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gstöttner ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Torsten Jokuschies`(person)
- `Taxerweg 19, 4952 Appersting, Österreich`(address)
- `04-517/2751`(tax_number)

**Example 76** (doc_id: `deanon_BFG_TRAIN/134434.1`) (sent_id: `deanon_BFG_TRAIN/134434.1_2`)


Kff. Eugenia Biegai, Bannberg 49K, 4791 Höcking, Österreich, vertreten durch Hopmeier Wagner Kirnbauer Rechtsanwälte OG,  Rathausstraße 15, 1010 Wien,    1.) über die Beschwerde (ursprünglich: Berufung) vom 15.12.2011 gegen den mit  8. November 2011 datierten und am 17. November 2011 zugestellten Bescheid  (Zurückweisungsbescheid) des Finanzamtes Neunkirchen Wr. Neustadt (belangte  Behörde) zu St.Nr. 33 StNr2, mit welchem die Berufung vom 29.12.2010 gegen den  Festellungsbescheid hinsichtlich X2 GmbH & (atypisch) stille Gesellschafter vom  29.11.2010 gemäß § 273 Abs. 1 BAO aF (alte Fassung vor BGBl. I 14/2013) als nicht  zulässig zurückgewiesen wurde,   2.) über die Beschwerde (ursprünglich: Berufung) vom 11.11.2011 gegen den mit  10. Oktober 2011 datierten und am 13. Oktober 2011 zugestellten Bescheid  (Zurückweisungsbescheid) des Finanzamtes Neunkirchen Wr. Neustadt zu  St.Nr. 33 StNr1, mit welchem die Berufung vom 29.12.2010 (Eingangsstempel  03.JAN.2011) gegen den Festellungsbescheid hinsichtlich X1 GmbH & (atypisch) stille  Gesellschafter vom 29.11.2010 gemäß § 273 Abs. 1 BAO aF als nicht zulässig  zurückgewiesen wurde,  nach Durchführung einer mündlichen Verhandlung am 16. September 2021 in Anwesenheit der  Schriftführerin Sf zu Recht erkannt:  Die Beschwerden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hopmeier Wagner Kirnbauer Rechtsanwälte OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bannberg 49K, 4791 Höcking, Österreich`(address)

**Example 77** (doc_id: `deanon_BFG_TRAIN/134507.1`) (sent_id: `deanon_BFG_TRAIN/134507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Dipl.-Ing. Xaver Kühlwetter, Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich, vertreten durch Dr. Ferdinand Jenni, Jahngasse 18, 6850  Dornbirn, über die Beschwerde vom 10. November 2014 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Oktober 2014 betreffend Einkommensteuer 2013, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Josef Ungericht`(person)
- `Dipl.-Ing. Xaver Kühlwetter`(person)
- `Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich`(address)

**Example 78** (doc_id: `deanon_BFG_TRAIN/134540.1`) (sent_id: `deanon_BFG_TRAIN/134540.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerde-sache DDr. Jasmin Waltram, Bakk. phil.,  Freithöhstraße 30, 5143 Haiderthal, Österreich, vertreten durch Hofer Papistock Wirtschaftstreuhand- Steuerberatung OG,  Norbert-Brüll-Straße 24, 5020 Salzburg, über die Beschwerde vom 15. Februar 2017 gegen die  Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 22. Dezember  2016 betreffend Einkommensteuer 2010 bis Einkommensteuer 2014 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hofer Papistock Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DDr. Jasmin Waltram, Bakk. phil.`(person)
- `Freithöhstraße 30, 5143 Haiderthal, Österreich`(address)

**Example 79** (doc_id: `deanon_BFG_TRAIN/134574.1`) (sent_id: `deanon_BFG_TRAIN/134574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Ing. Miklos Novikova, Carl Lutz-Straße 44, 2225 Blumenthal, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg, über die Beschwerde vom 14. Jänner 2019  gegen den Haftungsbescheid des Finanzamtes Lilienfeld St. Pölten vom 17. Dezember 2018,  Steuernummer 62-482/0330, Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `BKS Steuerberatung GmbH ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Miklos Novikova`(person)
- `Carl Lutz-Straße 44, 2225 Blumenthal, Österreich`(address)
- `62-482/0330`(tax_number)

**Example 80** (doc_id: `deanon_BFG_TRAIN/134630.1`) (sent_id: `deanon_BFG_TRAIN/134630.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ophelia Kirischenko  in der Beschwerdesache Violetta Düerkob,  Lorettogasse 8, 4252 Reitern, Österreich, vertreten durch Eveline Effler, Trappengasse 22, 2601 Eggendorf, über die  Beschwerde vom 22. Juni 2021 gegen den Bescheid des Finanzamtes Österreich vom 27. Mai  2021 betreffend Zwangsstrafen 2021 Steuernummer 31-466/0163  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Eveline Effler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Ophelia Kirischenko`(person)
- `Violetta Düerkob`(person)
- `Lorettogasse 8, 4252 Reitern, Österreich`(address)
- `31-466/0163`(tax_number)

**Example 81** (doc_id: `deanon_BFG_TRAIN/134703.1`) (sent_id: `deanon_BFG_TRAIN/134703.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Irene Hildebrecht  in der Beschwerdesache KommR Dipl.-Ing. ÖkR Valentina Steinbrunn,  Ebrasdorf 161, 4320 Oberwagram, Österreich, vertreten durch Dr. Anke Reisch, Franz-Reisch-Straße 4, 6370 Kitzbühel, über  die Beschwerde vom 28. Juni 2013 gegen die Bescheide des Finanzamtes Kitzbühel Lienz  (nunmehr: Finanzamt Österreich) vom 22. Mai 2013, Str. Nr. 36-608/1721, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Oktober 2010      und Verspätungszuschlag  2.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Irene Hildebrecht`(person)
- `KommR Dipl.-Ing. ÖkR Valentina Steinbrunn`(person)
- `Ebrasdorf 161, 4320 Oberwagram, Österreich`(address)
- `36-608/1721`(tax_number)

**Example 82** (doc_id: `deanon_BFG_TRAIN/134762.1`) (sent_id: `deanon_BFG_TRAIN/134762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Simon Zens  in der Beschwerdesache Miriam Große-Bley,  Tipschern 13, 4052 Fürhappen, Österreich, vertreten durch Herrn Michael Haberl, Steuerberater, Hauptstraße 65, 8962  Gröbming, über die Beschwerde vom 9.7.2018 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 12.6.2018 betreffend Festsetzung des Dienstgeberbeitrages (DB) für die  Jahre 2013, 2014, 2015 und 2016 sowie des Zuschlages zum Dienstgeberbeitrag (DZ) für die  Jahre 2013, 2014, 2015 und 2016 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Herrn Michael Haberl` — partial — gold is substring of pred: `Michael Haberl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Simon Zens`(person)
- `Miriam Große-Bley`(person)
- `Tipschern 13, 4052 Fürhappen, Österreich`(address)
- `Michael Haberl`(person)

**Example 83** (doc_id: `deanon_BFG_TRAIN/134768.1`) (sent_id: `deanon_BFG_TRAIN/134768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache James Johanntokrax, Wandeckstraße 6, 4730 Aschach, Österreich, vertreten durch Mag. Manuela Henrich, Dr. Karl Renner Str. 5, 2560 Berndorf, über die  Beschwerde vom 28.06.2019  gegen den Bescheid des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich) vom 27. Mai 2019 betreffend Wiedereinsetzung in den vorigen Stand  nach Durchführung einer mündlichen Verhandlung betreffend Einkommensteuer für das Jahr  2012 Steuernummer 68-133/5727  zu Recht erkannt:   Die Beschwerde gegen die Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `James Johanntokrax`(person)
- `Wandeckstraße 6, 4730 Aschach, Österreich`(address)
- `68-133/5727`(tax_number)

**Example 84** (doc_id: `deanon_BFG_TRAIN/134896.1`) (sent_id: `deanon_BFG_TRAIN/134896.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Gabriele Griepekoven  in der Beschwerdesache des  Beatrix Adamsen, Sallingerstraße 8, 4611 Buchkirchen, Österreich, vertreten durch Wirtschaftstreuhänder Michael Haberl,  Wirtschaftsprüfer und Steuerberater, Hauptstraße 65, 8962 Gröbming, über die Beschwerde  vom 11.6.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom 4.4.2019  betreffend Normverbrauchsabgabe für 8/2015 sowie Kfz-Steuer für 7-12/2015, 1-12/2016, 1- 12/2017 und 1-12/2018 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Wirtschaftstreuhänder Michael Haberl` — partial — gold is substring of pred: `Michael Haberl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hon.-Prof. Gabriele Griepekoven`(person)
- `Beatrix Adamsen`(person)
- `Sallingerstraße 8, 4611 Buchkirchen, Österreich`(address)
- `Michael Haberl`(person)

**Example 85** (doc_id: `deanon_BFG_TRAIN/134912.1`) (sent_id: `deanon_BFG_TRAIN/134912.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Xaver Markoff, Oberfrauenwies 100, 4362 Würzenberg, Österreich, vertreten durch Wesonig + Partner  Steuerberatung GmbH, Birkfelder Straße 25, 8160 Weiz, über die Beschwerde vom 9. April  2019 gegen den Bescheid des Finanzamtes Wien 1/23 vom 11. März 2019 betreffend  Zurücknahme der Beschwerde vom 31. Dezember 2018, Steuernummer 54-375/0993, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wesonig ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Xaver Markoff`(person)
- `Oberfrauenwies 100, 4362 Würzenberg, Österreich`(address)
- `54-375/0993`(tax_number)

**Example 86** (doc_id: `deanon_BFG_TRAIN/134926.1`) (sent_id: `deanon_BFG_TRAIN/134926.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Mag.a Wilhelmine Brückelmayer  in der Beschwerdesache des  Ruprecht Öhlmayer, Alanovaplatz 48, 4113 Erdmannsdorf, Österreich, vertreten durch Kanzlei Kleiner Eberl Brandstätter Steuerberatung  GmbH, Burgring 22, 8010 Graz, und Zangrando-Jaklitsch Stb GmbH & Co KG, 8720 Knittelfeld,  Gaalerstraße 5 über die Beschwerde vom 24. Juli 2019 gegen den Bescheid des FA Purkersdorf (jetzt  Dienststelle des Finanzamtes Österreich) vom 12. Juli 2019 über die Festsetzung einer  Zwangsstrafe zur Steuernummer 45-112/5628  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kanzlei Kleiner Eberl Brandstätter Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Mag.a Wilhelmine Brückelmayer`(person)
- `Ruprecht Öhlmayer`(person)
- `Alanovaplatz 48, 4113 Erdmannsdorf, Österreich`(address)
- `FA Purkersdorf`(organisation)
- `45-112/5628`(tax_number)

**Example 87** (doc_id: `deanon_BFG_TRAIN/135141.1`) (sent_id: `deanon_BFG_TRAIN/135141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  OMedR Bruno Kibar, Weissach 4, 5071 Walserfeld, Österreich, vertreten durch Dr. Martin Riedl, Franz-Josefs-Kai 5/DG, 1010  Wien, über die Beschwerde vom 3. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 26. August 2019  betreffend Gewährung von Familienbeihilfe ab März 2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Siegfried Fenz`(person)
- `OMedR Bruno Kibar`(person)
- `Weissach 4, 5071 Walserfeld, Österreich`(address)

**Example 88** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen Mag. Willibald Giesser, Eichingerweg 67, 4931 Neulendt, Österreich, vertreten durch HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft, Landstraßer Hauptstraße 27,  1030 Wien, über die Beschwerde des Beschuldigten vom 1. April 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 6,  Abgabenstrafen vom 2. März 2021, Zahl: MA6/206000002559/2020, in Anwesenheit des  Verteidigers und der Behördenvertreterin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der Zurückweisungsbescheid des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `HELLER TAXvisory  GmbH Wirtschafts` — partial — pred is substring of gold: `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Willibald Giesser`(person)
- `Eichingerweg 67, 4931 Neulendt, Österreich`(address)
- `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`(organisation)

**Example 89** (doc_id: `deanon_BFG_TRAIN/135571.1`) (sent_id: `deanon_BFG_TRAIN/135571.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Univ.-Prof. Quentin Gerdener  in der Beschwerdesache Hon.-Prof.in Tatjana Schweneke, MSc,  Moorweg 23, 9300 Hörzendorf, Österreich, vertreten durch Steuerberatung Dr. Alfred Sorger GmbH, Steyrergasse 89,  8010 Graz, über die Beschwerde vom 8.3.2018 gegen die Bescheide des Finanzamtes Graz- Umgebung vom 14.12.2017 betreffend Einkommensteuer und Umsatzsteuer, jeweils für die  Jahre 2007 bis 2012 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Steuerberatung Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Univ.-Prof. Quentin Gerdener`(person)
- `Hon.-Prof.in Tatjana Schweneke, MSc`(person)
- `Moorweg 23, 9300 Hörzendorf, Österreich`(address)

**Example 90** (doc_id: `deanon_BFG_TRAIN/135710.1`) (sent_id: `deanon_BFG_TRAIN/135710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Ramona Cudok  in der Beschwerdesache Maximilian Hagmanns,  Grazer Vorstadt 70, 4650 Hagenberg, Österreich, vertreten durch Dax & Partner Rechtsanwälte GmbH, Wienerstraße 8a, 7400  Oberwart, über die Beschwerde vom 7. November 2017 gegen die Bescheide des Finanzamtes  Oststeiermark vom 10. Oktober 2017 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und Einkommensteuer  (Arbeitnehmerveranlagung) 2016, Steuernummer 45-858/5437,   1. zu Recht erkannt:  Der Beschwerde gegen den Bescheid betreffend Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2016 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dax ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Ramona Cudok`(person)
- `Maximilian Hagmanns`(person)
- `Grazer Vorstadt 70, 4650 Hagenberg, Österreich`(address)
- `45-858/5437`(tax_number)

**Example 91** (doc_id: `deanon_BFG_TRAIN/135734.1`) (sent_id: `deanon_BFG_TRAIN/135734.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Dr. Melinda Thünnissen, Kornriegl 4, 9620 Kraß, Österreich, vertreten durch Villacher Treuhand  Dr. Nehsl & Partner Steuerberatungsges.m.b.H., Nikolaigasse 39, 9500 Villach, vom 23.10.2019  gegen den Bescheid des Bundesministers für Finanzen, GZ. BMF-X1 vom 18.10.2019, zugestellt  am 22.10.2019, mit dem der Antrag vom 26.07.2019 auf Zuerkennung des Zuzugsfreibetrages  gemäß § 103 Absatz 1a EStG 1988 abgewiesen wurde  zu Recht erkannt:  I.  Der Beschwerde wird gemäß § 279 BAO stattgegeben und gemäß § 103 Abs. 1a EStG 1988 in  Verbindung mit § 2 Abs. 2 Ziffer 3 ZBV 2016 der beantragte Zuzugsfreibetrag in Höhe von 30%  der zum Tarif besteuerten Einkünfte in dem Zeitraum von fünf Jahren ab dem Zuzugszeitpunkt  – das ist der 19.02.2019 – zuerkannt.

**False Positives:**

- `Villacher Treuhand  Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Melinda Thünnissen`(person)
- `Kornriegl 4, 9620 Kraß, Österreich`(address)

**Example 92** (doc_id: `deanon_BFG_TRAIN/135883.1`) (sent_id: `deanon_BFG_TRAIN/135883.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Hermann Walraevens, Am Sonnwendstein 8, 2022 Immendorf, Österreich, vertreten durch MOORE STEPHENS City  Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Hafnerplatz 12, 3500  Krems an der Donau, über die Beschwerde vom 23. August 2018 gegen den Bescheid des  Finanzamtes Waldviertel vom 1. August 2018, Steuernummer 14-863/6378, betreffend  Einkommensteuer 2017 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `MOORE STEPHENS City  Treuhand GmbH Wirtschaftsprüfungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Daniel Philip Pfau`(person)
- `Hermann Walraevens`(person)
- `Am Sonnwendstein 8, 2022 Immendorf, Österreich`(address)
- `14-863/6378`(tax_number)

**Example 93** (doc_id: `deanon_BFG_TRAIN/136145.1`) (sent_id: `deanon_BFG_TRAIN/136145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Gernot Sieglen, Oberlederau 7, 4224 Klingenwehr, Österreich  wohnhaft, StNr.: X1, vertreten durch Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010 Wien, betreffend die Berufung vom  25.05.2011 gegen die Einkommensteuerbescheide für die Jahre 2008 und 2009, vom  9.05.2011, zugestellt am 12.05.2011, des Finanzamtes Bruck Eisenstadt Oberwart  zu Recht erkannt

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gernot Sieglen`(person)
- `Oberlederau 7, 4224 Klingenwehr, Österreich`(address)
- `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`(organisation)

**Example 94** (doc_id: `deanon_BFG_TRAIN/136201.1`) (sent_id: `deanon_BFG_TRAIN/136201.1_1`)


IM NAMEN DER REPUBLI K  A.  Erkenntnis  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Karin Iosifescu, Bakk. iur., Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich, vertreten durch BDO Audit Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Am Belvedere 4, 1100 Wien, über die Beschwerde vom 17. Februar  2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom 6. Februar 2017 betreffend  1. Wiederaufnahme des Verfahrens der Vorsteuererstattung für 1-12/2012  2.

**False Positives:**

- `BDO Audit Wirtschaftsprüfungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alois Pichler`(person)
- `Karin Iosifescu, Bakk. iur.`(person)
- `Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich`(address)

**Example 95** (doc_id: `deanon_BFG_TRAIN/136201.1`) (sent_id: `deanon_BFG_TRAIN/136201.1_6`)


B.  Beschluss  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Karin Iosifescu, Bakk. iur., Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich  vertreten durch BDO Audit Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Am Belvedere 4, 1100 Wien, über die Beschwerden vom 17. Februar  2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom 6. Februar 2017 betreffend die  (Sach-) Bescheide im  1. wiederaufgenommenen Verfahren der Vorsteuererstattung für 1-12/2012  2.

**False Positives:**

- `BDO Audit Wirtschaftsprüfungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alois Pichler`(person)
- `Karin Iosifescu, Bakk. iur.`(person)
- `Robert Hohenwarter-Gasse 26, 2572 Steinbachtal, Österreich`(address)

</details>

---

## `Herr_Name_Corrected`

**F1:** 0.012 | **Precision:** 1.000 | **Recall:** 0.006  

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
| 1.000 | 0.006 | 0.012 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 0 | 1315 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Stanislaus Calisir (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Cynthia Neureuter  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Natascha Daschmann (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_8`)


Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der  Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische  Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur  Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit  1 von 20 Seite 2 von 20

| Predicted | Gold |
|---|---|
| `Brunhild Hoffschulz` | `Brunhild Hoffschulz` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/141435.1`) (sent_id: `deanon_BFG_TRAIN/141435.1_4`)


Begründung  Verfahrensgang:  MA67/226701281451/2022:  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner  2023, Zahl: MA67/226701281451/2022, wurde Herr Robert Grentzmann (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von einem 14 Stunden verhängt sowie ein  Verfahrenskostenbeitrag von € 10,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Robert Grentzmann` | `Robert Grentzmann` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/142976.1`) (sent_id: `deanon_BFG_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Nikolaus Thulke (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Nikolaus Thulke` | `Nikolaus Thulke` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_6`)


Entscheidungsgründe  Mit Straferkenntnis vom 16. April 2024, Zahl: MA67/246700162299/2024, hat der Magistrat  der Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Leonhard Facci (in weiterer  Folge: Beschwerdeführer – Bf) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt  indem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen I-57 VS  am  2. Februar 2024 um 09:20 Uhr in einer gebührenpflichtigen Kurzparkzone in 1210 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `I-57 VS` (vehicle_license)

**Example 7** (doc_id: `deanon_BFG_TRAIN/146476.1`) (sent_id: `deanon_BFG_TRAIN/146476.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Herr MedR Florentine Wägemann (in der Folge kurz: Bf.) brachte am 19.2.2024 den Antrag auf  Arbeitnehmerveranlagung für das Jahr 2023 per Finanzonline ein.

| Predicted | Gold |
|---|---|
| `MedR Florentine Wägemann` | `MedR Florentine Wägemann` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/147143.1`) (sent_id: `deanon_BFG_TRAIN/147143.1_5`)


Im Zuge einer Anhaltung durch die Finanzpolizei am 10.7.2015, 22:55 Uhr, in A-Ort1,XStr, hat  der Lenker des Fahrzeuges VW Touareg mit dem ausländischen Kennzeichen XX1, FIN Nr123,  Herr Kirstin Lünebach (= Beschwerdeführer, Bf) angegeben, dass Zulassungsbesitzerin des Fahrzeuges  die Fa. A-GmbH in D-Ort2 ist und er sich auf der Fahrt nach Hause befindet.

| Predicted | Gold |
|---|---|
| `Kirstin Lünebach` | `Kirstin Lünebach` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Einkommensteuerbescheid (Arbeitnehmerveranlagung) vom 1. März 2024 wurde die  Einkommensteuer von Herrn Bernhard Siegmundt (im Folgenden auch Beschwerdeführer oder Bf.) für das  Jahr 2023 mit einer Gutschrift in Höhe von EUR 29,- festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

</details>

---

## `Name_Herrn`

**F1:** 0.010 | **Precision:** 0.060 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `94942c84`  
**Description:**
Captures full names following 'Herrn' (accusative/dative), ensuring the full name including suffixes is extracted.

**Content:**
```
(?:Herrn|Herr)\s+([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=\s+(?:in|von|der|des|\(|$|\d{4}|\s+\d|Gattin|und))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.060 | 0.005 | 0.010 | 150 | 9 | 141 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 141 | 1627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Stanislaus Calisir (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Cynthia Neureuter  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Natascha Daschmann (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/138498.1`) (sent_id: `deanon_BFG_TRAIN/138498.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Im Rahmen der am 17.02.2020 eingereichten Erklärung zur Arbeitnehmerveranlagung 2019  wurde durch Herrn Zacharias Arhelger, BA (in der Folge „Bf“ oder „Beschwerdeführer“) die Gewährung des  (ganzen) Familienbonus Plus für 12 Monate beantragt.

| Predicted | Gold |
|---|---|
| `Zacharias Arhelger, BA` | `Zacharias Arhelger, BA` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_8`)


Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der  Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische  Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur  Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit  1 von 20 Seite 2 von 20

| Predicted | Gold |
|---|---|
| `Brunhild Hoffschulz` | `Brunhild Hoffschulz` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/141435.1`) (sent_id: `deanon_BFG_TRAIN/141435.1_4`)


Begründung  Verfahrensgang:  MA67/226701281451/2022:  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner  2023, Zahl: MA67/226701281451/2022, wurde Herr Robert Grentzmann (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von einem 14 Stunden verhängt sowie ein  Verfahrenskostenbeitrag von € 10,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Robert Grentzmann` | `Robert Grentzmann` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/142976.1`) (sent_id: `deanon_BFG_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Nikolaus Thulke (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Nikolaus Thulke` | `Nikolaus Thulke` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_6`)


Entscheidungsgründe  Mit Straferkenntnis vom 16. April 2024, Zahl: MA67/246700162299/2024, hat der Magistrat  der Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Leonhard Facci (in weiterer  Folge: Beschwerdeführer – Bf) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt  indem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen I-57 VS  am  2. Februar 2024 um 09:20 Uhr in einer gebührenpflichtigen Kurzparkzone in 1210 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `I-57 VS` (vehicle_license)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_5`)


III. Gemäß § 185 Abs.1 lit. a und b FinStrG hat Herrn J. die Kosten des verwaltungsbehördlichen und verwaltungsgerichtlichen Finanzstrafverfahrens in unveränderter Höhe von € 500,00 zu tragen.

**False Positives:**

- `J. die Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_9`)


Entscheidungsgründe Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg vom 8. Juni 2016, SpS 16, wurde Herr J. (in weiterer Folge: Beschuldigter), geb., österreichischer Staatsbürger, Geschäftsführer, aufhältig in Dohnalstraße 26, 8294 Steinbüchl, Österreich, in Abwesenheit schuldig erkannt, er habe im Bereich des Finanzamtes Wien 1/23 als für die Wahrnehmung der abgabenrechtlichen Obliegenheiten der A-GmbH vorsätzlich a) durch die verspätete Abgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2013, sohin unter Verletzung der abgabenrechtlichen Anzeige- ‚ Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2013 in Höhe von € 2.403,50 zu verkürzen versucht, b) durch die Nichtabgabe einer Abgabenerklärung zur Umsatzsteuer für das Kalenderjahr 2014, sohin unter Verletzung der abgabenrechtlichen Offenlegungs- und Wahrheitspflicht, bescheidmäßig festzusetzende Umsatzsteuer 2014 in Höhe von € 11.919,91 zu verkürzen versucht, c) unter Verletzung der Verpflichtung zur Abgabe von dem § 21 UStG entsprechenden Voranmeldungen Verkürzungen von Vorauszahlungen an Umsatzsteuer für 02/2015 in Höhe von € 520,51, 04 – 05 /2015 in Höhe von € 3.814,30 bewirkt, wobei er den Eintritt der Verkürzungen nicht nur für möglich, sondern für gewiss gehalten habe, d) lohnabhängige Abgaben, nämlich Lohnsteuer für 08/2015 in Höhe von € 14.602,93 und Dienstgeberbeiträge zum Ausgleichsfonds für Familienbeihilfen (Anmerkung: € 1.705,49) samt Zuschlägen zu den Dienstgeberbeiträgen für 08/2015 (Anmerkung: € 151,60) in Höhe von € 1.857,09 nicht spätestens am 5.

**False Positives:**

- `J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dohnalstraße 26, 8294 Steinbüchl, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_73`)


Dazu können die Herrn Mag. Y. und der Steuerberater, die in der Zeit vor Konkurseröffnung mit der Finanz Gespräche zur Verhinderung geführt haben, als Zeugen berichten.

**False Positives:**

- `Mag. Y.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/128762.1`) (sent_id: `deanon_BFG_TRAIN/128762.1_11`)


(Vertragsabwicklung) ist festgehalten, dass die Käufer Herrn RA mit der  Errichtung, treuhändigen Abwicklung und grundbücherlichen Durchführung dieses Vertrages  beauftragen.

**False Positives:**

- `RA mit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_25`)


Laut eigenen Aussagen ist Herr AB ein begeisterter Motorradfahrer und  nützt jede Gelegenheit, diesem Hobby nachzugehen.

**False Positives:**

- `AB ein begeisterter Motorradfahrer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_25`)


Die Bf. nannte der AP als Ansprechperson bei der M-GmbH einen Herr K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion und war weder bei der M-GmbH noch deren  Vorgängerin, der P-GmbH angestellt.

**False Positives:**

- `K.. Dieser hatte, wie  erhoben worden war, keine offizielle Funktion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_45`)


Es lasse  sich nicht ableiten, wie Herr K. in den Genuss der „Vorteilszuwendung“ gekommen sei, da die  Rechnung durch die M-GmbH ausgestellt und der Betrag an diese überwiesen worden sei.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_71`)


Herr K. war weder im Jahr 2007, vor dem  Gesellschafterwechsel, noch im Jahr 2008 beim genannten Unternehmen angestellt oder  4 von 6 Seite 5 von 6

**False Positives:**

- `K. war weder im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/130697.1`) (sent_id: `deanon_BFG_TRAIN/130697.1_75`)


In der Verhandlung vor dem BFG wurde nach dem überwiegend wiederholenden Vorbringen  des Bf., Herr Z, Kontrollorgan der MA 67 der Landespolizeidirektion Wien, als Zeuge und zwar  zu folgendem Beweisthema vernommen:   Abstellen des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen Vienna am 12.  Dezember 2019 um 14:52 Uhr in der gebührenpflichtigen Kurzparkzone in 1110 Wien,  Simmeringer Hauptstraße 59 - 61.

**False Positives:**

- `Z, Kontrollorgan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_117`)


Herr C ist 1985  nach Österreich zurückgekehrt, Frau Bf hat ihren deutschen Hauptwohnsitz hingegen  beibehalten.

**False Positives:**

- `C ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_130`)


Die Befragung durch die FinPol und auch die Kontakte mit dem für Strafverfügungen  zuständigen Referenten bei der BH xxx, Herrn G, hat sie als sehr belastend empfunden, weshalb  es zu inhaltlich unrichtigen Protokoll-Textierungen gekommen ist.

**False Positives:**

- `G, hat sie als sehr belastend empfunden, weshalb  es zu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_6`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 20. Februar 2019,  Strafnummer 007, wurde Herr Ronald Kleile, Bakk. rer. nat., geb. 1989, Geschäftsführer, wohnhaft in Fischteichweg 49, 4924 Hartlberg, Österreich  in Abwesenheit schuldig erkannt,   „A.) er hat in Wien vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von  1 von 18 Seite 2 von 18

**False Positives:**

- `Ronald Kleile, Bakk. rer. nat., geb.` — partial — gold is substring of pred: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_152`)


In den  Mietverträgen aller vier im Jahr 2017 von der H- GmbH betriebenen Geschäftslokale scheint  nicht die Gesellschaft, sondern Hr. S. als Mieter auf, obwohl die GmbH bereits existierte und  Herr S. im Zeitpunkt der Vertragsabschlüsse seine Tätigkeit im Textilhandel durch Zurücklegung  der Gewerbeberechtigung bereits beendet hatte.

**False Positives:**

- `S. im Zeitpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_158`)


Herr S. leistet seit 2015 weder USt-Vorauszahlungen noch reicht  er UVAs und Jahreserklärungen ein.

**False Positives:**

- `S. leistet seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_161`)


Zwischen Herrn Ronald Kleile, Bakk. rer. nat., Alleingesellschafter und einziger Geschäftsführer der H- GmbH und  Herrn S., seinem Vater, bestand und besteht nicht nur eine persönliche, sondern auch eine  wirtschaftliche Nahebeziehung.

**False Positives:**

- `Ronald Kleile, Bakk. rer. nat., Alleingesellschafter` — partial — gold is substring of pred: `Ronald Kleile, Bakk. rer. nat.`
- `S., seinem Vater, bestand` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 15** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_174`)


Gemäß § 12 Abs. 14 UStG werden daher folgende Vorsteuern nicht zum Abzug zugelassen:   2017: 24.338,38  2018: 2.557,16  Darüber hinaus ist das behauptete Mietverhältnis zwischen Herrn S. und der H- GmbH, deren  Alleingesellschafter und -geschäftsführer der Beschuldigte ist, auch unter dem Gesichtspunkt,  dass es sich um vertragliche Beziehungen zwischen nahen Angehörigen handelt, zu prüfen.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_19`)


2 Erbrachte Leistungen  J.N.  Da jedoch, wie oben erwähnt, die Leistungen von Herrn J.N. erbracht wurden, ist der bezahlte  Bruttoaufwand i.H.v. 20.000,-- als Betriebsausgabe zu berücksichtigen.

**False Positives:**

- `J.N. erbracht wurden, ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_42`)


Aufgrund von Erhebungen konnte festgestellt werden, dass durch Herrn J.N. von X beauftragte  Leistungen, wie Malerarbeiten und Räumungen erbracht wurden.

**False Positives:**

- `J.N.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_10`)


In der angeführten Bestätigung des Arbeitgebers des Bf. (X) vom 19.10.2015 wird wie folgt  ausgeführt:  "Wir bestätigen, dass Herr Bf. , wohnhaft in AdrBf  von 11.3.2013 bis 30.9.2015 in unserem Unternehmen im Bereich Energieberatung tätig war.

**False Positives:**

- `Bf. , wohnhaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_21`)


Das Schreiben des Dienstgebers des Bf. vom 9.2.2016 lautete wie folgt:  „Ergänzend zu unserem Schreiben von 1.12.2015 können wir bestätigen, dass der maßgebliche  Bestandteil der Tätigkeit von Herrn Bf. die Abwicklung von Geschäftsabschlüssen ist.

**False Positives:**

- `Bf. die Abwicklung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_22`)


Herr Bf. unterliegt einer Zielvereinbarung, welche im Wesentlichen auf die Abwicklung von  Geschäftsabschlüssen basiert.“

**False Positives:**

- `Bf. unterliegt einer Zielvereinbarung, welche im Wesentlichen auf die Abwicklung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_75`)


Als Beispiel ist das bereits zweimal  stattgefundene Verkaufstraining mit Herrn Hubert Mann zu nennen (siehe Beilagen).

**False Positives:**

- `Hubert Mann zu nennen` — partial — gold is substring of pred: `Hubert Mann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hubert Mann`(person)

**Example 22** (doc_id: `deanon_BFG_TRAIN/132647.1`) (sent_id: `deanon_BFG_TRAIN/132647.1_17`)


1) Höhe der 2014 in Österreich Steuerpflichtigen Bezüge aus nicht selbständiger Arbeit   Herr Bf. erzielte auch in 2014 Einkünfte aus nichtselbständiger Arbeit als angestellter  Staatsanwalt aus Dienstverhältnissen zu zwei Schweizer Körperschaften öffentlichen Rechtes  (Kanton Nidwalden und Bund).

**False Positives:**

- `Bf. erzielte auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/132870.1`) (sent_id: `deanon_BFG_TRAIN/132870.1_16`)


Im Zeitraum September 2008 bis Jänner 2009 habe der Gesellschafter  Herr EK insgesamt € 205.000,- in vier Teilbeträgen auf das Konto der Bf einbezahlt, da die  Gesellschaft nicht über die entsprechenden Mittel verfügt hätte, den Umbau zu finanzieren.

**False Positives:**

- `EK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/132996.1`) (sent_id: `deanon_BFG_TRAIN/132996.1_21`)


In diesem Antrag führte der Bf. aus, dass er in den Zeiträumen 2009 bis 2012 durch den WTH  Herrn M steuerlich vertreten gewesen sei, der gemäß Auftrag die monatliche Buchhaltung, den  Jahresabschluss und die Steuerklärungen erstellen sollte.

**False Positives:**

- `M steuerlich vertreten gewesen sei,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_35`)


Herr A und Herr B fungierten im Beschwerdezeitraum weiters als deren handelsrechtliche  Geschäftsführer.

**False Positives:**

- `A und Herr B fungierten im Beschwerdezeitraum weiters als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_43`)


Herr C schied in der Folge per xx.2012 als unbeschränkt haftender  Gesellschafter aus, welche Funktion er jedoch per xx.2016 wieder aufnahm.

**False Positives:**

- `C schied` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_88`)


Wie Herr B im Zuge der mündlichen Verhandlung vom 06.07.2021  (ho Verfahren zu RV/4100093/2018 und RV/4100775/2018) dazu anmerkte, habe er bei seiner  Tätigkeit iZm der Managementvereinbarung einzig den „Konzern Hut“ getragen.

**False Positives:**

- `B im Zuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_95`)


Die festgestellte Leistungserbringung geht aus den Ausführungen des Herr B hervor, der auf  Frage des Gerichtes in der bezeichneten Verhandlung in den Parallelverfahren glaubwürdig  und nachvollziehbar den Arbeitsablauf und die Aufteilung darlegte.

**False Positives:**

- `B hervor,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/134329.1`) (sent_id: `deanon_BFG_TRAIN/134329.1_104`)


All diese Prämissen vorausgeschickt, bestand aufgrund des durchgeführten  Beweisverfahrens keinerlei Veranlassung, an den diesbezüglichen Ausführungen der Bf. zu  zweifeln: Herr B schilderte sein enormes Arbeitspensum vor der Umstrukturierungsphase in  einen Konzern (vgl. dazu VH Protokoll vom 06.07.2021 zu RV/4100093/2018 und  RV/4100775/2018, S. 5, wonach er wörtlich „herumgeflogen [sei], wie ein Depperter“).

**False Positives:**

- `B schilderte sein enormes Arbeitspensum vor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_TRAIN/134380.1`) (sent_id: `deanon_BFG_TRAIN/134380.1_27`)


Im Vorlagebericht fasste das Finanzamt den Sachverhalt wie folgt zusammen:  "Herr NN, welcher steuerlich nicht vertreten ist, war im Jahr 2012 zu 33,33 % an der XXX OG (FA  12 - NUMMER) beteiligt und erzielte in diesem Jahr Einkünfte aus Gewerbebetrieb iHv €  14.523,77.

**False Positives:**

- `NN, welcher steuerlich nicht vertreten ist, war im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_TRAIN/134380.1`) (sent_id: `deanon_BFG_TRAIN/134380.1_28`)


Durch eine Aktualisierung der in der EDV-Anlage der Finanzverwaltung betreffend  Herrn NN gespeicherten Daten wurden vier Lohnzettel, welche bis dahin noch nicht erfasst  wurden, nachträglich automatisch dem Steuerakt Herrn NNs zugeordnet und anlässlich der  2 von 6 Seite 3 von 6

**False Positives:**

- `NNs zugeordnet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_TRAIN/134380.1`) (sent_id: `deanon_BFG_TRAIN/134380.1_33`)


Das Finanzamt hat Herrn NN mehrfach (erfolglos) darauf hingewiesen, dass Einwendungen  gegen im Grundlagenbescheid getroffene Feststellungen nur im Verfahren betreffend den  Grundlagenbescheid vorgebracht werden können.

**False Positives:**

- `NN mehrfach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_TRAIN/134402.1`) (sent_id: `deanon_BFG_TRAIN/134402.1_189`)


Seit 6.8.2014 ist auch Herr DI (FH) FG3 Geschäftsführer.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_TRAIN/134574.1`) (sent_id: `deanon_BFG_TRAIN/134574.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 4. September 2018 forderte das Finanzamt Herrn Ing. Miklos Novikova  (Beschwerdeführer) auf, einen Beweis zu erbringen, dass im haftungsgegenständlichen  Zeitraum alle Gläubiger der Primärschuldnerin GmbH (Primärschuldnerin) gleichmäßig  befriedigt worden seien (Gläubigergleichbehandlung).

**False Positives:**

- `Ing. Miklos Novikova ` — partial — gold is substring of pred: `Ing. Miklos Novikova`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Miklos Novikova`(person)

**Example 35** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_8`)


Frau Frau erhob gegen die zwei Strafverfügungen 1) und 2) bei der MA 67 am 08.05.2021  Einspruch und brachte vor „Hiermit geben wir bekannt, dass Herr Cynthia Neureuter  nicht Halter des  Fahrzeugs mit dem Kennzeichen 123 ist“.

**False Positives:**

- `Cynthia Neureuter  nicht Halter` — partial — gold is substring of pred: `Cynthia Neureuter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cynthia Neureuter`(person)

**Example 36** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_39`)


erschienen, dabei habe er mit Herrn Herr gesprochen und ihm den Zahlschein vorgelegt.

**False Positives:**

- `Herr gesprochen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_76`)


2. Die Bf, deutsche Staatsbürgerin, war seit 3.5.2006 mit Hauptwohnsitz in A-Ort2,  Unterkunftgeber Herr B, gemeldet (siehe ZMR-Abfragen;

**False Positives:**

- `B, gemeldet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_75`)


Erst vor ca 3 Jahren besuchte Frau Reinhold Moellenkamp  Herrn A. erstmals in Ort1  (Ö).

**False Positives:**

- `A. erstmals` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Reinhold Moellenkamp`(person)

**Example 39** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_85`)


Entweder schläft Frau  Reinhold Moellenkamp  bei Herrn A., oder Herr A. bei Frau Reinhold Moellenkamp  in der Schweiz.

**False Positives:**

- `A., oder Herr A. bei Frau Reinhold Moellenkamp ` — similar text (different position): `Reinhold Moellenkamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Reinhold Moellenkamp`(person)
- `Reinhold Moellenkamp`(person)

**Example 40** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_87`)


Als die Beziehung ein Level erreicht hat, bei dem es um die Planung einer gemeinsamen  Zukunft ging, haben Frau Reinhold Moellenkamp  und Herr A. beschlossen, einen Immobilienmakler zu  beauftragen um ein Haus in der Schweiz zu suchen, in das sie gemeinsam einziehen und einen  gemeinsamen Wohnsitz gründen wollten.

**False Positives:**

- `A. beschlossen, einen Immobilienmakler zu  beauftragen um ein Haus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Reinhold Moellenkamp`(person)

**Example 41** (doc_id: `deanon_BFG_TRAIN/135755.1`) (sent_id: `deanon_BFG_TRAIN/135755.1_43`)


Am 26.06.2007  übermittelte Herr WL der OG ein Kündigungsschreiben betreffend sein Ausscheiden aus der  OG zum 31.12.2007.

**False Positives:**

- `WL` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_TRAIN/135755.1`) (sent_id: `deanon_BFG_TRAIN/135755.1_44`)


Als Ausscheidungszeitpunkt (Stichtag auch für Abrechnungen) für das  Ausscheiden von Herrn WL aus der OG wurde zwischen den Gesellschaftern in weiterer Folge  der 29.02.2008 festgelegt.

**False Positives:**

- `WL aus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_TRAIN/135755.1`) (sent_id: `deanon_BFG_TRAIN/135755.1_70`)


Der Gewinn gemäß § 4 Abs 3 EStG 1988 und der ermittelte Übergangsgewinn wurden vom BF  mit Hinweis auf eine getroffene Vereinbarung anteilig auf Herrn WL und ihn selbst verteilt.

**False Positives:**

- `WL` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_61`)


Auch sei in dem dem Bescheid zugrunde liegenden Ermittlungsverfahren das Parteiengehör  nicht gewahrt worden, zumal der Bf. bzw. dessen Vertreterin nicht über sämtliche Ergebnisse,  insbesondere die in der Bescheidbegründung angesprochenen Ergebnisse der GPLA-Prüfung,  insbesondere über den Inhalt der Lohnkonten sowie der Arbeitsaufzeichnungen, der  Hausdurchsuchung am 23.08.2012 und den Inhalt der Vernehmung eines Herrn AB informiert  wurde, sodass diesen nicht die Möglichkeit einer entsprechenden Stellungnahme eingeräumt  worden sei.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_126`)


Laut Aussagen von Herrn AB und Herrn CD wurde mit jedem Dienstnehmer ein  Nettostundenlohn vereinbart und wurden die Mehrstunden laut Auszahlungslisten monatlich  in bar ausbezahlt.

**False Positives:**

- `AB` — no gold match — likely missing annotation
- `CD wurde mit jedem Dienstnehmer ein  Nettostundenlohn vereinbart` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 46** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_221`)


Antwort: Wie bereits ausgeführt, war dafür überwiegend Hr. AB zuständig, teilweise auch über  Anweisung des AB mein Bruder I L.  Frage: Welche Tätigkeit übt Herr I L in den Firmen A. GmbH, D-Stahl und Rohrleitungsbau  sowie in der Fa. c Stahl u. Anlagenbau aus?

**False Positives:**

- `I L` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_258`)


Meine Ermittlungen haben ergeben, dass Herr AB der Machthaber dieser drei Firmen (A.  GmbH, D Elektrotechnik GmbH, c Anlagenbau) war.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_271`)


Herr AB, Hr. CD und auch I L haben diese monatlichen Barauszahlungen getätigt.

**False Positives:**

- `AB, Hr. CD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_368`)


Die Fahndungsprüferin sagte dazu im Zuge der Zeugeneinvernahme aus, dass Herr AB der  Machthaber dieser drei Firmen (A. GmbH, D Elektrotechnik GmbH, c Anlagenbau) war.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_381`)


Herr AB, Hr. CD und auch I L haben diese monatlichen Barauszahlungen getätigt.

**False Positives:**

- `AB, Hr. CD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_383`)


Auch den Aussagen von Herrn AB (vom 16. Oktober 2012), Herrn CD (vom 7. April 2014) und J L  (vom 29.08.2012) ist zu entnehmen, dass mit jedem Dienstnehmer ein Nettostundenlohn  vereinbart und die Mehrstunden laut Auszahlungslisten monatlich in bar ausbezahlt wurden.

**False Positives:**

- `AB` — no gold match — likely missing annotation
- `CD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 52** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_397`)


Nach Ansicht des BFG stehen der Behauptung des anwaltlichen Vertreters auch die Aussagen  von Herrn AB (NS vom 16. Oktober 2012), Herrn CD (NS vom 7.  April 2014) und J L entgegen,  die ausgesagt haben, dass die Mehrstunden laut Auszahlungslisten monatlich in bar an die  Dienstnehmer ausbezahlt wurden.

**False Positives:**

- `AB` — no gold match — likely missing annotation
- `CD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 53** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_430`)


Abschließend ist noch festzuhalten, dass die Einvernahme des Herrn AB aus Sicht des BFG nicht  erforderlich ist, da dieser bereits am 16. Oktober 2012 als Beschuldigter einvernommen  worden ist.

**False Positives:**

- `AB aus Sicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_TRAIN/136573.1`) (sent_id: `deanon_BFG_TRAIN/136573.1_133`)


Mehrere Teilnehmer waren in der Unternehmensführung, Management, Projektleiter oder als  Führungskräfte tätig wie zB Frau Wilhelmine G, Vorstand ÖBB Personenverkehr AG, Herrn Ing.  HH (selbständiger Unternehmer) etc.

**False Positives:**

- `Ing.  HH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_TRAIN/136622.1`) (sent_id: `deanon_BFG_TRAIN/136622.1_28`)


…  Herr KR V ist aufgrund des Vertrages kein zivil- bzw. wirtschaftlicher Eigentümer der  übergebenen Liegenschaften.

**False Positives:**

- `KR V ist aufgrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_TRAIN/136679.1`) (sent_id: `deanon_BFG_TRAIN/136679.1_28`)


Beide würden mit  ihm in einem Haus leben und könnten bezeugen, dass Herr T. in seinem Urlaub einige Tage bei  ihm gewohnt habe und dass er mit seinem Auto nach Wien gefahren sei.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_TRAIN/136679.1`) (sent_id: `deanon_BFG_TRAIN/136679.1_65`)


Die willkürliche Annahme der  Behörde, dass Herr T. nicht der Lenker gewesen sei, entbehre jeglicher Grundlage.

**False Positives:**

- `T. nicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_TRAIN/136679.1`) (sent_id: `deanon_BFG_TRAIN/136679.1_151`)


Die willkürliche Annahme der Behörde, dass Herr T. nicht der Lenker gewesen sei,  entbehre jeglicher Grundlage.

**False Positives:**

- `T. nicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_11`)


Dabei  wurde die verdeckte Ausschüttung an Herrn F im Jahr 2009 vermindert.“

**False Positives:**

- `F im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_23`)


Gesellschafter der BF GmbH sind Herr C D und die Verlassenschaft nach E F. Geschäftsführer  waren Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `C D` — no gold match — likely missing annotation
- `C D` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 61** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_37`)


An Herrn D bzw. F wurden im Jahr 2009  zum Großteil und im Jahr 2010 für einen Monat Mieten verrechnet.

**False Positives:**

- `D bzw. F wurden im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_56`)


…  ad 5) Verdeckte Ausschüttung:  Stellungnahme Dr. K:  Der Geschäftsführer gibt bekannt, dass die Miet- bzw. Kostenbeiträge von Herrn D und Herr F  im Jahr 2009 und 2010 ausschließlich deswegen erfolgte, da Investitionen vorgenommen  wurden (wie aus dem AVZ 2009 und 2010 zu ersehen ist).

**False Positives:**

- `D und Herr F  im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_60`)


Weiters ist festzuhalten, dass Herr D ab Juni  2010 auch formal die handelsrechtliche Geschäftsführerstellung übernommen hat.

**False Positives:**

- `D ab Juni ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_105`)


Sachverhalt   Gesellschafter der BF waren in den beschwerdegegenständlichen Jahren Herr C D und E F.  Geschäftsführer waren Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `C D` — no gold match — likely missing annotation
- `C D` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 65** (doc_id: `deanon_BFG_TRAIN/137100.1`) (sent_id: `deanon_BFG_TRAIN/137100.1_113`)


An Herrn D bzw. F  wurden im Jahr 2009 zum Großteil und im Jahr 2010 für einen Monat Mieten verrechnet.

**False Positives:**

- `D bzw. F  wurden im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_TRAIN/138967.1`) (sent_id: `deanon_BFG_TRAIN/138967.1_159`)


Das könnten neben Herrn D noch weitere Mitarbeiter des Konzerns  (konkret Herr S. und Frau M) bezeugen.

**False Positives:**

- `D noch weitere Mitarbeiter` — no gold match — likely missing annotation
- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 67** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_68`)


Mit Datum 06.02.2015 findet sich ein  Aktenvermerk des Finanzamtes, wonach auf telefonische Anfrage bei der „H-GmbH“ vom  Geschäftsführer, Herrn MagK, angegeben wurde, der Bf sei ganz kurz im Betrieb beschäftigt  gewesen.

**False Positives:**

- `MagK, angegeben wurde,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_82`)


Des Weiteren  habe der Vermieter des Bf, Herr E, angegeben, dass der Bf seit 06.04.2013 sein Mieter sei und  seitdem auch das gegenständliche Fahrzeug verwende, für welches es auch einen Abstellplatz  gebe.

**False Positives:**

- `E, angegeben, dass` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_87`)


Die  Eidesstattliche Erklärung des Vaters werde als eine Gefälligkeitshandlung angesehen, da durch  die erhobenen Übertretungen nach dem Tiroler Parkabgabegesetz 2006 und die Aussagen des  Herrn E und Herrn MagK die Behauptung, der Bf habe das gegenständliche Kraftfahrzeug vor  Juni 2014 nie nach Österreich verbracht, widerlegt worden wäre und in völligem Widerspruch  zur Eidesstattlichen Erklärung stehen würden.

**False Positives:**

- `E und Herrn MagK die Behauptung,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_266`)


10. Die Aussage des Geschäftsführers der „H-GmbH“, Herrn MagK, (siehe lt. Aktenvermerk vom  06.02.2015) vermittelt dem BFG mangels konkret angeführter Zeitangaben nur darüber  Kenntnis, dass der Bf zwischen dem 15.04.2014 (Beendigung des Dienstverhältnisses des Bf)  und dem 06.02.2015 (Datum des Aktenvermerkes) die Betriebsstätte seines ehemaligen  Arbeitgebers noch einmal mit Auto (ohne konkrete Angabe der Marke, Farbe etc.) aufgesucht  hat.

**False Positives:**

- `MagK,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_TRAIN/140303.1`) (sent_id: `deanon_BFG_TRAIN/140303.1_63`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Auf Basis des oben geschilderten Verwaltungsgeschehens und der aktenkundigen Unterlagen  wird folgender entscheidungswesentlicher Sachverhalt festgestellt:  Gesellschafter der BF sind Frau MR mit einer Stammeinlage von € 35.700,00 und Herr MF mit  einer Stammeinlage von € 300,00.

**False Positives:**

- `MF mit  einer Stammeinlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_TRAIN/140303.1`) (sent_id: `deanon_BFG_TRAIN/140303.1_129`)


Die Feststellungen betreffend die Anteilsinhaberschaft von Frau MR und Herrn MF sowie der  Geschäftsführertätigkeit von Frau MR ergeben sich aus dem Firmenbuchauszug.

**False Positives:**

- `MF sowie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_TRAIN/140333.1`) (sent_id: `deanon_BFG_TRAIN/140333.1_54`)


In seiner Beschwerde führte der Bf. durch seine steuerliche Vertreterin Folgendes aus:  „Laut Bescheid solle Herr Bf. zu einer Haftung in Höhe von € 227.308,96 herangezogen werden.

**False Positives:**

- `Bf. zu einer Haftung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_TRAIN/140850.1`) (sent_id: `deanon_BFG_TRAIN/140850.1_83`)


Denn gegen den Einkommensteuerbescheid 2018 von Herrn M N sei am  7. Dezember 2020 Beschwerde erhoben worden und werde beim BFG unter der GZ.  RV/5101415/2020 geführt.

**False Positives:**

- `M N sei am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_TRAIN/140850.1`) (sent_id: `deanon_BFG_TRAIN/140850.1_169`)


Auch wenn gegenständlich nur Herr M N von der Feststellung  betroffen ist, so ändert dies nichts daran, dass Feststellungsbescheide grundsätzlich VOR den  davon abgeleiteten Einkommensteuerbescheiden zu erlassen sind.

**False Positives:**

- `M N` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_TRAIN/141022.1`) (sent_id: `deanon_BFG_TRAIN/141022.1_29`)


In der Begründung führte die Abgabenbehörde- unter Hinweis auf die erhöhte  Mitwirkungspflicht der Bf. aus -, dass von der Bf. mit Ausnahme der Stundenaufzeichnungen  des Mitarbeiters Herrn M, dessen Kosten an die FB Kft weiterverrechnet wurden, keinerlei  Unterlagen vorgelegt worden seien, die die eingesetzten Mitarbeiter der Bf. am Projekt, die  aufgezeichneten Stunden dieser Mitarbeiter oder die durchgeführten Projektarbeiten  (Versuchsschritte, Testprotokolle, …)  im österreichischen Betrieb dokumentieren würden.

**False Positives:**

- `M,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_TRAIN/141022.1`) (sent_id: `deanon_BFG_TRAIN/141022.1_78`)


Von der Bf. wurden - zum Nachweis, dass diese Forschungstätigkeit in Österreich durchgeführt  wurde -  exemplarisch Stundenaufzeichnungen des Mitarbeiters Herrn M vorgelegt und  ausgeführt, dass für das Jahr 2011 und die Folgejahre Mitarbeiter der Bf. und „jedenfalls zur  Gänze Hr. M (der dieses Projekt federführend bearbeitet hat) und Hr. N als wissenschaftlicher  Leiter für dieses Projekt“ an den Forschungstätigkeiten mitgewirkt hätten.

**False Positives:**

- `M vorgelegt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_TRAIN/142167.1`) (sent_id: `deanon_BFG_TRAIN/142167.1_35`)


Ich kann mich bezüglich des Herrn V wirklich nicht mehr erinnern, ob es bei diesem zu  Schwarzzahlungen gekommen ist, aber wenn der das in seiner Vernehmung so angegeben hat,  kann es schon so gewesen sein.“

**False Positives:**

- `V wirklich nicht mehr erinnern, ob es bei diesem zu  Schwarzzahlungen gekommen ist, aber wenn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_TRAIN/142216.1`) (sent_id: `deanon_BFG_TRAIN/142216.1_35`)


Die Beschwerdeverfahren von Herrn M und der Immo-GmbH gegen die Inanspruchnahme als  Gesamtschuldner sind beim BFG zu den Zahlen RV/7100729/2022 bzw. RV/7101720/2021  erfasst.

**False Positives:**

- `M und` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_TRAIN/142627.1`) (sent_id: `deanon_BFG_TRAIN/142627.1_31`)


Herr M ist Ehemann von B.M. (nachfolgend Frau M), der bis 2/2018 geschäftsführenden  Mehrheitsgesellschafterin der M-GmbH.

**False Positives:**

- `M ist Ehemann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_TRAIN/142627.1`) (sent_id: `deanon_BFG_TRAIN/142627.1_320`)


Vor dem Hintergrund der Mehrfachfunktionen des Herrn M als GF der M-GmbH,  geschäftsführender Alleingesellschafter der Bf und 2/3-Mehrheitsvertreter der MEG bedarf es  keiner Erörterung, dass die Veranlassung der Rückzahlung einer von der Bf vor der  Rechnungsberichtigung bereits an die M-GmbH gezahlten USt oder deren Weiterleitung an das  FA in der Hand des Herrn M und damit auch in der Verantwortung der Bf lag.

**False Positives:**

- `M als GF` — no gold match — likely missing annotation
- `M und damit auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 82** (doc_id: `deanon_BFG_TRAIN/142627.1`) (sent_id: `deanon_BFG_TRAIN/142627.1_325`)


Auch insofern genügt es, an die Mehrfachfunktionen des Herrn M zu erinnern, aus der eine  klare Mitverantwortung der Bf am Abgabenausfall bei der M-GmbH resultiert.

**False Positives:**

- `M zu erinnern, aus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_TRAIN/142635.1`) (sent_id: `deanon_BFG_TRAIN/142635.1_10`)


Mit Bescheid  der Rechtsanwaltskammer Wien wurde Herr Mag. Markus Bulgarini, Rechtsanwalt in 1070  Wien, Mariahilfer Straße 20, zum Vertreter des Beschwerdeführers bestellt.

**False Positives:**

- `Mag. Markus Bulgarini, Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_TRAIN/144625.1`) (sent_id: `deanon_BFG_TRAIN/144625.1_23`)


Davon wurden 60/14.358stel an Herrn B und  11/14.358stel an Frau C 2017 verkauft.

**False Positives:**

- `B und` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_TRAIN/145189.1`) (sent_id: `deanon_BFG_TRAIN/145189.1_44`)


Er habe Herrn ZS angerufen  und ihm mitgeteilt, wer das Fahrzeug holen komme und Herr ZS habe den Schlüssel dann  herausgegeben.

**False Positives:**

- `ZS angerufen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_TRAIN/145189.1`) (sent_id: `deanon_BFG_TRAIN/145189.1_82`)


Das Fahrzeug ist auf die T  S.r.l.. zugelassen, deren Geschäftsführer und Gesellschafter Herr CD, der Schwager der Bf., ist.

**False Positives:**

- `CD,` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_TRAIN/145189.1`) (sent_id: `deanon_BFG_TRAIN/145189.1_100`)


Den Mitarbeitern wurden entweder in Frankfurt von Hrn. CD oder in Graz von Herrn ZS das  Fahrzeug und der Schlüssel übergeben.

**False Positives:**

- `ZS das  Fahrzeug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_TRAIN/145189.1`) (sent_id: `deanon_BFG_TRAIN/145189.1_102`)


Wenn ein Mitarbeiter nachhause  fahren wollte, rief Hr. CD Herrn ZS an und teilte ihm mit, wer das Fahrzeug holen kommt und  wies ihn an, den Schlüssel herauszugeben.

**False Positives:**

- `ZS an` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_TRAIN/145271.1`) (sent_id: `deanon_BFG_TRAIN/145271.1_27`)


In weiterer Folge wurde dieser von Herrn Jan Kaspeizer  nicht behoben und gelangte zurück an die  Finanzstrafbehörde.

**False Positives:**

- `Jan Kaspeizer  nicht behoben` — partial — gold is substring of pred: `Jan Kaspeizer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jan Kaspeizer`(person)

**Example 90** (doc_id: `deanon_BFG_TRAIN/145271.1`) (sent_id: `deanon_BFG_TRAIN/145271.1_32`)


Im Zuge einer Akteneinsicht in einem anderen  Strafverfahren am 10.1.2017 legte der Vertreter der steuerlichen Vertreterin, Herr Mag.  OMedR Morgana Yolcu, eine Vollmacht (Beilage Dok.Nr. 8) vor.

**False Positives:**

- `Mag.  OMedR Morgana Yolcu, eine Vollmacht` — partial — gold is substring of pred: `OMedR Morgana Yolcu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Morgana Yolcu`(person)

**Example 91** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_14`)


Mit Schreiben vom 14. Dezember 2012 richtete die belangte Behörde ein Ergänzungsersuchen  betreffend die Veranlagungsjahre 2006 bis 2008 an den Bf. worin ihm mitgeteilt wurde, dass  dem Finanzamt Unterlagen vorliegen würden, welchen zufolge er gemeinsam mit seiner  Ehegattin Geldanlagen bei Herrn XY bzw. bei der XYF getätigt habe und die Zinsen aus diesen  Anlagen thesauriert habe.

**False Positives:**

- `XY bzw. bei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Representative_vertreten_durch`

**F1:** 0.008 | **Precision:** 0.052 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `aca7d129`  
**Description:**
Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+GmbH|\s+Steuerberatung|\s+OG|\s+KG|\s+Rechtsanwalts|\s+PartG|\s+StbG|\s+\(|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.052 | 0.004 | 0.008 | 134 | 7 | 127 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 7 | 127 | 1627 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/133177.1`) (sent_id: `deanon_BFG_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Podzus  in der Beschwerdesache der  Planung Monuniost, Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich, vertreten durch Ilona Christahl,  Beschlingerstraße 66, 3233 Schlögelsbach, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ilona Christahl` | `Ilona Christahl` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Juliana Podzus` (person)
- `Planung Monuniost` (organisation)
- `Bleichhügelstraße 288, 4794 Knechtelsdorf, Österreich` (address)
- `Beschlingerstraße 66, 3233 Schlögelsbach, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/133706.1`) (sent_id: `deanon_BFG_TRAIN/133706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gloria Andres, Fuchshub 19, 4204 Aigen, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die Beschwerde vom  3. Juli 2015 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 29. Mai 2015  betreffend Anspruchszinsen (§ 205 BAO) 2003, 2004, 2005 und 2006 zu Steuernummer  06-338/7966  zu Recht erkannt:   I. Die angefochtenen Bescheide werden - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Gloria Andres` (person)
- `Fuchshub 19, 4204 Aigen, Österreich` (address)
- `06-338/7966` (tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/136313.1`) (sent_id: `deanon_BFG_TRAIN/136313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger im  Beschwerdeverfahren über die Beschwerde der Verl nach XY, vertreten durch Laurence Krekemeyer,  Steyersberg 2, 8481 Priebing, Österreich  vom 20. Juli 2021 gegen den Zurückweisungsbescheid des Finanzamtes  Österreich vom 7. Juli 2021 betreffend Antrag auf Durchführung einer  Arbeitnehmerveranlagung, beschlossen:  Der Vorlageantrag der Beschwerdeführerin Verl nach XY vom 10.9.2021 wird gemäß § 260 Abs.  1 BAO iVm § 264 BAO (insbesondere Abs. 4 lit e und Abs. 5) als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Laurence Krekemeyer` | `Laurence Krekemeyer` |

**Missed by this rule (FN):**

- `Dr. Ansgar Unterberger` (person)
- `Steyersberg 2, 8481 Priebing, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/137275.1`) (sent_id: `deanon_BFG_TRAIN/137275.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Carla Schweykart, Saaz 45, 8413 Stiefing, Österreich, vertreten durch Dr. Elmar Kresbach LL.M., Rechtsanwalt,  Wipplingerstraße 29/9, 1010 Wien, vom 7. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. April 2022, Zl. Zahl, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Elmar Kresbach LL.M.` | `Dr. Elmar Kresbach LL.M.` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Carla Schweykart` (person)
- `Saaz 45, 8413 Stiefing, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/141417.1`) (sent_id: `deanon_BFG_TRAIN/141417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Louisa Luppert  in der Beschwerdesache Vera Hempel,  Schnepfengasse 38, 9161 Ehrensdorf, Österreich  vertreten durch Elvira Postel, Waldpark 180, 3214 Wohlfahrtsschlag, Österreich, über die Beschwerde vom  4. Jänner 2023 gegen den Bescheid des Finanzamtes Österreich vom 5. Dezember 2022  betreffend Abweisung eines Aussetzungsantrages gem. § 212a BAO betreffend  Säumniszuschlag, Steuernummer 36-933/4246, nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elvira Postel` | `Elvira Postel` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Louisa Luppert` (person)
- `Vera Hempel` (person)
- `Schnepfengasse 38, 9161 Ehrensdorf, Österreich` (address)
- `Waldpark 180, 3214 Wohlfahrtsschlag, Österreich` (address)
- `36-933/4246` (tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/145403.1`) (sent_id: `deanon_BFG_TRAIN/145403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Sven Siemglüß  in der Beschwerdesache Josefine Schrörs,  Niesenbergergasse 8, 9831 Innerfragant, Österreich, vertreten durch Dr.in Rita Leinhos, Gladiolengasse 40, 4864 Breitenröth, Österreich, über die Beschwerde vom  13. Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 8. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2022 Steuernummer 03-666/4395  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Rita Leinhos` | `Dr.in Rita Leinhos` |

**Missed by this rule (FN):**

- `Mag. Sven Siemglüß` (person)
- `Josefine Schrörs` (person)
- `Niesenbergergasse 8, 9831 Innerfragant, Österreich` (address)
- `Gladiolengasse 40, 4864 Breitenröth, Österreich` (address)
- `03-666/4395` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Catharina Moewis,  Im Klosterhof 21N, 5241 Großenaich, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

**False Positives:**

- `Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Catharina Moewis`(person)
- `Im Klosterhof 21N, 5241 Großenaich, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Lubomir Baltßun, Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Mercuria Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Lubomir Baltßun`(person)
- `Georg-Bucher-Gasse 32, 2122 Münichsthal, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Janis Dollnig, Bahnhofzeile 7, 9062 Tuderschitz, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Wolfgang Freudelsperger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janis Dollnig`(person)
- `Bahnhofzeile 7, 9062 Tuderschitz, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/129254.1`) (sent_id: `deanon_BFG_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache StR VetR Corbinian Drügemöller, Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grant Thornton Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.Dr. Thomas Leitner`(person)
- `StR VetR Corbinian Drügemöller`(person)
- `Lähngraben Umgebung 38y, 3701 Großwiesendorf, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Irene van der Hoven  in der Beschwerdesache Kordelia van Clewe,  Piettegasse 15, 3341 Oberamt, Österreich, vertreten durch Johann Putzer, Liechtensteinstraße 35 Tür 5, 1090 Wien, über  die Beschwerde vom 20. April 2018 gegen die Bescheide des FA Tirol Ost  vom 16. März 2018  betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer 2013,   Einkommensteuer 2013 und Umsatzsteuer 2013, Steuernummer 20-364/1486  nach  durchgeführter mündlicher Verhandlung am 29.06.2020

**False Positives:**

- `Johann Putzer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Irene van der Hoven`(person)
- `Kordelia van Clewe`(person)
- `Piettegasse 15, 3341 Oberamt, Österreich`(address)
- `FA Tirol Ost`(organisation)
- `20-364/1486`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/129477.1`) (sent_id: `deanon_BFG_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Vivian Wenk, Haitzingallee 20, 3662 Kollnitz, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `ICON Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Marco Laudacher`(person)
- `Vivian Wenk`(person)
- `Haitzingallee 20, 3662 Kollnitz, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Westra ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pastel Pharma`(organisation)
- `Retzenegg 222, 3242 Ramsau, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_TRAIN/129872.1`) (sent_id: `deanon_BFG_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache James Loratis, Platzerweg 28, 4673 Baumgarting, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Gugenberger Barbara` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang Freilinger`(person)
- `James Loratis`(person)
- `Platzerweg 28, 4673 Baumgarting, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Mikoleizik, Schulwiesen 13, 4203 Stratreith, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Margot Artner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daisy Mikoleizik`(person)
- `Schulwiesen 13, 4203 Stratreith, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Wladimir Nüssli, Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Elke Hager` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wolfgang Aigner`(person)
- `Wladimir Nüssli`(person)
- `Rudolf-Wilflingseder-Straße 94, 8742 Rötsch, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_TRAIN/130733.1`) (sent_id: `deanon_BFG_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Matthäus Buskens, Edlach 19, 3141 Oberkilling, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

**False Positives:**

- `Helmut Binder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alfred Klaming`(person)
- `Matthäus Buskens`(person)
- `Edlach 19, 3141 Oberkilling, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/130834.1`) (sent_id: `deanon_BFG_TRAIN/130834.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin R und die fachkundigen Laienrichter L1 und L2 in den  Finanzstrafsachen gegen   1. A B, [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  2. [...], Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  3. [...]., Dr. Wagner-Gasse 35, 8700 Leoben, Österreich  alle vertreten durch BKS Steuerberatungs GmbH W, Untere  Hauptstraße 10, 3150 Wilhelmsburg  wegen der Finanzvergehen der grob fahrlässigen Abgabenverkürzungen gemäß § 34 Abs. 1 des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten und der belangten  Verbände vom 3. Juli 2018 (Poststempel 9. Juli 2018) gegen das Erkenntnis des Spruchsenates  beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Baden Mödling als  Finanzstrafbehörde vom 12. April 2018, SpS 18, Strafnummer 001 ff, 002 ff, in Anwesenheit des  Beschuldigten, dieser auch als Vertreter der belangten Verbände V1 und B Gesellschaft m.b.H.,  deren Verteidiger W, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Den Beschwerden wird stattgegeben, das angefochtene Erkenntnis des Spruchsenates  aufgehoben und die beim Finanzamt Baden Mödling als Finanzstrafbehörde zu den  Strafnummern 001 ff, 002 ff, geführten Finanzstrafverfahren wegen des Verdachtes der grob  fahrlässigen Abgabenverkürzung des Geschäftsführers gemäß § 34 Abs. 1 FinStrG bzw. der  belangten Verbände auch gemäß § 28a FinStrG für Abgaben der V1 2011 bis 2015 und der B  Gesellschaft m.b.H 2013 bis 2015 gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

**False Positives:**

- `BKS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)
- `Dr. Wagner-Gasse 35, 8700 Leoben, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/130839.1`) (sent_id: `deanon_BFG_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Zarin Finke,  Brauhausplatz 29, 9422 Untereberndorf, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Rupert Karl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zarin Finke`(person)
- `Brauhausplatz 29, 9422 Untereberndorf, Österreich`(address)

**Example 13** (doc_id: `deanon_BFG_TRAIN/130895.1`) (sent_id: `deanon_BFG_TRAIN/130895.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Priv.-Doz. Univ.-Prof. Ernst Uckermarck  über die Vorlageerinnerung der  Erich Ennulat, Leumühle 11, 4680 Leiten, Österreich  vertreten durch Hedwig Weber, Ausseer Straße 32, 8940 Liezen, vom  22.10.2020 zur Beschwerde vom 06.05.2020 gegen den Bescheid des Finanzamtes Judenburg  Liezen vom 01.04.2020 betreffend Sicherstellung gemäß § 232 BAO beschlossen:  Die Vorlageerinnerung wird als unzulässig zurückgewiesen.

**False Positives:**

- `Hedwig Weber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Univ.-Prof. Ernst Uckermarck`(person)
- `Erich Ennulat`(person)
- `Leumühle 11, 4680 Leiten, Österreich`(address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Jean Wohlrap, Weyprechtgasse 44M, 9701 Nußdorf, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Astoria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Peter Unger`(person)
- `Jean Wohlrap`(person)
- `Weyprechtgasse 44M, 9701 Nußdorf, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Samuel Rehnke` — partial — pred is substring of gold: `Samuel Rehnke, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ottfried Bremermann`(person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich`(address)
- `Samuel Rehnke, BSc`(person)
- `Planetengasse 30, 8455 Bischofegg, Österreich`(address)
- `14-141/9449`(tax_number)

**Example 16** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Jeanne von Fritz  in der Beschwerdesache Martha Michenfelder,  Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Dkfm.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Univ.-Prof.in Jeanne von Fritz`(person)
- `Martha Michenfelder`(person)
- `Marianne-Pollak-Gasse 16, 5204 Brunn, Österreich`(address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/131368.1`) (sent_id: `deanon_BFG_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Dr. Zlatan Kappelsberger, Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `LeitnerLeitner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Zlatan Kappelsberger`(person)
- `Maiselgasse 26, 9654 St. Lorenzen im Lesachtal, Österreich`(address)

**Example 18** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Intercura Teuhand Revisions ` — partial — pred is substring of gold: `Intercura Teuhand Revisions  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karen Vennemeyer`(person)
- `Neu-Reinbach 11, 4693 Fallholz, Österreich`(address)
- `Intercura Teuhand Revisions  GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_TRAIN/131567.1`) (sent_id: `deanon_BFG_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Severin Wöllecke  in der Finanzstrafsache gegen die  Beschuldigte Nicole Schlemper, Uteweg 12, 9624 Latschach, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

**False Positives:**

- `Mag. Heinz Wolfbauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Severin Wöllecke`(person)
- `Nicole Schlemper`(person)
- `Uteweg 12, 9624 Latschach, Österreich`(address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/132255.1`) (sent_id: `deanon_BFG_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Chen Helwig  in der Beschwerdesache Roxana Gehrbrandt,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr Christian Leskoschek` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Chen Helwig`(person)
- `Roxana Gehrbrandt`(person)

**Example 21** (doc_id: `deanon_BFG_TRAIN/132752.1`) (sent_id: `deanon_BFG_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Manuel de Keijzer, Schmieddorf 5, 6215 Achenkirch, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Maria Brandstetter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manuel de Keijzer`(person)
- `Schmieddorf 5, 6215 Achenkirch, Österreich`(address)

**Example 22** (doc_id: `deanon_BFG_TRAIN/132794.1`) (sent_id: `deanon_BFG_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Edwin Uebel, Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich, vertreten durch Dkfm.

**False Positives:**

- `Dkfm.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Edwin Uebel`(person)
- `Schauerleiten 5C, 3240 Kirnberg an der Mank, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/132893.1`) (sent_id: `deanon_BFG_TRAIN/132893.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Ute Höltje, Burghof 44, 5222 Spreitzenberg, Österreich, vertreten durch KAPAS Steuerberatung GmbH, Birkfelder Straße 25, 8160 Weiz, über  die Beschwerde vom 19.12.2019 gegen den Bescheid des Finanzamtes FA vom 13.05.2020  betreffend Feststellung von Einkünften gemäß § 188 BAO 2018 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `KAPAS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ute Höltje`(person)
- `Burghof 44, 5222 Spreitzenberg, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_TRAIN/133172.1`) (sent_id: `deanon_BFG_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Hon.-Prof.in Lena Ünlüer, Modsiedl 8, 4150 Katzing, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 51-253/7194  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Uniconsult` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Lena Ünlüer`(person)
- `Modsiedl 8, 4150 Katzing, Österreich`(address)
- `51-253/7194`(tax_number)

**Example 25** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Huberta Schwandt, Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 30-672/6934  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Commendatio Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Huberta Schwandt`(person)
- `Hufschmiedgasse 4Y, 4925 Hartlhof, Österreich`(address)
- `30-672/6934`(tax_number)

**Example 26** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwalt Mag. Wolfgang Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/133873.1`) (sent_id: `deanon_BFG_TRAIN/133873.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die als  Bescheidbeschwerde zu erledigende Berufung vom 21.02.2011 der Xy, Emil Zöchling-Gasse 149, 9063 Rosendorf, Österreich  vertreten durch Dr. Hans Bodendorfer Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010  Wien, gegen den Einkommensteuerbescheid für das Jahr 2005 des Finanzamtes Bruck  Eisenstadt Oberwart vom 29.11.2010, Steuernummer 66-205/7303   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hans Bodendorfer` — partial — pred is substring of gold: `Dr. Hans Bodendorfer Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Emil Zöchling-Gasse 149, 9063 Rosendorf, Österreich`(address)
- `Dr. Hans Bodendorfer Steuerberatungsges.m.b.H.`(organisation)
- `66-205/7303`(tax_number)

**Example 28** (doc_id: `deanon_BFG_TRAIN/134099.1`) (sent_id: `deanon_BFG_TRAIN/134099.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lea Capoluongo  in der Beschwerdesache Rupert Lübbersmeyer,  Peter-Tunner-Straße 84, 3601 Oberloiben, Österreich, vertreten durch Stb Gerhard Obrist, Hans-Schrott-Fiechtl-Straße 30, 6134  Vomp, über die Beschwerde vom 14.1.2011 gegen den Bescheid des FA Kufstein Schwaz  (nunmehr FA Österreich) vom 15.12.2010, StrNr, betreffend 1. Festsetzung der  Normverbrauchsabgabe für den Zeitraum Oktober 2008 und   2.

**False Positives:**

- `Stb Gerhard Obrist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Lea Capoluongo`(person)
- `Rupert Lübbersmeyer`(person)
- `Peter-Tunner-Straße 84, 3601 Oberloiben, Österreich`(address)

**Example 29** (doc_id: `deanon_BFG_TRAIN/134507.1`) (sent_id: `deanon_BFG_TRAIN/134507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Dipl.-Ing. Xaver Kühlwetter, Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich, vertreten durch Dr. Ferdinand Jenni, Jahngasse 18, 6850  Dornbirn, über die Beschwerde vom 10. November 2014 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Oktober 2014 betreffend Einkommensteuer 2013, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Ferdinand Jenni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Josef Ungericht`(person)
- `Dipl.-Ing. Xaver Kühlwetter`(person)
- `Mirnig 3, 8081 Heiligenkreuz am Waasen, Österreich`(address)

**Example 30** (doc_id: `deanon_BFG_TRAIN/134574.1`) (sent_id: `deanon_BFG_TRAIN/134574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Ing. Miklos Novikova, Carl Lutz-Straße 44, 2225 Blumenthal, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Untere Hauptstraße 10, 3150 Wilhelmsburg, über die Beschwerde vom 14. Jänner 2019  gegen den Haftungsbescheid des Finanzamtes Lilienfeld St. Pölten vom 17. Dezember 2018,  Steuernummer 62-482/0330, Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `BKS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Miklos Novikova`(person)
- `Carl Lutz-Straße 44, 2225 Blumenthal, Österreich`(address)
- `62-482/0330`(tax_number)

**Example 31** (doc_id: `deanon_BFG_TRAIN/134630.1`) (sent_id: `deanon_BFG_TRAIN/134630.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ophelia Kirischenko  in der Beschwerdesache Violetta Düerkob,  Lorettogasse 8, 4252 Reitern, Österreich, vertreten durch Eveline Effler, Trappengasse 22, 2601 Eggendorf, über die  Beschwerde vom 22. Juni 2021 gegen den Bescheid des Finanzamtes Österreich vom 27. Mai  2021 betreffend Zwangsstrafen 2021 Steuernummer 31-466/0163  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Eveline Effler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Ophelia Kirischenko`(person)
- `Violetta Düerkob`(person)
- `Lorettogasse 8, 4252 Reitern, Österreich`(address)
- `31-466/0163`(tax_number)

**Example 32** (doc_id: `deanon_BFG_TRAIN/134703.1`) (sent_id: `deanon_BFG_TRAIN/134703.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Irene Hildebrecht  in der Beschwerdesache KommR Dipl.-Ing. ÖkR Valentina Steinbrunn,  Ebrasdorf 161, 4320 Oberwagram, Österreich, vertreten durch Dr. Anke Reisch, Franz-Reisch-Straße 4, 6370 Kitzbühel, über  die Beschwerde vom 28. Juni 2013 gegen die Bescheide des Finanzamtes Kitzbühel Lienz  (nunmehr: Finanzamt Österreich) vom 22. Mai 2013, Str. Nr. 36-608/1721, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Oktober 2010      und Verspätungszuschlag  2.

**False Positives:**

- `Dr. Anke Reisch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Irene Hildebrecht`(person)
- `KommR Dipl.-Ing. ÖkR Valentina Steinbrunn`(person)
- `Ebrasdorf 161, 4320 Oberwagram, Österreich`(address)
- `36-608/1721`(tax_number)

**Example 33** (doc_id: `deanon_BFG_TRAIN/134762.1`) (sent_id: `deanon_BFG_TRAIN/134762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Simon Zens  in der Beschwerdesache Miriam Große-Bley,  Tipschern 13, 4052 Fürhappen, Österreich, vertreten durch Herrn Michael Haberl, Steuerberater, Hauptstraße 65, 8962  Gröbming, über die Beschwerde vom 9.7.2018 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 12.6.2018 betreffend Festsetzung des Dienstgeberbeitrages (DB) für die  Jahre 2013, 2014, 2015 und 2016 sowie des Zuschlages zum Dienstgeberbeitrag (DZ) für die  Jahre 2013, 2014, 2015 und 2016 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Herrn Michael Haberl` — partial — gold is substring of pred: `Michael Haberl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Simon Zens`(person)
- `Miriam Große-Bley`(person)
- `Tipschern 13, 4052 Fürhappen, Österreich`(address)
- `Michael Haberl`(person)

**Example 34** (doc_id: `deanon_BFG_TRAIN/134768.1`) (sent_id: `deanon_BFG_TRAIN/134768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache James Johanntokrax, Wandeckstraße 6, 4730 Aschach, Österreich, vertreten durch Mag. Manuela Henrich, Dr. Karl Renner Str. 5, 2560 Berndorf, über die  Beschwerde vom 28.06.2019  gegen den Bescheid des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich) vom 27. Mai 2019 betreffend Wiedereinsetzung in den vorigen Stand  nach Durchführung einer mündlichen Verhandlung betreffend Einkommensteuer für das Jahr  2012 Steuernummer 68-133/5727  zu Recht erkannt:   Die Beschwerde gegen die Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Manuela Henrich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `James Johanntokrax`(person)
- `Wandeckstraße 6, 4730 Aschach, Österreich`(address)
- `68-133/5727`(tax_number)

**Example 35** (doc_id: `deanon_BFG_TRAIN/135141.1`) (sent_id: `deanon_BFG_TRAIN/135141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  OMedR Bruno Kibar, Weissach 4, 5071 Walserfeld, Österreich, vertreten durch Dr. Martin Riedl, Franz-Josefs-Kai 5/DG, 1010  Wien, über die Beschwerde vom 3. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 26. August 2019  betreffend Gewährung von Familienbeihilfe ab März 2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Martin Riedl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Siegfried Fenz`(person)
- `OMedR Bruno Kibar`(person)
- `Weissach 4, 5071 Walserfeld, Österreich`(address)

**Example 36** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen Mag. Willibald Giesser, Eichingerweg 67, 4931 Neulendt, Österreich, vertreten durch HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft, Landstraßer Hauptstraße 27,  1030 Wien, über die Beschwerde des Beschuldigten vom 1. April 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 6,  Abgabenstrafen vom 2. März 2021, Zahl: MA6/206000002559/2020, in Anwesenheit des  Verteidigers und der Behördenvertreterin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der Zurückweisungsbescheid des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `HELLER TAXvisory ` — partial — pred is substring of gold: `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Willibald Giesser`(person)
- `Eichingerweg 67, 4931 Neulendt, Österreich`(address)
- `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`(organisation)

**Example 37** (doc_id: `deanon_BFG_TRAIN/135571.1`) (sent_id: `deanon_BFG_TRAIN/135571.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Univ.-Prof. Quentin Gerdener  in der Beschwerdesache Hon.-Prof.in Tatjana Schweneke, MSc,  Moorweg 23, 9300 Hörzendorf, Österreich, vertreten durch Steuerberatung Dr. Alfred Sorger GmbH, Steyrergasse 89,  8010 Graz, über die Beschwerde vom 8.3.2018 gegen die Bescheide des Finanzamtes Graz- Umgebung vom 14.12.2017 betreffend Einkommensteuer und Umsatzsteuer, jeweils für die  Jahre 2007 bis 2012 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Steuerberatung Dr. Alfred Sorger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Univ.-Prof. Quentin Gerdener`(person)
- `Hon.-Prof.in Tatjana Schweneke, MSc`(person)
- `Moorweg 23, 9300 Hörzendorf, Österreich`(address)

**Example 38** (doc_id: `deanon_BFG_TRAIN/135883.1`) (sent_id: `deanon_BFG_TRAIN/135883.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Hermann Walraevens, Am Sonnwendstein 8, 2022 Immendorf, Österreich, vertreten durch MOORE STEPHENS City  Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Hafnerplatz 12, 3500  Krems an der Donau, über die Beschwerde vom 23. August 2018 gegen den Bescheid des  Finanzamtes Waldviertel vom 1. August 2018, Steuernummer 14-863/6378, betreffend  Einkommensteuer 2017 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `MOORE STEPHENS City  Treuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Daniel Philip Pfau`(person)
- `Hermann Walraevens`(person)
- `Am Sonnwendstein 8, 2022 Immendorf, Österreich`(address)
- `14-863/6378`(tax_number)

**Example 39** (doc_id: `deanon_BFG_TRAIN/136145.1`) (sent_id: `deanon_BFG_TRAIN/136145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Gernot Sieglen, Oberlederau 7, 4224 Klingenwehr, Österreich  wohnhaft, StNr.: X1, vertreten durch Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010 Wien, betreffend die Berufung vom  25.05.2011 gegen die Einkommensteuerbescheide für die Jahre 2008 und 2009, vom  9.05.2011, zugestellt am 12.05.2011, des Finanzamtes Bruck Eisenstadt Oberwart  zu Recht erkannt

**False Positives:**

- `Dr. Hans Bodendorfer ` — partial — pred is substring of gold: `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gernot Sieglen`(person)
- `Oberlederau 7, 4224 Klingenwehr, Österreich`(address)
- `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`(organisation)

**Example 40** (doc_id: `deanon_BFG_TRAIN/136322.1`) (sent_id: `deanon_BFG_TRAIN/136322.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache Bertram Bertsche, Großbergweg 17, 9112 Griffnergemeinde, Österreich, vertreten durch Mag Manuela Henrich, Dr. Karl Renner Straße 5, 2560 Berndorf, über  die Beschwerde vom 23. Mai 2017 gegen den Bescheid des Finanzamtes Baden Mödling  (nunmehr Finanzamt Österreich)  vom 24. April 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 nach Durchführung einer mündlichen Verhandlung zu Recht  erkannt:   I.Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag Manuela Henrich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bertram Bertsche`(person)
- `Großbergweg 17, 9112 Griffnergemeinde, Österreich`(address)

**Example 41** (doc_id: `deanon_BFG_TRAIN/136471.1`) (sent_id: `deanon_BFG_TRAIN/136471.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Dipl.-Ing. Chen Köbbel,  Öxeltalweg 10, 4783 Öhret, Österreich, vertreten durch Erwachsenenvertretung Salzburg, Hauptstraße 91d, 5600  St.Johann/Pongau, über die Beschwerde vom 15. Juni 2021 gegen den Abweisungsbescheid  des Finanzamtes Österreich vom 20. Mai 2021 betreffend Familienbeihilfe ab Dezember 2018  zu Recht erkannt:   Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `Erwachsenenvertretung Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Chen Köbbel`(person)
- `Öxeltalweg 10, 4783 Öhret, Österreich`(address)

**Example 42** (doc_id: `deanon_BFG_TRAIN/136516.1`) (sent_id: `deanon_BFG_TRAIN/136516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache ÖkR Alessia Starklof, Oberer Jägerweg 15, 3385 Gerersdorf, Österreich, vertreten durch Birgit Priklopil Steuerberatung  GmbH, Amtshausgasse 1 Tür A, 7132 Frauenkirchen, über die Beschwerde vom 21. April 2021  gegen den Bescheid des Finanzamtes Österreich vom 25. März 2021 betreffend  Einkommensteuer 2019, Steuernummer 83-347/8210, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der Bescheid zu  Ungunsten der Beschwerdeführerin abgeändert.

**False Positives:**

- `Birgit Priklopil` — partial — pred is substring of gold: `Birgit Priklopil Steuerberatung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Alessia Starklof`(person)
- `Oberer Jägerweg 15, 3385 Gerersdorf, Österreich`(address)
- `Birgit Priklopil Steuerberatung  GmbH`(organisation)
- `83-347/8210`(tax_number)

**Example 43** (doc_id: `deanon_BFG_TRAIN/136562.1`) (sent_id: `deanon_BFG_TRAIN/136562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger über die  Beschwerde des Florenzia Cordfulland, LLB, Mürzgasse 64, 8733 Feistritz bei Knittelfeld, Österreich, vertreten durch Werner Mec, Holzmeistergasse  6/1/10, 1210 Wien, vom 8. Februar 2022, gegen die Vollstreckungsverfügung des Magistrates  der Stadt Wien, Magistratsabteilung 6, vom 29. Jänner 2022, Zl. Zahl, iZm einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als unbe- gründet abgewiesen  Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach Art. 133  Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

**False Positives:**

- `Werner Mec` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Florenzia Cordfulland, LLB`(person)
- `Mürzgasse 64, 8733 Feistritz bei Knittelfeld, Österreich`(address)

**Example 44** (doc_id: `deanon_BFG_TRAIN/136587.1`) (sent_id: `deanon_BFG_TRAIN/136587.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Valentin Leuprecht  in der Beschwerdesache Hemma Pavel,  Richard-Kürth-Straße 37, 5201 Zaisberg, Österreich, vertreten durch Dr. Gerhard Holzinger, Stadtplatz 36, 5280 Braunau am Inn,  über die Beschwerde vom 14. November 2016 gegen die Bescheide des Finanzamtes Braunau  Ried Schärding vom 20. September 2016 betreffend Festsetzung der Kraftfahrzeugsteuer  01.2015-12.2015, 04.2014-12.2014 sowie Festsetzung der Normverbrauchsabgabe 04/2014,  Steuernummer 43-311/2462  zu Recht erkannt:   I. Die angefochtenen Bescheide werden ersatzlos aufgehoben.

**False Positives:**

- `Dr. Gerhard Holzinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof. Valentin Leuprecht`(person)
- `Hemma Pavel`(person)
- `Richard-Kürth-Straße 37, 5201 Zaisberg, Österreich`(address)
- `43-311/2462`(tax_number)

**Example 45** (doc_id: `deanon_BFG_TRAIN/136857.1`) (sent_id: `deanon_BFG_TRAIN/136857.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde des  Erhard Ptaczek, Lettengasse 56, 9314 Hochosterwitz, Österreich, vertreten durch Bezirkshauptmannschaft Mistelbach, Hauptplatz 4,  2130 Mistelbach, vom 28. September 2020, gegen den Bescheid des Finanzamtes Waldviertel  vom 14. September 2020, betreffend Zurückweisung des Antrages auf Familienbeihilfe und den  Erhöhungsbetrag für die Monate März 2020 bis Juli 2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bezirkshauptmannschaft Mistelbach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Christian Doktor`(person)
- `Erhard Ptaczek`(person)
- `Lettengasse 56, 9314 Hochosterwitz, Österreich`(address)

**Example 46** (doc_id: `deanon_BFG_TRAIN/137037.1`) (sent_id: `deanon_BFG_TRAIN/137037.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Cornelia Pretis-Pösinger in der  Beschwerdesache Prof. Thomas Lukits, Bakk. phil., Dr.-Stichl-Weg 45, 9601 Lind, Österreich, vertreten durch Mag. Dr. Wabnig Armin,  Ortenburgerstraße 4/2, 9800 Spittal/Drau, wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend die Beschwerde vom  16.01.2019 gegen den Abweisungsbescheid betreffend erhöhte Familienbeihilfe,  Steuernummer 26-963/1885, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

**False Positives:**

- `Mag. Dr. Wabnig Armin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Prof. Thomas Lukits, Bakk. phil.`(person)
- `Dr.-Stichl-Weg 45, 9601 Lind, Österreich`(address)
- `26-963/1885`(tax_number)

**Example 47** (doc_id: `deanon_BFG_TRAIN/137353.1`) (sent_id: `deanon_BFG_TRAIN/137353.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Aurelia Hoentschke, MBA, U-Bahnstation XXXX - Adressbez, 1020 Wien, vertreten durch Mag. Dieter  Schneider, Gartengasse 21/10, 1050 Wien, über die Beschwerde vom 22. Dezember 2015  gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 23. November 2015 betreffend  Umsatzsteuer 2014, Steuernummer 12 469/6972 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Dieter  Schneider` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aurelia Hoentschke, MBA`(person)

**Example 48** (doc_id: `deanon_BFG_TRAIN/137432.1`) (sent_id: `deanon_BFG_TRAIN/137432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Prof. Gerhard Eibert, Treffelsdorf/Siebenbrünnerweg 5, 5360 Rußbach, Österreich, vertreten durch Mag. Nikolaus Vasak,  Ditscheinergasse 3/10, 1030 Wien, über die Beschwerde vom 2. Dezember 2020 gegen den  Bescheid des Magistrats der Stadt Wien MA 46 Verkehrsorganisation und technische  Verkehrsangelegenheiten vom 6. November 2020 betreffend Gebrauch des Luftraumes über  dem öffentlichen Grund vor der Liegenschaft Adresse durch sieben Lampen ohne  Gebrauchserlaubnis für den Zeitraum 1.1.2017 bis 31.12.2020, nach Durchführung der  beantragten mündlichen Verhandlung am 3. August 2022 in Anwesenheit des Schriftführers Sf,  zu Recht erkannt:  Gemäß § 279 Abs. 1 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

**False Positives:**

- `Mag. Nikolaus Vasak` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Christian Seywald`(person)
- `Prof. Gerhard Eibert`(person)
- `Treffelsdorf/Siebenbrünnerweg 5, 5360 Rußbach, Österreich`(address)

**Example 49** (doc_id: `deanon_BFG_TRAIN/137567.1`) (sent_id: `deanon_BFG_TRAIN/137567.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Cassandra Franzas, Ketzerhub 14, 4730 Auwies, Österreich, vertreten durch Rudolf Peter, Esteplatz 3 Tür 9, 1030 Wien,  betreffend Beschwerde vom 20. Mai 2016 gegen die Bescheide des damaligen Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 21. April 2016 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) für 2009, 2010, 2012 und 2013, sowie den Bescheid vom 2.  Oktober 2019 betreffend Umsatzsteuer 2015, Steuernummer 57-376/4892, beschlossen:  I. a)

**False Positives:**

- `Rudolf Peter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cassandra Franzas`(person)
- `Ketzerhub 14, 4730 Auwies, Österreich`(address)
- `57-376/4892`(tax_number)

**Example 50** (doc_id: `deanon_BFG_TRAIN/139258.1`) (sent_id: `deanon_BFG_TRAIN/139258.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Ing. Univ.-Prof.in Scarlett Steinfurt, Andreas Schrembser-Straße 30, 2095 Wolfsbach, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Oeynhausen, über die Beschwerde  vom 12. Oktober 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich, Dienststelle 16 Baden Mödling) vom 13. Juli 2017 betreffend  Einkommensteuer 2011 bis 2015 und Umsatzsteuer 2012 bis 2015 sowie Vorauszahlungen an  Einkommensteuer für das Jahr 2017, Steuernummer 59-534/9010   zu Recht erkannt:   I. Die Beschwerde wird hinsichtlich der Bescheide betreffend die Einkommensteuer  der Jahre 2011 – 2013 sowie betreffend die Umsatzsteuer der Jahre 2012 und 2013  gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `LMG ` — partial — pred is substring of gold: `LMG  Steuerberatungsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Univ.-Prof.in Scarlett Steinfurt`(person)
- `Andreas Schrembser-Straße 30, 2095 Wolfsbach, Österreich`(address)
- `LMG  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `59-534/9010`(tax_number)

**Example 51** (doc_id: `deanon_BFG_TRAIN/139422.1`) (sent_id: `deanon_BFG_TRAIN/139422.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. René Semmelhak  in der Beschwerdesache der  Energie Synlexder, Schalchgraben 7, 9470 Johannesberg, Österreich, vertreten durch Mag. Robert Bitsche, Nikolsdorfergasse 7-11/15,  Wien, betreffend Beschwerde vom 7. Oktober 2014 gegen die Bescheide des Finanzamtes  Wien 4/5/10 vom 10. September 2014 betreffend 1) Wiederaufnahme des Verfahren  hinsichtlich Feststellung von Einkünften gemäß § 188 BAO für 2012 und   2) Feststellung von Einkünften gemäß § 188 BAO für 2012 beschlossen:  I. Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e iVm. § 260 Abs. 1 lit. a BAO als  nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Robert Bitsche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. René Semmelhak`(person)
- `Energie Synlexder`(organisation)
- `Schalchgraben 7, 9470 Johannesberg, Österreich`(address)

**Example 52** (doc_id: `deanon_BFG_TRAIN/139681.1`) (sent_id: `deanon_BFG_TRAIN/139681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Florentin Ginner, Russengasse 3, 4943 Kager, Österreich, vertreten durch TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG, Stadionplatz 2 Tür 3, 8041 Graz, über die Beschwerde vom  4. Oktober 2005 gegen die Bescheide des Finanzamtes Graz-Umgebung (nunmehr Finanzamt  Österreich) vom 29. August 2005 betreffend Umsatzsteuer für die Jahre 2000 – 2003,  Steuernummer 05-330/4121  zu Recht:   I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2000 – 2002 wird Folge  gegeben.

**False Positives:**

- `TPG Wirtschaftstreuhand und ` — partial — pred is substring of gold: `TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Ginner`(person)
- `Russengasse 3, 4943 Kager, Österreich`(address)
- `TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG`(organisation)
- `05-330/4121`(tax_number)

**Example 53** (doc_id: `deanon_BFG_TRAIN/139729.1`) (sent_id: `deanon_BFG_TRAIN/139729.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Brendon Meißnest, Tarnoczygasse 16, 9585 Neumüllnern, Österreich, vertreten durch Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft, Aspernstraße 87/72, 1220 Wien, vom  30. Juni 2016 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 3. Juni 2016 betreffend  Zahlungserleichterungen § 212 BAO 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Tax Wood Audit` — partial — pred is substring of gold: `Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brendon Meißnest`(person)
- `Tarnoczygasse 16, 9585 Neumüllnern, Österreich`(address)
- `Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `FA Amstetten Melk Scheibbs`(organisation)

**Example 54** (doc_id: `deanon_BFG_TRAIN/139731.1`) (sent_id: `deanon_BFG_TRAIN/139731.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache PhD RgR Evelyn Emmelius, Trenkerweg 16, 9563 Tiebel, Österreich, vertreten durch SOLIDUS Steuerberatungs- und  Wirtschaftstreuhand GmbH, Seilerstätte 17 Top 12, 1010 Wien, betreffend Beschwerde vom  21. November 2022 gegen den Bescheid des Finanzamtes Österreich vom 15. Juli 2022  betreffend Körperschaftsteuervorauszahlungen 2022, Steuernummer 22-857/6756,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `SOLIDUS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PhD RgR Evelyn Emmelius`(person)
- `Trenkerweg 16, 9563 Tiebel, Österreich`(address)
- `22-857/6756`(tax_number)

**Example 55** (doc_id: `deanon_BFG_TRAIN/139801.1`) (sent_id: `deanon_BFG_TRAIN/139801.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Timon Rüppel, Nebersdorfer Hauptstraße 7, 8504 Klein-Preding, Österreich, vertreten durch TPA Steuerberatung GmbH,  Franzosenhausweg 47, 4030 Linz, über die Beschwerde vom 26. April 2018 gegen den Bescheid  des Finanzamtes Amstetten Melk Scheibbs (nunmehr Finanzamt Österreich) vom 18. April 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummer  34-642/3766  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `TPA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Patrick Brandstetter`(person)
- `Timon Rüppel`(person)
- `Nebersdorfer Hauptstraße 7, 8504 Klein-Preding, Österreich`(address)
- `34-642/3766`(tax_number)

**Example 56** (doc_id: `deanon_BFG_TRAIN/139802.1`) (sent_id: `deanon_BFG_TRAIN/139802.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Roy Schreinert, LLB, Laurschweg 4, 4143 Haitzendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Franzosenhausweg 47, 4030 Linz, über die Beschwerde vom 25. Oktober 2018 gegen den  Bescheid des Finanzamtes Amstetten Melk Scheibbs (nunmehr Finanzamt Österreich) vom  15. Oktober 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017  Steuernummer 13-441/2069  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `TPA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Patrick Brandstetter`(person)
- `Roy Schreinert, LLB`(person)
- `Laurschweg 4, 4143 Haitzendorf, Österreich`(address)
- `13-441/2069`(tax_number)

**Example 57** (doc_id: `deanon_BFG_TRAIN/139959.1`) (sent_id: `deanon_BFG_TRAIN/139959.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde des Evelyn Walz, Bichlenweg 41, 9220 Latschach, Österreich, vertreten durch Dr. Wolf Dietrich Mazakarini,  Gaullachergasse 15/1/12, 1160 Wien, vom 30. November 2021, gegen den Bescheid des  Finanzamtes Österreich vom 22. November 2021, betreffend Abweisung des Antrages  Gewährung der Familienbeihilfe und des Erhöhungsbetrages ab April 2021, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Wolf Dietrich Mazakarini` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Evelyn Walz`(person)
- `Bichlenweg 41, 9220 Latschach, Österreich`(address)

**Example 58** (doc_id: `deanon_BFG_TRAIN/140310.1`) (sent_id: `deanon_BFG_TRAIN/140310.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Kaspar Zijlema, Fellinggasse 9, 6210 Ehrenstall, Österreich, vertreten durch Eidlwimmer Steuerberatung-GmbH, Neutorstraße  52, 5020 Salzburg, über die Beschwerde vom 17. September 2020 gegen den Bescheid des  Finanzamtes Österreich vom 24. August 2020 betreffend Einkommensteuer 2018  Steuernummer 49-843/5688  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Eidlwimmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ralf Schatzl`(person)
- `Kaspar Zijlema`(person)
- `Fellinggasse 9, 6210 Ehrenstall, Österreich`(address)
- `49-843/5688`(tax_number)

**Example 59** (doc_id: `deanon_BFG_TRAIN/140381.1`) (sent_id: `deanon_BFG_TRAIN/140381.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ashley Frommholz  in der Beschwerdesache  Magdalena Nikoleitzik, Lauteracher Straße 9, 4572 Kniewas, Österreich, vertreten durch BDO Assurance GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   über die Beschwerde vom 1. Juni 2018 gegen die Bescheide des Finanzamt Bruck Eisenstadt Oberwart  vom 14. Mai 2018  betreffend Festsetzung Umsatzsteuer 1-12/2010, 1-12/2011, 1-12/2012, 1- 12/2013, 1- 12/2014, 1-12/2015 und 1-12/2016 sowie Verspätungszuschlag 2012 – 2016   I. zu Recht erkannt:   Die Bescheide betreffend Festsetzung Umsatzsteuer 1-12/2010 und 1-12/2011 sowie die  Bescheide betreffend Verspätungszuschlag 2012 – 2016 werden - ersatzlos - aufgehoben.

**False Positives:**

- `BDO Assurance` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Ashley Frommholz`(person)
- `Magdalena Nikoleitzik`(person)
- `Lauteracher Straße 9, 4572 Kniewas, Österreich`(address)
- `Finanzamt Bruck Eisenstadt Oberwart`(organisation)

**Example 60** (doc_id: `deanon_BFG_TRAIN/140472.1`) (sent_id: `deanon_BFG_TRAIN/140472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Gerlinde Tegener  in der Beschwerdesache PhD Niels Mattutat,  Dr.-Salzmann-Straße 2, 4860 Pichlwang, Österreich, vertreten durch Effizient Steuerberatung OG, Murlingengasse 58/1/6, 1120  Wien, über die Beschwerde vom 23. Juli 2019 gegen die Bescheide des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 24. Juni 2019 betreffend Haftungsbescheid Lohnsteuer  sowie betreffend Abgabenbescheide Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  für den Zeitraum 01.2015-12.2017 sowie Säumniszuschläge zur Lohnsteuer für die Jahre 2015  bis 2017 Steuernummer 55-538/1267  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Effizient` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Gerlinde Tegener`(person)
- `PhD Niels Mattutat`(person)
- `Dr.-Salzmann-Straße 2, 4860 Pichlwang, Österreich`(address)
- `55-538/1267`(tax_number)

**Example 61** (doc_id: `deanon_BFG_TRAIN/140536.1`) (sent_id: `deanon_BFG_TRAIN/140536.1_3`)


OSR Carla Crato,  Rudolf von Alt-Weg 7, 4150 Katzing, Österreich  als belangten Verband, beide vertreten durch Mag. Wolfgang Anton Winkler,  Ditscheinergasse 2 Tür 4, 1030 Wien, wegen Finanzordnungswidrigkeiten gem. § 49 Abs. 1 lit. a  FinStrG über die Beschwerde des Beschuldigten und des belangten Verbandes vom 29.  September 2022 gegen das jeweilige Erkenntnis des Amtes für Betrugsbekämpfung als  Finanzstrafbehörde vom 24. August 2022, zu Recht erkannt:  I.)

**False Positives:**

- `Mag. Wolfgang Anton Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR Carla Crato`(person)
- `Rudolf von Alt-Weg 7, 4150 Katzing, Österreich`(address)

**Example 62** (doc_id: `deanon_BFG_TRAIN/140678.1`) (sent_id: `deanon_BFG_TRAIN/140678.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Liu Wegeli, MA, Hanfgartenweg 35, 9635 Goldberg, Österreich, vertreten durch Mag. Hanno Michael  Stromberger, Peraustraße 29, 9500 Villach, über die Beschwerde vom 13. August 2019 gegen  die Bescheide des Finanzamtes Österreich (vormals Finanzamtes Klagenfurt ) je vom 12. Juli  2019 betreffend Haftung gemäß § 82 EStG 1988 (und Festsetzung von Säumniszuschlägen) und  Festsetzung von Dienstgeberbeiträgen zum Ausgleichsfonds für Familienbeihilfen 2009 bis  2013 (Steuernummer 95-493/1909 ) zu Recht erkannt:   I. Der Beschwerde betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 (und  Festsetzung von Säumniszuschlägen) und Festsetzung von Dienstgeberbeiträgen  zum Ausgleichsfonds für Familienbeihilfen für die Jahre 2009 bis 2012 wird  gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Hanno Michael  Stromberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Liu Wegeli, MA`(person)
- `Hanfgartenweg 35, 9635 Goldberg, Österreich`(address)
- `95-493/1909`(tax_number)

**Example 63** (doc_id: `deanon_BFG_TRAIN/140703.1`) (sent_id: `deanon_BFG_TRAIN/140703.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den durch den Senatsvorsitzenden Dr. Michael Rauscher  und die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Anita Eberhardt über die Beschwerden der Dagobert Veigl,  Tscholweg 27, 4062 Schauersfreiling, Österreich, vertreten durch Dr. Heinrich Balas, Operngasse 18/12a-16, 1040 Wien, vom  13.03.2023 gegen den (Sammel-)Bescheid des Finanzamtes Österreich vom 21.02.2023  betreffend Abweisung von Anträgen auf Wiedereinsetzung in den vorigen Stand nach  mündlicher Verhandlung zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Dr. Heinrich Balas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dagobert Veigl`(person)
- `Tscholweg 27, 4062 Schauersfreiling, Österreich`(address)

**Example 64** (doc_id: `deanon_BFG_TRAIN/140850.1`) (sent_id: `deanon_BFG_TRAIN/140850.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Walter Aiglsdorfer, den  Richter Dr. Ansgar Unterberger sowie die fachkundigen Laienrichter Leopold Pichlbauer und  Ing. Johannes Gruber in der Beschwerdesache Istvan  Bitici, Obertaxeralm 410, 8383 Doiber, Österreich, vertreten durch TPA  Regio Steuerberatung GmbH & Co KG, Franzosenhausweg 47, 4030 Linz, und ** über die  Beschwerde der beschwerdeführenden Partei vom 7. Dezember 2020 gegen den Bescheid des  Finanzamtes Linz (nunmehr Finanzamt Österreich) vom 10. November 2020 betreffend  Feststellung der Einkünfte gemäß § 188 BAO 2018 Steuernummer 61-935/8222  in  Anwesenheit der Schriftführerin Andrea Tober zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `TPA  Regio` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Walter Aiglsdorfer`(person)
- `Dr. Ansgar Unterberger`(person)
- `Istvan  Bitici`(person)
- `Obertaxeralm 410, 8383 Doiber, Österreich`(address)
- `61-935/8222`(tax_number)

**Example 65** (doc_id: `deanon_BFG_TRAIN/141002.1`) (sent_id: `deanon_BFG_TRAIN/141002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Eva Gabriels, Kroppenweg 35, 4084 Bäckenhof, Österreich, vertreten durch Mazars Austria GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Kärntner Ring 5-7, 1010 Wien, über die  Beschwerde vom 11. September 2019 gegen die Bescheide des Finanzamtes Wien 9/18/19  Klosterneuburg – nunmehr Finanzamt Österreich - vom 16. August 2019 betreffend  Einkommensteuer der Jahre 2015 bis 2018, Steuernummer 13-419/8146,   zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mazars Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Eva Gabriels`(person)
- `Kroppenweg 35, 4084 Bäckenhof, Österreich`(address)
- `13-419/8146`(tax_number)

**Example 66** (doc_id: `deanon_BFG_TRAIN/141022.1`) (sent_id: `deanon_BFG_TRAIN/141022.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lukas Weinbauer  in der Beschwerdesache Xenia Ostler,  Junkerau 14, 4775 Unterpramau, Österreich, vertreten durch Mag. Philipp Casper, Kalchberggasse 1, 8010 Graz, über die  Beschwerde vom 28. Juli 2015 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3. Juli  2015 betreffend Forschungsprämie 2011 Steuernummer 93-914/0665  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Philipp Casper` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof.in Lukas Weinbauer`(person)
- `Xenia Ostler`(person)
- `Junkerau 14, 4775 Unterpramau, Österreich`(address)
- `93-914/0665`(tax_number)

**Example 67** (doc_id: `deanon_BFG_TRAIN/141677.1`) (sent_id: `deanon_BFG_TRAIN/141677.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Sonja Stradner in der Beschwerdesache  Traude Schellscheid, Heidenreichring 11, 6123 Umlberg, Österreich, vertreten durch Mag. Christoph Heimerl, Papagenogasse 1A Tür 7,  1060 Wien, betreffend Beschwerde vom 27. April 2015 gegen die Bescheide des Finanzamtes  Baden Mödling (nunmehr Finanzamt Österreich) vom 20. März 2015 betreffend Umsatzsteuer  2011 und Umsatzsteuer 2012 Steuernummer 50-793/3376  beschlossen:  I. Die Vorlageanträge werden gemäß § 264 Abs. 4 lit e BAO in Verbindung mit § 260 Abs. 1 lit. b  BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Mag. Christoph Heimerl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traude Schellscheid`(person)
- `Heidenreichring 11, 6123 Umlberg, Österreich`(address)
- `50-793/3376`(tax_number)

**Example 68** (doc_id: `deanon_BFG_TRAIN/141973.1`) (sent_id: `deanon_BFG_TRAIN/141973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Monika Ahorn in der  Beschwerdesache Nikolaus Tombült, Ebnergasse 2, 3681 Gartln, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse  11 Tür 4.

**False Positives:**

- `Sera Trust` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nikolaus Tombült`(person)
- `Ebnergasse 2, 3681 Gartln, Österreich`(address)

**Example 69** (doc_id: `deanon_BFG_TRAIN/141991.1`) (sent_id: `deanon_BFG_TRAIN/141991.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Deborah Sobcyk, Franz-Pfaffinger Platz 147, 3232 Großa, Österreich, vertreten durch Mag. (FH) Georg Sonnleitner,  Rathausstraße 21/12, 1010 Wien, über die Beschwerde vom 15. Februar 2021 gegen den  Einkommensteuerbescheid 2018 des Finanzamtes Österreich vom 22. Jänner 2021 zu  Steuernummer 92-863/8691  zu Recht erkannt:  Gemäß § 279 Abs. 1 BAO wird der Beschwerde stattgegeben und der angefochtene Bescheid  folgendermaßen abgeändert: Die Einkommensteuer für das Jahr 2018 wird mit 3.915,00 Euro  festgesetzt;

**False Positives:**

- `Mag.` — similar text (different position): `Mag. Christian Seywald`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Christian Seywald`(person)
- `Univ.-Prof.in Deborah Sobcyk`(person)
- `Franz-Pfaffinger Platz 147, 3232 Großa, Österreich`(address)
- `92-863/8691`(tax_number)

**Example 70** (doc_id: `deanon_BFG_TRAIN/142166.1`) (sent_id: `deanon_BFG_TRAIN/142166.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Fatima Sixel  in der Beschwerdesache Olga Gillissen,  Strebitzfeld 15, 3911 Riebeis, Österreich, vertreten durch Dr. Michael Kotschnigg, Stadlauer Straße 39/1/12, 1220 Wien,  über die Beschwerde vom 11. Juni 2014 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2014 betreffend Umsatzsteuer 2007, Steuernummer 56-737/3592, zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Michael Kotschnigg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Fatima Sixel`(person)
- `Olga Gillissen`(person)
- `Strebitzfeld 15, 3911 Riebeis, Österreich`(address)
- `56-737/3592`(tax_number)

**Example 71** (doc_id: `deanon_BFG_TRAIN/142167.1`) (sent_id: `deanon_BFG_TRAIN/142167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Silvia Ziegelmeier,  Conrad Crefe-Weg 6, 3924 Ober Neustift, Österreich, vertreten durch Mag. Beate Christina Holper, Gonzagagasse 15, 1010 Wien,  über die Beschwerde vom 27. April 2016 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 23. Februar 2016 betreffend Einkommensteuer für die  Jahre 2008 bis 2013, Umsatzsteuer 2008-2014 und Anspruchszinsen 2008 bis 2013;

**False Positives:**

- `Mag. Beate Christina Holper` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Silvia Ziegelmeier`(person)
- `Conrad Crefe-Weg 6, 3924 Ober Neustift, Österreich`(address)

**Example 72** (doc_id: `deanon_BFG_TRAIN/142222.1`) (sent_id: `deanon_BFG_TRAIN/142222.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Alois Hölscher  in der Beschwerdesache Anatol Waldhauser,  Kontiglühestraße 3, 9761 Emberg, Österreich  vertreten durch Fidas Graz Steuerberatung GmbH, Petersbergenstraße 7, 8042  Graz, über die Beschwerde vom 08. März 2022 gegen den Bescheid des Finanzamtes Österreich  vom 08. Februar 2022 betreffend Einkommensteuer 2020 zu Steuernummer 87-826/9783  zu  Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Fidas Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Alois Hölscher`(person)
- `Anatol Waldhauser`(person)
- `Kontiglühestraße 3, 9761 Emberg, Österreich`(address)
- `87-826/9783`(tax_number)

**Example 73** (doc_id: `deanon_BFG_TRAIN/142759.1`) (sent_id: `deanon_BFG_TRAIN/142759.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den Richter  Mag. Christian Seywald und die fachkundigen Laienrichter Mag. Johannes Denk und  Mag. Markus Fischer BA in der Beschwerdesache Calvin Arff, O1, St.1 wohnhaft, vertreten  durch LBG Wien Steuerberatung GmbH, 1030 Wien, Boerhaavegasse 6, betreffend die  Bescheidbeschwerde vom 30.01.2014 gegen die Einkommensteuerbescheide für die  Veranlagungsjahre 2005, 2006, 2007, 2008, 2009, 2010 und 2011, vom 12., 14., 19., 21., 25.,  27. und 29. November 2013, zugestellt im Nov. und Dez.

**False Positives:**

- `LBG Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Christian Seywald`(person)
- `Calvin Arff`(person)

**Example 74** (doc_id: `deanon_BFG_TRAIN/142919.1`) (sent_id: `deanon_BFG_TRAIN/142919.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Eckard Fläschendräger  in der Säumnisbeschwerdesache  DDr. DDr. Engelbert Krentzer, Gaisbuchen 26, 4203 Altenberg bei Linz, Österreich, vertreten durch Mag. Susanne Tanzmeister, MBA,  Steuerberaterin, Schönaugasse 106, 8010 Graz, über die Beschwerde vom 29.11.2023, beim  Bundesfinanzgericht am 7.12.2023 eingelangt, wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend den Antrag vom 26.4.2023 auf  Aufhebung des Einkommensteuerbescheides 2020 vom 26.4.2022 gemäß § 299 BAO  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs 7 lit b BAO iVm § 260 Abs 1 lit a BAO als nicht  zulässig zurückgewiesen.

**False Positives:**

- `Mag. Susanne Tanzmeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Eckard Fläschendräger`(person)
- `DDr. DDr. Engelbert Krentzer`(person)
- `Gaisbuchen 26, 4203 Altenberg bei Linz, Österreich`(address)

**Example 75** (doc_id: `deanon_BFG_TRAIN/143364.1`) (sent_id: `deanon_BFG_TRAIN/143364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Beate Holzem, LLB, Neurissenweg 9, 3240 Loipersdorf, Österreich, vertreten durch Mag. (FH) Gerda Budler,  Hochstraße 1, 2563 Pottenstein, über die Beschwerden (ursprünglich: Berufungen) des  Abgabepflichtigen, hierbei damals vertreten durch FrühereSteuerlicheVertretung,   vom 23. Dezember 2011 gegen folgende Bescheide des Finanzamtes WohnsitzFA:  - Einkommensteuerbescheid 2001 vom 6. Dezember 2011,  - Einkommensteuerbescheid 2002 vom 6. Dezember 2011,  - Einkommensteuerbescheid 2003 vom 6. Dezember 2011,  - Einkommensteuerbescheid 2004 vom 6. Dezember 2011,  - Einkommensteuerbescheid 2006 vom 12. Dezember 2011 und  - Einkommensteuerbescheid 2007 vom 12. Dezember 2011,  wobei die Beschwerde hinsichtlich 2003 und 2004 gemäß § 253 BAO auch als gegen die  Einkommensteuerbescheide 2003 und 2004 vom 7. Juli 2016 gerichtet gilt,   sowie vom 7. Mai 2013 gegen den Einkommensteuerbescheid 2005 des Finanzamtes  WohnsitzFA vom 29. März 2013 zu Steuernummer 79-920/3487, wobei die  Beschwerde gemäß § 253 BAO auch als gegen den Einkommensteuerbescheid 2005  vom 7. Juli 2016 gerichtet gilt,  zu Recht erkannt:  Gemäß § 279 Abs. 1 BAO wird der Beschwerde vom 23. Dezember 2011 gegen den  Einkommensteuerbescheid 2001 vom 6. Dezember 2011, gegen den Einkommensteuer- bescheid 2002 vom 6. Dezember 2011, gegen den Einkommensteuerbescheid 2006 vom  12. Dezember 2011 und gegen den Einkommensteuerbescheid 2007 vom 12. Dezember 2011  stattgegeben;

**False Positives:**

- `Mag.` — similar text (different position): `Mag. Christian Seywald`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Christian Seywald`(person)
- `Beate Holzem, LLB`(person)
- `Neurissenweg 9, 3240 Loipersdorf, Österreich`(address)
- `79-920/3487`(tax_number)

**Example 76** (doc_id: `deanon_BFG_TRAIN/143885.1`) (sent_id: `deanon_BFG_TRAIN/143885.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Liu Wollziefer  in der Beschwerdesache Maurice Vybiralik, Bakk. rer. nat.,  Burgstall 6, 9554 Gößeberg, Österreich, vertreten durch Dr. B., Burgstall 6, 9554 Gößeberg, Österreich, über die Beschwerde vom 8. Februar 2023  gegen den Bescheid des Finanzamtes Österreich vom 4. Jänner 2023 über die Festsetzung einer  Zwangsstrafe, Steuernummer 02-097/5090, nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Liu Wollziefer`(person)
- `Maurice Vybiralik, Bakk. rer. nat.`(person)
- `Burgstall 6, 9554 Gößeberg, Österreich`(address)
- `Burgstall 6, 9554 Gößeberg, Österreich`(address)
- `02-097/5090`(tax_number)

**Example 77** (doc_id: `deanon_BFG_TRAIN/143997.1`) (sent_id: `deanon_BFG_TRAIN/143997.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache OStR Priv.-Doz. Engelbert Donatius, Ponhut 30, 5144 Hangöbl, Österreich, vertreten durch Dr. Wolfgang Halm, Berggasse  10, 1090 Wien, betreffend Beschwerde vom 10. Juni 2022 gegen die Bescheide des  Finanzamtes Österreich betreffend Einkommensteuer 2002 und 2003 sowie Anspruchszinsen  (§ 205 BAO) 2002 und 2003, Steuernummer 40-814/0545, nach antragsgemäßer  Durchführung einer mündlichen Verhandlung beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Wolfgang Halm` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Priv.-Doz. Engelbert Donatius`(person)
- `Ponhut 30, 5144 Hangöbl, Österreich`(address)
- `40-814/0545`(tax_number)

**Example 78** (doc_id: `deanon_BFG_TRAIN/144072.1`) (sent_id: `deanon_BFG_TRAIN/144072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Yelec Träubel, Pelargonienweg 13, 4063 Rudelsdorf, Österreich, vertreten durch Mag. Wolfgang Andreas Kleinhappel, Rabensteig 8/3a, 1010 Wien,  über die Beschwerde vom 23. Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom  10. Mai 2023 betreffend Zurückweisung des Antrages auf Familienbeihilfe vom 14. Juni 2021  für Karin Steilen  für den Zeitraum März 2020 bis April 2021, Steuernummer  41-392/0377 (SVNR 4756010962), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Wolfgang Andreas Kleinhappel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Yelec Träubel`(person)
- `Pelargonienweg 13, 4063 Rudelsdorf, Österreich`(address)
- `Karin Steilen`(person)
- `41-392/0377`(tax_number)
- `4756010962`(social_security_number)

**Example 79** (doc_id: `deanon_BFG_TRAIN/144093.1`) (sent_id: `deanon_BFG_TRAIN/144093.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Leopold Tepe  in der Beschwerdesache Verona Döhl, Bakk. rer. nat. MA,  Liese Prokop-Gasse 7, 9560 Graben, Österreich, vertreten durch Dr. Georg Lugert, Dr Karl Renner Promenade 10, 3100 St.  Pölten, über die Beschwerde vom 27. September 2018 gegen den Haftungsbescheid  des Finanzamt Purkersdorf  vom 11. Juli 2018 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Georg Lugert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof. Dr. Leopold Tepe`(person)
- `Verona Döhl, Bakk. rer. nat. MA`(person)
- `Liese Prokop-Gasse 7, 9560 Graben, Österreich`(address)
- `Finanzamt Purkersdorf`(organisation)

**Example 80** (doc_id: `deanon_BFG_TRAIN/144409.1`) (sent_id: `deanon_BFG_TRAIN/144409.1_2`)


Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache OStR RgR Lubomir Repp, Am Klauberpark 71, 8461 Ratsch an der Weinstraße, Österreich  vertreten durch Mag. Hartwig Franz Allmaier,  Wirtschaftstreuhänder und Steuerberater in 9020 Klagenfurt/Wörthersee, Bäckergasse 15,  über die Beschwerde vom 12. März 2024 gegen den Bescheid des Finanzamtes Österreich vom  5. März 2024 betreffend Festsetzung einer Zwangsstrafe gemäß § 111 BAO in der mündlichen  Verhandlung am 22.04.2024 zu Recht erkannt (Steuernummer 63-831/2986):   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Hartwig Franz Allmaier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR RgR Lubomir Repp`(person)
- `Am Klauberpark 71, 8461 Ratsch an der Weinstraße, Österreich`(address)
- `63-831/2986`(tax_number)

**Example 81** (doc_id: `deanon_BFG_TRAIN/144618.1`) (sent_id: `deanon_BFG_TRAIN/144618.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Viola Wannags, Badeseeplatz 39, 8332 Wetzelsdorf, Österreich, vertreten durch RA, RA_Adr, über die Beschwerde vom 12. März 2019 gegen den  Bescheid des Finanzamtes Österreich vom 1. Februar 2019 betreffend Grunderwerbsteuer  2019, Steuernummer 05-238/5606, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

**False Positives:**

- `RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viola Wannags`(person)
- `Badeseeplatz 39, 8332 Wetzelsdorf, Österreich`(address)
- `05-238/5606`(tax_number)

**Example 82** (doc_id: `deanon_BFG_TRAIN/144697.1`) (sent_id: `deanon_BFG_TRAIN/144697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Virgil Wohlbrecht, Eledweg 14, 2534 Glashütten, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13  Tür Turm 24, 1100 Wien, und Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH,  Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 24. April 2024 gegen den  Bescheid des Finanzamtes Österreich vom 10. April 2024 betreffend Festsetzung des  Energiekrisenbeitrag-Strom für den Zeitraum 1. Dezember 2022 bis 30. Juni 2023,  Steuernummer 83-527/2663, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `TPA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Andreas Stanek`(person)
- `Virgil Wohlbrecht`(person)
- `Eledweg 14, 2534 Glashütten, Österreich`(address)
- `83-527/2663`(tax_number)

**Example 83** (doc_id: `deanon_BFG_TRAIN/144816.1`) (sent_id: `deanon_BFG_TRAIN/144816.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Maria Grohe in der Beschwerdesache  Marion Durukan, vertreten durch Edinger KG, Am Föhrensee 24, 3452 Atzenbrugg, betreffend  Beschwerde vom 13. Mai 2015 gegen den Bescheid des Finanzamtes Waldviertel vom 10. April  2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 Steuernummer  29-027/8170  den Beschluss gefasst:  I.  Der Vorlageantrag vom 28.01.2016 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 lit.d BAO als gegenstandslos erklärt.

**False Positives:**

- `Edinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Marion Durukan`(person)
- `29-027/8170`(tax_number)

**Example 84** (doc_id: `deanon_BFG_TRAIN/144822.1`) (sent_id: `deanon_BFG_TRAIN/144822.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Kurt Weiffenbach, Anton-Neumayr-Platz 21, 4175 Stamering, Österreich, vertreten durch Effizient Steuerberatung OG,  Murlingengasse 58/1/6, 1120 Wien, über die Beschwerde vom 20. Juni 2023 gegen den  Bescheid des Finanzamtes Österreich vom 7. Juni 2023, Steuernummer 01-202/0774,  betreffend Zahlungserleichterungen gemäß § 212 BAO, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Effizient` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kurt Weiffenbach`(person)
- `Anton-Neumayr-Platz 21, 4175 Stamering, Österreich`(address)
- `01-202/0774`(tax_number)

**Example 85** (doc_id: `deanon_BFG_TRAIN/144966.1`) (sent_id: `deanon_BFG_TRAIN/144966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Babette Stork, Am Kiesgrund 17, 2013 Untergrub, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 313, 4040 Linz, über die Beschwerde vom  18. Oktober 2022 gegen den Bescheid des Finanzamtes Österreich vom 22. September 2022  betreffend Einkommensteuer 2021 Steuernummer 04-174/6985  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Walter Aiglsdorfer`(person)
- `Babette Stork`(person)
- `Am Kiesgrund 17, 2013 Untergrub, Österreich`(address)
- `04-174/6985`(tax_number)

**Example 86** (doc_id: `deanon_BFG_TRAIN/144970.1`) (sent_id: `deanon_BFG_TRAIN/144970.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Sefzyk  in der Beschwerdesache Janis Buchal, MBA,  Moosscheibe 49, 3652 Losau, Österreich, vertreten durch Dr. Gerhard Holzinger, Stadtplatz 36, 5280 Braunau am Inn,  über die Beschwerde vom 14. November 2016 gegen die Bescheide des Finanzamtes Braunau  Ried Schärding vom 20. September 2016 betreffend Festsetzung der Kraftfahrzeugsteuer 04- 12/2014 sowie 01-12/2015, Steuernummer 12-285/8382  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gerhard Holzinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Univ.-Prof. Niels Sefzyk`(person)
- `Janis Buchal, MBA`(person)
- `Moosscheibe 49, 3652 Losau, Österreich`(address)
- `12-285/8382`(tax_number)

**Example 87** (doc_id: `deanon_BFG_TRAIN/145189.1`) (sent_id: `deanon_BFG_TRAIN/145189.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Fiona Dudek  in der Beschwerdesache Saskia Widmeier,  Donaupark 5, 3822 Schlader, Österreich, vertreten durch Rechtsanwalt Mag. Werner Purr, Neutorgasse 49/I, 8010 Graz,  im fortgesetzten Verfahren über die Beschwerde vom 27. Februar 2020 gegen den Bescheid  des Finanzamtes Österreich vom 29. Jänner 2020 betreffend Normverbrauchsabgabe 06.2019  Steuernummer 82-133/7483  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rechtsanwalt Mag. Werner Purr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag.a Fiona Dudek`(person)
- `Saskia Widmeier`(person)
- `Donaupark 5, 3822 Schlader, Österreich`(address)
- `82-133/7483`(tax_number)

**Example 88** (doc_id: `deanon_BFG_TRAIN/145451.1`) (sent_id: `deanon_BFG_TRAIN/145451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Herrn KzlR Estelle Kaufholz, Alte Schulgasse 37, 5521 Bairau, Österreich, vertreten durch Eckhardt  SteuerberatungsgmbH, Hauptstraße 58, 7033 Pöttsching, über   1. die Beschwerde vom 7. Februar 2024 gegen den Bescheid des Finanzamtes Österreich  vom 10. Jänner 2024 betreffend Abweisung eines Antrages auf Stundung gemäß § 212  BAO   2.

**False Positives:**

- `Eckhardt ` — partial — pred is substring of gold: `Eckhardt  SteuerberatungsgmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Estelle Kaufholz`(person)
- `Alte Schulgasse 37, 5521 Bairau, Österreich`(address)
- `Eckhardt  SteuerberatungsgmbH`(organisation)

**Example 89** (doc_id: `deanon_BFG_TRAIN/145500.1`) (sent_id: `deanon_BFG_TRAIN/145500.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Thaddäus Kusmierek  in der Beschwerdesache Sven Attanasio,  Rumänien , vertreten durch Frau Felicitas Niedermann, Rechtsanwältin, CH-8590 Romanshorn,  betreffend Säumnisbeschwerde vom 13.6.2024 betreffend Einkommensteuer 2022  (Arbeitnehmerveranlagung) gegen die Amtspartei FA Tirol Ost  beschlossen:  Das Beschwerdeverfahren wird gem. § 284 Abs 2 BAO eingestellt.

**False Positives:**

- `Frau Felicitas Niedermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Thaddäus Kusmierek`(person)
- `Sven Attanasio`(person)
- `FA Tirol Ost`(organisation)

**Example 90** (doc_id: `deanon_BFG_TRAIN/145612.1`) (sent_id: `deanon_BFG_TRAIN/145612.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pagitsch, der  Richterin Dr. Anna Radschek sowie die fachkundigen Laienrichter KR Ing. Hans Eisenkölbl und  Mag. Michael Heumesser in der Beschwerdesache Laura Kaplaner, Zehetmayrgut 160, 4710 Niederweng, Österreich, vertreten durch  APP Steuerberatung GmbH, Schenkenstraße 4 / 6.

**False Positives:**

- `APP` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laura Kaplaner`(person)
- `Zehetmayrgut 160, 4710 Niederweng, Österreich`(address)

**Example 91** (doc_id: `deanon_BFG_TRAIN/145648.1`) (sent_id: `deanon_BFG_TRAIN/145648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Eugen Mittlmaier, Westlandstraße 3, 5201 Schöngumprechting, Österreich  vertreten durch TPA STB Wien GmbH Wien,  Wiedner Gürtel 13, Turm 24, 1100 Wien, über die Beschwerde vom 2. Mai 2013 gegen den  Bescheid des Finanzamts Wien 9/18/19 Klosterneuburg (nunmehr: Finanzamt Österreich) vom  2. April 2013 betreffend Einkommensteuer 2004, Steuernummer 13-875/5748, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `TPA STB Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Eugen Mittlmaier`(person)
- `Westlandstraße 3, 5201 Schöngumprechting, Österreich`(address)
- `13-875/5748`(tax_number)

**Example 92** (doc_id: `deanon_BFG_TRAIN/145732.1`) (sent_id: `deanon_BFG_TRAIN/145732.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Prof.in Mag.a Cynthia Hayder, Anton Schott-Straße 67, 3386 Untergraben, Österreich, vertreten durch Keckeis Fiel Scheidbach OG, 6800 Feldkirch,  Drevesstraße 2, über die Beschwerde vom 17. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 16. Februar 2023 betreffend Festsetzung der Normverbrauchsabgabe  (Berechnungsstichtag 14.01.2022), zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Keckeis Fiel Scheidbach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Josef Ungericht`(person)
- `Prof.in Mag.a Cynthia Hayder`(person)
- `Anton Schott-Straße 67, 3386 Untergraben, Österreich`(address)

**Example 93** (doc_id: `deanon_BFG_TRAIN/145805.1`) (sent_id: `deanon_BFG_TRAIN/145805.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Zoltan Lentze  in der  Beschwerdesache Piedro Goeres, Bräuhausberg 16, 4625 Humplberg, Österreich, vertreten durch Heisinger Steuerberatung  GmbH, Am Teich 12, 7301 Deutschkreutz, betreffend Beschwerde vom 30. Juni 2020 gegen die  Bescheide des Finanzamtes Wien 1/23, nunmehr Finanzamt Österreich, Dienststelle Wien 1/23  vom 9. März 2020 betreffend Wiederaufnahme betreffend Einkommensteuer 2010,  Wiederaufnahme betreffend Einkommensteuer 2011, Wiederaufnahme betreffend  Einkommensteuer 2012, Wiederaufnahme betreffend Einkommensteuer 2013,  Wiederaufnahme betreffend Einkommensteuer 2014, Wiederaufnahme betreffend  Einkommensteuer 2015 und Einkommensteuer 2012 Steuernummer 75-025/8578  beschlossen:   Die Beschwerde vom 30. Juni 2020 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Heisinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Zoltan Lentze`(person)
- `Piedro Goeres`(person)
- `Bräuhausberg 16, 4625 Humplberg, Österreich`(address)
- `75-025/8578`(tax_number)

</details>

---

## `Frau_Name`

**F1:** 0.005 | **Precision:** 0.800 | **Recall:** 0.002  

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
| 0.800 | 0.002 | 0.005 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 1 | 1460 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_5`)


Entscheidungsgründe  I. Verfahrensgang:  1. Aufgrund einer anonymen Anzeige im April 2013 wurden finanzpolizeiliche Ermittlungen  durchgeführt und erhoben, dass Frau Martha Michenfelder (= Beschwerdeführerin, Bf) das Fahrzeug der  Marke X1, FIN Nr1, Erstzulassung (EZ) 1.10.2012, mit dem deutschen Kennzeichen AA1, im  Inland verwendet.

| Predicted | Gold |
|---|---|
| `Martha Michenfelder` | `Martha Michenfelder` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/134829.1`) (sent_id: `deanon_BFG_TRAIN/134829.1_5`)


Im April 2012 hatte Frau Ute Kirchhoefel (= Beschwerdeführerin, Bf) eine Erklärung über die  Normverbrauchsabgabe (NoVA) und über den Erwerb neuer Fahrzeuge  (Fahrzeugeinzelbesteuerung) zum Fahrzeug MarkeX, FahrgestellNr.

| Predicted | Gold |
|---|---|
| `Ute Kirchhoefel` | `Ute Kirchhoefel` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/135661.1`) (sent_id: `deanon_BFG_TRAIN/135661.1_85`)


Entweder schläft Frau  Reinhold Moellenkamp  bei Herrn A., oder Herr A. bei Frau Reinhold Moellenkamp  in der Schweiz.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/147375.1`) (sent_id: `deanon_BFG_TRAIN/147375.1_4`)


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

**Example 0** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_120`)


Nach ihrer Pensionierung ist Frau Dl Bf von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

**False Positives:**

- `Dl Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_Von`

**F1:** 0.001 | **Precision:** 0.001 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `4031b52e`  
**Description:**
Captures names following 'von' (of/from) in contexts like 'Gutachten von'.

**Content:**
```
(?:von\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+\(|$|\s+\d{4}|\s+Gattin|\s+und|\s+Vermietung|\s+Zimmer)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.001 | 0.001 | 0.001 | 1846 | 2 | 1844 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 1844 | 1634 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/102855.1`) (sent_id: `deanon_BFG_TRAIN/102855.1_69`)


Nach dem klaren Gesetzeswortlaut steht jede Art von Unterhaltsleistung einem Eigenanspruch auf Familienbeihilfe entgegen.

**False Positives:**

- `Unterhaltsleistung einem Eigenanspruch auf Familienbeihilfe entgegen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_83`)


Gemäß § 33 Abs. 2 lit. a FinStrG macht sich einer Abgabenhinterziehung schuldig, wer vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von Umsatzsteuer (Vorauszahlungen oder Gutschriften) bewirkt und dies nicht nur für möglich, sondern für gewiß hält.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_140`)


Wesentliche Tatbestandmerkmale einer Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG sind in subjektiver Hinsicht das Vorliegen von zumindest Eventualvorsatz hinsichtlich der Unterlassung der Abgabe von dem § 21 UStG entsprechenden (rechtzeitigen, richtigen, vollständigen) Voranmeldungen und von Wissentlichkeit in Bezug auf die nicht zeitgerechte Entrichtung der Umsatzsteuervorauszahlungen.

**False Positives:**

- `Wissentlichkeit in Bezug auf die nicht zeitgerechte Entrichtung der Umsatzsteuervorauszahlungen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_143`)


Auch wenn der Beschuldigte angesichts der vorgehaltenen zahlreichen finanzstrafbehördlichen Vorstrafen von sich behauptet, kein Serientäter zu sein, sind dem Beschuldigten aufgrund seiner Tätigkeit als Sanierer seit Jahren die abgabenrechtlichen Pflichten zu den Fälligkeitstagen ebenso bekannt wie die Verpflichtung zur fristgerechten Einreichung von Umsatzsteuervoranmeldungen bzw. die Entrichtung von Umsatzsteuervorauszahlungen.

**False Positives:**

- `Umsatzsteuervoranmeldungen bzw. die Entrichtung von Umsatzsteuervorauszahlungen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_170`)


Angesichts des über Jahre gezeigten steuerunehrlichen Verhaltens darf der Beschuldigte auf die Bestimmung des § 15 Abs. 2 FinStrG aufmerksam gemacht werden, wonach bei Finanzvergehen, die nicht mit einer zwingend zu verhängenden Freiheitsstrafe bedroht sind, auf eine solche nur erkannt werden darf, wenn es ihrer bedarf, um den Täter von weiteren Finanzvergehen abzuhalten oder der Begehung von Finanzvergehen durch andere entgegenzuwirken.

**False Positives:**

- `Finanzvergehen durch andere entgegenzuwirken.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_51`)


Dem Einwand der Beschwerdeführerin, dass bloß ein nicht der Bestandvertragsgebühr unterliegender Vorvertrag vorliege, kann von Seiten des Bundesfinanzgerichtes nicht gefolgt werden.

**False Positives:**

- `Seiten des Bundesfinanzgerichtes nicht gefolgt werden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_104`)


Im Sinne des § 93 Abs. 3 lit a BAO hat ein Bescheid eine Begründung zu enthalten, wenn dieser  von Amts wegen erlassen worden ist.

**False Positives:**

- `Amts wegen erlassen worden ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_105`)


Der angefochtene Bescheid vom 19.3.2014 wurde von Amts wegen erlassen und u.a. damit  7 von 12 Seite 8 von 12

**False Positives:**

- `Amts wegen erlassen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_119`)


Gewerblich oder beruflich ist jede nachhaltige Tätigkeit zur Erzielung von  Einnahmen, auch wenn die Absicht, Gewinn (Überschuss) zu erzielen, fehlt oder eine  Personenvereinigung nur gegenüber ihren Mitgliedern tätig wird.

**False Positives:**

- `Einnahmen, auch wenn die Absicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/128627.1`) (sent_id: `deanon_BFG_TRAIN/128627.1_168`)


Es lag eine nachhaltige, selbständige Tätigkeit zur Erzielung von Einnahmen vor,  auch wenn die Absicht, Gewinn zu erzielen, fehlte.

**False Positives:**

- `Einnahmen vor,  auch wenn die Absicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/128660.1`) (sent_id: `deanon_BFG_TRAIN/128660.1_35`)


Eine Abänderung nach § 295 Abs 1 BAO ist nur jedoch nur zulässig, wenn die Bescheide  betreffend Einkommensteuer für die Streitjahre von Feststellungsbescheiden abzuleiten sind.

**False Positives:**

- `Feststellungsbescheiden abzuleiten sind.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_50`)


Der Transport von Unterlagen zur Schule sei nicht maßgeblich, denn es käme  lediglich auf die mögliche Benutzung von Verkehrsmitteln an.

**False Positives:**

- `Verkehrsmitteln an.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_86`)


Wie der Verwaltungsgerichtshof in seinem Erkenntnis vom 20.1.1999, 98/13/0132, ist der  Mittelpunkt einer Lehrtätigkeit nach der Verkehrsauffassung zweifellos jener Ort, an dem die  Vermittlung von Wissen und technischem Können selbst erfolgt.

**False Positives:**

- `Wissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/128678.1`) (sent_id: `deanon_BFG_TRAIN/128678.1_89`)


Auch wenn für  die Lehrtätigkeit eine Vorbereitungszeit sowie eine Zeit für die Beurteilung vorzulegender  schriftlicher Arbeiten der Schüler erforderlich ist, so stellt die Ausübung dieser Tätigkeit - wie  immer sie auch vorgenommen wird - nicht den Mittelpunkt der Lehrtätigkeit, also die  unmittelbare Vermittlung von Wissen und Können an den Schüler, dar (vgl. VwGH 26.5.1999,  98/13/0138).

**False Positives:**

- `Wissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_19`)


Primäres Ziel von  Behindertenhilfen sei, Behinderten größtmögliche Selbstversorgung zu ermöglichen.

**False Positives:**

- `Behindertenhilfen sei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_31`)


Bei dem gegenständlichen Dusch-WC des Typs Geberit AquaClean 8000plus handelt es sich um  keine nur für Behinderte geeignete Anlage, sondern ist dieses auf Grund seiner Beschaffenheit  für jedermann nutzbar und auch für körperlich nicht einges chränkte Personen von Wert.

**False Positives:**

- `Wert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_69`)


Den vom Bundesfinanzgericht getroffenen Feststellungen zufolge (siehe dazu oben unter Punkt  1) handelt es sich bei dem vom Beschwerdeführer angeschafften Dusch-WC um keine spezifisch  nur für Behinderte geeignete Anlage, sondern ist dieses auf Grund seiner Beschaffenheit für  jedermann nutzbar und auch für körperlich nicht eingeschränkte Personen von Wert.

**False Positives:**

- `Wert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_23`)


Beschwerdeerwägungen:  Dem angefochtenen Bescheid über die Festsetzung von Anspruchszinsen 2007 liegt der im  Einkommensteuerbescheid 2007 des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013  ausgewiesene Differenzbetrag von € 254.913,99 zugrunde.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_24`)


Der Bf. bekämpft den Bescheid  über die Festsetzung von Anspruchszinsen 2007 ausschließlich mit der Begründung, dass der  zugrundeliegende Einkommensteuerbescheid unrichtig wäre bzw. nicht erlassen werden hätte  dürfen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_35`)


Eine  Abänderung von Zinsenbescheiden (anlässlich einer Abänderung bzw. Aufhebung des  Stammabgabenbescheides) ist im Gesetz nicht vorgesehen.

**False Positives:**

- `Zinsenbescheiden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_54`)


Auch das Bundesfinanzgericht kam in freier Beweiswürdigung aufgrund der nunmehr  vorliegenden Aktenlage zum Schluss, dass der Bf im Jahr 2017 keine Einnahmen bzw. Einkünfte  aus gewerblicher bzw. unternehmerischer Tätigkeit zugeflossen sind, die zu einer Festsetzung  von Umsatzsteuer und einer zusätzlichen Einkommensteuerbelastung für die Bf führen  konnten.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_65`)


Dabei sind alle Umstände zu berücksichtigen, die für  die Schätzung von Bedeutung sind.

**False Positives:**

- `Bedeutung sind.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/128734.1`) (sent_id: `deanon_BFG_TRAIN/128734.1_126`)


Bei der Schätzung von Besteuerungsgrundlagen handelt es sich um ein Beweisverfahren, bei  dem der Sachverhalt bezogen auf das im Einzelfall konkret vorliegende sachliche Geschehen  unter Zuhilfenahme mittelbarer Beweise ermittelt wird (VwGH 18.12.1997, 96/16/0143).

**False Positives:**

- `Besteuerungsgrundlagen handelt es sich um ein Beweisverfahren, bei  dem der Sachverhalt bezogen auf das im Einzelfall konkret vorliegende sachliche Geschehen  unter Zuhilfenahme mittelbarer Beweise ermittelt wird` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_39`)


 Rechtliche Erwägungen  Strittig ist die Abzugsfähigkeit von Fortbildungskosten als Werbungskosten.

**False Positives:**

- `Fortbildungskosten als Werbungskosten.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_55`)


Ferner sind idR nicht abzugsfähig Aufwendungen für den Besuch von Kursen  für neuro-linguistisches Programmieren (NLP), da diese im Regelfall Kenntnisse und  Fähigkeiten vermitteln, die auch für den Bereich der privaten Lebensführung von Bedeutung  sind (VwGH 28.5.2008, 2006/15/0237).

**False Positives:**

- `Bedeutung  sind` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/128776.1`) (sent_id: `deanon_BFG_TRAIN/128776.1_70`)


Dass der  Besuch von Seminaren für neurolinguistisches Programmieren (NLP) oder für Schauspiel und  Performance aber auch im Regelfall Kenntnisse und Fertigkeiten vermitteln, die für den Bereich  der privaten Lebensführung von Bedeutung sind, hat der Verwaltungsgerichtshof wiederholt  bejaht (zB VwGH 29.1.2004, 2000/15/0009;

**False Positives:**

- `Bedeutung sind, hat der Verwaltungsgerichtshof wiederholt  bejaht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_2`)


Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Elisabeth Tombült,  Landschacher Gasse 33, 3925 Neumelon, Österreich, vertreten durch Dr. Edelsbacher & Partner Wirtschaftsprüfungs- und Steuer-  beratungsgesellschaft mbH, Ernst-Grein-Straße 14A, 5026 Salzburg, betreffend Beschwerde  vom 17. Juli 2019 gegen den Bescheid des Finanzamtes vom 18. Juni 2019 über die Festsetzung  von Anspruchszinsen (§ 205 BAO) 2016 beschlossen:  Der Vorlageantrag vom 15.06.2020 wird gemäß § 260 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e  BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Elisabeth Tombült`(person)
- `Landschacher Gasse 33, 3925 Neumelon, Österreich`(address)

**Example 28** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_4`)


Begründung  Gleichzeitig mit der Erlassung des Einkommensteuerbescheides 2016 erließ das Finanzamt am  18.06.2019 einen Bescheid über die Festsetzung von Anspruchszinsen 2016 gegenüber der  Beschwerdeführerin (kurz: Bf).

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_5`)


Mit Schriftsatz vom 17.07.2019 brachte die steuerliche Vertretung der Bf Beschwerde gegen  den Einkommensteuerbescheid 2016 und gegen den Bescheid über die Festsetzung von  Anspruchszinsen 2016 ein.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_6`)


Aufgrund des Fehlens der Erklärung, in welchen Punkten der Bescheid angefochten wird, der  Erklärung, welche Änderungen beantragt werden, und einer Begründung erfolgte am  23.07.2019 ein Mängelbehebungsauftrag an die Bf betreffend die Beschwerde gegen den  Bescheid über die Festsetzung von Anspruchszinsen 2016 vom 18.06.2019.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_14`)


Abschließend wurde festgehalten, dass der Bescheid über die Festsetzung von  Anspruchszinsen 2016 vom 18.06.2019 aufgrund der Festsetzung der Einkommensteuer 2016  erlassen worden sei und bei Änderung des Einkommensteuerbescheides 2016 eine  Neuberechnung durch das Finanzamt erforderlich sei.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_15`)


Mit Beschwerdevorentscheidung vom 19.08.2019 wies das Finanzamt die Beschwerde gegen  den Bescheid über die Festsetzung von Anspruchszinsen 2016 vom 18.06.2019 ab, wogegen die  steuerliche Vertretung der Bf mit Schriftsatz vom 27.08.2019 einen Vorlageantrag einbrachte.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_16`)


Mit dem unangefochten gebliebenen Beschluss des Bundesfinanzgerichtes vom 25.09.2019,  RV/6100504/2019, wurde ausgesprochen, dass die Beschwerde vom 17.07.2019 gegen den  Bescheid über die Festsetzung von Anspruchszinsen 2016 vom 18.06.2019 gemäß § 85 Abs. 2  BAO als zurückgenommen gilt und das Beschwerdeverfahren eingestellt wird.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_29`)


Am 18.03.2020 erging aufgrund der abändernden Beschwerdevorentscheidung vom  18.03.2020 betreffend die Einkommensteuer 2016 ein neuer Bescheid über die Festsetzung  von Anspruchszinsen 2016.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_30`)


Mit zwei Berichten vom 25.06.2020 legte das Finanzamt diese Vorlageanträge dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Zurückweisung der Beschwerde  gegen den Bescheid über die Festsetzung von Anspruchszinsen 2016.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_39`)


Beschwerde gegen den  Bescheid über die Festsetzung von Anspruchszinsen 2016 vom 18.06.2019 eingebracht wurde.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_42`)


Aus diesem Grund kann es sich bei dem Vorlageantrag vom 15.06.2020 - soweit er den  Bescheid über die Festsetzung von Anspruchszinsen vom 18.06.2019 betrifft – nur um einen  Antrag auf Entscheidung über die Beschwerde vom 17.07.2019 betreffend den Bescheid über  die Festsetzung von Anspruchszinsen 2016 vom 19.08.2019 durch das Bundesfinanzgericht  handeln.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_TRAIN/128810.1`) (sent_id: `deanon_BFG_TRAIN/128810.1_43`)


Die Beschwerde vom 17.07.2019 betreffend den Bescheid über die Festsetzung von  Anspruchszinsen 2016, welche mit Beschwerdevorentscheidung vom 19.08.2019 abgewiesen  wurde, war allerdings – aufgrund des Vorlageantrags vom 27.08.2019 - bereits Gegenstand des  rechtskräftigen Beschlusses des Bundesfinanzgerichtes vom 25.09.2019, RV/6100504/2019.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_98`)


Zu Spruchpunkt I. (Abweisung/Abänderung/Stattgabe)  Gemäß § 224 Abs. 1 BAO werden die in Abgabenvorschriften geregelten persönlichen  Haftungen durch Erlassung von Haftungsbescheiden geltend gemacht.

**False Positives:**

- `Haftungsbescheiden geltend gemacht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_185`)


Das BFG stimmt der  Einschränkung der Haftung auf jene Abgaben, die im Zeitraum seiner Geschäftsführertätigkeit  von November 2010 bis April 2011 angefallen sind, zu, da durchaus nachvollziehbar ist, dass  der BF mit der Übernahme der Geschäftsführertätigkeit „geködert“ worden ist und die  tatsächlichen Machthaber damit das Risiko aus den Malversationen auf ihn abwälzen wollten.

**False Positives:**

- `November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_187`)


Dabei sind trotz der beschriebenen  wirtschaftlichen Situation des BF auch generalpräventive Gesichtspunkte von Bedeutung.

**False Positives:**

- `Bedeutung.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_TRAIN/128877.1`) (sent_id: `deanon_BFG_TRAIN/128877.1_19`)


Sachverhalt  Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:   Dem BF wurde am 22.10.2019 in die Databox von FinanzOnline der Einkommensteuerbescheid  2018 zugestellt.

**False Positives:**

- `FinanzOnline der Einkommensteuerbescheid ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_37`)


Dies umfasst beispielsweise gesellige Zusammenkünfte aller  Art, Bewirtung von Arbeitskollegen sowie Geschenke an Kunden, nicht in einer Bewirtung  bestehende Aufmerksamkeiten z.B. von Wein, Einladungen, kleinere Sachgeschenke,  Zuwendung zu Anlässen.

**False Positives:**

- `Arbeitskollegen sowie Geschenke an Kunden, nicht in einer Bewirtung  bestehende Aufmerksamkeiten z.B. von Wein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_46`)


Pauschalierungsmöglichkeiten  von Werbungskosten finden sich unter diesen Bestimmungen nicht.

**False Positives:**

- `Werbungskosten finden sich unter diesen Bestimmungen nicht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_56`)


Die gegenständliche Entscheidung basiert sowohl hinsichtlich der Frage der Abzugsfähigkeit  von Einladungen bzw. Geschenken an MitarbeiterInnen und Geschäftspartner als auch  hinsichtlich der Frage der Abzugsfähigkeit pauschaler Werbungskosten für Funktionäre auf den  unter Punkt 2.1. angeführten gesetzlichen und verordnungsmäßigen Grundlagen und ergibt  sich direkt aus diesen.

**False Positives:**

- `Einladungen bzw. Geschenken an MitarbeiterInnen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_26`)


Das Finanzamt legte die Beschwerden ohne Erlassung von Beschwerdevorentscheidungen an  das Bundesfinanzgericht zur Entscheidung vor und begehrte die Abweisung der Beschwerden.

**False Positives:**

- `Beschwerdevorentscheidungen an  das Bundesfinanzgericht zur Entscheidung vor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_15`)


Auf Grund der Befundlage ergeben sich massive Einschränkungen bei Grundnahrungsmitteln  (Weizen, Dinkel, Kuhmilch, allen Milchprodukten - auch von Ziege oder Schaf, Fructose- und  Sorbit haltige Nahrungsmittel) sowie bei ca. zehn weiteren einzelnen Nahrungsmitteln, die sie  speziell meiden müsse.

**False Positives:**

- `Ziege oder Schaf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_17`)


Jede einzelne Entscheidung beim Kauf von Lebensmitteln sei entweder im Hinblick auf  verträgliche teure Produkte im Gegensatz zu unverträglichen billigen zu treffen (z.B. vielfach  teurer Quinoa anstatt von billigem Weizenmehl, teure Kokosmilchprodukte anstatt von billigen  Milchprodukten, teures Backwerk an Stelle von billigstem selbst gebackenen Brot) oder (auf  Anraten ihres Arztes) auf Grund der medizinischen Wirksamkeit bzw. erwiesenen Schädlichkeit  von Nahrungsmitteln (z.B. teures Hirsch-, Reh- oder Welsﬂeisch = Medizin für den Magen  anstatt von billigem Schweinefleisch = entzündungsfördernd).

**False Positives:**

- `Nahrungsmitteln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_85`)


Diesem Schreiben wurde eine einseitige Liste angeschlossen, die eine medizinische Wirkung  von Weinessig, Wein, Hirschfleisch, Fenchel, Rehfleisch, Sonnenblumenöl kaltgepresst,  Kastanien Bio, Kichererbsen, Honig und Fenchelkörner/Galant sowie deren Zubereitung  beschreibt.

**False Positives:**

- `Weinessig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_TRAIN/128943.1`) (sent_id: `deanon_BFG_TRAIN/128943.1_187`)


Es reicht dazu nicht, dass sie bloß der Vorbeugung von  Krankheiten dienen.

**False Positives:**

- `Krankheiten dienen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_58`)


Die in Abgabenvorschriften geregelten persönlichen Haftungen werden durch Erlassung von  Haftungsbescheiden geltend gemacht.

**False Positives:**

- `Haftungsbescheiden geltend gemacht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_64`)


Der Vertreter haftet nicht für sämtliche Abgabenschulden des Vertretenen in voller Höhe,  sondern - was sich aus dem Wort „insoweit“ in § 9 BAO eindeutig ergibt - nur in dem Umfang,  in dem eine Kausalität zwischen der (schuldhaften) Pflichtverletzung des Vertreters und dem  Entgang von Abgaben besteht (VwGH 22.9.1999, 96/15/0049).

**False Positives:**

- `Abgaben besteht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_TRAIN/129035.1`) (sent_id: `deanon_BFG_TRAIN/129035.1_6`)


Gegen diesen Bescheid erhob der Bf. ebenfalls elektronisch per FinanzOnline rechtzeitig eine  Beschwerde, die sich gegen die Berechnung von Reisekosten richtete.

**False Positives:**

- `Reisekosten richtete.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_TRAIN/129035.1`) (sent_id: `deanon_BFG_TRAIN/129035.1_23`)


Im Zweifel hat die Behörde die Tatsache und  den Zeitpunkt des Einlangens von Amts wegen festzustellen (§ 98 Abs. 2 BAO).

**False Positives:**

- `Amts wegen festzustellen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_22`)


Meine Tätigkeit bestand aus  Zusammenräumen von Baustellen.

**False Positives:**

- `Baustellen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_34`)


Im Prüfungszeitraum 2010 - 2012 waren Hr. [B] und Hr. [A] mit der Durchführung von  Reinigungsarbeiten und mit Abladearbeiten von LKW`s und mit dem Verbringen von  Materialen auf der Baustelle mittels mündlich abgeschlossenen Werkvertrag  beschäftigt.

**False Positives:**

- `Reinigungsarbeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_38`)


Sie zeigt sich u.a. in der  Vorgabe von Arbeitszeit, Arbeitsort und Arbeitsmittel durch den Auftraggeber sowie die  unmittelbare Einbindung der Tätigkeit in betriebliche Abläufe des Arbeitgebers.

**False Positives:**

- `Arbeitszeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_109`)


In  Zusammenfassung dieser Überlegungen zeigt sich eine nahezu ausschließliche  Bestätigung der für das Vorliegen von Werkvertragen sprechenden Argumente.

**False Positives:**

- `Werkvertragen sprechenden Argumente.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_119`)


Somit waren die grundlegenden, formalen Voraussetzungen für die Erbringung  von Werkleistungen gegeben.

**False Positives:**

- `Werkleistungen gegeben.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_122`)


Schließlich ergab sich das Erfordernis zur  Ausführung von Reinigungsarbeiten und der Verbringung von Baumaterial.

**False Positives:**

- `Reinigungsarbeiten` — no gold match — likely missing annotation
- `Baumaterial.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 61** (doc_id: `deanon_BFG_TRAIN/129077.1`) (sent_id: `deanon_BFG_TRAIN/129077.1_138`)


Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:  Herr [B] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Aufräumen von Baustellen, bestehend im Zusammentragen und  eigenverantwortlichem Trennen von Bauschutt und -abfällen entsprechend der  Wiederverwertbarkeit‚ einschließlich des Bereitstellens zum Abtransport sowie im  Reinigen von Baumaschinen und Bauwerkzeugen durch Beseitigen von Rückständen  mittels einfacher mechanischer Methoden, wie Abkratzen, Abspachteln und dergleichen  und nachfolgendem Abspritzen mit Wasser, unter Verwendung ausschließlich eigener  Arbeitsgeräte sowie unter Ausschluss der den Denkmal-, Fassaden- und  Gebäudereinigern vorbehaltenen Tätigkeiten einer Grund- oder Bauschlussreinigung“  Herr [A] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Heben, Senken und Befördern von Lasten mittels Einsatzes von mechanischen oder  maschinellen Einrichtungen unter Ausschluss der Beförderung mittels Kraftfahrzeugen“  Herr [B] und Herr [A] führten im Beschwerdezeitraum Baustellenarbeiten entsprechend ihren  Gewerbeberechtigungen für den Beschwerdeführer aus.

**False Positives:**

- `Baustellen, bestehend im Zusammentragen` — no gold match — likely missing annotation
- `Bauschutt` — no gold match — likely missing annotation
- `Baumaschinen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 62** (doc_id: `deanon_BFG_TRAIN/129101.1`) (sent_id: `deanon_BFG_TRAIN/129101.1_56`)


Die in Abgabenvorschriften geregelten persönlichen Haftungen werden durch Erlassung von  Haftungsbescheiden geltend gemacht.

**False Positives:**

- `Haftungsbescheiden geltend gemacht.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_TRAIN/129101.1`) (sent_id: `deanon_BFG_TRAIN/129101.1_63`)


Der Vertreter haftet nicht für sämtliche Abgabenschulden des Vertretenen in voller Höhe,  sondern - was sich aus dem Wort „insoweit“ in § 9 BAO eindeutig ergibt - nur in dem Umfang,  in dem eine Kausalität zwischen der (schuldhaften) Pflichtverletzung des Vertreters und dem  Entgang von Abgaben besteht (VwGH 22.09.1999, 96/15/0049).

**False Positives:**

- `Abgaben besteht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_TRAIN/129101.1`) (sent_id: `deanon_BFG_TRAIN/129101.1_81`)


Sie  beschränkt sich lediglich mit dem Hinweis auf ein Erkenntnis des Bundesfinanzgerichts, worin  nicht sie, sondern ihr Ehemann bzw. ihr Sohn wegen des Verdachtes der Hinterziehung von  Umsatzsteuervorauszahlungen und Nichtabfuhr von Lohnabgaben verantwortlich gemacht  wurde bzw. keine finanzstrafrechtliche Bestrafung erfolgte, hinzuweisen.

**False Positives:**

- `Umsatzsteuervorauszahlungen` — no gold match — likely missing annotation
- `Lohnabgaben verantwortlich gemacht  wurde bzw. keine finanzstrafrechtliche Bestrafung erfolgte, hinzuweisen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 65** (doc_id: `deanon_BFG_TRAIN/129103.1`) (sent_id: `deanon_BFG_TRAIN/129103.1_72`)


Zwar sind Spruch und Begründung zusammen zu  berücksichtigen, die Begründung vermag aber jedenfalls den Spruch des Bescheides nicht zu  ändern, sofern dieser frei von Zweifeln ist.

**False Positives:**

- `Zweifeln ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_TRAIN/129137.1`) (sent_id: `deanon_BFG_TRAIN/129137.1_40`)


(1a) Bestehen begründete Zweifel, ob die Voraussetzungen gemäß Abs. 1 vorliegen, so ist dies  auf Antrag des Liegenschaftseigentümers oder von Amts wegen mit Bescheid festzustellen.

**False Positives:**

- `Amts wegen mit Bescheid festzustellen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_30`)


Anbei übermittle ich Ihnen eine Kopie der durch den  Dienstnehmer AB unterfertigten Untersagung der privaten Nutzung von Firmenfahrzeugen.

**False Positives:**

- `Firmenfahrzeugen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_83`)


dies gilt sinngemäß  a) für bei Veranlagung durch Anrechnung von Vorauszahlungen entstehende Gutschriften und  b) für Nachforderungszinsen (§ 205), soweit nachträglich dieselbe Abgabe betreffende  Gutschriftszinsen festgesetzt werden.

**False Positives:**

- `Vorauszahlungen entstehende Gutschriften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_107`)


Sollte sich der Umfang der Inanspruchnahme des Beschwerdeführers infolge Erledigung der  gegen die Haftungsbescheide gerichteten Beschwerde ändern, sieht § 217 Abs 8 BAO eine  nachträgliche Herabsetzung des hier in Rede stehenden Säumniszuschlages vor, die von Amts  wegen zu erfolgen hat (vgl. VwGH 24.3.2015, 2012/15/0206).

**False Positives:**

- `Amts  wegen zu erfolgen hat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_42`)


Nach Ansicht des Finanzamtes sei das  Fahrzeug „Polaris Ranger Crew" vielmehr vorwiegend zur Beförderung von Personen bestimmt,  was auch dem optischen Eindruck der (für den öffentlichen Straßenverkehr straßentauglichen)  Fahrzeuge bzw. der Verkehrsauffassung entspreche.

**False Positives:**

- `Personen bestimmt,  was auch dem optischen Eindruck der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_44`)


Des  Weiteren ändere das Anbringen von Vorrichtungen und Geräten für einen speziellen  Arbeitseinsatz (z.B. Schneepflug) nach der Verwaltungspraxis nichts an der steuerrechtlichen  Einstufung des Fahrzeuges selbst (RZ 1934 UStR).

**False Positives:**

- `Vorrichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_85`)


Gem. § 3 Abs. 1 Z 5 Kraftfahrgesetz ist ein Personenkraftwagen der nach seiner Bauart und  Ausrüstung ausschließlich oder vorwiegend zur Beförderung von Personen bestimmt ist und  außer dem Lenkplatz für nicht mehr als acht Personen Plätze aufweist.

**False Positives:**

- `Personen bestimmt ist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_107`)


In der mündlichen Verhandlung vom 10.6.2020 führten die Parteien des Verfahrens ergänzend  aus:  Frau Mag. A führte für die Bf aus, sie habe Rücksprache mit dem Hersteller des  gegenständlichen Fahrzeuges gehalten und dabei in Erfahrung bringen können, dass die  Fahrzeuge von Seiten des Finanzamtes in Vorarlberg als Zugmaschinen oder Leichttraktoren  eingestuft werden.

**False Positives:**

- `Seiten des Finanzamtes in Vorarlberg als Zugmaschinen oder Leichttraktoren  eingestuft werden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_113`)


C führte dazu seitens des Finanzamtes aus, dass der optische Eindruck und die  Verkehrsauffassung für die Einstufung eines solchen Fahrzeuges von Bedeutung seien.

**False Positives:**

- `Bedeutung seien.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_159`)


Nicht als für das Unternehmen ausgeführt gelten gemäß § 12 Abs. 2 Z 2 lit. b UStG 1994  Lieferungen, sonstige Leistungen oder Einfuhren, die im Zusammenhang mit der Anschaffung  (Herstellung), Miete oder dem Betrieb von Personenkraftwagen, Kombinationskraftwagen  oder Krafträdern stehen, ausgenommen Fahrschulkraftfahrzeuge, Vorführkraftfahrzeuge und  Kraftfahrzeuge, die ausschließlich zur gewerblichen Weiterveräußerung bestimmt sind, sowie  Kraftfahrzeuge, die zu mindestens 80% dem Zweck der gewerblichen Personenbeförderung  oder der gewerblichen Vermietung dienen.

**False Positives:**

- `Personenkraftwagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_162`)


Die dazu ergangene, für die Beschwerdejahre maßgebende Verordnung des Bundesministers  für Finanzen über die steuerliche Einstufung von Fahrzeugen als Kleinlastkraftwagen und  Kleinbusse, BGBl. II Nr. 193/2002 lautet auszugsweise:  § 1.

**False Positives:**

- `Fahrzeugen als Kleinlastkraftwagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_189`)


Werkseitig ist der geländegängige Polaris Ranger 800 Crew sowohl zur Personen- und  Lastenbeförderung als auch zum Ziehen und Schieben von Lasten konzipiert.

**False Positives:**

- `Lasten konzipiert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_200`)


Dabei ist das Anbringen  von Vorrichtungen und Geräten für einen speziellen Arbeitseinsatz, wie Seilwinde oder  Anhängervorrichtung, unbeachtlich.

**False Positives:**

- `Vorrichtungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_208`)


Im Hinblick auf die beim Polaris Ranger vorhandene Ladepritsche stellt sich die Frage, ob dieser  nach der Verordnung über die steuerliche Einstufung von Fahrzeugen als Kleinlastkraftwagen  und Kleinbusse nicht als Personen- oder Kombinationskraftwagen anzusehen ist.

**False Positives:**

- `Fahrzeugen als Kleinlastkraftwagen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_209`)


In der Verordnung über die steuerliche Einstufung von Fahrzeugen als Kleinlastkraftwagen und  Kleinbusse BGBl. II Nr. 193/2002 wird in § 4 normiert, dass Pritschenwagen unter den im § 2  angeführten allgemeinen Voraussetzungen nicht als Personen- oder Kombinationskraftwagen  anzusehen sind.

**False Positives:**

- `Fahrzeugen als Kleinlastkraftwagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_85`)


Mit Schreiben vom 03. Dezember 2019 wurden die Beträge von Basispacht, Umsatzpacht,  Betriebskosten und Franchisegebühr mitgeteilt.

**False Positives:**

- `Basispacht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_97`)


Die zentrale  Leistungspflicht des Franchisenehmers aus dem Franchisevertrag sei als Entgelt für die  Überlassung von Markenrechten, Know-how und Businesskonzept des Franchisegebers an die  Franchisenehmer zu qualifizieren.

**False Positives:**

- `Markenrechten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_190`)


Der Franchise-Vertrag ist ein Dauerschuldverhältnis, wodurch der Franchisegeber dem  Franchisenehmer gegen Entgelt das Recht einräumt, bestimmte Waren und/oder  Dienstleistungen unter Verwendung von Name, Marke, Ausstattung usw.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_196`)


Bei einem echten  Franchisevertrag treten die Bestandvertragselemente in den Hintergrund und beziehen sich  bestenfalls auf die Nutzung des Knowhow von Marken und Warenzeichen.

**False Positives:**

- `Marken` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_206`)


Wenn aber bei echten  Franchise-Verträgen überhaupt Bestandvertragselemente enthalten sind, so werden sie sich  bestenfalls auf die Nutzung von Know-how von Marke und Warenzeichen und dergleichen  mehr beziehen, nicht aber wie im gegenständlichen Fall auf die Pacht eines ganzen  Unternehmens.

**False Positives:**

- `Marke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_220`)


Dem Beschwerdevorbringen, die Franchisegebühr sei als Entgelt für die Überlassung von  Markenrechten, Know-how und Businesskonzept des Franchisegebers an die Franchisenehmer  zu qualifizieren und weise keinerlei Konnex zur Einräumung der Nutzungsrechte an den  Pachträumlichkeiten auf, wird entgegengehalten, dass nach dem schriftlich festgelegten  Urkundeninhalt die Verpachtung gemäß Art. 3 des Pachtvertrages ausschließlich zu dem Zweck  erfolgte, dem Pächter Räumlichkeiten (samt Parkplatzflächen) zum Betrieb eines Firmen  Restaurants zur Verfügung zu stellen.

**False Positives:**

- `Markenrechten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_TRAIN/129205.1`) (sent_id: `deanon_BFG_TRAIN/129205.1_80`)


Im gegenständlichen Fall war der Bf im Kalenderjahr 2018 nicht Bezieher und  Anspruchsberechtigter von Familienbeihilfe.

**False Positives:**

- `Familienbeihilfe.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_86`)


Anhand dieser Unterlagen habe man ausschließen können, dass es sich um  deutsche Fahrzeuge von Privatpersonen handle und somit sei die Differenzbesteuerung beim  Wiederverkauf nicht anwendbar gewesen.

**False Positives:**

- `Privatpersonen handle` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_188`)


Wenn die BP der Meinung sei, dass die MH in  Österreich die Differenzbesteuerung nicht hätte anwenden dürfen, dann müsse sie  korrekterweise diese Umsätze bei der MH in Österreich der Besteuerung unterziehen, denn die  Fahrzeuge seien ja von MH verkauft worden.

**False Positives:**

- `MH verkauft worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_199`)


Erst bei einem Verkauf durch den Bf. finde auch der  Verkauf von MH an den Bf. statt.

**False Positives:**

- `MH an den Bf. statt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_233`)


Es werde noch einmal darauf hingewiesen, dass es falsch sei, dass eine Lieferung von  Fahrzeugen von der MH an den Bf. stattgefunden habe und daher auch keine Vornahme einer  Erwerbsbesteuerung durch den Bf. möglich gewesen sei.

**False Positives:**

- `Fahrzeugen von der MH an den Bf. stattgefunden habe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_345`)


Weil ich wollte immer wissen …. weil  Ich hab schon gesehen, dass Leasingbesitzer … na, dass er von Privaten gekauft hat und von  dem gekauft hat … ok … wenn sie mir das bestätigen, ist mir das egal in dem Sinne habe ich  ihm gesagt.

**False Positives:**

- `Privaten gekauft hat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_467`)


SB: Ich habe da eine alte Rechnung von 2009, von Firma MH an Firma Bf.

**False Positives:**

- `Firma MH an Firma Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_522`)


Verkauf von Privaten, Verkauf von dem …..

**False Positives:**

- `Privaten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_582`)


Das Bundesfinanzgericht geht davon aus, dass der Bf. Fahrzeuge aus Deutschland von MH  angekauft und in Österreich verkauft hat.

**False Positives:**

- `MH  angekauft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_585`)


Dr Bf. gibt in der mündlichen Verhandlung selbst an, von MH  gekauft und im eigenen Namen weiterverkauft zu haben.

**False Positives:**

- `MH  gekauft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_595`)


In einem Dekret des Staatsrates sind die spezifischen Verfahren für die Anwendung des ersten  Absatzes festgelegt, wenn der Vertreter in einem Land niedergelassen ist, in dem es kein  Rechtsinstrument für die gegenseitige Unterstützung mit einem ähnlichen Umfang wie in der  Richtlinie gibt (2010/24 EU des Rates vom 16. März 2010 über die gegenseitige Unterstützung  bei der Beitreibung von Schulden in Bezug auf Steuern, Abgaben und andere Maßnahmen sowie  durch die Verordnung (EU) Nr. 904/2010 des Rates vom 7. Oktober 2010 über die  administrative Zusammenarbeit und die Betrugsbekämpfung im Bereich der Mehrwertsteuer).

**False Positives:**

- `Schulden in Bezug auf Steuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_634`)


b. (1) Gemäß Artikel 289 I 1 CGI in seiner seit 1. Juli 2003 gültigen Fassung muss jeder  Steuerpflichtige dafür sorgen, dass von ihm selbst – oder in seinem Namen und für seine  Rechnung durch seinen Kunden oder einen Dritten – für folgende Umsätze eine Rechnung  ausgestellt wird: Lieferung von Gegenständen oder Erbringung von Dienstleistungen an einen  anderen Steuerpflichtigen oder eine nichtsteuerpflichtige juristische Person.

**False Positives:**

- `Dienstleistungen an einen  anderen Steuerpflichtigen oder eine nichtsteuerpflichtige juristische Person.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_661`)


Schutz von Treu und Glauben berufen (Melhart/Tumpel, § 24 Rz 38 mit Verweis auf  Ruppe/Achatz, § 24 Rz 14).

**False Positives:**

- `Treu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_Bei`

**F1:** 0.001 | **Precision:** 0.002 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `6a54d072`  
**Description:**
Captures names following 'bei' (at/with) in contexts like 'bei der Hugo Buring'.

**Content:**
```
(?:bei\s+(?:der|die|den)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.)?)?)(?=,\s+[A-Z]|\s+\(|$|\s+\d{4}|\s+Gattin|\s+und)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.002 | 0.001 | 0.001 | 447 | 1 | 446 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 446 | 1635 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/125056.1`) (sent_id: `deanon_BFG_TRAIN/125056.1_162`)


Seite 13 von 15 Bedenkt man, dass der Verwaltungsgerichtshof bei drei einschlägigen Vorstrafen eine Geldstrafe im Ausmaß von 45 % der möglichen Höchststrafe für zulässig erklärt hat (VwGH 8.2.2007, 2006/15/0293) oder bei zwei Vorstrafen wegen Abgabenhinterziehung bei geringem Einkommen des Bestraften eine Geldstrafe von 34% des Strafrahmens und eine zusätzliche primäre Freiheitsstrafe von zwei Wochen als angemessen erklärt (VwGH 25.6.1998, 96/15/0041), so kann man erkennen, wie moderat die Bemessung der Geldstrafe bei den Vorstrafen des Beschuldigten ausgefallen ist.

**False Positives:**

- `Vorstrafen des Beschuldigten ausgefallen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/128704.1`) (sent_id: `deanon_BFG_TRAIN/128704.1_66`)


Ausgaben für den Erwerb eines Wirtschaftsgutes sind nach ständiger Rechtsprechung des  Verwaltungsgerichtshofes in der Regel von einer Berücksichtigung als außergewöhn liche  Belastung ausgeschlossen, da bei der Ans chaffung eines Wirtschaftsgutes in der Regel ein  entsprechender Gegenwert erlangt wird (vgl zB VwGH 27.6.2018, Ra 2017/15/0006, mwN).

**False Positives:**

- `Ans chaffung eines Wirtschaftsgutes in der Regel ein  entsprechender Gegenwert erlangt wird` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_13`)


Bedauerlicher Weise wurde weder innerhalb des Bundesfinanzgerichtes eine Information über  die bereits erfolgte Entscheidung im zugrundeliegenden Abgabenverfahren noch von der  belangten Behörde eine Information über die Erlassung eines Gutschriftszinsenbescheides für  dieses Beschwerdeverfahren weitergeleitet, sodass es zu dieser weiteren – wenn auch  kurzfristigen – Verzögerung bei der Entscheidung gekommen ist.

**False Positives:**

- `Entscheidung gekommen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_TRAIN/128731.1`) (sent_id: `deanon_BFG_TRAIN/128731.1_65`)


Eine unzumutbare Verlegung des Familienwohnsitzes zum Dienstort liegt jedoch bei Einkünften  der Ehefrau nur vor, wenn es sich diesfalls um steuerlich relevante Erwerbseinkünfte handelt,  die bei der Verlegung des Familienwohnsitzes verloren gingen (vgl VwGH 8. Februar 2007,  2004/15/0102 und VwGH 17. Februar 1999, 95/14/0059).

**False Positives:**

- `Verlegung des Familienwohnsitzes verloren gingen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_62`)


Der BF war im Zeitraum 09/2008 - 04/2011 als Lkw-Fahrer bei der GmbH (in der Folge GmbH)  beschäftigt.

**False Positives:**

- `GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_TRAIN/128871.1`) (sent_id: `deanon_BFG_TRAIN/128871.1_130`)


Die verfahrensgegenständlichen Abgaben waren – wie oben dargestellt - bei der GmbH nicht  einbringlich, da das Insolvenzverfahren im Oktober 2011 mangels eines die Kosten des  Verfahrens deckenden Vermögens nicht eröffnet wurde.

**False Positives:**

- `GmbH nicht  einbringlich, da das Insolvenzverfahren im Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_8`)


Nach  einem Ergänzungsersuchen des FA in dem der BF seine Werbungskosten aufgliederte,  veranlagte das FA den BF mit Bescheid vom 03.06.2016 zur Einkommensteuer 2014, kürzte  dabei die Werbungskosten und setzte die Ausgaben bei den Funktionsgebühren nicht an.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_TRAIN/128910.1`) (sent_id: `deanon_BFG_TRAIN/128910.1_22`)


Dies umfasse auch öffentlich-rechtliche Rechtsträger und  somit auch die beiden Funktionen bei der Arbeiterkammer und der Gebietskrankenkasse.

**False Positives:**

- `Arbeiterkammer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_16`)


4. Die genannten Beträge sind bei der GmbH als uneinbringlich anzusehen.

**False Positives:**

- `GmbH als uneinbringlich anzusehen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_TRAIN/128966.1`) (sent_id: `deanon_BFG_TRAIN/128966.1_25`)


Im Fall  der Nichterbringung dieser Nachweise muss das Finanzamt davon ausgehen, dass Sie die Ihnen  obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwalteten Mitteln zu  entrichten, schuldhaft verletzt haben, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH ist.

**False Positives:**

- `GmbH ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/129101.1`) (sent_id: `deanon_BFG_TRAIN/129101.1_19`)


Eventuell zu erhaltende Quoten seien bei der Auflistung noch nicht  abgezogen worden.

**False Positives:**

- `Auflistung noch nicht  abgezogen worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/129137.1`) (sent_id: `deanon_BFG_TRAIN/129137.1_43`)


2. Liegenschaften, deren Benützung auf Grund der Notwendigkeit umfangreicher Bauarbeiten  (zB Generalsanierungen) unmöglich ist, sodass kein Müll anfallen kann, wobei die Ausnahme  auf die Dauer der Unbenutzbarkeit zu befristen ist.

**False Positives:**

- `Ausnahme  auf die Dauer der Unbenutzbarkeit zu befristen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/129157.1`) (sent_id: `deanon_BFG_TRAIN/129157.1_26`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes komme es bei der Beurteilung  darauf an, zu welcher Verwendung das Fahrzeug werkseitig bestimmt sei und entscheidend sei  die wirtschaftliche Zweckbestimmung des Fahrzeuges nach seiner werkseitigen Bauart und  Beschaffenheit (VwGH 82/14/0005).

**False Positives:**

- `Beurteilung  darauf an, zu welcher Verwendung das Fahrzeug werkseitig bestimmt sei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/129187.1`) (sent_id: `deanon_BFG_TRAIN/129187.1_191`)


sowie der  gewerblichen und technischen Erfahrungen des Franchisegebers und unter Beachtung des von  diesem entwickelten Organisations- und Werbesystems zu vertreiben, wobei der  Franchisegeber Beistand, Rat und Schulung in technischer und verkaufstechnischer Hinsicht  gewährt und eine Kontrolle über die Geschäftstätigkeit des Franchisenehmers ausübt.

**False Positives:**

- `Franchisegeber Beistand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_15`)


(2) Bereits in der Vorprüfung (BP 2006 bis 2009, Nachschauzeitraum bis 7/2010) sei die  Anwendung der Differenzbesteuerung bei den Fahrzeugen der Firma MH hinterfragt worden.

**False Positives:**

- `Fahrzeugen der Firma MH hinterfragt worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_128`)


Zur Liste der 21 Fahrzeuge aus 2009 und 2010 wird ausgeführt:  „Hiermit bestätige ich, dass die 21 oben angeführten Fahrzeuge unter Anwendung der  Differenzbesteuerung angeschafft worden sind, weil diese   - entweder von einer Person erworben wurden, die nicht zum Ausweis einer Vorsteuer  berechtigt ist  - oder von einem anderen Wiederverkäufer, der seinerseits bei der Lieferung die  Differenzbesteuerung angewendet hat.

**False Positives:**

- `Lieferung die  Differenzbesteuerung angewendet hat.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_552`)


Stb: Die Außenprüfung hat damals festgestellt, dass bei der Firma MH etwas nicht in Ordnung  war.

**False Positives:**

- `Firma MH etwas nicht in Ordnung  war.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_595`)


In einem Dekret des Staatsrates sind die spezifischen Verfahren für die Anwendung des ersten  Absatzes festgelegt, wenn der Vertreter in einem Land niedergelassen ist, in dem es kein  Rechtsinstrument für die gegenseitige Unterstützung mit einem ähnlichen Umfang wie in der  Richtlinie gibt (2010/24 EU des Rates vom 16. März 2010 über die gegenseitige Unterstützung  bei der Beitreibung von Schulden in Bezug auf Steuern, Abgaben und andere Maßnahmen sowie  durch die Verordnung (EU) Nr. 904/2010 des Rates vom 7. Oktober 2010 über die  administrative Zusammenarbeit und die Betrugsbekämpfung im Bereich der Mehrwertsteuer).

**False Positives:**

- `Beitreibung von Schulden in Bezug auf Steuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_627`)


Bei Weiterverkauf kann der österreichische KFZ-Händler die  Differenzbesteuerung anwenden, wenn bei der Lieferung an ihn keine USt geschuldet oder  erhoben worden ist.

**False Positives:**

- `Lieferung an ihn keine USt geschuldet oder  erhoben worden ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_674`)


Zunächst ist festzuhalten, dass schon anlässlich der vorangegangenen BP (Prüfungsauftrag  19.10.2010, Prüfungsjahre 2006 bis 2008, in der Folge ausgedehnt auf 2009) die  beschwerdegegenständliche Thematik angesprochen wurde (Einkauf Fahrzeuge bei MH ab  2009) und damit bereits zu diesem Zeitpunkt bekannt war:   (1) So wird in Pkt vier der Niederschrift vom 1. März 2012 (Bericht vom 20. März 2012 zu den  Veranlagungsjahren 2006 bis 2009 und Nachschau 1-7/2010) ausgeführt, „im Jahr 2009 und  2010 wurden vom Bf. Fahrzeuge bei der Firma MH ohne Angabe der eigenen UID angekauft.

**False Positives:**

- `Firma MH ohne Angabe der eigenen UID angekauft.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_TRAIN/129233.1`) (sent_id: `deanon_BFG_TRAIN/129233.1_703`)


In der Besprechung vom 6. Dezember 2010 habe der Bf. bestätigt,  dass es sich bei den Fahrzeugen um endbesteuerte Fahrzeuge handle und zugesagt, sich von  MH Bestätigungen für die einzelnen Differenzbesteuerungen zu besorgen.

**False Positives:**

- `Fahrzeugen um endbesteuerte Fahrzeuge handle` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_TRAIN/129250.1`) (sent_id: `deanon_BFG_TRAIN/129250.1_6`)


Durch die zuständige Abgabenbehörde wurde bei der Bf., beginnend im Jahr 2009, eine  Außenprüfung (AP) durchgeführt, die neben Körperschaft- und Umsatzsteuer für das Jahr 2008  auch die Kapitalertragsteuer zum Prüfungsgegenstand hatte.

**False Positives:**

- `Bf., beginnend im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_9`)


Im Zuge einer Außenprüfung bei der Bf. wurde festgestellt, dass im Jahr 2013  Rechtsanwaltskosten in Höhe von 30.158,94 Euro plus 20% Umsatzsteuer in Höhe von  6.031,79 Euro auf dem Konto 775 "Rechtsberatung" verbucht waren.

**False Positives:**

- `Bf. wurde festgestellt, dass im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_90`)


Die betriebliche Veranlassung von Aufwendungen ist grundsätzlich von Amts wegen  festzustellen, wobei den Steuerpflichtigen eine Mitwirkungspflicht trifft.

**False Positives:**

- `Steuerpflichtigen eine Mitwirkungspflicht trifft.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_164`)


Die betriebliche Veranlassung von Aufwendungen ist grundsätzlich von Amts wegen  festzustellen, wobei den Steuerpflichtigen eine Mitwirkungspflicht trifft.

**False Positives:**

- `Steuerpflichtigen eine Mitwirkungspflicht trifft.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_TRAIN/129384.1`) (sent_id: `deanon_BFG_TRAIN/129384.1_191`)


Die Beweislast liegt daher im Beschwerdefall eindeutig bei der Bf.

**False Positives:**

- `Bf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_115`)


Ein X scheint im  österreichischen Firmenbuch bei der Bf. aber mit keiner Funktion auf.

**False Positives:**

- `Bf. aber mit keiner Funktion auf.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_TRAIN/129503.1`) (sent_id: `deanon_BFG_TRAIN/129503.1_9`)


Im gegenständlichen Fall sei zwar am 15. Juli 2019 bei der Firma C. GmbH ein  Umbuchungsantrag eingebracht worden.

**False Positives:**

- `Firma C. GmbH ein  Umbuchungsantrag eingebracht worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_TRAIN/129934.1`) (sent_id: `deanon_BFG_TRAIN/129934.1_61`)


Der Bf. erklärte, dass er bei den Bareinzahlungen der Erlöse aus den AGMbH Fahrten keinen  Text auf den Einzahlungsbeleg geschrieben habe, bei den Zahlungen betreffend die  Auftraggeber MT und J hingegen auf den Bankbelegen immer die Namen der Auftraggeber  vermerkt waren.

**False Positives:**

- `Zahlungen betreffend die  Auftraggeber MT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_80`)


Die Bf. gab folgende Stellungnahme ab:  "1  Das Gericht hält richtigerweise fest, dass es sich nach der Jud des VwGH bei der Gerichtspraxis  um eine Ausbildung im Sinne des FLAG handelt (VwGH 18.11.2009, 2008/13/0015) und die  Einkommensgrenze im vorliegenden Fall somit nicht überschritten wurde.

**False Positives:**

- `Gerichtspraxis  um eine Ausbildung im Sinne des FLAG handelt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_TRAIN/130437.1`) (sent_id: `deanon_BFG_TRAIN/130437.1_303`)


Dies geht einerseits aus dem RPG hervor, als auch aus einer auf der Website des  Oberlandesgerichtes Wien veröffentlichten Information:  "Die Gerichtspraxis gibt Personen, die ein rechtswissenschaftliches Studium abgeschlossen  haben, die Möglichkeit, ihre Berufsvorbildung durch eine Tätigkeit bei Gericht fortzusetzen und  dabei die Rechtskenntnisse zu vertiefen.

**False Positives:**

- `Rechtskenntnisse zu vertiefen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_TRAIN/130442.1`) (sent_id: `deanon_BFG_TRAIN/130442.1_17`)


Arzt1, Arzt für Allgemeinmedizin/Sportarzt, vom 30.11.2018, wonach bei der  Bf. seit 1998 ein Diabetes mellitus und eine Insulinisierung seit Juni 2017 bestehe  - Medikamentenverordnungsblatt  - Schreiben des Sozialministeriumservice, BASB Landesstelle NÖ, vom 01.06.2018 betreffend  Ausstellung eines Behindertenpasses;

**False Positives:**

- `Bf. seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_TRAIN/130442.1`) (sent_id: `deanon_BFG_TRAIN/130442.1_76`)


Sie sind bei der Einkunftsart abzuziehen,  bei der sie erwachsen sind.

**False Positives:**

- `Einkunftsart abzuziehen,  bei der sie erwachsen sind.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_TRAIN/130522.1`) (sent_id: `deanon_BFG_TRAIN/130522.1_137`)


Den vorgelegten  Tankrechnungen zufolge wurde das Fahrzeug ca. zweimal pro Monat im Inland (bei der Fa. L in  G, Südsteiermark) betankt, woraus sich erschließt, dass die Bf. mit diesem Kfz unmöglich – wie  behauptet - dreimal im Monat nach Liechtenstein gefahren sein konnte (S. 11 des  Erkenntnisses vom 19.7.2017).

**False Positives:**

- `Fa. L in  G` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_TRAIN/130561.1`) (sent_id: `deanon_BFG_TRAIN/130561.1_69`)


Das Pachtverhältnis endet durch Kündigung oder vorzeitige Auflösung, wobei die Beendigung  des Franchisevertrages zwischen der KG und der Franchisegeberin einen wichtigen  Kündigungsgrund darstellt.

**False Positives:**

- `Beendigung  des Franchisevertrages zwischen der KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_TRAIN/130561.1`) (sent_id: `deanon_BFG_TRAIN/130561.1_122`)


sowie der gewerblichen und technischen Erfahrungen des Franchisegebers  und unter Beachtung des von diesem entwickelten Organisations- und Werbesystems zu  vertreiben, wobei der Franchisegeber Beistand, Rat und Schulung in technischer und  verkaufstechnischer Hinsicht gewährt und eine Kontrolle über die Geschäftstätigkeit des  Franchisenehmers ausübt.

**False Positives:**

- `Franchisegeber Beistand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_13`)


Die Bf. wurde als Beschuldigte niederschriftlich einvernommen und gab zu Protokoll, dass sie  als diplomierte Gesundheits- und Krankenpflegerin bei der Fa. MOKI Wien arbeite.

**False Positives:**

- `Fa. MOKI Wien arbeite.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_TRAIN/130604.1`) (sent_id: `deanon_BFG_TRAIN/130604.1_14`)


Sie habe, da  sie noch nicht so lange in Wien arbeite, damals bei der Abstellung des Fahrzeuges vergessen,  ihre Einlegetafel, sprich Ausnahmegenehmigung, im Fahrzeug anzubringen.

**False Positives:**

- `Abstellung des Fahrzeuges vergessen,  ihre Einlegetafel, sprich Ausnahmegenehmigung, im Fahrzeug anzubringen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_TRAIN/130676.1`) (sent_id: `deanon_BFG_TRAIN/130676.1_57`)


Da die Voraussetzungen für die Anerkennung eines Alleinverdienerabsetzbetrages bei der Bf.  nicht gegeben waren, war dem beantragten Alleinverdienerabsetzbetrag die Anerkennung zu  versagen.

**False Positives:**

- `Bf.  nicht gegeben waren, war dem beantragten Alleinverdienerabsetzbetrag die Anerkennung zu  versagen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_TRAIN/130696.1`) (sent_id: `deanon_BFG_TRAIN/130696.1_26`)


Zur Begründung führte das Finanzamt aus, die genannten Abgabenschuldigkeiten seien bei der  Gesellschaft als uneinbringlich anzusehen.

**False Positives:**

- `Gesellschaft als uneinbringlich anzusehen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_TRAIN/130696.1`) (sent_id: `deanon_BFG_TRAIN/130696.1_140`)


Berechnungen, dass der  Abgabengläubiger gegenüber anderen Gläubigern bei der Entrichtung von Verbindlichkeiten  nicht benachteiligt worden ist, hat die Bf aber bis dato nicht vorgelegt.

**False Positives:**

- `Entrichtung von Verbindlichkeiten  nicht benachteiligt worden ist, hat die Bf aber bis dato nicht vorgelegt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_TRAIN/130697.1`) (sent_id: `deanon_BFG_TRAIN/130697.1_154`)


Zur Entrichtung des Entgeltes ist vom Abgabepflichtigen bei dem mit dem Betrieb des  elektronischen Systems beauftragten Unternehmen (Auftragsverarbeiter gemäß Art. 4 Z 8 der  Verordnung (EU) 2016/679 des Europäischen Parlaments und des Rates vom 27. April 2016  zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien  Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung),  ABl. Nr. L 119 vom 4.5.2016 S. 1) ein Benutzerkonto einzurichten.

**False Positives:**

- `Verarbeitung personenbezogener Daten, zum freien  Datenverkehr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_TRAIN/130697.1`) (sent_id: `deanon_BFG_TRAIN/130697.1_186`)


Sämtliche  Server-Zeiten werden bei der FA. ATOS von externen Zeitservern abgeleitet.

**False Positives:**

- `FA. ATOS von externen Zeitservern abgeleitet.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_TRAIN/130967.1`) (sent_id: `deanon_BFG_TRAIN/130967.1_28`)


Der Bf. wiederholte darin seine Ausführungen, dass seiner Meinung nach bei der Berechnung  der Steuerausgaben 2016 die Angaben in seiner Einnahmen /Ausgabenliste 2016 nicht richtig  berücksichtigt worden seien.

**False Positives:**

- `Berechnung  der Steuerausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_TRAIN/130978.1`) (sent_id: `deanon_BFG_TRAIN/130978.1_59`)


Nr. 79/1896, sind bei der Stelle  zu erheben, von der der Vollstreckungstitel ausgegangen ist.

**False Positives:**

- `Stelle  zu erheben, von der der Vollstreckungstitel ausgegangen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_6`)


Nach vorgelegter Tätigkeitsbeschreibung sei der Sohn  für administrative Tätigkeiten, Ordnung in der Ordination und im Arzneimittelschrank, Urlaubs-  und Krankenstandsvertretung, first-level-Support in der EDV sowie für die Organisation der  Rezepte für Patienten im Altersheim zuständig, wobei die Arbeit an den ordinationsfreien  Tagen (Donnerstag) im Ausmaß von ca fünf Stunden wöchentlich erbracht werde.

**False Positives:**

- `Arbeit an den ordinationsfreien  Tagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_14`)


Am 3.9.2013 reichte der Beschwerdeführer seine Steuererklärung für das Jahr 2012 ein, wobei  in einem Begleitschreiben vom selben Tage darauf hingewiesen wurde, dass bei der  Gewinnermittlung des Jahres 2012 ein Lohnaufwand samt Lohnnebenkosten für  Gehaltszahlungen an den Sohn des Beschwerdeführers iHv 8.869,04 € berücksichtigt worden  seien.

**False Positives:**

- `Gewinnermittlung des Jahres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_TRAIN/130980.1`) (sent_id: `deanon_BFG_TRAIN/130980.1_33`)


Mit Vorhalt der belangten Behörde vom 19.8.2014 wurde der Beschwerdeführer unter Hinweis  auf die Nichtanerkennung des Lohnaufwandes bei der Außenprüfung für die Jahre 2008 – 2010  bzw bei den Veranlagungen der Jahre 2011 und 2012 um Vorlage von Lohnaufzeichnungen und  Arbeitsnachweise ersucht.

**False Positives:**

- `Veranlagungen der Jahre` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_30`)


Diese besagen, dass bei der Berechnung der Fahrzeit, Wartezeiten vor Beginn  bzw. nach Ende der Berufsausbildung nicht einzurechnen sind.

**False Positives:**

- `Berechnung der Fahrzeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_34`)


Auf Grund Ihrer nachgereichten Fahrplanauskünfte und vom Finanzamt abgefragter  Fahrplanauskünften wurde festgestellt, dass die Fahrzeit bei der Fahrt nach Wien bis zum  ersten Umsteigepunkt im Stadtgebiet und bei der Fahrt nach X ab dem letzten Umsteigepunkt  in Wien jeweils zwischen 30 und 42 Minuten beträgt, je nachdem ob die Fahrtroute über  Liesing oder Wien Westbahnhof gewählt wird.

**False Positives:**

- `Fahrt nach Wien bis zum  ersten Umsteigepunkt im Stadtgebiet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_67`)


Diese besagen,  dass bei der Berechnung der Fahrzeit, Wartezeiten vor Beginn bzw. nach Ende der  Berufsausbildung nicht einzurechnen sind.

**False Positives:**

- `Berechnung der Fahrzeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_TRAIN/131011.1`) (sent_id: `deanon_BFG_TRAIN/131011.1_71`)


Fahrplanauskünfte sowie der, vom Finanzamt abgefragten, Fahrplanauskünfte wurde  festgestellt, dass die Fahrzeit bei der Fahrt nach Wien bis zum ersten Umsteigepunkt im  Stadtgebiet und bei der Fahrt nach X ab dem letzten Umsteigepunkt in Wien jeweils zwischen  30 und 42 Minuten beträgt, je nachdem ob die Fahrtroute über Liesing bzw. über Wien  Westbahnhof gewählt wird.

**False Positives:**

- `Fahrt nach Wien bis zum ersten Umsteigepunkt im  Stadtgebiet` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_84`)


Die Bf. gab mit Mail vom 20.3.2020 noch folgende Stellungnahme dazu ab: „Hier meine  Stellungnahme dazu: 1) Umschulungskosten: Anbei der Gutschein - dieser wurde bei der  Akademie bezogen und zählt als Bargeld, das wurde auch von der Landesförderung so  anerkannt (somit wurden 100% der Kurskosten zur Berechnung herangezogen).

**False Positives:**

- `Akademie bezogen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_87`)


3) Bewerbungsfahrten 2012 + 2013: anbei die Daten der Bewerbungsfahrten und die  Berechnungen  4) H.M. ist eine Promotion-Agentur, deshalb haben wir vorab ein Briefing erhalten mit den  jeweiligen Orten, wo wir anwesend sein sollten.

**False Positives:**

- `Daten der Bewerbungsfahrten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_TRAIN/131064.1`) (sent_id: `deanon_BFG_TRAIN/131064.1_100`)


Der Kursbeitrag beträgt EUR 3.390,00,  davon hat die Bf. im Jahr 2012 eine 1. Teilzahlung in der Höhe von EUR 1.134,00 und im Jahr  2013 eine 2. Teilzahlung in der Höhe von EUR 1.133,00 geleistet, wobei die Bf. zur Bezahlung  der restlichen Kursbeitragskosten (3. Teilzahlung) im Jahr 2013 einen Gutschein über EUR  1.123,00 einlöste.

**False Positives:**

- `Bf. zur Bezahlung  der restlichen Kursbeitragskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_TRAIN/131091.1`) (sent_id: `deanon_BFG_TRAIN/131091.1_41`)


In Übereinstimmung mit dieser Rechtsprechung hat das Finanzamt im Rahmen der bei der Bf.  hinsichtlich der Jahre 2009 bis 2012 durchgeführten Außenprüfung festgestellt, dass die  gegenüber Y erbrachten Vermittlungsleistungen im Inland der Umsatzsteuerpflicht unterliegen.

**False Positives:**

- `Bf.  hinsichtlich der Jahre` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_TRAIN/131197.1`) (sent_id: `deanon_BFG_TRAIN/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Ausbildung von Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 57** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_113`)


Die Bedeutung dieses  Fachbegriffes war ihr bei der Einvernahme durch die FinPol nicht bekannt.

**False Positives:**

- `Einvernahme durch die FinPol nicht bekannt.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_126`)


Überwiegend dann, wenn sie ihrem  Gatten bei der Arbeit geholfen hat bzw. zum Skifahren oder Wandern.

**False Positives:**

- `Arbeit geholfen hat bzw. zum Skifahren oder Wandern.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_TRAIN/131270.1`) (sent_id: `deanon_BFG_TRAIN/131270.1_130`)


Die Befragung durch die FinPol und auch die Kontakte mit dem für Strafverfügungen  zuständigen Referenten bei der BH xxx, Herrn G, hat sie als sehr belastend empfunden, weshalb  es zu inhaltlich unrichtigen Protokoll-Textierungen gekommen ist.

**False Positives:**

- `BH xxx` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_TRAIN/131313.1`) (sent_id: `deanon_BFG_TRAIN/131313.1_29`)


Der Bf ersuche, einem schwer an Krebs erkrankten Menschen die steuerliche Begünstigung bei  der Arbeitnehmerveranlagung 2019 zu gewähren.

**False Positives:**

- `Arbeitnehmerveranlagung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_TRAIN/131343.1`) (sent_id: `deanon_BFG_TRAIN/131343.1_12`)


Der Bf. erhob Beschwerde gegen den Einkommensteuerbescheid für das Jahr 2013 und führte  aus, dass Löhne doppelt berücksichtigt worden seien, weil er den Lohn von 1.9. bis 17.10.2013  bei der IEF Service GmbH eingeklagt habe.

**False Positives:**

- `IEF Service GmbH eingeklagt habe.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_TRAIN/131407.1`) (sent_id: `deanon_BFG_TRAIN/131407.1_47`)


Die Rückzahlung der Mindestsicherung sei nicht zu berücksichtigen, weil diese gem. § 3 Abs. 1  Z 3 lit a EStG 1988 bei der Auszahlung steuerfrei und in weiterer Folge die Rückzahlung gem.  § 20 Abs. 2 EStG 1988 vom Werbungskostenabzug ausgeschlossen sei (vgl. BFG 22.10.2019,  RV/7105309/2017).

**False Positives:**

- `Auszahlung steuerfrei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_TRAIN/131451.1`) (sent_id: `deanon_BFG_TRAIN/131451.1_14`)


Mit Bescheid vom 26.04.2017 sei die tatsächliche Höhe der Berufsunfähigkeitspension ab  01.10.2014 festgesetzt worden, wobei der Nachzahlungsbetrag ebenfalls zur Verrechnung der  Ersatzforderung der Tiroler Gebietskrankenkasse einbehalten worden sei.

**False Positives:**

- `Nachzahlungsbetrag ebenfalls zur Verrechnung der  Ersatzforderung der Tiroler Gebietskrankenkasse einbehalten worden sei.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_73`)


Baumaterials auf die Baustelle und das Einteilen der Arbeiter umfassten, ausgeführt worden  sind, erfolgte sodann die Rechnungslegung durch die D. GmbH, ist nicht zu erkennen, dass bei  der Bf. Zweifel aufkommen mussten, die Leistungserbringung sei nicht von der D.GmbH  vorgenommen worden.

**False Positives:**

- `Bf. Zweifel aufkommen mussten, die Leistungserbringung sei nicht von der D.GmbH  vorgenommen worden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_TRAIN/131524.1`) (sent_id: `deanon_BFG_TRAIN/131524.1_10`)


Die Kinder sind, laut Bestätigung der  polnischen Behörden, bei der Mutter mitversichert.

**False Positives:**

- `Mutter mitversichert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_17`)


Der Bf. brachte daraufhin einen Vorlageantrag hinsichtlich seiner Beschwerde ein und führte  darin begründend Folgendes aus:   „Der maßgebliche Bestandteil meiner Tätigkeit bei der X (Energieversorgung NÖ, zunächst  angestellt bei der X Business Service GmbH (Dienstbeginn 11.3.2013) bzw. ab 1.10.2015  angestellt bei der X AG, ist die Abwicklung von Geschäftsabschlüssen.

**False Positives:**

- `X Business Service GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_27`)


Die Beschwerde vom 10.2.2016 enthielt folgende Begründung:  „Der maßgebliche Bestandteil meiner Tätigkeit bei der X (Energieversorgung NÖ) - zunächst  angestellt bei der X Business Service GmbH (Dienstbeginn 11.3.2013) bzw. ab 1.10.2015  angestellt bei der X AG - ist die Abwicklung von Geschäftsabschlüssen.

**False Positives:**

- `X Business Service GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_TRAIN/131601.1`) (sent_id: `deanon_BFG_TRAIN/131601.1_23`)


Von Montag bis Freitag habe er bei den Arbeitgebern eine Schlafstelle gehabt und sei am  Wochenende nach Polen gefahren.

**False Positives:**

- `Arbeitgebern eine Schlafstelle gehabt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_TRAIN/131638.1`) (sent_id: `deanon_BFG_TRAIN/131638.1_7`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (im Folgenden mit Bf. bezeichnet) war in den Jahren 1988 bis 1999 bei  der Lauda Air und für die Jahre 1999 bis 2004 für die Korean Air in Korea jeweils als Berufspilot  tätig.

**False Positives:**

- `Lauda Air` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_TRAIN/131638.1`) (sent_id: `deanon_BFG_TRAIN/131638.1_150`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt:  Der Bf. war in den Jahren 1988 bis 1999 bei der Lauda Air und für die Jahre 1999 bis 2004 für  die Korean Air in Korea jeweils als Berufspilot tätig.

**False Positives:**

- `Lauda Air` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_TRAIN/131705.1`) (sent_id: `deanon_BFG_TRAIN/131705.1_43`)


Rechtliche Beurteilung:  Gemäß § 34 Abs. 1 EStG 1988, BGBl. Nr. 400/1988, sind bei der Ermittlung des Einkommens (§  2 Abs. 2 EStG 1988) eines unbeschränkt Steuerpflichtigen nach Abzug der Sonderausgaben (§  18 leg. cit.) außergewöhnliche Belastungen abzuziehen.

**False Positives:**

- `Ermittlung des Einkommens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_TRAIN/131773.1`) (sent_id: `deanon_BFG_TRAIN/131773.1_6`)


Gem. Abfrage aus dem Zentralen Melderegister hatte der Bf. einen Nebenwohnsitz von  23.06.2015 – 27.07.2015 in ö und von 28.07.2015 – 11.12.2017 in Ö.  Der Beschwerdeführer war von 13.6.2015 bis 31.1.2017 bei der Sozialversicherung der  gewerblichen Wirtschaft versichert.

**False Positives:**

- `Sozialversicherung der  gewerblichen Wirtschaft versichert.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_TRAIN/131804.1`) (sent_id: `deanon_BFG_TRAIN/131804.1_98`)


Deshalb geht das Bundesfinanzgericht übereinstimmend mit dem Finanzamt davon aus, dass  bei der Tochter des Bf. ab dem Juli 2014 keine ernsthafte und zielstrebige Berufsausbildung iSd  FLAG mehr vorgelegen ist.

**False Positives:**

- `Tochter des Bf. ab dem Juli` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_TRAIN/131886.1`) (sent_id: `deanon_BFG_TRAIN/131886.1_32`)


Nr. 79/1896, sind bei der Stelle  zu erheben, von der der Vollstreckungstitel ausgegangen ist.

**False Positives:**

- `Stelle  zu erheben, von der der Vollstreckungstitel ausgegangen ist.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_TRAIN/131941.1`) (sent_id: `deanon_BFG_TRAIN/131941.1_27`)


Der Ansicht des meldungslegenden Organs, dass die Ankunftszeit 14:10 Uhr sei, könne durch- aus gefolgt werden, zumal die Farbsättigung der Ziffer „1“ der Zahl „10“ bei Minute der  Farbsättigung der Ziffer „4“ bei der Zahl „14“ bei der Stunde entspreche.

**False Positives:**

- `Stunde entspreche.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_TRAIN/132030.1`) (sent_id: `deanon_BFG_TRAIN/132030.1_35`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (teilweise Stattgabe)   Rechtslage  Gemäß § 34 Abs. 1 EStG 1988 sind bei der Ermittlung des Einkommens (§ 2 Abs. 2) eines  unbeschränkt Steuerpflichtigen nach Abzug der Sonderausgaben (§ 18) außergewöhnliche  Belastungen abzuziehen.

**False Positives:**

- `Ermittlung des Einkommens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_TRAIN/132109.1`) (sent_id: `deanon_BFG_TRAIN/132109.1_43`)


Die zivilrechtliche Ausgestaltung in  Form einer atypisch stillen Gesellschaft habe nur dem Zweck gedient, bei den Beteiligten die  Verluste verwertbar zu machen.

**False Positives:**

- `Beteiligten die  Verluste verwertbar zu machen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_TRAIN/132165.1`) (sent_id: `deanon_BFG_TRAIN/132165.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Anlässlich der Überprüfung des Anspruches auf Familienbeihilfe betreffend ihre Tochter T gab  die Beschwerdeführerin (kurz: Bf) im Juli 2019 bekannt, dass ihre Tochter Aspirantin bei der  Landespolizeidirektion Salzburg sei und legte ua eine Bestätigung des Bildungszentrums der  Sicherheitsakademie in Linz sowie ein Zeugnis über die Ausbildung zur zahnärztlichen  Assistentin vor.

**False Positives:**

- `Landespolizeidirektion Salzburg sei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_TRAIN/132197.1`) (sent_id: `deanon_BFG_TRAIN/132197.1_10`)


bewusst, dass ich die durch meine geringfügige Beschäftigung bei der Firma Fa, anfallenden  Kilometer und Diäten Gelder steuerlich absetzen kann.

**False Positives:**

- `Firma Fa, anfallenden  Kilometer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_TRAIN/132197.1`) (sent_id: `deanon_BFG_TRAIN/132197.1_49`)


Die  Änderungen tragen auch rechtspolitischen (bzw. verfassungsrechtlichen Bedenken) gegen die  Unterschiede bei der Wiederaufnahme auf Antrag und jener von Amts wegen Rechnung.

**False Positives:**

- `Wiederaufnahme auf Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_TRAIN/132197.1`) (sent_id: `deanon_BFG_TRAIN/132197.1_55`)


Nach Ansicht des Bundesfinanzgerichtes lässt sich aus den Gesetzesmaterialien nur ableiten,  dass die bis zum 31.12.2013 bei der Wiederaufnahme auf Antrag und von Amts wegen  bestehenden, gesetzlich normierten, unterschiedlichen Anwendungsvoraussetzungen beseitigt  werden sollten.

**False Positives:**

- `Wiederaufnahme auf Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_TRAIN/132197.1`) (sent_id: `deanon_BFG_TRAIN/132197.1_61`)


Der Gesetzgeber wollte mit dem  Finanzverwaltungsgerichtsbarkeitsgesetz 2012 vorrangig eine Vereinheitlichung der  Anwendungsvoraussetzungen für die amtswegige und die antragsgebundene Wiederaufnahme  erreichen (vgl. Marchgraber/Pinetz, Neuerungen bei der Wiederaufnahme des Verfahrens  durch das Finanzverwaltungsgesetz 2012, FJ 2013, 169).

**False Positives:**

- `Wiederaufnahme des Verfahrens  durch das Finanzverwaltungsgesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_11`)


Die seitens der Bf eingewendeten  Renditeüberlegungen würden ohnehin bei der Ertragswertermittlung eingeflossen sein.

**False Positives:**

- `Ertragswertermittlung eingeflossen sein.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_97`)


In der Beschwerde vom 20.5.2016 (Postaufgabe am 27.5.2016, Eingang beim Finanzamt  30.5.2016) wendet sich die Bf gegen den Ansatz einer vA im Haftungsbescheid sowie gegen  die Berücksichtigung einer nur verminderten Abschreibungsbasis bei der Ermittlung des  Einkommens.

**False Positives:**

- `Ermittlung des  Einkommens.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_113`)


Der Prüfer nahm dazu mit einem Schreiben vom 22.6.2016 Stellung und führte darin  ergänzend aus, dass aufgrund des Abweichens vom Wert laut Erstgutachten die Gin  objektiv bereichert worden und in subjektiver Hinsicht die Absicht der Vorteilsgewährung  bei der Bf gegeben sei.

**False Positives:**

- `Bf gegeben sei.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_117`)


(das  Erstgutachten kann bei der Ermittlung des objektiven Wertes ein Kriterium gewesen sein  und hat die Gin auch veranlasst, den Preis zu senken;

**False Positives:**

- `Ermittlung des objektiven Wertes ein Kriterium gewesen sein ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_119`)


Auch unter Fremden können bei der  Kaufpreisermittlung mehrere Kriterien eine Rolle spielen.

**False Positives:**

- `Kaufpreisermittlung mehrere Kriterien eine Rolle spielen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_154`)


Die  seitens der Bf eingewandten Renditewerte hätten mangels nachvollziehbarer  Vergleichbarkeit keine Beweiskraft und würden bei der Verkehrswertermittlung nach dem  Ertragswertverfahren keine Rolle spielen.

**False Positives:**

- `Verkehrswertermittlung nach dem  Ertragswertverfahren keine Rolle spielen.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_159`)


Es würde sich somit eine wesentlich  höhere Wertminderung als bei den Gutachten (SV1: 0,8%, SV2: 0,5%) ergeben.

**False Positives:**

- `Gutachten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_TRAIN/132211.1`) (sent_id: `deanon_BFG_TRAIN/132211.1_307`)


Kaufvertrages ist aber rein buchungstechnisch dennoch eine Verbindlichkeit bei der Bf und  eine (nach Ansicht des Finanzamtes zu einer verdeckten Ausschüttung führenden überhöhte)  Forderung bei der Gin entstanden, die dann durch die per Salso Buchung letztlich ausgebucht  wurden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Gin entstanden, die dann durch die per Salso Buchung letztlich ausgebucht  wurden.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 91** (doc_id: `deanon_BFG_TRAIN/132303.1`) (sent_id: `deanon_BFG_TRAIN/132303.1_51`)


Dies gelte auch dann, wenn sich  der Familienbonus Plus bei der Pflegemutter steuerlich nicht auswirke.

**False Positives:**

- `Pflegemutter steuerlich nicht auswirke.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_TRAIN/132361.1`) (sent_id: `deanon_BFG_TRAIN/132361.1_34`)


Im Beschwerdefall liege also insofern eine Sondersituation vor, als das Expertengremium bei  der Erstellung des Gutachtens nicht unmittelbar aufgrund der Bestimmungen des AWG 2002,  sondern aufgrund eines privatrechtlichen Auftragsverhältnisses (gemeint: gegenüber der Bf.)  aktiv geworden sei.

**False Positives:**

- `Erstellung des Gutachtens nicht unmittelbar aufgrund der Bestimmungen des AWG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_TRAIN/132372.1`) (sent_id: `deanon_BFG_TRAIN/132372.1_16`)


Auf Nachfrage übermittelte die Firma Firma1 e.U. Ihre An- und Abmeldung bei der  Gebietskrankenkasse, Ihren Dienstzettel und Ihren Führerschein.

**False Positives:**

- `Gebietskrankenkasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_TRAIN/132430.1`) (sent_id: `deanon_BFG_TRAIN/132430.1_9`)


In der Beschwerde vom 09.04.2020 wurde vom BF bekannt gegeben, dass die Ausgaben für  Behinderung irrtümlich bei der Behinderung Ehegattin eingetragen worden seien.

**False Positives:**

- `Behinderung Ehegattin eingetragen worden seien.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_TRAIN/132660.1`) (sent_id: `deanon_BFG_TRAIN/132660.1_11`)


In diesem Vorlageantrag begehrt die bP nunmehr  ausschließlich das Ausscheiden der in der deutschen Altersrente enthaltenen Sonderzahlungen  bei der Berechnung des Progressionsvorbehaltes.

**False Positives:**

- `Berechnung des Progressionsvorbehaltes.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_TRAIN/132660.1`) (sent_id: `deanon_BFG_TRAIN/132660.1_30`)


Strittig ist ausschließlich, ob in der deutschen Altersrente anteilig Sonderzahlungen  enthalten sind, die bei der Ermittlung des Welteinkommens auszuscheiden sind.

**False Positives:**

- `Ermittlung des Welteinkommens auszuscheiden sind.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_TRAIN/132660.1`) (sent_id: `deanon_BFG_TRAIN/132660.1_37`)


Demzufolge waren  auch keine anteiligen Sonderzahlungen aus der deutschen Altersrente bei der Ermittlung des  Welteinkommens (Progressionsvorbehalt) auszuscheiden.

**False Positives:**

- `Ermittlung des  Welteinkommens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_TRAIN/132704.1`) (sent_id: `deanon_BFG_TRAIN/132704.1_42`)


Er habe bis 4.3.2014 für ein Projekt in rus_Ort gearbeitet  und mit 1.5.2014 eine befristete Anstellung bei der X AG (Schweiz) angenommen, für die er  nach i_Ort1 (Italien) entsendet worden sei.

**False Positives:**

- `X AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `deanon_BFG_TRAIN/132794.1`) (sent_id: `deanon_BFG_TRAIN/132794.1_46`)


Überdies wurde das KfZ bei der  Firma Lieferant eingestellt (somit gab es einen Abstellplatz) und konnte das Fahrzeug dort jeder  Zeit von Interessenten besichtigt werden.

**False Positives:**

- `Firma Lieferant eingestellt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

