# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-21T10:39:43.421127

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-21_v1/config.yaml 
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
| Max rules | 20 |
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
| Batch size | 100 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 89.9% |
| True Positives | 17 |
| False Positives | 81 |
| False Negatives | 73 |
| Total Gold Entities | 90 |
| Micro Precision | 17.3% |
| Micro Recall | 18.9% |
| Micro F1 | 18.1% |
| Macro F1 | 18.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `herrn_context` | 4.3% | 100.0% | 2.2% | 2 | 2 | 0 |
| `academic_and_professional_titles` | 22.4% | 70.6% | 13.3% | 17 | 12 | 5 |
| `party_names_in_context` | 2.2% | 50.0% | 1.1% | 2 | 1 | 1 |
| `generic_honorifics` | 8.0% | 40.0% | 4.4% | 10 | 4 | 6 |
| `role_based_identification` | 0.0% | 0.0% | 0.0% | 11 | 0 | 11 |
| `beschwerdesache_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `representative_names` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `generic_preposition_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `greeting_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_comma_in_list` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `techn_hr_title` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `name_in_comma_list` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `party_in_complaint_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `complaint_of_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `party_name_with_title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_with_suffix_no_title` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `name_as_role` | 0.0% | 0.0% | 0.0% | 58 | 0 | 58 |
| `name_after_born` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `genitive_party_name` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `party_in_complaint_context_no_address` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `beschwerdesache_party_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `academic_and_professional_titles`

**F1:** 0.224 | **Precision:** 0.706 | **Recall:** 0.133  

**Format:** `regex`  
**Rule ID:** `e26ac21a`  
**Description:**
Matches names preceded by one or more academic/professional titles. Handles multiple consecutive titles (e.g., 'RgR Dipl. Kff.', 'VetR OMedR'). Stops before addresses.

**Content:**
```
(?<!\S)(?!(?:Richter|Richterin|Senatsvorsitzender|Senatsvorsitzende|fachkundige\s+Laienrichter|fachkundige\s+Laienrichterin|vertreten\s+durch)\s+)(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.706 | 0.133 | 0.224 | 17 | 12 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 12 | 5 | 78 |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `name_as_role`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `807a9f64`  
**Description:**
Matches names appearing after 'als' (as) followed by a role. STRICTLY excludes common job titles and legal roles that are not names. REMOVED: This rule was causing false positives by matching the role itself (e.g., 'Abgabenstrafbehörde'). Replaced by more specific context rules.

**Content:**
```
als\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?!(?:Gesch\u00e4ftsf\u00fchrer|Pr\u00e4sident|Vorstand|Leiter|Manager|Inhaber|Eigent\u00fcmer|Mitglied|Vertreter|Beauftragter|Aufsichtsrat|Gesch\u00e4ftsf\u00fchrerin|Pr\u00e4sidentin|Vorstandin|Leiterin|Managerin|Inhaberin|Eigent\u00fcmerin|Mitgliedin|Vertreterin|Beauftragte|Aufsichtsr\u00e4tin|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Amtspartei|Gesamtrechtsnachfolger|Gesamtrechtsnachfolgerin|Leistungsgerbringerin|Zahlungsverpflichteten|Gemeinschuldner|Abgabenstrafbeh\u00f6rde|Beh\u00f6rde|Teil|Bf|Bf\.|Teilnehmer|Partei|Kanzlei|Firma|Gesellschaft|GmbH|AG|Partnerschaft))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 58 | 0 | 58 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 58 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_43`)


Die Zeiten ab Beendigung der entsprechenden Tätigkeit können nicht  mehr als Zeiten einer Berufsausbildung angesehen werden.

**False Positives:**

- `Zeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_51`)


monatlich € 1.000,- an meine Ex-Gattin überwiesen, die als Schulgeld galten.

**False Positives:**

- `Schulgeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Schulgeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_118`)


Nach § 17 Abs. 2 Z 1 StudFG gelten nicht als Studienwechsel im Sinne des Abs. 1 solche, bei  welchen die gesamten Vorstudienzeiten für die Anspruchsdauer des nunmehr betriebenen  Studiums berücksichtigt werden, weil sie dem nunmehr betriebenen Studium auf Grund der  besuchten Lehrveranstaltungen und absolvierten Prüfungen nach Inhalt und Umfang der  Anforderungen gleichwertig sind.

**False Positives:**

- `Studienwechsel im Sinne` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_144`)


Nicht hingegen gilt als Studienwechsel, wenn die gesamten Vorstudienzeiten in die neue  Studienrichtung eingerechnet werden.

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `role_based_identification`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e1c8479`  
**Description:**
Matches names following role indicators like 'Richter', 'Richterin'. Captures the full name including title and suffixes.

**Content:**
```
(?:durch\s+den\s+Richter|durch\s+die\s+Richterin|durch\s+den\s+Senatsvorsitzenden|durch\s+die\s+Senatsvorsitzende|durch\s+den\s+Schriftf\u00fchrer|durch\s+den\s+Liquidator|durch\s+den\s+Masseverwalter)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 11 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

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

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

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

- `Ashley Partenfelder` — partial — pred is substring of gold: `Mag. Ashley Partenfelder`

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

- `Farina Kohlstrunk` — partial — pred is substring of gold: `Priv.-Doz.in Farina Kohlstrunk`

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

- `Quirin Januszis` — partial — pred is substring of gold: `Priv.-Doz. Quirin Januszis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

</details>

---

## `name_after_comma_in_list`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c723ea57`  
**Description:**
Matches names appearing after a comma in a list or appositive context. TIGHTENED to exclude non-person words like 'Straße', 'Medizin', 'Zeugnis', 'Befund', 'Deutschland', 'Österreich', 'Abgabenstrafbehörde'.

**Content:**
```
,\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,|\s+(?:kurz:|Bf|Bf\.)|\s*$|\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s*,)(?!\s*(?:Straße|Medizin|Zeugnis|Befund|Anmerkung|Nachuntersuchung|Verdacht|Zustand|Note|Seite|Nr\.|Deutschland|Österreich|Abgabenstrafbehörde|Behörde|GmbH|GmbH\.|AG|Partnerschaft|Gesellschaft))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Nahrung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Statistik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Gasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_13`)


Am besagten Tag habe ich  bei Dienstantritt um 0600 Uhr, mein FzG mit dem beh. KZ.: 123, Marke, Farbe lackiert, am  Tatort abgestellt und die Gebühren welche der Parkometerabgabeverordnung entsprechen  mittels Kurzparkschein abgegolten.

**False Positives:**

- `Marke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_in_comma_list`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f6139da8`  
**Description:**
Matches names appearing after a comma in a list or appositive context, e.g., 'Beschwerdef\u00fchrer, Alan Faltinat'.

**Content:**
```
,\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,|\s*$|\s+\w+\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Nahrung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Statistik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Gasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_13`)


Am besagten Tag habe ich  bei Dienstantritt um 0600 Uhr, mein FzG mit dem beh. KZ.: 123, Marke, Farbe lackiert, am  Tatort abgestellt und die Gebühren welche der Parkometerabgabeverordnung entsprechen  mittels Kurzparkschein abgegolten.

**False Positives:**

- `Marke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `generic_honorifics`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `07d91ce9`  
**Description:**
Matches names preceded by 'Frau' or 'Herr'. Requires at least two words to avoid single-word false positives. Extended to capture suffixes like 'BA LLB'. TIGHTENED to avoid matching partial titles like 'Vet'.

**Content:**
```
(?:Frau|Herr|Herrn)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
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

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, Bakk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, Bakk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

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

## `beschwerdesache_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c42c0a90`  
**Description:**
Matches names appearing immediately after 'in der Beschwerdesache'. Updated to capture names WITH titles AND names WITHOUT titles. Stops at the address comma.

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s*,|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_preposition_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4c9f0780`  
**Description:**
Matches names following common prepositions or in 'in der Sache' contexts where the name is the first entity. Catches cases like 'der Beschwerde der [Name]' or 'in der Beschwerdesache [Name]' (if not caught by specific header rule).

**Content:**
```
(?:der|die)\s+(?:Beschwerde|Rechtsmittel|Antrag)\s+(?:der|des)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR)?\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `greeting_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a958e720`  
**Description:**
Matches names appearing after standard German legal greetings like 'Mit freundlichen Grüßen'.

**Content:**
```
(?:Mit freundlichen Grüßen|Mit herzlichen Grüßen|Hochachtungsvoll)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `party_in_complaint_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7a176545`  
**Description:**
Matches names following 'in der Beschwerdesache' or similar contexts. STRICTLY stops before address patterns (comma + number).

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `complaint_of_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ebf96c13`  
**Description:**
Matches names following 'Beschwerde des' or 'Beschwerde der'. Handles multiple titles and stops before addresses.

**Content:**
```
(?:Beschwerde|Rechtsmittel|Antrag)\s+(?:des|der)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `party_name_with_title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5e2a96d5`  
**Description:**
Specifically matches party names that start with a title (like KzlR, DDr.in) in the 'Beschwerdesache' context, ensuring the title is part of the match if it precedes the name.

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:KzlR|DDr\.in|DDr\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_born`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2fe0e05c`  
**Description:**
Matches names appearing after 'geboren am' (born on) to capture parents or individuals mentioned in birth contexts.

**Content:**
```
geboren\s+am\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `party_in_complaint_context_no_address`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e4c2475a`  
**Description:**
Matches names following 'in der Beschwerdesache' or similar contexts. FIXED: Ensures strict stopping before address (comma + number/street).

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s*,|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `beschwerdesache_party_name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `71f0680c`  
**Description:**
Matches party names appearing immediately after 'in der Beschwerdesache' or 'der Beschwerdesache'. Captures names with or without titles, stopping strictly before the address (comma + number).

**Content:**
```
(?:in\s+der|der)\s+Beschwerdesache\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*,\s*(?:\d+|\d+\s+[A-Z])
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

## `academic_and_professional_titles`

**F1:** 0.224 | **Precision:** 0.706 | **Recall:** 0.133  

**Format:** `regex`  
**Rule ID:** `e26ac21a`  
**Description:**
Matches names preceded by one or more academic/professional titles. Handles multiple consecutive titles (e.g., 'RgR Dipl. Kff.', 'VetR OMedR'). Stops before addresses.

**Content:**
```
(?<!\S)(?!(?:Richter|Richterin|Senatsvorsitzender|Senatsvorsitzende|fachkundige\s+Laienrichter|fachkundige\s+Laienrichterin|vertreten\s+durch)\s+)(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.706 | 0.133 | 0.224 | 17 | 12 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 12 | 5 | 78 |

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
| `Hon.-Prof.in OStR Tosca Knoller` | `Hon.-Prof.in OStR Tosca Knoller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

</details>

---

## `generic_honorifics`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `07d91ce9`  
**Description:**
Matches names preceded by 'Frau' or 'Herr'. Requires at least two words to avoid single-word false positives. Extended to capture suffixes like 'BA LLB'. TIGHTENED to avoid matching partial titles like 'Vet'.

**Content:**
```
(?:Frau|Herr|Herrn)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
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

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, Bakk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk, Bakk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, Bakk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `herrn_context`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Rule ID:** `0066ae82`  
**Description:**
Matches names preceded by 'Herrn' or 'Herr'. Strictly stops at the first comma or non-name word to avoid capturing addresses.

**Content:**
```
\b(?:Herrn|Herr)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 0 | 2 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

</details>

---

## `party_names_in_context`

**F1:** 0.022 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `60605e89`  
**Description:**
Matches names appearing after 'der' (genitive) or 'die' (accusative) in contexts like 'der Beschwerde der [Name]', 'die Beschwerde der [Name]'. Improved to handle multi-word names and stop at non-name characters.

**Content:**
```
(?:der|die)\s+(?:Beschwerde|Rechtsmittel|Antrag)\s+(?:der|des)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.022 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 18 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_47`)


Da der Einkommensteuerbescheid aufgrund der Beschwerde des Bf mit  Beschwerdevorentscheidung vom 12.03.2025 abgeändert wurde (zugunsten des Bf) erging am  12.03.2025 der neue (bzw. weitere) Bescheid über die Festsetzung von Anspruchszinsen 2021, in  dem diesem Umstand Rechnung getragen wurde (Gutschrift Anspruchszinsen in der Höhe von  Euro 7.963,60).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `role_based_identification`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e1c8479`  
**Description:**
Matches names following role indicators like 'Richter', 'Richterin'. Captures the full name including title and suffixes.

**Content:**
```
(?:durch\s+den\s+Richter|durch\s+die\s+Richterin|durch\s+den\s+Senatsvorsitzenden|durch\s+die\s+Senatsvorsitzende|durch\s+den\s+Schriftf\u00fchrer|durch\s+den\s+Liquidator|durch\s+den\s+Masseverwalter)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 11 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

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

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

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

- `Ashley Partenfelder` — partial — pred is substring of gold: `Mag. Ashley Partenfelder`

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

- `Farina Kohlstrunk` — partial — pred is substring of gold: `Priv.-Doz.in Farina Kohlstrunk`

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

- `Quirin Januszis` — partial — pred is substring of gold: `Priv.-Doz. Quirin Januszis`

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

- `Gabriele Friedbacher` — partial — pred is substring of gold: `Mag. Gabriele Friedbacher`

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

- `Juliana Bartjen` — partial — pred is substring of gold: `Priv.-Doz.in Juliana Bartjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Estelle Niederholz` — partial — pred is substring of gold: `Dr.in Estelle Niederholz`

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

- `Thassilo Averdiek` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Averdiek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dagobert Nordholt` — partial — pred is substring of gold: `Dr. Dagobert Nordholt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Peter Bilger` — partial — pred is substring of gold: `Mag. Peter Bilger`

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

## `beschwerdesache_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c42c0a90`  
**Description:**
Matches names appearing immediately after 'in der Beschwerdesache'. Updated to capture names WITH titles AND names WITHOUT titles. Stops at the address comma.

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s*,|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `representative_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3c42994b`  
**Description:**
Matches names following 'vertreten durch' (represented by) to capture legal representatives.

**Content:**
```
vertreten\s+durch\s+(?:die\s+)?(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 24 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

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

</details>

---

## `generic_preposition_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4c9f0780`  
**Description:**
Matches names following common prepositions or in 'in der Sache' contexts where the name is the first entity. Catches cases like 'der Beschwerde der [Name]' or 'in der Beschwerdesache [Name]' (if not caught by specific header rule).

**Content:**
```
(?:der|die)\s+(?:Beschwerde|Rechtsmittel|Antrag)\s+(?:der|des)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR)?\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `greeting_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a958e720`  
**Description:**
Matches names appearing after standard German legal greetings like 'Mit freundlichen Grüßen'.

**Content:**
```
(?:Mit freundlichen Grüßen|Mit herzlichen Grüßen|Hochachtungsvoll)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_comma_in_list`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c723ea57`  
**Description:**
Matches names appearing after a comma in a list or appositive context. TIGHTENED to exclude non-person words like 'Straße', 'Medizin', 'Zeugnis', 'Befund', 'Deutschland', 'Österreich', 'Abgabenstrafbehörde'.

**Content:**
```
,\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,|\s+(?:kurz:|Bf|Bf\.)|\s*$|\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s*,)(?!\s*(?:Straße|Medizin|Zeugnis|Befund|Anmerkung|Nachuntersuchung|Verdacht|Zustand|Note|Seite|Nr\.|Deutschland|Österreich|Abgabenstrafbehörde|Behörde|GmbH|GmbH\.|AG|Partnerschaft|Gesellschaft))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Nahrung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Statistik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Gasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_13`)


Am besagten Tag habe ich  bei Dienstantritt um 0600 Uhr, mein FzG mit dem beh. KZ.: 123, Marke, Farbe lackiert, am  Tatort abgestellt und die Gebühren welche der Parkometerabgabeverordnung entsprechen  mittels Kurzparkschein abgegolten.

**False Positives:**

- `Marke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_43`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) war am Freitag, 2.  Mai 2025 um 11:09 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Gasse,  abgestellt.

**False Positives:**

- `Gasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `1100 Wien`(address)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_187`)


Festzustellen war, dass für die haftungsgegenständlichen Umsatzsteuern, Lohnsteuern,  Kapitalertragsteuern, Körperschaftsteuern, Kammerumlagen, DB sowie Zuschlägen zum DB der  Bf. für deren Entrichtung Sorge zu tragen hatte, da deren Fälligkeiten in den Zeitraum seiner  Geschäftsführungstätigkeit fielen.

**False Positives:**

- `Lohnsteuern` — no gold match — likely missing annotation
- `Körperschaftsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `techn_hr_title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a0833bc2`  
**Description:**
Specifically matches the 'Techn R HR' title pattern found in training data, which is not covered by generic titles.

**Content:**
```
(?:Techn R|HR)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 39 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

</details>

---

## `name_in_comma_list`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f6139da8`  
**Description:**
Matches names appearing after a comma in a list or appositive context, e.g., 'Beschwerdef\u00fchrer, Alan Faltinat'.

**Content:**
```
,\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,|\s*$|\s+\w+\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Nahrung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Statistik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Gasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_13`)


Am besagten Tag habe ich  bei Dienstantritt um 0600 Uhr, mein FzG mit dem beh. KZ.: 123, Marke, Farbe lackiert, am  Tatort abgestellt und die Gebühren welche der Parkometerabgabeverordnung entsprechen  mittels Kurzparkschein abgegolten.

**False Positives:**

- `Marke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_43`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) war am Freitag, 2.  Mai 2025 um 11:09 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Gasse,  abgestellt.

**False Positives:**

- `Gasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `1100 Wien`(address)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_187`)


Festzustellen war, dass für die haftungsgegenständlichen Umsatzsteuern, Lohnsteuern,  Kapitalertragsteuern, Körperschaftsteuern, Kammerumlagen, DB sowie Zuschlägen zum DB der  Bf. für deren Entrichtung Sorge zu tragen hatte, da deren Fälligkeiten in den Zeitraum seiner  Geschäftsführungstätigkeit fielen.

**False Positives:**

- `Lohnsteuern` — no gold match — likely missing annotation
- `Körperschaftsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `party_in_complaint_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7a176545`  
**Description:**
Matches names following 'in der Beschwerdesache' or similar contexts. STRICTLY stops before address patterns (comma + number).

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `complaint_of_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ebf96c13`  
**Description:**
Matches names following 'Beschwerde des' or 'Beschwerde der'. Handles multiple titles and stops before addresses.

**Content:**
```
(?:Beschwerde|Rechtsmittel|Antrag)\s+(?:des|der)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `party_name_with_title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5e2a96d5`  
**Description:**
Specifically matches party names that start with a title (like KzlR, DDr.in) in the 'Beschwerdesache' context, ensuring the title is part of the match if it precedes the name.

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:KzlR|DDr\.in|DDr\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_with_suffix_no_title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `97deaa84`  
**Description:**
Matches names with suffixes (e.g., BA, LLB, Bakk. techn.) when no title is present, specifically in contexts like 'vertreten durch' or list items. Tightened to capture full suffix and avoid street names.

**Content:**
```
(?:vertreten\s+durch\s+(?:die\s+)?|,\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s*,|\s*$|\s+(?:vertreten|durch|als|als\s+RNF))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 65 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Nahrung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Statistik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_187`)


Festzustellen war, dass für die haftungsgegenständlichen Umsatzsteuern, Lohnsteuern,  Kapitalertragsteuern, Körperschaftsteuern, Kammerumlagen, DB sowie Zuschlägen zum DB der  Bf. für deren Entrichtung Sorge zu tragen hatte, da deren Fälligkeiten in den Zeitraum seiner  Geschäftsführungstätigkeit fielen.

**False Positives:**

- `Lohnsteuern,  Kapitalertragsteuern, Körperschaftsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_as_role`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `807a9f64`  
**Description:**
Matches names appearing after 'als' (as) followed by a role. STRICTLY excludes common job titles and legal roles that are not names. REMOVED: This rule was causing false positives by matching the role itself (e.g., 'Abgabenstrafbehörde'). Replaced by more specific context rules.

**Content:**
```
als\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?!(?:Gesch\u00e4ftsf\u00fchrer|Pr\u00e4sident|Vorstand|Leiter|Manager|Inhaber|Eigent\u00fcmer|Mitglied|Vertreter|Beauftragter|Aufsichtsrat|Gesch\u00e4ftsf\u00fchrerin|Pr\u00e4sidentin|Vorstandin|Leiterin|Managerin|Inhaberin|Eigent\u00fcmerin|Mitgliedin|Vertreterin|Beauftragte|Aufsichtsr\u00e4tin|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Amtspartei|Gesamtrechtsnachfolger|Gesamtrechtsnachfolgerin|Leistungsgerbringerin|Zahlungsverpflichteten|Gemeinschuldner|Abgabenstrafbeh\u00f6rde|Beh\u00f6rde|Teil|Bf|Bf\.|Teilnehmer|Partei|Kanzlei|Firma|Gesellschaft|GmbH|AG|Partnerschaft))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 58 | 0 | 58 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 58 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_43`)


Die Zeiten ab Beendigung der entsprechenden Tätigkeit können nicht  mehr als Zeiten einer Berufsausbildung angesehen werden.

**False Positives:**

- `Zeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_51`)


monatlich € 1.000,- an meine Ex-Gattin überwiesen, die als Schulgeld galten.

**False Positives:**

- `Schulgeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Schulgeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_118`)


Nach § 17 Abs. 2 Z 1 StudFG gelten nicht als Studienwechsel im Sinne des Abs. 1 solche, bei  welchen die gesamten Vorstudienzeiten für die Anspruchsdauer des nunmehr betriebenen  Studiums berücksichtigt werden, weil sie dem nunmehr betriebenen Studium auf Grund der  besuchten Lehrveranstaltungen und absolvierten Prüfungen nach Inhalt und Umfang der  Anforderungen gleichwertig sind.

**False Positives:**

- `Studienwechsel im Sinne` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_144`)


Nicht hingegen gilt als Studienwechsel, wenn die gesamten Vorstudienzeiten in die neue  Studienrichtung eingerechnet werden.

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Finanzstrafbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_6`)


Entscheidungsgründe  Verfahrensgang:  Mit Erkenntnis des Spruchsenates I-1 als Organ des Amtes für Betrugsbekämpfung als  Finanzstrafbehörde vom 2. Mai 2024 wurde der Beschwerdeführer (in der Folge kurz: Bf.) der  Finanzvergehen a) der Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG und b) der  Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG für schuldig erkannt.

**False Positives:**

- `Organ` — no gold match — likely missing annotation
- `Finanzstrafbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Amtes für Betrugsbekämpfung`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_16`)


Gegen den abweisenden Bescheid vom 02. Dezember 2024 erhob der Bf. mit Schreiben vom  17.12.2024 Beschwerde und führte dazu begründend aus: „Gerade während eines laufenden  Insolvenzverfahrens kann ich als Schuldner nur über den unpfändbaren Bezugsanteil verfügen.

**False Positives:**

- `Schuldner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Abgabenstrafbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

**False Positives:**

- `Vollstreckungsbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_20`)


Zudem wurde gemäß § 64  Abs. 2 Verwaltungsstrafgesetz (VStG) ein Betrag von 10,00 Euro als Beitrag zu den Kosten des  Strafverfahrens auferlegt, wodurch sich der zu zahlende Gesamtbetrag auf 65,00 Euro belief.

**False Positives:**

- `Beitrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_51`)


Rechtsgrundlage und rechtliche Würdigung:    Gemäß § 4 Abs. 1 Wiener Parkometergesetz 2006 sind Handlungen und Unterlassungen, durch  die die Abgabe hinterzogen oder fahrlässig verkürzt wird, als Verwaltungsübertretungen mit  Geldstrafen bis zu 365 Euro zu bestrafen.

**False Positives:**

- `Verwaltungsübertretungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_74`)


Die beschwerdeführende Partei hat daher gemäß § 52 Abs. 2 VwGVG weitere 11,00 Euro als  Kostenbeitrag zum verwaltungsgerichtlichen Verfahren zu leisten.

**False Positives:**

- `Kostenbeitrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `Vollstreckungsbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_4`)


Die Bemessungsgrundlagen und die Höhe der festgesetzten Abgaben sind den als Beilage  angeschlossenen Berechnungsblättern zu entnehmen und bilden einen Bestandteil des  Spruches dieses Erkenntnisses.

**False Positives:**

- `Beilage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_8`)


Der Bf. ist als Musiker sowohl selbständig als auch nichtselbständig tätig.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_11`)


Im Rahmen der beim Bf. durchgeführten Betriebsprüfung, die Jahre 2010 bis 2014 betreffend,  wurde die selbständige Tätigkeit als Musiker gemäß § 1 Abs. 2 Liebhabereiverordnung (LVO) ab  2012 als Liebhaberei eingestuft.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation
- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_13`)


Im gegebenen Fall gehe die Betriebsprüfung vom  Vorliegen einer solchen aus, da der Bf. auch nichtselbständige Einkünfte aus der Tätigkeit als  Musiker erzielt.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_17`)


In der Folge wurden die Verluste aus der selbständigen Tätigkeit als Musiker in den Jahren  2012 bis 2014 nicht anerkannt und im Bp-Bericht wurde dies wie folgt dargestellt:      2 von 14 Seite 3 von 14

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_20`)


Die Verfahren betreffend Einkommensteuer 2012 und 2013 wurden wiederaufgenommen und  es wurden am 19.10.2016 neue Einkommensteuerbescheide für diese Jahre und der  Erstbescheid für 2014 erlassen, in denen die Verluste aus der selbständigen Tätigkeit als  Musiker nicht berücksichtigt wurden.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_21`)


Gegen diese Einkommensteuerbescheide vom 19.10.2016 brachte der steuerliche Vertreter  am 14.11.2016 eine Beschwerde ein und führte aus, dass sich die Beschwerde gegen die  Feststellungen der abgabenbehördlichen Prüfung richte, welche die ausgeübte selbständige  Tätigkeit des Mandanten als Musiker ab dem Jahr 2012 als Liebhaberei gemäß § 1 Abs. 2 LVO  einstufe.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation
- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_27`)


Da aber inhaltliche Kongruenz seiner Tätigkeiten gegeben ist, kann der  selbständig erbrachte Teil der Tätigkeit unseres Mandanten daher weder als besondere, im  Privaten gelegene Neigung noch als Freizeitbetätigung bezeichnet werden, vielmehr ist die  Gesamttätigkeit jeweils für die einzelnen Tätigkeitsteile als gegenseitig förderlich zu sehen: ein  Dienstverhältnis als Musiker kommt z.B zu Stande, wenn ein selbständiger Musiker einem  Musicalveranstalter auffällt und er diesen für sein Musicalorchester engagiert.

**False Positives:**

- `Freizeitbetätigung` — no gold match — likely missing annotation
- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_29`)


Abgesehen von obigen Betrachtungen ist für die Einstufung einer Tätigkeit als Liebhaberei die  Frage, ob ein Gesamtverlust seit Beginn dieser Tätigkeit bzw. seit Änderung der  Bewirtschaftung entstanden ist, von zentraler Bedeutung.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_30`)


Die diesbezügliche Feststellung der Betriebsprüfung ist jedenfalls verfahrensrechtlich fehlerhaft,  da diese lediglich die letzten 3 Jahre vor Betriebsaufgabe als Liebhabereitätigkeit eingestuft  hat, ohne zu prüfen, ob ein für eine derartige Vorgangsweise erforderlicher Gesamtverlust  entstanden ist.

**False Positives:**

- `Liebhabereitätigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_39`)


Deshalb aber zu vermeinen, die gewinnträchtigen  Jahre unseres Mandanten in den Jahren davor außer Acht lassen zu können, wird wohl für die  Einstufung als Liebhaberei nicht reichen.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_42`)


Unser Mandant hat in den Hochzeiten seiner Tätigkeit als Mitglied zahlreicher Musikensembles  (unter anderem dem damals weltberühmten, weltweit konzertierenden Orchester2) in den  Siebziger- und Achtzigerjahren jährlich Honorare zwischen S 80.000 [umgerechnet € 5.813,83]  und S 120.000 [umgerechnet € 8.720,74] bzw. Einkünfte von jährlich S 60.000,- [umgerechnet €  4.360,37] bis S 100.000,- [umgerechnet € 7.267,28] erwirtschaftet.

**False Positives:**

- `Mitglied` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_47`)


Hier aber ausschließlich aufgrund der faktischen Nichtfeststellbarkeit eines Gesamtgewinnes  durch das Finanzamt eine hauptberuflich ausgeübte, lebenslange Tätigkeit für die letzten 3  Jahre vor Betriebsaufgabe als Liebhaberei einzustufen, ohne dass eine Änderung der  Bewirtschaftung eingetreten oder seitens der Betriebsprüfung behauptet worden wäre,  widerspricht Gesetz, Richtlinien sowie ständiger Rechtsprechung.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_72`)


Der Bf. habe seine hauptberufliche Tätigkeit als Musiker unverändert,  von Beginn an in der gleichen Art und Weise im Bereich Vibraphon/Schlagwerk ausgeübt.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_79`)


Es kam somit niemals zu einer Änderung der Bewirtschaftung, auch nicht ab  dem — scheinbar willkürlich gewählten - Jahr 2012, weshalb als Beurteilungszeitraum für einen  Gesamtüberschuss der hauptberuflichen Tätigkeit des Bf. nur jener von der Betriebseröffnung  bis zur Beendigung der Tätigkeit mit Ende 2014 sein könne.

**False Positives:**

- `Beurteilungszeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_80`)


Die Tätigkeit als Musiker könne nicht mit den Maßstäben eines normalen Gewerbebetriebes  gemessen werden.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_85`)


Der Bf. ist ein akademisch ausgebildeter Musiker und war in den beschwerdegegenständlichen  Jahren selbständig und nichtselbständig als Musiker tätig.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_90`)


Im Zuge der durchgeführten Betriebsprüfung wurde die selbständige Tätigkeit als Musiker für  die Jahre 2012 bis 2014 als Liebhaberei gemäß § 1 Abs. 2 LVO eingestuft und die Verluste  daraus nicht anerkannt.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation
- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_119`)


Zu Spruchpunkt I. (Stattgabe)  Strittig ist im gegenständlichen Verfahren, ob die künstlerische Tätigkeit des Bf. als Musiker in  den Jahren 2012 bis 2014 eine steuerlich anzuerkennende Einkunftsquelle darstellt oder ob es  sich aus steuerlicher Sicht um eine sog.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_121`)


Aus dem Begriff des Einkommens bzw. konkret aus der Umschreibung der Einkünfte als  Gewinn bzw. als Überschuss der Einnahmen über die Werbungskosten wird abgeleitet, dass  nur eine Tätigkeit, die auf Dauer ein positives wirtschaftliches Gesamtergebnis erbringt, als  Einkunftsquelle in Betracht kommt und bei der Einkommensteuer zu berücksichtigen ist.

**False Positives:**

- `Gewinn` — no gold match — likely missing annotation
- `Einkunftsquelle in Betracht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_123`)


Im Fall einer solchen privaten  Verursachung wird die Tätigkeit nicht als Einkunftsquelle anerkannt, mit der weiteren Folge,  dass die Verluste steuerlich nicht verwertet werden können, d.h. nicht mit anderen - positiven  - Einkünften ausgeglichen werden können.

**False Positives:**

- `Einkunftsquelle` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_134`)


Ob eine Tätigkeit als Musiker typisch erwerbswirtschaftlich ist oder typischerweise einer  besonderen in der Lebensführung begründeten Neigung entspricht, ist im Einzelfall anhand  ihrer Art und ihres Umfanges zu beurteilen.

**False Positives:**

- `Musiker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

**False Positives:**

- `Bestandteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_76`)


Erweist sich der Stammabgabenbescheid nachträglich als rechtswidrig und wird er  entsprechend abgeändert (oder aufgehoben), so wird diesem Umstand mit einem an den  Abänderungsbescheid (Aufhebungsbescheid) gebundenen Zinsenbescheid Rechnung getragen  (z.B. Gutschriftszinsen als Folge des Wegfalles einer rechtswidrigen Nachforderung).

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `Rechtsinstanz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_7`)


Leichte Fahrlässigkeit gelte bereits als Verschulden.

**False Positives:**

- `Verschulden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_12`)


Laut Firmenbuchauszug sei der Bf. seit 22.6.2001 als Vertreter der primärschuldnerischen  GmbH bestellt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_13`)


In dieser Funktion als Geschäftsführer sei ihm die Wahrnehmung der  abgabenrechtlichen Verpflichtungen der GmbH oblegen.

**False Positives:**

- `Geschäftsführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_42`)


Zur Stellung als Vertreter führte das Finanzamt in der Begründung aus, dass der Bf. von  22.06.2001 bis zur Insolvenzeröffnung der Primärschuldnerin (in weiterer Folge kurz GmbH) im  Firmenbuch als handelsrechtlicher Geschäftsführer der GmbH eingetragen gewesen sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_91`)


Durch die Nichtbeachtung dieses  Grundsatzes für die Umsatzsteuer, den Dienstgeberbeitrag, den Zuschlag zum  Dienstgeberbeitrag und die Körperschaftsteuer habe der Bf. seine abgabenrechtlichen  Pflichten als Vertreter der GmbH verletzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_100`)


Die Unterlassung der Abfuhr der Lohnsteuer stellt eine schuldhafte Verletzung der  abgabenrechtlichen Pflichten als Vertreter der GmbH dar.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_106`)


Die Unterlassung der Abfuhr der Kapitalertragsteuer stelle eine schuldhafte Verletzung  abgabenrechtlichen Pflichten des Bf. als Vertreter der GmbH dar   Betreffend das Verschulden des Vertreters erläuterte das Finanzamt, dass Verletzungen  abgabenrechtlicher Pflichten nur dann zur Haftungsinanspruchnahme berechtigten, wenn die  Verletzung schuldhaft erfolgt sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_174`)


Haftungsvoraussetzungen  - Abgabenforderungen gegen die vertretene Gesellschaft  - erschwerte Einbringlichkeit der Abgabenforderungen  - Stellung des Geschäftsführers als Vertreter  - abgabenrechtliche Pflichtverletzung des Vertreters  - dessen Verschulden an der Pflichtverletzung  - Ursächlichkeit der Pflichtverletzung für die erschwerte Einbringlichkeit der Abgaben  Abgabenforderungen

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_195`)


Am Bf., dem als Geschäftsführer der Primärschuldnerin ausreichend Einblick in die Gebarung  zustand, war es gelegen, das Ausmaß der quantitativen Unzulänglichkeit der in den  Fälligkeitszeitpunkten der Abgaben zur Verfügung stehenden Mittel nachzuweisen (VwGH  19.11.1998, 97/15/0115), da nicht die Abgabenbehörde das Ausreichen der Mittel zur  Abgabenentrichtung nachzuweisen hat, sondern der zur Haftung herangezogene  Geschäftsführer das Fehlen ausreichender Mittel (VwGH 23.4.1998, 95/15/0145).

**False Positives:**

- `Geschäftsführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_221`)


Ergebnis  Auf Grund des Vorliegens der gesetzlichen Voraussetzungen erfolgte somit die  Inanspruchnahme des Bf. als Haftungspflichtiger für die nachstehenden Abgabenschuldigkeiten  der Primärschuldnerin im Ausmaß von nunmehr 128.402,72 € zu Recht.

**False Positives:**

- `Haftungspflichtiger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_85`)


Der angefochtene Bescheid war hinsichtlich der Festsetzung des Säumniszuschlages für  die Umsatzsteuer daher in der Weise abzuändern, dass als Bemessungsgrundlage die  14.218,49 Euro heranzuziehen und der Säumniszuschlag mit 284,37 Euro festzusetzen war.

**False Positives:**

- `Bemessungsgrundlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_100`)


Mit der Einschränkung  „insoweit“ ist die zeitliche Beschränkung der Wirkung des § 217 Abs. 4 BAO gemeint, die nur so  lange gegeben ist, als Säumniszuschlag verhindernde Gründe vorliegen (vgl.  Ellinger/Sutter/Urtz, BAO3, § 217 Rz 33).

**False Positives:**

- `Säumniszuschlag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_after_born`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2fe0e05c`  
**Description:**
Matches names appearing after 'geboren am' (born on) to capture parents or individuals mentioned in birth contexts.

**Content:**
```
geboren\s+am\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `genitive_party_name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1edfdc30`  
**Description:**
Matches names in genitive contexts like 'des [Name]' or 'der [Name]' when not preceded by specific headers like 'Beschwerdesache'. FIXED: Excludes 'Beschwerdesache' context and stops before addresses.

**Content:**
```
(?<!\s)(?:des|der)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,|\s+(?:u\.\s+Mitbes|Bf|Bf\.)|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 31 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_20`)


Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_30`)


7. Mit Beschwerdevorentscheidung vom 18.03.2022 wurde die Beschwerde als unbegründet  abgewiesen und dies wie folgt begründet:  „Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_66`)


Wenn ein  Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder Anspruch,  wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen.

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_85`)


Die Belastung darf weder Betriebsausgaben, Werbungskosten noch Sonderausgaben sein.

**False Positives:**

- `Betriebsausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_96`)


Ob dies der Fall ist, bestimmt  sich nach dem Urteil billig und gerecht denkender Menschen, in dem das Rechtsgefühl der  6 von 8 Seite 7 von 8

**False Positives:**

- `Menschen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `party_in_complaint_context_no_address`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e4c2475a`  
**Description:**
Matches names following 'in der Beschwerdesache' or similar contexts. FIXED: Ensures strict stopping before address (comma + number/street).

**Content:**
```
(?:in\s+der\s+|im\s+|in\s+der)\s+(?:der\s+)?(?:Beschwerdesache|Rechtsmittelsache|Rechtssache|Revisionssache)\s+(?:(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Ing\.|VetR|OMedR|RgR|StR|\u00d6kR|KommR|MedR|PhD|MSc|BEd|LLB|LLM|Bakk\. art\.|Bakk\. rer\. nat\.|Bakk\. art\. MA|Bakk\. rer\. nat\. MBA|Techn R|HR|Prof\.in MedR|OStR|KzlR|DDr\.in|DDr\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?=,\s*\d|,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s*,|\s*$|\s+(?:vertreten|durch|als))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `beschwerdesache_party_name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `71f0680c`  
**Description:**
Matches party names appearing immediately after 'in der Beschwerdesache' or 'der Beschwerdesache'. Captures names with or without titles, stopping strictly before the address (comma + number).

**Content:**
```
(?:in\s+der|der)\s+Beschwerdesache\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:von|van|de|zu|im|am|in)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*,\s*(?:\d+|\d+\s+[A-Z])
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

