# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-29T03:57:22.838867

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-29/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 500 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 100 |
| Test documents | 792 |
| Train sentences | 659 |
| Validation sentences | 158 |
| Test sentences | 88613 |
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
| Batch size | 30 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 97.6% |
| True Positives | 459 |
| False Positives | 1007 |
| False Negatives | 1996 |
| Total Gold Entities | 2455 |
| Micro Precision | 31.3% |
| Micro Recall | 18.7% |
| Micro F1 | 23.4% |
| Macro F1 | 23.4% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Party Name Extraction` | 27.7% | 78.5% | 16.8% | 525 | 412 | 113 |
| `Dr Initial Name Extraction` | 3.1% | 75.0% | 1.6% | 52 | 39 | 13 |
| `Case Name Reference` | 0.3% | 21.1% | 0.2% | 19 | 4 | 15 |
| `Name with Suffix Extraction` | 0.3% | 0.7% | 0.2% | 566 | 4 | 562 |
| `Deceased Person Reference` | 0.0% | 0.0% | 0.0% | 32 | 0 | 32 |
| `Judge Name Extraction` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |
| `General Name with Title` | 0.0% | 0.0% | 0.0% | 148 | 0 | 148 |
| `Title Name Extraction` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name at Sentence Start` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Single Letter Initial` | 0.0% | 0.0% | 0.0% | 101 | 0 | 101 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Party Name Extraction` 🏆

**F1:** 0.277 | **Precision:** 0.785 | **Recall:** 0.168  

**Format:** `regex`  
**Rule ID:** `039b37eb`  
**Description:**
Captures the name of the party (appellant/respondent) following 'Beschwerdesache' or 'Verwaltungsstrafsache', ensuring the match is a capitalized name and not a common noun, excluding trailing punctuation.

**Content:**
```
(?:Beschwerdesache|Verwaltungsstrafsache|Revisionssache|Rechtsstreit)\s+(?:des\s+|der\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.785 | 0.168 | 0.277 | 525 | 412 | 113 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 412 | 113 | 2041 |

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

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache des Levi Panos,  Puchheimgasse 2, 4770 Pram, Österreich, über die Beschwerde vom 7. April 2014 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 1. April 2014 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 Steuernummer 73-863/0859  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Levi Panos` | `Levi Panos` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Puchheimgasse 2, 4770 Pram, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `73-863/0859` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Sandro Flunger` | `Sandro Flunger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Astrid Rüstmann` (person)
- `Rohrer Straße 29, 3231 Kainratsdorf, Österreich` (address)
- `Mag. Hermann Rupert Zittmayr` (person)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Luigi Wedekämper` | `Luigi Wedekämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Marianne Liuni` (person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Wolf Sackner, Altweitra 15, 6091 Götzens, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  34-684/1904  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wolf Sackner` | `Wolf Sackner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Altweitra 15, 6091 Götzens, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `34-684/1904` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Huberta Nothofer` | `Huberta Nothofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Florenzia Rutt` | `Florenzia Rutt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich` (address)
- `Zollamtes Feldkirch Wolfurt` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Thomas Kreul, Preberstraße 4, 3911 Dietharts, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Kreul` | `Thomas Kreul` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Preberstraße 4, 3911 Dietharts, Österreich` (address)
- `DI Heinrich Richter Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jennifer Rösl` | `Jennifer Rösl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Eckard Sellnow` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stephan Antonewitz` | `Stephan Antonewitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Felizitas Philippov` | `Felizitas Philippov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gerald Hellbing` | `Gerald Hellbing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Manuel Rathlev, Hadersfelder Straße 10, 4171 Kasten, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Edwin Meuser  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Manuel Rathlev` | `Manuel Rathlev` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hadersfelder Straße 10, 4171 Kasten, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Edwin Meuser` (person)

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

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Hüpgen   in der Beschwerdesache des Alois Jeckl, Amlach 6, 2620 Straßhof, Österreich,   betreffend die Bescheide des Finanzamt Waldviertel  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 66-092/6335,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Alois Jeckl` | `Alois Jeckl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jeannine Hüpgen` (person)
- `Amlach 6, 2620 Straßhof, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `66-092/6335` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Calvin Gorol` | `Calvin Gorol` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alfred Klaming` (person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich` (address)
- `Helmut Binder` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Anatol Hasenbein, Josef-Kaut-Straße 3, 4048 Großamberg, Österreich, über die Beschwerde vom 26. Mai 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 15. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anatol Hasenbein` | `Anatol Hasenbein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josef-Kaut-Straße 3, 4048 Großamberg, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ronald Töws` | `Ronald Töws` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gudrun Sochurek` | `Gudrun Sochurek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Mag. Rupert Karl` (person)
- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Hedwig Scheff, Franz Eckrieder Straße 50, 3142 Grunddorf, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Scheff` | `Hedwig Scheff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz Eckrieder Straße 50, 3142 Grunddorf, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/131065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131065.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valerie Süssmeier` | `Valerie Süssmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Weiskittel` | `Holger Weiskittel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dorothea Sulzbacher, Obergreith 14 - 23, 4924 Breitwies, Österreich, über die Beschwerde vom 21. August 2018 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 2. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dorothea Sulzbacher` | `Dorothea Sulzbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergreith 14 - 23, 4924 Breitwies, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131601.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Waltraud Herbrecher, Südweg 312, 4062 Niederbuch, Österreich, über die Beschwerde vom 3. Oktober 2018 gegen die Bescheide des Finanzamtes Wien  1/23 vom 30. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 und  2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Waltraud Herbrecher` | `Waltraud Herbrecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Südweg 312, 4062 Niederbuch, Österreich` (address)
- `Finanzamtes Wien  1/23` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Fridolin Härlin  in der Beschwerdesache Alva Czymzik,  Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alva Czymzik` | `Alva Czymzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Fridolin Härlin` (person)
- `Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Julian Pierchala,  Pracherweg 6, 8635 Gollrad, Österreich, über die Beschwerde vom 6. August 2019 gegen den Bescheid des Finanzamtes  Österreich vom 24. Juli 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018,  Steuernummer 74-273/9351, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julian Pierchala` | `Julian Pierchala` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pracherweg 6, 8635 Gollrad, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `74-273/9351` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Adrian Hofschmidt, Dechantsbühel 10, 9911 Bannberg, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Adrian Hofschmidt` | `Adrian Hofschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dechantsbühel 10, 9911 Bannberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Sandro Fischlein, Hans-Schilder-Platz 17, 9065 Untermieger, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sandro Fischlein` | `Sandro Fischlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hans-Schilder-Platz 17, 9065 Untermieger, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/132065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Torsten Gnapfeus, Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich, gegen die Bescheide des Finanzamtes Wien 4/5/10 vom 21. Februar 2014 betreffend  die auf § 303 Abs. 1 BAO basierende Verfügung der Wiederaufnahme der Verfahren zur  Umsatzsteuer für das Jahr 2010 und zur Einkommensteuer für die Jahre 2010 und 2011 sowie  die auf § 205 Abs. 1 BAO basierende Festsetzung von Anspruchszinsen für die Jahre 2010 bis  2012 beschlossen:  Der Vorlageantrag vom 26.9.2014 wird - betreffend vorgenannter Bescheide - gemäß § 264  Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Torsten Gnapfeus` | `Torsten Gnapfeus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natalie Emmerling,  Holzäpfeltal 15, 8081 Guggitzgraben, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Natalie Emmerling` | `Natalie Emmerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holzäpfeltal 15, 8081 Guggitzgraben, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Salzburg-Land` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132328.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132328.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Michael Mühlbeck, Glöckler 35, 5252 Parz, Österreich, betreffend Beschwerde vom 17. Jänner 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 18. Dezember 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 Steuernummer 92-602/5429  beschlossen:   Der Vorlageantrag vom 5.6.2020 wird gemäß § 260 Abs. 1 lit.b BAO in Verbindung mit § 264  Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michael Mühlbeck` | `Michael Mühlbeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Glöckler 35, 5252 Parz, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `92-602/5429` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Erhard Wintjens, Völkerweg 97, 8940 Döllach, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 17-868/7871  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erhard Wintjens` | `Erhard Wintjens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Völkerweg 97, 8940 Döllach, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `17-868/7871` (tax_number)

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

- `Vincent ` — partial — pred is substring of gold: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Univ.-Prof. Janis Abelen,  Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

**False Positives:**

- `Univ` — partial — pred is substring of gold: `Univ.-Prof. Janis Abelen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Janis Abelen`(person)
- `Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Ing` — similar text (different position): `Dr.  Karl Penninger`

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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache der Bf. Name vormals nunmehr Mehmet Faidt, Flitsch 4, 4822 Kogl, Österreich, vertreten durch  Mag. Wolfgang Freudelsperger, Am Weiher 8, 9400 Wolfsberg, über die Beschwerde vom  12. August 2010 gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. Juli 2010 betreffend   Haftungsbescheid Kapitalertragsteuer 2008 und Festsetzung eines Säumniszuschlages zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Mehmet Faidt`(person)
- `Flitsch 4, 4822 Kogl, Österreich`(address)
- `Mag. Wolfgang Freudelsperger`(person)
- `Finanzamtes Wien 1/23`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hon.-Prof. Gerhard Hübinger, Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich, St.Nr. xxxxxxxxxxxx, über die Beschwerden vom 2. April 2013 gegen den  Aufhebungsbescheid gemäß § 299 BAO vom 4. März 2013 und den Zurückweisungsbescheid  vom 4. März 2013 (betreffend Antrag auf Bescheidaufhebung gemäß § 295 Abs. 4 BAO, in  eventu Antrag auf Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 lit. b BAO) des  Finanzamtes Wien 9/18/19 Klosterneuburg, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. Gerhard Hübinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Gerhard Hübinger`(person)
- `Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129336.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129336.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Alwerkmon-Pharma,  Hinteralm 4, 3243 Lachau, Österreich  vertreten durch Stb., über die Beschwerde vom 17.10.2011 gegen den Bescheid  des Finanzamtes Lilienfeld St. Pölten vom 13.7.2011 betreffend Einkommensteuer 2009 nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Alwerkmon` — partial — pred is substring of gold: `Alwerkmon-Pharma`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Alwerkmon-Pharma`(organisation)
- `Hinteralm 4, 3243 Lachau, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gotthard Eppers  vertreten durch  Gf. über die Beschwerde vom 16. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 16. Dezember 2019, Steuernummer 98-639/6692, betreffend Feststellung der  Einkünfte gem. § 188 BAO für das Jahr 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gotthard Eppers  ` — partial — gold is substring of pred: `Gotthard Eppers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gotthard Eppers`(person)
- `Finanzamtes Wien  4/5/10`(organisation)
- `98-639/6692`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Stephan Neiser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Stephan Neiser`(person)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich`(address)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `Mag. Esra Rohleder`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Techn ` — partial — pred is substring of gold: `Techn R HR Martina Pisterer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Techn R HR Martina Pisterer`(person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Frau  Donald Hayder` — positional overlap with gold: `Donald Hayder, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Jeffrey Wengschick`(person)
- `Donald Hayder, MA`(person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131109.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Christiane Fredebold  in der Beschwerdesache des  Beschwerdeführers, vertreten durch X-Steuerberatung, über die Beschwerde vom 25.April  2019, beim Finanzamt eingelangt am 29. April 2019, gegen die Bescheide des FA Landeck Reutte  vom  7. Februar 2019 betreffend Einkommensteuer 2016 und 2017 zur Steuernummer  29-137/6865  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdeführers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Christiane Fredebold`(person)
- `X-Steuerberatung`(organisation)
- `Finanzamt`(organisation)
- `FA Landeck Reutte`(organisation)
- `29-137/6865`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Georgette Dörger  in der Beschwerdesache der  Roland Wüstemeier, Sebastianplatz 167, 3420 Klosterneuburg, Österreich, über die Beschwerde vom 4. November 2019 gegen die Bescheide  des FA Salzburg-Stadt  vom 30. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017 zur Steuernummer 99-999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Roland Wüstemeier` — type mismatch — same span as gold: `Roland Wüstemeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Georgette Dörger`(person)
- `Roland Wüstemeier`(organisation)
- `Sebastianplatz 167, 3420 Klosterneuburg, Österreich`(address)
- `FA Salzburg-Stadt`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Helmut Fürnkäß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman`(person)
- `Prof. Helmut Fürnkäß`(person)
- `Dr Christian Leskoschek`(person)
- `Finanzamtes Österreich`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132289.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Camilla Gembalies  in der Beschwerdesache der  Ost Verdon Systeme, Asangstraße 9c, 9580 Mittewald, Österreich, vertreten durch Apfelbaum & Senkfeil Software GmbH betreffend Beschwerde  vom 22. April 2016 gegen die als Bescheid des Finanzamtes X vom 27. Jänner 2016 intendierte  Erledigung betreffend Festsetzung der Kraftfahrzeugsteuer 01.2014-12.2014 zur StNr 99- 99/9999 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Ost Verdon Systeme` — type mismatch — same span as gold: `Ost Verdon Systeme`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Univ.-Prof.in Camilla Gembalies`(person)
- `Ost Verdon Systeme`(organisation)
- `Asangstraße 9c, 9580 Mittewald, Österreich`(address)
- `Apfelbaum & Senkfeil Software GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Adrian Radakovitsch  ` — partial — gold is substring of pred: `Adrian Radakovitsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Merlin Thorschmidt`(person)
- `Adrian Radakovitsch`(person)
- `Schlatterbergweg 97, 9344 Psein, Österreich`(address)
- `Finanzamt Steiermark Mitte`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132617.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132617.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Erika Matuszcyk  in der Beschwerdesache Hon.-Prof. Hugo Beerbaum,  Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich, über die Beschwerde vom 27.1.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 16.1.2020, SV-Nr, betreffend die Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Jänner 2020 zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. Hugo Beerbaum`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Erika Matuszcyk`(person)
- `Hon.-Prof. Hugo Beerbaum`(person)
- `Scheibmühler Siedlung 124, 8142 Gradenfeld, Österreich`(address)
- `Finanzamtes  Innsbruck`(organisation)

</details>

---

## `Dr Initial Name Extraction` 🏆

**F1:** 0.031 | **Precision:** 0.750 | **Recall:** 0.016  

**Format:** `regex`  
**Rule ID:** `3de81520`  
**Description:**
Captures names like 'Dr. A' or 'Dr. [Name]' which are common in anonymized legal texts, ensuring the title is included.

**Content:**
```
(?:Dr\.|Dr\.in\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.016 | 0.031 | 52 | 39 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 39 | 13 | 2416 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

| Predicted | Gold |
|---|---|
| `Dr.in Fabienne Siewek` | `Dr.in Fabienne Siewek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vincent und Zielinska Solar GmbH` (organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr.in Astrid Rüstmann` | `Dr.in Astrid Rüstmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandro Flunger` (person)
- `Rohrer Straße 29, 3231 Kainratsdorf, Österreich` (address)
- `Mag. Hermann Rupert Zittmayr` (person)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Dr.in Klara Willumelies` | `Dr.in Klara Willumelies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dorfcongart-Event` (organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133036.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133036.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Daniela Weickhart  in der Beschwerdesache Cäcilia Lüderitz,  Zallingergasse 21, 9372 St. Walburgen, Österreich, über die Beschwerde vom 2. Jänner 2020 gegen den Abweisungsbescheid des  Finanzamtes Bruck Leoben Mürzzuschlag vom 4. Dezember 2019 betreffend Familienbeihilfe  für sich selbst ab November 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Daniela Weickhart` | `Dr.in Daniela Weickhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cäcilia Lüderitz` (person)
- `Zallingergasse 21, 9372 St. Walburgen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Evamaria Moucha  in der   Beschwerdesache Ing. Techn R Emma Kirmiss, Balikostraße 6, 4072 Winkeln, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Evamaria Moucha` | `Dr.in Evamaria Moucha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Techn R Emma Kirmiss` (person)
- `Balikostraße 6, 4072 Winkeln, Österreich` (address)
- `Dr. Michael Jöstl` (person)
- `Finanzamtes für Gebühren` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/133177.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133177.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anabel Sezgin  in der Beschwerdesache der  Leichsner u. Knoerrnschild Getränke, Siegersdorf bei Herberstein 14, 4693 Buchleiten, Österreich, vertreten durch Heinz Wollkopf,  Gartenauerstraße 8, 4616 Grassing, Österreich, über die Beschwerde vom 18. April 2013 gegen den Bescheid des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 1. März 2013 betreffend die  Erstattung von Vorsteuern für den Zeitraum 01-12/2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Anabel Sezgin` | `Dr.in Anabel Sezgin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leichsner u. Knoerrnschild Getränke` (organisation)
- `Siegersdorf bei Herberstein 14, 4693 Buchleiten, Österreich` (address)
- `Heinz Wollkopf` (person)
- `Gartenauerstraße 8, 4616 Grassing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/133392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133392.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ruperta Ekonomou  in der Beschwerdesache Erhard Sennewaldt,  Taubenwaldweg 24, 3232 Unterschildbach, Österreich, betreffend Beschwerde vom 29. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuervorauszahlungen  2021 Steuernummer 21-935/5536  beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 5 BAO iVm § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Ruperta Ekonomou` | `Dr.in Ruperta Ekonomou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erhard Sennewaldt` (person)
- `Taubenwaldweg 24, 3232 Unterschildbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `21-935/5536` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/133723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133723.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr.in Agnes Rüping  in der Beschwerdesache Carla Melewzik,  Hochedtweg 173, 4170 Innenschlag, Österreich, vertreten durch Korber & Partner WTH-Stb GmbH, Grünbergstraße 31, 1120  Wien, über die Beschwerde vom 12.04.2018, 23:48:25 Uhr, eingebracht am 13.04.2018,  00:01:10 Uhr, gegen den Bescheid des Finanzamtes Wien 1/23 vom 07.03.2018, zugestellt am  12.03.2018, betreffend Festsetzung einer Zwangsstrafe wegen Nichtabgabe der Steuererklä- rung E1 2015 beschlossen:  I. Die Beschwerde wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Agnes Rüping` | `Dr.in Agnes Rüping` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Carla Melewzik` (person)
- `Hochedtweg 173, 4170 Innenschlag, Österreich` (address)
- `Korber & Partner WTH-Stb GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Juliette Kempke  in der Beschwerdesache des  Ronald Jundt, (Bf-Adresse), vertreten durch Dr. (Parteienvertretername), RA,  (Parteienvertreteradresse), zur Beschwerde vom 4. Dezember 2019 gegen den zur  Steuernummer 99-999/9999 (M-GmbH i.L.) als Leistungsgebot gem. § 6 BAO ergangenen  Bescheid des Finanzamtes Wien X (jetzt Dienststelle des Finanzamtes Österreich) vom  5. November 2019 betreffend „Umsatzsteuerveranlagungen und div.

| Predicted | Gold |
|---|---|
| `Dr.in Juliette Kempke` | `Dr.in Juliette Kempke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Ronald Jundt` (person)
- `Finanzamtes` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134798.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134798.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr.in Anastasia Preis  in der Beschwerdesache Claudia Lämmermayr,  Autenalm 32, 9433 Mettersdorf, Österreich, betreffend Beschwerde vom 27. April 2021 gegen den Bescheid des Finanzamtes  Österreich vom 17. Februar 2021 betreffend Einkommensteuer 2020  (Arbeitnehmerinnenveranlagung), Steuernummer 72-315/9078  beschlossen:   Die Beschwerde vom 27. April 2021 wird gemäß § 260 Abs. 1 lit. b in Verbindung mit § 278 Abs.  1 lit. a Bundesabgabenordnung (BAO) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Anastasia Preis` | `Dr.in Anastasia Preis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claudia Lämmermayr` (person)
- `Autenalm 32, 9433 Mettersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `72-315/9078` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/134910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134910.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr.in Alva Karp  in der Beschwerdesache Sheila Nagell,  Horner Straße 104, 3623 Ernst, Österreich, vertreten durch Pölzleithner Wirtschaftstreuhand KG  Steuerberatungsgesellschaft, Dr Scheiber Str 20, 4870 Vöcklamarkt, betreffend Beschwerde  vom 4. August 2014 gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck (nunmehr  Finanzamt Österreich) vom 21. Juli 2014 betreffend Einkommensteuer 2012 Steuernummer  29-285/1127  beschlossen:   Der Vorlageantrag vom 29. September 2014 wird gemäß § 256 Abs. 3 BAO in Verbindung mit §  264 Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr.in Alva Karp` | `Dr.in Alva Karp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sheila Nagell` (person)
- `Horner Straße 104, 3623 Ernst, Österreich` (address)
- `Pölzleithner Wirtschaftstreuhand KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `29-285/1127` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/134989.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134989.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Leitgebel  in der Beschwerdesache ÖkR Achmed von Lampe,  Kreuzbach 25, 6441 Köfels, Österreich, vertreten durch WIRTSCHAFTSTREUHAND Steuerberatung GmbH,  Ohlsdorferstraße 18, 4810 Gmunden, über die Beschwerde vom 31. Jänner 2020 gegen den  Bescheid des FA Steiermark Mitte  vom 28. Jänner 2020 betreffend Abweisung eines Antrages auf  Aussetzung der Einhebung gemäß § 212a BAO, Steuernummer 05-972/9664, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Leitgebel` | `Dr.in Huberta Leitgebel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Achmed von Lampe` (person)
- `Kreuzbach 25, 6441 Köfels, Österreich` (address)
- `WIRTSCHAFTSTREUHAND Steuerberatung GmbH` (organisation)
- `FA Steiermark Mitte` (organisation)
- `05-972/9664` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Mag.a Marlies Hilberath, die Richterin Dr.in Suleika Gammerschlag  sowie die fachkundigen Laienrichter Mag. XX und Mag. YY in der Beschwerdesache Univ.-Prof. Hademar Schimonsky.,  Vinzenz-Till-Gasse 138, 4451 Saaß, Österreich, vertreten durch Steuerberatungsgesellschaft., Wien, über die  Beschwerde vom 14. Oktober 2016 gegen die Bescheide des Finanzamtes Österreich (vormals  Finanzamt Graz-Stadt) vom 19. September 2016 betreffend

| Predicted | Gold |
|---|---|
| `Dr.in Suleika Gammerschlag` | `Dr.in Suleika Gammerschlag` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Marlies Hilberath` (person)
- `Univ.-Prof. Hademar Schimonsky.` (person)
- `Vinzenz-Till-Gasse 138, 4451 Saaß, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Graz-Stadt` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/136338.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136338.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Laurentia Wischnowski  in der Beschwerdesache Geraldine Tielschner, MSc,  Johann-Dulnig-Weg 19 - 33, 2732 Würflach, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Kitzbühel Lienz (nunmehr: FA Österreich) vom 12. Dezember 2019, SV-Nr,  betreffend die Abweisung des Antrages auf Zuerkennung der Familienbeihilfe (für die Tochter  B) für den Zeitraum Oktober 2018 bis September 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Laurentia Wischnowski` | `Dr.in Laurentia Wischnowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geraldine Tielschner, MSc` (person)
- `Johann-Dulnig-Weg 19 - 33, 2732 Würflach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/136951.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136951.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Juliette Keisers  in der Beschwerdesache   Daria Oberven, Reschenhof 9, 6622 Tal, Österreich, vertreten durch 1A Steuerberatungs GmbH, Münchner Straße 26,  6130 Schwaz,   über die Beschwerde vom 12. April 2021 gegen den Bescheid des FA Vorarlberg  vom 10. März  2021, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr.in Juliette Keisers` | `Dr.in Juliette Keisers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daria Oberven` (person)
- `Reschenhof 9, 6622 Tal, Österreich` (address)
- `1A Steuerberatungs GmbH` (organisation)
- `FA Vorarlberg` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/137464.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137464.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Louisa Melnicuk  in der Beschwerdesache OStR Dipl. Kff. Martha Mattiesen,  Königsbach 4, 3352 Hohenreith, Österreich, vertreten durch Mag. Natascha Vrabie Rechtsanwältin, Brückenkopfgasse 1/6,  8020 Graz, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Stadt vom 16. Dezember 2015 betreffend Wiederaufnahme des Verfahrens zur  Feststellung der Einkünfte gem. § 188 BAO betreffend 2011-2013 sowie Feststellung der  Einkünfte § 188 BAO 2011 -2013, Steuernummer 81-081/5243   I. zu Recht erkannt:   Der Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens hinsichtlich  Feststellung der Einkünfte 2011-2013 vom 16.12.2015 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Louisa Melnicuk` | `Dr.in Louisa Melnicuk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Dipl. Kff. Martha Mattiesen` (person)
- `Königsbach 4, 3352 Hohenreith, Österreich` (address)
- `Mag. Natascha Vrabie Rechtsanwältin` (person)
- `Finanzamtes  Graz-Stadt` (organisation)
- `81-081/5243` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/137507.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fatima Schensny  in der Beschwerdesache Jaden Bollbuck,  Götzweis 3, 9220 Sonnental, Österreich, über die Beschwerden vom 24. Mai 2021 gegen die Bescheide des Finanzamtes  Österreich vom 30. April 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  und 2019, Steuernummer 93-446/8744, zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO im Sinne der Beschwerdevorentscheidungen vom  9. August 2021 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Fatima Schensny` | `Dr.in Fatima Schensny` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Bollbuck` (person)
- `Götzweis 3, 9220 Sonnental, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `93-446/8744` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/138377.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Richterin Dr.in Elisabeth Hafner als Vorsitzende, die  Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. sowie die fachkundige Laienrichterin Eva  Maiwald-Wanderer und den fachkundigen Laienrichter Mag. Josef Bramer in der  Beschwerdesache Raimund Figgen, Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich, über die Beschwerde vom 13. August 2019  gegen den Bescheid des Finanzamtes Österreich vom 1. August 2019, vertreten durch Ilse  König, Bakk.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Eva  Maiwald-Wanderer` (person)
- `Mag. Josef Bramer` (person)
- `Raimund Figgen` (person)
- `Gruntzelstraße 23, 8223 Buchberg bei Herberstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Ilse  König, Bakk.` (person)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/138666.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138666.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Charlotte Bublies  in der Beschwerdesache des  Mario Bohms, Gruberweg 21, 2372 Gießhübl, Österreich, vertreten durch RA Dr. Rainer Wechselberger, Laubichl 121, 6290  Mayrhofen, über die Beschwerde vom 30. Dezember 2014 gegen die Bescheide des FA Bruck Eisenstadt Oberwart  vom 24. November 2014 betreffend Festsetzung der Normverbrauchsabgabe und Festsetzung  eines Verspätungszuschlages für den Zeitraum 06/2010 sowie Festsetzung der  Kraftfahrzeugsteuer für die Monate 06-12/2010, 01-12/2011, 01-12/2012, 01-12/2013 und 01-

| Predicted | Gold |
|---|---|
| `Dr.in Charlotte Bublies` | `Dr.in Charlotte Bublies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mario Bohms` (person)
- `Gruberweg 21, 2372 Gießhübl, Österreich` (address)
- `RA Dr. Rainer Wechselberger` (person)
- `FA Bruck Eisenstadt Oberwart` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/139225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Marilyn Rehnolt  in der Beschwerdesache der  Sanitär Consee, Am Halterberg 3, 4730 Lindbruck, Österreich, über die Beschwerde vom 17. März 2021 gegen den Bescheid des  Finanzamt Judenburg Liezen  vom 10. November 2020 betreffend Umsatzsteuer 2015 zu Steuernummer  28-493/5599  in der mündlichen Verhandlung am 12. Jännern 2023 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Marilyn Rehnolt` | `Dr.in Marilyn Rehnolt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sanitär Consee` (organisation)
- `Am Halterberg 3, 4730 Lindbruck, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)
- `28-493/5599` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/140274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140274.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Stephanie Stöfhas  in der Beschwerdesache Techn R Cedric Greuel, MBA,  Breitenschützing 2, 9651 Aigen, Österreich, vertreten durch DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger  Straße 2-4, 1090 Wien, über die Beschwerde vom 14. Februar 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel als Vorgängerorganisation des  Finanzamts Österreich Dienststelle Sonderzuständigkeiten vom 11. Jänner 2019 betreffend   Zahlungerserleichterungsansuchen für Glücksspielabgaben und Wettgebühren 2012  Steuernummer 93-237/4757  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Stephanie Stöfhas` | `Dr.in Stephanie Stöfhas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Cedric Greuel, MBA` (person)
- `Breitenschützing 2, 9651 Aigen, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamts Österreich` (organisation)
- `93-237/4757` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/140870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Pamela Hopperdizel, LLB, Liedlschwandt 9, 5121 Hörndl, Österreich, über die Beschwerde vom 18. Oktober 2017  gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr Finanzamt Österreich) vom  19. September 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 46-800/3472  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pamela Hopperdizel, LLB` (person)
- `Liedlschwandt 9, 5121 Hörndl, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `46-800/3472` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/141304.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Georg Künkel, Zirmkogelstraße 2, 9103 Grafenbach, Österreich, vertreten durch Mag. Ingrid Huber, Feldweg 7,  9241 Wernberg, über die Beschwerde vom 9. März 2018 gegen den Bescheid des Finanzamtes  Spittal Villach (nunmehr Finanzamt Österreich) vom  16. Februar 2018 betreffend Einkommensteuer 2011 Steuernummer 81-170/3133  zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Georg Künkel` (person)
- `Zirmkogelstraße 2, 9103 Grafenbach, Österreich` (address)
- `Mag. Ingrid Huber` (person)
- `Finanzamtes  Spittal Villach` (organisation)
- `Finanzamt Österreich` (organisation)
- `81-170/3133` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/141428.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Livia Husing  in der Beschwerdesache der  Dorflex-Textil, Zum See 22, 4281 Schreineredt, Österreich, Abgabenkontonummer 87-574/4251, über die Beschwerde  vom 7. März 2023 gegen den Bescheid des Finanzamt Braunau Ried Schärding  vom 6. Februar 2023 betreffend  Zurückweisung eines Antrages auf Aufhebung des Erkenntnisses des Bundesfinanzgerichts vom  10. August 2022 zu GZ RV/3100240/2010 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Livia Husing` | `Dr.in Livia Husing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dorflex-Textil` (organisation)
- `Zum See 22, 4281 Schreineredt, Österreich` (address)
- `87-574/4251` (tax_number)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Doris Grabmair  in der Beschwerdesache des  Wilhelm Fißenewert, LLM, Hingsham 7, 9184 Gorintschach, Österreich  vertreten durch Rechtsanwalt-X, über die Beschwerde vom  4. Dezember 2019 gegen den als Leistungsgebot gemäß § 6 (2) BAO zur Steuernummer 99- 999/9999 (M.-GmbH i.L.) ergangenen Bescheid des X (jetzt Dienststelle des Finanzamtes  Österreich) vom 5. November 2019 betreffend Heranziehung als Gemeinschuldner für  „Umsatzsteuerveranlagungen und div.

| Predicted | Gold |
|---|---|
| `Dr.in Doris Grabmair` | `Dr.in Doris Grabmair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Wilhelm Fißenewert, LLM` (person)
- `Hingsham 7, 9184 Gorintschach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/142610.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142610.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr.in Emanuela Ungers  in der Beschwerdesache Christina Dennessen,  Lauzilgasse 37 - 54, 3243 Steghof, Österreich, vertreten durch Treufinanz Wirtschaftstreuhand Gesellschaft m.b.H.,  Sternwartestraße 76, 1180 Wien, über die Beschwerde vom 18. August 2022 gegen die  Bescheide des Finanzamtes Österreich vom 2. Februar 2022 und vom 14. Februar 2022,  Steuernummer 98-034/4594, betreffend Umsatz- und Körperschaftsteuer 2017 bis 2019  beschlossen:   Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr.in Emanuela Ungers` | `Dr.in Emanuela Ungers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christina Dennessen` (person)
- `Lauzilgasse 37 - 54, 3243 Steghof, Österreich` (address)
- `Treufinanz Wirtschaftstreuhand Gesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-034/4594` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/142775.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142775.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Laurin Niegeloh  in der Beschwerdesache des  Thaddäus Wischeid, Freudstraße 81, 3442 Neusiedl, Österreich, über die Beschwerde vom 10. November 2022 gegen den Bescheid  des FA St. Johann Tamsweg Zell am See  vom 21. Oktober 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu Steuernummer 18-226/2821  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Laurin Niegeloh` | `Dr.in Laurin Niegeloh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thaddäus Wischeid` (person)
- `Freudstraße 81, 3442 Neusiedl, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `18-226/2821` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/143190.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143190.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner in der Beschwerdesache  Muran de Franceschi, Im Lagerfeld 323T, 4891 Haidach, Österreich, vertreten durch KWT Klagenfurter Wirtschaftstreuhand &  Steuerberatungs KG, Kempfstraße 23, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom  9. Mai 2018 gegen die Bescheide des Finanzamtes Klagenfurt (nunmehr Finanzamt Österreich)  vom 10. April 2018 betreffend die Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2014, Einkommensteuer 2014 sowie über die Festsetzung von  Anspruchszinsen 2014, Steuernummer 51-879/1950 ,  I. zu Recht erkannt:  1.)

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Muran de Franceschi` (person)
- `Im Lagerfeld 323T, 4891 Haidach, Österreich` (address)
- `KWT Klagenfurter Wirtschaftstreuhand &  Steuerberatungs KG` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `51-879/1950` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Judith Brocks  in der Beschwerdesache des  VetR Stephanie Kabak, Zennergasse 325, 9360 Engelsdorf, Österreich, über die Beschwerde vom 12. Juli 2023 gegen den Bescheid des  FA Graz-Stadt  vom 21. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  zu Steuernummer 70-314/9067  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Judith Brocks` | `Dr.in Judith Brocks` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Stephanie Kabak` (person)
- `Zennergasse 325, 9360 Engelsdorf, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `70-314/9067` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/144123.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144123.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Svenja Westkämper  in der Beschwerdesache des  Bartholomäus Dykmanns, Minköfle 2, 5233 Perleiten, Österreich, über die Beschwerde vom 10. August 2023 gegen den Bescheid des  Finanzamt Kirchdorf Perg Steyr  vom 26. Juli 2023 betreffend Einkommensteuer 2021 zu Steuernummer StNr zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Svenja Westkämper` | `Dr.in Svenja Westkämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bartholomäus Dykmanns` (person)
- `Minköfle 2, 5233 Perleiten, Österreich` (address)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/144596.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Jelena Luepken  in der Beschwerdesache HR Mag.a Hemma Pankratius,  Anton Zöhrer-Straße 32, 9141 Pudab, Österreich, über die Beschwerde vom 28. August 2023 gegen den Bescheid des  Finanzamtes Österreich vom 11. August 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 87-214/8742  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Jelena Luepken` | `Dr.in Jelena Luepken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR Mag.a Hemma Pankratius` (person)
- `Anton Zöhrer-Straße 32, 9141 Pudab, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `87-214/8742` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/144625.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sakura Sanli  in der Beschwerdesache Stella Henkels,  Handwerkergasse 8, 9470 Deutsch-Grutschen, Österreich, vertreten durch Mosser & CONFIDA Murtal Steuerberatung GmbH,  Frauengasse 33, 8750 Judenburg, über die Beschwerde vom 4. November 2020 gegen den  Bescheid des Finanzamtes Österreich vom 13. Oktober 2020 betreffend Einkommensteuer  2017 Steuernummer 04-222/2532  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Sakura Sanli` | `Dr.in Sakura Sanli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stella Henkels` (person)
- `Handwerkergasse 8, 9470 Deutsch-Grutschen, Österreich` (address)
- `Mosser & CONFIDA Murtal Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `04-222/2532` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/145135.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Iris Tucholski  in der Beschwerdesache des  Alma Kolesnikowa, Hochsteig 63, 8572 Bärnbach, Österreich, über die Beschwerde vom 12. November 2023 gegen den Bescheid  des FA Schwechat Gerasdorf  vom 2. November 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Steuernummer 98-235/7565  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Iris Tucholski` | `Dr.in Iris Tucholski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alma Kolesnikowa` (person)
- `Hochsteig 63, 8572 Bärnbach, Österreich` (address)
- `FA Schwechat Gerasdorf` (organisation)
- `98-235/7565` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/145271.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145271.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Kordelia Ros  über die Beschwerde des Melina Jakumeit,  Bürgerstraße 28, 3633 Lichtenau, Österreich, vertreten durch fh-wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Linzer Straße 26, 3100 St.Pölten, vom 4. Mai 2017 gegen den Bescheid des Finanzamtes  Finanzamt Innsbruck  als Finanzstrafbehörde vom 6. April 2017 über die Festsetzung von Gebühren und  Auslagenersätzen des Vollstreckungsverfahrens, zu Strafkontonummer 88-706/3272, zu  Recht erkannt:  Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Kordelia Ros` | `Dr.in Kordelia Ros` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melina Jakumeit` (person)
- `Bürgerstraße 28, 3633 Lichtenau, Österreich` (address)
- `fh-wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Innsbruck` (organisation)
- `88-706/3272` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/145727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Liliana Frischeisen  in der Beschwerdesache des  Ramon Karali, über die Beschwerde vom 20. September 2010 gegen den Bescheid Finanzamtes F  (nunmehr: Finanzamt Österreich) vom 6. September 2010 betreffend Einkommensteuer 2008  zu Steuernummer *** zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Liliana Frischeisen` | `Dr.in Liliana Frischeisen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ramon Karali` (person)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Gisela Frohmann  in der Beschwerdesache Tiffany Baudouin, Bakk. techn.,  Unterwollaniger Straße 5, 3804 Bernschlag, Österreich, über die Beschwerde vom 17. Dezember 2019 gegen die Bescheide des  Finanzamtes Österreich vom 16. Dezember 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 bis 2018 zu Steuernummer 25-390/4433  zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Gisela Frohmann` | `Dr.in Gisela Frohmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tiffany Baudouin, Bakk. techn.` (person)
- `Unterwollaniger Straße 5, 3804 Bernschlag, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `25-390/4433` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenA, den RichterB sowie die  fachkundigen Laienrichter C und D in der Beschwerdesache Priv.-Doz.in DDr.in Rafaela Ringart, Floraquellweg 70, 5573 Weißpriach, Österreich,  vertreten durch Silvestri Bau GmbH  WP_GmbH-Adr, vertreten durch Mag. WP über die Beschwerde  vom 22. August 2016 gegen die Bescheide des FA, vertreten durch AB, vom 4. Juli 2016  betreffend Haftung gemäß §§ 9, 80 BAO für Abgaben der GmbH, Steuernummer  38-663/2876  nach Durchführung einer mündlichen Verhandlung am 24. Juni 2020 zu Recht  erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Dr.in Rafaela Ringart` — partial — pred is substring of gold: `Priv.-Doz.in DDr.in Rafaela Ringart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in DDr.in Rafaela Ringart`(person)
- `Floraquellweg 70, 5573 Weißpriach, Österreich`(address)
- `Silvestri Bau GmbH`(organisation)
- `Mag. WP`(person)
- `38-663/2876`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133042.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133042.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Zeno Locherer  in der Beschwerdesache DDr.in Florentine Rimbeck,  Eichenfeldweg 43, 9702 Rudersdorf, Österreich, über die Beschwerden vom 20. Februar 2020 gegen die Bescheide des  Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 24. Jänner 2020 betreffend   1. Zurückweisung des Antrages vom 2.1.2020 auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2014 und   2.

**False Positives:**

- `Dr.in Florentine Rimbeck` — partial — pred is substring of gold: `DDr.in Florentine Rimbeck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Zeno Locherer`(person)
- `DDr.in Florentine Rimbeck`(person)
- `Eichenfeldweg 43, 9702 Rudersdorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135135.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Susanne Staschik  in der Beschwerdesache Serena Meierott, MSc,  Fiedelau 6, 9571 Sirnitz-Sonnseite, Österreich, über die Beschwerde vom 18. Juli 2015 gegen den Bescheid des Finanzamtes  Graz-Umgebung vom 15. Juni 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2009, Steuernummer 32-399/0872, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Susanne Staschik` — partial — pred is substring of gold: `Univ.-Prof.in Dr.in Susanne Staschik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Susanne Staschik`(person)
- `Serena Meierott, MSc`(person)
- `Fiedelau 6, 9571 Sirnitz-Sonnseite, Österreich`(address)
- `Finanzamtes  Graz-Umgebung`(organisation)
- `32-399/0872`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/137652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger  in der Beschwerdesache KommR Manuel Schmeikal,  Fimbabahnweg 6, 8993 Gößl, Österreich, über die Beschwerde vom 13. Juni 2019 gegen den Bescheid des Finanzamt St. Johann Tamsweg Zell am See  vom 3. Juni 2019 über die Rückforderung zu Unrecht bezogener Beträge Familienbeihilfe und  Kinderabsetzbetrag für März 2018 bis Mai 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Priv` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger`(person)
- `KommR Manuel Schmeikal`(person)
- `Fimbabahnweg 6, 8993 Gößl, Österreich`(address)
- `Finanzamt St. Johann Tamsweg Zell am See`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/138980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache OMedR DDr.in Griselda Bultink, vertreten durch Ernst & Young Steuerberatungsgesellschaft  m.b.H., Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 12. Juli 2021 gegen die  Bescheide des Finanzamtes Österreich vom 18. Jänner 2021 bzw. 21. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 bzw. 2019 zu Steuernummer  43-697/2735  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben.

**False Positives:**

- `Dr.in Griselda Bultink` — partial — pred is substring of gold: `OMedR DDr.in Griselda Bultink`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `OMedR DDr.in Griselda Bultink`(person)
- `Ernst & Young Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `43-697/2735`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/140461.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140461.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Madeleine Runke  in der Beschwerdesache Raimund Ondrouch,  Andreas Hammer-Gasse 101, 4150 Hundbrenning, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich – FAÖ) vom 14. Jänner 2020, SV-Nr,  betreffend Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Mai 2019 bis Juli 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Priv` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Madeleine Runke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Madeleine Runke`(person)
- `Raimund Ondrouch`(person)
- `Andreas Hammer-Gasse 101, 4150 Hundbrenning, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt Österreich`(organisation)
- `FAÖ`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/142470.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142470.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Alana Boetger  in der Beschwerdesache Heiko Stefano,  Tyroliaplatz 154, 4924 Nußbaum am Kobernaußer Walde, Österreich, vertreten durch Weger & Partner Steuerberatungs GmbH, Villacher Straße 34  Tür 1, 9800 Spittal/Drau, betreffend Beschwerde vom 8. Februar 2023 gegen den Bescheid des  Finanzamtes Österreich vom 5. Jänner 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 Steuernummer 29-729/5928  beschlossen:   Die Beschwerde vom 8. Februar 2023 wird gemäß § 260 Abs. 1 lit b BAO iVm § 278 Abs. 1 lit a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

**False Positives:**

- `Dr.in Alana Boetger` — partial — pred is substring of gold: `Hon.-Prof.in Dr.in Alana Boetger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Alana Boetger`(person)
- `Heiko Stefano`(person)
- `Tyroliaplatz 154, 4924 Nußbaum am Kobernaußer Walde, Österreich`(address)
- `Weger & Partner Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `29-729/5928`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Dr.in Hon.-Prof.in Susette Wiench  in der Beschwerdesache Sascha Hagdorn,  Kühwörther Wasser 43, 8770 Madstein, Österreich, vertreten durch VertretungsNetz - Erwachsenenvertretung Mag. Julia  Janovsky, Adamgasse 2a/4.

**False Positives:**

- `Dr.in Dr` — partial — pred is substring of gold: `Dr.in Dr.in Hon.-Prof.in Susette Wiench`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Dr.in Hon.-Prof.in Susette Wiench`(person)
- `Sascha Hagdorn`(person)
- `Kühwörther Wasser 43, 8770 Madstein, Österreich`(address)
- `Mag. Julia  Janovsky`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/145175.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145175.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Melina Groesche  in der Beschwerdesache Franka Neuleitner, BEd,  In der Dorfwiese 23, 6373 Jochberg, Österreich, über die Beschwerde vom 27. Juli 2015 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 23. Juni 2015 betreffend Einkommensteuer 2013, Steuernummer  12-249/3817, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr.in Univ` — partial — pred is substring of gold: `Dr.in Univ.-Prof.in Melina Groesche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Univ.-Prof.in Melina Groesche`(person)
- `Franka Neuleitner, BEd`(person)
- `In der Dorfwiese 23, 6373 Jochberg, Österreich`(address)
- `Finanzamtes`(organisation)
- `12-249/3817`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/146363.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146363.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Laetitia Raffler  in der Beschwerdesache Dipl.-Ing. DDr.in Karina Frischmann,  Apfelbrunngraben 8, 3543 Krumauer Waldhütten, Österreich, über die Beschwerde vom 3. Juli 2024 gegen den Bescheid des Finanzamtes  Österreich vom 18. Juni 2024, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  den Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum "ab Juli 2020"(= angefochtener  Zeitraum 07/2020 bis 06/2024) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Karina Frischmann` — partial — pred is substring of gold: `Dipl.-Ing. DDr.in Karina Frischmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Laetitia Raffler`(person)
- `Dipl.-Ing. DDr.in Karina Frischmann`(person)
- `Apfelbrunngraben 8, 3543 Krumauer Waldhütten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/148356.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148356.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Verena Heyd, Dr.Georg Prader Straße 5, 9862 Oberkremsberg, Österreich, vom 27. Februar 2025 (Poststempel) gegen das Straferkenntnis der  belangten Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 22.  Jänner 2025, GZ. MA67/GZ/2024, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt  Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Dr.Georg Prader Straße` — partial — pred is substring of gold: `Dr.Georg Prader Straße 5, 9862 Oberkremsberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Verena Heyd`(person)
- `Dr.Georg Prader Straße 5, 9862 Oberkremsberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Stadt  Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/149765.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Monika Ahorn in der Beschwerdesache  DDr.in Hedwig Novikovas, Am Lafnitzgrund 59, 5660 Hopfberg, Österreich, vertreten durch Dr. Thomas Krankl, Lerchenfelder Straße  120/2/28, 1080 Wien, über die Beschwerde vom 22. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 13. Jänner 2021 Einkommensteuer (Arbeitnehmerveranlagung)  2019 (Steuernummer 90-850/9744 ) nach Durchführung einer mündlichen Verhandlung am  07.11.2025 in Anwesenheit des Schriftführers Dietmar Gratz  I. beschlossen:  Der Vorlageantrag vom 23.11.2022 wird als gegenstandslos erklärt (§ 85 Abs. 2 iVm § 256 Abs.  3 iVm § 264 Abs. 4 lit. d BAO).

**False Positives:**

- `Dr.in Hedwig Novikovas` — partial — pred is substring of gold: `DDr.in Hedwig Novikovas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Monika Ahorn`(person)
- `DDr.in Hedwig Novikovas`(person)
- `Am Lafnitzgrund 59, 5660 Hopfberg, Österreich`(address)
- `Dr. Thomas Krankl`(person)
- `Finanzamtes Österreich`(organisation)
- `90-850/9744`(tax_number)

</details>

---

## `Case Name Reference` 💣

**F1:** 0.003 | **Precision:** 0.211 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `5d4ce98c`  
**Description:**
Captures person names appearing after 'Rs' (Rechtssache) or 'Rs.' which often refer to case names derived from the plaintiff/defendant.

**Content:**
```
(?:Rs\.?\s+|Rechtssache\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.211 | 0.002 | 0.003 | 19 | 4 | 15 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 15 | 2242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_85`)


Der  VwGH verneinte dies unter Hinweis auf Art. 283 Abs. 1 lit. c MwStSystRL und die Rs Schmelz.

| Predicted | Gold |
|---|---|
| `Schmelz` | `Schmelz` |

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Eugenia Vesen` | `Eugenia Vesen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Apollogasse 213, 5522 Lammertal, Österreich` (address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eleonore Rudloph, Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauerstrasse 39/1/12, 1220 Wien, und Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden je vom  25.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 26. Juli 2016  betreffend Haftung für Abzugsteuer gemäß § 99 EStG 1988 für die Jahre 2012-2014 nach  Durchführung einer öffentlichen mündlichen Verhandlung am 26.04.2021 zu Recht erkannt:   I. a.

| Predicted | Gold |
|---|---|
| `Eleonore Rudloph` | `Eleonore Rudloph` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Kleinhaugsdorf 18, 8481 Pichla bei Sankt Veit, Österreich` (address)
- `Dr. Michael Kotschnigg` (person)
- `Braschel & Braunstein Steuerberatung und  Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes für Großbetriebe` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/135680.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135680.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Karen Knollmüller, Am Weitblick 15, 5145 Kirchweg, Österreich, vertreten durch Saremba & Schinogl Stb.u.Buchh.KG,  Mießtaler Straße 30, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 31. Mai 2021  gegen den Bescheid des Finanzamtes Österreich vom 27. April 2021 betreffend Festsetzung  einer Zwangsstrafe (Steuernummer 47-692/3685 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karen Knollmüller` | `Karen Knollmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Am Weitblick 15, 5145 Kirchweg, Österreich` (address)
- `Saremba & Schinogl Stb.u.Buchh.KG` (organisation)
- `Finanzamtes Österreich` (organisation)
- `47-692/3685` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Frederike Wegerth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_19`)


Aufgrund der  Fachliteratur (Beiser und Kanduth-Kristen) sowie der EuGH-Rechtsprechung in der Rs  Stoppelkamp vertrat der Beschwerdeführer die Ansicht, dass ein Unternehmen dort betrieben  werde, wo sich das vermietete Grundstück befinde.

**False Positives:**

- `Stoppelkamp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_53`)


3. Aufgrund kritischer Betrachtungen in der Literatur, ob diese Regelung mit dem Primärrecht  in Einklang steht, wurde dem EuGH die Rs Schmelz vom Unabhängigen Finanzsenat zur  Vorabentscheidung vorgelegt.

**False Positives:**

- `Schmelz ` — partial — gold is substring of pred: `Schmelz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schmelz`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_63`)


Der EuGH ist in der Rs Stoppelkamp zum Ergebnis gekommen, dass insoweit der Sitz der  wirtschaftlichen Tätigkeit bekannt ist und sich außerhalb des Landes des Leistungsempfängers  befindet, ein etwaiger privater (Zweit-)Wohnsitz innerhalb dieses Landes keine  Berücksichtigung finden kann (Rn 28).

**False Positives:**

- `Stoppelkamp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_72`)


SWK 2017, 939) geht, an die Rs Stoppelkamp anknüpfend, von der  Annahme aus, dass der Sitz der wirtschaftlichen Tätigkeit und eine feste Niederlassung bei  einer Vermietungstätigkeit am Ort des Mietobjektes liegt.

**False Positives:**

- `Stoppelkamp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_90`)


Der BFH stützte seine Entscheidung auf die EuGH-Judikatur in der Rs Schmelz und kam zum  eindeutigen Ergebnis, dass „die Vermietung einer Wohnung jedenfalls für die Anwendung der  Kleinunternehmerregelung weder als ansässigkeits- noch als niederlassungsbegründend  anzusehen“ ist.

**False Positives:**

- `Schmelz ` — partial — gold is substring of pred: `Schmelz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFH`(organisation)
- `Schmelz`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_92`)


Die Ansicht des Beschwerdeführers, die in erster Linie auf deren Interpretation der Rs  Stoppelkamp und der darauf aufbauenden Meinung von Beiser beruht, kann nicht geteilt  werden.

**False Positives:**

- `Stoppelkamp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_93`)


Aus der Rs Stoppelkamp kann nach Ansicht des Bundesfinanzgerichtes nicht abgeleitet  werden, dass sich der Sitz der wirtschaftlichen Tätigkeit nicht am Wohnsitz des  Steuerpflichtigen befinden kann.

**False Positives:**

- `Stoppelkamp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_94`)


Zudem ist nach der Rs Stoppelkamp der Wohnsitz in jenen  Fällen zur Beurteilung der Ansässigkeit heranzuziehen, wenn weder Sitz der wirtschaftlichen  Tätigkeit noch feste Niederlassung feststellbar sind.

**False Positives:**

- `Stoppelkamp ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_96`)


Ein Ergebnis, das nach der Rn 70 der Rs Schmelz mit der  Ausnahmeregelung für Kleinunternehmer nicht in Einklang zu bringen ist.

**False Positives:**

- `Schmelz ` — partial — gold is substring of pred: `Schmelz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schmelz`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/141359.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141359.1_88`)


So legt auch Art. 1 Abs. 1 der VO  904/2010/EU fest, dass die Verordnung die Modalitäten der Zusammenarbeit zwischen den  Mitgliedstaaten und der Kommission regelt. Daraus ergibt sich, dass das zwischenstaatliche  Amtshilfeverfahren schon insofern einer Akteneinsicht nicht zugänglich ist, auch wenn es sich  bei der beschwerdeführenden Gesellschaft unzweifelhaft um ein dem österreichischen  Abgabenrecht unterworfenes Rechtssubjekt handelt.   In der Rs Sabou, EuGH 22.10.2013, C-276/12, hat sich der EuGH in Zusammenhang mit der  insofern vergleichbaren Amtshilferichtline 77/799/EWG bereits mit Fragen des Rechtschutzes  von Abgabenpflichtigen auseinandergesetzt und im Tenor festgehalten, dass das Unionsrecht  in Zusammenspiel mit dem Grundrecht auf rechtliches Gehör dem Steuerpflichtigen nicht das  Recht verleiht, über ein Amtshilfeersuchen informiert zu werden.

**False Positives:**

- `Sabou` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_276`)


Entsteht mangels Gefährdung gar keine Steuerschuld, bedarf es keiner Rechnungsberichtigung  (vgl. zuletzt EuGH 8.12.2022, C-378/21, Rs Mergel Bau GmbH und Zorn in RdW 2023, 225).

**False Positives:**

- `Mergel Bau Gmb` — partial — pred is substring of gold: `Mergel Bau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mergel Bau GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/141978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141978.1_79`)


Jedenfalls seit dem EuGH-Urteil vom 15.07.2004, Rs Lenz, war die Besteuerung von  ausländischen Kapitalerträgen immer wieder Thema in den Medien.

**False Positives:**

- `Lenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/145828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145828.1_34`)


Zwei Entscheidungen dokumentieren, dass diese Rechtsansicht auch vom EUGH und dem  deutschen Bundesfinanzhof geteilt wird:  In der Entscheidung vom 15.11.2012 in der Rechtssache Ines Zimmermann gegen das  Finanzamt Steglitz (Rechtssache C-174/11) stellte der Europäische Gerichtshof fest, dass es der  6.

**False Positives:**

- `Ines Zimmermann ` — partial — gold is substring of pred: `Ines Zimmermann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ines Zimmermann`(person)
- `Finanzamt Steglitz`(organisation)
- `Europäische Gerichtshof`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/145828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145828.1_38`)


Der deutsche Bundesfinanzhof kommt im Urteil zur Rechtssache Marietheres Driessen gegen  das Finanzamt Kleve (Az. V R 7/11 - Anlage 3) zu dem gleichen Ergebnis.

**False Positives:**

- `Marietheres Driessen ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

</details>

---

## `Name with Suffix Extraction` 💣

**F1:** 0.003 | **Precision:** 0.007 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `8c92f06c`  
**Description:**
Captures names followed by a comma and a degree/suffix (e.g., 'Name, Bakk. techn.') which are common in legal texts, extracting the full name and suffix.

**Content:**
```
(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)\s*,\s*(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.007 | 0.002 | 0.003 | 566 | 4 | 562 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 562 | 2435 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Florian Abbruzzese, BA` | `Florian Abbruzzese, BA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Nicola Folprecht` (person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_196`)


Zur Bemessungsgrundlage und damit zum Bescheidspruch gehört ggf auch die Anführung des  Zeitraums oder des Zeitpunktes, für den oder auf den bezogen die Abgabe festgesetzt wird  (vgl. Ellinger/Sutter/Urtz, BAO3, § 198, Rz 14).

**False Positives:**

- `Urtz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_200`)


In der Bemessungsgrundlage wird daher für den jeweils zu erlassenden Bescheid  ein bestimmter Sachvorgang, Zeitpunkt oder Zeitraum festgelegt (vgl. Stoll, BAO, 2078).

**False Positives:**

- `Stoll, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_254`)


Die Abgabenbehörde trägt zwar die  Feststellungslast für alle Tatsachen, die vorliegen müssen, um einen Abgabenanspruch geltend  zu machen, doch befreit dies die Partei nicht von ihrer Offenlegungs- und Mitwirkungspflicht  (vgl. Ritz, BAO5, § 115 Tz 4 und 7; VwGH 18.1.1998, 95/13/0069).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_257`)


Nach ständiger Rechtsprechung  genügt es dabei, von mehreren Möglichkeiten jene als erwiesen anzunehmen, die gegenüber  allen anderen Möglichkeiten eine überragende Wahrscheinlichkeit oder gar Gewissheit für sich  hat und alle anderen Möglichkeiten absolut oder mit Wahrscheinlichkeit ausschließt oder  zumindest weniger wahrscheinlich erscheinen lässt (vgl. Ritz, BAO5, § 167 Rz 8, mit Hinweisen  auf die Rechtsprechung).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_97`)


Unger in Althuber/Tanzer/Unger, BAO-HB, § 224, 654).

**False Positives:**

- `Unger, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_98`)


Ritz BAO6, § 224 Tz 1)  Zuständig für die Geltendmachung abgabenrechtlicher Haftungen sind jene Abgabenbehörden,  in deren örtliche und sachliche Zuständigkeit die Einhebung der haftungsverfangenen Abgabe  fällt. (Unger in Althuber/Tanzer/Unger, BAO-HB, § 224, 655)

**False Positives:**

- `Unger, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_115`)


(Ritz, BAO6, § 224, Tz.4)  Gemäß § 238 Abs. 1 BAO verjährt das Recht eine fällige Abgabe einzuheben …binnen fünf  Jahren nach Ablauf des Kalenderjahres , in welchem die Abgabe fällig geworden ist, keinesfalls  jedoch früher als das Recht zur Festsetzung der Abgabe.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_131`)


Eine solche Bekanntmachung hat durch Zusendung einer Ausfertigung (Ablichtung) des  maßgeblichen Bescheides über den Abgabenanspruch, allenfalls durch Mitteilung des  Bescheidinhaltes zu erfolgen (vgl zB Ellinger/ Wetzel, BAO, 194).

**False Positives:**

- `Wetzel, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_133`)


vgl auch Stoll, JBl 1982, 9). (Ritz, BAO6, § 248, Tz. 8)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_146`)


(Ritz, BAO6, § 9, Tz. 1) die Frage der Involvierung in allfällige steuerliche Malversationen kann  lediglich bei der Übung des Ermessens berücksichtigt werden, was das FA im Haftungsbescheid  auch getan hat, indem Abgabenvorschreibungen vor Aufnahme der Geschäftsführungstätigkeit  dem BF nicht vorgeschrieben wurden.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_165`)


(Ritz, BAO6, § 248, Tz.5 unter Verweis auf VwGH vom  30. Oktober 2001,98/14/0142)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_175`)


(Ritz, BAO6, § 9 Tz.15 mwN)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_176`)


Er hat - auch in dem Zeitpunkt, als er  seine Anteile veräußerte - keine Maßnahmen gesetzt um seine Geschäftsführertätigkeit  frühzeitig zu beenden und damit den Zeitraum der Behinderung (Ritz, BAO6, § 9 Tz 17 mwN)  bei der Ausübung seiner Tätigkeit so kurz wie möglich zu halten.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_39`)


Der Einstieg in FinanzOnline bzw. das tatsächliche Einsehen der Databox durch den  FinanzOnline-Teilnehmer durch konkretes Öffnen, Lesen oder Ausdrucken des Bescheides ist  dabei irrelevant (UFS 22.07.2013, RV/0002-F/13, BFG 24.11.2017, RV/7104134/2017, BFG  18.09.2018, RV/7103033/2018, vgl. weiters Ritz, BAO6, § 98 Tz 4).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/128877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128877.1_51`)


Ein Antrag auf Verlängerung der Berufungsfrist nach § 245 Abs. 3 BAO ist ein Anbringen zur  Geltendmachung von Rechten im Sinne des § 85 Abs. 1 BAO (vgl. Ritz, BAO6, § 245 Tz 12).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_106`)


Schon bisher wies Ritz zu Recht darauf hin (Ritz, BAO5, § 115 Tz 13), dass einen Bf. auch dann  eine erhöhte Mitwirkungspflicht trifft, wenn ungewöhnliche Verhältnisse vorliegen (vgl. VwGH  28.5.2002, 97/14/0053;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_35`)


Die rückwirkende Berücksichtigung des Herabsetzungsbetrages (iSd §  212a Abs. 9 drittletzter Satz) hat von Amts wegen zu erfolgen (Ritz, BAO6, § 212a, Rz. 34).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_6`)


Dem Beschwerdeführer (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, nach einer bei der  Zulassungsbesitzerin des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen  Vienna eingeholten Lenkerauskunft (§ 2 Wiener Parkometergesetz 2006) mit Strafverfügung  vom 18. Dezember 2019, MA 67/123/2019, angelastet, er habe das Fahrzeug am 11. Oktober  2019 um 13:54 Uhr in der gebührenpflichtigen Kurzparkzone in 1100 Wien, Theodor-Sickel- Gasse ggü 14, ohne einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und  demnach die Parkometerabgabe fahrlässig verkürzt.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_14`)


Ritz, BAO, Kommentar, 6. Auflage, Rz 12a zu § 264).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_56`)


Der  Vorrang der Rechtsrichtigkeit rechtfertige aber keine nur dieses Kriterium berücksichtigende  Ermessensübung (Ritz, BAO, § 303 Tz 63).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_123`)


Ritz, BAO, § 303 Tz 74).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_118`)


vgl zudem die bei Ritz, BAO6 § 303 Rz 31 angeführten Nachweise der  Rsp des VwGH).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_134`)


vgl zudem die bei  Ritz, BAO6 § 114 Rz 9 angeführten Nachweise der Rsp des VwGH).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_49`)


Eine Bescheidbeschwerde ist insbesondere unzulässig, wenn ein Bescheid nicht wirksam  geworden ist, weil er an eine nicht mehr bestehende juristische Person gerichtet ist (vgl Ritz,  BAO6, § 260 Tz 8;

**False Positives:**

- `Ritz,  BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_131`)


Die Regelung des  § 162 BAO stellt somit eine Ausnahme von der freien Beweisführung dar und führt zu einer  Umkehr der Beweislast (Ellinger/Iro/Kramer/Sutter/Urtz, BAO, § 162 Anm. 6).

**False Positives:**

- `Urtz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_54`)


Bei Bescheiden betreffend die Verfügung der Wiederaufnahme gemäß § 303 BAO ist § 250  Abs 1 lit b und c BAO inhaltsleer, weil hier die Anfechtung nur die Aufhebung des  angefochtenen Bescheides bezwecken kann, es somit nicht mehrere Beschwerdepunkte geben  kann bzw. weil eine Änderung solcher Bescheide nicht in Betracht kommt - die  Bescheidbeschwerde kann nur auf Aufhebung gerichtet sein (vgl. Ritz, BAO6, § 250 Tz 10; sowie  VwGH 28.1.1998, 96/13/0081).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_55`)


Die Angabe gemäß § 250 Abs. 1 lit d BAO soll die Behörde in die Lage versetzen, klar zu  erkennen, aus welchen Gründen der Beschwerdeführer die Bescheidbeschwerde für  gerechtfertigt bzw. für Erfolg versprechend hält.   Keine Begründung im Sinne des § 250 Abs. 1 lit d BAO stellt etwa dar die nicht näher  begründete Behauptung, der Bescheid sei ungesetzlich unrichtig oder er entspreche nicht dem  Gesetz (vgl. Ritz, BAO6, § 250 Tz 14 f und die dort wiedergegebene Judikatur des  Verwaltungsgerichtshofes)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_72`)


Ellinger-Iro-Kramer-Sutter-Urtz, BAO, 1. Band, Tz 10ff zu § 115).

**False Positives:**

- `Urtz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_137`)


Die  Entscheidung liegt eben (auch) dem Grund nach im Ermessen der Behörde“ (Stoll, BAO, § 48,  512 f zum Handlungsermessen).

**False Positives:**

- `Stoll, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_3`)


Entscheidungsgründe  Mit Bescheiden des Finanzamtes Wien 1/23 jeweils vom 9. August 2019 wurden über die  KommR Eckard Gaiss, Bakk. phil. (in weiterer Folge: Bf.) erste Säumniszuschläge für Umsatzsteuer 05/2019 in Höhe  von € 209.028,38 (Säumniszuschlag € 4.180,57), für Werbeabgabe 05/2019 in Höhe von €  177.156,96 (Säumniszuschlag € 3.543,14), für Lohnsteuer 06/2019 in Höhe von € 85.47466  (Säumniszuschlag € 1.709,49) und für Dienstgeberbeitrag 06/2019 in Höhe von € 20.536,18  (Säumniszuschlag € 410,72), Säumniszuschläge gesamt € 9.843,92, festgesetzt, da die  angeführten Abgabenschuldigkeiten nicht innerhalb der Frist 15. Juli 2019 entrichtet worden  sind.

**False Positives:**

- `Eckard Gaiss, Bakk. phil.` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 1/23`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_15`)


Am 15. Juli 2019 hat unsere Mandantschaft via Finanz Online einen Antrag auf Übertragung an  die KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10)  iHv EUR 336.224,91 eingebracht (Hinweis: Betreffend die Martinssen Versicherung GmbH wurde ebenfalls ein  Säumniszuschlag festgesetzt und ist eine Beschwerdevorentscheidung ergangen;

**False Positives:**

- `Eckard Gaiss, Bakk. phil.` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_31`)


Als Beilage dürfen wir Ihnen nachfolgende Unterlagen übermitteln:   XML-Datenträger UVA 05/2019 betreffend die Gerstbreu Umwelt GmbH  Fax an das Finanzamt 13.08.2019 inkl. UVA 05/2019 und Produktionsübermittlung  vom 12.Juli 2019 betreffend die Gerstbreu Umwelt GmbH inkl. Antrag betreffend die Übertragung  eines Geldbetrages für die KommR Eckard Gaiss, Bakk. phil.  und für die Martinssen Versicherung GmbH vom 15. Juli 2019 inkl.  Übermittlung der Rechnungen mit den größeren Vorsteuerbeträgen inkl.  Faxbestätigung vom 13. August 2019  Weiters stellen wir den Antrag den Säumniszuschlag in Höhe von EUR 9.843,92 herabzusetzen  bzw. nicht festzusetzen, da unserer Mandantschaft aus oben angeführten Gründen an der  Versäumnis kein grobes Verschulden trifft.

**False Positives:**

- `Eckard Gaiss, Bakk. phil.` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `Finanzamt`(organisation)
- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Martinssen Versicherung GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_52`)


Grobes Verschulden:   Zunächst ist festzustellen, dass ein Antrag gemäß § 217 Abs. 7 BAO auch in einer Beschwerde  gegen den Säumniszuschlagsbescheid gestellt werden kann (VwGH 31.5.2011, 2007/15/0169  mit Hinweis auf Ritz, BAO-Kommentar5, § 217 Tz 65 mwN) und diesfalls in der Entscheidung  über die Beschwerde zu berücksichtigen ist;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_54`)


Wird ein Antrag nach § 217 Abs. 7 BAO in der Beschwerde oder im  Vorlageantrag gestellt, ist im Sinne des § 280 BAO in der Berufungserledigung (Entscheidung  über die Beschwerde) darüber abzusprechen (siehe Ritz, BAO-HB, Seite 155;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_59`)


Grobes  Verschulden fehlt, wenn überhaupt kein Verschulden oder nur leichte Fahrlässigkeit vorliegt  (vgl. Ritz, BAO-Kommentar5, § 217, Tz 45).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_62`)


Entscheidend ist  diesfalls, ob der Partei selbst (bzw. ihrem Vertreter) grobes Verschulden, insbesondere grobes  Auswahl- oder Kontrollverschulden anzulasten ist (vgl. auch hiezu Ritz, BAO-Kommentar5, §  217 Tz 46;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


Der steuerliche Vertreter hat weiter ausgeführt, dass am 15. Juli 2019 unsere Mandantschaft  (aus dem Zusammenhang ist davon auszugehen, dass es sich bei der Mandantschaft hier  wieder um die Firma Gerstbreu Umwelt GmbH handelt) via FinanzOnline einen Antrag auf Übertragung an die  KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10) iHv  EUR 336.224,91 eingebracht hat (Hinweis: Laut steuerlichem Vertreter soll betreffend die Martinssen Versicherung GmbH ebenfalls ein Säumniszuschlag festgesetzt worden sein und sei eine  Beschwerdevorentscheidung ergangen, wogegen ein Vorlageantrag und Antrag gem. § 217 (7)  BAO eingebracht worden sei).

**False Positives:**

- `Eckard Gaiss, Bakk. phil.` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gerstbreu Umwelt GmbH`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_39`)


Die Begründung muss in einer Weise erfolgen, dass der Denkprozess, der in der behördlichen  Erledigung seinen Niederschlag findet, sowohl für die Partei, als auch für die Höchstgerichte  nachvollziehbar ist (Ritz, BAO6, § 3 Tz 15 unter Verweis auf VwGH-Judikatur).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_44`)


Das BFG sieht mit Ritz (Ritz, BAO6, § 274, Tz 5) im Anbot von Beweisen in einer mündlichen  Verhandlung in der Beschwerde bzw. im Vorlageantrag einen Antrag auf Durchführung einer  mündlichen Verhandlung vor dem Einzelrichter.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_52`)


(Ritz, BAO6,  § 303, Tz.55 mwN)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_191`)


Die vom FFG erstellte Forschungsbestätigung spricht über das Voliegen der Voraussetzungen  des § 108c EStG 1988 dem Grunde nach, nicht jedoch über die Bemessungsgrundlage für die  Forschungsprämie ab (vgl. Ritz, BAO6 § 118a Rz. 4)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_284`)


Gemäß Ritz, BAO6 § 93 Rz.

**False Positives:**

- `Gemäß Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_45`)


Zweck der Wiederaufnahme  wegen Neuerungen ist - wie schon nach der Regelung vor dem FVwGG 2012 – die  Berücksichtigung von bisher unbekannten, aber entscheidungswesentlichen  Sachverhaltselementen /Ritz, BAO5 §303 Tz24).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_82`)


Der Neuerungstatbestand fordert, dass  (entscheidungswesentliche) Tatsachen oder Beweismittel im (abgeschlossenen) Verfahren neu  hervorkommen und zwar in jenem Verfahren, dass bereits durch Bescheid abgeschlossenen ist  (vgl. Ritz, BAO5, § 303 Tz 45).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_84`)


Was das „neu Hervorkommens“ von Tatsachen und Beweismitteln nach § 303 Abs. 1 BAO  idF FVwGG 2012 anbelangt, gibt es zwei Kommentarmeinungen:   Nach Ritz ist sowohl bei der amtswegigen als auch bei der antragsgebundenen  Wiederaufnahme, einzig der Wissenstand der Abgabenbehörde, bezogen auf die Aktenlage im  Zeitpunkt der Erlassung des das Verfahren abschließenden Bescheides maßgebend (vgl. Ritz,  BAO5, § 303 Tz 45 und die dort angeführte Judikatur).

**False Positives:**

- `Ritz,  BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_90`)


Durch die Vereinheitlichung der Wiederaufnahmevoraussetzungen sei die  Judikatur, wonach für eine Antragswiederaufnahme die Wiederaufnahmsgründe für die Partei  neu hervorkommen müssten, überholt (vgl. Ritz, BAO5, § 303 Tz 47).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_112`)


Die Harmonisierung erfolgte in der Weise, dass ab 1.1.2014  die für die amtswegige Wiederaufnahmen geltenden Voraussetzungen (Ermessen,  Verjährungsfristen, kein Verschulden, keine Notwendigkeit der formellen Rechtskraft) auch für  die Wiederaufnahme auf Antrag gelten (vgl. Ritz, BAO5, § 303 Tz 2).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_116`)


Insoweit Ritz unter Hinweis auf die Judikatur des Verwaltungsgerichtshofes (vgl. Ritz,  BAO5, § 303, Tz 46) die Ansicht vertritt, maßgebend für das Hervorkommen neuer Tatsachen  und Beweismittel sei einzig der Wissenstand der Abgabenbehörde, bezogen auf die Aktenlage  im Zeitpunkt der Erlassung des das Verfahren abschließendes Bescheides, ist festzuhalten, dass  die von ihm zitierte Judikatur ausschließlich zur amstwegigen Wiederaufnahme des Verfahrens  nach § 303 Abs. 4 BAO alte Fassung ergangen ist.

**False Positives:**

- `Ritz,  BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_119`)


Weshalb dieser Judikatur „als Folge der  Gesetzesänderung „der Boden entzogen sein soll“, ist für das Bundesfinanzgericht nicht  ersichtlich, zumal Ritz und das Bundesministerium für Finanzen schon zur § 303 Abs. 1 BAO alte  Fassung nachstehende - von der Judikatur des Verwaltungsgerichtshofs abweichende -  Rechtsansicht vertreten haben (vgl. Ritz, BAO4, § 303 Tz 27 und vgl. Ritz, BAO5, § 303 Tz 47):     „

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation
- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesministerium für Finanzen`(organisation)
- `Verwaltungsgerichtshofs`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_155`)


Zum Obiter dictum des VwGH 19.10, 2014/15/0058, wonach für die Wiederaufnahme auf  Antrag die Sicht des Antragstellers maßgebend sei, siehe auch Ritz, BAO, 6.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_3`)


Entscheidungsgründe  Die Jaroslaw Lanwermeyer, MSc Bakk. iur. (im Folgenden kurz Beschwerdeführerin=Bf.) wurde mit Gesellschaftsvertrag  vom Dat1 in der Rechtsform einer Kommanditgesellschaft gegründet.

**False Positives:**

- `Entscheidungsgründe  Die Jaroslaw Lanwermeyer, MSc` — positional overlap with gold: `Jaroslaw Lanwermeyer, MSc Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jaroslaw Lanwermeyer, MSc Bakk. iur.`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Hademar Berking, Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Hademar Berking, Dr.` — partial — gold is substring of pred: `Hademar Berking`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Hademar Berking`(person)
- `Dr.-Karl-Schleinzer-Straße 28, 5231 Oberharlochen, Österreich`(address)
- `Mag. Margot Artner`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_25`)


Ritz, BAO-Kommentar, 5. Auflage, Rz 13 und  17 zu § 26; uvm).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130585.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130585.1_29`)


Dass die  Antragstellerin selbst die Aussichtslosigkeit nicht erkennt oder nicht erkennen kann, ist dabei  ohne Bedeutung (so Ritz, BAO6 zu § 292 Rz 24 unter Verweis auf Bydlinski in Fasching/Konecny,  Zivilprozessgesetze3 II/1, § 63 ZPO Rz 20).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Annette Reeners`(person)
- `Räuflach 3, 8731 Schattenberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_10`)


Entscheidungsgründe  Verfahrensgang:  Der Magistrat der Stadt Wien, MA 67, lastete der Beschwerdefüherin (Bf.) unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 31.10.2019 an, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 02.09.2019 um 14:43 Uhr in der  gebührenpflichtigen Kurzparkzone in 1140 Wien, Penzinger Straße 157, ohne einem für den  Beanstandungszeitpunkt gültigen Parkschein abgestellt.  Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2 Parkometerabgabe iVm § 4 Abs. 1  Wiener Parkometergesetz 2006 wurde über die Bf. eine Geldstrafe iHv € 60,00 und für den Fall  der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden verhängt.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130620.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130620.1_51`)


Ein Antrag auf Verlängerung der Frist zur Einbringung eines Vorlageantrages nach § 264 Abs 4  lit a BAO iVm § 245 Abs 3 BAO ist ein Anbringen zur Geltendmachung von Rechten im Sinne  des § 85 Abs 1 BAO (vgl. Ritz, BAO6, § 245 Tz 12).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130685.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130685.1_27`)


Mit Straferkenntnis vom 25. August 2020 wurde der Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung und wegen Verletzung des § 5  Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006  eine Geldstrafe von € 60,00 und für den Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von  14 Stunden verhängt.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130697.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Franz Trockenbrot,  Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich  vom 15. März 2020, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 10. März 2020,  MA67/000/2019, wegen der Verwaltungsübertretung gemäß § 9 Abs. 2 Wiener  Kontrolleinrichtungenverordnung iVm § 4 Abs. 3 Wiener Parkometergesetz 2006, nach  Durchführung einer mündlichen Verhandlung am 30. Juni 2020, im Beisein der Schriftführerin  S., zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Erkenntnis bestätigt.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Franz Trockenbrot`(person)
- `Franz Ehrenhöfer-Gasse 21, 4974 Hübing, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_19`)


Da ab dem Zeitpunkt der in den Hauptsachen ergangenen  Beschwerdeerledigungen eine Bewilligung der Aussetzung nicht mehr in Betracht kommt,  waren die Aussetzungsanträge als unbegründet abzuweisen (sh. Ritz, BAO, § 212a Rz. 12).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_157`)


auch dürfen Sachverhalte nicht allein deshalb einer abgabenbehördlichen Entscheidung  zugrunde gelegt werden, weil sie von der Partei außer Streit gestellt worden sind  (Ellinger/Iro/Kramer/Sutter/Urtz, BAO3 § 115 Rz 1f).

**False Positives:**

- `Urtz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_10`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, MA 67, erkannte den Beschwerdeführer (Bf.) mit  Straferkenntnis vom 18. Juni 2020, MA67/000/2020, für schuldig, das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna am 3. Jänner 2020 um 21:37 Uhr in  der gebührenpflichtigen Kurzparkzone in 1010 Wien, Bellariastraße 8, Nebenfahrbahn, ohne  einen für den Beanstandungszeitpunkt gültigen Parkschein abgestellt und demnach die  Parkometerabgabe fahrlässig verkürzt zu haben.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_9`)


Entscheidungsgründe  Verfahrensgang:  Der Beschwerdeführerin (Bf.) wurde vom Magistrat der Stadt Wien, MA 67, unter  Zugrundelegung der Anzeigedaten des Kontrollorgans KO der Parkraumüberwachung der  Landespolizeidirektion Wien mit Strafverfügung vom 13. August 2020,  MA67/206700430919/2020, angelastet, sie habe das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen Vienna am 20. Mai 2020 in der gebührenpflichtigen Kurzparkzone in  1110 Wien, Simmeringer Hauptstraße 152, ohne einem für den Beanstandungszeitpunkt 15:11  Uhr gültigen Parkschein abgestellt und demnach die Parkometerabgabe fahrlässig verkürzt.

**False Positives:**

- `Stadt Wien, MA` — positional overlap with gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Landespolizeidirektion Wien`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_59`)


Nach der ständigen Rechtsprechung  des Verwaltungsgerichtshofes genügt es, von mehreren Möglichkeiten jene als erwiesen  anzunehmen, die gegenüber allen anderen Möglichkeiten eine überragende  Wahrscheinlichkeit oder gar Gewissheit für sich hat und alle anderen Möglichkeiten absolut  oder mit Wahrscheinlichkeit ausschließt oder zumindest weniger wahrscheinlich erscheinen  lässt (vgl. Ritz, BAO5, § 167 Tz 6 und 8 mit der dort zitierten hg.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_55`)


VwGH 27.8.2008, 2008/15/0202, und VwGH 18.9.2003,  2002/16/0256, sowie Ritz, BAO4, § 217, Rz 2 ff und Ellinger/Iro/Kramer/Sutter/Urtz, BAO3, §  217 E 7ff, insbesondere 22 ff).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation
- `Urtz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_64`)


Die Umbuchung  (Überrechnung) nach § 215 Abs. 1 und 2 BAO hat gegebenenfalls zwingend zu erfolgen (Stoll,  BAO, 2308;

**False Positives:**

- `Stoll,  BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_65`)


Hinweis Ritz, BAO-Kommentar6, Tz 3 f zu § 215 BAO;

**False Positives:**

- `Hinweis Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_75`)


Ritz, BAO5, § 217  Tz 4, mwN;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_78`)


Wird eine Abgabe - gleichgültig, ob es sich um eine im Veranlagungsweg (mit  Abgabenbescheid) festgesetzte Abgabe oder um eine Selbstbemessungsabgabe handelt - nicht  rechtzeitig entrichtet, so tritt mit Ablauf des Fälligkeitstages die Säumniszuschlagspflicht ein  (Stoll, BAO-Kommentar Band 3, 2319).

**False Positives:**

- `Stoll, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Olschofski  und die weiteren Senatsmitglieder  Richterin R1 und die fachkundigen Laienrichter Ing. R2 und R3 in der Beschwerdesache  Natalie Gosebrink, Bakk. phil., Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel vom 24. April 2017 betreffend Festsetung der  Gebühr gemäß § 33 TP 5 GebG 1957, Steuernummer 50-818/5472  nach Durchführung  einer mündlichen Verhandlung am 11. November 2020 in Anwesenheit der Schriftführerin XY  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Natalie Gosebrink, Bakk. phil.` — partial — gold is substring of pred: `Natalie Gosebrink, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alessia Olschofski`(person)
- `Natalie Gosebrink, Bakk. phil.`(person)
- `Sepp-Huber-Straße 32, 4840 Buchleiten, Österreich`(address)
- `Finanzamtes für  Gebühren`(organisation)
- `50-818/5472`(tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_57`)


Tatsachen sind ausschließlich mit dem Sachverhalt des abgeschlossenen Verfahrens  zusammenhängende tatsächliche Umstände, die bei einer entsprechenden  Berücksichtigung zu einem anderen Ergebnis geführt hätten (vgl. Ritz, BAO Tz 221 zu  § 303).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_234`)


Hinsichtlich des mitsamt der Beschwerde übermittelten Offenlegungsschreiben  vom 1.12.2012, welches keine Unterschrift der steuerlichen Vertretung des Beschwerdeführers  und lediglich einen Stempelaufdruck „KOPIE“, ansonsten keine Stempel oder sonstigen  Bestätigungsvermerke aufweist, stellte die belangte Behörde im Zuge ihrer  Beschwerdevorentscheidung, welcher Vorhaltscharakter zukommt (vgl bereits Stoll, BAO- Kommentar, 2713 samt Judikaturnachweisen und zB VwGH 16.10.2014, Ra 2014/16/0026),  fest, dass ein solches Schreiben nicht im Steuerakt aufliege und daher nicht bei der belangten  Behörde eingegangen sei.

**False Positives:**

- `Stoll, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_32`)


nur er ist somit mit Bescheidbeschwerde anfechtbar (s. dazu auch Ritz, BAO, 6.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Jonathan Hewett, Bakk. techn., Kleinbodenerstraße 17, 4880 Rixing, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Revisionssache Jonathan Hewett, Bakk. techn.` — partial — gold is substring of pred: `Jonathan Hewett, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jonathan Hewett, Bakk. techn.`(person)
- `Kleinbodenerstraße 17, 4880 Rixing, Österreich`(address)
- `Mag. Anton Heisinger`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Samuel Hegenbart, Dr.` — partial — gold is substring of pred: `Samuel Hegenbart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Samuel Hegenbart`(person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_85`)


Bei der Festsetzung der Zwangsstrafe handelt es sich (dem Grunde und der Höhe nach) um  eine Ermessensentscheidung der Abgabenbehörde im Sinne des § 20 BAO (Ritz, BAO6, § 111, Tz  10; VwGH 22.2.2000,96/14/0079).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_91`)


Bei der Ermessensübung sind nach der Literatur (Ritz, BAO6, § 111, Tz 10 mwN) und  überwiegender Rechtsprechung des Bundesfinanzgerichtes (12.09.2014, RV/7102806/2014;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_99`)


Das Verwaltungsgericht ist in seinem Erkenntnis gehalten, die Ermessenübung der  Abgabenbehörde zu prüfen und das Ermessen in seinem Erkenntnis eigenverantwortlich zu  üben (Ritz, BAO6, § 20, Tz 11).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_119`)


Es konnte daher im gegenständlichen Fall  dahingestellt bleiben, ob - wie dies in der Literatur (Ritz, BAO6, § 111, Tz 10 mwN) und dem  Großteil der BFG-Rechtsprechung (etwa BFG 12.09.2014, RV/7102806/2014;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_134`)


Nach herrschender Meinung sei die Unschuldsvermutung auch für die Beurteilung der „hinter- zogenen Abgaben“ anzuwenden (vgl. Ritz, BAO, § 207, Rz. 15).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_39`)


(Ritz, BAO6, § 274, Tz. 5)  Im Antrag, „in eventu eine mündliche Berufungsverhandlung im Sinn des § 284 Abs. 1 BAO  (jetzt § 274 Abs. 1 BAO)“ anzuberaumen, vermochte der Gerichtshof im Hinblick auf seine  Unbestimmtheit (in eventu) nicht als einen Parteienantrag auf Durchführung einer mündlichen  Verhandlung zu erkennen (Ellinger/Sutter/Urtz, BAO, § 2 74, E 18 unter Verweis auf VwGH vom  01.10.1979, 870/79).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation
- `Urtz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_55`)


Wiedermann, Wiederaufnahme, 99 ff; vgl  hiezu auch Stoll,  BAO, 2935 ff).

**False Positives:**

- `Stoll,  BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_56`)


(Ritz, BAO6, § 303 Rz. 30f)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_60`)


20.1.2010, 2006/13/0015) (Ritz, BAO6,  § 303 Rz. 62)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_64`)


(Ritz, BAO6, § 303 Rz. 64)  Gemäß § 307 Abs. 1 BAO ist mit dem die Wiederaufnahme des Verfahrens bewilligenden oder  verfügenden Bescheid unter gleichzeitiger Aufhebung des früheren Bescheides die das wieder  aufgenommene Verfahren abschließende Sachentscheidung zu verbinden.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_70`)


(Ritz, BAO6, § 307 Rz. 3)  Gemäß § 279 Abs. 1 BAO hat das Verwaltungsgericht außer in den Fällen des § 278 in der  Sache selbst mit Erkenntnis zu entscheiden.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_81`)


29.1.2015, 2012/15/0030) (Ritz, BAO6, § 279  Rz. 10f)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_42`)


Anträge, die erst in einem die Beschwerde ergänzenden Schreiben gestellt werden, begründen  keinen Anspruch (vgl Ritz, BAO6, § 274 Tz 2 f; zum Antrag auf mündliche Verhandlung siehe  VwGH 27.6.2012, 2008/13/0148).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_91`)


Ohne äußere  Eindrücke von Beweismitteln ist ein Beweisverfahren derart undenkbar, dass eine davon  losgelöste Gedankenkette, mag sie noch so logisch erscheinen, Spekulation ist und bleiben  muss (Althuber/Tanzer/Unger, BAO-HB, § 166, 469).

**False Positives:**

- `Unger, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_14`)


Damit ist die ersteBeteiligungsKG,  FN FBnummerErsteBeteilKG (´AbkErsteBeteilKG´) ohne Liquidation erloschen und ihre  Gesamtrechtsnachfolgerin ist die KommanditistGmbH. (Vgl. auch Ritz, BAO6, § 19 Tz 1)

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_31`)


(Vgl. auch Ritz, BAO6, § 79 Tz 1, Tz 12 und 12a, Tz 3 f. mit Verweis auf Unger  in Althuber/Tanzer/Unger, BAO-HB § 79 S. 226)  Gegen den (vermeintlichen) Bescheid vom 28.5.2008 wurde durch die  alterFirmenwortlautsteuerlVertreter3 (nunmehriger Firmenwortlaut:  neuerFirmenwortlautsteuerlVertreter3) mit Schreiben vom 24.6.2008 namens und auftrags der   MituntBezeichBescheid [Anm. des BFG: damals bereits beendet und nicht mehr  parteifähig],   Rechtsnachfolger der ersteBeteiligungsKG, St.Nr. StNrErsteBeteilKG [Anm. des BFG:  Rechtsnachfolger ist die KommanditistGmbH],   dritteBeteiligungsKG, St.Nr. StNrDritteBeilKG  Berufung erhoben.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation
- `Unger, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)
- `BFG`(organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_36`)


Der Neuerungstatbestand fordert, dass  (entscheidungswesentliche) Tatsachen oder Beweismittel im (abgeschlossenen) Verfahren neu  hervorkommen und zwar in jenem Verfahren, dass bereits durch Bescheid abgeschlossenen ist  (vgl. Ritz, BAO5, § 303Tz 45).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_37`)


Was das "neu Hervorkommens" von Tatsachen und Beweismitteln nach § 303 Abs. 1 BAO idF  FVwGG 2012 anbelangt, gibt es zwei Kommentarmeinungen:   Nach Ritz ist sowohl bei der amtswegigen als auch bei der antragsgebundenen  Wiederaufnahme, einzig der Wissenstand der Abgabenbehörde, bezogen auf die Aktenlage im  Zeitpunkt der Erlassung des das Verfahren abschließenden Bescheides maßgebend (vgl. Ritz,  BAO5,§ 303 Tz 45 und die dort angeführte Judikatur).

**False Positives:**

- `Ritz,  BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_57`)


Die Harmonisierung erfolgte in der Weise, dass ab 1.1.2014  die für die amtswegige Wiederaufnahmen geltenden Voraussetzungen (Ermessen,  Verjährungsfristen, kein Verschulden, keine Notwendigkeit der formellen Rechtskraft) auch für  die Wiederaufnahme auf Antrag gelten (vgl. Ritz, BAO5, § 303 Tz 2).

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_60`)


Insoweit Ritz unter Hinweis auf die Judikatur des Verwaltungsgerichtshofes (vgl.Ritz, BAO5, §  303, Tz 46) die Ansicht vertritt, maßgebend für das Hervorkommen neuer Tatsachen und  Beweismittel sei einzig der Wissenstand der Abgabenbehörde, bezogen auf die Aktenlage im  Zeitpunkt der Erlassung des das Verfahren abschließendes Bescheides, ist festzuhalten, dass  die von ihm zitierte Judikatur ausschließlich zur amstwegigen Wiederaufnahme des Verfahrens  nach § 303 Abs. 4 BAO alte Fassung ergangen ist.

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_64`)


Weshalb dieser Judikatur "als Folge der  Gesetzesänderung "der Boden entzogen sein soll", ist für das Bundesfinanzgericht nicht  ersichtlich, zumal Ritz und das Bundesministerium für Finanzen schon zur § 303 Abs. 1 BAO alte  Fassung nachstehende - von der Judikatur des Verwaltungsgerichtshofs abweichende -  Rechtsansicht vertreten haben (vgl. Ritz, BAO4, § 303 Tz 27 und vgl. Ritz, BAO5,§ 303 Tz 47):   "Für die Frage des Neuhervorkommens ist - ebenso wie für die amtswegige Wiederaufnahme -  der Kenntnisstand der Abgabenbehörde (im jeweiligen Verfahren) maßgebend, nicht jedoch,  ob im Zeitpunkt des abgeschlossenen Verfahrens diese Umstände der Partei bekannt waren  (BMF, AÖF 2006/192, Abschn.2.1.; aM VwGH 28.9.1998, 96/16/0158;

**False Positives:**

- `Ritz, BA` — no gold match — likely missing annotation
- `Ritz, BA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesministerium für Finanzen`(organisation)
- `Verwaltungsgerichtshofs`(organisation)
- `BMF`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_4`)


Entscheidungsgründe  1.: Mit Strafverfügung des Magistrats de r Stadt Wien,  MA 67,  vom 15.10.2019 , GZ  MA67/196700867324/2019, wurde der Beschwerdeführer (Bf.) der  Begehung einer  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über ihn nach § 4 Abs. 1 Parkometergesetz 2006 eine Geldstrafe i.H. von € 60 und  im Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien,  MA` — partial — gold is substring of pred: `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_8`)


2.: Mit Strafverfügung des Magistrats der Stadt Wien, MA 67, vom 21.10.2019, GZ.   MA67/196700891928/2019 wurde der Beschwerdeführer (Bf.) der Begehung einer  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über ihn nach § 4 Abs. 1 Parkometergesetz 2006 eine Geldstrafe i.H. von € 60 und  im Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien, MA` — partial — pred is substring of gold: `Magistrats der Stadt Wien, MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, MA 67`(organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_11`)


3.: Mit Strafverfügung des Magistrats der Stadt Wien, MA 67, vom 21.10.2019, GZ.  MA67/196700890302/2019 wurde der Beschwerdeführer (Bf.) der Begehung einer  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über ihn nach § 4 Abs. 1 Parkometergesetz 2006 eine Geldstrafe i.H. von € 60 und  im Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Stadt Wien, MA` — partial — pred is substring of gold: `Magistrats der Stadt Wien, MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, MA 67`(organisation)

</details>

---

## `Deceased Person Reference` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a7b4c2e1`  
**Description:**
Captures the name of a deceased person referenced in the text (e.g., 'verstorbenen').

**Content:**
```
(?:verstorbenen|Verstorbenen)(?:\s+|\n)*(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 32 | 0 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 32 | 2428 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_53`)


Vom Finanzamt (kurz FA) wurden EUR 4.766,81  für Begräbniskosten für den verstorbenen Vater (Nachlassüberschuldung) erklärungsgemäß  anerkannt.

**False Positives:**

- `verstorbenen Vater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131110.1_30`)


Da die Bf als Erbin nach dem verstorbenen Gatten Antragstellerin und Adressatin der  entsprechenden ANV-Bescheide – und damit auch Empfängerin der aus dem  Sonderausgabenabzug resultierenden Steuergutschriften – war, erscheint es aus  verfahrensökonomischen Gründen vertretbar, von einer Korrektur der in Rechtskraft  erwachsenen ANV-Bescheide zur StNr. des verstorbenen Gatten Abstand zu nehmen.

**False Positives:**

- `verstorbenen Gatten Antragstellerin` — no gold match — likely missing annotation
- `verstorbenen Gatten Abstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_17`)


Im Fahrzeug  war lediglich eine Farbkopie des Ausweises gemäß § 29b StVO 1960 mit der Nr. 000 einer  bereits verstorbenen Person sichtbar eingelegt, wodurch die Parkometerabgabenbefreiung  vorgetäuscht wurde.

**False Positives:**

- `verstorbenen Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_29`)


Die Verwendung eines § 29b Ausweises einer verstorbenen Person bzw. eines nachgemachten  § 29b Ausweises falle daher nicht unter die Ausnahmebestimmung.

**False Positives:**

- `verstorbenen Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_32`)


Dass die Einhaltung der Vorschriften eine besondere Aufmerksamkeit erfordert habe oder dass  die Verwirklichung des Tatbestandes aus besonderen Gründen nur schwer hätte vermieden  werden können, sei auf Grund der Tatumstände nicht anzunehmen, zumal die Verwendung  eines kopierten § 29b-StVO-Ausweises einer verstorbenen Person nicht mehr auf fahrlässiges  3 von 9 Seite 4 von 9

**False Positives:**

- `verstorbenen Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_65`)


Es steht somit außer Frage, dass die Verwendung einer Farbkopie des Parkausweises gemäß  § 29b StVO einer verstorbenen Person nicht unter die Ausnahmebestimmung von § 6 lit. g  Wiener Parkometerabgabeverordnung fällt.  Der Bf. hat somit die objektive Tatseite der ihm von der belangten Behörde angelasteten  Verwaltungsübertretung verwirklicht.

**False Positives:**

- `verstorbenen Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_81`)


Die Verwendung eines kopierten § 29b-StVO-Ausweises einer verstorbenen Person weist schon  allein aus der Tat an sich auf eine vorsätzliche Handlungsweise hin, da jedenfalls davon  auszugehen ist, dass eine Person, die auf solche Art eine Befreiung von der Parkometerabgabe  vortäuscht, sich der Tragweite ihrer Handlungen wohl bewusst sein muss.

**False Positives:**

- `verstorbenen Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_82`)


Indem der Bf.  bewusst eine Kopie des auf seinen bereits verstorbenen Vater ausgestellten Ausweises gemäß  §29b StVO im Fahrzeug hinterlegt hat, hat er nicht nur eine fahrlässige Verkürzung der  Parkometerabgabe, sondern eine vorsätzliche Abgabenhinterziehung begangen.

**False Positives:**

- `verstorbenen Vater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_83`)


Aus diesem  Grund kann auch das Ausmaß des Verschuldens im vorliegenden Fall nicht als geringfügig  angesehen werden  Die vom Bf. angeführten Gründe für die Hinterlegung des Parkausweises eines Verstorbenen  sind nicht geeignet, von der Einstufung als schwere Verschuldensform abzugehen, noch dazu  wo der Bf. in seiner Beschwerde selbst vorgebracht hat, dass er den Parkausweis seines  verstorbenen Vaters vorsätzlich im Fahrzeug hinterlegt hat.

**False Positives:**

- `verstorbenen Vaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/134315.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134315.1_57`)


Die Bf habe ihren verstorbenen Ehegatten gepflegt.

**False Positives:**

- `verstorbenen Ehegatten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/134808.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134808.1_37`)


Mit Schreiben vom 25.08.2021 wies der Bf. die Aufwendungen für die doppelte  Haushaltsführung und die Krankheit durch Vorlage von Arbeitsunfähigkeitsbescheinigungen  und der Fahrten in eine Krankenanstalt zwecks onkologischer Chemotherapie und  Strahlentherapie seiner – mittlerweile verstorbenen Gattin – nach.

**False Positives:**

- `verstorbenen Gattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_29`)


Von der Pensionsversicherungsanstalt wurde die Waisenpension nach dem verstorbenen Vater  zuerkannt.

**False Positives:**

- `verstorbenen Vater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_73`)


Erwachsenenschutz 19 01 2021  Keine neuen Befunde vorliegend - Stellungsuntersuchungsblätter 12.03.1965 waren bereits  beim Vorgutachten vorliegend  Telefonat vom 17 03 2021 des Erwachsenenvertreters mit Chefärztin:  AW beziehe Invaliditätspension seit 1978, seit 2011 Alterspension,  beziehe keine Waisenrente nach den verstorbenen Eltern  Seit 2004 Erwachsenenvertreter  Behandlung/en / Medikamente / Hilfsmittel:  keine aktuellen Angaben  Ergebnis der durchgeführten Begutachtung:  Bezeichnung der körperlichen, geistigen oder sinnesbedingten Funktionseinschränkungen,  welche voraussichtlich länger als sechs Monate andauern werden:  Begründung der Rahmensätze:  Intelligenzminderung  Unterer Rahmensatz, da nach Befunddokumentation im Vorgutachten  keine schwerwiegenden Verhaltensauffälligkeiten beschrieben  Pos.Nr. 03.01.03  Gdb % 50  6 von 11 Seite 7 von 11

**False Positives:**

- `verstorbenen Eltern  Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/139828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139828.1_66`)


Schon aus dem Erbschaftsantritt wären beim Sohn des Verstorbenen Eigenmittel vorhanden  gewesen, um die Begräbniskosten zu bestreiten.

**False Positives:**

- `Verstorbenen Eigenmittel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/141857.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141857.1_51`)


Wie aus der beiliegenden Vorhaltsbeantwortung betreffend die verstorbene Ehegattin des  Beschwerdeführers ersichtlich, seien bei dieser folgende Kosten der häuslichen Betreuung  (nach Abzug des Pflegegeldes) angefallen:  2017: 20.900,70 €  2018: 21.900,25 €  2019: 18.793,60 €  2020: 16.192,70 €  2021: 24.369,60 €  Nach Abzug des steuerlichen Existenzminimums (11.000 €) vom steuerlichen Einkommen nach  § 33 Abs. 1 EStG 1988 seien bei der Ehegattin des Beschwerdeführers folgende Kosten zu  berücksichtigen:  2017: 22.533,94 € - 11.000 € = 11.533,94 €  2018: 22.894,32 € - 11.000 € = 11.894,32 €  2019: 23.352,20 € - 11.000 € = 12.352,20 €  2020: 23.896,04 € - 11.000 € = 12.896,04 €  2021: 24.254,38 € - 11.000 € = 13.254,38 €  Von den gesamten Kosten der häuslichen Betreuung verblieben nach Abzug der bei der  verstorbenen Ehegattin zu berücksichtigenden außergewöhnlichen Belastungen (ohne  Selbstbehalt auf Grund der eigenen Behinderung) die folgenden Beträge als außergewöhnliche  Belastung mit Selbstbehalt beim Beschwerdeführer aus dem Titel des Unterhaltes (§ 34 Abs. 7  Z 4 EStG 1988):  2017: 20.900,70 € - 11.533,94 € =   9.366,76 €  2018: 21.900,25 € - 11.894,32 € = 10.005,93 €  2019: 18.793,60 € - 12.352,20 € =   6.441,40 €  2020: 16.192,70 € - 12.896,04 € =   3.296,66 €  2021: 24.369,60 € - 13.254,38 € = 11.115,22 €

**False Positives:**

- `verstorbenen Ehegattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/141857.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141857.1_59`)


b. Dem Beschwerdeführer entstanden in den Jahren 2017 bis 2021 einerseits Aufwendungen  aufgrund eigener Erkrankung in der in den angefochtenen Bescheiden ausgewiesenen Höhe  sowie im Zusammenhang mit der Behinderung seiner mittlerweile verstorbenen Ehefrau, zu  deren Tragung er in nachfolgend angeführter Höhe verpflichtet war:    2017 9.366,76 €  2018 10.005,93 €  2019 6.441,40 €  2020 3.296,66 €  2021 11.115,22 €

**False Positives:**

- `verstorbenen Ehefrau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/141857.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141857.1_121`)


Im Beschwerdefall waren diese Voraussetzungen unstrittig nicht erfüllt, da das Einkommen der  verstorbenen Ehegattin des Beschwerdeführers in allen Jahren diesen Betrag überschritt,  sodass die als außergewöhnliche Belastung geltend gemachten Aufwendungen nur im Rahmen  der Unterhaltsverpflichtung mit Selbstbehalt berücksichtigt werden konnten (vgl. VwGH  18.02.2021, Ra 2019/15/0113).

**False Positives:**

- `verstorbenen Ehegattin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/141978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141978.1_49`)


Zu dem Abgabenverfahren des verstorbenen Ehegatten  (GZ RV/7101396/2015), dem eine fast gleichlautende Selbstanzeige zu Grunde lag und dass in  Rechtskraft erwachsen ist, könne sie keine weiteren Angaben machen.

**False Positives:**

- `verstorbenen Ehegatten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/143723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143723.1_3`)


Begründung  I. Dem gegenständlichen Beschluss liegt der nachfolgend als Ergebnis des finanzgerichtlichen  Ermittlungsverfahrens festgestellte Sachverhalt zugrunde, der auf unbedenklichen  abgabenbehördlichen Vorlage- und Ergänzungsunterlagen sowie Inhalten von Datenbanken  der Abgabenbehörde, des Grundbuchs und des Innenministeriums (ZMR/DHW) basiert:  Nach Durchführung einer Außenprüfung (AP) ergingen am 23.Juni 2014 an den inzwischen  verstorbenen Beschwerdeführer (Bf) Umsatz- und Einkommensteuerbescheide für 2006 – 2010  (Erstveranlagungsbescheide).

**False Positives:**

- `verstorbenen Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/143723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143723.1_32`)


Da sich in den übermittelten abgabenbehördlichen Unterlagen bzw. den eingesehenen  Datenbanken keine Hinweise auf eine für die Verlassenschaft des Bf vertretungsbefugte Person  finden, insbesondere auch nicht auf eine(n) gerichtlich bestellte(n) VerlassenschaftskuratorIn,  hält es das BFG für erwiesen, dass der ruhende Nachlass des verstorbenen Bf aktuell über  keine(n) gerichtlich bestellte(n) VerlassenschaftskuratorIn verfügt.

**False Positives:**

- `verstorbenen Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/144916.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144916.1_16`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer, Sohn der verstorbenen Frau A, brachte am 22.03.2023 eine von ihm  unterfertigte Steuererklärung (L1) für das Jahr 2022 betreffend StNr *** „Verlass nach A“ beim  Finanzamt Österreich ein.

**False Positives:**

- `verstorbenen Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/145301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145301.1_14`)


Das Begräbnis seines verstorbenen Bruders sei nicht durch Aktiva gedeckt  gewesen, es sei aufgrund der langen Krankheit nichts mehr da gewesen.

**False Positives:**

- `verstorbenen Bruders` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/145301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145301.1_24`)


Der Gerichtsbeschluss in der  Verlassenschaftssache des verstorbenen Bruders stellte somit fest, dass die Begräbniskosten  mit (nach Nachtragsverteilung) insgesamt EUR 2.582,47 in den Aktiva Deckung finden.

**False Positives:**

- `verstorbenen Bruders` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/145301.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145301.1_55`)


Das Finanzamt hat dazu in seinem Vorlagebericht an das Bundesfinanzgericht  festgehalten, dass es die sittliche Verpflichtung des Bf. anerkennt, für ein angemessenes  Begräbnis des verstorbenen Bruders zu sorgen.

**False Positives:**

- `verstorbenen Bruders` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/145664.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145664.1_15`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Mit Einantwortungsbeschluss des Bezirksgerichtes Ort_1 vom 18.5.2022 zu AZ_1 wurde die  Verlassenschaft nach der am 30.3.2021 verstorbenen Erblasserin dem Beschwerdeführer,  Erbe_2 und Erbin_3 aufgrund deren bedingter Erbantrittserklärungen je zu einem Drittel  eingeantwortet.

**False Positives:**

- `verstorbenen Erblasserin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/145664.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145664.1_17`)


Mit Kaufvertrag vom 7.4.2022 veräußerte die Verlassenschaft nach der am 30.3.2021  verstorbenen Erblasserin, vertreten durch den Beschwerdeführer, Erbe_2 und Erbin_3 als  erbantritteserklärte Erben, die Liegenschaft L, an die W GesmbH.

**False Positives:**

- `verstorbenen Erblasserin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/145727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145727.1_6`)


Die Begründung dazu lautet: „In  Ihrer Steuererklärung wurde neben Ihrem Verlustvortrag auch der noch offene Verlustvortrag  Ihres verstorbenen Vaters geltend gemacht.

**False Positives:**

- `verstorbenen Vaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/149046.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149046.1_6`)


Zur Begründung führte die Bf. im Wesentlichen aus, dass das Unternehmen wirtschaftlich von  der verstorbenen Mutter des geschäftsführenden Gesellschafters geleitet worden sei und im  Zuge dessen der Todesfall während dem Betriebsprüfungsverfahren eingetreten sei und der  geschäftsführende Gesellschafter, welcher körperlich auf der Baustelle jeweils arbeite, somit  nur einen geringen Einblick in das wirtschaftliche Geschehen des Unternehmens gehabt habe.

**False Positives:**

- `verstorbenen Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_11`)


Die Kosten werden nicht zur Gänze aus Mitteln der Kinder- und Jugendhilfe getragen, da die  betroffene Minderjährige nach ihrer verstorbenen Mutter Halbwaisenpension von der PVA  bezieht (siehe Anhang).

**False Positives:**

- `verstorbenen Mutter Halbwaisenpension` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/149272.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149272.1_29`)


Seitens der PVA wurde der minderjährigen Bf nach ihrer verstorbenen Mutter die  Halbwaisenpension sowie aufgrund ihrer chronischen Erkrankung auch Pflegegeld zuerkannt.

**False Positives:**

- `verstorbenen Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/149421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149421.1_36`)


Darin wurden weitere Nachweise und Unterlagen zu den Krankheitskosten für  die Mutter der Bf angefordert (Vereinbarung über die Kostentragung mit dem Pflegeheim,  Rechtsgrundlage für die Übernahme der Zahlungen für diverse Lebenshaltungskosten,  Nachweise über tatsächliche Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst SENECURA, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, etc).

**False Positives:**

- `verstorbenen Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `SENECURA`(organisation)

</details>

---

## `Judge Name Extraction` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `583afeab`  
**Description:**
Captures the judge's full name including title following 'durch den/die' + role, ensuring the title is part of the match and the name follows immediately.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Senatsvorsitzenden|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Mag\.|Mag\.a|Mag\.in|Mag\.Dr\.|Mag\.Dr\.in|OSR|StR|KommR|OMedR|MedR|VetR|\u00d6kR|RgR|HR|MMag\.|R\.|Bakk\.|LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Ing\.|Dipl\.-Ing\.|PhD|Techn\s+R|Techn\s+R\.\s+))([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 13 | 2409 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache MedR Irvin Leider, 10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich, über die Beschwerde vom 22. September 2017 gegen den Bescheid des FA vom  21. August 2017 betreffend Einkommensteuer 2016 Steuernummer 30-411/2742  zu Recht  erkannt:   1.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MedR Irvin Leider`(person)
- `10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich`(address)
- `30-411/2742`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129277.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache des Levi Panos,  Puchheimgasse 2, 4770 Pram, Österreich, über die Beschwerde vom 7. April 2014 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 1. April 2014 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 Steuernummer 73-863/0859  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Levi Panos`(person)
- `Puchheimgasse 2, 4770 Pram, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `73-863/0859`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gotthard Eppers  vertreten durch  Gf. über die Beschwerde vom 16. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 16. Dezember 2019, Steuernummer 98-639/6692, betreffend Feststellung der  Einkünfte gem. § 188 BAO für das Jahr 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gotthard Eppers`(person)
- `Finanzamtes Wien  4/5/10`(organisation)
- `98-639/6692`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/132065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Torsten Gnapfeus, Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich, gegen die Bescheide des Finanzamtes Wien 4/5/10 vom 21. Februar 2014 betreffend  die auf § 303 Abs. 1 BAO basierende Verfügung der Wiederaufnahme der Verfahren zur  Umsatzsteuer für das Jahr 2010 und zur Einkommensteuer für die Jahre 2010 und 2011 sowie  die auf § 205 Abs. 1 BAO basierende Festsetzung von Anspruchszinsen für die Jahre 2010 bis  2012 beschlossen:  Der Vorlageantrag vom 26.9.2014 wird - betreffend vorgenannter Bescheide - gemäß § 264  Abs. 5 BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Torsten Gnapfeus`(person)
- `Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich`(address)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Bodo Friehmann, Hohenwartweg 2, 4851 Fischham, Österreich, über die Beschwerde vom 30. September 2019 gegen den Einkommensteuerbescheid  2016 und den Einkommensteuerbescheid 2017 des Finanzamtes Wien 1/23 vom 27. August  2019 zu Steuernummer 09 75-279/5529  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bodo Friehmann`(person)
- `Hohenwartweg 2, 4851 Fischham, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)
- `75-279/5529`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Eduard Schulden, Bakk. rer. nat., Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich, vertreten durch Dkfm. Freund & Partner Steuerberater GmbH, Schellinggasse 3, 1010  Wien, über die Beschwerde vom 29. Juli 2016 (Eingangsstempel 1. August 2016 ) gegen den  Umsatzsteuerbescheid 2011 und den Bescheid über die Feststellung von Einkünften gemäß  § 188 BAO 2011 des Finanzamtes Baden Mödling vom 5. Juli 2016, Steuernummer  16 28-951/9095, zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Eduard Schulden, Bakk. rer. nat.`(person)
- `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich`(address)
- `Freund & Partner Steuerberater GmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `28-951/9095`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/133706.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Morgana Deppermann, MSc BEd, Am Steinparz 54, 2000 Oberolberndorf, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die Beschwerde vom  3. Juli 2015 gegen den Bescheid des Finanzamtes Braunau Ried Schärding vom 29. Mai 2015  betreffend Anspruchszinsen (§ 205 BAO) 2003, 2004, 2005 und 2006 zu Steuernummer  25-580/4262  zu Recht erkannt:   I. Die angefochtenen Bescheide werden - ersatzlos - aufgehoben.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Morgana Deppermann, MSc BEd`(person)
- `Am Steinparz 54, 2000 Oberolberndorf, Österreich`(address)
- `Martin Friedl`(person)
- `Finanzamtes Braunau Ried`(organisation)
- `25-580/4262`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/134201.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134201.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterDr. Martin Wittmann in der Beschwerdesache  [...], [...], vertreten durch Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Brockmanngasse 75, 8010 Graz, über die Beschwerde vom  27. Jänner 2017 gegen die Bescheide des Finanzamt Landeck Reutte  jeweils vom 10. Jänner 2017,  Steuernummer 16-981/1693, betreffend Energieabgabenvergütung 2011 -2015 zu Recht  erkannt:   I. Der Bescheid vom 10. Jänner 2017 betreffend Festsetzung des Vergütungsbetrages  nach dem Energieabgabenvergütungsgesetz für das Kalenderjahr 2011 wird  abgeändert.

**False Positives:**

- `durch den RichterDr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Styria Treuhand- und Revisions GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Landeck Reutte`(organisation)
- `16-981/1693`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Mona Jakubschak, Paukengraben 9, 9620 Obervellach, Österreich  und Wigand Venhuis, LLB BEd, Johann-Paur-Straße 24, 8483 Krobathen, Österreich  über die Beschwerde vom 25. Jänner 2021 gegen den  Grundsteuerbescheid des Magistrates der Stadt Wien, MA 6, vom 1. Jänner 2021 betreffend  Liegenschaft Wien BezirkAdresse, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mona Jakubschak`(person)
- `Paukengraben 9, 9620 Obervellach, Österreich`(address)
- `Wigand Venhuis, LLB BEd`(person)
- `Johann-Paur-Straße 24, 8483 Krobathen, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/135111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135111.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterPerson_A in der Beschwerdesache Leander Tumoseit,  Schwaighofweg, Oberau 122, 4121 Hörhag, Österreich, vertreten durch Othmar Huttary, Höttinger Au 76, 6020 Innsbruck, über die  Beschwerde vom 18. September 2015 gegen die Bescheide des [...] vom 20. August 2015 über  die Festsetzung von Anspruchszinsen (§ 205 BAO) für die Jahre 2011 und 2012, Steuernummer  56-131/0598, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `durch den RichterPerson` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Leander Tumoseit`(person)
- `Schwaighofweg, Oberau 122, 4121 Hörhag, Österreich`(address)
- `Othmar Huttary`(person)
- `56-131/0598`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/136061.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136061.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Oswald Marck, Hedorferhof 88, 4891 Matzlröth, Österreich, über die Beschwerde vom 30. Oktober 2020 gegen den  Einkommensteuerbescheid 2019 des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2020 zu  Steuernummer 45-652/7301  in der Senatssitzung am 7. März 2022 zu Recht erkannt:  Gemäß § 279 BAO wird die Beschwerde als unbegründet abgewiesen und es wird der  angefochtene Bescheid geändert.

**False Positives:**

- `durch den SenatsvorsitzendenRichter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Oswald Marck`(person)
- `Hedorferhof 88, 4891 Matzlröth, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `45-652/7301`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/136628.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136628.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Sascha Bozbiyik, Neumarkter Straße 9, 4694 Edlach, Österreich, über dessen Beschwerde vom 23. September 2021 gegen den Gebührenbescheid des  Magistrats der Stadt Wien, Fachgruppe Gebühren, MA31 vom 17. September 2021,  Rechnungsnr. ReNR, betreffend Wasser- und Abwassergebühren, beschlossen:  Die Beschwerde gilt gemäß § 2a Bundesabgabenordnung (BAO) in Verbindung mit § 85 Abs. 2,  § 250 Abs. 1 lit. c und § 269 Abs. 1 BAO als zurückgenommen.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sascha Bozbiyik`(person)
- `Neumarkter Straße 9, 4694 Edlach, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/137101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Heinrich Royke, Wilhelm-Fischer-Allee 11, 9314 Thalsdorf, Österreich, (Beschwerdeführer, Bf.), über die Beschwerde des Bf. vom 16. Juni 2021 gegen den  Einkommensteuerbescheid 2020 des Finanzamtes Österreich vom 9. Juni 2021 zu  Steuernummer 95-669/0680  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde stattgegeben und der angefochtene Bescheid  abgeändert.

**False Positives:**

- `durch den RichterRi ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Heinrich Royke`(person)
- `Wilhelm-Fischer-Allee 11, 9314 Thalsdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `95-669/0680`(tax_number)

</details>

---

## `General Name with Title` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f050eb9`  
**Description:**
Captures names with titles in other contexts, ensuring the title is part of the match and the name follows immediately, extracting the full title+name. Requires a preceding context anchor to avoid false positives.

**Content:**
```
(?:Herrn?\s+|Frau\s+|in\s+der\s+Beschwerdesache\s+(?:des\s+|der\s+)?|in\s+der\s+Rechtssache\s+gegen\s+|des\s+|der\s+|als\s+|von\s+|gegen\s+|mit\s+|bei\s+|zu\s+|durch\s+|der\s+|die\s+|das\s+)(?:Dr\.|Dr\.in\s+|Mag\.|Mag\.a\s+|Mag\.in\s+|Mag\.Dr\.|Mag\.Dr\.in\s+|Univ\.-Prof\.|Univ\.-Prof\.in\s+|Priv\.-Doz\.|Priv\.-Doz\.in\s+|Hon\.-Prof\.|Hon\.-Prof\.in\s+|KommR\s+|OSR\s+|StR\s+|OMedR\s+|MedR\s+|PhD\s+|\u00d6kR\s+|VetR\s+|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|LL\.M\.|M\.B\.L\.|MSc\s+|MA\s+|BA\s+|BSc\s+|Ing\.|Dipl\.-Ing\.|RgR\s+|HR\s+|MMag\.|R\.\s+|Techn\s+R\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 148 | 0 | 148 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 148 | 2455 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `in der Beschwerdesache Univ.-Prof.in Rachel Darnieder` — partial — gold is substring of pred: `Univ.-Prof.in Rachel Darnieder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hemma Bährs`(person)
- `Univ.-Prof.in Rachel Darnieder`(person)
- `Finanzamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129204.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache MedR Irvin Leider, 10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich, über die Beschwerde vom 22. September 2017 gegen den Bescheid des FA vom  21. August 2017 betreffend Einkommensteuer 2016 Steuernummer 30-411/2742  zu Recht  erkannt:   1.Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `in der Beschwerdesache MedR Irvin Leider` — partial — gold is substring of pred: `MedR Irvin Leider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MedR Irvin Leider`(person)
- `10.-Oktober-Gasse 6, 4802 Lahnstein, Österreich`(address)
- `30-411/2742`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Mag.a Reneé Kobayashi, Weinbaugebiet Losling 9, 4880 Aich, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `in der  Beschwerdesache Mag.a Rene` — positional overlap with gold: `Mag.a Reneé Kobayashi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Elisabeth Traxler`(person)
- `Mag.a Reneé Kobayashi`(person)
- `Weinbaugebiet Losling 9, 4880 Aich, Österreich`(address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `in der Beschwerdesache  HR Hedwig Barkholt` — partial — gold is substring of pred: `HR Hedwig Barkholt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in Vertretung der seit 1. April 2020 in  Ruhestand befindlichen Richterin D. in der Beschwerdesache KommR Eckard Gaiss, Bakk. phil., Hietzinger Kai 33, 4132 Lug, Österreich,  vertreten durch Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.,  Wasagasse 4, 1090 Wien, über die Beschwerde der Abgabepflichtigen vom 26. August 2019  gegen den Bescheid des Finanzamtes Wien 1/23 vom 9. August 2019 über die Festsetzung von  ersten Säumniszuschlägen gemäß § 217 BAO, Steuernummer 07-088/5911  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  insoweit abgeändert, als die Säumniszuschläge gemäß § 217 Abs. 7 BAO mit Null festgesetzt  werden.

**False Positives:**

- `in der Beschwerdesache KommR Eckard Gaiss` — positional overlap with gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `Hietzinger Kai 33, 4132 Lug, Österreich`(address)
- `Halpern & Prinz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `07-088/5911`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `der Dr.in Monika Wörther` — positional overlap with gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Monika Wörther-Madl`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `der Dr.in Monika Wörther` — positional overlap with gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. August Eichelsbacher  in der Beschwerdesache VetR Diethard Oldenbüttel,  Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich, vertreten durch BOD Steuerberatungs-GmbH, Europastraße 5, 6322  Kirchbichl,, über die Beschwerde vom 16. Dezember 2016 gegen den Bescheid des FA Landeck Reutte  vom 21. November 2016 betreffendBerichtigung des Einkommensteuerbescheides 2010 vom  29. November 2011 gem. § 293b BAO erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache VetR Diethard Oldenbüttel` — partial — gold is substring of pred: `VetR Diethard Oldenbüttel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. August Eichelsbacher`(person)
- `VetR Diethard Oldenbüttel`(person)
- `Rondeau-Volksprater 13, 4204 Altenbergerstraße, Österreich`(address)
- `BOD Steuerberatungs-GmbH`(organisation)
- `FA Landeck Reutte`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

**False Positives:**

- `von Dr.in Ljiljana Kos` — partial — gold is substring of pred: `Dr.in Ljiljana Kos`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Dr.in Ljiljana Kos`(person)
- `Dr. Alexander Nahler`(person)
- `Ljiljana Kos`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache HR Juliana Seidl, Am Gelände 10, 3282 Wiesmühl, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `in der Beschwerdesache HR Juliana Seidl` — partial — gold is substring of pred: `HR Juliana Seidl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `HR Juliana Seidl`(person)
- `Am Gelände 10, 3282 Wiesmühl, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `in der Beschwerdesache  StR Dr` — positional overlap with gold: `StR Dr.in Lydia Vogtleitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `StR Dr.in Lydia Vogtleitner`(person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich`(address)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `durch  HR Dr` — positional overlap with gold: `Dr. Amtsvertr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Claudia Noeltge`(person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)
- `Dr. Amtsvertr`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frieda Krein  in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy,  W.-Braun-Gasse 62, 9551 Stöcklweingarten, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  60-936/8299, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `in der Beschwerdesache Priv.-Doz.in Elena Kaminskiy` — partial — gold is substring of pred: `Priv.-Doz.in Elena Kaminskiy`

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

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache  HR Frederik Kleinmichel` — positional overlap with gold: `HR Frederik Kleinmichel, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `HR Frederik Kleinmichel, MA`(person)
- `Haniflgasse 12, 4725 Stadl, Österreich`(address)
- `Astoria Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache ÖkR Mag` — positional overlap with gold: `ÖkR Mag.a Catharina Schmalenstrot`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Priv.-Doz.in Nadine Schoormans,  Herderpark 21, 8444 Sankt Andrä im Sausal, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des Finanzamtes XY  vom 10.2.2020 betreffend Festsetzung einer Zwangsstrafe zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache Priv.-Doz.in Nadine Schoormans` — partial — gold is substring of pred: `Priv.-Doz.in Nadine Schoormans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Nadine Schoormans`(person)
- `Herderpark 21, 8444 Sankt Andrä im Sausal, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Univ.-Prof.in StR Caroline Akkoca, MBA, Hinterbachstraße 8, 4653 Spieldorf, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2021 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Jänner 2021, Zahl: MA67/206700566984/2020, mit  dem der Einspruch vom 10. November 2020 gegen die Strafverfügung vom 8. Oktober 2020 mit  derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `gegen Univ.-Prof.in St` — positional overlap with gold: `Univ.-Prof.in StR Caroline Akkoca, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)
- `Hinterbachstraße 8, 4653 Spieldorf, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. Oktober  2020, Zahl: MA67/206700566984/2020, wurde Herr Univ.-Prof.in StR Caroline Akkoca, MBA (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Herr Univ.-Prof.in St` — positional overlap with gold: `Univ.-Prof.in StR Caroline Akkoca, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Univ.-Prof.in StR Caroline Akkoca, MBA`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132646.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Urs Zumbroich  in der Beschwerdesache Techn R Huberta Witte,  Ebenweg 188, 4081 Mußbach, Österreich, über die Beschwerde vom 8. Juni 2016 gegen den Bescheid des Finanzamtes  Lilienfeld St. Pölten (jetzt Finanzamt Österreich) vom 13. Mai 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache Techn R Huberta Witte` — partial — gold is substring of pred: `Techn R Huberta Witte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Urs Zumbroich`(person)
- `Techn R Huberta Witte`(person)
- `Ebenweg 188, 4081 Mußbach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OSR Xenia Gerrit, Bakk. art.,  Märzenkellerberg 15, 3662 Edelsreith, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH, Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 23. Februar 2017 gegen den  Bescheid des Finanzamtes Gänserndorf Mistelbach vom 21. Dezember 2016 betreffend  Einkommensteuer 2014, Steuernummer 68-121/6369, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `in der Beschwerdesache OSR Xenia Gerrit` — positional overlap with gold: `OSR Xenia Gerrit, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Xenia Gerrit, Bakk. art.`(person)
- `Märzenkellerberg 15, 3662 Edelsreith, Österreich`(address)
- `gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH`(organisation)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `68-121/6369`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132957.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132957.1_3`)


des Herrn OSR Friedhelm Herwerth, vertreten durch Herrn Dr. Walter Suppan, Rechtsanwalt in Klagenfurt,

**False Positives:**

- `Herrn OSR Friedhelm Herwerth` — partial — gold is substring of pred: `OSR Friedhelm Herwerth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Friedhelm Herwerth`(person)
- `Dr. Walter Suppan`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132990.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Veronika Richerd  in der Beschwerdesache des  Priv.-Doz.in Felizia Claus, Mosenthalweg 10, 4076 Holzwiesen, Österreich  vertreten durch StB über die Beschwerde vom 11. Dezember 2019  gegen die Bescheide des Finanzamtes vom 18. November 2019 betreffend Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2009 und Einkommensteuer 2009 zu Recht  erkannt:     I. Der Beschwerde gegen den Bescheid betreffend Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2009 wird Folge gegeben.

**False Positives:**

- `in der Beschwerdesache des  Priv.-Doz.in Felizia Claus` — partial — gold is substring of pred: `Priv.-Doz.in Felizia Claus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Veronika Richerd`(person)
- `Priv.-Doz.in Felizia Claus`(person)
- `Mosenthalweg 10, 4076 Holzwiesen, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/133044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133044.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache OMedR Dr. Jaden Brabandt, Herd 8i, 4141 Harrau, Österreich, vertreten durch Dr. Klaus Erich Schmidt, Hauptstraße 27, 8582 Rosental/Kainach,  betreffend die Beschwerde vom 25.02.2019 gegen den Bescheid des Finanzamtes Graz- Umgebung vom 31.01.2019 betreffend Umsatzsteuer 2016, Steuernummer 60-356/1910,  beschlossen:   Der Vorlageantrag wird zurückgewiesen.

**False Positives:**

- `in der Beschwerdesache OMedR Dr` — positional overlap with gold: `OMedR Dr. Jaden Brabandt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Dr. Jaden Brabandt`(person)
- `Herd 8i, 4141 Harrau, Österreich`(address)
- `Dr. Klaus Erich Schmidt`(person)
- `Finanzamtes`(organisation)
- `60-356/1910`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_201`)


Am 7.2.2012 langte bei der Wiener Gebietskrankenkasse eine anwaltliche Stellungnahme von PhD Isaak Joern vom 31.1.2012 ein, in der sie ihre Tätigkeit für den Bf als Dienstverhältnis damit  begründete, dass sie als Veterinärmedizinerin humanmedizinische Tätigkeiten in seinem Labor  durchgeführt habe, bei denen sie die persönliche Arbeitskraft geschuldet hätte und eine  Vertretung ihrer Person nicht möglich gewesen wäre, die Erbringung einer Dienstleistung nicht  eines Werkes verlangt worden wäre, Arbeits- und Betriebsmittel vom Bf zur Verfügung gestellt  worden wären, sie dem Bf gegenüber weisungsgebunden gewesen und in den Betrieb  eingegliedert gewesen wäre insb durch Vorgabe der Arbeitszeit, des Arbeitsortes, der  Arbeitsmittel und Einbindung in den betrieblichen Ablauf durch Teilnahme an Besprechungen  und Konferenzen.

**False Positives:**

- `von PhD Isaak Joern ` — partial — gold is substring of pred: `PhD Isaak Joern`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gebietskrankenkasse`(organisation)
- `PhD Isaak Joern`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_406`)


Am 18.5.2021 wurde die belangte Behörde und der Bf vom Bundesfinanzgericht aufgefordert,  bekannt zu geben, ob bezüglich PhD Isaak Joern die in der Berufung angekündigte Vorlage allfälliger  Ergebnisse einer gerichtlichen Entscheidung betreffend den Vorwurf unkorrekter  Zeitaufzeichnungen in betrügerischer Absicht von PhD Isaak Joern vorgelegt wurden, da Derartiges nicht  im Akt enthalten ist.

**False Positives:**

- `von PhD Isaak Joern ` — similar text (different position): `PhD Isaak Joern`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `PhD Isaak Joern`(person)
- `PhD Isaak Joern`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_425`)


Da die persönliche Abhängigkeit im Unterschied zu PhD Isaak Joern und Dr. U bei Dr. B und Dr. H seitens  des Bundesverwaltungsgerichtes verneint wurde, qualifizierte das Bundesverwaltungsgericht  Dr. B und Dr. H als freie Dienstnehmerinnen iSd § 4 Abs. 4 ASVG.

**False Positives:**

- `zu PhD Isaak Joern ` — partial — gold is substring of pred: `PhD Isaak Joern`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Isaak Joern`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_631`)


3. Daraufhin erließ das Bundesfinanzgericht im fortgesetzten Verfahren ein neuerlich  stattgebendes Erkenntnis, das damit begründet wurde, dass hinsichtlich der  Weisungsgebundenheit von HR Dr. Emberger unterschieden werde zwischen angestellten  Ärzten - die auch fachlich weisungsgebunden sind, wobei eine verstärkte Einspruchspflicht bei  fachlich umstrittenen Weisungen bestehe (Stärker im Ärztegesetz mit Kommentar, § 3 Fußnote  7 und Emberger § 49 Fußnote 6 Z. 1.2.2) und nicht angestellten Ärzten, also niedergelassenen  Ärzten oder Wohnsitzärzten und somit auch Vertretungsärzten.

**False Positives:**

- `von HR Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_700`)


In diesem Zusammenhang ist auch die Aussage von Dr. H zu erwähnen, die angab, dass keine  vertragliche Gewährleistungspflicht für Mängel bestanden hätte und die Aussage von PhD Isaak Joern  die  besagte, die Befunde nicht einmal unterschrieben zu haben.

**False Positives:**

- `von PhD Isaak Joern  ` — partial — gold is substring of pred: `PhD Isaak Joern`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Isaak Joern`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/134021.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134021.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Kaspar Dolezil  in der Beschwerdesache StR Adam Reulmann,  Schipfäckerweg 22x, 9102 Obertrixen, Österreich, über die Beschwerde vom 31. Juli 2018 gegen den Bescheid des Finanzamt Judenburg Liezen  vom  28. Juni 2018 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80  Bundesabgabenordnung (BAO) (St.Nr. xx-xxx/xxxx HB) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache StR Adam Reulmann` — partial — gold is substring of pred: `StR Adam Reulmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Kaspar Dolezil`(person)
- `StR Adam Reulmann`(person)
- `Schipfäckerweg 22x, 9102 Obertrixen, Österreich`(address)
- `Finanzamt Judenburg Liezen`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/134170.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134170.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Francois Huppertz  in der Beschwerdesache OSR Isolde Bohnenkämper  vertreten  durch StB, über die Beschwerde vom 5. Dezember 2014 gegen die Bescheide des FA Klagenfurt St. Veit Wolfsberg  (nunmehr FA) vom 31. Oktober 2014 betreffend Einkommensteuer 2009 und 2010 St.Nr.  80-848/9629 (nunmehr xx-yyy/yyyy) zu Recht erkannt:     I. Die Beschwerde gegen den Einkommensteuerbescheid 2009 wird gemäß § 279  Bundesabgabenordnung (BAO) als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache OSR Isolde Bohnenkämper  ` — partial — gold is substring of pred: `OSR Isolde Bohnenkämper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Francois Huppertz`(person)
- `OSR Isolde Bohnenkämper`(person)
- `FA Klagenfurt St. Veit Wolfsberg`(organisation)
- `80-848/9629`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/134859.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134859.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Liu Leitgebel  in der Beschwerdesache Hon.-Prof.in Pascal Fredecke, MA BA,  Larchach 48, 7301 Girm, Österreich, über die Beschwerde vom 30. März 2021 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 15. Jänner 2021 betreffend Umsatzsteuer 2019 Steuernummer 40-437/5867  zu Recht  erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `in der Beschwerdesache Hon.-Prof.in Pascal Fredecke` — positional overlap with gold: `Hon.-Prof.in Pascal Fredecke, MA BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Liu Leitgebel`(person)
- `Hon.-Prof.in Pascal Fredecke, MA BA`(person)
- `Larchach 48, 7301 Girm, Österreich`(address)
- `FA Amstetten Melk Scheibbs`(organisation)
- `40-437/5867`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/134906.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134906.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dagobert Flachskamm  in der Beschwerdesache KommR Delia Fickentscher,  Busatisstraße 26, 5231 Au, Österreich, vertreten durch TMF Accounting & Payroll Steuerberatungsgesellschaft mbH,  Teinfaltstraße 8, 1010 Wien, über die Beschwerden vom 30. Juni 2015 und 30. Mai 2016 gegen  die Bescheide des Finanzamt Deutschlandsberg Leibnitz Voitsberg  vom 9. Mai 2016, betreffend Umsatzsteuer für das Jahr 2014, und  vom 9. Juni 2015, betreffend Umsatzsteuer für die Monate Jänner 2015 und Februar 2015  (gemäß § 253 BAO gilt die auch gegen die Bescheide der belangten Behörde vom 9. Juni 2015  betreffend Umsatzsteuer für die Monate Mai 2014 bis Dezember 2014 erhobene Beschwerde  vom 30. Juni 2015 auch als gegen den später erlassenen Umsatzsteuerbescheid für das Jahr  2014 gerichtet), Steuernummer 12-684/4735, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `in der Beschwerdesache KommR Delia Fickentscher` — partial — gold is substring of pred: `KommR Delia Fickentscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dagobert Flachskamm`(person)
- `KommR Delia Fickentscher`(person)
- `Busatisstraße 26, 5231 Au, Österreich`(address)
- `TMF Accounting & Payroll Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamt Deutschlandsberg Leibnitz Voitsberg`(organisation)
- `12-684/4735`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R Lucia Steinbrink, LLB, Beer-Hofmann-Weg 155, 4710 Schönau, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz -  Erwachsenenvertretung, Bewohnervertretung, Schloßstraße 1, 3680 Persenbeug-Gottsdorf,  über die Beschwerde vom 20. Jänner 2021 gegen den Bescheid des Finanzamtes Österreich  vom 14. Dezember 2020 betreffend Familienbeihilfe ab Juni 2015 Steuernummer  17-630/1579  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache  Techn R Lucia Steinbrink` — positional overlap with gold: `Techn R Lucia Steinbrink, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Techn R Lucia Steinbrink, LLB`(person)
- `Beer-Hofmann-Weg 155, 4710 Schönau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `17-630/1579`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/134989.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134989.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Leitgebel  in der Beschwerdesache ÖkR Achmed von Lampe,  Kreuzbach 25, 6441 Köfels, Österreich, vertreten durch WIRTSCHAFTSTREUHAND Steuerberatung GmbH,  Ohlsdorferstraße 18, 4810 Gmunden, über die Beschwerde vom 31. Jänner 2020 gegen den  Bescheid des FA Steiermark Mitte  vom 28. Jänner 2020 betreffend Abweisung eines Antrages auf  Aussetzung der Einhebung gemäß § 212a BAO, Steuernummer 05-972/9664, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache ÖkR Achmed ` — positional overlap with gold: `ÖkR Achmed von Lampe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Huberta Leitgebel`(person)
- `ÖkR Achmed von Lampe`(person)
- `Kreuzbach 25, 6441 Köfels, Österreich`(address)
- `WIRTSCHAFTSTREUHAND Steuerberatung GmbH`(organisation)
- `FA Steiermark Mitte`(organisation)
- `05-972/9664`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/135131.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135131.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Lindermeier  in der Beschwerdesache PhD Jeanne Goethemann, BSc,  Weindlau 45, 4230 Zudersdorf, Österreich, vertreten durch Gstöttner Ratzinger Stellnberger Wirtschaftsprüfung  Steuerberatung GmbH, Stelzhamerstraße 14b, 4400 Steyr, über die Beschwerde vom  14.10.2011 gegen den Bescheid des FA Braunau Ried Schärding  vom 22.9.2011 betreffend Festsetzung von  Verspätungszuschlägen 1/2011 – 7/2011 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `in der Beschwerdesache PhD Jeanne Goethemann` — positional overlap with gold: `PhD Jeanne Goethemann, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Lindermeier`(person)
- `PhD Jeanne Goethemann, BSc`(person)
- `Weindlau 45, 4230 Zudersdorf, Österreich`(address)
- `Gstöttner Ratzinger Stellnberger Wirtschaftsprüfung  Steuerberatung GmbH`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/135360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135360.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der KommR Dipl. Kff. Elvira Siegburg, Am Bürgerkogel 8, 3571 Stallegg, Österreich, vertreten durch die FreiTAX Wirtschaftsprüfungs- und  SteuerberatungsGmbH & Co KG, Rennweg 30, 6020 Innsbruck, über die Beschwerde vom  15. September 2021 gegen den Bescheid des Finanzamtes Österreich vom 26. August 2021  betreffend Abweisung des Antrages auf Berichtigung des Einkommensteuerbescheides 2018  gemäß § 293b BAO, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `in der Beschwerdesache  der KommR Dipl` — positional overlap with gold: `KommR Dipl. Kff. Elvira Siegburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `KommR Dipl. Kff. Elvira Siegburg`(person)
- `Am Bürgerkogel 8, 3571 Stallegg, Österreich`(address)
- `FreiTAX Wirtschaftsprüfungs- und  SteuerberatungsGmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/135431.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135431.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Fiona Halberscheid  in der Beschwerdesache MedR Jan Kothmeier,  Johann-Brunauer-Straße 1, 9020 Klagenfurt, Österreich, vertreten durch Hintermeier & Partner Rechtsanwälte, Andreas Hoferstr 8,  3100 St. Pölten, über die Beschwerden  1) vom 10. April 2019 gegen den Bescheid des Finanzamt Gmunden Vöcklabruck  vom 11. März 2019 betreffend  Festsetzung von ersten Säumniszuschlägen und  2) vom 13. September 2019 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 21. August 2019 und vom  22. August 2019 über die Festsetzung von Aussetzungszinsen  Steuernummer 25-981/8877, zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache MedR Jan Kothmeier` — partial — gold is substring of pred: `MedR Jan Kothmeier`

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

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache OMedR Lewis Scherrieb, Brunnhäuserweg 22R, 6080 Vill, Österreich, über die Beschwerde vom 19. Oktober 2020 gegen den Bescheid des Finanzamtes  Österreich vom 1. Oktober 2020 betreffend Familienbeihilfe 06.2015-02.2018, Steuernummer  30-264/4672, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache OMedR Lewis Scherrieb` — partial — gold is substring of pred: `OMedR Lewis Scherrieb`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Lewis Scherrieb`(person)
- `Brunnhäuserweg 22R, 6080 Vill, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `30-264/4672`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/135592.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135592.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  ÖkR Dipl.-Ing. Dipl. Kfm. Raimund Teschmer, Liebigstraße 2, 4725 Kößlau, Österreich, vom 17. Dezember 2021, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 1. Dezember 2021, GZ.  MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parko- meterabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016, in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `des  ÖkR Dipl` — positional overlap with gold: `ÖkR Dipl.-Ing. Dipl. Kfm. Raimund Teschmer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `ÖkR Dipl.-Ing. Dipl. Kfm. Raimund Teschmer`(person)
- `Liebigstraße 2, 4725 Kößlau, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Priv.-Doz.in Laetitia Pöstges, Krist 12, 3843 Riegers, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `der  Priv.-Doz.in Laetitia Pöstges` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Priv.-Doz.in Laetitia Pöstges`(person)
- `Krist 12, 3843 Riegers, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_50`)


4. In dem dagegen fristgerecht eingebrachten Vorlageantrag vom 01.04.2020 wurde zunächst  auf die beiden Beschwerden verwiesen und weiter vorgebracht:  „Frau Priv.-Doz.in Laetitia Pöstges  ist Schweizer Staatsbürgerin.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_60`)


Frau Priv.-Doz.in Laetitia Pöstges  hat auch einen starken persönlichen Bezug zur Schweiz.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_65`)


Der  anonymen Anzeige ist unschwer zu entnehmen, dass irgendjemand Frau Priv.-Doz.in Laetitia Pöstges  und Herrn  4 von 9 Seite 5 von 9

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_68`)


Nachdem Herr A. erst seit 23.5.2016 in Ort1 (Ö) wohnhaft ist, ist es ausgeschlossen, dass Frau  Priv.-Doz.in Laetitia Pöstges  seit 5-6 Jahren bei ihm in Ort1 (Ö) wohnhaft ist.

**False Positives:**

- `Frau  Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_70`)


Frau  Priv.-Doz.in Laetitia Pöstges  hat Herrn A. erst vor ca 4 - 5 Jahren kennengelernt.

**False Positives:**

- `Frau  Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_71`)


Nachdem sich diese  Freundschaft intensivierte, kam Herr A. zu Frau Priv.-Doz.in Laetitia Pöstges  nach Ort1 (CH).

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_73`)


Erst vor ca 3 Jahren besuchte Frau Priv.-Doz.in Laetitia Pöstges  Herrn A. erstmals in Ort1  (Ö).

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  Herrn ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_74`)


Frau Priv.-Doz.in Laetitia Pöstges  hat immer wieder bei ihrem Freund, Herrn A., übernachtet;

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_77`)


Frau Priv.-Doz.in Laetitia Pöstges  ist weder Eigentümerin, Mieterin, Ehegattin oder  sonst irgendwie nachhaltig berechtigt, im Haus von Herrn A. zu übernachten oder es sonst wie  zu nutzen.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_81`)


Er hat  regelmäßig zu Mittag bei Frau Priv.-Doz.in Laetitia Pöstges  gegessen und auch immer wieder bei ihr genächtigt.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_82`)


Er hatte dort auch familiären Kontakt zur Mutter von Frau Priv.-Doz.in Laetitia Pöstges.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_83`)


Entweder schläft Frau  Priv.-Doz.in Laetitia Pöstges  bei Herrn A., oder Herr A. bei Frau Priv.-Doz.in Laetitia Pöstges  in der Schweiz.

**False Positives:**

- `Frau  Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`
- `Frau Priv.-Doz.in Laetitia Pöstges  ` — similar text (different position): `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)
- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_84`)


Auch die  Wochenenden werden sowohl in Vorarlberg als auch in der Schweiz verbracht, wobei  diesbezüglich auf die Angaben von Frau Priv.-Doz.in Laetitia Pöstges  anlässlich ihrer Einvernahme vom  18.11.2019 verwiesen wird.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_85`)


Als die Beziehung ein Level erreicht hat, bei dem es um die Planung einer gemeinsamen  Zukunft ging, haben Frau Priv.-Doz.in Laetitia Pöstges  und Herr A. beschlossen, einen Immobilienmakler zu  beauftragen um ein Haus in der Schweiz zu suchen, in das sie gemeinsam einziehen und einen  gemeinsamen Wohnsitz gründen wollten.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_88`)


Frau Priv.-Doz.in Laetitia Pöstges  ist daher zweifellos in Ort1 (CH) steuerlich ansässig.

**False Positives:**

- `Frau Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/137040.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137040.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Alois Steinfeldt  in der Beschwerdesache RgR Meinrad Leibküchler,  Hintersteindl 2, 5122 Kreil, Österreich, vertreten durch UnionTAX & LAW, Donau-City-Straße 7/DC Tower/30th Floor,  1220 Wien, betreffend Säumnisbeschwerde vom 8.4.2022 betreffend Einkommensteuer 2020  (Arbeitnehmerveranlagung) gegen die Amtspartei FA Österreich  beschlossen:    Das Beschwerdeverfahren wird gem. § 284 Abs 2 BAO eingestellt.   Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 iVm Abs. 9  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `in der Beschwerdesache RgR Meinrad Leibküchler` — partial — gold is substring of pred: `RgR Meinrad Leibküchler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Alois Steinfeldt`(person)
- `RgR Meinrad Leibküchler`(person)
- `Hintersteindl 2, 5122 Kreil, Österreich`(address)
- `Verwaltungsgerichtshof`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/137083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  KommR Dimitri Grabig, Valschalangweg 61, 9322 Eberdorf, Österreich, über die Beschwerde vom 22. Oktober 2019 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Salzburg-Stadt) vom 10. Oktober 2019  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018, Steuernummer  05-254/8190  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache  KommR Dimitri Grabig` — partial — gold is substring of pred: `KommR Dimitri Grabig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `KommR Dimitri Grabig`(person)
- `Valschalangweg 61, 9322 Eberdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Salzburg-Stadt`(organisation)
- `05-254/8190`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/137198.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Helena Kemmerer  in der Beschwerdesache  ÖkR Jeannine Radmacher, Hirsbodenstraße 5, 4710 Neuwies, Österreich, vertreten durch Rechtsanwälte Offer & Partner OG, Museumstraße  16, 6020 Innsbruck, über die Beschwerde vom 4. Mai 2022 gegen den Bescheid des  Finanzamtes Österreich vom 4. April 2022, StrNr, betreffend Zurückweisung des Antrages vom  31.12.2020 auf "Durchführung einer Lohnsteuerprüfung gemäß § 86 EStG" zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache  ÖkR Jeannine Radmacher` — partial — gold is substring of pred: `ÖkR Jeannine Radmacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Helena Kemmerer`(person)
- `ÖkR Jeannine Radmacher`(person)
- `Hirsbodenstraße 5, 4710 Neuwies, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/137437.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Armin Maierle  in der Beschwerdesache HR Verona Hajny, LLM,  Heiligengestadeweg 46, 4841 Hocheck, Österreich, über die Beschwerde vom 5. Oktober 2011 gegen den Bescheid des Finanzamt Klagenfurt St. Veit Wolfsberg  vom 1. September 2011 betreffend Körperschaftsteuer 2009 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache HR Verona Hajny` — positional overlap with gold: `HR Verona Hajny, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Armin Maierle`(person)
- `HR Verona Hajny, LLM`(person)
- `Heiligengestadeweg 46, 4841 Hocheck, Österreich`(address)
- `Finanzamt Klagenfurt St. Veit Wolfsberg`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/137633.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137633.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache StR Priv.-Doz.in Annemarie Zaydler, Michael Denis-Straße 135, 4074 Kleinstroheim, Österreich, (Beschwerdeführer, abgekürzt: Bf.), vertreten  durch RA-GmbH, RA-Adresse, über die Beschwerde des Bf. vom 8. Juli 2022 gegen den  Bescheid des Magistrates der Stadt Wien, MBA 2/20, Brigittaplatz 10, 1200 Wien vom 30. April  2020 zur Geschäftszahl GZ betreffend Zurückweisung des Antrages des Bf. vom 28.04.2020 auf  aliquote Rückzahlung der Parkometerabgabe für den Zeitraum von 16.03.2020 bis 26.04.2020,  nach Durchführung einer mündlichen Verhandlung am 3. August 2022 in Anwesenheit des  Schriftführers Sf, zu Recht erkannt:  Der Beschwerde wird stattgegeben und gemäß § 279 Abs. 1 BAO wird der angefochtene  Bescheid ersatzlos aufgehoben.

**False Positives:**

- `in der  Beschwerdesache StR Priv` — positional overlap with gold: `StR Priv.-Doz.in Annemarie Zaydler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `StR Priv.-Doz.in Annemarie Zaydler`(person)
- `Michael Denis-Straße 135, 4074 Kleinstroheim, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/137652.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger  in der Beschwerdesache KommR Manuel Schmeikal,  Fimbabahnweg 6, 8993 Gößl, Österreich, über die Beschwerde vom 13. Juni 2019 gegen den Bescheid des Finanzamt St. Johann Tamsweg Zell am See  vom 3. Juni 2019 über die Rückforderung zu Unrecht bezogener Beträge Familienbeihilfe und  Kinderabsetzbetrag für März 2018 bis Mai 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache KommR Manuel Schmeikal` — partial — gold is substring of pred: `KommR Manuel Schmeikal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Mag.a Annalena Dietmannsperger`(person)
- `KommR Manuel Schmeikal`(person)
- `Fimbabahnweg 6, 8993 Gößl, Österreich`(address)
- `Finanzamt St. Johann Tamsweg Zell am See`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/137723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137723.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin BE in der Beschwerdesache OSR Dr. Jonas Witzorke,  Preber 31, 3874 Haugschlag, Österreich, betreffend Beschwerde vom 29. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 26. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 58-061/2981, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `in der Beschwerdesache OSR Dr` — positional overlap with gold: `OSR Dr. Jonas Witzorke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Dr. Jonas Witzorke`(person)
- `Preber 31, 3874 Haugschlag, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `58-061/2981`(tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/138498.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138498.1_26`)


Die Mutter des gemeinsamen Kindes, Frau Univ.-Prof.in Tatjana Madenci, BSc, ist mit September 2019 mit  dem gemeinsamen Kind nach Deutschland verzogen.

**False Positives:**

- `Frau Univ.-Prof.in Tatjana Madenci` — positional overlap with gold: `Univ.-Prof.in Tatjana Madenci, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Tatjana Madenci, BSc`(person)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/138511.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  VetR MedR Annette Weikard, Michael Glaser Gasse 11, 9500 Pogöriach, Österreich, über die Beschwerden vom 10. September 2018 gegen die  Bescheide des Finanzamtes Österreich vom 31. August 2018 betreffend Grunderwerbsteuer,  StNr 10-24-662/4687  zu Recht erkannt:   1)

**False Positives:**

- `in der Beschwerdesache  VetR Med` — positional overlap with gold: `VetR MedR Annette Weikard`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `VetR MedR Annette Weikard`(person)
- `Michael Glaser Gasse 11, 9500 Pogöriach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `10-24-662/4687`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_9`)


In der von Thilo Tenbrock  und HR Bertha Stölzel  eingebrachten Beschwerde vom 22.4.2021 betreffend  die Jahre 2016 – 2020 wird auf das Schreiben der HR Bertha Stölzel  vom 19.4.2021 verwiesen.

**False Positives:**

- `der HR Bertha Stölzel  ` — similar text (different position): `HR Bertha Stölzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thilo Tenbrock`(person)
- `HR Bertha Stölzel`(person)
- `HR Bertha Stölzel`(person)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_28`)


Strittig ist, ob die Einkünfte aus der Vermietung den Ehegatten je zur Hälfte oder ausschließlich  Frau HR Bertha Stölzel  zuzurechnen sind.

**False Positives:**

- `Frau HR Bertha Stölzel  ` — partial — gold is substring of pred: `HR Bertha Stölzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HR Bertha Stölzel`(person)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_61`)


Zusammenfassend ist festzustellen, dass eine Bewirtschaftung des(r) Appartements bzw die  Tragung des Unternehmerrisikos ausschließlich durch Frau HR Bertha Stölzel  alleine nicht erkennbar  ist.

**False Positives:**

- `Frau HR Bertha Stölzel  ` — partial — gold is substring of pred: `HR Bertha Stölzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HR Bertha Stölzel`(person)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_25`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Camilla Schiedmann“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `bei BA Sozial` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Camilla Schiedmann`(person)

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_43`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Camilla Schiedmann“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `bei BA Sozial` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Camilla Schiedmann`(person)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/138708.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138708.1_44`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `des BA Sozial` — no gold match — likely missing annotation
- `des BA Wirtschaftswissenschaften ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/138877.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138877.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache MedR Griselda Kaever, Bakk. rer. nat., Gasener-Straße 334, 5261 Lohnau, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauer Straße 39/I/Top 12, 1220 Wien, über die Beschwerden vom 5. April 2016 gegen die  Bescheide des Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und  Abgabewesen vom 07. März 2016, mit welchen die Anträge auf Aufhebung der  Kommunalsteuer- und Dienstgeberabgabebescheide für die Jahre 2008 und 2009 abgewiesen  wurden, zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der  Beschwerdesache MedR Griselda Kaever` — positional overlap with gold: `MedR Griselda Kaever, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `MedR Griselda Kaever, Bakk. rer. nat.`(person)
- `Gasener-Straße 334, 5261 Lohnau, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/138927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  StR Cornelius Pfeilschifter, Thal-Wendlleiten 45, 8522 Kraubath in der Weststeiermark, Österreich, über die Beschwerde vom 28. November 2019 gegen den Bescheid  des Finanzamtes Salzburg-Stadt (nunmehr Finanzamtes Österreich ) vom 14. November 2019  betreffend die Wiederaufnahme des Einkommensteuerverfahrens 2013 zu Recht erkannt:  I)  Der Wiederaufnahmebescheid wird aufgehoben.

**False Positives:**

- `in der Beschwerdesache  StR Cornelius Pfeilschifter` — partial — gold is substring of pred: `StR Cornelius Pfeilschifter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `StR Cornelius Pfeilschifter`(person)
- `Thal-Wendlleiten 45, 8522 Kraubath in der Weststeiermark, Österreich`(address)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/139178.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139178.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Egon Dervis  in der Beschwerdesache OMedR Thassilo Rotaug,  Karl-Kapferer-Straße 198, 8225 Winkl-Boden, Österreich, über die Beschwerde vom 17. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 14. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 66-732/8629  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache OMedR Thassilo Rotaug` — partial — gold is substring of pred: `OMedR Thassilo Rotaug`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Egon Dervis`(person)
- `OMedR Thassilo Rotaug`(person)
- `Karl-Kapferer-Straße 198, 8225 Winkl-Boden, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `66-732/8629`(tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Helwege  in der Beschwerdesache Techn R Martina Meyerhuber,  Dapontegasse 7, 4273 Neumühl, Österreich, über die Beschwerde vom 4. Oktober 2018 gegen den Bescheid des  Finanzamtes Landeck Reutte, nunmehr Finanzamt Österreich, vom 19. September 2018, SV-Nr,  betreffend Abweisung der Anträge auf Familienbeihilfe und Erhöhungsbetrag zur  Familienbeihilfe vom 27.4.2018 nach Durchführung einer mündlichen Verhandlung zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache Techn R Martina Meyerhuber` — partial — gold is substring of pred: `Techn R Martina Meyerhuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Petra Helwege`(person)
- `Techn R Martina Meyerhuber`(person)
- `Dapontegasse 7, 4273 Neumühl, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_4`)


Mit Anträgen Beih1 und Beih3 vom 27.4.2018 hat Herr Techn R Martina Meyerhuber (= Beschwerdeführer, Bf),  geb. Juli 1982, die Zuerkennung von Familienbeihilfe "ab 01/16" und Erhöhungsbetrag "ab  1989" wegen erheblicher Behinderung für sich beantragt.

**False Positives:**

- `Herr Techn R Martina Meyerhuber ` — partial — gold is substring of pred: `Techn R Martina Meyerhuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Martina Meyerhuber`(person)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_18`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:  ja  GdB liegt vor seit:   05/2018  Herr Techn R Martina Meyerhuber  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  NEIN  Anmerkung bzw Begründung betreffend die Fähigkeit bzw voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Es ergeben sich keine Hinweise, dass die Erwerbsfähigkeit dauerhaft aufgehoben ist.

**False Positives:**

- `Herr Techn R Martina Meyerhuber  ` — partial — gold is substring of pred: `Techn R Martina Meyerhuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Martina Meyerhuber`(person)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/139231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139231.1_157`)


Herr Techn R Martina Meyerhuber  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:   NEIN   Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:   Es ist keine irreparable Hirnschädigung festzustellen bzw. nach dem Gesichtsschädeltrauma  10 von 20 Seite 11 von 20

**False Positives:**

- `Herr Techn R Martina Meyerhuber  ` — partial — gold is substring of pred: `Techn R Martina Meyerhuber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Martina Meyerhuber`(person)

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/139288.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139288.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde der KommR Miklos Werhan, Darmstadtgasse 43, 4722 Dunkenedt, Österreich, vom 3. November 2022 gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 27. Oktober 2022, GZ. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `der KommR Miklos Werhan` — partial — gold is substring of pred: `KommR Miklos Werhan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KommR Miklos Werhan`(person)
- `Darmstadtgasse 43, 4722 Dunkenedt, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/139514.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139514.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache von Herrn ÖkR Ing. Stephanie Seiderer, Unterer Platz 29, 3852 Gastern, Österreich  vertreten durch Vertreter, Wien, zum  Vorlageantrag vom 18. Oktober 2019 gegen den (Sammel-)Bescheid des damaligen  Finanzamtes Salzburg-Land vom 6. September 2019 betreffend Nachsicht gemäß § 236 BAO zu  Steuernummer 40-949/8179  beschlossen:  Der Vorlageantrag vom 18. Oktober 2019 wird – soweit es die Nachsicht betrifft – gemäß § 264  Abs. 4 lit. e BAO i.V.m. § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Herrn ÖkR Ing` — positional overlap with gold: `ÖkR Ing. Stephanie Seiderer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `ÖkR Ing. Stephanie Seiderer`(person)
- `Unterer Platz 29, 3852 Gastern, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `40-949/8179`(tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/139514.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139514.1_5`)


Begründung  Im Schreiben vom 26. August 2019 beantragte Herr ÖkR Ing. Stephanie Seiderer (neben einem Antrag gemäß §  295 Abs. 4 BAO) auch die Nachsicht und die Stundung von Abgaben.

**False Positives:**

- `Herr ÖkR Ing` — positional overlap with gold: `ÖkR Ing. Stephanie Seiderer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖkR Ing. Stephanie Seiderer`(person)

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Klarissa Hallac, Kartäuserstraße 7, 9963 Unterrotte, Österreich  über den Vorlageantrag vom 04.07.2014 gegen die  Beschwerdevorentscheidung des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener  Wasser, vom 02.06.2014 über die Beschwerde des PhD Erwin Vanicek, Ing.-Franz-Zauner-Gasse 4, 3644 Fahnsdorf, Österreich, vom  17.03.2014 gegen den Bescheid vom 04.03.2014 betreffend Herabsetzung der  Abwassergebühr, MA 31 – 0024363/12, zu Recht erkannt:   I. Die Beschwerdevorentscheidung wird gemäß § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `des PhD Erwin Vanicek` — partial — gold is substring of pred: `PhD Erwin Vanicek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Klarissa Hallac`(person)
- `Kartäuserstraße 7, 9963 Unterrotte, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)
- `PhD Erwin Vanicek`(person)
- `Ing.-Franz-Zauner-Gasse 4, 3644 Fahnsdorf, Österreich`(address)

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_5`)


Mit Beschwerdevorentscheidung vom 02.06.2014, die an die Klarissa Hallac  zuhanden des  PhD Erwin Vanicek  gerichtet war, wurde die Beschwerde mit ausführlicher Begründung als  unbegründet abgewiesen.

**False Positives:**

- `des  PhD Erwin Vanicek  ` — partial — gold is substring of pred: `PhD Erwin Vanicek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klarissa Hallac`(person)
- `PhD Erwin Vanicek`(person)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_12`)


2. Beweiswürdigung  Der geschilderte Verfahrensgang stützt sich auf die von der belangten Behörde im Rahmen der  Aktenvorlage übermittelten oben genannten Schriftstücke, insbesondere die Beschwerde des  PhD Erwin Vanicek, in der die Klarissa Hallac  mit keinem Wort erwähnt wird.

**False Positives:**

- `des  PhD Erwin Vanicek` — partial — gold is substring of pred: `PhD Erwin Vanicek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Erwin Vanicek`(person)
- `Klarissa Hallac`(person)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_25`)


Die  gegenständliche Beschwerde ist objektiv betrachtet im eigenen Namen des PhD Erwin Vanicek  und nicht namens einer von ihm vertretenen Partei eingebracht worden.

**False Positives:**

- `des PhD Erwin Vanicek  ` — partial — gold is substring of pred: `PhD Erwin Vanicek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Erwin Vanicek`(person)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_27`)


Dementsprechend hätte auch die belangte Behörde über die Beschwerde des  PhD Erwin Vanicek  und nicht über die Beschwerde der Klarissa Hallac  mit  Beschwerdevorentscheidung absprechen müssen, da weder von dieser noch in ihrer  Vertretung eine Beschwerde eingebracht worden war.

**False Positives:**

- `des  PhD Erwin Vanicek  ` — partial — gold is substring of pred: `PhD Erwin Vanicek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Erwin Vanicek`(person)
- `Klarissa Hallac`(person)

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/139589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139589.1_34`)


Es wird in diesem Zusammenhang angemerkt, dass über die Beschwerde des PhD Erwin Vanicek  bislang nicht entschieden wurde.

**False Positives:**

- `des PhD Erwin Vanicek  ` — partial — gold is substring of pred: `PhD Erwin Vanicek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Erwin Vanicek`(person)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/139603.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139603.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Manuel Gaberle  in der Beschwerdesache des  HR Dagobert Overman, vertreten durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz,  wegen Verletzung der Entscheidungspflicht (Säumnis) des Finanzamtes Österreich betreffend  Veranlagung zur Einkommensteuer 2017 bis 2019 beschlossen:  I. Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 (letzter Satz) BAO  eingestellt.  II. Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `in der Beschwerdesache des  HR Dagobert Overman` — partial — gold is substring of pred: `HR Dagobert Overman`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuel Gaberle`(person)
- `HR Dagobert Overman`(person)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/139661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Lukas Nauberg, Hölling 5, 4144 Dittmannsdorf, Österreich, über die Beschwerde vom 15. November 2020  gegen den Bescheid des Finanzamtes Österreich vom 14. Oktober 2020 betreffend Aussetzung  § 212a BAO 2020 nach Durchführung einer mündlichen Verhandlung auf Antrag der Partei am  16.12.2022 in Anwesenheit des Beschwerdeführers und von HR Mag. Christian Schneider und  Mag. Peter Wilhelm für das Finanzamt zur Steuernummer 43-674/4510  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `von HR Mag` — positional overlap with gold: `HR Mag. Christian Schneider`

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

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/140017.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140017.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache KommR Bernhard Hadank, Johann Sauer-Gasse 11, 8144 Hautzendorf, Österreich, über die Beschwerde vom 7. April 2021 gegen den Bescheid des Finanzamtes  Österreich vom 5. Februar 2021 betreffend Rechtsgeschäftsgebühr, Steuernummer  09-601/7405, Erfassungsnummer 10-2020, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache KommR Bernhard Hadank` — partial — gold is substring of pred: `KommR Bernhard Hadank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KommR Bernhard Hadank`(person)
- `Johann Sauer-Gasse 11, 8144 Hautzendorf, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `09-601/7405`(tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/140274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140274.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Stephanie Stöfhas  in der Beschwerdesache Techn R Cedric Greuel, MBA,  Breitenschützing 2, 9651 Aigen, Österreich, vertreten durch DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Währinger  Straße 2-4, 1090 Wien, über die Beschwerde vom 14. Februar 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel als Vorgängerorganisation des  Finanzamts Österreich Dienststelle Sonderzuständigkeiten vom 11. Jänner 2019 betreffend   Zahlungerserleichterungsansuchen für Glücksspielabgaben und Wettgebühren 2012  Steuernummer 93-237/4757  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache Techn R Cedric Greuel` — positional overlap with gold: `Techn R Cedric Greuel, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Stephanie Stöfhas`(person)
- `Techn R Cedric Greuel, MBA`(person)
- `Breitenschützing 2, 9651 Aigen, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamts Österreich`(organisation)
- `93-237/4757`(tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/141397.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141397.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache ÖkR Helge Moravec,  Krinnerweg 8, 3233 Fleischessen, Österreich, vertreten durch Mag. Heimo Switil, Ignaz Glaser Straße 26 Tür 6, 5111  Bürmoos, über die Beschwerde vom 23. November 2021 gegen den Bescheid des Finanzamtes  Österreich vom 18. November 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 Steuernummer 72-764/7503  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `in der Beschwerdesache ÖkR Helge Moravec` — partial — gold is substring of pred: `ÖkR Helge Moravec`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `ÖkR Helge Moravec`(person)
- `Krinnerweg 8, 3233 Fleischessen, Österreich`(address)
- `Mag. Heimo Switil`(person)
- `Finanzamtes  Österreich`(organisation)
- `72-764/7503`(tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TRAIN/141773.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marianne Heimbold  in der Beschwerdesache des  StR Jessica Muschelknautz, Weichseltalweg 13, 4616 Graßing, Österreich, über die Beschwerde vom 30. Mai 2022 gegen den Bescheid des  Finanzamt Judenburg Liezen  vom 18. Mai 2022 betreffend Pfändung einer Geldforderung zu Steuernummer  91-049/7035  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache des  StR Jessica Muschelknautz` — partial — gold is substring of pred: `StR Jessica Muschelknautz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Marianne Heimbold`(person)
- `StR Jessica Muschelknautz`(person)
- `Weichseltalweg 13, 4616 Graßing, Österreich`(address)
- `Finanzamt Judenburg Liezen`(organisation)
- `91-049/7035`(tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_TRAIN/141996.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. über die  Beschwerde der Hon.-Prof.in Cynthia Körber, Madersperger-Straße 52N, 8570 Aichegg, Österreich, vom 10. August 2023, gegen das Straferkenntnis  der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als  Abgabenstrafbehörde vom 13. Juli 2023, GZ. MA67/GZ/2023, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr.  71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

**False Positives:**

- `der Hon.-Prof.in Cynthia Körber` — partial — gold is substring of pred: `Hon.-Prof.in Cynthia Körber`

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

**Example 93** (doc_id: `deanon_BFG_20260814_TRAIN/142273.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ingolf Schloßnickel  in der Beschwerdesache Dr.in Ing. Frauke Mühlenthaler,  Kettensteggasse 37a, 5261 Sonnleiten, Österreich, vertreten durch Kitzbühler WTH Dkfm Dr Karl Koller KG, Josef-Pirchl-Straße 18,  6370 Kitzbühel, über die Beschwerde vom 17. Mai 2021 gegen den Bescheid des Finanzamtes  Österreich vom 11. Mai 2021 betreffend Festsetzung einer Zwangsstrafe, Steuernummer  74-573/4900,  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache Dr.in Ing` — positional overlap with gold: `Dr.in Ing. Frauke Mühlenthaler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Ingolf Schloßnickel`(person)
- `Dr.in Ing. Frauke Mühlenthaler`(person)
- `Kettensteggasse 37a, 5261 Sonnleiten, Österreich`(address)
- `Dkfm Dr Karl Koller KG`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `74-573/4900`(tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_TRAIN/142425.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142425.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Benedikt Kastener  in der Beschwerdesache Techn R Dipl.-Ing. Jaqueline Naglschmid,  Strechen 6K, 3872 Amaliendorf, Österreich, vertreten durch MEMO Wirtschaftstreuhandges.m.b.H., Utzstraße 11 Tür 4,  3500 Krems/Donau, über die Beschwerde vom 24. Mai 2017 gegen die Bescheide des  Finanzamtes Österreich vom 26. April 2017 betreffend Säumniszuschlag 01.2012-12.2015  Steuernummer 88-919/1905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache Techn R Dipl` — positional overlap with gold: `Techn R Dipl.-Ing. Jaqueline Naglschmid`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mag. Benedikt Kastener`(person)
- `Techn R Dipl.-Ing. Jaqueline Naglschmid`(person)
- `Strechen 6K, 3872 Amaliendorf, Österreich`(address)
- `MEMO Wirtschaftstreuhandges.m.b.H.`(person)
- `Finanzamtes Österreich`(organisation)
- `88-919/1905`(tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_TRAIN/142669.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142669.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Josepha de Felice  in der Beschwerdesache HR Josefine Klingemann,  Bichlwangerstraße 9Y, 4673 Höft, Österreich  über Säumnisbeschwerde vom 23. Oktober 2023, mittels welcher die  Entscheidung über die am 10. Februar 2023 eingebrachte Erklärung zur  Arbeitnehmerveranlagung 2023 (samt Nachmeldung am 1. März 2023) sowie die Auszahlung  des zu erwartenden Guthabens „urgiert“ wurde, zu Steuernummer 79-010/2205, zu Recht  erkannt:   I. Die eingebrachte Säumnisbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache HR Josefine Klingemann` — partial — gold is substring of pred: `HR Josefine Klingemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Josepha de Felice`(person)
- `HR Josefine Klingemann`(person)
- `Bichlwangerstraße 9Y, 4673 Höft, Österreich`(address)
- `79-010/2205`(tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_TRAIN/142675.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142675.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Beschwerdesache RgR Techn R Frederike Brasche, Karl-Angermann-Weg 5, 5121 Tarsdorf, Österreich, über die Beschwerde vom 9. November 2015  gegen die Bescheide des Finanzamtes St. Veit Wolfsberg (nunmehr Finanzamtes Österreich)  vom 19. Oktober 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013 und  2014, Steuernummer 58-015/7701, zu Recht erkannt:   I. Die Beschwerde betreffend Einkommensteuer 2013 wird gemäß § 279 Abs. 1 BAO als  unbegründet abgewiesen.

**False Positives:**

- `in der  Beschwerdesache RgR Techn ` — positional overlap with gold: `RgR Techn R Frederike Brasche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Wolfgang Pagitsch`(person)
- `RgR Techn R Frederike Brasche`(person)
- `Karl-Angermann-Weg 5, 5121 Tarsdorf, Österreich`(address)
- `Finanzamtes St. Veit Wolfsberg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `58-015/7701`(tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_TRAIN/143871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/143871.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Judith Brocks  in der Beschwerdesache des  VetR Stephanie Kabak, Zennergasse 325, 9360 Engelsdorf, Österreich, über die Beschwerde vom 12. Juli 2023 gegen den Bescheid des  FA Graz-Stadt  vom 21. Juni 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  zu Steuernummer 70-314/9067  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache des  VetR Stephanie Kabak` — partial — gold is substring of pred: `VetR Stephanie Kabak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Judith Brocks`(person)
- `VetR Stephanie Kabak`(person)
- `Zennergasse 325, 9360 Engelsdorf, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `70-314/9067`(tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_TRAIN/144045.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144045.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Karsten Betsch  in der Beschwerdesache RgR Oskar Thiergart,  Hauptschulweg 31, 4751 Augendobl, Österreich, über die Beschwerde vom 23. April 1998 gegen den Bescheid des Finanzamt Salzburg-Stadt  vom 7. Jänner 1998 betreffend Einkommensteuer 1996 zu Recht erkannt:   I.   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `in der Beschwerdesache RgR Oskar Thiergart` — partial — gold is substring of pred: `RgR Oskar Thiergart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Karsten Betsch`(person)
- `RgR Oskar Thiergart`(person)
- `Hauptschulweg 31, 4751 Augendobl, Österreich`(address)
- `Finanzamt Salzburg-Stadt`(organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_TRAIN/144066.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  HR Viola Spital, Häuserer Gasse 37, 3720 Gaindorf, Österreich, über die Beschwerde vom 16. August 2022 gegen den Bescheid des  Finanzamtes Österreich vom 6. Juli 2022 betreffend Aussetzung § 212a BAO 2022,  Steuernummer 17-017/6587  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `in der Beschwerdesache  HR Viola Spital` — partial — gold is substring of pred: `HR Viola Spital`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `HR Viola Spital`(person)
- `Häuserer Gasse 37, 3720 Gaindorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `17-017/6587`(tax_number)

</details>

---

## `Title Name Extraction` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5af11c0c`  
**Description:**
Captures names with titles in other contexts, ensuring the title is part of the match and the name follows immediately, extracting only the name. Requires a preceding context anchor to avoid false positives.

**Content:**
```
(?:Herrn?\s+|Frau\s+|in\s+der\s+Beschwerdesache\s+(?:des\s+|der\s+)?|in\s+der\s+Rechtssache\s+gegen\s+|des\s+|der\s+|als\s+|von\s+|gegen\s+|mit\s+|bei\s+|zu\s+|durch\s+|der\s+|die\s+|das\s+)(?:Dr\.|Dr\.in\s+|Mag\.|Mag\.a\s+|Mag\.in\s+|Mag\.Dr\.|Mag\.Dr\.in\s+|Univ\.-Prof\.|Univ\.-Prof\.in\s+|Priv\.-Doz\.|Priv\.-Doz\.in\s+|Hon\.-Prof\.|Hon\.-Prof\.in\s+|KommR\s+|OSR\s+|StR\s+|OMedR\s+|MedR\s+|PhD\s+|\u00d6kR\s+|VetR\s+|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|LL\.M\.|M\.B\.L\.|MSc\s+|MA\s+|BA\s+|BSc\s+|Ing\.|Dipl\.-Ing\.|RgR\s+|HR\s+|MMag\.|R\.\s+|Techn\s+R\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name at Sentence Start` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `542d60df`  
**Description:**
Captures names appearing at the very beginning of a sentence or after a period, often with a title.

**Content:**
```
(?:^|\.\s+)(?:Dr\.|Dr\.in\s+|Mag\.|Mag\.a\s+|Mag\.in\s+|Mag\.Dr\.|Mag\.Dr\.in\s+|Univ\.-Prof\.|Univ\.-Prof\.in\s+|Priv\.-Doz\.|Priv\.-Doz\.in\s+|Hon\.-Prof\.|Hon\.-Prof\.in\s+|KommR\s+|OSR\s+|StR\s+|OMedR\s+|MedR\s+|PhD\s+|\u00d6kR\s+|VetR\s+|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|LL\.M\.|M\.B\.L\.|MSc\s+|MA\s+|BA\s+|BSc\s+|Ing\.|Dipl\.-Ing\.|RgR\s+|HR\s+|MMag\.|R\.\s+|Techn\s+R\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:LL\.M\.|M\.B\.L\.|MSc|MA|BA|BSc|Bakk\.\s*techn\.|Bakk\.\s*art\.|Bakk\.\s*phil\.|Bakk\.\s*jur\.|PhD|\u00d6kR|OMedR|MedR|VetR|OSR|StR|KommR|HR|RgR|Dr\.|Mag\.|Mag\.a|Mag\.in|Ing\.|Dipl\.-Ing\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|MMag\.|R\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 10 | 2398 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `. ÖkR Horst Stevens` — partial — pred is substring of gold: `Ing. ÖkR Horst Stevens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/131886.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131886.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Alice Rainprechter  in der Verwaltungsstrafsache gegen  Ing. Techn R Arthur Kornhass, Gstaudet 21, 9556 Besendorf, Österreich, über die Beschwerde des Beschuldigten vom 01.10.2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien, vom 07.09.2020, Zahl  MA67/Zahl1/2019, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Erkenntnisses des Bundesfinanzgerichtes vom 16.07.2020, Zahl  RV/Zahl2/2020 zu Zahl MA67/Zahl1/2019, betreffend eine Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird die angefochtene Vollstreckungsverfügung des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `. Techn R Arthur Kornhass` — partial — pred is substring of gold: `Ing. Techn R Arthur Kornhass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Alice Rainprechter`(person)
- `Ing. Techn R Arthur Kornhass`(person)
- `Gstaudet 21, 9556 Besendorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/133151.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133151.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Evamaria Moucha  in der   Beschwerdesache Ing. Techn R Emma Kirmiss, Balikostraße 6, 4072 Winkeln, Österreich, vertreten durch Dr. Michael Jöstl, Bozner Platz 1,  6020 Innsbruck, über die Beschwerde vom 18. Oktober 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 18. September 2018, ErfNr,  betreffend Grunderwerbsteuer   zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `. Techn R Emma Kirmiss` — partial — pred is substring of gold: `Ing. Techn R Emma Kirmiss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Evamaria Moucha`(person)
- `Ing. Techn R Emma Kirmiss`(person)
- `Balikostraße 6, 4072 Winkeln, Österreich`(address)
- `Dr. Michael Jöstl`(person)
- `Finanzamtes für Gebühren`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/133782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133782.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Leonhard Meesters  in der Beschwerdesache Univ.-Prof. MedR Wigand Matthisen,  Auflangenweg 177, 9816 Penk, Österreich, über die Beschwerde vom 26. November 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt FA) vom 2. November 2020 betreffend die  Einkommensteuer für das Jahr 2019, Steuernummer 48-577/9146, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `. MedR Wigand Matthisen` — partial — pred is substring of gold: `Univ.-Prof. MedR Wigand Matthisen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Leonhard Meesters`(person)
- `Univ.-Prof. MedR Wigand Matthisen`(person)
- `Auflangenweg 177, 9816 Penk, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt`(organisation)
- `48-577/9146`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_62`)


Priv.-Doz.in Laetitia Pöstges  ist mit A. befreundet.

**False Positives:**

- `Priv.-Doz.in Laetitia Pöstges  ` — partial — gold is substring of pred: `Priv.-Doz.in Laetitia Pöstges`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in Laetitia Pöstges`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/135955.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135955.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Elisabeth Hafner in der Beschwerdesache  Dipl.-Ing. StR Ali Butzler, Trenninggasse 37, 2130 Hobersdorf, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH,  Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom 30. September 2020 gegen die  Bescheide des Finanzamtes Klagenfurt vom 8. Juli 2020 betreffend  I. die Wiederaufnahme des Verfahrens zur Festsetzung des Vergütungsbetrages nach dem  Energieabgabenvergütungsgesetz für den Zeitraum 2014 und  II. die Festsetzung des Vergütungsbetrages nach dem Energieabgabengesetz für den Zeitraum  2014  I. zu Recht erkannt:  Der Beschwerde gegen den Bescheid betreffend die Wiederaufnahme des Verfahrens zur  Festsetzung des Vergütungsbetrages nach dem Energieabgabenvergütungsgesetz für den  Zeitraum 2014 wird Folge gegeben.

**False Positives:**

- `. StR Ali Butzler` — partial — pred is substring of gold: `Dipl.-Ing. StR Ali Butzler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Dipl.-Ing. StR Ali Butzler`(person)
- `Trenninggasse 37, 2130 Hobersdorf, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Klagenfurt`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/137683.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Matthäus Röske  in der Beschwerdesache Mag. Techn R Burkhard Mühlenberg,  Tennisplatzsiedlung 7, 3386 Hengstberg, Österreich, Tschechische Republik, über die Beschwerde vom 13. Jänner 2021 gegen den  Bescheid des Finanzamt Braunau Ried Schärding  vom 15. Dezember 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 52-669/6200  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `. Techn R Burkhard Mühlenberg` — partial — pred is substring of gold: `Mag. Techn R Burkhard Mühlenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Matthäus Röske`(person)
- `Mag. Techn R Burkhard Mühlenberg`(person)
- `Tennisplatzsiedlung 7, 3386 Hengstberg, Österreich`(address)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `52-669/6200`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_6`)


HR Bertha Stölzel  und  Thilo Tenbrock  sind jeweils als Beteiligte angeführt, sämtliche Vermietungseinkünfte wurde jedoch  ausschließlich HR Bertha Stölzel  zugeordnet.

**False Positives:**

- `HR Bertha Stölzel  ` — partial — gold is substring of pred: `HR Bertha Stölzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HR Bertha Stölzel`(person)
- `Thilo Tenbrock`(person)
- `HR Bertha Stölzel`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_11`)


HR Bertha Stölzel  wandte sich in ihrer Beschwerde vom 19.4.2021 gegen die Aufteilung der Einkünfte,  da diese ausschließlich ihr zuzurechnen seien.

**False Positives:**

- `HR Bertha Stölzel  ` — partial — gold is substring of pred: `HR Bertha Stölzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HR Bertha Stölzel`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/138591.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138591.1_22`)


HR Bertha Stölzel  beantragte die antragsgemäße  Veranlagung.

**False Positives:**

- `HR Bertha Stölzel  ` — partial — gold is substring of pred: `HR Bertha Stölzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HR Bertha Stölzel`(person)

</details>

---

## `Single Letter Initial` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dc359f25`  
**Description:**
Captures single letter initials (e.g., 'M.', 'E.') which appear in legal texts as anonymized names or references, but only when preceded by a context indicating a person (e.g., 'von', 'bei', 'der').

**Content:**
```
(?:von\s+|bei\s+|der\s+|die\s+|des\s+)([A-Z]\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 101 | 0 | 101 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 101 | 2425 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit Erklärung zur Arbeitnehmerveranlagung für das Jahr 2014 begehrte der Beschwerdeführer  (Bf.), der die Tätigkeit eines Alleinvorstandes der H. AG (H. AG) ausübte, die Anerkennung von  Werbungskosten (Arbeitsmittel in Höhe von € 1.397,52) und „Sonstige Werbungskosten“ in  Höhe von € 40.578,41.

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `H. AG`(organisation)
- `H. AG`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_12`)


In Beantwortung des Ergänzungsersuchens teilte der Bf. mit, dass er für den Zeitraum  Februar 2012 bis Februar 2017 als Alleinvorstand der H. AG (Dienstgeberin) bestellt worden  sei, jedoch vorzeitig vom Aufsichtsrat der H. AG ohne detaillierte Angabe von Gründen  abberufen und der Vorstandsvertrag gekündigt worden sei.

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`
- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `H. AG`(organisation)
- `H. AG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_16`)


Die vom Finanzamt in Zweifel gezogenen Aufwendungen für ein Arbeitszimmer stünden  ausschließlich im Zusammenhang mit dem oben angeführten Streitfall, da durch die  Abberufung als Vorstand der H. AG dem Bf. jegliche Infrastruktur entzogen worden sei (siehe  beiliegende Rückgabeliste vom 3. März 2014).

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `H. AG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_28`)


Die Kosten für die Fachzeitschriften seien für 5 Monate  anerkannt worden, da der Bf.  bis Mai 2014 bei der H. AG beschäftigt gewesen sei.

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `H. AG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_54`)


Betreffend das „Arbeitszimmer“ führte der Bf. aus, dass eine Büroinfrastruktur in der Wohnung  des Bf. deshalb notwendig gewesen sei, da ihm im Rahmen der Abberufung als Vorstand der H.  AG der Zugriff auf jegliche Büroinfrastruktur entzogen worden sei.

**False Positives:**

- `der H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_60`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. erzielte im streitgegenständlichen Jahr als Vorstand der H. AG Einkünfte aus  nichtselbständiger Tätigkeit;

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `H. AG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_61`)


von seiner Dienstgeberin wurde ihm ein eigenes Arbeitszimmer in  den Büroräumlichkeiten der H. AG zur Verfügung gestellt.   Strittig ist im vorliegenden Fall die Anerkennung der Aufwendungen für ein im  Wohnungsverband des Bf. gelegenes Arbeitszimmer.

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `H. AG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_71`)


Wenn nun der Bf. in seiner Beschwerde vorbringt, anlässlich der Beendigung seines  Dienstverhältnisses als Vorstand der H. AG habe er sämtliche im Eigentum der Dienstgeberin  stehenden Gegenstände abgeben müssen und dadurch sei ihm jegliche Verfügungsmöglichkeit  über eine ihm zustehende Büroinfrastruktur entzogen worden, ist zu erwidern, dass dies bei  Beendigung eines Dienstverhältnisses üblicherweise so der Fall ist und daher eine gleichzeitige  Begründung eines „häuslichen Arbeitszimmers“ nach Beendigung eines Dienstverhältnisses  nicht für beruflich bzw.betrieblich notwendig erachtet wird.

**False Positives:**

- `der H.` — positional overlap with gold: `H. AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `H. AG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_6`)


Im Zuge der Anspruchsüberprüfung wurde vom Sozialministerium im Juli 2018 mittels   Begutachtung bei S. der Gesamtgrad der Behinderung mit 30% ab 1.10.2018 festgestellt.   Die Bf. brachte am 30.08.2018 einen „Antrag auf erhöhte Familienbeihilfe“ ein, in dem sie  ausführte, dass sie gegen die Ablehnung der erhöhten Familienbeihilfe Berufung erhebe.

**False Positives:**

- `bei S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_28`)


Das genannte Bundesamt habe in der im Beschwerdeverfahren erstellten Bescheinigung bei  S. den erforderlichen Behinderungsgrad für den Bezug des Erhöhungsbetrages bis  einschließlich September 2018 festgestellt. Ab Oktober 2018 sei erneut ein Behinderungsgrad  von 30% festgestellt worden.

**False Positives:**

- `bei  S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_36`)


Im Gutachten des Sozialministeriumservice vom Juli 2018 wurde bei S. der Gesamtgrad der  Behinderung mit 30 % ab 01.10.2018 festgestellt.  Im Gutachten vom 17.12.2018 wurde der Gesamtgrad der Behinderung ebenfalls mit 30 % ab  Oktober 2018 festgestellt.  Eine voraussichtlich dauernde Erwerbsunfähigkeit wurde nicht bescheinigt.

**False Positives:**

- `bei S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_43`)


Kein zusätzlicher Unterstützungsbedarf beim  Lernen  30-40%  Leichte bis mäßige soziale Beeinträchtigung in ein bis zwei Bereichen, beispielsweise  Schulausbildung und alltägliche Tätigkeiten, Freizeitaktivitäten, in Teilbereichen  Unterstützungsbedarf beim Lernen  Die bei S. noch bestehende kombinierte umschriebene Störung der motorischen Funktionen  (leichte Gleichgewichts- und Koordinationsproblematik) wurde von der Sachverständigen  5 von 10 Seite 6 von 10

**False Positives:**

- `bei S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_55`)


Die frühkindliche Entwicklung bei S. verlief etwas verzögert.

**False Positives:**

- `bei S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_74`)


Inwiefern dieser Punkt eine Unzumutbarkeit begründen soll ist nicht ersichtlich, kann aber  dahingestellt bleiben, da im Hinblick auf die Unzumutbarkeit die Jahresbetrachtung gilt. Im  gegenständlichen Jahr 2018, war der Bf. ganzjährig bei der G... BAU GmbH & Co KG beschäftigt.

**False Positives:**

- `der G.` — positional overlap with gold: `G... BAU GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `G... BAU GmbH & Co KG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_110`)


In der Entscheidung vom 16.02.2004, RV/0555-L/03, erwog der unabhängige Finanzsenat:  Die Tatsache, dass die Gattin des Bws. in P [Polen] die Landwirtschaft betreibt, macht nach  Ansicht des unabhängigen Finanzsenates die Verlegung des Familienwohnsitzes von P. [Polen]  nach Ö. [Österreich] unzumutbar.

**False Positives:**

- `von P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_44`)


Der Bf erbrachte keinen Nachweis über Werbungskosten im Zusammenhang mit der Tätigkeit  im Tourismusverbandes A. Auch eine Glaubhaftmachung erfolgte nicht.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130978.1_30`)


Gemäß § 10 Abs. 1 Verwaltungsvollstreckungsgesetz (VVG) 1991 sind auf das  Vollstreckungsverfahren, soweit sich aus diesem Bundesgesetz nicht anderes ergibt, der I. Teil,  hinsichtlich der Rechtsmittelbelehrung die §§ 58 Abs. 1 und 61 und der 2. und 3. Abschnitt des  IV. Teiles des AVG sinngemäß anzuwenden.

**False Positives:**

- `der I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_75`)


In der Literatur finden sich gegenteilige Rechtsansichten von M. Mayr/Pfeiffer (SWK 2017, 895  als Anmerkung zu Beiser), P. Mayr (RWP 2019, 26), Gaedke/Huber-Wurzinger (SWK 2017, 1092)  und Knechtl (SWK 2017, 614).

**False Positives:**

- `von M.` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_29`)


Laut Sachverständigengutachten des Bundesamtes für Soziales und Behindertenwesen (BASB  Landesstelle OÖ) über die Begutachtung am 22.1.2019, in dem ein Gesamtgrad der  Behinderung von 50 % bescheinigt wird, leidet der Beschwerdeführer an    (1) Posttraumatischer Sprunggelenksarthrose rechts bei Z.n. Sprungbeinfraktur,  beginnender Hüft- und Kniegelenksarthrose beidseits (Grad der Behinderung 40 %)   (2) Chronischer Lumbalgie bei degenerativer Wirbelsäulenerkrankung und Z.n.  Bandscheibenoperation L2/L3 (Grad der Behinderung 30 %)   (3) Koronarer Herzkrankheit, Angina pectoris Z.n. erfolgreicher Gefäßaufdehnung und  Stentimplantation (Grad der Behinderung 30 %).

**False Positives:**

- `bei Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)
- `BASB  Landesstelle OÖ`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_153`)


 Einvernahme von Zeugen  Der Bf. beantragte im Zuge seiner Beschwerde die Einvernahme des Meldungslegers sowie die  Einvernahme von A. von der MA 48 und die Einvernahme von B., von der MA 67, ohne dass  dem Erfordernis der Angabe eines konkreten Beweisthemas entsprochen wurde.

**False Positives:**

- `von A.` — no gold match — likely missing annotation
- `von B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132861.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132861.1_157`)


Mangels Bekanntgabe eines konkreten Beweisthemas konnte von der Einvernahme des A. (MA  48) und von B. (MA 67) als Zeugen Abstand genommen werden.

**False Positives:**

- `des A.` — no gold match — likely missing annotation
- `von B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133459.1_214`)


Da der Gesamtbetrag der dort verbuchten AR - neben  diversen AR an den zweiten Hauptauftraggeber der Synkel-Versicherung GmbH– u.a. jene in der A.- Fenster-Buchhaltung bei der L-KEG verbuchten Rechnungen der Synkel-Versicherung GmbH aus dem  3.Quartal 2007 enthielt, wurden in diesem Berechnungsentwurf im Ergebnis die von der Fa A.- Fenster buchhalterisch der L-KEG zugeordneten Rechnungen der Synkel-Versicherung GmbH aus dem Zeitraum  Juni – August 2007 bei beiden Gesellschaften zum Ansatz gebracht.

**False Positives:**

- `der A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Synkel-Versicherung GmbH–`(organisation)
- `Synkel-Versicherung GmbH`(organisation)
- `Synkel-Versicherung GmbH`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_12`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist die Frage strittig, ob die für die Beschwerdeführerin (in der Folge  kurz: Bf.) an zwei inländischen Baustellen tätige X (in der Folge kurz: X oder X.) als  Werkunternehmerin oder aber als bloße Arbeitskräfteüberlasserin (mit der Konsequenz der  Haftung der Bf. für Abzugsteuer) agierte.

**False Positives:**

- `der X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_26`)


Schlussendlich seien die im Jahr 2014 in  Österreich tätig gewesenen Mitarbeiter der X. beim (vormaligen) Finanzamt Y für Zwecke der  Lohnbesteuerung erfasst gewesen.

**False Positives:**

- `der X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_91`)


Anfang November 2012 kamen die Bf. und die X mündlich dahingehend überein, dass die dort  anfallenden reinen Betonierarbeiten untertags durch Arbeitnehmer der X. durchgeführt  werden sollten, dies – wiederum - zu einem Stundensatz von EURO xxxx.

**False Positives:**

- `der X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_149`)


Sowohl Krank-, als auch Urlaubsmeldungen wurden von den Arbeitern  der X. an die Bf. gemeldet, die auch entsprechend Vorsorge für allfällige Vertretungen traf.

**False Positives:**

- `der X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/134126.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134126.1_41`)


Dr. X.Y.“  (BFG-Anm: Fertigung mit unleserlicher Unterschrift und Firmenstampiglie der Kirstin Frischbutter  Wirtschaftstreuhandgesellschaft m.b.H.(nachfolgend Mur-Sanitär GmbH.  In Erledigung dieser Beschwerde erging am 30.Nov.2020 zur Steuernummer (StNr.) der  M.-GmbH eine abweisende Beschwerdevorentscheidung (BVE) an Herrn M. (Direktzustellung  an Herrn M. mit geänderter Bescheidadresse;

**False Positives:**

- `der  M.` — similar text (different position): `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. X.Y.`(person)
- `Kirstin Frischbutter`(person)
- `Mur-Sanitär GmbH`(organisation)
- `M.`(person)
- `M.`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/134737.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134737.1_94`)


Glaubwürdig ist aber, dass jedenfalls zum Zeitpunkt der notariell beglaubigten Erklärung des Bf  und der A., am 31.7.2015, eine Lebensgemeinschaft vorlag.

**False Positives:**

- `der A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/134737.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134737.1_122`)


In den Jahren 2014 – 2016 haben die Einkünfte der A. die Grenze von 6.000 Euro jährlich  überschritten.

**False Positives:**

- `der A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_4`)


Dagegen wurde am 19.10.2020 Beschwerde erhoben und ausgeführt, dass in den Berichten  der Lebenshilfe vom 05.06.2014, des Hilfeplans der BH Hallein Abteilung Kinder- und  Jugendhilfe vom 03.04.2017, im Arztbericht des Dr. Flucher-Wolfram, Ambulatorium für  Entwicklungsdiagnostik, vom 01.03.2018 bzw. im Bericht des Dr. Alexander Holzknecht, KH  Schwarzach, vom 06.07.2020 für D. (und für seinen Bruder A.) die Verhaltensauffälligkeiten,  das Konzentrationsdefizit, die motorische Unruhe, die leichte Ablenkbarkeit, die verminderte  Aufmerksamkeit und das verminderte Durchhaltevermögen festgestellt wurden.

**False Positives:**

- `der A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alexander Holzknecht`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_6`)


Mit Beschwerdevorentscheidung vom 22.04.2021 wurde die Beschwerde als unbegründet  abgewiesen und darauf hingewiesen, dass aufgrund des neuerlichen Gutachtens der  Bundesministeriumservicestelle vom 07.03.2021 der Grad der Behinderung von D. mit 50% erst  ab 01.03.2018 bestätigt wurde.

**False Positives:**

- `von D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/135578.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135578.1_8`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 25.06.2020 stellte die Beschwerdeführerin (Bf) den Antrag auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe (FB) wegen erheblicher Behinderung (ADHS,  Entwicklungsstörung der motorischen Funktionen, Integrationsstörung) ab 06/2015 für das  Kind D..  Mit dem Sachverständigengutachten der Bundesministeriumservicestelle vom 21.09.2020  wurde der Grad der Behinderung des Sohnes D. ab 01.03.2018 mit 50% festgestellt.  Ein weiteres Gutachten der Bundesministeriumservicestelle vom 07.03.2021 bestätigte den  Grad der Behinderung von D. mit 50% erst ab 01.03.2018 bestätigt.

**False Positives:**

- `von D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_27`)


Soziale  Anknüpfungspunkte habe sie in beiden Ländern, in der Schweiz Familienangehörige (Mutter,  Großmutter, Brüder) und Freunde, in Österreich die Schwester von A. und seine Freunde sowie  2 von 9 Seite 3 von 9

**False Positives:**

- `von A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_30`)


Eine  Nachbarin von A. sagte am 5.4.2019 aus, dass sie die Bewohner des Hauses Ort1 (Ö)-Adr kenne  und die Lebensgefährtin von A. regelmäßig um 7:30 Uhr zeitgleich mit ihr losfahre, und zwar  mit einem schwarzen Kombi mit Schweizer Kennzeichen.

**False Positives:**

- `von A.` — no gold match — likely missing annotation
- `von A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_33`)


…   Die Beschwerdeführerin versucht zu dokumentieren, nicht bei A. zu wohnen.

**False Positives:**

- `bei A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_43`)


Das Vorbringen in der später aufgenommenen Niederschrift in sich widersprüchlich, wenn sie  gleichzeitig bestreitet, die Lebensgefährtin des A. zu sein, etwas später jedoch angibt,  grundsätzlich mit ihm zu nächtigen.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_118`)


Zu dieser Annahme hat das Finanzamt in der Beschwerdevorentscheidung vom 27.02.2020  näher begründend ausgeführt, die Angaben der Nachbarin, dass A. zusammen mit der Bf.,  seiner Lebensgefährtin, in Ort1 (Ö) wohne und die Angaben des A., der die Bf. als seine  Lebensgefährtin bezeichnet habe, seien vom Finanzamt gegenüber den Angaben der Bf.,  7 von 9 Seite 8 von 9

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Finanzamt`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_136`)


Dazu sei auch  festgehalten, dass dieser Makler-Such-Auftrag am 16.01.2019 erteilt wurde, also zu einem  Zeitpunkt, in dem die Bf. oder A. noch mit keinen Ermittlungen des Finanzamtes konfrontiert  waren.

**False Positives:**

- `der A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_20`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer (Bf. oder J.P. genannt) und seine Ehegattin haben ihre Tätigkeiten  betreffend die Trink- und Abwasserversorgung der Anrainer beim See I und II, die Vermietung  von dort errichteten Gebäuden sowie deren planmäßigen Verkauf nach wirtschaftlichen und  steuerlichen Aspekten zwischen sich aufgeteilt. Auf Grund einer Generalvollmacht wurden  faktisch alle relevanten Geschäfte vom Bf. vorgenommen.

**False Positives:**

- `der J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_22`)


Auf  Grund eines – vor dem Verkauf dieser Anlagen des Bf. an seine Ehegattin (Gattin.) noch vom  Bf. mit der K. See I (K1) abgeschlossenen Anschluss- und Abnahmevertrages wurden diese  Leistung an die K1 zwar von der Ehegattin erbracht, die Verrechnung an die K1 erfolgte aber  durch den Bf. und seine Ehegattin legte eine entsprechende Rechnung an ihn.

**False Positives:**

- `der K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_32`)


Eine über die gesamten  Jahre erfolgte Betrachtung zeigt folgendes Bild der Ertragssituation:   Die Erträge lt. Jahresabschlüsse 2000 bis 2005 bei J.P. und Gattin:  Erlöse Bf. – J.P. 2000 - ATS 2003 - Euro 2004-

**False Positives:**

- `bei J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_41`)


Die Jahresabschlüsse 2006 bis 2009 bei J.P. und Gattin zeigen folgende Ertragssituation:   Erlöse Bf. – J.P. 2006 2007  2008 2009   Erlöse- Abwasserentsorgung.

**False Positives:**

- `bei J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_7`)


Weiters legte der Bf. vor:   – Übersetzung des Beschlusses des Ungarischen Schatzamtes, Direktion des Komitats  Veszprém vom 27. April 2011 („Die Direktion stellt fest, dass (die Gattin des Bf. und Mutter des  Z.) ab 28. April 2011 auf Beihilfe zur Kinderpflege hinsichtlich (ihres) dauerhaft kranken, schwer  behinderten Kindes, namens Z…, geboren [...Nov.] 2005 berechtigt ist.“).   – Übersetzung des Beschlusses des Ungarischen Regierungsamtes des Komitats Veszprém vom  24. März 2016 („Das Regierungsamt stellt fest, dass der/die Kunde (die Gattin des Bf. und  Mutter des Z.) auf erhöhte Familienbeihilfe in Höhe von 23.300 HUF nach ihrem am  [...11].2005 geborenen Kinde, namens Z…, hinsichtlich der dauerhaften Krankheit und  schweren Behinderung des Kindes gemäß Abs. (1) des § 11 des Gesetzes Nr. LXXXIV  (Familiengesetz) des Jahres 1998 über die Unterstützung der Familien vom 01.03.2016 bis  31.03.2021 berechtigt ist.“)   – Übersetzung einer Bestätigung über ein dauerhaft krankes bzw. schwer behindertes Kind  eines (nicht namentlich genannten) Facharztes [Anm.: Laut beigelegtem Originaldokument ist  die Stampiglie einer Dr.V.I. erkennbar] vom 21. März 2016 („Hiermit wird bestätigt, dass das  oben genannte Kind (Z.) wegen seiner dauerhaften Krankheit bzw. wegen seiner schweren  Behinderung den Tatsachen gemäß Punkt f), Unterpunkt fa) des § 4 des Gesetzes Nr. LXXXIV.  des Jahres 1998 über die Unterstützung der Familien entspricht.

**False Positives:**

- `des  Z.` — no gold match — likely missing annotation
- `des Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_13`)


Nachdem am 29. Oktober 2020 vom Sozialministeriumservice mitgeteilt worden war, dass eine  dauernde Erwerbsunfähigkeit nicht geprüft, ein Grad einer Behinderung nicht festgestellt und  eine Bescheinigung nicht ausgestellt werden konnte, da keine Unterlagen eingelangt seien,  erließ das Finanzamt den angefochtenen Abweisungsbescheid vom 10. November 2020 mit  folgender Begründung:   Da keine Unterlagen betreffend die Erkrankung von Z. vorgelegt wurden, war der Antrag  abzuweisen.

**False Positives:**

- `von Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/136562.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136562.1_18`)


Über die Beschwerde wurde erwogen:  Rechtsgrundlagen und rechtliche Beurteilung:  Gemäß § 10 Abs. 1 VVG idF ab 01.01.2014 sind auf das Vollstreckungsverfahren, soweit sich  aus diesem Bundesgesetz nicht anderes ergibt, der I. Teil, hinsichtlich der Rechtsmittelbe- lehrung die §§ 58 Abs. 1 und 61 und der 2. und 3. Abschnitt des IV. Teiles des AVG sinngemäß  anzuwenden.

**False Positives:**

- `der I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_7`)


Gegen den Abweisungsbescheid wurde Beschwerde vom 17. Mai 2021 eingebracht und der  Erhöhungsbetrag wegen erheblicher Behinderung von J... für den Zeitraum vor Oktober 2020  beantragt mit folgender Begründung:   Laut Sachverständigengutachten vom 12. April 2021 wird der Gesamtgrad der Behinderung  unseres Sohnes J… mit 50 Prozent rückwirkend mit 10/2020 bestätigt.

**False Positives:**

- `von J.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_16`)


Mit Vorhalt vom 4. Februar 2020 wurde die Bf. um Vorlage eines Studienerfolgsnachweises von  T. für das Sommersemester 2019 (Kultur- und Sozialanthropologie an der Uni Wien, (auch  negative Ergebnisse!) sowie um einen Studienerfolgsnachweis der FH Kufstein ab  Studienbeginn ersucht.

**False Positives:**

- `von  T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FH Kufstein`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_157`)


Das Gericht nimmt in freier Beweiswürdigung an, dass die von der FH empfohlenen Übungen in  den Bereichen Langzeitgedächtnis, Textrechenaufgaben, Zahlenreihen, Figurales Denken und  Englischkenntnisse (Leseverständnis, Grammatik, Vokabular) nicht die volle Zeit von T. in  Anspruch genommen haben, da es sich dabei letztlich um Wiederholungen von bereits  Erlerntem handelt.  12 von 13 Seite 13 von 13

**False Positives:**

- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/137203.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137203.1_5`)


Die Beschwerdeführerin ist eine Gesellschaft mit beschränkter Haftung (in der Folge auch  kurz: Bf.), die mit Erklärung über die Errichtung der Gesellschaft samt Einbringungsvertrag vom  12.09.2013 von A. als 100 %iger Gesellschafter gegründet wurde (Neueintragung im  Firmenbuch am 04.10.2013).

**False Positives:**

- `von A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/137203.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137203.1_22`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt und Beweiswürdigung  Die Bf. ist eine Gesellschaft mit beschränkter Haftung, die mit Erklärung über die Errichtung der  Gesellschaft samt Einbringungsvertrag vom 12.09.2013 von A. als 100 %iger Gesellschafter  gegründet wurde (Neueintragung im Firmenbuch am 04.10.2013).

**False Positives:**

- `von A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/138189.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138189.1_18`)


Über die Beschwerde wurde erwogen:  Rechtsgrundlagen und rechtliche Beurteilung:  Gemäß § 10 Abs. 1 VVG idF ab 01.01.2014 sind auf das Vollstreckungsverfahren, soweit sich  aus diesem Bundesgesetz nicht anderes ergibt, der I. Teil, hinsichtlich der Rechtsmittelbe- lehrung die §§ 58 Abs. 1 und 61 und der 2. und 3. Abschnitt des IV. Teiles des AVG sinngemäß  anzuwenden.

**False Positives:**

- `der I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/138511.1`) (sent_id: `deanon_BFG_20260814_TRAIN/138511.1_31`)


Dieser Sachverhalt wird vom Bundesfinanzgericht rechtlich folgendermaßen beurteilt:  § 3 Abs 1 Z 4 GrEStG 1987 lautet:  „Von der Besteuerung sind ausgenommen:  4. der Erwerb eines Grundstückes im Wege eines Zusammenlegungsverfahrens im Sinne des  I. Hauptstückes, I. Abschnitt, und im Wege eines Flurbereinigungsverfahrens im Sinne des  II. Hauptstückes des Flurverfassungs-Grundsatzgesetzes 1951, BGBl Nr 103, in der jeweils  geltenden Fassung,“  Gemäß § 1 Flurverfassungsgrundsatzgesetz ist Zweck dieses Gesetzes die Schaffung und  Erhaltung einer leistungsfähigen und umweltverträglichen Landwirtschaft durch Neueinteilung  und Erschließung des land- und forstwirtschaftlichen Grundbesitzes sowie Ordnung der  rechtlichen und wirtschaftlichen Grundlagen der land- und forstwirtschaftlichen Betriebe nach  zeitgemäßen volks-, betriebswirtschaftlichen und ökologischen Gesichtspunkten im Wege  eines Zusammenlegungsverfahrens.

**False Positives:**

- `des  I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/139132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139132.1_27`)


Das Kind befinde sich vielmehr in einer vollen Erziehung des Landes A. Dies  erhelle sich auch daraus, dass die Bf an das Land A Kostenersätze für eine volle Erziehung zu  erbringen habe.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/139969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139969.1_4`)


Entscheidungsgründe  Verfahrensgang  Der Beschwerdeführer (Bf.), ein ungarischer Staatsbürger, bezog für seine Kinder A., geb. 1, B.,  geb. am 2, und C., geb. am 3, die sich ständig in Land aufhalten, auf Grund seiner Beschäftigung  in Österreich die Differenzzahlung zur Familienbeihilfe plus Kinderabsetzbeträgen.

**False Positives:**

- `der A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_5`)


Familienbeihilfe stehe bei einer ernsthaften und zielstrebigen Ausbildung zu. Die Ausbildung  gelte als ernsthaft und zielstrebig, wenn das Kind die volle Zeit dafür verwende und in  angemessener Zeit zu Prüfungen antrete, was bei T. nicht zutreffe.

**False Positives:**

- `bei T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_10`)


Laut der vom Bf. vorgelegten Bestätigung über positiv absolvierte Prüfungen vom 29. Juli 2021  sei die letzte Prüfung von T. am 11. Februar 2020 (= Wintersemester 2019/20) abgelegt  worden.

**False Positives:**

- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_11`)


Für den Zeitraum ab März 2020 (= Sommersemester 2020) seien keine weiteren  Unterlagen vorgelegt worden, die eine ernsthafte und zielstrebige Berufsausbildung, die die  volle Zeit von T. in Anspruch genommen hätte, nachgewiesen worden.

**False Positives:**

- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_34`)


Laut der vom Bf. vorgelegten Bestätigung über positiv absolvierte Prüfungen vom 29. Juli 2021  sei die letzte Prüfung von T. am 11. Februar 2020 (= Wintersemester 2019/20) abgelegt  worden.

**False Positives:**

- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/139978.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139978.1_35`)


Für den Zeitraum ab März 2020 (= Sommersemester 2020) seien keine weiteren  Unterlagen vorgelegt worden, die eine ernsthafte und zielstrebige Berufsausbildung, die die  volle Zeit von T. in Anspruch genommen hätten, nachweisen würden.

**False Positives:**

- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_4`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf.) und die Kinder S., geb. am 2010, und T., geb. am 2012, sind  rumänische Staatsbürger.

**False Positives:**

- `der S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_37`)


Wegen der absehbaren kurzzeitigen Unterbrechung des Hauptmieterstatuses des Kindes  ersucht die Familie den Meldezettel von S. zu belassen und den Hauptmietzeitraum zur Kenntnis  zu nehmen…“

**False Positives:**

- `von S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_38`)


Die Beschwerde wurde vom Finanzamt mit Beschwerdevorentscheidung vom 14. Juli 2017 mit  folgender Begründung abgewiesen:  „Sie und Ihre Kinder S. und T. sind rumänische Staatsbürger.

**False Positives:**

- `der S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_42`)


Laut Schreiben des Stadtschulrats vom 10.03.2017 wurde trotz Schulpflicht und  einer Hauptwohnsitzmeldung in Wien ein dauernder Aufenthalt von S. im Ausland festgestellt.  Laut Auskunft der Kindergartendirektorin Fr. P., besuchten Ihre Kinder mit Mai 2016 das letzte  Mal den Kindergarten in Österreich, da Sie angaben, dass beide Kinder sich anschließend in  Rumänien aufhalten werden.

**False Positives:**

- `von S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_44`)


Vorgelegt  wurde ein Schreiben, aus dem hervorgeht, dass sich S. ab dem Schuljahr 2016/17 in Rumänien  im Haushalt der Tante aufhielt. Weiteres wurden eine rumänische Schulbesuchsbestätigung von  S. und eine rumänische Vorschulbesuchsbestätigung von T. für das Schuljahr 2017/18  vorgewiesen.

**False Positives:**

- `von  S.` — no gold match — likely missing annotation
- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_60`)


Da Ihre Kinder S. und T. für den Zeitraum von Juni 2016 bis März 2017 im gemeinsamen  Haushalt mit der Tante in Rumänien lebten und diese für die Pflege und Erziehung der Kinder  aufkam, haben Sie somit im rückgeforderten Zeitraum keinen Anspruch auf Familienbeihilfe.“

**False Positives:**

- `der S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/140556.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140556.1_71`)


Der Sachverhalt ergibt sich aus dem Familienbeihilfenakt, den Angaben der Bf., den von der Bf.  vorgelegten Unterlagen, insbesondere aus dem Schreiben der Kindergartenleitung (Fr . P.) und  dem Schreiben von Ing. X.. vom 24. März 2017 sowie aus der rumänischen  Schulbesuchsbestätigung von S. und der rumänischen Vorschulbesuchsbestätigung von T. für  das Schuljahr 2017/18.

**False Positives:**

- `von S.` — no gold match — likely missing annotation
- `von T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. X..`(person)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_3`)


Begründung  Die im anhängigen Verfahren beschwerdeführende Partei (Bf) ist Masseverwalter (MV) in dem  im Juni 2017 eröffneten Insolvenzverfahren über das Vermögen des I.S. (nachfolgend  Insolvenzschuldner, IS), der im Zentrum eines im Immobilienbereich tätigen Firmenkomplexes  steht (Bauwesen/Bauträger, Immobilienentwicklung, -vermietung und -verkauf).

**False Positives:**

- `des I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/141136.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141136.1_205`)


Das FA formuliert:  „Dazu legt die Abgabenbehörde als Anlage 3 eine Aufstellung der Bankkonten von I.S. als  Beweismittel vor.

**False Positives:**

- `von I.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/141359.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141359.1_27`)


Es handele sich gegenständlich somit  um ein in Bulgarien geführtes Amtshaftungsverfahren seitens der B.  Im Zuge dieses Verfahrens in Bulgarien hätten die Finanzbehörden Bulgariens als beklagte  Partei Unterlagen aus den Steuerakten der beschwerdeführenden Gesellschaft vorgelegt.

**False Positives:**

- `der B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_33`)


Der Bf ist Ehemann von B.M., der bis 2/2018 geschäftsführenden Mehrheitsgesellschafterin der  M-GmbH. Die weiteren Gesellschafter der M-GmbH waren ebenfalls Familienmitglieder.

**False Positives:**

- `von B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/141663.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141663.1_326`)


Aktuell eröffnen sich dem Bf mit dem Nachfolgeprojekt in der K.-Gasse, bei welchem offenbar  zwei neue Häuser entstanden sind, konkrete Möglichkeiten der Einkünfteerzielung, sei es  durch eine Vermietungstätigkeit bis zu einem beabsichtigten Verkauf unter Inanspruchnahme  einer Hauptwohnsitzbefreiung nach § 30 (2) Z 1 EStG 1988 (wie von der Gattin bei  Wohnungsverkäufen in der Vergangenheit) oder durch die zeitnahe Veräußerung neu  geschaffener WE-Einheiten, wie beim verfahrensgegenständlichen Bauprojekt in der R-Gasse.

**False Positives:**

- `der K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/141790.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141790.1_106`)


Indem sowohl im Erkenntnis 0622/71 als auch im Beschwerdefall die Dauer des  Bestandvertrages befristet war und sich in beiden Fällen die Bestandgeberin die Möglichkeit  ausbedungen hatte, im Fall der Beendigung des Bestandsverhältnisses den Bestandgegenstand  nach ihrer Wahl auch im Zustand bei Vertragsabschluss zurückgestellt zu erhalten (vgl die  vertraglichen Formulierungen in 0622/71 einerseits „geräumt von allen Bauten und  Baubestandteilen, uzw in eine[m] solchen Zustand zurückzustellen habe, daß die  Wiederbenützung des A.-Platzes […] so möglich ist, als wäre der gegenständliche Vertrag nie  geschlossen worden“ bzw (Punkt 7. a) des gegenständlichen Mietvertrages andererseits: „[d]as  von der Bestandnehmerin errichtete Objekt […] von der Liegenschaft vollständig zu räumen, in  welchem Falle die Liegenschaft vollständig geräumt von sämtlichen beweglichen und  unbeweglichen Sachen der Bestandnehmerin und eigeebnet im ursprünglichen Zustand vor  Vermietung an die Bestandgeberin zurückzustellen ist“), liegt nach Ansicht des  Bundesfinanzgerichtes in beiden Fällen ein Superädifikat vor und ist somit die bestehende  Judikatur des Verwaltungsgerichtshofes auch auf den Beschwerdefall übertragbar.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/142086.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142086.1_16`)


Die für die Berechnung des Pendlerpauschales und des Pendler€ maßgebliche Entfernung der  Arbeitsstätte des Bf in der X.-Straße von dessen neuem Wohnsitz beträgt, je nachdem ob die  Benützung eines Massenbeförderungsmittels zumutbar ist oder nicht, 27 Kilometer  (FA-Unterlage zu Pendlerrechner v. 10.Aug.2023) bzw. 34 Kilometer (Bf-Ausdruck L34 v.  28.April 2022).

**False Positives:**

- `der X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/142167.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142167.1_147`)


Die Betriebsprüfung führte die Schätzung in der Weise  durch, dass die nicht anerkannten Schein- und Deckungsrechnungen der Firmen S_GmbH,  A_GmbH sowie der W_GmbH und des Z. dem Gewinn zugerechnet wurden.

**False Positives:**

- `des Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/142383.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142383.1_99`)


Damit lag  zumindest die Chance auf Wertsteigerungen bei P.  Wenn P in der mündlichen Verhandlung vorbringt, dass er als Treuhänder im Hinblick auf eine  Wertsteigerung des Anteils zur Auflösung der Treuhandschaft eine Kündigungsfrist einzuhalten  gehabt hätte und die Fiedler+Lehmpuhl Solar GmbH in dieser Zeit das Abtretungsangebot annehmen hätte können,  so verkennt er, dass er gleichzeitig selber Vertragspartei (Treuhänder) und für die andere  Vertragspartei (Treugeber) handeln konnte bzw. deren Entscheidung beeinflussen konnte.

**False Positives:**

- `bei P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Fiedler+Lehmpuhl Solar GmbH`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/145067.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145067.1_9`)


"… Anamnese:  sei mit ca. 20 Jahren an schizophrener Psychose erkrankt, damals an Verfolgungswahn und  akustischen Halluzinationen gelitten, damals erste stationäre psychiatrische Behandlung,  insgesamt bisher vier oder fünf stationäre Behandlungen, zuletzt im Frühling 2022 bei Z.n.  Suizidversuch, ausgelöst durch mehrere Verlusterlebnisse;

**False Positives:**

- `bei Z.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_13`)


Nach Darlegung des  Sachverhalts und auszugsweiser Wiedergabe der im angefochtenen Bescheid angeführten  Begründung wurden in der Beschwerde folgende Beschwerdegründe vorgebracht:   „… Gemäß § 41 Abs. 5 TirKAG sind folgende Ärzte berechtigt, von den von ihnen zu betreuten  Patienten in der Sonderklasse ein mit diesen zu vereinbarendes Honorar zu verlangen  (honorarberechtigte Ärzte):  a) im klinischen Bereich des A. ö.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_15`)


b) in sonstigen Krankenanstalten sowie im nichtklinischen Bereich des A. ö.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_71`)


(5) Folgende Ärzte sind berechtigt, von den von ihnen betreuten Patienten in der Sonderklasse  ein mit diesen zu vereinbarendes Honorar zu verlangen (honorarberechtigte Ärzte):   a) im klinischen Bereich des A. ö.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/145800.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145800.1_73`)


b) in sonstigen Krankenanstalten sowie im nichtklinischen Bereich des A. ö.

**False Positives:**

- `des A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_37`)


So betrugen die  bestätigten Ausbildungsstunden für Frau A. im Jahre 2017 beispielsweise 48 Stunden (IDD- Stunden-Nachweis der V., siehe Anlage).

**False Positives:**

- `der V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_64`)


Der Bf. ist hauptberuflich als selbständiger Versicherungsvertreter tätig und bezieht seine  Einkünfte (Provisionen) von der V.- Aktiengesellschaft (in der Folge auch kurz:Transport Bachtal AG.

**False Positives:**

- `der V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Transport Bachtal AG`(organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_106`)


ab August 2016 war die Bf. „eigener User“ bei der V.  („Einbindung in die V. Welt“ mit eigener Mailadresse und Zugriffberechtigungen.

**False Positives:**

- `der V.` — no gold match — likely missing annotation
- `die V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_108`)


Angeführt in der Stellungnahme wurde weiters, dass die Ehegattin an  internen Schulungen in den Kundencentern der V. durch Mitarbeiter der V. teilgenommen hat  („Hier wurde das GFB erklärt, wichtige Richtlinien der V., div.

**False Positives:**

- `der V.` — no gold match — likely missing annotation
- `der V.` — no gold match — likely missing annotation
- `der V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/145910.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145910.1_114`)


Ergänzend wurde in der Stellungnahme angeführt, 2019 wäre geplant gewesen, die Ehegattin  auf 50 % aufzustocken und über die V. eine Frontoffice Zertifizierung zu machen.

**False Positives:**

- `die V.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/146850.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146850.1_51`)


Dieser  Betrag wurde in der Steuererklärung von G. bei Ermittlung der Einkünfte aus L.u.F. für 2016  angegeben und als durch die Vollpauschalierung abgegolten behandelt.  Die Weitergabe der Nebenentschädigung an die Ehegattin ist nach Ansicht des Finanzamtes als  Einkommensverwendung durch den Verkäufer Raul Yel, Bakk. rer.

**False Positives:**

- `von G.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_TRAIN/146850.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146850.1_97`)


Die rechtsfreundliche Vertretung habe  deshalb eine entsprechende Verteilung der zugeflossenen Entschädigungen vorgenommen und  diese Einnahmen seien auch in der Einkommensteuererklärung der G. offengelegt worden.

**False Positives:**

- `der G.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_7`)


Die  Antragstellerin sei eine solche „Series“ (Teilvermögen) der T..  Ein Delaware Statutory Trust sei gemäß dem DSTA eine eigene juristische Person.

**False Positives:**

- `der T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_12`)


Forderungen, denen Verbindlichkeiten oder Aufwendungen, die in  Bezug auf eine bestimmte “Series” eingegangen worden sind, zugrunde liegen, könnten nur in  die Vermögenswerte dieser “Series” vollstreckt werden, jedoch nicht gegen die Anteilsinhaber  direkt und auch nicht in Vermögenswerte des T. selbst oder einer anderen „Series“.

**False Positives:**

- `des T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_TRAIN/149207.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149207.1_14`)


Jede “Series” des T. werde schlussendlich von einem “Board of Trustees” (Verwaltungsrat)  verwaltet, welches von den Anteilsinhabern gewählt wird.

**False Positives:**

- `des T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_TRAIN/149368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149368.1_147`)


Der Amtspartei wurde die ergänzende Stellungnahme des StV zur Kenntnis gebracht und dazu  folgende Replik abgegeben:  „[Zitat] Organisatorische Struktur   Bei dem Beschwerdeführer, Elvira Konzelmann  handelt es sich um einen im Bundesstaat Kalifornien  ansässigen „Trust“, der von der T., N.A. – als Trustee – verwaltet wird.

**False Positives:**

- `der T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Elvira Konzelmann`(person)

</details>

---

</details>

---

