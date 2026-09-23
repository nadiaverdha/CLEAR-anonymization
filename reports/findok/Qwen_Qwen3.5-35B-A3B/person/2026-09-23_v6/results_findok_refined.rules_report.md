# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-09-23T18:04:19.330920

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-09-23_v6/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 200 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 160 |
| Validation documents | 40 |
| Test documents | 792 |
| Train sentences | 247 |
| Validation sentences | 71 |
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
| Accuracy (exact match) | 98.6% |
| True Positives | 994 |
| False Positives | 511 |
| False Negatives | 1462 |
| Total Gold Entities | 2456 |
| Micro Precision | 66.0% |
| Micro Recall | 40.5% |
| Micro F1 | 50.2% |
| Macro F1 | 50.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `german_legal_person_in_case_context` | 22.7% | 72.3% | 13.5% | 458 | 331 | 127 |
| `german_legal_person_with_titles_and_abbreviations` | 38.0% | 64.6% | 26.9% | 1022 | 660 | 362 |
| `german_legal_person_complex_and_double_titles` | 0.2% | 12.0% | 0.1% | 25 | 3 | 22 |
| `german_legal_person_special_titles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `german_legal_person_in_case_context` 🏆

**F1:** 0.227 | **Precision:** 0.723 | **Recall:** 0.135  

**Format:** `regex`  
**Rule ID:** `f19839ac`  
**Description:**
Captures names appearing immediately after 'in der Beschwerdesache' or 'in der Verwaltungsstrafsache', handling both full names and names with suffixes.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|in\s+der\s+Verwaltungsstrafsache)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+Bakk\.(?:techn|phil|art)|LL\.M\.|M\.B\.L\.|BA)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.723 | 0.135 | 0.227 | 458 | 331 | 127 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 331 | 127 | 2125 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128893.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128893.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Alma Gaedecke, Höbelgasse 24, 9400 St. Thomas, Österreich, über die Beschwerde vom 24. März 2017 gegen den Bescheid des Finanzamtes Wien  1/23 vom 7. März 2017 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alma Gaedecke` | `Alma Gaedecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Höbelgasse 24, 9400 St. Thomas, Österreich` (address)
- `Finanzamtes Wien  1/23` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximilian Joobs` | `Maximilian Joobs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dominik Kuzu` | `Dominik Kuzu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Niels Aleksejew` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rudolf Schlohsmacher` | `Rudolf Schlohsmacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich` (address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Wolf Sackner, Altweitra 15, 6091 Götzens, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  34-684/1904  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wolf Sackner` | `Wolf Sackner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Altweitra 15, 6091 Götzens, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `34-684/1904` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Huberta Nothofer` | `Huberta Nothofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Florenzia Rutt` | `Florenzia Rutt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich` (address)
- `Zollamtes Feldkirch Wolfurt` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Thomas Kreul, Preberstraße 4, 3911 Dietharts, Österreich, vertreten durch DI Heinrich Richter Steuerberatungs GmbH, Liebenauer Hauptstraße  2/D/1, 8041 Graz, über die Beschwerde vom 20. Mai 2015 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 24. Februar 2015, betreffend Forschungsprämie § 108c EStG 1988  für die Wirtschaftsjahre 2011 und 2012 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Kreul` | `Thomas Kreul` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Preberstraße 4, 3911 Dietharts, Österreich` (address)
- `DI Heinrich Richter Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stephan Antonewitz` | `Stephan Antonewitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Viktoria Blaser` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Felizitas Philippov` | `Felizitas Philippov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gerald Hellbing` | `Gerald Hellbing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130274.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gotthard Eppers  vertreten durch  Gf. über die Beschwerde vom 16. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 16. Dezember 2019, Steuernummer 98-639/6692, betreffend Feststellung der  Einkünfte gem. § 188 BAO für das Jahr 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gotthard Eppers` | `Gotthard Eppers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien  4/5/10` (organisation)
- `98-639/6692` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Manuel Rathlev, Hadersfelder Straße 10, 4171 Kasten, Österreich, über die Beschwerde vom 16. September 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 6. September 2019 betreffend Rückforderung für Edwin Meuser  für den  Zeitraum November 2017 bis Juni 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO wie mit Beschwerdevorentscheidung vom 1. April  2020 teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Manuel Rathlev` | `Manuel Rathlev` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hadersfelder Straße 10, 4171 Kasten, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Edwin Meuser` (person)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alexander Powell` | `Alexander Powell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Lubomir Gruebert` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130768.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Anatol Hasenbein, Josef-Kaut-Straße 3, 4048 Großamberg, Österreich, über die Beschwerde vom 26. Mai 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 15. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anatol Hasenbein` | `Anatol Hasenbein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josef-Kaut-Straße 3, 4048 Großamberg, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gudrun Sochurek` | `Gudrun Sochurek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Mag. Rupert Karl` (person)
- `Finanzamtes` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/131051.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Hedwig Scheff, Franz Eckrieder Straße 50, 3142 Grunddorf, Österreich, über die Beschwerde vom 25. September 2020 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 3. September 2020 betreffend Abweisung des Antrages vom 15. Jänner 2020  auf Zuerkennung der Familienbeihilfe ab 1. Oktober 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Scheff` | `Hedwig Scheff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz Eckrieder Straße 50, 3142 Grunddorf, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/131065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131065.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Weiskittel` | `Holger Weiskittel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/131313.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131313.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/131343.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dorothea Sulzbacher, Obergreith 14 - 23, 4924 Breitwies, Österreich, über die Beschwerde vom 21. August 2018 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 2. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dorothea Sulzbacher` | `Dorothea Sulzbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergreith 14 - 23, 4924 Breitwies, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/131601.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Waltraud Herbrecher, Südweg 312, 4062 Niederbuch, Österreich, über die Beschwerde vom 3. Oktober 2018 gegen die Bescheide des Finanzamtes Wien  1/23 vom 30. August 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 und  2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Waltraud Herbrecher` | `Waltraud Herbrecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Südweg 312, 4062 Niederbuch, Österreich` (address)
- `Finanzamtes Wien  1/23` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/131624.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131624.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Fridolin Härlin  in der Beschwerdesache Alva Czymzik,  Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich, über die Beschwerde vom 4. November 2019 gegen den Bescheid des  Finanzamtes Innsbruck vom 21. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alva Czymzik` | `Alva Czymzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Fridolin Härlin` (person)
- `Furxstraße 4, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131687.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Julian Pierchala,  Pracherweg 6, 8635 Gollrad, Österreich, über die Beschwerde vom 6. August 2019 gegen den Bescheid des Finanzamtes  Österreich vom 24. Juli 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018,  Steuernummer 74-273/9351, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julian Pierchala` | `Julian Pierchala` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pracherweg 6, 8635 Gollrad, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `74-273/9351` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131772.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Adrian Hofschmidt, Dechantsbühel 10, 9911 Bannberg, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Adrian Hofschmidt` | `Adrian Hofschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dechantsbühel 10, 9911 Bannberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131805.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Sandro Fischlein, Hans-Schilder-Platz 17, 9065 Untermieger, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sandro Fischlein` | `Sandro Fischlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hans-Schilder-Platz 17, 9065 Untermieger, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/132065.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Torsten Gnapfeus, Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich, gegen die Bescheide des Finanzamtes Wien 4/5/10 vom 21. Februar 2014 betreffend  die auf § 303 Abs. 1 BAO basierende Verfügung der Wiederaufnahme der Verfahren zur  Umsatzsteuer für das Jahr 2010 und zur Einkommensteuer für die Jahre 2010 und 2011 sowie  die auf § 205 Abs. 1 BAO basierende Festsetzung von Anspruchszinsen für die Jahre 2010 bis  2012 beschlossen:  Der Vorlageantrag vom 26.9.2014 wird - betreffend vorgenannter Bescheide - gemäß § 264  Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Torsten Gnapfeus` | `Torsten Gnapfeus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Freudenauer Hafenstraße 109, 9374 Kirchberg, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natalie Emmerling,  Holzäpfeltal 15, 8081 Guggitzgraben, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Natalie Emmerling` | `Natalie Emmerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holzäpfeltal 15, 8081 Guggitzgraben, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Salzburg-Land` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Erhard Wintjens, Völkerweg 97, 8940 Döllach, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 17-868/7871  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erhard Wintjens` | `Erhard Wintjens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Völkerweg 97, 8940 Döllach, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `17-868/7871` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/132412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Merlin Thorschmidt  in der Beschwerdesache Adrian Radakovitsch  in  Liquidation, Schlatterbergweg 97, 9344 Psein, Österreich  über die Beschwerden vom 23.8.2013 gegen die Bescheide des  Finanzamt Steiermark Mitte  vom 22.7.2013 betreffend Wiederaufnahme und neue Sachbescheide Umsatzsteuer  der Jahre 2007 - 2011   1.) zu Recht erkannt:   Der Beschwerde gegen die Wiederaufnahmebescheide gemäß § 303 Abs. 4 BAO hinsichtlich  Umsatzsteuer der Jahre 2007 - 2011 wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Adrian Radakovitsch` | `Adrian Radakovitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Merlin Thorschmidt` (person)
- `Schlatterbergweg 97, 9344 Psein, Österreich` (address)
- `Finanzamt Steiermark Mitte` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/132524.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132524.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/132589.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132589.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Samir Schwahn,  Pichlmoarstraße 73, 3653 Ottenberg, Österreich, über die Beschwerde vom 7. Jänner 2016  gegen den Bescheid des  Finanzamtes Österreich vom 9. Dezember 2015 betreffend Abweisung des Antrags auf  Ausgleichszahlung (Familienbeihilfe 01.2010-12.2015 ) zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 9. Dezember 2015 wird gemäß § 279 Abs. 1 BAO  abgewiesen.

| Predicted | Gold |
|---|---|
| `Samir Schwahn` | `Samir Schwahn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pichlmoarstraße 73, 3653 Ottenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132660.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/132686.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132686.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Bodo Friehmann, Hohenwartweg 2, 4851 Fischham, Österreich, über die Beschwerde vom 30. September 2019 gegen den Einkommensteuerbescheid  2016 und den Einkommensteuerbescheid 2017 des Finanzamtes Wien 1/23 vom 27. August  2019 zu Steuernummer 09 75-279/5529  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bodo Friehmann` | `Bodo Friehmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hohenwartweg 2, 4851 Fischham, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `75-279/5529` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/133011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133011.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/133037.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133037.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/133114.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133114.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/133172.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133172.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/128755.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128755.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Chen Petermüller,  Sand 5, 4851 Hehenberg, Österreich, vertreten durch Anka Vrcic, Kummergasse 7//3/2, 1210 Wien, über die  Beschwerden vom 25. April 2019 gegen die Bescheide des Finanzamtes Salzburg-Land vom  25. März 2019 betreffend Abweisung des Antrages auf Wiederaufnahme des Verfahrens  hinsichtlich Umsatzsteuer 2016 und betreffend Abweisung des Antrages auf Wiederaufnahme  des Verfahrens hinsichtlich Einkommensteuer 2016, Steuernummer 20-238/1198, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Chen` — partial — pred is substring of gold: `Chen Petermüller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chen Petermüller`(person)
- `Sand 5, 4851 Hehenberg, Österreich`(address)
- `Anka Vrcic`(person)
- `Finanzamtes Salzburg-Land`(organisation)
- `20-238/1198`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128762.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Florenzia Claußing,  Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich, über die Beschwerde vom 4. Jänner 2019 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel vom 12. Dezember 2018 betreffend  Grunderwerbsteuer 2018, Erfassungsnummer ErfNr (10-95-558/8694 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Florenzia` — partial — pred is substring of gold: `Florenzia Claußing`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Florenzia Claußing`(person)
- `Walter-Eder-Straße 65, 8091 Oberzirknitz, Österreich`(address)
- `Finanzamtes`(organisation)
- `10-95-558/8694`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128811.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128811.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinNG in der Beschwerdesache Klarissa Kümml,  Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 10. Dezember 2016 gegen die Bescheide des  Finanzamtes XX vom 11. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 und vom 9. November 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Die Beschwerde gegen den Einkommensteuerbescheid 2013 wird gemäß § 279 BAO als  unbegründet abgewiesen.

**False Positives:**

- `Klarissa` — partial — pred is substring of gold: `Klarissa Kümml`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Klarissa Kümml`(person)
- `Hermann-Büchele-Straße 48, 4674 Altenhof am Hausruck, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128831.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Miroslav Hankel, BEd, Noricumgasse 10, 4870 Pfaffing, Österreich, vertreten durch Vertreter,  über die Beschwerde vom 15. März 2012 gegen die  Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 30. Jänner 2012 betreffend  Umsatz- und Einkommensteuer für die Jahre 2009 und 2010 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Miroslav Hankel` — partial — pred is substring of gold: `Miroslav Hankel, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Miroslav Hankel, BEd`(person)
- `Noricumgasse 10, 4870 Pfaffing, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128871.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128871.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Rainer Leutheußer,  Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

**False Positives:**

- `Rainer` — partial — pred is substring of gold: `Rainer Leutheußer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Rainer Leutheußer`(person)
- `Parbasdorferstraße 10n, 8330 Mühldorf bei Feldbach, Österreich`(address)
- `Egger & Freidorfer Steuerberatungs-OG`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Vincent` — partial — pred is substring of gold: `Vincent und Zielinska Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Fabienne Siewek`(person)
- `Vincent und Zielinska Solar GmbH`(organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Mag.a Reneé Kobayashi, Weinbaugebiet Losling 9, 4880 Aich, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

**False Positives:**

- `Mag` — similar text (different position): `Mag. Elisabeth Traxler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Elisabeth Traxler`(person)
- `Mag.a Reneé Kobayashi`(person)
- `Weinbaugebiet Losling 9, 4880 Aich, Österreich`(address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marianne Liuni  in der Beschwerdesache Luigi Wedekämper,  Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Luigi` — partial — pred is substring of gold: `Luigi Wedekämper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Marianne Liuni`(person)
- `Luigi Wedekämper`(person)
- `Josef-Weinheber-Straße 47, 8151 Attendorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Jennifer` — partial — pred is substring of gold: `Jennifer Rösl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Eckard Sellnow`(person)
- `Jennifer Rösl`(person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich`(address)
- `FA Landeck Reutte`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Klarissa Aßmus, Strombad Rustenweg 4, 3452 Trasdorf, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 52-573/0809  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Klarissa` — partial — pred is substring of gold: `Klarissa Aßmus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Michael Mandlmayr`(person)
- `Klarissa Aßmus`(person)
- `Strombad Rustenweg 4, 3452 Trasdorf, Österreich`(address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `52-573/0809`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ronald` — partial — pred is substring of gold: `Ronald Töws`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Ronald Töws`(person)
- `Schießstatt 9, 5124 Weyer, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Valentina Heumeyer  in der Beschwerdesache Emanuela Schöchl,  J. Schemmerl-Gasse 7, 4906 Felling, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

**False Positives:**

- `Emanuela` — partial — pred is substring of gold: `Emanuela Schöchl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Valentina Heumeyer`(person)
- `Emanuela Schöchl`(person)
- `J. Schemmerl-Gasse 7, 4906 Felling, Österreich`(address)
- `Anton Hörmann`(person)
- `Finanzamtes`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valerie` — partial — pred is substring of gold: `Valerie Süssmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Astrid Binder`(person)
- `Valerie Süssmeier`(person)
- `Ögglweg 86, 8623 Tutschach, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Tiffany Kleiß, Endergasse 74, 5411 Vorderwiestal, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 79-412/0834  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Tiffany` — partial — pred is substring of gold: `Tiffany Kleiß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Zwilling`(person)
- `Tiffany Kleiß`(person)
- `Endergasse 74, 5411 Vorderwiestal, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `79-412/0834`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `Wendy` — partial — pred is substring of gold: `Wendy Schärff`

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

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/132328.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132328.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Michael Mühlbeck, Glöckler 35, 5252 Parz, Österreich, betreffend Beschwerde vom 17. Jänner 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 18. Dezember 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 Steuernummer 92-602/5429  beschlossen:   Der Vorlageantrag vom 5.6.2020 wird gemäß § 260 Abs. 1 lit.b BAO in Verbindung mit § 264  Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Michael` — partial — pred is substring of gold: `Michael Mühlbeck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Michael Mühlbeck`(person)
- `Glöckler 35, 5252 Parz, Österreich`(address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `92-602/5429`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/132646.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Urs Zumbroich  in der Beschwerdesache Techn R Huberta Witte,  Ebenweg 188, 4081 Mußbach, Österreich, über die Beschwerde vom 8. Juni 2016 gegen den Bescheid des Finanzamtes  Lilienfeld St. Pölten (jetzt Finanzamt Österreich) vom 13. Mai 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Techn` — partial — pred is substring of gold: `Techn R Huberta Witte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Urs Zumbroich`(person)
- `Techn R Huberta Witte`(person)
- `Ebenweg 188, 4081 Mußbach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Oleg Bösehans  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 80-404/4147, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Oleg` — partial — pred is substring of gold: `Oleg Bösehans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Oleg Bösehans`(person)
- `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `80-404/4147`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Helga Zeißig, Im Markt 12, 5733 Bramberg am Wildkogel, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

**False Positives:**

- `Helga` — partial — pred is substring of gold: `Helga Zeißig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Helga Zeißig`(person)
- `Im Markt 12, 5733 Bramberg am Wildkogel, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/133133.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133133.1_1`)


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

</details>

---

## `german_legal_person_with_titles_and_abbreviations` 🏆

**F1:** 0.380 | **Precision:** 0.646 | **Recall:** 0.269  

**Format:** `regex`  
**Rule ID:** `bcb02ba7`  
**Description:**
Merged: The 'legal_abbreviations' rule (RgR, KommR, HR) is a subset of the broader 'with_titles' rule. Merging them into a single comprehensive pattern for titles and abbreviations improves maintainability and reduces false positives from overlapping matches.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\.in|MMag\.|M\.Mag\.|Univ\.-Prof\.|Univ\.-Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Dipl\.-Ing\.|Dipl\.-Ing\.in|Ing\.|RgR|KommR|HR|Bakk\.|Bakk\.techn\.|Bakk\.phil\.|Bakk\.art\.|LL\.M\.|M\.B\.L\.|BA|B\.A\.)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+(?:LL\.|Bakk\.(?:techn|phil|art)))?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.646 | 0.269 | 0.380 | 1022 | 660 | 362 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 660 | 362 | 1796 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Rachel Darnieder` | `Univ.-Prof.in Rachel Darnieder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Hemma Bährs` (person)
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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximilian Joobs` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Niels Aleksejew  in der Beschwerdesache  Dominik Kuzu Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des Finanzamt Spittal Villach  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Niels Aleksejew` | `Univ.-Prof. Niels Aleksejew` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Kuzu` (person)
- `Finanzamt Spittal Villach` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Schlohsmacher` (person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich` (address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Adalbert Bürks` (person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Fabienne Siewek  in der Beschwerdesache Vincent und Zielinska Solar GmbH  Dorfblickweg 33M, 5224 Holz, Österreich, vertreten durch zobl.bauer.

| Predicted | Gold |
|---|---|
| `Dr.in Fabienne Siewek` | `Dr.in Fabienne Siewek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vincent und Zielinska Solar GmbH` (organisation)
- `Dorfblickweg 33M, 5224 Holz, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Univ.-Prof. Janis Abelen,  Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Janis Abelen` | `Univ.-Prof. Janis Abelen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Plattweg 14, 2054 Alberndorf im Pulkautal, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Hermann Rupert Zittmayr` | `Mag. Hermann Rupert Zittmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Astrid Rüstmann` (person)
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
| `HR Hedwig Barkholt` | `HR Hedwig Barkholt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich` (address)
- `ICON Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)

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

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Klara Willumelies  in der Beschwerdesache Dorfcongart-Event,  Schauensteingasse 48, 8503 Tobisegg, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Dr.in Klara Willumelies` | `Dr.in Klara Willumelies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dorfcongart-Event` (organisation)
- `Schauensteingasse 48, 8503 Tobisegg, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/129688.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129688.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Sellnow  in der Beschwerdesache Jennifer Rösl,  Reslfeldtgasse 32, 9300 Baiersdorf, Österreich, gegen den von der belangten Behörde FA Landeck Reutte  am 22. Jänner 2020  ausgefertigten Bescheid, mit dem der Antrag auf Wiederaufnahme des Verfahrens betreffend  den Einkommensteuerbescheid 2013 abgewiesen wurde, terkannt:   I. Die Bescheidbeschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Sellnow` | `Priv.-Doz. Eckard Sellnow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Rösl` (person)
- `Reslfeldtgasse 32, 9300 Baiersdorf, Österreich` (address)
- `FA Landeck Reutte` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_2`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Antonewitz` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr.in Ljiljana Kos` | `Dr.in Ljiljana Kos` |
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Ljiljana Kos` (person)

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |
| `Dr. Schmid` | `Dr. Schmid` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Ljiljana Kos` (person)
- `Klinik Favoriten` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

| Predicted | Gold |
|---|---|
| `Dr. Sasan Hamzavi` | `Dr. Sasan Hamzavi` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/129969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache HR Juliana Seidl, Am Gelände 10, 3282 Wiesmühl, Österreich, über die Beschwerde der beschwerdeführenden Partei vom 9.10.2020 wegen  behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 2/20/21/22  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `HR Juliana Seidl` | `HR Juliana Seidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Gelände 10, 3282 Wiesmühl, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/129969.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129969.1_2`)


Begründung  HR Juliana Seidl   als Beschwerdeführer (Bf.) hat mit Eingabe vom 9.10.2020, eingelangt am 13.10.2020, gemäß  § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht  betreffend Antrag auf Durchführung der Arbeitnehmerveranlagung für 2019 erhoben.

| Predicted | Gold |
|---|---|
| `HR Juliana Seidl` | `HR Juliana Seidl` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Philippov` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Dr.in Lydia Vogtleitner` (person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Neiser` | `Dr. Stephan Neiser` |
| `Mag. Esra Rohleder` | `Mag. Esra Rohleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

| Predicted | Gold |
|---|---|
| `Mag. Artner` | `Mag. Artner` |

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr. Padesse` | `Dr. Padesse` |
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R HR Martina Pisterer` (person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_2`)


Begründung  Der Beschwerdeführer Priv.-Doz.in Elena Kaminskiy  hat mit Eingabe vom 22.10.2020, eingelangt am 27.10.2020,  gemäß § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der Entscheidungspflicht  über die Beschwerde gegen den Einkommensteuerbescheid für 2019 erhoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Elena Kaminskiy` | `Priv.-Doz.in Elena Kaminskiy` |

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/130631.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130631.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nicola Folprecht  in der Verwaltungsstrafsache gegen  Florian Abbruzzese, BA, Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich, über die Beschwerde vom 1. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien vom 9. März 2020, zugestellt am 23. März 2020, Geschäftszahl  MA67/196701252879/2019, zu Recht erkannt:    I. Das Straferkenntnis vom 9. März 2020 wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Nicola Folprecht` | `Univ.-Prof.in Nicola Folprecht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florian Abbruzzese, BA` (person)
- `Sankt Veit in der Gegend 15, 3130 St. Andrä an der Traisen, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lubomir Gruebert  in der Beschwerdesache Alexander Powell,  Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lubomir Gruebert` | `Priv.-Doz. Lubomir Gruebert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexander Powell` (person)
- `Kleinebersdorferstraße 6, 3592 Greillenstein, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/130754.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130754.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Lex` (person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Irene Kohler` | `Mag. Irene Kohler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Erwin Göktan` (person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ronald Töws` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Rupert Karl` | `Mag. Rupert Karl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gudrun Sochurek` (person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130927.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/130963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130963.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Cäcilia Wlcek` (person)
- `Rambergweg 3, 4950 Weidenthal, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

| Predicted | Gold |
|---|---|
| `Dr. Karl Renner` | `Dr. Karl Renner` |

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valerie Süssmeier` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jeffrey Wengschick` | `Dr. Jeffrey Wengschick` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donald Hayder, MA` (person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/131109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131109.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Valentin Kreuthmayr  in der Beschwerdesache Naomi Ruddis, LLB,  Schuselkagasse 21, 9570 Alt-Ossiach, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 10. März 2020 betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für sich selbst ab Jänner 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Valentin Kreuthmayr` | `Mag. Valentin Kreuthmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Naomi Ruddis, LLB` (person)
- `Schuselkagasse 21, 9570 Alt-Ossiach, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holger Weiskittel` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Dr.in Hemma Bährs  in der Beschwerdesache Univ.-Prof.in Rachel Darnieder, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Dr.in Hemma` — partial — pred is substring of gold: `Dr.in Hemma Bährs`

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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Ing. Dipl.-Ing. Brunhild Fleischfresser, Margaretengürtel 23, 4092 Pyrawang, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Ing. Dipl` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`
- `Ing. Brunhild Fleischfresser` — partial — pred is substring of gold: `Ing. Dipl.-Ing. Brunhild Fleischfresser`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Ing. ÖkR Horst Stevens, Glinzen 13, 4661 Kirnbach, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 24. August 2017,  gegen die Bescheide des Finanzamtes Linz vom 31. Mai 2017, 9. Juni 2017, 13. Juni 2017,  19. Juni 2017 und 22. Juni 2017 betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO  hinsichtlich Körperschaftsteuer 2011 bis 2015

**False Positives:**

- `Mag. Manfred Fr` — partial — pred is substring of gold: `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Ing. ÖkR Horst Stevens`(person)
- `Glinzen 13, 4661 Kirnbach, Österreich`(address)
- `Mag. Manfred Frühwirth, Wirtschaftstreuhand-  und SteuerberatungsgmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129265.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hon.-Prof. Gerhard Hübinger, Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich, St.Nr. xxxxxxxxxxxx, über die Beschwerden vom 2. April 2013 gegen den  Aufhebungsbescheid gemäß § 299 BAO vom 4. März 2013 und den Zurückweisungsbescheid  vom 4. März 2013 (betreffend Antrag auf Bescheidaufhebung gemäß § 295 Abs. 4 BAO, in  eventu Antrag auf Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 lit. b BAO) des  Finanzamtes Wien 9/18/19 Klosterneuburg, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon.-Prof. Gerhard` — partial — pred is substring of gold: `Hon.-Prof. Gerhard Hübinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Gerhard Hübinger`(person)
- `Gewerbezone, Josef-Stefan-Straße 47, 8184 Baierdorf-Umgebung, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Astrid Rüstmann  in der Beschwerdesache des  Sandro Flunger, Rohrer Straße 29, 3231 Kainratsdorf, Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des FA Klagenfurt St. Veit Wolfsberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Dr.in Astrid` — partial — pred is substring of gold: `Dr.in Astrid Rüstmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Astrid Rüstmann`(person)
- `Sandro Flunger`(person)
- `Rohrer Straße 29, 3231 Kainratsdorf, Österreich`(address)
- `Mag. Hermann Rupert Zittmayr`(person)
- `FA Klagenfurt St. Veit Wolfsberg`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129392.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129392.1_2`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  HR Hedwig Barkholt, Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

**False Positives:**

- `Dr. Andreas Wei` — partial — pred is substring of gold: `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `HR Hedwig Barkholt`(person)
- `Dr. Andreas Weißenbäck-Gasse 903, 4755 Gmeinedt, Österreich`(address)
- `ICON Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der BergLuftfahrt, KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `BergLuftfahrt`(organisation)
- `KLG ÖBB Wien-West 2050 (Lidlgasse) 3, 3593 Kleinraabs, Österreich`(address)
- `Westra  GmbH Steuerberatungsgesellschaft`(organisation)
- `BMF`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_3`)


Entscheidungsgründe  Mit Bescheiden des Finanzamtes Wien 1/23 jeweils vom 9. August 2019 wurden über die  KommR Eckard Gaiss, Bakk. phil. (in weiterer Folge: Bf.) erste Säumniszuschläge für Umsatzsteuer 05/2019 in Höhe  von € 209.028,38 (Säumniszuschlag € 4.180,57), für Werbeabgabe 05/2019 in Höhe von €  177.156,96 (Säumniszuschlag € 3.543,14), für Lohnsteuer 06/2019 in Höhe von € 85.47466  (Säumniszuschlag € 1.709,49) und für Dienstgeberbeitrag 06/2019 in Höhe von € 20.536,18  (Säumniszuschlag € 410,72), Säumniszuschläge gesamt € 9.843,92, festgesetzt, da die  angeführten Abgabenschuldigkeiten nicht innerhalb der Frist 15. Juli 2019 entrichtet worden  sind.

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Wien 1/23`(organisation)
- `KommR Eckard Gaiss, Bakk. phil.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_15`)


Am 15. Juli 2019 hat unsere Mandantschaft via Finanz Online einen Antrag auf Übertragung an  die KommR Eckard Gaiss, Bakk. phil. (St.Nr. 09-07-088/5911) iHv EUR 490.885,84 und an die Martinssen Versicherung GmbH (St.Nr. 10)  iHv EUR 336.224,91 eingebracht (Hinweis: Betreffend die Martinssen Versicherung GmbH wurde ebenfalls ein  Säumniszuschlag festgesetzt und ist eine Beschwerdevorentscheidung ergangen;

**False Positives:**

- `KommR Eckard Gaiss` — partial — pred is substring of gold: `KommR Eckard Gaiss, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Eckard Gaiss, Bakk. phil.`(person)
- `09-07-088/5911`(tax_number)
- `Martinssen Versicherung GmbH`(organisation)
- `Martinssen Versicherung GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_31`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129503.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129503.1_73`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `Dr.in Monika` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Monika Wörther-Madl`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dr.in Monika` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_26`)


Sie könne nicht  aufstehen, bewegt aber seitengleich (diesbezüglich liegen keine Befunde vor)   Derzeitige Beschwerden:   diverse Schmerzen, sie könne nicht gehen   Behandlung(en) / Medikamente / Hilfsmittel:   kann keine Angaben machen   Sozialanamnese:   lebt in Caritasheim vollbetreut, I(nvaliditäts)Pension, Pflegestufe 4, Erwachsenenvertretung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   28.4.87 Dipl.-Ing. Kirsten Hüffner: Es handelt sich bei (der Bf.) um eine Oligophrenie.

**False Positives:**

- `Dipl.-Ing. Kirsten` — partial — pred is substring of gold: `Dipl.-Ing. Kirsten Hüffner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_77`)


Wie aus dem Gutachten Prof. Univ.Doz. Dr.med Dipl.-Ing. Kirsten Hüffner  vom 28.04.1987, Seite 6, ersichtlich,  sind schizophreniforme Psychosen bei Oligophrenie sehr schwer und oft gar nicht deutbar.

**False Positives:**

- `Dipl.-Ing. Kirsten` — partial — pred is substring of gold: `Dipl.-Ing. Kirsten Hüffner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirsten Hüffner`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `HR Dr` — positional overlap with gold: `Dr. Amtsvertr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Claudia Noeltge`(person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich`(address)
- `Finanzamtes Spittal Villach`(organisation)
- `Dr. Amtsvertr`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Mag. Artner` — partial — pred is substring of gold: `Mag. Artner-Tauscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Artner-Tauscher`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Björn Hüpscher  in der Beschwerdesache Igor Strunz,  Litschauer Straße 12, 3001 Mauerbach, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr. Bj` — partial — pred is substring of gold: `Dr. Björn Hüpscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Björn Hüpscher`(person)
- `Igor Strunz`(person)
- `Litschauer Straße 12, 3001 Mauerbach, Österreich`(address)
- `Vedat Gökdemir`(person)
- `Finanzamtes`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `HR Martina Pisterer` — partial — pred is substring of gold: `Techn R HR Martina Pisterer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Techn R HR Martina Pisterer`(person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/130723.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jeannine Hüpgen   in der Beschwerdesache des Alois Jeckl, Amlach 6, 2620 Straßhof, Österreich,   betreffend die Bescheide des Finanzamt Waldviertel  vom 11. Juli 2018   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2015, 2016 und 2017,  Steuernummer 66-092/6335,   zu Recht erkannt:  Den Beschwerden wird im Umfang der Beschwerdevorentscheidungen teilweise Folge  gegeben.

**False Positives:**

- `Priv.-Doz.in Jeannine` — partial — pred is substring of gold: `Priv.-Doz.in Jeannine Hüpgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Jeannine Hüpgen`(person)
- `Alois Jeckl`(person)
- `Amlach 6, 2620 Straßhof, Österreich`(address)
- `Finanzamt Waldviertel`(organisation)
- `66-092/6335`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache RgR Frederike Wegerth, KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt am Wörthersee, über  die Beschwerde vom 05.02.2016 gegen die Bescheide des Finanzamtes Spittal Villach vom  25.01.2016 die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2012 sowie  die Einkommensteuer 2012 und 2013 betreffend in der mündlichen Verhandlung vom  03.06.2020 beschlossen:  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `RgR Frederike Wegerth`(person)
- `KLG Gartenfreunde 43, 3340 Zell-Markt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Spittal Villach`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Dipl.-Ing. Erwin` — partial — pred is substring of gold: `Dipl.-Ing. Erwin Göktan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Irene Kohler`(person)
- `Dipl.-Ing. Erwin Göktan`(person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  HR Frederik Kleinmichel, MA, Haniflgasse 12, 4725 Stadl, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `HR Frederik Kleinmichel` — partial — pred is substring of gold: `HR Frederik Kleinmichel, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `HR Frederik Kleinmichel, MA`(person)
- `Haniflgasse 12, 4725 Stadl, Österreich`(address)
- `Astoria Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) veräußerte mit Kaufvertrag vom 06.07.2016 seinen Hälfteanteil am  Grundstück Nr. x/17 in C., Katastralgemeinde a, an seine Geschwister Edeltraud Gonszerowski und Univ.-Prof.in Techn R Nicoletta Constin um  einen Kaufpreis in Höhe von 140.100,00 Euro.

**False Positives:**

- `Univ.-Prof.in Techn` — partial — pred is substring of gold: `Univ.-Prof.in Techn R Nicoletta Constin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edeltraud Gonszerowski`(person)
- `Univ.-Prof.in Techn R Nicoletta Constin`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_44`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Für die Beurteilung der in Streit stehenden Frage geht das Bundesfinanzgericht von folgendem  entscheidungsrelevantem Sachverhalt aus:  Der Bf. veräußerte mit Kaufvertrag vom 06.07.2016 seinen Hälfteanteil am Grundstück Nr. x/17  in C., Katastralgemeinde a, an seine Geschwister Edeltraud Gonszerowski und Univ.-Prof.in Techn R Nicoletta Constin um einen Kaufpreis in Höhe  von 140.100,00 Euro.

**False Positives:**

- `Univ.-Prof.in Techn` — partial — pred is substring of gold: `Univ.-Prof.in Techn R Nicoletta Constin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Edeltraud Gonszerowski`(person)
- `Univ.-Prof.in Techn R Nicoletta Constin`(person)

</details>

---

## `german_legal_person_complex_and_double_titles` 💣

**F1:** 0.002 | **Precision:** 0.120 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `350d5e97`  
**Description:**
Merged: Both rules target German academic titles (Professors, Doctors, Magisters) with similar name patterns. Merging reduces redundancy while maintaining coverage for complex and double titles.

**Content:**
```
\b(?:Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Prof\.|Mag\.\s+Dr\.|Dr\.\s+Mag\.)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\-[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.120 | 0.001 | 0.002 | 25 | 3 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 22 | 2453 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/141415.1`) (sent_id: `deanon_BFG_20260814_TRAIN/141415.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Mag. Dr. Guntram Leitenmaier, Lutta 4, 6912 Hörbranz, Österreich, vertreten durch Dr. Christian Burghardt, Am Hof 13/1/18, 1010 Wien, über die  Beschwerde vom 11. April 2022 gegen die Bescheide des Finanzamtes Österreich vom 6. April  2022 betreffend   Abweisung des Antrages vom 9. August 2021 auf Familienbeihilfe ab April 2021 und   Abweisung des Antrages vom 11. August 2021 auf den Erhöhungsbetrag ab April 2021,   Steuernummer 80-622/0885 (SVNR 2814 050576), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Guntram Leitenmaier` | `Mag. Dr. Guntram Leitenmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lutta 4, 6912 Hörbranz, Österreich` (address)
- `Dr. Christian Burghardt` (person)
- `Finanzamtes Österreich` (organisation)
- `80-622/0885` (tax_number)
- `2814 050576` (social_security_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  der Prof. Clemens Podzum, Grunholz 39, 4070 Unterrudling, Österreich, vertreten durch VertretungsNetz - Erwachsenenvertretung,  Forsthausgasse 16-20, 1200 Wien, vom 5. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 11. März 2022 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab Dezember 2021 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Prof. Clemens Podzum` | `Prof. Clemens Podzum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Grunholz 39, 4070 Unterrudling, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_40`)


Frau Prof. Clemens Podzum  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Dies besteht seit: 01/2004  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Die Fähigkeit sich selbst den Unterhält zu verschaffen ist nicht gegeben, da kognitive Beein- trächtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Prof. Clemens Podzum` | `Prof. Clemens Podzum` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_17`)


Darüber hinaus werden die dem Erwachsenenvertreter vorliegenden psychiatrischen  Gutachten vorgelegt, aus diesen ist ersichtlich, dass bei (der Bf.) eine angeborene Oligophrenie  vorliegt (Psychiatrisches Gutachten Univ.Prof. Dr.med. F. St. vom 28.04.1987), ebenso wie die  Sachverständige Charles Hegler von einer angeborenen Minderbegabung ausgeht, mit später  aufgetretenen psychotischen und schizophrenen Symptomen.

**False Positives:**

- `Univ.Prof. Dr` — partial — pred is substring of gold: `Univ.Prof. Dr.med. F. St.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.Prof. Dr.med. F. St.`(person)
- `Charles Hegler`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_19`)


Beweis: beiliegendes Gutachten Univ.Prof. Dr.med.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_20`)


F. St. vom 28.04.1987,                  beiliegendes Gutachten Univ.Prof. Dr.med.

**False Positives:**

- `Univ.Prof. Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_73`)


Wie aus dem vorgelegten Gutachten von Prof. Dr.med.

**False Positives:**

- `Prof. Dr` — no gold match — likely missing annotation

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

- `Univ.Prof. Dr` — partial — pred is substring of gold: `Univ.Prof. Dr.med. F. St.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.Prof. Dr.med. F. St.`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Dragan` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Prof. Helmut` — partial — pred is substring of gold: `Prof. Helmut Fürnkäß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman`(person)
- `Prof. Helmut Fürnkäß`(person)
- `Dr Christian Leskoschek`(person)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_13`)


Mag. Dr. Wieland Reinecke (Beschwerdeführer, kurz: Bf.) wurde von Kontrollorganen der  Parkraumüberwachung der Landespolizeidirektion Wien in der gebührenpflichtigen  Kurzparkzone in 1030 Wien, Marokannergasse 18,   1. am 1. Dezember P20 um 15:45 Uhr (Z1 und  2. am 3. Dezember 2020 um 15:11 Uhr (Z2  3. am 7. Dezember 2020 um 12:32 Uhr (Z3),  4. am 9. Dezember 2020 um 20:04 Uhr (Z4)  beanstandet, da es ohne einen für den jeweiligen Beanstandungszeitpunkt gültigen Parkschein  abgestellt war.

**False Positives:**

- `Mag. Dr. Wieland Reinecke` — partial — gold is substring of pred: `Wieland Reinecke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wieland Reinecke`(person)
- `Landespolizeidirektion Wien`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/140098.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140098.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Andrea Drom  in der Beschwerdesache Corbinian Neumetzler,  Am Haidbach 19, 9620 Obervellach, Österreich, über die Beschwerde vom 6.Mai 2022 gegen den Bescheid des FA Graz-Stadt  vom  12. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021, Steuernummer  85-520/0851, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Prof. Andrea Drom` — partial — pred is substring of gold: `Hon.-Prof. Univ.-Prof. Andrea Drom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Univ.-Prof. Andrea Drom`(person)
- `Corbinian Neumetzler`(person)
- `Am Haidbach 19, 9620 Obervellach, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `85-520/0851`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_23`)


Darin liegt der „negative Leistungsanreiz“, den Frau Prof. Kanduth-Kristen im  der ersten Beschwerde beigelegten Artikel meines Erachtens zurecht als verfassungsrechtlich  bedenklich kritisiert.

**False Positives:**

- `Prof. Kanduth-Kristen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/140533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/140533.1_33`)


Ich hoffe,  meine weiteren Ausführungen veranlassen — zusammen mit dem bereits erwähnten Artikel  von Frau Prof. Kanduth-Kristen — das Gericht dazu, meine Zweifel an der  Verfassungsmäßigkeit der gegenständlichen Regelung zu teilen und wie angeregt deren  Aufhebung beim Verfassungsgerichtshof zu beantragen.

**False Positives:**

- `Prof. Kanduth-Kristen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/142010.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142010.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Alexander Thevessen  in der Revisionssache Guntram Oberschmid,  Stauding 26, 5771 Schwarzleo, Österreich, vertreten durch Mag. Dr. Gerald Pichler LL.M. MBA, Rechtsanwalt,  Kremstalstraße 4, 4501 Neuhofen/Krems, über den in der außerordentlichen Revision vom  25.8.2023 gegen das Erkenntnis des Bundesfinanzgerichtes vom 15.11.2022,  RV/7103505/2017, betreffend Haftung für Lohnsteuer 2008, 2009 und 2010 sowie  Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2008, 2009 und 2010, enthaltenen  Antrag, der Revision die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Mag. Dr. Gerald Pichler` — partial — pred is substring of gold: `Mag. Dr. Gerald Pichler LL.M. MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alexander Thevessen`(person)
- `Guntram Oberschmid`(person)
- `Stauding 26, 5771 Schwarzleo, Österreich`(address)
- `Mag. Dr. Gerald Pichler LL.M. MBA`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/145828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Janosch Krutki  in der Beschwerdesache Priv.-Doz. Hon.-Prof. Emmerich Vormfenne,  KLG Halterbachtal 3, 9371 Tschutta, Österreich, vertreten durch Mag. Walther Wawronek Steuerberatungsgesellschaft mbH,  Linke Wienzeile 4, 1060 Wien, über die Beschwerde vom 28. Februar 2017 gegen den Bescheid  des Finanzamtes Österreich vom 1. Februar 2017 betreffend Aufhebung § 299 BAO /  USt 2014  und Umsatzsteuer 2015 Steuernummer 92-348/0781  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Emmerich Vormfenne` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Janosch Krutki`(person)
- `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`(person)
- `KLG Halterbachtal 3, 9371 Tschutta, Österreich`(address)
- `Mag. Walther Wawronek Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `92-348/0781`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/145828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145828.1_27`)


In der Beschwerde hinsichtlich Umsatzsteuer 2015 wird eingewendet, dass Herr Priv.-Doz. Hon.-Prof. Emmerich Vormfenne  für  eine Vielzahl von Personen als gerichtlich beauftragter Sachwalter tätig ist.

**False Positives:**

- `Prof. Emmerich Vormfenne` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/145828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145828.1_29`)


Lediglich für Leistungen, die Herr Priv.-Doz. Hon.-Prof. Emmerich Vormfenne  in seiner  Eigenschaft als Anwalt für den Besachwalteten erbringt, steht ihm ein „angemessenes Entgelt“  zu (§ 276 Abs. 2 ABGB).

**False Positives:**

- `Prof. Emmerich Vormfenne` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/145828.1`) (sent_id: `deanon_BFG_20260814_TRAIN/145828.1_40`)


Herr Priv.-Doz. Hon.-Prof. Emmerich Vormfenne  hat im  Jahr 2015 im Rahmen seiner Sachwaltertätigkeit Entschädigungen von insgesamt 317.114,84  erhalten (Anlage 5), für die unrichtigerweise und entgegen Art. 132 Abs.1 lit. g der EU- Umsatzsteuer-Richtlinie Umsatzsteuer in Höhe von 63.422,96 1t.

**False Positives:**

- `Prof. Emmerich Vormfenne` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Hon.-Prof. Emmerich Vormfenne`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_74`)


Vorgutachten im Verfahren Zahl für die Erwachsenenvertretung von Prof. Otto L.:  Es handelt sich bei der Untersuchten nach Unterlagen und Befund um eine primäre Leistungs- reduktion, die vor allem in Teilbereichen, Realitätsanpassung, Kritikfähigkeit, Zahlenverständ- nis, komplexere Rechnungen die Wertigkeit einer geistigen Behinderung erreicht.

**False Positives:**

- `Prof. Otto` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/146142.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146142.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hon.-Prof. Janosch Weinberger  in der Beschwerdesache Igor Golobic,  Fernitz 24, 8832 Krumegg, Österreich, vertreten durch Peter Weinmar, Lerchengasse 18, 1080 Wien, über die  Beschwerde vom 14.November 2023 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom 24. Oktober 2023  betreffend Zahlungserleichterungen § 212 BAO 24.10.2023 zur Steuernummer  58-685/2299  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Janosch Weinberger` — partial — pred is substring of gold: `Hon.-Prof. Hon.-Prof. Janosch Weinberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Hon.-Prof. Janosch Weinberger`(person)
- `Igor Golobic`(person)
- `Fernitz 24, 8832 Krumegg, Österreich`(address)
- `Peter Weinmar`(person)
- `Finanzamt Schwechat Gerasdorf`(organisation)
- `58-685/2299`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/146425.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146425.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Priv.-Doz.in Wilhelmine Steinheit, Prof. Rheden-Straße 16E, 2572 Obertriesting, Österreich, über die Beschwerde vom 26. April 2024 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2024 betreffend Rückforderung Familienbeihilfe  01.2023-12.2023 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Rheden-Stra` — partial — pred is substring of gold: `Prof. Rheden-Straße 16E, 2572 Obertriesting, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Priv.-Doz.in Wilhelmine Steinheit`(person)
- `Prof. Rheden-Straße 16E, 2572 Obertriesting, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/148568.1`) (sent_id: `deanon_BFG_20260814_TRAIN/148568.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Frank Wunderle  in der Beschwerdesache Doris Jasaitis,  Auf der Huben 29, 6460 Imst, Österreich, betreffend Beschwerde vom 3. März 2025 gegen den Bescheid des  Finanzamtes Österreich vom 25. Februar 2025 betreffend Einkommensteuer 2022,  Steuernummer 95-477/9911, beschlossen:   I. Der Vorlageantrag vom 15. Mai 2025 wird gemäß § 256 Abs 3 BAO in Verbindung mit  § 264 Abs 4 BAO als gegenstandslos erklärt.

**False Positives:**

- `Prof. Frank Wunderle` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Frank Wunderle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Frank Wunderle`(person)
- `Doris Jasaitis`(person)
- `Auf der Huben 29, 6460 Imst, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `95-477/9911`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/149316.1`) (sent_id: `deanon_BFG_20260814_TRAIN/149316.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Yussuf Muehlenbrock  in der Beschwerdesache Mag. Karim Bendlage,  Mühlgrundweg 28, 2544 Enzesfeld-Lindabrunn, Österreich, über die Beschwerde vom 22. Dezember 2017 gegen die Bescheide des  Finanzamt Salzburg-Stadt  vom 5. Dezember 2017 betreffend Festsetzung der   Normverbrauchsabgabe für April 2014 (4.338,82 €) und Kraftfahrzeugsteuer für die  Zeiträume 4 - 12/2014 (608,26 €) und 1 - 9/2015 (684,29 €) sowie    Normverbrauchsabgabe für September 2015 (11.193,28 €) und Kraftfahrzeugsteuer für  die Zeiträume 10 - 12/2015 (574,60 €), 1 - 12/2016 (2.298,38) und 1 - 9/2017 (1.723,79  €)   Normverbrauchsabgabe für Oktober 2017 (20.414,12 €) und Kraftfahrzeugsteuer für die  Zeiträume 10 - 12/2017 (240 €), 1 - 12/2018 (960 €) und 1 - 8/2019 (640 €),  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Priv.-Doz. Yussuf Muehlenbrock` — partial — pred is substring of gold: `Mag. Priv.-Doz. Yussuf Muehlenbrock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Yussuf Muehlenbrock`(person)
- `Mag. Karim Bendlage`(person)
- `Mühlgrundweg 28, 2544 Enzesfeld-Lindabrunn, Österreich`(address)
- `Finanzamt Salzburg-Stadt`(organisation)

</details>

---

## `german_legal_person_special_titles` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45077246`  
**Description:**
Matches special legal titles (Senatspräsident, Hofrat, etc.) followed by academic titles and names, capturing the FULL title and name sequence.

**Content:**
```
\b(?:Hofrat|Hofr\u00e4tin|Senatspr\u00e4sident|Senatspr\u00e4sidentin|Vizepr\u00e4sident|Vizepr\u00e4sidentin|Pr\u00e4sident|Pr\u00e4sidentin|\u00d6kR|OMedR|Landeshauptmann|Landeshauptmannin)\s+(?:Hon\.-?Prof\.|PD\s+Dr\.|Dr\.|Mag\.|MMag\.)?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\-[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 2456 |

</details>

---

</details>

---

