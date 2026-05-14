# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-14T03:39:08.657835

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
| Training documents | 2549 |
| Validation documents | 639 |
| Test documents | 1247 |
| Train sentences | 4268 |
| Validation sentences | 968 |
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

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | findok |
| Seed Rule Count | 27 |
| New Rules Added | 5 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 4080 |
| Phase1 Eval Sentences | 927 |
| Transfer Train Sentences | 188 |
| Transfer Eval Sentences | 41 |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 77.7% |
| True Positives | 19 |
| False Positives | 349 |
| False Negatives | 71 |
| Total Gold Entities | 90 |
| Micro Precision | 5.2% |
| Micro Recall | 21.1% |
| Micro F1 | 8.3% |
| Macro F1 | 8.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Dr_in_Person` | 2.2% | 100.0% | 1.1% | 1 | 1 | 0 |
| `Herr_Person` | 4.3% | 100.0% | 2.2% | 2 | 2 | 0 |
| `Mag_Person` | 6.4% | 75.0% | 3.3% | 4 | 3 | 1 |
| `Fuer_Person_Fixed` | 2.2% | 33.3% | 1.1% | 3 | 1 | 2 |
| `Title_Person_General_Fixed` | 4.2% | 33.3% | 2.2% | 6 | 2 | 4 |
| `Frau_Person` | 4.1% | 25.0% | 2.2% | 8 | 2 | 6 |
| `Pronoun_Person` | 7.0% | 16.7% | 4.4% | 24 | 4 | 20 |
| `Sentence_Start_Person` | 7.0% | 16.7% | 4.4% | 24 | 4 | 20 |
| `Von_Person` | 2.4% | 2.6% | 2.2% | 77 | 2 | 75 |
| `Genitive_Person` | 1.2% | 1.2% | 1.1% | 83 | 1 | 82 |
| `Preposition_Person` | 0.9% | 0.8% | 1.1% | 127 | 1 | 126 |
| `HR_Person` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `RgR_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Herrn_Frau_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nach_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mandantin_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Nachname_Wie_Bf_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sohn_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gegen_Person_Fixed` | 0.0% | 0.0% | 0.0% | 21 | 0 | 21 |
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
| `Prof_in_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Univ_Prof_Person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Von_Frau_Person` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Preposition_Person`

**F1:** 0.009 | **Precision:** 0.008 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following other prepositions. Updated to include suffixes and exclude legal entities and common nouns.

**Content:**
```
\b(?:aus|mit|bei|nach|ohne|durch|gegen\u00fcber)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Steuerberatungsgesellschaft|Wirtschaftstreuhand|Grant\s+Thornton|Ernst\s+&\s+Young|Djuric\s+&\s+Oberger|Nowothnig|Depp|Wind|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember))(?!\s*(?:Herr|Herrn|Frau|Frauen|Sohn|Tochter|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.008 | 0.011 | 0.009 | 127 | 1 | 126 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 126 | 84 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Schriftsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_24`)


Er ist österreichischer Staatsbürger mit Wohnsitz in Wien und geschieden;

**False Positives:**

- `Wohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Ihrer Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

</details>

---

## `Genitive_Person`

**F1:** 0.012 | **Precision:** 0.012 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following genitive articles 'der', 'des', 'die', 'den' (e.g., 'der Othmar Arvanitidis').

**Content:**
```
\b(?:der|des|die|den)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s|,|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.012 | 0.011 | 0.012 | 83 | 1 | 82 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 82 | 89 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `Zeitraum  November` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

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

- `Richter Dr` — positional overlap with gold: `Dr. Siegfried Fenz`
- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_34`)


Siehe Inhaltsverzeichnis  Stellungnahme:  In seiner Beschwerde verzichtete der Bf ausdrücklich auf das Erlassen einer  Beschwerdevorentscheidung gem § 262 Abs 2 BAO und stellte zudem klar, dass er  Familienbeihilfe für den Zeitraum Juni 2019 – September 2020 beantragt.

**False Positives:**

- `Zeitraum Juni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

</details>

---

## `Von_Person`

**F1:** 0.024 | **Precision:** 0.026 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures person names following 'von' (of/from) to handle cases like 'von Hademar Peschek'.

**Content:**
```
\b(?:von|Von)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=,|\s|$)(?!\\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\\u00e4ftsf\\u00fchrer|Schriftf\\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\\u00f6rden|Finanzstrafbeh\\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\\u00e4ftsf\\u00fchrers|belangten Verb\\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\\u00fchrerin|Spruchsenates|M\\u00f6dling|Stadt|Magistrat|\\d+|\\d{1,2}\\s*[a-zA-Z]{1,3}\\s*\\d{1,2}|\\d{1,2}\\s*[a-zA-Z]{1,3}\\s*\\d{1,2}\\s*,|\\d{1,2}\\s*[a-zA-Z]{1,3}\\s*\\d{1,2}\\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.026 | 0.022 | 0.024 | 77 | 2 | 75 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 75 | 85 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

| Predicted | Gold |
|---|---|
| `Maximiliane Sakschewsky, MA` | `Maximiliane Sakschewsky, MA` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


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

## `Gegen_Person_Fixed`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after 'gegen'. Updated to include suffixes like ', MA' and exclude legal entities and common nouns.

**Content:**
```
\b(?:gegen|Gegen)\s+(?:die|der|den|dem|einer|einem|eine)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `Strafverfügung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG,`(organisation)

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

## `Sentence_Start_Person`

**F1:** 0.070 | **Precision:** 0.167 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures person names at the start of a sentence or after specific punctuation if they are capitalized and followed by a period or comma.

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
Captures person names following case context words. Fixed to exclude the trigger word and capture only the name.

**Content:**
```
(?:Beschwerdesache|Rechtssache|Revisionssache|Verfahren|Sache|in\s+der|gegen)\s+(?:der\s+|des\s+|die\s+|den\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=,|\s+\d+|\s*$)
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

## `Title_Person_General_Fixed`

**F1:** 0.042 | **Precision:** 0.333 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names with academic/professional titles. Enhanced to handle complex title combinations and ensure full name capture.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Bakk\.\s+iur\.|Dipl\.-Ing\.|\u00d6kR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+rer\.\s+nat\.\s+MBA|HR|VetR|Techn\s+R|OStR\s+Ing\.|Ing\.|Hon\.-Prof\s+Univ\.-Prof\.|Univ\.-Prof\s+Hon\.-Prof\.|Hon\.-Prof\.in\s+Priv\.-Doz\.in|Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|Mag\.\s+Ing\.|Mag\.\s+Dipl\.|Ri|OSR|OMedR|DDr\.?|OStR|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|Hon\.-Prof\.\s+Hon\.-Prof\.)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Bakk\.\s+iur\.|Dipl\.-Ing\.|\u00d6kR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+rer\.\s+nat\.\s+MBA|HR|VetR|Techn\s+R|OStR\s+Ing\.|Ing\.|Hon\.-Prof\s+Univ\.-Prof\.|Univ\.-Prof\s+Hon\.-Prof\.|Hon\.-Prof\.in\s+Priv\.-Doz\.in|Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|Mag\.\s+Ing\.|Mag\.\s+Dipl\.|Ri|OSR|OMedR|DDr\.?|OStR|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|Hon\.-Prof\.\s+Hon\.-Prof\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.022 | 0.042 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 4 | 88 |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Ri  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

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

## `Nach_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'nach' (e.g., 'Verlassenschaft nach dem...'). Requires a second capitalized word to ensure it's a name, not a legal term.

**Content:**
```
\b(?:nach|Nach)\s+(?:dem|der|den)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)(?=[,\s]|$)
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

## `Sentence_Start_Person`

**F1:** 0.070 | **Precision:** 0.167 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures person names at the start of a sentence or after specific punctuation if they are capitalized and followed by a period or comma.

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

## `Mag_Person`

**F1:** 0.064 | **Precision:** 0.750 | **Recall:** 0.033  

**Format:** `regex`  
**Description:**
Captures 'Mag.' or 'Mag.a' titles followed by names, including suffixes like ', Bakk. rer. nat.'

**Content:**
```
\bMag\.(?:a)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.033 | 0.064 | 4 | 3 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 1 | 38 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

## `Title_Person_General_Fixed`

**F1:** 0.042 | **Precision:** 0.333 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names with academic/professional titles. Enhanced to handle complex title combinations and ensure full name capture.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Bakk\.\s+iur\.|Dipl\.-Ing\.|\u00d6kR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+rer\.\s+nat\.\s+MBA|HR|VetR|Techn\s+R|OStR\s+Ing\.|Ing\.|Hon\.-Prof\s+Univ\.-Prof\.|Univ\.-Prof\s+Hon\.-Prof\.|Hon\.-Prof\.in\s+Priv\.-Doz\.in|Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|Mag\.\s+Ing\.|Mag\.\s+Dipl\.|Ri|OSR|OMedR|DDr\.?|OStR|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|Hon\.-Prof\.\s+Hon\.-Prof\.)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Bakk\.\s+iur\.|Dipl\.-Ing\.|\u00d6kR|LL\.M\.|LL\.B\.|StB|RA|KommR|MedR|StR|Bakk\.\s+rer\.\s+nat\.\s+MBA|HR|VetR|Techn\s+R|OStR\s+Ing\.|Ing\.|Hon\.-Prof\s+Univ\.-Prof\.|Univ\.-Prof\s+Hon\.-Prof\.|Hon\.-Prof\.in\s+Priv\.-Doz\.in|Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in|Priv\.-Doz\.in|Univ\.-Prof\.in|DDr\.in|Mag\.\s+Ing\.|Mag\.\s+Dipl\.|Ri|OSR|OMedR|DDr\.?|OStR|OStR\.?|RgR|PhD\s+Ing\.|KzlR\s+DDr\.|OStR\s+Dipl\.|Hon\.-Prof\.\s+Hon\.-Prof\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.022 | 0.042 | 6 | 2 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 4 | 88 |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Ri  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

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

## `Von_Person`

**F1:** 0.024 | **Precision:** 0.026 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures person names following 'von' (of/from) to handle cases like 'von Hademar Peschek'.

**Content:**
```
\b(?:von|Von)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=,|\s|$)(?!\\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\\u00e4ftsf\\u00fchrer|Schriftf\\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\\u00f6rden|Finanzstrafbeh\\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\\u00e4ftsf\\u00fchrers|belangten Verb\\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\\u00fchrerin|Spruchsenates|M\\u00f6dling|Stadt|Magistrat|\\d+|\\d{1,2}\\s*[a-zA-Z]{1,3}\\s*\\d{1,2}|\\d{1,2}\\s*[a-zA-Z]{1,3}\\s*\\d{1,2}\\s*,|\\d{1,2}\\s*[a-zA-Z]{1,3}\\s*\\d{1,2}\\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.026 | 0.022 | 0.024 | 77 | 2 | 75 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 75 | 85 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

| Predicted | Gold |
|---|---|
| `Maximiliane Sakschewsky, MA` | `Maximiliane Sakschewsky, MA` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_101`)


Aus der nicht im gleichen Umfang erfolgten Anrechnung zum Zeitpunkt des  Studienwechsels kann daher noch kein automatischer Schluss betreffend die Vergleichbarkeit  von Studien gezogen werden.

**False Positives:**

- `Studien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `Studienortwechseln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `Vorteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_13`)


Als Begründung wurde dazu angegeben, während eines  Insolvenzverfahrens seien die Voraussetzungen für die Bewilligung von  Zahlungserleichterungen grundsätzlich nicht gegeben.

**False Positives:**

- `Zahlungserleichterungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_31`)


Die Gewährung von Zahlungserleichterungen für die Entrichtung von Geldstrafen und Kosten  nach dem Finanzstrafgesetz richtet sich damit nach § 212 BAO (vgl. VwGH 24.02.2011,  2010/16/0276, uHa Vorjudikatur).

**False Positives:**

- `Zahlungserleichterungen` — no gold match — likely missing annotation
- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_38`)


Die Unterstellung der Gewährung von Zahlungserleichterungen für die Entrichtung von  Geldstrafen nach dem Finanzstrafgesetz unter das Regelungsregime des § 212 BAO erfolgt  nach dem Wortlaut der Vorschrift des § 172 Abs. 1 FinStrG nur "sinngemäß".

**False Positives:**

- `Zahlungserleichterungen` — no gold match — likely missing annotation
- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_47`)


Für diesen Bereich galt eine ordnungsgemäß kundgemachte flächendeckende Kurzparkzone für  die Zeit von Montag bis Freitag (werktags) von 09:00 bis 22:00 Uhr.

**False Positives:**

- `Montag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_56`)


Die Einkommens- und Vermögensverhältnisse und allfällige Sorgepflichten des Beschuldigten  sind bei der Bemessung von Geldstrafen zu berücksichtigen.

**False Positives:**

- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_19`)


Die Art und  Weise der ausgeübten Tätigkeit sowie die Zusammensetzung von Einnahmen und Ausgaben  stellen neue Tatsachen gemäß § 303 Bundesabgabenordnung dar und diese konnten nur im  Wege einer Außenprüfung ermittelt werden.

**False Positives:**

- `Einnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_23`)


Unser Mandant ist hauptberuflich Musiker (Vibraphon, Schlagwerk), seine Tätigkeiten übt er  sowohl in Form von Dienstverhältnissen (z.B. Orchester) als auch als selbständiger Musiker  (Einzelunternehmer oder Gesellschafter diverser Musikensembles) aus.

**False Positives:**

- `Dienstverhältnissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_32`)


Er hat  diese Tätigkeit in gleicher Weise von Betriebseröffnung bis Betriebsaufgabe ausgeübt.

**False Positives:**

- `Betriebseröffnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_36`)


Nur, weil es insbesondere in den letzten Jahren der  selbständigen Tätigkeit unseres Mandanten zu dem einen oder anderen Verlustjahr gekommen  ist - dies auch bedingt durch die Tatsache, dass junge Konkurrenz nachwuchs und unser  Mandant dadurch nicht mehr so einfach an Aufträge kam, weiters die Gagenhöhe im Bereich  der Jazzmusik laufend gesunken ist und viele Veranstalter vermehrt auf modischere Diskjockeys  zurückgegriffen haben - kann nicht ohne weitere Prüfung des Gesamterfolges einer Tätigkeit  von Liebhaberei ausgegangen werden.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_41`)


Unser Mandant war über die Jahre stets bemüht, neue Aufträge zu erhalten, hat dann aber  2014 die Schließung seines Betriebes beim Finanzamt bekanntgegeben, da es für ihn aus  Altersgründen zu anstrengend wurde, neue Aufträge zu lukrieren und die Mühen von  Konzerttourneen auf sich zu nehmen.

**False Positives:**

- `Konzerttourneen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_44`)


Laut LRL Rz 22 ist der Gesamtgewinn das betriebliche Ergebnis von Begründung der Tätigkeit  durch den jeweiligen Steuerpflichtigen bis zu deren Beendigung durch denselben  Steuerpflichtigen (Veräußerung, Aufgabe oder Liquidation).

**False Positives:**

- `Begründung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_45`)


Aus diesem Grund wäre das  Finanzamt verpflichtet gewesen, aufgrund der Feststellung der Betriebsprüfung die Gewinne  der selbständigen Schaffensperiode unseres Mandanten von Beginn seiner Tätigkeit 1975 bis zu  deren Beendigung 2014 zu berücksichtigen.

**False Positives:**

- `Beginn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_51`)


In der Begründung ging das Finanzamt, wie im Bericht über den Abschluss der Außenprüfung  dargestellt, vom Vorliegen von Liebhaberei ab dem Jahr 2012 aus.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_55`)


Weiters wurde begründend ausgeführt:  „Das Vorliegen von Liebhaberei gemäß § 1 Abs. 2 Liebhabereiverordnung wurde festgestellt, da  zwar eine inhaltliche Kongruenz zwischen selbständiger und nichtselbständiger Tätigkeit  vorliegt, aber die Behörde aufgrund der umfangreichen Ausübung vom Vorliegen einer im  Privaten gelegenen Neigung ausgeht.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_72`)


Der Bf. habe seine hauptberufliche Tätigkeit als Musiker unverändert,  von Beginn an in der gleichen Art und Weise im Bereich Vibraphon/Schlagwerk ausgeübt.

**False Positives:**

- `Beginn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_77`)


Lediglich aufgrund eines bestimmten Verhältnisses von Einnahmen zu Ausgaben auf eine  Änderung der Bewirtschaftung zu schließen, sei unzureichend.

**False Positives:**

- `Einnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_100`)


1. aus der Bewirtschaftung von Wirtschaftsgütern, die sich nach der Verkehrsauffassung in  einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung eignen (zB  Wirtschaftsgüter, die der Sport- und Freizeitausübung dienen, Luxuswirtschaftsgüter) und  typischerweise einer besonderen in der Lebensführung begründeten Neigung entsprechen oder  2. aus Tätigkeiten, die typischerweise auf eine besondere in der Lebensführung begründete  Neigung zurückzuführen sind, oder  3. aus der Bewirtschaftung von Eigenheimen, Eigentumswohnungen und  Mietwohngrundstücken mit qualifizierten Nutzungsrechten.

**False Positives:**

- `Wirtschaftsgütern` — no gold match — likely missing annotation
- `Eigenheimen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_101`)


Die Annahme von Liebhaberei kann in diesen Fällen nach Maßgabe des § 2 Abs. 4  ausgeschlossen sein.

**False Positives:**

- `Liebhaberei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_107`)


(2) Innerhalb der ersten drei Kalenderjahre (Wirtschaftsjahre) ab Beginn einer Betätigung (zB  Eröffnung eines Betriebes) im Sinn des § 1 Abs. 1, längstens jedoch innerhalb der ersten fünf  Kalenderjahre (Wirtschaftsjahre) ab dem erstmaligen Anfallen von Aufwendungen (Ausgaben)  für diese Betätigung liegen jedenfalls Einkünfte vor (Anlaufzeitraum).

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_110`)


Ablauf dieses Zeitraumes ist unter Berücksichtigung der Verhältnisse auch innerhalb dieses  Zeitraumes nach dem Gesamtbild der Verhältnisse zu beurteilen, ob weiterhin vom Vorliegen  von Einkünften auszugehen ist.

**False Positives:**

- `Einkünften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_114`)


Steuerfreie Einnahmen sind  nur insoweit anzusetzen, als sie nicht zu einer Kürzung von Aufwendungen (Ausgaben) führen.

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_115`)


Wertänderungen von Grund und Boden, der zum Anlagevermögen gehört, sind nur bei der  Gewinnermittlung nach § 5 EStG 1988 anzusetzen.

**False Positives:**

- `Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_129`)


Liebhaberei ist gemäß § 1 Abs. 2 Z 1 LVO hingegen bei einer Betätigung anzunehmen, wenn  Verluste aus der Bewirtschaftung von Wirtschaftsgütern entstehen, die sich nach der  Verkehrsauffassung in einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung  eignen (u.a. Luxuswirtschaftsgüter) und typischerweise einer besonderen in der Lebensführung  begründeten Neigung entsprechen.

**False Positives:**

- `Wirtschaftsgütern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

**False Positives:**

- `Musikern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_8`)


Mit Bescheid über die Festsetzung von Anspruchszinsen 2021 vom 12.3.2025 ergibt die  Berechnung der Anspruchszinsen für das Jahr 2021 eine Gutschrift in Höhe von 7.963,60 €, da  1 von 7 Seite 2 von 7

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_17`)


Das Finanzamt erließ am 21.7.2025 eine abweisende Beschwerdevorentscheidung gegen den  Bescheid über die Festsetzung von Anspruchszinsen 2021 vom 12.03.2025 aufgrund der  Beschwerde vom 26.3.2025, da die Anspruchszinsenbescheide nach ständiger Rechtsprechung  an die Höhe der im Bescheidspruch des jeweiligen Einkommensteuerbescheides  ausgewiesenen Nachforderung gebunden seien.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_20`)


Mit Schreiben vom 23.7.2025 stellte die steuerliche Vertretung den Antrag auf Entscheidung  über die Beschwerde (Vorlageantrag) durch das Bundesfinanzgericht betreffend den Bescheid  über Festsetzung von Anspruchszinsen für das Jahr 2021 vom 12.3.2025.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_25`)


Ebenso erging am 22.05.2024 der (erste) Bescheid über die Festsetzung von Anspruchszinsen  2021.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_29`)


- die Beschwerde gegen den Bescheid über die Festsetzung von Anspruchszinsen 2021 (Anm:  vom 22.5.2024) wurde mit BVE vom 07.10.2025 abgewiesen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_30`)


Darüber hinaus erging am 12.03.2025 ein (neuer) Bescheid über die Festsetzung von  Anspruchszinsen für das Jahr 2021, in dem sich eine Gutschrift in der Höhe von Euro 7.963,60  ergab.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation
- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_45`)


Da der Erstbescheid des Bf zur Einkommensteuer 2021 eine Nachforderung von Euro  167.848,00 ergeben hat und dieser erst am 22.05.2024 ergangen ist (also somit nach dem  01.10.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_46`)


des dem Jahr des Entstehens des Abgabenanspruch folgenden Jahres) wurden mit  Bescheid vom 22.05.2024 Anspruchszinsen gem. § 205 BAO in der Höhe von Euro 13.809,18  festgesetzt.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_47`)


Da der Einkommensteuerbescheid aufgrund der Beschwerde des Bf mit  Beschwerdevorentscheidung vom 12.03.2025 abgeändert wurde (zugunsten des Bf) erging am  12.03.2025 der neue (bzw. weitere) Bescheid über die Festsetzung von Anspruchszinsen 2021, in  dem diesem Umstand Rechnung getragen wurde (Gutschrift Anspruchszinsen in der Höhe von  Euro 7.963,60).

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation
- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_50`)


Unter Verweis auf die bisherigen  Ausführungen, den Bescheid und die Beschwerdevorentscheidung wird von Seiten der  Abgabenbehörde die Abweisung der Beschwerde beantragt“.

**False Positives:**

- `Seiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Anzahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_90`)


Unabhängig vom Ausgang der eingebrachten Beschwerde gegen den  Einkommensteuerbescheid für das Jahr 2020 (und der Vorlage an das BFG) ist die Beschwerde  vom 25.3.2025 gegen den Bescheid vom 12.3.2025 betreffend Festsetzung von  Anspruchszinsen (§ 205 BAO) für das Jahr 2021 als unbegründet abzuweisen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_5`)


Am 31. Oktober 2023 erging ein Ergänzungsersuchen an den Bf. betreffend die geltend  gemachten Behandlungskosten in Höhe von Euro 10.299,13.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_43`)


Der Bf. machte in der Einkommensteuerveranlagung für das Jahr 2022 die Kosten für die  Operation in der Privatklinik in Höhe von Euro 10.299,13 als außergewöhnliche Belastung  geltend.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_44`)


Die Kosten setzen sich aus Spitalskosten in Höhe von Euro 10.340,97 abzüglich  Euro 41,84 Haushaltsersparnis für die Dauer des Spitalsaufenthalts von acht Tagen zusammen.

**False Positives:**

- `Euro` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_61`)


Triftige medizinische Gründe lassen auch höhere Aufwendungen des Steuerpflichtigen als die  von Sozialversicherungsträgern finanzierten zwangsläufig erscheinen.

**False Positives:**

- `Sozialversicherungsträgern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_70`)


In diesem Zusammenhang wird angemerkt,  dass auch in öffentlichen Krankenhäusern die Vergabe von Operationsterminen der  medizinischen Indikation und Dringlichkeit entsprechend erfolgt.

**False Positives:**

- `Operationsterminen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_108`)


Dabei ist zu beachten, dass triftige  medizinische Gründe auch höhere Aufwendungen als die von Sozialversicherungsträgern  finanzierten zwangsläufig erscheinen lassen (vgl. VwGH 11.2.2022, Ra 2020/13/0062).

**False Positives:**

- `Sozialversicherungsträgern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_56`)


Zu den abgabenrechtlichen Pflichten würden insbesondere gehören:  die Abgabenentrichtung aus den Mitteln, die der Vertreter verwalte,  die Führung gesetzlicher Aufzeichnungen (VwGH 30.5.1989, 89/14/0043),  die zeitgerechte Einreichung von Abgabenerklärungen (VwGH 29.5.2001, 2000/14/0006).

**False Positives:**

- `Abgabenerklärungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_166`)


Zu Spruchpunkt I. (Abweisung/Abänderung/Stattgabe)  Geltendmachung von Haftungen  10 von 15 Seite 11 von 15

**False Positives:**

- `Haftungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_171`)


Gemäß § 224 Abs. 1 BAO werden die in Abgabenvorschriften geregelten persönlichen  Haftungen durch Erlassung von Haftungsbescheiden geltend gemacht.

**False Positives:**

- `Haftungsbescheiden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_220`)


Vom Bf. wurden keine weiteren Gründe vorgebracht, die bei Abwägung von Zweckmäßigkeit  und Billigkeit eine andere Einschätzung bewirken hätten können.

**False Positives:**

- `Zweckmäßigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_7`)


2. Mit dem angefochtenen Bescheid über die Festsetzung von Säumniszuschlägen vom  9.1.2025 folgte eine Festsetzung von Säumniszuschlägen auf diese Abgaben gemäß § 217 Abs.  1 von 7 Seite 2 von 7

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation
- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_35`)


Die für die im Beschwerdefall für die Festsetzung von Säumniszuschlägen maßgeblichen  gesetzlichen Bestimmungen in der Bundesabgabenordnung BGBl. 1961/194 lauten:  § 217 BAO  (1) Wird eine Abgabe, ausgenommen Nebengebühren (§ 3 Abs. 2 lit. d), nicht spätestens am  Fälligkeitstag entrichtet, so sind nach Maßgabe der folgenden Bestimmungen  Säumniszuschläge zu entrichten.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_43`)


Die Dreimonatsfristen werden insoweit unterbrochen, als nach Abs. 4  Anbringen oder Amtshandlungen der Verpflichtung zur Entrichtung von Säumniszuschlägen  entgegenstehen.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_50`)


Die  Verwirkung von Säumniszuschlägen setzt kein Verschulden des Abgabepflichtigen voraus.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_70`)


Ob die Normverbrauchsabgabe- und Umsatzsteuerfestsetzungen zu Unrecht erfolgt  waren oder nicht, war für die Frage, ob das Finanzamt zur Festsetzung von Säumniszuschlägen  berechtigt war oder nicht, wie bereits weiter oben ausgeführt, nicht relevant.

**False Positives:**

- `Säumniszuschlägen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_78`)


Der Bf. hat gleichzeitig  mit den Beschwerden gegen die Bescheide über die Festsetzung von Normverbrauchsabgabe  und Umsatzsteuer (Fahrzeugeinzelbesteuerung) die Aussetzung dieser Abgaben beantragt.

**False Positives:**

- `Normverbrauchsabgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_80`)


Anlässlich der Erledigung der Beschwerden gegen die Festsetzung von  Umsatzsteuer für den Erwerb des Kfz.

**False Positives:**

- `Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_95`)


Die mit dem angefochtenen Bescheid verfügte Festsetzung von Säumniszinsen für die  Normverbrauchsabgabe in Höhe von 235,71 Euro ist daher zu Unrecht erfolgt.

**False Positives:**

- `Säumniszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_101`)


Fallen diese weg, steht einer neuerlichen Festsetzung  von Säumniszinsen, auf die ja bereits ein Anspruch entstanden ist, nichts im Weg.

**False Positives:**

- `Säumniszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Genitive_Person`

**F1:** 0.012 | **Precision:** 0.012 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following genitive articles 'der', 'des', 'die', 'den' (e.g., 'der Othmar Arvanitidis').

**Content:**
```
\b(?:der|des|die|den)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s|,|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.012 | 0.011 | 0.012 | 83 | 1 | 82 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 82 | 89 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `Zeitraum  November` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

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

- `Richter Dr` — positional overlap with gold: `Dr. Siegfried Fenz`
- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_34`)


Siehe Inhaltsverzeichnis  Stellungnahme:  In seiner Beschwerde verzichtete der Bf ausdrücklich auf das Erlassen einer  Beschwerdevorentscheidung gem § 262 Abs 2 BAO und stellte zudem klar, dass er  Familienbeihilfe für den Zeitraum Juni 2019 – September 2020 beantragt.

**False Positives:**

- `Zeitraum Juni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

**False Positives:**

- `Landespolizeidirektion Wien` — similar text (different position): `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)
- `Landespolizeidirektion Wien`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Richter Mag` — positional overlap with gold: `Mag. Ashley Partenfelder`
- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Johannes Kepler Universität` — partial — pred is substring of gold: `Johannes Kepler Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU Linz)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_16`)


 Studienerfolgsnachweis der Hamburger Fern-Hochschule betreffend den Studiengang  Betriebswirtschaft für HAK-Absolventen betreffend im Jahr 2021 absolvierte Prüfungen  vom 02.08.2021  3.

**False Positives:**

- `Studiengang  Betriebswirtschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hamburger Fern-Hochschule`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_26`)


6. Die Bf. antwortete mit einer am 13.12.2021 bei der belangten Behörde eingelangter Eingabe  und legte ein E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  3 von 16 Seite 4 von 16

**False Positives:**

- `Johannes Kepler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Zulassungsservices Lehr` — no gold match — likely missing annotation
- `Johannes Kepler Universität Linz` — type mismatch — same span as gold: `Johannes Kepler Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Johannes Kepler  Universität Linz` — type mismatch — same span as gold: `Johannes Kepler  Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_57`)


Da dies ein schädlicher Studienwechsel nach 4 Semestern ist, und eine Wartezeit von 3  Semester festgestellt wurde (aufgrund der Anrechnung Verkürzung um 1 Semester), wurde am  6 von 16 Seite 7 von 16

**False Positives:**

- `Anrechnung Verkürzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`
- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU)`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — type mismatch — same span as gold: `Johannes Kepler Universität Linz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes  Kepler Universität Linz` — type mismatch — same span as gold: `Johannes  Kepler Universität Linz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes  Kepler Universität Linz`(organisation)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Richterin Priv` — positional overlap with gold: `Priv.-Doz.in Farina Kohlstrunk`
- `Beschwerdesache Mathilda Eckholdt` — partial — gold is substring of pred: `Mathilda Eckholdt`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_5`)


§ 284 BAO lautet auszugsweise:  (1) Wegen Verletzung der Entscheidungspflicht kann die Partei Beschwerde  (Säumnisbeschwerde) beim Verwaltungsgericht erheben, wenn ihr Bescheide der  Abgabenbehörden nicht innerhalb von sechs Monaten nach Einlangen der Anbringen oder nach  1 von 3 Seite 2 von 3

**False Positives:**

- `Partei Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Quirin Januszis`
- `Jennifer Papenhagen` — partial — pred is substring of gold: `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_52`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

**False Positives:**

- `Revision  Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Richterin Mag` — positional overlap with gold: `Mag. Gabriele Friedbacher`
- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, MA 67`
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien, MA 67`

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_22`)


solches in einer Kurzparkzone abstellt, müsse gemäß § 5 Abs. 2 der Wiener  Parkometerabgabeverordnung bei Beginn des Abstellens die Parkometerabgabe entrichten.

**False Positives:**

- `Wiener  Parkometerabgabeverordnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_23`)


Die Abgabe sei mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

**False Positives:**

- `Stadt  Wien` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_24`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, hätten dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert sei  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien  Nr. 33/2008).

**False Positives:**

- `Stadt Wien  Nr` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_25`)


Zur ordnungsgemäßen Entrichtung der Abgabe und Vermeidung einer Abgabenverkürzung  bedürfe es gemäß den Bestimmungen der Wiener Kontrolleinrichtungenverordnung nicht nur  des richtigen und deutlichen Ausfüllens des Parkscheines, da dieser auch gut sichtbar hinter  der Windschutzscheibe anzubringen sei.

**False Positives:**

- `Wiener Kontrolleinrichtungenverordnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`
- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_83`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Revision  Eine Revision` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Richterin Priv` — positional overlap with gold: `Priv.-Doz.in Juliana Bartjen`
- `Beschwerdesache Renate Brombusch` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

**False Positives:**

- `Musikhochschule Wien` — type mismatch — same span as gold: `Musikhochschule Wien`
- `Stadt Wien` — partial — pred is substring of gold: `Konservatorium  der Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Musikhochschule Wien`(organisation)
- `Konservatorium  der Stadt Wien`(organisation)

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_7`)


Ein Jahr lang erhielt er in Ort, in den Vereinigten Staaten, eine Ausbildung in Marimba und  Percussion.

**False Positives:**

- `Vereinigten Staaten` — type mismatch — same span as gold: `Vereinigten Staaten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vereinigten Staaten`(country)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_18`)


Betreffend die Wiederaufnahme der Verfahren wurde im Betriebsprüfungsbericht ausgeführt,  dass für die Beurteilung einer Tätigkeit hinsichtlich der Liebhabereiverordnung Informationen  nötig seien, die über die bloßen Zahlen der Abgabenerklärungen hinausgehen.

**False Positives:**

- `Liebhabereiverordnung Informationen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_142`)


Das objektiv erkennbare Ertragsstreben muss darauf gerichtet  sein, im Laufe der Betätigung Gewinne in einer Höhe zu erwirtschaften, die nicht nur die  angefallenen Verluste ausgleichen, sondern darüber hinaus zu einem Gesamtgewinn führen.

**False Positives:**

- `Betätigung Gewinne` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_147`)


Nur in der Saldenliste für 2014 wurden die Aufwendungen für die Miete  Arbeitszimmer und die Energiekosten markiert und angemerkt „nicht Mittelpunkt der  Tätigkeit“.

**False Positives:**

- `Miete  Arbeitszimmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_153`)


An der in diesen beiden Erkenntnis zum Ausdruck gebrachten Rechtsansicht hat der  Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der Wiener  Philharmoniker betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241,  festgehalten und sie vertieft.

**False Positives:**

- `Wiener  Philharmoniker` — type mismatch — same span as gold: `Wiener  Philharmoniker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Wiener  Philharmoniker`(organisation)

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_163`)


Auch hat die Beurteilung der  gegenständlichen Rechtsfrage nur für den Einzelfall Bedeutung, weshalb die Revision nicht  zulässig ist.

**False Positives:**

- `Einzelfall Bedeutung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richterin Dr` — positional overlap with gold: `Dr.in Estelle Niederholz`
- `Beschwerdesache Hon` — positional overlap with gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_49`)


In diesem wurde darüber hinaus der Änderung der Einkommensteuer (Stammabgabe) in der  Beschwerdevorentscheidung Rechnung getragen.

**False Positives:**

- `Beschwerdevorentscheidung Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Richter Hon` — positional overlap with gold: `Hon.-Prof. Thassilo Averdiek`
- `Beschwerdesache Alma Springel` — partial — gold is substring of pred: `Alma Springel`
- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richterin Mag` — positional overlap with gold: `Mag.Dr. Katrin Allram`
- `Beschwerdesache  Oleg Dell` — partial — gold is substring of pred: `Oleg Dell`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr` — positional overlap with gold: `Dr. Dagobert Nordholt`
- `Beschwerdesache Dieter Leufkes` — partial — gold is substring of pred: `Dieter Leufkes`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `Finanzamt Kirchdorf Perg Steyr` — type mismatch — same span as gold: `Finanzamt Kirchdorf Perg Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_121`)


Bei schuldhafter  Pflichtverletzung dürfe die Abgabenbehörde mangels dagegensprechender Umstände  annehmen, dass die Pflichtverletzung Ursache der Uneinbringlichkeit sei (VwGH 16.12.1999,  97/15/0051;

**False Positives:**

- `Pflichtverletzung Ursache` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `Finanzamt Kirchdorf Perg Steyr` — type mismatch — same span as gold: `Finanzamt Kirchdorf Perg Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_174`)


Haftungsvoraussetzungen  - Abgabenforderungen gegen die vertretene Gesellschaft  - erschwerte Einbringlichkeit der Abgabenforderungen  - Stellung des Geschäftsführers als Vertreter  - abgabenrechtliche Pflichtverletzung des Vertreters  - dessen Verschulden an der Pflichtverletzung  - Ursächlichkeit der Pflichtverletzung für die erschwerte Einbringlichkeit der Abgaben  Abgabenforderungen

**False Positives:**

- `Abgaben  Abgabenforderungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_186`)


Insbesondere  ist im Rahmen dieser Verpflichtung für die rechtzeitige und vollständige Entrichtung der  Abgaben Sorge zu tragen.

**False Positives:**

- `Abgaben Sorge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

**False Positives:**

- `Pflichtverletzung Ursache` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Richter Mag` — positional overlap with gold: `Mag. Peter Bilger`
- `Beschwerdesache  Ludger Weynand` — partial — gold is substring of pred: `Ludger Weynand`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `Ludger Weynand`(person)
- `Plestätten 139Y, 4923 Reintal, Österreich`(address)
- `27-924/8149`(tax_number)
- `Finanzamtes Österreich`(organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_6`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt gegenüber dem Beschwerdeführer (Bf.)  Normverbrauchsabgabe (NoVA) in Höhe von 11.785,71 Euro und Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro für ein Kraftfahrzeug der Marke  Porsche Cayenne Diesel Platinum Edition (in der Folge: Kfz.) fest.

**False Positives:**

- `Marke  Porsche Cayenne Diesel Platinum Edition` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Preposition_Person`

**F1:** 0.009 | **Precision:** 0.008 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following other prepositions. Updated to include suffixes and exclude legal entities and common nouns.

**Content:**
```
\b(?:aus|mit|bei|nach|ohne|durch|gegen\u00fcber)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Steuerberatungsgesellschaft|Wirtschaftstreuhand|Grant\s+Thornton|Ernst\s+&\s+Young|Djuric\s+&\s+Oberger|Nowothnig|Depp|Wind|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember))(?!\s*(?:Herr|Herrn|Frau|Frauen|Sohn|Tochter|Vater|Mutter|Bruder|Schwester|Onkel|Tante|Neffe|Nichte|Enkel|Kind|Leute|Personen|Behauptung|Mitteilung|Antrag|Bescheid|Entscheidung|Verfahren|Gericht|Finanzamt|Amt|Beh\u00f6rde|Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|Stadt|Magistrat|Tod|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.008 | 0.011 | 0.009 | 127 | 1 | 126 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 126 | 84 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Schriftsatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_24`)


Er ist österreichischer Staatsbürger mit Wohnsitz in Wien und geschieden;

**False Positives:**

- `Wohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Ihrer Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_24`)


Ein Vergleich der Studienrichtungen werde gerade von der  Wirtschaftsuniversität angefordert und nach Erhalt nachgereicht.

**False Positives:**

- `Erhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU Wien`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_74`)


Weiters absolvierte die Tochter der Bf. an der JKU Linz Lehrveranstaltungen mit  31 ECTS-Punkten (ohne Berücksichtigung von Anrechnungen).

**False Positives:**

- `Berücksichtigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_94`)


In dieser Hinsicht kann ein Vergleich gezogen werden mit dem  bisherigen rechtswissenschaftlichen Diplomstudium, welches ebenfalls an mehreren  Universitätsstandorten in Österreich angeboten wurde bzw. wird (und nunmehr zusehends  durch einen Bologna-konformen Aufbau aus Bachelor und Master ersetzt wird), wobei sich  auch hier die konkreten Studienpläne bzw. –inhalte im Detail regelmäßig unterscheiden und  dennoch zum selben, als gleichartig anerkannten Ausbildungsergebnis führen sowie jeweils  Voraussetzung für die drei juristischen „Kernberufe“ Richter, Anwalt und Notar sind.

**False Positives:**

- `Bachelor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Österreich`(country)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_99`)


Dies muss jedoch nicht zwangsläufig an  unterschiedlichen Ausbildungsinhalten liegen, sondern kann auch unterschiedlichen  Kursteilnahme-Voraussetzungsketten und Detailunterschieden der Studienpläne liegen, die  manche Lehrveranstaltungen entweder erst später (nach Absolvierung anderer Kurse)  anrechenbar machen bzw. die aufgrund unterschiedlicher (ECTS-)

**False Positives:**

- `Absolvierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_102`)


Vielmehr kommt es auf die gewonnenen Ausbildungsinhalte mit  Abschluss des Studiums und die Qualifikationsprofile sowie Karriereaussichten der Absolventen  an.

**False Positives:**

- `Abschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_118`)


Nach § 17 Abs. 2 Z 1 StudFG gelten nicht als Studienwechsel im Sinne des Abs. 1 solche, bei  welchen die gesamten Vorstudienzeiten für die Anspruchsdauer des nunmehr betriebenen  Studiums berücksichtigt werden, weil sie dem nunmehr betriebenen Studium auf Grund der  besuchten Lehrveranstaltungen und absolvierten Prüfungen nach Inhalt und Umfang der  Anforderungen gleichwertig sind.

**False Positives:**

- `Inhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `Verweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `Einführung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_138`)


Ein bloßer  Studienortwechsel kann nicht erfordern, dass das andernorts aufgenommene Studium mit  dem vorherigen Studium gänzlich deckungsgleich sein muss, da es ansonsten in der Praxis  keinen einzigen (reinen) Studienortwechsel geben würde: Schließlich unterscheiden sich auch  inhaltsgleiche Studien schon jedenfalls aufgrund der Universitätsautonomie, welche sich je  nach Studienort jeweils in individuellen Studienplänen und nicht immer gleichartigen  Anrechenbarkeitskriterien ausdrückt.

**False Positives:**

- `Studienort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_166`)


maßgeblich sei vielmehr, ob die Studien gleichartig  bzw. gleichwertig sind (mit Hinweis auf Doralt, EStG4, § 34, Tz 76).

**False Positives:**

- `Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `Verweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_170`)


Der Beschwerde war daher durch Aufhebung des angefochtenen Rückforderungsbescheides  stattzugeben.

**False Positives:**

- `Aufhebung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_4`)


Dem Finanzamt wurde mit Beschluss vom 17. Oktober 2025 gemäß § 284 Abs. 2 BAO  aufgetragen, innerhalb von drei Monaten ab Einlangen der Beschwerde (somit bis längstens  10. Jänner 2026) den säumigen Bescheid zu erlassen und eine Abschrift der Entscheidung  vorzulegen oder anzugeben, warum eine Verletzung der Pflicht zur Erlassung des Bescheides  nicht oder nicht mehr vorliegt.

**False Positives:**

- `Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_5`)


§ 284 BAO lautet auszugsweise:  (1) Wegen Verletzung der Entscheidungspflicht kann die Partei Beschwerde  (Säumnisbeschwerde) beim Verwaltungsgericht erheben, wenn ihr Bescheide der  Abgabenbehörden nicht innerhalb von sechs Monaten nach Einlangen der Anbringen oder nach  1 von 3 Seite 2 von 3

**False Positives:**

- `Einlangen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_12`)


Diesen Antrag vom 25.11.2024 hat das Amt für Betrugsbekämpfung mit Bescheid vom 02.  Dezember 2024 abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_16`)


Gegen den abweisenden Bescheid vom 02. Dezember 2024 erhob der Bf. mit Schreiben vom  17.12.2024 Beschwerde und führte dazu begründend aus: „Gerade während eines laufenden  Insolvenzverfahrens kann ich als Schuldner nur über den unpfändbaren Bezugsanteil verfügen.

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_25`)


Gemäß § 172 FinStrG obliegt die Einhebung, Sicherung und Einbringung der Geldstrafen und  Wertersätze sowie der Zwangs- und Ordnungsstrafen und die Geltendmachung der Haftung  den Finanzstrafbehörden, die dazu auch Amtshilfe durch Abgabenbehörden in Anspruch  nehmen können.

**False Positives:**

- `Abgabenbehörden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_13`)


Am besagten Tag habe ich  bei Dienstantritt um 0600 Uhr, mein FzG mit dem beh. KZ.: 123, Marke, Farbe lackiert, am  Tatort abgestellt und die Gebühren welche der Parkometerabgabeverordnung entsprechen  mittels Kurzparkschein abgegolten.

**False Positives:**

- `Dienstantritt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

**False Positives:**

- `Straferkenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_21`)


Zur Begründung wurde im Straferkenntnis nach Wiedergabe des Verwaltungsgeschehens und  Einspruchsvorbringen festgestellt, jeder Lenker eines mehrspurigen Kraftfahrzeuges, der ein  2 von 7 Seite 3 von 7

**False Positives:**

- `Wiedergabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_22`)


solches in einer Kurzparkzone abstellt, müsse gemäß § 5 Abs. 2 der Wiener  Parkometerabgabeverordnung bei Beginn des Abstellens die Parkometerabgabe entrichten.

**False Positives:**

- `Beginn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_23`)


Die Abgabe sei mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

**False Positives:**

- `Verwendung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_27`)


Bemerkt werde, dass der Bf. sich nach Verlassen des Fahrzeuges davon überzeugen hätte  müssen, dass der Parknachweis gut sichtbar angebracht gewesen sei.

**False Positives:**

- `Verlassen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `Anbringen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG,`(organisation)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_51`)


Rechtsgrundlage und rechtliche Würdigung:    Gemäß § 4 Abs. 1 Wiener Parkometergesetz 2006 sind Handlungen und Unterlassungen, durch  die die Abgabe hinterzogen oder fahrlässig verkürzt wird, als Verwaltungsübertretungen mit  Geldstrafen bis zu 365 Euro zu bestrafen.

**False Positives:**

- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_58`)


Der Bf. hat das öffentliche Interesse an der Rationierung des in Wien vorhandenen Parkraums  dadurch geschädigt, dass er das Kraftfahrzeug ohne Parkschein in einer Kurzparkzone  abgestellt hat.

**False Positives:**

- `Parkschein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_62`)


Auch das Bundesfinanzgericht folgt dieser Vorgehensweise und gibt im gegebenen  Kontext jedoch auch zu bedenken, dass dadurch, dass weder der mit Organstrafverfügung  noch der mit Anonymverfügung verhängte Strafbetrag einbezahlt wurde, ein nicht  unerheblicher zusätzlicher Verwaltungsaufwand verursacht wurde.

**False Positives:**

- `Organstrafverfügung` — no gold match — likely missing annotation
- `Anonymverfügung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_64`)


Wie bereits ausgeführt, sind Verwaltungsübertretungen wie die vorliegende, nämlich die  fahrlässige Verkürzung der Parkometerabgabe gemäß § 4 Abs. 1 Wiener Parkometergesetz  2006, mit Geldstrafen bis zu 365,00 Euro zu bestrafen.

**False Positives:**

- `Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_76`)


Gemäß § 54b Abs. 1 VStG idF BGBl l 2013/33 sind rechtskräftig verhängte Geldstrafen oder  sonstige in Geld bemessene Unrechtsfolgen binnen zwei Wochen nach Eintritt der Rechtskraft  zu bezahlen.

**False Positives:**

- `Eintritt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_79`)


Ist mit Grund anzunehmen, dass der Bestrafte zur  Zahlung nicht bereit ist oder die Unrechtsfolge uneinbringlich ist, hat keine Mahnung zu  erfolgen und ist sofort zu vollstrecken oder nach Abs. 2 vorzugehen.

**False Positives:**

- `Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_83`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_12`)


Im Betriebsprüfungsbericht vom 15.9.2016 wurde unter „TZ 1 Liebhaberei“ ausgeführt, dass  gemäß Liebhabereiverordnung Liebhaberei bei Betätigungen anzunehmen sei, wenn Verluste  aus Tätigkeiten entstehen, die typischerweise auf eine besondere in der Lebensführung  begründete Neigung zurückzuführen sind.

**False Positives:**

- `Betätigungen` — no gold match — likely missing annotation
- `Tätigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_41`)


Unser Mandant war über die Jahre stets bemüht, neue Aufträge zu erhalten, hat dann aber  2014 die Schließung seines Betriebes beim Finanzamt bekanntgegeben, da es für ihn aus  Altersgründen zu anstrengend wurde, neue Aufträge zu lukrieren und die Mühen von  Konzerttourneen auf sich zu nehmen.

**False Positives:**

- `Altersgründen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

**False Positives:**

- `Dafürhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_100`)


1. aus der Bewirtschaftung von Wirtschaftsgütern, die sich nach der Verkehrsauffassung in  einem besonderen Maß für eine Nutzung im Rahmen der Lebensführung eignen (zB  Wirtschaftsgüter, die der Sport- und Freizeitausübung dienen, Luxuswirtschaftsgüter) und  typischerweise einer besonderen in der Lebensführung begründeten Neigung entsprechen oder  2. aus Tätigkeiten, die typischerweise auf eine besondere in der Lebensführung begründete  Neigung zurückzuführen sind, oder  3. aus der Bewirtschaftung von Eigenheimen, Eigentumswohnungen und  Mietwohngrundstücken mit qualifizierten Nutzungsrechten.

**False Positives:**

- `Tätigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_101`)


Die Annahme von Liebhaberei kann in diesen Fällen nach Maßgabe des § 2 Abs. 4  ausgeschlossen sein.

**False Positives:**

- `Maßgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_103`)


(3) Liebhaberei liegt nicht vor, wenn eine Betätigung bei einer einzelnen Einheit im Sinn des Abs.  1 vorletzter Satz, die im wirtschaftlichen Zusammenhang mit weiteren Einheiten steht, aus  Gründen der Gesamtrentabilität, der Marktpräsenz oder der wirtschaftlichen Verflechtung  aufrechterhalten wird.

**False Positives:**

- `Gründen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_104`)


§ 2. (1) Fallen bei Betätigungen im Sinn des § 1 Abs. 1 Verluste an, so ist das Vorliegen der  Absicht, einen Gesamtgewinn oder Gesamtüberschuß der Einnahmen über die Werbungskosten  (§ 3) zu erzielen, insbesondere anhand folgender Umstände zu beurteilen:  1. Ausmaß und Entwicklung der Verluste,  2.

**False Positives:**

- `Betätigungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_117`)


§ 6. Liebhaberei im umsatzsteuerlichen Sinn kann nur bei Betätigungen im Sinne des § 1 Abs. 2,  nicht hingegen bei anderen Betätigungen vorliegen.“

**False Positives:**

- `Betätigungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_136`)


Ausschlaggebend ist daher, ob die konkrete Tätigkeit bei Anlegen eines  abstrakten Maßstabes ("typischerweise") einen Zusammenhang mit einer in der  Lebensführung begründeten Neigung aufweist, wie dies etwa bei einer nebenberuflich  betriebenen schriftstellerischen Tätigkeit zur Herausgabe eines Sachbuches, die erst auf Grund  der hobbymäßigen Beschäftigung mit jener Materie, die im Sachbuch behandelt wird, zu  bejahen ist (VwGH vom 26.4.2000, 96/14/0095).

**False Positives:**

- `Anlegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_138`)


Für eine typische erwerbswirtschaftliche Betätigung spricht nach Ansicht des BFG die  hauptberufliche Ausübung der musikalischen Tätigkeit auf Grundlage der gehobenen  musikalischen Ausbildung des Bf.  11 von 14 Seite 12 von 14

**False Positives:**

- `Ansicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

**False Positives:**

- `Ansicht` — no gold match — likely missing annotation
- `Jazzgrößen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

**False Positives:**

- `Ansicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_157`)


Die betriebliche Veranlassung der restlichen geltend gemachten Aufwendungen ist aus Sicht  der Richterin glaubhaft.

**False Positives:**

- `Sicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_7`)


Aufgrund der Beschwerde vom 10.6.2024 wurde der Einkommensteuerbescheid 2021 vom  22.5.2024 mit Beschwerdevorentscheidung gem. § 262 BAO vom 12.3.2025 geändert und die  Einkommensteuer für das Jahr 2021 mit 71.052,00 € (anstatt wie bisher vorgeschrieben iHv  167.848,00 €) festgesetzt.

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_27`)


Darüber wurde folgendermaßen entschieden:   - die Beschwerde gegen den ESt-Bescheid 2020 wurde mit Beschwerdevorentscheidung (BVE)  vom 12.3.2025 (Anm. laut BFG richtig: 11.03.2025) abgewiesen.

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_31`)


Dagegen brachte die Vertreterin des Bf mit Schreiben vom 25.03.2025 Beschwerde ein.

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_34`)


Die Beschwerde wurde von der Abgabenbehörde mit Beschwerdevorentscheidung vom  21.07.2025 als unbegründet abgewiesen, da die Anspruchszinsenbescheide nach ständiger  Rechtsprechung an die Höhe, der im Bescheidspruch des jeweiligen  Einkommensteuerbescheides ausgewiesenen Nachforderung gebunden seien.

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_37`)


Dazu brachte die Vertreterin des Bf. mit Schreiben vom 23.07.2025 beiliegenden Vorlageantrag  ein.

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_39`)


„… Anspruchszinsen sind mit Abgabenbescheid festzusetzen.

**False Positives:**

- `Abgabenbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_42`)


Wegen dieser Bindung ist der Zinsenbescheid allerdings nicht (mit  Aussicht auf Erfolg) mit der Begründung anfechtbar, der maßgebende Einkommensteuer-  (Körperschaftsteuer-)bescheid sei inhaltlich rechtswidrig (Ritz/Koran, BAO, § 205, Rz 32, 33, 34).

**False Positives:**

- `Aussicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_46`)


des dem Jahr des Entstehens des Abgabenanspruch folgenden Jahres) wurden mit  Bescheid vom 22.05.2024 Anspruchszinsen gem. § 205 BAO in der Höhe von Euro 13.809,18  festgesetzt.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_47`)


Da der Einkommensteuerbescheid aufgrund der Beschwerde des Bf mit  Beschwerdevorentscheidung vom 12.03.2025 abgeändert wurde (zugunsten des Bf) erging am  12.03.2025 der neue (bzw. weitere) Bescheid über die Festsetzung von Anspruchszinsen 2021, in  dem diesem Umstand Rechnung getragen wurde (Gutschrift Anspruchszinsen in der Höhe von  Euro 7.963,60).

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Abgabenbescheiden` — no gold match — likely missing annotation
- `Gegenüberstellung` — no gold match — likely missing annotation
- `Vorauszahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_63`)


die Gutschrift wird mit Bekanntgabe des im Abs. 1 genannten Bescheides  wirksam.

**False Positives:**

- `Bekanntgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_68`)


Anspruchszinsen sind mit Abgabenbescheid (§ 198 BAO) festzusetzen.

**False Positives:**

- `Abgabenbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_71`)


Anspruchszinsenbescheide sind zwar mit Bescheidbeschwerde anfechtbar, etwa mit der  Begründung, der maßgebende Einkommensteuerbescheid sei nicht zugestellt worden oder der  im Zinsenbescheid angenommene Festsetzungszeitpunkt sei unzutreffend.

**False Positives:**

- `Bescheidbeschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_72`)


Der Zinsenbescheid ist an die im Spruch des zur Nachforderung oder Gutschrift führenden  Bescheides ausgewiesene Nachforderung bzw. Gutschrift gebunden (Ritz, BAO8, § 205 mit  Hinweis auf VwGH 27.2.2008, 2005/13/0039;

**False Positives:**

- `Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_75`)


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

**False Positives:**

- `Aussicht` — no gold match — likely missing annotation
- `Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_78`)


es erfolgt daher keine Abänderung des ursprünglichen  Zinsenbescheides (Ritz, BAO8, § 205 Tz 35 mit Hinweis auf VwGH 28.5.2009, 2006/15/0316,  VwGH 31.1.2019, Ro 2018/15/0005; sowie zahlreiche Erkenntnisse des BFG).

**False Positives:**

- `Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_85`)


Gegenständlich wurde mit Beschwerdevorentscheidung vom 12.03.2025 der Beschwerde  gegen den Einkommensteuerbescheid 2021 teilweise stattgegeben.

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_4`)


Begründung  1. Sachverhalt  Gegen die Einkommensteuerbescheide 2011, 2012, 2013 und 2015 sowie die  Umsatzsteuerbescheide 2011, 2012, 2013 und 2014 wurde fristgerecht mit Eingabe vom  19. April 2016 Beschwerde eingebracht.

**False Positives:**

- `Eingabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_6`)


Dagegen wurden mit Eingaben vom 24. Mai 2022 fristgerecht  Vorlageanträge eingebracht.

**False Positives:**

- `Eingaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_11`)


Rechtliche Beurteilung (Spruchpunkt I.)  Gemäß § 256 Abs 3 BAO ist eine Beschwerde mit Beschwerdevorentscheidung (§ 262) oder mit  Beschluss (§ 278) als gegenstandslos zu erklären, wenn sie zurückgenommen wird.

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation
- `Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_13`)


Da mit selbem Anbringen vom 12. November 2025 der Antrag auf mündliche Verhandlung und  auf Entscheidung durch den Senat zurückgezogen wurde, erfolgt die Entscheidung durch den  Einzelrichter ohne Durchführung einer mündlichen Verhandlung.

**False Positives:**

- `Durchführung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Durchführung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_13`)


Dagegen erhob der Bf. mit Eingabe vom 8. Februar 2024 Beschwerde und führte  zusammengefasst aus, dass es aufgrund der großen Schmerzen der Ehefrau des Bf. nicht  möglich gewesen sei, einige Monate zuzuwarten, bis ein Termin in der Kassenmedizin  verfügbar gewesen wäre.

**False Positives:**

- `Eingabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_16`)


Außerdem lebe der Bf.  abwechselnd an beiden Meldeadressen und werde auch von seiner Ehefrau nach Maßgabe  ihres Gesundheitszustandes begleitet.

**False Positives:**

- `Maßgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_44`)


Die Kosten setzen sich aus Spitalskosten in Höhe von Euro 10.340,97 abzüglich  Euro 41,84 Haushaltsersparnis für die Dauer des Spitalsaufenthalts von acht Tagen zusammen.

**False Positives:**

- `Spitalskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_73`)


Der  Befundbericht vom 6. Oktober 2025 beschreibt zunächst den Gesundheitszustand der Ehefrau  des Bf. vor der Operation und weist dabei insbesondere auf die bestehende  Schmerzsymptomatik und die Herausforderungen der Schmerztherapie bei Diabetikern hin.

**False Positives:**

- `Diabetikern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_78`)


Unabhängig davon, dass es aus menschlicher Sicht durchaus verständlich und nachvollziehbar  ist, dass die Ehefrau des Bf. so schnell wie möglich wieder schmerzfrei und voll mobil sein  wollte, liegen den obigen Ausführungen folgend nach Maßgabe der höchstgerichtlichen  Rechtsprechung keine triftigen medizinischen Gründe für die streitgegenständliche Operation  in der Privatklinik vor.

**False Positives:**

- `Maßgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_80`)


Zu Spruchpunkt I. (Abweisung)  § 34 Einkommensteuergesetz 1988 (EStG 1988), BGBl. Nr. 400/1988 idF BGBl. I Nr. 103/2019,  lautet auszugsweise wie folgt:  (1) Bei der Ermittlung des Einkommens (§ 2 Abs. 2) eines unbeschränkt Steuerpflichtigen sind  nach Abzug der Sonderausgaben (§ 18) außergewöhnliche Belastungen abzuziehen.

**False Positives:**

- `Abzug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_8`)


Der Bf. werde daher in seinem Interesse ersucht, die nachfolgenden Fragen sorgfältig und  vollständig zu beantworten und durch Vorlage geeigneter Unterlagen, die zu seiner Entlastung  dienen könnten, zu belegen.

**False Positives:**

- `Vorlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_30`)


Werde der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liege es im Ermessen des Finanzamtes, die Haftung für die genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

**False Positives:**

- `Benachteiligung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `Beachtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_81`)


Die im Rahmen des § 224 BAO zu treffende Ermessensentscheidung iSd § 20 BAO sei innerhalb  der vom Gesetzgeber gezogenen Grenze nach Billigkeit und Zweckmäßigkeit unter  Berücksichtigung aller in Betracht kommenden Umstände zu treffen.

**False Positives:**

- `Billigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

**False Positives:**

- `Heranziehung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Gleichbehandlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_126`)


Gem. § 20  BAO seien Ermessensentscheidungen nach Billigkeit und Zweckmäßigkeit unter  Berücksichtigung aller in Betracht kommenden Umstände zu treffen.

**False Positives:**

- `Billigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_130`)


Beantragt wurde den Haftungsbescheid  ersatzlos aufzuheben, da die belangte Behörde diesen Bescheid nach Würdigung der  Gesamtumstände nicht hätte erlassen dürfen.

**False Positives:**

- `Würdigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_141`)


Dazu führte das Finanzamt in der Begründung aus, dass die Geltendmachung einer Haftung in  das Ermessen der Abgabenbehörde gestellt sei (VwGH 23.1.1997, 95/15/0173), wobei die  Ermessensentscheidung im Sinne des § 20 BAO innerhalb der vom Gesetz gezogenen Grenzen  nach Billigkeit und Zweckmäßigkeit unter Berücksichtigung aller in Betracht kommenden  Umstände zu treffen sei.

**False Positives:**

- `Billigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_148`)


Wie bereits im Haftungsbescheid vom 11.01.2016 ausgeführt, obliege dem Vertreter der GmbH  der Nachweis, welcher Betrag bei Gleichbehandlung sämtlicher Gläubiger bezogen auf die  jeweiligen Fälligkeitszeitpunkte einerseits und das Vorhandensein liquider Mittel andererseits  an die Abgabenbehörde zu entrichten gewesen wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `Gleichbehandlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_156`)


Nach einer Vorsprache des  Bf. in der Abgabensicherung des Finanzamtes nahm der Bf. mit Eingabe vom 2.10.2025 sowohl  den Antrag auf eine mündliche Verhandlung als auch auf die Abhaltung einer Verhandlung vor  dem Senat zurück.

**False Positives:**

- `Eingabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_159`)


Ergänzend dazu wird durch das Verwaltungsgericht festgestellt, dass mit Beschluss vom  tt.5.2013 ein Sanierungsverfahren ohne Eigenverantwortung eröffnet und am tt.8.2013 der  Sanierungsplan bestätigt und das Sanierungsverfahren aufgehoben wurde.

**False Positives:**

- `Beschluss` — no gold match — likely missing annotation
- `Eigenverantwortung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_167`)


Die in den §§ 80 ff BAO bezeichneten Vertreter haften neben den durch sie vertretenen  Abgabepflichtigen insoweit, als diese Abgaben infolge schuldhafter Verletzung der ihnen  auferlegten abgabenrechtlichen oder sonstigen Pflichten nicht ohne Schwierigkeiten  eingebracht werden können, insbesondere im Fall der Eröffnung des Insolvenzverfahrens.

**False Positives:**

- `Schwierigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_171`)


Gemäß § 224 Abs. 1 BAO werden die in Abgabenvorschriften geregelten persönlichen  Haftungen durch Erlassung von Haftungsbescheiden geltend gemacht.

**False Positives:**

- `Erlassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_173`)


Gemäß § 224 Abs. 3 BAO ist die erstmalige Geltendmachung eines Abgabenanspruches  anlässlich der Erlassung eines Haftungsbescheides gemäß Abs. 1 nach Eintritt der Verjährung  des Rechtes zur Festsetzung der Abgabe nicht mehr zulässig.

**False Positives:**

- `Eintritt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_182`)


Im Beschwerdefall steht sogar die Uneinbringlichkeit der haftungsgegenständlichen Abgaben,  fest, da mit Beschluss des Landesgerichtes für Zivilrechtssachen vom 12.9.2023 die  Nichteröffnung eines Insolvenzverfahrens mangels kostendeckenden Vermögens festgestellt  wurde.

**False Positives:**

- `Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_200`)


VwGH 24.1.2013, 2012/16/0100), womit dieser  klarstellte, dass eine Betrachtung der Gläubigergleichbehandlung zum jeweiligen  Fälligkeitszeitpunkt zu erfolgen hatte, wurde mit dem Erkenntnis vom 28.6.2022, Ra  2020/13/0067, aufgegeben:  "Dabei kommt es für den Nachweis der Gläubigergleichbehandlung nicht nur auf die  liquiden Mittel zum Fälligkeitstag an, die den an diesem einen Tag jeweilig fälligen  Verbindlichkeiten gegenüberzustellen sind, weil eine derartige Betrachtung für nur einen  einzigen Tag im Monat ohne Berücksichtigung der vorhandenen liquiden Mittel für die  Zeiträume nach der Fälligkeit der Abgaben keinen Nachweis über eine  Gläubigergleichbehandlung geben kann."

**False Positives:**

- `Berücksichtigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
Captures person names appearing after 'nach' (e.g., 'Verlassenschaft nach dem...'). Requires a second capitalized word to ensure it's a name, not a legal term.

**Content:**
```
\b(?:nach|Nach)\s+(?:dem|der|den)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)(?=[,\s]|$)
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
Captures person names after 'gegen'. Updated to include suffixes like ', MA' and exclude legal entities and common nouns.

**Content:**
```
\b(?:gegen|Gegen)\s+(?:die|der|den|dem|einer|einem|eine)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=[,\s]|$)(?!\s*(?:Firma|Gesellschaft|AG|GmbH|KG|mbH|UG|OHG|PartG|Stiftung|Verein|Verband|Richter|Richterin|Bescheid|Finanzamt|Amt|Beh\u00f6rde|Verfahren|Antrag|Antragsteller|Bestraften|Beschuldigten|Gesch\u00e4ftsf\u00fchrer|Schriftf\u00fchrerin|Amtsbeauftragten|Spruchsenat|Finanzvergehen|Finanzstrafgesetz|Strafvollzugsgesetz|Widerruf|Strafaufschubes|Vollzuges|Vollzug|Bestrafte|Vereins|Neustart|Finanzstrafbeh\u00f6rden|Finanzstrafbeh\u00f6rde|Finanzstrafverfahren|Strafnummern|Verdachtes|Gesch\u00e4ftsf\u00fchrers|belangten Verb\u00e4nde|Beschuldigten|Amtsbeauftragten|Schriftf\u00fchrerin|Spruchsenates|M\u00f6dling|\d+|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*,|\d{1,2}\s*[a-zA-Z]{1,3}\s*\d{1,2}\s*$|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `Strafverfügung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG,`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_61`)


Die belangte Behörde hat die vom Bf. in seinem Einspruch gegen die Strafverfügung  vorgebrachten Umstände (samt seiner Sorgepflichten für ein Kind) gewürdigt, als sie die in der  Strafverfügung festgesetzte Strafhöhe von 75,00 Euro, auf die im nunmehr angefochtenen  Straferkenntnis festgesetzten 55,00 Euro herabsetzte (Ersatzfreiheitsstrafe von 17 auf 13  Stunden).

**False Positives:**

- `Strafverfügung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_21`)


Gegen diese Einkommensteuerbescheide vom 19.10.2016 brachte der steuerliche Vertreter  am 14.11.2016 eine Beschwerde ein und führte aus, dass sich die Beschwerde gegen die  Feststellungen der abgabenbehördlichen Prüfung richte, welche die ausgeübte selbständige  Tätigkeit des Mandanten als Musiker ab dem Jahr 2012 als Liebhaberei gemäß § 1 Abs. 2 LVO  einstufe.

**False Positives:**

- `Feststellungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_17`)


Das Finanzamt erließ am 21.7.2025 eine abweisende Beschwerdevorentscheidung gegen den  Bescheid über die Festsetzung von Anspruchszinsen 2021 vom 12.03.2025 aufgrund der  Beschwerde vom 26.3.2025, da die Anspruchszinsenbescheide nach ständiger Rechtsprechung  an die Höhe der im Bescheidspruch des jeweiligen Einkommensteuerbescheides  ausgewiesenen Nachforderung gebunden seien.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_29`)


- die Beschwerde gegen den Bescheid über die Festsetzung von Anspruchszinsen 2021 (Anm:  vom 22.5.2024) wurde mit BVE vom 07.10.2025 abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_90`)


Unabhängig vom Ausgang der eingebrachten Beschwerde gegen den  Einkommensteuerbescheid für das Jahr 2020 (und der Vorlage an das BFG) ist die Beschwerde  vom 25.3.2025 gegen den Bescheid vom 12.3.2025 betreffend Festsetzung von  Anspruchszinsen (§ 205 BAO) für das Jahr 2021 als unbegründet abzuweisen.

**False Positives:**

- `Einkommensteuerbescheid` — no gold match — likely missing annotation
- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Bescheide` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_44`)


Hinsichtlich des Bestehens einer Abgabenforderung gegen den Vertretenen wurde dargelegt,  dass die Umsatzsteuer 10/2011 bis 12/2011, 02/2012 bis 12/2012 sowie 01/2013 bis 02/2013  jeweils mittels Umsatzsteuervoranmeldung gemeldet worden sei.

**False Positives:**

- `Vertretenen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Bescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `Ludger Weynand`(person)
- `Plestätten 139Y, 4923 Reintal, Österreich`(address)
- `27-924/8149`(tax_number)
- `Finanzamtes Österreich`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_57`)


22.2.2024, RV/7100415/2023) bestehen keine Bedenken, wenn über  Beschwerden gegen Säumniszuschläge entschieden wird, obwohl über die gegen die  Stammabgabenbescheide gerichteten Beschwerden noch nicht abgesprochen wurde.

**False Positives:**

- `Stammabgabenbescheide` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_78`)


Der Bf. hat gleichzeitig  mit den Beschwerden gegen die Bescheide über die Festsetzung von Normverbrauchsabgabe  und Umsatzsteuer (Fahrzeugeinzelbesteuerung) die Aussetzung dieser Abgaben beantragt.

**False Positives:**

- `Bescheide` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_80`)


Anlässlich der Erledigung der Beschwerden gegen die Festsetzung von  Umsatzsteuer für den Erwerb des Kfz.

**False Positives:**

- `Festsetzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
Captures person names following case context words. Fixed to exclude the trigger word and capture only the name.

**Content:**
```
(?:Beschwerdesache|Rechtssache|Revisionssache|Verfahren|Sache|in\s+der|gegen)\s+(?:der\s+|des\s+|die\s+|den\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][A-Z]+)?)\s*(?=,|\s+\d+|\s*$)
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

## `Prof_in_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically captures 'Prof.in' titles followed by names to ensure the full title is included in the output.

**Content:**
```
\bProf\.in\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Univ_Prof_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically captures 'Univ.-Prof.' and complex academic titles followed by names.

**Content:**
```
\b(?:Univ\.-Prof\.(?:\s+Dr\.(?:\s+Priv\.-Doz\.)?)?|Dr\.(?:\s+Priv\.-Doz\.)?\s+Univ\.-Prof\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Von_Frau_Person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'von Frau' to handle cases like 'von Frau Mag. Janosch Moehrle, Bakk. rer. nat.'

**Content:**
```
\b(?:von|Von)\s+Frau\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `von Frau Stella Marschalk, Bakk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

</details>

---

