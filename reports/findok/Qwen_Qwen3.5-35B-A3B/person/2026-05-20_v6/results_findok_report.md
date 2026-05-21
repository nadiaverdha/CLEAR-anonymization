# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-21T08:07:10.218568

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-20_v6/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2473 |
| Validation documents | 619 |
| Test documents | 12 |
| Train sentences | 4080 |
| Validation sentences | 927 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 3 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 150 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 88.5% |
| True Positives | 26 |
| False Positives | 114 |
| False Negatives | 64 |
| Total Gold Entities | 90 |
| Micro Precision | 18.6% |
| Micro Recall | 28.9% |
| Micro F1 | 22.6% |
| Macro F1 | 22.6% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Names in Legal Contexts` | 18.0% | 90.0% | 10.0% | 10 | 9 | 1 |
| `Names with Special Titles` | 20.2% | 57.9% | 12.2% | 19 | 11 | 8 |
| `Herr/Frau Name Identification` | 8.0% | 40.0% | 4.4% | 10 | 4 | 6 |
| `Names after 'Zu' (To)` | 1.9% | 5.6% | 1.1% | 18 | 1 | 17 |
| `Names after 'von' (Possessive)` | 1.2% | 1.2% | 1.1% | 82 | 1 | 81 |
| `Name in Parentheses` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Children Name Identification` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after 'Ehepaar'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Names in Legal Contexts`

**F1:** 0.180 | **Precision:** 0.900 | **Recall:** 0.100  

**Format:** `regex`  
**Rule ID:** `403b75b0`  
**Description:**
Identifies person names appearing specifically after 'in der Beschwerdesache', 'in der Säumnisbeschwerdesache', 'im Beschwerdeverfahren', capturing the full name including title and suffixes.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Säumnisbeschwerdesache|Rechtssache)|im\s+Beschwerdeverfahren)\s+(?:des|der|der\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|de|la|del|di|da|van|ter|in\s+der)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?:\s*,\s*(?:BSc|MSc|PhD|Dr\.in|Mag\.in|Dipl\.-Ing\.in|Dipl\.-Ing\.m|B\.Sc\.|M\.Sc\.|Bakk\.(?:\s+rer\.+\s+\w+|\s+techn\.)?|BA|LL\.M\.|M\.B\.L\.|BEd|LLB|MA|Bakk\.\s+art\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.900 | 0.100 | 0.180 | 10 | 9 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 1 | 81 |

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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `Names with Special Titles`

**F1:** 0.202 | **Precision:** 0.579 | **Recall:** 0.122  

**Format:** `regex`  
**Rule ID:** `a9988c88`  
**Description:**
Consolidated rule to capture full name entities including multiple titles (e.g., 'Mag. Mag. Hon.-Prof.') and suffixes (e.g., 'MA Bakk. art.'). Handles complex title sequences and ensures the full string is captured.

**Content:**
```
(?:Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R|OStR|OMedR|HR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Dr\.|Mag\.|RgR|KommR|\u00d6kR|VetR|OSR|StR|MedR|KzlR|R\.?|Ing\.|DDr\.|Bakk\.|M\.B\.L\.|LL\.M\.|Dipl\.-Ing\.|PhD\.|Mag\.a|Dr\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|Ri|R1|R2|R3)(?:\s+(?:Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R|OStR|OMedR|HR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Dr\.|Mag\.|RgR|KommR|\u00d6kR|VetR|OSR|StR|MedR|KzlR|R\.?|Ing\.|DDr\.|Bakk\.|M\.B\.L\.|LL\.M\.|Dipl\.-Ing\.|PhD\.|Mag\.a|Dr\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|Ri|R1|R2|R3))*\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|de|la|del|di|da|van|ter|in\s+der)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?:\s*,\s*(?:BSc|MSc|PhD|Dr\.in|Mag\.in|Dipl\.-Ing\.in|Dipl\.-Ing\.m|B\.Sc\.|M\.Sc\.|Bakk\.(?:\s+rer\.+\s+\w+|\s+techn\.)?|BA|LL\.M\.|M\.B\.L\.|BEd|LLB|MA|Bakk\.\s+art\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.579 | 0.122 | 0.202 | 19 | 11 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 8 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hon.-Prof. Gotthard Clement` | `Priv.-Doz. Hon.-Prof. Gotthard Clement` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Mag. Ashley Partenfelder` | `Mag. Ashley Partenfelder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Farina Kohlstrunk` | `Priv.-Doz.in Farina Kohlstrunk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Quirin Januszis` | `Priv.-Doz. Quirin Januszis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Ri  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Names after 'von' (Possessive)`

**F1:** 0.012 | **Precision:** 0.012 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `2a1ea4ba`  
**Description:**
Identifies person names appearing after 'von' (of/from) in legal texts, capturing the full name including title if present. Excludes common legal nouns.

**Content:**
```
\bvon\s+(?:Dr\.in(?:\s+Dr\.in\s+Univ\.-Prof\.in|\s+Univ\.-Prof\.in|\s+Dr\.in)?|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.|Mag\.|Dr\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Bakk\.|M\.B\.L\.|LL\.M\.|Dipl\.-Ing\.|StR\.|RgR\.|KommR\.|\u00d6kR\.|VetR\.|OSR\.|PhD\.|Mag\.a|Dr\.in|Ri|R1|R2|R3|Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|de|la|del|di|da|van|ter|in\s+der)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?!\s*(?:ung|heit|keit|schaft|tät|e|n)\b)(?!\s*(?:Anspruch|Zinsen|Gebühren|Frist|Verfahren|Sache|Recht|Klage|Urteil|Beschluss|Verfügung|Entscheidung|Einsatzgebühren|Familienbeihilfe|Kinderabsetzbetrag|Bescheide|Verfahren|Sache|Recht|Klage|Urteil|Beschluss|Verfügung|Entscheidung|Verfahren|Sache|Recht|Klage|Urteil|Beschluss|Verfügung|Entscheidung)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.012 | 0.011 | 0.012 | 82 | 1 | 81 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 81 | 86 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_7`)


3. Mit Bescheid vom 12.11.2019 forderte das Finanzamt die für den Zeitraum von November  2017 bis Juni 2018 bezogenen Beträge an Familienbeihilfe und Kinderabsetzbeträgen iHv.

**False Positives:**

- `November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'Zu' (To)`

**F1:** 0.019 | **Precision:** 0.056 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `4d247c0c`  
**Description:**
Identifies person names appearing after 'Zu' (To) in legal contexts, often used to introduce a specific person in a list or context.

**Content:**
```
\bZu\s+(?!den|die|dem|der|den\s+Akten|den\s+Verfahren|den\s+Sachen)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.056 | 0.011 | 0.019 | 18 | 1 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 17 | 74 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_19`)


Zur Begründung wurde ausgeführt:  „Zu Viktoria Immohr:  Bei einem Studienwechsel nach dem 3. gemeldeten Semester steht Familienbeihilfe dann zu,  wenn die absolvierten Semester aus dem Vorstudium zur Gänze angerechnet wurden (§ 17  Studienförderungsgesetz 1992).

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

</details>

---

## `Herr/Frau Name Identification`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `c4117de7`  
**Description:**
Identifies names preceded by 'Herr' or 'Frau' in legal contexts. Excludes known compound titles and ensures 'Herr' is not followed by a female name.

**Content:**
```
\b(?:Herr|Frau)\s+(?!Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R|Rechtsanwältin|Rechtsanwalt|Anwalt|Notar|Steuerberater|Berater|Frau|Mag\.a|Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Hon\.-Prof\.in)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
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

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

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

## `Children Name Identification`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `75948241`  
**Description:**
Identifies names of children appearing after 'für die Kinder' or 'Kinder'.

**Content:**
```
(?:für\s+die\s+Kinder|Kinder)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Names after 'Ehepaar'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5cdfa1e8`  
**Description:**
Identifies names appearing after 'Ehepaar' (couple), capturing the full list of names.

**Content:**
```
Ehepaar\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)(?:\s+und\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)?)?
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

## `Names with Special Titles`

**F1:** 0.202 | **Precision:** 0.579 | **Recall:** 0.122  

**Format:** `regex`  
**Rule ID:** `a9988c88`  
**Description:**
Consolidated rule to capture full name entities including multiple titles (e.g., 'Mag. Mag. Hon.-Prof.') and suffixes (e.g., 'MA Bakk. art.'). Handles complex title sequences and ensures the full string is captured.

**Content:**
```
(?:Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R|OStR|OMedR|HR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Dr\.|Mag\.|RgR|KommR|\u00d6kR|VetR|OSR|StR|MedR|KzlR|R\.?|Ing\.|DDr\.|Bakk\.|M\.B\.L\.|LL\.M\.|Dipl\.-Ing\.|PhD\.|Mag\.a|Dr\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|Ri|R1|R2|R3)(?:\s+(?:Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R|OStR|OMedR|HR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Dr\.|Mag\.|RgR|KommR|\u00d6kR|VetR|OSR|StR|MedR|KzlR|R\.?|Ing\.|DDr\.|Bakk\.|M\.B\.L\.|LL\.M\.|Dipl\.-Ing\.|PhD\.|Mag\.a|Dr\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|Ri|R1|R2|R3))*\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|de|la|del|di|da|van|ter|in\s+der)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?:\s*,\s*(?:BSc|MSc|PhD|Dr\.in|Mag\.in|Dipl\.-Ing\.in|Dipl\.-Ing\.m|B\.Sc\.|M\.Sc\.|Bakk\.(?:\s+rer\.+\s+\w+|\s+techn\.)?|BA|LL\.M\.|M\.B\.L\.|BEd|LLB|MA|Bakk\.\s+art\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.579 | 0.122 | 0.202 | 19 | 11 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 8 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hon.-Prof. Gotthard Clement` | `Priv.-Doz. Hon.-Prof. Gotthard Clement` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Mag. Ashley Partenfelder` | `Mag. Ashley Partenfelder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Farina Kohlstrunk` | `Priv.-Doz.in Farina Kohlstrunk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Quirin Januszis` | `Priv.-Doz. Quirin Januszis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gabriele Friedbacher` | `Mag. Gabriele Friedbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Juliana Bartjen` | `Priv.-Doz.in Juliana Bartjen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Renate Brombusch` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Estelle Niederholz` | `Dr.in Estelle Niederholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thassilo Averdiek` | `Hon.-Prof. Thassilo Averdiek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Dagobert Nordholt` | `Dr. Dagobert Nordholt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Ri  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof.in OStR Tosca Knoller,  ` — partial — gold is substring of pred: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

</details>

---

## `Names in Legal Contexts`

**F1:** 0.180 | **Precision:** 0.900 | **Recall:** 0.100  

**Format:** `regex`  
**Rule ID:** `403b75b0`  
**Description:**
Identifies person names appearing specifically after 'in der Beschwerdesache', 'in der Säumnisbeschwerdesache', 'im Beschwerdeverfahren', capturing the full name including title and suffixes.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Säumnisbeschwerdesache|Rechtssache)|im\s+Beschwerdeverfahren)\s+(?:des|der|der\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|de|la|del|di|da|van|ter|in\s+der)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?:\s*,\s*(?:BSc|MSc|PhD|Dr\.in|Mag\.in|Dipl\.-Ing\.in|Dipl\.-Ing\.m|B\.Sc\.|M\.Sc\.|Bakk\.(?:\s+rer\.+\s+\w+|\s+techn\.)?|BA|LL\.M\.|M\.B\.L\.|BEd|LLB|MA|Bakk\.\s+art\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.900 | 0.100 | 0.180 | 10 | 9 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 1 | 81 |

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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `Herr/Frau Name Identification`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `c4117de7`  
**Description:**
Identifies names preceded by 'Herr' or 'Frau' in legal contexts. Excludes known compound titles and ensures 'Herr' is not followed by a female name.

**Content:**
```
\b(?:Herr|Frau)\s+(?!Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R|Rechtsanwältin|Rechtsanwalt|Anwalt|Notar|Steuerberater|Berater|Frau|Mag\.a|Dr\.in|Univ\.-Prof\.in|Priv\.-Doz\.in|Hon\.-Prof\.in)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
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

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `Names after 'Zu' (To)`

**F1:** 0.019 | **Precision:** 0.056 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `4d247c0c`  
**Description:**
Identifies person names appearing after 'Zu' (To) in legal contexts, often used to introduce a specific person in a list or context.

**Content:**
```
\bZu\s+(?!den|die|dem|der|den\s+Akten|den\s+Verfahren|den\s+Sachen)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.056 | 0.011 | 0.019 | 18 | 1 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 17 | 74 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_19`)


Zur Begründung wurde ausgeführt:  „Zu Viktoria Immohr:  Bei einem Studienwechsel nach dem 3. gemeldeten Semester steht Familienbeihilfe dann zu,  wenn die absolvierten Semester aus dem Vorstudium zur Gänze angerechnet wurden (§ 17  Studienförderungsgesetz 1992).

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_123`)


3.2. Zu Spruchpunkt I. (Stattgabe)  Die Bf. absolvierte im ersten Studienjahr erfolgreich die Studieneingangs- und  Orientierungsphase (StEOP).

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_119`)


Zu Spruchpunkt I. (Stattgabe)  Strittig ist im gegenständlichen Verfahren, ob die künstlerische Tätigkeit des Bf. als Musiker in  den Jahren 2012 bis 2014 eine steuerlich anzuerkennende Einkunftsquelle darstellt oder ob es  sich aus steuerlicher Sicht um eine sog.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_80`)


Zu Spruchpunkt I. (Abweisung)  § 34 Einkommensteuergesetz 1988 (EStG 1988), BGBl. Nr. 400/1988 idF BGBl. I Nr. 103/2019,  lautet auszugsweise wie folgt:  (1) Bei der Ermittlung des Einkommens (§ 2 Abs. 2) eines unbeschränkt Steuerpflichtigen sind  nach Abzug der Sonderausgaben (§ 18) außergewöhnliche Belastungen abzuziehen.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_166`)


Zu Spruchpunkt I. (Abweisung/Abänderung/Stattgabe)  Geltendmachung von Haftungen  10 von 15 Seite 11 von 15

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_34`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  1.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_104`)


3.2. Zu Spruchpunkt II. (Revision)  1.

**False Positives:**

- `Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'von' (Possessive)`

**F1:** 0.012 | **Precision:** 0.012 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `2a1ea4ba`  
**Description:**
Identifies person names appearing after 'von' (of/from) in legal texts, capturing the full name including title if present. Excludes common legal nouns.

**Content:**
```
\bvon\s+(?:Dr\.in(?:\s+Dr\.in\s+Univ\.-Prof\.in|\s+Univ\.-Prof\.in|\s+Dr\.in)?|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.|Mag\.|Dr\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Bakk\.|M\.B\.L\.|LL\.M\.|Dipl\.-Ing\.|StR\.|RgR\.|KommR\.|\u00d6kR\.|VetR\.|OSR\.|PhD\.|Mag\.a|Dr\.in|Ri|R1|R2|R3|Techn\s+R\s+OMedR|Techn\s+R\s+HR|Techn\s+R)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|de|la|del|di|da|van|ter|in\s+der)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?!\s*(?:ung|heit|keit|schaft|tät|e|n)\b)(?!\s*(?:Anspruch|Zinsen|Gebühren|Frist|Verfahren|Sache|Recht|Klage|Urteil|Beschluss|Verfügung|Entscheidung|Einsatzgebühren|Familienbeihilfe|Kinderabsetzbetrag|Bescheide|Verfahren|Sache|Recht|Klage|Urteil|Beschluss|Verfügung|Entscheidung|Verfahren|Sache|Recht|Klage|Urteil|Beschluss|Verfügung|Entscheidung)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.012 | 0.011 | 0.012 | 82 | 1 | 81 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 81 | 86 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_7`)


3. Mit Bescheid vom 12.11.2019 forderte das Finanzamt die für den Zeitraum von November  2017 bis Juni 2018 bezogenen Beträge an Familienbeihilfe und Kinderabsetzbeträgen iHv.

**False Positives:**

- `November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_28`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“

**False Positives:**

- `Fähigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `Fähigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_74`)


Weiters absolvierte die Tochter der Bf. an der JKU Linz Lehrveranstaltungen mit  31 ECTS-Punkten (ohne Berücksichtigung von Anrechnungen).

**False Positives:**

- `Anrechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_101`)


Aus der nicht im gleichen Umfang erfolgten Anrechnung zum Zeitpunkt des  Studienwechsels kann daher noch kein automatischer Schluss betreffend die Vergleichbarkeit  von Studien gezogen werden.

**False Positives:**

- `Studien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_107`)


Die Qualifikations- bzw. Ausbildungsziele für ein  Studium der Wirtschaftswissenschaften in Hinblick auf Kompetenzen (im Sinne eines  spezialisiertes Systems von Fähigkeiten) sowie von avisierten Lernergebnissen  (operationalisiert durch vollzogene Prüfungen) seien an beiden Universitäten in Hinblick auf  diesen beiden Programme als gleichwertig anzusehen.

**False Positives:**

- `Fähigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `Studienortwechseln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `Vorteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_13`)


Als Begründung wurde dazu angegeben, während eines  Insolvenzverfahrens seien die Voraussetzungen für die Bewilligung von  Zahlungserleichterungen grundsätzlich nicht gegeben.

**False Positives:**

- `Zahlungserleichterungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_31`)


Die Gewährung von Zahlungserleichterungen für die Entrichtung von Geldstrafen und Kosten  nach dem Finanzstrafgesetz richtet sich damit nach § 212 BAO (vgl. VwGH 24.02.2011,  2010/16/0276, uHa Vorjudikatur).

**False Positives:**

- `Zahlungserleichterungen` — no gold match — likely missing annotation
- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_38`)


Die Unterstellung der Gewährung von Zahlungserleichterungen für die Entrichtung von  Geldstrafen nach dem Finanzstrafgesetz unter das Regelungsregime des § 212 BAO erfolgt  nach dem Wortlaut der Vorschrift des § 172 Abs. 1 FinStrG nur "sinngemäß".

**False Positives:**

- `Zahlungserleichterungen` — no gold match — likely missing annotation
- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_47`)


Für diesen Bereich galt eine ordnungsgemäß kundgemachte flächendeckende Kurzparkzone für  die Zeit von Montag bis Freitag (werktags) von 09:00 bis 22:00 Uhr.

**False Positives:**

- `Montag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_56`)


Die Einkommens- und Vermögensverhältnisse und allfällige Sorgepflichten des Beschuldigten  sind bei der Bemessung von Geldstrafen zu berücksichtigen.

**False Positives:**

- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_19`)


Die Art und  Weise der ausgeübten Tätigkeit sowie die Zusammensetzung von Einnahmen und Ausgaben  stellen neue Tatsachen gemäß § 303 Bundesabgabenordnung dar und diese konnten nur im  Wege einer Außenprüfung ermittelt werden.

**False Positives:**

- `Einnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_23`)


Unser Mandant ist hauptberuflich Musiker (Vibraphon, Schlagwerk), seine Tätigkeiten übt er  sowohl in Form von Dienstverhältnissen (z.B. Orchester) als auch als selbständiger Musiker  (Einzelunternehmer oder Gesellschafter diverser Musikensembles) aus.

**False Positives:**

- `Dienstverhältnissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_32`)


Er hat  diese Tätigkeit in gleicher Weise von Betriebseröffnung bis Betriebsaufgabe ausgeübt.

**False Positives:**

- `Betriebseröffnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_36`)


Nur, weil es insbesondere in den letzten Jahren der  selbständigen Tätigkeit unseres Mandanten zu dem einen oder anderen Verlustjahr gekommen  ist - dies auch bedingt durch die Tatsache, dass junge Konkurrenz nachwuchs und unser  Mandant dadurch nicht mehr so einfach an Aufträge kam, weiters die Gagenhöhe im Bereich  der Jazzmusik laufend gesunken ist und viele Veranstalter vermehrt auf modischere Diskjockeys  zurückgegriffen haben - kann nicht ohne weitere Prüfung des Gesamterfolges einer Tätigkeit  von Liebhaberei ausgegangen werden.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_41`)


Unser Mandant war über die Jahre stets bemüht, neue Aufträge zu erhalten, hat dann aber  2014 die Schließung seines Betriebes beim Finanzamt bekanntgegeben, da es für ihn aus  Altersgründen zu anstrengend wurde, neue Aufträge zu lukrieren und die Mühen von  Konzerttourneen auf sich zu nehmen.

**False Positives:**

- `Konzerttourneen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_44`)


Laut LRL Rz 22 ist der Gesamtgewinn das betriebliche Ergebnis von Begründung der Tätigkeit  durch den jeweiligen Steuerpflichtigen bis zu deren Beendigung durch denselben  Steuerpflichtigen (Veräußerung, Aufgabe oder Liquidation).

**False Positives:**

- `Begründung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_45`)


Aus diesem Grund wäre das  Finanzamt verpflichtet gewesen, aufgrund der Feststellung der Betriebsprüfung die Gewinne  der selbständigen Schaffensperiode unseres Mandanten von Beginn seiner Tätigkeit 1975 bis zu  deren Beendigung 2014 zu berücksichtigen.

**False Positives:**

- `Beginn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_51`)


In der Begründung ging das Finanzamt, wie im Bericht über den Abschluss der Außenprüfung  dargestellt, vom Vorliegen von Liebhaberei ab dem Jahr 2012 aus.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_55`)


Weiters wurde begründend ausgeführt:  „Das Vorliegen von Liebhaberei gemäß § 1 Abs. 2 Liebhabereiverordnung wurde festgestellt, da  zwar eine inhaltliche Kongruenz zwischen selbständiger und nichtselbständiger Tätigkeit  vorliegt, aber die Behörde aufgrund der umfangreichen Ausübung vom Vorliegen einer im  Privaten gelegenen Neigung ausgeht.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_58`)


Es wird nicht vom Vorliegen eines Gesamtverlustes über den gesamten Tätigkeitszeitraum von  Bf. ausgegangen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_72`)


Der Bf. habe seine hauptberufliche Tätigkeit als Musiker unverändert,  von Beginn an in der gleichen Art und Weise im Bereich Vibraphon/Schlagwerk ausgeübt.

**False Positives:**

- `Beginn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_77`)


Lediglich aufgrund eines bestimmten Verhältnisses von Einnahmen zu Ausgaben auf eine  Änderung der Bewirtschaftung zu schließen, sei unzureichend.

**False Positives:**

- `Einnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_100`)


1. aus der Bewirtschaftung von Wirtschaftsgütern, die sich nach der Verkehrsauffassung in  einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung eignen (zB  Wirtschaftsgüter, die der Sport- und Freizeitausübung dienen, Luxuswirtschaftsgüter) und  typischerweise einer besonderen in der Lebensführung begründeten Neigung entsprechen oder  2. aus Tätigkeiten, die typischerweise auf eine besondere in der Lebensführung begründete  Neigung zurückzuführen sind, oder  3. aus der Bewirtschaftung von Eigenheimen, Eigentumswohnungen und  Mietwohngrundstücken mit qualifizierten Nutzungsrechten.

**False Positives:**

- `Wirtschaftsgütern` — no gold match — likely missing annotation
- `Eigenheimen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_101`)


Die Annahme von Liebhaberei kann in diesen Fällen nach Maßgabe des § 2 Abs. 4  ausgeschlossen sein.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_107`)


(2) Innerhalb der ersten drei Kalenderjahre (Wirtschaftsjahre) ab Beginn einer Betätigung (zB  Eröffnung eines Betriebes) im Sinn des § 1 Abs. 1, längstens jedoch innerhalb der ersten fünf  Kalenderjahre (Wirtschaftsjahre) ab dem erstmaligen Anfallen von Aufwendungen (Ausgaben)  für diese Betätigung liegen jedenfalls Einkünfte vor (Anlaufzeitraum).

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_110`)


Ablauf dieses Zeitraumes ist unter Berücksichtigung der Verhältnisse auch innerhalb dieses  Zeitraumes nach dem Gesamtbild der Verhältnisse zu beurteilen, ob weiterhin vom Vorliegen  von Einkünften auszugehen ist.

**False Positives:**

- `Einkünften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_114`)


Steuerfreie Einnahmen sind  nur insoweit anzusetzen, als sie nicht zu einer Kürzung von Aufwendungen (Ausgaben) führen.

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_115`)


Wertänderungen von Grund und Boden, der zum Anlagevermögen gehört, sind nur bei der  Gewinnermittlung nach § 5 EStG 1988 anzusetzen.

**False Positives:**

- `Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_129`)


Liebhaberei ist gemäß § 1 Abs. 2 Z 1 LVO hingegen bei einer Betätigung anzunehmen, wenn  Verluste aus der Bewirtschaftung von Wirtschaftsgütern entstehen, die sich nach der  Verkehrsauffassung in einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung  eignen (u.a. Luxuswirtschaftsgüter) und typischerweise einer besonderen in der Lebensführung  begründeten Neigung entsprechen.

**False Positives:**

- `Wirtschaftsgütern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

**False Positives:**

- `Musikern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_8`)


Mit Bescheid über die Festsetzung von Anspruchszinsen 2021 vom 12.3.2025 ergibt die  Berechnung der Anspruchszinsen für das Jahr 2021 eine Gutschrift in Höhe von 7.963,60 €, da  1 von 7 Seite 2 von 7

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_17`)


Das Finanzamt erließ am 21.7.2025 eine abweisende Beschwerdevorentscheidung gegen den  Bescheid über die Festsetzung von Anspruchszinsen 2021 vom 12.03.2025 aufgrund der  Beschwerde vom 26.3.2025, da die Anspruchszinsenbescheide nach ständiger Rechtsprechung  an die Höhe der im Bescheidspruch des jeweiligen Einkommensteuerbescheides  ausgewiesenen Nachforderung gebunden seien.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_20`)


Mit Schreiben vom 23.7.2025 stellte die steuerliche Vertretung den Antrag auf Entscheidung  über die Beschwerde (Vorlageantrag) durch das Bundesfinanzgericht betreffend den Bescheid  über Festsetzung von Anspruchszinsen für das Jahr 2021 vom 12.3.2025.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_25`)


Ebenso erging am 22.05.2024 der (erste) Bescheid über die Festsetzung von Anspruchszinsen  2021.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_29`)


- die Beschwerde gegen den Bescheid über die Festsetzung von Anspruchszinsen 2021 (Anm:  vom 22.5.2024) wurde mit BVE vom 07.10.2025 abgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_30`)


Darüber hinaus erging am 12.03.2025 ein (neuer) Bescheid über die Festsetzung von  Anspruchszinsen für das Jahr 2021, in dem sich eine Gutschrift in der Höhe von Euro 7.963,60  ergab.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation
- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_45`)


Da der Erstbescheid des Bf zur Einkommensteuer 2021 eine Nachforderung von Euro  167.848,00 ergeben hat und dieser erst am 22.05.2024 ergangen ist (also somit nach dem  01.10.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_46`)


des dem Jahr des Entstehens des Abgabenanspruch folgenden Jahres) wurden mit  Bescheid vom 22.05.2024 Anspruchszinsen gem. § 205 BAO in der Höhe von Euro 13.809,18  festgesetzt.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_47`)


Da der Einkommensteuerbescheid aufgrund der Beschwerde des Bf mit  Beschwerdevorentscheidung vom 12.03.2025 abgeändert wurde (zugunsten des Bf) erging am  12.03.2025 der neue (bzw. weitere) Bescheid über die Festsetzung von Anspruchszinsen 2021, in  dem diesem Umstand Rechnung getragen wurde (Gutschrift Anspruchszinsen in der Höhe von  Euro 7.963,60).

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation
- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_50`)


Unter Verweis auf die bisherigen  Ausführungen, den Bescheid und die Beschwerdevorentscheidung wird von Seiten der  Abgabenbehörde die Abweisung der Beschwerde beantragt“.

**False Positives:**

- `Seiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Anzahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_90`)


Unabhängig vom Ausgang der eingebrachten Beschwerde gegen den  Einkommensteuerbescheid für das Jahr 2020 (und der Vorlage an das BFG) ist die Beschwerde  vom 25.3.2025 gegen den Bescheid vom 12.3.2025 betreffend Festsetzung von  Anspruchszinsen (§ 205 BAO) für das Jahr 2021 als unbegründet abzuweisen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_5`)


Am 31. Oktober 2023 erging ein Ergänzungsersuchen an den Bf. betreffend die geltend  gemachten Behandlungskosten in Höhe von Euro 10.299,13.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_43`)


Der Bf. machte in der Einkommensteuerveranlagung für das Jahr 2022 die Kosten für die  Operation in der Privatklinik in Höhe von Euro 10.299,13 als außergewöhnliche Belastung  geltend.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_44`)


Die Kosten setzen sich aus Spitalskosten in Höhe von Euro 10.340,97 abzüglich  Euro 41,84 Haushaltsersparnis für die Dauer des Spitalsaufenthalts von acht Tagen zusammen.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_61`)


Triftige medizinische Gründe lassen auch höhere Aufwendungen des Steuerpflichtigen als die  von Sozialversicherungsträgern finanzierten zwangsläufig erscheinen.

**False Positives:**

- `Sozialversicherungsträgern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_70`)


In diesem Zusammenhang wird angemerkt,  dass auch in öffentlichen Krankenhäusern die Vergabe von Operationsterminen der  medizinischen Indikation und Dringlichkeit entsprechend erfolgt.

**False Positives:**

- `Operationsterminen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_108`)


Dabei ist zu beachten, dass triftige  medizinische Gründe auch höhere Aufwendungen als die von Sozialversicherungsträgern  finanzierten zwangsläufig erscheinen lassen (vgl. VwGH 11.2.2022, Ra 2020/13/0062).

**False Positives:**

- `Sozialversicherungsträgern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_56`)


Zu den abgabenrechtlichen Pflichten würden insbesondere gehören:  die Abgabenentrichtung aus den Mitteln, die der Vertreter verwalte,  die Führung gesetzlicher Aufzeichnungen (VwGH 30.5.1989, 89/14/0043),  die zeitgerechte Einreichung von Abgabenerklärungen (VwGH 29.5.2001, 2000/14/0006).

**False Positives:**

- `Abgabenerklärungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_166`)


Zu Spruchpunkt I. (Abweisung/Abänderung/Stattgabe)  Geltendmachung von Haftungen  10 von 15 Seite 11 von 15

**False Positives:**

- `Haftungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_171`)


Gemäß § 224 Abs. 1 BAO werden die in Abgabenvorschriften geregelten persönlichen  Haftungen durch Erlassung von Haftungsbescheiden geltend gemacht.

**False Positives:**

- `Haftungsbescheiden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_220`)


Vom Bf. wurden keine weiteren Gründe vorgebracht, die bei Abwägung von Zweckmäßigkeit  und Billigkeit eine andere Einschätzung bewirken hätten können.

**False Positives:**

- `Zweckmäßigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_7`)


2. Mit dem angefochtenen Bescheid über die Festsetzung von Säumniszuschlägen vom  9.1.2025 folgte eine Festsetzung von Säumniszuschlägen auf diese Abgaben gemäß § 217 Abs.  1 von 7 Seite 2 von 7

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation
- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_35`)


Die für die im Beschwerdefall für die Festsetzung von Säumniszuschlägen maßgeblichen  gesetzlichen Bestimmungen in der Bundesabgabenordnung BGBl. 1961/194 lauten:  § 217 BAO  (1) Wird eine Abgabe, ausgenommen Nebengebühren (§ 3 Abs. 2 lit. d), nicht spätestens am  Fälligkeitstag entrichtet, so sind nach Maßgabe der folgenden Bestimmungen  Säumniszuschläge zu entrichten.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_43`)


Die Dreimonatsfristen werden insoweit unterbrochen, als nach Abs. 4  Anbringen oder Amtshandlungen der Verpflichtung zur Entrichtung von Säumniszuschlägen  entgegenstehen.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_50`)


Die  Verwirkung von Säumniszuschlägen setzt kein Verschulden des Abgabepflichtigen voraus.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_70`)


Ob die Normverbrauchsabgabe- und Umsatzsteuerfestsetzungen zu Unrecht erfolgt  waren oder nicht, war für die Frage, ob das Finanzamt zur Festsetzung von Säumniszuschlägen  berechtigt war oder nicht, wie bereits weiter oben ausgeführt, nicht relevant.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_78`)


Der Bf. hat gleichzeitig  mit den Beschwerden gegen die Bescheide über die Festsetzung von Normverbrauchsabgabe  und Umsatzsteuer (Fahrzeugeinzelbesteuerung) die Aussetzung dieser Abgaben beantragt.

**False Positives:**

- `Normverbrauchsabgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_80`)


Anlässlich der Erledigung der Beschwerden gegen die Festsetzung von  Umsatzsteuer für den Erwerb des Kfz.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_95`)


Die mit dem angefochtenen Bescheid verfügte Festsetzung von Säumniszinsen für die  Normverbrauchsabgabe in Höhe von 235,71 Euro ist daher zu Unrecht erfolgt.

**False Positives:**

- `Säumniszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_101`)


Fallen diese weg, steht einer neuerlichen Festsetzung  von Säumniszinsen, auf die ja bereits ein Anspruch entstanden ist, nichts im Weg.

**False Positives:**

- `Säumniszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name in Parentheses`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `01f03575`  
**Description:**
Identifies names that appear in parentheses followed by a role description (e.g., 'Name (Beschwerdeführerin)').

**Content:**
```
\((?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+(?:de|von|la|del|di|da|van|ter|van|de\s+)?[A-Z][a-z]+)*)?(?:\s+(?:Mag\.?|Dr\.?|Prof\.?|Hon\.-Prof\.?|Priv\.-Doz\.?|Univ\.-Prof\.?|Bakk\.?|M\.?B\.?L\.?|LL\.?M\.?|Dipl\.-Ing\.?|StR\.?|RgR\.?|KommR\.?|\u00d6kR\.?|VetR\.?|OSR\.?|PhD\.?|DDr\.|Mag\.a|Dr\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|Ri|R1|R2|R3))?(?:\s+[A-Z][a-z]+(?:\s+(?:de|von|la|del|di|da|van|ter|van|de\s+)?[A-Z][a-z]+)*)+\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 39 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `` — similar text (different position): `5966 230804`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

**False Positives:**

- `` — partial — pred is substring of gold: `Viktoria Immohr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `` — similar text (different position): `5966 230804`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

</details>

---

## `Children Name Identification`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `75948241`  
**Description:**
Identifies names of children appearing after 'für die Kinder' or 'Kinder'.

**Content:**
```
(?:für\s+die\s+Kinder|Kinder)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Names after 'Ehepaar'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5cdfa1e8`  
**Description:**
Identifies names appearing after 'Ehepaar' (couple), capturing the full list of names.

**Content:**
```
Ehepaar\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)(?:\s+und\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)?)?
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

