# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-24T07:07:26.032684

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
| Refinement iterations | 0 |
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
| Accuracy (exact match) | 98.2% |
| True Positives | 789 |
| False Positives | 1368 |
| False Negatives | 1602 |
| Total Gold Entities | 2391 |
| Micro Precision | 36.6% |
| Micro Recall | 33.0% |
| Micro F1 | 34.7% |
| Macro F1 | 34.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `case_marker_name` | 28.0% | 83.4% | 16.8% | 482 | 402 | 80 |
| `von_title_name` | 0.3% | 80.0% | 0.2% | 5 | 4 | 1 |
| `herr_context_name` | 9.2% | 67.8% | 4.9% | 174 | 118 | 56 |
| `title_only_person` | 16.8% | 38.1% | 10.7% | 674 | 257 | 417 |
| `verb_context_name` | 0.5% | 18.2% | 0.3% | 33 | 6 | 27 |
| `preposition_name` | 0.2% | 1.3% | 0.1% | 158 | 2 | 156 |
| `academic_suffix_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `born_context_name` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `accused_context_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `senatspraesident_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `family_relation_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `witness_context_name` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `accusative_genitive_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `mj_minor_name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `single_initial_person_2` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `anonymous_person_dr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `herr_initial_person` | 0.0% | 0.0% | 0.0% | 30 | 0 | 30 |
| `richter_initial_person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `contextual_name_no_title` | 0.0% | 0.0% | 0.0% | 153 | 0 | 153 |
| `herr_frau_name` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `definite_article_person` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `von_role_name` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `richter_context_name` | 0.0% | 0.0% | 0.0% | 413 | 0 | 413 |
| `single_initial_person` | 0.0% | 0.0% | 0.0% | 15 | 0 | 15 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `case_marker_name` 🏆

**F1:** 0.280 | **Precision:** 0.834 | **Recall:** 0.168  

**Format:** `regex`  
**Rule ID:** `b457b19b`  
**Description:**
Captures person names following legal case markers like 'Beschwerdesache', 'Revisionssache', etc., ensuring only the name is captured. TIGHTENED to require a full name immediately after the marker to avoid partial matches like 'Rg' or 'Hon'.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)(?:Beschwerdesache|Revisionssache|Verwaltungsstrafsache|Strafsache|Zivilsache|Familiensache|Nachlasssache|Insolvenzsache|Konkurssache|Vollstreckungssache|Geldw\u00e4schereisache|Kartellsache|Wettbewerbsrechtssache|Sozialversicherungssache|Arbeitsrechtssache|Verwaltungsgerichtsbarkeitssache|Verfassungsgerichtssache|Verwaltungsstrafgesetzssache|Bundesfinanzgerichtssache|Finanzstrafssache|Finanzverwaltungsstrafssache|Finanzverwaltungsstrafverfahrenssache|Finanzverwaltungsstrafverfahren|Finanzverwaltungsstrafverfahrens|Finanzverwaltungsstrafverfahrensf\u00e4lle|Finanzverwaltungsstrafverfahrensfalls|Finanzverwaltungsstrafverfahrensf\u00e4llen|Finanzverwaltungsstrafverfahrensfalls|Finanzverwaltungsstrafverfahrensf\u00e4lle|Finanzverwaltungsstrafverfahrensfalls|Finanzverwaltungsstrafverfahrensf\u00e4llen|Finanzverwaltungsstrafverfahrensfalls)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.834 | 0.168 | 0.280 | 482 | 402 | 80 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 402 | 80 | 1987 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Zeno Matyssek` | `Zeno Matyssek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)
- `Finanzamt für Gebühren` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Chen Petermüller,  Sand 5, 4851 Hehenberg, Österreich, vertreten durch Anka Vrcic, Kummergasse 7//3/2, 1210 Wien, über die  Beschwerden vom 25. April 2019 gegen die Bescheide des Finanzamtes Salzburg-Land vom  25. März 2019 betreffend Abweisung des Antrages auf Wiederaufnahme des Verfahrens  hinsichtlich Umsatzsteuer 2016 und betreffend Abweisung des Antrages auf Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2016, Steuernummer 20-238/1198, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Chen Petermüller` | `Chen Petermüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sand 5, 4851 Hehenberg, Österreich` (address)
- `Anka Vrcic` (person)
- `Finanzamtes Salzburg-Land` (organisation)
- `20-238/1198` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Florenzia Claußing` | `Florenzia Claußing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich` (address)
- `Finanzamtes` (organisation)
- `10-95-558/8694` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wendy Scherl` | `Wendy Scherl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich` (address)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `53-864/4798` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Klarissa Kümml` | `Klarissa Kümml` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

| Predicted | Gold |
|---|---|
| `Daisy Wegelein` | `Daisy Wegelein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Feichtenschlager` (person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `61-004/6209` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Alma Gaedecke, Höbelgasse 24, 9400 St. Thomas, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alma Gaedecke` | `Alma Gaedecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Höbelgasse 24, 9400 St. Thomas, Österreich` (address)
- `Finanzamtes Wien  1/23` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Nadja Rossetto` | `Nadja Rossetto` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich` (address)
- `Imre & Schaffer Rechtsanwälte OG` (organisation)
- `Finanzamtes` (organisation)
- `85-716/2059` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Rainer Leutheußer` | `Rainer Leutheußer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich` (address)
- `Egger & Freidorfer Steuerberatungs-OG` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Donald Paulovits` | `Donald Paulovits` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Tröbach 41, 9130 Leibsdorf, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `95-720/4312` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximilian Joobs` | `Maximilian Joobs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Oleg Kreissl` | `Oleg Kreissl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rudolf Schlohsmacher` | `Rudolf Schlohsmacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich` (address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Miroslav Treischl` | `Miroslav Treischl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Thomas Leitner` (person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich` (address)
- `Grant Thornton Austria GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Irvin Kurrek  in der Beschwerdesache Alexandra Kesler,  Illyrerweg 5, 4073 Edramsberg, Österreich, (nunmehr Valsyn-Maschinenbau GmbH als Rechtsnachfolgerin der Schameitat Sanitär GmbH, vertreten durch StB,  über die Berufung (nunmehr Beschwerde) vom 21. August 2013 gegen die Bescheide des FA  vom 9. Juli 2013 betreffend Wiederaufnahme der Verfahren hinsichtlich der  Körperschaftsteuer für die Jahre 2009 und 2010 sowie die Körperschaftsteuer für die Jahre  2009 bis 2011 beschlossen:    I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) als nicht  zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Alexandra Kesler` | `Alexandra Kesler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Priv.-Doz. Irvin Kurrek` (person)
- `Illyrerweg 5, 4073 Edramsberg, Österreich` (address)
- `Valsyn-Maschinenbau GmbH` (organisation)
- `Schameitat Sanitär GmbH` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Luigi Wedekämper` | `Luigi Wedekämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Marianne Liuni` (person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Wolf Sackner, Altweitra 15, 6091 Götzens, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  34-684/1904  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wolf Sackner` | `Wolf Sackner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Altweitra 15, 6091 Götzens, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `34-684/1904` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Florentin Blissenbach, Gotschmanninstraße 11, 9170 Seidolach, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  03-281/0693  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Florentin Blissenbach` | `Florentin Blissenbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Gotschmanninstraße 11, 9170 Seidolach, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `03-281/0693` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Huberta Nothofer` | `Huberta Nothofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Florenzia Rutt` | `Florenzia Rutt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich` (address)
- `Zollamtes Feldkirch Wolfurt` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vivian Malek` | `Vivian Malek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich` (address)
- `Mag. Walter Dienstl & Partner  KG` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Tanja Wescher, Margaretenplatz 55, 3170 Gerstbach, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 07-638/8400  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tanja Wescher` | `Tanja Wescher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ralf Schatzl` (person)
- `Margaretenplatz 55, 3170 Gerstbach, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `07-638/8400` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Thomas Kreul, Preberstraße 4, 3911 Dietharts, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Kreul` | `Thomas Kreul` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Preberstraße 4, 3911 Dietharts, Österreich` (address)
- `DI Heinrich Richter Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jennifer Rösl` | `Jennifer Rösl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Eckard Sellnow` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stephan Antonewitz` | `Stephan Antonewitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter OMedR Viktor Butterbrod in der Beschwerdesache Holger Virhus,  Bisamberger Straße 67, 8342 Wörth, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 36-425/3917  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Holger Virhus` | `Holger Virhus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Viktor Butterbrod` (person)
- `Bisamberger Straße 67, 8342 Wörth, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `36-425/3917` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Sahin, Fischmarkt 627, 4153 Vorderschiffl, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

| Predicted | Gold |
|---|---|
| `Dimitri Sahin` | `Dimitri Sahin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Fischmarkt 627, 4153 Vorderschiffl, Österreich` (address)
- `LMG  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Felizitas Philippov` | `Felizitas Philippov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gerald Hellbing` | `Gerald Hellbing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gotthard Eppers  vertreten durch  Gf. über die Beschwerde vom 16. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 16. Dezember 2019, Steuernummer 98-639/6692, betreffend Feststellung der  Einkünfte gem. § 188 BAO für das Jahr 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gotthard Eppers` | `Gotthard Eppers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien  4/5/10` (organisation)
- `98-639/6692` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Manuel Rathlev, Hadersfelder Straße 10, 4171 Kasten, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Edwin Meuser  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Manuel Rathlev` | `Manuel Rathlev` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hadersfelder Straße 10, 4171 Kasten, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Edwin Meuser` (person)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Hademar Berking, Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich` (address)
- `Mag. Margot Artner` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Igor Strunz` | `Igor Strunz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Björn Hüpscher` (person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich` (address)
- `Vedat Gökdemir` (person)
- `Finanzamtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alexander Powell` | `Alexander Powell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Lubomir Gruebert` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Calvin Gorol` | `Calvin Gorol` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alfred Klaming` (person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich` (address)
- `Helmut Binder` (person)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Klarissa Aßmus, Strombad Rustenweg 4, 3452 Trasdorf, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 52-573/0809  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Klarissa Aßmus` | `Klarissa Aßmus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Strombad Rustenweg 4, 3452 Trasdorf, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `52-573/0809` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Melina Wellenbrock  in der Verwaltungsstrafsache  Gabriele Vogrin, Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich, 1.) über die Beschwerde vom 19.06.2020 gegen die Strafverfügung  des Magistrats der Stadt Wien vom 30.12.2019, zugestellt am 27.02.2020, Geschäftszahl  MA67/196701166656/2019, und 2.) über die Beschwerde vom 19.06.2020 gegen die Strafver- fügung des Magistrats der Stadt Wien vom 20.01.2020, zugestellt am 03.03.2020, Geschäfts- zahl MA67/196701283117/2019, beschlossen:    Die Beschwerden werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Gabriele Vogrin` | `Gabriele Vogrin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Melina Wellenbrock` (person)
- `Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt Wien` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Anatol Hasenbein, Josef-Kaut-Straße 3, 4048 Großamberg, Österreich, über die Beschwerde vom 26. Mai 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 15. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anatol Hasenbein` | `Anatol Hasenbein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josef-Kaut-Straße 3, 4048 Großamberg, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ronald Töws` | `Ronald Töws` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gudrun Sochurek` | `Gudrun Sochurek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Mag. Rupert Karl` (person)
- `Finanzamtes` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Valentina Heumeyer  in der Beschwerdesache Emanuela Schöchl,  J. Schemmerl-Gasse 7, 4906 Felling, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Emanuela Schöchl` | `Emanuela Schöchl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Valentina Heumeyer` (person)
- `J. Schemmerl-Gasse 7, 4906 Felling, Österreich` (address)
- `Anton Hörmann` (person)
- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Hedwig Scheff, Franz Eckrieder Straße 50, 3142 Grunddorf, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Scheff` | `Hedwig Scheff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz Eckrieder Straße 50, 3142 Grunddorf, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/131065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131065.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Kirstin Detlef  in der Beschwerdesache  Pawel Wnent, Reinbergweg 21, 9112 Wölfnitz, Österreich, vertreten durch X-Steuerberatung über die Beschwerde vom  19. Februar 2016 gegen den Bescheid des FA Oststeiermark  vom 15. Jänner 2016 betreffend  Feststellung der Einkünfte § 188 BAO 2012 zur Steuernummer 999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Pawel Wnent` | `Pawel Wnent` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Mag.a Kirstin Detlef` (person)
- `Reinbergweg 21, 9112 Wölfnitz, Österreich` (address)
- `X-Steuerberatung` (organisation)
- `FA Oststeiermark` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valerie Süssmeier` | `Valerie Süssmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Weiskittel` | `Holger Weiskittel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Theophil Schachenmeier, Gsteinert 21, 4115 Steining, Österreich, betreffend die Beschwerde vom 03.04.2020 gegen den Bescheid  des Finanzamtes Freistadt Rohrbach Urfahr vom 26.03.2020 über die Einstellung der  Vollstreckung zu Steuernummer 63-906/4998  beschlossen:   Die Beschwerde wird gem. § 260 Abs. 1 lit. a) BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Theophil Schachenmeier` | `Theophil Schachenmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Norbert Zöls` (person)
- `Gsteinert 21, 4115 Steining, Österreich` (address)
- `Finanzamtes` (organisation)
- `63-906/4998` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ursula Raubart, Tschupbach 5c, 4144 Karlsbach, Österreich, vertreten durch Rachel Woiczyk, Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich, über die Beschwerden vom  12. November 2018 gegen die Bescheide des Finanzamtes Österreich vom 23. Oktober 2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017 zu  Steuernummer 86-917/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Raubart` | `Ursula Raubart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tschupbach 5c, 4144 Karlsbach, Österreich` (address)
- `Rachel Woiczyk` (person)
- `Christian-Fritz-Weg 13, 4183 Unterbrunnwald, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `86-917/1669` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Annemarie Wittjen  in der Beschwerdesache Samuel Herpel,  Ansfelden 2, 3822 Münchreith an der Thaya, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 39-702/2118  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

| Predicted | Gold |
|---|---|
| `Samuel Herpel` | `Samuel Herpel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Annemarie Wittjen` (person)
- `Ansfelden 2, 3822 Münchreith an der Thaya, Österreich` (address)
- `Erwin Baldauf` (person)
- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft` (organisation)
- `Finanzamtes Landeck Reutte` (organisation)
- `39-702/2118` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tiffany Kleiß` | `Tiffany Kleiß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Endergasse 74, 5411 Vorderwiestal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `79-412/0834` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Wilmerdinger  in der Beschwerdesache Kirsten Constantinescu,  Höhenwald 50, 4822 Primesberg, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-83-382/2498  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kirsten Constantinescu` | `Kirsten Constantinescu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Delia Wilmerdinger` (person)
- `Höhenwald 50, 4822 Primesberg, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `41-83-382/2498` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dorothea Sulzbacher, Obergreith 14 - 23, 4924 Breitwies, Österreich, über die Beschwerde vom 21. August 2018 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 2. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dorothea Sulzbacher` | `Dorothea Sulzbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergreith 14 - 23, 4924 Breitwies, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

| Predicted | Gold |
|---|---|
| `Wendy Schärff` | `Wendy Schärff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Norbert Zöls` (person)
- `Krainberg 12, 4633 Weilbach, Österreich` (address)
- `LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Linz` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131601.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Waltraud Herbrecher, Südweg 312, 4062 Niederbuch, Österreich, über die Beschwerde vom 3. Oktober 2018 gegen die Bescheide des Finanzamtes Wien  1/23 vom 30. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 und  2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Waltraud Herbrecher` | `Waltraud Herbrecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Südweg 312, 4062 Niederbuch, Österreich` (address)
- `Finanzamtes Wien  1/23` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Fridolin Härlin  in der Beschwerdesache Alva Czymzik,  Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alva Czymzik` | `Alva Czymzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Fridolin Härlin` (person)
- `Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck in der Beschwerdesache  Thobias Dommert, Hainfelder Straße 56, 4846 Gewerbepark West, Österreich, vertreten durch LBG Niederösterreich Steuerberatung GmbH, Wie- ner Straße 2, 2640 Gloggnitz, über die Beschwerden vom 29. Dezember 2017 und 31. Jänner  2018 gegen die Bescheide des Finanzamtes Neunkirchen Wiener Neustadt vom 6. Dezember  2017 und 10. Jänner 2018 betreffend Einkommensteuer 2007 bis 2011, St.Nr. 33- 66-847/2354, zu Recht erkannt:    Der Beschwerde gegen den Einkommensteuerbescheid 2007 wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Thobias Dommert` | `Thobias Dommert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johannes Böck` (person)
- `Hainfelder Straße 56, 4846 Gewerbepark West, Österreich` (address)
- `LBG Niederösterreich Steuerberatung GmbH` (organisation)
- `Finanzamtes Neunkirchen Wiener Neustadt` (organisation)
- `66-847/2354` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Moses Hallbauer, Glanstraße 125, 8271 Großhart, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft mbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 1. Februar 2017 gegen den Bescheid  des Finanzamtes Gänserndorf Mistelbach vom 12. Jänner 2017 betreffend Einkommensteuer  2015, Steuernummer 73-564/0656, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Moses Hallbauer` | `Moses Hallbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Glanstraße 125, 8271 Großhart, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft mbH,` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `73-564/0656` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Julian Pierchala,  Pracherweg 6, 8635 Gollrad, Österreich, über die Beschwerde vom 6. August 2019 gegen den Bescheid des Finanzamtes  Österreich vom 24. Juli 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018,  Steuernummer 74-273/9351, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julian Pierchala` | `Julian Pierchala` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pracherweg 6, 8635 Gollrad, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `74-273/9351` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Ralph Staibler, Pregerstraße 17, 4242 Kirchberg, Österreich, über die Beschwerde vom 15. Juni 2019 gegen den Bescheid des Finanzamtes  Österreich, vormals des Finanzamtes Salzburg-Land vom 16. Mai 2019 betreffend die  Wiederaufnahme des Verfahren gemäß § 303 Abs.1 BAO zur Einkommensteuer 2013 sowie die  Bescheide vom 17. Mai 2019 betreffend die Wiederaufnahme der Verfahren gemäß § 303  Abs.1 BAO zur Einkommensteuer 2014 und 2015 zu Steuernummer 92-314/9447  zu Recht  erkannt:   1.

| Predicted | Gold |
|---|---|
| `Ralph Staibler` | `Ralph Staibler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pregerstraße 17, 4242 Kirchberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `92-314/9447` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Adrian Hofschmidt, Dechantsbühel 10, 9911 Bannberg, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Adrian Hofschmidt` | `Adrian Hofschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dechantsbühel 10, 9911 Bannberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thomas Drieschner  in der Beschwerdesache Gebhard Determann,  Mooseggweg 49, 9624 Fritzendorf, Österreich, Deutschland, vertreten durch die Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H. über die Beschwerden gegen die Bescheide des  Finanzamtes Kufstein Schwaz betreffend Einkommensteuer 2017 und Umsatzsteuer 2017  jeweils vom 10. Jänner 2019 zu Recht erkannt:   I. Der Beschwerde gegen den Umsatzsteuerbescheid 2017 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Gebhard Determann` | `Gebhard Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Thomas Drieschner` (person)
- `Mooseggweg 49, 9624 Fritzendorf, Österreich` (address)
- `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Gudrun Breunlein, Am Rintl 6, 5324 Faistenau, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 75-682/2104  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gudrun Breunlein` | `Gudrun Breunlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Am Rintl 6, 5324 Faistenau, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `75-682/2104` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Sandro Fischlein, Hans-Schilder-Platz 17, 9065 Untermieger, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sandro Fischlein` | `Sandro Fischlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hans-Schilder-Platz 17, 9065 Untermieger, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Torsten Gnapfeus, Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich, gegen die Bescheide des Finanzamtes Wien 4/5/10 vom 21. Februar 2014 betreffend  die auf § 303 Abs. 1 BAO basierende Verfügung der Wiederaufnahme der Verfahren zur  Umsatzsteuer für das Jahr 2010 und zur Einkommensteuer für die Jahre 2010 und 2011 sowie  die auf § 205 Abs. 1 BAO basierende Festsetzung von Anspruchszinsen für die Jahre 2010 bis  2012 beschlossen:  Der Vorlageantrag vom 26.9.2014 wird - betreffend vorgenannter Bescheide - gemäß § 264  Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Torsten Gnapfeus` | `Torsten Gnapfeus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natalie Emmerling,  Holzäpfeltal 15, 8081 Guggitzgraben, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Natalie Emmerling` | `Natalie Emmerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holzäpfeltal 15, 8081 Guggitzgraben, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Salzburg-Land` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Veit Vissers, Wander Bertoni-Straße 166, 5223 Fludau, Österreich, über die Beschwerde vom 10. September 2019 gegen den  Bescheid des Finanzamtes Österreich vom 13. August 2019 betreffend Abweisung eines  Antrages auf Wiederaufnahme § 303 BAO /  ESt 2017 Steuernummer 94-198/2586  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Veit Vissers` | `Veit Vissers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Wander Bertoni-Straße 166, 5223 Fludau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `94-198/2586` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132328.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132328.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Michael Mühlbeck, Glöckler 35, 5252 Parz, Österreich, betreffend Beschwerde vom 17. Jänner 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 18. Dezember 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 Steuernummer 92-602/5429  beschlossen:   Der Vorlageantrag vom 5.6.2020 wird gemäß § 260 Abs. 1 lit.b BAO in Verbindung mit § 264  Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michael Mühlbeck` | `Michael Mühlbeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Glöckler 35, 5252 Parz, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `92-602/5429` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Malik Stellmaszick, Am Weberbach 26, 9640 Gailberg, Österreich, über die Beschwerde vom 19. November 2012 gegen den Bescheid  des FA Wien 1/23 vom 8. November 2012 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2011, Steuernummer 92-110/0462  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Malik Stellmaszick` | `Malik Stellmaszick` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Am Weberbach 26, 9640 Gailberg, Österreich` (address)
- `FA Wien 1/23` (organisation)
- `92-110/0462` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Erhard Wintjens, Völkerweg 97, 8940 Döllach, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 17-868/7871  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erhard Wintjens` | `Erhard Wintjens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Völkerweg 97, 8940 Döllach, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `17-868/7871` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Adrian Radakovitsch` | `Adrian Radakovitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Merlin Thorschmidt` (person)
- `Schlatterbergweg 97, 9344 Psein, Österreich` (address)
- `Finanzamt Steiermark Mitte` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer in der Beschwerdesache  Silvius Fingermann, Steibstraße 113, 5723 Litzldorf, Österreich, über die Beschwerde vom 3. Mai 2018 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 5. April 2018 betreffend Anspruchszinsen (§ 205 BAO) 2013,  Steuernummer 91-977/4633, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvius Fingermann` | `Silvius Fingermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Diana Sammer` (person)
- `Steibstraße 113, 5723 Litzldorf, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)
- `91-977/4633` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/132524.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132524.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Corinna Royackers  in der Beschwerdesache Lena Grobbing,  Johann Burkl-Gasse 58, 4170 Unterriedl, Österreich, betreffend Beschwerde vom 1. Mai 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 12. April 2019 hinsichtlich Wiederaufnahme § 303 BAO /  ESt 2016,  Steuernummer 94-382/8878  den Beschluss gefasst:  I.  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lena Grobbing` | `Lena Grobbing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Corinna Royackers` (person)
- `Johann Burkl-Gasse 58, 4170 Unterriedl, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `94-382/8878` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Samir Schwahn,  Pichlmoarstraße 73, 3653 Ottenberg, Österreich, über die Beschwerde vom 7. Jänner 2016  gegen den Bescheid des  Finanzamtes Österreich vom 9. Dezember 2015 betreffend Abweisung des Antrags auf  Ausgleichszahlung (Familienbeihilfe 01.2010-12.2015 ) zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 9. Dezember 2015 wird gemäß § 279 Abs. 1 BAO  abgewiesen.

| Predicted | Gold |
|---|---|
| `Samir Schwahn` | `Samir Schwahn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pichlmoarstraße 73, 3653 Ottenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Franka Hilgenstock, Bockackerstraße 19, 4892 Sieberer, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Franka Hilgenstock` | `Franka Hilgenstock` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Bockackerstraße 19, 4892 Sieberer, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Bodo Friehmann, Hohenwartweg 2, 4851 Fischham, Österreich, über die Beschwerde vom 30. September 2019 gegen den Einkommensteuerbescheid  2016 und den Einkommensteuerbescheid 2017 des Finanzamtes Wien 1/23 vom 27. August  2019 zu Steuernummer 09 75-279/5529  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bodo Friehmann` | `Bodo Friehmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hohenwartweg 2, 4851 Fischham, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `75-279/5529` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rocco Girstenbrei, Waubergweg 6, 9710 Pöllan, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rocco Girstenbrei` | `Rocco Girstenbrei` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Waubergweg 6, 9710 Pöllan, Österreich` (address)
- `Dr. Maria Brandstetter` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Oleg Bösehans  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 80-404/4147, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oleg Bösehans` | `Oleg Bösehans` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `80-404/4147` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Helga Zeißig, Im Markt 12, 5733 Bramberg am Wildkogel, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Helga Zeißig` | `Helga Zeißig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Im Markt 12, 5733 Bramberg am Wildkogel, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/133011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133011.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Helena Przybilowski  in der Beschwerdesache Michaela Lomanns,  Kolmtaler Weg 694, 4294 Wenigfirling, Österreich, vertreten durch Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H,  Wienerstraße 73, 2604 Theresienfeld, betreffend Beschwerde vom 28. Februar 2020 gegen die  Bescheide des Finanzamtes Baden Mödling vom 31. Jänner 2020 betreffend Einkommensteuer  2015, 2016 und 2017, Steuernummer 73-613/0108, beschlossen:  Die Vorlageanträge vom 16. Februar 2021 gegen die Beschwerdevorentscheidungen 2015,  2016 und 2017 vom 15. Jänner 2021 werden gemäß § 260 Abs. 1 lit b BAO in Verbindung mit  § 264 Abs. 4 lit e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michaela Lomanns` | `Michaela Lomanns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Helena Przybilowski` (person)
- `Kolmtaler Weg 694, 4294 Wenigfirling, Österreich` (address)
- `Mag. Marion Mayer Steuerberatungsgesellschaft m.b.H` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `73-613/0108` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Daniela Weickhart  in der Beschwerdesache Cäcilia Lüderitz,  Zallingergasse 21, 9372 St. Walburgen, Österreich, über die Beschwerde vom 2. Jänner 2020 gegen den Abweisungsbescheid des  Finanzamtes Bruck Leoben Mürzzuschlag vom 4. Dezember 2019 betreffend Familienbeihilfe  für sich selbst ab November 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Cäcilia Lüderitz` | `Cäcilia Lüderitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Daniela Weickhart` (person)
- `Zallingergasse 21, 9372 St. Walburgen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/133037.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133037.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Marcel Tummernicht, Gesern 3, 9433 Kienberg, Österreich, über die Beschwerde vom 9. November 2017  gegen den Bescheid des Finanzamtes Österreich vom 19. Oktober 2017 betreffend Haftung für  Kapitalertragsteuer für die Jahre 2009 bis 2012, Steuernummer 30-367/8113, zu Recht  erkannt:   Der Beschwerde betreffend Haftung für Kapitalertragsteuer 2009 wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marcel Tummernicht` | `Marcel Tummernicht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Gesern 3, 9433 Kienberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `30-367/8113` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/133114.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133114.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Heinz Clee, Am Seeweg 250, 4284 Schmierreith, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 8.1.2020  gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich)  betreffend  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2013 vom 12.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2014 vom 13.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2015 vom 13.12.2019  zu Recht erkannt:   I. Soweit sich die Beschwerden vom 8.1.2020 gegen die Bescheide über die  Wiederaufnahme der Verfahren betreffend Einkommensteuer 2013, 2014 und 2015  richten, wird diesen gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Heinz Clee` | `Heinz Clee` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Am Seeweg 250, 4284 Schmierreith, Österreich` (address)
- `Pallauf Meißnitzer Staindl & Partner` (organisation)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Raphael Williamson, BEd, Züggen 8, 8042 Graz, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Raphael Williamson` — partial — pred is substring of gold: `Raphael Williamson, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Raphael Williamson, BEd`(person)
- `Züggen 8, 8042 Graz, Österreich`(address)
- `Monika Pfundner-Lenz`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Muran Waldhans` — partial — pred is substring of gold: `Muran Waldhans, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Viktoria Kreiselmayer`(person)
- `Muran Waldhans, BEd`(person)
- `Am Tegel 5, 9831 Waben, Österreich`(address)
- `Corazza Kocholl Laimer Rechtsanwälte OG`(organisation)
- `Finanzamtes Innsbruck`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Miroslav Hankel` — partial — pred is substring of gold: `Miroslav Hankel, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miroslav Hankel, BEd`(person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz.in DDr.in Rafaela Ringart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in DDr.in Rafaela Ringart`(person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich`(address)
- `Silvestri Bau GmbH`(organisation)
- `Mag. WP`(person)
- `38-663/2876`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dominik Kuzu Bf` — partial — gold is substring of pred: `Dominik Kuzu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Niels Aleksejew`(person)
- `Dominik Kuzu`(person)
- `Finanzamt Spittal Villach`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Vincent` — partial — pred is substring of gold: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. ÖkR Horst Stevens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Alwerkmon-Pharma,  Hinteralm 4, 3243 Lachau, Österreich  vertreten durch Stb., über die Beschwerde vom 17.10.2011 gegen den Bescheid  des Finanzamtes Lilienfeld St. Pölten vom 13.7.2011 betreffend Einkommensteuer 2009 nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Alwerkmon` — partial — pred is substring of gold: `Alwerkmon-Pharma`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Alwerkmon-Pharma`(organisation)
- `Hinteralm 4, 3243 Lachau, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

**False Positives:**

- `Dorfcongart` — partial — pred is substring of gold: `Dorfcongart-Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Klara Willumelies`(person)
- `Dorfcongart-Event`(organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich`(address)
- `Finanzamtes  Neunkirchen Wr. Neustadt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R HR Martina Pisterer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Techn R HR Martina Pisterer`(person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Natalie Gosebrink` — partial — pred is substring of gold: `Natalie Gosebrink, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alessia Olschofski`(person)
- `Natalie Gosebrink, Bakk. phil.`(person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich`(address)
- `Finanzamtes für  Gebühren`(organisation)
- `50-818/5472`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl. Kff. Cäcilia Wlcek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Stefan Pipal`(person)
- `Dipl. Kff. Cäcilia Wlcek`(person)
- `Rambergweg 3, 4950 Weidenthal, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Valentin Kreuthmayr  in der Beschwerdesache Naomi Ruddis, LLB,  Schuselkagasse 21, 9570 Alt-Ossiach, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 10. März 2020 betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für sich selbst ab Jänner 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Naomi Ruddis` — partial — pred is substring of gold: `Naomi Ruddis, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Valentin Kreuthmayr`(person)
- `Naomi Ruddis, LLB`(person)
- `Schuselkagasse 21, 9570 Alt-Ossiach, Österreich`(address)
- `Finanzamt Niederösterreich Mitte`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Jonathan Hewett, Bakk. techn., Kleinbodenerstraße 17, 4880 Rixing, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Jonathan Hewett` — partial — pred is substring of gold: `Jonathan Hewett, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jonathan Hewett, Bakk. techn.`(person)
- `Kleinbodenerstraße 17, 4880 Rixing, Österreich`(address)
- `Mag. Anton Heisinger`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dipl` — partial — pred is substring of gold: `Dipl.-Ing. Waldemar Zumloh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Michael Mandlmayr`(person)
- `Dipl.-Ing. Waldemar Zumloh`(person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `09-591/1655`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RgR OMedR Miklos Pellegrin, Ostendeweg 9, 9981 Glor-Berg, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 73-541/6746, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rg` — similar text (different position): `Dr. Ansgar Unterberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `RgR OMedR Miklos Pellegrin`(person)
- `Ostendeweg 9, 9981 Glor-Berg, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `73-541/6746`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Eduard Schulden, Bakk. rer. nat., Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich, vertreten durch Dkfm. Freund & Partner Steuerberater GmbH, Schellinggasse 3, 1010  Wien, über die Beschwerde vom 29. Juli 2016 (Eingangsstempel 1. August 2016 ) gegen den  Umsatzsteuerbescheid 2011 und den Bescheid über die Feststellung von Einkünften gemäß  § 188 BAO 2011 des Finanzamtes Baden Mödling vom 5. Juli 2016, Steuernummer  16 28-951/9095, zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Eduard Schulden` — partial — pred is substring of gold: `Eduard Schulden, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Eduard Schulden, Bakk. rer. nat.`(person)
- `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich`(address)
- `Freund & Partner Steuerberater GmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `28-951/9095`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Jennifer Kuntzemann, MSc Bakk. iur., Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich, über die Beschwerde vom 11. April 2020 gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 11. März 2020 betreffend  Rückzahlung ausbezahlter Zuschüsse zum Kinderbetreuungsgeld für das Jahr 2014,  Steuernummer StrNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Jennifer Kuntzemann` — partial — pred is substring of gold: `Jennifer Kuntzemann, MSc Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Monika Kofler`(person)
- `Jennifer Kuntzemann, MSc Bakk. iur.`(person)
- `Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich`(address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

</details>

---

## `von_title_name` 

**F1:** 0.003 | **Precision:** 0.800 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `211a4808`  
**Description:**
Captures names following 'von' + Title (e.g., 'von Herrn Esra Lindacher', 'von Dr. Stephan Schiwy') to extract the name without the title.

**Content:**
```
(?:von\s+(?:Herrn|Herr|Frau|Fr\.\s+|Dr\.|Mag\.|Prof\.|Univ\.-?Prof\.|Priv\.-?Doz\.|Hon\.-?Prof\.|Ing\.|Dipl\.-?Ing\.|Bakk\.|StR\s+|OMedR\s+|KzlR\s+|\u00d6kR\s+|RgR\s+|MedR\s+|KommR\s+|Vizepr\u00e4sident\s+|Senatspr\u00e4sident\s+|Hofrat\s+|Hofr\u00e4tin\s+|Hofr\u00e4ts\s+|Vizepr\u00e4sidentin\s+|Senatspr\u00e4sidentin\s+|Dr\.in|Mag\.a)\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.002 | 0.003 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 1 | 2127 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Floriane Herppich  nicht gemangelt hat, Frau Floriane Herppich  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/136739.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136739.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache von Frau Christina Schnellhard, Schießstättgasse 15, 3744 Klein-Meiseldorf, Österreich, vertreten durch Dr. Margit Kaufmann,  Hammerschmidtgasse 18/Haus 4/1, 1190 Wien, betreffend Beschwerde vom 23. Dezember  2020 gegen den Bescheid des damaligen Finanzamtes Wien 4/5/10 vom 10. Dezember 2020  betreffend Haftung gemäß §§ 9, 80 ff Bundesabgabenordnung, Steuernummer  68-538/7874  beschlossen:   Die Beschwerde vom 23. Dezember 2020 wird gemäß § 260 Abs. 1 lit. a BAO iVm § 93 Abs. 2  BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Christina Schnellhard` | `Christina Schnellhard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Schießstättgasse 15, 3744 Klein-Meiseldorf, Österreich` (address)
- `Dr. Margit Kaufmann` (person)
- `Finanzamtes Wien 4/5/10` (organisation)
- `68-538/7874` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/145288.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145288.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Konstanze Roeschel  in der Beschwerdesache von Frau  Alva Wuensch, Söllhamer Straße 2, 8742 Kienberg, Österreich, über    die Beschwerde vom 23.12.2013 gegen den Bescheid des Finanzamtes Wien 1/23  (nunmehr Finanzamt Österreich) vom 25.11.2013 betreffend Einkommensteuer 2003,    die Beschwerde vom 23.12.2013 gegen den Bescheid des Finanzamtes Wien 1/23  (nunmehr Finanzamt Österreich) vom 25.11.2013 betreffend Einkommensteuer 2004,    die Beschwerde vom 19.05.2014 gegen den Bescheid des Finanzamtes Wien 1/23  (nunmehr Finanzamt Österreich) vom 06.05.2014 betreffend Einkommensteuer 2013   zu Steuernummer 01-981/9185  beschlossen:  I. Die Beschwerden werden gemäß § 261 Abs 1 lit a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Alva Wuensch` | `Alva Wuensch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Konstanze Roeschel` (person)
- `Söllhamer Straße 2, 8742 Kienberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `01-981/9185` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/145291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145291.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Univ.-Prof.in Elvira Mülke  in der Beschwerdesache von Frau  Wilhelmine Tsirakidis, Agathaweg 77, 4540 Pfarrkirchen bei Bad Hall, Österreich  betreffend die Beschwerde vom 14. April 2014, eingebracht am 17.  April 2014, gegen den Bescheid des Finanzamtes Wien 1/23 vom 11. März 2014 betreffend  Verspätungszuschlag 2011 zu der Steuernummer 64-651/6333  beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wilhelmine Tsirakidis` | `Wilhelmine Tsirakidis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Univ.-Prof.in Elvira Mülke` (person)
- `Agathaweg 77, 4540 Pfarrkirchen bei Bad Hall, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `64-651/6333` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/149407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149407.1_99`)


Der Hund sei im Besitz von Frau Schweinebarth Der Hund sei  in CZ registriert.

**False Positives:**

- `Schweinebarth Der Hund` — partial — gold is substring of pred: `Schweinebarth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schweinebarth`(person)

</details>

---

## `herr_context_name` 🏆

**F1:** 0.092 | **Precision:** 0.678 | **Recall:** 0.049  

**Format:** `regex`  
**Rule ID:** `5e5a7a12`  
**Description:**
Captures names following 'Herr' or 'Herrn', requiring a capitalized surname or initial, and allowing optional post-nominal titles (e.g., DI, LLM, Dr.). Excludes common nouns like 'Kollegen' or 'Zeuge'.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)Herr(?:n)?\s+((?:[A-Z][a-zäöüßéèêëïîôùûü]+|[A-Z]\.)+(?:\s+(?:[A-Z][a-zäöüßéèêëïîôùûü]+|[A-Z]\.)+)*)\s*(?:,\s*(?:LLM|Dr\.?|Dipl\.?|Ing\.?|DI|B\.?|BEd|PhD|etc\.?))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.678 | 0.049 | 0.092 | 174 | 118 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 118 | 56 | 2214 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_92`)


Mit dieser E-Mail entgegnete der Bf in Beantwortung des Vorhaltes der belangten Behörde wie  folgt:   "Ich darf auf Ihr Email vom 06.06.2017 in Sachen Beschwerde Bf — StNr. 61 68-535/9689  zurückkommen und nach Besprechung mit Herrn Noeltge folgenden Lösungsvorschlag unterbreiten:  Grundsätzliche Überlegung:  Der VwGH vertritt in seinem Erkenntnis vom 29.03.2017 zur Hauptwohnsitzbefreiung die  Ansicht, dass sich die Befreiungsbestimmung des § 30 Abs. 2 Z 1 EStG lediglich auf den Grund  und Boden eines bebauten Grundstücks erstreckt, der nach der Verkehrsauffassung einem  üblicherweise als Bauplatz erforderlichen Grundstück entspricht.

| Predicted | Gold |
|---|---|
| `Noeltge` | `Noeltge` |

**Missed by this rule (FN):**

- `68-535/9689` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_106`)


Aus ökonomische Überlegungen (Vermeidung von Sachverständigen- und anderen  Rechtskosten bzw. zur Erlangung von Rechtssicherheit) wäre Herr Noeltge mit folgender Lösung, die  zwar sachlich stark vereinfachend ist, aber auch durch die Erlasslage gedeckt scheint  (Grundanteil lt. VO, Schätzung der anteiligen Anschaffungskosten der steuerhängigen Fläche  nach § 184 BAO aufgrund des VPI = nachvollziehbare Schätzmethode, die auch wie unten  dargestellt nach steuerlichen Grundsätzen plausibilisierbar ist) einverstanden:  Wie von Ihnen vorgeschlagen wird der Grundanteil mit 20% (lt. VO) angenommen und  aliquotiert in einen Teil von 1.000 m2 steuerbefreit und 1.144 m2 steuerpflichtig.

| Predicted | Gold |
|---|---|
| `Noeltge` | `Noeltge` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_30`)


Lfd.Nr. Bezeichnung der körperlichen, geistigen oder sinnesbedingten  Funktionseinschränkungen, welche voraussichtlich länger als sechs Monate andauern werden:  Begründung der Rahmensätze: Pos.Nr. Gdb%  1 paranoide Schizophrenie  Unterer Rahmensatz, da verminderte psychische Belastbarkeit 03.07.02 50  Gesamtgrad der Behinderung 50 v. H.  Begründung für den Gesamtgrad der Behinderung:  Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keine Änderung gegenüber dem VGA von 9/2015  der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 07/2014  Herr Hademar Berking  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_111`)


Herr Hademar Berking  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_172`)


Vorgutachten 14 08 2018:   paranoide Schizophrenie GdB 50%   seit 07/2014   Herr Hademar Berking  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA    Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_219`)


Herr Hademar Berking  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA   Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_57`)


Der Mietvertrag lautet auf Herrn Lukasz Jan Chlebek.

| Predicted | Gold |
|---|---|
| `Lukasz Jan Chlebek` | `Lukasz Jan Chlebek` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130564.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130564.1_15`)


Die Strafverfügung wurde Ihnen zugestellt und Sie erhoben fristgerecht Einspruch und gaben  erneut Herrn Schnak  geboren am geb, wohnhaft in AdrHerr, als Lenker an.

| Predicted | Gold |
|---|---|
| `Schnak` | `Schnak` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_5`)


Bescheide der Abgabenbehörde  Mit Einkommensteuerbescheid 2013 vom 5.4.2018 wurde für das Jahr 2013 aus der  Arbeitnehmerveranlagung des Herrn Silvius Fingermann (in der Folge kurz: Bf.) eine Abgabengutschrift  in Höhe von € 1.649,00 festgestellt. Aufgrund dieser Gutschrift erfolgte - ebenfalls mit Bescheid  vom 5.4.2018 - die Berechnung der Anspruchszinsen, woraus sich eine Gutschrift für das Jahr  2013 in Höhe von € 93,06 ergab.

| Predicted | Gold |
|---|---|
| `Silvius Fingermann` | `Silvius Fingermann` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_28`)


Mit fristgerechter E-Mail vom 17. Februar 2021 führte der Bf. die drei vorgenannten GZen an  und brachte vor:  „Zu dieser Zeit habe ich in Linz gewohnt und gearbeitet und das Auto mit dem Kennzeichen 123  habe ich für einige Wochen Herrn Flachmeier  geboren am geb überlassen, da er damals neu in  Österreich war und er das Auto nötiger hatte als ich.

| Predicted | Gold |
|---|---|
| `Flachmeier` | `Flachmeier` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_36`)


In dieser Niederschrift wurde festgehalten, dass lediglich Herr Ruhkopf mit diesem  Auto fuhr.

| Predicted | Gold |
|---|---|
| `Ruhkopf` | `Ruhkopf` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_83`)


Das streitgegenständliche Kfz wurde nur von Herrn Hus  gefahren, welcher   im Streitjahr 2011 als einer der beiden unbeschränkt haftenden Gesellschafter der Bf.  maßgebenden Einfluss auf die Bf. hatte;

| Predicted | Gold |
|---|---|
| `Hus` | `Hus` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_88`)


Wie aus dem Beschwerdeverfahren des BFG zu GZ. RV/4100396/2016 – betreffend die  Vorschreibung von Kfz-Steuer und NoVA an Herrn Dilaver wegen Privatnutzung des  nicht angemeldeten, streitgegenständliche Kfz durch das Finanzamt Spittal Villach –  hervorgeht, präsentierte Herr Ruhkopf das streitgegenständliche Kfz von 2011 bis  2015 jährlich beim Sportwagentreffen in KärntnerOrt, wobei er sich einen Verkaufspreis von  ca. 300.000,00 € vorstellte.

| Predicted | Gold |
|---|---|
| `Dilaver` | `Dilaver` |
| `Ruhkopf` | `Ruhkopf` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `Finanzamt Spittal Villach` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_90`)


Primäre Zweckbestimmung des streitgegenständlichen Kfz, welches sich ab dem Erwerb im  Jahr 2011 bis zum Verkauf im Jahr 2016 im zivilrechtlichen Eigentum der Bf. befand, war die  Ermöglichung der Nutzung durch Herrn Hus  welcher wie ein  Eigentümer über das Kfz verfügte.

| Predicted | Gold |
|---|---|
| `Hus` | `Hus` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_94`)


Es ist auch daraus zu  schließen, dass der zivilrechtliche Verkauf des Kfz von der Bf. an die KomplementärGes m.b.H.  im Jahr 2016 nichts daran änderte, dass Herr Ruhkopf weiterhin – nunmehr als  Geschäftsführer der KomplementärGes m.b.H. – vollen Zugriff auf das Kfz hatte.

| Predicted | Gold |
|---|---|
| `Ruhkopf` | `Ruhkopf` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_95`)


Daraus resultiert, dass das streitgegenständliche Kfz vom Kauf im Jahr 2011 bis zum Verkauf im  Jahr 2016 nicht im wirtschaftlichen Eigentum der Bf., sondern im wirtschaftlichen Eigentum  von Herrn Dilaver gestanden ist.

| Predicted | Gold |
|---|---|
| `Dilaver` | `Dilaver` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_36`)


Herr Wolfgang Orosz  wird ohne sachliche Grundlage um 123 TEUR entreichert, während in  vergleichbaren Fällen im betrieblichen Bereich dies nicht geschieht.

| Predicted | Gold |
|---|---|
| `Wolfgang Orosz` | `Wolfgang Orosz` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_72`)


Während die nach der AP an den Masseverwalter der L- GmbH i.L. ergangenen Bescheide  unbekämpft in Rechtskraft erwuchsen, brachte die T-Datenverarbeitungs GmbH gegen die  KeSt-Bescheide 2007-2009 namens des Bf fristgerecht Berufung ein, die in einem  nachgereichten Schriftsatz wir folgt begründet wurde:  „Wir als Vertretung (Vollmacht liegt auf) und im Auftrag und Rücksprache mit Herrn  Patrick Kirschbauer, legen wir folgenden Sachverhalt dar:  Tz. 4 Kapitalertragssteuer verdeckte Gewinnausschüttung  Jahr 2007  1.)

| Predicted | Gold |
|---|---|
| `Patrick Kirschbauer` | `Patrick Kirschbauer` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_99`)


Wegen  detaillierten Leistungsaufzeichnungen müssen wir darauf hinweisen, dass diese nicht vorliegen,  da sämtliche Unterlagen an die neue Geschäftsleitung Herrn Rubarth übergeben wurden.

| Predicted | Gold |
|---|---|
| `Rubarth` | `Rubarth` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_100`)


Zusammenfassend muss schon gesagt werden, dass von der Seite der Buchhaltungsführung  durch die Kanzlei XY zu groben Fehlern gekommen ist die Herrn Oeverhaus nicht  bekannt sein konnten, da er im vollen Vertrauen die Firmenunterlagen zur Bearbeitung  abgegeben hat und diese Arbeiten naturgemäß nicht geprüft hat.

| Predicted | Gold |
|---|---|
| `Oeverhaus` | `Oeverhaus` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_101`)


Das auch wie der Kunde, A.- Fenster sonderliche Buchungen durchgeführt hat, ist auch nicht Herrn Oeverhaus zu  zuschreiben.

| Predicted | Gold |
|---|---|
| `Oeverhaus` | `Oeverhaus` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_104`)


Herr Patrick Kirschbauer  ersucht daher höflich um Aufhebung der Bescheide über die Festsetzung der  Kapitalertragssteuer für die Jahre 2007 über € 17.853,95, sowie für 2008 über € 20.933,35 und  2009 über € 8.350,00.“

| Predicted | Gold |
|---|---|
| `Patrick Kirschbauer` | `Patrick Kirschbauer` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_144`)


2. Die Gesellschafter der Weierstrass Textil  haben bisher mündlich vereinbart und halten  hinsichtlich des Geschäftsführerbezuges von Herrn Siegfried Terentew  folgendes fest: Herr  Siegfried Terentew  erhält einen fixen Geschäftsführerbezug von € 30.000,00 pro Jahr bzw. €  7 von 16 Seite 8 von 16

| Predicted | Gold |
|---|---|
| `Siegfried Terentew` | `Siegfried Terentew` |
| `Siegfried Terentew` | `Siegfried Terentew` |

**Missed by this rule (FN):**

- `Weierstrass Textil` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_145`)


2.500, 00 monatlich, des weiteren erhält Herr Siegfried Terentew  einen variablen Bezug von  max.

| Predicted | Gold |
|---|---|
| `Siegfried Terentew` | `Siegfried Terentew` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_6`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. Firmenbuch-  und Grundbuchdaten ergibt sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung  als erwiesen zu Grunde legt:  Adressat der angefochtenen Erledigung ist Herr Ronald Jundt (nachfolgend Herr M.), der  aufgrund eines Kaufvertrages vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel  Miteigentümer jener Liegenschaft war, auf welcher der strittige Rohbau errichtet wurde  (Lageadresse: R-Gasse 15, 9999 Wien).

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)
- `BFG` (organisation)
- `M.` (person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_8`)


Herr M. war im Verfahrenszeitraum Geschäftsführer der Furtnex-Versand GmbH (nachfolgend M.-GmbH,  Insolvenz 9/2019 – 7/2020) und ist geschäftsführender Alleingesellschafter der R-Gasse 15  Immobilienverwertungs GmbH, FN 999999x (nachfolgend Immo-GmbH) sowie Ehemann von  FrauM., deren Rechtsmittelverfahren beim BFG zu den Zahlen RV/7101720/2021 bzw.  RV/7101724/2021 erfasst sind.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)
- `BFG` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_9`)


Herr M. erzielte nach den Daten seines Abgabenkontos langjährig, neben geringfügigen  Einkünften aus der Untervermietung einer Mietwohnung in der S-Straße 3/ 4, 9998 Wien an  die Immo-GmbH, ausschließlich Einkünfte aus steuerfreien Transferleistungen (AMS/GKK).

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `AMS/GKK` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_12`)


In den - handschriftlich erstellten – Einkommensteuer-(ESt-) Erklärungen bis 2017 ließ Herr M.  das Feld für die Bekanntgabe eines steuerlichen Vertreters jeweils ohne Eintragung.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_13`)


Entsprechend waren die (erklärungsgemäß ohne steuerliche Auswirkung ergehenden)  ESt-Bescheide an die Wohnadressen des Herrn M. adressiert.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_14`)


Nachdem Herr M. in einem (handschriftlich verfassten) Begleitschreiben zur  ESt-Erklärung 2017 mitgeteilt hatte, dass er „die vermietete Wohnung in der S-Straße 3/ 4,  9998 Wien“ „seit Ende August 2018“ „an die Hausverwaltung zurückgegeben habe“, reichte er  keine Abgabenerklärungen mehr ein.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_16`)


Zuletzt  erging ein antragsloser ANV-Bescheid für 2019 an Herrn M.  Eine steuerliche Vertretung oder Zustellbevollmächtigung für Herrn M. ist in der  abgabenbehördlichen Datenbank bis heute nicht erfasst (Quellen: abgabenbehördliche  Datenbank DB2, Grundbuch, Firmenbuch).

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_25`)


Die Inanspruchnahme von Herrn Ronald Jundt  als Zahlungsverpflichteter erfolgte, weil die als  Leistungsgerbringerin fungierende Furtnex-Versand GmbH in Liqu. ihrer Zahlungsverpflichtung nicht  nachgekommen ist.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_32`)


Beschwerde gegen den Bescheid - Leistungsgebot  Meine Beschwerde richtet sich gegen den Bescheid-Leistungsgebot an Herrn Ronald Jundt  vom  5.11.2019, zugestellt am 13.11.2019, mit dem Antrag auf Aufhebung dieses Bescheides.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_33`)


Als Begründung ist anzuführen, dass Herr Ronald Jundt  kein Gesamtschuldner aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der Furtnex-Versand GmbH nicht um Bauleistungen handelt.  Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  Zur Korrektur des Irrtums wurden die Rechnungen berichtigt, neu ausgestellt mit  Umsatzsteuerausweis von 20 % und bezahlt gemäß dem Prüfungsergebnis.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_41`)


Dr. X.Y.“  (BFG-Anm: Fertigung mit unleserlicher Unterschrift und Firmenstampiglie der Kirstin Frischbutter  Wirtschaftstreuhandgesellschaft m.b.H.(nachfolgend Mur-Sanitär GmbH.  In Erledigung dieser Beschwerde erging am 30.Nov.2020 zur Steuernummer (StNr.) der  M.-GmbH eine abweisende Beschwerdevorentscheidung (BVE) an Herrn M. (Direktzustellung  an Herrn M. mit geänderter Bescheidadresse;

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Dr. X.Y.` (person)
- `Kirstin Frischbutter` (person)
- `Mur-Sanitär GmbH` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_43`)


Mit Schriftsatz vom 11.Jänner 2019 schritt erstmals die im Spruch des gegenständlichen  Beschlusses angeführte Rechtsvertretung für Herrn M. ein und beantragte zur selben StNr.  unter Vollmachtsbekanntgabe im Namen von Herrn M. als Beschwerdeführer eine  Bescheidaufhebung im Rahmen einer Entscheidung des BFG über die Beschwerde des Herrn M.  gegen den „Bescheid Leistungsgebot vom 5.11.2019“.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |
| `M.` | `M.` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_91`)


Gem. § 246 Abs. 1 BAO war daher allein Herr M. zur Einbringung einer Bescheidbeschwerde  befugt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_101`)


Der Erwähnung von Herrn M. im Betreff der Beschwerde kommt beim vorliegenden  Sachverhalt - nicht zuletzt in Hinblick auf die am selben Tag ergangenen Bescheide an die  beiden weiteren Miteigentümer der Liegenschaft R-Gasse 15 - die Bedeutung eines bloßen  Konkretisierungsmerkmales für die Bezug habende Erledigung zu.   Eine explizite Berufung auf die erteilte Vollmacht findet sich erstmals im Vorlageantrag vom  11. Jänner 2020, der von einer damit erstmalig und ohne Bezug zur Mur-Sanitär GmbH für Herrn M.  einschreitenden Rechtsvertretung eingebracht wurde.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Mur-Sanitär GmbH` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_104`)


Da die Abgabenbehörde auch nicht via FinanzOnline-Zugang des Herrn M. über eine  Bevollmächtigung der Mur-Sanitär GmbH informiert war und Herr M. selbst kein Verhalten setzte, das  die Annahme einer Anscheinsvollmacht der Mur-Sanitär GmbH rechtfertigen konnte (vgl. VwGH  28.10.2014, 2012/13/0102;

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Mur-Sanitär GmbH` (organisation)
- `Mur-Sanitär GmbH` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_106`)


Die Beschwerde vom 4.Dez.2019 gegen  den an Herrn M. ergangenen „Bescheid – Leistungsgebot“ vom 5.Nov.2019 war daher als  unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_87`)


Ich bitte Sie für diesen Zeitraum den Krankenstand zu gewähren.“   < Schreiben des Arbeitgebers vom 28. Jänner 2019:  „Hiermit wird bestätigt, dass kein Einwand besteht, dass Herr Franziskus während des  6 von 13 Seite 7 von 13

| Predicted | Gold |
|---|---|
| `Franziskus` | `Franziskus` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_6`)


Demnach habe Herr  Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_17`)


Demnach habe Herr  Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_29`)


Demnach habe Herr  Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_52`)


Demnach  habe Herr Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_21`)


Hinweis:  Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Leander Krupa  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Missed by this rule (FN):**

- `Finanzamt für Gebühren` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_22`)


Nach den Angaben von Herrn Leander Krupa sollten auf diesem Datenträger alle notwendigen  Unterlagen gespeichert sein, welche für die ordnungsgemäße Selbstberechnung notwendig  gewesen sind (siehe dazu auch die Ausführungen in der Einleitung).

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_24`)


In einer Besprechung vom 16.1.2015 hat Herr Leander Krupa zu  diesem Thema ua. angegeben, dass Schätzungsgutachten sich heute nicht in seinen Akten  befinden und er zum Zeitpunkt der Selbstberechnung davon ausgegangen ist, dass der  vereinbarte Kaufpreis zumindest dem gemeinen Wert entspricht und er sich damals auf die  Auskünfte der Vertragsparteien verlassen habe, wonach der Wert (gemeint gemeiner Wert)  dem vereinbarten Kaufpreis entspricht.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_25`)


Weiter hat Herr Leander Krupa angegeben, dass er zu allen  betroffenen Selbstberechnungen die entsprechenden Nachweise vorlegen wird.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_26`)


Mit Mail vom 9.2.2015 teilt Herr Leander Krupa dem Finanzamt für Gebühren Verkehrsteuern und  Glücksspiel mit, dass sich die entsprechenden Berechnungsgrundlagen (gemeint Nachweise  über die gemeinen Werte) bei der Firma K (die Bf) befinden.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Missed by this rule (FN):**

- `Finanzamt für Gebühren` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/138498.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138498.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Im Rahmen der am 17.02.2020 eingereichten Erklärung zur Arbeitnehmerveranlagung 2019  wurde durch Herrn Gisbert Paßerschroer (in der Folge „Bf“ oder „Beschwerdeführer“) die Gewährung des  (ganzen) Familienbonus Plus für 12 Monate beantragt.

| Predicted | Gold |
|---|---|
| `Gisbert Paßerschroer` | `Gisbert Paßerschroer` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_26`)


Da es sich bei dem  Guntram Beinling  auch um keinen berufsmäßigen Parteienvertreter handelt, kann auch nicht  davon ausgegangen werden, dass dieses regelmäßig für andere einschreitet, weshalb der  Wortlaut seiner Beschwerde, in dem Herr Guntram Beinling  ausdrücklich im eigenen Namen  Beschwerde erhebt, auch zu keinen Zweifeln Anlass geben konnte.

| Predicted | Gold |
|---|---|
| `Guntram Beinling` | `Guntram Beinling` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Verwaltungsstrafsache gegen Herrn Brunhild Stanislav, Johann Hoffer-Weg 990, 8385 Neuhaus am Klausenbach, Österreich, vertreten durch Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH, Tuchlauben 11/18, 1010 Wien, wegen der  Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifen D Post  1 und D Post 4 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der derzeit geltenden Fassung über die Beschwerde des Beschuldigten vom 4. März 2022  gegen   I. das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020,   II. das Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020,   nach Durchführung einer mündlichen Verhandlung am 15. Dezember 2022 in Abwesenheit des  Beschuldigten, jedoch in Anwesenheit der Verteidigerin, auch als Vertreterin der haftenden  GmbH, der Behördenvertreterin und der Schriftführerin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als bei  unverändert bleibenden Schuldsprüchen die Höhe der Strafen und der Kosten wie folgt  geändert werden:  II. Wegen der Verwaltungsübertretungen laut Erkenntnis vom 3. Februar 2022, GZ.  MA6/206000003074/2020, werden über den Beschuldigten folgende Strafen jeweils gemäß  § 16 Abs. 1 GAG LGBl. für Wien Nr. 20, in der derzeit geltenden Fassung verhängt:   1. – 5. Geldstrafen in Höhe von je € 330,00, falls diese uneinbringlich sind,   5 Ersatzfreiheitsstrafen von je 11 Stunden,   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Brunhild Stanislav` | `Brunhild Stanislav` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Johann Hoffer-Weg 990, 8385 Neuhaus am Klausenbach, Österreich` (address)
- `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` (organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_36`)


Die KI Synlogtra GmbH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Brunhild Stanislav, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00  und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Brunhild Stanislav` | `Brunhild Stanislav` |

**Missed by this rule (FN):**

- `KI Synlogtra GmbH` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_37`)


II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020, wurde Herr Brunhild Stanislav, (in weiterer Folge: Beschuldigter) als  handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  mit Sitz in Altfinkensteiner Weg 15, 9065 Moosberg, Österreich,  schuldig erkannt,   1. er habe als handelsrechtlicher Geschäftsführer der Firma KI Synlogtra GmbH  im Juni 2020 vor  der Liegenschaft in An der Welserbahn 27, 3763 Sabatenreith, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür  bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `Brunhild Stanislav` | `Brunhild Stanislav` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `KI Synlogtra GmbH` (organisation)
- `Altfinkensteiner Weg 15, 9065 Moosberg, Österreich` (address)
- `KI Synlogtra GmbH` (organisation)
- `An der Welserbahn 27, 3763 Sabatenreith, Österreich` (address)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_62`)


Die KI Synlogtra GmbH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Brunhild Stanislav, verhängten Geldstrafen von 3 x je € 520,00, 3 x je € 320,00 und 2  x je € 700,00 und die Verfahrenskosten in der Höhe von € 392,00 sowie für sonstige in Geld  bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.“

| Predicted | Gold |
|---|---|
| `Brunhild Stanislav` | `Brunhild Stanislav` |

**Missed by this rule (FN):**

- `KI Synlogtra GmbH` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/140794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140794.1_4`)


Begründung  Beschwerdeführer (Bf) ist Herr Paolo Ofzareck.

| Predicted | Gold |
|---|---|
| `Paolo Ofzareck` | `Paolo Ofzareck` |

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_190`)


Abschließend wird darauf hingewiesen, dass seit Jänner 2013 in zahlreichen Telefonaten,  persönlichen Gesprächen sowie mehrfacher Korrespondenz mit Herrn Dücking und Frau B der  Umstand der Einbehaltung und Erstattung der Familienbeihilfe zur Kenntnis gebracht wurde.

| Predicted | Gold |
|---|---|
| `Dücking` | `Dücking` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_198`)


2. Im Haftungsbescheid und auch in der Beschwerdevorentscheidung ist Herr Erika Puttfarken, der  nunmehrige Beschwerdeführer, genannt.

| Predicted | Gold |
|---|---|
| `Erika Puttfarken` | `Erika Puttfarken` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/141761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141761.1_8`)


Sie haben bekannt gegeben, dass der Kindesvater Herr Pennings laufend in Deutschland lebt und  arbeitet.

| Predicted | Gold |
|---|---|
| `Pennings` | `Pennings` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/141761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141761.1_13`)


Meinen Kindern S. (geb.  am 2019) und A. (geb. am 2021) kommt ebenfalls der Status der Asylberechtigten zu. Der Vater  meiner Kinder,Herr Pennings  lebt in Deutschland, konkret in D, Thüringen.

| Predicted | Gold |
|---|---|
| `Pennings` | `Pennings` |

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_3`)


Begründung  Mit Bescheid des Finanzamtes Österreich vom 21.10.2021 wurde Herr Ilhan Drommelschmidt, geboren am  2. September 2011, gemäß § 26 Abs 1 Familienlastenausgleichsgesetz 1967 (nachfolgend „FLAG  1967“) in Verbindung mit § 33 Abs 3 EStG 1988 aufgefordert, die für ihn selbst bezogene  Familienbeihilfe sowie die Kinderabsetzbeträge für den Zeitraum Oktober 2018 bis März 2021  zurückzuzahlen.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Missed by this rule (FN):**

- `Finanzamtes Österreich` (organisation)
- `2. September 2011` (date)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_6`)


Am 19.11.2021 erhob Herr Ilhan Drommelschmidt  fristgerecht Beschwerde gegen den  Rückforderungsbescheid.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_8`)


Herr Ilhan Drommelschmidt  habe mit Oktober 2016 das Studium Lehramt mit den  Unterrichtsfächern Englisch und Psychologie begonnen.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_16`)


Ein  Familienbeihilfenanspruch bestehe erst dann (wieder), wenn Herr Ilhan Drommelschmidt  in dem nunmehr  gewählten Studium so viele Semester wie in den vor dem nunmehr gewählten Studium  zurückgelegt hat (§ 2 Abs 1 lit b FLAG 1967).

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_154`)


Ich habe dann mit dem Herrn Kollegen FT Kontakt aufgenommen und er hat mir gesagt, er  sucht auch Unterlagen und hat sie mir dann mitgegeben.

**False Positives:**

- `Kollegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_181`)


Der Herr Ing KB und ich sind langjährig befreundet.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing KB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing KB`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_43`)


Es lasse  sich nicht ableiten, wie Herr K. in den Genuss der „Vorteilszuwendung“ gekommen sei, da die  Rechnung durch die Unter Wilkel GmbH ausgestellt und der Betrag an diese überwiesen worden sei.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_67`)


Zudem waren die durch die Bf.  genannten Ansprechpersonen, ein Herr K. sowie die Gesellschafter-Geschäftsführerin GfIn für  die AP weder im In- noch im Ausland greifbar.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_68`)


Herr K. war weder im Jahr 2007, vor dem  Gesellschafterwechsel, noch im Jahr 2008 beim genannten Unternehmen angestellt oder  4 von 6 Seite 5 von 6

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_4`)


Laut Firmenbuchauszug ist Herr Jeskin Geschäftsführer seit 23.7.2009.

**False Positives:**

- `Jeskin Geschäftsführer` — partial — gold is substring of pred: `Jeskin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeskin`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_27`)


Dagegen wandte sich der Bf mit dem Rechtsmittel der Beschwerde und führte aus, dass er den  Zeugen Herrn P.R. gefragt hätte, ob er ein Gewerbe bei ihm anmelde.

**False Positives:**

- `P.R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_29`)


Er habe Herrn P.R. bezahlt, wenn er für ihn gearbeitet (Entsorgung der  Autos) habe.

**False Positives:**

- `P.R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_30`)


Nachdem Herr P.R. nicht mehr gekommen sei, habe ihm Herr M.F. geholfen, die  Autos zu entsorgen.

**False Positives:**

- `P.R.` — no gold match — likely missing annotation
- `M.F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_32`)


Nach der  Anzeige habe Herr F. den Standort bei ihm abgemeldet.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_23`)


Auf Grund einer Anfrage des Bundesfinanzgerichtes bei der für Meldeangelegenheiten  zuständigen Fachdienststelle in der Stadt Wien, der MA 62, teilte diese mit E-Mail vom  25.2.2021 folgendes mit:  „Zu Ihrer Anfrage teile ich Ihnen seitens der Magistratsabteilung 62 als zuständiger  Fachdienststelle für Meldeangelegenheiten in der Stadt Wien mit, dass Herr Lieselotte Rübenkönig, Bakk. rer. nat.  wie  von ihm angegeben von uns nach Durchführung eines Verfahrens nach § 15 Meldegesetz  amtlich von der Adresse xy abgemeldet wurde.

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_26`)


Der Erheber bekam vor Ort am  14. Jänner 2020 von einer Hauspartei, deren Identität wir nicht kennen, die Auskunft, dass Herr  Lieselotte Rübenkönig, Bakk. rer. nat.  unbekannt wohin verzogen sei.

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_27`)


Herr Lieselotte Rübenkönig, Bakk. rer. nat.  wurde von uns zweimal im  Verfahren angeschrieben, davon einmal mit RSb-Rückscheinbrief, und hat darauf nicht  reagiert.“

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_16`)


1) Höhe der 2014 in Österreich Steuerpflichtigen Bezüge aus nicht selbständiger Arbeit   Herr Bf. erzielte auch in 2014 Einkünfte aus nichtselbständiger Arbeit als angestellter  Staatsanwalt aus Dienstverhältnissen zu zwei Schweizer Körperschaften öffentlichen Rechtes  (Kanton Nidwalden und Bund).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_171`)


Wie den vorgelegten  Einkommensteuererklärungen und späteren Berufungen/Beschwerden entnommen werden  kann, sind Herrn Gerrit Einkünfte niemals unbesteuert geblieben: Österreich besteuert das  Welteinkommen, einerseits im Wege der Anrechnungsmethode, andererseits im Wege der  Befreiungsmethode.

**False Positives:**

- `Gerrit Einkünfte` — partial — gold is substring of pred: `Gerrit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerrit`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_101`)


vielmehr stand es im wirtschaftlichen  Eigentum des Herrn Hus  Es gehörte daher nicht zum  (notwendigen) Betriebsvermögen der Bf. und konnte – mangels Gewinnermittlung gemäß § 5  EStG – jedenfalls auch nicht zum gewillkürten Betriebsvermögen bestimmt werden.

**False Positives:**

- `Hus  Es` — partial — gold is substring of pred: `Hus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hus`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_16`)


Zuletzt  erging ein antragsloser ANV-Bescheid für 2019 an Herrn M.  Eine steuerliche Vertretung oder Zustellbevollmächtigung für Herrn M. ist in der  abgabenbehördlichen Datenbank bis heute nicht erfasst (Quellen: abgabenbehördliche  Datenbank DB2, Grundbuch, Firmenbuch).

**False Positives:**

- `M.  Eine` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `M.`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_92`)


Ein Vertreter konnte wirksam nur im Namen von Herrn M. Beschwerde erheben.

**False Positives:**

- `M. Beschwerde` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/134399.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134399.1_28`)


Mit E-Mail vom 26. April 2021 stellte der Beschwerdeführer einen Vorlageantrag und führte  aus, das Lokal in W., S-Straße, sei auch im Jahr 2020 an Herrn Mieter vermietet gewesen.

**False Positives:**

- `Mieter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/134399.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134399.1_35`)


Das sich im Gebäude befindliche Geschäftslokal war im Streitjahr an Herrn Mieter vermietet.

**False Positives:**

- `Mieter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_68`)


Nachdem Herr A. erst seit 23.5.2016 in Ort1 (Ö) wohnhaft ist, ist es ausgeschlossen, dass Frau  Priv.-Doz.in Laetitia Pöstges  seit 5-6 Jahren bei ihm in Ort1 (Ö) wohnhaft ist.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_70`)


Frau  Priv.-Doz.in Laetitia Pöstges  hat Herrn A. erst vor ca 4 - 5 Jahren kennengelernt.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_71`)


Nachdem sich diese  Freundschaft intensivierte, kam Herr A. zu Frau Priv.-Doz.in Laetitia Pöstges  nach Ort1 (CH).

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_73`)


Erst vor ca 3 Jahren besuchte Frau Priv.-Doz.in Laetitia Pöstges  Herrn A. erstmals in Ort1  (Ö).

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_77`)


Frau Priv.-Doz.in Laetitia Pöstges  ist weder Eigentümerin, Mieterin, Ehegattin oder  sonst irgendwie nachhaltig berechtigt, im Haus von Herrn A. zu übernachten oder es sonst wie  zu nutzen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_80`)


Herr A. ist Eigentümer einer Bau- und Konstruktionsschlosserei in der Ort1 (CH)-Adr2.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_83`)


Entweder schläft Frau  Priv.-Doz.in Laetitia Pöstges  bei Herrn A., oder Herr A. bei Frau Priv.-Doz.in Laetitia Pöstges  in der Schweiz.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)
- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_85`)


Als die Beziehung ein Level erreicht hat, bei dem es um die Planung einer gemeinsamen  Zukunft ging, haben Frau Priv.-Doz.in Laetitia Pöstges  und Herr A. beschlossen, einen Immobilienmakler zu  beauftragen um ein Haus in der Schweiz zu suchen, in das sie gemeinsam einziehen und einen  gemeinsamen Wohnsitz gründen wollten.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/137291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137291.1_18`)


Als Zeugen für diesen Sachverhalt gaben Sie  Herrn Zeuge, AdrZeuge an.

**False Positives:**

- `Zeuge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_28`)


Infolge sind von Herrn Leander Krupa Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

**False Positives:**

- `Leander Krupa Unterlagen` — partial — gold is substring of pred: `Leander Krupa`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leander Krupa`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_129`)


30 Auf dieser Grundlage meint das vorlegende Gericht, das im Ausgangsverfahren in Rede  stehende Kind und seine Mutter seien, was den Anspruch auf Familienleistungen betreffe, als  Familienangehörige von Herrn Trapkowski im Sinne des deutschen Rechts anzusehen.

**False Positives:**

- `Trapkowski` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_120`)


Die Inanspruchnahme von Herrn Wilhelm Fißenewert, LLM  als Zahlungsverpflichteten erfolgte, weil die als  Leistungsgerbringerin fungierende Hemken Automotive GmbH in Liqu. ihrer Zahlungsverpflichtung nicht  nachgekommen ist.

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilhelm Fißenewert, LLM`(person)
- `Hemken Automotive GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_133`)


Der Bf brachte im Wege der XY WTH GmbH, fristgerecht „Beschwerde gegen den  Bescheid – Leistungsgebot“ vom 5.Nov.2021 ein und begehrte mit folgender Begründung die  Aufhebung der bekämpften Erledigung:  „Als Begründung ist anzuführen, dass Herr Wilhelm Fißenewert, LLM  kein Gesamtschuldner aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der Hemken Automotive GmbH nicht um Bauleistungen handelt.  Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  Zur Korrektur des Irrtums wurden die Rechnungen berichtigt, neu ausgestellt mit  Umsatzsteuerausweis von 20 % und bezahlt gemäß dem Prüfungsergebnis.

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XY WTH GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)
- `Hemken Automotive GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_138`)


Die von der Firma Hemken Automotive GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Wilhelm Fißenewert, LLM  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.“  (Zitatende/Beschwerde)  10.

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hemken Automotive GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_13`)


Da die Treuhandvereinbarung somit jederzeit sowohl vom  Treugeber, als auch vom Treuhänder kurzfristig gekündigt werden kann, verbleibt … auch das  wirtschaftliche Eigentum - beim zivilrechtlichen Eigentümer, Herrn Dr. M P (vgl. VwGH  13.09.2018, Ra 2018/15/0055).“

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `title_only_person` 🏆

**F1:** 0.168 | **Precision:** 0.381 | **Recall:** 0.107  

**Format:** `regex`  
**Rule ID:** `0ddd9a21`  
**Description:**
Captures person names immediately following a title (e.g., 'Dr. Hans', 'Mag. Dr. Wolfgang', 'VetR Hon.-Prof.in Leya'). Handles compound titles and academic suffixes. FIXED to capture the full name including suffixes.

**Content:**
```
(?<!\w)(?:RA\s+|Hon\.-?Prof\.|Univ\.-?Prof\.|Univ\.-?Prof\.in|Prof\.|Dr\.|Dr\.in|Mag\.|Mag\.a|Mag\.Mag\.|Dr\.Mag\.|MMag\.|DI\.|Ing\.|Ing\.KomzlR\.|Bakk\.\s+iur\.|PhD\.|HR\s+Ing\.|Techn\s+R|TechnR|Dipl\.-?HTL\-?Ing\.|PD\s+Dr\.|Priv\.-?Doz\.|Priv\.-?Doz\.in|DDr\.|KommR\s+|\u00d6kR\s+|RgR\s+|StR\s+|MedR\s+|HR\s+|KzlR\s+|OMedR\s+|VetR\s+|AR\s+|Vizepr\u00e4sident\s+|Senatspr\u00e4sident\s+|Hofrat\s+|Hofr\u00e4tin\s+|Hofr\u00e4ts\s+|Vizepr\u00e4sidentin\s+|Senatspr\u00e4sidentin\s+|Dr\.in|Mag\.a|Mag\.Dr\.|Dr\.Mag\.|Dipl\.\s+|Univ\.-?Prof\.\s+Dipl\.-?Ing\.\s+Dr\.|Priv\.-?Doz\.\s+|Prof\.in\s+Techn\s+R|OStR|OStRin|Priv\.-?Doz\.in\s+Mag\.a|Priv\.-?Doz\.in|OStR(?:\s+Ing\.)?|OStRin|KzlR|StR|MedR|KommR|\u00d6kR|VetR|Vizepr\u00e4sident|Senatspr\u00e4sident|Hofrat|Hofr\u00e4tin|Hofr\u00e4ts|Vizepr\u00e4sidentin|Senatspr\u00e4sidentin|Prof\.in\s+Techn\s+R|Univ\.-?Prof\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s*,\s*(?:LL\.B\.|LL\.M\.|M\.Sc|M\.B\.L\.|MBA|PhD|Dr\.|Mag\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.381 | 0.107 | 0.168 | 674 | 257 | 417 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 257 | 417 | 2134 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Viktoria Kreiselmayer` | `Univ.-Prof.in Viktoria Kreiselmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Muran Waldhans, BEd` (person)
- `Am Tegel 5, 9831 Waben, Österreich` (address)
- `Corazza Kocholl Laimer Rechtsanwälte OG` (organisation)
- `Finanzamtes Innsbruck` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Niels Aleksejew` | `Univ.-Prof. Niels Aleksejew` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Kuzu` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Dr.  Karl Penninger` | `Dr.  Karl Penninger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Mag. Susanne Haim` (person)
- `Leopold Pichlbauer` (person)
- `Ing. Dipl.-Ing. Brunhild Fleischfresser` (person)
- `Margaretengürtel 23, 4092 Pyrawang, Österreich` (address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH` (organisation)
- `Finanzamtes` (organisation)
- `Tanja Grottenthaler` (person)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Miroslav Treischl, Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Thomas Leitner` | `Mag.Dr. Thomas Leitner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miroslav Treischl` (person)
- `Pfarrerboden-Siedlung 10, 2753 Ober-Piesting, Österreich` (address)
- `Grant Thornton Austria GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marianne Liuni` | `Univ.-Prof.in Marianne Liuni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Luigi Wedekämper` (person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Sellnow` | `Priv.-Doz. Eckard Sellnow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Rösl` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_2`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Dr.in Ljiljana Kos` (person)
- `Ljiljana Kos` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Ljiljana Kos` (person)
- `Dr. Schmid` (person)
- `Klinik Favoriten` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Dr.in Lydia Vogtleitner` (person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Esra Rohleder` | `Mag. Esra Rohleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Stephan Neiser` (person)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_199`)


Der Bf führte in seinem Schussantrag aus, dass er die ImmoESt gar nicht schulde, sondern hätte  diese vielmehr sein vormaliger steuerlicher Vertreter, StB Techn R Melinda Kälbli  zu tragen.

| Predicted | Gold |
|---|---|
| `Techn R Melinda Kälbli` | `Techn R Melinda Kälbli` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_349`)


Mit der Vertragserrichtung beauftragt wurde Rechtsanwalt StR Lukas Vielmäder, MBA Dieser gilt als  Parteienvertreter iSd § 30c Abs. 3 EStG 1988, welcher unter den genannten Voraussetzungen  für die richtige Berechnung der strittigen Steuer haftet.

| Predicted | Gold |
|---|---|
| `StR Lukas Vielmäder, MBA` | `StR Lukas Vielmäder, MBA` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_350`)


Eine Haftung des ehemaligen  steuerlichen Vertreters des Bf, StB Techn R Melinda Kälbli  auf Grundlage der Bestimmung des § 30c Abs. 3 leg.  cit.

| Predicted | Gold |
|---|---|
| `Techn R Melinda Kälbli` | `Techn R Melinda Kälbli` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

| Predicted | Gold |
|---|---|
| `Mag. Artner` | `Mag. Artner` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr. Padesse` | `Dr. Padesse` |
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_2`)


Begründung  Der Beschwerdeführer Priv.-Doz.in Elena Kaminskiy  hat mit Eingabe vom 22.10.2020, eingelangt am 27.10.2020,  gemäß § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht  über die Beschwerde gegen den Einkommensteuerbescheid für 2019 erhoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Elena Kaminskiy` | `Priv.-Doz.in Elena Kaminskiy` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Nicola Folprecht` | `Univ.-Prof.in Nicola Folprecht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florian Abbruzzese, BA` (person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lubomir Gruebert` | `Priv.-Doz. Lubomir Gruebert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexander Powell` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Hüpgen   in der Beschwerdesache des Alois Jeckl, Amlach 6, 2620 Straßhof, Österreich,   betreffend die Bescheide des Finanzamt Waldviertel  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 66-092/6335,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jeannine Hüpgen` | `Priv.-Doz.in Jeannine Hüpgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alois Jeckl` (person)
- `Amlach 6, 2620 Straßhof, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `66-092/6335` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Melina Wellenbrock  in der Verwaltungsstrafsache  Gabriele Vogrin, Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich, 1.) über die Beschwerde vom 19.06.2020 gegen die Strafverfügung  des Magistrats der Stadt Wien vom 30.12.2019, zugestellt am 27.02.2020, Geschäftszahl  MA67/196701166656/2019, und 2.) über die Beschwerde vom 19.06.2020 gegen die Strafver- fügung des Magistrats der Stadt Wien vom 20.01.2020, zugestellt am 03.03.2020, Geschäfts- zahl MA67/196701283117/2019, beschlossen:    Die Beschwerden werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Melina Wellenbrock` | `Univ.-Prof.in Melina Wellenbrock` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gabriele Vogrin` (person)
- `Otto-Wilhartitz-Straße 6, 9816 Oberkolbnitz, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt Wien` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ronald Töws` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

| Predicted | Gold |
|---|---|
| `Dr. Karl Renner` | `Dr. Karl Renner` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/131065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131065.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Kirstin Detlef  in der Beschwerdesache  Pawel Wnent, Reinbergweg 21, 9112 Wölfnitz, Österreich, vertreten durch X-Steuerberatung über die Beschwerde vom  19. Februar 2016 gegen den Bescheid des FA Oststeiermark  vom 15. Jänner 2016 betreffend  Feststellung der Einkünfte § 188 BAO 2012 zur Steuernummer 999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Kirstin Detlef` | `Mag.a Kirstin Detlef` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Pawel Wnent` (person)
- `Reinbergweg 21, 9112 Wölfnitz, Österreich` (address)
- `X-Steuerberatung` (organisation)
- `FA Oststeiermark` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/131567.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Valerius Wilbert  in der Finanzstrafsache gegen die  Beschuldigte Chen Kürkcü, An der Museumsbahn 11, 3122 Bichl, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Valerius Wilbert` | `Hon.-Prof. Valerius Wilbert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chen Kürkcü` (person)
- `An der Museumsbahn 11, 3122 Bichl, Österreich` (address)
- `Mag. Heinz Wolfbauer` (person)
- `Finanzamtes  Wien 9/18/19 Klosterneuburg` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Fridolin Härlin  in der Beschwerdesache Alva Czymzik,  Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Fridolin Härlin` | `Priv.-Doz. Fridolin Härlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alva Czymzik` (person)
- `Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132289.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Camilla Gembalies  in der Beschwerdesache der  Ost Verdon Systeme, Asangstraße 9c, 9580 Mittewald, Österreich, vertreten durch Apfelbaum & Senkfeil Software GmbH betreffend Beschwerde  vom 22. April 2016 gegen die als Bescheid des Finanzamtes X vom 27. Jänner 2016 intendierte  Erledigung betreffend Festsetzung der Kraftfahrzeugsteuer 01.2014-12.2014 zur StNr 99- 99/9999 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Camilla Gembalies` | `Univ.-Prof.in Camilla Gembalies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Ost Verdon Systeme` (organisation)
- `Asangstraße 9c, 9580 Mittewald, Österreich` (address)
- `Apfelbaum & Senkfeil Software GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Merlin Thorschmidt` | `Univ.-Prof. Merlin Thorschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adrian Radakovitsch` (person)
- `Schlatterbergweg 97, 9344 Psein, Österreich` (address)
- `Finanzamt Steiermark Mitte` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/132557.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karen Billhard  in der Beschwerdesache der  KEX Solar Entwicklung, Deniflestraße 24, 3032 Rekawinkel, Österreich, vertreten durch Ort, über die Beschwerde vom 6.9.2017 gegen die  Bescheide des Finanzamtes Innsbruck vom 2. August 2017 betreffend Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 und Festsetzung der  Kraftfahrzeugsteuer für die Zeiträume Juli bis Dezember 2014 und Jänner bis Juni 2015 zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung der  Normverbrauchsabgabe für den Zeitraum September 2014 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Karen Billhard` | `Univ.-Prof.in Karen Billhard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KEX Solar Entwicklung` (organisation)
- `Deniflestraße 24, 3032 Rekawinkel, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Erika Matuszcyk  in der Beschwerdesache Hon.-Prof. Hugo Beerbaum,  Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich, über die Beschwerde vom 27.1.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 16.1.2020, SV-Nr, betreffend die Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Jänner 2020 zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Erika Matuszcyk` | `Univ.-Prof.in Erika Matuszcyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Hugo Beerbaum` (person)
- `Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich` (address)
- `Finanzamtes  Innsbruck` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Hon.-Prof. Hugo Beerbaum (= Beschwerdeführerin, Bf), geb. Juni 1998, hatte mit Formular Beih100 im  September 2019 für sich die Zuerkennung der Familienbeihilfe (FB) wegen "Ausbildung" bzw.  "Lehre" mit einer voraussichtlichen Dauer bis 28.1.2022 beantragt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Hugo Beerbaum` | `Hon.-Prof. Hugo Beerbaum` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/132646.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Urs Zumbroich  in der Beschwerdesache Techn R Huberta Witte,  Ebenweg 188, 4081 Mußbach, Österreich, über die Beschwerde vom 8. Juni 2016 gegen den Bescheid des Finanzamtes  Lilienfeld St. Pölten (jetzt Finanzamt Österreich) vom 13. Mai 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Urs Zumbroich` | `Priv.-Doz. Urs Zumbroich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Huberta Witte` (person)
- `Ebenweg 188, 4081 Mußbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Univ.-Prof.in Rachel Darnieder, ` — partial — gold is substring of pred: `Univ.-Prof.in Rachel Darnieder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hemma Bährs`(person)
- `Univ.-Prof.in Rachel Darnieder`(person)
- `Finanzamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128730.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

**False Positives:**

- `Dr. Gerlinde  Rieser, ` — partial — gold is substring of pred: `Dr. Gerlinde  Rieser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Matthäus Domrös`(person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Dr. Gerlinde  Rieser`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Achmed Ghazal Aswad, ` — partial — gold is substring of pred: `Mag. Achmed Ghazal Aswad`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alois Pichler`(person)
- `Donald Paulovits`(person)
- `Tröbach 41, 9130 Leibsdorf, Österreich`(address)
- `Mag. Achmed Ghazal Aswad`(person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `95-720/4312`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `KzlR Adalbert Bürks, ` — partial — gold is substring of pred: `KzlR Adalbert Bürks`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Aigner`(person)
- `KzlR Adalbert Bürks`(person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache MedR Irvin Leider, 10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich, über die Beschwerde vom 22. September 2017 gegen den Bescheid des FA vom  21. August 2017 betreffend Einkommensteuer 2016 Steuernummer 30-411/2742  zu Recht  erkannt:   1.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `MedR Irvin Leider, ` — partial — gold is substring of pred: `MedR Irvin Leider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MedR Irvin Leider`(person)
- `10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich`(address)
- `30-411/2742`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Univ.-Prof. Janis Abelen,  Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

**False Positives:**

- `Univ.-Prof. Janis Abelen,  ` — partial — gold is substring of pred: `Univ.-Prof. Janis Abelen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Janis Abelen`(person)
- `Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Mag.a Reneé Kobayashi, Weinbaugebiet Losling 9, 4880 Aich, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `Mag.a Reneé Kobayashi, ` — partial — gold is substring of pred: `Mag.a Reneé Kobayashi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Elisabeth Traxler`(person)
- `Mag.a Reneé Kobayashi`(person)
- `Weinbaugebiet Losling 9, 4880 Aich, Österreich`(address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Mag. Marco Laudacher, ` — partial — gold is substring of pred: `Mag. Marco Laudacher`
- `Ing. Dipl` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`
- `Ing. Brunhild Fleischfresser, ` — positional overlap with gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `ÖkR Horst Stevens, ` — positional overlap with gold: `Ing. ÖkR Horst Stevens`
- `Mag. Manfred Frühwirth, ` — partial — pred is substring of gold: `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Mehmet Faidt, Flitsch 4, 4822 Kogl, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Wolfgang Freudelsperger, ` — partial — gold is substring of pred: `Mag. Wolfgang Freudelsperger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Mehmet Faidt`(person)
- `Flitsch 4, 4822 Kogl, Österreich`(address)
- `Mag. Wolfgang Freudelsperger`(person)
- `Finanzamtes Wien 1/23`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hon.-Prof. Gerhard Hübinger, Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich, St.Nr. xxxxxxxxxxxx, über die Beschwerden vom 2. April 2013 gegen den  Aufhebungsbescheid gemäß § 299 BAO vom 4. März 2013 und den Zurückweisungsbescheid  vom 4. März 2013 (betreffend Antrag auf Bescheidaufhebung gemäß § 295 Abs. 4 BAO, in  eventu Antrag auf Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 lit. b BAO) des  Finanzamtes Wien 9/18/19 Klosterneuburg, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon.-Prof. Gerhard Hübinger, ` — partial — gold is substring of pred: `Hon.-Prof. Gerhard Hübinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Gerhard Hübinger`(person)
- `Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Mag. Hermann Rupert Zittmayr, ` — partial — gold is substring of pred: `Mag. Hermann Rupert Zittmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Astrid Rüstmann`(person)
- `Sandro Flunger`(person)
- `Rohrer Straße 29, 3231 Kainratsdorf, Österreich`(address)
- `Mag. Hermann Rupert Zittmayr`(person)
- `FA Klagenfurt St. Veit Wolfsberg`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Irvin Kurrek  in der Beschwerdesache Alexandra Kesler,  Illyrerweg 5, 4073 Edramsberg, Österreich, (nunmehr Valsyn-Maschinenbau GmbH als Rechtsnachfolgerin der Schameitat Sanitär GmbH, vertreten durch StB,  über die Berufung (nunmehr Beschwerde) vom 21. August 2013 gegen die Bescheide des FA  vom 9. Juli 2013 betreffend Wiederaufnahme der Verfahren hinsichtlich der  Körperschaftsteuer für die Jahre 2009 und 2010 sowie die Körperschaftsteuer für die Jahre  2009 bis 2011 beschlossen:    I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) als nicht  zulässig zurückgewiesen.

**False Positives:**

- `Priv.-Doz. Priv` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Irvin Kurrek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Priv.-Doz. Irvin Kurrek`(person)
- `Alexandra Kesler`(person)
- `Illyrerweg 5, 4073 Edramsberg, Österreich`(address)
- `Valsyn-Maschinenbau GmbH`(organisation)
- `Schameitat Sanitär GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `Dr. Andreas Weißenbäck` — partial — pred is substring of gold: `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache KommR Eckard Gaiss, Bakk. phil., Hietzinger Kai 33, 4132 Lug, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 07-088/5911  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `KommR Eckard Gaiss, ` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Hietzinger Kai 33, 4132 Lug, Österreich`(address)
- `Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `07-088/5911`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_3`)


Entscheidungsgründe  Mit Bescheiden des Finanzamtes Wien 1/23 jeweils vom 9. August 2019 wurden über die  KommR Eckard Gaiss, Bakk. phil. (in weiterer Folge: Bf.) erste Säumniszuschläge für Umsatzsteuer 05/2019 in Höhe  von € 209.028,38 (Säumniszuschlag € 4.180,57), für Werbeabgabe 05/2019 in Höhe von €  177.156,96 (Säumniszuschlag € 3.543,14), für Lohnsteuer 06/2019 in Höhe von € 85.47466  (Säumniszuschlag € 1.709,49) und für Dienstgeberbeitrag 06/2019 in Höhe von € 20.536,18  (Säumniszuschlag € 410,72), Säumniszuschläge gesamt € 9.843,92, festgesetzt, da die  angeführten Abgabenschuldigkeiten nicht innerhalb der Frist 15. Juli 2019 entrichtet worden  sind.

**False Positives:**

- `KommR Eckard Gaiss, ` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 1/23`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_15`)


Am 15. Juli 2019 hat unsere Mandantschaft via Finanz Online einen Antrag auf Übertragung an  die KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10)  iHv EUR 336.224,91 eingebracht (Hinweis: Betreffend die Martinssen Versicherung GmbH wurde ebenfalls ein  Säumniszuschlag festgesetzt und ist eine Beschwerdevorentscheidung ergangen;

**False Positives:**

- `KommR Eckard Gaiss, ` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_31`)


Als Beilage dürfen wir Ihnen nachfolgende Unterlagen übermitteln:   XML-Datenträger UVA 05/2019 betreffend die Gerstbreu Umwelt GmbH  Fax an das Finanzamt 13.08.2019 inkl. UVA 05/2019 und Produktionsübermittlung  vom 12.Juli 2019 betreffend die Gerstbreu Umwelt GmbH inkl. Antrag betreffend die Übertragung  eines Geldbetrages für die KommR Eckard Gaiss, Bakk. phil.  und für die Martinssen Versicherung GmbH vom 15. Juli 2019 inkl.  Übermittlung der Rechnungen mit den größeren Vorsteuerbeträgen inkl.  Faxbestätigung vom 13. August 2019  Weiters stellen wir den Antrag den Säumniszuschlag in Höhe von EUR 9.843,92 herabzusetzen  bzw. nicht festzusetzen, da unserer Mandantschaft aus oben angeführten Gründen an der  Versäumnis kein grobes Verschulden trifft.

**False Positives:**

- `KommR Eckard Gaiss, ` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `Finanzamt`(organisation)
- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Martinssen Versicherung GmbH`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


Der steuerliche Vertreter hat weiter ausgeführt, dass am 15. Juli 2019 unsere Mandantschaft  (aus dem Zusammenhang ist davon auszugehen, dass es sich bei der Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH handelt) via FinanzOnline einen Antrag auf Übertragung an die  KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10) iHv  EUR 336.224,91 eingebracht hat (Hinweis: Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH ebenfalls ein Säumniszuschlag festgesetzt worden sein und sei eine  Beschwerdevorentscheidung ergangen, wogegen ein Vorlageantrag und Antrag gem. § 217 (7)  BAO eingebracht worden sei).

**False Positives:**

- `KommR Eckard Gaiss, ` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `Dr.in Monika Wörther` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Monika Wörther-Madl`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dr.in Monika Wörther` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. August Eichelsbacher  in der Beschwerdesache VetR Diethard Oldenbüttel,  Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich, vertreten durch BOD Steuerberatungs-GmbH, Europastraße 5, 6322  Kirchbichl,, über die Beschwerde vom 16. Dezember 2016 gegen den Bescheid des FA Landeck Reutte  vom 21. November 2016 betreffendBerichtigung des Einkommensteuerbescheides 2010 vom  29. November 2011 gem. § 293b BAO erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `VetR Diethard Oldenbüttel,  ` — partial — gold is substring of pred: `VetR Diethard Oldenbüttel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. August Eichelsbacher`(person)
- `VetR Diethard Oldenbüttel`(person)
- `Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich`(address)
- `BOD Steuerberatungs-GmbH`(organisation)
- `FA Landeck Reutte`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

**False Positives:**

- `Dr.in Ljiljana Kos, ` — partial — gold is substring of pred: `Dr.in Ljiljana Kos`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Dr.in Ljiljana Kos`(person)
- `Dr. Alexander Nahler`(person)
- `Ljiljana Kos`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

**False Positives:**

- `Dr. Schmid,  ` — partial — gold is substring of pred: `Dr. Schmid`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Dr. Alexander Nahler`(person)
- `Ljiljana Kos`(person)
- `Dr. Schmid`(person)
- `Klinik Favoriten`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

**False Positives:**

- `Univ.Prof. Dr` — positional overlap with gold: `Dr. Sasan Hamzavi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sasan Hamzavi`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `StR Dr` — partial — pred is substring of gold: `StR Dr.in Lydia Vogtleitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `StR Dr.in Lydia Vogtleitner`(person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich`(address)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gerald Hellbing`(person)
- `Unterretzbach 125, 5092 Kirchental, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_17`)


Darüber hinaus werden die dem Erwachsenenvertreter vorliegenden psychiatrischen  Gutachten vorgelegt, aus diesen ist ersichtlich, dass bei (der Bf.) eine angeborene Oligophrenie  vorliegt (Psychiatrisches Gutachten Univ.Prof. Dr.med. F. St. vom 28.04.1987), ebenso wie die  Sachverständige Charles Hegler von einer angeborenen Minderbegabung ausgeht, mit später  aufgetretenen psychotischen und schizophrenen Symptomen.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Charles Hegler`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_19`)


Beweis: beiliegendes Gutachten Univ.Prof. Dr.med.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_20`)


F. St. vom 28.04.1987,                  beiliegendes Gutachten Univ.Prof. Dr.med.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_26`)


Sie könne nicht  aufstehen, bewegt aber seitengleich (diesbezüglich liegen keine Befunde vor)   Derzeitige Beschwerden:   diverse Schmerzen, sie könne nicht gehen   Behandlung(en) / Medikamente / Hilfsmittel:   kann keine Angaben machen   Sozialanamnese:   lebt in Caritasheim vollbetreut, I(nvaliditäts)Pension, Pflegestufe 4, Erwachsenenvertretung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   28.4.87 Dipl.-Ing. Kirsten Hüffner: Es handelt sich bei (der Bf.) um eine Oligophrenie.

**False Positives:**

- `Ing. Kirsten Hüffner` — partial — pred is substring of gold: `Dipl.-Ing. Kirsten Hüffner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_73`)


Wie aus dem vorgelegten Gutachten von Prof. Dr.med.

**False Positives:**

- `Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_77`)


Wie aus dem Gutachten Prof. Univ.Doz. Dr.med Dipl.-Ing. Kirsten Hüffner  vom 28.04.1987, Seite 6, ersichtlich,  sind schizophreniforme Psychosen bei Oligophrenie sehr schwer und oft gar nicht deutbar.

**False Positives:**

- `Prof. Univ` — no gold match — likely missing annotation
- `Ing. Kirsten Hüffner` — partial — pred is substring of gold: `Dipl.-Ing. Kirsten Hüffner`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_114`)


2. Beweiswürdigung  Diese Feststellungen beruhen auf dem Akteninhalt, insb. auf dem Inhalt der Gutachten  (Univ.Prof. Dr.med. F. St.), und sind unstrittig.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Stephan Neiser, ` — partial — gold is substring of pred: `Dr. Stephan Neiser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Stephan Neiser`(person)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich`(address)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `Mag. Esra Rohleder`(person)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Amtsvertr, ` — partial — gold is substring of pred: `Dr. Amtsvertr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Claudia Noeltge`(person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)
- `Dr. Amtsvertr`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Hademar Berking, Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Margot Artner,  ` — partial — gold is substring of pred: `Mag. Margot Artner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Hademar Berking`(person)
- `Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich`(address)
- `Mag. Margot Artner`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Mag. Artner` — partial — pred is substring of gold: `Mag. Artner-Tauscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Artner-Tauscher`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Priv.-Doz.in Elena Kaminskiy,  ` — partial — gold is substring of pred: `Priv.-Doz.in Elena Kaminskiy`
- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Radics`

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

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über den Antrag  der Antonia Piekorz, LLB Bakk. phil., Aubrunnerweg 10d, 9150 Rinkenberg, Österreich  vom 23. März 2020 auf Gewährung der Verfahrenshilfe für das  Beschwerdeverfahren gegen den Bescheid der belangten Behörde Finanzamt Bruck Eisenstadt  Oberwart vom 28. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 beschlossen:  Der Antragstellerin wird gemäß § 292 BAO Verfahrenshilfe bewilligt.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Antonia Piekorz, LLB Bakk. phil.`(person)
- `Aubrunnerweg 10d, 9150 Rinkenberg, Österreich`(address)
- `Finanzamt Bruck Eisenstadt  Oberwart`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Ing. Erwin Göktan, ` — positional overlap with gold: `Dipl.-Ing. Erwin Göktan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Irene Kohler`(person)
- `Dipl.-Ing. Erwin Göktan`(person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Rupert Karl, ` — partial — gold is substring of pred: `Mag. Rupert Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gudrun Sochurek`(person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich`(address)
- `Mag. Rupert Karl`(person)
- `Finanzamtes`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hon` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`
- `Prof. Dragan Höh` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`
- `ÖkR Mag` — partial — pred is substring of gold: `ÖkR Mag.a Catharina Schmalenstrot`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) veräußerte mit Kaufvertrag vom 06.07.2016 seinen Hälfteanteil am  Grundstück Nr. x/17 in C., Katastralgemeinde a, an seine Geschwister Edeltraud Gonszerowski und Univ.-Prof.in Techn R Nicoletta Constin um  einen Kaufpreis in Höhe von 140.100,00 Euro.

**False Positives:**

- `Univ.-Prof.in Techn` — partial — pred is substring of gold: `Univ.-Prof.in Techn R Nicoletta Constin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edeltraud Gonszerowski`(person)
- `Univ.-Prof.in Techn R Nicoletta Constin`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_44`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Für die Beurteilung der in Streit stehenden Frage geht das Bundesfinanzgericht von folgendem  entscheidungsrelevantem Sachverhalt aus:  Der Bf. veräußerte mit Kaufvertrag vom 06.07.2016 seinen Hälfteanteil am Grundstück Nr. x/17  in C., Katastralgemeinde a, an seine Geschwister Edeltraud Gonszerowski und Univ.-Prof.in Techn R Nicoletta Constin um einen Kaufpreis in Höhe  von 140.100,00 Euro.

**False Positives:**

- `Univ.-Prof.in Techn` — partial — pred is substring of gold: `Univ.-Prof.in Techn R Nicoletta Constin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Edeltraud Gonszerowski`(person)
- `Univ.-Prof.in Techn R Nicoletta Constin`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Jonathan Hewett, Bakk. techn., Kleinbodenerstraße 17, 4880 Rixing, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Mag. Anton Heisinger Wirtschaftstreuhänder, ` — partial — gold is substring of pred: `Mag. Anton Heisinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jonathan Hewett, Bakk. techn.`(person)
- `Kleinbodenerstraße 17, 4880 Rixing, Österreich`(address)
- `Mag. Anton Heisinger`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Dr. Viktor Frankl` — partial — pred is substring of gold: `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Priv.-Doz.in Nadine Schoormans,  Herderpark 21, 8444 Sankt Andrä im Sausal, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des Finanzamtes XY  vom 10.2.2020 betreffend Festsetzung einer Zwangsstrafe zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Nadine Schoormans,  ` — partial — gold is substring of pred: `Priv.-Doz.in Nadine Schoormans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Nadine Schoormans`(person)
- `Herderpark 21, 8444 Sankt Andrä im Sausal, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Waldemar Zumloh, ` — positional overlap with gold: `Dipl.-Ing. Waldemar Zumloh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Michael Mandlmayr`(person)
- `Dipl.-Ing. Waldemar Zumloh`(person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `09-591/1655`(tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Ruprecht Kalmes, Freistabl 34, 9400 Gries, Österreich, über die Beschwerde vom 5. Februar 2020 gegen die  Bescheide des Finanzamtes Lilienfeld St. Pölten vom 4. November 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, Steuernummer  03-702/3005, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `KzlR Ruprecht Kalmes, ` — partial — gold is substring of pred: `KzlR Ruprecht Kalmes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `KzlR Ruprecht Kalmes`(person)
- `Freistabl 34, 9400 Gries, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `03-702/3005`(tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131567.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Valerius Wilbert  in der Finanzstrafsache gegen die  Beschuldigte Chen Kürkcü, An der Museumsbahn 11, 3122 Bichl, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

**False Positives:**

- `Mag. Heinz Wolfbauer,  ` — partial — gold is substring of pred: `Mag. Heinz Wolfbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Valerius Wilbert`(person)
- `Chen Kürkcü`(person)
- `An der Museumsbahn 11, 3122 Bichl, Österreich`(address)
- `Mag. Heinz Wolfbauer`(person)
- `Finanzamtes  Wien 9/18/19 Klosterneuburg`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_92`)


Davon kann im gegenständlichen Fall hinsichtlich des  beschwerdegegenständlichen Jahres 2018 keine Rede sein:   Die Bf. hat zwar einen Schriftsatz (Arztbrief) vorgelegt, in dem der Arzt Dr. Martin Köppl  regelmäßige Rehabilitationsbehandlungen zum Erhalt der Selbständigkeit empfiehlt. Diese  Bestätigung des Hausarztes stammt vom 10.9.2018 und wurde also nachträglich ausgestellt.   Diese vermag jedoch aus o.a. Gründen mangels vorfeldweiser Verordnung keine  7 von 9 Seite 8 von 9

**False Positives:**

- `Dr. Martin Köppl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Ing. Techn` — partial — pred is substring of gold: `Ing. Techn R Arthur Kornhass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Alice Rainprechter`(person)
- `Ing. Techn R Arthur Kornhass`(person)
- `Gstaudet 21, 9556 Besendorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Dr` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Sophie Nauman`
- `Prof. Helmut Fürnkäß,  ` — partial — gold is substring of pred: `Prof. Helmut Fürnkäß`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman`(person)
- `Prof. Helmut Fürnkäß`(person)
- `Dr Christian Leskoschek`(person)
- `Finanzamtes Österreich`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Univ.-Prof.in StR Caroline Akkoca, MBA, Hinterbachstraße 8, 4653 Spieldorf, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2021 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Jänner 2021, Zahl: MA67/206700566984/2020, mit  dem der Einspruch vom 10. November 2020 gegen die Strafverfügung vom 8. Oktober 2020 mit  derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Univ.-Prof.in St` — partial — pred is substring of gold: `Univ.-Prof.in StR Caroline Akkoca, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)
- `Hinterbachstraße 8, 4653 Spieldorf, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. Oktober  2020, Zahl: MA67/206700566984/2020, wurde Herr Univ.-Prof.in StR Caroline Akkoca, MBA (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Univ.-Prof.in St` — partial — pred is substring of gold: `Univ.-Prof.in StR Caroline Akkoca, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Erika Matuszcyk  in der Beschwerdesache Hon.-Prof. Hugo Beerbaum,  Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich, über die Beschwerde vom 27.1.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 16.1.2020, SV-Nr, betreffend die Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Jänner 2020 zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Hugo Beerbaum,  ` — partial — gold is substring of pred: `Hon.-Prof. Hugo Beerbaum`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Erika Matuszcyk`(person)
- `Hon.-Prof. Hugo Beerbaum`(person)
- `Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich`(address)
- `Finanzamtes  Innsbruck`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/132646.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Urs Zumbroich  in der Beschwerdesache Techn R Huberta Witte,  Ebenweg 188, 4081 Mußbach, Österreich, über die Beschwerde vom 8. Juni 2016 gegen den Bescheid des Finanzamtes  Lilienfeld St. Pölten (jetzt Finanzamt Österreich) vom 13. Mai 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn R Huberta Witte,  ` — partial — gold is substring of pred: `Techn R Huberta Witte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Urs Zumbroich`(person)
- `Techn R Huberta Witte`(person)
- `Ebenweg 188, 4081 Mußbach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/132731.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132731.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat über die Beschwerde vom  11. September 2020 des Beschwerdeführers Leila Höflein, Äussere Vorachstraße 25, 4081 Deinham, Österreich, vertreten durch die  Dr. Heinz Häupl Rechtsanwalts GmbH, 4865 Nußdorf, Stockwinkl 18, gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 10. August 2020  betreffend Abweisung des Antrages vom 24.07.2020 auf Aufhebung der  Umsatzsteuerbescheide 2011 und 2013 sowie der Einkommensteuerbescheide 2010, 2011  und 2013 gemäß § 299 Abs 1 BAO den Beschluss:      I)

**False Positives:**

- `Dr. Heinz Häupl Rechtsanwalts Gmb` — partial — pred is substring of gold: `Dr. Heinz Häupl Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Leila Höflein`(person)
- `Äussere Vorachstraße 25, 4081 Deinham, Österreich`(address)
- `Dr. Heinz Häupl Rechtsanwalts GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rocco Girstenbrei, Waubergweg 6, 9710 Pöllan, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Maria Brandstetter,  ` — partial — gold is substring of pred: `Dr. Maria Brandstetter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Rocco Girstenbrei`(person)
- `Waubergweg 6, 9710 Pöllan, Österreich`(address)
- `Dr. Maria Brandstetter`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Eduard Schulden, Bakk. rer. nat., Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich, vertreten durch Dkfm. Freund & Partner Steuerberater GmbH, Schellinggasse 3, 1010  Wien, über die Beschwerde vom 29. Juli 2016 (Eingangsstempel 1. August 2016 ) gegen den  Umsatzsteuerbescheid 2011 und den Bescheid über die Feststellung von Einkünften gemäß  § 188 BAO 2011 des Finanzamtes Baden Mödling vom 5. Juli 2016, Steuernummer  16 28-951/9095, zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hans Klöpfer` — partial — pred is substring of gold: `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Eduard Schulden, Bakk. rer. nat.`(person)
- `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich`(address)
- `Freund & Partner Steuerberater GmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `28-951/9095`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_63`)


NachnameGeser1 und dessen Steuerberater Mag. Stb bekannte Hr.  NachnameGeser1 zunächst, dass die [Bf.] über keinen Autoabstellplatz verfüge.

**False Positives:**

- `Mag. Stb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_74`)


Auch in der Schlussbesprechung vom 24.05.2016  wurde von Hrn. NachnameGeser1 in Anwesenheit seines Steuerberaters, Mag. Stb, behauptet,  er hätte einen potentiellen Käufer, der das Kfz in ca. zwei Wochen eventuell um ca. 300.000,-  Euro kaufen wolle, konkrete Angaben dazu wollte Hr. NachnameGeser1 aber nicht machen.

**False Positives:**

- `Mag. Stb, ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_76`)


Am 13.06.2016 erklärte dann der Steuerberater Mag. Stb, der Verkauf sei nicht zustande  gekommen, sodass Hr. NachnameGeser1 beabsichtige, das Kfz aus dem Betrieb um einen  gegenüber den Anschaffungskosten geringeren Preis zu entnehmen.

**False Positives:**

- `Mag. Stb, ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `verb_context_name` 🏆

**F1:** 0.005 | **Precision:** 0.182 | **Recall:** 0.003  

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
| 0.182 | 0.003 | 0.005 | 33 | 6 | 27 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 27 | 2287 |

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

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_49`)


Im Firmenbuch ist Herr Jeskin als Geschäftsführer seit x.2009 eingetragen.

**False Positives:**

- `Herr Jeskin` — partial — gold is substring of pred: `Jeskin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeskin`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_62`)


Anspruch auf Familienbeihilfe, noch auf den Erhöhungsbetrag zur Familienbeihilfe wegen  erheblichen Behinderung zu.   Laut amtsärztlichen Sachverständigengutachten vom 3.12.2019 wurde Ihr Behinderungsgrad  im Ausmaß von 80 v.H. ab dem Monat Jänner 1987 und Ihr Unvermögen sich den Unterhalt  selbst zu verschaffen ab dem Monat Jänner 1987, also nach Vollendung Ihres 21.

**False Positives:**

- `Ihr Behinderungsgrad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_124`)


Das Gutachten des Sozialministeriumservice ist Ihrer Meinung nach nicht in sich schlüssig.

**False Positives:**

- `Ihrer Meinung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_148`)


Im gegenständlichen Fall wurde Ihr Unvermögen sich den Unterhalt selbst zu verschaffen, nach  Vollendung Ihres 21.

**False Positives:**

- `Ihr Unvermögen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_20`)


Dahingehend konnte Ihrer Beschwerde nicht entsprochen werden.

**False Positives:**

- `Ihrer Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_37`)


Welche Tätigkeit üben Sie in Österreich aus ? Wer ist Ihr Arbeitgeber ? Welche Arbeitszeiten  2 von 14 Seite 3 von 14

**False Positives:**

- `Ihr Arbeitgeber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_116`)


Nach ihrer Pensionierung ist Frau Merbot von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

**False Positives:**

- `Frau Merbot` — partial — gold is substring of pred: `Merbot`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Merbot`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_24`)


Mit Bescheid vom 22.07.2019 wurde Ihr Antrag auf Familienbeihilfe ab August 2018  abgewiesen.

**False Positives:**

- `Ihr Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_44`)


Die überwiegende Kostentragung wurde nicht nachgewiesen, daher wurde Ihr  Antrag auf Wiederaufnahme mit Bescheid vom 16.09.2020 abgewiesen.

**False Positives:**

- `Ihr  Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_57`)


Anschließend ist Herr  Mag. R ein neues Dienstverhältnis in der Schweiz eingegangen und mit der Familie von den USA  in die Schweiz übersiedelt. Die Verlagerung des Lebensmittelpunktes in den Entsendestaat sei  ergänzend an Hand der (Vermutungs-)Regel gemäß Rz 7596 EStR zu beurteilen.

**False Positives:**

- `Herr  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_102`)


Grundsätzlich sind gewisse Gegebenheiten zu bemängeln, aber es ist Herrn Oeverhaus in keiner Weise eine verdeckte Gewinnausschüttung an zu lasten.

**False Positives:**

- `Herrn Oeverhaus` — partial — gold is substring of pred: `Oeverhaus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oeverhaus`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_5`)


Alleingesellschafterin und Geschäftsführerin ist Frau Wahl   1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (kurz: Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Bf ist eine GmbH deren alleinige Gesellschafterin Frau Wahl ist.

**False Positives:**

- `Frau Wahl` — partial — gold is substring of pred: `Wahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wahl`(person)
- `Wahl`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_75`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Wahl   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Frau Wahl   Gegenstand` — partial — gold is substring of pred: `Wahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wahl`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_7`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_32`)


Begründung  Mit Erkenntnis vom 21.11.2019 wurde Frau Valerian Unterfranz  wegen Finanzvergehen gemäß § 33 Abs  1 FinStrG und § 33 Abs 2 lit a FinStrG zu einer Geldstrafe von € 8.800 verurteilt.  Strafbemessungsbasis waren – neben nichterklärten Einkünften aus Vermietung und  Verpachtung – Sicherheitszuschläge, welche die Außenprüfung den Einkünften aus  Gewerbebetrieb bzw. den Umsätzen hinzugerechnet hat.

**False Positives:**

- `Frau Valerian Unterfranz` — partial — gold is substring of pred: `Valerian Unterfranz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerian Unterfranz`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134192.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134192.1_6`)


Abgabe Frist Betrag Säumniszuschlag  Anspruchszinsen  2011  22.6.2018 6.419,16 128,38  Umsatzsteuer 2011 15.2.2012 28.439,73 568,79  Umsatzsteuer 2013 17.2.2014 13.343,44 266,89  Summe 964,04  Mit einem mit 16.9.2019 datierten Schreiben, das dem Finanzamt aber bereits am 12.9.2019  per Fax übermittelt worden war, erhob der Bf durch seine anwaltliche Vertretung Beschwerde  gegen die festgesetzten Säumniszuschläge und beantragte, die angefochtenen Bescheide  aufzuheben.

**False Positives:**

- `Betrag Säumniszuschlag  Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/135431.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135431.1_3`)


Entscheidungsgründe  Sachverhalt:    1) Bescheid vom 11.3.2019 über die Festsetzung von ersten Säumniszuschlägen:  Mit Bescheid vom 11.3.2019 wurden gegenüber dem Beschwerdeführer (Bf) nachstehende  erste Säumniszuschläge festgesetzt, weil er die angeführten Abgabenschulden nicht innerhalb  nachstehender Fristen entrichtet hatte:  Abgabe Frist Betrag Säumniszuschlag  Umsatzsteuer 2013 17.2.2014 37.501,16 750,02  1 von 14 Seite 2 von 14

**False Positives:**

- `Betrag Säumniszuschlag  Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135629.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135629.1_26`)


Bereits am 7.Juli 2017 unterfertigte der Bf einen unbefristeten Arbeitsvertrag mit der Fa XY - Interational, aufgrund dessen er ab Mitte August 2017 in CH-Ort-1/Schweiz als „Spezialist  Sensor Optics“ tätig war (Vollzeitdienstnehmer im Schichtbetrieb, bei Bedarf 3-Schichtdienst  incl.

**False Positives:**

- `Sensor Optics` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_50`)


4. In dem dagegen fristgerecht eingebrachten Vorlageantrag vom 01.04.2020 wurde zunächst  auf die beiden Beschwerden verwiesen und weiter vorgebracht:  „Frau Priv.-Doz.in Laetitia Pöstges  ist Schweizer Staatsbürgerin.

**False Positives:**

- `Schweizer Staatsbürgerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_91`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Bf. ist Schweizer Staatsbürgerin, hatte im Streitjahr 2019 in der Schweiz in ihrem  Elternhaus in Ort1 (CH)-Adr1 gemeinsam mit ihrer Mutter einen Wohnsitz und war im Jahr  2019 in der Schweiz als Lehrerin beschäftigt.

**False Positives:**

- `Schweizer Staatsbürgerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/138273.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138273.1_21`)


Da von der Kindsmutter ebenfalls der Familienbonus Plus für Ihren Sohn, geb.yyy  beantragt wurde, konnte Ihr Antrag auf den Familienbonus Plus nur zur Hälfte berücksichtigt  werden.

**False Positives:**

- `Ihr Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/139204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139204.1_31`)


Jene Familien, die dem Finanzamt Änderungen bekannt gegeben haben und bei  denen die Familienbeihilfe gestoppt wurde, bekamen die Familienbeihilfe nachträglich  ausgezahlt.  In diesen Fällen ist Ende Juli 2021 eine Nachzahlung der entsprechenden Familienbeihilfe- beträge durch das Finanzamt erfolgt.

**False Positives:**

- `Ende Juli` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamt`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_31`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. den  finanzgerichtlichen Datenbankrecherchen (Abgabenbehörde, Firmenbuch, Grundbuch) ergibt  sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung als erwiesen zu Grunde legt:  1. Adressat der angefochtenen Erledigung ist Wilhelm Fißenewert, LLM (Bf), der aufgrund eines Kaufvertrages  vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel Miteigentümer jener Liegenschaft  war, auf welcher der strittige Rohbau errichtet wurde (Lageadresse: 9999 R-Gasse 99,  nachfolgend R-Gasse).

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamtes`(organisation)
- `BFG`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_6`)


Laut Ihren Schreiben ist Ihre Tochter bei den  Großeltern haushaltzugehörig.

**False Positives:**

- `Ihre Tochter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/146600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146600.1_23`)


Laut Ihrem  Schreiben ist Ihre Tochter bei den Großeltern haushaltzugehörig.

**False Positives:**

- `Ihre Tochter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/149117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149117.1_53`)


Geschäftsführer ist Hc Kb. Gesellschafter der Bf. sind zu je 50 % Herr T Kb und  Frau H Kb.

**False Positives:**

- `Hc Kb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/149834.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149834.1_30`)


• Veranstaltungszentrum   Die Scheune – ein eigenes Gebäude (110m²) - sollte It Planung der Bf als  Veranstaltungszentrum Verwendung finden, wie ua für Feuerwehrfeste, Hochzeiten,  Adventmärkte, Flohmärkte, usw.

**False Positives:**

- `It Planung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `preposition_name` 💣

**F1:** 0.002 | **Precision:** 0.013 | **Recall:** 0.001  

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
| 0.013 | 0.001 | 0.002 | 158 | 2 | 156 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 156 | 2365 |

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

- `Ausgabenseite Umst` — no gold match — likely missing annotation

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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_70`)


Rechnung vom 29.10.2012 über € 21.583,10 , Leistungszeitraum 24.9.12-9.10.12 an der  Baustelle  Adresse1  2.)

**False Positives:**

- `Baustelle  Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_71`)


Rechnung vom 27.4.2012 über € 44.204,19, Leistungszeitraum 10.10.2012- 20.4.2012  an der Baustelle Adresse2  3.)

**False Positives:**

- `Baustelle Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_72`)


Rechnung vom 25.9.2012 über € 16.122,-, Leistungszeitraum 6.8.2012- 21.9.2012 an  der Baustelle Adresse3  4.)

**False Positives:**

- `Baustelle Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_14`)


Es handelt sich um eine Anonymverfügung die ich an der Adresse Semperstraße 19 erhalten  habe.

**False Positives:**

- `Adresse Semperstra` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129896.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129896.1_15`)


Wie bereits in einigen Telefonaten und emails an das jeweilige Magistrat mitgeteilt,  handelt es sich bei diesem Parkplatz um einen Privatparkplatz der zu der Liegenschaft  Semperstraße 19 gehört.

**False Positives:**

- `Liegenschaft  Semperstra` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_58`)


In der Bescheidbegründung führte die Behörde  aus:  "Gemäß § 30 Abs. 2 Z 1 EStG 1988 sind von der Besteuerung Einkünfte aus der Veräußerung  von Eigenheimen ausgenommen, wenn sie dem Veräußerer ab der Anschaffung bis zur  Veräußerung für mindestens zwei Jahre durchgehend als Hauptwohnsitz gedient haben und der  Hauptwohnsitz aufgegeben wird oder innerhalb der letzten zehn Jahre vor der Veräußerung  mindestens fünf Jahre durchgehend als Hauptwohnsitz gedient haben und der Hauptwohnsitz  aufgegeben wird.

**False Positives:**

- `Besteuerung Eink` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_6`)


Der Bf. wurde am 14. August 2018 untersucht und von der Neurologin Dr.in B am 28. August  2018 folgendes Gutachten erstellt:  "Anamnese:  Lt. VGA von 9/2015 50% GdB mit Diagnose paranoide Schizophrenie.

**False Positives:**

- `Neurologin Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_16`)


Ansonsten habe er lediglich auf einen Auszug aus der Fachliteratur Bezug genommen.

**False Positives:**

- `Fachliteratur Bezug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_93`)


welche in die Berechnung der Zeit nicht einzubeziehen ist, da die Zeiten des Fußweges nicht zu  berücksichtigen ist), von der Station Wien Volkstheater (U2) bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

**False Positives:**

- `Station Wien Volkstheater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_18`)


Beweis wurde erhoben durch Einsichtnahme in die Organstrafverfügung samt Fotos, welche  von einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund einer  eigenen dienstlichen Wahrnehmung gelegt wurde.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_11`)


Seine Arbeitsstätte  befinde sich an der Adresse Arbeitgeber, und seine genaue Berufsbezeichnung laute  Triebfahrzeugführer.

**False Positives:**

- `Adresse Arbeitgeber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_23`)


Belege von  der Schule Zeugnisse und Bestätigungen zwischen dem Zeitraum Juli 2014 bis September 2016  in Kopien sind beigelegt.“

**False Positives:**

- `Schule Zeugnisse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_68`)


Das Bundesfinanzgericht weicht mit dem vorliegenden Erkenntnis nicht von der  Rechtsprechungdes Verwaltungsgerichtshofes zu § 303 BAO ab, sondern folgt der in den  Erkenntnissen zB vom 17. Mai 1990, 89/16/0037, vom 24. Februar 2000, 96/15/0149, und vom  21. November 2007, 2006/13/0107 zum Ausdruck gebrachten Judikaturlinie, weshalb die  Revision nicht zuzulassen war.

**False Positives:**

- `Rechtsprechungdes Verwaltungsgerichtshofes` — partial — gold is substring of pred: `Verwaltungsgerichtshofes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_29`)


Von der Bestattung Wien wurden Ihnen mit einer ersten Rechnung vom 6.4.2011 folgende  Kosten in Rechnung gestellt:  Begräbnis Friedhof Malik Stellmaszick, Mittwoch 6.4.2011, 13:00 Uhr:    Mit einer zweiten Rechnung vom 6.4.2011 wurden Ihnen für die Exhumierung und  Wiederbestattung folgende Kosten in Rechnung gestellt:    Von den Friedhöfen Wien wurden Ihnen ebenfalls Leistungen in Rechnung gestellt, welche aber  offenbar von der Bestattung Wien bezahlt und an Sie unter dem Titel "Auslagen in Ihrem  Namen" weiter verrechnet wurden.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Malik Stellmaszick`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_34`)


Betrag setzt sich aus der Summe der von der Bestattung Wien in Rechnung gestellten Kosten  zusammen:    Bei der Todesfallaufnahme wurden folgende Begräbniskosten angeführt:    Dem Finanzamt wurden nur die Rechnungen der Bestattung Wien und der Friedhöfe Wien  vorgelegt.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_55`)


Der Gesamtbetrag wurde von der Bestattung Wien für Sie ausgelegt und Ihnen anschließend als  "Auslagen in Ihrem Namen" weiterverrechnet.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_73`)


Mit einer zweiten Rechnung vom 6.4.2011 wurden von der Bestattung Wien für die  Exhumierung und Wiederbestattung folgende Kosten verrechnet:    Dies steht im Einklang mit den Angaben des Bf. zu den Begräbniskosten bei der  Todesfallaufnahme.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_75`)


Dieser Betrag setzt sich aus der Summe der von der Bestattung Wien in Rechnung  gestellten Kosten zusammen:    9 von 14 Seite 10 von 14

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_89`)


Aus den  vorgelegten Rechnungen ist ersichtlich, dass die Rechnungen der Friedhöfe Wien von der  Bestattung Wien im Namen des Bf. bezahlt und an diesen weiterverrechnet wurden.

**False Positives:**

- `Bestattung Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_27`)


Grundsätzlich gelten hinterlegte Dokumente gem. § 17 Abs. 3 Zustellgesetz mit dem ersten Tag  der Abholfrist, dies sei der 14. Dezember 2018 gewesen, als zugestellt. Der Bf. werde in diesem  Zusammenhang um Bekanntgabe ersucht, ob er zum Zeitpunkt der Hinterlegung der  Strafverfügung nicht nur vorübergehend von der Abgabestelle abwesend gewesen sei und ob  er insbesondere durch eine Reise, einen Urlaub oder einen Krankenhausaufenthalt gehindert  gewesen sei, von der Zustellung Kenntnis zu erlangen.

**False Positives:**

- `Zustellung Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_14`)


Mit Schreiben vom 2. September 2020 („Verständigung vom Ergebnis der Beweisaufnahme“)  wurde der Bf. von der MA 67 in Kenntnis gesetzt, dass sich aus der Organstrafverfügung sowie  zwei Fotos, welche von einem Organ der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung ausgestellt worden sei, ergebe, dass das näher bezeichnete Fahr- zeug am 28. April 2020 um 19:40 Uhr in Wien 3, Landstraßer Hauptstraße 136, in einer ge- bührenpflichtigen Kurzparkzone ohne einem für den Beanstandungszeitpunkt gültigen Park- schein abgestellt gewesen sei.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_73`)


Der Beschwerdeführer erzielte im Zeitraum 09/2019 bis 12/2019 steuerpflichtige Einkünfte  (von der Landespolizeidirektion Steiermark) in Höhe von 5.075,80 € und im Zeitraum von  01/2020 bis 03/2020 4251,98 € (17.007,92 € : 4).

**False Positives:**

- `Landespolizeidirektion Steiermark` — partial — gold is substring of pred: `Landespolizeidirektion`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Mit "Kauf- und Wohnungseigentumsvertrag" vom 21.10.1998 hatte A (=  Beschwerdeführerin, Bf) von der Lemcon Entwicklung GmbH an der Liegenschaft in EZ1 (= Gst12 im  Gesamtausmaß von 734 m²) 25/481 ideelle Miteigentumsanteile erworben.

**False Positives:**

- `Lemcon Entwicklung Gmb` — partial — pred is substring of gold: `Lemcon Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lemcon Entwicklung GmbH`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_7`)


25/481 Anteile verbunden mit Wohnungseigentum  an der Dachbodeneinheit Top 7 für die Bf.   Erwerbszweck ist der Dachbodenausbau durch die Bf auf ihre alleinigen Kosten (Pkt. III.2.i)  1 von 8 Seite 2 von 8

**False Positives:**

- `Dachbodeneinheit Top` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_41`)


Seit August 2014 bezieht er eine Altersrente von der Liechtensteinischen Alters-  und Hinterlassenenversicherung.

**False Positives:**

- `Liechtensteinischen Alters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_6`)


Gegen diesen Bescheid wurde am 19.09.2014 von der Mieterin Beschwerde erhoben.

**False Positives:**

- `Mieterin Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_25`)


Seit Februar 2016 bezieht sie eine inländische Pension und seit 1. Mai  2017 eine Altersrente von der Liechtensteinischen Alters- und Hinterlassenenversicherung.

**False Positives:**

- `Liechtensteinischen Alters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/133565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133565.1_3`)


über das von der West Altrader GmbH  Dorf,  eingebrachte Anbringen vom 17. Mai 2021 in Zusammenhang mit dem an Gundula Doerfner, Öttlstraße 14, 3804 Reinsbach, Österreich  ergangenen Straferkenntnis des Magistrates der Stadt Wien vom 7. Mai 2021, GZ.  MA67/Zahl/2021, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, den  Beschluss gefasst:  Das Anbringen vom 17. Mai 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG zurückgewiesen.

**False Positives:**

- `West Altrader Gmb` — partial — pred is substring of gold: `West Altrader GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Altrader GmbH`(organisation)
- `Gundula Doerfner`(person)
- `Öttlstraße 14, 3804 Reinsbach, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_161`)


keine Buchführungspflicht besteht und auch nicht freiwillig Bücher geführt  werden, die eine Gewinnermittlung nach § 4 Abs. 1 ermöglichen,  2. die Umsätze im Sinne des § 125 Abs. 1 der Bundesabgabenordnung des  vorangegangenen Wirtschaftsjahres nicht mehr als 220 000 Euro betragen,  3. aus der Steuererklärung hervorgeht, dass der Steuerpflichtige von der  Pauschalierung Gebrauch macht.

**False Positives:**

- `Pauschalierung Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

**False Positives:**

- `Firma Furtnex` — positional overlap with gold: `Furtnex-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Furtnex-Versand GmbH`(organisation)
- `Ronald Jundt`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/134234.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134234.1_11`)


Im Rahmen eines zwischenstaatlichen Informationsaustausches erhielt das Finanzamt am  10.06.2020 Kenntnis darüber, dass der Beschwerdeführer im Jahr 2019 von der Deutschen  Rentenversicherung Bund eine Pensionsauszahlung in Höhe von 2437,02 € erhalten hat.

**False Positives:**

- `Deutschen  Rentenversicherung Bund` — type mismatch — same span as gold: `Deutschen  Rentenversicherung Bund`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Deutschen  Rentenversicherung Bund`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/134388.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134388.1_5`)


Entscheidungsgründe  Der Bf., der im Streitjahr 2019 an der Adresse Adresse wohnhaft war, bezog im Jahr 2019  Einkünfte aus nichtselbständiger Arbeit als Head of Business Development.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/134512.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134512.1_30`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Die im Jahr 1943 geborene Bf. war im Streitjahr durchgehend in Österreich ansässig und erhielt  unter anderem auch zwei Pensionskassenrenten und zwar eine Witwen-Rente von der X  Pensionskasse AG in Höhe von brutto CHF 19.490,30 und Alters-Rente von der Pensionskasse Contrazor AG in Höhe von CHF 7.210,00.

**False Positives:**

- `Pensionskasse Contrazor` — positional overlap with gold: `Contrazor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `X  Pensionskasse AG`(organisation)
- `Contrazor AG`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/134737.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134737.1_62`)


Der Bf hat ab 2005 an der Adresse Adr2 einen Nebenwohnsitz  gemeldet.

**False Positives:**

- `Adresse Adr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_30`)


Da die Daten des GWR von der  Statistik Austria dem BMF zur Verfügung gestellt werden und das BMF eine andere Behörde als  das zuständige Finanzamt ist, würde eine Abfrage dieser Daten das Erfordernis einer nach  außen erkennbaren Amtshandlung erfüllen.

**False Positives:**

- `Statistik Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)
- `BMF`(organisation)
- `Finanzamt`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_78`)


Das GWR wird von  Gemeinden und Bezirkshauptmannschaften mit Daten befüllt. Das GWR wird von der Statistik  Austria geführt und dem Bundesministerium für Finanzen zur Verfügung gestellt. Die Abfragen  des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel im GWR waren nach außen  erkennbare Amtshandlungen, auch wenn die (elektronische) Erkennbarkeit nur innerhalb des  Finanzressorts gegeben war.

**False Positives:**

- `Statistik  Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/134840.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134840.1_96`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt  Der Beschwerdeführer (infolge Bf) hat seinen Wohnsitz in Österreich an der Wohnsitzadresse  Ehrensdorf 23, 4720 Hading, Österreich (laut ZMR seit 10.3.2011, vorher befand sich der Wohnsitz in L) und bezieht  auch eine Pension von der Pensionsversicherungsanstalt.  Dem zuständigen FA G wurde laut Aktenvermerk vom 28.10.2015 bekannt, dass der Bf.  ausländische (deutsche) Pensionseinkünfte bezieht, die dem Progressionsvorbehalt  unterliegen, daher wurde dem Bf. die Formulare L1i zur ANV für 2010 bis 2014 zur  Beantwortung ausgehändigt.

**False Positives:**

- `Wohnsitzadresse  Ehrensdorf` — positional overlap with gold: `Ehrensdorf 23, 4720 Hading, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ehrensdorf 23, 4720 Hading, Österreich`(address)
- `Pensionsversicherungsanstalt`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/134859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134859.1_78`)


Beispiel  Ein Kleinunternehmer hat im Jahr X1 von der Toleranzregelung Gebrauch gemacht.

**False Positives:**

- `Toleranzregelung Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_108`)


In den Jahren 2005 bis 2008 war er  an der Adresse Adresse_A mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_109`)


Der Beschwerdeführer hat  gemeinsam mit seiner Ehegattin am 30.5.2005 einen Mietvertrag über eine Wohnung an der  Adresse Adresse_A, unterfertigt (vgl. Seiten 869-874 des Arbeitsbogens der Außenprüfung;

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_120`)


Auch die Ehegattin des Beschwerdeführers, E, und seine beiden Töchter Tochter_1 (geboren  1991) und Tochter_2 (geboren 1998) waren in den Jahren 2005 bis 2008 an der Adresse  Adresse_A mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse  Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/135216.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135216.1_177`)


Die Feststellung zum Zufluss von EUR 34.000,- im Zusammenhang mit dem Projekt P/Ort_3  ergibt sich aus der Aussage des Rechtsanwaltes S über die Einrichtung eines Treuhandkontos  zugunsten des Beschwerdeführers, aus der Rechnung Nr_2 über EUR 34.000,- und aus den  Belegen über die Einzahlung dieses Betrages auf das bzw. die Behebung vom Treuhandkonto  10 von 14 Seite 11 von 14

**False Positives:**

- `Rechnung Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_279`)


Das Vorbringen, die Annahme einer durchschnittlichen Stereckenlänge von 4,5 km sei zu kurz  bemessen, da Kunden, die sich zu Fuß zu einem Standplatz begeben „eher längere Strecken  fahren“ ist eine durch nichts begründete Behauptung, wohingegen die von der Wiener  Taxiinnung angegebene durchschnittliche Streckenlänge als durch Erfahrungswerte gesichert  angenommen werden kann.

**False Positives:**

- `Wiener  Taxiinnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_9`)


Mit dem angefochtenen Bescheid vom 8. Jänner 2020 forderte das Finanzamt von der  Antragstellerin Andrea Christoffelsmeier  die von ihr für März 2018 bis August 2019 für ihre Tochter  Karola Dannhäußer  bezogenen Beträge an Familienbeihilfe und Kinderabsetzbetrag zurück.

**False Positives:**

- `Antragstellerin Andrea Christoffelsmeier` — partial — gold is substring of pred: `Andrea Christoffelsmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Andrea Christoffelsmeier`(person)
- `Karola Dannhäußer`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_15`)


Hierauf langte die am 22. Jänner 2020 (Datum des Poststempels) zur Post gegebene, von der  Tochter Karola Dannhäußer  im eigenen Namen erhobene Beschwerde beim Finanzamt ein wie  folgt:   Sehr geehrte Damen und Herren,   hiermit lege ich, Karola Dannhäußer, eine Beschwerde gegen die Rückzahlung der Familienbeihilfe  und des Kinderabsetzbetrages ein.

**False Positives:**

- `Tochter Karola Dannh` — positional overlap with gold: `Karola Dannhäußer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karola Dannhäußer`(person)
- `Finanzamt`(organisation)
- `Karola Dannhäußer`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/135496.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135496.1_41`)


Diese brachte vor,  dass ihre Mutter von der Beschwerde Kenntnis hatte und damit auch einverstanden war.

**False Positives:**

- `Beschwerde Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/135828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135828.1_7`)


Sohn habe ab September 2016 auf das Studium Finanz-, Rechnungs- u. Steuerwesen  an der Fachhochschule Wien gewechselt.  1 von 7 Seite 2 von 7

**False Positives:**

- `Fachhochschule Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/135828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135828.1_22`)


Ab September 2016 wird das Bachelorstudium Finanz-, Rechnungs-und Steuerwesen an der  Fachhochschule Wien der WKW (laut Bestätigung des Studienerfolges für das Studienjahr  2016/17 wurden 62 SemStd.

**False Positives:**

- `Fachhochschule Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/136053.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136053.1_11`)


- Eine Bescheinigung über den Bestand eines festen Wohnsitzes vom 4. Juni 2020 betreffend  seine Ehegattin G, sowie der Töchter K1 und K2 an der Adresse Polen, x;  - mehrere Tankrechnungen;

**False Positives:**

- `Adresse Polen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_40`)


Eine Betrachtung anhand des von der Statistik Austria veröffentlichten Baukostenindex für den  Wohnungsbau Basis Mai 1945 ermögliche, die Preisentwicklung zwischen Mai 1945 und  Juni 2019 nachzuvollziehen.

**False Positives:**

- `Statistik Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Das Fahrzeug MarkeX, FahrgestellNr. 123, erstzugelassen in Deutschland im November 2010,  wurde am 1.12.2011 von der Dyksma Marine GmbH  die seit August 2012 als Alana Olfs (=  Beschwerdeführerin, Bf) mit Sitz in A-Ort1 firmiert, käuflich erworben.

**False Positives:**

- `Dyksma Marine Gmb` — partial — pred is substring of gold: `Dyksma Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dyksma Marine GmbH`(organisation)
- `Alana Olfs`(person)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_21`)


In diesen ist zu erkennen, dass der  Mietzins über dem von der Stadt Wien berechnet Mietzins liegt.

**False Positives:**

- `Stadt Wien` — type mismatch — same span as gold: `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/136338.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136338.1_18`)


Diese seien  nach dem Auslandsstudium im SS 2019 erfolgreich an der Uni Ort1 nachgeholt worden.

**False Positives:**

- `Uni Ort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/136623.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136623.1_43`)


Zur Reisezulage:  Im Kalenderjahr 2019 war ich einmal für die Organisation "Europäische Grenzschutzagentur  Frontex" in Trapani auf der Insel Silzilien (I) tätig.

**False Positives:**

- `Insel Silzilien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Europäische Grenzschutzagentur  Frontex`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/136669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136669.1_262`)


Zum Fliegen der Drohnen sei von der Austro Control eine  Pilotenlizenz vorgeschrieben (Beilage 24, S. 2 gelb markiert).

**False Positives:**

- `Austro Control` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_16`)


Mit Vorhalt vom 4. Februar 2020 wurde die Bf. um Vorlage eines Studienerfolgsnachweises von  T. für das Sommersemester 2019 (Kultur- und Sozialanthropologie an der Uni Wien, (auch  negative Ergebnisse!) sowie um einen Studienerfolgsnachweis der FH Kufstein ab  Studienbeginn ersucht.

**False Positives:**

- `Uni Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FH Kufstein`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_64`)


Sie bereitete sich aber im Laufe des Semesters auf die  Aufnahmeprüfung an der Fachhochschule Kufstein vor;

**False Positives:**

- `Fachhochschule Kufstein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_67`)


Die Aufnahmeprüfung an der Fachhochschule Kufstein bestand die Tochter der Bf.   Seit Oktober 2019 (Wintersemester 2019/20) ist sie als aktiv Studierende an der  Fachhochschule Kufstein Tirol im Bachelorstudiengang Sport-, Kultur- und  Veranstaltungsmanagement (Vollzeit) inskribiert (Inskriptionsbestätigung vom 04.09.2019,  Beschwerdevorbringen).

**False Positives:**

- `Fachhochschule Kufstein` — no gold match — likely missing annotation
- `Fachhochschule Kufstein Tirol` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_122`)


Die Tochter der Bf. absolvierte von Oktober bis Dezember 2018 an der Universidad de Grenada  in Spanien die Kurse „Spanish Grammar, Speaking and Writing Skills“, „History of Art in Spain“  und „Spanish Civilization and Culture“ und begann im Oktober 2019 an der Fachhochschule  Kufstein mit dem Bachelorstudium „Sport-, Kultur- & Veranstaltungsmanagement“.

**False Positives:**

- `Fachhochschule  Kufstein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_156`)


Die beiden bestehenden Garagentore wurden durch neue von der Firma Palisa ersetzt.

**False Positives:**

- `Firma Palisa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/137291.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137291.1_10`)


Begründend führte die belangte Behörde aus:  „Aus der dem Verfahren zugrundeliegenden Organstrafverfügung, welche von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien erstattet wurde, geht hervor,  dass das von Ihnen gelenkte mehrspurige Kraftfahrzeug an der im Spruch bezeichneten  Örtlichkeit zur angeführten Zeit im Bereich einer gebührenpflichtigen Kurzparkzone abgestellt  war, ohne dass die Parkometerabgabe entrichtet worden ist.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_66`)


Die Parkometerabgabe ist gemäß § 7 (Wiener)  Parkometergesetz 2006 von der Gemeinde Wien – mit Ausnahme eines diesbezüglichen  Verwaltungsstrafverfahrens – im eigenen Wirkungsbereich zu vollziehen.

**False Positives:**

- `Gemeinde Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/138030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138030.1_12`)


Beweis sei durch Einsichtnahme in die Organstrafverfügung erhoben worden, welche von  einem Parkraumüberwachungsorgan der Landespolizeidirektion Wien auf Grund eigener  dienstlicher Wahrnehmung gelegt worden sei, sowie in die (von diesem) angefertigten Fotos.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_59`)


Beschwerde  Innerhalb offener Frist wurde von der Bf Beschwerde erhoben und im Wesentlichen unter  Hinweis auf § 6 GrEStG – vor Inkrafttreten der Novelle 01.06.2014 – vorgebracht, dass mit der  Schätzung des Architekten Dipl. Ing. J M für das Kaufgrundstück ein gemeiner Wert von ca. €  261.000,00 nachgewiesen worden sei.

**False Positives:**

- `Bf Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/138705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138705.1_8`)


Dem vom Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde mit Bericht  vom 26. September 2022 dem Bundesfinanzgericht als zuständiges Verwaltungsgericht  vorgelegten Verwaltungsstrafakt ist folgender Verfahrensgang zu entnehmen:  Ein Parkraumüberwachungsorgan der Landespolizeidirektion Wien mit der Dienstnummer X  stellte am (Montag) 20. Juni 2022 um 12:54 Uhr fest, dass das mehrspurige Kraftfahrzeug mit  dem behördlichen Kennzeichen 123 (A) in einer gebührenpflichtigen Kurzparkzone in 1230  Wien, Haeckelstraße 4, abgestellt war und dass dieses Kraftfahrzeug nicht mit einem für diesen  Beanstandungszeitpunkt gültigen Parkschein gekennzeichnet war.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_8`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Johannes Kepler Universit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_68`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Camilla Schiedmann) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Johannes Kepler Universit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Camilla Schiedmann`(person)
- `Wirtschaftsuniversität Wien`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_83`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Johannes Kepler Universit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Finanzamtes`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_120`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

**False Positives:**

- `Johannes Kepler Universit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_143`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

**False Positives:**

- `Johannes  Kepler Universit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/138863.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138863.1_39`)


50 Bei der Prüfung der Behandlung der von der Verordnung Nr. 883/2004 erfassten  Arbeitnehmer kommt es daher auf den wirtschaftlichen Wert dieser Leistungen nicht im  Hinblick auf die Kaufkraft und das Preisniveau am Wohnort der betreffenden Personen, sondern  im Hinblick auf die Höhe der geschuldeten Leistungen an.

**False Positives:**

- `Verordnung Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/138903.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138903.1_9`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna wurde von einem  Parkraumüberwachungsorgan der Landespolizeidirektion Wien am 3. Jänner 2022 um 09:32  Uhr in der gebührenpflichtigen Kurzparkzone in 1130 Wien, Am Platz, beanstandet, da zur  Beanstandungszeit ein gültiger Parkschein fehlte.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/139535.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139535.1_41`)


Dies dient bestimmten - die Erfassung der Beträge beim  Empfänger betreffenden - Gesetzeszwecken, an denen sich auch die Ausübung des Ermessens,  von der Bestimmung Gebrauch zu machen, zu orientieren hat (vgl. VwGH 23.08.2022, Ra  2022/13/0072;

**False Positives:**

- `Bestimmung Gebrauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_153`)


In den von dem Bf. übermittelten Bank-Austria-Kontoauszügen (Konto XYZ in CHF) werden von  der Bank Austria Devisen-Brief-Kurswerte von 1,1936 (zum 31.12.2014) und von 1,1952 (zum  2.2.2015) angeführt (und nicht jene 1,04 laut steuerlicher Vertretung).

**False Positives:**

- `Bank Austria Devisen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/139642.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139642.1_159`)


Erst am 15. Januar 2015 wurde der im September 2011 eingeführte Mindestkurs von 1,20  Schweizer Franken pro Euro von der Schweizerischen Nationalbank (SNB) aufgehoben.

**False Positives:**

- `Schweizerischen Nationalbank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/140017.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140017.1_5`)


Darunter ein von der Nieder Glanzber GmbH  als Leasinggeber, mit der Beschwerdeführerin (kurz: Bf), FN-h,  damals noch mit dem Firmennamen K-GmbH, als Leasingnehmer, abgeschlossener  Leasingvertrag.

**False Positives:**

- `Nieder Glanzber Gmb` — partial — pred is substring of gold: `Nieder Glanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Glanzber GmbH`(organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/140074.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140074.1_23`)


2011 ein Zuschlag iHv € 5.802,15 nach § 28 Abs 7 iVm § 4 Abs 2 Z 2 EStG 1988 aus der Afa  Differenz berechnet und 2012 zum Überschuss aus Vermietung und Verpachtung  hinzugerechnet.

**False Positives:**

- `Afa  Differenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/140387.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140387.1_42`)


Weiters würden von der Firma FirmaA aufgrund  einer Sonderabmachung, beispielsweise KM-Preis von netto € 0,75 seit Jahren unverändert,  nicht alle Kilometer bezahlt werden.

**False Positives:**

- `Firma Firma` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/140707.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140707.1_58`)


Die von der Stadt Wien im elektronischen Wege gefertigten Dokumente weisen die Amts- signatur der Stadt Wien auf.

**False Positives:**

- `Stadt Wien` — type mismatch — same span as gold: `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/141261.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141261.1_19`)


Mit Schreiben vom 25. Februar 2019 wurde die Beschwerdeführerin neuerlich aufgefordert,  die Beträge mittels entsprechender Unterlagen unter Beweis zu stellen, da widrigenfalls die  von der Wiener Gebietskrankenkasse ermittelten Bemessungsgrundlagen herangezogen  würden.

**False Positives:**

- `Wiener Gebietskrankenkasse` — type mismatch — same span as gold: `Wiener Gebietskrankenkasse`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gebietskrankenkasse`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/141261.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141261.1_20`)


Mit Beschwerdevorentscheidung vom 03. April 2019 wurde die Beschwerde als unbegründet  abgewiesen und begründend ausgeführt, die Beschwerdeführerin sei von der Wiener  Gebietskrankenkasse zur Vorlage von Unterlagen aufgefordert und zur Schlussbesprechung  eingeladen worden, habe jedoch diesen Aufforderungen nicht Folge geleistet.

**False Positives:**

- `Wiener  Gebietskrankenkasse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/141403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141403.1_11`)


Unter Hinweis auf die Bestimmungen des § 17 Abs. 3 Zustellgesetz wurde der Bf. ersucht, der  Behörde binnen zwei Wochen bekanntzugeben, ob er zum Zeitpunkt der Hinterlegung der  Strafverfügung nicht nur vorübergehend von der Abgabestelle abwesend gewesen sei und  insbesondere durch eine Reise, einen Urlaub oder einen Krankenhausaufenthalt gehindert  gewesen sei, von der Zustellung Kenntnis zu nehmen.

**False Positives:**

- `Zustellung Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_138`)


Die von der Firma Hemken Automotive GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Wilhelm Fißenewert, LLM  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.“  (Zitatende/Beschwerde)  10.

**False Positives:**

- `Firma Hemken Automotive Gmb` — positional overlap with gold: `Hemken Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hemken Automotive GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/141761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141761.1_79`)


Dieser vorrangige  Anspruch wird auch in Deutschland anerkannt und wurde von der Familienkasse Bayern Süd an  die belangte Behörde gemeldet.

**False Positives:**

- `Familienkasse Bayern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/141773.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141773.1_74`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes genügt es für die  Unterbrechungswirkung einer Amtshandlung im Sinne des § 238 Abs. 2 BAO, dass sie nach  außen in Erscheinung tritt und erkennbar den Zweck verfolgt, den Anspruch gegen einen  bestimmten Abgabenschuldner durchzusetzen, ohne dass es darauf ankommt, ob die  Amtshandlung zur Erreichung des angestrebten Erfolges konkret geeignet war und ob der  Abgabenschuldner von der Amtshandlung Kenntnis erlangte (VwGH 13.09.2018, Ro  2018/16/0016 mwN).

**False Positives:**

- `Amtshandlung Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/142116.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142116.1_14`)


„Aus der Organstrafverfügung ergibt sich, dass das Fahrzeug mit dem behördlichen  Kennzeichen Vienna am 22.03.2023 um 12:29 Uhr von einem Parkraumüberwachungsorgan der  Landespolizeidirektion Wien in einer gebührenpflichtigen Kurzparkzone in Wien 1., Eßlinggasse  gegenüber 5 ohne gültigen Parkschein abgestellt wahrgenommen wurde.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/142791.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142791.1_71`)


Entspricht es doch dem Wesen einer einheitlichen Feststellung von Einkünften, dass sie  gegenüber allen an der Feststellung Beteiligten wirkt, wie sich dies auch aus § 191 Abs 3 lit b  BAO ergibt, wonach einheitliche Feststellungsbescheide gegen alle wirken, denen  gemeinschaftliche Einkünfte zufließen (VwGH 27.6.1991, 91/13/0002;

**False Positives:**

- `Feststellung Beteiligten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/143091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143091.1_7`)


Begründend wurde ausgeführt, dass die von der Deutschen Rentenversicherung Bayern Süd  bezogene Rente in Österreich als Ansässigkeitsstaat zur Berechnung des  Progressionssteuersatzes heranzuziehen sei.

**False Positives:**

- `Deutschen Rentenversicherung Bayern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/143091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143091.1_20`)


Aufgrund der von der deutschen Finanzverwaltung übermittelten Kontrollmitteilung wurde  bekannt, dass die Beschwerdeführerin im Jahr 2021 von der Deutschen Rentenversicherung  Bayern Süd eine Rente in Höhe von 1.954,92 € bezogen hat.

**False Positives:**

- `Deutschen Rentenversicherung  Bayern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/143785.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143785.1_27`)


Gegen den Sicherstellungsauftrag vom 22.04.2020 sei Beschwerde ergriffen  worden, da es sich beim von der Steuerfahndung Linz geschätzten Betrag nicht um eine  plausible Schätzung gehandelt habe.

**False Positives:**

- `Steuerfahndung Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_23`)


Der Beschwerdeführer war ausweislich des Zentralen Melderegisters von 4.9.2020 bis  15.12.2023 an der Adresse Adresse_A mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_33`)


K ist ausweislich des Zentralen Melderegisters seit Geburt an der  Adresse Adresse_B mit Hauptwohnsitz gemeldet.

**False Positives:**

- `Adresse Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/144274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144274.1_10`)


Der Bf. werde in diesem Zusammenhang ersucht bekanntzugeben, ob er zum Zeitpunkt der  Zustellung der Strafverfügung nicht nur vorübergehend von der Abgabestelle abwesend war  und insbesondere durch eine Reise, einen Urlaub oder einen Krankenhausaufenthalt gehindert  gewesen sei, von der Zustellung Kenntnis zu nehmen.

**False Positives:**

- `Zustellung Kenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_43`)


Das BFG richtete mit verfahrensleitendem Beschluss vom 6. März 2024 einen Vorhalt an Frau  Ruperta Keymer  und die belangte Behörde samt folgenden, fünf Beilagen:   Anbringen der Hausverwaltungskanzlei vom 17. Februar 2016 an das Finanzamt für  Gebühren, Verkehrssteuern und Glückspiel betreffend die ihr von der Vitt Logistik GmbH erteilte  Vollmacht, wobei die Vitt Logistik GmbH vom Finanzamt gemäß § 81 Abs. 2 BAO als Vertreter für  die Gesamtheit der Eigentümer bestellt wurde.

**False Positives:**

- `Vitt Logistik Gmb` — partial — pred is substring of gold: `Vitt Logistik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Ruperta Keymer`(person)
- `Finanzamt für  Gebühren`(organisation)
- `Vitt Logistik GmbH`(organisation)
- `Vitt Logistik GmbH`(organisation)
- `Finanzamt`(organisation)

</details>

---

## `academic_suffix_name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `336950c7`  
**Description:**
Matches person names with academic suffixes (MSc, LL.M., etc.) including preceding titles (Mag., Dr.) and suffixes like MBA, M.B.L.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*\s+(?:MSc|LL\.M\.|B\.Sc\.|M\.Sc\.|B\.A\.|M\.A\.|Ph\.D\.|Dr\.\s+iur\.|Bakk\.\s+iur\.|Dipl\.\s+iur\.|MBA|M\.B\.L\.|M\.B\.L\.)(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*)\b(?![,\s])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

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

## `family_relation_name` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

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

## `single_initial_person_2` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a1335c60`  
**Description:**
Captures single initials (e.g., 'M.', 'E.') when they appear in contexts indicating a person (e.g., 'Sohn C. M.', 'Firma Y. GmbH').

**Content:**
```
(?:Sohn\s+[A-Z]\s+([A-Z]\.)|Firma\s+([A-Z]\.)\s+GmbH|Vereinbarung\s+getroffen,\s+dass\s+die\s+([A-Z]\.)\s+eine)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `anonymous_person_dr` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92c2ef4c`  
**Description:**
Captures anonymous persons denoted by 'Dr. X.' or similar single-letter citations in quotes or specific contexts.

**Content:**
```
(?:\u201e|\u201c|\u201d|\u201c|"|\()Dr\.\s+([A-Z]\.)\s*(?:\)|\u201d|\u201d|"|\s|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `herr_initial_person` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a31d3f83`  
**Description:**
Captures person initials following 'Herr' (e.g., 'Herr JG').

**Content:**
```
\bHerr\s+([A-Z]{2,3})\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 30 | 0 | 30 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 30 | 2332 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_159`)


Das heißt, auch 2005, 2006, 2007, was wir gemacht haben und 2008, was Herr FT gemacht hat,  da hat er zwar vergessen, das einzutragen, das steht auch völlig außer Streit, aber er hat die  Beilage und die KÖSt-Erklärung eingegeben und hat dann angekreuzt, ja da sind Beilagen.

**False Positives:**

- `FT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_184`)


Eigentlich gar nicht Buchhaltung und Herr KB hat überwiegend nur Buchhaltung.

**False Positives:**

- `KB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_185`)


Darum hat man gesagt, in seiner Nähe ist Herr FT und man ist in Kontakt gewesen.

**False Positives:**

- `FT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_190`)


SB: Also sie sagen, aus dem was der Herr FT da eingereicht hat, geht eindeutig hervor, dass  man die Zurechnung erkennen konnte.

**False Positives:**

- `FT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_195`)


Wir haben das damals genauso formuliert mit dem  Firmenwert, den der Herr FT quasi übernommen hat, 1:1 in seiner Buchhaltung.

**False Positives:**

- `FT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/132289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132289.1_9`)


Geschäftsführender Alleingesellschafter ist Herr XY-.

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/132289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132289.1_30`)


Diesen beiden Urkunden und den Angaben des FA in der BVE vom 17.Mai 2016 zufolge, ist die  XY- Trans Slovakia s.r.o., ICO 99 999 999, eine - der Rechtsform nach einer österreichischen  GmbH vergleichbare - Gesellschaft mit Sitz in 999 99 MA/Slowakei, in welcher Herr XY-  ebenfalls als geschäftsführender Alleingesellschafter fungiert.

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_15`)


Im Zeitraum September 2008 bis Jänner 2009 habe der Gesellschafter  Herr EK insgesamt € 205.000,- in vier Teilbeträgen auf das Konto der Bf einbezahlt, da die  Gesellschaft nicht über die entsprechenden Mittel verfügt hätte, den Umbau zu finanzieren.

**False Positives:**

- `EK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_33`)


Ebenso sei es unstrittig, dass Herr WS letztlich sowohl die Betriebskosten als auch die  Kreditraten übernommen habe.

**False Positives:**

- `WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_39`)


Als Nutznießer dieser Konstruktion komme  nur Herr MS in Betracht, um die durch die Scheidungsvereinbarung erforderliche private  Kostentragung der Wohnung in das Erscheinungsbild einer unternehmerischen Vermietung zu  kleiden.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_57`)


Herr MS habe daraus keinen persönlichen  Vorteil, weder in wirtschaftlicher noch in steuerrechtlicher Hinsicht.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_81`)


Der Gatte der  Gesellschafter-Geschäftsführerin, Herr WS, hat nach Aufbrauchen des VSt-Guthabens die  Bezahlung der monatlichen Kreditraten übernommen.

**False Positives:**

- `WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_101`)


Aus dem Mietvertrag ergibt sich, dass Herr MS zur Bezahlung der Miete verpflichtet war.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_104`)


Da Herr MS der Schwager der Gesellschafter-Geschäftsführerin ist, handelt es sich beim Mieter  der gegenständlichen Eigentumswohnung um einen nahen Angehörigen.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_146`)


Die Miete hat laut Mietvertrag der Mieter, Herr MS, zu bezahlen.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_45`)


Darauf Bezug nehmend wurde dem BFG vom Fachbereich des Finanzamtes mit mail vom  29.11.2017 mitgeteilt:  "… Herr AA gibt an, am 31.3.2014 eine NoVA-Erklärung für den streitgegenständlichen MarkeX  eingereicht zu haben.

**False Positives:**

- `AA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Finanzamtes`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_56`)


2. In Widerspruch dazu haben Sie bzw. Herr GF AA im e-mail vom 23.11.2017 dem Finanzamt  mitgeteilt, dass Ihnen nunmehr "die mit 31.3.2014 eingereichte NoVA-Erklärung für den  4 von 13 Seite 5 von 13

**False Positives:**

- `GF` — partial — pred is substring of gold: `GF AA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GF AA`(person)
- `Finanzamt`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_115`)


In der streitgegenständlichen Erklärung datiert mit 26.03.2014 geht die Bf. bzw. Herr AA  offensichtlich davon aus, dass der NoVA Tatbestand bereits mit Januar 2014 eingetreten ist.

**False Positives:**

- `AA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_121`)


Zu Anlage H darf noch ausgeführt werden, dass Herr AA in seiner Stellungnahme vom  29.12.2021 angibt, dass er am 26.03.2014 mit der Verfassung der Erklärung bereits begonnen  habe.

**False Positives:**

- `AA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/136069.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136069.1_123`)


Warum Herr AA in der Erklärung, welche er  am 30.03.2014 erstellen begonnen hat, ein rückwirkendes Datum und zwar den 26.03.2014 und  nicht den 30.03.2014 festgehalten hat, ist fraglich.

**False Positives:**

- `AA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_43`)


Im angeführten Postskriptum dieser Schreiben hat Herr DI M  folgendes angeführt:  PS.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/138117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138117.1_40`)


Infolge des  Testamentes und der Eröffnungsniederschrift vom 26.6.2020 sind gesetzliche Erben des  Nachlasses: Die Ehegattin Frau Vorname Vorname2 Nachname, zu 50 % des Erbteiles, der Sohn  Herr G A Nachname zu 25 % des Erbteiles sowie Herr AC Nachname zu 25 % des Erbteiles.

**False Positives:**

- `AC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/138648.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138648.1_25`)


Wenn Herr XY auf das Schreiben der  Behörde nicht geantwortet habe, könne er nichts dafür.

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/138648.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138648.1_98`)


Der Bf. ist der Aufforderung der Behörde vom 27. November 2020, geeignete Beweise für die  Lenkereigenschaft von XY vorzulegen, trotz Hinweis auf seine erhöhte Mitwirkungspflicht, nicht  nachgekommen, sondern hat sich darauf beschränkt vorzubringen, dass er nichts dafür könne,  wenn Herr XY auf das Schreiben der Behörde nicht geantwortet habe.

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_5`)


Das Fahrzeug ist auf die T S.r.l. zugelassen, deren Geschäftsführer  und Gesellschafter Herr CD, der Schwager der Bf., ist.

**False Positives:**

- `CD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_45`)


Herr ZS sei als Fahrer beschäftigt gewesen und habe administrative Tätigkeiten sowie  Vertragsabschlüsse für Hr. CD gemacht (im Namen der Firma T S.r.l.).

**False Positives:**

- `ZS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_55`)


habe, gab Hr. CD an, dass das Herr ZS und er selbst dies gewesen wären.

**False Positives:**

- `ZS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/145191.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145191.1_101`)


Der Ehemann der Bf., Herr ZS, nutzte bei seiner Kraftfahrertätigkeit für die T S.r.l. neben einem  Kastenwagen der Marke Citroen mit dem Kennzeichen CDE auch das gegenständliche Kfz Audi  A6.

**False Positives:**

- `ZS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_373`)


Seit  6.8.2014 bis jedenfalls 31.12.2015 ist auch Herr DI ……..(ein weiterer Fremdgeschäftsführer)  Geschäftsführer.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_377`)


Seit 4.8.2014 bis jedenfalls 31.12.2015 ist auch Herr DI …..(ein  weiterer Fremdgeschäftsführer) Geschäftsführer.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `richter_initial_person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4768de29`  
**Description:**
Captures single initials following 'Richter' or 'Richterin' (e.g., 'Richter I.').

**Content:**
```
\b(?:Richter|Richterin)\s+([A-Z]\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `contextual_name_no_title` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f62c0124`  
**Description:**
Captures person surnames following legal case markers ('in der Sache', 'in der ...-Entscheidung') and possessive phrases ('von Frau', 'von Herrn', 'bei der'), ensuring full surname capture and excluding trailing punctuation.

**Content:**
```
(?:in\s+der\s+(?:Sache|Beschwerdesache|Verwaltungsstrafsache|Rechtssache|Verfahren|Entscheidung|Urteil|Sache\s+\w+)|von\s+(?:Frau|Herrn|Herr|Frau\s+\w+)|bei\s+der|bei\s+den|bei\s+einem|bei\s+einer)\s+(?<!\w)([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*)\b(?![,\s])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 153 | 0 | 153 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 153 | 2375 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_201`)


Nach der Rechtsprechung des VwGH ist es zulässig, dass das Bundesfinanzgericht den dem  Erstbescheid zugrunde gelegten Sachverhalt rechtlich anders würdigt als das Finanzamt und  den Zeitpunkt der Entstehung der Steuerschuld anders ansetzt (vgl. VwGH vom 11.9.2014,  2013/16/0156, zur Änderung des Zeitraumes bei einer Normverbrauchsabgabe;

**False Positives:**

- `Normverbrauchsabgabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_234`)


Im Rahmen der anzustellenden Gesamtbildbetrachtung spricht im vorliegenden Fall gegen den  behaupteten Wegzug bereits im Streitjahr 2013 die erst am 27. Oktober 2013 erfolgte  Abmeldung seines Hauptwohnsitzes in Österreich, die Anmeldung in der Schweiz am 10.  Dezember 2013 - somit verzögert und nicht zeitgleich -, die erst am 17. März 2014 erfolgte  Abmeldung des Kraftfahrzeuges in Österreich und der per 1. Jänner 2014 erfolgte Abschluss bei  der Schweizer Krankenversicherung.

**False Positives:**

- `Schweizer Krankenversicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_11`)


In Ansehung vorbeschriebener Geschäftsgebarung wurden seitens der Prüferin im  Schätzungsweg die Umsatzsteuerbemessungsgrundlagen der Jahre 2009 und 2010 auf  Bruttobasen von 36.800,00 Euro (Wochenerlöse von 800,00 Euro auf Basis von 46  Aktivwochen) zuzüglich der rund 30 % nämlichen Betrages zum Ansatz gebrachten Erlöse der  bei der Bf. beschäftigten, namentlich jedoch unbekannten beschäftigten Prostituierten von  11.200, 00 Euro, sprich sohin im Nettoausmaß von jeweils 40.000,00 Euro errechnet und von  aus diesen resultierenden Umsatzsteuern von 8.000,00 Euro auf abgabenbehördlich  erhobenen Mietzahlungen basierende Vorsteuern von 1.950,00 Euro (2009) bzw. 2.802.00  Euro (2010) in Abzug gebracht, so dass die Umsatzsteuerzahllasten summa summarum auf  6.050,00 Euro (2009) sowie auf 5.198,00 Euro (2010) lauteten.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_676`)


Bei der Besprechung vom 30. November 2011  wurde vom Bf. mitgeteilt, dass diese Lieferungen seit Mitte Oktober (Ergänzungsfrage 4 bei der  Artikel-V-Anfrage in Deutschland, Befragung der Ehegatten MH zum Fahrer) mittels LKW-

**False Positives:**

- `Artikel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_6`)


Durch die zuständige Abgabenbehörde wurde bei der Bf., beginnend im Jahr 2009, eine  Außenprüfung (AP) durchgeführt, die neben Körperschaft- und Umsatzsteuer für das Jahr 2008  auch die Kapitalertragsteuer zum Prüfungsgegenstand hatte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_79`)


Die AP selbst gab an, dass sie weder hatte zuordnen können wer bei der Bf. die Entscheidung  über die Zahlung getroffen hatte, noch ob der angenommene Zufluss des Betrages an einen  oder sämtliche Anteilsinhaber anteilig erfolgt war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_92`)


noch nicht fälligen Leasingraten und des Restwertes, abgezinst zur jeweils geltenden  Basiszinssatz der OeNB, zuzüglich einer Pauschale in der Höhe von € 300,- für den aufgrund der  außerordentlichen Auflösung [bei der Beschwerdeführerin] anfallenden Arbeitsaufwand zu.  Beim Restwert handelt es sich um den entweder vertraglich festgelegten oder, wenn eine  vertragliche Festlegung nicht erfolgt ist, von [der Beschwerdeführerin] kalkulierten, am Ende  der Leasingzeit zu erwartenden Fahrzeugerlös.

**False Positives:**

- `Beschwerdeführerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_8`)


Im Rahmen einer Betriebsprüfung der Jahre 2015 bis 2017 bei der Bf. wurde im Bericht vom  23. Juni 2020 unter Tz 3 folgendes festgehalten:   1 von 12 Seite 2 von 12

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_125`)


Die „doch realistische Chance“ beim VfGH wird  darin gesehen, dass die Pönalisierung der Abmilderung sozialer Härten durch ein Abzugsverbot  nicht dazu beitragen kann, das Einkommensgefälle in der Bevölkerung zu reduzieren und sich  der VfGH „in einem neuerlichen Verfahren anders entscheiden könnte, als bei den Golden  Handshakes“.   c. In der Beschwerde vom 30. Juni 2020 wird dazu ausgeführt, die unsachliche  Gleichbehandlung bewirke, dass von Sozialplänen Abstand genommen werde.

**False Positives:**

- `Golden  Handshakes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_111`)


Ein X scheint im  österreichischen Firmenbuch bei der Bf. aber mit keiner Funktion auf.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_38`)


Zu der vermeintlich formalen  Meldung sei festgehalten, dass es sich bei der Bf. um eine Gesellschaft mbH handelt, an der  neben drei natürlichen Personen auch zwei Gesellschaften mit begrenzter Haftung beteiligt  sind.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_225`)


- Die FFG gab der Behörde mit Schreiben vom 25. Oktober 2016 bekannt, dass die  übermittelten Unterlagen (vom 31. Mai 2016) nur sehr allgemeine Beschreibungen enthalten  wobei ersucht wurde, weitere Unterlagen hinsichtlich der in der Pilotanlage bzw. großen  Anlage durchgeführten Probetrocknungen bei der Bf. anzufordern und in denen auf (im  Schreiben) näher dargestellte Fragen eingegangen werden sollte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_328`)


Dessen ungeachtet hat die Behörde in der Beschwerdevorentscheidung die beantragten  Aufwendungen sowohl von der GET als auch von der FMT im Jahr 2012 bei der Bf. bei der  Bemessung der Forschungsprämie für Auftragsforschung anerkannt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_297`)


Die Kontrolle der Arbeit erfolge durch Telefonanrufe durch ÖU bei den Kunden.

**False Positives:**

- `Kunden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_25`)


Das heiße, kein  Anspruch bei der Arbeitnehmerveranlagung.

**False Positives:**

- `Arbeitnehmerveranlagung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_101`)


Die Kosten für das A4-Heft in Höhe von 2,09 € vom 7.01.2013 waren analog den Ausführungen  zum Werbungskostencharakter der Kosten für das A4-Heft bei der Fa. Thalia Bücher GmbH als  Werbungskosten gemäß § 16 Abs. 1 EStG 1988 anzuerkennen.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_118`)


Aufgrund der Bestimmungen des § 34 Abs. 4 und 5 EStG 1988 ergibt sich der Selbstbehalt bei  der Bf. somit wie folgt:       Da die Ausgaben für das Blutdruckmessgerät in Höhe von 66,90 € den Selbstbehalt (§ 34 Abs. 4  EStG 1988) von 2.703,20 € nicht übersteigen, waren diese Kosten bei der Berechnung der  Einkommensteuer für das Jahr 2013 nicht zu berücksichtigen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_111`)


Im April 1987 lag bei der Bf. eine Oligophrenie vor, sie war (im Jahr 1983) in ihrer Ehe  überfordert, es kam zu Erregungszuständen, die bei solchen Kranken den Wert einer Psychose  haben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_5`)


Kommanditist mit einer  Haftsumme von € 1.000,00 ist A.  Im Zuge der Bearbeitung des Aktes des Kommanditisten durch das Finanzamt wurde  festgestellt, dass dieser bei der Bf. auch regelmäßig in einem geringfügigen  Beschäftigungsverhältnis stand.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_20`)


Von 09/2018 bis 09/2019 hat ihr Sohn ehrenamtlich  bei der Ausbildung zum Versicherungsagenten und Vermögensberater bei der Fa. I…  Finanzmanagement im Gegenzug diverser Sponsoraktivitäten teilgenommen.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_21`)


Laut Vereinbarung war er in der Saison 2019 bei der Fa. …speed als Rennfahrer, ohne Bezüge  tätig.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_59`)


Versicherungsagenten und Vermögensberater bei der Fa. I… Finanzmanagement im Gegenzug  diverser Sponsoraktivitäten teil‘ und betätigte sich (ohne Bezüge) als Rennfahrer.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Von 01. Februar 2016 bis 30. November 2018 war die Tochter des Bf. Arbeiterlehrling bei der  Fa. D. KG (Beschwerde, Abgabeninformationssystemabfrage).

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_54`)


In den folgenden Monaten Juli - bis Ende November 2018 - setzte die Tochter des Bf. ihre Lehre  bei der Fa. D. KG bis 30. November 2018 fort.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Heilsarmee` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Artner-Tauscher`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_204`)


Übers AMS Berufsfindungskurse   Lebte bei den Eltern;

**False Positives:**

- `Eltern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_206`)


Lebt seit Herbst 2017 bei der Heilsarmee- zuerst betreute WG (dort sei es nicht gut gegangen  weil er mehr äußere Tagesstruktur brauchte).

**False Positives:**

- `Heilsarmee` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_89`)


Seit 29. August 2016 ist der Bf. bei der Fa. G. Bau GmbH & Co KG nichtselbständig beschäftigt  (Abgabeninformationssystemabfrage).

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `G. Bau GmbH & Co KG`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_12`)


Die Bf. wurde als Beschuldigte niederschriftlich einvernommen und gab zu Protokoll, dass sie  als diplomierte Gesundheits- und Krankenpflegerin bei der Fa. MOKI Wien arbeite.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_15`)


Eine Bestätigung ihres Dienstgebers  bezüglich ihres damaligen Patienten lasse sie bei der Behörde.

**False Positives:**

- `Behörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_124`)


Der Bf. hat jedoch lediglich vorgebracht, dass sein Fahrzeug auf Grund von Erledigungen beim  Ausfüllen (gemeint wohl: bei der Aktivierung) des ersten Parkscheines in erheblichem Abstand  zum folgenden Abstellort stadtauswärts auf derselben Straßenseite gestanden sei.

**False Positives:**

- `Aktivierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_39`)


Mit Vertrag vom 29.12.2006 kaufte der Bf. von FrauA die vorbezeichnete Liegenschaft (mit  Ausnahme des neu gebildeten Grundstückes Nr. im Ausmaß von 5000 m² gemäß  Vermessungsurkunde DI) samt dem Inventar gemäß der einen integrierenden Bestandteil des  Vertrages bildenden Beilage./1, die einen Auszug aus dem Schätzungsgutachten SV2 vom  Datum2 bildet [Pkt. 1.1. und 2.1. des Kaufvertrages (in der Folge kurz: KV)] ; als Kaufpreis  wurde ein Betrag von Euro XX vereinbart (Pkt 3.1 des KV), wobei der Bf. für den Erwerb der  Liegenschaft inklusive sämtlicher Nebenkosten insgesamt Euro XY aufbrachte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_107`)


Die belangte Behörde ging bei den Einkommens- und Vermögensverhältnissen der Bf. von  durchschnittlichen Verhältnissen aus, da die Bf. hierzu keine Angaben machte.

**False Positives:**

- `Einkommens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_43`)


Bei diesen Gelegenheiten besuche er ebenso seine von ihm  getrennt lebende Frau und manchmal deren behinderte Nachbarin und helfe diesen bei der  Gartenarbeit.

**False Positives:**

- `Gartenarbeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_40`)


In Übereinstimmung mit dieser Rechtsprechung hat das Finanzamt im Rahmen der bei der Bf.  hinsichtlich der Jahre 2009 bis 2012 durchgeführten Außenprüfung festgestellt, dass die  gegenüber Y erbrachten Vermittlungsleistungen im Inland der Umsatzsteuerpflicht unterliegen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_169`)


Die Verjährungsfrist beträgt nach § 207 Abs. 2 BAO bei den Verbrauchsteuern, bei den festen  Stempelgebühren nach dem II. Abschnitt des Gebührengesetzes 1957, weiters bei den Gebüh- ren gemäß § 17a des Verfassungsgerichtshofgesetzes 1953 und § 24a des Verwaltungsgerichts- hofgesetzes 1985 drei Jahre, bei allen übrigen Abgaben fünf Jahre.

**False Positives:**

- `Gebüh` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_18`)


Er benötige vor allem bei der Körperpflege Hilfe.

**False Positives:**

- `Körperpflege Hilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_31`)


Die Leistungen der Friedhöfe Wien wurden bereits vollständig in den Rechnungen der  Bestattung Wien wie folgt erfasst:  In der ersten Rechnung unter "Friedhöfe Wien" bzw. "Zusatzleistungen Friedhöfe Wien":      In der zweiten Rechnung unter "Friedhöfe Wien":    Die Summe dieser Beträge entspricht dem von den Friedhöfen Wien in Rechnung gestellten  Betrag:    Dies steht im Einklang mit Ihren Angaben zu den Begräbniskosten bei der Todesfallaufnahme.

**False Positives:**

- `Todesfallaufnahme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_73`)


Mit einer zweiten Rechnung vom 6.4.2011 wurden von der Bestattung Wien für die  Exhumierung und Wiederbestattung folgende Kosten verrechnet:    Dies steht im Einklang mit den Angaben des Bf. zu den Begräbniskosten bei der  Todesfallaufnahme.

**False Positives:**

- `Todesfallaufnahme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_91`)


Die Kosten für einen einfachen Sarg wurden im Schätzungsweg anhand von Erfahrungswerten  ermittelt, wobei der Bf. keine Stellungnahme dazu abgegeben hat.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_11`)


Nach anschließendem Bezug von Arbeitslosengeld und Notstandshilfe ist die Bf "seit 4.5.2020  bis laufend" bei der Fa. Y-GmbH als Angestellte beschäftigt.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_20`)


Sie  besuche von 9.9.2019 bis 6.7.2020 die Berufsschule (aufgrund der Pandemie derzeit lt. eigenen  Angaben online) und sei lt. SV-Daten seit 4.5.2020 bei der Fa. Y-GmbH angestellt. Die  Lehrausbildung in einem gesetzlich anerkannten Lehrverhältnis, die im österr.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_13`)


In jedem der beiden Bescheide wurde bei der Einkünfte- und  Einkommensermittlung nur der Pauschbetrag für Werbungskosten in Höhe von 132,00 €  abgezogen.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_260`)


Die steuerfreien Einkünfte gemäß  § 3 Abs. 1 Z 5 lit. a EStG 1988 (Arbeitslosengeld, Notstandshilfe, Krankengeld während  Arbeitslosigkeit) wurden im verfahrensgegenständlichen Bescheid vom Finanzamt bei der Bf.  beim "Einkommen gemäß § 2 Abs. 2 EStG 1988" erfasst, beim Kindesvater wurden diese nicht  berücksichtigt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_18`)


Anlässlich des Verlassens  der Vorsorgeeinrichtung infolge der Beendigung der Grenzgängertätigkeit sei aufgrund der  liechtensteinischen gesetzlichen Bestimmungen zwingend eine Übertragung auf ein Freizügig- keitskonto bei einer liechtensteinischen Bank oder auf eine Freizügigkeitspolice bei einer Ver- sicherung in Liechtenstein vorzunehmen gewesen.

**False Positives:**

- `Ver` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_74`)


Auch haben wir feststellt, dass diese Rechnungen bei der Fa. A.-Fenster auf die  Beschwerdeführer KEG gebucht wurden (ersichtlich auf Kontoblatt von der Fa. A.-Fenster).

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_92`)


In der Praxis kommt dies  unentwegt vor und wird üblicher weise wie auch bei der Fa. Beschwerdeführer GmbH  ausgebucht.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_96`)


Es wird der Verdacht, dass es sich bei der Fa.POU Bau GmbH  eingesetzt als Subunternehmen im  Jahr 2008 und der Fa. Y-Montage GmbH eingesetzt als Subunternehmer im Jahr 2009 um  Scheinfirmen handelt im vollen Umfang zurück gewiesen.

**False Positives:**

- `Fa` — partial — pred is substring of gold: `Fa.POU Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fa.POU Bau GmbH`(organisation)
- `Y-Montage GmbH`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_210`)


Vor dem dargestellten Hintergrund geht das BFG davon aus, dass Letzteren Leistungen der Synkel-Versicherung GmbH zugrunde liegen und die zugehörigen Erlöse bei der Synkel-Versicherung GmbH versteuert wurden.

**False Positives:**

- `Synkel` — similar text (different position): `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_211`)


Dem AP-Bericht ist nicht zu ersehen, dass bei der Synkel-Versicherung GmbH erfasste Erlöse aus AR des  3.Quartals 2007 an die Fa A.-Fenster im Zuge der AP aus den Besteuerungsgrundlagen 2007  ausgeschieden wurden.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_224`)


In den Prüferaufzeichnungen ist vermerkt (AP-Akt OZ 13), dass bei der Synkel-Versicherung GmbH Kassaeinlagen  „in nicht geringem Ausmaß“ gegen das Verrechnungskonto des Bf gebucht wurden  (Verrechnungsverbindlichkeit der Synkel-Versicherung GmbH gegenüber dem Bf zum 31.12.2007 rd.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_227`)


Obwohl der Bf seine Anteile an der Synkel-Versicherung GmbH bereits zwei Jahre vor der AP veräußert hatte und  zudem bei der Synkel-Versicherung GmbH ein Insolvenzverfahren anhängig war, beschränkten sich die  AP-Erhebungen zur Klärung der Kassaeinlagen auf eine Aufforderung an den Bf zur Beibringung  der „Einzahlungsbelege“ bzw. der „entsprechenden Bankbehebungen (…) (Bankauszüge)“.

**False Positives:**

- `Synkel` — similar text (different position): `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_262`)


Ende April 2009 erfolgte eine buchhalterische Berichtigung der Kassaeinlagen und zugleich  Reduktion des “fiktiven“ Kassenstandes bei der Synkel-Versicherung GmbH unter Ausbuchung der zugehörigen  Verrechnungsverbindlichkeiten gegenüber dem Bf.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_265`)


c) Rechtliche Beurteilung:  Auf Basis der festgestellten Sach- und der dargestellten Rechtslage erweist sich die Zurechnung  einer verdeckten Ausschüttung an den Bf im Zusammenhang mit den im AP-Bericht Tz.4/1.)  erfassten Vorgängen betreffend die Fa A.-Fenster als nicht berechtigt, da insofern weder von  einer Vermögensverminderung bei der Synkel-Versicherung GmbH bzw. einer Bereicherung beim Bf auszugehen,  noch eine Zuwendungsabsicht der Synkel-Versicherung GmbH erwiesen ist.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_275`)


Ertragswirksame Auswirkungen bei der Synkel-Versicherung GmbH hätten aus den genannten Maßnahmen nicht  resultiert.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_276`)


Auf Basis des als erwiesen angenommenen Sachverhalts trat somit im Zusammenhang mit den  unter Tz.4/1.) des AP-Berichts erfassten Vorgängen weder im Jahr 2007 noch später eine  Vermögensverminderung bei der Synkel-Versicherung GmbH oder eine Bereicherung des Bf ein.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_279`)


Für die Verwirklichung einer verdeckten Gewinnauswirkung fehlte es somit, neben einem  gewinnmindernden Vermögensabfluss bei der Synkel-Versicherung GmbH  auch am Nachweis der beabsichtigten  Zuwendung eines durch das Gesellschaftsverhältnis begründeten Vermögensvorteils an den Bf.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_428`)


Den Prüferanmerkungen auf der Rechnung ist zu entnehmen, dass  entsprechende Kassa-/Bankbewegungen bei der Synkel-Versicherung GmbH fehlten (AP-Akt OZ 25).

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synkel-Versicherung GmbH`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_430`)


Der zugeordnete Kassaeingangsbeleg der Noruniwerk Robotik GmbH vom 10.Juni 2009 über den Erhalt der  Restzahlung von 5.000,- € ist als Dokument aus dem Rechenwerk der Noruniwerk Robotik GmbH zum Nachweis  für einen entsprechenden Kassaausgang bei der Synkel-Versicherung GmbH schon dem Grunde nach nicht  geeignet.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)
- `Noruniwerk Robotik GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_433`)


Aufgrund der angeführten Umstände misst das BFG dem Kassabeleg vom 10.Juni 2009 keine  Beweiskraft für den nachzuweisenden Geldabfluss bei der Synkel-Versicherung GmbH bei.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_449`)


2.2 Nachdem das BFG den beiden im AP Akt der Rechnung der Noruniwerk Robotik GmbH vom 3.Juni 2009  angeschlossenen Kassabelegen aus den dargestellten Gründen keine Beweiskraft für den darin  dokumentierten Geldfluss beimisst und darüber hinaus keine tragfähigen Beweismittel zum  Nachweis der mit diesen Belegen verbundenen Geldbewegungen bei der Synkel-Versicherung GmbH vorliegen, ist  eine Bereicherung des Bf insofern nicht erwiesen.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Noruniwerk Robotik GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_450`)


Zugleich konnte auch eine im Zusammenhang mit der Verbuchung der Rechnung der Noruniwerk Robotik GmbH  vom 3.Juni 2009 eintretende Gewinnminderung bei der Synkel-Versicherung GmbH zu keiner Bereicherung beim  Bf führen, da er am Gewinn des Jahres 2009 nicht mehr teilnahm.

**False Positives:**

- `Synkel` — partial — pred is substring of gold: `Synkel-Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Noruniwerk Robotik GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_100`)


derartige Arbeitsmittel spezialisierten Fachfirma angemietet und den Mitarbeitern der X - nach  einer entsprechenden Einschulung durch dieses Spezialunternehmen - zur Verfügung gestellt.   Auf der Baustelle agierte der bei der Bf. angestellte W als Bauführer, der nicht nur die Qualität  der Arbeiten an Ort und Stelle überprüfte, sondern dort auch als Ansprechpartner für andere  Firmen auftrat;

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_185`)


In derselben Rechnung wird als Besteller ein  „Herr T“ angeführt, dabei handelt es sich um den (damals) bei der Bf. beschäftigten Johann T.  Dass an Baubesprechungen ausschließlich Mitarbeiter der Bf. teilnahmen, ist zwischen den  Streitteilen unstrittig.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_220`)


beide bezeichneten den bei der Bf. beschäftigten W wörtlich als  „Polier“ der Baustelle (ZV M aaO, S. 7; ZV N aaO, S. 10).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/133676.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133676.1_95`)


Die Einkommens-  und Vermögensverhältnisse und allfällige Sorgepflichtendes Beschuldigten sind bei der Be- messung von Geldstrafen zu berücksichtigen.

**False Positives:**

- `Be` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_112`)


Pflichtversicherung auf Grund dieser Tätigkeit  liege genausowenig vor wie Mitgliedschaft bei einer Kammer.

**False Positives:**

- `Kammer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_194`)


Bezüglich der Geltendmachung offener Ansprüche hätte sie am 22.4.2011 einen  Termin bei der Arbeiterkammer.

**False Positives:**

- `Arbeiterkammer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_214`)


Betreffend Fragestellung 2) ist zunächst die oben zitierte Rechtsprechung des BFG vom  15.06.2020, RV/3100661/2018 ins Treffen zu führen, wonach bei einem Gesellschafts- Geschäftsführer der nicht Unternehmer iSd. UStG ist, für die Bemessungsgrundlage des  Betriebsausgabenpauschales gemäß § 17 Abs. 1 EStG 1988 die Betriebseinnahmen  maßgeblich sind.

**False Positives:**

- `Gesellschafts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_72`)


Der Umstand, dass dem Bf. der Milderungsgrund der verwaltungsstrafrechtlichen Unbe- scholtenheit nach dem Wiener Parkometergesetz zu Gute komme, habe jedoch bei der Straf- bemessung insofern berücksichtigt werden können, als dass die Strafe entsprechend niedrig  bemessen worden sei, da nicht erkennbar sei, dass nur eine höhere Geldstrafe geeignet wäre,  den Bf. wirksam von einer Wiederholung abzuhalten.

**False Positives:**

- `Straf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_102`)


An Hand von sieben „Beispielfahrten“ und unter Zugrundelegung der im Internet  veröffentlichten Preistabellen sowie der Annahme, dass „in der Regel“ die Retourfahrt eine  Leerfahrt sei, und einem tatsächlichen Anteil des Bf. i.H. von 62 % bei der Fa. G und 54 % bei  der Fa. V des Gesamtumsatzes des Botendienstunternehmens ermittelte der Bf.  einen  Kilometerertrag von € 0,50/km.

**False Positives:**

- `Fa` — no gold match — likely missing annotation
- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_267`)


Der Treibstoffverbrauch muss daher geschätzt werden, wobei der  Bf. die der Schätzung innwohnende Ungenauigkeit zu tragen hat.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/135379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135379.1_9`)


Die Beschwerdevorentscheidung wurde dem Bf. nach einem Zustellversuch am 29. Jänner 2021  durch Hinterlegung bei der Post-Geschäftsstelle 1213 zugestellt und das behördliche Schrift- stück ab 1. Februar 2021 zur Abholung bereitgestellt.   Die Verständigung über die Hinterlegung wurde in die Abgabeeinrichtung eingelegt.

**False Positives:**

- `Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/135379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135379.1_11`)


Sachverhalt und Beweiswürdigung:  Aus der Aktenlage ergibt sich, dass die Beschwerdevorentscheidung des Finanzamtes, mit  welchem der Beschwerde des Bf. gegen den Bescheid des Finanzamtes vom 12. November  2020 teilweise stattgegeben wurde, indem die Familienbeihilfe ab Oktober 2020 gewährt und  für den Zeitraum von August 2020 bis September 2020 abgewiesen wurde, dem Bf. durch  Hinterlegung bei der Post-Geschäftsstelle 1213 am 1. Februar 2021 (= 1. Tag der Abholfrist)  zugestellt wurde.

**False Positives:**

- `Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_24`)


Es gebe deutliche Problem bei der Alltagsbewältigung.

**False Positives:**

- `Alltagsbewältigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/135523.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135523.1_85`)


LJ.   04.06.1996 18.06.1996  Krankengeldbezug    19.06.1996 12.07.2002 6 J u 1 M Tischlereihilfsarbeiter  bei der Fa. AG2  GmbH, Vollzeit  19.06.96-31.12.96  5.599,22 Euro  01.01.97-31.12.97  10.073,76 Euro  01.01.98-31.12.98  10.243,74 Euro  01.01.99-31.12.99  10.449,12 Euro  01.01.00-31.12.00  10.664,59 Euro  01.01.01-31.12.01  10.882,25 Euro  01.01.02-12.07.02  5.941,35 Euro  Mit Schreiben 19.02.2021 bestätigt die Fa.  AG2 GmbH (Tischlerei), dass der Bf im  genannten Zeitraum als Hilfsarbeiter tätig  war und es sich hierbei, aufgrund der  Einstufung des Bf als begünstigt behinderte  Person, um einen geschützten Arbeitsplatz  gehandelt hat   Am 00 vollendet der Bf sein 25.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/135774.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135774.1_19`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:   Sachverhalt:   Die Beschwerdeführerin (Bf.) war im Jahr 2019 als Schadenreferentin bei der Fa. X..AG  beschäftigt und bezog für den Zeitraum 01.01. – 31.12.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/135794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135794.1_83`)


Eine solcher Fall läge beispielsweise dann vor, wenn der Behörde nur die Mitteilung der PVA  (Schreiben vom 16. Februar 2018) vorgelegen wäre, wonach bei der Bf. Beiträge an  Krankenversicherungen gemäß § 73a ASVG i.H.v. € 109,68 als Werbungskosten zu  berücksichtigen sind.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/136083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136083.1_13`)


Im Jahr 2011 fand bei der Bf. eine Außenprüfung gemäß § 150 BAO statt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/136562.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136562.1_8`)


Die Strafverfügung wurde dem Bf. am 17. Dezember 2021 durch Hinterlegung bei der Post- Geschäftsstelle 1160 Wien zugestellt und nach Nichtbehebung binnen der Abholfrist an die  Magistratsabteilung 67 am 4. Jänner 2022 retourniert.

**False Positives:**

- `Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/136562.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136562.1_65`)


Aus dem Verwaltungsstrafakt ergibt sich folgender Sachverhalt:  Die Strafverfügung des Magistrates der Stadt Wien, MA 67, vom 3. November 2021, GZ. Zahl  (Titelbescheid) wurde dem Bf. am 17. Dezember 2021 durch Hinterlegung bei der Post- Geschäftsstelle 1160 Wien zugestellt.  Die Strafverfügung wurde nicht behoben und erwuchs in Rechtskraft.

**False Positives:**

- `Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_8`)


Ich ersuche Sie höflich,  den nun im Anhang nachgereichten Unterlagen von Frau Mag. M… (Klinische und  Gesundheitspsychologin, Hilfswerk NÖ) und Frau OA Dr. St… (FA für Kinder- und  Jugendheilkunde) zu entnehmen, dass der für den rückwirkenden Anspruch auf erhöhte  Familienbeihilfe erforderliche Behinderungsgrad von J… bereits zu einem früheren Zeitpunkt  belegbar ist.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_179`)


Diese Beträge bleiben bei der  Einnahmen-Ausgaben-Rechnung außer Ansatz.

**False Positives:**

- `Einnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_69`)


Abfuhrpflichtige (zB der Arbeitgeber bei der Lohnsteuer) sind Abgabepflichtige iSd § 77 Abs 1  (zB Ritz, Akteneinsicht, 10, FN 16;

**False Positives:**

- `Lohnsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/137437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137437.1_11`)


Da es sich gegenständlich um eine Biogasanlage und nicht um eine Wasserkraftanlage handle,  seien die oa. Voraussetzungen nicht erfüllt. Aufgrund dessen stehe der Hälftesteuersatz nicht  zu.  In der als Beschwerde zu behandelnden Berufung vom 4.10.2011 wurde dargelegt, dass es sich  bei der Bf. um ein Elektrizitätsversorgungsunternehmen im Sinne des § 1 EnFG handle.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/137464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137464.1_6`)


Im Herbst 2015 wurde eine Betriebsprüfung bei der Bf.  durchgeführt, die zu einer Wiederaufnahme der Verfahren zur Gewinnfeststellung gem. § 188  BAO für die Jahre 2011-2013 führte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/138586.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138586.1_6`)


Dem Finanzamt wurden jedoch vom Arbeitgeber die bereits um das  Pendlerpauschale gekürzten nichtselbständigen Einkünfte aus dem Dienstverhältnis  übermittelt.  Es wurden daher auch im Einkommensteuerbescheid 2016 vom 27.02.2017 bei der  Berechnung des Einkommens und der Einkommensteuer die bereits um das Pendlerpauschale  in Höhe von 1.476,00 € gekürzten Einkünfte bei der Fa. Düsterloh Pflege AG  in Ansatz gebracht.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Düsterloh Pflege AG`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/138700.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138700.1_9`)


Das Auskunftsersuchen wurde nach einem Zustellversuch am 28. November 2019 durch  Hinterlegung bei der Post-Geschäftsstelle 1150 Wien, Europaplatz 3, am Freitag, den  29. November 2019 zugestellt und ab diesem Tag zur Abholung bereitgehalten.

**False Positives:**

- `Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/138903.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138903.1_14`)


In der Folge wurde dem Bf. von der Magistratsabteilung 67 nach einer bei der Zulassungs- besitzerin eingeholten Lenkerauskunft mit Strafverfügung vom 28. März 2022 angelastet, er  habe das in Rede stehende Kraftfahrzeug am 3. Jänner 2022 in der gebührenpflichtigen Kurz- parkzone in 1130 Wien, Am Platz vor Kirche bei Denkmal, ohne einen für den Beanstandungs- zeitpunkt 09:32 Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahr- lässig verkürzt.

**False Positives:**

- `Zulassungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/139132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139132.1_59`)


Ab Oktober 2020 war S bis zur Auskunft von Pro Juventute am 16.03.2021 an  folgenden Tagen bei der Bf:  untertags: 23.10., 27.10., 15.11., 14.11., 06.12., 02.02., 14.03..  über Nacht: 24.-30.12., 01.-03.01, 05.-09.02., 20.-22.02., 06.-07.03..

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/139132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139132.1_118`)


Der Sohn gilt daher nicht als haushaltszugehörig bei der Bf.  Besteht keine nur vorübergehende Abwesenheit im Sinne des § 2 Abs 5 lit a FLAG 1967 und  liegt keine ständige Anstaltspflege wegen eines Leidens oder Gebrechens des Kindes gemäß  § 2 Abs 5 lit c FLAG 1967 vor, könnte gemäß § 2 Abs 2 FLAG 1967 einen  Familienbeihilfenanspruch dann gegeben sein, wenn der Antragsteller oder die Antragstellerin  die Unterhaltskosten überwiegend trägt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_49`)


Lebensjahr: demnach war er zB in den Jahren 2005, 2006 und 2007 nahezu durchgehend       bei der Fa. EE beschäftigt;

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_271`)


Zugleich  war er aber lt. vorliegenden Einkommensdaten beispielsweise in den Jahren 2005, 2006 und  2007 nahezu durchgehend bei der Fa. EE sowie in den Jahren 2014 und 2015 durchgehend bei  18 von 20 Seite 19 von 20

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/139689.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139689.1_148`)


Die Einkommens-  und Vermögensverhältnisse und allfällige Sorgepflichten des Beschuldigten sind bei der Be- messung von Geldstrafen zu berücksichtigen."

**False Positives:**

- `Be` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/139802.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139802.1_9`)


Diesen Antrag begründete die beschwerdeführende Partei dergestalt, dass es sich bei der Aus-  bzw. Fortbildung um ein MSc Studium für Management und Leadership handle.

**False Positives:**

- `Aus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/140044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140044.1_74`)


Folgender Sachverhalt wird der Entscheidung zu Grunde gelegt:  Der Bf bezog im Streitjahr 2020 neben seiner inländischen Pension auch eine Rente von der  „Deutschen Rentenversicherung Bund“ in Höhe von 1.115,58 €, wobei der Kranken- versicherungsbeitrag für die ausländische Leistung 4,66 € pro Monat (ds 55,92 € p.a.) beträgt.

**False Positives:**

- `Kranken` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Deutschen Rentenversicherung Bund`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_4`)


Auf Grundlage der am 07.07.2017 beim damals zuständigen Finanzamt Innsbruck  eingegangenen Beantwortung der „Überprüfung des Anspruches auf Familienbeihilfe“  (Schreiben vom 30.06.2017) und vor allem des beigelegten Lehrvertrages des Sohnes der Frau  Raimund Ondrouch (= Beschwerdeführerin, Bf) vom 21.09.2016 (Lehrzeit vom 02.09.2016 bis zum  01.09.2019 bei der Fa. S-GmbH als Sonnenschutztechniker) wurde die Familienbeihilfe für den  Sohn A, geb. 07/1999, zunächst verlängert.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Innsbruck`(organisation)
- `Raimund Ondrouch`(person)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_10`)


4. Mit 19.11.2019 erging an die Bf ein Vorhaltschreiben des Finanzamtes, wonach aufgrund des  Versicherungsdatenauszuges des Sohnes die Lehre bei der Fa. S-GmbH mit April 2019  abgebrochen worden sei.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_39`)


Vom 09.05.2014 - 15.10.2018  waren sie bei der Firma Berg-Transport Werke GmbH beschäftigt.

**False Positives:**

- `Firma Berg` — positional overlap with gold: `Berg-Transport Werke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Berg-Transport Werke GmbH`(organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/140745.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140745.1_15`)


Lt. Vorhaltsbeantwortung im Zuge der Vor-BP bei der Fa. XY Immo GmbH wird das Facility  Management für die Anlagen und Gebäude der Fa. XY Immo GmbH sowie die  Finanzierungsverhandlungen bei Banken und Investoren durchgeführt.

**False Positives:**

- `Fa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `herr_frau_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `34129a99`  
**Description:**
Captures names following 'Herr' or 'Frau' titles, ensuring the full name is captured including suffixes, and excluding trailing punctuation.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)(?:Herr|Frau)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*)\b(?![,\s])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 1423 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/137270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137270.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dr. OStR Vivian Stinneßen (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 03/1997, laufend die  Familienbeihilfe (FB) samt Kinderabsetzbetrag (KG) bezogen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. OStR Vivian Stinneßen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. OStR Vivian Stinneßen`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_225`)


Während des gesamten Zeitraumes war seine Hausärztin  Frau Hausärztin.

**False Positives:**

- `Hausärztin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/149384.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149384.1_79`)


Eine Kontrolle in unserer Crohn/Colitis/Reizdarm-ambulanz  nach tel Terminvereinbarung wird empfohlen....  Konsil Psychiatrie vom 09.06.2020:  Diagnose: Panikstörung bzw. unspezifische Angststörung Komplexe posttraumatische   Belastungsstörung, DD: Emotional instabile Persönlichkeitsstörung  Therapieempfehlung: - die Reevaluierung der psychopharmakologischen Medikation wäre  notwendig - diesbezüglich soll sich die Patientin an ihren niedergelassenen Facharzt wenden  - aktuell nimmt die Patientin nur Atarax bei Bedarf  - mit der Patientin wird die mögliche Teilnahme an einem Therapieprogramm h.o. evaluiert   - die Teilnahme an unserem stationären Turnus-Therapieprogramm erscheint zielführend –  diesbezüglich noch Abklärung mit Frau Mag. K. Aus psychiatrischer Sicht scheint die Patientin  derzeit ausreichend stabil für die Teilnahme.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/149470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149470.1_329`)


Die StB brachte hiezu vor: Die Fremdgeschäftsführerin Frau Mag…….

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `definite_article_person` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `af8afcca`  
**Description:**
Captures person names preceded by 'die' or 'den' followed by a legal role (Richter, etc.) or specific context. FIXED to capture the full name including any title immediately following the role.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)(?:die\s+(?:Richter|Richterin|Senatsvorsitzende|Vizepr\u00e4sident|Vizepr\u00e4sidentin|Senatspr\u00e4sident|Senatspr\u00e4sidentin)|den\s+(?:Richter|Richterin|Senatsvorsitzende|Vizepr\u00e4sident|Vizepr\u00e4sidentin|Senatspr\u00e4sident|Senatspr\u00e4sidentin|steu\u00e4rlichen\s+Vertreter|steuerlichen\s+Vertreter))\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Mag\.Mag\.|MMag\.|DI\.|Ing\.|Bakk\.|Dipl\.|Univ\.-?Prof\.|Prof\.|Priv\.-?Doz\.|DDr\.|KommR\.|\u00d6kR\.|RgR\.|MedR\.|VetR\.|AR\.|OMedR\.|KzlR\.|HR\.|Techn\.|PhD\.|Senatspr\u00e4sident\.|Vizepr\u00e4sident\.|Hofrat\.|Hofr\u00e4tin\.|Hofr\u00e4ts\.|Vizepr\u00e4sidentin\.|Senatspr\u00e4sidentin\.|Hon\.-?Prof\.|OStR|OStRin|Priv\.-?Doz\.in|Univ\.-?Prof\.in|OStR(?:\s+Ing\.)?|OStRin|KzlR|StR|MedR|KommR|\u00d6kR|VetR|Vizepr\u00e4sident|Senatspr\u00e4sident|Hofrat|Hofr\u00e4tin|Hofr\u00e4ts|Vizepr\u00e4sidentin|Senatspr\u00e4sidentin|Prof\.in\s+Techn\s+R|Univ\.-?Prof\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `von_role_name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d228660e`  
**Description:**
Captures names following 'von' + [Legal Role] (e.g., 'von Zweitbeschuldigten', 'vom Erstbeschuldigten') to handle genitive case patterns where the role precedes the name.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)(?:von\s+(?:dem|der|den|einem|einer|dem|des|dem|dem)|vom|von\s+der|von\s+den|von\s+einem|von\s+einer)\s+(?:Zweitbeschuldigten|Erstbeschuldigten|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Angeklagte|Angeklagten|Antragsteller|Antragstellerin|Antragsgegner|Antragsgegnerin|Partei|Parteien|Zeuge|Zeugin|Zeugen|Kl\u00e4ger|Kl\u00e4gerin|Beklagte|Beklagten|Vertreter|vertreten|Sohn|Kind|Frau|Herrn|Herr|die|den|des|der|dem)\s+(?<!\w)([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)+)(?:\s*,\s*(?:Bakk\.\s+(?:art\.|techn\.|iur\.|jur\.|phil\.)|MBA|M\.Sc|LL\.B\.\s*LL\.M\.|LL\.M\.|PhD|Dr\.|Mag\.)?)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 2322 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_157`)


Ausgeführt wurde wie folgt:  „Mit Schreiben vom 21.2.2020 wurde vom Beschwerdeführer Ihre Einvernahme als Zeuge im  gegenständlichen Verfahren beantragt.

**False Positives:**

- `Ihre Einvernahme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_175`)


Ausgeführt wurde wie folgt:  „Mit Schreiben vom 21.2.2020 wurde vom Beschwerdeführer Ihre Einvernahme als Zeuge im  gegenständlichen Verfahren beantragt.

**False Positives:**

- `Ihre Einvernahme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_49`)


Jene Firma, von der die Fytterer Handel GmbH hauptsächlich beliefert wird, ist die Fa.TraunBeratung GmbH  Der  Gesellschafter und Geschäftsführer der letztgenannten GmbH ist B.B., Ehegemahl der Bf..

**False Positives:**

- `Fytterer Handel` — partial — pred is substring of gold: `Fytterer Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fytterer Handel GmbH`(organisation)
- `Fa.TraunBeratung GmbH`(organisation)

</details>

---

## `richter_context_name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `975d50e9`  
**Description:**
Captures person names following 'Richter' or 'Richterin' when a title is present, ensuring the full name including title is captured.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)(?:Richter|Richterin)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\.a|Mag\.Mag\.|MMag\.|DI\.|Ing\.|Bakk\.|Dipl\.|Univ\.-?Prof\.|Prof\.|Priv\.-?Doz\.|DDr\.|KommR\.|\u00d6kR\.|RgR\.|MedR\.|VetR\.|AR\.|OMedR\.|KzlR\.|HR\.|Techn\.|PhD\.|Senatspr\u00e4sident\.|Vizepr\u00e4sident\.|Hofrat\.|Hofr\u00e4tin\.|Hofr\u00e4ts\.|Vizepr\u00e4sidentin\.|Senatspr\u00e4sidentin\.|Hon\.-?Prof\.|OStR|OStRin|Priv\.-?Doz\.in|Univ\.-?Prof\.in|OStR(?:\s+Ing\.)?|OStRin|KzlR|StR|MedR|KommR|\u00d6kR|VetR|Vizepr\u00e4sident|Senatspr\u00e4sident|Hofrat|Hofr\u00e4tin|Hofr\u00e4ts|Vizepr\u00e4sidentin|Senatspr\u00e4sidentin|Prof\.in\s+Techn\s+R|Univ\.-?Prof\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*(?:\s+-\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df\u00e9\u00e8\u00ea\u00eb\u00ef\u00ee\u00f4\u00f9\u00fb\u00fc]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 413 | 0 | 413 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 413 | 2389 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Gerald Erwin Ehgartner` — partial — pred is substring of gold: `MMag. Gerald Erwin Ehgartner`

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

- `Manuela Fischer` — partial — pred is substring of gold: `Mag. Manuela Fischer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Raphael Williamson, BEd`(person)
- `Züggen 8, 8042 Graz, Österreich`(address)
- `Monika Pfundner-Lenz`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Wendy Scherl, Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich, über die Beschwerde vom 27. Mai 2019 gegen  den Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 14. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 53-864/4798  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Wendy Scherl`(person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `53-864/4798`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Feichtenschlager in der  Beschwerdesache Daisy Wegelein, Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich, über die Beschwerde vom 28. November 2018  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 13. November 2018 betreffend  Einkommensteuer 2017, Steuernummer 61-004/6209, zu Recht erkannt:   I. Der angefochtene Bescheid wird wie folgt abgeändert:  Außergewöhnliche Belastungen   Freibetrag wegen eigener Behinderung (§ 35 (3) EStG 1988) - 75,00 €  Pauschbetrag für Diät nach der Verordnung über  außergewöhnliche Belastungen wegen eigener Behinderung  - 840,00 €  Nachgewiesene Kosten aus der eigenen Behinderung nach der  Verordnung über außergewöhnliche Belastungen  - 36,11 €  Summe außergewöhnliche Belastungen - 951,11 €  Einkommen 29.456,86 €  Einkommensteuer 5.813,10 €  Anrechenbare Lohnsteuer - 3,301,16 €  Festgesetzte Einkommensteuer gerundet - 2.512,00 €  II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig

**False Positives:**

- `Susanne Feichtenschlager` — partial — pred is substring of gold: `Mag. Susanne Feichtenschlager`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Feichtenschlager`(person)
- `Daisy Wegelein`(person)
- `Schmiedbachweg 9, 4722 Hötzmannsberg, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `61-004/6209`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom  31. Juli 2019 der Beschwerdeführerin Matthäus Domrös, Halstenbekerstraße 17, 9652 Nostra, Österreich, gegen den Bescheid des  Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Dr. Gerlinde  Rieser, vom 8. Juli 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:  I)  Der Einkommensteuerbescheid 2018 wird abgeändert und die Einkommensteuer wird mit  einem Guthaben von EUR 1.853,00 festgesetzt.

**False Positives:**

- `Erich Schwaiger` — partial — pred is substring of gold: `Mag. Erich Schwaiger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Matthäus Domrös`(person)
- `Halstenbekerstraße 17, 9652 Nostra, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Dr. Gerlinde  Rieser`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Nadja Rossetto, Rechte Quergasse 2, 2512 Oeynhausen, Österreich, vertreten durch Imre & Schaffer Rechtsanwälte OG, Ludersdorf  201, 8200 Gleisdorf, über die Beschwerde vom 6. August 2018 gegen den Haftungsbescheid  des Finanzamtes Oststeiermark vom 6. Juli 2018 Steuernummer 85-716/2059  zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Alois Pichler` — partial — pred is substring of gold: `Dr. Alois Pichler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alois Pichler`(person)
- `Nadja Rossetto`(person)
- `Rechte Quergasse 2, 2512 Oeynhausen, Österreich`(address)
- `Imre & Schaffer Rechtsanwälte OG`(organisation)
- `Finanzamtes`(organisation)
- `85-716/2059`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Donald Paulovits, Tröbach 41, 9130 Leibsdorf, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 95-720/4312  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Alois Pichler` — partial — pred is substring of gold: `Dr. Alois Pichler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alois Pichler`(person)
- `Donald Paulovits`(person)
- `Tröbach 41, 9130 Leibsdorf, Österreich`(address)
- `Mag. Achmed Ghazal Aswad`(person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `95-720/4312`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Monika Kofler` — partial — pred is substring of gold: `Dr. Monika Kofler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Monika Kofler`(person)
- `Maximilian Joobs`(person)
- `Forsthausweg 11, 3580 Poigen, Österreich`(address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Oleg Kreissl, Schoaderstraße 2, 3441 Freundorf, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Peter Unger` — partial — pred is substring of gold: `Dr. Peter Unger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `Oleg Kreissl`(person)
- `Schoaderstraße 2, 3441 Freundorf, Österreich`(address)
- `Mercuria Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anna Radschek` — partial — pred is substring of gold: `Dr. Anna Radschek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Rudolf Schlohsmacher`(person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich`(address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich`(address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Wolfgang Aigner` — partial — pred is substring of gold: `Dr. Wolfgang Aigner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Aigner`(person)
- `KzlR Adalbert Bürks`(person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Fabienne Siewek` — partial — pred is substring of gold: `Dr.in Fabienne Siewek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Mag.a Reneé Kobayashi, Weinbaugebiet Losling 9, 4880 Aich, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `Elisabeth Traxler` — partial — pred is substring of gold: `Mag. Elisabeth Traxler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Elisabeth Traxler`(person)
- `Mag.a Reneé Kobayashi`(person)
- `Weinbaugebiet Losling 9, 4880 Aich, Österreich`(address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Susanne Haim` — partial — pred is substring of gold: `Mag. Susanne Haim`

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

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `Marco Laudacher` — partial — pred is substring of gold: `Mag. Marco Laudacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Mehmet Faidt, Flitsch 4, 4822 Kogl, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Manuela Fischer` — partial — pred is substring of gold: `Mag. Manuela Fischer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Mehmet Faidt`(person)
- `Flitsch 4, 4822 Kogl, Österreich`(address)
- `Mag. Wolfgang Freudelsperger`(person)
- `Finanzamtes Wien 1/23`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Astrid Rüstmann` — partial — pred is substring of gold: `Dr.in Astrid Rüstmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Astrid Rüstmann`(person)
- `Sandro Flunger`(person)
- `Rohrer Straße 29, 3231 Kainratsdorf, Österreich`(address)
- `Mag. Hermann Rupert Zittmayr`(person)
- `FA Klagenfurt St. Veit Wolfsberg`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Florentin Blissenbach, Gotschmanninstraße 11, 9170 Seidolach, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  03-281/0693  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Anna Radschek` — partial — pred is substring of gold: `Dr. Anna Radschek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Florentin Blissenbach`(person)
- `Gotschmanninstraße 11, 9170 Seidolach, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `03-281/0693`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `Marco Laudacher` — partial — pred is substring of gold: `Mag. Marco Laudacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der BergLuftfahrt, KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dieter Fröhlich` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `BergLuftfahrt`(organisation)
- `KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich`(address)
- `Westra  GmbH Steuerberatungsgesellschaft`(organisation)
- `BMF`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Huberta Nothofer`(person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

**False Positives:**

- `Walter Summersberger` — partial — pred is substring of gold: `Dr. Walter Summersberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Walter Summersberger`(person)
- `Florenzia Rutt`(person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich`(address)
- `Zollamtes Feldkirch Wolfurt`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Vivian Malek, Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Manuela Fischer` — partial — pred is substring of gold: `Mag. Manuela Fischer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Vivian Malek`(person)
- `Korbergasse 7, 8563 Krottendorf bei Ligist, Österreich`(address)
- `Mag. Walter Dienstl & Partner  KG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  Tanja Wescher, Margaretenplatz 55, 3170 Gerstbach, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 07-638/8400  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

**False Positives:**

- `Ralf Schatzl` — partial — pred is substring of gold: `Dr. Ralf Schatzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `Tanja Wescher`(person)
- `Margaretenplatz 55, 3170 Gerstbach, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `07-638/8400`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

**False Positives:**

- `Klara Willumelies` — partial — pred is substring of gold: `Dr.in Klara Willumelies`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Klara Willumelies`(person)
- `Dorfcongart-Event`(organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich`(address)
- `Finanzamtes  Neunkirchen Wr. Neustadt`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über den Antrag der  Valentin Heinicke, Hofstätt 196, 3970 Sulz, Österreich, vertreten durch BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, QBC 4 – Am Belvedere 4, 1100 Wien, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer  für das Jahr 2014 erhobenen ordentlichen Revision vom 24. Juni 2020 die aufschiebende  Wirkung zuzuerkennen, beschlossen:  Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Renate Schohaj` — partial — pred is substring of gold: `Mag. Renate Schohaj`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Renate Schohaj`(person)
- `Valentin Heinicke`(person)
- `Hofstätt 196, 3970 Sulz, Österreich`(address)
- `BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Viktoria Blaser` — partial — pred is substring of gold: `Dr. Viktoria Blaser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Stephan Antonewitz`(person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Sahin, Fischmarkt 627, 4153 Vorderschiffl, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

**False Positives:**

- `Helga Hochrieser` — partial — pred is substring of gold: `Mag. Helga Hochrieser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Dimitri Sahin`(person)
- `Fischmarkt 627, 4153 Vorderschiffl, Österreich`(address)
- `LMG  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Baden Mödling`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

**False Positives:**

- `Helga Hochrieser` — partial — pred is substring of gold: `Mag. Helga Hochrieser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Felizitas Philippov`(person)
- `Hauser 155, 9422 Aich, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Hademar Berking, Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Helga Hochrieser` — partial — pred is substring of gold: `Mag. Helga Hochrieser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Hademar Berking`(person)
- `Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich`(address)
- `Mag. Margot Artner`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Björn Hüpscher` — partial — pred is substring of gold: `Dr. Björn Hüpscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Björn Hüpscher`(person)
- `Igor Strunz`(person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich`(address)
- `Vedat Gökdemir`(person)
- `Finanzamtes`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Techn R HR Martina Pisterer`(person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Christine Schweinfort  über den Antrag der Kira Ballis, BEd,  Josefiwaldweg 48, 3071 Diemannsberg, Österreich, auf Gewährung der Verfahrenshilfe im Beschwerdeverfahren gegen den  Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020  betreffend Abweisung des Rückzahlungsantrages, Steuernummer 24-406/6946  beschlossen:  I. Der Antrag auf Gewährung der Verfahrenshilfe wird als unbegründet abgewiesen.

**False Positives:**

- `Christine Schweinfort` — partial — pred is substring of gold: `Mag.a Christine Schweinfort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Christine Schweinfort`(person)
- `Kira Ballis, BEd`(person)
- `Josefiwaldweg 48, 3071 Diemannsberg, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `24-406/6946`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

**False Positives:**

- `Hans Blasina` — partial — pred is substring of gold: `Dr. Hans Blasina`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Annette Reeners`(person)
- `Räuflach 3, 8731 Schattenberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130620.1_1`)


BESCHLUSS   Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über den  Vorlageantrag vom 19. Dezember 2018 des Beschwerdeführers Diethard Uphof, Unterrotte 8, 3061 Unterwolfsbach, Österreich,  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten, 3100 St. Pölten, Daniel Gran-Straße 8,  vom 4. Mai 2018 betreffend Umsatzsteuer 2016:    I)

**False Positives:**

- `Günter Narat` — partial — pred is substring of gold: `Mag. Günter Narat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Diethard Uphof`(person)
- `Unterrotte 8, 3061 Unterwolfsbach, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

**False Positives:**

- `Alfred Klaming` — partial — pred is substring of gold: `Dr. Alfred Klaming`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alfred Klaming`(person)
- `Calvin Gorol`(person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich`(address)
- `Helmut Binder`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Klarissa Aßmus, Strombad Rustenweg 4, 3452 Trasdorf, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 52-573/0809  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Michael Mandlmayr` — partial — pred is substring of gold: `Dr. Michael Mandlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Michael Mandlmayr`(person)
- `Klarissa Aßmus`(person)
- `Strombad Rustenweg 4, 3452 Trasdorf, Österreich`(address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `52-573/0809`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

**False Positives:**

- `Judith Leodolter` — partial — pred is substring of gold: `Dr. Judith Leodolter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Judith Leodolter`(person)
- `Franziskus Lex`(person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Irene Kohler` — partial — pred is substring of gold: `Mag. Irene Kohler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Irene Kohler`(person)
- `Dipl.-Ing. Erwin Göktan`(person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gerhard Groschedl` — partial — pred is substring of gold: `Mag. Gerhard Groschedl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Valentina Heumeyer  in der Beschwerdesache Emanuela Schöchl,  J. Schemmerl-Gasse 7, 4906 Felling, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

**False Positives:**

- `Valentina Heumeyer` — partial — pred is substring of gold: `Dr.in Valentina Heumeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Valentina Heumeyer`(person)
- `Emanuela Schöchl`(person)
- `J. Schemmerl-Gasse 7, 4906 Felling, Österreich`(address)
- `Anton Hörmann`(person)
- `Finanzamtes`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Alessia Olschofski` — partial — pred is substring of gold: `Dr.in Alessia Olschofski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alessia Olschofski`(person)
- `Natalie Gosebrink, Bakk. phil.`(person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich`(address)
- `Finanzamtes für  Gebühren`(organisation)
- `50-818/5472`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Peter Unger` — partial — pred is substring of gold: `Dr. Peter Unger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `HR Frederik Kleinmichel, MA`(person)
- `Haniflgasse 12, 4725 Stadl, Österreich`(address)
- `Astoria Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Stefan Pipal` — partial — pred is substring of gold: `Mag. Stefan Pipal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Stefan Pipal`(person)
- `Dipl. Kff. Cäcilia Wlcek`(person)
- `Rambergweg 3, 4950 Weidenthal, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Astrid Binder` — partial — pred is substring of gold: `Dr. Astrid Binder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Astrid Binder`(person)
- `Valerie Süssmeier`(person)
- `Ögglweg 86, 8623 Tutschach, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Jeffrey Wengschick` — partial — pred is substring of gold: `Dr. Jeffrey Wengschick`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Jeffrey Wengschick`(person)
- `Donald Hayder, MA`(person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Georgette Dörger  in der Beschwerdesache der  Roland Wüstemeier, Sebastianplatz 167, 3420 Klosterneuburg, Österreich, über die Beschwerde vom 4. November 2019 gegen die Bescheide  des FA Salzburg-Stadt  vom 30. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017 zur Steuernummer 99-999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Georgette Dörger` — partial — pred is substring of gold: `Mag.a Georgette Dörger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Georgette Dörger`(person)
- `Roland Wüstemeier`(organisation)
- `Sebastianplatz 167, 3420 Klosterneuburg, Österreich`(address)
- `FA Salzburg-Stadt`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Valentin Kreuthmayr  in der Beschwerdesache Naomi Ruddis, LLB,  Schuselkagasse 21, 9570 Alt-Ossiach, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 10. März 2020 betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für sich selbst ab Jänner 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valentin Kreuthmayr` — partial — pred is substring of gold: `Mag. Valentin Kreuthmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Valentin Kreuthmayr`(person)
- `Naomi Ruddis, LLB`(person)
- `Schuselkagasse 21, 9570 Alt-Ossiach, Österreich`(address)
- `Finanzamt Niederösterreich Mitte`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Peter Bilger` — partial — pred is substring of gold: `Mag. Peter Bilger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `Holger Weiskittel`(person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Theophil Schachenmeier, Gsteinert 21, 4115 Steining, Österreich, betreffend die Beschwerde vom 03.04.2020 gegen den Bescheid  des Finanzamtes Freistadt Rohrbach Urfahr vom 26.03.2020 über die Einstellung der  Vollstreckung zu Steuernummer 63-906/4998  beschlossen:   Die Beschwerde wird gem. § 260 Abs. 1 lit. a) BAO zurückgewiesen.

**False Positives:**

- `Norbert Zöls` — partial — pred is substring of gold: `Dr. Norbert Zöls`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Norbert Zöls`(person)
- `Theophil Schachenmeier`(person)
- `Gsteinert 21, 4115 Steining, Österreich`(address)
- `Finanzamtes`(organisation)
- `63-906/4998`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Proidl über die Beschwerde der  Istvan  Sicking, Fanny Elßler-Gasse 30, 9375 Zosen, Österreich, vom 09. Oktober 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 28. September 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in  der Fassung LGBl. für Wien Nr. 24/2012, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als der  Spruch des bekämpften Straferkenntnisses insoweit abgeändert wird, als die Geldstrafe von  Euro 60,00 auf Euro 36,00 und die Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden  herabgesetzt wird.

**False Positives:**

- `Andrea Proidl` — partial — pred is substring of gold: `Mag. Andrea Proidl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Proidl`(person)
- `Istvan  Sicking`(person)
- `Fanny Elßler-Gasse 30, 9375 Zosen, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt  Wien`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Josef Zwilling` — partial — pred is substring of gold: `Mag. Josef Zwilling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Zwilling`(person)
- `Tiffany Kleiß`(person)
- `Endergasse 74, 5411 Vorderwiestal, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `79-412/0834`(tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Wilmerdinger  in der Beschwerdesache Kirsten Constantinescu,  Höhenwald 50, 4822 Primesberg, Österreich, über die Beschwerde vom 28. August 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 26. August 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 41-83-382/2498  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Delia Wilmerdinger` — partial — pred is substring of gold: `Mag.a Delia Wilmerdinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Delia Wilmerdinger`(person)
- `Kirsten Constantinescu`(person)
- `Höhenwald 50, 4822 Primesberg, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `41-83-382/2498`(tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `Norbert Zöls` — partial — pred is substring of gold: `Dr. Norbert Zöls`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Norbert Zöls`(person)
- `Wendy Schärff`(person)
- `Krainberg 12, 4633 Weilbach, Österreich`(address)
- `LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater`(organisation)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Dipl.-Ing. Waldemar Zumloh, Oberdorfer Weg 40, 4682 Brunau, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 09-591/1655  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Michael Mandlmayr` — partial — pred is substring of gold: `Dr. Michael Mandlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Michael Mandlmayr`(person)
- `Dipl.-Ing. Waldemar Zumloh`(person)
- `Oberdorfer Weg 40, 4682 Brunau, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `09-591/1655`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Ruprecht Kalmes, Freistabl 34, 9400 Gries, Österreich, über die Beschwerde vom 5. Februar 2020 gegen die  Bescheide des Finanzamtes Lilienfeld St. Pölten vom 4. November 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, Steuernummer  03-702/3005, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Wolfgang Freilinger` — partial — pred is substring of gold: `Dr. Wolfgang Freilinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `KzlR Ruprecht Kalmes`(person)
- `Freistabl 34, 9400 Gries, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `03-702/3005`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck in der Beschwerdesache  Thobias Dommert, Hainfelder Straße 56, 4846 Gewerbepark West, Österreich, vertreten durch LBG Niederösterreich Steuerberatung GmbH, Wie- ner Straße 2, 2640 Gloggnitz, über die Beschwerden vom 29. Dezember 2017 und 31. Jänner  2018 gegen die Bescheide des Finanzamtes Neunkirchen Wiener Neustadt vom 6. Dezember  2017 und 10. Jänner 2018 betreffend Einkommensteuer 2007 bis 2011, St.Nr. 33- 66-847/2354, zu Recht erkannt:    Der Beschwerde gegen den Einkommensteuerbescheid 2007 wird teilweise Folge gegeben.

**False Positives:**

- `Johannes Böck` — partial — pred is substring of gold: `Mag. Johannes Böck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johannes Böck`(person)
- `Thobias Dommert`(person)
- `Hainfelder Straße 56, 4846 Gewerbepark West, Österreich`(address)
- `LBG Niederösterreich Steuerberatung GmbH`(organisation)
- `Finanzamtes Neunkirchen Wiener Neustadt`(organisation)
- `66-847/2354`(tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Marion Weißhar, Magnusplatz 23, 9555 Glantscha, Österreich, vom 20. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 8. Jänner 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis mit der Maßgabe bestätigt, dass der Kostenbeitrag für das  behördliche Strafverfahren gemäß § 64 Abs. 2 VStG nicht 10,00 €, sondern 14,00 € beträgt.

**False Positives:**

- `Judith Leodolter` — partial — pred is substring of gold: `Dr. Judith Leodolter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Judith Leodolter`(person)
- `Marion Weißhar`(person)
- `Magnusplatz 23, 9555 Glantscha, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Gudrun Breunlein, Am Rintl 6, 5324 Faistenau, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 75-682/2104  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hans Blasina` — partial — pred is substring of gold: `Dr. Hans Blasina`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Gudrun Breunlein`(person)
- `Am Rintl 6, 5324 Faistenau, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `75-682/2104`(tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Alice Rainprechter` — partial — pred is substring of gold: `Mag.a Alice Rainprechter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Alice Rainprechter`(person)
- `Ing. Techn R Arthur Kornhass`(person)
- `Gstaudet 21, 9556 Besendorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Sandro Fischlein, Hans-Schilder-Platz 17, 9065 Untermieger, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Sandro Fischlein`(person)
- `Hans-Schilder-Platz 17, 9065 Untermieger, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache RgR OMedR Miklos Pellegrin, Ostendeweg 9, 9981 Glor-Berg, Österreich, über die Beschwerde vom 20.1.2017 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 20.12.2016 betreffend Wiederaufnahme §  303 BAO /  USt 2008, Steuernummer 73-541/6746, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ansgar Unterberger` — partial — pred is substring of gold: `Dr. Ansgar Unterberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `RgR OMedR Miklos Pellegrin`(person)
- `Ostendeweg 9, 9981 Glor-Berg, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `73-541/6746`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Veit Vissers, Wander Bertoni-Straße 166, 5223 Fludau, Österreich, über die Beschwerde vom 10. September 2019 gegen den  Bescheid des Finanzamtes Österreich vom 13. August 2019 betreffend Abweisung eines  Antrages auf Wiederaufnahme § 303 BAO /  ESt 2017 Steuernummer 94-198/2586  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Susanne Haim` — partial — pred is substring of gold: `Mag. Susanne Haim`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `Veit Vissers`(person)
- `Wander Bertoni-Straße 166, 5223 Fludau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `94-198/2586`(tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132342.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132342.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Rechtsmittelsache Olaf Vasiliadis, Weingartsberg 5, 9065 Niederdorf, Österreich, über die Vorlageanträge vom 21.12.2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 und Einkommensteuer  (Arbeitnehmerveranlagung) 2017, Steuernummer 03 13-336/4289  beschlossen:  Der Vorlageantrag vom 21.12.2020 betreffend Einkommensteuer 2015 wird gemäß § 264  Abs. 5 zweiter Fall BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Christian Seywald` — partial — pred is substring of gold: `Mag. Christian Seywald`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Olaf Vasiliadis`(person)
- `Weingartsberg 5, 9065 Niederdorf, Österreich`(address)
- `13-336/4289`(tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Malik Stellmaszick, Am Weberbach 26, 9640 Gailberg, Österreich, über die Beschwerde vom 19. November 2012 gegen den Bescheid  des FA Wien 1/23 vom 8. November 2012 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2011, Steuernummer 92-110/0462  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Monika Kofler` — partial — pred is substring of gold: `Dr. Monika Kofler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Monika Kofler`(person)
- `Malik Stellmaszick`(person)
- `Am Weberbach 26, 9640 Gailberg, Österreich`(address)
- `FA Wien 1/23`(organisation)
- `92-110/0462`(tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

**False Positives:**

- `Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eugenia Vesen`(person)
- `Apollogasse 213, 5522 Lammertal, Österreich`(address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132430.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132430.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 9. April 2020 des Beschwerdeführers Julian Büsges, Schleifmühle 12, 8530 Freiland bei Deutschlandsberg, Österreich  gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 3. April 2020 betreffend Einkommensteuer 2019 zu  Recht:     I)

**False Positives:**

- `Günter Narat` — partial — pred is substring of gold: `Mag. Günter Narat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Julian Büsges`(person)
- `Schleifmühle 12, 8530 Freiland bei Deutschlandsberg, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer in der Beschwerdesache  Silvius Fingermann, Steibstraße 113, 5723 Litzldorf, Österreich, über die Beschwerde vom 3. Mai 2018 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 5. April 2018 betreffend Anspruchszinsen (§ 205 BAO) 2013,  Steuernummer 91-977/4633, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Diana Sammer` — partial — pred is substring of gold: `Mag. Diana Sammer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `Silvius Fingermann`(person)
- `Steibstraße 113, 5723 Litzldorf, Österreich`(address)
- `Finanzamtes Wien 4/5/10`(organisation)
- `91-977/4633`(tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Univ.-Prof.in StR Caroline Akkoca, MBA, Hinterbachstraße 8, 4653 Spieldorf, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2021 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Jänner 2021, Zahl: MA67/206700566984/2020, mit  dem der Einspruch vom 10. November 2020 gegen die Strafverfügung vom 8. Oktober 2020 mit  derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Robert Pernegger` — partial — pred is substring of gold: `Mag. Robert Pernegger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)
- `Hinterbachstraße 8, 4653 Spieldorf, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde von Sebastian Claasen, Schloß Stainach 146, 4844 Lahn, Österreich, vom 9. März 2021, gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 67, vom 23. Februar 2021, Zahl  MA67/Zahl1/2018, wegen Verspätung zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Andrea Müller` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Sebastian Claasen`(person)
- `Schloß Stainach 146, 4844 Lahn, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Franka Hilgenstock, Bockackerstraße 19, 4892 Sieberer, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Albert Salzmann` — partial — pred is substring of gold: `Mag. Albert Salzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Franka Hilgenstock`(person)
- `Bockackerstraße 19, 4892 Sieberer, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/132731.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132731.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat über die Beschwerde vom  11. September 2020 des Beschwerdeführers Leila Höflein, Äussere Vorachstraße 25, 4081 Deinham, Österreich, vertreten durch die  Dr. Heinz Häupl Rechtsanwalts GmbH, 4865 Nußdorf, Stockwinkl 18, gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 10. August 2020  betreffend Abweisung des Antrages vom 24.07.2020 auf Aufhebung der  Umsatzsteuerbescheide 2011 und 2013 sowie der Einkommensteuerbescheide 2010, 2011  und 2013 gemäß § 299 Abs 1 BAO den Beschluss:      I)

**False Positives:**

- `Günter Narat` — partial — pred is substring of gold: `Mag. Günter Narat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Leila Höflein`(person)
- `Äussere Vorachstraße 25, 4081 Deinham, Österreich`(address)
- `Dr. Heinz Häupl Rechtsanwalts GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rocco Girstenbrei, Waubergweg 6, 9710 Pöllan, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Rocco Girstenbrei`(person)
- `Waubergweg 6, 9710 Pöllan, Österreich`(address)
- `Dr. Maria Brandstetter`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Jennifer Kuntzemann, MSc Bakk. iur., Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich, über die Beschwerde vom 11. April 2020 gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 11. März 2020 betreffend  Rückzahlung ausbezahlter Zuschüsse zum Kinderbetreuungsgeld für das Jahr 2014,  Steuernummer StrNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Monika Kofler` — partial — pred is substring of gold: `Dr. Monika Kofler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Monika Kofler`(person)
- `Jennifer Kuntzemann, MSc Bakk. iur.`(person)
- `Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich`(address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Helga Zeißig, Im Markt 12, 5733 Bramberg am Wildkogel, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

**False Positives:**

- `Peter Steurer` — partial — pred is substring of gold: `Dr. Peter Steurer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Helga Zeißig`(person)
- `Im Markt 12, 5733 Bramberg am Wildkogel, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/132990.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Veronika Richerd  in der Beschwerdesache des  Priv.-Doz.in Felizia Claus, Mosenthalweg 10, 4076 Holzwiesen, Österreich  vertreten durch StB über die Beschwerde vom 11. Dezember 2019  gegen die Bescheide des Finanzamtes vom 18. November 2019 betreffend Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2009 und Einkommensteuer 2009 zu Recht  erkannt:     I. Der Beschwerde gegen den Bescheid betreffend Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2009 wird Folge gegeben.

**False Positives:**

- `Veronika Richerd` — partial — pred is substring of gold: `Mag.a Veronika Richerd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Veronika Richerd`(person)
- `Priv.-Doz.in Felizia Claus`(person)
- `Mosenthalweg 10, 4076 Holzwiesen, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Daniela Weickhart  in der Beschwerdesache Cäcilia Lüderitz,  Zallingergasse 21, 9372 St. Walburgen, Österreich, über die Beschwerde vom 2. Jänner 2020 gegen den Abweisungsbescheid des  Finanzamtes Bruck Leoben Mürzzuschlag vom 4. Dezember 2019 betreffend Familienbeihilfe  für sich selbst ab November 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Daniela Weickhart` — partial — pred is substring of gold: `Dr.in Daniela Weickhart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Daniela Weickhart`(person)
- `Cäcilia Lüderitz`(person)
- `Zallingergasse 21, 9372 St. Walburgen, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/133037.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133037.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Marcel Tummernicht, Gesern 3, 9433 Kienberg, Österreich, über die Beschwerde vom 9. November 2017  gegen den Bescheid des Finanzamtes Österreich vom 19. Oktober 2017 betreffend Haftung für  Kapitalertragsteuer für die Jahre 2009 bis 2012, Steuernummer 30-367/8113, zu Recht  erkannt:   Der Beschwerde betreffend Haftung für Kapitalertragsteuer 2009 wird Folge gegeben.

**False Positives:**

- `Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Marcel Tummernicht`(person)
- `Gesern 3, 9433 Kienberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `30-367/8113`(tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/133114.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133114.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Heinz Clee, Am Seeweg 250, 4284 Schmierreith, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 8.1.2020  gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich)  betreffend  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2013 vom 12.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2014 vom 13.12.2019  - Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2015 vom 13.12.2019  zu Recht erkannt:   I. Soweit sich die Beschwerden vom 8.1.2020 gegen die Bescheide über die  Wiederaufnahme der Verfahren betreffend Einkommensteuer 2013, 2014 und 2015  richten, wird diesen gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Albert Salzmann` — partial — pred is substring of gold: `Mag. Albert Salzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Heinz Clee`(person)
- `Am Seeweg 250, 4284 Schmierreith, Österreich`(address)
- `Pallauf Meißnitzer Staindl & Partner`(organisation)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Evamaria Moucha  in der   Beschwerdesache Ing. Techn R Emma Kirmiss, Balikostraße 6, 4072 Winkeln, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Evamaria Moucha` — partial — pred is substring of gold: `Dr.in Evamaria Moucha`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Evamaria Moucha`(person)
- `Ing. Techn R Emma Kirmiss`(person)
- `Balikostraße 6, 4072 Winkeln, Österreich`(address)
- `Dr. Michael Jöstl`(person)
- `Finanzamtes für Gebühren`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/133172.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Scarlett Beverungen, Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 71-240/3156  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Karin Pitzer` — partial — pred is substring of gold: `Mag. Karin Pitzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Scarlett Beverungen`(person)
- `Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich`(address)
- `Uniconsult Steuerberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Braunau Ried`(organisation)
- `71-240/3156`(tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/133179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133179.1_2`)


Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Verein Annkathrin Cattus, vertreten durch AUDITREU Steuerberatungsgesellschaft  m.b.H., Gonzagagasse 17, 1010 Wien, über die Beschwerde vom 24. Februar 2021 gegen die  Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 17. Juli 2020  betreffend  - Umsatzsteuer für die Jahre 2012 bis 2016 sowie  - Wiederaufnahme betreffend Umsatzsteuer für die Jahre 2012 bis 2016  zu Recht:  I. Der Beschwerde gegen die Wiederaufnahmsbescheide betreffend Umsatzsteuer 2012 bis  2016 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Gerald Erwin Ehgartner` — partial — pred is substring of gold: `MMag. Gerald Erwin Ehgartner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Gerald Erwin Ehgartner`(person)
- `Annkathrin Cattus`(person)
- `AUDITREU Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Torsten Schattner, Stögersbach 35, 7031 Krensdorf, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 21. September 2017  betreffend Abweisung eines  Antrages auf Aufhebung des Einkommensteuerbescheides 2016 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Peter Steurer` — partial — pred is substring of gold: `Dr. Peter Steurer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Torsten Schattner`(person)
- `Stögersbach 35, 7031 Krensdorf, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Dalibor Kochendörfer, Max-Opravil-Hof 3 - 7, 8051 Graz, Österreich, über die Beschwerde vom 16. Oktober 2020 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 16. September 2020  betreffend Wiederaufnahme des Verfahrens hinsichtlich des Antrages auf Familienbeihilfe vom  22. Juli 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Dalibor Kochendörfer`(person)
- `Max-Opravil-Hof 3 - 7, 8051 Graz, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Hermann Bloehdorn, Bierbaum 35, 8983 Bad Mitterndorf, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerden vom 9. und 13. Jänner 2014 sowie vom 25. September 2015 und vom 20.  Oktober 2017 gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt  Österreich) vom 6. Dezember 2013, sowie vom 26. August 2015 und vom 11. September 2017  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 bis 2014, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Hermann Bloehdorn`(person)
- `Bierbaum 35, 8983 Bad Mitterndorf, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/133297.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133297.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Anton Lauscheck, Kesselstraße 10, 9551 Unterberg, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 10. Februar 2017 betreffend Einkommensteuer 2015 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Peter Steurer` — partial — pred is substring of gold: `Dr. Peter Steurer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Anton Lauscheck`(person)
- `Kesselstraße 10, 9551 Unterberg, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Christian Jovanovic, BA, Himmelsstiege 8, 4521 Matzelsdorf, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Peter Steurer` — partial — pred is substring of gold: `Dr. Peter Steurer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Christian Jovanovic, BA`(person)
- `Himmelsstiege 8, 4521 Matzelsdorf, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/133392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133392.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ruperta Ekonomou  in der Beschwerdesache Erhard Sennewaldt,  Taubenwaldweg 24, 3232 Unterschildbach, Österreich, betreffend Beschwerde vom 29. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuervorauszahlungen  2021 Steuernummer 21-935/5536  beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 5 BAO iVm § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Ruperta Ekonomou` — partial — pred is substring of gold: `Dr.in Ruperta Ekonomou`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Ruperta Ekonomou`(person)
- `Erhard Sennewaldt`(person)
- `Taubenwaldweg 24, 3232 Unterschildbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `21-935/5536`(tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/133404.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. Juni 2020 des Beschwerdeführers Edgar Soutschek, Am Klosterbruch 21, 3661 Hart, Österreich  gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 26. Mai 2020  hinsichtlich Einkommensteuer 2019 vom 3. April 2020 zu Recht:    I)  Der Einkommensteuerbescheid 2019 wird abgeändert.

**False Positives:**

- `Günter Narat` — partial — pred is substring of gold: `Mag. Günter Narat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Edgar Soutschek`(person)
- `Am Klosterbruch 21, 3661 Hart, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Wolfgang Orosz, Tenoplatz 5, 8524 Hohenfeld, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 45-492/4197  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gabriele Krafft` — partial — pred is substring of gold: `Dr. Gabriele Krafft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Krafft`(person)
- `Wolfgang Orosz`(person)
- `Tenoplatz 5, 8524 Hohenfeld, Österreich`(address)
- `Commendatio Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `45-492/4197`(tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/133447.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133447.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Philipp Harazin  in der Beschwerdesache Priv.-Doz. Kevin Morzinsky,  Strußnighof 37, 9631 Kleinbergl, Österreich, über die Beschwerde vom 15. Jänner 2015 gegen die Bescheides des  Finanzamtes Wien 12/13/14 Purkersdorf (nunmehr: FA Bruck Eisenstadt Oberwart), jeweils  vom 11. Dezember  2014 betreffend    Säumniszuschlag im Zusammenhang mit Lohnsteuer 2007;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2007;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2008;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2008;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2009;   Säumniszuschlag im Zusammenhang mit Dienstgeberbeitrag 2009;   Säumniszuschlag im Zusammenhang mit Lohnsteuer 2010,  jeweils zur Steuernummer 58-060/5953  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Philipp Harazin` — partial — pred is substring of gold: `Dr. Philipp Harazin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Philipp Harazin`(person)
- `Priv.-Doz. Kevin Morzinsky`(person)
- `Strußnighof 37, 9631 Kleinbergl, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `FA Bruck Eisenstadt Oberwart`(organisation)
- `58-060/5953`(tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eleonore Rudloph, Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauerstrasse 39/1/12, 1220 Wien, und Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden je vom  25.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 26. Juli 2016  betreffend Haftung für Abzugsteuer gemäß § 99 EStG 1988 für die Jahre 2012-2014 nach  Durchführung einer öffentlichen mündlichen Verhandlung am 26.04.2021 zu Recht erkannt:   I. a.

**False Positives:**

- `Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Rudloph`(person)
- `Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/133773.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133773.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Reinhold Optenhoevel, Heinrich von Schullernweg 4, 9710 Feffernitz, Österreich, vertreten durch Mag. Wolfgang Standfest,  Wallnerstraße 4 / 2.Hof / Top 44, 1010 Wien, über die Beschwerde vom 26.2.2016, soweit sie  gegen den Körperschaftsteuerbescheid 2011 des Finanzamtes Baden Mödling vom 23. Oktober  2015 zu Steuernummer 69-995/7038  gerichtet ist, beschlossen:  Die Beschwerde vom 26.2.2016 gilt – soweit sie gegen den Körperschaftsteuerbescheid 2011  vom 23. Oktober 2015 gerichtet ist – gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als  zurückgenommen.

**False Positives:**

- `Christian Seywald` — partial — pred is substring of gold: `Mag. Christian Seywald`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Reinhold Optenhoevel`(person)
- `Heinrich von Schullernweg 4, 9710 Feffernitz, Österreich`(address)
- `Mag. Wolfgang Standfest`(person)
- `Finanzamtes Baden Mödling`(organisation)
- `69-995/7038`(tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/133823.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Friedhelm Wandel, Falkenburg, Schulgasse 8, 4364 Thomasreit, Österreich, über die Beschwerde vom 30. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 3. Oktober 2019 betreffend Familienbeihilfe ab  September 2019 zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Friedhelm Wandel`(person)
- `Falkenburg, Schulgasse 8, 4364 Thomasreit, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/133856.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133856.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Dipl.-Ing. Justin Maierhöfer, Direktor Lukas-Weg 5, 4820 Kreutern, Österreich, über die Beschwerde vom 24. Dezember 2019  gegen den Bescheid des Finanzamtes für Gebühren Verkehrsteuern und Glücksspiel vom  22. November 2019, Steuernummer 61-942/0225, betreffend Grunderwerbsteuer 2019 zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Daniel Philip Pfau` — partial — pred is substring of gold: `Mag. Daniel Philip Pfau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniel Philip Pfau`(person)
- `Dipl.-Ing. Justin Maierhöfer`(person)
- `Direktor Lukas-Weg 5, 4820 Kreutern, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `61-942/0225`(tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/133998.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133998.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Imre Wittek  über die Beschwerde des Lara Schwertzel,  Stockinger Straße 23, 4892 Schwandeck, Österreich, vertreten durch Mag. Ingrid Huber, Feldweg 7, 9241 Wernberg, vom  02.01.2017 gegen den Bescheid des Finanzamtes St. Veit Wolfsberg (nunmehr FA Österreich),  dieses vertreten durch Ilse König BA MA, vom 17.03.2016 betreffend Einkommensteuer 2010  (ANV) im fortgesetzten Verfahren den Beschluss gefasst:   Der Vorlageantrag wird gemäß § 264 Abs. 4 lit e BAO iVm § 260 Abs. 1 BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Imre Wittek` — partial — pred is substring of gold: `Dr. Imre Wittek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Imre Wittek`(person)
- `Lara Schwertzel`(person)
- `Stockinger Straße 23, 4892 Schwandeck, Österreich`(address)
- `Mag. Ingrid Huber`(person)
- `Finanzamtes St. Veit Wolfsberg`(organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Siegfried Terentew, Hartergasse 375, 4772 Blindendorf, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Josef Zwilling` — partial — pred is substring of gold: `Mag. Josef Zwilling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Zwilling`(person)
- `Siegfried Terentew`(person)
- `Hartergasse 375, 4772 Blindendorf, Österreich`(address)

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin Dr. Michaela Schmutzer und die fachkundigen  Laienrichter L1 und L2 in der Finanzstrafsache gegen Frau Valerian Unterfranz, geb., Schanzplatz 130, 3664 Hundsbach, Österreich,  vertreten durch LBG Niederösterreich GmbH, Raiffeisenpromenade 2/1/6, 3830 Waidhofen an  der Thaya, wegen der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 1 und  Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde der Beschuldigten vom 9.  März 2020 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19  Klosterneuburg als Organ des Finanzamtes Waldviertel als Finanzstrafbehörde vom  21. November 2019, SpS 19, Strafnummer 23-2018, in Anwesenheit der Beschuldigten, ihres  Verteiigers, des Amtsbeauftragten HR AB sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Waldviertel als Finanzstrafbehörde zur Strafnummer 2018 gegen die  Beschuldigte geführte Finanzstrafverfahren wegen des Verdachts der Verkürzung von  Umsatzsteuer 2012 von € 860,00, Umsatzsteuer 2013 von € 860,00, Umsatzsteuer 2014 von €  860,00, Umsatzsteuer 2015 von € 860,00 bzw. Umsatzsteuer 2016 von € 433,33 und  Umsatzsteuervorauszahlungen 01-09/2017 von € 433,33 wird gemäß §§ 136, 157, 82 Abs. 3  lit. c FinStrG eingestellt.  Über Valerian Unterfranz  wird für die verbleibenden Finanzvergehen (bzw. strafbestimmenden  Werteträge) gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 7.944,00 verhängt.

**False Positives:**

- `Michaela Schmutzer` — partial — pred is substring of gold: `Dr. Michaela Schmutzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Dr. Michaela Schmutzer`(person)
- `Valerian Unterfranz`(person)
- `Schanzplatz 130, 3664 Hundsbach, Österreich`(address)
- `Finanzamt Wien 9/18/19`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamt Waldviertel`(organisation)
- `Valerian Unterfranz`(person)

</details>

---

## `single_initial_person` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ba721a93`  
**Description:**
Captures single initials (e.g., 'M.', 'E.') in specific contexts like 'Richter M.' or 'M. Lehner' to avoid false positives.

**Content:**
```
(?:^|\s|,|\(|\)|\[|\]|\.|\?|!|\n)(?:Richter|Richterin|Vorsitzender|Vorsitzende|Mag\.\s+|Dr\.\s+|Prof\.\s+|Univ\.-?Prof\.|Senatspr\u00e4sident|Vizepr\u00e4sident|Hofrat|Hofr\u00e4tin|Herr|Frau|von\s+|bei\s+|mit\s+|durch\s+|gegen\s+|f\u00fcr\s+|in\s+|aus\s+|zu\s+|nach\s+|vor\s+|unter\s+|\u00fcber\s+|auf\s+|ohne\s+|um\s+|seit\s+|bis\s+|ab\s+|wider\s+|neben\s+|zwischen\s+|entlang\s+|gegen\u00fcber\s+|statt\s+|au\u00dfer\s+|Sohn\s+|Kind\s+|Eltern\s+|Mutter\s+|Vater\s+|Bruder\s+|Schwester\s+|Onkel\s+|Tante\s+|Cousin\s+|Cousine\s+|Gro\u00dfvater\s+|Gro\u00dfmutter\s+|Enkel\s+|Enkelin\s+|Neffe\s+|Nichte\s+|Tante\s+|Onkel\s+|Urgro\u00dfvater\s+|Urgro\u00dfmutter\s+|Urenkel\s+|Urenkelin\s+|Gro\u00dfonkel\s+|Gro\u00dftante\s+|Gro\u00dfneffe\s+|Gro\u00dfnichte\s+|Gro\u00dfcousin\s+|Gro\u00dfcousine\s+|Gro\u00dfvater\s+|Gro\u00dfmutter\s+|Enkel\s+|Enkelin\s+|Neffe\s+|Nichte\s+|Tante\s+|Onkel\s+|Urgro\u00dfvater\s+|Urgro\u00dfmutter\s+|Urenkel\s+|Urenkelin\s+|Gro\u00dfonkel\s+|Gro\u00dftante\s+|Gro\u00dfneffe\s+|Gro\u00dfnichte\s+|Gro\u00dfcousin\s+|Gro\u00dfcousine\s+)([A-Z]\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 15 | 0 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 15 | 2210 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_130`)


Das polnische Kennzeichen, das in der Aufstellung ausgewiesen ist, betrifft folgendes Kfz  (polnischer Zulassungsschein):  Marke BMW, Type 320 D, Baujahr 2003, Erstzulassung April 2003  Erstzulassung von 01.04.2003 bis 04.01.2014 für S.N., polnische Anschrift  Hubraum 1.995 l, Kraftstoff Diesel, Motorleistung 110 kw  Die iHv € 3.672,00 geltend gemachten Kosten für Familienheimfahrten entsprechen dem  höchsten Pendlerpauschale-Betrag.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_29`)


Laut Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen (BASB  Landesstelle OÖ) über die Begutachtung am 22.1.2019, in dem ein Gesamtgrad der  Behinderung von 50 % bescheinigt wird, leidet der Beschwerdeführer an    (1) Posttraumatischer Sprunggelenksarthrose rechts bei Z.n. Sprungbeinfraktur,  beginnender Hüft- und Kniegelenksarthrose beidseits (Grad der Behinderung 40 %)   (2) Chronischer Lumbalgie bei degenerativer Wirbelsäulenerkrankung und Z.n.  Bandscheibenoperation L2/L3 (Grad der Behinderung 30 %)   (3) Koronarer Herzkrankheit, Angina pectoris Z.n. erfolgreicher Gefäßaufdehnung und  Stentimplantation (Grad der Behinderung 30 %).

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)
- `BASB  Landesstelle OÖ`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_41`)


Dr. X.Y.“  (BFG-Anm: Fertigung mit unleserlicher Unterschrift und Firmenstampiglie der Kirstin Frischbutter  Wirtschaftstreuhandgesellschaft m.b.H.(nachfolgend Mur-Sanitär GmbH.  In Erledigung dieser Beschwerde erging am 30.Nov.2020 zur Steuernummer (StNr.) der  M.-GmbH eine abweisende Beschwerdevorentscheidung (BVE) an Herrn M. (Direktzustellung  an Herrn M. mit geänderter Bescheidadresse;

**False Positives:**

- `X.` — partial — pred is substring of gold: `Dr. X.Y.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. X.Y.`(person)
- `Kirstin Frischbutter`(person)
- `Mur-Sanitär GmbH`(organisation)
- `M.`(person)
- `M.`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_32`)


Eine über die gesamten  Jahre erfolgte Betrachtung zeigt folgendes Bild der Ertragssituation:   Die Erträge lt. Jahresabschlüsse 2000 bis 2005 bei J.P. und Gattin:  Erlöse Bf. – J.P. 2000 - ATS 2003 - Euro 2004-

**False Positives:**

- `J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_41`)


Die Jahresabschlüsse 2006 bis 2009 bei J.P. und Gattin zeigen folgende Ertragssituation:   Erlöse Bf. – J.P. 2006 2007  2008 2009   Erlöse- Abwasserentsorgung.

**False Positives:**

- `J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_88`)


[Anm.: Geburtsdatum]   4.14 Termin der nächsten Kontrolle  [blank]   Das in der Folge erstellte Gutachten vom 4. Mai 2021 des Bundesamtes für Soziales und  Behindertenwesen, BASB Landesstelle NÖ trifft folgende Aussagen:   Sachverständigengutachten auf Grund der Aktenlage   nach der Einschätzungsverordnung (BGBl. II Nr. 261/2010)   Name: (Sohn des Bf.) … Geburtsdatum: …11.2005, wohnhaft in … Ungarn   Aktengutachten erstellt am: 04.05.2021   Name des Sachverständigen: Dr. G.H.   Fachgebiet: Allgemeinmedizin und Augenheilkunde   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Formular E407, gezeichnet von Dr.B.E.T. in Papa (Ungarn) am 17.3.2021:   15 Jahre, 4 Monate   85 kg, 187 cm   vollständige Selbständigkeit, keine Hilfestellungen erforderlich   Sehbehinderung ab 11/2005   Behandlung ab 06/2006   keine anderen Behinderungen   TH: Implantat für künstliche Linsen 31.9.2006;

**False Positives:**

- `G.` — partial — pred is substring of gold: `Dr. G.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesamtes für Soziales und  Behindertenwesen`(organisation)
- `Dr. G.H.`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_93`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: x ja   GdB liegt vor seit: [blank]   Begründung - GdB liegt rückwirkend vor: [blank]   x Dauerzustand   Gutachten erstellt am 04.05.2021 von Dr. G.H.

**False Positives:**

- `G.` — partial — pred is substring of gold: `Dr. G.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. G.H.`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_205`)


Das FA formuliert:  „Dazu legt die Abgabenbehörde als Anlage 3 eine Aufstellung der Bankkonten von I.S. als  Beweismittel vor.

**False Positives:**

- `I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_33`)


Der Bf ist Ehemann von B.M., der bis 2/2018 geschäftsführenden Mehrheitsgesellschafterin der  M-GmbH. Die weiteren Gesellschafter der M-GmbH waren ebenfalls Familienmitglieder.

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_9`)


"… Anamnese:  sei mit ca. 20 Jahren an schizophrener Psychose erkrankt, damals an Verfolgungswahn und  akustischen Halluzinationen gelitten, damals erste stationäre psychiatrische Behandlung,  insgesamt bisher vier oder fünf stationäre Behandlungen, zuletzt im Frühling 2022 bei Z.n.  Suizidversuch, ausgelöst durch mehrere Verlusterlebnisse;

**False Positives:**

- `Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/146327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146327.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf.) ist die geschäftsführende Gesellschafterin der Fytterer Handel GmbH  verheiratet mit B.B..

**False Positives:**

- `B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Fytterer Handel GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/146850.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146850.1_43`)


diese Einnahmen sind jedoch abzüglich der anteiligen  Betriebsausgaben als Einkünfte aus L.u.F. zu versteuern.

**False Positives:**

- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/146850.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146850.1_51`)


Dieser  Betrag wurde in der Steuererklärung von G. bei Ermittlung der Einkünfte aus L.u.F. für 2016  angegeben und als durch die Vollpauschalierung abgegolten behandelt.  Die Weitergabe der Nebenentschädigung an die Ehegattin ist nach Ansicht des Finanzamtes als  Einkommensverwendung durch den Verkäufer Raul Yel, Bakk. rer.

**False Positives:**

- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/146850.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146850.1_54`)


Der Zufluss selbst stellt  bei Raul Yel, Bakk. rer. nat. MSc  sonstige Einnahmen aus L.u.F. dar und ist bei Ermittlung der Einkünfte aus L.u.F.  in Ansatz zu bringen.

**False Positives:**

- `L.` — no gold match — likely missing annotation
- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Raul Yel, Bakk. rer. nat. MSc`(person)

</details>

---

</details>

---

