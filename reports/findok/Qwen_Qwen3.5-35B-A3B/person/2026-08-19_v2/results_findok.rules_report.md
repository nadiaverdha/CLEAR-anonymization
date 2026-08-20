# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-19T23:06:43.132211

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-19_v2/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 0 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 1525 |
| Validation documents | 382 |
| Test documents | 792 |
| Train sentences | 2914 |
| Validation sentences | 776 |
| Test sentences | 88613 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 100 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | True |
| Critic Interval | 20 |
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
| Accuracy (exact match) | 95.4% |
| True Positives | 717 |
| False Positives | 3688 |
| False Negatives | 1674 |
| Total Gold Entities | 2391 |
| Micro Precision | 16.3% |
| Micro Recall | 30.0% |
| Micro F1 | 21.1% |
| Macro F1 | 21.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `title_based_person` | 39.4% | 82.0% | 25.9% | 755 | 619 | 136 |
| `party_context_name` | 2.3% | 36.8% | 1.2% | 76 | 28 | 48 |
| `verb_context_name` | 0.5% | 13.6% | 0.3% | 44 | 6 | 38 |
| `title_first_name_only` | 0.7% | 11.9% | 0.3% | 67 | 8 | 59 |
| `first_name_only_no_title` | 2.8% | 4.3% | 2.0% | 1139 | 49 | 1090 |
| `role_followed_name` | 0.2% | 1.7% | 0.1% | 176 | 3 | 173 |
| `no_title_conjunction` | 0.2% | 1.6% | 0.1% | 188 | 3 | 185 |
| `von_name` | 0.0% | 0.1% | 0.0% | 1898 | 1 | 1897 |
| `academic_suffix_name` | 0.0% | 0.0% | 0.0% | 16 | 0 | 16 |
| `preposition_name` | 0.0% | 0.0% | 0.0% | 19 | 0 | 19 |
| `born_context_name` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `accused_context_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `senatspraesident_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `family_relation_name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `witness_context_name` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `first_name_only_title` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |
| `accusative_genitive_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `mj_minor_name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `title_based_person` 🏆

**F1:** 0.394 | **Precision:** 0.820 | **Recall:** 0.259  

**Format:** `regex`  
**Rule ID:** `e11bde94`  
**Description:**
Matches person names preceded by German legal/academic titles. Fixed to handle 'Dr.in', 'Prof. Dr.', and 'Univ.-Prof.' combinations.

**Content:**
```
(?<![A-Za-z])(?:Hon\.-?Prof\.|Univ\.-?Prof\.|Prof\.|Dr\.|Mag\.|MMag\.|DI\.|Ing\.|Bakk\.\s+iur\.|PhD\.|HR\s+Ing\.|Techn\s+|Dipl\.-?HTL\-?Ing\.|PD\s+Dr\.|Priv\.-?Doz\.|DDr\.|KommR\s+|ÖkR\s+|RgR\s+|StR\s+|MedR\s+|HR\s+|KzlR\s+|OMedR\s+|VetR\s+|AR\s+|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+|Dr\.in)(?:\s+Dr\.)?\s+[A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+(?:[A-Z]\.|\s+[A-Z][a-zäöüßéèêëïîôùûü]+|-?[A-Z][a-zäöüßéèêëïîôùûü]+)*)\b(?![a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.820 | 0.259 | 0.394 | 755 | 619 | 136 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 619 | 136 | 1772 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hemma Bährs` | `Dr.in Hemma Bährs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Rachel Darnieder` (person)
- `Finanzamtes Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MMag. Gerald Erwin Ehgartner` | `MMag. Gerald Erwin Ehgartner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zeno Matyssek` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)
- `Finanzamt für Gebühren` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Raphael Williamson, BEd, Züggen 8, 8042 Graz, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raphael Williamson, BEd` (person)
- `Züggen 8, 8042 Graz, Österreich` (address)
- `Monika Pfundner-Lenz` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

| Predicted | Gold |
|---|---|
| `Mag. Susanne Feichtenschlager` | `Mag. Susanne Feichtenschlager` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daisy Wegelein` (person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `61-004/6209` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Dr. Gerlinde  Rieser` | `Dr. Gerlinde  Rieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Matthäus Domrös` (person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nadja Rossetto` (person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `Imre & Schaffer Rechtsanwälte OG` (organisation)
- `Finanzamtes` (organisation)
- `85-716/2059` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |
| `Mag. Achmed Ghazal Aswad` | `Mag. Achmed Ghazal Aswad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donald Paulovits` (person)
- `Tröbach 41, 9130 Leibsdorf, Österreich` (address)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `95-720/4312` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximilian Joobs` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oleg Kreissl` (person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Niels Aleksejew` | `Univ.-Prof. Niels Aleksejew` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Kuzu` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Schlohsmacher` (person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich` (address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Adalbert Bürks` (person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

| Predicted | Gold |
|---|---|
| `Dr.in Fabienne Siewek` | `Dr.in Fabienne Siewek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vincent und Zielinska Solar GmbH` (organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Univ.-Prof. Janis Abelen,  Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Janis Abelen` | `Univ.-Prof. Janis Abelen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Mag.a Reneé Kobayashi, Weinbaugebiet Losling 9, 4880 Aich, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Elisabeth Traxler` | `Mag. Elisabeth Traxler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Reneé Kobayashi` (person)
- `Weinbaugebiet Losling 9, 4880 Aich, Österreich` (address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |
| `Dr.  Karl Penninger` | `Dr.  Karl Penninger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold Pichlbauer` (person)
- `Ing. Dipl.-Ing. Brunhild Fleischfresser` (person)
- `Margaretengürtel 23, 4092 Pyrawang, Österreich` (address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH` (organisation)
- `Finanzamtes` (organisation)
- `Tanja Grottenthaler` (person)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. ÖkR Horst Stevens` (person)
- `Glinzen 13, 4661 Kirnbach, Österreich` (address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH` (organisation)
- `Finanzamtes Linz` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Mehmet Faidt, Flitsch 4, 4822 Kogl, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |
| `Mag. Wolfgang Freudelsperger` | `Mag. Wolfgang Freudelsperger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mehmet Faidt` (person)
- `Flitsch 4, 4822 Kogl, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hon.-Prof. Gerhard Hübinger, Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich, St.Nr. xxxxxxxxxxxx, über die Beschwerden vom 2. April 2013 gegen den  Aufhebungsbescheid gemäß § 299 BAO vom 4. März 2013 und den Zurückweisungsbescheid  vom 4. März 2013 (betreffend Antrag auf Bescheidaufhebung gemäß § 295 Abs. 4 BAO, in  eventu Antrag auf Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 lit. b BAO) des  Finanzamtes Wien 9/18/19 Klosterneuburg, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Gerhard Hübinger` | `Hon.-Prof. Gerhard Hübinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr.in Astrid Rüstmann` | `Dr.in Astrid Rüstmann` |
| `Mag. Hermann Rupert Zittmayr` | `Mag. Hermann Rupert Zittmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandro Flunger` (person)
- `Rohrer Straße 29, 3231 Kainratsdorf, Österreich` (address)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Florentin Blissenbach, Gotschmanninstraße 11, 9170 Seidolach, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  03-281/0693  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Blissenbach` (person)
- `Gotschmanninstraße 11, 9170 Seidolach, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `03-281/0693` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR Hedwig Barkholt` (person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich` (address)
- `ICON Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der BergLuftfahrt, KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BergLuftfahrt` (organisation)
- `KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich` (address)
- `Westra  GmbH Steuerberatungsgesellschaft` (organisation)
- `BMF` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Huberta Nothofer` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florenzia Rutt` (person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich` (address)
- `Zollamtes Feldkirch Wolfurt` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vivian Malek` (person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich` (address)
- `Mag. Walter Dienstl & Partner  KG` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Tanja Wescher, Margaretenplatz 55, 3170 Gerstbach, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 07-638/8400  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tanja Wescher` (person)
- `Margaretenplatz 55, 3170 Gerstbach, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `07-638/8400` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

| Predicted | Gold |
|---|---|
| `Dr.in Monika Wörther-Madl` | `Dr.in Monika Wörther-Madl` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

| Predicted | Gold |
|---|---|
| `Dr.in Monika Wörther-Madl` | `Dr.in Monika Wörther-Madl` |

**Missed by this rule (FN):**

- `Kuranstalt Vigaun GmbH & Co. KG` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Dr.in Klara Willumelies` | `Dr.in Klara Willumelies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dorfcongart-Event` (organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Sellnow` | `Priv.-Doz. Eckard Sellnow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Rösl` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über den Antrag der  Valentin Heinicke, Hofstätt 196, 3970 Sulz, Österreich, vertreten durch BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, QBC 4 – Am Belvedere 4, 1100 Wien, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer  für das Jahr 2014 erhobenen ordentlichen Revision vom 24. Juni 2020 die aufschiebende  Wirkung zuzuerkennen, beschlossen:  Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentin Heinicke` (person)
- `Hofstätt 196, 3970 Sulz, Österreich` (address)
- `BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. August Eichelsbacher  in der Beschwerdesache VetR Diethard Oldenbüttel,  Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich, vertreten durch BOD Steuerberatungs-GmbH, Europastraße 5, 6322  Kirchbichl,, über die Beschwerde vom 16. Dezember 2016 gegen den Bescheid des FA Landeck Reutte  vom 21. November 2016 betreffendBerichtigung des Einkommensteuerbescheides 2010 vom  29. November 2011 gem. § 293b BAO erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. August Eichelsbacher` | `Hon.-Prof. August Eichelsbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Diethard Oldenbüttel` (person)
- `Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich` (address)
- `BOD Steuerberatungs-GmbH` (organisation)
- `FA Landeck Reutte` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Antonewitz` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr.in Ljiljana Kos` | `Dr.in Ljiljana Kos` |
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Ljiljana Kos` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Ljiljana Kos` (person)
- `Dr. Schmid` (person)
- `Klinik Favoriten` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Sahin, Fischmarkt 627, 4153 Vorderschiffl, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimitri Sahin` (person)
- `Fischmarkt 627, 4153 Vorderschiffl, Österreich` (address)
- `LMG  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Philippov` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Dr.in Lydia Vogtleitner` (person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Thomas Hofer-Zeni` | `Dr. Thomas Hofer-Zeni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerald Hellbing` (person)
- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Neiser` | `Dr. Stephan Neiser` |
| `Mag. Esra Rohleder` | `Mag. Esra Rohleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Hademar Berking, Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hademar Berking` (person)
- `Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Missed by this rule (FN):**

- `Dr. Padesse` (person)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Björn Hüpscher` | `Dr. Björn Hüpscher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Igor Strunz` (person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich` (address)
- `Vedat Gökdemir` (person)
- `Finanzamtes` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R HR Martina Pisterer` (person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130620.1_1`)


BESCHLUSS   Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über den  Vorlageantrag vom 19. Dezember 2018 des Beschwerdeführers Diethard Uphof, Unterrotte 8, 3061 Unterwolfsbach, Österreich,  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten, 3100 St. Pölten, Daniel Gran-Straße 8,  vom 4. Mai 2018 betreffend Umsatzsteuer 2016:    I)

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diethard Uphof` (person)
- `Unterrotte 8, 3061 Unterwolfsbach, Österreich` (address)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lubomir Gruebert` | `Priv.-Doz. Lubomir Gruebert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexander Powell` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Calvin Gorol` (person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich` (address)
- `Helmut Binder` (person)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Klarissa Aßmus, Strombad Rustenweg 4, 3452 Trasdorf, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 52-573/0809  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klarissa Aßmus` (person)
- `Strombad Rustenweg 4, 3452 Trasdorf, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `52-573/0809` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Lex` (person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Irene Kohler` | `Mag. Irene Kohler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Erwin Göktan` (person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ronald Töws` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Rupert Karl` | `Mag. Rupert Karl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gudrun Sochurek` (person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Valentina Heumeyer  in der Beschwerdesache Emanuela Schöchl,  J. Schemmerl-Gasse 7, 4906 Felling, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Dr.in Valentina Heumeyer` | `Dr.in Valentina Heumeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emanuela Schöchl` (person)
- `J. Schemmerl-Gasse 7, 4906 Felling, Österreich` (address)
- `Anton Hörmann` (person)
- `Finanzamtes` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Alessia Olschofski` | `Dr.in Alessia Olschofski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Gosebrink, Bakk. phil.` (person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `50-818/5472` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR Frederik Kleinmichel, MA` (person)
- `Haniflgasse 12, 4725 Stadl, Österreich` (address)
- `Astoria Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Cäcilia Wlcek` (person)
- `Rambergweg 3, 4950 Weidenthal, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valerie Süssmeier` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jeffrey Wengschick` | `Dr. Jeffrey Wengschick` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donald Hayder, MA` (person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Valentin Kreuthmayr  in der Beschwerdesache Naomi Ruddis, LLB,  Schuselkagasse 21, 9570 Alt-Ossiach, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 10. März 2020 betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für sich selbst ab Jänner 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Valentin Kreuthmayr` | `Mag. Valentin Kreuthmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Naomi Ruddis, LLB` (person)
- `Schuselkagasse 21, 9570 Alt-Ossiach, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holger Weiskittel` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Theophil Schachenmeier, Gsteinert 21, 4115 Steining, Österreich, betreffend die Beschwerde vom 03.04.2020 gegen den Bescheid  des Finanzamtes Freistadt Rohrbach Urfahr vom 26.03.2020 über die Einstellung der  Vollstreckung zu Steuernummer 63-906/4998  beschlossen:   Die Beschwerde wird gem. § 260 Abs. 1 lit. a) BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Norbert Zöls` | `Dr. Norbert Zöls` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theophil Schachenmeier` (person)
- `Gsteinert 21, 4115 Steining, Österreich` (address)
- `Finanzamtes` (organisation)
- `63-906/4998` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Proidl über die Beschwerde der  Istvan  Sicking, Fanny Elßler-Gasse 30, 9375 Zosen, Österreich, vom 09. Oktober 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 28. September 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der Fassung LGBl. für Wien Nr. 24/2012, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als der  Spruch des bekämpften Straferkenntnisses insoweit abgeändert wird, als die Geldstrafe von  Euro 60,00 auf Euro 36,00 und die Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden  herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Proidl` | `Mag. Andrea Proidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Istvan  Sicking` (person)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt  Wien` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Zwilling` | `Mag. Josef Zwilling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tiffany Kleiß` (person)
- `Endergasse 74, 5411 Vorderwiestal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `79-412/0834` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Hegenbart` (person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

| Predicted | Gold |
|---|---|
| `Dr. Norbert Zöls` | `Dr. Norbert Zöls` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendy Schärff` (person)
- `Krainberg 12, 4633 Weilbach, Österreich` (address)
- `LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Linz` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Waldemar Zumloh` (person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `09-591/1655` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Ruprecht Kalmes, Freistabl 34, 9400 Gries, Österreich, über die Beschwerde vom 5. Februar 2020 gegen die  Bescheide des Finanzamtes Lilienfeld St. Pölten vom 4. November 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, Steuernummer  03-702/3005, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Ruprecht Kalmes` (person)
- `Freistabl 34, 9400 Gries, Österreich` (address)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `03-702/3005` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/131567.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Valerius Wilbert  in der Finanzstrafsache gegen die  Beschuldigte Chen Kürkcü, An der Museumsbahn 11, 3122 Bichl, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Valerius Wilbert` | `Hon.-Prof. Valerius Wilbert` |
| `Mag. Heinz Wolfbauer` | `Mag. Heinz Wolfbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chen Kürkcü` (person)
- `An der Museumsbahn 11, 3122 Bichl, Österreich` (address)
- `Finanzamtes  Wien 9/18/19 Klosterneuburg` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Fridolin Härlin  in der Beschwerdesache Alva Czymzik,  Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Fridolin Härlin` | `Priv.-Doz. Fridolin Härlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alva Czymzik` (person)
- `Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck in der Beschwerdesache  Thobias Dommert, Hainfelder Straße 56, 4846 Gewerbepark West, Österreich, vertreten durch LBG Niederösterreich Steuerberatung GmbH, Wie- ner Straße 2, 2640 Gloggnitz, über die Beschwerden vom 29. Dezember 2017 und 31. Jänner  2018 gegen die Bescheide des Finanzamtes Neunkirchen Wiener Neustadt vom 6. Dezember  2017 und 10. Jänner 2018 betreffend Einkommensteuer 2007 bis 2011, St.Nr. 33- 66-847/2354, zu Recht erkannt:    Der Beschwerde gegen den Einkommensteuerbescheid 2007 wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Johannes Böck` | `Mag. Johannes Böck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thobias Dommert` (person)
- `Hainfelder Straße 56, 4846 Gewerbepark West, Österreich` (address)
- `LBG Niederösterreich Steuerberatung GmbH` (organisation)
- `Finanzamtes Neunkirchen Wiener Neustadt` (organisation)
- `66-847/2354` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thomas Drieschner  in der Beschwerdesache Gebhard Determann,  Mooseggweg 49, 9624 Fritzendorf, Österreich, Deutschland, vertreten durch die Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H. über die Beschwerden gegen die Bescheide des  Finanzamtes Kufstein Schwaz betreffend Einkommensteuer 2017 und Umsatzsteuer 2017  jeweils vom 10. Jänner 2019 zu Recht erkannt:   I. Der Beschwerde gegen den Umsatzsteuerbescheid 2017 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Thomas Drieschner` | `Univ.-Prof. Thomas Drieschner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Determann` (person)
- `Mooseggweg 49, 9624 Fritzendorf, Österreich` (address)
- `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Marion Weißhar, Magnusplatz 23, 9555 Glantscha, Österreich, vom 20. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis mit der Maßgabe bestätigt, dass der Kostenbeitrag für das  behördliche Strafverfahren gemäß § 64 Abs. 2 VStG nicht 10,00 €, sondern 14,00 € beträgt.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marion Weißhar` (person)
- `Magnusplatz 23, 9555 Glantscha, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Gudrun Breunlein, Am Rintl 6, 5324 Faistenau, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 75-682/2104  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gudrun Breunlein` (person)
- `Am Rintl 6, 5324 Faistenau, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `75-682/2104` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RgR OMedR Miklos Pellegrin, Ostendeweg 9, 9981 Glor-Berg, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 73-541/6746, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR OMedR Miklos Pellegrin` (person)
- `Ostendeweg 9, 9981 Glor-Berg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `73-541/6746` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Veit Vissers, Wander Bertoni-Straße 166, 5223 Fludau, Österreich, über die Beschwerde vom 10. September 2019 gegen den  Bescheid des Finanzamtes Österreich vom 13. August 2019 betreffend Abweisung eines  Antrages auf Wiederaufnahme § 303 BAO /  ESt 2017 Steuernummer 94-198/2586  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Veit Vissers` (person)
- `Wander Bertoni-Straße 166, 5223 Fludau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `94-198/2586` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Prof. Helmut Fürnkäß` | `Prof. Helmut Fürnkäß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman` (person)
- `Dr Christian Leskoschek` (person)
- `Finanzamtes Österreich` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der  Verwaltungsstrafsache gegen Lieselotte Rübenkönig, Bakk. rer. nat., Strohweg 140g, 8593 Salla, Österreich, über die Beschwerde des  Beschuldigten vom 9.11.2020 gegen die Vollstreckungsverfügungen des Magistrates der Stadt  Wien, Magistratsabteilung 6, vom 11. Jänner 2020, 1) MA67/196700867324/2019 und 2)  MA67/196700891928/2019 vom 14.1.2020, MA67/196700890302/2019 und vom 25.1.2020,   MA67/196700930712/2019, alle in Zusammenhang mit einer Verwaltungsübertretung gemäß  § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, i.d.g.F., in  Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, i.d.g.F. zu Recht  erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und werden die angefochtenen  Vollstreckungsverfügungen ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lieselotte Rübenkönig, Bakk. rer. nat.` (person)
- `Strohweg 140g, 8593 Salla, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 6` (organisation)
- `Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache QZKX Beratung, Lambacher Straße 9, 3123 Mittermerking, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 45-817/1493  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Dieter Walla` — partial — pred is substring of gold: `Mag. Dieter Walla & Partner Steuerberater OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `QZKX Beratung`(organisation)
- `Lambacher Straße 9, 3123 Mittermerking, Österreich`(address)
- `Mag. Dieter Walla & Partner Steuerberater OG`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `45-817/1493`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Wendy Scherl`(person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `53-864/4798`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Ing. Brunhild Fleischfresser` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Mag. Susanne Haim`(person)
- `Leopold Pichlbauer`(person)
- `Dr.  Karl Penninger`(person)
- `Ing. Dipl.-Ing. Brunhild Fleischfresser`(person)
- `Margaretengürtel 23, 4092 Pyrawang, Österreich`(address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH`(organisation)
- `Finanzamtes`(organisation)
- `Tanja Grottenthaler`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `Mag. Manfred Frühwirth` — partial — pred is substring of gold: `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Miroslav Treischl`(person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich`(address)
- `Grant Thornton Austria GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Irvin Kurrek  in der Beschwerdesache Alexandra Kesler,  Illyrerweg 5, 4073 Edramsberg, Österreich, (nunmehr Valsyn-Maschinenbau GmbH als Rechtsnachfolgerin der Schameitat Sanitär GmbH, vertreten durch StB,  über die Berufung (nunmehr Beschwerde) vom 21. August 2013 gegen die Bescheide des FA  vom 9. Juli 2013 betreffend Wiederaufnahme der Verfahren hinsichtlich der  Körperschaftsteuer für die Jahre 2009 und 2010 sowie die Körperschaftsteuer für die Jahre  2009 bis 2011 beschlossen:    I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) als nicht  zulässig zurückgewiesen.

**False Positives:**

- `Priv.-Doz. Irvin Kurrek` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Irvin Kurrek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Priv.-Doz. Irvin Kurrek`(person)
- `Alexandra Kesler`(person)
- `Illyrerweg 5, 4073 Edramsberg, Österreich`(address)
- `Valsyn-Maschinenbau GmbH`(organisation)
- `Schameitat Sanitär GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `Dr. Andreas Weißenbäck-Gasse` — partial — pred is substring of gold: `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Walter Dienstl` — partial — pred is substring of gold: `Mag. Walter Dienstl & Partner  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Vivian Malek`(person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich`(address)
- `Mag. Walter Dienstl & Partner  KG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

**False Positives:**

- `Univ.Prof. Dr. Sasan Hamzavi` — partial — gold is substring of pred: `Dr. Sasan Hamzavi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sasan Hamzavi`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Lydia Vogtleitner` — partial — pred is substring of gold: `StR Dr.in Lydia Vogtleitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `StR Dr.in Lydia Vogtleitner`(person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich`(address)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_26`)


Sie könne nicht  aufstehen, bewegt aber seitengleich (diesbezüglich liegen keine Befunde vor)   Derzeitige Beschwerden:   diverse Schmerzen, sie könne nicht gehen   Behandlung(en) / Medikamente / Hilfsmittel:   kann keine Angaben machen   Sozialanamnese:   lebt in Caritasheim vollbetreut, I(nvaliditäts)Pension, Pflegestufe 4, Erwachsenenvertretung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   28.4.87 Dipl.-Ing. Kirsten Hüffner: Es handelt sich bei (der Bf.) um eine Oligophrenie.

**False Positives:**

- `Ing. Kirsten Hüffner` — partial — pred is substring of gold: `Dipl.-Ing. Kirsten Hüffner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_77`)


Wie aus dem Gutachten Prof. Univ.Doz. Dr.med Dipl.-Ing. Kirsten Hüffner  vom 28.04.1987, Seite 6, ersichtlich,  sind schizophreniforme Psychosen bei Oligophrenie sehr schwer und oft gar nicht deutbar.

**False Positives:**

- `Ing. Kirsten Hüffner` — partial — pred is substring of gold: `Dipl.-Ing. Kirsten Hüffner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

**False Positives:**

- `Dr. Prause ` — partial — gold is substring of pred: `Dr. Prause`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Prause`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

**False Positives:**

- `Dr. Prause ` — partial — gold is substring of pred: `Dr. Prause`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Prause`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

**False Positives:**

- `Mag. Artner ` — partial — gold is substring of pred: `Mag. Artner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Artner`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Ing. Erwin Göktan` — partial — pred is substring of gold: `Dipl.-Ing. Erwin Göktan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Irene Kohler`(person)
- `Dipl.-Ing. Erwin Göktan`(person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

**False Positives:**

- `Dr. Karl Renner-Ring` — partial — gold is substring of pred: `Dr. Karl Renner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl Renner`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Dragan Höh` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

**False Positives:**

- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft` — partial — pred is substring of gold: `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Annemarie Wittjen`(person)
- `Samuel Herpel`(person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich`(address)
- `Erwin Baldauf`(person)
- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `Finanzamtes Landeck Reutte`(organisation)
- `39-702/2118`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Jonathan Hewett, Bakk. techn., Kleinbodenerstraße 17, 4880 Rixing, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Mag. Anton Heisinger Wirtschaftstreuhänder` — partial — gold is substring of pred: `Mag. Anton Heisinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jonathan Hewett, Bakk. techn.`(person)
- `Kleinbodenerstraße 17, 4880 Rixing, Österreich`(address)
- `Mag. Anton Heisinger`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Dr. Viktor Frankl-Gasse` — partial — pred is substring of gold: `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Waldemar Zumloh` — partial — pred is substring of gold: `Dipl.-Ing. Waldemar Zumloh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Michael Mandlmayr`(person)
- `Dipl.-Ing. Waldemar Zumloh`(person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `09-591/1655`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_92`)


Davon kann im gegenständlichen Fall hinsichtlich des  beschwerdegegenständlichen Jahres 2018 keine Rede sein:   Die Bf. hat zwar einen Schriftsatz (Arztbrief) vorgelegt, in dem der Arzt Dr. Martin Köppl  regelmäßige Rehabilitationsbehandlungen zum Erhalt der Selbständigkeit empfiehlt. Diese  Bestätigung des Hausarztes stammt vom 10.9.2018 und wurde also nachträglich ausgestellt.   Diese vermag jedoch aus o.a. Gründen mangels vorfeldweiser Verordnung keine  7 von 9 Seite 8 von 9

**False Positives:**

- `Dr. Martin Köppl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Ing. Techn ` — partial — pred is substring of gold: `Ing. Techn R Arthur Kornhass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Alice Rainprechter`(person)
- `Ing. Techn R Arthur Kornhass`(person)
- `Gstaudet 21, 9556 Besendorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Sandro Fischlein, Hans-Schilder-Platz 17, 9065 Untermieger, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Sandro Fischlein`(person)
- `Hans-Schilder-Platz 17, 9065 Untermieger, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Sophie Nauman` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Sophie Nauman`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman`(person)
- `Prof. Helmut Fürnkäß`(person)
- `Dr Christian Leskoschek`(person)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `party_context_name` 🏆

**F1:** 0.023 | **Precision:** 0.368 | **Recall:** 0.012  

**Format:** `regex`  
**Rule ID:** `e2b3ca6f`  
**Description:**
Captures names following 'Partei', 'durch', 'vertreten' but strictly requires a two-word name pattern (First Last) to avoid matching institutions.

**Content:**
```
(?:Partei|Parteien|durch|vertreten|Vertreter)\s+([A-Z][a-zäöüßéèêëïîôùûü]+\s+[A-Z][a-zäöüßéèêëïîôùûü]+)\b(?![a-z])(?!\s*(?:Rechtsanwälte|Anwälte|Partnerschaft|GmbH|AG|KG|Gesellschaft|Firma|Unternehmen|Bildung|Dienstleistungen|Versicherung|Bank|Konto|Kredit|Darlehen|Hypothek|Steuer|Finanz|Gericht|Kammer|Behörde|Amt|Ministerium|Bundes|Land|Stadt|Gemeinde|Ort|Bezirk|Kreis|Region|Lage|Position|Stelle|Job|Beruf|Tätigkeit|Funktion|Rolle|Aufgabe|Pflicht|Recht|Anspruch|Klage|Klagegrund|Klageantrag|Klagebegründung|Klageerwiderung|Klageantwort|Klageerhebung|Klageverhandlung|Klageentscheidung|Klageurteil|Klagebeschluss|Klageverfahren|Klagekosten|Klagegebühr|Klagefrist|Klageverjährung|Klageverwirkung|Klageverzicht|Revisionsgericht|Berufungsgericht|Oberste|Gerichtshof|Senatspräsidentin|Vizepräsident|Vizepräsidentin|Rekursgericht|Kontaktrecht|Dr\.\s+|Mag\.\s+|Prof\.\s+|Univ\.\s+|Hon\.\s+|MMag\.\s+|DI\.\s+|Ing\.\s+|Bakk\.\s+|PhD\.\s+|HR\.\s+|Techn\.\s+|Dipl\.\s+|PD\.\s+|Priv\.\s+|KommR\.\s+|ÖkR\.\s+|RgR\.\s+|StR\.\s+|MedR\.\s+|KzlR\.\s+|OMedR\.\s+|VetR\.\s+|AR\.\s+|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+|Jugendhilfeträger|Mutter|Vater|Eltern|Kind|Sohn|Tochter|Gewährung|Unterhaltsvorschuss|Strafsachen|Zivilrechtssachen|Maurer|Schalungsbauer|Anzahl|Verbrechen|Missbrauchs|Unmündigen|Geborenen|Schuld|Tatzeitraum|Verfahren|Nichtigkeitsb))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.368 | 0.012 | 0.023 | 76 | 28 | 48 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 28 | 48 | 2361 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Chen Petermüller,  Sand 5, 4851 Hehenberg, Österreich, vertreten durch Anka Vrcic, Kummergasse 7//3/2, 1210 Wien, über die  Beschwerden vom 25. April 2019 gegen die Bescheide des Finanzamtes Salzburg-Land vom  25. März 2019 betreffend Abweisung des Antrages auf Wiederaufnahme des Verfahrens  hinsichtlich Umsatzsteuer 2016 und betreffend Abweisung des Antrages auf Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2016, Steuernummer 20-238/1198, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anka Vrcic` | `Anka Vrcic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chen Petermüller` (person)
- `Sand 5, 4851 Hehenberg, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `20-238/1198` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vedat Gökdemir` | `Vedat Gökdemir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Björn Hüpscher` (person)
- `Igor Strunz` (person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Helmut Binder` | `Helmut Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alfred Klaming` (person)
- `Calvin Gorol` (person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich` (address)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ursula Raubart, Tschupbach 5c, 4144 Karlsbach, Österreich, vertreten durch Rachel Woiczyk, Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 86-917/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Rachel Woiczyk` | `Rachel Woiczyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Raubart` (person)
- `Tschupbach 5c, 4144 Karlsbach, Österreich` (address)
- `Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `86-917/1669` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133177.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anabel Sezgin  in der Beschwerdesache der  Leichsner u. Knoerrnschild Getränke, Siegersdorf bei Herberstein 14, 4693 Buchleiten, Österreich, vertreten durch Heinz Wollkopf,  Gartenauerstraße 8, 4616 Grassing, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heinz Wollkopf` | `Heinz Wollkopf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Anabel Sezgin` (person)
- `Leichsner u. Knoerrnschild Getränke` (organisation)
- `Siegersdorf bei Herberstein 14, 4693 Buchleiten, Österreich` (address)
- `Gartenauerstraße 8, 4616 Grassing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/133706.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Morgana Deppermann, MSc BEd, Am Steinparz 54, 2000 Oberolberndorf, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die Beschwerde vom  3. Juli 2015 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 29. Mai 2015  betreffend Anspruchszinsen (§ 205 BAO) 2003, 2004, 2005 und 2006 zu Steuernummer  25-580/4262  zu Recht erkannt:   I. Die angefochtenen Bescheide werden - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Morgana Deppermann, MSc BEd` (person)
- `Am Steinparz 54, 2000 Oberolberndorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `25-580/4262` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/135111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135111.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterPerson_A in der Beschwerdesache Leander Tumoseit,  Schwaighofweg, Oberau 122, 4121 Hörhag, Österreich, vertreten durch Othmar Huttary, Höttinger Au 76, 6020 Innsbruck, über die  Beschwerde vom 18. September 2015 gegen die Bescheide des [...] vom 20. August 2015 über  die Festsetzung von Anspruchszinsen (§ 205 BAO) für die Jahre 2011 und 2012, Steuernummer  56-131/0598, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Othmar Huttary` | `Othmar Huttary` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leander Tumoseit` (person)
- `Schwaighofweg, Oberau 122, 4121 Hörhag, Österreich` (address)
- `56-131/0598` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/136562.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger über die  Beschwerde des Vivian Cyriack, Erlbrücke 21, 8063 Höf, Österreich, vertreten durch Werner Mec, Holzmeistergasse  6/1/10, 1210 Wien, vom 8. Februar 2022, gegen die Vollstreckungsverfügung des Magistrates  der Stadt Wien, Magistratsabteilung 6, vom 29. Jänner 2022, Zl. Zahl, iZm einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als unbe- gründet abgewiesen  Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach Art. 133  Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `Werner Mec` | `Werner Mec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Vivian Cyriack` (person)
- `Erlbrücke 21, 8063 Höf, Österreich` (address)
- `Magistrates  der Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_92`)


Punkt 2.5.10.2 Abs 1 der AGB 2006 lautet wörtlich:   „Schadenersatz aufgrund fristloser Kündigung  Bei fristloser Kündigung durch Simon Zieselsberger  und – falls die Parteien keine andere Vereinbarung  getroffen haben – in allen sonstigen Fällen der vorzeitigen Vertragsbeendigung schuldet der  Kunde neben den rückständigen Leasingraten – auch im Fall der Insolvenz – einen sofort  fälligen Schadenersatzanspruch statt der Leistung;

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_106`)


Bei außerordentlicher Kündigung durch Simon Zieselsberger  und – falls die Parteien keine andere  Vereinbarung getroffen haben – in allen sonstigen Fällen der Vertragsbeendigung vor Erreichen  der Kalkulationsbasisdauer, ausgenommen im Falle des Diebstahls oder Totalschadens,  schuldet der Kunde neben den rückständigen Leasingraten – auch im Fall der Insolvenz – einen  sofort fälligen Schadenersatzanspruch statt der Leistung;

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_1`)


BESCHLUSS-VERFAHRENSHILFE   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. über den Antrag auf  Gewährung der Verfahrenshilfe des Antragstellers Oliver Simmer Schwag 3, 4852 Steinwand, Österreich, vertreten durch  Franka Reissl, vom 17.5.2022 für das Beschwerdeverfahren betreffend Beschwerde  gegen den Bescheid über die Festsetzung von Aussetzungszinsen des Finanzamtes Österreich  vom 21.6.2019 zur Steuernummer 28-382/0919  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe gemäß § 292 BAO wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Franka Reissl` | `Franka Reissl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Oliver Simmer` (person)
- `Schwag 3, 4852 Steinwand, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `28-382/0919` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/138464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138464.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Constantin Mosmüller  in der Angelegenheit der Parteien   Sean Spies (Beschwerdeführer), vertreten durch die Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH, 1010 Wien und    FA Freistadt Rohrbach Urfahr  als Amtspartei und Gesamtrechtsnachfolger des FA Wien 2/20/21/22 betreffend die  Beschwerde vom 25.9.2020               gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 25.8.2020 betreffend  Abweisung eines Antrages auf Aufhebung des Einkommensteuerbescheides 2017 vom  28.6.2019 gem. § 299 BAO   den Beschluss gefasst:  Der Vorlageantrag des Beschwerdeführers vom 23.8.2022 gegen die  Beschwerdevorentscheidung vom 21.7.2022 über die Beschwerde gegen den Bescheid vom  25.8.2020 über die Abweisung des Antrags auf Aufhebung des Einkommensteuerbescheides  2017 vom 28.6.2019 gem. § 299 BAO   wird als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Sean Spies` | `Sean Spies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Constantin Mosmüller` (person)
- `Centurion Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `FA Freistadt Rohrbach Urfahr` (organisation)
- `FA Wien 2/20/21/22` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/141068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Nicola Diessel  in der Beschwerdesache Dipl. Kfm. Fridolin Lucks,  Schlagturn 100, 4762 Wamprechtsham, Österreich, vertreten durch Corinna Giebelmann, betreffend Beschwerde vom 03.06.2022 gegen den  Bescheid des Finanzamtes Österreich vom 05.04.2022 über die Feststellung von Einkünften  gemäß § 188 BAO für 2020, beschlossen:  Der Vorlageantrag vom 23.12.2022 wird gemäß § 260 Abs 1 lit a iVm § 264 Abs 4 lit e der  Bundesabgabenordnung, BGBl. Nr. 194/1961 idgF (BAO) als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Giebelmann` | `Corinna Giebelmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Nicola Diessel` (person)
- `Dipl. Kfm. Fridolin Lucks` (person)
- `Schlagturn 100, 4762 Wamprechtsham, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/141878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141878.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dieter Hasler  in der Angelegenheit der Parteien  Gabriele Esser, XXX (Beschwerdeführer), vertreten durch Herrn Mag. Erich Guggi, Steuerberater  und Wirtschaftsprüfer in 9020 Klagenfurt und Finanzamt Österreich als Amtspartei und als  Gesamtrechtsnachfolger des Finanzamtes A über die Beschwerde vom 29.4.2015   gegen den Bescheid des Finanzamtes A vom 27.2.2015 betreffend Einkommensteuer 2012  (83-913/2342)

| Predicted | Gold |
|---|---|
| `Gabriele Esser` | `Gabriele Esser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Dieter Hasler` (person)
- `Mag. Erich Guggi` (person)
- `Finanzamt Österreich` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)
- `83-913/2342` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/144352.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144352.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Ivan Damlos  in der Beschwerdesache Sascha Kovalczyk,  Untertweng-Hauserweg 9, 8130 Schrauding, Österreich, vertreten durch Iris Lorensen, über die Beschwerde vom 06.02.2024 gegen den  Bescheid des Finanzamtes Österreich vom 09.01.2024 betreffend Festsetzung des  Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum 01.12.2022 bis 30.06.2023, St.Nr. 72-875/7408, zu Recht erkannt:   I.  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Iris Lorensen` | `Iris Lorensen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Ivan Damlos` (person)
- `Sascha Kovalczyk` (person)
- `Untertweng-Hauserweg 9, 8130 Schrauding, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `72-875/7408` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/144733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144733.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Valerius Leitmeyr  in der Beschwerdesache Levi Strathoff,  Biberngasse 90H, 9560 St. Martin, Österreich, vertreten durch Daisy Karayigit, über die Beschwerde der beschwerdeführenden  Partei vom 06.05.2024 wegen behaupteter Verletzung der Pflicht zur Erlassung eines  Bescheides durch das Finanzamt Österreich über den Antrag vom 23.05.2023 gemäß § 299  BAO auf Aufhebung des Einkommensteuerbescheides 2021 vom 17.11.2022, Steuernummer  51-246/3233, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs 2 letzter Satz der Bundes- abgabenordnung, BGBl. 1961/194, idgF (BAO) eingestellt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Daisy Karayigit` | `Daisy Karayigit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Valerius Leitmeyr` (person)
- `Levi Strathoff` (person)
- `Biberngasse 90H, 9560 St. Martin, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `51-246/3233` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/144802.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144802.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Scarlett Kizilyel  in der Beschwerdesache Hon.-Prof.in Cathleen Andrulat,  Am Schutzdamm 27B, 9871 Liedweg, Österreich, vertreten durch Wolfgang Fußgänger, Währinger Gürtel 125 Tür 5, 1180 Wien,  betreffend Beschwerde vom 7. Jänner 2014 gegen die Bescheide des Finanzamtes Wien  2/20/21/22 vom 25. November 2013 betreffend Einkommensteuer 2011, Einkommensteuer  2012, Umsatzsteuerfestsetzung 01.2013-06.2013, Umsatzsteuer 2011 und Umsatzsteuer 2012  Steuernummer 26-988/8559  beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wolfgang Fußgänger` | `Wolfgang Fußgänger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Scarlett Kizilyel` (person)
- `Hon.-Prof.in Cathleen Andrulat` (person)
- `Am Schutzdamm 27B, 9871 Liedweg, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `26-988/8559` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/145381.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145381.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. März  2024, Zahl: MA67/246700033979/2024, wurde die beschwerdeführende Partei Erika Bronnenmeier  der  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Erika Bronnenmeier` | `Erika Bronnenmeier` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/145403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Torsten Schöpfner  in der Beschwerdesache Pjotr Bergtholdt,  Berg-Isel-Weg 19, 4861 Jetzing, Österreich, vertreten durch Silvester Köhlert, IZ NÖ-Süd, Straße 3 27, 3500 Landersdorf, Österreich, über die Beschwerde vom  13. Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 8. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2022 Steuernummer 06-564/4508  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvester Köhlert` | `Silvester Köhlert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Torsten Schöpfner` (person)
- `Pjotr Bergtholdt` (person)
- `Berg-Isel-Weg 19, 4861 Jetzing, Österreich` (address)
- `IZ NÖ-Süd, Straße 3 27, 3500 Landersdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `06-564/4508` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/146142.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146142.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hon.-Prof. Janosch Weinberger  in der Beschwerdesache Igor Golobic,  Fernitz 24, 8832 Krumegg, Österreich, vertreten durch Peter Weinmar, Lerchengasse 18, 1080 Wien, über die  Beschwerde vom 14.November 2023 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom 24. Oktober 2023  betreffend Zahlungserleichterungen § 212 BAO 24.10.2023 zur Steuernummer  58-685/2299  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Weinmar` | `Peter Weinmar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Hon.-Prof. Janosch Weinberger` (person)
- `Igor Golobic` (person)
- `Fernitz 24, 8832 Krumegg, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)
- `58-685/2299` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/146145.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Sonja Hillbrand, Weiglweg 5, 2871 Guggendorf, Österreich, vertreten durch Khachador Jalmanian, Grenzackerstraße 7/17/1,  1100 Wien, über die Beschwerde vom 1. Februar 2023 gegen die Bescheide des Finanzamtes  Österreich vom 30. September 2022 betreffend Umsatz- und Einkommensteuer 2018 bis 2021,  Steuernummer 25-480/0274, nach Abhaltung einer mündlichen Verhandlung am 9.  Oktober 2024 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Khachador Jalmanian` | `Khachador Jalmanian` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Sonja Hillbrand` (person)
- `Weiglweg 5, 2871 Guggendorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `25-480/0274` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/147390.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147390.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Christian Linz  in der Beschwerdesache Georg Gramlich,  Englen 8, 3804 Bernschlag, Österreich, vertreten durch Adalbert Keidel, Haltergraben 6, 8636 Göriach, Österreich, über die Beschwerde vom  25.03.2016 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 24.02.2016 betreffend Kommunalsteuer für den Zeitraum 2010 bis  2013, beschlossen:  Die Beschwerde wird gemäß § 256 Ab 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Adalbert Keidel` | `Adalbert Keidel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Linz` (person)
- `Georg Gramlich` (person)
- `Englen 8, 3804 Bernschlag, Österreich` (address)
- `Haltergraben 6, 8636 Göriach, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/147962.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147962.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Konstanze Bachstelz  in der Beschwerdesache der  Heizung Werklem, Hählingen 3, 3650 Haag, Österreich, vertreten durch Zoltan Brunsmann  als Masseverwalter im  Insolvenzverfahren der Heizung Werklem, Wr.Stadthallenbad 68, 8990 Reith, Österreich, über die Beschwerde vom 5. März 2025  gegen den Bescheid des Finanzamtes Österreich vom 6. Februar 2025 betreffend  Zwangsstrafen 2025 Steuernummer 68-648/0616  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Zoltan Brunsmann` | `Zoltan Brunsmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Konstanze Bachstelz` (person)
- `Heizung Werklem` (organisation)
- `Hählingen 3, 3650 Haag, Österreich` (address)
- `Heizung Werklem` (organisation)
- `Wr.Stadthallenbad 68, 8990 Reith, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `68-648/0616` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/148500.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148500.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karola Vlachodimitris  in der Beschwerdesache DDr. Diego Leberfinger,  Dietrichsteinerstraße 6, 5232 Kobl, Österreich  vertreten durch  Cedric Werly, über die Beschwerde vom 15. Jänner 2016 gegen  den Bescheid des Finanzamt Niederösterreich Mitte (nunmehr Finanzamt Österreich) vom 22. Dezember 2015  betreffend Einkommensteuer 2005, Steuernummer 78-413/6163  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Cedric Werly` | `Cedric Werly` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Karola Vlachodimitris` (person)
- `DDr. Diego Leberfinger` (person)
- `Dietrichsteinerstraße 6, 5232 Kobl, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)
- `Finanzamt Österreich` (organisation)
- `78-413/6163` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/148994.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148994.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Damian Janne, BA, Straßhof 20, 3595 Atzelsdorf, Österreich, vertreten durch Helga Reutner, Habsburgstrasse  20, 3680 Persenbeug/NÖ, über die Beschwerde vom 24. April 2017 gegen die Bescheide des  Finanzamtes Amstetten Melk Scheibbs vom 27. März 2017 betreffend Anspruchszinsen (§ 205  BAO) 2008, 2009, 2010 und 2011 Steuernummer 29-286/8127  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Helga Reutner` | `Helga Reutner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Damian Janne, BA` (person)
- `Straßhof 20, 3595 Atzelsdorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `29-286/8127` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149046.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Patricia Zegger  in der Beschwerdesache Esmeralda Abeling,  Am Klostergrund 28, 3382 Neubach, Österreich  vertreten durch Dagmar Thanel, über die Beschwerde vom 20. August 2024 gegen  den Bescheid des Finanzamtes Österreich vom 12. August 2024 über die Abweisung eines  Zahlungserleichterungsansuchens, Steuernummer 12-957/0008  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dagmar Thanel` | `Dagmar Thanel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Patricia Zegger` (person)
- `Esmeralda Abeling` (person)
- `Am Klostergrund 28, 3382 Neubach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `12-957/0008` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149380.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149380.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Univ.-Prof.in Sibylle Bacher  in der Beschwerdesache  Alina Pater, Jakob-Ladroner-Weg 1i, 7432 Willersdorf, Österreich, vertreten durch Milena Baldszun, über die Beschwerde vom 14. November  2016 gegen die Bescheide des Finanzamtes Wien 2/20/21/22 (nun Finanzamt Österreich) vom  10. Oktober 2016 betreffend Einkommensteuer 2011, 2012, 2013 und 2014, Steuernummer  96-926/8972, zu Recht:   I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Milena Baldszun` | `Milena Baldszun` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Sibylle Bacher` (person)
- `Alina Pater` (person)
- `Jakob-Ladroner-Weg 1i, 7432 Willersdorf, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)
- `96-926/8972` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149834.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Sara Thanopoulos  in der Beschwerdesache  Wolf Mauel, Mellach, vertreten durch Peter Weinmar, Neudeggergasse 5 Tür 22, 1080  Wien, über die Beschwerde vom 11. Dezember 2019 gegen die Bescheide des Finanzamtes  Österreich vom 15. März 2019 betreffend Feststellung der Einkünfte § 188 BAO 2011 bis 2017  und betreffend Umsatzsteuer 2013 bis 2017 zu Steuernummer 01-978/5098  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Weinmar` | `Peter Weinmar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Sara Thanopoulos` (person)
- `Wolf Mauel` (person)
- `Mellach` (city)
- `Finanzamtes  Österreich` (organisation)
- `01-978/5098` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Jank Weiler` — partial — pred is substring of gold: `Jank Weiler Operenyi Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Gerald Erwin Ehgartner`(person)
- `Zeno Matyssek`(person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH`(organisation)
- `Finanzamt für Gebühren`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Raphael Williamson, BEd, Züggen 8, 8042 Graz, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Monika Pfundner` — partial — pred is substring of gold: `Monika Pfundner-Lenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Raphael Williamson, BEd`(person)
- `Züggen 8, 8042 Graz, Österreich`(address)
- `Monika Pfundner-Lenz`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_57`)


Es gab  somit im Ermittlungsverfahren für das Finanzamt keine Möglichkeit, den tatsächlich durch Ihre  Behinderung verursachten Mehraufwand für die Diätverpflegung festzustellen, sodass nur der  bereits im Erstbescheid berücksichtigte Pauschalbetrag für die Diätverpflegung als steuerliche  Abzugspost anerkannt werden konnte.“

**False Positives:**

- `Ihre  Behinderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Grant Thornton` — partial — pred is substring of gold: `Grant Thornton Austria GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Miroslav Treischl`(person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich`(address)
- `Grant Thornton Austria GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_28`)


Im Schreiben vom 5.3.2019 fordert der Bf vom BFA eine Begründung für die vormalige  erkennungsdienstliche Behandlung, wozu er an das BFA und auf eine Akteneinsicht verwiesen  worden sei, und führt weiter aus:  "Ich benötige keinen Termin zur Akteneinsicht, sondern den Grund der erkennungsdienstlichen  Behandlung durch Ihre Behörde …".

**False Positives:**

- `Ihre Behörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_70`)


Die  Bundesverfassung verbietet es dem Gesetzgeber nicht, für die Inanspruchnahme behördlicher  Tätigkeiten durch Privatpersonen Gebühren zu erheben und die Gebührenpflicht bereits an die  Eingabe zu knüpfen (VfGH 10.6.1978, B 448/77; vgl.

**False Positives:**

- `Privatpersonen Gebühren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_9`)


keine aktuelle Schulbestätigung von Ihrem Sohn M… vorgelegt haben und dadurch Ihrer  Mitwirkungspflicht nach § 119 Bundesabgabenordnung nicht nachgekommen sind, muss  angenommen werden, dass in oben genannten Zeitraum kein Anspruch auf Familienbeihilfe  bestanden hat bzw. besteht.

**False Positives:**

- `Ihrer  Mitwirkungspflicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Treufinanz Steuerberatung` — partial — pred is substring of gold: `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

**False Positives:**

- `Kleiner Eberl` — partial — pred is substring of gold: `Kleiner Eberl Brandstätter  Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eugenia Vesen`(person)
- `Apollogasse 213, 5522 Lammertal, Österreich`(address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_90`)


Primäre Zweckbestimmung des streitgegenständlichen Kfz, welches sich ab dem Erwerb im  Jahr 2011 bis zum Verkauf im Jahr 2016 im zivilrechtlichen Eigentum der Bf. befand, war die  Ermöglichung der Nutzung durch Herrn Hus  welcher wie ein  Eigentümer über das Kfz verfügte.

**False Positives:**

- `Herrn Hus` — partial — gold is substring of pred: `Hus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hus`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Cathleen Ganczarczyk  in der Beschwerdesache Hon.-Prof. Gregor Liechtenstein,  Platz der Menschenrechte 39, 4652 Reuharting, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, über die Beschwerde vom 28. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 26. November 2020 betreffend Gebühren 29.04.2014  Steuernummer 82-359/1150  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Deloitte Tax` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Cathleen Ganczarczyk`(person)
- `Hon.-Prof. Gregor Liechtenstein`(person)
- `Platz der Menschenrechte 39, 4652 Reuharting, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `82-359/1150`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Delia Kavelmann  in der Beschwerdesache Larissa Rastätter,  Wendelgraben 27, 6563 Galtür, Österreich, vertreten durch Glocknitzer Hollenthoner Stb.GmbH & Co KG,1050 Wien,  Bräuhausgasse 37/4, 1150 Wien, über die Beschwerde vom 10. April 2012 gegen den Bescheid  des FA Wien 9/18/19 Klosterneuburg vom 14. März 2012 betreffend Festsetzung des  Dienstgeberbeitrages 2006 bis 2009 Steuernummer abc zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben:  I. Die Beschwerde hinsichtlich Dienstgeberbeitrag für die Ärztinnen Dr. U und PhD Isaak Joern wird  abgewiesen.

**False Positives:**

- `Glocknitzer Hollenthoner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Delia Kavelmann`(person)
- `Larissa Rastätter`(person)
- `Wendelgraben 27, 6563 Galtür, Österreich`(address)
- `FA Wien 9/18/19 Klosterneuburg`(organisation)
- `PhD Isaak Joern`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133998.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Imre Wittek  über die Beschwerde des Lara Schwertzel,  Stockinger Straße 23, 4892 Schwandeck, Österreich, vertreten durch Mag. Ingrid Huber, Feldweg 7, 9241 Wernberg, vom  02.01.2017 gegen den Bescheid des Finanzamtes St. Veit Wolfsberg (nunmehr FA Österreich),  dieses vertreten durch Ilse König BA MA, vom 17.03.2016 betreffend Einkommensteuer 2010  (ANV) im fortgesetzten Verfahren den Beschluss gefasst:   Der Vorlageantrag wird gemäß § 264 Abs. 4 lit e BAO iVm § 260 Abs. 1 BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Ilse König` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Imre Wittek`(person)
- `Lara Schwertzel`(person)
- `Stockinger Straße 23, 4892 Schwandeck, Österreich`(address)
- `Mag. Ingrid Huber`(person)
- `Finanzamtes St. Veit Wolfsberg`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Frederike Bookholdt  in der Beschwerdesache DDr. Dr. Lorenz Wachenhusen,  Am Lurnbichl 4, 4871 Redl, Österreich, vertreten durch Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Eduard-Wallnöfer-Platz 1, 6460 Imst, über die Beschwerde vom  10. Juni 2013 gegen den Bescheid des FA Landeck Reutte (nunmehr FA Österreich) vom 15. Mai  2013, StrNr, betreffend Festsetzung der Normverbrauchsabgabe für den Zeitraum März 2012  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Kapferer Frei` — partial — pred is substring of gold: `Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Frederike Bookholdt`(person)
- `DDr. Dr. Lorenz Wachenhusen`(person)
- `Am Lurnbichl 4, 4871 Redl, Österreich`(address)
- `Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `FA Landeck Reutte`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134201.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134201.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterDr. Martin Wittmann in der Beschwerdesache  [...], [...], vertreten durch Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Brockmanngasse 75, 8010 Graz, über die Beschwerde vom  27. Jänner 2017 gegen die Bescheide des Finanzamt Landeck Reutte  jeweils vom 10. Jänner 2017,  Steuernummer 16-981/1693, betreffend Energieabgabenvergütung 2011 -2015 zu Recht  erkannt:   I. Der Bescheid vom 10. Jänner 2017 betreffend Festsetzung des Vergütungsbetrages  nach dem Energieabgabenvergütungsgesetz für das Kalenderjahr 2011 wird  abgeändert.

**False Positives:**

- `Styria Treuhand` — partial — pred is substring of gold: `Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Landeck Reutte`(organisation)
- `16-981/1693`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134614.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134614.1_7`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Richter1, den RichterRichter2  sowie die fachkundigen Laienrichter Richter3 und Richter4 in der Beschwerdesache Massimo Heimker,  Klöpplergasse 7, 9781 Unterpirkach, Österreich  Österreich, vertreten durch Steuerberater Vertreter, AdresseVertreter,  Österreich, betreffend die Beschwerde vom 27. Februar 2012 gegen den  Umsatzsteuerbescheid 2010 des Finanzamtes X vom 27. Jänner 2012 beschlossen:  Dem Gerichtshof der Europäischen Union wird gemäß Art. 267 AEUV folgende Frage zur  Vorabentscheidung vorgelegt:  Ist die Richtlinie 2006/112/EG des Rates vom 28. November 2006 über das gemeinsame  Mehrwertsteuersystem in der Fassung der Richtlinie 2008/8/EG des Rates vom 12. Februar  2008 so auszulegen, dass die nationalen Behörden und Gerichte den Ort einer Dienstleistung,  der formal nach dem geschriebenen Recht in dem anderen Mitgliedstaat, in welchem sich der  Sitz des Leistungsempfängers befindet, liegt, als im Inland liegend anzusehen haben, wenn der  leistungserbringende inländische Steuerpflichtige hätte wissen müssen, dass er sich durch die  erbrachte Dienstleistung an einer im Rahmen einer Leistungskette begangenen  Mehrwertsteuerhinterziehung beteiligt?

**False Positives:**

- `Steuerberater Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Massimo Heimker`(person)
- `Klöpplergasse 7, 9781 Unterpirkach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_84`)


§ 6 Wiener Parkometergesetz 2006, LGBl. 71/2018, normiert:  Aus Gründen der Verwaltungsvereinfachung und der Vereinheitlichung kann die Gemeinde  durch Verordnung Pauschalierungsrichtlinien festlegen, die die Höhe und die Form der Ab- gabenentrichtung regeln und auf das unterschiedliche Abstellverhalten der Wohnbevölkerung  in Gebieten, die gemäß § 43 Abs. 2a StVO 1960, BGBl. Nr. 159/1960, in der Fassung des  Bundes¬gesetzes BGBl. I Nr. 99/2005, verordnet sind, des Wirtschaftsverkehrs und des  sonstigen Verkehrs Bedacht nehmen.

**False Positives:**

- `Verordnung Pauschalierungsrichtlinien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135600.1_8`)


Bemerkungen (Spesenreglement durch Kanton Zürich am  24.2.2004 genehmigt),   1 von 4 Seite 2 von 4

**False Positives:**

- `Kanton Zürich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/135955.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135955.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Elisabeth Hafner in der Beschwerdesache  Dipl.-Ing. StR Ali Butzler, Trenninggasse 37, 2130 Hobersdorf, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH,  Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom 30. September 2020 gegen die  Bescheide des Finanzamtes Klagenfurt vom 8. Juli 2020 betreffend  I. die Wiederaufnahme des Verfahrens zur Festsetzung des Vergütungsbetrages nach dem  Energieabgabenvergütungsgesetz für den Zeitraum 2014 und  II. die Festsetzung des Vergütungsbetrages nach dem Energieabgabengesetz für den Zeitraum  2014  I. zu Recht erkannt:  Der Beschwerde gegen den Bescheid betreffend die Wiederaufnahme des Verfahrens zur  Festsetzung des Vergütungsbetrages nach dem Energieabgabenvergütungsgesetz für den  Zeitraum 2014 wird Folge gegeben.

**False Positives:**

- `Deloitte Tax` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Dipl.-Ing. StR Ali Butzler`(person)
- `Trenninggasse 37, 2130 Hobersdorf, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Klagenfurt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Gunderson  in der Beschwerdesache Florentin Mavrakis,  Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich, vertreten durch Intercura Treuhand - und Revisionsgesellschaft m.b.H.,  Langobardenstraße 51 Tür 6, 1220 Wien, über die Beschwerde vom 23. Dezember 2021 gegen  den Bescheid des FA Wien 2/20/21/22  vom 9. Dezember 2021 betreffend Festsetzung eines ersten  Säumniszuschlages, Steuernummer 95-900/0656, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Intercura Treuhand` — partial — pred is substring of gold: `Intercura Treuhand - und Revisionsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Björn Gunderson`(person)
- `Florentin Mavrakis`(person)
- `Dr.-Adolf-Hörhager-Straße 299, 3691 Mitterndorf, Österreich`(address)
- `Intercura Treuhand - und Revisionsgesellschaft m.b.H.`(organisation)
- `FA Wien 2/20/21/22`(organisation)
- `95-900/0656`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Helena Kemmerer  in der Beschwerdesache  ÖkR Jeannine Radmacher, Hirsbodenstraße 5, 4710 Neuwies, Österreich, vertreten durch Rechtsanwälte Offer & Partner OG, Museumstraße  16, 6020 Innsbruck, über die Beschwerde vom 4. Mai 2022 gegen den Bescheid des  Finanzamtes Österreich vom 4. April 2022, StrNr, betreffend Zurückweisung des Antrages vom  31.12.2020 auf "Durchführung einer Lohnsteuerprüfung gemäß § 86 EStG" zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwälte Offer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Helena Kemmerer`(person)
- `ÖkR Jeannine Radmacher`(person)
- `Hirsbodenstraße 5, 4710 Neuwies, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_96`)


Ausgenommen sind: …  g) Fahrzeuge, die lediglich zum Zwecke des Aus- und Einsteigens von Personen oder für die  Dauer der Durchführung einer Ladetätigkeit halten.“  § 1 Abs. 1 Wiener Landes-Gesetz über die Regelung der Benützung von Straßen durch  abgestellte mehrspurige Kraftfahrzeuge (Parkometergesetz 2006): „Die Gemeinde wird  ermächtigt, durch Verordnung für das Abstellen von mehrspurigen Kraftfahrzeugen in  Kurzparkzonen gemäß § 25 der Straßenverkehrsordnung 1960 (StVO 1960),  BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005, die Entrichtung  einer Abgabe auch für mehrspurige Kraftfahrzeuge vorzuschreiben, die lediglich zum Zwecke  des Aus- und Einsteigens von Personen oder für die Dauer der Durchführung einer Ladetätigkeit  halten.“  § 6 Parkometergesetz 2006: „Aus Gründen der Verwaltungsvereinfachung und der  Vereinheitlichung kann die Gemeinde durch Verordnung Pauschalierungsrichtlinien festlegen,  die die Höhe und die Form der Abgabenentrichtung regeln und auf das unterschiedliche  Abstellverhalten der Wohnbevölkerung in Gebieten, die gemäß § 43 Abs. 2a StVO 1960,  BGBl. Nr. 159/1960, in der Fassung des Bundesgesetzes BGBl. I Nr. 99/2005, verordnet sind, des  Wirtschaftsverkehrs und des sonstigen Verkehrs Bedacht nehmen.“  8 von 13 Seite 9 von 13

**False Positives:**

- `Verordnung Pauschalierungsrichtlinien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/137638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137638.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Torsten Jagenteufel  in der Beschwerdesache Klarissa Grahmann,  Scheibbser Straße 6, 4904 Unterapping, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, betreffend Beschwerden  - vom 15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20.  August 2020 betreffend Feststellungsbescheid Gruppenmitglied 2014 bis 2016; sowie  - vom 17. November 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 30.  Oktober 2020 betreffend Feststellungsbescheid Gruppenmitglied 2017 und 2018  den Beschluss:  I. Die Beschwerden werden gemäß § 278 Abs. 1 lit. b iVm § 256 Abs. 3 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Deloitte Tax` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Torsten Jagenteufel`(person)
- `Klarissa Grahmann`(person)
- `Scheibbser Straße 6, 4904 Unterapping, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/137664.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137664.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Linn Weinfurt  in der Beschwerdesache Friedhelm Duvenkropp,  Waldachweg 16, 9761 Kalch, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, betreffend Beschwerden vom 11. Februar 2020 und 27. Februar 2020  gegen die Bescheide betreffend Feststellungsbescheid Gruppenmitglied 2014 vom 11. Februar  2020 sowie vom 13. Jänner 2020 betreffend Feststellungsbescheid Gruppenmitglied 2015 und  2016 jeweils des Finanzamtes Wien 1/23 den Beschluss:   I. Die Beschwerden werden gemäß § 278 Abs. 1 lit b iVm § 256 Abs. 3 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Deloitte Tax` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Linn Weinfurt`(person)
- `Friedhelm Duvenkropp`(person)
- `Waldachweg 16, 9761 Kalch, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Richterin Dr.in Elisabeth Hafner als Vorsitzende, die  Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. sowie die fachkundige Laienrichterin Eva  Maiwald-Wanderer und den fachkundigen Laienrichter Mag. Josef Bramer in der  Beschwerdesache Raimund Figgen, Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich, über die Beschwerde vom 13. August 2019  gegen den Bescheid des Finanzamtes Österreich vom 1. August 2019, vertreten durch Ilse  König, Bakk.

**False Positives:**

- `Ilse  König` — partial — pred is substring of gold: `Ilse  König, Bakk.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Elisabeth Hafner`(person)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eva  Maiwald-Wanderer`(person)
- `Mag. Josef Bramer`(person)
- `Raimund Figgen`(person)
- `Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Ilse  König, Bakk.`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/139132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139132.1_10`)


In der dagegen eingebrachten Beschwerde vom 29.11.2021 hielt die Erwachsenenvertretung  der Bf begründend fest, dass die Beschaffung der im Vorhalt vom 04.08.2021 angeführten  Unterlagen aufgrund der Urlaubszeiten, der äußerst schwierigen Kontaktaufnahme der  Erwachsenenvertretung mit der Bf, und der viel Zeit in Anspruch nehmenden Übermittlung von  Unterlagen durch Pro Juventute nicht fristgerecht möglich gewesen sei und sie daher zwei Mal  (am 02.09.2021 und am 13.10.2021) telefonisch um Fristerstreckung ersucht habe.

**False Positives:**

- `Pro Juventute` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/139570.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139570.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rosemarie Ulmeier  in der Beschwerdesache Waldtriost,  Pratztrumer Straße 9, 8820 Unterwald, Österreich, betreffend den Antrag auf Akteneinsicht der Antragstellerin, vertreten durch  Brauneis Klauser Prändl Rechtsanwälte GmbH, Bauernmarkt 2, 1010 Wien, vom 18.10.2021,  beschlossen:  Der Antrag wird mangels Legitimation als nicht zulässig zurückgewiesen.

**False Positives:**

- `Brauneis Klauser` — partial — pred is substring of gold: `Brauneis Klauser Prändl Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rosemarie Ulmeier`(person)
- `Waldtriost`(organisation)
- `Pratztrumer Straße 9, 8820 Unterwald, Österreich`(address)
- `Brauneis Klauser Prändl Rechtsanwälte GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/140199.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140199.1_86`)


§ 43 Abs 2a Z 1 StVO 1960 normiert:  Um Erschwernisse für die Wohnbevölkerung auszugleichen, die durch Verkehrsbeschränkungen  hervorgerufen werden, kann die Behörde durch Verordnung Gebiete bestimmen, deren  Bewohner die Erteilung einer Ausnahmegenehmigung für ein zeitlich uneingeschränktes Parken  in - in der Verordnung zu bezeichnenden - nahegelegenen Kurzparkzonen mit Kraftfahrzeugen  mit einem höchsten zulässigen Gesamtgewicht von nicht mehr als 3 500 kg gemäß § 45 Abs. 4  beantragen können.

**False Positives:**

- `Verordnung Gebiete` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/140299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gabriel Riedmiller  in der Angelegenheit der Parteien  Armin Lohwasser, BSc (Bf) und FA Innsbruck  als Amtspartei über die Beschwerde vom 7.2.2022              gegen den Bescheid des Finanzamtes vom 31.1.2022 betreffend Einkommensteuer           2020 (Arbeitnehmerveranlagung)

**False Positives:**

- `Armin Lohwasser` — partial — pred is substring of gold: `Armin Lohwasser, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriel Riedmiller`(person)
- `Armin Lohwasser, BSc`(person)
- `FA Innsbruck`(organisation)
- `Finanzamtes`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_14`)


Begründend wird  ausgeführt, die Bf habe trotz Aufforderung die von ihr abverlangten Unterlagen nicht  beigebracht und sei hierdurch Ihrer Mitwirkungspflicht nach § 115 Bundesabgabenordnung  (BAO) nicht nachgekommen.

**False Positives:**

- `Ihrer Mitwirkungspflicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Göß 3, 4852 Alexenau, Österreich, vertreten durch Hadaier Wirtschaftsprüfungs- und  Steuerberatungs-GmbH, Keplerstraße 1, 4910 Ried/Innkreis, über die Beschwerde vom 16. Juni  2021 gegen den Bescheid des Finanzamtes Österreich vom 20. Mai 2021 betreffend  Einkommensteuer 2019, Steuernummer 43-296/8747, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Hadaier Wirtschaftsprüfungs` — partial — pred is substring of gold: `Hadaier Wirtschaftsprüfungs- und  Steuerberatungs-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Göß 3, 4852 Alexenau, Österreich`(address)
- `Hadaier Wirtschaftsprüfungs- und  Steuerberatungs-GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `43-296/8747`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/141359.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Torsten Aichler, Unternehmerzentrum 21, 4652 Frohnhofen, Österreich, vertreten durch Rechtsanwälte Estermann und  Partner OG, Stadtplatz 6, 5230 Mattighofen, über die Beschwerde vom 21. April 2022 gegen  den Bescheid des Amtes für Betrugsbekämpfung vom 1. April 2022 betreffend Antrag auf  Akteneinsicht in Sachen Torsten Aichler, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwälte Estermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Torsten Aichler`(person)
- `Unternehmerzentrum 21, 4652 Frohnhofen, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)
- `Torsten Aichler`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_20`)


Im Vorlageantrag widerspricht der im Verfahren neu einschreitende, langjährige Rechtsberater  des Bf dem Beschwerdevorbringen mit einem Verweis auf die als weitere  Leistungsempfängerin beteiligte Immobilienverwertungs-GmbH, die ihrerseits durch  Erfüllungsgehilfen Bauleistungen erbracht habe.

**False Positives:**

- `Erfüllungsgehilfen Bauleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/142156.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142156.1_48`)


§ 43 Abs. 2a Z. 1 StVO 1960 lautet:  Um Erschwernisse für die Wohnbevölkerung auszugleichen, die durch Verkehrsbeschränkungen  hervorgerufen werden, kann die Behörde durch Verordnung Gebiete bestimmen, deren  Bewohner die Erteilung einer Ausnahmegenehmigung für ein zeitlich uneingeschränktes Parken  in - in der Verordnung zu bezeichnenden - nahegelegenen Kurzparkzonen mit Kraftfahrzeugen  mit einem höchsten zulässigen Gesamtgewicht von nicht mehr als 3 500 kg gemäß § 45 Abs. 4  beantragen können.

**False Positives:**

- `Verordnung Gebiete` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/142178.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142178.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Nancy Traxel, Kupferweg 6, 4263 Riemetschlag, Österreich, vertreten durch Rechtsanwälte Estermann &  Partner OG, Stadtplatz 6, 5230 Mattighofen, über die Beschwerde vom 22. Juni 2022 gegen  den Bescheid des Amtes für Betrugsbekämpfung vom 2. Juni 2022 betreffend Antrag auf  Auskunftserteilung in Sachen Nancy Traxel  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwälte Estermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Nancy Traxel`(person)
- `Kupferweg 6, 4263 Riemetschlag, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)
- `Nancy Traxel`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Karim Ickstadt  in der Beschwerdesache   Axel Jastrzemsky, als Gruppenträgerin, V GmbH, als Gruppenmitglied und der Klemeyer + Heisterhagen Pharma GmbH  als von der  Teilnahme an der Unternehmensgruppe ausgeschlossene Körperschaft, jeweils vertreten durch  Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG, Linzer Bundesstraße 101, 5023  Salzburg-Gnigl, über die Beschwerde der Axel Jastrzemsky, Sandweg 7, 4782 Aigerding, Österreich, vom 28. März 2019 gegen  den Gruppenfeststellungsbescheid 2018 des Finanzamtes Wien 12/13/14 Purkersdorf -  nunmehr Finanzamtes Österreich - vom 27. Februar 2019, Steuernummer 74-905/9339,  nach Durchführung einer mündlichen Verhandlung am 22. August 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Unterberger Fidas` — partial — pred is substring of gold: `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Karim Ickstadt`(person)
- `Axel Jastrzemsky`(person)
- `Klemeyer + Heisterhagen Pharma GmbH`(organisation)
- `Unterberger Fidas Salzburg Steuerberatung GmbH & Co KG`(organisation)
- `Axel Jastrzemsky`(person)
- `Sandweg 7, 4782 Aigerding, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `Finanzamtes Österreich`(organisation)
- `74-905/9339`(tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/142761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142761.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  Mag. Monika Ahorn sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Clarissa Maak, Haidenweg 21, 5321 Koppl, Österreich, vertreten durch Sacha  Katzensteiner Blauensteiner Rechtsanwälte GmbH, Gartenaugasse 3, 3500 Krems/Donau, über  die Beschwerde vom 28. Dezember 2020 gegen die Bescheide des Finanzamtes Hollabrunn  Korneuburg Tulln (nunmehr Finanzamt Österreich,   § 323b BAO) vom 30. November 2020 betreffend Wiederaufnahme der Verfahren  Einkommensteuer 2014 und 2015 gemäß § 303 BAO sowie betreffend Einkommensteuer 2014  und 2015 (Steuernummer 35-947/5347 ) nach Durchführung einer mündlichen  Verhandlung am 21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Sacha  Katzensteiner` — partial — pred is substring of gold: `Sacha  Katzensteiner Blauensteiner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Mag. Monika Ahorn`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dipl. Ing.  Thomas Hrdinka`(person)
- `Clarissa Maak`(person)
- `Haidenweg 21, 5321 Koppl, Österreich`(address)
- `Sacha  Katzensteiner Blauensteiner Rechtsanwälte GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `35-947/5347`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/144891.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144891.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde von Istvan  Meesmann,Drabunaschach 37, 4672 Krottendorf, Österreich, vertreten durch Steuerberater Mag. András Radics, Obere Hauptstraße 18- 20/Top 6, 7100 Neusiedl am See, vom 12.6.2024 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag vom 27.11.2023 auf  Familienbeihilfe (Steuernummer 91-528/1192) den Beschluss:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art 133 Abs 4 B-VG nicht zulässig.

**False Positives:**

- `Steuerberater Mag` — positional overlap with gold: `Mag. András Radics`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Maria Daniel`(person)
- `Istvan  Meesmann`(person)
- `Drabunaschach 37, 4672 Krottendorf, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Österreich`(organisation)
- `91-528/1192`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/145272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145272.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Melanie Czieselski, Obergiem 48, 8454 Remschnigg, Österreich, vertreten durch Rechtsanwälte Estermann &  Partner OG, Stadtplatz 6, 5230 Mattighofen, betreffend Beschwerde vom 24. September 2020  und 28. September 2020 gegen die Bescheide des Finanzamtes Österreich vom 24. August  2020 und vom 25. August 2020 betreffend Einkommensteuer 2013, 2016 und 2017,  Steuernummer 38-523/1139, beschlossen:  I. Die Beschwerdevorentscheidungen betreffend Einkommensteuer 2013, 2016 und  2017 vom 12.11.2020 werden wegen Rechtswidrigkeit aufgehoben.

**False Positives:**

- `Rechtsanwälte Estermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Melanie Czieselski`(person)
- `Obergiem 48, 8454 Remschnigg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `38-523/1139`(tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/145612.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145612.1_259`)


Dazu kommt noch die Klarstellung durch Senatspräsident Zorn: „Neben der Fläche, auf welcher  das Gebäude errichtet ist, erfasst die Befreiung so viel an das Gebäude umgebender Fläche, als  üblicherweise (nach der Verkehrsauffassung, wohl unter Einbeziehung der örtlichen  Bauvorschriften) als Bauplatz erforderlich ist.

**False Positives:**

- `Senatspräsident Zorn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/146640.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die VorsitzendeRi_1, die beisitzende Richterin Ri_2 und die  fachkundigen Laienrichterinnen Ri_3 und Ri_4 in der Beschwerdesache der Dontalcon-Getränke, Im Urtel 11, 9871 Pirk, Österreich, vertreten durch Hadaier Wirtschaftsprüfungs- und Steuerberatungs-GmbH,  Keplerstraße 1, 4910 Ried im Innkreis, über die Beschwerde vom 13. September 2023 gegen  den Bescheid des FA Salzburg-Land  vom 24. August 2023 über die Abweisung eines Antrages auf  Freigabe einer Fahrzeugidentifikationsnummer in der Genehmigungsdatenbank und über die  Beschwerde vom 12. Oktober 2023 gegen den Bescheid des FA Salzburg-Land  vom 2. Oktober 2023  über die Festsetzung der Normverbrauchsabgabe für den Zeitraum 01/2023 zu Steuernummer  73-990/7390  nach Durchführung einer mündlichen Verhandlung am 19. Dezember 2024 G  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Abweisung eines Antrages auf  Freigabe einer Fahrzeugidentifikationsnummer in der Genehmigungsdatenbank  wird als unbegründet abgewiesen.

**False Positives:**

- `Hadaier Wirtschaftsprüfungs` — partial — pred is substring of gold: `Hadaier Wirtschaftsprüfungs- und Steuerberatungs-GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dontalcon-Getränke`(organisation)
- `Im Urtel 11, 9871 Pirk, Österreich`(address)
- `Hadaier Wirtschaftsprüfungs- und Steuerberatungs-GmbH`(organisation)
- `FA Salzburg-Land`(organisation)
- `FA Salzburg-Land`(organisation)
- `73-990/7390`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/146673.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146673.1_3`)


Begründung  Mit Bescheid des Magistrates der Stadt Wien, Magistratsabteilung 6, vom 26. September  2024, Hauptzahl: MBA/220000033975/2022, wurde der Antrag der beschwerdeführenden  Partei Stephan Hirschfeld, MSc  vom 21. August 2024 auf Bewilligung eines Zahlungsaufschubes gemäß § 54  Abs 3 Verwaltungsstrafgesetz 1991 (VStG) abgewiesen.

**False Positives:**

- `Stephan Hirschfeld` — partial — pred is substring of gold: `Stephan Hirschfeld, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 6`(organisation)
- `Stephan Hirschfeld, MSc`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/148033.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148033.1_5`)


Den Gewinn des Gewerbebetriebes ermittelte der Bf. durch Betriebsvermögensvergleich   Mit Bescheiden  - vom 11. Oktober 2010 für das Abgabenjahr 2009 (BFG-Akt AS 9),  - vom 10. November 2011 für das Abgabenjahr 2010 (BFG-Akt AS 11),  - vom 14. Mai 2012 für das Abgabenjahr 2011 (BFG-Akt AS 13),  - vom 3. Juni 2014 für das Abgabenjahr 2012 (BFG-Akt AS 15) und   - vom 27. April 2015 für das Abgabenjahr 2013 (BFG-Akt AS 17)  wurde der Bf. erklärungsgemäß – unter Berücksichtigung einer beantragten  Teilwertabschreibung bei der Ermittlung der Einkünfte aus Gewerbebetrieb – zur  Einkommensteuer veranlagt.

**False Positives:**

- `Betriebsvermögensvergleich   Mit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)
- `BFG`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/148329.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148329.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Marilyn Bestel  in der Beschwerdesache Chantal Harpointner,  Nazhüttl 56, 4400 Tinsting, Österreich, vertreten durch Raiffeisenverband Steiermark, Raiffeisen-Platz 11, 8074  Raaba-Grambach, über die Beschwerde vom 15. November 2018 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. Oktober 2018 betreffend Berichtigung §§ 293 ff BAO 2012,  Steuernummer 83-205/8553  zu Recht erkannt:    I. Der angefochtene Bescheid wird gem. dem VwGH-Erkenntnis Ra 2023/15/0112-8  abgeändert.

**False Positives:**

- `Raiffeisenverband Steiermark` — type mismatch — same span as gold: `Raiffeisenverband Steiermark`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Marilyn Bestel`(person)
- `Chantal Harpointner`(person)
- `Nazhüttl 56, 4400 Tinsting, Österreich`(address)
- `Raiffeisenverband Steiermark`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `83-205/8553`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/148936.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148936.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mirko Boeshenz  in der Beschwerdesache KommR Manuel Ruppoldt,  Hauptschulweg 5, 8563 Oberwald, Österreich, vertreten durch Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG, Karl-Emminger-Straße 23, 5020 Salzburg, über die Beschwerde vom 27. Juni 2022  gegen den Bescheid des Finanzamtes Österreich vom 19. Mai 2022 betreffend  Einkommensteuer 2020 Steuernummer 90-698/6357  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Höllermeier Schaller` — partial — pred is substring of gold: `Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Mirko Boeshenz`(person)
- `KommR Manuel Ruppoldt`(person)
- `Hauptschulweg 5, 8563 Oberwald, Österreich`(address)
- `Höllermeier Schaller & Partner Steuerberatung Salzburg GmbH  & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `90-698/6357`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/149029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149029.1_86`)


§ 43 Abs. 2a Z 1 StVO 1960 normiert:  „Um Erschwernisse für die Wohnbevölkerung auszugleichen, die durch  Verkehrsbeschränkungen hervorgerufen werden, kann die Behörde durch Verordnung Gebiete  bestimmen, deren Bewohner die Erteilung einer Ausnahmegenehmigung für ein zeitlich  uneingeschränktes Parken in - in der Verordnung zu bezeichnenden - nahegelegenen  Kurzparkzonen mit Kraftfahrzeugen mit einem höchsten zulässigen Gesamtgewicht von nicht  mehr als 3 500 kg gemäß § 45 Abs. 4 beantragen können.“

**False Positives:**

- `Verordnung Gebiete` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Verena Khalidi  in der Beschwerdesache MedR Fiona Davydova,  St.-Anna-Park 16i, 5274 Unterhartberg, Österreich, vertreten durch Liepert Greussing Sturm Steuerberatung GmbH & Co KG,  Mühlgasse 21, 6700 Bludenz, über die Beschwerde vom 2. Februar 2018 gegen den Bescheid  des FA Baden Mödling  vom 10. Jänner 2018 betreffend Haftungs- und Abgabenbescheid 2016  Steuernummer 96-418/3627  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung  teilweise Folge gegeben.

**False Positives:**

- `Liepert Greussing` — partial — pred is substring of gold: `Liepert Greussing Sturm Steuerberatung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Verena Khalidi`(person)
- `MedR Fiona Davydova`(person)
- `St.-Anna-Park 16i, 5274 Unterhartberg, Österreich`(address)
- `Liepert Greussing Sturm Steuerberatung GmbH & Co KG`(organisation)
- `FA Baden Mödling`(organisation)
- `96-418/3627`(tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/149793.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Huberta Sideri  in der Beschwerdesache Evelyn Kowall,  Engfeld 6, 4083 Sieberstal, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 68-217/0896  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anwälte Mandl` — positional overlap with gold: `Mandl & Mitterbauer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Huberta Sideri`(person)
- `Evelyn Kowall`(person)
- `Engfeld 6, 4083 Sieberstal, Österreich`(address)
- `Mandl & Mitterbauer GmbH`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `68-217/0896`(tax_number)

</details>

---

## `verb_context_name` 🏆

**F1:** 0.005 | **Precision:** 0.136 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `78d8dfa8`  
**Description:**
Captures names following verbs like 'ist', 'wurde', 'lebte' which often precede person names in legal texts, specifically for cases like 'lebte mit Ernst Schoenekaess'. Excludes common professions and abstract nouns.

**Content:**
```
(?:lebte\s+mit\s+|heiratete\s+die\s+|heiratete\s+den\s+|wurde\s+|ist\s+|konnte\s+|sollte\s+)([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)+)\b(?![a-z])(?!\s*(?:Rechtsanwälte|Anwälte|Partnerschaft|GmbH|AG|KG|Gesellschaft|Firma|Unternehmen|Bildung|Dienstleistungen|Versicherung|Bank|Konto|Kredit|Darlehen|Hypothek|Steuer|Finanz|Gericht|Kammer|Behörde|Amt|Ministerium|Bundes|Land|Stadt|Gemeinde|Ort|Bezirk|Kreis|Region|Lage|Position|Stelle|Job|Beruf|Tätigkeit|Funktion|Rolle|Aufgabe|Pflicht|Recht|Anspruch|Klage|Klagegrund|Klageantrag|Klagebegründung|Klageerwiderung|Klageantwort|Klageerhebung|Klageverhandlung|Klageentscheidung|Klageurteil|Klagebeschluss|Klageverfahren|Klagekosten|Klagegebühr|Klagefrist|Klageverjährung|Klageverwirkung|Klageverzicht|Revisionsgericht|Berufungsgericht|Oberste|Gerichtshof|Senatspräsidentin|Vizepräsident|Vizepräsidentin|Rekursgericht|Kontaktrecht|Dr\.\s+|Mag\.\s+|Prof\.\s+|Univ\.\s+|Hon\.\s+|MMag\.\s+|DI\.\s+|Ing\.\s+|Bakk\.\s+|PhD\.\s+|HR\.\s+|Techn\.\s+|Dipl\.\s+|PD\.\s+|Priv\.\s+|KommR\.\s+|ÖkR\.\s+|RgR\.\s+|StR\.\s+|MedR\.\s+|KzlR\.\s+|OMedR\.\s+|VetR\.\s+|AR\.\s+|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+|Jugendhilfeträger|Mutter|Vater|Eltern|Kind|Sohn|Tochter|Gewährung|Unterhaltsvorschuss|Strafsachen|Zivilrechtssachen|Maurer|Schalungsbauer|Anzahl|Verbrechen|Missbrauchs|Unmündigen|Geborenen|Schuld|Tatzeitraum|Verfahren|Nichtigkeitsb))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.136 | 0.003 | 0.005 | 44 | 6 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 38 | 2288 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_10`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung, vom 28. September 2020, Zahl MA67/Zahl/2020, wurde Istvan  Sicking,  Fanny Elßler-Gasse 30, 9375 Zosen, Österreich (in weiterer Folge: Bf.) vorgeworfen, am 22.06.2020 um 19:47 Uhr in einer  gebührenpflichtigen Kurzparkzone in 1020 Wien, Machstraße 8, mit dem mehrspurigen  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) folgende Verwaltungsübertretung  begangen zu haben:  Abstellen des Fahrzeuges, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Istvan  Sicking` | `Istvan  Sicking` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien` (organisation)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich` (address)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_8`)


In der Folge wurde Gundula Doerfner  vom Magistrat der Stadt Wien, MA 67, mit Strafverfügung vom  23. April 2021 angelastet, dass er das in Rede stehende Fahrzeug an der bereits genannten  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Gundula Doerfner` | `Gundula Doerfner` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_13`)


Mit Straferkenntnis vom 7. Mai 2021 wurde Gundula Doerfner  vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig befunden und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 140,00 und für den Fall der Un- einbringlichkeit 1 Tag und 9 Stunden Ersatzfreiheitsstrafe festgesetzt.

| Predicted | Gold |
|---|---|
| `Gundula Doerfner` | `Gundula Doerfner` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_124`)


Der Deckungsumfang ist Simon Zieselsberger  mittels Versicherungspolizze  nachzuweisen.

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_127`)


Im Fall der nicht  ordnungsgemäßen Einhaltung dieser Verpflichtungen ist Simon Zieselsberger  berechtigt, ihr zustehende  Rechte wie z.B. Kennzeicheneinzug auszuüben.“

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_16`)


Entscheidungsgründe  I. Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020, wurde Brunhild Stanislav (in weiterer Folge:  Beschuldigter) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im April 2020 vor  der Liegenschaft in Erlebnisweg 684, 6943 Riefensberg, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 42,50 m² und ein Gerüst im  Ausmaß von 13,60 m², somit im Gesamtausmaß von 56,10 m² genutzt, wobei er hiefür bis zum  12.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe entrichtet  habe.

| Predicted | Gold |
|---|---|
| `Brunhild Stanislav` | `Brunhild Stanislav` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `KI Synlogtra GmbH` (organisation)
- `Erlebnisweg 684, 6943 Riefensberg, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_4`)


Laut Firmenbuchauszug ist Herr Jeskin Geschäftsführer seit 23.7.2009.

**False Positives:**

- `Herr Jeskin Geschäftsführer` — partial — gold is substring of pred: `Jeskin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeskin`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_49`)


Im Firmenbuch ist Herr Jeskin als Geschäftsführer seit x.2009 eingetragen.

**False Positives:**

- `Herr Jeskin` — partial — gold is substring of pred: `Jeskin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeskin`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_62`)


Anspruch auf Familienbeihilfe, noch auf den Erhöhungsbetrag zur Familienbeihilfe wegen  erheblichen Behinderung zu.   Laut amtsärztlichen Sachverständigengutachten vom 3.12.2019 wurde Ihr Behinderungsgrad  im Ausmaß von 80 v.H. ab dem Monat Jänner 1987 und Ihr Unvermögen sich den Unterhalt  selbst zu verschaffen ab dem Monat Jänner 1987, also nach Vollendung Ihres 21.

**False Positives:**

- `Ihr Behinderungsgrad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_124`)


Das Gutachten des Sozialministeriumservice ist Ihrer Meinung nach nicht in sich schlüssig.

**False Positives:**

- `Ihrer Meinung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_148`)


Im gegenständlichen Fall wurde Ihr Unvermögen sich den Unterhalt selbst zu verschaffen, nach  Vollendung Ihres 21.

**False Positives:**

- `Ihr Unvermögen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_20`)


Dahingehend konnte Ihrer Beschwerde nicht entsprochen werden.

**False Positives:**

- `Ihrer Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_37`)


Welche Tätigkeit üben Sie in Österreich aus ? Wer ist Ihr Arbeitgeber ? Welche Arbeitszeiten  2 von 14 Seite 3 von 14

**False Positives:**

- `Ihr Arbeitgeber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_116`)


Nach ihrer Pensionierung ist Frau Merbot von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

**False Positives:**

- `Frau Merbot` — partial — gold is substring of pred: `Merbot`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Merbot`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. Oktober  2020, Zahl: MA67/206700566984/2020, wurde Herr Univ.-Prof.in StR Caroline Akkoca, MBA (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Herr Univ` — positional overlap with gold: `Univ.-Prof.in StR Caroline Akkoca, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_24`)


Mit Bescheid vom 22.07.2019 wurde Ihr Antrag auf Familienbeihilfe ab August 2018  abgewiesen.

**False Positives:**

- `Ihr Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_44`)


Die überwiegende Kostentragung wurde nicht nachgewiesen, daher wurde Ihr  Antrag auf Wiederaufnahme mit Bescheid vom 16.09.2020 abgewiesen.

**False Positives:**

- `Ihr  Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_57`)


Anschließend ist Herr  Mag. R ein neues Dienstverhältnis in der Schweiz eingegangen und mit der Familie von den USA  in die Schweiz übersiedelt. Die Verlagerung des Lebensmittelpunktes in den Entsendestaat sei  ergänzend an Hand der (Vermutungs-)Regel gemäß Rz 7596 EStR zu beurteilen.

**False Positives:**

- `Herr  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_102`)


Grundsätzlich sind gewisse Gegebenheiten zu bemängeln, aber es ist Herrn Oeverhaus in keiner Weise eine verdeckte Gewinnausschüttung an zu lasten.

**False Positives:**

- `Herrn Oeverhaus` — partial — gold is substring of pred: `Oeverhaus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oeverhaus`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_5`)


Alleingesellschafterin und Geschäftsführerin ist Frau Wahl   1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (kurz: Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Bf ist eine GmbH deren alleinige Gesellschafterin Frau Wahl ist.

**False Positives:**

- `Frau Wahl` — partial — gold is substring of pred: `Wahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wahl`(person)
- `Wahl`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_75`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Wahl   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Frau Wahl   Gegenstand` — partial — gold is substring of pred: `Wahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wahl`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Waldviertel als Finanzstrafbehörde vom 21. November 2019, SpS 19,  Strafnummer 2018, wurde Frau Valerian Unterfranz, geboren am 13. Juli 1971, wohnhaft in Schanzplatz 130, 3664 Hundsbach, Österreich  schuldig erkannt, sie habe im Bereich des Finanzamtes Waldviertel   A.) durch Abgabe unrichtige Umsatz- und Einkommensteuererklärungen für die Jahre 2010 bis  2016, sohin unter Verletzung einer Wahrheits- und Offenlegungspﬂicht gemäß § 119 BAO  vorsätzlich bewirkt, dass   Umsatzsteuer für 2012 in Höhe von € 2.614,430, für 2013 in Höhe von € 2.981,49, für 2014 in  Höhe von € 3.307,05, für 2015 in Höhe von € 3.395,74, für 2016 in Höhe von € 3.430,78,   Einkommensteuer für 2010 in Höhe von € 1.446,00, für 2011 in Höhe von € 1.712,00, für 2012  in Höhe von € 4.691,00, für 2013 in Höhe von € 5.037,00, für 2014 in Höhe von € 5.599,00, für  2015 in Höhe von € 7.530,00 (€ 41.744,49)  verkürzt worden sei, und   B) vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes entsprechenden Voranmeldungen eine Verkürzung von  Vorauszahlungen an Umsatzsteuer für 01-09/2017 in der Höhe von € 2.605,11 bewirkt und dies  nicht nur für möglich, sondern für gewiss gehalten.

**False Positives:**

- `Frau Valerian Unterfranz` — partial — gold is substring of pred: `Valerian Unterfranz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Valerian Unterfranz`(person)
- `Schanzplatz 130, 3664 Hundsbach, Österreich`(address)
- `Finanzamtes Waldviertel`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_32`)


Begründung  Mit Erkenntnis vom 21.11.2019 wurde Frau Valerian Unterfranz  wegen Finanzvergehen gemäß § 33 Abs  1 FinStrG und § 33 Abs 2 lit a FinStrG zu einer Geldstrafe von € 8.800 verurteilt.  Strafbemessungsbasis waren – neben nichterklärten Einkünften aus Vermietung und  Verpachtung – Sicherheitszuschläge, welche die Außenprüfung den Einkünften aus  Gewerbebetrieb bzw. den Umsätzen hinzugerechnet hat.

**False Positives:**

- `Frau Valerian Unterfranz` — partial — gold is substring of pred: `Valerian Unterfranz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerian Unterfranz`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_6`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. Firmenbuch-  und Grundbuchdaten ergibt sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung  als erwiesen zu Grunde legt:  Adressat der angefochtenen Erledigung ist Herr Ronald Jundt (nachfolgend Herr M.), der  aufgrund eines Kaufvertrages vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel  Miteigentümer jener Liegenschaft war, auf welcher der strittige Rohbau errichtet wurde  (Lageadresse: R-Gasse 15, 9999 Wien).

**False Positives:**

- `Herr Ronald Jundt` — partial — gold is substring of pred: `Ronald Jundt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamtes`(organisation)
- `BFG`(organisation)
- `Ronald Jundt`(person)
- `M.`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

**False Positives:**

- `Herr Ronald Jundt` — partial — gold is substring of pred: `Ronald Jundt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnex-Versand GmbH`(organisation)
- `Ronald Jundt`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_6`)


Abgabe Frist Betrag Säumniszuschlag  Anspruchszinsen  2011  22.6.2018 6.419,16 128,38  Umsatzsteuer 2011 15.2.2012 28.439,73 568,79  Umsatzsteuer 2013 17.2.2014 13.343,44 266,89  Summe 964,04  Mit einem mit 16.9.2019 datierten Schreiben, das dem Finanzamt aber bereits am 12.9.2019  per Fax übermittelt worden war, erhob der Bf durch seine anwaltliche Vertretung Beschwerde  gegen die festgesetzten Säumniszuschläge und beantragte, die angefochtenen Bescheide  aufzuheben.

**False Positives:**

- `Betrag Säumniszuschlag  Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135431.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135431.1_3`)


Entscheidungsgründe  Sachverhalt:    1) Bescheid vom 11.3.2019 über die Festsetzung von ersten Säumniszuschlägen:  Mit Bescheid vom 11.3.2019 wurden gegenüber dem Beschwerdeführer (Bf) nachstehende  erste Säumniszuschläge festgesetzt, weil er die angeführten Abgabenschulden nicht innerhalb  nachstehender Fristen entrichtet hatte:  Abgabe Frist Betrag Säumniszuschlag  Umsatzsteuer 2013 17.2.2014 37.501,16 750,02  1 von 14 Seite 2 von 14

**False Positives:**

- `Betrag Säumniszuschlag  Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/135629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135629.1_26`)


Bereits am 7.Juli 2017 unterfertigte der Bf einen unbefristeten Arbeitsvertrag mit der Fa XY - Interational, aufgrund dessen er ab Mitte August 2017 in CH-Ort-1/Schweiz als „Spezialist  Sensor Optics“ tätig war (Vollzeitdienstnehmer im Schichtbetrieb, bei Bedarf 3-Schichtdienst  incl.

**False Positives:**

- `Sensor Optics` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_50`)


4. In dem dagegen fristgerecht eingebrachten Vorlageantrag vom 01.04.2020 wurde zunächst  auf die beiden Beschwerden verwiesen und weiter vorgebracht:  „Frau Priv.-Doz.in Laetitia Pöstges  ist Schweizer Staatsbürgerin.

**False Positives:**

- `Schweizer Staatsbürgerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_91`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf. ist Schweizer Staatsbürgerin, hatte im Streitjahr 2019 in der Schweiz in ihrem  Elternhaus in Ort1 (CH)-Adr1 gemeinsam mit ihrer Mutter einen Wohnsitz und war im Jahr  2019 in der Schweiz als Lehrerin beschäftigt.

**False Positives:**

- `Schweizer Staatsbürgerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/138273.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138273.1_21`)


Da von der Kindsmutter ebenfalls der Familienbonus Plus für Ihren Sohn, geb.yyy  beantragt wurde, konnte Ihr Antrag auf den Familienbonus Plus nur zur Hälfte berücksichtigt  werden.

**False Positives:**

- `Ihr Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/139204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139204.1_31`)


Jene Familien, die dem Finanzamt Änderungen bekannt gegeben haben und bei  denen die Familienbeihilfe gestoppt wurde, bekamen die Familienbeihilfe nachträglich  ausgezahlt.  In diesen Fällen ist Ende Juli 2021 eine Nachzahlung der entsprechenden Familienbeihilfe- beträge durch das Finanzamt erfolgt.

**False Positives:**

- `Ende Juli` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamt`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_37`)


II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020, wurde Herr Brunhild Stanislav, (in weiterer Folge: Beschuldigter) als  handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  mit Sitz in Altfinkensteiner Weg 15, 9065 Moosberg, Österreich,  schuldig erkannt,   1. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juni 2020 vor  der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür  bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

**False Positives:**

- `Herr Brunhild Stanislav` — partial — gold is substring of pred: `Brunhild Stanislav`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Brunhild Stanislav`(person)
- `KI Synlogtra GmbH`(organisation)
- `Altfinkensteiner Weg 15, 9065 Moosberg, Österreich`(address)
- `KI Synlogtra GmbH`(organisation)
- `An der Welserbahn 27, 3763 Sabatenreith, Österreich`(address)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/140794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140794.1_4`)


Begründung  Beschwerdeführer (Bf) ist Herr Paolo Ofzareck.

**False Positives:**

- `Herr Paolo Ofzareck` — partial — gold is substring of pred: `Paolo Ofzareck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Paolo Ofzareck`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_31`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. den  finanzgerichtlichen Datenbankrecherchen (Abgabenbehörde, Firmenbuch, Grundbuch) ergibt  sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung als erwiesen zu Grunde legt:  1. Adressat der angefochtenen Erledigung ist Wilhelm Fißenewert, LLM (Bf), der aufgrund eines Kaufvertrages  vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel Miteigentümer jener Liegenschaft  war, auf welcher der strittige Rohbau errichtet wurde (Lageadresse: 9999 R-Gasse 99,  nachfolgend R-Gasse).

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamtes`(organisation)
- `BFG`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_138`)


Die von der Firma Hemken Automotive GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Wilhelm Fißenewert, LLM  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.“  (Zitatende/Beschwerde)  10.

**False Positives:**

- `Herr Wilhelm Fißenewert` — positional overlap with gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hemken Automotive GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_198`)


2. Im Haftungsbescheid und auch in der Beschwerdevorentscheidung ist Herr Erika Puttfarken, der  nunmehrige Beschwerdeführer, genannt.

**False Positives:**

- `Herr Erika Puttfarken` — partial — gold is substring of pred: `Erika Puttfarken`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Erika Puttfarken`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_3`)


Begründung  Mit Bescheid des Finanzamtes Österreich vom 21.10.2021 wurde Herr Ilhan Drommelschmidt, geboren am  2. September 2011, gemäß § 26 Abs 1 Familienlastenausgleichsgesetz 1967 (nachfolgend „FLAG  1967“) in Verbindung mit § 33 Abs 3 EStG 1988 aufgefordert, die für ihn selbst bezogene  Familienbeihilfe sowie die Kinderabsetzbeträge für den Zeitraum Oktober 2018 bis März 2021  zurückzuzahlen.

**False Positives:**

- `Herr Ilhan Drommelschmidt` — partial — gold is substring of pred: `Ilhan Drommelschmidt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Österreich`(organisation)
- `Ilhan Drommelschmidt`(person)
- `2. September 2011`(date)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/144555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144555.1_5`)


Zum Grund der Befundaufnahme wurde noch ausgeführt, der Bf sei mit Schreiben des LVwG  vom 3.9.2020 darauf hingewiesen worden, dass gem. § 24a Z 1 VwGG die Eingabengebühr von  € 240 zu entrichten und dem LVwG der diesbezügliche Einzahlungsbeleg zu übermitteln sei,  und weiter: "Dieser Aufforderung ist Herr Vivian Hartmann  nicht nachgekommen."

**False Positives:**

- `Herr Vivian Hartmann` — partial — gold is substring of pred: `Vivian Hartmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vivian Hartmann`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_6`)


Laut Ihren Schreiben ist Ihre Tochter bei den  Großeltern haushaltzugehörig.

**False Positives:**

- `Ihre Tochter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_23`)


Laut Ihrem  Schreiben ist Ihre Tochter bei den Großeltern haushaltzugehörig.

**False Positives:**

- `Ihre Tochter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/148971.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148971.1_75`)


des Behindertenausweises ist Herr Ausweisinhaber.

**False Positives:**

- `Herr Ausweisinhaber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_53`)


Geschäftsführer ist Hc Kb. Gesellschafter der Bf. sind zu je 50 % Herr T Kb und  Frau H Kb.

**False Positives:**

- `Hc Kb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/149834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149834.1_30`)


• Veranstaltungszentrum   Die Scheune – ein eigenes Gebäude (110m²) - sollte It Planung der Bf als  Veranstaltungszentrum Verwendung finden, wie ua für Feuerwehrfeste, Hochzeiten,  Adventmärkte, Flohmärkte, usw.

**False Positives:**

- `It Planung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `title_first_name_only` 🏆

**F1:** 0.007 | **Precision:** 0.119 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `6622ca3e`  
**Description:**
Matches titles followed by a single capitalized word (e.g., 'Dr. Heinrich') or hyphenated names. Fixed to prevent trailing whitespace.

**Content:**
```
(?<![A-Za-z])(?:Hon\.-?Prof\.|Univ\.-?Prof\.|Prof\.|Dr\.|Mag\.|MMag\.|DI\.|Ing\.|Bakk\.\s+iur\.|PhD\.|HR\s+Ing\.|Techn\s+|Dipl\.-?HTL\-?Ing\.|PD\s+Dr\.|Priv\.-?Doz\.|DDr\.|KommR\s+|ÖkR\s+|RgR\s+|StR\s+|MedR\s+|HR\s+|KzlR\s+|OMedR\s+|VetR\s+|AR\s+|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+)(?:\s+Dr\.)?\s+[A-Z][a-zäöüßéèêëïîôùûü]+(?:-[A-Z][a-zäöüßéèêëïîôùûü]+)*\b(?![a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.119 | 0.003 | 0.007 | 67 | 8 | 59 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 8 | 59 | 2333 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Schmid` | `Dr. Schmid` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Dr. Alexander Nahler` (person)
- `Ljiljana Kos` (person)
- `Klinik Favoriten` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Amtsvertr` | `Dr. Amtsvertr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claudia Noeltge` (person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich` (address)
- `Finanzamtes Spittal Villach` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

| Predicted | Gold |
|---|---|
| `Mag. Artner-Tauscher` | `Mag. Artner-Tauscher` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr. Padesse` | `Dr. Padesse` |

**Missed by this rule (FN):**

- `Dr.  Tadesse Bedasa` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_40`)


Der Streitpunkt   „Tz 5 PB Pensionsversicherung - Rückstellung und Aktivierung“ wurde aufgrund des Verzichts  des steuerlichen Vertreters der Fytterer Handel GmbH (und der Bf.) auf die Korrektur der Rückstellung  aus verwaltungsökologischen Gründen außer Streit gestellt. Bezüglich der Umsatzsteuer für die  Jahre 2011 bis 2013 verständigten sich die Amtsvertretung und Mag. Haderer als Steuerberater  der Fytterer Handel GmbH auf die Festsetzung der Umsatzsteuer für die Jahre 2011 bis 2013 wie vor der  Betriebsprüfung.

| Predicted | Gold |
|---|---|
| `Mag. Haderer` | `Mag. Haderer` |

**Missed by this rule (FN):**

- `Fytterer Handel GmbH` (organisation)
- `Fytterer Handel GmbH` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Ing. Dipl` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Mag. Susanne Haim`(person)
- `Leopold Pichlbauer`(person)
- `Dr.  Karl Penninger`(person)
- `Ing. Dipl.-Ing. Brunhild Fleischfresser`(person)
- `Margaretengürtel 23, 4092 Pyrawang, Österreich`(address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH`(organisation)
- `Finanzamtes`(organisation)
- `Tanja Grottenthaler`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_17`)


Darüber hinaus werden die dem Erwachsenenvertreter vorliegenden psychiatrischen  Gutachten vorgelegt, aus diesen ist ersichtlich, dass bei (der Bf.) eine angeborene Oligophrenie  vorliegt (Psychiatrisches Gutachten Univ.Prof. Dr.med. F. St. vom 28.04.1987), ebenso wie die  Sachverständige Charles Hegler von einer angeborenen Minderbegabung ausgeht, mit später  aufgetretenen psychotischen und schizophrenen Symptomen.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Charles Hegler`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_19`)


Beweis: beiliegendes Gutachten Univ.Prof. Dr.med.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_20`)


F. St. vom 28.04.1987,                  beiliegendes Gutachten Univ.Prof. Dr.med.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_77`)


Wie aus dem Gutachten Prof. Univ.Doz. Dr.med Dipl.-Ing. Kirsten Hüffner  vom 28.04.1987, Seite 6, ersichtlich,  sind schizophreniforme Psychosen bei Oligophrenie sehr schwer und oft gar nicht deutbar.

**False Positives:**

- `Prof. Univ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_114`)


2. Beweiswürdigung  Diese Feststellungen beruhen auf dem Akteninhalt, insb. auf dem Inhalt der Gutachten  (Univ.Prof. Dr.med. F. St.), und sind unstrittig.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über den Antrag  der Antonia Piekorz, LLB Bakk. phil., Aubrunnerweg 10d, 9150 Rinkenberg, Österreich  vom 23. März 2020 auf Gewährung der Verfahrenshilfe für das  Beschwerdeverfahren gegen den Bescheid der belangten Behörde Finanzamt Bruck Eisenstadt  Oberwart vom 28. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 beschlossen:  Der Antragstellerin wird gemäß § 292 BAO Verfahrenshilfe bewilligt.

**False Positives:**

- `Dr. Maria-Luise` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Antonia Piekorz, LLB Bakk. phil.`(person)
- `Aubrunnerweg 10d, 9150 Rinkenberg, Österreich`(address)
- `Finanzamt Bruck Eisenstadt  Oberwart`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_63`)


NachnameGeser1 und dessen Steuerberater Mag. Stb bekannte Hr.  NachnameGeser1 zunächst, dass die [Bf.] über keinen Autoabstellplatz verfüge.

**False Positives:**

- `Mag. Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_74`)


Auch in der Schlussbesprechung vom 24.05.2016  wurde von Hrn. NachnameGeser1 in Anwesenheit seines Steuerberaters, Mag. Stb, behauptet,  er hätte einen potentiellen Käufer, der das Kfz in ca. zwei Wochen eventuell um ca. 300.000,-  Euro kaufen wolle, konkrete Angaben dazu wollte Hr. NachnameGeser1 aber nicht machen.

**False Positives:**

- `Mag. Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_76`)


Am 13.06.2016 erklärte dann der Steuerberater Mag. Stb, der Verkauf sei nicht zustande  gekommen, sodass Hr. NachnameGeser1 beabsichtige, das Kfz aus dem Betrieb um einen  gegenüber den Anschaffungskosten geringeren Preis zu entnehmen.

**False Positives:**

- `Mag. Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Oleg Bösehans  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 80-404/4147, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Axel-Hans` — partial — pred is substring of gold: `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Oleg Bösehans`(person)
- `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `80-404/4147`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_631`)


3. Daraufhin erließ das Bundesfinanzgericht im fortgesetzten Verfahren ein neuerlich  stattgebendes Erkenntnis, das damit begründet wurde, dass hinsichtlich der  Weisungsgebundenheit von HR Dr. Emberger unterschieden werde zwischen angestellten  Ärzten - die auch fachlich weisungsgebunden sind, wobei eine verstärkte Einspruchspflicht bei  fachlich umstrittenen Weisungen bestehe (Stärker im Ärztegesetz mit Kommentar, § 3 Fußnote  7 und Emberger § 49 Fußnote 6 Z. 1.2.2) und nicht angestellten Ärzten, also niedergelassenen  Ärzten oder Wohnsitzärzten und somit auch Vertretungsärzten.

**False Positives:**

- `Dr. Emberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134483.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Revisionssache Hannelore Schierstein, Am Tieberhof 11, 5142 Kleinschäding, Österreich, vertreten durch Dr. Christa-Maria Scheimpflug,  Erdberger Lände 6/27, 1030 Wien, über den Antrag des Revisionswerbers vom 06.09.2021, der  gegen das Erkenntnis des Bundesfinanzgerichtes vom 20.04.2021, RV/7104561/2018,  betreffend Umsatzsteuer 2006 bis 2010 und Einkommensteuer 2010 erhobenen  außerordentlichen Revision vom 06.09.2021 die aufschiebende Wirkung zuzuerkennen,  beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Dr. Christa-Maria` — partial — pred is substring of gold: `Dr. Christa-Maria Scheimpflug`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Hannelore Schierstein`(person)
- `Am Tieberhof 11, 5142 Kleinschäding, Österreich`(address)
- `Dr. Christa-Maria Scheimpflug`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_12`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf  Mag. Dr.iur.

**False Positives:**

- `Mag. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_45`)


Sachverständigengutachten der Fachärztin für Psychiatrie Yelec Seref vom 04.12.2020:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Stellungsuntersuchungsblätter 12.03.1965:  Angeborene Fehler oder Krankheiten: Schwachsinn  untauglich  Amtliche Anfrage Strafregister 28.08.1964  Dr. Feh… Psychiaterin 16.08.2004:  (Der Bf.) ist bei Bewusstsein und wach, er ist kontakt- und rapportfähig, die  Intelligenz ist an der unteren Normgrenze, Beschulung durch 8 Klassen Volksschule.

**False Positives:**

- `Dr. Feh` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Yelec Seref`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_101`)


Dem Bundesfinanzgericht liegen folgende ärztliche Sachverständigengutachten vor: ein  ärztliches Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen  vom 19.03.2020 erstellt von Frau Dr. Arzt, einer Fachärztin für Neurologie und Psychiatrie,  (hier: Erstgutachten) sowie – infolge der gegenständlichen Bescheidbeschwerde - eine  Gesamtbeurteilung nach der Einschätzverordnung des Bundesamtes für Soziales und  Behindertenwesen vom 28.12.2020 erstellt von Frau Dr. Arzt1, der ein psychiatrisches  Teilgutachten von Frau Dr. Arzt1 - sowie ein psychologisches Teilgutachten von Frau Dr. Arzt2  (beide Teilgutachten erstellt am 22.12.2020) zu Grunde liegt.

**False Positives:**

- `Dr. Arzt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesamtes für Soziales und Behindertenwesen`(organisation)
- `Bundesamtes für Soziales und  Behindertenwesen`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_102`)


Das letzte dem  Bundesfinanzgericht zur Verfügung stehende Sachverständigengutachten des Bundesamtes für  Soziales und Behindertenwesen stammt vom 09.09.2021/10.09.2021 und wurde wiederum  von Frau Dr. Arzt erstellt (hier: Letztgutachten).

**False Positives:**

- `Dr. Arzt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesamtes für  Soziales und Behindertenwesen`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_4`)


Dagegen wurde am 19.10.2020 Beschwerde erhoben und ausgeführt, dass in den Berichten  der Lebenshilfe vom 05.06.2014, des Hilfeplans der BH Hallein Abteilung Kinder- und  Jugendhilfe vom 03.04.2017, im Arztbericht des Dr. Flucher-Wolfram, Ambulatorium für  Entwicklungsdiagnostik, vom 01.03.2018 bzw. im Bericht des Dr. Alexander Holzknecht, KH  Schwarzach, vom 06.07.2020 für D. (und für seinen Bruder A.) die Verhaltensauffälligkeiten,  das Konzentrationsdefizit, die motorische Unruhe, die leichte Ablenkbarkeit, die verminderte  Aufmerksamkeit und das verminderte Durchhaltevermögen festgestellt wurden.

**False Positives:**

- `Dr. Flucher-Wolfram` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alexander Holzknecht`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/135592.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135592.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  ÖkR Dipl.-Ing. Dipl. Kfm. Raimund Teschmer, Liebigstraße 2, 4725 Kößlau, Österreich, vom 17. Dezember 2021, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 1. Dezember 2021, GZ.  MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parko- meterabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Ing. Dipl` — partial — pred is substring of gold: `ÖkR Dipl.-Ing. Dipl. Kfm. Raimund Teschmer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `ÖkR Dipl.-Ing. Dipl. Kfm. Raimund Teschmer`(person)
- `Liebigstraße 2, 4725 Kößlau, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_8`)


Ich ersuche Sie höflich,  den nun im Anhang nachgereichten Unterlagen von Frau Mag. M… (Klinische und  Gesundheitspsychologin, Hilfswerk NÖ) und Frau OA Dr. St… (FA für Kinder- und  Jugendheilkunde) zu entnehmen, dass der für den rückwirkenden Anspruch auf erhöhte  Familienbeihilfe erforderliche Behinderungsgrad von J… bereits zu einem früheren Zeitpunkt  belegbar ist.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_13`)


Im Anhang dieses Schreibens übermitteln wir folgende Unterlagen:   • Psychologischer Kurzbericht von Fr. Mag. M…   • Bestätigung über Psychologisch-diagnostische Abklärung 2017 u. 2019 von Fr. Mag. M…   • Ärztliche Bestätigung von Fr. OA Dr. St…   • 1.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_33`)


Auf Grund dieser war J… in weiterer Folge  bei OA Dr. St… (FA für Kinder- und Jugendheilkunde) in Behandlung.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_34`)


Im Anhang dieses Schreibens übermitteln wir nochmals folgende Unterlagen:   • Psychologischer Kurzbericht von Fr. Mag. M…   • Ärztliche Bestätigung von Fr. OA Dr. St…   Wir ersuchen insbesondere um Würdigung der beigebrachten Bestätigungen bezüglich der  vorhandenen Diagnose.

**False Positives:**

- `Dr. St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_38`)


Nach herrschender Literaturmeinung (zB Kommentar Dr. Karl-Werner Fellner zur  Grunderwerbsteuer) könnte ein gemeiner Wert eines Gebäudes in der Regel von einem  Bausachverständigen im Wege der Schätzung erfolgen.

**False Positives:**

- `Dr. Karl-Werner` — partial — pred is substring of gold: `Dr. Karl-Werner Fellner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl-Werner Fellner`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/139911.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  des Bettina Kroonen, Karnerviertel 22M, 4730 Grillparz, Österreich, vertreten durch Dr. Schuhmeister & Mag. Haydn GesbR, Bruck- Hainburger Straße 7, 2320 Schwechat, über die Beschwerde vom 8. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 9. September 2022, betreffend die Abweisung des  Antrages auf Erlassung eines Feststellungsbescheides gemäß § 92 BAO zum Nichtvorliegen der  unbeschränkten Steuerpflicht in Österreich ab dem Zeitraum 2016, Steuernummer  26-097/7496, zu Recht erkannt:     I. Der angefochtene Bescheid wird dahingehend abgeändert, sodass dessen Spruch nunmehr  wie folgt zu lauten hat:  "Der Antrag auf Erlassung eines Feststellungsbescheides gemäß § 92 BAO zum Nichtvorliegen  der unbeschränkten Steuerpflicht in Österreich ab dem Zeitraum 2016 wird zurückgewiesen."

**False Positives:**

- `Dr. Schuhmeister` — partial — pred is substring of gold: `Dr. Schuhmeister & Mag. Haydn GesbR`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Bettina Kroonen`(person)
- `Karnerviertel 22M, 4730 Grillparz, Österreich`(address)
- `Dr. Schuhmeister & Mag. Haydn GesbR`(organisation)
- `Finanzamtes Österreich`(organisation)
- `26-097/7496`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/140478.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140478.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mag. Mag. Clemens Meuwsen  in der Revisionssache Ali Litwinski,  Am Gallberg 8, 2561 Grillenberg, Österreich, vertreten durch Mag. Klaudius May, Franz-Josef-Straße 41, 5020 Salzburg, über  den Antrag des Revisionswerbers vom 6. April 2023, der gegen den Beschluss des  Bundesfinanzgerichtes vom 23. Februar 2023 (GZ RV/6100268/2021) erhobenen ordentlichen  Revision die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag auf Zuerkennung der aufschiebenden Wirkung  nicht stattgegeben.

**False Positives:**

- `Univ.-Prof. Mag` — partial — pred is substring of gold: `Univ.-Prof. Mag. Mag. Clemens Meuwsen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Mag. Mag. Clemens Meuwsen`(person)
- `Ali Litwinski`(person)
- `Am Gallberg 8, 2561 Grillenberg, Österreich`(address)
- `Mag. Klaudius May`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_23`)


Darin liegt der „negative Leistungsanreiz“, den Frau Prof. Kanduth-Kristen im  der ersten Beschwerde beigelegten Artikel meines Erachtens zurecht als verfassungsrechtlich  bedenklich kritisiert.

**False Positives:**

- `Prof. Kanduth-Kristen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_33`)


Ich hoffe,  meine weiteren Ausführungen veranlassen — zusammen mit dem bereits erwähnten Artikel  von Frau Prof. Kanduth-Kristen — das Gericht dazu, meine Zweifel an der  Verfassungsmäßigkeit der gegenständlichen Regelung zu teilen und wie angeregt deren  Aufhebung beim Verfassungsgerichtshof zu beantragen.

**False Positives:**

- `Prof. Kanduth-Kristen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_18`)


Herkömmliche konservative  Behandlungsmethoden hätten keine Besserung erzielt, weshalb der Bf Kontakt mit dem  Wirbelsäulenchirurg Dr. Clinic  (Anm. d. Ri.: Managing Director der die Behandlung  durchführenden Klinik) aufgenommen habe.

**False Positives:**

- `Dr. Clinic` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_166`)


In dem Herr Dr. Clinic den MRT-Bericht folgend eine medizinische Indikation folgert.

**False Positives:**

- `Dr. Clinic` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_189`)


Herr Dr. Röntgen (Anm. d. Ri.: der Münchner Arzt, bei  dem die upright-MRT gemacht wurde) teilte mir anschließend in einem Gespräch mit, dass es  zwei Möglichkeiten für mich gibt, 1.

**False Positives:**

- `Dr. Röntgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_192`)


Als 2. Variante hat mir Dr. Röntgen die Clinic-Stammzellentherapie ans  Herz gelegt.

**False Positives:**

- `Dr. Röntgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_194`)


Ich war bereits im Dezember 2014 bei Dr. Röntgen zur Aufnahme eines derartigen MRTs.

**False Positives:**

- `Dr. Röntgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_73`)


Seit 8/2013 besachwaltet (Dr. Bu…);

**False Positives:**

- `Dr. Bu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_96`)


Seit 8/2013 besachwaltet (Dr. Bu…);

**False Positives:**

- `Dr. Bu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_125`)


siehe auch VGA vom 05.09.2017 Intelligenzminderung, atypische Anorexie 50%   Derzeitige Beschwerden:   Keine Beschwerden   Behandlung(en) / Medikamente / Hilfsmittel:   Gesprächstherapie einmal in der Woche   Sozialanamnese:   ledig, keine Kinder, lebt alleine in der Wohnung der Großeltern, in einer Beziehung   Jugend am Werk Beschäftigungtherapie, davor Sonderschule   Seit 8/2013 besachwaltet (Dr. Bu…)   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   keine Befunde   Untersuchungsbefund:   Allgemeinzustand:   gut   Ernährungszustand:   gut   Größe: 162,00 cm Gewicht: 50,00 kg Blutdruck: -/-   Status (Kopf / Fußschema) - Fachstatus:   28 Jahre   Visus mit Brille   Thorax.

**False Positives:**

- `Dr. Bu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_137`)


Seit 8/2013 besachwaltet (Dr. Bu…)   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   keine   Untersuchungsbefund:   Allgemeinzustand:   gut   Ernährungszustand:   gut   Größe: 162,00 cm Gewicht: 50,00 kg Blutdruck: -/-   Status (Kopf / Fußschema) - Fachstatus:   29 Jahre   Visus mit Brille   Thorax.

**False Positives:**

- `Dr. Bu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_48`)


Fahrtkosten St. Pölten HNO Dr. Gradl, Hansaton,  Hörgerät  80 km x 0,42 € 33,60  2.5.

**False Positives:**

- `Dr. Gradl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_60`)


Folgende dem Beschwerdeführer im streitgegenständlichen Veranlagungsjahr 2022  angefallenen Kosten stehen nicht im Zusammenhang mit seiner Behinderung (Taubheit bzw.  Hörstörung):  Datum Ort Beschreibung  Betrag  in EUR  20.1 Dr. Winter, Texing Rezeptgeb. + Medikamente  13,30  23.2. Apo.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_62`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  13,30  14.3. BVA Behandlungsbeitrag  7,83  21.3. Dr. Winter Rezeptgeb. + Medikamente  50,90  31.3.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_64`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  40,05  16.5.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_69`)


Bösel, Tulln Femannose-Blase  69,85  5.9. Dr. Winter, Texing Rezeptgeb. + Medikamente  30,05  6 von 11 Seite 7 von 11

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_72`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  32,65  3.10.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_73`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  17,85  5.10.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_74`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  6,65  17.10.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_75`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  13,30  4.11.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_76`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  13,30  13.11.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_85`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  13,30  21.12.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_86`)


Dr. Winter, Texing Rezeptgeb. + Medikamente  60,60  21.12.

**False Positives:**

- `Dr. Winter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_88`)


Fahrtkosten  Scheibbs  Röntgeninstitut Dr. Hopf, MRD 32 km x 0,42 € 13,44  21.10.

**False Positives:**

- `Dr. Hopf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_89`)


Fahrtkosten  Scheibbs  Röntgeninstitut Dr. Hopf, CD 32 km x 0,42 € 13,44  5.12..

**False Positives:**

- `Dr. Hopf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_90`)


Fahrtkosten St.  Pölten  Dr. Lagler, Urologe 80 km x 0,42 € 33,60  7 von 11 Seite 8 von 11

**False Positives:**

- `Dr. Lagler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/145956.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145956.1_92`)


M.O., ASSOC. PROF. PRIV. DOZ. DR.MED. M.P,  MBA, DR.MED. M.Q:,  • F-Spital, Wien: DR.MED. M.R..  Mit Schreiben des BFG vom 9.08.2024 wurde der Bf. zur Homepage des Chirurgen der Bf. -  Wahlfacharzt Dr. Dr. ABC mit Ordination – der folgende (über die Startseite abrufbare) Text  vorgehalten:   „Patienten mit Lipödem leiden an schweren, schmerzhaften Beinen, berichten über Druck- und  Berührungsschmerzen als auch über häufige Hämatome – ohne echtes Trauma.

**False Positives:**

- `Dr. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_6`)


Das Finanzamt für  Großbetriebe wurde von Mag. Mag. (F.H) Michael Wukowits vom ehemaligen Finanzamt  Baden Mödling vertreten.

**False Positives:**

- `Mag. Mag` — partial — pred is substring of gold: `Mag. Mag. (F.H) Michael Wukowits`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt für  Großbetriebe`(organisation)
- `Mag. Mag. (F.H) Michael Wukowits`(person)
- `Finanzamt  Baden Mödling`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/146425.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146425.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Priv.-Doz.in Wilhelmine Steinheit, Prof. Rheden-Straße 16E, 2572 Obertriesting, Österreich, über die Beschwerde vom 26. April 2024 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2024 betreffend Rückforderung Familienbeihilfe  01.2023-12.2023 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Rheden-Straße` — partial — pred is substring of gold: `Prof. Rheden-Straße 16E, 2572 Obertriesting, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Priv.-Doz.in Wilhelmine Steinheit`(person)
- `Prof. Rheden-Straße 16E, 2572 Obertriesting, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/146661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Reinhard Glüer  in der Beschwerdesache  ÖkR Astrid Brück, Herborngasse 7, 6283 Schwendau, Österreich, vertreten durch Dr. Schuhmeister & Mag. Haydn GesbR, Bruck- Hainburger Straße 7, 2320 Schwechat, über die Beschwerde vom 12. Mai 2017 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf (nunmehr „Finanzamt  Österreich“) vom 26. April 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2015 zur Steuernummer 92-177/7514  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Schuhmeister` — partial — pred is substring of gold: `Dr. Schuhmeister & Mag. Haydn GesbR`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Reinhard Glüer`(person)
- `ÖkR Astrid Brück`(person)
- `Herborngasse 7, 6283 Schwendau, Österreich`(address)
- `Dr. Schuhmeister & Mag. Haydn GesbR`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamt  Österreich`(organisation)
- `92-177/7514`(tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/148533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr. Damian van Cleev, Vorderanger 3, 9130 Annamischl, Österreich, vertreten durch Dr. Kohler und Partner  Steuerberatungs GmbH, Schönbrunner Straße 53, 1050 Wien, über   die Beschwerde vom 7. April 2014 gegen die Bescheide des Finanzamtes Wien 8/16/17  (nunmehr Finanzamt Österreich) vom 6. März 2014 betreffend Einkommensteuer und  Umsatzsteuer 2006 bis 2011 und Umsatzsteuer 2012, sowie   die Beschwerde vom 3. März 2016 gegen die Bescheide des Finanzamtes Baden Mödling  (nunmehr Finanzamt Österreich) vom 10. Februar 2016 betreffend Einkommensteuer 2012  und 2013 sowie Umsatzsteuer 2013,  Steuernummer 46-222/0399, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Damian` — partial — pred is substring of gold: `Dr. Damian van Cleev`
- `Dr. Kohler` — positional overlap with gold: `Kohler und Partner  Steuerberatungs GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr. Damian van Cleev`(person)
- `Vorderanger 3, 9130 Annamischl, Österreich`(address)
- `Kohler und Partner  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 8/16/17`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)
- `46-222/0399`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mag. Mag. Oskar Raczeck  über die Beschwerde vom 31.3.2014   der Benedikt Rehkopp , vertreten durch DI Mag. Gabriele Wiedergut, Steuerberaterin in 9500 Villach,  gegen die Bescheide des Finanzamt St. Johann Tamsweg Zell am See  vom 23.1.2014 (Gesamtrechtsnachfolger Finanzamt für  Großbetriebe) betreffend Festsetzung Dienstgeberbeitrag und des Zuschlages zum  Dienstgeberbeitrag 2011-2012   nach am 12.5.2021, 2.6.2021, 2.3.2023 und 16.10.2025 durchgeführten mündlichen  Verhandlungen   zu Recht erkannt:    Die bekämpften Bescheide werden abgeändert (§ 279 Abs 1 BAO).

**False Positives:**

- `Univ.-Prof. Mag` — partial — pred is substring of gold: `Univ.-Prof. Mag. Mag. Oskar Raczeck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Mag. Mag. Oskar Raczeck`(person)
- `Benedikt Rehkopp`(person)
- `DI Mag. Gabriele Wiedergut`(person)
- `Finanzamt St. Johann Tamsweg Zell am See`(organisation)
- `Finanzamt für  Großbetriebe`(organisation)

</details>

---

## `first_name_only_no_title` 🏆

**F1:** 0.028 | **Precision:** 0.043 | **Recall:** 0.020  

**Format:** `regex`  
**Rule ID:** `20326c43`  
**Description:**
Captures names without titles ONLY when preceded by specific legal roles or prepositions, strictly excluding common institution suffixes and ensuring at least two words if no title is present.

**Content:**
```
(?:(?:Angeklagte|Angeklagten|Antragsteller|Antragstellerin|Antragsgegner|Antragsgegnerin|Partei|Parteien|Zeuge|Zeugin|Zeugen|Kläger|Klägerin|Beklagte|Beklagten|Vertreter|vertreten|durch|von\s+der|von\s+den|von\s+einem|von\s+einer|gegen|mit|bei|nach|vor|unter|über|auf|in|aus|zu|für|ohne|um|seit|bis|ab|durch|wider|neben|zwischen|entlang|gegenüber|statt|außer)\s+)([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)+)\b(?![a-z])(?!\s*(?:Rechtsanwälte|Anwälte|Partnerschaft|GmbH|AG|KG|Gesellschaft|Firma|Unternehmen|Bildung|Dienstleistungen|Versicherung|Bank|Konto|Kredit|Darlehen|Hypothek|Steuer|Finanz|Gericht|Kammer|Behörde|Amt|Ministerium|Bundes|Land|Stadt|Gemeinde|Ort|Bezirk|Kreis|Region|Lage|Position|Stelle|Job|Beruf|Tätigkeit|Funktion|Rolle|Aufgabe|Pflicht|Recht|Anspruch|Klage|Klagegrund|Klageantrag|Klagebegründung|Klageerwiderung|Klageantwort|Klageerhebung|Klageverhandlung|Klageentscheidung|Klageurteil|Klagebeschluss|Klageverfahren|Klagekosten|Klagegebühr|Klagefrist|Klageverjährung|Klageverwirkung|Klageverzicht|Revisionsgericht|Berufungsgericht|Oberste|Gerichtshof|Senatspräsidentin|Vizepräsident|Vizepräsidentin|Rekursgericht|Kontaktrecht|Dr\.\s+|Mag\.\s+|Prof\.\s+|Univ\.\s+|Hon\.\s+|MMag\.\s+|DI\.\s+|Ing\.\s+|Bakk\.\s+|PhD\.\s+|HR\.\s+|Techn\.\s+|Dipl\.\s+|PD\.\s+|Priv\.\s+|KommR\.\s+|ÖkR\.\s+|RgR\.\s+|StR\.\s+|MedR\.\s+|KzlR\.\s+|OMedR\.\s+|VetR\.\s+|AR\.\s+|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+|Jugendhilfeträger|Mutter|Vater|Eltern|Kind|Sohn|Tochter|Gewährung|Unterhaltsvorschuss|Strafsachen|Zivilrechtssachen|Maurer|Schalungsbauer|Anzahl|Verbrechen|Missbrauchs|Unmündigen|Geborenen|Schuld|Tatzeitraum|Verfahren|Nichtigkeitsb|Rechtsanw\s+|Anwalt\s+|Partei\s+|Firma\s+|Unternehmen\s+|GmbH\s+|AG\s+|KG\s+|Gesellschaft\s+|Partnerschaft\s+|Bildung\s+|Dienstleistungen\s+|Versicherung\s+|Bank\s+|Konto\s+|Kredit\s+|Darlehen\s+|Hypothek\s+|Steuer\s+|Finanz\s+|Gericht\s+|Kammer\s+|Behörde\s+|Amt\s+|Ministerium\s+|Bundes\s+|Land\s+|Stadt\s+|Gemeinde\s+|Ort\s+|Bezirk\s+|Kreis\s+|Region\s+|Lage\s+|Position\s+|Stelle\s+|Job\s+|Beruf\s+|Tätigkeit\s+|Funktion\s+|Rolle\s+|Aufgabe\s+|Pflicht\s+|Recht\s+|Anspruch\s+|Klage\s+|Klagegrund\s+|Klageantrag\s+|Klagebegründung\s+|Klageerwiderung\s+|Klageantwort\s+|Klageerhebung\s+|Klageverhandlung\s+|Klageentscheidung\s+|Klageurteil\s+|Klagebeschluss\s+|Klageverfahren\s+|Klagekosten\s+|Klagegebühr\s+|Klagefrist\s+|Klageverjährung\s+|Klageverwirkung\s+|Klageverzicht\s+|Revisionsgericht\s+|Berufungsgericht\s+|Oberste\s+|Gerichtshof\s+|Senatspräsidentin\s+|Vizepräsident\s+|Vizepräsidentin\s+|Rekursgericht\s+|Kontaktrecht\s+|Dr\.\s+|Mag\.\s+|Prof\.\s+|Univ\.\s+|Hon\.\s+|MMag\.\s+|DI\.\s+|Ing\.\s+|Bakk\.\s+|PhD\.\s+|HR\.\s+|Techn\.\s+|Dipl\.\s+|PD\.\s+|Priv\.\s+|KommR\.\s+|ÖkR\.\s+|RgR\.\s+|StR\.\s+|MedR\.\s+|KzlR\.\s+|OMedR\.\s+|VetR\.\s+|AR\.\s+|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+|Jugendhilfeträger\s+|Mutter\s+|Vater\s+|Eltern\s+|Kind\s+|Sohn\s+|Tochter\s+|Gewährung\s+|Unterhaltsvorschuss\s+|Strafsachen\s+|Zivilrechtssachen\s+|Maurer\s+|Schalungsbauer\s+|Anzahl\s+|Verbrechen\s+|Missbrauchs\s+|Unmündigen\s+|Geborenen\s+|Schuld\s+|Tatzeitraum\s+|Verfahren\s+|Nichtigkeitsb\s+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.043 | 0.020 | 0.028 | 1139 | 49 | 1090 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 49 | 1090 | 2342 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Matthäus Domrös` | `Matthäus Domrös` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Dr. Gerlinde  Rieser` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Tanja Grottenthaler` | `Tanja Grottenthaler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Mag. Susanne Haim` (person)
- `Leopold Pichlbauer` (person)
- `Dr.  Karl Penninger` (person)
- `Ing. Dipl.-Ing. Brunhild Fleischfresser` (person)
- `Margaretengürtel 23, 4092 Pyrawang, Österreich` (address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_2`)


in der Verwaltungsstrafsache gegen  Desiree Barrabaß, Rollfährensiedlung Rollfährestraße 187, 8184 Oberfeistritz, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006 über die  zwei gleichlautenden Beschwerden der Beschuldigten vom 24. März 2020 gegen die zwei  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 25. Februar  2020, Zahl: a) MA67/xxxxx/2019 und b) MA67/yyyyy/2019, zu Recht erkannt:  I) Die zwei Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Barrabaß` | `Desiree Barrabaß` |

**Missed by this rule (FN):**

- `Rollfährensiedlung Rollfährestraße 187, 8184 Oberfeistritz, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Manuel Rathlev, Hadersfelder Straße 10, 4171 Kasten, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Edwin Meuser  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Edwin Meuser` | `Edwin Meuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Manuel Rathlev` (person)
- `Hadersfelder Straße 10, 4171 Kasten, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Rachel Darnieder` — partial — pred is substring of gold: `Univ.-Prof.in Rachel Darnieder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hemma Bährs`(person)
- `Univ.-Prof.in Rachel Darnieder`(person)
- `Finanzamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_2`)


Die Kommunalsteuer wird für die Jahre 2007 bis 2012 wie folgt festgesetzt:  Zeitraum Bemessungsgrundlage  in Euro  Abgabenbetrag in  Euro  Abgabe  Nachforderung  2007 47.203,86 1.416,12 881,20  2008 45.056,47 1.351,69 1.240,01  2009 64.738,83 1.942,16 929,36  2010 85.718,62 2.571,56 838,19  2011 65.910,95 1.977,33 385,94  2012 56.152,66 1.684,58 384,23  Summen 364.781,39 10.943,44 4.658,93

**False Positives:**

- `Euro  Abgabenbetrag` — no gold match — likely missing annotation
- `Euro  Abgabe  Nachforderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_33`)


Zeitraum Bemessungsgrundlage in Euro Abgabenbetrag in Euro  2007 47.203,86 1.416,12  2008 45.056,47 1.351,69  2009 64.738,83 1.942,16  2010 85.718,62 2.571,56  2011 65.910,95 1.977,33  2012 56.152,66 1.684,58  Summe 364.781,39 10.943,44  Ebenso wurde gem. §§ 217 und 217a BAO wegen nicht fristgerechter Entrichtung der  Kommunalsteuer ein Säumniszuschlag von Euro 90,98 festgesetzt.

**False Positives:**

- `Euro Abgabenbetrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_23`)


 Mind-Designer: Äußere Umstände werfen Dich nur mehr selten um und Du findest  schneller zu Deiner Mitte, Stress-Situationen empfindest Du als Herausforderungen, bei  denen Du zu Höchstform aufläufst und die Dich stärken.“

**False Positives:**

- `Deiner Mitte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_24`)


Trinergy-NLP Practitioner  „Von Life-Design bis Mind-Design mit Trinergy – Akademie für Coaching & NLP  Erlebe bei Deinem Trinergy-NLP Practitioner, was ohne Drama erfahr- und machbar ist:   Life-Design: Erlaube alten Gewohnheiten nicht länger, Dein Leben zu lenken, nimm die  Zügel selbst in die Hand, nutze die Geheimnisse von Top-ManagerInnen, Zen-Mönchen  und SpitzensportlerInnen, bau mit TrinergyNLP ein Fundament für die Welt, in der Du  leben willst!

**False Positives:**

- `Deinem Trinergy` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_25`)


 Kommunikations-Design: Lies Dein Gegenüber, bring Deine Botschaft besser hinüber,  löse elegant und souverän Konflikte, steigere damit Deine Arbeitsfreude und  Lebensqualität;

**False Positives:**

- `Deine Arbeitsfreude` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Viktoria Kreiselmayer` — partial — pred is substring of gold: `Univ.-Prof.in Viktoria Kreiselmayer`
- `Corazza Kocholl Laimer Rechtsanwälte` — partial — pred is substring of gold: `Corazza Kocholl Laimer Rechtsanwälte OG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Viktoria Kreiselmayer`(person)
- `Muran Waldhans, BEd`(person)
- `Am Tegel 5, 9831 Waben, Österreich`(address)
- `Corazza Kocholl Laimer Rechtsanwälte OG`(organisation)
- `Finanzamtes Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_7`)


1. Aufgrund einer anonymen Anzeige im Jahr 2006 wurden seitens der Abgabenbehörde  Ermittlungen über die widerrechtliche Verwendung eines Fahrzeuges mit italienischem  Kennzeichen im Inland bei Muran Waldhans, BEd (= Beschwerdeführer, Bf) durchgeführt:  1 von 15 Seite 2 von 15

**False Positives:**

- `Muran Waldhans` — partial — pred is substring of gold: `Muran Waldhans, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Muran Waldhans, BEd`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_140`)


Zwar hatte der Bf im Streitzeitraum auch in Italien Verwandte, die er besuchte,  7 von 15 Seite 8 von 15

**False Positives:**

- `Italien Verwandte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_16`)


Schließlich wurde die Rz 851 aus dem Steuerbuch 2018 zum Thema Heilbehandlung zitiert.

**False Positives:**

- `Thema Heilbehandlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_17`)


Mit Schreiben vom 05.12.2018 legte das Finanzamt die Rechtslage dar und hielt der  Beschwerdeführerin vor, dass sie abweichend von den Pauschalsätzen Kosten für die  Beschaffung von Lebensmitteln geltend mache, welche bestimmte Anforderungen erfüllen  würden (Biolebensmittel, glutenfrei, Gemüse), aus deren Artikelbezeichnung aber keinesfalls  geschlossen werden könne, dass sie ausschließlich wegen der bestehenden Behinderung  konsumiert werden müssten.

**False Positives:**

- `Pauschalsätzen Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_44`)


Für die Art der Kommunikation, wie die Beschwerdeführerin sie vom Finanzamt erfahre, habe  offensichtlich nur ein Finanzamt Zeit und Geld zur Verfügung.

**False Positives:**

- `Finanzamt Zeit` — similar text (different position): `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamt`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_46`)


Mit Beschwerdevorentscheidung vom 10.01.2019 wies das Finanzamt die Beschwerde als  unbegründet ab, beließ den Erstbescheid unverändertund führte begründend aus:  „Nach den Bestimmungen des § 35 EStG steht einem Steuerpflichtigen jeweils ein Freibetrag für  außergewöhnliche Belastungen durch eine eigene körperliche oder geistige Behinderung zu.  Diese Pauschalsätze sind im Abs. 3 dieser Bestimmung geregelt und betragen bei einer in Ihrem  Fall festgestellten Behinderung von 30 % € 75,-.

**False Positives:**

- `Ihrem  Fall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Rafaela Ringart` — partial — pred is substring of gold: `Priv.-Doz.in DDr.in Rafaela Ringart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in DDr.in Rafaela Ringart`(person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich`(address)
- `Silvestri Bau GmbH`(organisation)
- `Mag. WP`(person)
- `38-663/2876`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_4`)


Der Haftungsbetrag  umfasst folgende Abgaben:    Abgabenart Zeitraum Fälligkeit Höhe in EUR  Umsatzsteuer 10/2010 15.12.2010 4.014,46  Lohnsteuer 11/2010 15.12.2010 385,82  Lohnsteuer 12/2010 17.01.2011 552,12  Lohnsteuer 01/2011 15.02.2011 252,19  Körperschaftsteuer 01-03/2011 15.02.2011 874,00  Dienstgeberbeitrag 11/2010 15.12.2010 359,70  Dienstgeberbeitrag 12/2010 17.01.2011 238,84  Dienstgeberbeitrag 01/2011 15.02.2011 174,26  1 von 15 Seite 2 von 15

**False Positives:**

- `Fälligkeit Höhe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_69`)


Das Dienstverhältnis des BF zur GmbH wurde mit Ende April 2011 gelöst, die Funktion als  Geschäftsführer blieb davon unberührt.

**False Positives:**

- `Ende April` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_74`)


2011 wurden folgende Abgaben vorgeschrieben bzw. (soweit Lohnabgaben betroffen sind) von  der GmbH selbst gemeldet:    Abgabenart Zeitraum Fälligkeit Höhe in EUR

**False Positives:**

- `Fälligkeit Höhe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_126`)


Gemäß § 248 BAO kann der nach Abgabenvorschriften Haftungspflichtige unbeschadet der  Einbringung einer Bescheidbeschwerde gegen seine Heranziehung zur Haftung  (Haftungsbescheid, § 224 Abs. 1) innerhalb der für die Einbringung der Bescheidbeschwerde  gegen den Haftungsbescheid offenstehenden Frist auch gegen den Bescheid über den  Abgabenanspruch Bescheidbeschwerde einbringen.

**False Positives:**

- `Abgabenvorschriften Haftungspflichtige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_88`)


 20. August 2015 Facharzt für Psychiatrie  Im umfangreichen Gutachten ist das Ergebnis zusammengefasst wie folgt festgehalten:    Die Einstufung mit 50% wurde damit begründet, dass Punkt 2 Punkt 1 um eine Stufe steigert,  da sich die Leiden gegenseitig beeinflussen.

**False Positives:**

- `Psychiatrie  Im` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_199`)


Antrag auf Erörterungstermin  Gem. § 269 Abs. 3 BAO kann der Einzelrichter die Parteien zur Erörterung der Sach- und  Rechtslage sowie zur Beilegung des Rechtsstreits laden.

**False Positives:**

- `Erörterungstermin  Gem` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_9`)


Sie werden in Ihrem Interesse ersucht, die nachfolgenden Fragen sorgfältig und vollständig  zu beantworten und durch Vorlage geeigneter Unterlagen, die zu Ihrer Entlastung dienen  können, zu belegen.

**False Positives:**

- `Ihrem Interesse` — no gold match — likely missing annotation
- `Ihrer Entlastung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_42`)


Die Bf. war laut Zentralem Melderegister bereits seit Ende Juni 2019 nicht mehr an derselben  Adresse mit Hauptwohnsitz gemeldet wie ihre Kinder und hat die gemeinsame Wohnung selbst  nach eigenen Angaben mit 3. Juli 2019 verlassen.

**False Positives:**

- `Ende Juni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_45`)


Der Pächter verpflichtet sich, ein Firmen Restaurant im Pachtgegenstand nachhaltig  und sorgfältig zu betreiben und es zu den im Franchise-Vertrag festgelegten  Geschäftsstunden offenzuhalten.

**False Positives:**

- `Firmen Restaurant` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_219`)


Instandhaltung und Instandsetzung, im Art. 5 wonach sich der Pächter verpflichtet, ein Firmen  Restaurant in den Pachträumen nachhaltig zu betreiben und es zu den im Franchisevertrag  festgelegten Geschäftsstunden offen zu halten sowie im Art. 9 2) wonach die Vertragsteile  vereinbaren, dass der Pächter bei Beendigung des Franchisevertrages nicht mehr zum Betrieb  des Firmen Restaurants berechtigt ist.

**False Positives:**

- `Firmen  Restaurant` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_23`)


Zeige ein Käufer Interesse, sei das  Fahrzeug durch den Bf. im Namen und auf Rechnung der MH verkauft worden (eine  entsprechende Vollmacht habe man bisher nicht vorgelegt).

**False Positives:**

- `Käufer Interesse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_44`)


(2) Zeige ein Käufer Interesse, sei durch den Bf. (Gutschrift als Rechnung/Kaufvertrag) ein  Kaufvertrag zwischen der deutschen MH und dem Bf. erstellt worden (laut Auskunft per Fax  übermittelt), anschließend ein Kaufvertrag zwischen dem Bf. und dem Käufer.

**False Positives:**

- `Käufer Interesse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_296`)


Stb: Man kann doch nicht sagen, wenn ein Deutscher Umsätze in Österreich tätigt, er mit  keiner Umsatzsteuer belastet wird und man dem österreichischen Unternehmer die  Umsatzsteuer vorschreibt.

**False Positives:**

- `Deutscher Umsätze` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_676`)


Bei der Besprechung vom 30. November 2011  wurde vom Bf. mitgeteilt, dass diese Lieferungen seit Mitte Oktober (Ergänzungsfrage 4 bei der  Artikel-V-Anfrage in Deutschland, Befragung der Ehegatten MH zum Fahrer) mittels LKW-

**False Positives:**

- `Mitte Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_60`)


Der zum Abzug  Verpflichtete (Abs. 3) haftet dem Bund für die Einbehaltung und Abfuhr der  Kapitalertragsteuer.

**False Positives:**

- `Abzug  Verpflichtete` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_142`)


Vorliegen eines Bestandvertrages und Vertragsdauer  Nach § 33 TP 5 Abs 1 Z 1 GebG unterliegen der Gebühr für Rechtsgeschäfte Bestandverträge  (§§ 1090 ff ABGB) und sonstige Verträge, wodurch jemand den Gebrauch einer  unverbrauchbaren Sache auf eine gewisse Zeit und gegen einen bestimmten Preis erhält.  Leasingverträge haben keinen einheitlichen feststehenden Inhalt, sondern treten in vielfältigen  Varianten und Erscheinungsformen mit jeweils anderen Rechten und Pflichten auf.

**False Positives:**

- `Rechtsgeschäfte Bestandverträge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_5`)


Verfahrensablauf  Mit Einkommensteuerbescheid für das Jahr 2009 vom 13.7.2011 wurde im Rahmen der  Einkünfte aus Vermietung und Verpachtung ein AfA-Satz von 1,5% im Hinblick auf die  Vermietung eines Betriebsgebäudes berücksichtigt und wie folgt begründet:  Bei Gebäuden betrage der AfA-Satz grundsätzlich bis zu 1,5% (1,5% würden einer  Nutzungsdauer von rund 67 Jahren entsprechen).

**False Positives:**

- `Mit Einkommensteuerbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_126`)


Mit Schreiben vom 2.1.2020 wurde wie folgt geantwortet:  1.  Abschreibung für Abnutzung  Hier sei zweifellos die Abschreibung für den Grundwert auszuscheiden, das hieße die  Bemessungsgrundlage sei um den Grundwert zu kürzen.

**False Positives:**

- `Abnutzung  Hier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_167`)


Es finden sich in Ihrem Gutachten keine Feststellungen zur Qualität der Bauausführung der  einzelnen Gebäude.

**False Positives:**

- `Ihrem Gutachten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_5`)


Verfahrensverlauf  Die Beschwerdeführerin (in der Folge abgekürzt Bf) wurde unter der Firma „A-GmbH“ am 14.  Juli 1999 beim Handelsgericht Wien zu Firmenbuchnummer xxxxxxs im Firmenbuch  eingetragen.

**False Positives:**

- `Die Beschwerdeführerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Marianne Liuni` — partial — pred is substring of gold: `Univ.-Prof.in Marianne Liuni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Marianne Liuni`(person)
- `Luigi Wedekämper`(person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_50`)


Die Antragstellerin hat eine  vorläufige Lizenz in Griechenland für Online Sportwetten, Casino und Poker (Beweis:Online  Gambling in Greece, Appendix A).

**False Positives:**

- `Online Sportwetten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_55`)


Das von der Antragstellerin – in englischer Sprache vorgelegte - griechischen Gesetz 4002/2011,  Art. 25 bis Art. 54, zum Stand März 2014, lässt auch keine eindeutige Beurteilung der  griechischen Rechtslage für den gesamten hier gegenständlichen Zeitraum 2010 bis 2014 zu.  Der Sachverhalt ist unklar geblieben und hinsichtlich der Geschäftstätigkeit der Antragstellerin  in Griechenland (Stellung als Abgabenschuldnerin in Griechenland) mit erheblichen Zweifel  behaftet.

**False Positives:**

- `Stand März` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_98`)


Allerdings ist der Vertragspartner der Online- Wetten nicht die Bf., sondern die BergLuftfahrt  Eood mit Sitz in Bulgarien oder die BB (siehe  Beilage Goalbet Wettbedingungen, Punkte 36 und Schlusssatz nach Punkt 39 zum Stand April  2017).

**False Positives:**

- `Stand April` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BergLuftfahrt`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_100`)


Laut dem Schreiben der Bf. vom 13.10.2016 sei das Online Glücksspiel in den Art. 45 bis 50 des  griechischen Gesetzes 4002/2011 geregelt, in Art. 50 sei die Besteuerung geregelt. Mit E-Mail  vom 14.10.2016 wurde als Beilage das Gesetz 4002/2011, zum Stand März 2014, in englischer  Sprache vorgelegt.

**False Positives:**

- `Stand März` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_130`)


Alleine mit der Vorlage des  Gesetzes 4002/2011, Teil D, Art. 25 – Art. 54, zum Stand März 2014, in englischer Übersetzung,  wurde die für eine Vergleichsprüfung maßgebliche Rechtslage nicht hinreichend dargelegt.

**False Positives:**

- `Stand März` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_162`)


Keinen Beweis gibt  es jedoch, dass die Bf. auch in Griechenland Abgaben bezahlt hat.

**False Positives:**

- `Griechenland Abgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_22`)


Dies schildert unsere Mandantschaft auch in  Ihrem Fax vom 13. August 2019 an das Finanzamt (siehe Beilage).

**False Positives:**

- `Ihrem Fax` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_76`)


Mit Eingabe vom 20. Mai 2015 wurde nach Fristverlängerung Beschwerde gegen die Bescheide  betreffend   a) Festsetzung der eigenbetrieblichen Forschung und experimentelle Entwicklung für das  Kalenderjahr 2011;

**False Positives:**

- `Fristverlängerung Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_89`)


Der Vorstand der Bf. habe im Jahr 2011 Auswertungen für Probetrocknungen durchgeführt und  ab Anfang Dezember Herrn X als Mitarbeiter eingestellt. Aus den bereits vorgelegten  Unterlagen gehe hervor, dass die Angestellten F, X und Y zumindest zeitanteilig  Entwicklungsarbeiten direkt ausgeführt hätten.

**False Positives:**

- `Anfang Dezember Herrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_220`)


Der Vorstand der Bf. hat nach ihrer Darstellung im Jahr 2011 Auswertungen für  Probetrocknungen durchgeführt und ab Anfang Dezember Herrn X als Mitarbeiter eingestellt.  Aus den bereits vorgelegten Unterlagen geht nach ihren Ausführungen hervor, dass die  Angestellten F, X und Y zumindest zeitanteilig Entwicklungsarbeiten direkt ausgeführt haben.

**False Positives:**

- `Anfang Dezember Herrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_13`)


Entscheidungsgründe  I. Verfahrensgang  Am 27.4.2011 erging ein Bescheid über einen Prüfungsauftrag betreffend einer Außenprüfung  gemäß § 147 BAO an die Beschwerdeführerin Firma Dorfcongart-Event (in der Folge als Bf bezeichnet).

**False Positives:**

- `Firma Dorfcongart` — positional overlap with gold: `Dorfcongart-Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dorfcongart-Event`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_14`)


Gegenstand der Außenprüfung war die Lohnsteuerprüfung - Lohnsteuer, Dienstnehmerbeitrag  (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) gem. § 86 Abs. 1 EStG sowie  Sozialversicherungsprüfung gem. § 41 a ASVG und Kommunalsteuerprüfung gem. § 14  KommStG für die Zeiträume Anfang Jänner 2006 bis Ende Dezember 2010.

**False Positives:**

- `Ende Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_203`)


Gleichzeitig mit ihm ist auch sein Freund Herr UG4 in das Unternehmen als  Gesellschafter eingetreten.

**False Positives:**

- `Freund Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_316`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf, eine GesnbR – Namensgeber ÖU – , die als Hausbetreuung tätig war  (Reinigungsarbeiten, Schneeräumung etc.) mit österreichischen und ungarischen  Gesellschaftern war Gegenstand einer Außenprüfung für die Zeiträume Anfang Jänner 2006 bis  Ende Dezember 2010, einem Zeitraum, in dem ungarische Staatsangehörige trotz des EU-

**False Positives:**

- `Ende Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_43`)


Kein zusätzlicher Unterstützungsbedarf beim  Lernen  30-40%  Leichte bis mäßige soziale Beeinträchtigung in ein bis zwei Bereichen, beispielsweise  Schulausbildung und alltägliche Tätigkeiten, Freizeitaktivitäten, in Teilbereichen  Unterstützungsbedarf beim Lernen  Die bei S. noch bestehende kombinierte umschriebene Störung der motorischen Funktionen  (leichte Gleichgewichts- und Koordinationsproblematik) wurde von der Sachverständigen  5 von 10 Seite 6 von 10

**False Positives:**

- `Teilbereichen  Unterstützungsbedarf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_92`)


Von den Büchern sind die Kaufartikel „Pluspunkt  Deutsch-Österreich“, „Tschechisch Österreich“ und „Deutsch-Österreich“ Druckerzeugnisse, die  bei Integrationskursen Verwendung finden.

**False Positives:**

- `Integrationskursen Verwendung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_43`)


Der VwGH hat in seinem Erkenntnis GZ 2014/15/0058 vom 19.10.2016 folgendes festgehalten:  „Gemäß § 303 Abs. 1 lit. b BAO kann ein durch Bescheid abgeschlossenes Verfahren auf  Antrageiner Partei oder von Amts wegen wiederaufgenommen werden, wenn Tatsachen oder  Beweismittel im abgeschlossenen Verfahren neu hervorgekommen sind und die Kenntnis dieser  Umstände allein oder in Verbindung mit dem sonstigen Ergebnis des Verfahrens einen im  Spruch anderslautenden Bescheid herbeigeführt hatte.

**False Positives:**

- `Antrageiner Partei` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_28`)


4.6.93 Sozialzentrum Caritas: Bezugnehmend auf Ihr Schreiben vom 24.05.1993 in dem Sie um  einen Befundbericht über (die Bf.), geb. [TT/MM/1961] ansuchen, teilen wir Ihnen mit, daß  sich die Pat. seit 1987 in unserer ambulanten Behandlung befindet.

**False Positives:**

- `Ihr Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_32`)


Ergebnis der durchgeführten Begutachtung  Lfd.  Nr.  Bezeichnung der körperlichen, geistigen oder sinnesbedingten Funktions - einschränkungen, welche voraussichtlich länger als sechs Monate andauern  werden:   Begründung der Rahmensätze:  Pos.Nr. Gdb %  1 Residualzustand bei Schizophrenie bei Oligophrenie   Unterer Rahmensatz, da keine ständige Beaufsichtigung notwendig.

**False Positives:**

- `Oligophrenie   Unterer Rahmensatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_58`)


Ein Anspruch auf Familienbeihilfe gemäß § 6 Abs. 5 1. u.2. Satz Familienlastenausgleichsgesetz  1967 in ab 1.1.2016 geltenden Fassung wäre unter den vorgesehenen  Anspruchsvoraussetzungen dann gegeben, wenn bei Ihnen im Sinne des § 6 Abs. 2 lit. d  Familienlastenausgleichsgesetz 1967 Ihr Unvermögen sich den Unterhalt selbst zu verschaffen  vor Vollendung Ihres 21.

**False Positives:**

- `Vollendung Ihres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_62`)


Anspruch auf Familienbeihilfe, noch auf den Erhöhungsbetrag zur Familienbeihilfe wegen  erheblichen Behinderung zu.   Laut amtsärztlichen Sachverständigengutachten vom 3.12.2019 wurde Ihr Behinderungsgrad  im Ausmaß von 80 v.H. ab dem Monat Jänner 1987 und Ihr Unvermögen sich den Unterhalt  selbst zu verschaffen ab dem Monat Jänner 1987, also nach Vollendung Ihres 21.

**False Positives:**

- `Vollendung Ihres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_29`)


Die belangte Behörde legte am 16.03.2020 die Beschwerde dem BFG vor und führte dazu aus,  dass gem. § 23 Z 2 EStG 1988 Einkünfte aus Gewerbebetrieb Gewinnanteile der Gesellschafter  von Gesellschaften wären, bei denen die Mitgesellschafter als Mitunternehmer anzusehen  wären (wie insbesondere OGs und KGs) sowie die Vergütungen, die die Gesellschafter von der  2 von 6 Seite 3 von 6

**False Positives:**

- `Gewerbebetrieb Gewinnanteile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_55`)


Zum Zeitraum November 2017 bis August 2018:  Der Sohn des Bf. hatte die o.a. Schule im Schuljahr 2017/18 bis August 2018 besucht.

**False Positives:**

- `Zeitraum November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_57`)


Zum Zeitraum September 2018 bis Juni 2019:  Ab September 2018 besuchte der Sohn des Bf. die o.a. Schule nicht (auch keine andere Schule).

**False Positives:**

- `Zeitraum September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_37`)


Diese wurden  mit Sicherheit vom AMS protokolliert und Sie hätten bei Bedarf Einsicht.

**False Positives:**

- `Bedarf Einsicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_54`)


In den folgenden Monaten Juli - bis Ende November 2018 - setzte die Tochter des Bf. ihre Lehre  bei der Fa. D. KG bis 30. November 2018 fort.

**False Positives:**

- `Ende November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_92`)


Mit dieser E-Mail entgegnete der Bf in Beantwortung des Vorhaltes der belangten Behörde wie  folgt:   "Ich darf auf Ihr Email vom 06.06.2017 in Sachen Beschwerde Bf — StNr. 61 68-535/9689  zurückkommen und nach Besprechung mit Herrn Noeltge folgenden Lösungsvorschlag unterbreiten:  Grundsätzliche Überlegung:  Der VwGH vertritt in seinem Erkenntnis vom 29.03.2017 zur Hauptwohnsitzbefreiung die  Ansicht, dass sich die Befreiungsbestimmung des § 30 Abs. 2 Z 1 EStG lediglich auf den Grund  und Boden eines bebauten Grundstücks erstreckt, der nach der Verkehrsauffassung einem  üblicherweise als Bauplatz erforderlichen Grundstück entspricht.

**False Positives:**

- `Ihr Email` — no gold match — likely missing annotation
- `Sachen Beschwerde Bf` — no gold match — likely missing annotation
- `Herrn Noeltge` — partial — gold is substring of pred: `Noeltge`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `68-535/9689`(tax_number)
- `Noeltge`(person)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

**False Positives:**

- `Vienna International School` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Prause`(person)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_49`)


Aus dem Befund vom August 2013 des St. Gabriel Hospital in Addis Abeba, Äthiopien, geht die  Diagnose einer „schweren depressiven Verstimmung mit psychotischen Zügen“ hervor.

**False Positives:**

- `Addis Abeba` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

**False Positives:**

- `Vienna International School` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Prause`(person)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_107`)


Begründung der Rahmensätze: Pos.Nr. Gdb%  1 paranoide Schizophrenie  Unterer Rahmensatz, da unter Therapie Teilselbständigkeit gegeben 03.07.02 50  Gesamtgrad der Behinderung 50 v. H.  Begründung für den Gesamtgrad der Behinderung:  Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keine Änderung  Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja   GdB liegt vor seit: 07/2014  Begründung - GdB liegt rückwirkend vor: GdB seit 4/14 ( siehe Befund im VGA)

**False Positives:**

- `Therapie Teilselbständigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_123`)


Weiters enthält die Beschwerdevorentscheidung folgende Begründung:  "In Ihrem Beschwerdebegehren führten Sie aus, dass Sie tatsächlich bereits seit Jänner 2013  auf Grund Ihrer bestehenden paranoiden Schizophrenie nicht erwerbsunfähig sind.

**False Positives:**

- `Grund Ihrer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_125`)


§ 6 Abs. 5 1. Satz : Kinder haben einen Eigenanspruch auf Familienbeihilfe unter denselben  Voraussetzungen unter denen ein Vollwaise Anspruch auf Familienbeihilfe hat (§6 Abs. 1 bis 3),  sofern ihre Eltern ihnen nicht überwiegend Unterhalt leisten und ihr Unterhalt nicht zur Gänze  aus Mitteln der Kinder- und Jugendhilfe oder nicht zur Gänze aus öffentlichen Mitteln zur  Sicherung des Lebensunterhaltes oder des Wohnbedarfs getragen wird.

**False Positives:**

- `Vollwaise Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_126`)


§ 6 Abs. 5 2. Satz: Erheblich behinderte Kinder im Sinne des § 2 Abs. 1 lit. c haben einen  Eigenanspruch auf Familienbeihilfe unter denselben Voraussetzungen unter denen ein  Vollwaise Anspruch auf Familienbeihilfe hat (§6 Abs. 1 bis 3), sofern ihre Eltern ihnen nicht  überwiegend Unterhalt leisten und sie einen eigenständigen Haushalt führen.

**False Positives:**

- `Vollwaise Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_127`)


§ 6 Abs. 6: kein Eigenanspruch Anspruch auf Familienbeihilfe besteht für Personen im Sinne  des § 1 Z 3 und Z 4 des Strafvollzugsgesetzes, sofern die Bestimmungen des  Strafvollzugsgesetzes auf sie Anwendung finden.

**False Positives:**

- `Eigenanspruch Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_140`)


Satz  Familienlastenausgleichsgesetzes 1967 in der mit 1. Jänner 2016 geltenden Fassung des BGBl  Nr. XX/2018 wäre unter den vorgesehenen Anspruchsvoraussetzungen dann gegeben, wenn  bei Ihnen im Sinne des § 6 Abs. 2 lit. d Familienlastenausgleichsgesetz 1967 Ihr Unvermögen  sich den Unterhalt selbst zu verschaffen vor Vollendung Ihres 21.Lebensjahres festgestellt  worden wäre.

**False Positives:**

- `Vollendung Ihres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_141`)


Tritt die Erwerbsunfähigkeit nicht vor Vollendung des 21.Lebensjahres ein, besteht weder  Anspruch auf Familienbeihilfe, noch auf den Erhöhungsbetrag zur Familienbeihilfe wegen  erheblichen Behinderung zu.  Die medizinischen Sachverständigengutachten vom 28.8.2018 und vom 4.6.2019 gehen davon  aus, das Ihr Unvermögen sich den Unterhalt selbst zu verschaffen nicht vor Vollendung Ihres  21.

**False Positives:**

- `Vollendung Ihres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_148`)


Im gegenständlichen Fall wurde Ihr Unvermögen sich den Unterhalt selbst zu verschaffen, nach  Vollendung Ihres 21.

**False Positives:**

- `Vollendung Ihres` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_152`)


Laut Gutachten ist der Befund des St. Gabriel Hospital in Addis Abeba aus August 2013 nicht  ausreichend detailliert um den Grad der Behinderung zu beurteilen.

**False Positives:**

- `Addis Abeba` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_201`)


12 Kl. Vienna International School- Abschluss mit Zertifikat 2011   Bundesheer: absolviert, 6 Monate   Ferialjob 1 Monat vor dem Studium   Beginn Studium (in GB/ Wales) Physikstudium für ein Jahr (2013), dann 2-3 Monate wieder in  Wien, dann 6 Mo.

**False Positives:**

- `Beginn Studium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_202`)


Studium für Computerwissenschaft 2014 (in Addis Abbeba).

**False Positives:**

- `Addis Abbeba` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_217`)


Konzentration und  Antrieb reduziert ; Stimmungslage ausgeglichen, kaum affizierbar ; Affekte: angepasst, optische  Halluzinationen   Ergebnis der durchgeführten Begutachtung:   Lfd. Nr. : 1  Bezeichnung der körperlichen, geistigen oder sinnesbedingten Funktions-einschränkungen,  welche voraussichtlich länger als sechs Monate andauern werden: Begründung der  Rahmensätze:  paranoide Schizophrenie mit deutlichem Residuum Mittlerer Rahmensatz, da instabil,  verminderte belastbar, Minussympotmatik, daher betreute Wohnform erforderlich  Pos.Nr.:  03.07.02 60   Gdb %: 60  Gesamtgrad der Behinderung 60 v. H.   Begründung für den Gesamtgrad der Behinderung:   Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:   --   Stellungnahme zu Vorgutachten:   Erhöhung um 1 Stufe gegenüber Vorgutachten 28 05 2019, da Verschlechterung und  Ausbildung eines Residuums.

**False Positives:**

- `Mittlerer Rahmensatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_229`)


X Dauerzustand“  In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Bezüglich des Sachverständigengutachtens von 09.07.2020 Seite 5 letzter Absatz legt der  Erwachsenenvertreter dem Gericht zwei Schriftsätze vor und weist darauf hin, dass das St.  Gabriel General Hospital in Addis Ababa ein renomiertes Privatspital ist.

**False Positives:**

- `Addis Ababa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_267`)


In der von den Sachverständigen heranzuziehenden Einschätzungsverordnung wird bei  Schizophrenen Störungen (Schizophrenie, schizoide Persönlichkeitsstörung, schizoaffektive  Erkrankungen, akut psychotische Zustandsbilder) zwischen leichten, mittelschweren und  schweren Verlaufsformen unterschieden.

**False Positives:**

- `Schizophrenen Störungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_333`)


• Anspruchszeitraum  Die Frage, ob für einen bestimmten Anspruchszeitraum Familienbeihilfe zusteht, ist anhand  der rechtlichen und tatsächlichen Gegebenheiten im Anspruchszeitraum zu beantworten.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) reichte die Einkommensteuererklärung (Arbeitnehmerveranlagung)  2018 ein und machte folgende Werbungskosten geltend:  Kosten für Familienheimfahrten Kennzahl 300 - 3.672,00 €   Kosten für doppelte Haushaltsführung Kennzahl 723 - 939,10 €

**False Positives:**

- `Familienheimfahrten Kennzahl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_57`)


Der Mietvertrag lautet auf Herrn Lukasz Jan Chlebek.

**False Positives:**

- `Herrn Lukasz Jan Chlebek` — partial — gold is substring of pred: `Lukasz Jan Chlebek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lukasz Jan Chlebek`(person)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Frieda Krein` — partial — pred is substring of gold: `Hon.-Prof.in Frieda Krein`
- `Elena Kaminskiy` — partial — pred is substring of gold: `Priv.-Doz.in Elena Kaminskiy`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Frieda Krein`(person)
- `Priv.-Doz.in Elena Kaminskiy`(person)
- `W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `60-936/8299`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_2`)


Begründung  Der Beschwerdeführer Priv.-Doz.in Elena Kaminskiy  hat mit Eingabe vom 22.10.2020, eingelangt am 27.10.2020,  gemäß § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht  über die Beschwerde gegen den Einkommensteuerbescheid für 2019 erhoben.

**False Positives:**

- `Elena Kaminskiy` — partial — pred is substring of gold: `Priv.-Doz.in Elena Kaminskiy`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Elena Kaminskiy`(person)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter in den Beschwerdesachen des Janosch Findeise,  Reichenauweg 22, 4724 Oberaubach, Österreich, gegen die zwei Straferkenntnisse des Magistrats der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde (beide) vom 23. Juni 2020, GZen 1)  MA67/Zahl1 und 2) MA67/Zahl2, in beiden Fällen wegen einer Verwaltungsübertretung nach §  2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der  geltenden Fassung, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) werden die Beschwerden als unbegründet abgewiesen  und werden die angefochtenen Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Wien Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Janosch Findeise`(person)
- `Reichenauweg 22, 4724 Oberaubach, Österreich`(address)
- `Magistrats der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_2`)


2016/46 iVm § 4 Abs. 1 Wiener Parkometergesetz 2006  idF LGBl Nr. 71/2018, nach Durchführung einer mündlichen Verhandlung am 11. September  2020, im Beisein der Schriftführerin Ingrid Pavlik, zu Recht erkannt:  Der Beschwerde wird gemäß § 50 VwGVG insofern teilweise stattgegeben, als die Geldstrafe  von € 60,00 auf € 36,00 und die Ersatzfreiheitsstrafe von 14 Stunden auf 8 Stunden  herabgesetzt wird.

**False Positives:**

- `Ingrid Pavlik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_64`)


• Bestätigung des Dienstgebers, in dessen Auftrag unterwegs gewesen zu sein  Die Bf. bringt vor, zur Beanstandungszeit nachweislich für ihren Dienstgeber MOKI Wien tätig  gewesen sei und eine entsprechende Dienstbestätigung vorgelegt zu haben.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

**False Positives:**

- `Nicola Folprecht` — partial — pred is substring of gold: `Univ.-Prof.in Nicola Folprecht`
- `Florian Abbruzzese` — partial — pred is substring of gold: `Florian Abbruzzese, BA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Nicola Folprecht`(person)
- `Florian Abbruzzese, BA`(person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_5`)


Verfahrensverlauf  Mir Haftungsvorhalt vom 1. Oktober 2014 teilte die belangte Behörde der Beschwerdeführerin  (in der Folge Bf) mit, dass beabsichtigt sei, sie für diverse Abgabenschuldigkeiten  (Umsatzsteuer, Körperschaftsteuer, Lohnsteuer, Dienstgeberbeitrag samt Zuschlag sowie  Nebenansprüche) betreffend den Zeitraum 2012 bis 2013 der Garten Taltralex GmbH (in der Folge  Gesellschaft), deren Geschäftsführerin die Bf gewesen sei, im Gesamtausmaß von 37.817,42  Euro als Haftungsverpflichtete in Anspruch zu nehmen.

**False Positives:**

- `Mir Haftungsvorhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Garten Taltralex GmbH`(organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_22`)


Dieses Ergänzungsersuchen blieb – nach  einem Ersuchen um Fristerstreckung bis Ende Jänner 2016 – inhaltlich unbeantwortet.

**False Positives:**

- `Ende Jänner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_51`)


Die Zahlungseingänge seien vor allem dafür aufgewendet worden, Zug um  Zug Geschäfte abzuwickeln, insbesondere für Materialeinkäufe, um die vorhandenen Aufträge  erfüllen zu können.

**False Positives:**

- `Zug Geschäfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_72`)


Hinsichtlich des von der belangten Behörde abverlangten  Liquiditätsstatus wurde um Fristerstreckung bis Ende September 2018 ersucht.

**False Positives:**

- `Ende September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_99`)


Dem streitgegenständlichen Bescheid liegen folgende Abgabenschuldigkeiten zugrunde:  Abgabenart  Zeitraum   Betrag  Umsatzsteuer 10/2012 3.651,92  Umsatzsteuer 11/2012 3.425,03  Umsatzsteuer  12/2012  3.938,46   Umsatzsteuer  01/2013  1.250,24   Umsatzsteuer  02/2013  547,88   Umsatzsteuer 04/2013 9.334,46  Lohnsteuer  11/2012 1.461,75  Lohnsteuer  12/2012  1.667,61  Lohnsteuer  01/2013  795,61  Lohnsteuer  02/2013  708,53  Lohnsteuer  03/2013  703,18  Lohnsteuer  04/2013  884,55  Lohnsteuer  05/2013  1.119,73  Körperschaftsteuer 10-12/2012 412,19  Körperschaftsteuer 01-03/2013 240,43  8 von 15 Seite 9 von 15

**False Positives:**

- `Betrag  Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_122`)


Diese Mittel wurden va für  Materialeinkäufe im Rahmen von Zug um Zug Geschäften verwendet.

**False Positives:**

- `Zug Geschäften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_169`)


Die Geltendmachung einer Haftung ist aber in das Ermessen der Abgabenbehörde gestellt.  Die  belangte Behörde hat diesbezüglich im Haftungsbescheid festgehalten: „Da der Nachweis, dass  Sie ohne Ihr Verschulden gehindert waren, für die Entrichtung der Abgaben zu sorgen, nicht  erbracht werden konnte, muss angenommen werden, dass der Abgabenrückstand durch Ihr  offenbar schuldhaftes Verhalten nicht entrichtet worden ist.

**False Positives:**

- `Ihr Verschulden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_64`)


In der am 30. Juni 2020 durchgeführten mündlichen Verhandlung wurde zunächst durch den  Beschwerdeführer folgendes vorgebracht:  „Ich stand vor der Beanstandungszeit (14:52 Uhr) und vor dem Ausfüllen des zweiten  Parkscheines um 14:45 Uhr mindestens 100 m (geschätzt) in Richtung Justizanstalt  stadtauswärts auf der gleichen Seite.

**False Positives:**

- `Richtung Justizanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `role_followed_name` 💣

**F1:** 0.002 | **Precision:** 0.017 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `d357cad1`  
**Description:**
Captures names immediately following legal roles like 'Senatspräsidenten', 'Hofrat', 'Vizepräsidenten' to avoid matching the title itself.

**Content:**
```
(?:Senatspräsidenten|Senatspräsidentin|Vizepräsidenten|Vizepräsidentin|Hofrat|Hofrätin|Hofräte|Oberlandesgerichtsrat|Landesgerichtsrat|Bezirksgerichtsrat|Rechtsanwalt|Rechtsanwältin|Notar|Notarin|Richter|Richterin)\s+([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)*)\b(?![a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.017 | 0.001 | 0.002 | 176 | 3 | 173 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 173 | 2375 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/137847.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137847.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Marlies Roesecke, Heinrichsbrunn 35, 3592 Greillenstein, Österreich, unvertreten, über die Beschwerde vom 29. Juli 2019 gegen den  Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom  18. Juli 2019 betreffend Abweisung des Antrages vom 19. Februar 2019 auf Gewährung des  Unterschiedsbetrages der Familienbeihilfe und des Kinderabsetzbetrag im Vergleich von deren  nicht indexierter und indexierter Höhe ab Januar2019, Steuernummer 86-380/1195, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marlies Roesecke` (person)
- `Heinrichsbrunn 35, 3592 Greillenstein, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `Finanzamt Österreich` (organisation)
- `86-380/1195` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Viktoria Kreiselmayer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Viktoria Kreiselmayer`(person)
- `Muran Waldhans, BEd`(person)
- `Am Tegel 5, 9831 Waben, Österreich`(address)
- `Corazza Kocholl Laimer Rechtsanwälte OG`(organisation)
- `Finanzamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miroslav Hankel, BEd`(person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_2`)


Das Bundesfinanzgericht beschließt durch den Richter Ri über die Beschwerde vom 25.  November 2019 des Beschwerdeführers Emma Türker, Frauenhofenstraße 13, 5132 Gasteig, Österreich, gegen den Bescheid des  Finanzamtes Linz, 4020 Linz, Bahnhofplatz 7, vom 22. Oktober 2019 betreffend  Einkommensteuer 2018:  I)

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Emma Türker`(person)
- `Frauenhofenstraße 13, 5132 Gasteig, Österreich`(address)
- `Finanzamtes Linz`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Miroslav Treischl`(person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich`(address)
- `Grant Thornton Austria GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Irvin Kurrek  in der Beschwerdesache Alexandra Kesler,  Illyrerweg 5, 4073 Edramsberg, Österreich, (nunmehr Valsyn-Maschinenbau GmbH als Rechtsnachfolgerin der Schameitat Sanitär GmbH, vertreten durch StB,  über die Berufung (nunmehr Beschwerde) vom 21. August 2013 gegen die Bescheide des FA  vom 9. Juli 2013 betreffend Wiederaufnahme der Verfahren hinsichtlich der  Körperschaftsteuer für die Jahre 2009 und 2010 sowie die Körperschaftsteuer für die Jahre  2009 bis 2011 beschlossen:    I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) als nicht  zulässig zurückgewiesen.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Irvin Kurrek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Priv.-Doz. Irvin Kurrek`(person)
- `Alexandra Kesler`(person)
- `Illyrerweg 5, 4073 Edramsberg, Österreich`(address)
- `Valsyn-Maschinenbau GmbH`(organisation)
- `Schameitat Sanitär GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Marianne Liuni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Marianne Liuni`(person)
- `Luigi Wedekämper`(person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Thomas Kreul, Preberstraße 4, 3911 Dietharts, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberatungs` — partial — pred is substring of gold: `DI Heinrich Richter Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Thomas Kreul`(person)
- `Preberstraße 4, 3911 Dietharts, Österreich`(address)
- `DI Heinrich Richter Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Frieda Krein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Frieda Krein`(person)
- `Priv.-Doz.in Elena Kaminskiy`(person)
- `W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `60-936/8299`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Christine Schweinfort  über den Antrag der Kira Ballis, BEd,  Josefiwaldweg 48, 3071 Diemannsberg, Österreich, auf Gewährung der Verfahrenshilfe im Beschwerdeverfahren gegen den  Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020  betreffend Abweisung des Rückzahlungsantrages, Steuernummer 24-406/6946  beschlossen:  I. Der Antrag auf Gewährung der Verfahrenshilfe wird als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Christine Schweinfort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Christine Schweinfort`(person)
- `Kira Ballis, BEd`(person)
- `Josefiwaldweg 48, 3071 Diemannsberg, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `24-406/6946`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Nicola Folprecht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Nicola Folprecht`(person)
- `Florian Abbruzzese, BA`(person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Hüpgen   in der Beschwerdesache des Alois Jeckl, Amlach 6, 2620 Straßhof, Österreich,   betreffend die Bescheide des Finanzamt Waldviertel  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 66-092/6335,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Jeannine Hüpgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Jeannine Hüpgen`(person)
- `Alois Jeckl`(person)
- `Amlach 6, 2620 Straßhof, Österreich`(address)
- `Finanzamt Waldviertel`(organisation)
- `66-092/6335`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Melina Wellenbrock  in der Verwaltungsstrafsache  Gabriele Vogrin, Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich, 1.) über die Beschwerde vom 19.06.2020 gegen die Strafverfügung  des Magistrats der Stadt Wien vom 30.12.2019, zugestellt am 27.02.2020, Geschäftszahl  MA67/196701166656/2019, und 2.) über die Beschwerde vom 19.06.2020 gegen die Strafver- fügung des Magistrats der Stadt Wien vom 20.01.2020, zugestellt am 03.03.2020, Geschäfts- zahl MA67/196701283117/2019, beschlossen:    Die Beschwerden werden als verspätet zurückgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Melina Wellenbrock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Melina Wellenbrock`(person)
- `Gabriele Vogrin`(person)
- `Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)
- `Magistrats der Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131065.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Kirstin Detlef  in der Beschwerdesache  Pawel Wnent, Reinbergweg 21, 9112 Wölfnitz, Österreich, vertreten durch X-Steuerberatung über die Beschwerde vom  19. Februar 2016 gegen den Bescheid des FA Oststeiermark  vom 15. Jänner 2016 betreffend  Feststellung der Einkünfte § 188 BAO 2012 zur Steuernummer 999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Kirstin Detlef`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Kirstin Detlef`(person)
- `Pawel Wnent`(person)
- `Reinbergweg 21, 9112 Wölfnitz, Österreich`(address)
- `X-Steuerberatung`(organisation)
- `FA Oststeiermark`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131109.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Christiane Fredebold  in der Beschwerdesache des  Beschwerdeführers, vertreten durch X-Steuerberatung, über die Beschwerde vom 25.April  2019, beim Finanzamt eingelangt am 29. April 2019, gegen die Bescheide des FA Landeck Reutte  vom  7. Februar 2019 betreffend Einkommensteuer 2016 und 2017 zur Steuernummer  29-137/6865  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Christiane Fredebold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Christiane Fredebold`(person)
- `X-Steuerberatung`(organisation)
- `Finanzamt`(organisation)
- `FA Landeck Reutte`(organisation)
- `29-137/6865`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Georgette Dörger  in der Beschwerdesache der  Roland Wüstemeier, Sebastianplatz 167, 3420 Klosterneuburg, Österreich, über die Beschwerde vom 4. November 2019 gegen die Bescheide  des FA Salzburg-Stadt  vom 30. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017 zur Steuernummer 99-999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Georgette Dörger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Georgette Dörger`(person)
- `Roland Wüstemeier`(organisation)
- `Sebastianplatz 167, 3420 Klosterneuburg, Österreich`(address)
- `FA Salzburg-Stadt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ursula Raubart, Tschupbach 5c, 4144 Karlsbach, Österreich, vertreten durch Rachel Woiczyk, Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 86-917/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ursula Raubart`(person)
- `Tschupbach 5c, 4144 Karlsbach, Österreich`(address)
- `Rachel Woiczyk`(person)
- `Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `86-917/1669`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Annemarie Wittjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Annemarie Wittjen`(person)
- `Samuel Herpel`(person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich`(address)
- `Erwin Baldauf`(person)
- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft`(organisation)
- `Finanzamtes Landeck Reutte`(organisation)
- `39-702/2118`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Wilmerdinger  in der Beschwerdesache Kirsten Constantinescu,  Höhenwald 50, 4822 Primesberg, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-83-382/2498  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Delia Wilmerdinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Delia Wilmerdinger`(person)
- `Kirsten Constantinescu`(person)
- `Höhenwald 50, 4822 Primesberg, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `41-83-382/2498`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Julian Pierchala,  Pracherweg 6, 8635 Gollrad, Österreich, über die Beschwerde vom 6. August 2019 gegen den Bescheid des Finanzamtes  Österreich vom 24. Juli 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018,  Steuernummer 74-273/9351, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Julian Pierchala`(person)
- `Pracherweg 6, 8635 Gollrad, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `74-273/9351`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ralph Staibler, Pregerstraße 17, 4242 Kirchberg, Österreich, über die Beschwerde vom 15. Juni 2019 gegen den Bescheid des Finanzamtes  Österreich, vormals des Finanzamtes Salzburg-Land vom 16. Mai 2019 betreffend die  Wiederaufnahme des Verfahren gemäß § 303 Abs.1 BAO zur Einkommensteuer 2013 sowie die  Bescheide vom 17. Mai 2019 betreffend die Wiederaufnahme der Verfahren gemäß § 303  Abs.1 BAO zur Einkommensteuer 2014 und 2015 zu Steuernummer 92-314/9447  zu Recht  erkannt:   1.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ralph Staibler`(person)
- `Pregerstraße 17, 4242 Kirchberg, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `92-314/9447`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Alice Rainprechter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Alice Rainprechter`(person)
- `Ing. Techn R Arthur Kornhass`(person)
- `Gstaudet 21, 9556 Besendorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Sophie Nauman`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman`(person)
- `Prof. Helmut Fürnkäß`(person)
- `Dr Christian Leskoschek`(person)
- `Finanzamtes Österreich`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132289.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Camilla Gembalies  in der Beschwerdesache der  Ost Verdon Systeme, Asangstraße 9c, 9580 Mittewald, Österreich, vertreten durch Apfelbaum & Senkfeil Software GmbH betreffend Beschwerde  vom 22. April 2016 gegen die als Bescheid des Finanzamtes X vom 27. Jänner 2016 intendierte  Erledigung betreffend Festsetzung der Kraftfahrzeugsteuer 01.2014-12.2014 zur StNr 99- 99/9999 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Camilla Gembalies`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Univ.-Prof.in Camilla Gembalies`(person)
- `Ost Verdon Systeme`(organisation)
- `Asangstraße 9c, 9580 Mittewald, Österreich`(address)
- `Apfelbaum & Senkfeil Software GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eugenia Vesen`(person)
- `Apollogasse 213, 5522 Lammertal, Österreich`(address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132524.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132524.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Corinna Royackers  in der Beschwerdesache Lena Grobbing,  Johann Burkl-Gasse 58, 4170 Unterriedl, Österreich, betreffend Beschwerde vom 1. Mai 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 12. April 2019 hinsichtlich Wiederaufnahme § 303 BAO /  ESt 2016,  Steuernummer 94-382/8878  den Beschluss gefasst:  I.  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Corinna Royackers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Corinna Royackers`(person)
- `Lena Grobbing`(person)
- `Johann Burkl-Gasse 58, 4170 Unterriedl, Österreich`(address)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `94-382/8878`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karen Billhard  in der Beschwerdesache der  KEX Solar Entwicklung, Deniflestraße 24, 3032 Rekawinkel, Österreich, vertreten durch Ort, über die Beschwerde vom 6.9.2017 gegen die  Bescheide des Finanzamtes Innsbruck vom 2. August 2017 betreffend Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 und Festsetzung der  Kraftfahrzeugsteuer für die Zeiträume Juli bis Dezember 2014 und Jänner bis Juni 2015 zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 wird abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Karen Billhard`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Karen Billhard`(person)
- `KEX Solar Entwicklung`(organisation)
- `Deniflestraße 24, 3032 Rekawinkel, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Samir Schwahn,  Pichlmoarstraße 73, 3653 Ottenberg, Österreich, über die Beschwerde vom 7. Jänner 2016  gegen den Bescheid des  Finanzamtes Österreich vom 9. Dezember 2015 betreffend Abweisung des Antrags auf  Ausgleichszahlung (Familienbeihilfe 01.2010-12.2015 ) zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 9. Dezember 2015 wird gemäß § 279 Abs. 1 BAO  abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Samir Schwahn`(person)
- `Pichlmoarstraße 73, 3653 Ottenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Erika Matuszcyk  in der Beschwerdesache Hon.-Prof. Hugo Beerbaum,  Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich, über die Beschwerde vom 27.1.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 16.1.2020, SV-Nr, betreffend die Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Jänner 2020 zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Erika Matuszcyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Erika Matuszcyk`(person)
- `Hon.-Prof. Hugo Beerbaum`(person)
- `Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich`(address)
- `Finanzamtes  Innsbruck`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OSR Xenia Gerrit, Bakk. art.,  Märzenkellerberg 15, 3662 Edelsreith, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH, Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 23. Februar 2017 gegen den  Bescheid des Finanzamtes Gänserndorf Mistelbach vom 21. Dezember 2016 betreffend  Einkommensteuer 2014, Steuernummer 68-121/6369, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Xenia Gerrit, Bakk. art.`(person)
- `Märzenkellerberg 15, 3662 Edelsreith, Österreich`(address)
- `gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH`(organisation)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `68-121/6369`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/132957.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132957.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Florens Dykhoff  über die Beschwerden

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Florens Dykhoff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Priv.-Doz. Florens Dykhoff`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/132990.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Veronika Richerd  in der Beschwerdesache des  Priv.-Doz.in Felizia Claus, Mosenthalweg 10, 4076 Holzwiesen, Österreich  vertreten durch StB über die Beschwerde vom 11. Dezember 2019  gegen die Bescheide des Finanzamtes vom 18. November 2019 betreffend Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2009 und Einkommensteuer 2009 zu Recht  erkannt:     I. Der Beschwerde gegen den Bescheid betreffend Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2009 wird Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Veronika Richerd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Veronika Richerd`(person)
- `Priv.-Doz.in Felizia Claus`(person)
- `Mosenthalweg 10, 4076 Holzwiesen, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/133011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133011.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Helena Przybilowski  in der Beschwerdesache Michaela Lomanns,  Kolmtaler Weg 694, 4294 Wenigfirling, Österreich, vertreten durch Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H,  Wienerstraße 73, 2604 Theresienfeld, betreffend Beschwerde vom 28. Februar 2020 gegen die  Bescheide des Finanzamtes Baden Mödling vom 31. Jänner 2020 betreffend Einkommensteuer  2015, 2016 und 2017, Steuernummer 73-613/0108, beschlossen:  Die Vorlageanträge vom 16. Februar 2021 gegen die Beschwerdevorentscheidungen 2015,  2016 und 2017 vom 15. Jänner 2021 werden gemäß § 260 Abs. 1 lit b BAO in Verbindung mit  § 264 Abs. 4 lit e BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Helena Przybilowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Helena Przybilowski`(person)
- `Michaela Lomanns`(person)
- `Kolmtaler Weg 694, 4294 Wenigfirling, Österreich`(address)
- `Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `73-613/0108`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/133027.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Helge Angenheyster  in der Beschwerdesache des  [...], [...], Steuernummer 86-194/1844, über die Beschwerde vom 19. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 13. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Helge Angenheyster`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Helge Angenheyster`(person)
- `86-194/1844`(tax_number)
- `Finanzamtes Österreich`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Cathleen Ganczarczyk  in der Beschwerdesache Hon.-Prof. Gregor Liechtenstein,  Platz der Menschenrechte 39, 4652 Reuharting, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, über die Beschwerde vom 28. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 26. November 2020 betreffend Gebühren 29.04.2014  Steuernummer 82-359/1150  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Cathleen Ganczarczyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Cathleen Ganczarczyk`(person)
- `Hon.-Prof. Gregor Liechtenstein`(person)
- `Platz der Menschenrechte 39, 4652 Reuharting, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `82-359/1150`(tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Hon.-Prof.in Sascha Weisenfels  in der Beschwerdesache des  Patrick Kirschbauer, August-Sigl-Straße 501, 3352 St. Peter in der Au-Dorf, Österreich, über die Beschwerde vom 28.März 2012 bzw. 26.April 2012 gegen  die Bescheide des FA X vom 28. Februar 2012 betreffend Kapitalertragsteuer 2007 – 2009 zur  Steuernummer 99-47-826/0792  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Hon.-Prof.in Sascha Weisenfels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Hon.-Prof.in Sascha Weisenfels`(person)
- `Patrick Kirschbauer`(person)
- `August-Sigl-Straße 501, 3352 St. Peter in der Au-Dorf, Österreich`(address)
- `99-47-826/0792`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eleonore Rudloph, Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauerstrasse 39/1/12, 1220 Wien, und Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden je vom  25.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 26. Juli 2016  betreffend Haftung für Abzugsteuer gemäß § 99 EStG 1988 für die Jahre 2012-2014 nach  Durchführung einer öffentlichen mündlichen Verhandlung am 26.04.2021 zu Recht erkannt:   I. a.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Rudloph`(person)
- `Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Delia Kavelmann  in der Beschwerdesache Larissa Rastätter,  Wendelgraben 27, 6563 Galtür, Österreich, vertreten durch Glocknitzer Hollenthoner Stb.GmbH & Co KG,1050 Wien,  Bräuhausgasse 37/4, 1150 Wien, über die Beschwerde vom 10. April 2012 gegen den Bescheid  des FA Wien 9/18/19 Klosterneuburg vom 14. März 2012 betreffend Festsetzung des  Dienstgeberbeitrages 2006 bis 2009 Steuernummer abc zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben:  I. Die Beschwerde hinsichtlich Dienstgeberbeitrag für die Ärztinnen Dr. U und PhD Isaak Joern wird  abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Delia Kavelmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Delia Kavelmann`(person)
- `Larissa Rastätter`(person)
- `Wendelgraben 27, 6563 Galtür, Österreich`(address)
- `FA Wien 9/18/19 Klosterneuburg`(organisation)
- `PhD Isaak Joern`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Frederike Bookholdt  in der Beschwerdesache DDr. Dr. Lorenz Wachenhusen,  Am Lurnbichl 4, 4871 Redl, Österreich, vertreten durch Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Eduard-Wallnöfer-Platz 1, 6460 Imst, über die Beschwerde vom  10. Juni 2013 gegen den Bescheid des FA Landeck Reutte (nunmehr FA Österreich) vom 15. Mai  2013, StrNr, betreffend Festsetzung der Normverbrauchsabgabe für den Zeitraum März 2012  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Frederike Bookholdt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Frederike Bookholdt`(person)
- `DDr. Dr. Lorenz Wachenhusen`(person)
- `Am Lurnbichl 4, 4871 Redl, Österreich`(address)
- `Kapferer Frei und Partner Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `FA Landeck Reutte`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/134157.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Elena Leinenkugel  in der Beschwerdesache der Bf,  vertreten durch StB, über die Beschwerden vom 27. Oktober 2017 gegen die Bescheide des  Finanzamtes vom 25. September 2017 betreffend die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2013 und Körperschaftsteuer 2013 zu Steuernummer  41-600/1876    I. zu Recht erkannt: Der Beschwerde gegen den Bescheid über die Wiederaufnahme des  Verfahrens hinsichtlich Körperschaftsteuer 2013 wird Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Elena Leinenkugel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Elena Leinenkugel`(person)
- `Finanzamtes`(organisation)
- `41-600/1876`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ilona Eißrich  in der Beschwerdesache Prof. Priv.-Doz. Johann Engelkemeier,  Wintenstraße 28j, 4076 Sankt Marienkirchen an der Polsenz, Österreich, über die Beschwerde vom 26. Februar 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. Februar 2021 betreffend Gebühren 2020 Steuernummer  02-891/6290  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Ilona Eißrich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Ilona Eißrich`(person)
- `Prof. Priv.-Doz. Johann Engelkemeier`(person)
- `Wintenstraße 28j, 4076 Sankt Marienkirchen an der Polsenz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `02-891/6290`(tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lorena Zydat  in der Beschwerdesache Knut Duchoslav,  Felbauweg 4, 8435 Wagendorf, Österreich, vertreten durch Dr. Heinz Häupl Rechtsanwalts GmbH, Stockwinkl 18, 4865  Nußdorf/Attersee, über die   1) Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamt Purkersdorf  vom 9. August  2019 betreffend Festsetzung von ersten Säumniszuschlägen in Höhe von 128,38 €,  568,79 € und 266,87 €;  2) Beschwerde vom 15. Oktober 2019 gegen den Bescheid des FA Purkersdorf  vom 13.  September 2019 über die Abweisung eines Aussetzungsantrages;

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Lorena Zydat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Lorena Zydat`(person)
- `Knut Duchoslav`(person)
- `Felbauweg 4, 8435 Wagendorf, Österreich`(address)
- `Dr. Heinz Häupl Rechtsanwalts GmbH`(organisation)
- `Finanzamt Purkersdorf`(organisation)
- `FA Purkersdorf`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/134234.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134234.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Geraldine Klebes  in der Beschwerdesache Jeannine Dictus  Adr.,  über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid über die Aufhebung gemäß  § 299 BAO des Finanzamtes Graz-Umgebung vom 2. Dezember 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 und über die Beschwerde vom 10. März  2020 gegen den Bescheid des Finanzamtes Graz-Umgebung vom 9. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019, Steuernummer 35-674/7682, zu  Recht erkannt:   Die Beschwerde gegen den Bescheid über die Aufhebung gemäß § 299 BAO vom 02.12.2020  wird als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Geraldine Klebes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Geraldine Klebes`(person)
- `Jeannine Dictus`(person)
- `Finanzamtes Graz`(organisation)
- `Finanzamtes Graz`(organisation)
- `35-674/7682`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/134456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134456.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Linn Benli  in der Beschwerdesache Lewis Wiechard,  Platteckweg 9, 4731 Pertmannshub, Österreich, über die Beschwerde gegen den Bescheid des (damaligen) Finanzamtes  Feldkirch vom 20.5.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 61-563/9200, zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Linn Benli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Linn Benli`(person)
- `Lewis Wiechard`(person)
- `Platteckweg 9, 4731 Pertmannshub, Österreich`(address)
- `Finanzamtes`(organisation)
- `61-563/9200`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/134512.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134512.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Diana Grambusch  in der Beschwerdesache Adalbert Gruenaeugl,  Schloßbauerweg 3, 2474 Gattendorf, Österreich, über die Beschwerde vom 24. Juni 2020 gegen den Bescheid des Finanzamtes  Feldkirch vom 23. Juni 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu  Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Diana Grambusch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Diana Grambusch`(person)
- `Adalbert Gruenaeugl`(person)
- `Schloßbauerweg 3, 2474 Gattendorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/134737.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134737.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Corinna Dergwill  in der Beschwerdesache Ilona Ewersmeyer,  Adr2, über die Beschwerden gegen die Bescheide des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf,   - die Beschwerde vom 27. Mai 2016 gegen den Bescheid vom 27. April 2016 betreffend  Einkommensteuer 2013  - die Beschwerde vom 3. Juli 2017 gegen den Bescheid vom 23. Juni 2017 betreffend  Einkommensteuer 2014  - die Beschwerde vom 27. Mai 2016  gegen den Bescheid vom 28. April 2016 betreffend  Einkommensteuer 2015  - die Beschwerde vom 6. Juli 2017  gegen den Bescheid vom 8. Juni 2017 betreffend  Einkommensteuer 2016,  Steuernummer 05-335/0344, zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Corinna Dergwill`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Corinna Dergwill`(person)
- `Ilona Ewersmeyer`(person)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf`(organisation)
- `05-335/0344`(tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/135135.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Susanne Staschik  in der Beschwerdesache Serena Meierott, MSc,  Fiedelau 6, 9571 Sirnitz-Sonnseite, Österreich, über die Beschwerde vom 18. Juli 2015 gegen den Bescheid des Finanzamtes  Graz-Umgebung vom 15. Juni 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2009, Steuernummer 32-399/0872, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Dr.in Susanne Staschik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Susanne Staschik`(person)
- `Serena Meierott, MSc`(person)
- `Fiedelau 6, 9571 Sirnitz-Sonnseite, Österreich`(address)
- `Finanzamtes  Graz-Umgebung`(organisation)
- `32-399/0872`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Edeltraud Kooper  in der Beschwerdesache des *Bf*,  vertreten durch Rechtsanwälte AB, über die Beschwerde vom 20. November 2017 gegen die  Bescheide des FA Judenburg Liezen  vom 19. Oktober 2015 betreffend Einkommensteuer und  Anspruchszinsen für die Jahre 2005 bis 2008 zu Recht erkannt:  I. Der Beschwerde gegen die Einkommensteuerbescheide für die Jahre 2005 bis 2008  wird teilweise Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Edeltraud Kooper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Edeltraud Kooper`(person)
- `FA Judenburg Liezen`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/135344.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135344.1_3`)


Entscheidungsgründe  Die Beschwerdeführerin (Bf.) erzielt als Richterin Einkünfte aus nichtselbständiger Tätigkeit.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/135431.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135431.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Fiona Halberscheid  in der Beschwerdesache MedR Jan Kothmeier,  Johann-Brunauer-Straße 1, 9020 Klagenfurt, Österreich, vertreten durch Hintermeier & Partner Rechtsanwälte, Andreas Hoferstr 8,  3100 St. Pölten, über die Beschwerden  1) vom 10. April 2019 gegen den Bescheid des Finanzamt Gmunden Vöcklabruck  vom 11. März 2019 betreffend  Festsetzung von ersten Säumniszuschlägen und  2) vom 13. September 2019 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 21. August 2019 und vom  22. August 2019 über die Festsetzung von Aussetzungszinsen  Steuernummer 25-981/8877, zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Fiona Halberscheid`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Fiona Halberscheid`(person)
- `MedR Jan Kothmeier`(person)
- `Johann-Brunauer-Straße 1, 9020 Klagenfurt, Österreich`(address)
- `Hintermeier & Partner Rechtsanwälte`(organisation)
- `Finanzamt Gmunden Vöcklabruck`(organisation)
- `Finanzamt Gmunden Vöcklabruck`(organisation)
- `25-981/8877`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/135629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135629.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Juliana Preissle  in der Beschwerdesache des  OStR Adalbert Rehak, Untere Morgengabe 6, 4150 Märzing, Österreich, vertreten durch murtax Steuerberatungs GmbH, Bundesstraße  13b, 8850 Murau, über die Beschwerde vom 17. März 2021 gegen den Bescheid des FA Niederösterreich Mitte  vom 18. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017  Steuernummer 18-360/7906  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Hon.-Prof.in Juliana Preissle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Priv.-Doz.in Hon.-Prof.in Juliana Preissle`(person)
- `OStR Adalbert Rehak`(person)
- `Untere Morgengabe 6, 4150 Märzing, Österreich`(address)
- `murtax Steuerberatungs GmbH`(organisation)
- `FA Niederösterreich Mitte`(organisation)
- `18-360/7906`(tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/135680.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135680.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Karen Knollmüller, Am Weitblick 15, 5145 Kirchweg, Österreich, vertreten durch Saremba & Schinogl Stb.u.Buchh.KG,  Mießtaler Straße 30, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 31. Mai 2021  gegen den Bescheid des Finanzamtes Österreich vom 27. April 2021 betreffend Festsetzung  einer Zwangsstrafe (Steuernummer 47-692/3685 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Karen Knollmüller`(person)
- `Am Weitblick 15, 5145 Kirchweg, Österreich`(address)
- `Saremba & Schinogl Stb.u.Buchh.KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `47-692/3685`(tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/135732.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135732.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Deborah Cremerius  in der Beschwerdesache Charles Meusel,  Kapitelplatz 11, 9344 Oberort, Österreich, vertreten durch VertretungsNetz SW/Mag Nöstler Johannes, Fabrikstraße 12,  4600 Wels, über die Beschwerde vom 27. März 2018 gegen den Bescheid des Finanzamtes  Grieskirchen Wels vom 27. Februar 2018 betreffend Familienbeihilfe ab 09/2017  Steuernummer 86-132/5999  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Deborah Cremerius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Deborah Cremerius`(person)
- `Charles Meusel`(person)
- `Kapitelplatz 11, 9344 Oberort, Österreich`(address)
- `Finanzamtes`(organisation)
- `86-132/5999`(tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/135942.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135942.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Beatrix Rzepczyk  in der Beschwerdesache Lukas Kükelhan, LLM,  Gut Neudau 11, 8324 Kirchberg an der Raab, Österreich, über die Beschwerde vom 27. April 2020 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 5. März 2020 betreffend Gebühren  21.11.2019 Steuernummer 23-720/1666  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Beatrix Rzepczyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Beatrix Rzepczyk`(person)
- `Lukas Kükelhan, LLM`(person)
- `Gut Neudau 11, 8324 Kirchberg an der Raab, Österreich`(address)
- `Finanzamtes`(organisation)
- `23-720/1666`(tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/136045.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136045.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Bernadette Neunreuther  in der Beschwerdesache Oswald Schelzel,  Lanzing 21, 3623 Kalkgrub, Österreich, über die Beschwerde vom 07. März 2021 gegen die Bescheide des Finanzamtes  Österreich vom 9. Februar 2021 betreffend Abweisung der Anträge auf Wiederaufnahme  hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018 Steuernummer  69-880/2770  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Bernadette Neunreuther`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Bernadette Neunreuther`(person)
- `Oswald Schelzel`(person)
- `Lanzing 21, 3623 Kalkgrub, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `69-880/2770`(tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ali Weibert  in der Beschwerdesache Alana Olfs,  Adr1, vertreten durch GF AA, Adr1, über die Beschwerde vom 16. Oktober 2016 gegen den  Bescheid (Sammelbescheid Punkt II.) des Finanzamtes Landeck Reutte (nunmehr: Finanzamt  Österreich) vom 10. Oktober 2016, StrNr, betreffend die Festsetzung eines  Verspätungzuschlages (hinsichtlich Normverbrauchsabgabe für den Zeitraum April 2014) zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Ali Weibert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Ali Weibert`(person)
- `Alana Olfs`(person)
- `GF AA`(person)
- `Finanzamtes Landeck Reutte`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Emma Drogmöller  in der Beschwerdesache Werner Gernet,  Marksee 9, 3522 Gloden, Österreich, über die Beschwerde vom 23.10.2011 gegen die Bescheide des Finanzamt Wien 2/20/21/22  betreffend Wiederaufnahme des Verfahrens hinsichtlich Körperschaftsteuer für die Jahre 2005  bis 2008 vom 22.9.2011, Wiederaufnahme des Verfahrens hinsichtlich Körperschaftsteuer  2009 vom 23.9.2011, Körperschaftsteuer für die Jahre 2005 bis 2008 vom 22.9.2011,  Körperschaftsteuer 2009 vom 23.9.2011 sowie gegen Umsatzsteuer für die Jahre 2010 und  2011 vom 3.5.2012

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Emma Drogmöller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Emma Drogmöller`(person)
- `Werner Gernet`(person)
- `Marksee 9, 3522 Gloden, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/136202.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136202.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Nicoletta Blümel  über die Beschwerde des Malik Bednors,  Perschling 12, 8230 Ring, Österreich, vom 31. Jänner 2022, gegen die Zurückweisungsbescheides des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 19. Jänner 2022, Zlen.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Nicoletta Blümel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Nicoletta Blümel`(person)
- `Malik Bednors`(person)
- `Perschling 12, 8230 Ring, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Karola Schüttmeyer  in der Beschwerdesache Sieglinde Kraupa,  Im Gütle 38, 8232 Obersafen, Österreich, über die Beschwerde vom 27.06.2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. Juni 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 92-708/1515  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Karola Schüttmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Karola Schüttmeyer`(person)
- `Sieglinde Kraupa`(person)
- `Im Gütle 38, 8232 Obersafen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `92-708/1515`(tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/136998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136998.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Fiona Acikgöz  über die Beschwerde des Gabriel Leroy,  Loretostraße 13, 9504 Villach-Warmbad-Judendorf, Österreich, vom 8. März 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Februar 2022, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Fiona Acikgöz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Fiona Acikgöz`(person)
- `Gabriel Leroy`(person)
- `Loretostraße 13, 9504 Villach-Warmbad-Judendorf, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Helena Kemmerer  in der Beschwerdesache  ÖkR Jeannine Radmacher, Hirsbodenstraße 5, 4710 Neuwies, Österreich, vertreten durch Rechtsanwälte Offer & Partner OG, Museumstraße  16, 6020 Innsbruck, über die Beschwerde vom 4. Mai 2022 gegen den Bescheid des  Finanzamtes Österreich vom 4. April 2022, StrNr, betreffend Zurückweisung des Antrages vom  31.12.2020 auf "Durchführung einer Lohnsteuerprüfung gemäß § 86 EStG" zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Helena Kemmerer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Helena Kemmerer`(person)
- `ÖkR Jeannine Radmacher`(person)
- `Hirsbodenstraße 5, 4710 Neuwies, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/137270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Agatha Ferrari  in der Beschwerdesache Dr. OStR Vivian Stinneßen,  Schwaigergasse 12, 9911 Unterassling, Österreich, über die Beschwerde vom 18. November 2019 gegen den Bescheid des  Finanzamtes Österreich (vormals: FA Ort1) vom 5. November 2019, SV-Nr, betreffend die  Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag für  den Zeitraum März 2018 bis Juni 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Agatha Ferrari`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Agatha Ferrari`(person)
- `Dr. OStR Vivian Stinneßen`(person)
- `Schwaigergasse 12, 9911 Unterassling, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_1`)


BESCHLUSS-VERFAHRENSHILFE   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. über den Antrag auf  Gewährung der Verfahrenshilfe des Antragstellers Oliver Simmer Schwag 3, 4852 Steinwand, Österreich, vertreten durch  Franka Reissl, vom 17.5.2022 für das Beschwerdeverfahren betreffend Beschwerde  gegen den Bescheid über die Festsetzung von Aussetzungszinsen des Finanzamtes Österreich  vom 21.6.2019 zur Steuernummer 28-382/0919  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe gemäß § 292 BAO wird abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Oliver Simmer`(person)
- `Schwag 3, 4852 Steinwand, Österreich`(address)
- `Franka Reissl`(person)
- `Finanzamtes Österreich`(organisation)
- `28-382/0919`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/137558.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Othmar Oelhaf, In der Stockwiesen 24, 4730 Gewerbepark Süd, Österreich, vertreten durch Ilse Maria Bereuter-Hauser, Ofnerstraße 25, 2232 Deutsch-Wagram,  betreffend Beschwerde vom 6. März 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22, nunmehr Finanzamt Österreich, vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 03-656/5352  beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO i.V.m. § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Othmar Oelhaf`(person)
- `In der Stockwiesen 24, 4730 Gewerbepark Süd, Österreich`(address)
- `Ilse Maria Bereuter-Hauser`(person)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)
- `03-656/5352`(tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/137603.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137603.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Farina Spitzner  in der Beschwerdesache Laurence Swintek,  Spechtenhauserstraße 10, 3151 Reitzersdorf, Österreich, vertreten durch Dr. Helmut Grubmüller, Weyrgasse 5, 1030 Wien, über die  Beschwerde vom 22. Jänner 2020 gegen den Bescheid des Magistrats der Stadt Wien,  Rechnungs und Abgabenwesen, Referat Landes- und Gemeindeabgaben vom 23. Dezember  2019 betreffend Kommunalsteuer 2014 bis 2016, Steuernummer MA 6/***, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Farina Spitzner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Farina Spitzner`(person)
- `Laurence Swintek`(person)
- `Spechtenhauserstraße 10, 3151 Reitzersdorf, Österreich`(address)
- `Dr. Helmut Grubmüller`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/137652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger  in der Beschwerdesache KommR Manuel Schmeikal,  Fimbabahnweg 6, 8993 Gößl, Österreich, über die Beschwerde vom 13. Juni 2019 gegen den Bescheid des Finanzamt St. Johann Tamsweg Zell am See  vom 3. Juni 2019 über die Rückforderung zu Unrecht bezogener Beträge Familienbeihilfe und  Kinderabsetzbetrag für März 2018 bis Mai 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger`(person)
- `KommR Manuel Schmeikal`(person)
- `Fimbabahnweg 6, 8993 Gößl, Österreich`(address)
- `Finanzamt St. Johann Tamsweg Zell am See`(organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/138054.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138054.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Dipl. Kfm. Ilhan von Hesse,  Lendorfgasse 11, 9831 Grafenberg, Österreich, Tschechien über die Beschwerde vom 29. April 2020 gegen den Bescheid des  ehemaligen Finanzamtes Amstetten Melk Scheibbs (nunmehr des Finanzamtes Österreich )  vom 9. April 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 20-194/7632  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl. Kfm. Ilhan von Hesse`(person)
- `Lendorfgasse 11, 9831 Grafenberg, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes Österreich`(organisation)
- `20-194/7632`(tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/138114.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138114.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Wendelin Sadlers, Festgasse 39, 8950 Niederhofen, Österreich, (Beschwerdeführer, abgekürzt: Bf.), über die Beschwerde des Bf. vom 13. Mai 2021  gegen das Straferkenntnis des Magistrates der Stadt Wien vom 3. Mai 2021, GZ.  MA67/GZ/2021, betreffend eine am 17. September 2020 begangene Verwaltungsübertretung  nach § 2 in Verbindung mit § 4 Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idgF, beschlossen:  I.) Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR)   wird das Beschwerdeverfahren eingestellt, weil das angefochtene Straferkenntnis vom  3. Mai 2021 gemäß § 43 Abs. 1 VwGVG von Gesetzes wegen mit Ablauf des 13. August  2022 außer Kraft getreten ist,   und wird das zugrundeliegende Verwaltungsstrafverfahren eingestellt.  II.)

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Wendelin Sadlers`(person)
- `Festgasse 39, 8950 Niederhofen, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/138117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138117.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Mag.a Ulrike Maletschek  in der Beschwerdesache Monika Mateja,  Niedertorplatz 135, 9521 Pölling, Österreich, über die Beschwerde vom 9. August 2013 gegen die Bescheide des FA Landeck Reutte  vom 11. Juli 2013 betreffend Einkommensteuer und Umsatzsteuer der Jahre 2009 bis 2011,  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Mag.a Ulrike Maletschek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Mag.a Ulrike Maletschek`(person)
- `Monika Mateja`(person)
- `Niedertorplatz 135, 9521 Pölling, Österreich`(address)
- `FA Landeck Reutte`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Richterin Dr.in Elisabeth Hafner als Vorsitzende, die  Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. sowie die fachkundige Laienrichterin Eva  Maiwald-Wanderer und den fachkundigen Laienrichter Mag. Josef Bramer in der  Beschwerdesache Raimund Figgen, Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich, über die Beschwerde vom 13. August 2019  gegen den Bescheid des Finanzamtes Österreich vom 1. August 2019, vertreten durch Ilse  König, Bakk.

**False Positives:**

- `Maga` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Elisabeth Hafner`(person)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eva  Maiwald-Wanderer`(person)
- `Mag. Josef Bramer`(person)
- `Raimund Figgen`(person)
- `Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Ilse  König, Bakk.`(person)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/138506.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138506.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Svenja Lilienfeld  in der Beschwerdesache  Danielle Ganczarsky, Kaiserschildstraße 60, 3843 Lexnitz, Österreich, Niederlande, vertreten durch X-SteuerberatungsGmbH, betreffend  die Beschwerde vom 22. Oktober 2021 gegen die zur Steuernummer 98-974/5862  ergangenen Bescheide des Finanzamt Oststeiermark  vom 27. Mai 2021 betreffend Umsatzsteuer 2010 - 2019  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Svenja Lilienfeld`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Univ.-Prof.in Svenja Lilienfeld`(person)
- `Danielle Ganczarsky`(person)
- `Kaiserschildstraße 60, 3843 Lexnitz, Österreich`(address)
- `X-SteuerberatungsGmbH`(organisation)
- `98-974/5862`(tax_number)
- `Finanzamt Oststeiermark`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/138586.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138586.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Madeleine Hövelberndt  in der Beschwerdesache Lubomir Loedermann,  Am Schierlinggrund 17y, 2111 Harmannsdorf, Österreich, betreffend Beschwerde vom 15. März 2021 gegen den Bescheid des  Finanzamtes Österreich vom 27. Februar 2017 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2016, Steuernummer 71-149/0172, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Madeleine Hövelberndt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Madeleine Hövelberndt`(person)
- `Lubomir Loedermann`(person)
- `Am Schierlinggrund 17y, 2111 Harmannsdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `71-149/0172`(tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Margarete Söhn  in der Beschwerdesache Dora Diel,  Pertitschach 2, 4120 Unterfeuchtenbach, Österreich, über die Beschwerde vom 22. April 2021 gegen die Bescheide des Finanzamtes  Österreich vom 14. April bzw. 16. April bzw. 20. April 2021 betreffend Feststellung der  Einkünfte gemäß § 188 BAO für 2016 bis 2020, Steuernummer 51-014/4875, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Margarete Söhn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Margarete Söhn`(person)
- `Dora Diel`(person)
- `Pertitschach 2, 4120 Unterfeuchtenbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `51-014/4875`(tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/138705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Herbert Schober BA über die Beschwerde des  Kordelia Henschke, Schlägerbergweg 7, 4672 Pühret, Österreich, vom 21. September 2022, gegen das Straferkenntnis des  Magistrats der Stadt Wien, Magistratsabteilung 67 - Parkraumüberwachung, als  Abgabenstrafbehörde, vom 16. September 2022, Zahl MA67/Zahl/2022, betreffend eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:   I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Herbert Schober` — partial — pred is substring of gold: `Herbert Schober BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Herbert Schober BA`(person)
- `Kordelia Henschke`(person)
- `Schlägerbergweg 7, 4672 Pühret, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/138766.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138766.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Sophie Szcygiel  in der Beschwerdesache Veronika Krenzin, LLM,  Allramstraße 3, 3925 Dietrichsbach, Österreich, vertreten durch ARNOLD Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerden vom 14. Juni 2019 gegen die Bescheide des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel als Vorgängerorganisation des Finanzamts  Österreich, Dienststelle Sonderzuständigkeiten, vom 9. Mai 2019 betreffend   50 Säumniszuschläge für die Monate   Jänner 2014 bis Februar 2017 und Mai 2017 bis April 2018,  Steuernummer 33-539/1315  zu Recht erkannt:     I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Sophie Szcygiel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Sophie Szcygiel`(person)
- `Veronika Krenzin, LLM`(person)
- `Allramstraße 3, 3925 Dietrichsbach, Österreich`(address)
- `Finanzamtes für  Gebühren`(organisation)
- `Finanzamts  Österreich`(organisation)
- `33-539/1315`(tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/138982.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. James von Loewenich  in der Beschwerdesache Isidor Märklin,  Beintratten 4C, 1190 Weidling, Österreich, vertreten durch Mag. Marion Riezinger, Grieskirchner Straße 9/4/3, 4600 Wels,  über die Beschwerde vom 25. Februar 2016 gegen den Bescheid des Finanzamtes Freistadt  Rohrbach Urfahr vom 26. Jänner 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 Steuernummer 54-029/5365  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. James von Loewenich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. James von Loewenich`(person)
- `Isidor Märklin`(person)
- `Beintratten 4C, 1190 Weidling, Österreich`(address)
- `Mag. Marion Riezinger`(person)
- `Finanzamtes`(organisation)
- `54-029/5365`(tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/139204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Priv.-Doz.in Juri Eßwein  in der Beschwerdesache Alexander Mutter,  Kraftwerkring 43, 8362 Fürstenfeld, Österreich, über die Beschwerde vom 24. März 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. März 2022, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  Familienbeihilfe für den Zeitraum März 2020 bis Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Priv.-Doz.in Juri Eßwein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Priv.-Doz.in Juri Eßwein`(person)
- `Alexander Mutter`(person)
- `Kraftwerkring 43, 8362 Fürstenfeld, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Helwege  in der Beschwerdesache Techn R Martina Meyerhuber,  Dapontegasse 7, 4273 Neumühl, Österreich, über die Beschwerde vom 4. Oktober 2018 gegen den Bescheid des  Finanzamtes Landeck Reutte, nunmehr Finanzamt Österreich, vom 19. September 2018, SV-Nr,  betreffend Abweisung der Anträge auf Familienbeihilfe und Erhöhungsbetrag zur  Familienbeihilfe vom 27.4.2018 nach Durchführung einer mündlichen Verhandlung zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Petra Helwege`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Petra Helwege`(person)
- `Techn R Martina Meyerhuber`(person)
- `Dapontegasse 7, 4273 Neumühl, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/139570.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139570.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rosemarie Ulmeier  in der Beschwerdesache Waldtriost,  Pratztrumer Straße 9, 8820 Unterwald, Österreich, betreffend den Antrag auf Akteneinsicht der Antragstellerin, vertreten durch  Brauneis Klauser Prändl Rechtsanwälte GmbH, Bauernmarkt 2, 1010 Wien, vom 18.10.2021,  beschlossen:  Der Antrag wird mangels Legitimation als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Rosemarie Ulmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rosemarie Ulmeier`(person)
- `Waldtriost`(organisation)
- `Pratztrumer Straße 9, 8820 Unterwald, Österreich`(address)
- `Brauneis Klauser Prändl Rechtsanwälte GmbH`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/139661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Lukas Nauberg, Hölling 5, 4144 Dittmannsdorf, Österreich, über die Beschwerde vom 15. November 2020  gegen den Bescheid des Finanzamtes Österreich vom 14. Oktober 2020 betreffend Aussetzung  § 212a BAO 2020 nach Durchführung einer mündlichen Verhandlung auf Antrag der Partei am  16.12.2022 in Anwesenheit des Beschwerdeführers und von HR Mag. Christian Schneider und  Mag. Peter Wilhelm für das Finanzamt zur Steuernummer 43-674/4510  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Lukas Nauberg`(person)
- `Hölling 5, 4144 Dittmannsdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `HR Mag. Christian Schneider`(person)
- `Mag. Peter Wilhelm`(person)
- `Finanzamt`(organisation)
- `43-674/4510`(tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/139725.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139725.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Mag.a Rosalia Alberternst  in der Revisionssache Helge Kleinejäger,  Goggerwenig 79, 3925 Schwarzau, Österreich, vertreten durch Rechtsanwälte Zauner Schachermayr Koller & Partner, Graben  21, 4020 Linz, über den Antrag des Revisionswerbers vom 14.2.2023, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 2.1.2023, Geschäftszahl RV/5100155/2020, betreffend  Haftungsbescheid gemäß §§ 9, 80 BAO erhobenen außerordentlichen Revision vom 14.2.2023  die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Rosalia Alberternst`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rosalia Alberternst`(person)
- `Helge Kleinejäger`(person)
- `Goggerwenig 79, 3925 Schwarzau, Österreich`(address)
- `Bundesfinanzgerichtes`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/139969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri über die Beschwerde des Karen Umfrid,  Oisnitz 8, 8674 Rettenegg, Österreich ,Land, vom 21. April 2020, gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart vom 1. April 2020, betreffend Abweisung des Antrags vom 19. Februar  2020 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme einer  Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Nr., zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Karen Umfrid`(person)
- `Oisnitz 8, 8674 Rettenegg, Österreich`(address)
- `Finanzamtes Bruck  Eisenstadt Oberwart`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Andrea Drom  in der Beschwerdesache Corbinian Neumetzler,  Am Haidbach 19, 9620 Obervellach, Österreich, über die Beschwerde vom 6.Mai 2022 gegen den Bescheid des FA Graz-Stadt  vom  12. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021, Steuernummer  85-520/0851, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. Univ.-Prof. Andrea Drom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Univ.-Prof. Andrea Drom`(person)
- `Corbinian Neumetzler`(person)
- `Am Haidbach 19, 9620 Obervellach, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `85-520/0851`(tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/140281.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140281.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Matthew Tschöpe, Mayr-Melnhof-Gasse 27, 5133 Mairhof, Österreich, über die Beschwerde vom 12. Juli 2021 gegen  die Bescheide des Finanzamtes Österreich je vom 28. Juni 2021 betreffend Einkommensteuer  2015 bis 2020 (Steuernummer 97-482/5270 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Matthew Tschöpe`(person)
- `Mayr-Melnhof-Gasse 27, 5133 Mairhof, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `97-482/5270`(tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/140387.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140387.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Daisy Röskens  in der Beschwerdesache KzlR Charlotte Pavelek,  Adr, vertreten durch die XY Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und  Wirtschaftsprüfungsgesellschaft, Adr2, über die Beschwerde vom 14. Juni 2016 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr: Finanzamt Österreich) vom 7. Juni 2016,  StrNr, betreffend   1. die Festsetzung der Normverbrauchsabgabe für den Zeitraum 01/2014 und   2.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Daisy Röskens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Daisy Röskens`(person)
- `KzlR Charlotte Pavelek`(person)
- `XY Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und  Wirtschaftsprüfungsgesellschaft`(organisation)
- `Finanzamtes Landeck Reutte`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Madeleine Runke  in der Beschwerdesache Raimund Ondrouch,  Andreas Hammer-Gasse 101, 4150 Hundbrenning, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich – FAÖ) vom 14. Jänner 2020, SV-Nr,  betreffend Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Mai 2019 bis Juli 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Madeleine Runke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Madeleine Runke`(person)
- `Raimund Ondrouch`(person)
- `Andreas Hammer-Gasse 101, 4150 Hundbrenning, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt Österreich`(organisation)
- `FAÖ`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/140705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Charlotte Klare  in der Beschwerdesache Anselm Pöhlemann,  Ramwoldnerstraße 89, 1040 Wien, Österreich, über die Beschwerde vom 3. September 2021 gegen den Bescheid des  Finanzamt Vorarlberg  vom 19. August 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2020 Steuernummer 67-273/2026  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Charlotte Klare`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Charlotte Klare`(person)
- `Anselm Pöhlemann`(person)
- `Ramwoldnerstraße 89, 1040 Wien, Österreich`(address)
- `Finanzamt Vorarlberg`(organisation)
- `67-273/2026`(tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/141013.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marianne Polmann  in der Beschwerdesache der  Görts+Cebulsky Luftfahrt  und Miteigentümer vertreten durch Rechtsanwälte R, über die Beschwerde vom  20.2.2020 gegen den Grundsteuermessbescheid zum 1.1.2018 – Fortschreibungsveranlagung  gemäß § 21 GrStG 1955 des Finanzamt Klosterneuburg  vom 26. Jänner 2020 zu Einheitswertaktenzeichen E zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Marianne Polmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Marianne Polmann`(person)
- `Görts+Cebulsky Luftfahrt`(organisation)
- `Finanzamt Klosterneuburg`(organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Camilla Tutschek  in der Beschwerdesache des  Karola Poepping, Gemeine Brongen 4, 9433 St. Jakob, Österreich, vertreten durch X-Steuerberatung betreffend Beschwerde vom  20. März 2020 gegen die zur Steuernummer 34-783/3935  ergangenen Bescheide des  FA Niederösterreich Mitte (nunmehr Dienststelle des Finanzamtes Österreich) vom 17. Februar 2020  betreffend Umsatz- und Einkommensteuer 2012 und 2013 beschlossen:  Die angefochtenen Bescheide vom 17. Februar 2020 betreffend Umsatz- und  Einkommensteuer 2012 und 2013 werden gemäß § 278 Abs. 1 BAO aufgehoben und das  Verfahren an die Abgabenbehörde zurückverwiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Camilla Tutschek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Camilla Tutschek`(person)
- `Karola Poepping`(person)
- `Gemeine Brongen 4, 9433 St. Jakob, Österreich`(address)
- `X-Steuerberatung`(organisation)
- `34-783/3935`(tax_number)
- `FA Niederösterreich Mitte`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/141193.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141193.1_1`)


BESCHLUSS-VERFAHRENSHILFE   Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Elvira Janzen  über den Antrag auf Gewährung der  Verfahrenshilfe des Antragstellers Leonie Thalmeyer, Roßmanngasse 172, 4921 Aching, Österreich, vom 10. Juli 2023 für das  Beschwerdeverfahren hinsichtlich der Beschwerden vom 14., 19. und 22. Juli 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 25. Juni 2015 betreffend  Einkommensteuer 2011 bis 2013 und Umsatzsteuer 2010 bis 2013, zu Steuernummer  48-156/9386, nunmehr Steuernummer 12-526/2401, beschlossen:  Dem Antragsteller wird für die Beschwerdeverfahren gegen die o.a. Bescheide Verfahrenshilfe  gemäß § 292 BAO bewilligt.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Elvira Janzen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Elvira Janzen`(person)
- `Leonie Thalmeyer`(person)
- `Roßmanngasse 172, 4921 Aching, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `48-156/9386`(tax_number)
- `12-526/2401`(tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/141476.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141476.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Priv.-Doz.in Mag.a Evelyn Schlötter  in der Beschwerdesache  Laurence Kienitz, St. Michael Ort 8, 8970 Pichl, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid  des Finanzamtes Österreich vom 25. November 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021, Steuernummer 47-758/9641, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Evelyn Schlötter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Evelyn Schlötter`(person)
- `Laurence Kienitz`(person)
- `St. Michael Ort 8, 8970 Pichl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `47-758/9641`(tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Mag.a Helge Kristionat  in der Beschwerdesache Erika Puttfarken,  Robert-Lieben-Straße 7, 4715 Oberolzing, Österreich, über die Beschwerde vom 5. Mai 2014 gegen den Bescheid des Finanzamtes  Innsbruck, nunmehr Finanzamt Österreich, vom 31. März 2014, SV-Nr, betreffend  Inanspruchnahme als Haftungspflichtiger gemäß § 26 Abs. 3 Familienlastenausgleichsgesetz  (FLAG) 1967 und gemäß § 33 Abs. 3 Einkommensteuergesetz (EStG) 1988 für aushaftende  Abgabenschuldigkeiten (dtes. Kindergeld im Zeitraum Jänner 2012 bis März 2013) der Frau B  (Haftungsbescheid), nach Durchführung einer mündlichen Verhandlung zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Mag.a Helge Kristionat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Mag.a Helge Kristionat`(person)
- `Erika Puttfarken`(person)
- `Robert-Lieben-Straße 7, 4715 Oberolzing, Österreich`(address)
- `Finanzamtes  Innsbruck`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/141773.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marianne Heimbold  in der Beschwerdesache des  StR Jessica Muschelknautz, Weichseltalweg 13, 4616 Graßing, Österreich, über die Beschwerde vom 30. Mai 2022 gegen den Bescheid des  Finanzamt Judenburg Liezen  vom 18. Mai 2022 betreffend Pfändung einer Geldforderung zu Steuernummer  91-049/7035  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Marianne Heimbold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Marianne Heimbold`(person)
- `StR Jessica Muschelknautz`(person)
- `Weichseltalweg 13, 4616 Graßing, Österreich`(address)
- `Finanzamt Judenburg Liezen`(organisation)
- `91-049/7035`(tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/141912.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141912.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Anneliese Görth  in der Revisionssache Patrick Leidhäusl,  Windigsteig 19, 3650 Grub bei Aschelberg, Österreich, vertreten durch Mag. Erhard Donhoffer, Ungargasse 4/11, 1030 Wien, über  den Antrag der Revisionswerberin, der beschwerdeführenden Partei, vom 9. Juni 2023 , der  gegen das Erkenntnis des Bundesfinanzgerichtes vom 8. Mai 2023, Geschäftszahl des BFG  RV/7400163/2020 betreffend Wasser- und Abwassergebühren erhobenen außerordentlichen  Revision vom 9. Juni 2023 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in Anneliese Görth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Anneliese Görth`(person)
- `Patrick Leidhäusl`(person)
- `Windigsteig 19, 3650 Grub bei Aschelberg, Österreich`(address)
- `Mag. Erhard Donhoffer`(person)
- `Bundesfinanzgerichtes`(organisation)
- `BFG`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/141996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. über die  Beschwerde der Hon.-Prof.in Cynthia Körber, Madersperger-Straße 52N, 8570 Aichegg, Österreich, vom 10. August 2023, gegen das Straferkenntnis  der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als  Abgabenstrafbehörde vom 13. Juli 2023, GZ. MA67/GZ/2023, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr.  71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Hon.-Prof.in Cynthia Körber`(person)
- `Madersperger-Straße 52N, 8570 Aichegg, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt  Wien`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/142086.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Edeltraud Daubach  in der Beschwerdesache des  Shirley Kettelhut, Orchideenweg 172, 4894 Gewerbegebiet-Salzweg, Österreich, über die Beschwerde vom 2.März 2023, eingebracht am 6. März  2023, gegen den Bescheid des Finanzamt Wien 1/23  vom 7. März 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zur Steuernummer 45-222/8813  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.a Edeltraud Daubach`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Edeltraud Daubach`(person)
- `Shirley Kettelhut`(person)
- `Orchideenweg 172, 4894 Gewerbegebiet-Salzweg, Österreich`(address)
- `Finanzamt Wien 1/23`(organisation)
- `45-222/8813`(tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/142425.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142425.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Benedikt Kastener  in der Beschwerdesache Techn R Dipl.-Ing. Jaqueline Naglschmid,  Strechen 6K, 3872 Amaliendorf, Österreich, vertreten durch MEMO Wirtschaftstreuhandges.m.b.H., Utzstraße 11 Tür 4,  3500 Krems/Donau, über die Beschwerde vom 24. Mai 2017 gegen die Bescheide des  Finanzamtes Österreich vom 26. April 2017 betreffend Säumniszuschlag 01.2012-12.2015  Steuernummer 88-919/1905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Mag. Benedikt Kastener`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mag. Benedikt Kastener`(person)
- `Techn R Dipl.-Ing. Jaqueline Naglschmid`(person)
- `Strechen 6K, 3872 Amaliendorf, Österreich`(address)
- `MEMO Wirtschaftstreuhandges.m.b.H.`(person)
- `Finanzamtes Österreich`(organisation)
- `88-919/1905`(tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/142456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142456.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Carla Jegers  in der Beschwerdesache Gisela Sramek,  Elsniggasse 69, 6364 Brixen im Thale, Österreich, vertreten durch ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG, Plüddemanngasse 87, 8010 Graz, betreffend Beschwerde vom 13. Juni  2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf, nunmehr Finanzamt  Österreich, vom 2. Mai 2019   betreffend Zwangsstrafe gemäß § 111 BAO iVm §§ 5 und 16 WieREG   Steuernummer 18-269/6388  beschlossen:  Der Vorlageantrag wird gemäß § 262 Abs. 1 iVm § 264 Abs. 5 BAO als unzulässig  zurückgewiesen.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof.in Carla Jegers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Carla Jegers`(person)
- `Gisela Sramek`(person)
- `Elsniggasse 69, 6364 Brixen im Thale, Österreich`(address)
- `ASPIDA Rechtsanwälte Siarlidis Huber-Erlenwein  Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `Finanzamt  Österreich`(organisation)
- `18-269/6388`(tax_number)

</details>

---

## `no_title_conjunction` 💣

**F1:** 0.002 | **Precision:** 0.016 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `b6b529df`  
**Description:**
Captures names with prepositions like 'auf der', 'von der' but strictly requires the preceding word to be a valid name component, not a title or institution.

**Content:**
```
(?:auf\s+der\s+|von\s+der\s+|zu\s+der\s+|aus\s+der\s+|an\s+der\s+)([A-Z][a-zäöüßéèêîôû]+(?:\s+[A-Z][a-zäöüßéèêîôû]+)+)\b(?![a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.001 | 0.002 | 188 | 3 | 185 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 185 | 2364 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_245`)


Die Tätigkeiten,  welche die inhaltlichen Voraussetzungen des § 108c Abs. 2 Z 1 EStG 1988 erfüllen, können von  den externen Partnern als eigenbetriebliche F&E-Aktivitäten bzw. von der Thomas Kreul  als  Auftragsforschung geltend gemacht werden.‘   - Mit Eingabe vom 21. Mai 2018 nahm die Bf. zu der ihr übermittelten Begutachtung der FFG  Stellung.

| Predicted | Gold |
|---|---|
| `Thomas Kreul` | `Thomas Kreul` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_32`)


Im Hinblick darauf aber, dass von der Klarissa Hallac  gar keine Beschwerde gegen den Bescheid  vom 04.03.2014 eingebracht worden war, und somit gegenüber der Klarissa Hallac  auch keine  3 von 5 Seite 4 von 5

| Predicted | Gold |
|---|---|
| `Klarissa Hallac` | `Klarissa Hallac` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_24`)


Im Beschwerdejahr 2016 betrieb T ein Studium an der Fachhochschule  Campus Wien und schloss dieses im Juli ab.

**False Positives:**

- `Fachhochschule  Campus Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_171`)


Da sich somit im  vorliegenden Fall sowohl auf der Einnahmen- als auch auf der Ausgabenseite Umstände sowohl  zu Lasten als auch zu Gunsten der Auftragnehmer auswirken konnten, kann im Beschwerdefall  von einem sachverhaltsbezogenen Unternehmerwagnis ausgegangen werden.

**False Positives:**

- `Ausgabenseite Umstände` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_18`)


Der Bf. werde in diesem Zusammenhang um Bekanntgabe ersucht, ob er zum Zeitpunkt der  Zustellung der Strafverfügung nicht nur vorübergehend von der Abgabestelle abwesend  gewesen und insbesondere durch eine Reise, einen Urlaub oder einen Krankenhausaufenthalt  gehindert gewesen sei, von der Zustellung Kenntnis zu nehmen.

**False Positives:**

- `Zustellung Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_41`)


Eine Akzeptanz der von der Firma Ma erhaltenen Erlöse mit Aberkennung der verbundenen  Aufwendungen entbehre jeder Logik.

**False Positives:**

- `Firma Ma` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_21`)


Die Methode bzw. Vorgangsweise wurde wie folgt beschrieben:  Ad 1) die Erstellung von Unterlagen durch die Ferro Montagetechnik GmbH (i.d.F. FMT) nach  eigenen Vorgaben und Erkenntnissen der von der Güssing Energie Technologies (i.d.F. GET)  erzeugten Pilotanlage und den damit erzielten Ergebnissen;

**False Positives:**

- `Güssing Energie Technologies` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_276`)


Auf neue Tatsachen, die der Abgabenbehörde im Laufe des  Beschwerdeverfahrens zur Kenntnis gelangen, ist von der Abgabenbehörde Bedacht zu  nehmen, auch wenn dadurch das Beschwerdeverfahren geändert oder ergänzt wird.

**False Positives:**

- `Abgabenbehörde Bedacht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_14`)


Es handelt sich um eine Anonymverfügung die ich an der Adresse Semperstraße 19 erhalten  habe.

**False Positives:**

- `Adresse Semperstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_15`)


Wie bereits in einigen Telefonaten und emails an das jeweilige Magistrat mitgeteilt,  handelt es sich bei diesem Parkplatz um einen Privatparkplatz der zu der Liegenschaft  Semperstraße 19 gehört.

**False Positives:**

- `Liegenschaft  Semperstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_58`)


In der Bescheidbegründung führte die Behörde  aus:  "Gemäß § 30 Abs. 2 Z 1 EStG 1988 sind von der Besteuerung Einkünfte aus der Veräußerung  von Eigenheimen ausgenommen, wenn sie dem Veräußerer ab der Anschaffung bis zur  Veräußerung für mindestens zwei Jahre durchgehend als Hauptwohnsitz gedient haben und der  Hauptwohnsitz aufgegeben wird oder innerhalb der letzten zehn Jahre vor der Veräußerung  mindestens fünf Jahre durchgehend als Hauptwohnsitz gedient haben und der Hauptwohnsitz  aufgegeben wird.

**False Positives:**

- `Besteuerung Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_6`)


Der Bf. wurde am 14. August 2018 untersucht und von der Neurologin Dr.in B am 28. August  2018 folgendes Gutachten erstellt:  "Anamnese:  Lt. VGA von 9/2015 50% GdB mit Diagnose paranoide Schizophrenie.

**False Positives:**

- `Neurologin Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_259`)


Im Gutachten vom 9.7.2020 wurde dem Bf. von der Sachverständigen Dr.in X, Fachärztin für  Neurologie und Psychiatrie, ein Grad der Behinderung von 60vH seit 7/2020 sowie eine  voraussichtlich dauernde Erwerbsunfähigkeit bescheinigt.

**False Positives:**

- `Sachverständigen Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_68`)


• Abfragemöglichkeiten durch das Kontrollorgan der Parkraumüberwachung  Die Bf. bringt vor, dass sie davon ausgehe, dass die Kontrollorgane der Parkraumüberwachung  auf dem Handcomputer (Personal Digital Computer, kurz: PDA) überprüfen können, ob für  Personen im diplomierten ambulanten Pflegedienst eine Ausnahmebewilligung vorliegt.

**False Positives:**

- `Parkraumüberwachung  Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_65`)


Ich habe den zweiten Gratisparkschein erst gelöst, als ich nach Verlassen des ersten Parkplatzes  das Fahrzeug auf der Höhe Simmeringer Hauptstraße 59 - 61 abgestellt hatte.

**False Positives:**

- `Höhe Simmeringer Hauptstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_16`)


Ansonsten habe er lediglich auf einen Auszug aus der Fachliteratur Bezug genommen.

**False Positives:**

- `Fachliteratur Bezug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_93`)


welche in die Berechnung der Zeit nicht einzubeziehen ist, da die Zeiten des Fußweges nicht zu  berücksichtigen ist), von der Station Wien Volkstheater (U2) bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

**False Positives:**

- `Station Wien Volkstheater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_11`)


Sachverhalt:   Tatsächlich befinde ich mich rechtmäßig in Österreich seit Mai 2015 und seit Oktober 2015 bin  ich ordentliche Studentin an der Wirtschaftsuniversität Wien.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_125`)


Seit dem Wintersemester 2015/16, Beginn 25.09.2015, studiert die Bf. als ordentliche  Studierende an der Wirtschaftsuniversität Wien das Bachelorstudium Wirtschafts- und  Sozialwissenschaften.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_18`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung samt Fotos, welche  von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt wurde.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_11`)


Seine Arbeitsstätte  befinde sich an der Adresse Arbeitgeber, und seine genaue Berufsbezeichnung laute  Triebfahrzeugführer.

**False Positives:**

- `Adresse Arbeitgeber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_8`)


Im Einkommensteuerbescheid vom 21. Oktober 2019 wurden von der Abgabenbörde Einkünfte  aus selbständiger Arbeit in Höhe von 1.274,02 € (1.464,39 € abzüglich 13 % Gewinnfreibetrag)  1 von 5 Seite 2 von 5

**False Positives:**

- `Abgabenbörde Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_23`)


Belege von  der Schule Zeugnisse und Bestätigungen zwischen dem Zeitraum Juli 2014 bis September 2016  in Kopien sind beigelegt.“

**False Positives:**

- `Schule Zeugnisse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_68`)


Das Bundesfinanzgericht weicht mit dem vorliegenden Erkenntnis nicht von der  Rechtsprechungdes Verwaltungsgerichtshofes zu § 303 BAO ab, sondern folgt der in den  Erkenntnissen zB vom 17. Mai 1990, 89/16/0037, vom 24. Februar 2000, 96/15/0149, und vom  21. November 2007, 2006/13/0107 zum Ausdruck gebrachten Judikaturlinie, weshalb die  Revision nicht zuzulassen war.

**False Positives:**

- `Rechtsprechungdes Verwaltungsgerichtshofes` — partial — gold is substring of pred: `Verwaltungsgerichtshofes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_29`)


Von der Bestattung Wien wurden Ihnen mit einer ersten Rechnung vom 6.4.2011 folgende  Kosten in Rechnung gestellt:  Begräbnis Friedhof Malik Stellmaszick, Mittwoch 6.4.2011, 13:00 Uhr:    Mit einer zweiten Rechnung vom 6.4.2011 wurden Ihnen für die Exhumierung und  Wiederbestattung folgende Kosten in Rechnung gestellt:    Von den Friedhöfen Wien wurden Ihnen ebenfalls Leistungen in Rechnung gestellt, welche aber  offenbar von der Bestattung Wien bezahlt und an Sie unter dem Titel "Auslagen in Ihrem  Namen" weiter verrechnet wurden.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Malik Stellmaszick`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_34`)


Betrag setzt sich aus der Summe der von der Bestattung Wien in Rechnung gestellten Kosten  zusammen:    Bei der Todesfallaufnahme wurden folgende Begräbniskosten angeführt:    Dem Finanzamt wurden nur die Rechnungen der Bestattung Wien und der Friedhöfe Wien  vorgelegt.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_55`)


Der Gesamtbetrag wurde von der Bestattung Wien für Sie ausgelegt und Ihnen anschließend als  "Auslagen in Ihrem Namen" weiterverrechnet.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_73`)


Mit einer zweiten Rechnung vom 6.4.2011 wurden von der Bestattung Wien für die  Exhumierung und Wiederbestattung folgende Kosten verrechnet:    Dies steht im Einklang mit den Angaben des Bf. zu den Begräbniskosten bei der  Todesfallaufnahme.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_75`)


Dieser Betrag setzt sich aus der Summe der von der Bestattung Wien in Rechnung  gestellten Kosten zusammen:    9 von 14 Seite 10 von 14

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_89`)


Aus den  vorgelegten Rechnungen ist ersichtlich, dass die Rechnungen der Friedhöfe Wien von der  Bestattung Wien im Namen des Bf. bezahlt und an diesen weiterverrechnet wurden.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_27`)


Grundsätzlich gelten hinterlegte Dokumente gem. § 17 Abs. 3 Zustellgesetz mit dem ersten Tag  der Abholfrist, dies sei der 14. Dezember 2018 gewesen, als zugestellt. Der Bf. werde in diesem  Zusammenhang um Bekanntgabe ersucht, ob er zum Zeitpunkt der Hinterlegung der  Strafverfügung nicht nur vorübergehend von der Abgabestelle abwesend gewesen sei und ob  er insbesondere durch eine Reise, einen Urlaub oder einen Krankenhausaufenthalt gehindert  gewesen sei, von der Zustellung Kenntnis zu erlangen.

**False Positives:**

- `Zustellung Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_77`)


Folge man der Argumentation der Beschwerdeführerin, sei auch das Halten eines  Wettterminals, an welchem der Kunde den Wettvertrag selbst am Gerät abschließen könne,  dann nicht abgabepflichtig, wenn die Benutzer von der Möglichkeit Gebrauch machen würden,  die Wettteilnahme vor der Bezahlung des Einsatzes abzubrechen.

**False Positives:**

- `Möglichkeit Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_14`)


Mit Schreiben vom 2. September 2020 („Verständigung vom Ergebnis der Beweisaufnahme“)  wurde der Bf. von der MA 67 in Kenntnis gesetzt, dass sich aus der Organstrafverfügung sowie  zwei Fotos, welche von einem Organ der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung ausgestellt worden sei, ergebe, dass das näher bezeichnete Fahr- zeug am 28. April 2020 um 19:40 Uhr in Wien 3, Landstraßer Hauptstraße 136, in einer ge- bührenpflichtigen Kurzparkzone ohne einem für den Beanstandungszeitpunkt gültigen Park- schein abgestellt gewesen sei.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_73`)


Der Beschwerdeführer erzielte im Zeitraum 09/2019 bis 12/2019 steuerpflichtige Einkünfte  (von der Landespolizeidirektion Steiermark) in Höhe von 5.075,80 € und im Zeitraum von  01/2020 bis 03/2020 4251,98 € (17.007,92 € : 4).

**False Positives:**

- `Landespolizeidirektion Steiermark` — partial — gold is substring of pred: `Landespolizeidirektion`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Mit "Kauf- und Wohnungseigentumsvertrag" vom 21.10.1998 hatte A (=  Beschwerdeführerin, Bf) von der Lemcon Entwicklung GmbH an der Liegenschaft in EZ1 (= Gst12 im  Gesamtausmaß von 734 m²) 25/481 ideelle Miteigentumsanteile erworben.

**False Positives:**

- `Lemcon Entwicklung` — partial — pred is substring of gold: `Lemcon Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemcon Entwicklung GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_7`)


25/481 Anteile verbunden mit Wohnungseigentum  an der Dachbodeneinheit Top 7 für die Bf.   Erwerbszweck ist der Dachbodenausbau durch die Bf auf ihre alleinigen Kosten (Pkt. III.2.i)  1 von 8 Seite 2 von 8

**False Positives:**

- `Dachbodeneinheit Top` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_41`)


Seit August 2014 bezieht er eine Altersrente von der Liechtensteinischen Alters-  und Hinterlassenenversicherung.

**False Positives:**

- `Liechtensteinischen Alters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_6`)


Gegen diesen Bescheid wurde am 19.09.2014 von der Mieterin Beschwerde erhoben.

**False Positives:**

- `Mieterin Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_25`)


Seit Februar 2016 bezieht sie eine inländische Pension und seit 1. Mai  2017 eine Altersrente von der Liechtensteinischen Alters- und Hinterlassenenversicherung.

**False Positives:**

- `Liechtensteinischen Alters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_3`)


über das von der West Altrader GmbH  Dorf,  eingebrachte Anbringen vom 17. Mai 2021 in Zusammenhang mit dem an Gundula Doerfner, Öttlstraße 14, 3804 Reinsbach, Österreich  ergangenen Straferkenntnis des Magistrates der Stadt Wien vom 7. Mai 2021, GZ.  MA67/Zahl/2021, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, den  Beschluss gefasst:  Das Anbringen vom 17. Mai 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG zurückgewiesen.

**False Positives:**

- `West Altrader` — partial — pred is substring of gold: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Altrader GmbH`(organisation)
- `Gundula Doerfner`(person)
- `Öttlstraße 14, 3804 Reinsbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_161`)


keine Buchführungspflicht besteht und auch nicht freiwillig Bücher geführt  werden, die eine Gewinnermittlung nach § 4 Abs. 1 ermöglichen,  2. die Umsätze im Sinne des § 125 Abs. 1 der Bundesabgabenordnung des  vorangegangenen Wirtschaftsjahres nicht mehr als 220 000 Euro betragen,  3. aus der Steuererklärung hervorgeht, dass der Steuerpflichtige von der  Pauschalierung Gebrauch macht.

**False Positives:**

- `Pauschalierung Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

**False Positives:**

- `Firma Furtnex` — positional overlap with gold: `Furtnex-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnex-Versand GmbH`(organisation)
- `Ronald Jundt`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/134234.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134234.1_11`)


Im Rahmen eines zwischenstaatlichen Informationsaustausches erhielt das Finanzamt am  10.06.2020 Kenntnis darüber, dass der Beschwerdeführer im Jahr 2019 von der Deutschen  Rentenversicherung Bund eine Pensionsauszahlung in Höhe von 2437,02 € erhalten hat.

**False Positives:**

- `Deutschen  Rentenversicherung Bund` — type mismatch — same span as gold: `Deutschen  Rentenversicherung Bund`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Deutschen  Rentenversicherung Bund`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/134388.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134388.1_5`)


Entscheidungsgründe  Der Bf., der im Streitjahr 2019 an der Adresse Adresse wohnhaft war, bezog im Jahr 2019  Einkünfte aus nichtselbständiger Arbeit als Head of Business Development.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/134512.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134512.1_30`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Die im Jahr 1943 geborene Bf. war im Streitjahr durchgehend in Österreich ansässig und erhielt  unter anderem auch zwei Pensionskassenrenten und zwar eine Witwen-Rente von der X  Pensionskasse AG in Höhe von brutto CHF 19.490,30 und Alters-Rente von der Pensionskasse Contrazor AG in Höhe von CHF 7.210,00.

**False Positives:**

- `Pensionskasse Contrazor` — positional overlap with gold: `Contrazor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `X  Pensionskasse AG`(organisation)
- `Contrazor AG`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_30`)


Da die Daten des GWR von der  Statistik Austria dem BMF zur Verfügung gestellt werden und das BMF eine andere Behörde als  das zuständige Finanzamt ist, würde eine Abfrage dieser Daten das Erfordernis einer nach  außen erkennbaren Amtshandlung erfüllen.

**False Positives:**

- `Statistik Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)
- `BMF`(organisation)
- `Finanzamt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_78`)


Das GWR wird von  Gemeinden und Bezirkshauptmannschaften mit Daten befüllt. Das GWR wird von der Statistik  Austria geführt und dem Bundesministerium für Finanzen zur Verfügung gestellt. Die Abfragen  des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel im GWR waren nach außen  erkennbare Amtshandlungen, auch wenn die (elektronische) Erkennbarkeit nur innerhalb des  Finanzressorts gegeben war.

**False Positives:**

- `Statistik  Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/134840.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134840.1_96`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt  Der Beschwerdeführer (infolge Bf) hat seinen Wohnsitz in Österreich an der Wohnsitzadresse  Ehrensdorf 23, 4720 Hading, Österreich (laut ZMR seit 10.3.2011, vorher befand sich der Wohnsitz in L) und bezieht  auch eine Pension von der Pensionsversicherungsanstalt.  Dem zuständigen FA G wurde laut Aktenvermerk vom 28.10.2015 bekannt, dass der Bf.  ausländische (deutsche) Pensionseinkünfte bezieht, die dem Progressionsvorbehalt  unterliegen, daher wurde dem Bf. die Formulare L1i zur ANV für 2010 bis 2014 zur  Beantwortung ausgehändigt.

**False Positives:**

- `Wohnsitzadresse  Ehrensdorf` — positional overlap with gold: `Ehrensdorf 23, 4720 Hading, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ehrensdorf 23, 4720 Hading, Österreich`(address)
- `Pensionsversicherungsanstalt`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/134859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134859.1_78`)


Beispiel  Ein Kleinunternehmer hat im Jahr X1 von der Toleranzregelung Gebrauch gemacht.

**False Positives:**

- `Toleranzregelung Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_279`)


Das Vorbringen, die Annahme einer durchschnittlichen Stereckenlänge von 4,5 km sei zu kurz  bemessen, da Kunden, die sich zu Fuß zu einem Standplatz begeben „eher längere Strecken  fahren“ ist eine durch nichts begründete Behauptung, wohingegen die von der Wiener  Taxiinnung angegebene durchschnittliche Streckenlänge als durch Erfahrungswerte gesichert  angenommen werden kann.

**False Positives:**

- `Wiener  Taxiinnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_9`)


Mit dem angefochtenen Bescheid vom 8. Jänner 2020 forderte das Finanzamt von der  Antragstellerin Andrea Christoffelsmeier  die von ihr für März 2018 bis August 2019 für ihre Tochter  Karola Dannhäußer  bezogenen Beträge an Familienbeihilfe und Kinderabsetzbetrag zurück.

**False Positives:**

- `Antragstellerin Andrea Christoffelsmeier` — partial — gold is substring of pred: `Andrea Christoffelsmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Andrea Christoffelsmeier`(person)
- `Karola Dannhäußer`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_15`)


Hierauf langte die am 22. Jänner 2020 (Datum des Poststempels) zur Post gegebene, von der  Tochter Karola Dannhäußer  im eigenen Namen erhobene Beschwerde beim Finanzamt ein wie  folgt:   Sehr geehrte Damen und Herren,   hiermit lege ich, Karola Dannhäußer, eine Beschwerde gegen die Rückzahlung der Familienbeihilfe  und des Kinderabsetzbetrages ein.

**False Positives:**

- `Tochter Karola Dannhäußer` — partial — gold is substring of pred: `Karola Dannhäußer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karola Dannhäußer`(person)
- `Finanzamt`(organisation)
- `Karola Dannhäußer`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_41`)


Diese brachte vor,  dass ihre Mutter von der Beschwerde Kenntnis hatte und damit auch einverstanden war.

**False Positives:**

- `Beschwerde Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/135828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135828.1_7`)


Sohn habe ab September 2016 auf das Studium Finanz-, Rechnungs- u. Steuerwesen  an der Fachhochschule Wien gewechselt.  1 von 7 Seite 2 von 7

**False Positives:**

- `Fachhochschule Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/135828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135828.1_8`)


Der Bf. erhob gegen den Zurückweisungsbescheid fristgerecht Beschwerde (Schreiben vom  15. Dezember 2017) und brachte vor, dass das Finanzamt in der Begründung des Bescheides  von einem Studienwechsel ausgegangen sei, sein Sohn habe aber lediglich zu seinem  bestehenden Studium an der Wirtschaftsuniversität Wien ein fachverwandtes Parallelstudium  an der Fachhochschule begonnen.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Wirtschaftsuniversität Wien`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/135828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135828.1_22`)


Ab September 2016 wird das Bachelorstudium Finanz-, Rechnungs-und Steuerwesen an der  Fachhochschule Wien der WKW (laut Bestätigung des Studienerfolges für das Studienjahr  2016/17 wurden 62 SemStd.

**False Positives:**

- `Fachhochschule Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/136053.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136053.1_11`)


- Eine Bescheinigung über den Bestand eines festen Wohnsitzes vom 4. Juni 2020 betreffend  seine Ehegattin G, sowie der Töchter K1 und K2 an der Adresse Polen, x;  - mehrere Tankrechnungen;

**False Positives:**

- `Adresse Polen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_40`)


Eine Betrachtung anhand des von der Statistik Austria veröffentlichten Baukostenindex für den  Wohnungsbau Basis Mai 1945 ermögliche, die Preisentwicklung zwischen Mai 1945 und  Juni 2019 nachzuvollziehen.

**False Positives:**

- `Statistik Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Das Fahrzeug MarkeX, FahrgestellNr. 123, erstzugelassen in Deutschland im November 2010,  wurde am 1.12.2011 von der Dyksma Marine GmbH  die seit August 2012 als Alana Olfs (=  Beschwerdeführerin, Bf) mit Sitz in A-Ort1 firmiert, käuflich erworben.

**False Positives:**

- `Dyksma Marine` — partial — pred is substring of gold: `Dyksma Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dyksma Marine GmbH`(organisation)
- `Alana Olfs`(person)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_21`)


In diesen ist zu erkennen, dass der  Mietzins über dem von der Stadt Wien berechnet Mietzins liegt.

**False Positives:**

- `Stadt Wien` — type mismatch — same span as gold: `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_43`)


Zur Reisezulage:  Im Kalenderjahr 2019 war ich einmal für die Organisation "Europäische Grenzschutzagentur  Frontex" in Trapani auf der Insel Silzilien (I) tätig.

**False Positives:**

- `Insel Silzilien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Europäische Grenzschutzagentur  Frontex`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_64`)


Für ein exklusives Wohnprojekt an der Küste  Kroatiens sei für eine österreichische Investorengruppe eine Standortanalyse durchgeführt  worden.

**False Positives:**

- `Küste  Kroatiens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_262`)


Zum Fliegen der Drohnen sei von der Austro Control eine  Pilotenlizenz vorgeschrieben (Beilage 24, S. 2 gelb markiert).

**False Positives:**

- `Austro Control` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_12`)


Weiters habe die Tochter im Sommersemester 2018 (richtig 2019) an der Universität Wien  immatrikuliert und den Studiengang „Kultur- und Sozialanthropologie" inskribiert.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_16`)


Mit Vorhalt vom 4. Februar 2020 wurde die Bf. um Vorlage eines Studienerfolgsnachweises von  T. für das Sommersemester 2019 (Kultur- und Sozialanthropologie an der Uni Wien, (auch  negative Ergebnisse!) sowie um einen Studienerfolgsnachweis der FH Kufstein ab  Studienbeginn ersucht.

**False Positives:**

- `Uni Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FH Kufstein`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_63`)


Im Sommersemester 2019 immatrikulierte T. an der Universität Wien, inskribierte als  ordentliche Studierende das Bachelorstudium „Kultur- und Sozialanthropologie" (UA033 610)  und besuchte die Vorlesungen „Grundlagen sozialwissenschaftlicher Methodologie“ und  „Fachspezifische Einführung“.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_64`)


Sie bereitete sich aber im Laufe des Semesters auf die  Aufnahmeprüfung an der Fachhochschule Kufstein vor;

**False Positives:**

- `Fachhochschule Kufstein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_67`)


Die Aufnahmeprüfung an der Fachhochschule Kufstein bestand die Tochter der Bf.   Seit Oktober 2019 (Wintersemester 2019/20) ist sie als aktiv Studierende an der  Fachhochschule Kufstein Tirol im Bachelorstudiengang Sport-, Kultur- und  Veranstaltungsmanagement (Vollzeit) inskribiert (Inskriptionsbestätigung vom 04.09.2019,  Beschwerdevorbringen).

**False Positives:**

- `Fachhochschule Kufstein` — no gold match — likely missing annotation
- `Fachhochschule Kufstein Tirol` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_122`)


Die Tochter der Bf. absolvierte von Oktober bis Dezember 2018 an der Universidad de Grenada  in Spanien die Kurse „Spanish Grammar, Speaking and Writing Skills“, „History of Art in Spain“  und „Spanish Civilization and Culture“ und begann im Oktober 2019 an der Fachhochschule  Kufstein mit dem Bachelorstudium „Sport-, Kultur- & Veranstaltungsmanagement“.

**False Positives:**

- `Fachhochschule  Kufstein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_142`)


Inskription an der Universität Wien im Studiengang „Kultur- und Sozialanthropologie“  T. war im Sommersemester 2019 an der Universität Wien im Studiengang „Kultur- und  Sozialanthropologie" (UA033 610) inskribiert und hat nach den Angaben der Bf.  (Vorhaltsbeantwortung vom 25. Februar 2020) die Veranstaltungen „Grundlagen  sozialwissenschaftlicher Methodologie“ und „Fachspezifische Einführung“ besucht.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`
- `Universität Wien` — similar text (different position): `Universität Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)
- `Universität Wien`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_147`)


Angesichts des Vorbringens der Bf., ihre Tochter habe sich im Laufe des Semesters für die  Aufnahmeprüfung an der FH Kufstein vorbereitet und keine Prüfungen an der Universität Wien  11 von 13 Seite 12 von 13

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Kufstein`(organisation)
- `Universität Wien`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_156`)


(https://www.fh-kufstein.ac.at/Bewerben/faq/Bewerbung-Aufnahme/Wie-funktionieren-der- Online-Aufnahmetest-und-das-Aufnahmegespraech )  Die Bf. brachte zum zeitlichen Umfang der Vorbereitungszeit ihrer Tochter auf den  Aufnahmetest bei der FH Kufstein lediglich vor, dass T. im Sommersemester 2019 an der  Universität Wien im Studiengang „Kultur- und Sozialanthropologie" (UA033 610) inskribierte  und sich im Lauf des Semesters für die Aufnahmeprüfung an der FH Kufstein (März 2019)  vorbereitet habe.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FH Kufstein`(organisation)
- `Universität Wien`(organisation)
- `FH Kufstein`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_156`)


Die beiden bestehenden Garagentore wurden durch neue von der Firma Palisa ersetzt.

**False Positives:**

- `Firma Palisa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/137291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137291.1_10`)


Begründend führte die belangte Behörde aus:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien erstattet wurde, geht hervor,  dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug an der im Spruch bezeichneten  Örtlichkeit zur angeführten Zeit im Bereich einer gebührenpflichtigen Kurzparkzone abgestellt  war, ohne dass die Parkometerabgabe entrichtet worden ist.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_66`)


Die Parkometerabgabe ist gemäß § 7 (Wiener)  Parkometergesetz 2006 von der Gemeinde Wien – mit Ausnahme eines diesbezüglichen  Verwaltungsstrafverfahrens – im eigenen Wirkungsbereich zu vollziehen.

**False Positives:**

- `Gemeinde Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/138030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138030.1_12`)


Beweis sei durch Einsichtnahme in die Organstrafverfügung erhoben worden, welche von  einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung gelegt worden sei, sowie in die (von diesem) angefertigten Fotos.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_59`)


Beschwerde  Innerhalb offener Frist wurde von der Bf Beschwerde erhoben und im Wesentlichen unter  Hinweis auf § 6 GrEStG – vor Inkrafttreten der Novelle 01.06.2014 – vorgebracht, dass mit der  Schätzung des Architekten Dipl. Ing. J M für das Kaufgrundstück ein gemeiner Wert von ca. €  261.000,00 nachgewiesen worden sei.

**False Positives:**

- `Bf Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/138705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138705.1_8`)


Dem vom Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde mit Bericht  vom 26. September 2022 dem Bundesfinanzgericht als zuständiges Verwaltungsgericht  vorgelegten Verwaltungsstrafakt ist folgender Verfahrensgang zu entnehmen:  Ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien mit der Dienstnummer X  stellte am (Montag) 20. Juni 2022 um 12:54 Uhr fest, dass das mehrspurige Kraftfahrzeug mit  dem behördlichen Kennzeichen 123 (A) in einer gebührenpflichtigen Kurzparkzone in 1230  Wien, Haeckelstraße 4, abgestellt war und dass dieses Kraftfahrzeug nicht mit einem für diesen  Beanstandungszeitpunkt gültigen Parkschein gekennzeichnet war.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_8`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_9`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_68`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Camilla Schiedmann) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Camilla Schiedmann`(person)
- `Wirtschaftsuniversität Wien`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_83`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Finanzamtes`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_120`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_143`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes  Kepler Universität Linz` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_39`)


50 Bei der Prüfung der Behandlung der von der Verordnung Nr. 883/2004 erfassten  Arbeitnehmer kommt es daher auf den wirtschaftlichen Wert dieser Leistungen nicht im  Hinblick auf die Kaufkraft und das Preisniveau am Wohnort der betreffenden Personen, sondern  im Hinblick auf die Höhe der geschuldeten Leistungen an.

**False Positives:**

- `Verordnung Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/138903.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138903.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien am 3. Jänner 2022 um 09:32  Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Am Platz, beanstandet, da zur  Beanstandungszeit ein gültiger Parkschein fehlte.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/139535.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139535.1_41`)


Dies dient bestimmten - die Erfassung der Beträge beim  Empfänger betreffenden - Gesetzeszwecken, an denen sich auch die Ausübung des Ermessens,  von der Bestimmung Gebrauch zu machen, zu orientieren hat (vgl. VwGH 23.08.2022, Ra  2022/13/0072;

**False Positives:**

- `Bestimmung Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/139582.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139582.1_4`)


Lebensjahr vollendete ist seit dem  WS 2020/21 an der Universität Wien bis laufend im Masterstudium des Faches  Betriebswirtschaft inskribiert.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/139582.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139582.1_105`)


Lebensjahr vollendende Beschwerdeführerin (Bf.) ist an der  Universität Wien seit dem WS 2020/21 bis laufend im Masterstudium Betriebswirtschaft  inskribiert.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_153`)


In den von dem Bf. übermittelten Bank-Austria-Kontoauszügen (Konto XYZ in CHF) werden von  der Bank Austria Devisen-Brief-Kurswerte von 1,1936 (zum 31.12.2014) und von 1,1952 (zum  2.2.2015) angeführt (und nicht jene 1,04 laut steuerlicher Vertretung).

**False Positives:**

- `Bank Austria Devisen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_159`)


Erst am 15. Januar 2015 wurde der im September 2011 eingeführte Mindestkurs von 1,20  Schweizer Franken pro Euro von der Schweizerischen Nationalbank (SNB) aufgehoben.

**False Positives:**

- `Schweizerischen Nationalbank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_12`)


Es liege somit ab März  2020 keine Berufsausbildung iSd FLAG vor und bestehe kein Anspruch auf Familienbeihilfe für  T..  Der Bf. brachte in seiner dagegen eingebrachten Beschwerde vom 28. Februar 2022  (eingelangt beim Finanzamt am 01. März 2022) vor, dass seine Tochter im Wintersemester  2015 ihre Sprachstudien an der Universität Wien begonnen und im Oktober 2019 an der  University of Birmingham den Titel Master of Arts (Translation Studies) with Distinction  (Auszeichnung) erworben habe.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Universität Wien`(organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_14`)


Nach Rückkehr aus Großbritannien habe seine Tochter ihre Studien an der Universität Wien im  Wintersemester 2019/20 fortgesetzt und ihre letzte Prüfung am 11. Februar 2020 abgelegt.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_38`)


Mindeststudienzeit um 1 Jahr durch Auslandsstudium, Fortsetzung  der Studien an der Universität Wien und Prüfung zuletzt am 11. Februar 2020 erhalten habe.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_45`)


T. schloss ihr Sprachstudium an der University of Birmingham im Dezember 2019 mit dem Titel  Master of Arts (Translation Studies) with Distinction (Auszeichnung) ab und begann ab dem  Wintersemester 2019 (Oktober 2019) an der Universität Wien das Masterstudium Translation  Deutsch Englisch (A070 331 342).

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_46`)


Die letzte Prüfung an der Universität Wien wurde am 11.  Februar 2020 abgelegt.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_125`)


Zusammenfassend wird Folgendes festgestellt:  Die Tochter des Bf. schloss ihr Sprachstudium an der University of Birmingham im Dezember  2019 mit dem Titel Master of Arts (Translation Studies) with Distinction (Auszeichnung) ab und  begann ab dem Wintersemester 2019 (Oktober 2019) an der Universität Wien mit dem  Masterstudium Translation Deutsch Englisch (A070 331 342).

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_126`)


Die letzte Prüfung an der  Universität Wien wurde am 11. Februar 2020 abgelegt (ab dem SS 2020 keine ECTS-Punkte).

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/140017.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140017.1_5`)


Darunter ein von der Nieder Glanzber GmbH  als Leasinggeber, mit der Beschwerdeführerin (kurz: Bf), FN-h,  damals noch mit dem Firmennamen K-GmbH, als Leasingnehmer, abgeschlossener  Leasingvertrag.

**False Positives:**

- `Nieder Glanzber` — partial — pred is substring of gold: `Nieder Glanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Glanzber GmbH`(organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/140029.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140029.1_24`)


Lebensjahr vollendet und war laut  Studienbestätigung vom 9.4.2021 im Sommersemester 2021 an der Universität Wien im  Studienstatus „ordentlich“ zum UA 032 375 342 Bachelorstudium „Transkulturelle  Kommunikation Polnisch Englisch“ zur Fortsetzung gemeldet.

**False Positives:**

- `Universität Wien` — type mismatch — same span as gold: `Universität Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Universität Wien`(organisation)

</details>

---

## `von_name` 💣

**F1:** 0.000 | **Precision:** 0.001 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `adc92bd5`  
**Description:**
Captures names containing 'von' (e.g., 'Violetta von Amelunxen') but strictly requires the word before 'von' to be a valid name component, preventing matches like 'Dienstverrichtung von Dr'.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)(?:\s*(?:,|\.|\)|$|\s+als\s+|\s+und\s+|\s+von\s+|\s+der\s+|\s+die\s+|\s+den\s+|\s+des\s+|\s+dem\s+|\s+einem\s+|\s+einer\s+|\s+eines\s+|\s+mit\s+|\s+bei\s+|\s+zu\s+|\s+in\s+|\s+auf\s+|\s+an\s+|\s+nach\s+|\s+vor\s+|\s+ohne\s+|\s+um\s+|\s+durch\s+|\s+f\u00fcr\s+|\s+unter\s+|\s+ober\s+|\s+neben\s+|\s+zwischen\s+|\s+entlang\s+|\s+gegen\u00fcber\s+|\s+statt\s+|\s+au\u00dfer\s+|\s+ab\s+|\s+bis\s+|\s+seit\s+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.001 | 0.000 | 0.000 | 1898 | 1 | 1897 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1897 | 2388 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_22`)


Im Jahr 2005 +29 lebte er in Scheidung, rechtskräftig wurde die Gattin in einem Provisorialverfahren zur Zahlung von Unterhalt in Höhe von monatlich € 265,40 ab Juli 2011 verpflichtet.

**False Positives:**

- `Zahlung von Unterhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `2005`(date)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_69`)


Nach dem klaren Gesetzeswortlaut steht jede Art von Unterhaltsleistung einem Eigenanspruch auf Familienbeihilfe entgegen.

**False Positives:**

- `Art von Unterhaltsleistung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_43`)


Der Bf. beitreibe zudem ein „Tennisstüberl“ in welchem die Mitglieder Getränke und eine  beschränkte Anzahl von Speisen zu ermäßigten Preisen beziehen könnten.

**False Positives:**

- `Anzahl von Speisen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_111`)


Auch wenn eine etwaige Mangelhaftigkeit der Begründung eines Bescheides als Verletzung von  Verfahrensvorschriften zu beurteilen wäre, steht dies jedoch der Annahme der  Bescheidqualität der Erledigung nicht entgegen.

**False Positives:**

- `Verletzung von  Verfahrensvorschriften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_118`)


Gewerblich oder beruflich ist jede nachhaltige Tätigkeit zur Erzielung von  Einnahmen, auch wenn die Absicht, Gewinn (Überschuss) zu erzielen, fehlt oder eine  Personenvereinigung nur gegenüber ihren Mitgliedern tätig wird.

**False Positives:**

- `Erzielung von  Einnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_132`)


Zudem wurde durch den Bf. eine Kantine, ein „Tennisstüberl“ betrieben, in welchem Getränke  und eine beschränkte Anzahl von Speisen zu ermäßigten Preisen bezogen werden konnten.

**False Positives:**

- `Anzahl von Speisen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_19`)


Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus den Abgabenbescheiden unter Außerachtlassung von Anzahlungen, nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen.

**False Positives:**

- `Außerachtlassung von Anzahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_48`)


Die Abgabe von Abgabenerklärungen nach Eintritt der Rechtskraft der im Schätzungswege  ergangenen Bescheide erfüllt den behaupteten Neuerungstatbestand jedenfalls nicht, da dem  Bf. sämtliche Daten für die Erstellung der Abgabenerklärungen bereits vorher (mit Ablauf des  Veranlagungsjahres) bekannt waren.

**False Positives:**

- `Die Abgabe von Abgabenerklärungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_26`)


Im Übrigen vertrat die Abgabenbehörde in  der Beschwerdevorentscheidung den Standpunkt, es sei nach der Lebenserfahrung  anzunehmen, dass bei der Durchführung von Wohnungsverkäufen im Rahmen der Errichtung  von Wohnhausanlagen mit mehreren Wohnungen der Veräußerer an einen Rechtsanwalt  oder Notar mit dem Auftrag zur Erstellung eines Mustervertrages herantrete.

**False Positives:**

- `Errichtung  von Wohnhausanlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_32`)


Es sei für die Einbeziehung von Vertragserrichtungskosten in die grunderwerbsteuerliche  Bemessungsgrundlage nicht relevant, ob der Käufer betreffend den Urkundenverfasser ein  Wahlrecht habe, sondern einzig, ob er durch seine Honorierung des Vertragserrichters den  Verkäufer von einer diesbezüglichen Zahlungspflicht befreie.

**False Positives:**

- `Einbeziehung von Vertragserrichtungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_39`)


 Rechtliche Erwägungen  Strittig ist die Abzugsfähigkeit von Fortbildungskosten als Werbungskosten.

**False Positives:**

- `Abzugsfähigkeit von Fortbildungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_55`)


Ferner sind idR nicht abzugsfähig Aufwendungen für den Besuch von Kursen  für neuro-linguistisches Programmieren (NLP), da diese im Regelfall Kenntnisse und  Fähigkeiten vermitteln, die auch für den Bereich der privaten Lebensführung von Bedeutung  sind (VwGH 28.5.2008, 2006/15/0237).

**False Positives:**

- `Besuch von Kursen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_70`)


Dass der  Besuch von Seminaren für neurolinguistisches Programmieren (NLP) oder für Schauspiel und  Performance aber auch im Regelfall Kenntnisse und Fertigkeiten vermitteln, die für den Bereich  der privaten Lebensführung von Bedeutung sind, hat der Verwaltungsgerichtshof wiederholt  bejaht (zB VwGH 29.1.2004, 2000/15/0009;

**False Positives:**

- `Besuch von Seminaren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_58`)


Nachdem sich der Standort des Fahrzeuges aufgrund des Familienwohnsitzes im Inland  befinde, sei für den innergemeinschaftlichen Erwerb des Fahrzeuges die Umsatzsteuer  vorzuschreiben (Fahrzeugeinzelbesteuerung, Lieferung von Italien nach Österreich).

**False Positives:**

- `Lieferung von Italien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_72`)


Die Vorschreibung von  Umsatzsteuer für ein Gebrauchtfahrzeug sei vom Gesetz nicht vorgesehen und unzulässig.

**False Positives:**

- `Die Vorschreibung von  Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_170`)


Ebenso bestimmt Art. 28b Teil A Abs. 1 der Sechsten Richtlinie des Rates vom 17. Mai 1977  (77/388/EWG), dass als Ort eines innergemeinschaftlichen Erwerbs von Gegenständen der Ort  gilt, in dem sich die Gegenstände zum Zeitpunkt der Beendigung des Versands oder der  Beförderung an den Erwerber befinden (vgl. nunmehr Art. 40 der Richtlinie 2006/112/EG des  Rates vom 28.11.2006 über das gemeinsame Mehrwertsteuersystem).

**False Positives:**

- `Erwerbs von Gegenständen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_175`)


Zu  diesen im Rahmen des Gesamtbildes der Verhältnisse zu berücksichtigenden Umständen  gehören u.a. der Ort der gewöhnlichen Verwendung des Gegenstandes, seine Registrierung,  der Wohnort des Erwerbers sowie das Bestehen oder Fehlen von Verbindungen des Erwerbers  zu einzelnen Mitgliedstaaten (Rn. 44 f des angeführten Urteils).

**False Positives:**

- `Fehlen von Verbindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_239`)


In diesem Zusammenhang ist auch auf die Ausführungen von Tumpel in Melhardt/Tumpel,  UStG², Rz 131 zu Art. 1, zu verweisen, wonach mit der Steuerbarkeit und (echten)  Steuerfreiheit der innergemeinschaftlichen Lieferung neuer Fahrzeuge die Möglichkeit des  (nachträglichen) Vorsteuerabzugs für die Anschaffung des neuen Fahrzeugs auch für jene  Personen verbunden ist, die nicht Unternehmer sind oder aus anderen Gründen vom  Vorsteuerabzug ausgeschlossen wären.

**False Positives:**

- `Ausführungen von Tumpel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_248`)


Die Lösung der Frage, ob gegenständlich die Voraussetzungen für einen  innergemeinschaftlichen Erwerb vorgelegen waren, ergibt sich anhand der eingehenden  Würdigung des Sachverhaltes und damit aus der Lösung von Tatfragen.

**False Positives:**

- `Lösung von Tatfragen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_59`)


Im  Dezember 2015 sei er mit seiner Partnerin von Ort nach Ort3 verzogen.

**False Positives:**

- `Partnerin von Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_168`)


Verfügen natürliche Personen über einen Wohnsitz in zwei oder mehreren Staaten, so sind die  Besteuerungsrechte auf Grund von Doppelbesteuerungsabkommen auf die beteiligten Staaten  aufzuteilen.

**False Positives:**

- `Grund von Doppelbesteuerungsabkommen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_27`)


Auch könne beim Kauf von Neoangin, Kalzium,  Vitamintabletten und ähnlichem in Apotheken kein Zusammenhang mit der Behinderung  erkannt werden.

**False Positives:**

- `Kauf von Neoangin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_72`)


Die Art und Weise, wie die Eingaben und Vorlagen der Beschwerdeführerin beurteilt würden,  würde die sie als äußerst schikanös und diskriminieren empfinden und diese Art der  Kommunikation sei eine Verschwendung von Zeit und Geld des Staates Österreich.

**False Positives:**

- `Verschwendung von Zeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_118`)


Bei Zusammentreffen von Krankheiten, die unterschiedliche  Pauschbeträge bedingen, steht nur der jeweils höhere Pauschbetrag zu, wobei jedoch vom  Beschwerdeführer nachzuweisen ist, dass grundsätzlich eine medizinische Diätverpflegung  8 von 10 Seite 9 von 10

**False Positives:**

- `Bei Zusammentreffen von Krankheiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_138`)


Die Beschwerdeführerin stellt einerseits in Frage, ob ein Finanzbeamter über die Kompetenz  verfügt, über die medizinische Notwendigkeit von Heilmaßnahmen zu befinden, weigert sich  jedoch andererseits, eine ärztliche Bestätigung oder Verschreibung vorzulegen und übersieht  dabei offensichtlich, dass denjenigen, der von einer steuerliche Begünstigung Gebrauch  machen möchte, eine erhöhte Beweispflicht trifft.

**False Positives:**

- `Notwendigkeit von Heilmaßnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_72`)


Der GmbH wurden vom FA im Zuge von Prüfungshandlungen bis Dezember 2010  Umsatzsteuern in Gesamthöhe von ca. € 1,9 Mio aufgrund von Umsatzsteuerhinterziehungen  im Zusammenhang mit Heizölverkäufen vorgeschrieben.

**False Positives:**

- `Zuge von Prüfungshandlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_179`)


Dabei sind trotz der beschriebenen  wirtschaftlichen Situation des BF auch generalpräventive Gesichtspunkte von Bedeutung.

**False Positives:**

- `Gesichtspunkte von Bedeutung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_26`)


Im Zeitraum von Jänner bis September 2016  unterzog sich die Tochter der Bf. ärztlich verordneten Skoliosetherapien, wofür  Behandlungskosten iHv insgesamt 4.361,75 € angefallen sind.

**False Positives:**

- `Im Zeitraum von Jänner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_82`)


Diesem Schreiben wurde eine einseitige Liste angeschlossen, die eine medizinische Wirkung  von Weinessig, Wein, Hirschfleisch, Fenchel, Rehfleisch, Sonnenblumenöl kaltgepresst,  Kastanien Bio, Kichererbsen, Honig und Fenchelkörner/Galant sowie deren Zubereitung  beschreibt.

**False Positives:**

- `Wirkung  von Weinessig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Festsetzung von Dienstgeberbeiträgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `Oleg Kreissl`(person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich`(address)
- `Mercuria Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_2`)


Die angefochtenen Abgabenbescheide betreffend Festsetzung von Dienstgeberbeiträgen für  2010 bis 2012 werden gemäß § 279 BAO abgeändert.

**False Positives:**

- `Festsetzung von Dienstgeberbeiträgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Im Zuge einer beim Beschwerdeführer durchgeführten gemeinsamen Prüfung lohnabhängiger  Abgaben (GPLA) betreffend den Beschwerdezeitraum 2010 bis 2012 wurden ua folgende  Feststellungen getroffen:  „Im Prüfungszeitraum wurden die Mitarbeiter [A] und [B], im Rahmen eines mündlichen  Werkvertrages, für Reinigungsarbeiten auf Baustellen und für Be- und Entladen von  Materialien, sowie das Verbringen von Materialien auf den Baustellen beschäftigt.

**False Positives:**

- `Entladen von  Materialien` — no gold match — likely missing annotation
- `Verbringen von Materialien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_21`)


Meine Tätigkeit bestand aus  Zusammenräumen von Baustellen.

**False Positives:**

- `Zusammenräumen von Baustellen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_33`)


Im Prüfungszeitraum 2010 - 2012 waren Hr. [B] und Hr. [A] mit der Durchführung von  Reinigungsarbeiten und mit Abladearbeiten von LKW`s und mit dem Verbringen von  Materialen auf der Baustelle mittels mündlich abgeschlossenen Werkvertrag  beschäftigt.

**False Positives:**

- `Durchführung von  Reinigungsarbeiten` — no gold match — likely missing annotation
- `Verbringen von  Materialen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_37`)


Sie zeigt sich u.a. in der  Vorgabe von Arbeitszeit, Arbeitsort und Arbeitsmittel durch den Auftraggeber sowie die  unmittelbare Einbindung der Tätigkeit in betriebliche Abläufe des Arbeitgebers.

**False Positives:**

- `Vorgabe von Arbeitszeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_43`)


Die erforderlichen Reinigungsutensilien wie Besen, Schaufel und  Reinigungssäcke wurden von Hr. [B] und Hr. [A] selbst beigestellt, wurden allerdings mit  einem vereinbarten Pauschalbetrag von Hr. [Beschwerdeführer] abgegolten.

**False Positives:**

- `Pauschalbetrag von Hr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_72`)


Die Tatsache spricht jedoch nicht gegen das Vorliegen eines  Dienstverhältnisses beim Einzelunternehmen von Hr. [Beschwerdeführer].

**False Positives:**

- `Einzelunternehmen von Hr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_118`)


Schließlich ergab sich das Erfordernis zur  Ausführung von Reinigungsarbeiten und der Verbringung von Baumaterial.

**False Positives:**

- `Ausführung von Reinigungsarbeiten` — no gold match — likely missing annotation
- `Verbringung von Baumaterial` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_134`)


Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens und  der aktenkundigen Unterlagen folgenden entscheidungswesentlichen Sachverhalt fest:  Herr [B] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Aufräumen von Baustellen, bestehend im Zusammentragen und  eigenverantwortlichem Trennen von Bauschutt und -abfällen entsprechend der  Wiederverwertbarkeit‚ einschließlich des Bereitstellens zum Abtransport sowie im  Reinigen von Baumaschinen und Bauwerkzeugen durch Beseitigen von Rückständen  mittels einfacher mechanischer Methoden, wie Abkratzen, Abspachteln und dergleichen  und nachfolgendem Abspritzen mit Wasser, unter Verwendung ausschließlich eigener  Arbeitsgeräte sowie unter Ausschluss der den Denkmal-, Fassaden- und  Gebäudereinigern vorbehaltenen Tätigkeiten einer Grund- oder Bauschlussreinigung“  Herr [A] hatte im Beschwerdezeitraum eine aufrechte Gewerbeanmeldung des freien  Gewerbes:  „Heben, Senken und Befördern von Lasten mittels Einsatzes von mechanischen oder  maschinellen Einrichtungen unter Ausschluss der Beförderung mittels Kraftfahrzeugen“  Herr [B] und Herr [A] führten im Beschwerdezeitraum Baustellenarbeiten entsprechend ihren  Gewerbeberechtigungen für den Beschwerdeführer aus.

**False Positives:**

- `Trennen von Bauschutt` — no gold match — likely missing annotation
- `Reinigen von Baumaschinen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_141`)


Die konkret für den Beschwerdeführer durchgeführten Arbeiten wurden auch von der  belangten Behörde, aufbauend auf die im Verfahren niederschriftlich aufgenommenen,  aktenkundigen Aussagen mit „Reinigungsarbeiten auf Baustellen und für Be- und Entladen von  Materialien, sowie das Verbringen von Materialien auf den Baustellen“ umschrieben.

**False Positives:**

- `Entladen von  Materialien` — no gold match — likely missing annotation
- `Verbringen von Materialien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_142`)


Dass die vereinbarten Arbeitsaufträge mit von den Herrn [B] und [A] selbst beigesteuerten  Werkzeugen und Materialien durchgeführt wurden, wird auch von der belangten Behörde  ausdrücklich festgestellt. Die damit zusammenhängende Feststellung der belangten Behörde:  „Die erforderlichen Reinigungsutensilien wie Besen, Schaufel und Reinigungssäcke wurden von  Hr. [B] und Hr. [A] selbst beigestellt, wurden allerdings mit einem vereinbarten Pauschalbetrag  von Hr. [Beschwerdeführer] abgegolten.“, geht offensichtlich davon aus, dass die  Betriebsmittel der Herrn [B] und [A] zusätzlich und gesondert zum Arbeitshonorar vom  Beschwerdeführer abgegolten worden seien, zum Gegenbeweis dafür, dass die Betriebsmittel  von den Herrn [B] und [A] selbst beigesteuert wurden.

**False Positives:**

- `Pauschalbetrag  von Hr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_17`)


Weiters wurde die Bf. zur Beibringung von Liquiditätsaufstellungen zu den  jeweiligen Fälligkeitstagen aufgefordert, falls die GmbH bereits zu diesen Tagen nicht mehr  über ausreichende Mittel zur Zahlung der Abgaben verfügte.

**False Positives:**

- `Beibringung von Liquiditätsaufstellungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_78`)


Sie  beschränkt sich lediglich mit dem Hinweis auf ein Erkenntnis des Bundesfinanzgerichts, worin  nicht sie, sondern ihr Ehemann bzw. ihr Sohn wegen des Verdachtes der Hinterziehung von  Umsatzsteuervorauszahlungen und Nichtabfuhr von Lohnabgaben verantwortlich gemacht  wurde bzw. keine finanzstrafrechtliche Bestrafung erfolgte, hinzuweisen.

**False Positives:**

- `Hinterziehung von  Umsatzsteuervorauszahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_4`)


In der fristgerecht eingebrachten Beschwerde beantragte der Beschwerdeführer die  „Herstellung des Vertrages zur saisonalisierten Müllentleerung von März bis Oktober des  Kalenderjahres“.

**False Positives:**

- `Müllentleerung von März` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_31`)


Das Gesetz über die Vermeidung und Behandlung von Abfällen und die Einhebung einer hiefür  erforderlichen Abgabe im Gebiete des Landes Wien (Wiener Abfallwirtschaftsgesetz – Wr.  AWG) normiert – soweit im gegenständlichen Fall relevant - Folgendes:  „…  4. ABSCHNITT  Sammlung und Behandlung von Müll  Öffentliche Müllabfuhr  § 16.

**False Positives:**

- `Behandlung von Abfällen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_39`)


Von der öffentlichen Müllabfuhr sind ausgenommen:  1. unbebaute Liegenschaften, auf denen kein regelmäßiger Anfall von Müll zu erwarten ist,  2. Liegenschaften, auf denen durch eine Benützung, die für solche Liegenschaftsarten nach der  allgemeinen Verkehrsanschauung üblich ist, und durch die tatsächliche Benützung durch den  hiezu Berechtigten kein Müll anfällt.  (1a) Bestehen begründete Zweifel, ob die Voraussetzungen gemäß Abs. 1 vorliegen, so ist dies  auf Antrag des Liegenschaftseigentümers oder von Amts wegen mit Bescheid festzustellen.

**False Positives:**

- `Anfall von Müll` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_44`)


(1) Ist die Zufahrt zu mehreren Liegenschaften oder Kleingärten, die nicht gemäß § 18  von der öffentlichen Müllabfuhr ausgenommen sind, wegen der Beschaffenheit des Geländes,  der Durchführung von Bauarbeiten, behördlicher Verfügungen oder technischer oder  betrieblicher Gründe im Bereich der öffentlichen Müllabfuhr nicht oder zeitweise nicht möglich,  oder sind die damit zusammenhängenden Mehrkosten unverhältnismäßig, kann der Magistrat  durch Verordnung festlegen, dass  1. Sammelbehälter im Umleersystem (§ 4 Abs. 4 Z 1) auf einem vom Magistrat festgesetzten  gemeinsamen Sammelbehälterstandplatz zu benützen sind, wobei größere Sammelbehälter für  mehrere Liegenschaften gemeinsam bereitgestellt werden können, oder  2.

**False Positives:**

- `Durchführung von Bauarbeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_87`)


(2) Wird aus dem Gebrauch von öffentlichem Grund ein wirtschaftlicher Nutzen gezogen und ist  aus dieser Tätigkeit nach allgemeinen Erfahrungen ein regelmäßiger Anfall von Müll zu  erwarten, trifft die Abgabepflicht denjenigen, dem der wirtschaftliche Nutzen tatsächlich  zufließt.

**False Positives:**

- `Anfall von Müll` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_57`)


§ 32 AVG normiert:  (1) Bei der Berechnung von Fristen, die nach Tagen bestimmt sind, wird der Tag nicht  mitgerechnet, in den der Zeitpunkt oder das Ereignis fällt, wonach sich der Anfang der Frist  richten soll.

**False Positives:**

- `Berechnung von Fristen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_69`)


Die Rechtsfrage, ob ein Einspruch rechtzeitig oder verspätet eingebracht wurde, ist auf Grund  von Tatsachen zu entscheiden, die die Behörde gemäß § 39 Abs. 2 AVG von Amts wegen  festzustellen hat (vgl. VwGH 03.10.1977, 2583, 2623/76;

**False Positives:**

- `Grund  von Tatsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_90`)


Es konnte somit auf das Vorbringen des Bf., dass seine Daten von Firmen, für welche er nicht  einmal gearbeitet habe, missbräuchlich verwendet worden seien, nicht eingehen.

**False Positives:**

- `Daten von Firmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_83`)


Mit Schreiben vom 03. Dezember 2019 wurden die Beträge von Basispacht, Umsatzpacht,  Betriebskosten und Franchisegebühr mitgeteilt.   Daraufhin wurde mit endgültigem Bescheid vom 15. Jänner 2020 wurde für den Pachtvertrag  eine Gebühr gemäß § 33 TP 5 Abs. 1 Z 1 GebG iHv € 27.989,96 festgesetzt.

**False Positives:**

- `Beträge von Basispacht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_160`)


Zum Urkundeninhalt zählt auch der  Inhalt von Schriften, der durch Bezugnahme zum rechtsgeschäftlichen Inhalt gemacht wird.

**False Positives:**

- `Inhalt von Schriften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_185`)


Der Franchise-Vertrag ist ein Dauerschuldverhältnis, wodurch der Franchisegeber dem  Franchisenehmer gegen Entgelt das Recht einräumt, bestimmte Waren und/oder  Dienstleistungen unter Verwendung von Name, Marke, Ausstattung usw.

**False Positives:**

- `Verwendung von Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_191`)


Bei einem echten  Franchisevertrag treten die Bestandvertragselemente in den Hintergrund und beziehen sich  bestenfalls auf die Nutzung des Knowhow von Marken und Warenzeichen.

**False Positives:**

- `Knowhow von Marken` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_63`)


Der Bundesminister für Finanzen wird  ermächtigt, an Hand geeigneter Kriterien (z. B. Lage, Bebauung) abweichende  Aufteilungsverhältnisse von Grund und Boden und Gebäude im Verordnungswege festzulegen.

**False Positives:**

- `Aufteilungsverhältnisse von Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_189`)


Natürlich habe es Kommissionsvereinbarungen  gegeben, wer überstelle sonst schon ein Fahrzeug von Deutschland nach Österreich auf einen  Verkaufsplatz?

**False Positives:**

- `Fahrzeug von Deutschland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_226`)


Es werde noch einmal darauf hingewiesen, dass es falsch sei, dass eine Lieferung von  Fahrzeugen von der MH an den Bf. stattgefunden habe und daher auch keine Vornahme einer  Erwerbsbesteuerung durch den Bf. möglich gewesen sei.

**False Positives:**

- `Lieferung von  Fahrzeugen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_501`)


Verkauf von Privaten, Verkauf von dem …..

**False Positives:**

- `Verkauf von Privaten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_567`)


C. Rechtslage  1. Artikel 262 CGI  I. Folgendes ist von der Mehrwertsteuer befreit:  (1) Lieferung von Waren, die vom Verkäufer oder in seinem Namen außerhalb der  Europäischen Gemeinschaft versandt oder transportiert werden, sowie von Dienstleistungen, die  in direktem Zusammenhang mit der Ausfuhr stehen;

**False Positives:**

- `Lieferung von Waren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_568`)


(2) Lieferung von Waren, die vom Käufer versandt oder transportiert werden, der nicht in  Frankreich oder in seinem Namen außerhalb der Europäischen Gemeinschaft ansässig ist,  ausgenommen Investitionsgüter und Bunker für Sportboote, Privatflugzeuge oder andere  Transportmittel für den privaten Gebrauch sowie Dienstleistungen, die direkt mit dem Export  verbunden sind.

**False Positives:**

- `Lieferung von Waren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_571`)


In einem Dekret des Staatsrates sind die spezifischen Verfahren für die Anwendung des ersten  Absatzes festgelegt, wenn der Vertreter in einem Land niedergelassen ist, in dem es kein  Rechtsinstrument für die gegenseitige Unterstützung mit einem ähnlichen Umfang wie in der  Richtlinie gibt (2010/24 EU des Rates vom 16. März 2010 über die gegenseitige Unterstützung  bei der Beitreibung von Schulden in Bezug auf Steuern, Abgaben und andere Maßnahmen sowie  durch die Verordnung (EU) Nr. 904/2010 des Rates vom 7. Oktober 2010 über die  administrative Zusammenarbeit und die Betrugsbekämpfung im Bereich der Mehrwertsteuer).

**False Positives:**

- `Beitreibung von Schulden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_573`)


Die Rechnung wird grundsätzlich nach Abschluss der Lieferung oder Leistungserbringung  ausgestellt  - für Lieferungen von Waren, die gemäß Artikel 262 Ter I und Artikel 298 II von Sexies befreit  sind   - und für die Erbringung von Dienstleistungen, für die der Mieter die Steuer gemäß Artikel 196  der Richtlinie zu zahlen hat.

**False Positives:**

- `Lieferungen von Waren` — no gold match — likely missing annotation
- `Erbringung von Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_606`)


In Frankreich gemäß Artikel 262 I CGI von der Mehrwertsteuer befreite Ausfuhren sind  Lieferungen von Gegenständen im Sinne des Artikels 289 I 1 CGI. Die Rechnungen für solche  Ausfuhren müssen daher gemäß den Bestimmungen des CGI ausgestellt werden, wenn es sich  beim Empfänger der Lieferung um einen Steuerpflichtigen oder eine nichtsteuerpflichtige  juristische Person handelt.   b. (1) Gemäß Artikel 289 I 1 CGI in seiner seit 1. Juli 2003 gültigen Fassung muss jeder  Steuerpflichtige dafür sorgen, dass von ihm selbst – oder in seinem Namen und für seine  Rechnung durch seinen Kunden oder einen Dritten – für folgende Umsätze eine Rechnung  ausgestellt wird: Lieferung von Gegenständen oder Erbringung von Dienstleistungen an einen  anderen Steuerpflichtigen oder eine nichtsteuerpflichtige juristische Person.

**False Positives:**

- `Erbringung von Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_625`)


Die Differenzbesteuerung ist somit nur auf Lieferungen von  Gegenständen anzuwenden, die folgendermaßen im Gemeinschaftsgebiet erworben wurden  - von einem Nichtunternehmer,  - von einem Unternehmer aus dem nichtunternehmerischen Bereich,  - von einem steuerbefreiten Unternehmer ohne Vorsteuerabzugsrecht (Kleinunternehmer)  oder  - von einem anderen Unternehmer, der selbst die Differenzbesteuerung angewendet hat (zB  bei Verkäufen von Händler zu Händler).

**False Positives:**

- `Verkäufen von Händler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_633`)


Schutz von Treu und Glauben berufen (Melhart/Tumpel, § 24 Rz 38 mit Verweis auf  Ruppe/Achatz, § 24 Rz 14).

**False Positives:**

- `Schutz von Treu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_657`)


Zur angeblichen Provisionsvereinbarung mit MH wird festgehalten: „Die Vollmacht  betreffend den Verkauf von Fahrzeugen in Österreich im Namen und auf Rechnung der MH (=  Provisionsvereinbarung), die am 30. November 2011 per Mail vom Bf. an die Prüferin  übermittelt wurde, unterscheidet sich zu der bereits in den Unterlagen vorhandenen Vollmacht  in folgenden Punkten: Der Stempel der MH wurde an einer anderen Stelle angebracht.

**False Positives:**

- `Verkauf von Fahrzeugen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_59`)


Der beschwerdegegenständliche Betrag von 268,00 € sei sowohl in absoluter als auch in  relativer Höhe als geringfügig zu werten, selbst unter Berücksichtigung der  Nachforderungsbeträge (Verbrauch von Mindestkörperschaftsteuer) für die ebenfalls  wiederaufgenommenen Veranlagungsjahre 2014 (268,00 €) und 2015 (451,00 €).

**False Positives:**

- `Verbrauch von Mindestkörperschaftsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_66`)


Zur Beschwerde betreffend Veranlagung 2015:  (1) Damit verblieben als weitere Wiederaufnahmegründe für das Veranlagungsjahr 2015 die  Korrektur der Abschreibung eines Bürogebäudes um 1.071,65 € sowie die Nichtanerkennung  von Betriebskosten für eine Wohnung in Wien in Höhe von 734,30 €.   (2) Unter Anwendung eines linearen Körperschaftsteuersatzes von 25% ergebe dies eine  Steuernachforderung für 2015 von rund 451,00 €.  7. Mit Beschwerdevorentscheidung vom 30. Juli 2019 wurde die Beschwerde gegen die  Wiederaufnahmebescheide KÖSt für 2011 bis 2015 als unbegründet abgewiesen.

**False Positives:**

- `Nichtanerkennung  von Betriebskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_86`)


So sei einerseits die Notwendigkeit der  steuerlichen Hinzurechnung der Abschreibungsbeträge aus den vom Unternehmen für 2011  und 2012 eingereichten Unterlagen nicht erkennbar gewesen und es hätte andererseits diese  Hinzurechnung (etwa durch Saldierung von Beträgen) in diversen Kennzahlen versteckt sein  können.

**False Positives:**

- `Saldierung von Beträgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_96`)


Zudem würde selbst ein allfälliges Verschulden der  Abgabenbehörde an der Nichtausforschung von Sachverhaltselementen nach ständiger Rspr  des VwGH die amtswegige Wiederaufnhme des Verfahrens keineswegs ausschließen (VwGH  23.11.2016, Ra 2014/15/0006;

**False Positives:**

- `Nichtausforschung von Sachverhaltselementen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_99`)


Das  Hervorkommen von Tatsachen und Beweismitteln sei aus der Sicht des jeweiligen Verfahrens  zu beurteilen.

**False Positives:**

- `Das  Hervorkommen von Tatsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_114`)


Die obigen Ausführungen würden für die Wiederaufnahme der Körperschaftsteuerverfahren  2013 bis 2015 gleichermaßen gelten, wobei die Entdeckung des Fehlens des  Hinzurechnungsbetrages von Veranlagung zu Veranlagung unwahrscheinlicher geworden sei,  weil das auslösende Ereignis (der Wechsel der steuerlichen Vertretung und damit das  erstmalige Unterbleiben der Hinzurechnung) immer weiter in den Hintergrund getreten sei und  kein Anlass bestanden habe, plötzlich Vergleiche mit dem Veranlagungsjahr 2007 (dem letzten  Jahr der Erfassung des Hinzurechnungsbetrages) zu ziehen.

**False Positives:**

- `Hinzurechnungsbetrages von Veranlagung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_41`)


Das Vorgehen der belangten Behörde verstoße aus diesem Grund zudem  gegen den Grundsatz von Treu und Glauben.

**False Positives:**

- `Grundsatz von Treu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_63`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Auf Basis des oben geschilderten Verwaltungsgeschehens und der aktenkundigen Unterlagen  wird folgender entscheidungswesentlicher Sachverhalt festgestellt:  Zur Geschäftstätigkeit der Beschwerdeführerin gehört laufend der Abschluss von  Bestandverträgen.

**False Positives:**

- `Abschluss von  Bestandverträgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_132`)


Betreffend das Beschwerdevorbringen, die gegenständlichen Bescheide stünden im  Widerspruch zum Grundsatz von Treu und Glauben, ist wie folgt auszuführen:  Eine bei einer abgabenbehördlichen Prüfung für Vorjahre vorgenommene verfehlte  Beurteilung, die sich zu Gunsten des Abgabepflichtigen ausgewirkt hat, ist im Allgemeinen dazu  geeignet, bei diesem die Hoffnung wecken, die Abgabenbehörde werde diese Beurteilung auch  in den Folgejahren beibehalten.

**False Positives:**

- `Grundsatz von Treu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_133`)


Nach der ständigen Rechtsprechung des VwGH schützt der  Grundsatz von Treu und Glauben jedoch nicht ganz allgemein das Vertrauen des  Abgabepflichtigen auf die Rechtsbeständigkeit einer unrichtigen abgabenrechtlichen  Beurteilung in der Vergangenheit (vgl zB VwGH 27.2.2014, 2011/15/0106;

**False Positives:**

- `Grundsatz von Treu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_136`)


Für eine Verletzung des Grundsatzes von Treu und Glauben müssten besondere Umstände  vorliegen, die ein Abgehen von der bisherigen Auffassung durch die Finanzverwaltung unbillig  erscheinen ließen, wie dies zB der Fall sein kann, wenn ein Abgabepflichtiger von der  Abgabenbehörde ausdrücklich zu einer bestimmten Vorgangsweise aufgefordert wurde und  sich nachträglich die Unrichtigkeit dieser Vorgangsweise herausstellt (vgl VwGH 23.9.2010,  2010/15/0135).

**False Positives:**

- `Grundsatzes von Treu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_189`)


Der Verweis der belangten Behörde auf die Rsp des VwGH zur Behandlung von  Mietzinsvorauszahlungen als einmalige Leistung (VwGH 14.12.1994, 94/16/0050;

**False Positives:**

- `Behandlung von  Mietzinsvorauszahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_26`)


Beigelegt wurde eine Schätzung des Verkehrswertes der gegenständlichen Liegenschaft zum  20.8.2011, durchgeführt von einer "Realitätenkanzlei, Ankauf, Verkauf und Vermittlung von  Baugründen, Villen, Zinshäusern, Industrieobjekten, Eigentums- und Mietwohnungen".

**False Positives:**

- `Vermittlung von  Baugründen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_27`)


Zudem eine Überschussrechnung betreffend Einkünfte aus Vermietung und Verpachtung, aus  der sich nach einem Ansatz von Finanzierungskosten in Höhe von 7.245,27 € ein Überschuss  von 6.958,07 € im Jahr 2009 ergibt.

**False Positives:**

- `Ansatz von Finanzierungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_68`)


Bezüglich der AfA-Basis (Anschaffungskosten) wäre vom Beschwerdeführer  2009 überdies kein Anteil von Grund und Boden ausgeschieden worden.

**False Positives:**

- `Anteil von Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_244`)


Rechtliche Begründung  1.  Gemäß § 85 Abs. 1 BAO sind Anbringen zur Geltendmachung von Rechten oder zur Erfüllung  von Verpflichtungen (insbesondere Erklärungen, Anträge, Beantwortungen von  Bedenkenvorhalten, Rechtsmittel) vorbehaltlich der Bestimmungen des Abs. 3 schriftlich  einzureichen (Eingaben).

**False Positives:**

- `Beantwortungen von  Bedenkenvorhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_248`)


Auf § 86a Abs. 2 BAO gestützte Verordnungen sind die Verordnung des Bundesministers für  Finanzen über die Zulassung von Telekopierern zur Einreichung von Anbringen an das  Bundesministerium für Finanzen, an den unabhängigen Finanzsenat, an die  Finanzlandesdirektionen sowie an die Finanzämter und Zollämter, BGBl. 1991/494 idF BGBl. II  2002/395, sowie Verordnung des Bundesministers für Finanzen über die Einreichung von  Anbringen, die Akteneinsicht und die Zustellung von Erledigungen in  automatisationsunterstützter Form (FinanzOnline-Verordnung 2006 - FonV 2006, BGBl. II  2006/9).

**False Positives:**

- `Einreichung von Anbringen` — no gold match — likely missing annotation
- `Einreichung von  Anbringen` — no gold match — likely missing annotation
- `Zustellung von Erledigungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_249`)


Die erstgenannte Verordnung betrifft die Einreichung von Anbringen unter Verwendung eines  Telekopierers (Telefaxgerätes).

**False Positives:**

- `Einreichung von Anbringen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_21`)


Dem  Beschwerdeführer (und seinem Vertreter) war das Fehlen von Inhaltserfordernissen in seinen  Beschwerden schon bei deren Einreichung bewusst.

**False Positives:**

- `Fehlen von Inhaltserfordernissen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_69`)


Das Gebührengesetz knüpft im § 14 TP 6 die Gebührenpflicht nur an den äußeren formalen  Tatbestand der Einbringung einer Eingabe von Privatpersonen an Organe der  Gebietskörperschaften in Angelegenheiten ihres öffentlich-rechtlichen Wirkungskreises, die die  Privatinteressen der Einschreiter betreffen (vgl. VwGH 23.6.1993, 91/15/0129).

**False Positives:**

- `Eingabe von Privatpersonen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_104`)


Einer Aufforderung nach § 162 BAO ist dann nicht entsprochen, wenn ohne Verletzung von  Verfahrensvorschriften die Feststellung getroffen wird, dass die benannten Personen nicht die  tatsächlichen Empfänger der abgesetzten Beträge sind (VwGH 20.12.2017, Ra 2016/13/0041).

**False Positives:**

- `Verletzung von  Verfahrensvorschriften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_111`)


Die vom Bf. als Empfänger von Fremdleistungen im Jahr 2012  im Betrag von € 271.314,-  genannte Firma T kann aufgrund der festgestellten Tatsachen (nicht ausreichende Anzahl von  Dienstnehmern für die verrechneten Leistungen, nur Lager als Firmensitz festgestellt ) nicht als  Empfänger im Sinn des § 162 BAO anerkannt werden.

**False Positives:**

- `Anzahl von  Dienstnehmern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_134`)


Bei der hier vorliegenden Branche (Trockenbau) handelt es sich um eine Risikobrache, bei der  eine erhöhte Sorgfaltspflicht beim Eingehen von Geschäftsbeziehungen zu Grunde zu legen ist.

**False Positives:**

- `Eingehen von Geschäftsbeziehungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_142`)


Auch erscheint dem Bundesfinanzgericht die Bezahlung von Geldbeträgen in Höhe von €  17.000,- bis € 44.000,- in bar gegen Kassaeingangsbeleg weder fremdüblich noch glaubwürdig.

**False Positives:**

- `Bezahlung von Geldbeträgen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_150`)


Die Rechtsfrage der Nichtanerkennung von Betriebsausgaben bei nicht erfolgter  Empfängerbenennung  gemäß § 162 BAO wurde gemäß der Judikatur des  Verwaltungsgerichtshofes entschieden, eine Revision war nicht zuzulassen.

**False Positives:**

- `Nichtanerkennung von Betriebsausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_28`)


Die Begründung der Beschwerde verbleibe allerdings, dass eine  pauschale Ablehnung von Ausgaben und Aufwendungen nicht zulässig sei und - zumal die  Unterlagen für die Beurteilung der Behörde vorgelegen seien - diese zumindest eine der  Wahrheit möglichst nahekommende Schätzung hätte vornehmen müssen.

**False Positives:**

- `Ablehnung von Ausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_45`)


Gemäß § 85 Abs. 1 BAO sind Anbringen zur Geltendmachung von Rechten oder zur Erfüllung  von Verpflichtungen (insbesondere Erklärungen, Anträge, Beantwortungen von  Bedenkenvorhalten, Rechtsmittel) vorbehaltlich der Bestimmungen des § 85 Abs. 3 BAO  schriftlich einzureichen (Eingaben).

**False Positives:**

- `Beantwortungen von  Bedenkenvorhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_59`)


Er  bringt lediglich zum Ausdruck, dass das Finanzamt Werbungskosten und Betriebsausgaben in  einem höheren Ausmaß hätte berücksichtigen müssen, als dies in den angefochtenen  Bescheiden geschehen ist, bezweifelt aber nicht die Berechtigung des Finanzamtes, die  Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2011 und 2012 zu verfügen,  geht er doch selbst davon aus, dass er die von ihm geltend gemachten Werbungskosten und  Betriebsausgaben nicht in vollem Umfang belegen könne und diese daher mangels Vorlage von  Belegen zu schätzen seien.

**False Positives:**

- `Vorlage von  Belegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamtes`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_35`)


§ 67 Abs 8 lit f EStG sehe vor, dass beendigungskausale Bezüge, sofern sie im Rahmen von  Sozialplänen als Folge von „Betriebsänderungen“ iSd § 109 ArbVerfG anfielen und soweit dafür  nicht der Steuersatz von 6% zur Anwendung komme, bis zu einem Betrag von 22.000,00 € mit  der Hälfte des Steuersatzes, der sich bei gleichmäßiger Verteilung des Bezuges auf die Monate  des Kalenderjahres als Lohnzahlungszeitraum ergebe, zu versteuern seien.

**False Positives:**

- `Rahmen von  Sozialplänen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_84`)


(6) Gelindestes Mittel:  Der Gesetzgeber unterscheide nicht zwischen normalen freiwilligen Abfertigungen und solchen  im Rahmen von Sozialplänen.

**False Positives:**

- `Rahmen von Sozialplänen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_112`)


4. Gemäß § 67 Abs 8 lit f EStG sind Bezüge bis zu einem Betrag von 22.000,00 € mit der Hälfte  des Steuersatzes (bei gleichmäßiger Verteilung des Bezuges) zu versteuern, die bei oder nach  Beendigung des Dienstverhältnisses im Rahmen von Sozialplänen als Folge von  7 von 12 Seite 8 von 12

**False Positives:**

- `Rahmen von Sozialplänen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_123`)


Von der Bf. wird auch nicht bestritten, dass Auszahlungen im Rahmen von Sozialplänen  nach § 67 Abs 8 lit f EStG und freiwillige Zahlungen gemäß § 67 Abs 6 EStG prinzipiell dieselbe  steuerliche Behandlung erfahren.

**False Positives:**

- `Rahmen von Sozialplänen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_134`)


Den Erläuterungen kann damit zunächst entnommen werden, dass Auszahlungen im  Rahmen von Sozialplänen nach § 67 Abs 8 lit f EStG, die nach dem 28. Februar 2014  abgeschlossen wurden, ebenso vom Abzugsverbot betroffen sein sollen, wie Zahlungen nach  § 67 Abs 6 EStG.   b. (1)

**False Positives:**

- `Rahmen von Sozialplänen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `academic_suffix_name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `51317fdc`  
**Description:**
Matches person names with academic suffixes (MSc, LL.M., etc.) even without preceding titles. Fixed to handle hyphenated names and suffixes.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)*\s+(?:MSc|LL\.M\.|B\.Sc\.|M\.Sc\.|B\.A\.|M\.A\.|Ph\.D\.|Dr\.\s+iur\.|Bakk\.\s+iur\.|Dipl\.\s+iur\.)(?:\s*,\s*[A-Z][a-zäöüßéèêëïîôùûü]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 16 | 0 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 16 | 2184 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eugenia Vesen`(person)
- `Apollogasse 213, 5522 Lammertal, Österreich`(address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eleonore Rudloph, Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauerstrasse 39/1/12, 1220 Wien, und Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden je vom  25.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 26. Juli 2016  betreffend Haftung für Abzugsteuer gemäß § 99 EStG 1988 für die Jahre 2012-2014 nach  Durchführung einer öffentlichen mündlichen Verhandlung am 26.04.2021 zu Recht erkannt:   I. a.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Rudloph`(person)
- `Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135680.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135680.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Karen Knollmüller, Am Weitblick 15, 5145 Kirchweg, Österreich, vertreten durch Saremba & Schinogl Stb.u.Buchh.KG,  Mießtaler Straße 30, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 31. Mai 2021  gegen den Bescheid des Finanzamtes Österreich vom 27. April 2021 betreffend Festsetzung  einer Zwangsstrafe (Steuernummer 47-692/3685 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Karen Knollmüller`(person)
- `Am Weitblick 15, 5145 Kirchweg, Österreich`(address)
- `Saremba & Schinogl Stb.u.Buchh.KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `47-692/3685`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_1`)


BESCHLUSS-VERFAHRENSHILFE   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. über den Antrag auf  Gewährung der Verfahrenshilfe des Antragstellers Oliver Simmer Schwag 3, 4852 Steinwand, Österreich, vertreten durch  Franka Reissl, vom 17.5.2022 für das Beschwerdeverfahren betreffend Beschwerde  gegen den Bescheid über die Festsetzung von Aussetzungszinsen des Finanzamtes Österreich  vom 21.6.2019 zur Steuernummer 28-382/0919  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe gemäß § 292 BAO wird abgewiesen.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Oliver Simmer`(person)
- `Schwag 3, 4852 Steinwand, Österreich`(address)
- `Franka Reissl`(person)
- `Finanzamtes Österreich`(organisation)
- `28-382/0919`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Richterin Dr.in Elisabeth Hafner als Vorsitzende, die  Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. sowie die fachkundige Laienrichterin Eva  Maiwald-Wanderer und den fachkundigen Laienrichter Mag. Josef Bramer in der  Beschwerdesache Raimund Figgen, Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich, über die Beschwerde vom 13. August 2019  gegen den Bescheid des Finanzamtes Österreich vom 1. August 2019, vertreten durch Ilse  König, Bakk.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Elisabeth Hafner`(person)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eva  Maiwald-Wanderer`(person)
- `Mag. Josef Bramer`(person)
- `Raimund Figgen`(person)
- `Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Ilse  König, Bakk.`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/139661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Lukas Nauberg, Hölling 5, 4144 Dittmannsdorf, Österreich, über die Beschwerde vom 15. November 2020  gegen den Bescheid des Finanzamtes Österreich vom 14. Oktober 2020 betreffend Aussetzung  § 212a BAO 2020 nach Durchführung einer mündlichen Verhandlung auf Antrag der Partei am  16.12.2022 in Anwesenheit des Beschwerdeführers und von HR Mag. Christian Schneider und  Mag. Peter Wilhelm für das Finanzamt zur Steuernummer 43-674/4510  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Lukas Nauberg`(person)
- `Hölling 5, 4144 Dittmannsdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `HR Mag. Christian Schneider`(person)
- `Mag. Peter Wilhelm`(person)
- `Finanzamt`(organisation)
- `43-674/4510`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/140281.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140281.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Matthew Tschöpe, Mayr-Melnhof-Gasse 27, 5133 Mairhof, Österreich, über die Beschwerde vom 12. Juli 2021 gegen  die Bescheide des Finanzamtes Österreich je vom 28. Juni 2021 betreffend Einkommensteuer  2015 bis 2020 (Steuernummer 97-482/5270 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Matthew Tschöpe`(person)
- `Mayr-Melnhof-Gasse 27, 5133 Mairhof, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `97-482/5270`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/141996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. über die  Beschwerde der Hon.-Prof.in Cynthia Körber, Madersperger-Straße 52N, 8570 Aichegg, Österreich, vom 10. August 2023, gegen das Straferkenntnis  der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als  Abgabenstrafbehörde vom 13. Juli 2023, GZ. MA67/GZ/2023, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr.  71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

**False Positives:**

- `Sebastian Pfeiffer LL.M.` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Hon.-Prof.in Cynthia Körber`(person)
- `Madersperger-Straße 52N, 8570 Aichegg, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt  Wien`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/143820.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Gerald Sellemerten, Mühlgrabenweg 55, 7151 Wallern im Burgenland, Österreich  vertreten durch Glatzhofer & Matschek GmbH,  Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 31. März 2014  gegen die Bescheide des Finanzamtes für Großbetriebe je vom 23. Jänner 2014 betreffend  Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2009 - 2012 (Steuernummer  14-586/7014) zu Recht erkannt:   I. Die Beschwerde vom 31. März 2014 gegen die Bescheide betreffend Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag 2009 und 2011 wird gemäß § 279 BAO als unbegründet  abgewiesen.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Gerald Sellemerten`(person)
- `Mühlgrabenweg 55, 7151 Wallern im Burgenland, Österreich`(address)
- `Glatzhofer & Matschek GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `14-586/7014`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/146521.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146521.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Veronika Gerasimos, Edelputenweg 15, 9341 Langwiesen, Österreich, über die Beschwerde vom 27. Mai 2024 gegen  den Bescheid des Finanzamtes Österreich vom 23. April 2024 betreffend Gebühren und  Auslagenersätzen des Vollstreckungsverfahrens zur Steuernummer 23-307/4374  zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Veronika Gerasimos`(person)
- `Edelputenweg 15, 9341 Langwiesen, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `23-307/4374`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/147088.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147088.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Leopold Hattemer, Seifriedsedt 4, 9150 Penk, Österreich  vertreten durch Ernst & Young Steuerberatungs  GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 5. März 2024 gegen die  Bescheide des Finanzamtes für Großbetriebe vom 13. Dezember 2023 bzw. 17. und 29. Jänner  2024 die Festsetzung der Stabilitätsabgabe die Jahre 2018-2023 betreffend (Steuernummer xx  xxx/xxxx) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Leopold Hattemer`(person)
- `Seifriedsedt 4, 9150 Penk, Österreich`(address)
- `Ernst & Young Steuerberatungs  GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/147127.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147127.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Verona Laiß, Denkerstraße 82, 9133 Dullach, Österreich  über die Beschwerden vom 19. August 2024  gegen die Bescheide des Finanzamtes Österreich vom 19. Juli 2024 betreffend Aussetzung der  Einhebung (§ 212a BAO) für  -) Umsatzsteuer Jänner bis Dezember 2023   -) Umsatzsteuer 2022  -) Umsatzsteuer 2021  -) Umsatzsteuer 2020  -) Umsatzsteuer 2019  -) Körperschaftsteuer 2022  -) Körperschaftsteuer 2020  -) Körperschaftsteuer 2019  nach Durchführung einer mündlichen Verhandlung am 20.2.2025 in Anwesenheit von RA Mag.  Michael Glaser als Masseverwalter-Stellvertreter für die Beschwerdeführerin und von Mag.  Peter Wilhelm und Christian Pirker für das Finanzamt sowie der Schriftführerin Mag. Jacqueline  Pfeiffer zur Steuernummer 63-599/4428  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Verona Laiß`(person)
- `Denkerstraße 82, 9133 Dullach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `RA Mag.  Michael Glaser`(person)
- `Mag.  Peter Wilhelm`(person)
- `Christian Pirker`(person)
- `Finanzamt`(organisation)
- `Mag. Jacqueline  Pfeiffer`(person)
- `63-599/4428`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/147585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/147585.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Xaver Danneil, Pulverweg 6, 7540 Sankt Nikolaus, Österreich  über die Beschwerde vom 8. September 2024  gegen den Bescheid des Finanzamtes Österreich vom 25. Juli 2024 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2023 (Steuernummer 48-395/8410) zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Xaver Danneil`(person)
- `Pulverweg 6, 7540 Sankt Nikolaus, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `48-395/8410`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/148111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148111.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Pia Hauswerth, Hafing 209, 3123 Obermerking, Österreich  vertreten durch APP Steuerberatung GmbH,  Schenkenstraße 4 Tür 6, 1010 Wien, über die Beschwerde vom 9. Mai 2023 gegen die als  Bescheid intendierte Erledigung des Finanzamtes Österreich vom 11. April 2023 betreffend  Festsetzung einer Zwangsstrafe gemäß § 111 BAO (Steuernummer 72-680/0581)  beschlossen:  1.

**False Positives:**

- `Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Pia Hauswerth`(person)
- `Hafing 209, 3123 Obermerking, Österreich`(address)
- `APP Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `72-680/0581`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/149322.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149322.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Sascha Kowalschuk, Unfallkrankenhaus Meidling 69, 4880 Berg im Attergau, Österreich, betreffend Beschwerde vom 8. April 2025 gegen  den Bescheid des Finanzamtes Österreich vom 10. März 2025 betreffend Säumniszuschlag  10.03.2025 zur Steuernummer 82-491/3472  beschlossen:   Die Beschwerde vom 8. April 2025 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Markus Knechtl LL.M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Sascha Kowalschuk`(person)
- `Unfallkrankenhaus Meidling 69, 4880 Berg im Attergau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `82-491/3472`(tax_number)

</details>

---

## `preposition_name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `843bb75c`  
**Description:**
Captures names with prepositions like 'auf der', 'von der', 'zu der' which are common in German names (e.g., 'Renata auf der Heyde'). Fixed to capture only the name.

**Content:**
```
(?:auf\s+der\s+|von\s+der\s+|zu\s+der\s+|aus\s+der\s+|an\s+der\s+)([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 19 | 0 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 19 | 2313 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_70`)


Rechnung vom 29.10.2012 über € 21.583,10 , Leistungszeitraum 24.9.12-9.10.12 an der  Baustelle  Adresse1  2.)

**False Positives:**

- `Baustelle  Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_71`)


Rechnung vom 27.4.2012 über € 44.204,19, Leistungszeitraum 10.10.2012- 20.4.2012  an der Baustelle Adresse2  3.)

**False Positives:**

- `Baustelle Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_72`)


Rechnung vom 25.9.2012 über € 16.122,-, Leistungszeitraum 6.8.2012- 21.9.2012 an  der Baustelle Adresse3  4.)

**False Positives:**

- `Baustelle Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/134737.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134737.1_62`)


Der Bf hat ab 2005 an der Adresse Adr2 einen Nebenwohnsitz  gemeldet.

**False Positives:**

- `Adresse Adr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_108`)


In den Jahren 2005 bis 2008 war er  an der Adresse Adresse_A mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_109`)


Der Beschwerdeführer hat  gemeinsam mit seiner Ehegattin am 30.5.2005 einen Mietvertrag über eine Wohnung an der  Adresse Adresse_A, unterfertigt (vgl. Seiten 869-874 des Arbeitsbogens der Außenprüfung;

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_120`)


Auch die Ehegattin des Beschwerdeführers, E, und seine beiden Töchter Tochter_1 (geboren  1991) und Tochter_2 (geboren 1998) waren in den Jahren 2005 bis 2008 an der Adresse  Adresse_A mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse  Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_177`)


Die Feststellung zum Zufluss von EUR 34.000,- im Zusammenhang mit dem Projekt P/Ort_3  ergibt sich aus der Aussage des Rechtsanwaltes S über die Einrichtung eines Treuhandkontos  zugunsten des Beschwerdeführers, aus der Rechnung Nr_2 über EUR 34.000,- und aus den  Belegen über die Einzahlung dieses Betrages auf das bzw. die Behebung vom Treuhandkonto  10 von 14 Seite 11 von 14

**False Positives:**

- `Rechnung Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/136338.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136338.1_18`)


Diese seien  nach dem Auslandsstudium im SS 2019 erfolgreich an der Uni Ort1 nachgeholt worden.

**False Positives:**

- `Uni Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/140387.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140387.1_42`)


Weiters würden von der Firma FirmaA aufgrund  einer Sonderabmachung, beispielsweise KM-Preis von netto € 0,75 seit Jahren unverändert,  nicht alle Kilometer bezahlt werden.

**False Positives:**

- `Firma Firma` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_23`)


Der Beschwerdeführer war ausweislich des Zentralen Melderegisters von 4.9.2020 bis  15.12.2023 an der Adresse Adresse_A mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_33`)


K ist ausweislich des Zentralen Melderegisters seit Geburt an der  Adresse Adresse_B mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_6`)


Im Begleitschreiben v. 26.7.2022 teilt die Vertreterin ua. mit, dass nach einigen Recherchen an  der Klinik Ort1 nicht auszuschliessen sei, dass die vorliegende psychische Erkrankung bereits  seit vielen Jahren bestehe.

**False Positives:**

- `Klinik Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_16`)


Anzumerken ist,  dass die Firma A.GmbH hauptsächlich von der Firma TraunBeratung GmbH (Gf: B.B.) beliefert wird.

**False Positives:**

- `Firma Traun` — positional overlap with gold: `TraunBeratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunBeratung GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/148533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148533.1_16`)


Das Beschwerdebegehren betrifft lediglich die Feststellungen der Betriebsprüfung hinsichtlich  der Liegenschaften an der Adresse Liegenschaft1, Ort und Liegenschaft2, Ort.

**False Positives:**

- `Adresse Liegenschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/148533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148533.1_82`)


Hinsichtlich der Liegenschaft an der Adresse Liegenschaft2, Ort, ist folgendes festzuhalten:  Gemäß den Feststellungen wurde die gegenständliche Liegenschaft im Jahr 2004 vom  Beschwerdeführer gemeinsam mit seiner Ehefrau zu gleichen Teilen erworben.

**False Positives:**

- `Adresse Liegenschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/148533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148533.1_105`)


Es liegt daher keine Einkunftsquelle vor, die diesbezüglichen Aufwendungen sind  ertragsteuerrechtlich nicht abzugsfähig, ein Vorsteuerabzug steht nicht zu.  Hinsichtlich der Liegenschaft an der Adresse Liegenschaft1, Ort, ist folgendes festzuhalten:  Von der Betriebsprüfung wurden Vorsteuern sowie Aufwendungen für einzelne Wohnungen,  die im Rahmen des Vorbringens des Beschwerdeführers für eine Bewirtschaftung im Rahmen  eines Kurzentrums verwendet werden sollten, ausgeschieden.

**False Positives:**

- `Adresse Liegenschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/148533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148533.1_107`)


Liegenschaft an der Adresse Liegenschaft1, Ort unabhängig von diesem Vorhaben zu  beurteilen.

**False Positives:**

- `Adresse Liegenschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/149061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149061.1_11`)


Der Beschwerde  beigelegt war ein Schreiben in ungarischer Sprache von der Magyar Allamkincstár  Nyugdijfolyósitó Igazgatóság.

**False Positives:**

- `Magyar Allamkincst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `born_context_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `71881870`  
**Description:**
Captures names following 'geboren am' (born on) which is a common pattern for identifying individuals.

**Content:**
```
geboren\s+am\s+([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 2231 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_4`)


Der Beschwerdeführer (Bf.), geboren am Dezember 1992, ist besachwaltet.

**False Positives:**

- `Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132557.1_32`)


Der Ehegatte der  Beschwerdeführerin, K, geboren am Datum, ist an dieser Adresse seit 2.1.2003 mit  Hauptwohnsitz gemeldet.

**False Positives:**

- `Datum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_145`)


…"  7. Mit Beschwerdevorentscheidung vom 10.6.2014 wurde die Beschwerde als unbegründet  abgewiesen und in der Begründung ausgeführt:  " … Mit Eingabe vom 30. Oktober 2013, eingelangt am 7. November 2013, ersuchte die  Bundesagentur für Arbeit, Familienkasse D-Ort1, das Finanzamt Innsbruck gemäß Art. 84 der  Verordnung (EG) Nr. 883/2004 i. V. m. Art. 72 ff. der Verordnung (EG) Nr. 987/2009 um  Einbehaltung und Erstattung von zu Unrecht erbrachten Leistungen aus dem Anspruch von Frau  B, geboren am    September 1974, wohnhaft A-Ort2.

**False Positives:**

- `September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/143535.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143535.1_4`)


Die Tochter der Bf, Name, geboren am Datum, hat im Wintersemester (WS) 2020/21 das  Lehramtsstudium Englisch/Biologie begonnen.

**False Positives:**

- `Datum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `accused_context_name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2db930ba`  
**Description:**
Captures names following 'Angeklagte' (accused) or 'Angeklagten' to identify defendants, ensuring only the name is captured.

**Content:**
```
(?:Angeklagte|Angeklagten)\s+([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)*)\b(?![a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `senatspraesident_name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2af0d0f5`  
**Description:**
Captures names following 'Senatspräsidenten', 'Senatspräsidentin', 'Vizepräsidenten', 'Vizepräsidentin' to avoid matching the title or preceding institution.

**Content:**
```
(?:Senatspräsident(?:en|in)|Vizepräsident(?:en|in))\s+(?:des\s+)?(?:des\s+)?(?:Obersten\s+Gerichtshofs\s+)?(?<!\w)([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+(?:[A-Z]\.|\s+[A-Z][a-z]+|-?[A-Z][a-z]+)+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `family_relation_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ea45e77c`  
**Description:**
Captures names following family relation terms like 'von' in 'Eltern von' or 'Mutter von' to identify persons without titles.

**Content:**
```
(?:Eltern\s+von\s+|Mutter\s+von\s+|Vater\s+von\s+|Sohn\s+von\s+|Tochter\s+von\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1613 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_82`)


Er hatte dort auch familiären Kontakt zur Mutter von Frau Priv.-Doz.in Laetitia Pöstges.

**False Positives:**

- `Frau Priv` — positional overlap with gold: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

</details>

---

## `witness_context_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `571abaa8`  
**Description:**
Captures names following 'Zeuge', 'Zeugin', 'Zeugen' (witness) to identify witnesses in legal texts.

**Content:**
```
(?:Zeuge|Zeugin|Zeugen)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00ee\u00f4\u00fb]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00ee\u00f4\u00fb]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 2322 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_198`)


Aus diesen Gründen  sei es für unseren Mandanten (Baugewerbe) nicht möglich, einen Sommertermin bei Gericht  wahrzunehmen bzw. für die beantragten Zeugen Gutachtensänderungen rechtzeitig  vorzubereiten.

**False Positives:**

- `Gutachtensänderungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_27`)


Dagegen wandte sich der Bf mit dem Rechtsmittel der Beschwerde und führte aus, dass er den  Zeugen Herrn P.R. gefragt hätte, ob er ein Gewerbe bei ihm anmelde.

**False Positives:**

- `Herrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_153`)


 Einvernahme von Zeugen  Der Bf. beantragte im Zuge seiner Beschwerde die Einvernahme des Meldungslegers sowie die  Einvernahme von A. von der MA 48 und die Einvernahme von B., von der MA 67, ohne dass  dem Erfordernis der Angabe eines konkreten Beweisthemas entsprochen wurde.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_157`)


Mangels Bekanntgabe eines konkreten Beweisthemas konnte von der Einvernahme des A. (MA  48) und von B. (MA 67) als Zeugen Abstand genommen werden.

**False Positives:**

- `Abstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_180`)


Dass  schließlich eine spezielle Betonpumpe aufgrund der Länge des Stollens notwendig war, führte  der Zeuge Ing. Z überzeugend aus;

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/137291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137291.1_53`)


Auch ist  es für mich unverständlich, dass Sie negieren, dass die Befragung des Zeugen Zeuge1 kein  taugliches Beweismittel sei.

**False Positives:**

- `Zeuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_95`)


Die  Feststellungen zur Schwiegermutter basieren auf den diesbezüglichen Angaben der Bf. bzw.  des Zeugen GatteW im Zuge der mündlichen Verhandlung.

**False Positives:**

- `Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/144827.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144827.1_61`)


Die belangte Behörde legte am 6. Dezember 2023 eine Niederschrift über die Befragung des  Zustellorgans vor, in welcher der Zeuge Folgendes angab:  „Das Schriftstück (Verständigung zur Hinterlegung) mit Nr. [Nr] wurde von mir am 09.03.2022  vorschriftsmäßig in die Abgabeeinrichtung (Einfamilienhaus, Blankenfeldgasse 17, 8453 Untergreith, Österreich) eingelegt.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Blankenfeldgasse 17, 8453 Untergreith, Österreich`(address)

</details>

---

## `first_name_only_title` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `461e3f03`  
**Description:**
Matches titles followed by a single capitalized word (e.g., 'Dr. Heinrich') to handle cases where the surname is not part of the entity or is separated by context.

**Content:**
```
(?<![A-Za-z])(?:Dr\.|Mag\.|Prof\.|Hon\.-?Prof\.|Univ\.-?Prof\.|DI\.|Ing\.|Bakk\.\s+iur\.|PhD\.|HR\s+Ing\.|Techn\s+|Dipl\.-?HTL\-?Ing\.|PD\s+Dr\.|Priv\.-?Doz\.|DDr\.|KommR\s+|\u00d6kR\s+|RgR\s+|StR\s+|MedR\s+|HR\s+|KzlR\s+|OMedR\s+|VetR\s+|AR\s+|Vizepr\u00e4sident\s+|Senatspr\u00e4sident\s+|Hofrat\s+|Hofr\u00e4tin\s+|Hofr\u00e4t\s+|Vizepr\u00e4sidentin\s+|Senatspr\u00e4sidentin\s+)(?:\s+Dr\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00ee\u00f4\u00fb]+)(?:\s+(?:LL\.M\.|PhD|Dipl\.|Ing\.|Bakk\.|Dr\.))?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 13 | 2210 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Radics`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Frieda Krein`(person)
- `Priv.-Doz.in Elena Kaminskiy`(person)
- `W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `60-936/8299`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Leonhard Meesters  in der Beschwerdesache Univ.-Prof. MedR Wigand Matthisen,  Auflangenweg 177, 9816 Penk, Österreich, über die Beschwerde vom 26. November 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt FA) vom 2. November 2020 betreffend die  Einkommensteuer für das Jahr 2019, Steuernummer 48-577/9146, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Univ.-Prof. Med` — partial — pred is substring of gold: `Univ.-Prof. MedR Wigand Matthisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Leonhard Meesters`(person)
- `Univ.-Prof. MedR Wigand Matthisen`(person)
- `Auflangenweg 177, 9816 Penk, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt`(organisation)
- `48-577/9146`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_101`)


Dem Bundesfinanzgericht liegen folgende ärztliche Sachverständigengutachten vor: ein  ärztliches Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen  vom 19.03.2020 erstellt von Frau Dr. Arzt, einer Fachärztin für Neurologie und Psychiatrie,  (hier: Erstgutachten) sowie – infolge der gegenständlichen Bescheidbeschwerde - eine  Gesamtbeurteilung nach der Einschätzverordnung des Bundesamtes für Soziales und  Behindertenwesen vom 28.12.2020 erstellt von Frau Dr. Arzt1, der ein psychiatrisches  Teilgutachten von Frau Dr. Arzt1 - sowie ein psychologisches Teilgutachten von Frau Dr. Arzt2  (beide Teilgutachten erstellt am 22.12.2020) zu Grunde liegt.

**False Positives:**

- `Dr. Arzt` — no gold match — likely missing annotation
- `Dr. Arzt` — no gold match — likely missing annotation
- `Dr. Arzt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesamtes für Soziales und Behindertenwesen`(organisation)
- `Bundesamtes für Soziales und  Behindertenwesen`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135955.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135955.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Elisabeth Hafner in der Beschwerdesache  Dipl.-Ing. StR Ali Butzler, Trenninggasse 37, 2130 Hobersdorf, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH,  Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom 30. September 2020 gegen die  Bescheide des Finanzamtes Klagenfurt vom 8. Juli 2020 betreffend  I. die Wiederaufnahme des Verfahrens zur Festsetzung des Vergütungsbetrages nach dem  Energieabgabenvergütungsgesetz für den Zeitraum 2014 und  II. die Festsetzung des Vergütungsbetrages nach dem Energieabgabengesetz für den Zeitraum  2014  I. zu Recht erkannt:  Der Beschwerde gegen den Bescheid betreffend die Wiederaufnahme des Verfahrens zur  Festsetzung des Vergütungsbetrages nach dem Energieabgabenvergütungsgesetz für den  Zeitraum 2014 wird Folge gegeben.

**False Positives:**

- `Ing. St` — partial — pred is substring of gold: `Dipl.-Ing. StR Ali Butzler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Dipl.-Ing. StR Ali Butzler`(person)
- `Trenninggasse 37, 2130 Hobersdorf, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Klagenfurt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_101`)


Dr. Dok1 reihte in ihrem Gutachten vom 1. Juli 2022 die Erkrankung/Behinderung der Bf. unter  die Richtsatzposition der Einschätzungsverordnung 03.01.03, welche bei kognitiver  Leistungseinschränkung folgende Behinderungsgrade vorsieht:    Dr. Dok1 setzte den Gesamtgrad der Behinderung mit 50% fest und bescheinigte der Bf. eine  Erwerbsunfähigkeit rückwirkend ab 1. Jänner 2004.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`
- `Dr. Dok` — similar text (different position): `Dr. Dok1`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)
- `Dr. Dok1`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_104`)


Im Beschwerdefall hat das Bundesfinanzgericht zu beurteilen, ob die von Dr. Dok1 in ihrem  Gutachten vom 1. Juli 2022 getroffene Feststellung, wonach bei der Bf. die Erwerbsunfähigkeit  nicht vor dem 21.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dok1`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_118`)


Dr. Dok1 gelangte zu der Feststellung, dass eine dauernde Erwerbsunfähigkeit seit Jänner 2004  vorliegt.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_127`)


Von der Bf. wurden keine relevanten Befunde vorgelegt, denen zufolge Dr. Dok1 eine  Erwerbsunfähigkeit vor dem 21.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_130`)


Das Bundesfinanzgericht erachtet die von Dr. Dok1 in ihrem Gutachten vom 1. Juli 2022  getroffene Feststellung, wonach bei der Bf. eine Erwerbsunfähigkeit seit 2004 vorliegt, als mit  größter Wahrscheinlichkeit den Tatsachen entsprechend an.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dok1`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/149834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149834.1_20`)


Unter Tz 2 BP des Bericht gemäß § 150 BAO (BP) vom 26.02.2019 wurde zu den  Beurteilungseinheiten im Rahmen der Vermietung und Verpachtung von einzelnen Teilen der  Liegenschaft Bf A-Ort 1 – das Medizinische Zentrum Dr. Bf1, eine Dienstwohnung, das  Veranstaltungszentrum, das Stallgebäude, die Vermietung der Gästewohnung sowie den  Betrieb einer Imbissstube – folgende Feststellungen getroffen:   2 von 25 Seite 3 von 25

**False Positives:**

- `Dr. Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `accusative_genitive_name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ce93ecd2`  
**Description:**
Captures person names following legal role terms in accusative or genitive cases (e.g., 'des Angeklagten', 'der Zehra Dreissig') to identify defendants, witnesses, etc., without titles.

**Content:**
```
(?:dem\s+Angeklagten|des\s+Angeklagten|den\s+Angeklagten|der\s+Angeklagten|dem\s+Beschuldigten|des\s+Beschuldigten|den\s+Beschuldigten|der\s+Beschuldigten|dem\s+Zeugen|des\s+Zeugen|den\s+Zeugen|der\s+Zeugin|dem\s+Beklagten|des\s+Beklagten|den\s+Beklagten|der\s+Beklagten|dem\s+Kläger|des\s+Klägers|den\s+Klägern|der\s+Klägerin|dem\s+Opfer|des\s+Opfers|den\s+Opfern|der\s+Opferin|dem\s+Verteidiger|des\s+Verteidigers|den\s+Verteidigern|der\s+Verteidigerin|dem\s+Anwalt|des\s+Anwalts|den\s+Anwälten|der\s+Anwältin|dem\s+Notar|des\s+Notars|den\s+Notaren|der\s+Notarin|dem\s+Richter|des\s+Richters|den\s+Richtern|der\s+Richterin|dem\s+Staatsanwalt|des\s+Staatsanwalts|den\s+Staatsanwälten|der\s+Staatsanwältin|dem\s+Vizepräsidenten|des\s+Vizepräsidenten|den\s+Vizepräsidenten|der\s+Vizepräsidentin|dem\s+Senatspräsidenten|des\s+Senatspräsidenten|den\s+Senatspräsidenten|der\s+Senatspräsidentin|dem\s+Hofrat|des\s+Hofrats|den\s+Hofräten|der\s+Hofrätin|dem\s+Hofräts|des\s+Hofräts|den\s+Hofräten|der\s+Hofrätin)(?:\s+|,|\.|$)([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)+)(?:\s*(?:,|\.|$|\s+und\s+|\s+von\s+|\s+als\s+))(?!\s*(?:Ltd|GmbH|AG|KG|Rechtsanw|Anwalt|Gesellschaft|Partei|Firma|Unternehmen|Form|Abs|Absatz|Nr|Nr\.|Vorsitzenden|Vorsitzende|Senatspräsident|Hofrat|Hofräts|Angeklagte|Angeklagten|Zeugin|Zeuge|Beklagte|Beklagten|Klägerin|Kläger|Abstimmung|Feststellung|Ansehen|Strafe|Arbeitgeber|Arbeitnehmer|Sozialrechtssachen|Sozialgericht|Rente|Familie|Unterhaltsvorschuss|Unterhaltsverpflichteten|Frau|Landl|Verhandlung|Ausfertigung|Erkenntnis|Vorsitzenden|Vorsitzende|Maurer|Fliesenleger|Arbeiter|Ingenieur|Lehrer|Arzt|Notar|Bank|Konto|Kredit|Darlehen|Hypothek|Versicherung|Versicherungs|Steuer|Finanz|Finanzamt|Gericht|Kammer|Behörde|Amt|Ministerium|Bundes|Land|Stadt|Gemeinde|Ort|Bezirk|Kreis|Region|Lage|Position|Stelle|Job|Beruf|Tätigkeit|Funktion|Rolle|Aufgabe|Pflicht|Recht|Anspruch|Klage|Klagegrund|Klageantrag|Klagebegründung|Klageerwiderung|Klageantwort|Klageerhebung|Klageverhandlung|Klageentscheidung|Klageurteil|Klagebeschluss|Klageverfahren|Klagekosten|Klagegebühr|Klagefrist|Klageverjährung|Klageverwirkung|Klageverzicht|Revisionsgericht|Berufungsgericht|Oberste|Gerichtshof|Senatspräsidentin|Vizepräsident|Vizepräsidentin|Rekursgericht|Kontaktrecht|Dr\.|Mag\.|Prof\.|Univ\.|Hon\.|MMag\.|DI\.|Ing\.|Bakk\.|PhD\.|HR\.|Techn\.|Dipl\.|PD\.|Priv\.|KommR\.|ÖkR\.|RgR\.|StR\.|MedR\.|KzlR\.|OMedR\.|VetR\.|AR\.|Vizepräsident\s+|Senatspräsident\s+|Hofrat\s+|Hofrätin\s+|Hofräts\s+|Vizepräsidentin\s+|Senatspräsidentin\s+|Jugendhilfeträger|Mutter|Vater|Eltern|Kind|Sohn|Tochter|Gewährung|Unterhaltsvorschuss))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `mj_minor_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fcc80868`  
**Description:**
Captures names following 'mj' (minderjährig) which indicates a minor person in legal texts.

**Content:**
```
\bmj\s+([A-Z][a-zäöüßéèêëïîôùûü]+(?:\s+[A-Z][a-zäöüßéèêëïîôùûü]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 401 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_184`)


Anspruch des (Groß-)Elternteils nach nationalem Recht i. V. m. Unionsrecht  Die Großmutter/der Großvater bzw. ein (Groß-)Elternteil des beschwerdegegenständlichen  Kindes erfüllt im Beschwerdezeitraum die persönlichen Voraussetzungen für einen Anspruch  auf Ausgleichszahlung/ Familienbeihilfe für das mj Kind (§ 2 Abs. 1 lit. b FLAG 1967;

**False Positives:**

- `Kind` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

