# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-28T10:12:39.697151

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
| Training documents | 2473 |
| Validation documents | 619 |
| Test documents | 792 |
| Train sentences | 3896 |
| Validation sentences | 1147 |
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
| Best Batch Idx | 4 |
| Best Batch F1 | 0.5191594561186651 |
| Best Rules Serialized | [{'id': 'b11b6b1a', 'name': 'Judge_Richter', 'description': 'Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.', 'format': 'regex', 'content': '(?:durch\\s+(?:den\\s+)?(?:Richter|Richterin|Vorsitzende)\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|Dr\\.\\s+Univ\\.-Prof\\.in?|Univ\\.-Prof\\.in?|Priv\\.-Doz\\.in?|Hon\\.-Prof\\.in?)?)?)(?:\\s+(?:in der|\\u00fcber die|in der Verwaltungsstrafsache)|$)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'ee477b11', 'name': 'Party_Beschwerdesache', 'description': "Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.", 'format': 'regex', 'content': '(?:in der\\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\\s+(?:der\\s+|des\\s+)?)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.))?(?=,\\s+[A-Z]|\\s+vertreten|\\s+\\(|\\s+\\)|$|\\s+\\d{4}\\s+\\w+))', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4913d14d', 'name': 'Representative_vertreten_durch', 'description': "Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.", 'format': 'regex', 'content': '(?:vertreten\\s+durch\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|DDr\\.|R\\.in?|R\\.)?)(?=,\\s+[A-Z]|\\s+GmbH|\\s+Steuerberatung|\\s+OG|\\s+KG|\\s+Rechtsanwalts|\\s+PartG|\\s+StbG|\\s+\\(|$))', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4bee6298', 'name': 'Herr_Name', 'description': "Captures full names following 'Herr' or 'Herrn', ensuring the full name is extracted.", 'format': 'regex', 'content': '(?:Herr|Herrn)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'b07361b5', 'name': 'Frau_Name', 'description': "Captures full names following 'Frau'.", 'format': 'regex', 'content': '(?:Frau|Frauen)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d))', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '98f92f79', 'name': 'Herr_Name_Corrected', 'description': "Captures full names following 'Herr' or 'Herrn', ensuring it matches a name (not a title) and handles German characters.", 'format': 'regex', 'content': '(?:Herr|Herrn)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d))', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 99.0% |
| True Positives | 630 |
| False Positives | 159 |
| False Negatives | 1008 |
| Total Gold Entities | 1638 |
| Micro Precision | 79.8% |
| Micro Recall | 38.5% |
| Micro F1 | 51.9% |
| Macro F1 | 51.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Herr_Name_Corrected` | 1.2% | 100.0% | 0.6% | 10 | 10 | 0 |
| `Party_Beschwerdesache` | 40.0% | 86.6% | 26.0% | 492 | 426 | 66 |
| `Frau_Name` | 0.5% | 80.0% | 0.2% | 5 | 4 | 1 |
| `Herr_Name` | 6.3% | 79.4% | 3.3% | 68 | 54 | 14 |
| `Judge_Richter` | 15.7% | 69.0% | 8.9% | 210 | 145 | 65 |
| `Representative_vertreten_durch` | 0.2% | 13.3% | 0.1% | 15 | 2 | 13 |

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

**F1:** 0.400 | **Precision:** 0.866 | **Recall:** 0.260  

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
| 0.866 | 0.260 | 0.400 | 492 | 426 | 66 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 426 | 66 | 1210 |

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

- `Roxana Gehrbrandt,` — partial — gold is substring of pred: `Roxana Gehrbrandt`

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

## `Herr_Name`

**F1:** 0.063 | **Precision:** 0.794 | **Recall:** 0.033  

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
| 0.794 | 0.033 | 0.063 | 68 | 54 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 54 | 14 | 1575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_49`)


Die  Fahrzeugschlüssel und Papiere wurden von Herrn OStR Karl Ostendarp  oder Frau AB persönlich  entgegengenommen und im Büro versperrt aufbewahrt.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/129950.1`) (sent_id: `deanon_BFG_TRAIN/129950.1_5`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Denise Adamske – machte in der Erklärung zur Arbeitnehmer-

| Predicted | Gold |
|---|---|
| `Denise Adamske` | `Denise Adamske` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_30`)


Lfd.Nr. Bezeichnung der körperlichen, geistigen oder sinnesbedingten  Funktionseinschränkungen, welche voraussichtlich länger als sechs Monate andauern werden:  Begründung der Rahmensätze: Pos.Nr. Gdb%  1 paranoide Schizophrenie  Unterer Rahmensatz, da verminderte psychische Belastbarkeit 03.07.02 50  Gesamtgrad der Behinderung 50 v. H.  Begründung für den Gesamtgrad der Behinderung:  Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keine Änderung gegenüber dem VGA von 9/2015  der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 07/2014  Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_113`)


Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_178`)


Vorgutachten 14 08 2018:   paranoide Schizophrenie GdB 50%   seit 07/2014   Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA    Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_225`)


Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA   Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_57`)


Der Mietvertrag lautet auf Herrn Lukasz Jan Chlebek.

| Predicted | Gold |
|---|---|
| `Lukasz Jan Chlebek` | `Lukasz Jan Chlebek` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_75`)


Als Beispiel ist das bereits zweimal  stattgefundene Verkaufstraining mit Herrn Hubert Mann zu nennen (siehe Beilagen).

| Predicted | Gold |
|---|---|
| `Hubert Mann` | `Hubert Mann` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_73`)


Im Schreiben der Privatklink vom 21. Oktober 2019 wird auszugsweise ausgeführt:  "Herr Ernestine Schittenhelm  stellte sich bei uns am 07.11.2017 erstmals vor.

| Predicted | Gold |
|---|---|
| `Ernestine Schittenhelm` | `Ernestine Schittenhelm` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Stanislaus Calisir (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Example 10** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_37`)


Herr Huberta Schwandt  wird ohne sachliche Grundlage um 123 TEUR entreichert, während in  vergleichbaren Fällen im betrieblichen Bereich dies nicht geschieht.

| Predicted | Gold |
|---|---|
| `Huberta Schwandt` | `Huberta Schwandt` |

**Example 11** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_8`)


Frau Frau erhob gegen die zwei Strafverfügungen 1) und 2) bei der MA 67 am 08.05.2021  Einspruch und brachte vor „Hiermit geben wir bekannt, dass Herr Cynthia Neureuter  nicht Halter des  Fahrzeugs mit dem Kennzeichen 123 ist“.

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 12** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Cynthia Neureuter  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 13** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_26`)


Deshalb sei Frau Frau mit Schreiben der Magistratsabteilung 67 vom 09.06.2021 aufgefordert  worden, binnen zwei Wochen eine für das Verwaltungsstrafverfahren gültige Vollmacht von  Herrn Cynthia Neureuter  zu übermitteln.

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 14** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_28`)


Am 23.06.2021 sei von Herrn  Cynthia Neureuter  lediglich ein Schreiben mit folgendem Inhalt übermittelt worden: „Bezugnehmend  auf Ihr Schreiben an Frau Frau vom 09.06.2021 möchte ich hiermit eigenhändig bestätigen,  dass das Fahrzeug mit dem angegebenen Kennzeichen nicht in meinem Besitz ist und ich auch  nicht weiß, wem es gehört“.

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 15** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_38`)


Herr Cynthia Neureuter  sei persönlich bei genannter Firma  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 16** (doc_id: `deanon_BFG_TRAIN/134762.1`) (sent_id: `deanon_BFG_TRAIN/134762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Simon Zens  in der Beschwerdesache Miriam Große-Bley,  Tipschern 13, 4052 Fürhappen, Österreich, vertreten durch Herrn Michael Haberl, Steuerberater, Hauptstraße 65, 8962  Gröbming, über die Beschwerde vom 9.7.2018 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 12.6.2018 betreffend Festsetzung des Dienstgeberbeitrages (DB) für die  Jahre 2013, 2014, 2015 und 2016 sowie des Zuschlages zum Dienstgeberbeitrag (DZ) für die  Jahre 2013, 2014, 2015 und 2016 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Michael Haberl` | `Michael Haberl` |

**Missed by this rule (FN):**

- `Priv.-Doz. Simon Zens` (person)
- `Miriam Große-Bley` (person)
- `Tipschern 13, 4052 Fürhappen, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/136573.1`) (sent_id: `deanon_BFG_TRAIN/136573.1_71`)


Weiters verweise ich auf das Steuersparbuch von Herrn Eduard Müller,  Mitarbeiter im BM für Finanzen, welcher die Ausgaben für eine Coaching Ausbildung für  Führungskräfte bestätigt.

| Predicted | Gold |
|---|---|
| `Eduard Müller` | `Eduard Müller` |

**Example 18** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Natascha Daschmann (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Example 19** (doc_id: `deanon_BFG_TRAIN/139959.1`) (sent_id: `deanon_BFG_TRAIN/139959.1_48`)


Begründung – GdB liegt rückwirkend vor:  Herr Evelyn Walz  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Auf Grund von fehlender Vorlage medizinischer Befunde ist keine Einschätzung der  Selbsterhaltungsfähigkeit möglich.“

| Predicted | Gold |
|---|---|
| `Evelyn Walz` | `Evelyn Walz` |

**Example 20** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_8`)


Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der  Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische  Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur  Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit  1 von 20 Seite 2 von 20

| Predicted | Gold |
|---|---|
| `Brunhild Hoffschulz` | `Brunhild Hoffschulz` |

**Example 21** (doc_id: `deanon_BFG_TRAIN/141435.1`) (sent_id: `deanon_BFG_TRAIN/141435.1_4`)


Begründung  Verfahrensgang:  MA67/226701281451/2022:  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner  2023, Zahl: MA67/226701281451/2022, wurde Herr Robert Grentzmann (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von einem 14 Stunden verhängt sowie ein  Verfahrenskostenbeitrag von € 10,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Robert Grentzmann` | `Robert Grentzmann` |

**Example 22** (doc_id: `deanon_BFG_TRAIN/141974.1`) (sent_id: `deanon_BFG_TRAIN/141974.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Gottfried Kroehner – bezog im Jahr 2021 Bezüge durch die  Österreichische Gesundheitskasse in Form eines Wiedereingliederungsgeldes gemäß § 143d  ASVG für 132 Tage in Höhe von 19,09 € brutto täglich, ds 2.519,88 €.

| Predicted | Gold |
|---|---|
| `Gottfried Kroehner` | `Gottfried Kroehner` |

**Example 23** (doc_id: `deanon_BFG_TRAIN/142976.1`) (sent_id: `deanon_BFG_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Nikolaus Thulke (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Nikolaus Thulke` | `Nikolaus Thulke` |

**Example 24** (doc_id: `deanon_BFG_TRAIN/144254.1`) (sent_id: `deanon_BFG_TRAIN/144254.1_94`)


Das beanstandete Fahrzeug wurde zum  Tatzeitpunkt von Herrn Wilfried Körbelin  gelenkt.

| Predicted | Gold |
|---|---|
| `Wilfried Körbelin` | `Wilfried Körbelin` |

**Example 25** (doc_id: `deanon_BFG_TRAIN/144254.1`) (sent_id: `deanon_BFG_TRAIN/144254.1_95`)


Bitte beantworten Sie innerhalb von zwei Wochen ab Zustellung dieses Schreibens brieflich oder  per E-Mail folgende Fragen:  Wurden  - Sie innerhalb der letzten 2 Monate, insbesondere am 14.06.2023, von Herrn Wilfried Körbelin  mit  dem Fahrzeug mit dem behördlichen Kennzeichen Vienna befördert oder haben Sie dieses selbst  gelenkt?  - Kopien Ihres Ausweises gemäß § 29b StVO gemacht?

| Predicted | Gold |
|---|---|
| `Wilfried Körbelin` | `Wilfried Körbelin` |

**Example 26** (doc_id: `deanon_BFG_TRAIN/144576.1`) (sent_id: `deanon_BFG_TRAIN/144576.1_13`)


Bitte beantworten Sie innerhalb von zwei Wochen ab Zustellung dieses Schreibens brieflich oder  per E-Mail folgende Fragen:   Wurden  - Sie am 04.04.2023 von Herrn Ivan Färbers  mit dem Fahrzeug mit dem behördlichen  Kennzeichen Vienna befördert oder haben Sie dieses Fahrzeug selbst gelenkt?  - Kopien Ihres Ausweises gemäß § 29b StVO gemacht?

| Predicted | Gold |
|---|---|
| `Ivan Färbers` | `Ivan Färbers` |

**Example 27** (doc_id: `deanon_BFG_TRAIN/144625.1`) (sent_id: `deanon_BFG_TRAIN/144625.1_22`)


unentgeltlich an Herrn Ludmilla Seubel  übertragen.

| Predicted | Gold |
|---|---|
| `Ludmilla Seubel` | `Ludmilla Seubel` |

**Example 28** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_6`)


Entscheidungsgründe  Mit Straferkenntnis vom 16. April 2024, Zahl: MA67/246700162299/2024, hat der Magistrat  der Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Leonhard Facci (in weiterer  Folge: Beschwerdeführer – Bf) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt  indem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen I-57 VS  am  2. Februar 2024 um 09:20 Uhr in einer gebührenpflichtigen Kurzparkzone in 1210 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `I-57 VS` (vehicle_license)

**Example 29** (doc_id: `deanon_BFG_TRAIN/145067.1`) (sent_id: `deanon_BFG_TRAIN/145067.1_16`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:    ja  GdB liegt vor seit:   03/2022  Herr Olaf Klockmeier  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  JA  Dies besteht seit:      03/2022  2 von 14 Seite 3 von 14

| Predicted | Gold |
|---|---|
| `Olaf Klockmeier` | `Olaf Klockmeier` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_5`)


Entscheidungsgründe  Zum Erkenntnis: Mit Bescheid des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013 wurden  die Anspruchszinsen 2007 für die Einkommensteuernachforderung 2007 von Herrn Bauermeister Getränke,  nunmehr Bauermeister Getränke (in weiterer Folge: Bf.) in einer Höhe von € 27.080,78 festgesetzt.

**False Positives:**

- `Bauermeister Getränke` — type mismatch — same span as gold: `Bauermeister Getränke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Bauermeister Getränke`(organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Ronald Kleile, Bakk. rer. nat., Fischteichweg 49, 4924 Hartlberg, Österreich, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 15. März 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 20. Februar 2019, Strafnummer 007, in Anwesenheit des  Beschuldigten, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Über Ronald Kleile, Bakk. rer. nat.  wird gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 17.600,00  verhängt.

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)
- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_6`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 20. Februar 2019,  Strafnummer 007, wurde Herr Ronald Kleile, Bakk. rer. nat., geb. 1989, Geschäftsführer, wohnhaft in Fischteichweg 49, 4924 Hartlberg, Österreich  in Abwesenheit schuldig erkannt,   „A.) er hat in Wien vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von  1 von 18 Seite 2 von 18

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_140`)


Gesellschafter/Geschäftsführer der H- GmbH ist Herr Ronald Kleile, Bakk. rer. nat..

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat..`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat..`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_161`)


Zwischen Herrn Ronald Kleile, Bakk. rer. nat., Alleingesellschafter und einziger Geschäftsführer der H- GmbH und  Herrn S., seinem Vater, bestand und besteht nicht nur eine persönliche, sondern auch eine  wirtschaftliche Nahebeziehung.

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/134402.1`) (sent_id: `deanon_BFG_TRAIN/134402.1_195`)


Seit 1.8.2014 ist auch Herr DI FG5 Geschäftsführer.

**False Positives:**

- `DI FG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/136573.1`) (sent_id: `deanon_BFG_TRAIN/136573.1_126`)


Weiters darf ich auf Aussagen von Herrn Dipl Kfm Eduard Müller, Mitarbeiter im BMF, im  Steuerbuch verweisen, welcher die Ausgaben für eine Coaching-Ausbildung für Führungskräfte  bestätigt.

**False Positives:**

- `Dipl Kfm Eduard Müller` — partial — gold is substring of pred: `Dipl Kfm`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl Kfm`(person)
- `Eduard Müller`(person)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138117.1`) (sent_id: `deanon_BFG_TRAIN/138117.1_41`)


Infolge des  Testamentes und der Eröffnungsniederschrift vom 26.6.2020 sind gesetzliche Erben des  Nachlasses: Die Ehegattin Frau Vorname Vorname2 Nachname, zu 50 % des Erbteiles, der Sohn  Herr G A Nachname zu 25 % des Erbteiles sowie Herr AC Nachname zu 25 % des Erbteiles.

**False Positives:**

- `AC Nachname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/138498.1`) (sent_id: `deanon_BFG_TRAIN/138498.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Im Rahmen der am 17.02.2020 eingereichten Erklärung zur Arbeitnehmerveranlagung 2019  wurde durch Herrn Zacharias Arhelger, BA (in der Folge „Bf“ oder „Beschwerdeführer“) die Gewährung des  (ganzen) Familienbonus Plus für 12 Monate beantragt.

**False Positives:**

- `Zacharias Arhelger` — partial — pred is substring of gold: `Zacharias Arhelger, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zacharias Arhelger, BA`(person)

**Example 9** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_19`)


Der Bf. beantwortete den Vorhalt mit Schreiben vom 15. Jänner 2013 wie folgt:  "Frau W und Herr M T haben bei Herrn XY Geldanlagen getätigt.

**False Positives:**

- `XY Geldanlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_335`)


Im daraufhin fortgesetzten Verfahren zu RV/2100547/2022 wurden seitens des Bf.  Beweisanträge auf Einvernahme Herrn XY, Herrn RA Dr. C D (Vertreter der  InsolvenzverwaltungsGmbH als Masseverwalter im Konkurs über das Vermögen der ZZZ- Gruppe), sowie Herrn Dr. O P (RA) gestellt.

**False Positives:**

- `RA Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_369`)


Der Bf. und seine Ehegattin überließen Herrn XY Geldbeträge jeweils in bar, wobei die  Einzahlungen in individuell wählbaren Beträgen erfolgten und nicht an den Ausgabewert der  ZZZ-Zertifikate (Genussschein) gebunden waren.

**False Positives:**

- `XY Geldbeträge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/146514.1`) (sent_id: `deanon_BFG_TRAIN/146514.1_15`)


Die Bf. brachte in ihrem fristgerecht erhobenen Einspruch (E-Mail vom 12. September 2024) zu  allen fünf GZen vor, dass Herr Herr Lenker zur gegebenen Zeit gewesen sei.

**False Positives:**

- `Herr Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_20`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im verfahrensgegenständlichen Veranlagungszeitraum 2023 hatte Herr Bernhard Siegmundt  Einkünfte aus  nichtselbständiger Tätigkeit von zwei Dienstgebern:   Im Zeitraum zwischen Jänner und der zweiten Monatshälfte des Juli 2023 (mit einer  kurzen Unterbrechung und dem Bezug von Arbeitslosengeld im Jänner 2023) bezog der  Bf. Einkünfte von der Arbeitgeber NÖ in Adr Arbeitgeber NÖ.

**False Positives:**

- `Bernhard Siegmundt  Einkünfte` — partial — gold is substring of pred: `Bernhard Siegmundt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Siegmundt`(person)

</details>

---

## `Judge_Richter`

**F1:** 0.157 | **Precision:** 0.690 | **Recall:** 0.089  

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
| 0.690 | 0.089 | 0.157 | 210 | 145 | 65 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 145 | 65 | 1491 |

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

**Example 0** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128877.1`) (sent_id: `deanon_BFG_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers OSR DDr. Heiko Lehwaldt, Point 6, 3232 Zauching, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR DDr. Heiko Lehwaldt`(person)
- `Point 6, 3232 Zauching, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl.

**False Positives:**

- `Mag. Emmerich Bleekmann ` — partial — gold is substring of pred: `Mag. Emmerich Bleekmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Emmerich Bleekmann`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christoph Mehlbeer`(person)
- `Schötz Gasse 45, 7434 Holzschlag, Österreich`(address)
- `Margarete Wiepking`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/131051.1`) (sent_id: `deanon_BFG_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Kirsten Öllrich, Grundemanngasse 2, 4755 Hub, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Öllrich`(person)
- `Grundemanngasse 2, 4755 Hub, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_TRAIN/131772.1`) (sent_id: `deanon_BFG_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Dipl.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/131922.1`) (sent_id: `deanon_BFG_TRAIN/131922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Bodo Ibel  in der Verwaltungsstrafsache  Fridolin Jodeleid, Stiftergasse 75z, 2262 Stillfried, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in  Verbindung mit § 16 Abs. 1 und Tarifpost B 8 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli  1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl.

**False Positives:**

- `Mag. Mag. Bodo Ibel ` — partial — gold is substring of pred: `Mag. Mag. Bodo Ibel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Mag. Bodo Ibel`(person)
- `Fridolin Jodeleid`(person)
- `Stiftergasse 75z, 2262 Stillfried, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Karola Birkenzeller, Reifnitz 2, 4532 Rohr im Kremstal, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Pascal Tiessen, Dipl.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karola Birkenzeller`(person)
- `Reifnitz 2, 4532 Rohr im Kremstal, Österreich`(address)
- `Pascal Tiessen`(person)

**Example 10** (doc_id: `deanon_BFG_TRAIN/133042.1`) (sent_id: `deanon_BFG_TRAIN/133042.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Siegfried Borneleit  in der Beschwerdesache Ashley Kutluca,  Pabensteinstraße 20, 5132 Reith, Österreich, über die Beschwerden vom 20. Februar 2020 gegen die Bescheide des  Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 24. Jänner 2020 betreffend   1. Zurückweisung des Antrages vom 2.1.2020 auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2014 und   2.

**False Positives:**

- `Dr. Dr. Siegfried Borneleit ` — partial — gold is substring of pred: `Dr. Dr. Siegfried Borneleit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Siegfried Borneleit`(person)
- `Ashley Kutluca`(person)
- `Pabensteinstraße 20, 5132 Reith, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Lorenz Lohkampff ` — partial — gold is substring of pred: `Mag. Lorenz Lohkampff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/133768.1`) (sent_id: `deanon_BFG_TRAIN/133768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Daphne Heinzlmeir, Holzwiesengasse 15, 4723 Natternbach, Österreich, über die Beschwerde vom 20. Mai 2021 gegen den Bescheid des Finanzamtes  Österreich vom 26. April 2021 betreffend Zwangsstrafen 2021 zu Steuernummer  68-502/3247  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daphne Heinzlmeir`(person)
- `Holzwiesengasse 15, 4723 Natternbach, Österreich`(address)
- `68-502/3247`(tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/134729.1`) (sent_id: `deanon_BFG_TRAIN/134729.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Philipp Dahlhues  in der Beschwerdesache August Combach,  Damweg 1, 7501 Spitzzicken, Österreich, gegen die Bescheide des Finanzamtes Österreich vom   - 11. Juli 2017 betreffend Einkommensteuer 2014 sowie  - 06. Juni 2018 betreffend Einkommensteuer 2016 und 2017  den Beschluss:  I. Die Beschwerde betreffend Einkommensteuer 2014 wird gemäß  § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Philipp Dahlhues ` — partial — gold is substring of pred: `Mag. Philipp Dahlhues`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Philipp Dahlhues`(person)
- `August Combach`(person)
- `Damweg 1, 7501 Spitzzicken, Österreich`(address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/134866.1`) (sent_id: `deanon_BFG_TRAIN/134866.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Daniel Priskorn  in der Beschwerdesache Felix Kerling,  Rassbergstraße 13, 3742 Passendorf, Österreich, wegen behaupteter Verletzung der Entscheidungspflicht des FA St. Johann Tamsweg Zell am See  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 beschlossen:   Die Säumnisbeschwerde wird als unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Daniel Priskorn ` — partial — gold is substring of pred: `Dr. Daniel Priskorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Daniel Priskorn`(person)
- `Felix Kerling`(person)
- `Rassbergstraße 13, 3742 Passendorf, Österreich`(address)
- `FA St. Johann Tamsweg Zell am See`(organisation)

**Example 15** (doc_id: `deanon_BFG_TRAIN/135112.1`) (sent_id: `deanon_BFG_TRAIN/135112.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Zlatan Deisen  in der Beschwerdesache des  Prof. Richard Paulick, Scharmühlwinkel 13, 3144 Baumgarten, Österreich, über 1) die Beschwerde vom 27.9.2017 gegen den Bescheid des  Finanzamtes Bruck Leoben Mürzzuschlag (nunmehr Finanzamt Österreich) vom 4.9.2017  betreffend Umsatzsteuer 2015 sowie über 2) die Beschwerde vom 7.9.2018 gegen den  Bescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 21.8.2018 betreffend Abweisung  von Anträgen auf Aufhebung der Bescheide hinsichtlich Umsatzsteuer 2011 bis 2014 nach  Durchführung einer mündlichen Verhandlung am 2.12.2021 zu Recht erkannt:   I. Den Beschwerden wird Folge gegeben.

**False Positives:**

- `Dr. Dr. Zlatan Deisen ` — partial — gold is substring of pred: `Dr. Dr. Zlatan Deisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Zlatan Deisen`(person)
- `Prof. Richard Paulick`(person)
- `Scharmühlwinkel 13, 3144 Baumgarten, Österreich`(address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/135347.1`) (sent_id: `deanon_BFG_TRAIN/135347.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache DDr. DDr. Björn Wöber, Bisamgasse 3i, 9433 Tschrietes, Österreich, betreffend Beschwerde vom 27. Oktober 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 9. Oktober 2020 zu Steuernummer  60-281/1996  betreffend Abweisung des Antrages auf Zuerkennung der Familienbeihilfe für  KommR Hugo Vollpracht  ab Oktober 2019 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `R.` — similar text (different position): `DDr. DDr. Björn Wöber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. DDr. Björn Wöber`(person)
- `Bisamgasse 3i, 9433 Tschrietes, Österreich`(address)
- `60-281/1996`(tax_number)
- `KommR Hugo Vollpracht`(person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/135585.1`) (sent_id: `deanon_BFG_TRAIN/135585.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Charles Schindele  in der Beschwerdesache Gregor Branz,  Tandlerstraße 7, 9341 Herd, Österreich, vertreten durch die Germuth Steuerberatungs GmbH, Johannesgasse 16/5,  1010 Wien, über die Beschwerde vom 17. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 14. Juli 2021 betreffend Nachsicht gemäß § 236 BAO, Steuernummer  79-519/7411  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Charles Schindele ` — partial — gold is substring of pred: `Mag. Charles Schindele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Charles Schindele`(person)
- `Gregor Branz`(person)
- `Tandlerstraße 7, 9341 Herd, Österreich`(address)
- `79-519/7411`(tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/135774.1`) (sent_id: `deanon_BFG_TRAIN/135774.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache MedR Uwe Preikschas, Marika Rökk-Straße 67, 3131 Anzenberg, Österreich, über die Beschwerde vom 19. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019, Steuernummer 19-302/7367, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO – wie mit Beschwerdevorentscheidung vom 26. April  2021 – teilweise Folge gegeben und der angefochtene Bescheid in diesem Sinne abgeändert.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MedR Uwe Preikschas`(person)
- `Marika Rökk-Straße 67, 3131 Anzenberg, Österreich`(address)
- `19-302/7367`(tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/136313.1`) (sent_id: `deanon_BFG_TRAIN/136313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger im  Beschwerdeverfahren über die Beschwerde der Verl nach XY, vertreten durch Laurence Krekemeyer,  Steyersberg 2, 8481 Priebing, Österreich  vom 20. Juli 2021 gegen den Zurückweisungsbescheid des Finanzamtes  Österreich vom 7. Juli 2021 betreffend Antrag auf Durchführung einer  Arbeitnehmerveranlagung, beschlossen:  Der Vorlageantrag der Beschwerdeführerin Verl nach XY vom 10.9.2021 wird gemäß § 260 Abs.  1 BAO iVm § 264 BAO (insbesondere Abs. 4 lit e und Abs. 5) als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr. Ansgar Unterberger im  Beschwerdeverfahren` — partial — gold is substring of pred: `Dr. Ansgar Unterberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Laurence Krekemeyer`(person)
- `Steyersberg 2, 8481 Priebing, Österreich`(address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/137032.1`) (sent_id: `deanon_BFG_TRAIN/137032.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_TRAIN/137355.1`) (sent_id: `deanon_BFG_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Dr. Theobald Korschinek ` — partial — gold is substring of pred: `Dr. Theobald Korschinek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Theobald Korschinek`(person)
- `Dieter Papakiriakou`(person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/137493.1`) (sent_id: `deanon_BFG_TRAIN/137493.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Herbert Kramp, Kinkstraße 6, 3541 Senftenberg, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Waldviertel, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend Abweisung des  Antrages auf Gewährung der vollen nichtindexierten Familienbeihilfe ab Jänner 2019,  Steuernummer 15-114/2120, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Herbert Kramp`(person)
- `Kinkstraße 6, 3541 Senftenberg, Österreich`(address)
- `15-114/2120`(tax_number)

**Example 24** (doc_id: `deanon_BFG_TRAIN/137516.1`) (sent_id: `deanon_BFG_TRAIN/137516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Friedhelm Servais, Ölbrennerweg 38, 5231 Wiesing, Österreich, über die Beschwerde vom 15. Oktober 2020 gegen den Bescheid des Finanzamtes  Österreich vom 1. Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 86-385/7500  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Friedhelm Servais`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Friedhelm Servais`(person)
- `Ölbrennerweg 38, 5231 Wiesing, Österreich`(address)
- `86-385/7500`(tax_number)

**Example 25** (doc_id: `deanon_BFG_TRAIN/137596.1`) (sent_id: `deanon_BFG_TRAIN/137596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Egon Hintenberg  in der Beschwerdesache des  OMedR Rafaela Balcius, Hoferweg 3, 3033 Manzing, Österreich, über die Beschwerde vom 11. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Egon Hintenberg ` — partial — gold is substring of pred: `Mag. Egon Hintenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Egon Hintenberg`(person)
- `OMedR Rafaela Balcius`(person)
- `Hoferweg 3, 3033 Manzing, Österreich`(address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/137664.1`) (sent_id: `deanon_BFG_TRAIN/137664.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Dr. Emanuel Rauschmeir  in der Beschwerdesache Bertha Hueber,  Schirnes 10, 9871 Kötzing, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, betreffend Beschwerden vom 11. Februar 2020 und 27. Februar 2020  gegen die Bescheide betreffend Feststellungsbescheid Gruppenmitglied 2014 vom 11. Februar  2020 sowie vom 13. Jänner 2020 betreffend Feststellungsbescheid Gruppenmitglied 2015 und  2016 jeweils des Finanzamtes Wien 1/23 den Beschluss:   I. Die Beschwerden werden gemäß § 278 Abs. 1 lit b iVm § 256 Abs. 3 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Dr. Emanuel Rauschmeir ` — partial — gold is substring of pred: `Dr. Emanuel Rauschmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Emanuel Rauschmeir`(person)
- `Bertha Hueber`(person)
- `Schirnes 10, 9871 Kötzing, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/138011.1`) (sent_id: `deanon_BFG_TRAIN/138011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Sascha Grosan  in der Beschwerdesache Carla Kurrek,  Moosacker 29, 4724 Stocket, Österreich, über die Beschwerde vom 30. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Kirchdorf Perg Steyr)vom 30. November 2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 92-841/4978  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Sascha Grosan ` — partial — gold is substring of pred: `Dr. Sascha Grosan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sascha Grosan`(person)
- `Carla Kurrek`(person)
- `Moosacker 29, 4724 Stocket, Österreich`(address)
- `92-841/4978`(tax_number)

**Example 28** (doc_id: `deanon_BFG_TRAIN/138321.1`) (sent_id: `deanon_BFG_TRAIN/138321.1_1`)


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

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Representative_vertreten_durch`

**F1:** 0.002 | **Precision:** 0.133 | **Recall:** 0.001  

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
| 0.133 | 0.001 | 0.002 | 15 | 2 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 13 | 1581 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Samuel Rehnke, BSc` | `Samuel Rehnke, BSc` |

**Missed by this rule (FN):**

- `Ottfried Bremermann` (person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich` (address)
- `Planetengasse 30, 8455 Bischofegg, Österreich` (address)
- `14-141/9449` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/137275.1`) (sent_id: `deanon_BFG_TRAIN/137275.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Carla Schweykart, Saaz 45, 8413 Stiefing, Österreich, vertreten durch Dr. Elmar Kresbach LL.M., Rechtsanwalt,  Wipplingerstraße 29/9, 1010 Wien, vom 7. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. April 2022, Zl. Zahl, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Elmar Kresbach LL.M.` | `Dr. Elmar Kresbach LL.M.` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Carla Schweykart` (person)
- `Saaz 45, 8413 Stiefing, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Westra ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pastel Pharma`(organisation)
- `Retzenegg 222, 3242 Ramsau, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Intercura Teuhand Revisions ` — partial — pred is substring of gold: `Intercura Teuhand Revisions  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karen Vennemeyer`(person)
- `Neu-Reinbach 11, 4693 Fallholz, Österreich`(address)
- `Intercura Teuhand Revisions  GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen Mag. Willibald Giesser, Eichingerweg 67, 4931 Neulendt, Österreich, vertreten durch HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft, Landstraßer Hauptstraße 27,  1030 Wien, über die Beschwerde des Beschuldigten vom 1. April 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 6,  Abgabenstrafen vom 2. März 2021, Zahl: MA6/206000002559/2020, in Anwesenheit des  Verteidigers und der Behördenvertreterin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der Zurückweisungsbescheid des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `HELLER TAXvisory ` — partial — pred is substring of gold: `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Willibald Giesser`(person)
- `Eichingerweg 67, 4931 Neulendt, Österreich`(address)
- `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`(organisation)

**Example 3** (doc_id: `deanon_BFG_TRAIN/136145.1`) (sent_id: `deanon_BFG_TRAIN/136145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Gernot Sieglen, Oberlederau 7, 4224 Klingenwehr, Österreich  wohnhaft, StNr.: X1, vertreten durch Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010 Wien, betreffend die Berufung vom  25.05.2011 gegen die Einkommensteuerbescheide für die Jahre 2008 und 2009, vom  9.05.2011, zugestellt am 12.05.2011, des Finanzamtes Bruck Eisenstadt Oberwart  zu Recht erkannt

**False Positives:**

- `Dr. Hans Bodendorfer ` — partial — pred is substring of gold: `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gernot Sieglen`(person)
- `Oberlederau 7, 4224 Klingenwehr, Österreich`(address)
- `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`(organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/136516.1`) (sent_id: `deanon_BFG_TRAIN/136516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache ÖkR Alessia Starklof, Oberer Jägerweg 15, 3385 Gerersdorf, Österreich, vertreten durch Birgit Priklopil Steuerberatung  GmbH, Amtshausgasse 1 Tür A, 7132 Frauenkirchen, über die Beschwerde vom 21. April 2021  gegen den Bescheid des Finanzamtes Österreich vom 25. März 2021 betreffend  Einkommensteuer 2019, Steuernummer 83-347/8210, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der Bescheid zu  Ungunsten der Beschwerdeführerin abgeändert.

**False Positives:**

- `Birgit Priklopil Steuerberatung ` — partial — pred is substring of gold: `Birgit Priklopil Steuerberatung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Alessia Starklof`(person)
- `Oberer Jägerweg 15, 3385 Gerersdorf, Österreich`(address)
- `Birgit Priklopil Steuerberatung  GmbH`(organisation)
- `83-347/8210`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/139258.1`) (sent_id: `deanon_BFG_TRAIN/139258.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Ing. Univ.-Prof.in Scarlett Steinfurt, Andreas Schrembser-Straße 30, 2095 Wolfsbach, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Oeynhausen, über die Beschwerde  vom 12. Oktober 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich, Dienststelle 16 Baden Mödling) vom 13. Juli 2017 betreffend  Einkommensteuer 2011 bis 2015 und Umsatzsteuer 2012 bis 2015 sowie Vorauszahlungen an  Einkommensteuer für das Jahr 2017, Steuernummer 59-534/9010   zu Recht erkannt:   I. Die Beschwerde wird hinsichtlich der Bescheide betreffend die Einkommensteuer  der Jahre 2011 – 2013 sowie betreffend die Umsatzsteuer der Jahre 2012 und 2013  gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `LMG ` — partial — pred is substring of gold: `LMG  Steuerberatungsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Univ.-Prof.in Scarlett Steinfurt`(person)
- `Andreas Schrembser-Straße 30, 2095 Wolfsbach, Österreich`(address)
- `LMG  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `59-534/9010`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/139681.1`) (sent_id: `deanon_BFG_TRAIN/139681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Florentin Ginner, Russengasse 3, 4943 Kager, Österreich, vertreten durch TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG, Stadionplatz 2 Tür 3, 8041 Graz, über die Beschwerde vom  4. Oktober 2005 gegen die Bescheide des Finanzamtes Graz-Umgebung (nunmehr Finanzamt  Österreich) vom 29. August 2005 betreffend Umsatzsteuer für die Jahre 2000 – 2003,  Steuernummer 05-330/4121  zu Recht:   I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2000 – 2002 wird Folge  gegeben.

**False Positives:**

- `TPG Wirtschaftstreuhand und ` — partial — pred is substring of gold: `TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Ginner`(person)
- `Russengasse 3, 4943 Kager, Österreich`(address)
- `TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG`(organisation)
- `05-330/4121`(tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/139729.1`) (sent_id: `deanon_BFG_TRAIN/139729.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Brendon Meißnest, Tarnoczygasse 16, 9585 Neumüllnern, Österreich, vertreten durch Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft, Aspernstraße 87/72, 1220 Wien, vom  30. Juni 2016 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 3. Juni 2016 betreffend  Zahlungserleichterungen § 212 BAO 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Tax Wood Audit GmbH ` — partial — pred is substring of gold: `Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brendon Meißnest`(person)
- `Tarnoczygasse 16, 9585 Neumüllnern, Österreich`(address)
- `Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `FA Amstetten Melk Scheibbs`(organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/145451.1`) (sent_id: `deanon_BFG_TRAIN/145451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Herrn KzlR Estelle Kaufholz, Alte Schulgasse 37, 5521 Bairau, Österreich, vertreten durch Eckhardt  SteuerberatungsgmbH, Hauptstraße 58, 7033 Pöttsching, über   1. die Beschwerde vom 7. Februar 2024 gegen den Bescheid des Finanzamtes Österreich  vom 10. Jänner 2024 betreffend Abweisung eines Antrages auf Stundung gemäß § 212  BAO   2.

**False Positives:**

- `Eckhardt ` — partial — pred is substring of gold: `Eckhardt  SteuerberatungsgmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Estelle Kaufholz`(person)
- `Alte Schulgasse 37, 5521 Bairau, Österreich`(address)
- `Eckhardt  SteuerberatungsgmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/145805.1`) (sent_id: `deanon_BFG_TRAIN/145805.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Zoltan Lentze  in der  Beschwerdesache Piedro Goeres, Bräuhausberg 16, 4625 Humplberg, Österreich, vertreten durch Heisinger Steuerberatung  GmbH, Am Teich 12, 7301 Deutschkreutz, betreffend Beschwerde vom 30. Juni 2020 gegen die  Bescheide des Finanzamtes Wien 1/23, nunmehr Finanzamt Österreich, Dienststelle Wien 1/23  vom 9. März 2020 betreffend Wiederaufnahme betreffend Einkommensteuer 2010,  Wiederaufnahme betreffend Einkommensteuer 2011, Wiederaufnahme betreffend  Einkommensteuer 2012, Wiederaufnahme betreffend Einkommensteuer 2013,  Wiederaufnahme betreffend Einkommensteuer 2014, Wiederaufnahme betreffend  Einkommensteuer 2015 und Einkommensteuer 2012 Steuernummer 75-025/8578  beschlossen:   Die Beschwerde vom 30. Juni 2020 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Heisinger Steuerberatung ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Zoltan Lentze`(person)
- `Piedro Goeres`(person)
- `Bräuhausberg 16, 4625 Humplberg, Österreich`(address)
- `75-025/8578`(tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/146359.1`) (sent_id: `deanon_BFG_TRAIN/146359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Wieser in der Beschwerdesache  Jolanda Schloegel, Apfenthal 97, 4070 Seebach, Österreich, vertreten durch Eckbauer Wirtschaftstreuhand Ges.m.b.H.  Steuerberatungsgesellschaft, Wiener Straße 29, 2640 Gloggnitz, betreffend der  Säumnisbeschwerde vom 23.07.2024 wegen behaupteter Verletzung der Entscheidungspflicht  des Finanzamtes Österreich hinsichtlich der Einkommenssteuer (Arbeitnehmerveranlagung)  2022 zu Steuernummer 55-954/7033  beschlossen:  Das Beschwerdeverfahren wird gemäß § 284 Abs 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Eckbauer Wirtschaftstreuhand Ges.m.b.H. ` — partial — pred is substring of gold: `Eckbauer Wirtschaftstreuhand Ges.m.b.H.  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Andreas Wieser`(person)
- `Jolanda Schloegel`(person)
- `Apfenthal 97, 4070 Seebach, Österreich`(address)
- `Eckbauer Wirtschaftstreuhand Ges.m.b.H.  Steuerberatungsgesellschaft`(organisation)
- `55-954/7033`(tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/148282.1`) (sent_id: `deanon_BFG_TRAIN/148282.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Delila Fritzmeier, Joderweg 16, 3333 Sonntagberg, Österreich, vertreten durch Raml und Partner  Steuerberatung GmbH, Museumstraße 31a, 4020 Linz, über die Beschwerde vom 10. Juni 2024  gegen den Bescheid des Finanzamtes Österreich vom 6. Juni 2024 betreffend  Einkommensteuer 2023 zu Steuernummer 04-427/9729  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Raml und Partner ` — partial — pred is substring of gold: `Raml und Partner  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Johann Fischerlehner`(person)
- `Delila Fritzmeier`(person)
- `Joderweg 16, 3333 Sonntagberg, Österreich`(address)
- `Raml und Partner  Steuerberatung GmbH`(organisation)
- `04-427/9729`(tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/148533.1`) (sent_id: `deanon_BFG_TRAIN/148533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Ronald Maichrzik, Walknerhofweg 2, 2813 Pürahöfen, Österreich, vertreten durch Dr. Kohler und Partner  Steuerberatungs GmbH, Schönbrunner Straße 53, 1050 Wien, über   die Beschwerde vom 7. April 2014 gegen die Bescheide des Finanzamtes Wien 8/16/17  (nunmehr Finanzamt Österreich) vom 6. März 2014 betreffend Einkommensteuer und  Umsatzsteuer 2006 bis 2011 und Umsatzsteuer 2012, sowie   die Beschwerde vom 3. März 2016 gegen die Bescheide des Finanzamtes Baden Mödling  (nunmehr Finanzamt Österreich) vom 10. Februar 2016 betreffend Einkommensteuer 2012  und 2013 sowie Umsatzsteuer 2013,  Steuernummer 96-996/1461, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Kohler und Partner ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Maichrzik`(person)
- `Walknerhofweg 2, 2813 Pürahöfen, Österreich`(address)
- `96-996/1461`(tax_number)

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

**F1:** 0.400 | **Precision:** 0.866 | **Recall:** 0.260  

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
| 0.866 | 0.260 | 0.400 | 492 | 426 | 66 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 426 | 66 | 1210 |

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

- `Roxana Gehrbrandt,` — partial — gold is substring of pred: `Roxana Gehrbrandt`

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

**F1:** 0.157 | **Precision:** 0.690 | **Recall:** 0.089  

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
| 0.690 | 0.089 | 0.157 | 210 | 145 | 65 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 145 | 65 | 1491 |

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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/127180.1`) (sent_id: `deanon_BFG_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Bauermeister Getränke, Zur Piesting 7, 8682 Hönigsberg, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 09-169/6729  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Zur Piesting 7, 8682 Hönigsberg, Österreich`(address)
- `09-169/6729`(tax_number)

**Example 2** (doc_id: `deanon_BFG_TRAIN/128877.1`) (sent_id: `deanon_BFG_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers OSR DDr. Heiko Lehwaldt, Point 6, 3232 Zauching, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OSR DDr. Heiko Lehwaldt`(person)
- `Point 6, 3232 Zauching, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/128929.1`) (sent_id: `deanon_BFG_TRAIN/128929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Emmerich Bleekmann  in der Beschwerdesache Dipl.

**False Positives:**

- `Mag. Emmerich Bleekmann ` — partial — gold is substring of pred: `Mag. Emmerich Bleekmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Emmerich Bleekmann`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/130324.1`) (sent_id: `deanon_BFG_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Christoph Mehlbeer, Schötz Gasse 45, 7434 Holzschlag, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Margarete Wiepking  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christoph Mehlbeer`(person)
- `Schötz Gasse 45, 7434 Holzschlag, Österreich`(address)
- `Margarete Wiepking`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/131051.1`) (sent_id: `deanon_BFG_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Kirsten Öllrich, Grundemanngasse 2, 4755 Hub, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Öllrich`(person)
- `Grundemanngasse 2, 4755 Hub, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_TRAIN/131772.1`) (sent_id: `deanon_BFG_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Dipl.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/131922.1`) (sent_id: `deanon_BFG_TRAIN/131922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Bodo Ibel  in der Verwaltungsstrafsache  Fridolin Jodeleid, Stiftergasse 75z, 2262 Stillfried, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in  Verbindung mit § 16 Abs. 1 und Tarifpost B 8 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli  1966, LGBl. für Wien Nr. 20, in der Fassung der Kundmachung ABl.

**False Positives:**

- `Mag. Mag. Bodo Ibel ` — partial — gold is substring of pred: `Mag. Mag. Bodo Ibel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Mag. Bodo Ibel`(person)
- `Fridolin Jodeleid`(person)
- `Stiftergasse 75z, 2262 Stillfried, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_TRAIN/132406.1`) (sent_id: `deanon_BFG_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Karola Birkenzeller, Reifnitz 2, 4532 Rohr im Kremstal, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Pascal Tiessen, Dipl.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karola Birkenzeller`(person)
- `Reifnitz 2, 4532 Rohr im Kremstal, Österreich`(address)
- `Pascal Tiessen`(person)

**Example 10** (doc_id: `deanon_BFG_TRAIN/133042.1`) (sent_id: `deanon_BFG_TRAIN/133042.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Siegfried Borneleit  in der Beschwerdesache Ashley Kutluca,  Pabensteinstraße 20, 5132 Reith, Österreich, über die Beschwerden vom 20. Februar 2020 gegen die Bescheide des  Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 24. Jänner 2020 betreffend   1. Zurückweisung des Antrages vom 2.1.2020 auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2014 und   2.

**False Positives:**

- `Dr. Dr. Siegfried Borneleit ` — partial — gold is substring of pred: `Dr. Dr. Siegfried Borneleit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Siegfried Borneleit`(person)
- `Ashley Kutluca`(person)
- `Pabensteinstraße 20, 5132 Reith, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_TRAIN/133764.1`) (sent_id: `deanon_BFG_TRAIN/133764.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Lorenz Lohkampff  in der Beschwerdesache Dagmar Helmerding,  Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich  vertreten durch Rechtsanwalt Mag. Wolfgang Winkler, Ditscheinergasse 2,  1030 Wien, über die Beschwerde vom 25. Februar 2021 gegen den Bescheid des Magistrates  der Stadt Wien, MA 6, Rechnungs- und Abgabenwesen, Referat Landes- und  Gemeindeabgaben vom 19. Jänner 2021 betreffend Haftung gemäß § 6a des  Kommunalsteuergesetzes 1993 samt Nebenansprüchen (Säumniszuschläge) und § 6a des  Dienstgeberabgabegesetzes zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Lorenz Lohkampff ` — partial — gold is substring of pred: `Mag. Lorenz Lohkampff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Lorenz Lohkampff`(person)
- `Dagmar Helmerding`(person)
- `Landaschluchtgasse 11, 3721 Unterdürnbach, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_TRAIN/133768.1`) (sent_id: `deanon_BFG_TRAIN/133768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Daphne Heinzlmeir, Holzwiesengasse 15, 4723 Natternbach, Österreich, über die Beschwerde vom 20. Mai 2021 gegen den Bescheid des Finanzamtes  Österreich vom 26. April 2021 betreffend Zwangsstrafen 2021 zu Steuernummer  68-502/3247  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Daphne Heinzlmeir`(person)
- `Holzwiesengasse 15, 4723 Natternbach, Österreich`(address)
- `68-502/3247`(tax_number)

**Example 13** (doc_id: `deanon_BFG_TRAIN/134729.1`) (sent_id: `deanon_BFG_TRAIN/134729.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Philipp Dahlhues  in der Beschwerdesache August Combach,  Damweg 1, 7501 Spitzzicken, Österreich, gegen die Bescheide des Finanzamtes Österreich vom   - 11. Juli 2017 betreffend Einkommensteuer 2014 sowie  - 06. Juni 2018 betreffend Einkommensteuer 2016 und 2017  den Beschluss:  I. Die Beschwerde betreffend Einkommensteuer 2014 wird gemäß  § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Philipp Dahlhues ` — partial — gold is substring of pred: `Mag. Philipp Dahlhues`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Philipp Dahlhues`(person)
- `August Combach`(person)
- `Damweg 1, 7501 Spitzzicken, Österreich`(address)

**Example 14** (doc_id: `deanon_BFG_TRAIN/134866.1`) (sent_id: `deanon_BFG_TRAIN/134866.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Daniel Priskorn  in der Beschwerdesache Felix Kerling,  Rassbergstraße 13, 3742 Passendorf, Österreich, wegen behaupteter Verletzung der Entscheidungspflicht des FA St. Johann Tamsweg Zell am See  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 beschlossen:   Die Säumnisbeschwerde wird als unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Daniel Priskorn ` — partial — gold is substring of pred: `Dr. Daniel Priskorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Daniel Priskorn`(person)
- `Felix Kerling`(person)
- `Rassbergstraße 13, 3742 Passendorf, Österreich`(address)
- `FA St. Johann Tamsweg Zell am See`(organisation)

**Example 15** (doc_id: `deanon_BFG_TRAIN/135112.1`) (sent_id: `deanon_BFG_TRAIN/135112.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dr. Zlatan Deisen  in der Beschwerdesache des  Prof. Richard Paulick, Scharmühlwinkel 13, 3144 Baumgarten, Österreich, über 1) die Beschwerde vom 27.9.2017 gegen den Bescheid des  Finanzamtes Bruck Leoben Mürzzuschlag (nunmehr Finanzamt Österreich) vom 4.9.2017  betreffend Umsatzsteuer 2015 sowie über 2) die Beschwerde vom 7.9.2018 gegen den  Bescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 21.8.2018 betreffend Abweisung  von Anträgen auf Aufhebung der Bescheide hinsichtlich Umsatzsteuer 2011 bis 2014 nach  Durchführung einer mündlichen Verhandlung am 2.12.2021 zu Recht erkannt:   I. Den Beschwerden wird Folge gegeben.

**False Positives:**

- `Dr. Dr. Zlatan Deisen ` — partial — gold is substring of pred: `Dr. Dr. Zlatan Deisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. Zlatan Deisen`(person)
- `Prof. Richard Paulick`(person)
- `Scharmühlwinkel 13, 3144 Baumgarten, Österreich`(address)

**Example 16** (doc_id: `deanon_BFG_TRAIN/135347.1`) (sent_id: `deanon_BFG_TRAIN/135347.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache DDr. DDr. Björn Wöber, Bisamgasse 3i, 9433 Tschrietes, Österreich, betreffend Beschwerde vom 27. Oktober 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 9. Oktober 2020 zu Steuernummer  60-281/1996  betreffend Abweisung des Antrages auf Zuerkennung der Familienbeihilfe für  KommR Hugo Vollpracht  ab Oktober 2019 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `R.` — similar text (different position): `DDr. DDr. Björn Wöber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. DDr. Björn Wöber`(person)
- `Bisamgasse 3i, 9433 Tschrietes, Österreich`(address)
- `60-281/1996`(tax_number)
- `KommR Hugo Vollpracht`(person)

**Example 17** (doc_id: `deanon_BFG_TRAIN/135585.1`) (sent_id: `deanon_BFG_TRAIN/135585.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Charles Schindele  in der Beschwerdesache Gregor Branz,  Tandlerstraße 7, 9341 Herd, Österreich, vertreten durch die Germuth Steuerberatungs GmbH, Johannesgasse 16/5,  1010 Wien, über die Beschwerde vom 17. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 14. Juli 2021 betreffend Nachsicht gemäß § 236 BAO, Steuernummer  79-519/7411  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Charles Schindele ` — partial — gold is substring of pred: `Mag. Charles Schindele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Charles Schindele`(person)
- `Gregor Branz`(person)
- `Tandlerstraße 7, 9341 Herd, Österreich`(address)
- `79-519/7411`(tax_number)

**Example 18** (doc_id: `deanon_BFG_TRAIN/135774.1`) (sent_id: `deanon_BFG_TRAIN/135774.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache MedR Uwe Preikschas, Marika Rökk-Straße 67, 3131 Anzenberg, Österreich, über die Beschwerde vom 19. Februar 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019, Steuernummer 19-302/7367, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO – wie mit Beschwerdevorentscheidung vom 26. April  2021 – teilweise Folge gegeben und der angefochtene Bescheid in diesem Sinne abgeändert.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MedR Uwe Preikschas`(person)
- `Marika Rökk-Straße 67, 3131 Anzenberg, Österreich`(address)
- `19-302/7367`(tax_number)

**Example 19** (doc_id: `deanon_BFG_TRAIN/136313.1`) (sent_id: `deanon_BFG_TRAIN/136313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger im  Beschwerdeverfahren über die Beschwerde der Verl nach XY, vertreten durch Laurence Krekemeyer,  Steyersberg 2, 8481 Priebing, Österreich  vom 20. Juli 2021 gegen den Zurückweisungsbescheid des Finanzamtes  Österreich vom 7. Juli 2021 betreffend Antrag auf Durchführung einer  Arbeitnehmerveranlagung, beschlossen:  Der Vorlageantrag der Beschwerdeführerin Verl nach XY vom 10.9.2021 wird gemäß § 260 Abs.  1 BAO iVm § 264 BAO (insbesondere Abs. 4 lit e und Abs. 5) als nicht zulässig zurückgewiesen.

**False Positives:**

- `Dr. Ansgar Unterberger im  Beschwerdeverfahren` — partial — gold is substring of pred: `Dr. Ansgar Unterberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ansgar Unterberger`(person)
- `Laurence Krekemeyer`(person)
- `Steyersberg 2, 8481 Priebing, Österreich`(address)

**Example 20** (doc_id: `deanon_BFG_TRAIN/137032.1`) (sent_id: `deanon_BFG_TRAIN/137032.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_TRAIN/137355.1`) (sent_id: `deanon_BFG_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_TRAIN/137456.1`) (sent_id: `deanon_BFG_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Theobald Korschinek  in der Beschwerdesache der Frau  Dieter Papakiriakou, Karl Eichinger-Straße 8g, 9074 Linden, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Dr. Theobald Korschinek ` — partial — gold is substring of pred: `Dr. Theobald Korschinek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Theobald Korschinek`(person)
- `Dieter Papakiriakou`(person)
- `Karl Eichinger-Straße 8g, 9074 Linden, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_TRAIN/137493.1`) (sent_id: `deanon_BFG_TRAIN/137493.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Herbert Kramp, Kinkstraße 6, 3541 Senftenberg, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Waldviertel, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend Abweisung des  Antrages auf Gewährung der vollen nichtindexierten Familienbeihilfe ab Jänner 2019,  Steuernummer 15-114/2120, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Herbert Kramp`(person)
- `Kinkstraße 6, 3541 Senftenberg, Österreich`(address)
- `15-114/2120`(tax_number)

**Example 24** (doc_id: `deanon_BFG_TRAIN/137516.1`) (sent_id: `deanon_BFG_TRAIN/137516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Friedhelm Servais, Ölbrennerweg 38, 5231 Wiesing, Österreich, über die Beschwerde vom 15. Oktober 2020 gegen den Bescheid des Finanzamtes  Österreich vom 1. Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 86-385/7500  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Friedhelm Servais`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Friedhelm Servais`(person)
- `Ölbrennerweg 38, 5231 Wiesing, Österreich`(address)
- `86-385/7500`(tax_number)

**Example 25** (doc_id: `deanon_BFG_TRAIN/137596.1`) (sent_id: `deanon_BFG_TRAIN/137596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Egon Hintenberg  in der Beschwerdesache des  OMedR Rafaela Balcius, Hoferweg 3, 3033 Manzing, Österreich, über die Beschwerde vom 11. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Egon Hintenberg ` — partial — gold is substring of pred: `Mag. Egon Hintenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Egon Hintenberg`(person)
- `OMedR Rafaela Balcius`(person)
- `Hoferweg 3, 3033 Manzing, Österreich`(address)

**Example 26** (doc_id: `deanon_BFG_TRAIN/137664.1`) (sent_id: `deanon_BFG_TRAIN/137664.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Dr. Emanuel Rauschmeir  in der Beschwerdesache Bertha Hueber,  Schirnes 10, 9871 Kötzing, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, betreffend Beschwerden vom 11. Februar 2020 und 27. Februar 2020  gegen die Bescheide betreffend Feststellungsbescheid Gruppenmitglied 2014 vom 11. Februar  2020 sowie vom 13. Jänner 2020 betreffend Feststellungsbescheid Gruppenmitglied 2015 und  2016 jeweils des Finanzamtes Wien 1/23 den Beschluss:   I. Die Beschwerden werden gemäß § 278 Abs. 1 lit b iVm § 256 Abs. 3 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Dr. Emanuel Rauschmeir ` — partial — gold is substring of pred: `Dr. Emanuel Rauschmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Emanuel Rauschmeir`(person)
- `Bertha Hueber`(person)
- `Schirnes 10, 9871 Kötzing, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_TRAIN/138011.1`) (sent_id: `deanon_BFG_TRAIN/138011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Sascha Grosan  in der Beschwerdesache Carla Kurrek,  Moosacker 29, 4724 Stocket, Österreich, über die Beschwerde vom 30. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Kirchdorf Perg Steyr)vom 30. November 2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 92-841/4978  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Sascha Grosan ` — partial — gold is substring of pred: `Dr. Sascha Grosan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sascha Grosan`(person)
- `Carla Kurrek`(person)
- `Moosacker 29, 4724 Stocket, Österreich`(address)
- `92-841/4978`(tax_number)

**Example 28** (doc_id: `deanon_BFG_TRAIN/138321.1`) (sent_id: `deanon_BFG_TRAIN/138321.1_1`)


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

## `Herr_Name`

**F1:** 0.063 | **Precision:** 0.794 | **Recall:** 0.033  

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
| 0.794 | 0.033 | 0.063 | 68 | 54 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 54 | 14 | 1575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129140.1`) (sent_id: `deanon_BFG_TRAIN/129140.1_49`)


Die  Fahrzeugschlüssel und Papiere wurden von Herrn OStR Karl Ostendarp  oder Frau AB persönlich  entgegengenommen und im Büro versperrt aufbewahrt.

| Predicted | Gold |
|---|---|
| `OStR Karl Ostendarp` | `OStR Karl Ostendarp` |

**Example 1** (doc_id: `deanon_BFG_TRAIN/129950.1`) (sent_id: `deanon_BFG_TRAIN/129950.1_5`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Denise Adamske – machte in der Erklärung zur Arbeitnehmer-

| Predicted | Gold |
|---|---|
| `Denise Adamske` | `Denise Adamske` |

**Example 2** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_30`)


Lfd.Nr. Bezeichnung der körperlichen, geistigen oder sinnesbedingten  Funktionseinschränkungen, welche voraussichtlich länger als sechs Monate andauern werden:  Begründung der Rahmensätze: Pos.Nr. Gdb%  1 paranoide Schizophrenie  Unterer Rahmensatz, da verminderte psychische Belastbarkeit 03.07.02 50  Gesamtgrad der Behinderung 50 v. H.  Begründung für den Gesamtgrad der Behinderung:  Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keine Änderung gegenüber dem VGA von 9/2015  der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 07/2014  Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 3** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_113`)


Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 4** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_178`)


Vorgutachten 14 08 2018:   paranoide Schizophrenie GdB 50%   seit 07/2014   Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA    Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 5** (doc_id: `deanon_BFG_TRAIN/130423.1`) (sent_id: `deanon_BFG_TRAIN/130423.1_225`)


Herr Daisy Mikoleizik  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA   Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Daisy Mikoleizik` | `Daisy Mikoleizik` |

**Example 6** (doc_id: `deanon_BFG_TRAIN/130533.1`) (sent_id: `deanon_BFG_TRAIN/130533.1_57`)


Der Mietvertrag lautet auf Herrn Lukasz Jan Chlebek.

| Predicted | Gold |
|---|---|
| `Lukasz Jan Chlebek` | `Lukasz Jan Chlebek` |

**Example 7** (doc_id: `deanon_BFG_TRAIN/131561.1`) (sent_id: `deanon_BFG_TRAIN/131561.1_75`)


Als Beispiel ist das bereits zweimal  stattgefundene Verkaufstraining mit Herrn Hubert Mann zu nennen (siehe Beilagen).

| Predicted | Gold |
|---|---|
| `Hubert Mann` | `Hubert Mann` |

**Example 8** (doc_id: `deanon_BFG_TRAIN/132743.1`) (sent_id: `deanon_BFG_TRAIN/132743.1_73`)


Im Schreiben der Privatklink vom 21. Oktober 2019 wird auszugsweise ausgeführt:  "Herr Ernestine Schittenhelm  stellte sich bei uns am 07.11.2017 erstmals vor.

| Predicted | Gold |
|---|---|
| `Ernestine Schittenhelm` | `Ernestine Schittenhelm` |

**Example 9** (doc_id: `deanon_BFG_TRAIN/132810.1`) (sent_id: `deanon_BFG_TRAIN/132810.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Herr Stanislaus Calisir (= Beschwerdeführer, Bf), vertreten lt. Vollmacht durch AA, hat am  30.5.2012 zu dem für Privatzwecke erworbenen Fahrzeug XY (gebraucht, Leistung 92 kW,  Diesel, CO2-Emission 228g/km) die Normverbrauchsabgabe (NoVA) erklärt.

| Predicted | Gold |
|---|---|
| `Stanislaus Calisir` | `Stanislaus Calisir` |

**Example 10** (doc_id: `deanon_BFG_TRAIN/133433.1`) (sent_id: `deanon_BFG_TRAIN/133433.1_37`)


Herr Huberta Schwandt  wird ohne sachliche Grundlage um 123 TEUR entreichert, während in  vergleichbaren Fällen im betrieblichen Bereich dies nicht geschieht.

| Predicted | Gold |
|---|---|
| `Huberta Schwandt` | `Huberta Schwandt` |

**Example 11** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_8`)


Frau Frau erhob gegen die zwei Strafverfügungen 1) und 2) bei der MA 67 am 08.05.2021  Einspruch und brachte vor „Hiermit geben wir bekannt, dass Herr Cynthia Neureuter  nicht Halter des  Fahrzeugs mit dem Kennzeichen 123 ist“.

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 12** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Cynthia Neureuter  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 13** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_26`)


Deshalb sei Frau Frau mit Schreiben der Magistratsabteilung 67 vom 09.06.2021 aufgefordert  worden, binnen zwei Wochen eine für das Verwaltungsstrafverfahren gültige Vollmacht von  Herrn Cynthia Neureuter  zu übermitteln.

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 14** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_28`)


Am 23.06.2021 sei von Herrn  Cynthia Neureuter  lediglich ein Schreiben mit folgendem Inhalt übermittelt worden: „Bezugnehmend  auf Ihr Schreiben an Frau Frau vom 09.06.2021 möchte ich hiermit eigenhändig bestätigen,  dass das Fahrzeug mit dem angegebenen Kennzeichen nicht in meinem Besitz ist und ich auch  nicht weiß, wem es gehört“.

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 15** (doc_id: `deanon_BFG_TRAIN/134652.1`) (sent_id: `deanon_BFG_TRAIN/134652.1_38`)


Herr Cynthia Neureuter  sei persönlich bei genannter Firma  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Cynthia Neureuter` | `Cynthia Neureuter` |

**Example 16** (doc_id: `deanon_BFG_TRAIN/134762.1`) (sent_id: `deanon_BFG_TRAIN/134762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Simon Zens  in der Beschwerdesache Miriam Große-Bley,  Tipschern 13, 4052 Fürhappen, Österreich, vertreten durch Herrn Michael Haberl, Steuerberater, Hauptstraße 65, 8962  Gröbming, über die Beschwerde vom 9.7.2018 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 12.6.2018 betreffend Festsetzung des Dienstgeberbeitrages (DB) für die  Jahre 2013, 2014, 2015 und 2016 sowie des Zuschlages zum Dienstgeberbeitrag (DZ) für die  Jahre 2013, 2014, 2015 und 2016 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Michael Haberl` | `Michael Haberl` |

**Missed by this rule (FN):**

- `Priv.-Doz. Simon Zens` (person)
- `Miriam Große-Bley` (person)
- `Tipschern 13, 4052 Fürhappen, Österreich` (address)

**Example 17** (doc_id: `deanon_BFG_TRAIN/136573.1`) (sent_id: `deanon_BFG_TRAIN/136573.1_71`)


Weiters verweise ich auf das Steuersparbuch von Herrn Eduard Müller,  Mitarbeiter im BM für Finanzen, welcher die Ausgaben für eine Coaching Ausbildung für  Führungskräfte bestätigt.

| Predicted | Gold |
|---|---|
| `Eduard Müller` | `Eduard Müller` |

**Example 18** (doc_id: `deanon_BFG_TRAIN/137289.1`) (sent_id: `deanon_BFG_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Natascha Daschmann (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Natascha Daschmann` | `Natascha Daschmann` |

**Example 19** (doc_id: `deanon_BFG_TRAIN/139959.1`) (sent_id: `deanon_BFG_TRAIN/139959.1_48`)


Begründung – GdB liegt rückwirkend vor:  Herr Evelyn Walz  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Auf Grund von fehlender Vorlage medizinischer Befunde ist keine Einschätzung der  Selbsterhaltungsfähigkeit möglich.“

| Predicted | Gold |
|---|---|
| `Evelyn Walz` | `Evelyn Walz` |

**Example 20** (doc_id: `deanon_BFG_TRAIN/140210.1`) (sent_id: `deanon_BFG_TRAIN/140210.1_8`)


Aufgrund von persönlichen Wahrnehmungen einer Finanzbediensteten (sich auf der  Windschutzscheibe des streitgegenständlichen Kraftfahrzeuges befindende österreichische  Vignetten) vor dem Finanzamt Innsbruck wurde Herr Brunhild Hoffschulz (= Beschwerdeführer, Bf) zur  Sachverhaltsdarstellung – Nutzung eines Kraftfahrzeuges mit rumänischem Kennzeichen – mit  1 von 20 Seite 2 von 20

| Predicted | Gold |
|---|---|
| `Brunhild Hoffschulz` | `Brunhild Hoffschulz` |

**Example 21** (doc_id: `deanon_BFG_TRAIN/141435.1`) (sent_id: `deanon_BFG_TRAIN/141435.1_4`)


Begründung  Verfahrensgang:  MA67/226701281451/2022:  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner  2023, Zahl: MA67/226701281451/2022, wurde Herr Robert Grentzmann (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von einem 14 Stunden verhängt sowie ein  Verfahrenskostenbeitrag von € 10,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Robert Grentzmann` | `Robert Grentzmann` |

**Example 22** (doc_id: `deanon_BFG_TRAIN/141974.1`) (sent_id: `deanon_BFG_TRAIN/141974.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Gottfried Kroehner – bezog im Jahr 2021 Bezüge durch die  Österreichische Gesundheitskasse in Form eines Wiedereingliederungsgeldes gemäß § 143d  ASVG für 132 Tage in Höhe von 19,09 € brutto täglich, ds 2.519,88 €.

| Predicted | Gold |
|---|---|
| `Gottfried Kroehner` | `Gottfried Kroehner` |

**Example 23** (doc_id: `deanon_BFG_TRAIN/142976.1`) (sent_id: `deanon_BFG_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Nikolaus Thulke (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Nikolaus Thulke` | `Nikolaus Thulke` |

**Example 24** (doc_id: `deanon_BFG_TRAIN/144254.1`) (sent_id: `deanon_BFG_TRAIN/144254.1_94`)


Das beanstandete Fahrzeug wurde zum  Tatzeitpunkt von Herrn Wilfried Körbelin  gelenkt.

| Predicted | Gold |
|---|---|
| `Wilfried Körbelin` | `Wilfried Körbelin` |

**Example 25** (doc_id: `deanon_BFG_TRAIN/144254.1`) (sent_id: `deanon_BFG_TRAIN/144254.1_95`)


Bitte beantworten Sie innerhalb von zwei Wochen ab Zustellung dieses Schreibens brieflich oder  per E-Mail folgende Fragen:  Wurden  - Sie innerhalb der letzten 2 Monate, insbesondere am 14.06.2023, von Herrn Wilfried Körbelin  mit  dem Fahrzeug mit dem behördlichen Kennzeichen Vienna befördert oder haben Sie dieses selbst  gelenkt?  - Kopien Ihres Ausweises gemäß § 29b StVO gemacht?

| Predicted | Gold |
|---|---|
| `Wilfried Körbelin` | `Wilfried Körbelin` |

**Example 26** (doc_id: `deanon_BFG_TRAIN/144576.1`) (sent_id: `deanon_BFG_TRAIN/144576.1_13`)


Bitte beantworten Sie innerhalb von zwei Wochen ab Zustellung dieses Schreibens brieflich oder  per E-Mail folgende Fragen:   Wurden  - Sie am 04.04.2023 von Herrn Ivan Färbers  mit dem Fahrzeug mit dem behördlichen  Kennzeichen Vienna befördert oder haben Sie dieses Fahrzeug selbst gelenkt?  - Kopien Ihres Ausweises gemäß § 29b StVO gemacht?

| Predicted | Gold |
|---|---|
| `Ivan Färbers` | `Ivan Färbers` |

**Example 27** (doc_id: `deanon_BFG_TRAIN/144625.1`) (sent_id: `deanon_BFG_TRAIN/144625.1_22`)


unentgeltlich an Herrn Ludmilla Seubel  übertragen.

| Predicted | Gold |
|---|---|
| `Ludmilla Seubel` | `Ludmilla Seubel` |

**Example 28** (doc_id: `deanon_BFG_TRAIN/144851.1`) (sent_id: `deanon_BFG_TRAIN/144851.1_6`)


Entscheidungsgründe  Mit Straferkenntnis vom 16. April 2024, Zahl: MA67/246700162299/2024, hat der Magistrat  der Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Leonhard Facci (in weiterer  Folge: Beschwerdeführer – Bf) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt  indem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen I-57 VS  am  2. Februar 2024 um 09:20 Uhr in einer gebührenpflichtigen Kurzparkzone in 1210 Wien,  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Leonhard Facci` | `Leonhard Facci` |

**Missed by this rule (FN):**

- `I-57 VS` (vehicle_license)

**Example 29** (doc_id: `deanon_BFG_TRAIN/145067.1`) (sent_id: `deanon_BFG_TRAIN/145067.1_16`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:    ja  GdB liegt vor seit:   03/2022  Herr Olaf Klockmeier  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  JA  Dies besteht seit:      03/2022  2 von 14 Seite 3 von 14

| Predicted | Gold |
|---|---|
| `Olaf Klockmeier` | `Olaf Klockmeier` |

**Example 30** (doc_id: `deanon_BFG_TRAIN/145067.1`) (sent_id: `deanon_BFG_TRAIN/145067.1_56`)


Herr Olaf Klockmeier  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  JA  Dies besteht seit:      03/2022  Anmerkung bzw Begründung betreffend die Fähigkeit bzw voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Aus den vorliegenden Unterlagen geht nicht genau hervor, ab welchem Zeitpunkt eine  dauerhafte Erwerbsunfähigkeit bestanden hat.

| Predicted | Gold |
|---|---|
| `Olaf Klockmeier` | `Olaf Klockmeier` |

**Example 31** (doc_id: `deanon_BFG_TRAIN/145271.1`) (sent_id: `deanon_BFG_TRAIN/145271.1_27`)


In weiterer Folge wurde dieser von Herrn Jan Kaspeizer  nicht behoben und gelangte zurück an die  Finanzstrafbehörde.

| Predicted | Gold |
|---|---|
| `Jan Kaspeizer` | `Jan Kaspeizer` |

**Example 32** (doc_id: `deanon_BFG_TRAIN/145451.1`) (sent_id: `deanon_BFG_TRAIN/145451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Herrn KzlR Estelle Kaufholz, Alte Schulgasse 37, 5521 Bairau, Österreich, vertreten durch Eckhardt  SteuerberatungsgmbH, Hauptstraße 58, 7033 Pöttsching, über   1. die Beschwerde vom 7. Februar 2024 gegen den Bescheid des Finanzamtes Österreich  vom 10. Jänner 2024 betreffend Abweisung eines Antrages auf Stundung gemäß § 212  BAO   2.

| Predicted | Gold |
|---|---|
| `KzlR Estelle Kaufholz` | `KzlR Estelle Kaufholz` |

**Missed by this rule (FN):**

- `Alte Schulgasse 37, 5521 Bairau, Österreich` (address)
- `Eckhardt  SteuerberatungsgmbH` (organisation)

**Example 33** (doc_id: `deanon_BFG_TRAIN/145451.1`) (sent_id: `deanon_BFG_TRAIN/145451.1_4`)


Entscheidungsgründe  Bisheriger Verfahrensgang:  I. In einem über FinanzOnline gestellten Antrag vom 18. Dezember 2023 beantragte Herr  KzlR Estelle Kaufholz  eine Stundung bis 28. Juni 2024 für den aktuellen Gesamtrückstand mit der  Begründung, dass „aufgrund der derzeitigen Liquiditätssituation unseres Mandanten ist die  sofortige volle Entrichtung der angeführten Abgaben nur mittels zusätzlicher Aufnahme von  Fremdkapital möglich und daher mit erheblichen Härten verbunden.

| Predicted | Gold |
|---|---|
| `KzlR Estelle Kaufholz` | `KzlR Estelle Kaufholz` |

**Example 34** (doc_id: `deanon_BFG_TRAIN/145555.1`) (sent_id: `deanon_BFG_TRAIN/145555.1_2`)


Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat in der Beschwerdesache  Xenia Oberaigner, Landsturmstraße 28, 5222 Haidberg, Österreich  Steuernummer: 30-622/5363, vertreten durch den  Steuerberater Herrn Martin Friedl, Marktplatz 2, 4650 Lambach, zur Beschwerde vom 6.  Oktober 2022 gegen den Bescheid des Finanzamtes Österreich vom 19. September 2022 über  die Festsetzung der Kapitalertragsteuer für den Zeitraum 2020 den Beschluss:      I. Die Beschwerde wird an das vorlegende Finanzamt Österreich weiter- bzw.  rückgeleitet.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Xenia Oberaigner` (person)
- `Landsturmstraße 28, 5222 Haidberg, Österreich` (address)
- `30-622/5363` (tax_number)

**Example 35** (doc_id: `deanon_BFG_TRAIN/146062.1`) (sent_id: `deanon_BFG_TRAIN/146062.1_127`)


Gesellschafter der beschwerdeführenden Partei waren im  beschwerdegegenständlichen Jahr Herr Eugenia Reinholdt  und Herr Ing. Eugenia Reinholdt.

| Predicted | Gold |
|---|---|
| `Eugenia Reinholdt` | `Eugenia Reinholdt` |

**Example 36** (doc_id: `deanon_BFG_TRAIN/146062.1`) (sent_id: `deanon_BFG_TRAIN/146062.1_137`)


Diese Mitteilung wurde vom Geschäftsführer des  Unternehmens, Herrn Eugenia Reinholdt  am 22.09.2021 um 08:49 Uhr gelesen.

| Predicted | Gold |
|---|---|
| `Eugenia Reinholdt` | `Eugenia Reinholdt` |

**Example 37** (doc_id: `deanon_BFG_TRAIN/146476.1`) (sent_id: `deanon_BFG_TRAIN/146476.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Herr MedR Florentine Wägemann (in der Folge kurz: Bf.) brachte am 19.2.2024 den Antrag auf  Arbeitnehmerveranlagung für das Jahr 2023 per Finanzonline ein.

| Predicted | Gold |
|---|---|
| `MedR Florentine Wägemann` | `MedR Florentine Wägemann` |

**Example 38** (doc_id: `deanon_BFG_TRAIN/147143.1`) (sent_id: `deanon_BFG_TRAIN/147143.1_5`)


Im Zuge einer Anhaltung durch die Finanzpolizei am 10.7.2015, 22:55 Uhr, in A-Ort1,XStr, hat  der Lenker des Fahrzeuges VW Touareg mit dem ausländischen Kennzeichen XX1, FIN Nr123,  Herr Kirstin Lünebach (= Beschwerdeführer, Bf) angegeben, dass Zulassungsbesitzerin des Fahrzeuges  die Fa. A-GmbH in D-Ort2 ist und er sich auf der Fahrt nach Hause befindet.

| Predicted | Gold |
|---|---|
| `Kirstin Lünebach` | `Kirstin Lünebach` |

**Example 39** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Einkommensteuerbescheid (Arbeitnehmerveranlagung) vom 1. März 2024 wurde die  Einkommensteuer von Herrn Bernhard Siegmundt (im Folgenden auch Beschwerdeführer oder Bf.) für das  Jahr 2023 mit einer Gutschrift in Höhe von EUR 29,- festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 40** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_25`)


 In der zweiten Monatshälfte des Juli 2023 hat Herr Bernhard Siegmundt  eine Beschäftigung bei der  Arbeitgeber Wien in Adr Arbeitgeber Wien, begonnen.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 41** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_29`)


Herr Bernhard Siegmundt  verfügte im Jahr 2023 über zwei Wohnsitze:   Herr Bernhard Siegmundt  hat seit 1. Juli 2020 einen Wohnsitz in einer Mietwohnung in Grabental 83, 9300 Goggerwenig, Österreich.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Grabental 83, 9300 Goggerwenig, Österreich` (address)

**Example 42** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_32`)


 Weiters verfügt Herr Bernhard Siegmundt  über einen Wohnsitz in einem Haus in Ungarn in der Adr  Wohnsitz Ungarn.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 43** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_38`)


Der Lebensmittelpunkt von Herrn Bernhard Siegmundt  liegt in Österreich.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 44** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_39`)


2. Beweiswürdigung  Der Sachverhalt zu den beiden Dienstverhältnissen von Herrn Bernhard Siegmundt  im Jahr 2023 ergibt  sich aus den Angaben zu Lohnzettel und Meldungen im Einkommensteuerbescheid 2023 sowie  aus den Antworten von Herrn Bernhard Siegmundt  auf die Vorhalte der belangten Behörde und des  Bundesfinanzgerichtes.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 45** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_41`)


Die Feststellungen zu den beiden Wohnsitzen basieren auf den von Herrn Bernhard Siegmundt  zur  Verfügung gestellten Unterlagen (Mietvertrag der Wohnung in Österreich, Grundbuchsauszug  aus Ungarn, ungarische Adresskarte) und seinen Erläuterungen im Rahmen der Beantwortung  der Vorhalte der belangten Behörde und des Bundesfinanzgerichtes.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 46** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_44`)


 Mit Österreich verbindet Herrn Bernhard Siegmundt  seine Lebenspartnerin, sein Arbeitsplatz und  seine langfristigen Pläne, sodass seine Bindung zu Österreich stärker ist.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 47** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_45`)


Auch als Herr  Bernhard Siegmundt  nach Österreich gekommen ist, hatte er bereits geplant für längere Zeit in  Österreich zu bleiben.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 48** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_48`)


Die  Lebenspartnerin von Herrn Bernhard Siegmundt  lebt und arbeitet ebenfalls in Österreich.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 49** (doc_id: `deanon_BFG_TRAIN/148943.1`) (sent_id: `deanon_BFG_TRAIN/148943.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Florentine Gößelein  in der Beschwerdesache des Herrn  Harald Haffner, Mondseebergstraße 13, 3204 Kirchberggegend, Österreich, über die Beschwerde vom 06. Juni 2025 (beim  Bundesfinanzgericht eingelangt am 13.06.2025), wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich, betreffend  die Beschwerde vom 30.11.2024 gegen den Einkommensteuerbescheid 2023  (Arbeitnehmerveranlagung) vom 25.10.2024  zu der Steuernummer 80-806/1585  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `Harald Haffner` | `Harald Haffner` |

**Missed by this rule (FN):**

- `Dr.in Florentine Gößelein` (person)
- `Mondseebergstraße 13, 3204 Kirchberggegend, Österreich` (address)
- `80-806/1585` (tax_number)

**Example 50** (doc_id: `deanon_BFG_TRAIN/148943.1`) (sent_id: `deanon_BFG_TRAIN/148943.1_3`)


Begründung:  Herr Harald Haffner  hat mit Eingabe vom 06.06.2025 eingelangt am 13.06.2025, gemäß § 284 Abs 1  BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht über die  Beschwerde vom 30.11.2024 gegen den Einkommensteuerbescheid 2023 vom 25.10.2024  erhoben.

| Predicted | Gold |
|---|---|
| `Harald Haffner` | `Harald Haffner` |

**Example 51** (doc_id: `deanon_BFG_TRAIN/149511.1`) (sent_id: `deanon_BFG_TRAIN/149511.1_5`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, MA 67 lastete mit Strafverfügung vom 10. Juli 2025,  GZ. MA67/MA-GZ/2025, dem nunmehrigen Beschwerdeführer (Bf.), Herrn Bertha Goldhammer  an, er  habe als zur Vertretung nach außen Berufener der Zulassungsbesitzerin (ZLB) des Fahrzeugs  mit dem behördlichen Kennzeichen SW-Kennz. (A), dem ordnungsgemäß zugestellten  Verlangen der Behörde, innerhalb von zwei Wochen ab Zustellung bekanntzugeben, wem das  Fahrzeug überlassen worden war, sodass dieses am 08. April 2025 um 11:07 Uhr in 1220 Wien,  Saltenstraße gegenüber 11 gestanden ist, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Bertha Goldhammer` | `Bertha Goldhammer` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/128730.1`) (sent_id: `deanon_BFG_TRAIN/128730.1_5`)


Entscheidungsgründe  Zum Erkenntnis: Mit Bescheid des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013 wurden  die Anspruchszinsen 2007 für die Einkommensteuernachforderung 2007 von Herrn Bauermeister Getränke,  nunmehr Bauermeister Getränke (in weiterer Folge: Bf.) in einer Höhe von € 27.080,78 festgesetzt.

**False Positives:**

- `Bauermeister Getränke` — type mismatch — same span as gold: `Bauermeister Getränke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bauermeister Getränke`(organisation)
- `Bauermeister Getränke`(organisation)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Ronald Kleile, Bakk. rer. nat., Fischteichweg 49, 4924 Hartlberg, Österreich, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 15. März 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 20. Februar 2019, Strafnummer 007, in Anwesenheit des  Beschuldigten, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Über Ronald Kleile, Bakk. rer. nat.  wird gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 17.600,00  verhängt.

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)
- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 2** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_6`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 20. Februar 2019,  Strafnummer 007, wurde Herr Ronald Kleile, Bakk. rer. nat., geb. 1989, Geschäftsführer, wohnhaft in Fischteichweg 49, 4924 Hartlberg, Österreich  in Abwesenheit schuldig erkannt,   „A.) er hat in Wien vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von  1 von 18 Seite 2 von 18

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)
- `Fischteichweg 49, 4924 Hartlberg, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_140`)


Gesellschafter/Geschäftsführer der H- GmbH ist Herr Ronald Kleile, Bakk. rer. nat..

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat..`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat..`(person)

**Example 4** (doc_id: `deanon_BFG_TRAIN/131396.1`) (sent_id: `deanon_BFG_TRAIN/131396.1_161`)


Zwischen Herrn Ronald Kleile, Bakk. rer. nat., Alleingesellschafter und einziger Geschäftsführer der H- GmbH und  Herrn S., seinem Vater, bestand und besteht nicht nur eine persönliche, sondern auch eine  wirtschaftliche Nahebeziehung.

**False Positives:**

- `Ronald Kleile` — partial — pred is substring of gold: `Ronald Kleile, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Kleile, Bakk. rer. nat.`(person)

**Example 5** (doc_id: `deanon_BFG_TRAIN/134402.1`) (sent_id: `deanon_BFG_TRAIN/134402.1_195`)


Seit 1.8.2014 ist auch Herr DI FG5 Geschäftsführer.

**False Positives:**

- `DI FG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_TRAIN/136573.1`) (sent_id: `deanon_BFG_TRAIN/136573.1_126`)


Weiters darf ich auf Aussagen von Herrn Dipl Kfm Eduard Müller, Mitarbeiter im BMF, im  Steuerbuch verweisen, welcher die Ausgaben für eine Coaching-Ausbildung für Führungskräfte  bestätigt.

**False Positives:**

- `Dipl Kfm Eduard Müller` — partial — gold is substring of pred: `Dipl Kfm`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl Kfm`(person)
- `Eduard Müller`(person)

**Example 7** (doc_id: `deanon_BFG_TRAIN/138117.1`) (sent_id: `deanon_BFG_TRAIN/138117.1_41`)


Infolge des  Testamentes und der Eröffnungsniederschrift vom 26.6.2020 sind gesetzliche Erben des  Nachlasses: Die Ehegattin Frau Vorname Vorname2 Nachname, zu 50 % des Erbteiles, der Sohn  Herr G A Nachname zu 25 % des Erbteiles sowie Herr AC Nachname zu 25 % des Erbteiles.

**False Positives:**

- `AC Nachname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_TRAIN/138498.1`) (sent_id: `deanon_BFG_TRAIN/138498.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Im Rahmen der am 17.02.2020 eingereichten Erklärung zur Arbeitnehmerveranlagung 2019  wurde durch Herrn Zacharias Arhelger, BA (in der Folge „Bf“ oder „Beschwerdeführer“) die Gewährung des  (ganzen) Familienbonus Plus für 12 Monate beantragt.

**False Positives:**

- `Zacharias Arhelger` — partial — pred is substring of gold: `Zacharias Arhelger, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zacharias Arhelger, BA`(person)

**Example 9** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_19`)


Der Bf. beantwortete den Vorhalt mit Schreiben vom 15. Jänner 2013 wie folgt:  "Frau W und Herr M T haben bei Herrn XY Geldanlagen getätigt.

**False Positives:**

- `XY Geldanlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_335`)


Im daraufhin fortgesetzten Verfahren zu RV/2100547/2022 wurden seitens des Bf.  Beweisanträge auf Einvernahme Herrn XY, Herrn RA Dr. C D (Vertreter der  InsolvenzverwaltungsGmbH als Masseverwalter im Konkurs über das Vermögen der ZZZ- Gruppe), sowie Herrn Dr. O P (RA) gestellt.

**False Positives:**

- `RA Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_TRAIN/145899.1`) (sent_id: `deanon_BFG_TRAIN/145899.1_369`)


Der Bf. und seine Ehegattin überließen Herrn XY Geldbeträge jeweils in bar, wobei die  Einzahlungen in individuell wählbaren Beträgen erfolgten und nicht an den Ausgabewert der  ZZZ-Zertifikate (Genussschein) gebunden waren.

**False Positives:**

- `XY Geldbeträge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_TRAIN/146514.1`) (sent_id: `deanon_BFG_TRAIN/146514.1_15`)


Die Bf. brachte in ihrem fristgerecht erhobenen Einspruch (E-Mail vom 12. September 2024) zu  allen fünf GZen vor, dass Herr Herr Lenker zur gegebenen Zeit gewesen sei.

**False Positives:**

- `Herr Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_TRAIN/148648.1`) (sent_id: `deanon_BFG_TRAIN/148648.1_20`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im verfahrensgegenständlichen Veranlagungszeitraum 2023 hatte Herr Bernhard Siegmundt  Einkünfte aus  nichtselbständiger Tätigkeit von zwei Dienstgebern:   Im Zeitraum zwischen Jänner und der zweiten Monatshälfte des Juli 2023 (mit einer  kurzen Unterbrechung und dem Bezug von Arbeitslosengeld im Jänner 2023) bezog der  Bf. Einkünfte von der Arbeitgeber NÖ in Adr Arbeitgeber NÖ.

**False Positives:**

- `Bernhard Siegmundt  Einkünfte` — partial — gold is substring of pred: `Bernhard Siegmundt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Siegmundt`(person)

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

## `Representative_vertreten_durch`

**F1:** 0.002 | **Precision:** 0.133 | **Recall:** 0.001  

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
| 0.133 | 0.001 | 0.002 | 15 | 2 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 13 | 1581 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/131248.1`) (sent_id: `deanon_BFG_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ottfried Bremermann, Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich, vertreten durch Samuel Rehnke, BSc, Planetengasse 30, 8455 Bischofegg, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 14-141/9449  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Samuel Rehnke, BSc` | `Samuel Rehnke, BSc` |

**Missed by this rule (FN):**

- `Ottfried Bremermann` (person)
- `Kleinebersdorferstraße 2, 8862 Bodendorf, Österreich` (address)
- `Planetengasse 30, 8455 Bischofegg, Österreich` (address)
- `14-141/9449` (tax_number)

**Example 1** (doc_id: `deanon_BFG_TRAIN/137275.1`) (sent_id: `deanon_BFG_TRAIN/137275.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Carla Schweykart, Saaz 45, 8413 Stiefing, Österreich, vertreten durch Dr. Elmar Kresbach LL.M., Rechtsanwalt,  Wipplingerstraße 29/9, 1010 Wien, vom 7. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. April 2022, Zl. Zahl, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, iVm § 4 Abs. 1 Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Elmar Kresbach LL.M.` | `Dr. Elmar Kresbach LL.M.` |

**Missed by this rule (FN):**

- `Dr. Hans Blasina` (person)
- `Carla Schweykart` (person)
- `Saaz 45, 8413 Stiefing, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_TRAIN/129484.1`) (sent_id: `deanon_BFG_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Pastel Pharma, Retzenegg 222, 3242 Ramsau, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Westra ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pastel Pharma`(organisation)
- `Retzenegg 222, 3242 Ramsau, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_TRAIN/131483.1`) (sent_id: `deanon_BFG_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Karen Vennemeyer, Neu-Reinbach 11, 4693 Fallholz, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

**False Positives:**

- `Intercura Teuhand Revisions ` — partial — pred is substring of gold: `Intercura Teuhand Revisions  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karen Vennemeyer`(person)
- `Neu-Reinbach 11, 4693 Fallholz, Österreich`(address)
- `Intercura Teuhand Revisions  GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_TRAIN/135539.1`) (sent_id: `deanon_BFG_TRAIN/135539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Heidemarie Winkler in der  Verwaltungsstrafsache gegen Mag. Willibald Giesser, Eichingerweg 67, 4931 Neulendt, Österreich, vertreten durch HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft, Landstraßer Hauptstraße 27,  1030 Wien, über die Beschwerde des Beschuldigten vom 1. April 2021 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien, Magistratsabteilung 6,  Abgabenstrafen vom 2. März 2021, Zahl: MA6/206000002559/2020, in Anwesenheit des  Verteidigers und der Behördenvertreterin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der Zurückweisungsbescheid des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `HELLER TAXvisory ` — partial — pred is substring of gold: `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Willibald Giesser`(person)
- `Eichingerweg 67, 4931 Neulendt, Österreich`(address)
- `HELLER TAXvisory  GmbH Wirtschafts- prüfungs- und Steuerberatungs- gesellschaft`(organisation)

**Example 3** (doc_id: `deanon_BFG_TRAIN/136145.1`) (sent_id: `deanon_BFG_TRAIN/136145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Gernot Sieglen, Oberlederau 7, 4224 Klingenwehr, Österreich  wohnhaft, StNr.: X1, vertreten durch Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H., Hegelgasse 8/22, 1010 Wien, betreffend die Berufung vom  25.05.2011 gegen die Einkommensteuerbescheide für die Jahre 2008 und 2009, vom  9.05.2011, zugestellt am 12.05.2011, des Finanzamtes Bruck Eisenstadt Oberwart  zu Recht erkannt

**False Positives:**

- `Dr. Hans Bodendorfer ` — partial — pred is substring of gold: `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gernot Sieglen`(person)
- `Oberlederau 7, 4224 Klingenwehr, Österreich`(address)
- `Dr. Hans Bodendorfer  Steuerberatungsges.m.b.H.`(organisation)

**Example 4** (doc_id: `deanon_BFG_TRAIN/136516.1`) (sent_id: `deanon_BFG_TRAIN/136516.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache ÖkR Alessia Starklof, Oberer Jägerweg 15, 3385 Gerersdorf, Österreich, vertreten durch Birgit Priklopil Steuerberatung  GmbH, Amtshausgasse 1 Tür A, 7132 Frauenkirchen, über die Beschwerde vom 21. April 2021  gegen den Bescheid des Finanzamtes Österreich vom 25. März 2021 betreffend  Einkommensteuer 2019, Steuernummer 83-347/8210, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der Bescheid zu  Ungunsten der Beschwerdeführerin abgeändert.

**False Positives:**

- `Birgit Priklopil Steuerberatung ` — partial — pred is substring of gold: `Birgit Priklopil Steuerberatung  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Alessia Starklof`(person)
- `Oberer Jägerweg 15, 3385 Gerersdorf, Österreich`(address)
- `Birgit Priklopil Steuerberatung  GmbH`(organisation)
- `83-347/8210`(tax_number)

**Example 5** (doc_id: `deanon_BFG_TRAIN/139258.1`) (sent_id: `deanon_BFG_TRAIN/139258.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Ing. Univ.-Prof.in Scarlett Steinfurt, Andreas Schrembser-Straße 30, 2095 Wolfsbach, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Oeynhausen, über die Beschwerde  vom 12. Oktober 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr  Finanzamt Österreich, Dienststelle 16 Baden Mödling) vom 13. Juli 2017 betreffend  Einkommensteuer 2011 bis 2015 und Umsatzsteuer 2012 bis 2015 sowie Vorauszahlungen an  Einkommensteuer für das Jahr 2017, Steuernummer 59-534/9010   zu Recht erkannt:   I. Die Beschwerde wird hinsichtlich der Bescheide betreffend die Einkommensteuer  der Jahre 2011 – 2013 sowie betreffend die Umsatzsteuer der Jahre 2012 und 2013  gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `LMG ` — partial — pred is substring of gold: `LMG  Steuerberatungsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Univ.-Prof.in Scarlett Steinfurt`(person)
- `Andreas Schrembser-Straße 30, 2095 Wolfsbach, Österreich`(address)
- `LMG  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `59-534/9010`(tax_number)

**Example 6** (doc_id: `deanon_BFG_TRAIN/139681.1`) (sent_id: `deanon_BFG_TRAIN/139681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Florentin Ginner, Russengasse 3, 4943 Kager, Österreich, vertreten durch TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG, Stadionplatz 2 Tür 3, 8041 Graz, über die Beschwerde vom  4. Oktober 2005 gegen die Bescheide des Finanzamtes Graz-Umgebung (nunmehr Finanzamt  Österreich) vom 29. August 2005 betreffend Umsatzsteuer für die Jahre 2000 – 2003,  Steuernummer 05-330/4121  zu Recht:   I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2000 – 2002 wird Folge  gegeben.

**False Positives:**

- `TPG Wirtschaftstreuhand und ` — partial — pred is substring of gold: `TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Ginner`(person)
- `Russengasse 3, 4943 Kager, Österreich`(address)
- `TPG Wirtschaftstreuhand und  Steuerberatung GmbH & Co KG`(organisation)
- `05-330/4121`(tax_number)

**Example 7** (doc_id: `deanon_BFG_TRAIN/139729.1`) (sent_id: `deanon_BFG_TRAIN/139729.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Brendon Meißnest, Tarnoczygasse 16, 9585 Neumüllnern, Österreich, vertreten durch Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft, Aspernstraße 87/72, 1220 Wien, vom  30. Juni 2016 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 3. Juni 2016 betreffend  Zahlungserleichterungen § 212 BAO 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Tax Wood Audit GmbH ` — partial — pred is substring of gold: `Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brendon Meißnest`(person)
- `Tarnoczygasse 16, 9585 Neumüllnern, Österreich`(address)
- `Tax Wood Audit GmbH  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `FA Amstetten Melk Scheibbs`(organisation)

**Example 8** (doc_id: `deanon_BFG_TRAIN/145451.1`) (sent_id: `deanon_BFG_TRAIN/145451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in den  Beschwerdesachen von Herrn KzlR Estelle Kaufholz, Alte Schulgasse 37, 5521 Bairau, Österreich, vertreten durch Eckhardt  SteuerberatungsgmbH, Hauptstraße 58, 7033 Pöttsching, über   1. die Beschwerde vom 7. Februar 2024 gegen den Bescheid des Finanzamtes Österreich  vom 10. Jänner 2024 betreffend Abweisung eines Antrages auf Stundung gemäß § 212  BAO   2.

**False Positives:**

- `Eckhardt ` — partial — pred is substring of gold: `Eckhardt  SteuerberatungsgmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Estelle Kaufholz`(person)
- `Alte Schulgasse 37, 5521 Bairau, Österreich`(address)
- `Eckhardt  SteuerberatungsgmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_TRAIN/145805.1`) (sent_id: `deanon_BFG_TRAIN/145805.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Zoltan Lentze  in der  Beschwerdesache Piedro Goeres, Bräuhausberg 16, 4625 Humplberg, Österreich, vertreten durch Heisinger Steuerberatung  GmbH, Am Teich 12, 7301 Deutschkreutz, betreffend Beschwerde vom 30. Juni 2020 gegen die  Bescheide des Finanzamtes Wien 1/23, nunmehr Finanzamt Österreich, Dienststelle Wien 1/23  vom 9. März 2020 betreffend Wiederaufnahme betreffend Einkommensteuer 2010,  Wiederaufnahme betreffend Einkommensteuer 2011, Wiederaufnahme betreffend  Einkommensteuer 2012, Wiederaufnahme betreffend Einkommensteuer 2013,  Wiederaufnahme betreffend Einkommensteuer 2014, Wiederaufnahme betreffend  Einkommensteuer 2015 und Einkommensteuer 2012 Steuernummer 75-025/8578  beschlossen:   Die Beschwerde vom 30. Juni 2020 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Heisinger Steuerberatung ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Zoltan Lentze`(person)
- `Piedro Goeres`(person)
- `Bräuhausberg 16, 4625 Humplberg, Österreich`(address)
- `75-025/8578`(tax_number)

**Example 10** (doc_id: `deanon_BFG_TRAIN/146359.1`) (sent_id: `deanon_BFG_TRAIN/146359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Wieser in der Beschwerdesache  Jolanda Schloegel, Apfenthal 97, 4070 Seebach, Österreich, vertreten durch Eckbauer Wirtschaftstreuhand Ges.m.b.H.  Steuerberatungsgesellschaft, Wiener Straße 29, 2640 Gloggnitz, betreffend der  Säumnisbeschwerde vom 23.07.2024 wegen behaupteter Verletzung der Entscheidungspflicht  des Finanzamtes Österreich hinsichtlich der Einkommenssteuer (Arbeitnehmerveranlagung)  2022 zu Steuernummer 55-954/7033  beschlossen:  Das Beschwerdeverfahren wird gemäß § 284 Abs 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Eckbauer Wirtschaftstreuhand Ges.m.b.H. ` — partial — pred is substring of gold: `Eckbauer Wirtschaftstreuhand Ges.m.b.H.  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Andreas Wieser`(person)
- `Jolanda Schloegel`(person)
- `Apfenthal 97, 4070 Seebach, Österreich`(address)
- `Eckbauer Wirtschaftstreuhand Ges.m.b.H.  Steuerberatungsgesellschaft`(organisation)
- `55-954/7033`(tax_number)

**Example 11** (doc_id: `deanon_BFG_TRAIN/148282.1`) (sent_id: `deanon_BFG_TRAIN/148282.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Delila Fritzmeier, Joderweg 16, 3333 Sonntagberg, Österreich, vertreten durch Raml und Partner  Steuerberatung GmbH, Museumstraße 31a, 4020 Linz, über die Beschwerde vom 10. Juni 2024  gegen den Bescheid des Finanzamtes Österreich vom 6. Juni 2024 betreffend  Einkommensteuer 2023 zu Steuernummer 04-427/9729  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Raml und Partner ` — partial — pred is substring of gold: `Raml und Partner  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Johann Fischerlehner`(person)
- `Delila Fritzmeier`(person)
- `Joderweg 16, 3333 Sonntagberg, Österreich`(address)
- `Raml und Partner  Steuerberatung GmbH`(organisation)
- `04-427/9729`(tax_number)

**Example 12** (doc_id: `deanon_BFG_TRAIN/148533.1`) (sent_id: `deanon_BFG_TRAIN/148533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Ronald Maichrzik, Walknerhofweg 2, 2813 Pürahöfen, Österreich, vertreten durch Dr. Kohler und Partner  Steuerberatungs GmbH, Schönbrunner Straße 53, 1050 Wien, über   die Beschwerde vom 7. April 2014 gegen die Bescheide des Finanzamtes Wien 8/16/17  (nunmehr Finanzamt Österreich) vom 6. März 2014 betreffend Einkommensteuer und  Umsatzsteuer 2006 bis 2011 und Umsatzsteuer 2012, sowie   die Beschwerde vom 3. März 2016 gegen die Bescheide des Finanzamtes Baden Mödling  (nunmehr Finanzamt Österreich) vom 10. Februar 2016 betreffend Einkommensteuer 2012  und 2013 sowie Umsatzsteuer 2013,  Steuernummer 96-996/1461, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Kohler und Partner ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ronald Maichrzik`(person)
- `Walknerhofweg 2, 2813 Pürahöfen, Österreich`(address)
- `96-996/1461`(tax_number)

</details>

---

</details>

---

