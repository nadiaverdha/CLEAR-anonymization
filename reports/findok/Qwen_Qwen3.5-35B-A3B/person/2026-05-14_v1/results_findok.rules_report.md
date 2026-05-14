# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-14T03:33:23.494289

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-14_v1/config.yaml 
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
| Max samples in prompt | 60 |
| Refinement iterations | 0 |
| Seed | 42 |
| Agentic | False |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 63.0% |
| True Positives | 13 |
| False Positives | 596 |
| False Negatives | 77 |
| Total Gold Entities | 90 |
| Micro Precision | 2.1% |
| Micro Recall | 14.4% |
| Micro F1 | 3.7% |
| Macro F1 | 3.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Dr_in_Person` | 2.2% | 100.0% | 1.1% | 1 | 1 | 0 |
| `Herr_Person` | 4.3% | 100.0% | 2.2% | 2 | 2 | 0 |
| `Von_Person` | 2.2% | 50.0% | 1.1% | 2 | 1 | 1 |
| `Fuer_Person_Fixed` | 2.2% | 33.3% | 1.1% | 3 | 1 | 2 |
| `Preposition_Person` | 2.2% | 33.3% | 1.1% | 3 | 1 | 2 |
| `Frau_Person` | 4.1% | 25.0% | 2.2% | 8 | 2 | 6 |
| `Pronoun_Person` | 7.0% | 16.7% | 4.4% | 24 | 4 | 20 |
| `Title_Person_General_Fixed` | 1.6% | 0.9% | 5.6% | 552 | 5 | 547 |
| `HR_Person` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `RgR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Herrn_Frau_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nach_Person` | 0.0% | 0.0% | 0.0% | 40 | 0 | 40 |
| `Mandantin_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nachname_Wie_Bf_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sohn_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gegen_Person_Fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Name_No_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `StR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Person_CaseContext` | 0.0% | 0.0% | 0.0% | 16 | 0 | 16 |
| `General_Person_Context` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Role_Person` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Name_With_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Date_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zu_Person` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Herr_Abbrev_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KzlR_Title_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag_Person` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Title_Person_General_Fixed`

**F1:** 0.016 | **Precision:** 0.009 | **Recall:** 0.056  

**Format:** `regex`  
**Description:**
Captures names with academic/professional titles. Strictly excludes legal entities, document headers, and common false positives. Requires a title prefix.

**Content:**
```
\b(?:KommR\s+Ing\.|(?:Mag\.a\s+Dr\.in|Dr\.in\s+Dr\.in|Dr\.in|Dr\.|Prof\.|Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Bakk\.\s+iur\.|Dipl\.-Ing\.|\u00d6kR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+rer\.\s+nat\.\s+MBA|HR|VetR|Techn\s+R|Mag\.|Mag\.a|OStR\s+Ing\.|Ing\.|Hon\.-Prof\s+Univ\.-Prof\.|Univ\.-Prof\s+Hon\.-Prof\.|Hon\.-Prof\.in\s+Priv\.-Doz\.in|Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|Mag\.\s+Ing\.|Mag\.\s+Dipl\.|Ri|OSR|OMedR|DDr\.?|OStR|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|Hon\.-Prof\.\s+Hon\.-Prof\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Bundesfinanzgericht|Das|Die|Der|Die\s+Beschwerde|Die\s+Beschwerden|Der\s+Beschwerde|Die\s+Vorlageantrag|Die\s+Einkommensteuerbescheide|Das\s+Bundesfinanzgericht|Die\s+Beschwerdef\u00fchrerin|Sachverhalt|Im|In|Laut|Es|Nach|Mit|Durch|Gegen|Wegen|Zu|Von|Bei|F\u00fcr|Auf|Unter|Ober|In|An|Um|Ohne|Seit|Bis|Zwischen|W\u00e4hrend|Trotz|Wegen|Wider|Ohne|Neben|Gegen\u00fcber|Entlang|Au\u00dfer|Innerhalb|Au\u00dferhalb|W\u00e4hrend|Trotz|Wegen|Wider|Ohne|Neben|Gegen\u00fcber|Entlang|Au\u00dfer|Innerhalb|Au\u00dferhalb|Zum|Mit|Entscheidungsgr\u00fcnde|Die\s+BF|Die\s+BF\s+ist|Die\s+BF\s+ist|Die\s+BF\s+ist|Die\s+BF\s+ist|S\u00e4mtliche|Verfahrensgang|Die\s+Beschwerde|Der\s+Beschwerde|Die\s+Beschwerden|Der\s+Vorlageantrag|Die\s+Einkommensteuerbescheide|Alternativen|Investmentfonds|Verwaltung|Wirtschaft|Steuerberatungsgesellschaft|Wirtschaftstreuhand|Grant\s+Thornton|Ernst\s+&\s+Young|Djuric\s+&\s+Oberger|Nowothnig|Depp|Wind|Verband|Verein|Stiftung|Firma|Beh\u00f6rde|Amt|Bescheid|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Begr\u00fcndung|Mit\s+Beschluss|IM\s+NAMEN|REPUBLIC|REPUBLIK|BESCHLUSS|VERFAHREN|SACHE|ORDNUNGSBEGRIFF|NACHTRAG|ANMERKUNG|HINWEIS|ZUSATZ|ERL\u00c4UTERUNG|BEMERKUNG|FESTSTELLUNG|ENTSCHEIDUNG|URTEIL|RECHTSPRECHUNG|GESETZ|VERORDNUNG|RAT|KOMMISSION|PARLAMENT|MINISTERIUM|BEH\u00d6RDE|AMT|FINANZAMT|STEUERAMT|GERICHT|BUNDESFINANZGERICHT|LANDGERICHT|OBERSGERICHT|VERWALTUNGSGERICHT|VERWALTUNGSGERICHTSHOF|VERFAHRENSBEHANDLUNG|VERFAHRENSGANG|VERFAHRENSABLAUF|VERFAHRENSSTAND|VERFAHRENSSTATUS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.009 | 0.056 | 0.016 | 552 | 5 | 547 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 547 | 85 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`
- `Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `Kind Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Die Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 4  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `In Beantwortung` — no gold match — likely missing annotation
- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_7`)


3. Mit Bescheid vom 12.11.2019 forderte das Finanzamt die für den Zeitraum von November  2017 bis Juni 2018 bezogenen Beträge an Familienbeihilfe und Kinderabsetzbeträgen iHv.

**False Positives:**

- `Mit Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Die Bescheidbegründung` — no gold match — likely missing annotation
- `Ihre Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Nach_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'nach' (e.g., 'Verlassenschaft nach dem...'), indicating a deceased person or heir. Updated to handle 'des' and 'der'.

**Content:**
```
\b(?:nach|Nach)\s+(?:dem|der|den)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 40 | 0 | 40 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 40 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Rausschmiss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_44`)


Ein solches ist nach der Judikatur der Höchstgerichte zu  diesem Themenkreis jedoch nicht erforderlich.

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

**False Positives:**

- `Sommersemester` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_137`)


Vorausgeschickt sei, dass zwar einerseits nach dem Universitätsgesetz 2002 (UG) die  Universitäten autonom sind, jedoch zur besseren Vergleichbarkeit in Folge des Bologna- Prozesses Standards aufgestellt wurden, die in den Studienplänen abzubilden sind.

**False Positives:**

- `Universitätsgesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Pronoun_Person`

**F1:** 0.070 | **Precision:** 0.167 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures person names following pronouns like 'Er', 'Sie', 'Es' or in parentheses. Refined to avoid matching common nouns.

**Content:**
```
(?:^|\.|\?|\!|\(|,)\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*|\s*\)|\s*$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|Sohn|Tochter|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.044 | 0.070 | 24 | 4 | 20 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 20 | 75 |

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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`
- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `Party_Person_CaseContext`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following case context words like 'Beschwerdesache'. Uses capture group to exclude the trigger word.

**Content:**
```
(?:Beschwerdesache|Rechtssache|Revisionssache|Verfahren|Sache|in\s+der|gegen)\s+(?:der\s+|des\s+|die\s+|den\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?=,|\s+\d+|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 16 | 0 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 16 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Lage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Fassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

</details>

---

## `Frau_Person`

**F1:** 0.041 | **Precision:** 0.250 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names following 'Frau' to extract the name without the title. Refined to avoid matching 'Frau' as part of a title like 'Frau Rechtsanwältin'.

**Content:**
```
\bFrau\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Rechtsanw\u00e4ltin|Anwalt|Vertreter|Vertreterin|Schriftf\u00fchrer|Schriftf\u00fchrerin|Gesch\u00e4ftsf\u00fchrer|Gesch\u00e4ftsf\u00fchrerin|Vorsitzender|Vorsitzende|Richter|Richterin|Professor|Professoren|Dozent|Dozentin|Lehrer|Lehrerin|Arzt|\u00c4rztin|Ingenieur|Ingenieurin|Architekt|Architektin|Notar|Notarin|Steuerberater|Steuerberaterin|Wirtschaftspr\u00fcfer|Wirtschaftspr\u00fcferin|Banker|Bankerin|Manager|Managerin|Direktor|Direktorin|Pr\u00e4sident|Pr\u00e4sidentin|Sekret\u00e4r|Sekret\u00e4rin|Assistent|Assistentin|Mitarbeiter|Mitarbeiterin|Kollege|Kollegin|Freund|Freundin|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.022 | 0.041 | 8 | 2 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 6 | 81 |

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

## `RgR_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically captures 'RgR' (Regierungsrat) followed by a name, excluding cases where HR follows (handled by HR_Person).

**Content:**
```
\bRgR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?!\s+HR)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Herrn_Frau_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'Herrn' or 'Frau', allowing for optional titles including 'Techn R'.

**Content:**
```
\b(Herrn|Frau)\s+(?:OSR|OMedR|DDr\.?|OStR|Dr\.in|Dr\.|Mag\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Bakk\. iur\.|Dipl\.-Ing\.|ÖkR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Univ\.-Prof\.in|Priv\.-Doz\.in|Hon\.-Prof\.in|Dr\. Dr\. Priv\.-Doz\.|Techn R)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mandantin_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'Mandantin' or 'Mandant' (e.g., 'meiner Mandantin, Frau Livia Roux').

**Content:**
```
(?:Mandantin|Mandant)(?:,\s+)?(?:Frau|Herr)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nachname_Wie_Bf_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after the specific legal marker '(Nachname wie Bf.)'.

**Content:**
```
\(Nachname wie Bf\.\)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sohn_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'Sohn' (son) in contexts like 'meinem Sohn', 'Ihr Sohn'.

**Content:**
```
(?:meinem|Ihr|sein|unser|deinem)\s+Sohn,?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gegen_Person_Fixed`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after 'gegen', strictly requiring a capitalized name and excluding common nouns like 'Firma' or 'Gesellschaft'.

**Content:**
```
\b(?:gegen|Gegen)\s+(?:die|der|den|dem|einer|einem|eine)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Party_Name_No_Title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'für' (for) or 'Kinder' (children) in family contexts, handling un-titled names.

**Content:**
```
(?:für\s+die\s+Kinder|Kinder\s+|für\s+Kinder)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `StR_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names with 'StR' (Strafrecht) title. Fixed to stop capturing addresses.

**Content:**
```
\bStR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_With_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names with academic or professional suffixes like ', BA', ', Bakk. art.', ', MBA' that appear after a title or in case contexts. Includes title prefix if present.

**Content:**
```
\b(?!(?:Frau|Herr)\s)(?:([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s*,\s*)?(?:([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+))(?:\s*,\s*(?:BA|B\.A\.|B\.A\.\s+iur\.|Bakk\.\s+art\.|Bakk\.\s+rer\.\s+nat\.|MBA|LL\.M\.|LL\.B\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Date_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names immediately following a date pattern (e.g., '22.9.2016 Ida Vetterlin').

**Content:**
```
(?:^|\s)(\d{1,2}\.\d{1,2}\.\d{2,4})\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
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

## `Pronoun_Person`

**F1:** 0.070 | **Precision:** 0.167 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures person names following pronouns like 'Er', 'Sie', 'Es' or in parentheses. Refined to avoid matching common nouns.

**Content:**
```
(?:^|\.|\?|\!|\(|,)\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*|\s*\)|\s*$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|Sohn|Tochter|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.167 | 0.044 | 0.070 | 24 | 4 | 20 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 20 | 75 |

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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`
- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of Bristol`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Eine Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_112`)


Bei Kindern, die eine in § 3 des Studienförderungsgesetzes 1992, BGBl.Nr. 305, genannte  Einrichtung besuchen, ist eine Berufsausbildung nur dann anzunehmen, wenn sie die  vorgesehene Studienzeit pro Studienabschnitt um nicht mehr als ein Semester oder die  vorgesehene Ausbildungszeit um nicht mehr als ein Ausbildungsjahr überschreiten.

**False Positives:**

- `Bei Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_30`)


Ein Rechtfertigungsgrund, also eine Norm, die das tatbestandsmäßige Verhalten  ausnahmsweise erlaube bzw. welche die Strafbarkeit aufheben würde, liege im  gegenständlichen Fall nicht vor.

**False Positives:**

- `Ein Rechtfertigungsgrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_49`)


Der Abstellort, der Beanstandungszeitpunkt und die Lenkereigenschaft des Bf. wurden vom Bf.  im gegenständlichen Fall nicht bestritten.

**False Positives:**

- `Der Abstellort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_74`)


Zur  Frage, wie lange ein Zuwarten auf einen Operationstermin ohne erhebliche medizinische  Nachteile möglich gewesen wäre, wird allgemein ausgeführt, dass ein Abwarten konkreter  motorischer Schwächen, um dann erst die Operation vorzunehmen, sicherlich nicht der  optimale Verlauf wäre und zudem (wiederum allgemein) angemerkt, dass eine zu späte  operative Versorgung zu bleibenden Wurzelschäden und motorischen Schwächen führen kann.

**False Positives:**

- `Zur  Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_102`)


Bloße Wünsche, Befürchtungen oder Standesrücksichten der Betroffenen reichen nicht, um die  Zwangsläufigkeit zu rechtfertigen.

**False Positives:**

- `Bloße Wünsche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `Auch Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `Der Zeitpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `Zum Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_181`)


Erschwerte Einbringlichkeit

**False Positives:**

- `Erschwerte Einbringlichkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_49`)


3. Die Gründe, die zum Zahlungsverzug geführt haben, sind grundsätzlich unbeachtlich.

**False Positives:**

- `Die Gründe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Herr_Person`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names following 'Herr' or 'Herrn'. Extracts only the name (group 1), excluding the title.

**Content:**
```
\b(?:Herr|Herrn)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
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

## `Frau_Person`

**F1:** 0.041 | **Precision:** 0.250 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names following 'Frau' to extract the name without the title. Refined to avoid matching 'Frau' as part of a title like 'Frau Rechtsanwältin'.

**Content:**
```
\bFrau\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Rechtsanw\u00e4ltin|Anwalt|Vertreter|Vertreterin|Schriftf\u00fchrer|Schriftf\u00fchrerin|Gesch\u00e4ftsf\u00fchrer|Gesch\u00e4ftsf\u00fchrerin|Vorsitzender|Vorsitzende|Richter|Richterin|Professor|Professoren|Dozent|Dozentin|Lehrer|Lehrerin|Arzt|\u00c4rztin|Ingenieur|Ingenieurin|Architekt|Architektin|Notar|Notarin|Steuerberater|Steuerberaterin|Wirtschaftspr\u00fcfer|Wirtschaftspr\u00fcferin|Banker|Bankerin|Manager|Managerin|Direktor|Direktorin|Pr\u00e4sident|Pr\u00e4sidentin|Sekret\u00e4r|Sekret\u00e4rin|Assistent|Assistentin|Mitarbeiter|Mitarbeiterin|Kollege|Kollegin|Freund|Freundin|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.022 | 0.041 | 8 | 2 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 6 | 81 |

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

## `Dr_in_Person`

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures 'Dr.in' followed by a name, including the title in the output. Fixed to handle 'Dr.in Mag.a' patterns and trim trailing spaces.

**Content:**
```
\bDr\.in\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.022 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 14 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

</details>

---

## `Von_Person`

**F1:** 0.022 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'von', strictly requiring a capitalized name to filter out common nouns. Excludes the trigger word 'von' and honorifics like 'Herrn', 'Frau'. Added 'Alternativen' to exclusion list.

**Content:**
```
\b(?:von|Von)\s+(?!Herrn|Frau|Herr|Dame|Fr\u00e4ulein|Alternativen|Investmentfonds|Verwaltung|Wirtschaft|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$)\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.022 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 44 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `Fuer_Person_Fixed`

**F1:** 0.022 | **Precision:** 0.333 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names after 'f\u00fcr', strictly requiring a capitalized name to filter out common nouns. Excludes the trigger word 'f\u00fcr'.

**Content:**
```
\b(?:fuer|f\u00fcr)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.011 | 0.022 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 80 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `Preposition_Person`

**F1:** 0.022 | **Precision:** 0.333 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following other prepositions like 'aus', 'mit', 'bei', 'nach', 'ohne', 'durch', 'gegenüber'. Excludes 'Herr', 'Herrn', 'Frau', 'Frauen' and legal entities.

**Content:**
```
\b(?:aus|mit|bei|nach|ohne|durch|gegenüber)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Steuerberatungsgesellschaft|Wirtschaftstreuhand|Grant\s+Thornton|Ernst\s+&\s+Young|Djuric\s+&\s+Oberger|Nowothnig|Depp|Wind|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))(?!\s*(?:Herr|Herrn|Frau|Frauen|Sohn|Tochter|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.011 | 0.022 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 63 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_37`)


Der Bf. ist mit Delia Moebes  verheiratet.

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Ihrer Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anwälte Mandl` — partial — pred is substring of gold: `Anwälte Mandl & Mitterbauer GmbH`

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

## `Title_Person_General_Fixed`

**F1:** 0.016 | **Precision:** 0.009 | **Recall:** 0.056  

**Format:** `regex`  
**Description:**
Captures names with academic/professional titles. Strictly excludes legal entities, document headers, and common false positives. Requires a title prefix.

**Content:**
```
\b(?:KommR\s+Ing\.|(?:Mag\.a\s+Dr\.in|Dr\.in\s+Dr\.in|Dr\.in|Dr\.|Prof\.|Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Bakk\.\s+iur\.|Dipl\.-Ing\.|\u00d6kR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+rer\.\s+nat\.\s+MBA|HR|VetR|Techn\s+R|Mag\.|Mag\.a|OStR\s+Ing\.|Ing\.|Hon\.-Prof\s+Univ\.-Prof\.|Univ\.-Prof\s+Hon\.-Prof\.|Hon\.-Prof\.in\s+Priv\.-Doz\.in|Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|Mag\.\s+Ing\.|Mag\.\s+Dipl\.|Ri|OSR|OMedR|DDr\.?|OStR|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|Hon\.-Prof\.\s+Hon\.-Prof\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Bundesfinanzgericht|Das|Die|Der|Die\s+Beschwerde|Die\s+Beschwerden|Der\s+Beschwerde|Die\s+Vorlageantrag|Die\s+Einkommensteuerbescheide|Das\s+Bundesfinanzgericht|Die\s+Beschwerdef\u00fchrerin|Sachverhalt|Im|In|Laut|Es|Nach|Mit|Durch|Gegen|Wegen|Zu|Von|Bei|F\u00fcr|Auf|Unter|Ober|In|An|Um|Ohne|Seit|Bis|Zwischen|W\u00e4hrend|Trotz|Wegen|Wider|Ohne|Neben|Gegen\u00fcber|Entlang|Au\u00dfer|Innerhalb|Au\u00dferhalb|W\u00e4hrend|Trotz|Wegen|Wider|Ohne|Neben|Gegen\u00fcber|Entlang|Au\u00dfer|Innerhalb|Au\u00dferhalb|Zum|Mit|Entscheidungsgr\u00fcnde|Die\s+BF|Die\s+BF\s+ist|Die\s+BF\s+ist|Die\s+BF\s+ist|Die\s+BF\s+ist|S\u00e4mtliche|Verfahrensgang|Die\s+Beschwerde|Der\s+Beschwerde|Die\s+Beschwerden|Der\s+Vorlageantrag|Die\s+Einkommensteuerbescheide|Alternativen|Investmentfonds|Verwaltung|Wirtschaft|Steuerberatungsgesellschaft|Wirtschaftstreuhand|Grant\s+Thornton|Ernst\s+&\s+Young|Djuric\s+&\s+Oberger|Nowothnig|Depp|Wind|Verband|Verein|Stiftung|Firma|Beh\u00f6rde|Amt|Bescheid|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Begr\u00fcndung|Mit\s+Beschluss|IM\s+NAMEN|REPUBLIC|REPUBLIK|BESCHLUSS|VERFAHREN|SACHE|ORDNUNGSBEGRIFF|NACHTRAG|ANMERKUNG|HINWEIS|ZUSATZ|ERL\u00c4UTERUNG|BEMERKUNG|FESTSTELLUNG|ENTSCHEIDUNG|URTEIL|RECHTSPRECHUNG|GESETZ|VERORDNUNG|RAT|KOMMISSION|PARLAMENT|MINISTERIUM|BEH\u00d6RDE|AMT|FINANZAMT|STEUERAMT|GERICHT|BUNDESFINANZGERICHT|LANDGERICHT|OBERSGERICHT|VERWALTUNGSGERICHT|VERWALTUNGSGERICHTSHOF|VERFAHRENSBEHANDLUNG|VERFAHRENSGANG|VERFAHRENSABLAUF|VERFAHRENSSTAND|VERFAHRENSSTATUS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|VERFAHRENSERLEDIGUNG|VERFAHRENSBEENDIGUNG|VERFAHRENSABSCHLUSS|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.009 | 0.056 | 0.016 | 552 | 5 | 547 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 547 | 85 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`
- `Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `Kind Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Die Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 4  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `In Beantwortung` — no gold match — likely missing annotation
- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_7`)


3. Mit Bescheid vom 12.11.2019 forderte das Finanzamt die für den Zeitraum von November  2017 bis Juni 2018 bezogenen Beträge an Familienbeihilfe und Kinderabsetzbeträgen iHv.

**False Positives:**

- `Mit Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Die Bescheidbegründung` — no gold match — likely missing annotation
- `Ihre Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Der Beschwerde` — no gold match — likely missing annotation
- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_16`)


Mit Ergänzungsersuchen vom 23.06.2020 wurde die BF aufgefordert die Unterschrift unter die  Beschwerde nachzuholen.

**False Positives:**

- `Mit Ergänzungsersuchen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `Mit Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

**False Positives:**

- `Mit Schriftsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Frau  Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Im Verlauf` — no gold match — likely missing annotation
- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Frau  Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Dem Vorlageantrag` — no gold match — likely missing annotation
- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`
- `Sachverhalt   Die` — no gold match — likely missing annotation
- `Zeitraum Familienbeihilfe` — no gold match — likely missing annotation
- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)
- `September 1998`(date)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_29`)


Die Tochter der BF absolvierte in der Zeit vom 01.10.2016 bis 04.10.2017 die Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith.

**False Positives:**

- `Die Tochter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_33`)


Beweiswürdigung  Der festgestellte Sachverhalt geht unstrittig aus den im Verfahrensgang genannten Unterlagen  hervor, die vom Finanzamt vorgelegt wurden.

**False Positives:**

- `Beweiswürdigung  Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Zu Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_43`)


Die Zeiten ab Beendigung der entsprechenden Tätigkeit können nicht  mehr als Zeiten einer Berufsausbildung angesehen werden.

**False Positives:**

- `Die Zeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_49`)


Diese Verpflichtung zur Rückerstattung ist von  subjektiven Momenten unabhängig.

**False Positives:**

- `Diese Verpflichtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_52`)


Die Rückforderung der bezogenen Beträge erfolgte daher zu Recht und die Beschwerde war  spruchgemäß abzuweisen.

**False Positives:**

- `Die Rückforderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Zu Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`
- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`
- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`
- `Die Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der beschwerdegegenständliche Abweisungsbescheid wurde erlassen wie folgt:  Ihr Antrag auf Familienbeihilfe vom 07.10.2020 wird abgewiesen für:  Name des Kindes – VNR/Geb.dat.

**False Positives:**

- `Verfahrensgang  Der` — no gold match — likely missing annotation
- `Ihr Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_4`)


– Zeitraum von – bis  (Nachname die Bf.) Maximiliane Sakschewsky, MA … 1201 ab Juli 2019  Begründung  Der Mittelpunkt der Lebensinteressen ihrer bereits volljährigen Tochter liegt nicht in  Österreich.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`
- `Begründung  Der Mittelpunkt` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Österreich`(country)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_7`)


Eine  Person hält sich ständig in Österreich auf und es bestehen auch die engeren persönlichen und  wirtschaftlichen Beziehungen zu Österreich.

**False Positives:**

- `Eine  Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Österreich`(country)
- `Österreich`(country)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_8`)


Eine Wohnsitzmeldung oder die österreichische  Staatsbürgerschaft alleine reichen nicht aus, um den Lebensmittelpunkt in Österreich  anzunehmen.

**False Positives:**

- `Eine Wohnsitzmeldung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_9`)


Die Beschwerde wurde mit folgender Begründung erhoben:  Klarstellung: Der Zeitraum der beantragten Familienbeihilfe ist von 01.06.2019 bis 30.09.2020  für meine Tochter Maximiliane Sakschewsky, MA (Nachname wie Bf.) (geboren am … .12.2001).

**False Positives:**

- `Die Beschwerde` — no gold match — likely missing annotation
- `Der Zeitraum` — no gold match — likely missing annotation
- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Bezirksgericht Purkersdorf` — type mismatch — same span as gold: `Bezirksgericht Purkersdorf`
- `Protokoll Ri` — no gold match — likely missing annotation
- `Vereinigtes Königreich` — type mismatch — same span as gold: `Vereinigtes Königreich`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_12`)


Dort besuchte Maximiliane Sakschewsky, MA  ab Herbst 2014 das King's School.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `King's School`(organisation)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_15`)


Unbeschadet dieses  Umstandes habe ich sämtliche Unterhaltskosten für meine Tochter Maximiliane Sakschewsky, MA, wie  bereits seit Ihren Aufenthaltswechsel im Jahr 2014 in das Vereinigte Königreich, im  Antragszeitraum noch EU-Mitgliedstaat, weiter getragen.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`
- `Ihren Aufenthaltswechsel` — no gold match — likely missing annotation
- `Vereinigte Königreich` — type mismatch — same span as gold: `Vereinigte Königreich`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Vereinigte Königreich`(country)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`
- `England Advanced Level` — partial — gold is substring of pred: `England`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_18`)


Im Falle einer Rückkehr nach  Österreich hätte Sie automatisch das letzte Schuljahr wiederholen müssen.

**False Positives:**

- `Im Falle` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Österreich`(country)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_20`)


Gemäß obigen Ausführungen ist meine Tochter Maximiliane Sakschewsky, MA  seit Sommer 2014,  ausgenommen ferienbedingte Abwesenheiten, in Vereinigten Königreich wohnhaft.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`
- `Vereinigten Königreich` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_21`)


Die  Abweisung meines Antrages stellt somit eine inhaltliche Rechtswidrigkeit dar.

**False Positives:**

- `Die  Abweisung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_22`)


Ich beantrage, meiner Beschwerde Folge zu geben.

**False Positives:**

- `Beschwerde Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_23`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:  Sachverhalt:  Der Bf stellte einen Antrag auf Gewährung der Familienbeihilfe für seine Tochter  Maximiliane Sakschewsky, MA  ab Juni 2019.

**False Positives:**

- `Die Beschwerdevorlage` — no gold match — likely missing annotation
- `Der Bf` — no gold match — likely missing annotation
- `Tochter  Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_26`)


Die Tochter studiert an der University of Bristol bis voraussichtlich Juli 2023.

**False Positives:**

- `Die Tochter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `University of Bristol`(organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_27`)


Laut Angaben im Antrag wohne die Tochter im streitgegenständlichen Zeitraum beim Bf und  dieser trage auch die überwiegenden Unterhaltskosten für seine Tochter.

**False Positives:**

- `Laut Angaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_32`)


Der Bf überwies ab Juni 2019 monatlich EUR 1.000,00 an die Kindesmutter.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_34`)


Siehe Inhaltsverzeichnis  Stellungnahme:  In seiner Beschwerde verzichtete der Bf ausdrücklich auf das Erlassen einer  Beschwerdevorentscheidung gem § 262 Abs 2 BAO und stellte zudem klar, dass er  Familienbeihilfe für den Zeitraum Juni 2019 – September 2020 beantragt.

**False Positives:**

- `Siehe Inhaltsverzeichnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_35`)


Der Besuch in den Sommerferien und zB auch über Weihnachten begründen keine  Haushaltszugehörigkeit, weswegen zu prüfen ist, ob der Bf die überwiegenden  Unterhaltskosten seiner Tochter trägt.

**False Positives:**

- `Der Besuch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_36`)


Der Bf überwies im beschwerdegegenständlichen Zeitraum monatlich EUR 1.000,- an die  Kindesmutter und brachte vor, dass dieses Geld für die Schulkosten verwendet würde.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Die Tragung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_38`)


Trotz Aufforderung einer Vorlage eines behördlichen Nachweises über den ausländischen  Bezug einer Familienleistung respektive die Nichtgewährung einer solchen, wurde so einer  nicht vorgelegt.

**False Positives:**

- `Trotz Aufforderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`
- `School Worcester` — similar text (different position): `The King´s School Worcester`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `The King´s School Worcester`(organisation)
- `Maximiliane Sakschewsky, MA`(person)
- `The King's  School Worcester`(organisation)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`
- `Ihrer Mutter` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_43`)


Im Mai 2019 wurde Maximiliane Sakschewsky, MA  nach einem Streit mit dem Ziehvater aus der  gemeinsamen Wohnung gewiesen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_56`)


In den Zeiträumen 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019  sowie 17. bis 19. Februar 2020 unternahm die Tochter des Bf. in Wien Fahrten gemäß § 19  Abs. 8 FSG (Fahrtenprotokoll).

**False Positives:**

- `Wien Fahrten` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`
- `Führerschein Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`
- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`
- `Maximiliane Sakschewsky` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `University of Bristol`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of Bristol`(organisation)

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Die Tochter` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_71`)


Diese Feststellung beruht auf folgenden Umständen:  Maximiliane Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der King's School Worcester,  Großbritannien.

**False Positives:**

- `Diese Feststellung` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`
- `School Worcester` — partial — pred is substring of gold: `King's School Worcester`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `King's School Worcester`(organisation)
- `Großbritannien`(country)

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of  Bristol`(organisation)

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

**False Positives:**

- `Diesen Lebensumständen` — no gold match — likely missing annotation
- `Nachweisliche Aufenthalte` — no gold match — likely missing annotation
- `Landespolizeidirektion Wien` — similar text (different position): `Wien`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Wien`(city)
- `Landespolizeidirektion Wien`(organisation)

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_77`)


2.  Eine überwiegende Unterhaltstragung betreffend Maximiliane Sakschewsky, MA  durch den Bf. kann nicht  erkannt werden.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_79`)


Der Bf. leistete im beschwerdegegenständlichen Zeitraum Unterhalt wie folgt:  - Für beide Töchter – Maximiliane Sakschewsky, MA  und E. – insgesamt monatlich € 1.000,00 (am 11. August  2020 überwies der Bf. für seine Tochter E. € 500,00, am 14. September 2020 € 140,00 und am  01. Oktober 2020 € 500,00).

**False Positives:**

- `Zeitraum Unterhalt` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Unter Bedachtnahme` — no gold match — likely missing annotation
- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `Zu Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Eine Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_85`)


Wie oben unter Punkt ausgeführt, erfüllt der Bf. die Voraussetzung, die Person zu sein, zu  deren Haushalt Maximiliane Sakschewsky, MA  gehört, nicht.

**False Positives:**

- `Haushalt Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_87`)


Bemerkt wird abschließend, dass vom Finanzamt darauf Folgendes hingewiesen wurde:  Trotz Aufforderung einer Vorlage eines behördlichen Nachweises über den ausländischen  Bezug einer Familienleistung respektive die Nichtgewährung einer solchen, wurde so einer  nicht vorgelegt.

**False Positives:**

- `Trotz Aufforderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

**False Positives:**

- `Zu Spruchpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_91`)


Diese Voraussetzungen sind im vorliegenden auf der Sachverhaltsebene zu lösenden Fall nicht  gegeben.

**False Positives:**

- `Diese Voraussetzungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`
- `Ashley Partenfelder` — partial — pred is substring of gold: `Mag. Ashley Partenfelder`
- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Der Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

**False Positives:**

- `Tochter  Viktoria Immohr` — partial — gold is substring of pred: `Viktoria Immohr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

**False Positives:**

- `Die  Auszahlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Bachelorstudium Wirtschaftswissenschaften` — no gold match — likely missing annotation
- `Johannes Kepler Universität` — partial — pred is substring of gold: `Johannes Kepler Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU Linz)`
- `Bachelorstudium Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

**False Positives:**

- `Bachelorstudium  Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_16`)


 Studienerfolgsnachweis der Hamburger Fern-Hochschule betreffend den Studiengang  Betriebswirtschaft für HAK-Absolventen betreffend im Jahr 2021 absolvierte Prüfungen  vom 02.08.2021  3.

**False Positives:**

- `Studiengang  Betriebswirtschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hamburger Fern-Hochschule`(organisation)

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_17`)


Mit Bescheid vom 17.09.2021 forderte die belangte Behörde von der Beschwerdeführerin (=  „Bf.“) zu Unrecht bezogener Beiträge an Familienbeihilfe und Kinderabsetzbetrag von  insgesamt EUR 4.163,20 für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die  Kinder mit der SVNr.

**False Positives:**

- `Mit Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_19`)


Zur Begründung wurde ausgeführt:  „Zu Viktoria Immohr:  Bei einem Studienwechsel nach dem 3. gemeldeten Semester steht Familienbeihilfe dann zu,  wenn die absolvierten Semester aus dem Vorstudium zur Gänze angerechnet wurden (§ 17  Studienförderungsgesetz 1992).

**False Positives:**

- `Zur Begründung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Kind Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Im Rückforderungsbetrag` — no gold match — likely missing annotation
- `Unrecht Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_24`)


Ein Vergleich der Studienrichtungen werde gerade von der  Wirtschaftsuniversität angefordert und nach Erhalt nachgereicht.

**False Positives:**

- `Ein Vergleich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Universität Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_30`)


7. Mit Beschwerdevorentscheidung vom 18.03.2022 wurde die Beschwerde als unbegründet  abgewiesen und dies wie folgt begründet:  „Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Mit Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

**False Positives:**

- `Studium Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU Wien`(organisation)
- `Linz`(city)

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_35`)


Die Beschwerde wird aus den oben angeführten Gründen abgewiesen.“

**False Positives:**

- `Die Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Zulassungsservices Lehr` — no gold match — likely missing annotation
- `Johannes Kepler Universität Linz` — type mismatch — same span as gold: `Johannes Kepler Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_39`)


Die Qualifikationsprofile der beiden Studien, was vor allem für weitere Unternehmen und  Arbeitgeber entscheidend sind, sind ident!

**False Positives:**

- `Die Qualifikationsprofile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)


Siehe Internetseite JKU und WU  Karriereaussichten!

**False Positives:**

- `Siehe Internetseite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU`(organisation)
- `WU`(organisation)

**Example 98** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Dem Vorlageantrag` — no gold match — likely missing annotation
- `Johannes Kepler  Universität Linz` — type mismatch — same span as gold: `Johannes Kepler  Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

</details>

---

## `HR_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'HR' (Hauptreferent) followed by a name, including titles like KzlR and multi-word names. Updated to handle 'Techn R' prefix.

**Content:**
```
\b(?:Techn\s+R\s+)?HR\s+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]*\.?\s+)*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*
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

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

</details>

---

## `RgR_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically captures 'RgR' (Regierungsrat) followed by a name, excluding cases where HR follows (handled by HR_Person).

**Content:**
```
\bRgR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?!\s+HR)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Herrn_Frau_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'Herrn' or 'Frau', allowing for optional titles including 'Techn R'.

**Content:**
```
\b(Herrn|Frau)\s+(?:OSR|OMedR|DDr\.?|OStR|Dr\.in|Dr\.|Mag\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|Bakk\. iur\.|Dipl\.-Ing\.|ÖkR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Univ\.-Prof\.in|Priv\.-Doz\.in|Hon\.-Prof\.in|Dr\. Dr\. Priv\.-Doz\.|Techn R)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nach_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'nach' (e.g., 'Verlassenschaft nach dem...'), indicating a deceased person or heir. Updated to handle 'des' and 'der'.

**Content:**
```
\b(?:nach|Nach)\s+(?:dem|der|den)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 40 | 0 | 40 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 40 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Rausschmiss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_44`)


Ein solches ist nach der Judikatur der Höchstgerichte zu  diesem Themenkreis jedoch nicht erforderlich.

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

**False Positives:**

- `Sommersemester` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_137`)


Vorausgeschickt sei, dass zwar einerseits nach dem Universitätsgesetz 2002 (UG) die  Universitäten autonom sind, jedoch zur besseren Vergleichbarkeit in Folge des Bologna- Prozesses Standards aufgestellt wurden, die in den Studienplänen abzubilden sind.

**False Positives:**

- `Universitätsgesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

**False Positives:**

- `Sommersemester` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes  Kepler Universität Linz`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_31`)


Die Gewährung von Zahlungserleichterungen für die Entrichtung von Geldstrafen und Kosten  nach dem Finanzstrafgesetz richtet sich damit nach § 212 BAO (vgl. VwGH 24.02.2011,  2010/16/0276, uHa Vorjudikatur).

**False Positives:**

- `Finanzstrafgesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_38`)


Die Unterstellung der Gewährung von Zahlungserleichterungen für die Entrichtung von  Geldstrafen nach dem Finanzstrafgesetz unter das Regelungsregime des § 212 BAO erfolgt  nach dem Wortlaut der Vorschrift des § 172 Abs. 1 FinStrG nur "sinngemäß".

**False Positives:**

- `Finanzstrafgesetz` — no gold match — likely missing annotation
- `Wortlaut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_34`)


Fahrlässig handle, wer die Sorgfalt außer Acht lasse, zu der er nach  den Umständen verpflichtet, nach seinen geistigen und körperlichen Verhältnissen befähigt  und ihm zuzumuten sei, und deshalb nicht erkenne, dass er einen Sachverhalt verwirklichen  könne, der einem gesetzlichen Tatbild entspreche.

**False Positives:**

- `Umständen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_53`)


Gemäß § 19 Abs. 2 VStG sind im ordentlichen Verfahren (§§ 40 bis 46) überdies die nach dem  Zweck der Strafdrohung in Betracht kommenden Erschwerungs- und Milderungsgründe, soweit  sie nicht schon die Strafdrohung bestimmen, gegeneinander abzuwägen.

**False Positives:**

- `Zweck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

**False Positives:**

- `Kriterien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_14`)


Die Betriebsprüfung gehe ab 2012 vom Vorliegen eines eigenständigen  Beobachtungszeitraumes aus, in dem ein Streben nach der Erzielung eines Gewinnes nicht  mehr erkennbar sei.

**False Positives:**

- `Erzielung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_100`)


1. aus der Bewirtschaftung von Wirtschaftsgütern, die sich nach der Verkehrsauffassung in  einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung eignen (zB  Wirtschaftsgüter, die der Sport- und Freizeitausübung dienen, Luxuswirtschaftsgüter) und  typischerweise einer besonderen in der Lebensführung begründeten Neigung entsprechen oder  2. aus Tätigkeiten, die typischerweise auf eine besondere in der Lebensführung begründete  Neigung zurückzuführen sind, oder  3. aus der Bewirtschaftung von Eigenheimen, Eigentumswohnungen und  Mietwohngrundstücken mit qualifizierten Nutzungsrechten.

**False Positives:**

- `Verkehrsauffassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_110`)


Ablauf dieses Zeitraumes ist unter Berücksichtigung der Verhältnisse auch innerhalb dieses  Zeitraumes nach dem Gesamtbild der Verhältnisse zu beurteilen, ob weiterhin vom Vorliegen  von Einkünften auszugehen ist.

**False Positives:**

- `Gesamtbild` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_111`)


Ein Anlaufzeitraum im Sinn des ersten Satzes darf nicht  angenommen werden, wenn nach den Umständen des Einzelfalls damit zu rechnen ist, daß die  Betätigung vor dem Erzielen eines Gesamtgewinnes (Gesamtüberschusses) beendet wird.

**False Positives:**

- `Umständen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_124`)


Die Frage der Liebhaberei ist nach der Liebhabereiverordnung (LVO, BGBl. 1993/33) zu  beurteilen.

**False Positives:**

- `Liebhabereiverordnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_129`)


Liebhaberei ist gemäß § 1 Abs. 2 Z 1 LVO hingegen bei einer Betätigung anzunehmen, wenn  Verluste aus der Bewirtschaftung von Wirtschaftsgütern entstehen, die sich nach der  Verkehrsauffassung in einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung  eignen (u.a. Luxuswirtschaftsgüter) und typischerweise einer besonderen in der Lebensführung  begründeten Neigung entsprechen.

**False Positives:**

- `Verkehrsauffassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_130`)


Steht bei einer Betätigung, die typischerweise auf eine besondere in der Lebensführung  begründete Neigung zurückzuführen ist, nicht die Bewirtschaftung eines Wirtschaftsgutes, das  sich nach der Verkehrsauffassung in einem besonderen Maß für eine Nutzung im Rahmen der  Lebensführung eignet, sondern eine bloße Tätigkeit im Vordergrund, so fällt diese unter § 1  Abs. 2 Z 2 LVO.

**False Positives:**

- `Verkehrsauffassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_151`)


Solcherart kann der Mittelpunkt der Tätigkeit einer Konzertpianistin nach der  Verkehrsauffassung an dem Ort angenommen werden, an dem sie die überwiegende Zeit an  ihrem Instrument verbringt, im Beschwerdefall in dem in Rede stehenden Arbeitszimmer  (VwGH vom 24. Juni 2004, 2001/15/0052).

**False Positives:**

- `Verkehrsauffassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_27`)


Im angeschlossenen Vorlagebericht vom selben Tag  führte die belangte Behörde ergänzend aus, dass das Kriterium der Zwangsläufigkeit, das stets  nach den Umständen des Einzelfalles zu prüfen sei, strittig sei.

**False Positives:**

- `Umständen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation
- `Umständen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `VwGH`(organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation
- `Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `VwGH`(organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_96`)


Ob dies der Fall ist, bestimmt  sich nach dem Urteil billig und gerecht denkender Menschen, in dem das Rechtsgefühl der  6 von 8 Seite 7 von 8

**False Positives:**

- `Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_100`)


Da davon auszugehen ist, dass nach dem Urteil billig und gerecht denkender Menschen den  Ehepartnern in einer aufrechten ehelichen Gemeinschaft das Wohlergehen des jeweils  anderen am Herzen liegt, bestand vor dem Hintergrund der Einkommenssituation der Ehefrau  des Bf. unstrittig eine sittliche Verpflichtung des Bf. zur Übernahme der Operationskosten (vgl.  Protokoll zur Verhandlung vom 1. Oktober 2025).

**False Positives:**

- `Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_101`)


Die Zwangsläufigkeit des Aufwands ist stets nach den Umständen des Einzelfalls zu prüfen.

**False Positives:**

- `Umständen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

**False Positives:**

- `Fälligkeitstag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_90`)


Der Bf. sei zur anteilsmäßigen Verteilung der liquiden Mittel nach dem  Gleichbehandlungsgrundsatz verpflichtet gewesen.

**False Positives:**

- `Gleichbehandlungsgrundsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_117`)


Aufgrund der Aktenlage müsse davon ausgegangen werden, dass zu den jeweiligen  Fälligkeitstagen bzw. ab dem ersten Fälligkeitstag liquide Mittel vorhanden gewesen seien,  diese jedoch nicht nach dem Gleichbehandlungsgrundsatz verteilt worden seien.

**False Positives:**

- `Gleichbehandlungsgrundsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_146`)


Selbst wenn auf Grund der derzeitigen wirtschaftlichen Situation des Beschwerdeführers die  Abgaben erschwert einbringlich seien, ließe sich daraus eine Unzumutbarkeit der  Haftungsinanspruchnahme nicht ableiten, weil es nach der Rechtsprechung nicht zutreffe, dass  die Haftung nur bis zur Höhe der aktuellen Einkünfte bzw. des aktuellen Vermögens geltend  gemacht werden dürfte (vgl. VwGH 29.

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_200`)


VwGH 24.1.2013, 2012/16/0100), womit dieser  klarstellte, dass eine Betrachtung der Gläubigergleichbehandlung zum jeweiligen  Fälligkeitszeitpunkt zu erfolgen hatte, wurde mit dem Erkenntnis vom 28.6.2022, Ra  2020/13/0067, aufgegeben:  "Dabei kommt es für den Nachweis der Gläubigergleichbehandlung nicht nur auf die  liquiden Mittel zum Fälligkeitstag an, die den an diesem einen Tag jeweilig fälligen  Verbindlichkeiten gegenüberzustellen sind, weil eine derartige Betrachtung für nur einen  einzigen Tag im Monat ohne Berücksichtigung der vorhandenen liquiden Mittel für die  Zeiträume nach der Fälligkeit der Abgaben keinen Nachweis über eine  Gläubigergleichbehandlung geben kann."

**False Positives:**

- `Fälligkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_39`)


Ein zweiter Säumniszuschlag ist für eine Abgabe zu entrichten, soweit sie nicht spätestens  drei Monate nach dem Eintritt ihrer Vollstreckbarkeit (§ 226) entrichtet ist.

**False Positives:**

- `Eintritt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_41`)


Säumniszuschlag ist für eine Abgabe zu entrichten, soweit sie nicht spätestens drei Monate  nach dem Eintritt der Verpflichtung zur Entrichtung des zweiten Säumniszuschlages entrichtet  ist.

**False Positives:**

- `Eintritt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_55`)


6. Nach der Rechtsprechung (zB VwGH 24.1.2018, Ra 2017/13/0023;

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_68`)


spätestens einen Monat nach dem Tag des Erwerbs des Kfz. am 13.4.2017, also am  13.5.2017, selbst zu berechnen und abzuführen gehabt.

**False Positives:**

- `Tag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Mandantin_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'Mandantin' or 'Mandant' (e.g., 'meiner Mandantin, Frau Livia Roux').

**Content:**
```
(?:Mandantin|Mandant)(?:,\s+)?(?:Frau|Herr)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Nachname_Wie_Bf_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after the specific legal marker '(Nachname wie Bf.)'.

**Content:**
```
\(Nachname wie Bf\.\)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sohn_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'Sohn' (son) in contexts like 'meinem Sohn', 'Ihr Sohn'.

**Content:**
```
(?:meinem|Ihr|sein|unser|deinem)\s+Sohn,?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gegen_Person_Fixed`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after 'gegen', strictly requiring a capitalized name and excluding common nouns like 'Firma' or 'Gesellschaft'.

**Content:**
```
\b(?:gegen|Gegen)\s+(?:die|der|den|dem|einer|einem|eine)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Party_Name_No_Title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'für' (for) or 'Kinder' (children) in family contexts, handling un-titled names.

**Content:**
```
(?:für\s+die\s+Kinder|Kinder\s+|für\s+Kinder)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `StR_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names with 'StR' (Strafrecht) title. Fixed to stop capturing addresses.

**Content:**
```
\bStR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Party_Person_CaseContext`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following case context words like 'Beschwerdesache'. Uses capture group to exclude the trigger word.

**Content:**
```
(?:Beschwerdesache|Rechtssache|Revisionssache|Verfahren|Sache|in\s+der|gegen)\s+(?:der\s+|des\s+|die\s+|den\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?=,|\s+\d+|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 16 | 0 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 16 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Lage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Fassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Beschwerdesache Mathilda Eckholdt` — partial — gold is substring of pred: `Mathilda Eckholdt`

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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_31`)


Es werde daher der Sachverhalt als erwiesen angenommen, wie er aus den schlüssigen und  widerspruchsfreien Angaben in der Organstrafverfügung, sowie aus der Tatumschreibung  dieses Straferkenntnisses ersichtlich sei.

**False Positives:**

- `Organstrafverfügung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Beschwerdesache Renate Brombusch` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_84`)


Festgehalten wird, dass die vom Vertreter des Bf. genannte Beschwerdevorentscheidung vom  11.3.2025 nicht die Einkommensteuer für das Jahr 2021, sondern die Einkommensteuer für das  Jahr 2020 betrifft (Die Beschwerde gegen den Einkommensteuerbescheid 2020 wurde dem  BFG zur Entscheidung vorgelegt, die noch unerledigt ist, RV/5100771/2025).

**False Positives:**

- `Einkommensteuerbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_85`)


Gegenständlich wurde mit Beschwerdevorentscheidung vom 12.03.2025 der Beschwerde  gegen den Einkommensteuerbescheid 2021 teilweise stattgegeben.

**False Positives:**

- `Einkommensteuerbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_89`)


(Hinweis: Es erging keine Vorlage der Beschwerde gegen  den Einkommensteuerbescheid 2021 an das Bundesfinanzgericht).

**False Positives:**

- `Einkommensteuerbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Beschwerdesache Alma Springel` — partial — gold is substring of pred: `Alma Springel`

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

- `Beschwerdesache  Oleg Dell` — partial — gold is substring of pred: `Oleg Dell`

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

- `Beschwerdesache Dieter Leufkes` — partial — gold is substring of pred: `Dieter Leufkes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Geschäftsführers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Beschwerdesache  Ludger Weynand` — partial — gold is substring of pred: `Ludger Weynand`

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

## `General_Person_Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following common legal verbs or prepositions that are not covered by specific title rules. Tightened to exclude non-persons.

**Content:**
```
\b(?:ist|habe|sei|war|wurde|hat|konnte|musste|wollte|sollte|konnte|dürfte|könnte|wird|werden|wurde|sind|seien|soll|sollen|haben|hatte|hatten|ist|ist|beschwerdeführende Partei)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Behörde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Geschäftsführer|Schriftführerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbehörden|Finanzstrafbehörde|Finanzstrafverfahren|Strafnummern|Verdachtes|Geschäftsführers|belangten Verbände|Beschuldigten|Amtsbeauftragten|Schriftführerin|Spruchsenates|Mödling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 82 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_43`)


Im Mai 2019 wurde Maximiliane Sakschewsky, MA  nach einem Streit mit dem Ziehvater aus der  gemeinsamen Wohnung gewiesen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_110`)


3. Rechtliche Beurteilung  3.1. Rechtslage  Gemäß § 2 Abs. 1 lit. b Familienlastenausgleichsgesetz 1967 idF. BGBl. I Nr. 24/2019 und Nr.  28/2020 haben Personen Anspruch auf Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `Personen Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

**False Positives:**

- `Herr  Dieter Leufkes` — partial — gold is substring of pred: `Dieter Leufkes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dieter Leufkes`(person)

</details>

---

## `Role_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following specific legal roles or abbreviations. Excludes 'Herr', 'Herrn', 'Frau', 'Frauen' and legal entities. Excludes cases where a title precedes the name.

**Content:**
```
\b(?:Gesch\u00e4ftsf\u00fchrerin|Gesch\u00e4ftsf\u00fchrer|Bf\.?|Kl\.?|Bekl\.?|Antragsteller|Antragstellerin|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Vertreter|Vertreterin|Ehegatte|Ehegatten|Ehepartner|Gattin|Kindesvater|Kindesmutterschaft|Mag\.|Dr\.|Prof\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:GmbH|AG|KG|mbH|UG|OHG|PartG|Steuerberatungsgesellschaft|Wirtschaftstreuhand|Grant\s+Thornton|Ernst\s+&\s+Young|Djuric\s+&\s+Oberger))(?!\s*(?:Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|OMedR|OSR|OStR|DDr\.|RgR|PhD|KzlR|StB|RA|MedR|StR|Bakk\.|Dipl\.-Ing\.|Ing\.|Techn R|Mag\.a|Mag\.|Dr\.in|Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|ÖkR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+iur\.|Dipl\.-Ing\.\s+)?\s+)
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

## `Name_With_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names with academic or professional suffixes like ', BA', ', Bakk. art.', ', MBA' that appear after a title or in case contexts. Includes title prefix if present.

**Content:**
```
\b(?!(?:Frau|Herr)\s)(?:([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s*,\s*)?(?:([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+))(?:\s*,\s*(?:BA|B\.A\.|B\.A\.\s+iur\.|Bakk\.\s+art\.|Bakk\.\s+rer\.\s+nat\.|MBA|LL\.M\.|LL\.B\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Date_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names immediately following a date pattern (e.g., '22.9.2016 Ida Vetterlin').

**Content:**
```
(?:^|\s)(\d{1,2}\.\d{1,2}\.\d{2,4})\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zu_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following the preposition 'zu' (to) in contexts like 'Zu Pascal Tiessen'.

**Content:**
```
\bzu\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 30 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Unrecht Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Herr_Abbrev_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following the abbreviation 'Hr.' (Herr).

**Content:**
```
\bHr\.\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Behörde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Geschäftsführer|Schriftführerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbehörden|Finanzstrafbehörde|Finanzstrafverfahren|Strafnummern|Verdachtes|Geschäftsführers|belangten Verbände|Beschuldigten|Amtsbeauftragten|Schriftführerin|Spruchsenates|Mödling|Stadt|Magistrat|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KzlR_Title_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically captures names with the 'KzlR' title, which is often associated with tax advisors or auditors.

**Content:**
```
\bKzlR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically captures 'Mag.' or 'Mag.a' titles followed by names to ensure they are not missed or partially matched.

**Content:**
```
\bMag\.(?:a)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 41 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Mag.Ashley Partenfelder` — positional overlap with gold: `Mag. Ashley Partenfelder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Mag.Gabriele Friedbacher` — positional overlap with gold: `Mag. Gabriele Friedbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Mag.Peter Bilger` — positional overlap with gold: `Mag. Peter Bilger`

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

</details>

---

