# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-29T06:28:50.824240

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-29_v3/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 0 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2517 |
| Validation documents | 630 |
| Test documents | 792 |
| Train sentences | 4815 |
| Validation sentences | 1344 |
| Test sentences | 88613 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | True |
| Critic Interval | 20 |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.9% |
| True Positives | 1340 |
| False Positives | 397 |
| False Negatives | 1115 |
| Total Gold Entities | 2455 |
| Micro Precision | 77.1% |
| Micro Recall | 54.6% |
| Micro F1 | 63.9% |
| Macro F1 | 63.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `German Legal Person (Context: In der Beschwerdesache)` | 27.2% | 91.0% | 16.0% | 431 | 392 | 39 |
| `German Legal Person (Titles)` | 46.7% | 74.9% | 34.0% | 1113 | 834 | 279 |
| `German Legal Person (Frau/Herr Context)` | 8.6% | 59.1% | 4.6% | 193 | 114 | 79 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `German Legal Person (Context: In der Beschwerdesache)` 🏆

**F1:** 0.272 | **Precision:** 0.910 | **Recall:** 0.160  

**Format:** `regex`  
**Rule ID:** `520f8603`  
**Description:**
Captures names following legal context phrases, ensuring the name is at least 2 words or contains a specific pattern to avoid abbreviations.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|in\s+der\s+Verwaltungsstrafsache|in\s+der\s+Finanzstrafsache|in\s+der\s+Beschwerde-\s+sache)\s+(?!(?:Dr\.|Mag\.|Rg\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|KommR|Techn\s+R|ÖkR|LL\.M\.|BSc|Dipl\.-Ing\.|PhD|MA|LLB|MSc|MBA|Bakk\.))([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.910 | 0.160 | 0.272 | 431 | 392 | 39 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 392 | 39 | 2061 |

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
- `Zollamtes Klagenfurt` (organisation)

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

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/133172.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133172.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Scarlett Beverungen, Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich, vertreten durch Uniconsult Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried, über die Beschwerde vom 18.6.2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 3. April 2015 betreffend Umsatzsteuer 2009 und  Umsatzsteuer 2010 Steuernummer 71-240/3156  beschlossen:  Die Beschwerde vom 18.6.2015 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO  als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Scarlett Beverungen` | `Scarlett Beverungen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Agrarstraße 50f, 6361 Hopfgarten-Markt, Österreich` (address)
- `Uniconsult Steuerberatungs GmbH & Co KG` (organisation)
- `Finanzamtes Braunau Ried` (organisation)
- `71-240/3156` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/133213.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Torsten Schattner, Stögersbach 35, 7031 Krensdorf, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 21. September 2017  betreffend Abweisung eines  Antrages auf Aufhebung des Einkommensteuerbescheides 2016 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Torsten Schattner` | `Torsten Schattner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Stögersbach 35, 7031 Krensdorf, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/133262.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133262.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Dalibor Kochendörfer, Max-Opravil-Hof 3 - 7, 8051 Graz, Österreich, über die Beschwerde vom 16. Oktober 2020 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 16. September 2020  betreffend Wiederaufnahme des Verfahrens hinsichtlich des Antrages auf Familienbeihilfe vom  22. Juli 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dalibor Kochendörfer` | `Dalibor Kochendörfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Max-Opravil-Hof 3 - 7, 8051 Graz, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Hermann Bloehdorn, Bierbaum 35, 8983 Bad Mitterndorf, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerden vom 9. und 13. Jänner 2014 sowie vom 25. September 2015 und vom 20.  Oktober 2017 gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt  Österreich) vom 6. Dezember 2013, sowie vom 26. August 2015 und vom 11. September 2017  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 bis 2014, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hermann Bloehdorn` | `Hermann Bloehdorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Bierbaum 35, 8983 Bad Mitterndorf, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/133292.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133292.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Matthew Czeschelsky  in der Beschwerdesache Lucia Kaffenberger,  Bachleite 6, 2276 Katzelsdorf, Österreich, vertreten durch Ernst & Young Steuerberatungs- gesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, gegen den Bescheid des Finanzamtes Wien 1/23 vom  8. Jänner 2019 betreffend Forschungsprämie § 108c EStG 1988 2015 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Lucia Kaffenberger` | `Lucia Kaffenberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Matthew Czeschelsky` (person)
- `Bachleite 6, 2276 Katzelsdorf, Österreich` (address)
- `Ernst & Young Steuerberatungs- gesellschaft m.b.H.` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/133297.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133297.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Anton Lauscheck, Kesselstraße 10, 9551 Unterberg, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Feldkirch  (nunmehr: Finanzamt Österreich) vom 10. Februar 2017 betreffend Einkommensteuer 2015 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Anton Lauscheck` | `Anton Lauscheck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Kesselstraße 10, 9551 Unterberg, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/133392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133392.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ruperta Ekonomou  in der Beschwerdesache Erhard Sennewaldt,  Taubenwaldweg 24, 3232 Unterschildbach, Österreich, betreffend Beschwerde vom 29. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuervorauszahlungen  2021 Steuernummer 21-935/5536  beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 5 BAO iVm § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Erhard Sennewaldt` | `Erhard Sennewaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Ruperta Ekonomou` (person)
- `Taubenwaldweg 24, 3232 Unterschildbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `21-935/5536` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Wolfgang Orosz, Tenoplatz 5, 8524 Hohenfeld, Österreich, vertreten durch Commendatio Wirtschaftstreuhand GmbH,  Hermanngasse 21/10, 1070 Wien, über die Beschwerde vom 14. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 18. März 2021 betreffend Einkommensteuer 2019  Steuernummer 45-492/4197  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wolfgang Orosz` | `Wolfgang Orosz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Krafft` (person)
- `Tenoplatz 5, 8524 Hohenfeld, Österreich` (address)
- `Commendatio Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `45-492/4197` (tax_number)

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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dominik Kuzu Bf` — partial — gold is substring of pred: `Dominik Kuzu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Niels Aleksejew`(person)
- `Dominik Kuzu`(person)
- `Finanzamt Spittal Villach`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Ulrich Nieklaus, LLM, Weiberfelderweg 11, 5151 Kleinberg, Österreich, über die Beschwerde vom 3. November 2015 gegen die Bescheide des Finanzamtes  Bruck Eisenstadt Oberwart vom 1. Oktober 2015 betreffend Wiederaufnahme § 303 BAO /  ESt  01.10.2015 betreffend Einkommensteuer für die Jahre 2012 und 2013, Steuernummer  41-460/8999  zu Recht erkannt: .  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ulrich Nieklaus` — partial — pred is substring of gold: `Ulrich Nieklaus, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrich Nieklaus, LLM`(person)
- `Weiberfelderweg 11, 5151 Kleinberg, Österreich`(address)
- `Finanzamtes  Bruck Eisenstadt Oberwart`(organisation)
- `41-460/8999`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133179.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133179.1_2`)


Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der  Beschwerdesache Verein Annkathrin Cattus, vertreten durch AUDITREU Steuerberatungsgesellschaft  m.b.H., Gonzagagasse 17, 1010 Wien, über die Beschwerde vom 24. Februar 2021 gegen die  Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 17. Juli 2020  betreffend  - Umsatzsteuer für die Jahre 2012 bis 2016 sowie  - Wiederaufnahme betreffend Umsatzsteuer für die Jahre 2012 bis 2016  zu Recht:  I. Der Beschwerde gegen die Wiederaufnahmsbescheide betreffend Umsatzsteuer 2012 bis  2016 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Verein Annkathrin Cattus` — partial — gold is substring of pred: `Annkathrin Cattus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Gerald Erwin Ehgartner`(person)
- `Annkathrin Cattus`(person)
- `AUDITREU Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Christian Jovanovic, BA, Himmelsstiege 8, 4521 Matzelsdorf, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 26. März 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Christian Jovanovic` — partial — pred is substring of gold: `Christian Jovanovic, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Christian Jovanovic, BA`(person)
- `Himmelsstiege 8, 4521 Matzelsdorf, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt Österreich`(organisation)

</details>

---

## `German Legal Person (Titles)` 🏆

**F1:** 0.467 | **Precision:** 0.749 | **Recall:** 0.340  

**Format:** `regex`  
**Rule ID:** `55c77a67`  
**Description:**
Matches academic/professional titles followed by a valid name, excluding cases where the title is followed by another title or abbreviation.

**Content:**
```
(?:Dr\.|Mag\.|Mag\.\s+Dr\.|Dr\.\s+Mag\.|Priv\.-Doz\.|Priv\.-Doz\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|PhD|OSR|VetR|KommR|Bakk\.\s+phil\.|LLB|BSc|Dipl\.-Ing\.|Dipl\.-Ing\.in|DDr\.|DDr\.in|Mag\.\s+MBA\s+MSc|Mag\.\s+MSc|Mag\.\s+MBA|Mag\.\s+in|Mag\.a|Dr\.in|Ing\.|RgR|ÖkR|Techn\s+R)\s+(?!(?:Dr\.|Mag\.|Rg\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|KommR|Techn\s+R|ÖkR|LL\.M\.|BSc|Dipl\.-Ing\.|PhD|MA|LLB|MSc|MBA|Bakk\.))([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.749 | 0.340 | 0.467 | 1113 | 834 | 279 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 834 | 279 | 1621 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hemma Bährs` | `Dr.in Hemma Bährs` |
| `Univ.-Prof.in Rachel Darnieder` | `Univ.-Prof.in Rachel Darnieder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128627.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marianne Liuni` | `Univ.-Prof.in Marianne Liuni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Luigi Wedekämper` (person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Huberta Nothofer` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florenzia Rutt` (person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich` (address)
- `Zollamtes Feldkirch Wolfurt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Dr.in Klara Willumelies` | `Dr.in Klara Willumelies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dorfcongart-Event` (organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Sellnow` | `Priv.-Doz. Eckard Sellnow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Rösl` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. August Eichelsbacher  in der Beschwerdesache VetR Diethard Oldenbüttel,  Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich, vertreten durch BOD Steuerberatungs-GmbH, Europastraße 5, 6322  Kirchbichl,, über die Beschwerde vom 16. Dezember 2016 gegen den Bescheid des FA Landeck Reutte  vom 21. November 2016 betreffendBerichtigung des Einkommensteuerbescheides 2010 vom  29. November 2011 gem. § 293b BAO erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. August Eichelsbacher` | `Hon.-Prof. August Eichelsbacher` |
| `VetR Diethard Oldenbüttel` | `VetR Diethard Oldenbüttel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich` (address)
- `BOD Steuerberatungs-GmbH` (organisation)
- `FA Landeck Reutte` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Antonewitz` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr.in Ljiljana Kos` | `Dr.in Ljiljana Kos` |
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Ljiljana Kos` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |
| `Dr. Schmid` | `Dr. Schmid` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Ljiljana Kos` (person)
- `Klinik Favoriten` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

| Predicted | Gold |
|---|---|
| `Dr. Sasan Hamzavi` | `Dr. Sasan Hamzavi` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Philippov` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Dr.in Lydia Vogtleitner` (person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_26`)


Sie könne nicht  aufstehen, bewegt aber seitengleich (diesbezüglich liegen keine Befunde vor)   Derzeitige Beschwerden:   diverse Schmerzen, sie könne nicht gehen   Behandlung(en) / Medikamente / Hilfsmittel:   kann keine Angaben machen   Sozialanamnese:   lebt in Caritasheim vollbetreut, I(nvaliditäts)Pension, Pflegestufe 4, Erwachsenenvertretung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   28.4.87 Dipl.-Ing. Kirsten Hüffner: Es handelt sich bei (der Bf.) um eine Oligophrenie.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Kirsten Hüffner` | `Dipl.-Ing. Kirsten Hüffner` |

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_77`)


Wie aus dem Gutachten Prof. Univ.Doz. Dr.med Dipl.-Ing. Kirsten Hüffner  vom 28.04.1987, Seite 6, ersichtlich,  sind schizophreniforme Psychosen bei Oligophrenie sehr schwer und oft gar nicht deutbar.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Kirsten Hüffner` | `Dipl.-Ing. Kirsten Hüffner` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Neiser` | `Dr. Stephan Neiser` |
| `Mag. Esra Rohleder` | `Mag. Esra Rohleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Amtsvertr` | `Dr. Amtsvertr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claudia Noeltge` (person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich` (address)
- `Finanzamtes Spittal Villach` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_199`)


Der Bf führte in seinem Schussantrag aus, dass er die ImmoESt gar nicht schulde, sondern hätte  diese vielmehr sein vormaliger steuerlicher Vertreter, StB Techn R Melinda Kälbli  zu tragen.

| Predicted | Gold |
|---|---|
| `Techn R Melinda Kälbli` | `Techn R Melinda Kälbli` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_350`)


Eine Haftung des ehemaligen  steuerlichen Vertreters des Bf, StB Techn R Melinda Kälbli  auf Grundlage der Bestimmung des § 30c Abs. 3 leg.  cit.

| Predicted | Gold |
|---|---|
| `Techn R Melinda Kälbli` | `Techn R Melinda Kälbli` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

| Predicted | Gold |
|---|---|
| `Mag. Artner` | `Mag. Artner` |

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr. Padesse` | `Dr. Padesse` |
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R HR Martina Pisterer` (person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frieda Krein` | `Hon.-Prof.in Frieda Krein` |
| `Priv.-Doz.in Elena Kaminskiy` | `Priv.-Doz.in Elena Kaminskiy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich` (address)
- `Mag. András Radics` (person)
- `Finanzamt Wien` (organisation)
- `60-936/8299` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_2`)


Begründung  Der Beschwerdeführer Priv.-Doz.in Elena Kaminskiy  hat mit Eingabe vom 22.10.2020, eingelangt am 27.10.2020,  gemäß § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht  über die Beschwerde gegen den Einkommensteuerbescheid für 2019 erhoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Elena Kaminskiy` | `Priv.-Doz.in Elena Kaminskiy` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Christine Schweinfort  über den Antrag der Kira Ballis, BEd,  Josefiwaldweg 48, 3071 Diemannsberg, Österreich, auf Gewährung der Verfahrenshilfe im Beschwerdeverfahren gegen den  Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020  betreffend Abweisung des Rückzahlungsantrages, Steuernummer 24-406/6946  beschlossen:  I. Der Antrag auf Gewährung der Verfahrenshilfe wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Christine Schweinfort` | `Mag.a Christine Schweinfort` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kira Ballis, BEd` (person)
- `Josefiwaldweg 48, 3071 Diemannsberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `24-406/6946` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/130620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130620.1_1`)


BESCHLUSS   Das Bundesfinanzgericht beschließt durch den Richter Mag. Günter Narat über den  Vorlageantrag vom 19. Dezember 2018 des Beschwerdeführers Diethard Uphof, Unterrotte 8, 3061 Unterwolfsbach, Österreich,  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten, 3100 St. Pölten, Daniel Gran-Straße 8,  vom 4. Mai 2018 betreffend Umsatzsteuer 2016:    I)

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diethard Uphof` (person)
- `Unterrotte 8, 3061 Unterwolfsbach, Österreich` (address)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Nicola Folprecht` | `Univ.-Prof.in Nicola Folprecht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florian Abbruzzese, BA` (person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lubomir Gruebert` | `Priv.-Doz. Lubomir Gruebert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexander Powell` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Dr. Alfred Klaming` | `Dr. Alfred Klaming` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Calvin Gorol` (person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich` (address)
- `Helmut Binder` (person)
- `Zollamtes Klagenfurt` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

| Predicted | Gold |
|---|---|
| `RgR Frederike Wegerth` | `RgR Frederike Wegerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich` (address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Spittal Villach` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Lex` (person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Irene Kohler` | `Mag. Irene Kohler` |
| `Dipl.-Ing. Erwin Göktan` | `Dipl.-Ing. Erwin Göktan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leckbichl 2, 8151 Altreiteregg, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ronald Töws` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Rupert Karl` | `Mag. Rupert Karl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gudrun Sochurek` (person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Cäcilia Wlcek` (person)
- `Rambergweg 3, 4950 Weidenthal, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

| Predicted | Gold |
|---|---|
| `Dr. Karl Renner` | `Dr. Karl Renner` |

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/131065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131065.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valerie Süssmeier` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jeffrey Wengschick` | `Dr. Jeffrey Wengschick` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donald Hayder, MA` (person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/131109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131109.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Christiane Fredebold  in der Beschwerdesache des  Beschwerdeführers, vertreten durch X-Steuerberatung, über die Beschwerde vom 25.April  2019, beim Finanzamt eingelangt am 29. April 2019, gegen die Bescheide des FA Landeck Reutte  vom  7. Februar 2019 betreffend Einkommensteuer 2016 und 2017 zur Steuernummer  29-137/6865  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Christiane Fredebold` | `Hon.-Prof.in Christiane Fredebold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `X-Steuerberatung` (organisation)
- `Finanzamt` (organisation)
- `FA Landeck Reutte` (organisation)
- `29-137/6865` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Mag. Gerald Erwin Ehgartner` — partial — pred is substring of gold: `MMag. Gerald Erwin Ehgartner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag. Gerald Erwin Ehgartner`(person)
- `Zeno Matyssek`(person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH`(organisation)
- `Finanzamt für Gebühren`(organisation)

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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `DDr.in Rafaela Ringart` — partial — pred is substring of gold: `Priv.-Doz.in DDr.in Rafaela Ringart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in DDr.in Rafaela Ringart`(person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich`(address)
- `Silvestri Bau GmbH`(organisation)
- `Mag. WP`(person)
- `38-663/2876`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Mag.a Reneé Kobayashi, Weinbaugebiet Losling 9, 4880 Aich, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `Mag.a Rene` — partial — pred is substring of gold: `Mag.a Reneé Kobayashi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Elisabeth Traxler`(person)
- `Mag.a Reneé Kobayashi`(person)
- `Weinbaugebiet Losling 9, 4880 Aich, Österreich`(address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Dipl.-Ing. Brunhild Fleischfresser` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`

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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `ÖkR Horst Stevens` — partial — pred is substring of gold: `Ing. ÖkR Horst Stevens`
- `Mag. Manfred Frühwirth` — partial — pred is substring of gold: `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache KommR Eckard Gaiss, Bakk. phil., Hietzinger Kai 33, 4132 Lug, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 07-088/5911  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Hietzinger Kai 33, 4132 Lug, Österreich`(address)
- `Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `07-088/5911`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_3`)


Entscheidungsgründe  Mit Bescheiden des Finanzamtes Wien 1/23 jeweils vom 9. August 2019 wurden über die  KommR Eckard Gaiss, Bakk. phil. (in weiterer Folge: Bf.) erste Säumniszuschläge für Umsatzsteuer 05/2019 in Höhe  von € 209.028,38 (Säumniszuschlag € 4.180,57), für Werbeabgabe 05/2019 in Höhe von €  177.156,96 (Säumniszuschlag € 3.543,14), für Lohnsteuer 06/2019 in Höhe von € 85.47466  (Säumniszuschlag € 1.709,49) und für Dienstgeberbeitrag 06/2019 in Höhe von € 20.536,18  (Säumniszuschlag € 410,72), Säumniszuschläge gesamt € 9.843,92, festgesetzt, da die  angeführten Abgabenschuldigkeiten nicht innerhalb der Frist 15. Juli 2019 entrichtet worden  sind.

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 1/23`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_15`)


Am 15. Juli 2019 hat unsere Mandantschaft via Finanz Online einen Antrag auf Übertragung an  die KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10)  iHv EUR 336.224,91 eingebracht (Hinweis: Betreffend die Martinssen Versicherung GmbH wurde ebenfalls ein  Säumniszuschlag festgesetzt und ist eine Beschwerdevorentscheidung ergangen;

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_31`)


Als Beilage dürfen wir Ihnen nachfolgende Unterlagen übermitteln:   XML-Datenträger UVA 05/2019 betreffend die Gerstbreu Umwelt GmbH  Fax an das Finanzamt 13.08.2019 inkl. UVA 05/2019 und Produktionsübermittlung  vom 12.Juli 2019 betreffend die Gerstbreu Umwelt GmbH inkl. Antrag betreffend die Übertragung  eines Geldbetrages für die KommR Eckard Gaiss, Bakk. phil.  und für die Martinssen Versicherung GmbH vom 15. Juli 2019 inkl.  Übermittlung der Rechnungen mit den größeren Vorsteuerbeträgen inkl.  Faxbestätigung vom 13. August 2019  Weiters stellen wir den Antrag den Säumniszuschlag in Höhe von EUR 9.843,92 herabzusetzen  bzw. nicht festzusetzen, da unserer Mandantschaft aus oben angeführten Gründen an der  Versäumnis kein grobes Verschulden trifft.

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `Finanzamt`(organisation)
- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Martinssen Versicherung GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


Der steuerliche Vertreter hat weiter ausgeführt, dass am 15. Juli 2019 unsere Mandantschaft  (aus dem Zusammenhang ist davon auszugehen, dass es sich bei der Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH handelt) via FinanzOnline einen Antrag auf Übertragung an die  KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10) iHv  EUR 336.224,91 eingebracht hat (Hinweis: Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH ebenfalls ein Säumniszuschlag festgesetzt worden sein und sei eine  Beschwerdevorentscheidung ergangen, wogegen ein Vorlageantrag und Antrag gem. § 217 (7)  BAO eingebracht worden sei).

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `Dr.in Monika Wörther` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Monika Wörther-Madl`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dr.in Monika Wörther` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Mag. Artner` — partial — pred is substring of gold: `Mag. Artner-Tauscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Artner-Tauscher`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

</details>

---

## `German Legal Person (Frau/Herr Context)` 🏆

**F1:** 0.086 | **Precision:** 0.591 | **Recall:** 0.046  

**Format:** `regex`  
**Rule ID:** `451550d3`  
**Description:**
Matches names preceded by 'Frau' or 'Herr', capturing the full name including suffixes, while excluding titles from the match.

**Content:**
```
(?:Frau\s+|Herr\s+)(?=[A-Z][a-zäöüß]+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-\s+[A-Z][a-zäöüß]+)*(?:\s+(?:LL\.M\.|BSc|Dipl\.-Ing\.|PhD|MA|LLB|MSc|MBA|Bakk\.))*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.591 | 0.046 | 0.086 | 193 | 114 | 79 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 114 | 79 | 2282 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_49`)


Im Firmenbuch ist Herr Jeskin als Geschäftsführer seit x.2009 eingetragen.

| Predicted | Gold |
|---|---|
| `Jeskin` | `Jeskin` |

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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_162`)


PV;  ZV Frau Bittlmeier (Mutter des Beschwerdeführers) pA Beschwerdevertreterin;

| Predicted | Gold |
|---|---|
| `Bittlmeier` | `Bittlmeier` |

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_172`)


Vorgutachten 14 08 2018:   paranoide Schizophrenie GdB 50%   seit 07/2014   Herr Hademar Berking  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA    Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_219`)


Herr Hademar Berking  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA   Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Hademar Berking` | `Hademar Berking` |

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_3`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes für Gebühren, Verkehrsteuer und Glücksspiel über die  Festsetzung eines ersten Säumniszuschlages vom 10. November 2014 wurde über Frau Eign (kurz: Bf.) von den Gebühren (Bestandsverträge) Journale 07/2014 von EUR 2.701,00 gemäß  § 217 Abs. 1 und 2 BAO ein Säumniszuschlag mit 2%, das sind EUR 54,02, mit der Begründung  festgesetzt, dass die oben angeführte Abgabenschuldigkeit nicht bis 15. September 2014  entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Eign` | `Eign` |

**Missed by this rule (FN):**

- `Finanzamtes für Gebühren` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Floriane Herppich  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Maltern  in Ausbildung zur Krankenpflegerin.

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |

**Missed by this rule (FN):**

- `Maltern` (city)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Floriane Herppich  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Floriane Herppich  nicht mehr in Frage kam, sodass sich Frau  Floriane Herppich  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |
| `Floriane Herppich` | `Floriane Herppich` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Floriane Herppich  nicht gemangelt hat, Frau Floriane Herppich  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

| Predicted | Gold |
|---|---|
| `Floriane Herppich` | `Floriane Herppich` |
| `Floriane Herppich` | `Floriane Herppich` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Aufgrund einer anonymen Anzeige im April 2013 wurden finanzpolizeiliche Ermittlungen  durchgeführt und erhoben, dass Frau Samuel Herpel (= Beschwerdeführerin, Bf) das Fahrzeug der  Marke X1, FIN Nr1, Erstzulassung (EZ) 1.10.2012, mit dem deutschen Kennzeichen AA1, im  Inland verwendet.

| Predicted | Gold |
|---|---|
| `Samuel Herpel` | `Samuel Herpel` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_92`)


Im Antwortschreiben vom 7.12.2020 wird seitens der Bf ausgeführt:  " … Ad 1)Frau Merbot hat im strittigen Zeitraum ab Oktober 2012 nach ihren Angaben und nach  ihrer Erinnerung mehrmals monatlich die Strecke D/Y (Hauptwohnsitz) nach A/X  (Nebenwohnsitz) zurück gelegt.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_96`)


Herr und Frau Herpel besuchen dort  gemeinsam Restaurants, das FitnessCenter, Ärzte oder absolvieren Theaterbesuche.

| Predicted | Gold |
|---|---|
| `Herpel` | `Herpel` |

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_97`)


In Land3 besitzt Frau Merbot ein Haus, das sie alle ca. 6 Wochen im Jahr für einige Tage entweder  allein oder mit ihrem Gatten aufsucht.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_102`)


Überdies besitzt es einen großen Obstgarten mit ca. 800 m2 (Kirschen, Äpfel,  Pflaumen, Walnüsse), die jedes Jahr von Frau Merbot selbst geernet werden.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_103`)


Anmerkungen:  Der Vollständigkeit halber möchten wir festhalten, dass Frau Merbot immer ihren Hauptwohnsitz  in Deutschland, D/Z bzw. D/Y, hatte.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_110`)


Frau Merbot ist und war ausschließlich in Deutschland versichert, bezahlt ihre Steuern nur in  Deutschland und war stets in Deutschland beschäftigt (XX) und wohnhaft (Hauptwohnsitz).

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_113`)


Herr C ist 1985  nach Österreich zurückgekehrt,Frau Herpel hat ihren deutschen Hauptwohnsitz hingegen  beibehalten.

| Predicted | Gold |
|---|---|
| `Herpel` | `Herpel` |

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_116`)


Nach ihrer Pensionierung ist Frau Merbot von D/Z nach D/Y gezogen, um räumlich näher bei ihrem  Mann zu sein.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_121`)


Frau Merbot hat sich immer wieder in A/X aufgehalten.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_124`)


Frau Merbot hat nie die Aussage getätigt, dass sie sich zu irgend einem Zeitpunkt überwiegend in  Österreich aufhält. Dies wäre schlichtweg falsch.

| Predicted | Gold |
|---|---|
| `Merbot` | `Merbot` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_36`)


In dieser Niederschrift wurde festgehalten, dass lediglich Herr Ruhkopf mit diesem  Auto fuhr.

| Predicted | Gold |
|---|---|
| `Ruhkopf` | `Ruhkopf` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_88`)


Wie aus dem Beschwerdeverfahren des BFG zu GZ. RV/4100396/2016 – betreffend die  Vorschreibung von Kfz-Steuer und NoVA an Herrn Dilaver wegen Privatnutzung des  nicht angemeldeten, streitgegenständliche Kfz durch das Finanzamt Spittal Villach –  hervorgeht, präsentierte Herr Ruhkopf das streitgegenständliche Kfz von 2011 bis  2015 jährlich beim Sportwagentreffen in KärntnerOrt, wobei er sich einen Verkaufspreis von  ca. 300.000,00 € vorstellte.

| Predicted | Gold |
|---|---|
| `Ruhkopf` | `Ruhkopf` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `Dilaver` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_94`)


Es ist auch daraus zu  schließen, dass der zivilrechtliche Verkauf des Kfz von der Bf. an die KomplementärGes m.b.H.  im Jahr 2016 nichts daran änderte, dass Herr Ruhkopf weiterhin – nunmehr als  Geschäftsführer der KomplementärGes m.b.H. – vollen Zugriff auf das Kfz hatte.

| Predicted | Gold |
|---|---|
| `Ruhkopf` | `Ruhkopf` |

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_36`)


Herr Wolfgang Orosz  wird ohne sachliche Grundlage um 123 TEUR entreichert, während in  vergleichbaren Fällen im betrieblichen Bereich dies nicht geschieht.

| Predicted | Gold |
|---|---|
| `Wolfgang Orosz` | `Wolfgang Orosz` |

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_104`)


Herr Patrick Kirschbauer  ersucht daher höflich um Aufhebung der Bescheide über die Festsetzung der  Kapitalertragssteuer für die Jahre 2007 über € 17.853,95, sowie für 2008 über € 20.933,35 und  2009 über € 8.350,00.“

| Predicted | Gold |
|---|---|
| `Patrick Kirschbauer` | `Patrick Kirschbauer` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_5`)


Alleingesellschafterin und Geschäftsführerin ist Frau Wahl   1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (kurz: Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Bf ist eine GmbH deren alleinige Gesellschafterin Frau Wahl ist.

| Predicted | Gold |
|---|---|
| `Wahl` | `Wahl` |
| `Wahl` | `Wahl` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_144`)


2. Die Gesellschafter der Weierstrass Textil  haben bisher mündlich vereinbart und halten  hinsichtlich des Geschäftsführerbezuges von Herrn Siegfried Terentew  folgendes fest: Herr  Siegfried Terentew  erhält einen fixen Geschäftsführerbezug von € 30.000,00 pro Jahr bzw. €  7 von 16 Seite 8 von 16

| Predicted | Gold |
|---|---|
| `Siegfried Terentew` | `Siegfried Terentew` |

**Missed by this rule (FN):**

- `Weierstrass Textil` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/134026.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134026.1_145`)


2.500, 00 monatlich, des weiteren erhält Herr Siegfried Terentew  einen variablen Bezug von  max.

| Predicted | Gold |
|---|---|
| `Siegfried Terentew` | `Siegfried Terentew` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Gerhard Groschedl, die Richterin Dr. Michaela Schmutzer und die fachkundigen  Laienrichter L1 und L2 in der Finanzstrafsache gegen Frau Valerian Unterfranz, geb., Schanzplatz 130, 3664 Hundsbach, Österreich,  vertreten durch LBG Niederösterreich GmbH, Raiffeisenpromenade 2/1/6, 3830 Waidhofen an  der Thaya, wegen der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 1 und  Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde der Beschuldigten vom 9.  März 2020 gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19  Klosterneuburg als Organ des Finanzamtes Waldviertel als Finanzstrafbehörde vom  21. November 2019, SpS 19, Strafnummer 23-2018, in Anwesenheit der Beschuldigten, ihres  Verteiigers, des Amtsbeauftragten HR AB sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Waldviertel als Finanzstrafbehörde zur Strafnummer 2018 gegen die  Beschuldigte geführte Finanzstrafverfahren wegen des Verdachts der Verkürzung von  Umsatzsteuer 2012 von € 860,00, Umsatzsteuer 2013 von € 860,00, Umsatzsteuer 2014 von €  860,00, Umsatzsteuer 2015 von € 860,00 bzw. Umsatzsteuer 2016 von € 433,33 und  Umsatzsteuervorauszahlungen 01-09/2017 von € 433,33 wird gemäß §§ 136, 157, 82 Abs. 3  lit. c FinStrG eingestellt.  Über Valerian Unterfranz  wird für die verbleibenden Finanzvergehen (bzw. strafbestimmenden  Werteträge) gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 7.944,00 verhängt.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Dr. Michaela Schmutzer` (person)
- `Schanzplatz 130, 3664 Hundsbach, Österreich` (address)
- `Finanzamt Wien 9/18/19` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt Waldviertel` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Waldviertel als Finanzstrafbehörde vom 21. November 2019, SpS 19,  Strafnummer 2018, wurde Frau Valerian Unterfranz, geboren am 13. Juli 1971, wohnhaft in Schanzplatz 130, 3664 Hundsbach, Österreich  schuldig erkannt, sie habe im Bereich des Finanzamtes Waldviertel   A.) durch Abgabe unrichtige Umsatz- und Einkommensteuererklärungen für die Jahre 2010 bis  2016, sohin unter Verletzung einer Wahrheits- und Offenlegungspﬂicht gemäß § 119 BAO  vorsätzlich bewirkt, dass   Umsatzsteuer für 2012 in Höhe von € 2.614,430, für 2013 in Höhe von € 2.981,49, für 2014 in  Höhe von € 3.307,05, für 2015 in Höhe von € 3.395,74, für 2016 in Höhe von € 3.430,78,   Einkommensteuer für 2010 in Höhe von € 1.446,00, für 2011 in Höhe von € 1.712,00, für 2012  in Höhe von € 4.691,00, für 2013 in Höhe von € 5.037,00, für 2014 in Höhe von € 5.599,00, für  2015 in Höhe von € 7.530,00 (€ 41.744,49)  verkürzt worden sei, und   B) vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes entsprechenden Voranmeldungen eine Verkürzung von  Vorauszahlungen an Umsatzsteuer für 01-09/2017 in der Höhe von € 2.605,11 bewirkt und dies  nicht nur für möglich, sondern für gewiss gehalten.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Schanzplatz 130, 3664 Hundsbach, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_32`)


Begründung  Mit Erkenntnis vom 21.11.2019 wurde Frau Valerian Unterfranz  wegen Finanzvergehen gemäß § 33 Abs  1 FinStrG und § 33 Abs 2 lit a FinStrG zu einer Geldstrafe von € 8.800 verurteilt.  Strafbemessungsbasis waren – neben nichterklärten Einkünften aus Vermietung und  Verpachtung – Sicherheitszuschläge, welche die Außenprüfung den Einkünften aus  Gewerbebetrieb bzw. den Umsätzen hinzugerechnet hat.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/134050.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134050.1_35`)


Laut Prüfungsbericht vom 30.11.2017 wurde von der Außenprüfung bei Frau Valerian Unterfranz  hinsichtlich Ihrer Einkünfte / Umsätze aus Gewerbebetrieb aufgrund von  Aufzeichnungsmängeln ein Sicherheitszuschlag gewinn- und umsatzerhöhend hinzugerechnet.

| Predicted | Gold |
|---|---|
| `Valerian Unterfranz` | `Valerian Unterfranz` |

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_6`)


Das Bundesfinanzgericht hat erwogen:  I. Aus den insoweit unbedenklichen Vorlageunterlagen des Finanzamtes (FA) bzw. Firmenbuch-  und Grundbuchdaten ergibt sich nachfolgender Sachverhalt, den das BFG dieser Entscheidung  als erwiesen zu Grunde legt:  Adressat der angefochtenen Erledigung ist Herr Ronald Jundt (nachfolgend Herr M.), der  aufgrund eines Kaufvertrages vom 19.Mai 2017 im Verfahrenszeitraum zu einem Drittel  Miteigentümer jener Liegenschaft war, auf welcher der strittige Rohbau errichtet wurde  (Lageadresse: R-Gasse 15, 9999 Wien).

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)
- `BFG` (organisation)
- `M.` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_33`)


Als Begründung ist anzuführen, dass Herr Ronald Jundt  kein Gesamtschuldner aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der Furtnex-Versand GmbH nicht um Bauleistungen handelt.  Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  Zur Korrektur des Irrtums wurden die Rechnungen berichtigt, neu ausgestellt mit  Umsatzsteuerausweis von 20 % und bezahlt gemäß dem Prüfungsergebnis.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_38`)


Die von der Firma Furtnex-Versand GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Ronald Jundt  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.

| Predicted | Gold |
|---|---|
| `Ronald Jundt` | `Ronald Jundt` |

**Missed by this rule (FN):**

- `Furtnex-Versand GmbH` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_87`)


Ich bitte Sie für diesen Zeitraum den Krankenstand zu gewähren.“   < Schreiben des Arbeitgebers vom 28. Jänner 2019:  „Hiermit wird bestätigt, dass kein Einwand besteht, dass Herr Franziskus während des  6 von 13 Seite 7 von 13

| Predicted | Gold |
|---|---|
| `Franziskus` | `Franziskus` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_6`)


Demnach habe Herr  Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_17`)


Demnach habe Herr  Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_29`)


Demnach habe Herr  Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_52`)


Demnach  habe Herr Judith Koerstgen  die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Judith Koerstgen` | `Judith Koerstgen` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_67`)


Ich bin Frau Celebioglu  mutter von Judith Koerstgen  und Ich möchte Ihnnen  bescheid  sagen:um diesse zeit Mein sohn ist nicht mit die auto gefahren,eine bekante von Ihm  G… …lov [Vor- und Nachname] und er muss die strafen zahlen.Ich schike Ihnenn Vollmacht  zwischen mein sohn und G… …lov [Vor- und Nachname wie vorangehende Zeile].

| Predicted | Gold |
|---|---|
| `Celebioglu` | `Celebioglu` |

**Missed by this rule (FN):**

- `Judith Koerstgen` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/135933.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135933.1_69`)


Wenn  Sie noch was brauchen schreiben Sie mir Bitte  mit freundliche Grüße  Frau Celebioglu  2)

| Predicted | Gold |
|---|---|
| `Celebioglu` | `Celebioglu` |

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/136739.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136739.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/137456.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Siegfried Herboldt  in der Beschwerdesache der Frau  Erich Vossebrink, Voestalpine-Straße 28, 2813 Pengersdorf, Österreich, vertreten durch Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft, Mariahilfer  Straße 74A, 1070 Wien, über die Beschwerde vom 8. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 9. März 2021 betreffend Abweisung eines Antrages auf  Aufhebung gemäß § 299 BAO (hinsichtlich Einkommensteuer 2019) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Erich Vossebrink` | `Erich Vossebrink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Siegfried Herboldt` (person)
- `Voestalpine-Straße 28, 2813 Pengersdorf, Österreich` (address)
- `Leonhart & Leonhart  Wirtschaftstreuhandgesellschaft m.b.H. & Co KG Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_24`)


In einer Besprechung vom 16.1.2015 hat Herr Leander Krupa zu  diesem Thema ua. angegeben, dass Schätzungsgutachten sich heute nicht in seinen Akten  befinden und er zum Zeitpunkt der Selbstberechnung davon ausgegangen ist, dass der  vereinbarte Kaufpreis zumindest dem gemeinen Wert entspricht und er sich damals auf die  Auskünfte der Vertragsparteien verlassen habe, wonach der Wert (gemeint gemeiner Wert)  dem vereinbarten Kaufpreis entspricht.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_25`)


Weiter hat Herr Leander Krupa angegeben, dass er zu allen  betroffenen Selbstberechnungen die entsprechenden Nachweise vorlegen wird.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/138082.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138082.1_26`)


Mit Mail vom 9.2.2015 teilt Herr Leander Krupa dem Finanzamt für Gebühren Verkehrsteuern und  Glücksspiel mit, dass sich die entsprechenden Berechnungsgrundlagen (gemeint Nachweise  über die gemeinen Werte) bei der Firma K (die Bf) befinden.

| Predicted | Gold |
|---|---|
| `Leander Krupa` | `Leander Krupa` |

**Missed by this rule (FN):**

- `Finanzamt für Gebühren` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_26`)


Da es sich bei dem  Guntram Beinling  auch um keinen berufsmäßigen Parteienvertreter handelt, kann auch nicht  davon ausgegangen werden, dass dieses regelmäßig für andere einschreitet, weshalb der  Wortlaut seiner Beschwerde, in dem Herr Guntram Beinling  ausdrücklich im eigenen Namen  Beschwerde erhebt, auch zu keinen Zweifeln Anlass geben konnte.

| Predicted | Gold |
|---|---|
| `Guntram Beinling` | `Guntram Beinling` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_37`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_4`)


Auf Grundlage der am 07.07.2017 beim damals zuständigen Finanzamt Innsbruck  eingegangenen Beantwortung der „Überprüfung des Anspruches auf Familienbeihilfe“  (Schreiben vom 30.06.2017) und vor allem des beigelegten Lehrvertrages des Sohnes der Frau  Raimund Ondrouch (= Beschwerdeführerin, Bf) vom 21.09.2016 (Lehrzeit vom 02.09.2016 bis zum  01.09.2019 bei der Fa. S-GmbH als Sonnenschutztechniker) wurde die Familienbeihilfe für den  Sohn A, geb. 07/1999, zunächst verlängert.

| Predicted | Gold |
|---|---|
| `Raimund Ondrouch` | `Raimund Ondrouch` |

**Missed by this rule (FN):**

- `Finanzamt Innsbruck` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/140794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140794.1_4`)


Begründung  Beschwerdeführer (Bf) ist Herr Paolo Ofzareck.

| Predicted | Gold |
|---|---|
| `Paolo Ofzareck` | `Paolo Ofzareck` |

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_198`)


2. Im Haftungsbescheid und auch in der Beschwerdevorentscheidung ist Herr Erika Puttfarken, der  nunmehrige Beschwerdeführer, genannt.

| Predicted | Gold |
|---|---|
| `Erika Puttfarken` | `Erika Puttfarken` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/141761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141761.1_8`)


Sie haben bekannt gegeben, dass der Kindesvater Herr Pennings laufend in Deutschland lebt und  arbeitet.

| Predicted | Gold |
|---|---|
| `Pennings` | `Pennings` |

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/141761.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141761.1_13`)


Meinen Kindern S. (geb.  am 2019) und A. (geb. am 2021) kommt ebenfalls der Status der Asylberechtigten zu. Der Vater  meiner Kinder,Herr Pennings  lebt in Deutschland, konkret in D, Thüringen.

| Predicted | Gold |
|---|---|
| `Pennings` | `Pennings` |

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_3`)


Begründung  Mit Bescheid des Finanzamtes Österreich vom 21.10.2021 wurde Herr Ilhan Drommelschmidt, geboren am  2. September 2011, gemäß § 26 Abs 1 Familienlastenausgleichsgesetz 1967 (nachfolgend „FLAG  1967“) in Verbindung mit § 33 Abs 3 EStG 1988 aufgefordert, die für ihn selbst bezogene  Familienbeihilfe sowie die Kinderabsetzbeträge für den Zeitraum Oktober 2018 bis März 2021  zurückzuzahlen.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Missed by this rule (FN):**

- `Finanzamtes Österreich` (organisation)
- `2. September 2011` (date)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_6`)


Am 19.11.2021 erhob Herr Ilhan Drommelschmidt  fristgerecht Beschwerde gegen den  Rückforderungsbescheid.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_8`)


Herr Ilhan Drommelschmidt  habe mit Oktober 2016 das Studium Lehramt mit den  Unterrichtsfächern Englisch und Psychologie begonnen.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_16`)


Ein  Familienbeihilfenanspruch bestehe erst dann (wieder), wenn Herr Ilhan Drommelschmidt  in dem nunmehr  gewählten Studium so viele Semester wie in den vor dem nunmehr gewählten Studium  zurückgelegt hat (§ 2 Abs 1 lit b FLAG 1967).

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_17`)


Diese Wartezeit habe im vorliegenden Fall bis  09/2020 bestanden; mit 13. Dezember 1973  habe Herr Ilhan Drommelschmidt  das 25.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Missed by this rule (FN):**

- `13. Dezember 1973` (date)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_55`)


In Ansehung dieser Grundsätze ist das am 17.05.2022 beim Finanzamt eingelangte Schreiben  nicht als Antrag auf Entscheidung über die Beschwerde vom 19.11.2021 durch das  Bundesfinanzgericht (Vorlageantrag) zu werten:  Dass Herr Ilhan Drommelschmidt  eine Rechtsmittelentscheidung durch das Bundesfinanzgericht anstrebt, ist  dem Inhalt der Eingabe nicht zu entnehmen (vgl auch die Ausführungen von Herrn Alan Zygan,  wonach er zwar auf die Beschwerdevorentscheidung vom 11.04.2022 reagiert, sogleich aber  festhält, diese „im Lichte der Judikatur des VwGH inhaltlich nachvollziehen zu können“;

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Alan Zygan` (person)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/142519.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142519.1_59`)


Herr Ilhan Drommelschmidt  regt in dem Schreiben die Vorlage  des Aktes bei der sachlich in Betracht kommenden Oberbehörde (= für die Vollziehung des  FLAG zuständiger Bundesminister) an, diese möge von ihrem Mäßigungsrecht gemäß § 26  Abs 4 FLAG Gebrauch machen.

| Predicted | Gold |
|---|---|
| `Ilhan Drommelschmidt` | `Ilhan Drommelschmidt` |

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/142976.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142976.1_6`)


Mit Schreiben vom 22.11.2021 teilte Herr Ida Doelling (= Beschwerdeführer, Bf) dem  Finanzamt mit, dass er lt. Beschluss des BG Ort1 v. 16.11.2021 wieder die Obsorge über seine  beiden Kinder A, geb. 11/2019, und B, geb. 05/2018, übernommen habe und ersuchte um  Auszahlung der Familienbeihilfe (FB) wiederum auf sein Konto.

| Predicted | Gold |
|---|---|
| `Ida Doelling` | `Ida Doelling` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/143180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143180.1_14`)


Mit Schreiben vom 19. September 2023 teilte der Sozialministeriumsservice der belangten  Behörde aufgrund einer Anfrage mit, dass der Parkausweis mit der Nummer Nr unbefristet an Frau Hannak ausgegeben worden sei und dass Frau Hannak  zuletzt wohnhaft in Schauflacker 13, 6425 Schlierenzau, Österreich, am  tt.mm.2021 verstorben sei.

| Predicted | Gold |
|---|---|
| `Hannak` | `Hannak` |
| `Hannak` | `Hannak` |

**Missed by this rule (FN):**

- `Schauflacker 13, 6425 Schlierenzau, Österreich` (address)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_2`)


Der Spruch des angefochtenen  Bescheides wird gemäß § 279 Abs. 1 BAO dahingehend abgeändert, dass er lautet: Die  Grundsteuer für die gegenständliche Liegenschaft wird Frau Ruperta Keymer  ab 1. Jänner  2018 mit einem Jahresbetrag von 82,79 € vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Ruperta Keymer` | `Ruperta Keymer` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_181`)


Der Herr Ing KB und ich sind langjährig befreundet.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing KB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing KB`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_4`)


Laut Firmenbuchauszug ist Herr Jeskin Geschäftsführer seit 23.7.2009.

**False Positives:**

- `Jeskin Geschäftsführer` — partial — gold is substring of pred: `Jeskin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeskin`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_18`)


Mit Eingabe vom 04.11.2020 erhob die Bf. gegen diese Vollstreckungsverfügung Beschwerde  und brachte dabei Folgendes vor: „Frau Alva van de Velden  hat den PKW nicht gelenkt.

**False Positives:**

- `Alva` — partial — pred is substring of gold: `Alva van de Velden`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alva van de Velden`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Donald Hayder` — partial — pred is substring of gold: `Donald Hayder, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Jeffrey Wengschick`(person)
- `Donald Hayder, MA`(person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_23`)


Auf Grund einer Anfrage des Bundesfinanzgerichtes bei der für Meldeangelegenheiten  zuständigen Fachdienststelle in der Stadt Wien, der MA 62, teilte diese mit E-Mail vom  25.2.2021 folgendes mit:  „Zu Ihrer Anfrage teile ich Ihnen seitens der Magistratsabteilung 62 als zuständiger  Fachdienststelle für Meldeangelegenheiten in der Stadt Wien mit, dass Herr Lieselotte Rübenkönig, Bakk. rer. nat.  wie  von ihm angegeben von uns nach Durchführung eines Verfahrens nach § 15 Meldegesetz  amtlich von der Adresse xy abgemeldet wurde.

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_26`)


Der Erheber bekam vor Ort am  14. Jänner 2020 von einer Hauspartei, deren Identität wir nicht kennen, die Auskunft, dass Herr  Lieselotte Rübenkönig, Bakk. rer. nat.  unbekannt wohin verzogen sei.

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_27`)


Herr Lieselotte Rübenkönig, Bakk. rer. nat.  wurde von uns zweimal im  Verfahren angeschrieben, davon einmal mit RSb-Rückscheinbrief, und hat darauf nicht  reagiert.“

**False Positives:**

- `Lieselotte Rübenkönig` — partial — pred is substring of gold: `Lieselotte Rübenkönig, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lieselotte Rübenkönig, Bakk. rer. nat.`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_16`)


1) Höhe der 2014 in Österreich Steuerpflichtigen Bezüge aus nicht selbständiger Arbeit   Herr Bf. erzielte auch in 2014 Einkünfte aus nichtselbständiger Arbeit als angestellter  Staatsanwalt aus Dienstverhältnissen zu zwei Schweizer Körperschaften öffentlichen Rechtes  (Kanton Nidwalden und Bund).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_7`)


Unbeschränkt haftende Gesellschafter der Bf. waren bis 9.7.2016 Herr VornameGeser1  NachnameGeser1 und bis 28.9.2012 Herr Geser2.

**False Positives:**

- `Vorname` — no gold match — likely missing annotation
- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_10`)


der KomplementärGes m.b.H. ist seit ihrer Gründung im Jahr 2013 Herr VornameGeser1  NachnameGeser1;

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_11`)


ihr Gesellschafter war bis 24.6.2016 zu 100% Herr VornameGeser1  NachnameGeser1;

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_12`)


seitdem hält dieser 6% des Stammkapitals und Frau Eisenkrammer NachnameGeser1  94% des Stammkapitals.

**False Positives:**

- `Eisenkrammer Nachname` — partial — gold is substring of pred: `Eisenkrammer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Eisenkrammer`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_54`)


Die Beschwerdevorentscheidungen für die Jahre 2013 und 2014 wurden wie folgt begründet:  „Herr Mag R wurde von seinem österreichischen Arbeitgeber,IGS Pflege AG  von 1. August 2010 bis 31.  März 2015 in die USA entsendet.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IGS Pflege AG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/133275.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133275.1_57`)


Anschließend ist Herr  Mag. R ein neues Dienstverhältnis in der Schweiz eingegangen und mit der Familie von den USA  in die Schweiz übersiedelt. Die Verlagerung des Lebensmittelpunktes in den Entsendestaat sei  ergänzend an Hand der (Vermutungs-)Regel gemäß Rz 7596 EStR zu beurteilen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/133829.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133829.1_75`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Wahl   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Wahl   Gegenstand` — partial — gold is substring of pred: `Wahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wahl`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/134808.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134808.1_39`)


Aus diesem Bescheid ist  ersichtlich, dass Frau Gattin im verfahrensgegenständlichen Jahr (bis Mai 2019) Kranken, Pflege  und Renten versichert ist.

**False Positives:**

- `Gattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/135161.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135161.1_37`)


Es  würde eine Bestätigung eines Allgemein Mediziners,Frau RauC, vorliegen, die einen Aufenthalt  3 von 13 Seite 4 von 13

**False Positives:**

- `Rau` — similar text (different position): `RauC`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RauC`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/135344.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mikolaj Naethler  in der Beschwerdesache der Frau  KzlR Charles Eski, Zweigeltweg 9, 3426 Wipfing, Österreich, über die Beschwerde vom 19. Oktober 2021 gegen den Bescheid  des Finanzamtes Österreich vom 15. Oktober 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Kzl` — partial — pred is substring of gold: `KzlR Charles Eski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Mikolaj Naethler`(person)
- `KzlR Charles Eski`(person)
- `Zweigeltweg 9, 3426 Wipfing, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/136066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136066.1_9`)


Das Fahrzeug sei auf Frau Hünkemeier  AdrFrau, zugelassen gewesen.

**False Positives:**

- `Hünkemeier  Adr` — partial — gold is substring of pred: `Hünkemeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hünkemeier`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_8`)


Ich ersuche Sie höflich,  den nun im Anhang nachgereichten Unterlagen von Frau Mag. M… (Klinische und  Gesundheitspsychologin, Hilfswerk NÖ) und Frau OA Dr. St… (FA für Kinder- und  Jugendheilkunde) zu entnehmen, dass der für den rückwirkenden Anspruch auf erhöhte  Familienbeihilfe erforderliche Behinderungsgrad von J… bereits zu einem früheren Zeitpunkt  belegbar ist.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/137270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137270.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dr. OStR Vivian Stinneßen (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 03/1997, laufend die  Familienbeihilfe (FB) samt Kinderabsetzbetrag (KG) bezogen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. OStR Vivian Stinneßen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. OStR Vivian Stinneßen`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/138117.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138117.1_40`)


Infolge des  Testamentes und der Eröffnungsniederschrift vom 26.6.2020 sind gesetzliche Erben des  Nachlasses: Die Ehegattin Frau Vorname Vorname2 Nachname, zu 50 % des Erbteiles, der Sohn  Herr G A Nachname zu 25 % des Erbteiles sowie Herr AC Nachname zu 25 % des Erbteiles.

**False Positives:**

- `Vorname Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_23`)


Darin liegt der „negative Leistungsanreiz“, den Frau Prof. Kanduth-Kristen im  der ersten Beschwerde beigelegten Artikel meines Erachtens zurecht als verfassungsrechtlich  bedenklich kritisiert.

**False Positives:**

- `Prof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_33`)


Ich hoffe,  meine weiteren Ausführungen veranlassen — zusammen mit dem bereits erwähnten Artikel  von Frau Prof. Kanduth-Kristen — das Gericht dazu, meine Zweifel an der  Verfassungsmäßigkeit der gegenständlichen Regelung zu teilen und wie angeregt deren  Aufhebung beim Verfassungsgerichtshof zu beantragen.

**False Positives:**

- `Prof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_149`)


Nach dem Vortrag des bisherigen verwaltungsbehördlichen und  verwaltungsgerichtlichen Verfahrens (wie oben dargestellt) gaben die Parteien auf Befragung  des Richters an:  Ri: Frage an den Bf: Ist Frau Hausärztin auch schon vor der jetzt fraglichen Behandlung im  Belgien Ihre Ärztin gewesen?

**False Positives:**

- `Hausärztin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_151`)


Bf: Frau Hausärztin war auch schon vor 2013 meine Hausärztin und behandelte mich auch in  diesem Zusammenhang.

**False Positives:**

- `Hausärztin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_225`)


Während des gesamten Zeitraumes war seine Hausärztin  Frau Hausärztin.

**False Positives:**

- `Hausärztin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/141087.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141087.1_264`)


Die langjährige Hausärztin des Bf Frau Hausärztin bestätigte im Schreiben vom 10.6.2021 die  erhebliche Beeinträchtigung der Lebensqualität des Bf durch dessen Krankheit, die  Erfolglosigkeit der herkömmlichen konservativen Behandlungen, die europaweite  Einzigartigkeit der Behandlung in Belgien sowie den Heilungserfolg (Schmerzfreiheit) durch die  Behandlung.

**False Positives:**

- `Hausärztin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_133`)


Der Bf brachte im Wege der XY WTH GmbH, fristgerecht „Beschwerde gegen den  Bescheid – Leistungsgebot“ vom 5.Nov.2021 ein und begehrte mit folgender Begründung die  Aufhebung der bekämpften Erledigung:  „Als Begründung ist anzuführen, dass Herr Wilhelm Fißenewert, LLM  kein Gesamtschuldner aufgrund von  Bauleistungen ist, da es sich bei den Rechnungen der Hemken Automotive GmbH nicht um Bauleistungen handelt.  Weiters wurden alle Rechnungen zum Bruttobetrag von den Leistungsempfängern bezahlt.  Der Leistende und der Leistungsempfänger hatten ursprünglich irrtümlich angenommen, dass  die Leistungen Bauleistungen sind und auf den Rechnungen wurde irrtümlich vermerkt, dass es  sich bei diesen Rechnungen um Bauleistungen handelt.  Zur Korrektur des Irrtums wurden die Rechnungen berichtigt, neu ausgestellt mit  Umsatzsteuerausweis von 20 % und bezahlt gemäß dem Prüfungsergebnis.

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XY WTH GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)
- `Hemken Automotive GmbH`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_138`)


Die von der Firma Hemken Automotive GmbH gelegten Rechnungen inclusive der Umsatzsteuer wurden mit dem  Bruttobetrag, also inclusive der Mehrwertsteuer von den Leistungsempfängern bezahlt.  Da es sich demnach nicht um Bauleistungen handelt, ist Herr Wilhelm Fißenewert, LLM  keine Person, die  gemeinsam zur Abgabenentrichtung heranzuziehen ist, da er nicht Gesamtschuldner ist.“  (Zitatende/Beschwerde)  10.

**False Positives:**

- `Wilhelm Fißenewert` — partial — pred is substring of gold: `Wilhelm Fißenewert, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hemken Automotive GmbH`(organisation)
- `Wilhelm Fißenewert, LLM`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/141720.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141720.1_199`)


Allerdings erfolgte die Auszahlung in Deutschland nicht an den nunmehrigen Beschwerdeführer,  sondern an Frau Zemanek  Artikel 72 der Durchführungsverordnung (EG) Nr. 987/2009 führt an, dass Rückzahlungen  begehrt werden können von einem „Träger jedes anderen Mitgliedstaates, der gegenüber der  betreffenden Person zu Leistungen verpflichtet ist.

**False Positives:**

- `Zemanek  Artikel` — partial — gold is substring of pred: `Zemanek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zemanek`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/143180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143180.1_15`)


Aufgrund des Todes von Frau Frau1 sei der Parkausweis nicht mehr  gültig.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/144414.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144414.1_32`)


Die belangte Behörde erließ eine mit 13. Juli 2023 datierte, abweisende Beschwerdevorent- scheidung an „FrauBF1 und Miteigentümer z.H. Frau FrauJ, X-StraßeB, PLZwien“ über die  Bescheidbeschwerde vom 22. April 2023 „gegen den Bescheid des Magistrats der Stadt Wien …  vom 01.04.2023, mit welchem die Grundsteuer ab 01.01.2018 mit einem Jahresbetrag in der  Höhe von 829,60 Euro vorgeschrieben wurde“.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrats der Stadt Wien`(organisation)

</details>

---

</details>

---

