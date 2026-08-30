# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-30T11:28:28.525842

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/transfer/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 400 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 320 |
| Validation documents | 80 |
| Test documents | 792 |
| Train sentences | 587 |
| Validation sentences | 185 |
| Test sentences | 88613 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 20 |
| Refinement iterations | 1 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | True |
| Critic Interval | 2 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 20 |
| Refine per batch | 4 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.1% |
| True Positives | 469 |
| False Positives | 386 |
| False Negatives | 1986 |
| Total Gold Entities | 2455 |
| Micro Precision | 54.9% |
| Micro Recall | 19.1% |
| Micro F1 | 28.3% |
| Macro F1 | 28.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `german_legal_person_with_titles` | 28.3% | 71.0% | 17.6% | 610 | 433 | 177 |
| `german_legal_person_double_titles` | 0.1% | 33.3% | 0.0% | 3 | 1 | 2 |
| `german_legal_person_complex_titles` | 0.1% | 25.0% | 0.0% | 4 | 1 | 3 |
| `german_legal_person_without_titles` | 2.5% | 14.6% | 1.4% | 233 | 34 | 199 |
| `german_legal_person_special_titles` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `german_legal_person_standalone` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `german_legal_person_with_titles` 🏆

**F1:** 0.283 | **Precision:** 0.710 | **Recall:** 0.176  

**Format:** `regex`  
**Rule ID:** `6de20d83`  
**Description:**
Matches standard titles (Dr., Mag., MMag., M.Mag.) followed by names, capturing the full title and name, including hyphenated surnames.

**Content:**
```
\b(?:Dr\.|Mag\.|M\.Mag\.|MMag\.)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\-[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.710 | 0.176 | 0.283 | 610 | 433 | 177 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 433 | 177 | 2020 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_0`)


GZ. RV/7100281/2020 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter MMag. Gerald Erwin Ehgartner in der Beschwerdesache Zeno Matyssek, vertreten durch Jank Weiler Operenyi Rechtsanwälte GmbH, Schottengasse 1, 1010 Wien, über die Beschwerde vom 18.11.2019 gegen den Bescheid der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel vom 10.10.2019, ERFNR 123/2019, betreffend Gebühren zu Recht:  I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MMag. Gerald Erwin Ehgartner` | `MMag. Gerald Erwin Ehgartner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zeno Matyssek` (person)
- `Jank Weiler Operenyi Rechtsanwälte GmbH` (organisation)
- `Finanzamt für Gebühren` (organisation)

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

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128943.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128943.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129068.1_2`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Maximilian Joobs, Forsthausweg 11, 3580 Poigen, Österreich, über die Beschwerde vom 16. September 2019 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 23. August 2019  betreffend Rückforderung der für die Kinder NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 für den Zeitraum von Juli 2019 bis August 2019 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximilian Joobs` (person)
- `Forsthausweg 11, 3580 Poigen, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129077.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129137.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Rudolf Schlohsmacher, Linzerstraße 4, 4209 Oberkulm, Österreich, über die Beschwerde vom 21. Jänner 2020 gegen den Bescheid der  Magistratsabteilung 6, Rechnungs- und Abgabenwesen, Dezernat Rechnungswesen- Buchhaltungsabteilung 34, vom 9. Jänner 2020 betreffend Festsetzung der Abgabe nach dem  Wiener Abfallwirtschaftsgesetz ab 01.01.2020 für die Liegenschaft  Schloß-Siedlung 52, 4070 Grüben, Österreich, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Schlohsmacher` (person)
- `Linzerstraße 4, 4209 Oberkulm, Österreich` (address)
- `Schloß-Siedlung 52, 4070 Grüben, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  KzlR Adalbert Bürks, Schörbergerstraße 99, 9560 Maltschach, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Adalbert Bürks` (person)
- `Schörbergerstraße 99, 9560 Maltschach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129231.1_2`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129233.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129379.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129460.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Huberta Nothofer, Hartfeldweg 45, 9374 Unterwietingberg, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Huberta Nothofer` (person)
- `Hartfeldweg 45, 9374 Unterwietingberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/129555.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129555.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Florenzia Rutt, Rohrmayrstraße 24, 9961 Lerch, Österreich, betreffend Beschwerde vom 2. Juli 2020 gegen  den Bescheid des Zollamtes Feldkirch Wolfurt vom 12. Mai 2017, GZ 920000/xxxx/35/2015  betreffend Einfuhrabgaben (Zoll, Einfuhrumsatzsteuer und Verzugszinsen) beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm lit b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florenzia Rutt` (person)
- `Rohrmayrstraße 24, 9961 Lerch, Österreich` (address)
- `Zollamtes Feldkirch Wolfurt` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Stephan Antonewitz, Grabäckergasse 7, 4641 Oberhart, Österreich, über die Beschwerde vom 30. August 2018 gegen den Bescheid des  Finanzamtes Baden Mödling vom 7. September 2018 betreffend Abweisung des Antrages vom  30.08.2018 auf erhöhte Familienbeihilfe ab September 2018 zu Recht erkannt:   Der Beschwerde gegen den Bescheid, soweit dieser über den Zeitraum September 2018  abspricht, wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Antonewitz` (person)
- `Grabäckergasse 7, 4641 Oberhart, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Dr.in Ljiljana Kos` (person)
- `Ljiljana Kos` (person)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Nahler` | `Dr. Alexander Nahler` |
| `Dr. Schmid` | `Dr. Schmid` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Ljiljana Kos` (person)
- `Klinik Favoriten` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129949.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Felizitas Philippov, Hauser 155, 9422 Aich, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Philippov` (person)
- `Hauser 155, 9422 Aich, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  StR Dr.in Lydia Vogtleitner, Dorf Haus 27V, 9556 Sörgerberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Dr.in Lydia Vogtleitner` (person)
- `Dorf Haus 27V, 9556 Sörgerberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Gerald Hellbing, Unterretzbach 125, 5092 Kirchental, Österreich, vertreten durch Dr. Thomas Hofer-Zeni, Landstraßer Hauptstraße 82/11, 1030 Wien,  über die Beschwerde vom 7. Mai 2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22  vom 8. April 2019 betreffend Abweisung des Eigenantrages vom 12. Dezember 2018 auf  Familienbeihilfe und erhöhte Familienbeihilfe ab Dezember 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Thomas Hofer-Zeni` | `Dr. Thomas Hofer-Zeni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerald Hellbing` (person)
- `Unterretzbach 125, 5092 Kirchental, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/130412.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130412.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Dr. Stephan Neiser, Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich, über die Beschwerde vom 10. Dezember 2019 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 25. November 2019 betreffend Rückforderung für Mag. Esra Rohleder  für den  Zeitraum Dezember 2018 bis September 2019 zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Neiser` | `Dr. Stephan Neiser` |
| `Mag. Esra Rohleder` | `Mag. Esra Rohleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johann Seifriedsberger-Straße 21, 9470 Kampach, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Claudia Noeltge, Lachmayrring 6, 2485 Wampersdorf, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Amtsvertr` | `Dr. Amtsvertr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claudia Noeltge` (person)
- `Lachmayrring 6, 2485 Wampersdorf, Österreich` (address)
- `Finanzamtes Spittal Villach` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

| Predicted | Gold |
|---|---|
| `Mag. Artner-Tauscher` | `Mag. Artner-Tauscher` |

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

| Predicted | Gold |
|---|---|
| `Mag. Artner` | `Mag. Artner` |

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr. Padesse` | `Dr. Padesse` |
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Techn R HR Martina Pisterer, Kremenetzkygasse 12, 8385 Kalch, Österreich, über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 18. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R HR Martina Pisterer` (person)
- `Kremenetzkygasse 12, 8385 Kalch, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/130604.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde der  Annette Reeners, Räuflach 3, 8731 Schattenberg, Österreich  vom 10.12.2019, gegen das Straferkenntnis der belangten Behörde,  Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 26.11.2019,  MA67/196700932076/2019, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annette Reeners` (person)
- `Räuflach 3, 8731 Schattenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130748.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/130759.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130759.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter über die Beschwerde des  Franziskus Lex, Hansbauerweg 18, 4782 Oberhofen, Österreich, vom 22. Juni 2020 gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 18. Juni 2020, MA67/000/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit teilweise stattgegeben, als die von der  belangten Behörde mit € 60,00 verhängte Geldstrafe auf € 48,00 und die für den Fall der  Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfreiheitsstrafe auf 10 Stunden herabgesetzt  wird.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Lex` (person)
- `Hansbauerweg 18, 4782 Oberhofen, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/130804.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130804.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde der  Dipl.-Ing. Erwin Göktan, Leckbichl 2, 8151 Altreiteregg, Österreich, vom 21. Oktober 2020, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 30. September 2020, Zl.  MA67/206700734150/2020, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Irene Kohler` | `Mag. Irene Kohler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Erwin Göktan` (person)
- `Leckbichl 2, 8151 Altreiteregg, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ronald Töws, Schießstatt 9, 5124 Weyer, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ronald Töws` (person)
- `Schießstatt 9, 5124 Weyer, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/130839.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130839.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Gudrun Sochurek,  Rudolf-Novak-Gasse 63, 4225 Forst, Österreich, vertreten durch Mag. Rupert Karl, Kopplerstraße 59, 5321 Koppl, über die  Beschwerde vom 26. Oktober 2019 gegen den vorläufigen Bescheid des Finanzamtes vom  9. Oktober 2019 betreffend Einkommensteuer 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Rupert Karl` | `Mag. Rupert Karl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gudrun Sochurek` (person)
- `Rudolf-Novak-Gasse 63, 4225 Forst, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Dipl. Kff. Cäcilia Wlcek, Rambergweg 3, 4950 Weidenthal, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Cäcilia Wlcek` (person)
- `Rambergweg 3, 4950 Weidenthal, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/131072.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Valerie Süssmeier, Ögglweg 86, 8623 Tutschach, Österreich, über die Beschwerde vom 3. März 2020 gegen die Bescheide des  Finanzamtes Oststeiermark vom 10. Februar 2020 betreffend Umsatzsteuer 2013 bis 2018 und  Einkommensteuer 2013 bis 2018 sowie vom  4. Februar 2020 betreffend Festsetzung von  Selbstbemessungsabgaben gem. § 201 BAO 01.2019-06.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valerie Süssmeier` (person)
- `Ögglweg 86, 8623 Tutschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Jeffrey Wengschick  in der Beschwerdesache der Frau  Donald Hayder, MA, Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jeffrey Wengschick` | `Dr. Jeffrey Wengschick` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donald Hayder, MA` (person)
- `Koloman-Liebenberg-Gasse 23, 5442 Rußbachsaag, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/131160.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131160.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Valentin Kreuthmayr  in der Beschwerdesache Naomi Ruddis, LLB,  Schuselkagasse 21, 9570 Alt-Ossiach, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des Finanzamt Niederösterreich Mitte  vom 10. März 2020 betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für sich selbst ab Jänner 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Valentin Kreuthmayr` | `Mag. Valentin Kreuthmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Naomi Ruddis, LLB` (person)
- `Schuselkagasse 21, 9570 Alt-Ossiach, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/131225.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131225.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Holger Weiskittel, Schleifbachgasse 22, 4152 Leiten, Österreich, über die Beschwerde vom 4. Juli 2018 gegen den Bescheid des  Finanzamtes Feldkirch vom 6. Juni 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Holger Weiskittel` (person)
- `Schleifbachgasse 22, 4152 Leiten, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/131268.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131268.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131299.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Samuel Hegenbart, Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich, vom 23. November 2020 (eingelangt bei der belangten Behörde)  gegen die Vollstreckungsverfügung der belangten Behörde, Magistrat der Stadt Wien,  Magistratsabteilung 6, BA 32, vom 7. November 2020, GZ. MA67/Zahl/2020, betreffend  Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen Strafe auf Grund der  Strafverfügung vom 14. August 2020, MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Hegenbart` (person)
- `Dr. Viktor Frankl-Gasse 9, 6822 Dünserberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131407.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/131429.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131429.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/131567.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131567.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Valerius Wilbert  in der Finanzstrafsache gegen die  Beschuldigte Chen Kürkcü, An der Museumsbahn 11, 3122 Bichl, Österreich, vertreten durch Mag. Heinz Wolfbauer,  Rechtsanwalt, Stubenbastei 2, 1010 Wien, wegen des Finanzvergehens der  Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die  Beschwerde der Beschuldigten vom 15. März 2018 gegen das Erkenntnis des Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 14. Februar 2018,  Strafnummer StrNr,  zu Recht erkannt:  Der Beschwerde der Beschuldigten wird teilweise Folge gegeben und bei unverändert aufrecht  bleibendem Schuldspruch wegen Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG die  gemäß § 33 Abs. 5 FinStrG zu verhängende Geldstrafe auf € 2.800,00 sowie die gemäß § 21  Abs. 1 und 2 Finanzstrafgesetz für den Fall der Uneinbringlichkeit zu bemessende  Ersatzfreiheitsstrafe auf 7 Tage herabgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Heinz Wolfbauer` | `Mag. Heinz Wolfbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Valerius Wilbert` (person)
- `Chen Kürkcü` (person)
- `An der Museumsbahn 11, 3122 Bichl, Österreich` (address)
- `Finanzamtes  Wien 9/18/19 Klosterneuburg` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/131866.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131866.1_2`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131880.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/132162.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132162.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/132197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132197.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/132264.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132264.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/132342.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132342.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Rechtsmittelsache Olaf Vasiliadis, Weingartsberg 5, 9065 Niederdorf, Österreich, über die Vorlageanträge vom 21.12.2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 und Einkommensteuer  (Arbeitnehmerveranlagung) 2017, Steuernummer 03 13-336/4289  beschlossen:  Der Vorlageantrag vom 21.12.2020 betreffend Einkommensteuer 2015 wird gemäß § 264  Abs. 5 zweiter Fall BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olaf Vasiliadis` (person)
- `Weingartsberg 5, 9065 Niederdorf, Österreich` (address)
- `13-336/4289` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/132370.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132370.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Malik Stellmaszick, Am Weberbach 26, 9640 Gailberg, Österreich, über die Beschwerde vom 19. November 2012 gegen den Bescheid  des FA Wien 1/23 vom 8. November 2012 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2011, Steuernummer 92-110/0462  zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Malik Stellmaszick` (person)
- `Am Weberbach 26, 9640 Gailberg, Österreich` (address)
- `FA Wien 1/23` (organisation)
- `92-110/0462` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/132446.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer in der Beschwerdesache  Silvius Fingermann, Steibstraße 113, 5723 Litzldorf, Österreich, über die Beschwerde vom 3. Mai 2018 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 5. April 2018 betreffend Anspruchszinsen (§ 205 BAO) 2013,  Steuernummer 91-977/4633, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Diana Sammer` | `Mag. Diana Sammer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvius Fingermann` (person)
- `Steibstraße 113, 5723 Litzldorf, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)
- `91-977/4633` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132480.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Univ.-Prof.in StR Caroline Akkoca, MBA, Hinterbachstraße 8, 4653 Spieldorf, Österreich, über die Beschwerde des  Beschuldigten vom 19. Jänner 2021 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Jänner 2021, Zahl: MA67/206700566984/2020, mit  dem der Einspruch vom 10. November 2020 gegen die Strafverfügung vom 8. Oktober 2020 mit  derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in StR Caroline Akkoca, MBA` (person)
- `Hinterbachstraße 8, 4653 Spieldorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Franka Hilgenstock, Bockackerstraße 19, 4892 Sieberer, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franka Hilgenstock` (person)
- `Bockackerstraße 19, 4892 Sieberer, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rocco Girstenbrei, Waubergweg 6, 9710 Pöllan, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Maria Brandstetter` | `Dr. Maria Brandstetter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Rocco Girstenbrei` (person)
- `Waubergweg 6, 9710 Pöllan, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_63`)


NachnameGeser1 und dessen Steuerberater Mag. Stb bekannte Hr.  NachnameGeser1 zunächst, dass die [Bf.] über keinen Autoabstellplatz verfüge.

| Predicted | Gold |
|---|---|
| `Mag. Stb` | `Mag. Stb` |

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_74`)


Auch in der Schlussbesprechung vom 24.05.2016  wurde von Hrn. NachnameGeser1 in Anwesenheit seines Steuerberaters, Mag. Stb, behauptet,  er hätte einen potentiellen Käufer, der das Kfz in ca. zwei Wochen eventuell um ca. 300.000,-  Euro kaufen wolle, konkrete Angaben dazu wollte Hr. NachnameGeser1 aber nicht machen.

| Predicted | Gold |
|---|---|
| `Mag. Stb` | `Mag. Stb` |

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_76`)


Am 13.06.2016 erklärte dann der Steuerberater Mag. Stb, der Verkauf sei nicht zustande  gekommen, sodass Hr. NachnameGeser1 beabsichtige, das Kfz aus dem Betrieb um einen  gegenüber den Anschaffungskosten geringeren Preis zu entnehmen.

| Predicted | Gold |
|---|---|
| `Mag. Stb` | `Mag. Stb` |

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Jennifer Kuntzemann, MSc Bakk. iur., Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich, über die Beschwerde vom 11. April 2020 gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 11. März 2020 betreffend  Rückzahlung ausbezahlter Zuschüsse zum Kinderbetreuungsgeld für das Jahr 2014,  Steuernummer StrNr, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Kuntzemann, MSc Bakk. iur.` (person)
- `Margaretha-Eder-Straße 20, 2733 Gutenmann, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

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

- `Dr. Gabriele Grossgut-Palot` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Wendy Scherl`(person)
- `Eugen Markusplatz 18, 3261 Zarnsdorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `53-864/4798`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129235.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129235.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129477.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129571.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130444.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130559.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/130727.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130727.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/130744.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130744.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

**False Positives:**

- `Dr. Karl Renner-Ring` — partial — gold is substring of pred: `Dr. Karl Renner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl Renner`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hon.-Prof. Dragan Höh  in der Beschwerdesache ÖkR Mag.a Catharina Schmalenstrot,  8.b Straße 126, 4632 Buchet, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Floriane Herppich  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hon` — partial — pred is substring of gold: `Dr. Hon.-Prof. Dragan Höh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hon.-Prof. Dragan Höh`(person)
- `ÖkR Mag.a Catharina Schmalenstrot`(person)
- `8.b Straße 126, 4632 Buchet, Österreich`(address)
- `FA Braunau Ried Schärding`(organisation)
- `Floriane Herppich`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/131239.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131239.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Theophil Schachenmeier, Gsteinert 21, 4115 Steining, Österreich, betreffend die Beschwerde vom 03.04.2020 gegen den Bescheid  des Finanzamtes Freistadt Rohrbach Urfahr vom 26.03.2020 über die Einstellung der  Vollstreckung zu Steuernummer 63-906/4998  beschlossen:   Die Beschwerde wird gem. § 260 Abs. 1 lit. a) BAO zurückgewiesen.

**False Positives:**

- `Dr. Norbert` — partial — pred is substring of gold: `Dr. Norbert Zöls`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Norbert Zöls`(person)
- `Theophil Schachenmeier`(person)
- `Gsteinert 21, 4115 Steining, Österreich`(address)
- `Finanzamtes`(organisation)
- `63-906/4998`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die RichterinR in der Revisionssache Jonathan Hewett, Bakk. techn., Kleinbodenerstraße 17, 4880 Rixing, Österreich, vertreten durch Mag. Anton Heisinger Wirtschaftstreuhänder, Steuerberater,  Mühlallee 1, 7301 Deutschkreutz, über den Antrag des Revisionswerbers vom 26.6.2020, der  erhobenen außerordentlichen Revision vom 26.6.2020 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 12.5.2020, GZ RV/7103858/2015, betreffend Einkommensteuer  2010 die aufschiebende Wirkung zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

**False Positives:**

- `Mag. Anton Heisinger Wirtschaftstreuh` — partial — gold is substring of pred: `Mag. Anton Heisinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jonathan Hewett, Bakk. techn.`(person)
- `Kleinbodenerstraße 17, 4880 Rixing, Österreich`(address)
- `Mag. Anton Heisinger`(person)
- `Bundesfinanzgerichtes`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/131365.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131365.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/131368.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Norbert Zöls in der Beschwerdesache  Wendy Schärff, Krainberg 12, 4633 Weilbach, Österreich, vertreten durch LeitnerLeitner GmbH Wirtschaftsprüfer und  Steuerberater, Ottensheimer Straße 32, 4040 Linz, im fortgesetzten Verfahren über die  Beschwerde vom 27.08.2018  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2013 in Höhe von 6.232,84 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.2018 mit dem Anspruchszinsen (§ 205  BAO) für 2014 in Höhe von 4.137,27 € festgesetzt wurden  gegen den Bescheid des Finanzamtes Linz vom 27.06.

**False Positives:**

- `Dr. Norbert` — partial — pred is substring of gold: `Dr. Norbert Zöls`

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

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/131638.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131638.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck in der Beschwerdesache  Thobias Dommert, Hainfelder Straße 56, 4846 Gewerbepark West, Österreich, vertreten durch LBG Niederösterreich Steuerberatung GmbH, Wie- ner Straße 2, 2640 Gloggnitz, über die Beschwerden vom 29. Dezember 2017 und 31. Jänner  2018 gegen die Bescheide des Finanzamtes Neunkirchen Wiener Neustadt vom 6. Dezember  2017 und 10. Jänner 2018 betreffend Einkommensteuer 2007 bis 2011, St.Nr. 33- 66-847/2354, zu Recht erkannt:    Der Beschwerde gegen den Einkommensteuerbescheid 2007 wird teilweise Folge gegeben.

**False Positives:**

- `Mag. Johannes` — partial — pred is substring of gold: `Mag. Johannes Böck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johannes Böck`(person)
- `Thobias Dommert`(person)
- `Hainfelder Straße 56, 4846 Gewerbepark West, Österreich`(address)
- `LBG Niederösterreich Steuerberatung GmbH`(organisation)
- `Finanzamtes Neunkirchen Wiener Neustadt`(organisation)
- `66-847/2354`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/131705.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131705.1_92`)


Davon kann im gegenständlichen Fall hinsichtlich des  beschwerdegegenständlichen Jahres 2018 keine Rede sein:   Die Bf. hat zwar einen Schriftsatz (Arztbrief) vorgelegt, in dem der Arzt Dr. Martin Köppl  regelmäßige Rehabilitationsbehandlungen zum Erhalt der Selbständigkeit empfiehlt. Diese  Bestätigung des Hausarztes stammt vom 10.9.2018 und wurde also nachträglich ausgestellt.   Diese vermag jedoch aus o.a. Gründen mangels vorfeldweiser Verordnung keine  7 von 9 Seite 8 von 9

**False Positives:**

- `Dr. Martin` — partial — pred is substring of gold: `Dr. Martin Köppl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Martin Köppl`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/132030.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Sandro Fischlein, Hans-Schilder-Platz 17, 9065 Untermieger, Österreich, über die Beschwerde vom 29. Oktober 2020  gegen den Bescheid des Finanzamtes Gmunden Vöcklabruck vom 22. Oktober 2020 betreffend  Einkommensteuer 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-Palot` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Sandro Fischlein`(person)
- `Hans-Schilder-Platz 17, 9065 Untermieger, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Eugenia Vesen, Apollogasse 213, 5522 Lammertal, Österreich, vertreten durch Kleiner Eberl Brandstätter  Steuerberatung GmbH, Burgring 22, 8010 Graz, über die Beschwerde vom 25. September 2015  gegen die Bescheide des Finanzamtes Österreich je vom 25. August 2015 betreffend  Körperschaftsteuer 2006 bis einschließlich 2009 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eugenia Vesen`(person)
- `Apollogasse 213, 5522 Lammertal, Österreich`(address)
- `Kleiner Eberl Brandstätter  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde von Sebastian Claasen, Schloß Stainach 146, 4844 Lahn, Österreich, vom 9. März 2021, gegen den Bescheid des  Magistrats der Stadt Wien, Magistratsabteilung 67, vom 23. Februar 2021, Zahl  MA67/Zahl1/2018, wegen Verspätung zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen.

**False Positives:**

- `Mag. Andrea` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Sebastian Claasen`(person)
- `Schloß Stainach 146, 4844 Lahn, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/132731.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132731.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat über die Beschwerde vom  11. September 2020 des Beschwerdeführers Leila Höflein, Äussere Vorachstraße 25, 4081 Deinham, Österreich, vertreten durch die  Dr. Heinz Häupl Rechtsanwalts GmbH, 4865 Nußdorf, Stockwinkl 18, gegen den Bescheid des  Finanzamtes Freistadt Rohrbach Urfahr (nunmehr Finanzamt Österreich) vom 10. August 2020  betreffend Abweisung des Antrages vom 24.07.2020 auf Aufhebung der  Umsatzsteuerbescheide 2011 und 2013 sowie der Einkommensteuerbescheide 2010, 2011  und 2013 gemäß § 299 Abs 1 BAO den Beschluss:      I)

**False Positives:**

- `Dr. Heinz` — partial — pred is substring of gold: `Dr. Heinz Häupl Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Leila Höflein`(person)
- `Äussere Vorachstraße 25, 4081 Deinham, Österreich`(address)
- `Dr. Heinz Häupl Rechtsanwalts GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/132752.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132752.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rocco Girstenbrei, Waubergweg 6, 9710 Pöllan, Österreich, vertreten durch Dr. Maria Brandstetter,  Stephansplatz 4/VIII, 1010 Wien, über die Beschwerde vom 5. August 2020 gegen die  Bescheide des Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 01. Juli  2020 betreffend Vorschreibung der Wettterminalabgabe für den Monat April 2017 und eines  Verspätungszuschlages zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Rocco Girstenbrei`(person)
- `Waubergweg 6, 9710 Pöllan, Österreich`(address)
- `Dr. Maria Brandstetter`(person)
- `Magistrats der Stadt Wien`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Eduard Schulden, Bakk. rer. nat., Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich, vertreten durch Dkfm. Freund & Partner Steuerberater GmbH, Schellinggasse 3, 1010  Wien, über die Beschwerde vom 29. Juli 2016 (Eingangsstempel 1. August 2016 ) gegen den  Umsatzsteuerbescheid 2011 und den Bescheid über die Feststellung von Einkünften gemäß  § 188 BAO 2011 des Finanzamtes Baden Mödling vom 5. Juli 2016, Steuernummer  16 28-951/9095, zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hans Kl` — partial — pred is substring of gold: `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Eduard Schulden, Bakk. rer. nat.`(person)
- `Dr. Hans Klöpfer-Straße 49, 4941 Baching, Österreich`(address)
- `Freund & Partner Steuerberater GmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `28-951/9095`(tax_number)

</details>

---

## `german_legal_person_double_titles` 

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `662e9140`  
**Description:**
Matches double titles like 'Mag. Dr.' or 'Dr. Mag.' followed by names, capturing the full title and name.

**Content:**
```
\b(?:Mag\.\s+Dr\.|Dr\.\s+Mag\.)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.000 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 1781 |

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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_13`)


Mag. Dr. Wieland Reinecke (Beschwerdeführer, kurz: Bf.) wurde von Kontrollorganen der  Parkraumüberwachung der Landespolizeidirektion Wien in der gebührenpflichtigen  Kurzparkzone in 1030 Wien, Marokannergasse 18,   1. am 1. Dezember P20 um 15:45 Uhr (Z1 und  2. am 3. Dezember 2020 um 15:11 Uhr (Z2  3. am 7. Dezember 2020 um 12:32 Uhr (Z3),  4. am 9. Dezember 2020 um 20:04 Uhr (Z4)  beanstandet, da es ohne einen für den jeweiligen Beanstandungszeitpunkt gültigen Parkschein  abgestellt war.

**False Positives:**

- `Mag. Dr. Wieland Reinecke` — partial — gold is substring of pred: `Wieland Reinecke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wieland Reinecke`(person)
- `Landespolizeidirektion Wien`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/142010.1`) (sent_id: `deanon_BFG_20260814_TRAIN/142010.1_1`)


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

</details>

---

## `german_legal_person_complex_titles` 

**F1:** 0.001 | **Precision:** 0.250 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e3249e95`  
**Description:**
Matches complex academic titles (Univ.-Prof., Hon.-Prof., Priv.-Doz.) followed by Dr. and names, capturing the full title and name, including hyphenated surnames.

**Content:**
```
\b(?:Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Prof\.)\s+Dr\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\-[A-Z][a-z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.000 | 0.001 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 2329 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/139698.1`) (sent_id: `deanon_BFG_20260814_TRAIN/139698.1_106`)


Der nachmalige (seit 2014) Präsident des Verwaltungsgerichtshofes, Univ.-Prof. Dr. Rudolf  Thienel, führt dazu in der Festschrift zum 65.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Rudolf  Thienel` | `Univ.-Prof. Dr. Rudolf  Thienel` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_46`)


Der Sachverständigen standen folgende Unterlagen zur Verfügung:  Arztbrief von Univ.Prof. Dr. Sasan Hamzavi vom 05.09.2018:  Dem Arztbrief ist Folgendes zu entnehmen:  "Nachfolgend berichte ich über Patienten S., der am 05.09.2018 bei mir in Behandlung war.

**False Positives:**

- `Univ.Prof. Dr. Sasan Hamzavi` — partial — gold is substring of pred: `Dr. Sasan Hamzavi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sasan Hamzavi`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/144966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/144966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Piedro Röbbel, Konstanze-Weber-Gasse 15, 9400 Raggl, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 313, 4040 Linz, über die Beschwerde vom  18. Oktober 2022 gegen den Bescheid des Finanzamtes Österreich vom 22. September 2022  betreffend Einkommensteuer 2021 Steuernummer 91-345/5352  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Piedro Röbbel`(person)
- `Konstanze-Weber-Gasse 15, 9400 Raggl, Österreich`(address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `91-345/5352`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_116`)


Lebensjahr festgestellt.  Im Privatgutachten vom 25. Juli 2023 bescheinigt Univ.-Prof. Dr. Otto L., Facharzt für  Psychiatrie und Neurologie, allgem. beeid, und gerichtlich zertifizierter Sachverständiger der  Bf. eine schwere Leistungseinbuße seit Geburt.

**False Positives:**

- `Univ.-Prof. Dr. Otto` — partial — pred is substring of gold: `Univ.-Prof. Dr. Otto L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Dr. Otto L.`(person)

</details>

---

## `german_legal_person_without_titles` 🏆

**F1:** 0.025 | **Precision:** 0.146 | **Recall:** 0.014  

**Format:** `regex`  
**Rule ID:** `e7a4688e`  
**Description:**
Matches person names appearing after specific legal role indicators or conjunctions to capture names without titles, ensuring full name capture and excluding partial words.

**Content:**
```
(?:Partei|Kl\u00e4ger|Beklagte|Vertreter|Anwalt|Zeuge|Gutachter|Sachverst\u00e4ndige|Vorsitzende|Vorsitzender|Mitglied|Mitglieder|durch|und|sowie)\s+([A-Z][a-z]+\s+[A-Z][a-z]+)(?:\s|,|\)|\.|$)(?!\s*(?:Gericht|Hof|Oberlandes|Landes|Spruch|Kopf|Der|Die|Dem|Den|Zivil|Straf|Handel|Sozial|Weg|Markt|Gruppe|GmbH|AG|Rechtsanw|Versand|Schaf|Zumtobel|Oberste|Landesgerichts|Bezirksgerichts|Zivilrechtssachen|Sozialrechtssachen|Urteilsver|Divitschek|Software|Unterlassung|Feststellung|Partei|Mag\.\s+Istjan|Tr\.\s+|Co\.\s+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.146 | 0.014 | 0.025 | 233 | 34 | 199 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 34 | 199 | 2419 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/129075.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129075.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Maximilian Joobs, in der Folge kurz mit Bf. bezeichnet, wohnte vom 15.7.2014 bis 27.2.2017 mit  ihrem Mann NN-KV VN-KV und den Kindern NN-KV Kind2, NN-KV Kind3, NN-KV Kind4, NN-KV  Kind1 und NN-KV Kind5 in einem gemeinsamen Haushalt.  Mit Beschluss des Bezirksgerichtes ORT wurde die zwischen VN-KV NN-KV und Maximilian Joobs  am  x.2007 geschlossene Ehe mit der Wirkung geschieden, dass sie mit Rechtskraft dieses  Beschlusses aufgelöst war.

| Predicted | Gold |
|---|---|
| `Maximilian Joobs` | `Maximilian Joobs` |

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_16`)


Der Bf. wurde vom Finanzamt im Zuge des Antrages auf Erhöhungsbetrag zur Familienbeihilfe  wegen erheblicher Behinderung das folgende Sachverständigengutachten vom 17.12.2018  übermittelt.  Am 17.12.2018 wurde von Dr.in Ljiljana Kos, Fachärztin für Kinder- und Jugendheilkunde das  Gutachten vom 17.12.2018 erstellt:  "Zusammenfassung der Sachverständigengutachten  Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos, Kinder- und Jugendheilkunde, vom 26.11.2018  Die genannten Gutachten sind ein wesentlicher Bestandteil dieser Gesamtbeurteilung.

| Predicted | Gold |
|---|---|
| `Ljiljana Kos` | `Ljiljana Kos` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Dr.in Ljiljana Kos` (person)
- `Dr. Alexander Nahler` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/129876.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129876.1_33`)


Auf Grund eines Ersuchens um Ergänzung des Finanzamtes brachte die Bf. eine Kopie der  Gesamtbeurteilung nach der Einschätzungsverordnung vom 17.12.2018 mit der  Zusammenfassung der Sachverständigengutachten Dr. Alexander Nahler vom 08.10.2018 und  Ljiljana Kos vom 26.11.2018, ein Audiogramm vom 26.6.20 Dr. Schmid,  die Neuropädiatrische  Stellungnahme vom 7.9.2018, Patientenbriefe der Klinik Favoriten von 6.8.2019, 13.2.2020 und  25.8.2020, deren jeweilige Diagnose „Hyperhidrosis palmaris et Plantaris bds“ war und als  frühere Krankheiten Innenschwerhörigkeiten li. anführten.

| Predicted | Gold |
|---|---|
| `Ljiljana Kos` | `Ljiljana Kos` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Dr. Alexander Nahler` (person)
- `Dr. Schmid` (person)
- `Klinik Favoriten` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_17`)


Darüber hinaus werden die dem Erwachsenenvertreter vorliegenden psychiatrischen  Gutachten vorgelegt, aus diesen ist ersichtlich, dass bei (der Bf.) eine angeborene Oligophrenie  vorliegt (Psychiatrisches Gutachten Univ.Prof. Dr.med. F. St. vom 28.04.1987), ebenso wie die  Sachverständige Charles Hegler von einer angeborenen Minderbegabung ausgeht, mit später  aufgetretenen psychotischen und schizophrenen Symptomen.

| Predicted | Gold |
|---|---|
| `Charles Hegler` | `Charles Hegler` |

**Missed by this rule (FN):**

- `Univ.Prof. Dr.med. F. St.` (person)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/130733.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alfred Klaming in der Beschwerdesache  Calvin Gorol, Paulanergasse 10, 8211 Schirnitz, Österreich, vertreten durch Helmut Binder, Postgasse 8 Tür 1, 9500 Villach,  über die Beschwerden vom 12. Oktober 2018 gegen die Bescheide des Zollamtes Klagenfurt  Villach vom 11. September 2018, GZlen.

| Predicted | Gold |
|---|---|
| `Helmut Binder` | `Helmut Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alfred Klaming` (person)
- `Calvin Gorol` (person)
- `Paulanergasse 10, 8211 Schirnitz, Österreich` (address)
- `Zollamtes Klagenfurt` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/131248.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131248.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/133177.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133177.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/135111.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135111.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterPerson_A in der Beschwerdesache Leander Tumoseit,  Schwaighofweg, Oberau 122, 4121 Hörhag, Österreich, vertreten durch Othmar Huttary, Höttinger Au 76, 6020 Innsbruck, über die  Beschwerde vom 18. September 2015 gegen die Bescheide des [...] vom 20. August 2015 über  die Festsetzung von Anspruchszinsen (§ 205 BAO) für die Jahre 2011 und 2012, Steuernummer  56-131/0598, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Othmar Huttary` | `Othmar Huttary` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leander Tumoseit` (person)
- `Schwaighofweg, Oberau 122, 4121 Hörhag, Österreich` (address)
- `56-131/0598` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/136562.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136562.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_92`)


Punkt 2.5.10.2 Abs 1 der AGB 2006 lautet wörtlich:   „Schadenersatz aufgrund fristloser Kündigung  Bei fristloser Kündigung durch Simon Zieselsberger  und – falls die Parteien keine andere Vereinbarung  getroffen haben – in allen sonstigen Fällen der vorzeitigen Vertragsbeendigung schuldet der  Kunde neben den rückständigen Leasingraten – auch im Fall der Insolvenz – einen sofort  fälligen Schadenersatzanspruch statt der Leistung;

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_106`)


Bei außerordentlicher Kündigung durch Simon Zieselsberger  und – falls die Parteien keine andere  Vereinbarung getroffen haben – in allen sonstigen Fällen der Vertragsbeendigung vor Erreichen  der Kalkulationsbasisdauer, ausgenommen im Falle des Diebstahls oder Totalschadens,  schuldet der Kunde neben den rückständigen Leasingraten – auch im Fall der Insolvenz – einen  sofort fälligen Schadenersatzanspruch statt der Leistung;

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/137355.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137355.1_143`)


Der Kunde wird für die  termingerechte Vorführung zu gesetzlich vorgeschriebenen Untersuchungen (z.B. § 57a KFG  Überprüfung) sorgen und Simon Zieselsberger  von allen Ansprüchen Dritter in Bezug auf das  Leasingfahrzeug freistellen.“

| Predicted | Gold |
|---|---|
| `Simon Zieselsberger` | `Simon Zieselsberger` |

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/127180.1`) (sent_id: `deanon_BFG_20260814_TRAIN/127180.1_3`)


I. Zugrundeliegender Sachverhalt und Verfahrensgang Strittig erwies sich in der gegenständlichen Beschwerdesache, ob zwischen den Vertragsparteien eine der Bestandvertragsgebühr unterliegende Option oder ein gebührenrechtlich nicht steuerbarer Vorvertrag vereinbart wurde: Die Beschwerdeführerin schloss als Bestandnehmerin mit der Hötzel Lebensmittel GmbH  als Bestandgeberin den mit 14.9.2019 datieren schriftlichen Pachtvertrag über eine Geschäftsräumlichkeit (Betrieb einer Apotheke) ab.

**False Positives:**

- `Verfahrensgang Strittig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hötzel Lebensmittel GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/128776.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128776.1_16`)


Die Seminarveranstalter werben mit der Übermittlung folgender Fertigkeiten:  NLP-KOMPAKT & Trinergy  „Das bringt dir dein KOMPAKT: Hast Du jemals etwas getan, das Deine Lebensqualität und  Deine Qualifikation grundlegend verbessert hat?

**False Positives:**

- `Deine Qualifikation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/128782.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128782.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Viktoria Kreiselmayer  in der Beschwerdesache Muran Waldhans, BEd,  Am Tegel 5, 9831 Waben, Österreich, vertreten durch Corazza Kocholl Laimer Rechtsanwälte OG, Maximilianstraße  9, 6020 Innsbruck, über die Beschwerde vom 22. April 2010 gegen den Bescheid des  Finanzamtes Innsbruck vom 22. März 2010, StrNr, betreffend Umsatzsteuer für den Erwerb  neuer Fahrzeuge (Art. 1 Abs. 7 UStG 1994) für den Zeitraum August 2005 im fortgesetzten  Verfahren zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Corazza Kocholl` — partial — pred is substring of gold: `Corazza Kocholl Laimer Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Viktoria Kreiselmayer`(person)
- `Muran Waldhans, BEd`(person)
- `Am Tegel 5, 9831 Waben, Österreich`(address)
- `Corazza Kocholl Laimer Rechtsanwälte OG`(organisation)
- `Finanzamtes Innsbruck`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/128855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128855.1_57`)


Es gab  somit im Ermittlungsverfahren für das Finanzamt keine Möglichkeit, den tatsächlich durch Ihre  Behinderung verursachten Mehraufwand für die Diätverpflegung festzustellen, sodass nur der  bereits im Erstbescheid berücksichtigte Pauschalbetrag für die Diätverpflegung als steuerliche  Abzugspost anerkannt werden konnte.“

**False Positives:**

- `Ihre  Behinderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TRAIN/128966.1`) (sent_id: `deanon_BFG_20260814_TRAIN/128966.1_12`)


Laut Firmenbuchauszug waren Sie vom xx.yy.2017 bis zur Eröffnung des Insolvenzverfahrens  am 28.02.2018 als Vertreter der GmbH bestellt. Auf Grund Ihrer Funktion, als zur Vertretung  2 von 9 Seite 3 von 9

**False Positives:**

- `Ihrer Funktion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129187.1_4`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Am 18.

**False Positives:**

- `Sachverhalt  Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129218.1_5`)


Mit Ergänzungsvorhalt vom 14.9.2016 wurde der Beschwerdeführer ersucht, betreffend  doppelter Haushaltsführung, Familienheimfahrten und Pendlereuro Fragen zu beantworten  bzw. Unterlagen einzureichen.

**False Positives:**

- `Pendlereuro Fragen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TRAIN/129250.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129250.1_64`)


Die Unter Wilkel GmbH war nach Abtretung der Anteile am 15.1.2008 und  Gesellschafterwechsel Nachfolgerin der vormaligen P-GmbH. Diese war im Einzelhandel tätig  und hatte sogenannte Ein-Euro-Shops betrieben.

**False Positives:**

- `Gesellschafterwechsel Nachfolgerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Unter Wilkel GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129254.1_142`)


Vorliegen eines Bestandvertrages und Vertragsdauer  Nach § 33 TP 5 Abs 1 Z 1 GebG unterliegen der Gebühr für Rechtsgeschäfte Bestandverträge  (§§ 1090 ff ABGB) und sonstige Verträge, wodurch jemand den Gebrauch einer  unverbrauchbaren Sache auf eine gewisse Zeit und gegen einen bestimmten Preis erhält.  Leasingverträge haben keinen einheitlichen feststehenden Inhalt, sondern treten in vielfältigen  Varianten und Erscheinungsformen mit jeweils anderen Rechten und Pflichten auf.

**False Positives:**

- `Vertragsdauer  Nach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_59`)


Die Stellungnahme des Finanzamtes wurde zur Wahrung des Parteiengehörs dem Bf.  übermittelt.  Der Bf. erklärte ergänzend, dass nach seiner Ansicht im vorliegenden Fall Fremdleistungen an  seine Firma durch die Firma T zu beurteilen seinen und die Frage, ob der  Fremdleistungsaufwand der Firma T an deren Subfirmen Firma C und Firma Ch anzuerkennen  sei, im gegenständlichen Verfahren nicht relevant sei.

**False Positives:**

- `Firma Ch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129432.1_62`)


es sei lediglich der Austausch zwischen  der Firma T und deren Subunternehmern Firma Spies&Wickert Solar GmbH und Firma Ch angezweifelt worden.

**False Positives:**

- `Firma Ch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Spies&Wickert Solar GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129484.1_3`)


Entscheidungsgründe  I. Sachverhalt und Verfahrensgang  Die Beschwerdeführerin (in der Folge Bf. genannt) ist eine im Jahr 2009 ins Firmenbuch  eingetragene Gesellschaft mit beschränkter Haftung.

**False Positives:**

- `Verfahrensgang  Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TRAIN/129635.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129635.1_246`)


Die Darstellung im Vorlageantrag an das BFG wurde teilweise wiederholt.   Die Bf. erläutert, dass sie als start-up das mit dem Ziel der Entwicklung einer neuartigen  Trocknungsanlage gegründet wurde und gemeinsam mit professionellen Forschungs- und  Anlagefirmen Pilotanlagen und Prototypen entwickelt und Probetrocknungen durchgeführt  hat.

**False Positives:**

- `Anlagefirmen Pilotanlagen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129789.1_25`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

**False Positives:**

- `Hinweise  Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Verfassungsgerichtshof`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TRAIN/129832.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129832.1_4`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Der Beschwerdeführer erzielt u.a. Einkünfte aus Vermietung und Verpachtung.

**False Positives:**

- `Sachverhalt  Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/129907.1_78`)


Da das Finanzamt den anteiligen Kosten für Telefon  und Internet Abzugskostencharakter zugesprochen und die Bf. die in Rede stehenden  Ausgaben als Werbungskosten gewertet hatte, bestanden angesichts der Aktenlage keine  Bedenken, die in Höhe von 287,64 € geltend gemachten Telefon- und Internetkosten  antragsgemäß als Werbungskosten anzuerkennen und bei der Berechnung der  Einkommensteuer für das Jahr 2013 bei den Einkünften aus nichtselbständiger Arbeit zu  berücksichtigen.

**False Positives:**

- `Internet Abzugskostencharakter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TRAIN/130152.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130152.1_129`)


In der Entscheidung vom 20.08.2003, RV/4055-W/02, erwog der unabhängige Finanzsenat:   Im gegenständlichen Berufungsfall stellte der Facharzt für Neurologie und Psychiatrie Linn Gösele in  seinem schlüssig begründeten Gutachten vom 14. Dezember 2002 den Grad der Behinderung  mit 50 v.H. (Oligophrenie mit Verhaltensstörung) fest, ebenso wurde im Gutachten festgestellt,  dass die Bw. nicht.

**False Positives:**

- `Psychiatrie Linn` — positional overlap with gold: `Linn Gösele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linn Gösele`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TRAIN/130311.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130311.1_9`)


keine aktuelle Schulbestätigung von Ihrem Sohn M… vorgelegt haben und dadurch Ihrer  Mitwirkungspflicht nach § 119 Bundesabgabenordnung nicht nachgekommen sind, muss  angenommen werden, dass in oben genannten Zeitraum kein Anspruch auf Familienbeihilfe  bestanden hat bzw. besteht.

**False Positives:**

- `Ihrer  Mitwirkungspflicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130423.1_207`)


Ab 19 05 2020 im Wohnheim (2 Bettzimmer) der  Heilsarmee mit Betreuung und Tagesstruktur    Ledig, keine Kinder   Seit 2016 besachwaltet   Bezüge: das wisse er nicht   Führerschein: in Äthiopien habe er den 2014 oder 2015 gemacht , kein FS in Österreich

**False Positives:**

- `Tagesstruktur    Ledig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TRAIN/130533.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130533.1_7`)


Bei Fahrten mit dem eigenen Auto: Vorlage Fahrtenbuch, Kopie Zulassungsschein und Vorlage  Tankbelege.

**False Positives:**

- `Vorlage  Tankbelege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Bf., Wien, vertreten durch Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH., Sternwartestraße 76, 1180 Wien, über die Beschwerde der Abgabepflichtigen vom  28. November 2014 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 10. November 2014 über die Festsetzung eines ersten Säumniszuschlages zur  Steuernummer 10-012/8743 nach Durchführung von mündlichen Verhandlungen, zuletzt am  12. Oktober 2020 in Anwesenheit der Beschwerdeführerin, der Vertreter der belangten  Behörde sowie der Schriftführerin zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Treufinanz Steuerberatung` — partial — pred is substring of gold: `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Treufinanz Steuerberatung Wirtschaftstreuhand  GmbH.`(organisation)
- `Finanzamtes für Gebühren`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TRAIN/130914.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130914.1_16`)


Da aus diesem Grund zum Fälligkeitstag  der Gebühren 07/2014 kein Guthaben auf dem Abgabenkonto bestand, besteht der  Säumniszuschlag zu Recht und Ihrem Antrag musste der Erfolg versagt werden."

**False Positives:**

- `Ihrem Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260814_TRAIN/130980.1_184`)


Schon alleine durch die Unterstützung im IT-Bereich durch seinen Sohn und Mitarbeiter  Herrn [SohnBf] konnten maßgebliche finanzielle Mehrbelastungen vermieden werden -  vor allem im Hinblick auf Stundensätze die von externen Unternehmen in der IT-Branche  durchschnittlich in Rechnung gestellt werden.

**False Positives:**

- `Mitarbeiter  Herrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Maltern, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Krankenpflege Maltern` — partial — gold is substring of pred: `Maltern`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maltern`(city)

**Example 26** (doc_id: `deanon_BFG_20260814_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Floriane Herppich  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Maltern  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Krankenpflege Maltern` — partial — gold is substring of pred: `Maltern`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Floriane Herppich`(person)
- `Maltern`(city)

**Example 27** (doc_id: `deanon_BFG_20260814_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131270.1_96`)


Herr und Frau Herpel besuchen dort  gemeinsam Restaurants, das FitnessCenter, Ärzte oder absolvieren Theaterbesuche.

**False Positives:**

- `Frau Herpel` — partial — gold is substring of pred: `Herpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Herpel`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TRAIN/131327.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131327.1_18`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

**False Positives:**

- `Hinweise  Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Verfassungsgerichtshof`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_58`)


Verfahrensablauf nach DB2:  2014 (Frist 30.4. bzw. 30.6.2015):  18.12.2014 - Versand E1  13.10.2015 – automatische Erinnerung mit Nachfristsetzung 3.11.2015  2.2.2016 - Erinnerung mit Nachfrist 23.2.2016 und Androhung Zwangsstrafe  19.2.2016 – Erklärungseingang  2015 (Frist 30.4. bzw. 30.6.2016)  18.12.2015 – Versand E1  21.10.2016 – automatische Erinnerung mit Nachfristsetzung  28.10.2016 – Erklärungseingang  2016 (Frist 30.4. bzw. 30.6.2017)  19.12.2016 – Versand E1  2.11.2017 – automatische Erinnerung mit Nachfristsetzung 23.11.2017  22.1.2018 – Erinnerung mit Nachfrist 12.2.2018 und Androhung Zwangsstrafe  22.2.2018 – Erklärungseingang  4 von 10 Seite 5 von 10

**False Positives:**

- `Androhung Zwangsstrafe` — no gold match — likely missing annotation
- `Androhung Zwangsstrafe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 30** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_59`)


2017 (Frist 30.4. bzw. 30.6.2018)  21.12.2017 – Versand E1  26.9.2018 – Erklärungseingang  2018 (Frist 30.4. bzw. 30.6.2019)  20.12.2018 – Versand E1  10.10.2019 – automatische Erinnerung mit Nachfristsetzung 31.10.2019  19.11.2019 – Erinnerung mit Nachfrist 10.12.2019 und Androhung Zwangsstrafe  10.2.2020 – Festsetzung Zwangsstrafe und Nachfrist 2.3.2020  30.4.2020 – Erklärungseingang  Ad 2.

**False Positives:**

- `Androhung Zwangsstrafe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TRAIN/131366.1`) (sent_id: `deanon_BFG_20260814_TRAIN/131366.1_72`)


Im Hinblick auf das bisherige Verhalten des Beschwerdeführers bei der Erfüllung seiner  abgabenrechtlichen Pflichten ist unstrittig von folgenden Geschehnissen auszugehen:  2014 (Frist 30.4. bzw. 30.6.2015):  18.12.2014 - Versand E1  13.10.2015 – automatische Erinnerung mit Nachfristsetzung 3.11.2015  2.2.2016 - Erinnerung mit Nachfrist 23.2.2016 und Androhung Zwangsstrafe  19.2.2016 – Erklärungseingang  2015 (Frist 30.4. bzw. 30.6.2016)  18.12.2015 – Versand E1  21.10.2016 – automatische Erinnerung mit Nachfristsetzung  28.10.2016 – Erklärungseingang  2016 (Frist 30.4. bzw. 30.6.2017)  19.12.2016 – Versand E1  2.11.2017 – automatische Erinnerung mit Nachfristsetzung 23.11.2017  22.1.2018 – Erinnerung mit Nachfrist 12.2.2018 und Androhung Zwangsstrafe  22.2.2018 – Erklärungseingang  2017 (Frist 30.4. bzw. 30.6.2018)  21.12.2017 – Versand E1  26.9.2018 – Erklärungseingang  2018 (Frist 30.4. bzw. 30.6.2019)  20.12.2018 – Versand E1  10.10.2019 – automatische Erinnerung mit Nachfristsetzung 31.10.2019  19.11.2019 – Erinnerung mit Nachfrist 10.12.2019 und Androhung Zwangsstrafe  10.2.2020 – Festsetzung Zwangsstrafe und Nachfrist 2.3.2020  30.4.2020 – Erklärungseingang  Die vom Beschwerdeführer ins Treffen geführten privaten und beruflichen Probleme, die ihn  an der Abgabe einer Erklärung gehindert hätten, konnten von diesem weder näher erläutert,  noch nachgewiesen oder glaubhaft gemacht werden.

**False Positives:**

- `Androhung Zwangsstrafe` — no gold match — likely missing annotation
- `Androhung Zwangsstrafe` — no gold match — likely missing annotation
- `Androhung Zwangsstrafe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 32** (doc_id: `deanon_BFG_20260814_TRAIN/132109.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132109.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch den RichterR zu folgenden, samt Vorlagebericht vom  8.8.2019 an das BFG vorgelegten, vermeintlichen Rechtsmitteln:   von der steuerlVertreter1alterFirmenwortlaut, FN steuerlVertr1Firmenbuchnummer  (nunmehriger Firmenwortlaut: steuerlVertr1neuerFirmenwortlaut) mit Schreiben vom  19.12.2013 für die nicht (mehr) parteifähige nunmehrFirmenwortlautExGeschäftsherrin  (vormals alterFirmenwortlautExGeschäftsherrin) & atypisch stille Gesellschaft,  Steuernummer 06-57-096/3352  erhobene vermeintliche Berufung (nunmehr:  vermeintliche Beschwerde) gegen Feststellungsbescheide nach § 92 iVm § 190 Abs. 1  BAO für 2003 bis 2006 und gegen Bescheide über die Wiederaufnahme der Verfahren  betreffend Feststellung der Einkünfte gemäß § 188 BAO für 2003 bis 2006 des  Finanzamtes Wien 8/16/17 vom 4.12.2013,   von steuerlicherVertreter2 mit Schreiben vom 9. Mai 2019 für die nicht (mehr)  parteifähige nunmehrFirmenwortlautExGeschäftsherrin & atypisch Still, Steuernummer:  06-57-096/3352  gestellter, vermeintlicher Vorlageantrag aufgrund zweier,  abweisender Beschwerdevorentscheidungen des Finanzamtes Wien 8/16/17 vom  15.4.2019 hinsichtlich Feststellungen gemäß § 92 iVm § 190 Abs. 1 BAO für 2003 bis  2005 und Wiederaufnahme Feststellungsverfahren 2003 bis 2005,  beschlossen:  Die diesbezüglichen verwaltungsgerichtlichen Verfahren werden eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) zulässig.

**False Positives:**

- `Wiederaufnahme Feststellungsverfahren` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `BFG`(organisation)
- `06-57-096/3352`(tax_number)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-57-096/3352`(tax_number)
- `Finanzamtes Wien 8/16/17`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_73`)


204  Angewandte Psychologie  Kommunikation und  Konfliktmanagement   Berufsethik und  Gesellschaftslehre    Menschenrechte

**False Positives:**

- `Konfliktmanagement   Berufsethik` — no gold match — likely missing annotation
- `Gesellschaftslehre    Menschenrechte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 34** (doc_id: `deanon_BFG_20260814_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132165.1_75`)


1134  Sicherheitspolizeiliche  Handlungslehre   Straf- und Privatrecht   Verfassungsrecht und  Europäische Union   Verkehrsrecht   Verwaltungsrecht   Kriminalistik   Bürokommunikation

**False Positives:**

- `Privatrecht   Verfassungsrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TRAIN/132255.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132255.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Sophie Nauman  in der Beschwerdesache Prof. Helmut Fürnkäß,  vertreten durch Dr Christian Leskoschek, Landstrasser Hauptstrasse 75-77/12, 1030 Wien, über  die Beschwerde vom 14. Juni 2017 gegen den Bescheid des Finanzamtes Österreich vom  23. Mai 2017 betreffend Einkommensteuer 2015 Steuernummer 024/4992 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr Christian` — partial — pred is substring of gold: `Dr Christian Leskoschek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Sophie Nauman`(person)
- `Prof. Helmut Fürnkäß`(person)
- `Dr Christian Leskoschek`(person)
- `Finanzamtes Österreich`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TRAIN/132394.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132394.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132647.1_166`)


• Sonstige Bezüge Niwalden und Bund   Vom Finanzamt wurden diese wieder mit 100 % angesetzt;

**False Positives:**

- `Bund   Vom` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_12`)


seitdem hält dieser 6% des Stammkapitals und Frau Eisenkrammer NachnameGeser1  94% des Stammkapitals.

**False Positives:**

- `Frau Eisenkrammer` — partial — gold is substring of pred: `Eisenkrammer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Eisenkrammer`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132794.1_90`)


Primäre Zweckbestimmung des streitgegenständlichen Kfz, welches sich ab dem Erwerb im  Jahr 2011 bis zum Verkauf im Jahr 2016 im zivilrechtlichen Eigentum der Bf. befand, war die  Ermöglichung der Nutzung durch Herrn Hus  welcher wie ein  Eigentümer über das Kfz verfügte.

**False Positives:**

- `Herrn Hus` — partial — gold is substring of pred: `Hus`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hus`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_71`)


Das Kinderbetreuungsgeld und der Zuschuss für den Zeitraum von 1.1. bis DATUM errechnen  sich gemäß § 3 Abs. 1 KBGG und § 10 KBGG wie folgt:  [...]  Der anzurechnende, den Grenzbetrag übersteigende Betrag errechnet sich wie folgt:    Daraus ergibt sich, dass Sie 2012 die Einkommensgrenze des § 8 Abs. 1 so weit überschritten  haben, dass Sie und Ihr Mann in diesem Jahr keinen Anspruch auf Kinderbetreuungsgeld und  den Zuschuss hatten.

**False Positives:**

- `Ihr Mann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_TRAIN/132855.1`) (sent_id: `deanon_BFG_20260814_TRAIN/132855.1_78`)


Das Finanzamt hat Ihnen und Ihrem Mann im September 2019 Formulare KBG2 betreffend die  Rückzahlung des Zuschusses zum Kinderbetreuungsgeld für das Jahr 2014 übermittelt.  In diesem Jahr überstieg das Familieneinkommen zum ersten Mal die für die Abgabe gemäß  §§ 18 und 19 KBGG festgelegte Grenze von 35.000,00 Euro.

**False Positives:**

- `Ihrem Mann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_TRAIN/133241.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133241.1_4`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt   Am 29.04.2014 unterfertigten die B und die C als Vermieterinnen und die (spätere) X als  Mieterin einen Bestandvertrag auf die Dauer von fünf Jahren samt Option auf dreimalige  Verlängerung von je fünf Jahren (Punkt 2.1. des Mietvertrages).

**False Positives:**

- `Sachverhalt   Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133433.1_74`)


Im  Bereich der außerbetrieblichen Einkünfte - wie im beschwerdegegenständlichen Verfahren  -  waren die Verlustverwertungsbeschränkungen bei sonstigen Einkünften sowie bei Einkünften  aus Vermietung und Verpachtung Gegenstand verfassungsgerichtlicher Entscheidungen.

**False Positives:**

- `Verpachtung Gegenstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_TRAIN/133530.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133530.1_68`)


II. Sachverhalt  II.1. Involvierte Firmen und Gewerbeberechtigungen  Die Bf. ist eine im Jahr 2007 errichtete und im österreichischen Firmenbuch eingetragene  Kapitalgesellschaft mit dem Sitz in der politischen Gemeinde Y; ihr Geschäftszweig ist das Bau-  bzw. Baumeistergewerbe.

**False Positives:**

- `Gewerbeberechtigungen  Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_TRAIN/133679.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133679.1_428`)


Im Unterschied dazu bestätigte die Stattgabe des Bundesverwaltungsgerichtes den  Werkvertrag aber betreffend der 5. gegenständlichen Person, der Expertin und Supervisorin Fr.  Expertin.

**False Positives:**

- `Supervisorin Fr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_TRAIN/133856.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133856.1_5`)


Danach seien die im bisherigen Hälftemiteigentum der ehemaligen Ehegatten stehenden  Wohnungseigentumsobjekte (Top 22, Top 23 in natura zur einstigen Ehewohnung verbunden  und Kfz Abstellplatz Nr. 2) derart aufgeteilt worden, dass die geschiedene Ehefrau nunmehr  „Alleineigentümerin“ der Top 23 und der geschiedene Ehemann (Beschwerdeführer)  „Alleineigentümer“ der Top 22 sowie des Kfz Stellplatzes geworden sei.

**False Positives:**

- `Kfz Abstellplatz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_TRAIN/133963.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133963.1_37`)


Im beschwerdegegenständlichen Zeitraum lag eine tatsächliche Wohn- und  Wirtschaftsgemeinschaft zwischen Ihnen und Ihren Kindern nicht vor.

**False Positives:**

- `Ihren Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TRAIN/134146.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134146.1_1`)


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
- `FA Österreich`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TRAIN/134157.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134157.1_38`)


Aus dieser Berechnungsgrundlage ergibt sich eindeutig, dass die in der Gewinn-  und Verlustrechnung der Beschwerdeführerin ausgewiesenen Provisionsaufwendungen in Höhe  von 7,5 % berechnet wurden und entspricht dies dem zwischen der Firma Nord Kraftzor AG und Firma Bf am  13.12.2002 abgeschlossenen Vertrag.

**False Positives:**

- `Firma Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nord Kraftzor AG`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134159.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Mit 20.01.2021 wurde der amtliche Befund über eine Verkürzung von Stempel- oder  Rechtsgebühren vom Verfassungsgerichtshof dem Finanzamt Österreich, Dienststelle für  Sonderzuständigkeiten, zur Anzeige gebracht.

**False Positives:**

- `Sachverhalt  Mit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TRAIN/134483.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134483.1_21`)


Rechtsbelehrung und Hinweise  Gegen Beschlüsse gemäß § 30a Abs. 3 VwGG ist eine Revision an den Verwaltungsgerichtshof  (§ 25a Abs. 2 Z 1 VwGG) oder Beschwerde an den Verfassungsgerichtshof (§ 88a Abs. 2 VfGG)  nicht zulässig.

**False Positives:**

- `Hinweise  Gegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Verfassungsgerichtshof`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TRAIN/134614.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134614.1_7`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TRAIN/134682.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134682.1_84`)


§ 6 Wiener Parkometergesetz 2006, LGBl. 71/2018, normiert:  Aus Gründen der Verwaltungsvereinfachung und der Vereinheitlichung kann die Gemeinde  durch Verordnung Pauschalierungsrichtlinien festlegen, die die Höhe und die Form der Ab- gabenentrichtung regeln und auf das unterschiedliche Abstellverhalten der Wohnbevölkerung  in Gebieten, die gemäß § 43 Abs. 2a StVO 1960, BGBl. Nr. 159/1960, in der Fassung des  Bundes¬gesetzes BGBl. I Nr. 99/2005, verordnet sind, des Wirtschaftsverkehrs und des  sonstigen Verkehrs Bedacht nehmen.

**False Positives:**

- `Verordnung Pauschalierungsrichtlinien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_TRAIN/134746.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134746.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Mona Jakubschak, Paukengraben 9, 9620 Obervellach, Österreich  und Wigand Venhuis, LLB BEd, Johann-Paur-Straße 24, 8483 Krobathen, Österreich  über die Beschwerde vom 25. Jänner 2021 gegen den  Grundsteuerbescheid des Magistrates der Stadt Wien, MA 6, vom 1. Jänner 2021 betreffend  Liegenschaft Wien BezirkAdresse, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wigand Venhuis` — partial — pred is substring of gold: `Wigand Venhuis, LLB BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mona Jakubschak`(person)
- `Paukengraben 9, 9620 Obervellach, Österreich`(address)
- `Wigand Venhuis, LLB BEd`(person)
- `Johann-Paur-Straße 24, 8483 Krobathen, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_TRAIN/134907.1`) (sent_id: `deanon_BFG_20260814_TRAIN/134907.1_44`)


Im Dezember 2020 und im März 2021 wurden vom Bundesamt für Soziales und  Behindertenwesen Sozialministeriumservice Sachverständigengutachten erstellt.  3 von 11 Seite 4 von 11

**False Positives:**

- `Behindertenwesen Sozialministeriumservice` — positional overlap with gold: `Bundesamt für Soziales und  Behindertenwesen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesamt für Soziales und  Behindertenwesen`(organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Suleika Fuljahn, Kohlschwarz 113, 9772 Holztratten, Österreich, vertreten durch Dr Ralph Mayer, Invalidenstraße 1, 1030 Wien,  über die Beschwerde vom 12. Februar 2015 gegen die Bescheide des Finanzamtes Österreich  (damals Finanzamt Wien 2/20/21/22) vom 12. Jänner 2015 betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 2010 bis 2013 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr Ralph` — partial — pred is substring of gold: `Dr Ralph Mayer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Suleika Fuljahn`(person)
- `Kohlschwarz 113, 9772 Holztratten, Österreich`(address)
- `Dr Ralph Mayer`(person)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TRAIN/135289.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135289.1_60`)


Tz.3 Vorsteuerkürzung:  Im Prüfungszeitraum seien für die Anschaffung sämtlicher PKW´s sowie für die damit in  Zusammenhang stehenden Aufwendungen wie Treibstoff und Reparatur Vorsteuern geltend  gemacht worden.

**False Positives:**

- `Reparatur Vorsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_TRAIN/135337.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135337.1_20`)


Die Erstausstattungsbox enthält:  - die ausgewählten Kontaktlinsen  - einen Kontaktlinsenbehälter  - eine AGB-Broschüre  - Broschüre Handhabung und Pflege Kontaktlinsen  - eine Ausfertigung der unterschriebenen Vertragsunterlagen betreffend den weiteren Bezug  von Kontaktlinsen (Tages- und Monatslinsen) sowie Pflegemitteln.

**False Positives:**

- `Pflege Kontaktlinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_TRAIN/135600.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135600.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Der Beschwerdeführer (in der Folge: Bf.) war im Jahr 2018 als Grenzgänger in einer Weberei in  der Schweiz unselbständig beschäftigt.

**False Positives:**

- `Sachverhalt  Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_TRAIN/135661.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135661.1_12`)


…  Da der Mittelpunkt Ihrer Lebensinteressen aufgrund Ihres Familienwohnsitzes in Österreich  liegt, war aufgrund der Standortvermutung davon auszugehen, dass das ggst Kfz seinen  dauernden Standort in Österreich hat und daher nach dem Kraftfahrgesetz zuzulassen wäre.

**False Positives:**

- `Ihres Familienwohnsitzes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_TRAIN/135915.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135915.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ronald Morosow, Schlumbergerstraße 26, 9072 Franzendorf, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die Beschwerde  vom 7. April 2021 gegen die Bescheide des Finanzamtes Österreich vom 24. März 2021,  Steuernummer 41-331/9010, betreffend Abweisung des Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2016, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hertwich  Steuerberatungsgesellschaft` — partial — pred is substring of gold: `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag.Dr. Ingrid Fehrer`(person)
- `Ronald Morosow`(person)
- `Schlumbergerstraße 26, 9072 Franzendorf, Österreich`(address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `41-331/9010`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_TRAIN/135915.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135915.1_42`)


(….)  Erwägungen  Zum Wiederaufnahmegrund  Den Wiederaufnahmegrund bestimmt bei der Wiederaufnahme auf Antrag die betroffene  Partei.

**False Positives:**

- `Den Wiederaufnahmegrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_TRAIN/135955.1`) (sent_id: `deanon_BFG_20260814_TRAIN/135955.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_TRAIN/136132.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136132.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_TRAIN/136147.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136147.1_9`)


Die Streitthemen waren insbesondere gewerblicher  Grundstückhandel und daraus erzielte Schwarzerlöse (2001 – 2005) sowie Erlösschätzung  durch Anwendung eines progressiv ansteigenden Sicherheitszuschlages von 2001 bis 2008  (siehe BP-Bericht vom 3.12.2010, Tz. 5 sowie Berichtsbeilage Seite 42 bis 45).

**False Positives:**

- `Berichtsbeilage Seite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_TRAIN/136517.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136517.1_88`)


[Anm.: Geburtsdatum]   4.14 Termin der nächsten Kontrolle  [blank]   Das in der Folge erstellte Gutachten vom 4. Mai 2021 des Bundesamtes für Soziales und  Behindertenwesen, BASB Landesstelle NÖ trifft folgende Aussagen:   Sachverständigengutachten auf Grund der Aktenlage   nach der Einschätzungsverordnung (BGBl. II Nr. 261/2010)   Name: (Sohn des Bf.) … Geburtsdatum: …11.2005, wohnhaft in … Ungarn   Aktengutachten erstellt am: 04.05.2021   Name des Sachverständigen: Dr. G.H.   Fachgebiet: Allgemeinmedizin und Augenheilkunde   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Formular E407, gezeichnet von Dr.B.E.T. in Papa (Ungarn) am 17.3.2021:   15 Jahre, 4 Monate   85 kg, 187 cm   vollständige Selbständigkeit, keine Hilfestellungen erforderlich   Sehbehinderung ab 11/2005   Behandlung ab 06/2006   keine anderen Behinderungen   TH: Implantat für künstliche Linsen 31.9.2006;

**False Positives:**

- `Augenheilkunde   Zusammenfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamtes für Soziales und  Behindertenwesen`(organisation)
- `Dr. G.H.`(person)

**Example 69** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_38`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Bezüglich des Sohnes der Bf. sind folgende Befunde und Maßnahmen aktenkundig:   Testung am 11. Juni 2017 [Sohn der Bf. 3-jährig] durch die Klinische und  Gesundheitspsychologin und Wahlpsychologin Mag. M.:   Es zeigten sich klare Hinweise auf eine mögliche AHDS, wenn auch diese in diesem jungen Alter  noch nicht diagnostiziert wurde.

**False Positives:**

- `Wahlpsychologin Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)

**Example 70** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_47`)


Testung am 06. August 2019 [Sohn der Bf. 5 Jahre] durch die Klinische und  Gesundheitspsychologin und Wahlpsychologin Mag. M.:   Die Testung zeigte abermals die deutlichen AHDS-Symptomatiken und ließ zusätzlich eine  Zugehörigkeit zum Autismusspektrum vermuten.

**False Positives:**

- `Wahlpsychologin Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 71** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_52`)


Am 20. September 2019 empfahl die o.a. Klinische und Gesundheitspsychologin und  Wahlpsychologin Mag. M., um für den Sohn der Bf. eine gute Ausgangsposition für den  Schulanfang zu gestalten, dringend eine weitere medizinische Abklärung bezgl.

**False Positives:**

- `Wahlpsychologin Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 72** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_57`)


Begutachtung Bundesamt für Soziales und Behindertenwesen Sozialministeriumservice   Aktengutachten erstellt am 12. April 2021:   Fachgebiet der Sachverständigen: Kinder- und Jugendheilkunde   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   2021-03-12 Amanda Guichard  Kinder-und Jugendpsychiatrie, Hinterbrühl, Kurzarztbrief nach Aufenthalt  in der kooperativen Tagesklinik vom 20.10.20 bis 29.01.2021, Diagnosen:   einfache Aktivitäts- und Aufmerksamkeitsstörung mit Förderbedürfnissen in der sozialen  Interaktion, Förderbedarf in Bezug auf sensorische Interaktion und die Motorikentwicklung  /fein und grob), logopädisch: phonetische Aussprachestörung in Form eines interdentalen  Sigmatismus sowie ein ad-/bzw. interdentales Schluckmuster, durchschnittliche Intelligenz,  keine chronischen oder akuten körperlichen Erkrankungen bekannt, mäßige soziale  Beeinträchtigung (Aufbau und Erhalt von Freundschaften, wiederholte Konflikte mit  Erwachsenen und Kindern, auch Konflikte mit Erwachsenen außerhalb der Familie, gehemmte  soziale Aktivität, wenig effektive Copingmechanismen.

**False Positives:**

- `Behindertenwesen Sozialministeriumservice` — positional overlap with gold: `Bundesamt für Soziales und Behindertenwesen`
- `Jugendheilkunde   Zusammenfassung` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesamt für Soziales und Behindertenwesen`(organisation)
- `Amanda Guichard`(person)

**Example 73** (doc_id: `deanon_BFG_20260814_TRAIN/136565.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136565.1_60`)


Nachuntersuchung:   NU in 3 Jahren zur Überprüfung der Beeinträchtigung   Begutachtung Bundesamt für Soziales und Behindertenwesen Sozialministeriumservice   Sachverständigengutachten (mit Untersuchung am 23. August 2021),   vidiert am 27. August 2021:   Fachgebiet des Sachverständigen: Kinder- und Jugendheilkunde   Anamnese:   Die Eltern haben gegen den Bescheid schriftlich Einspruch erhoben, da die rückwirkende  Geltendmachung des GdB mit 10/2020 festgelegt wurde, die Eltern jedoch den Beginn der  Symptomatik dtl.

**False Positives:**

- `Behindertenwesen Sozialministeriumservice` — positional overlap with gold: `Bundesamt für Soziales und Behindertenwesen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesamt für Soziales und Behindertenwesen`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_TRAIN/136860.1`) (sent_id: `deanon_BFG_20260814_TRAIN/136860.1_42`)


Und während in Lehre und Rechtsprechung Einigkeit darüber herrsche, dass ein Sprachkurs im  Allgemeinen nicht als Berufsausbildung iSd FLAG qualifiziert werden könne, müsse im  vorliegendem Fall dem besonderen Umstand Rechnung getragen werden, dass im Rahmen des  Bachelorstudiums „Sport-, Kultur- und Veranstaltungsmanagement an der FH Kufstein, das T.  im Wintersemester 2019/2020 aufgenommen und seitdem erfolgreich betreibe, ein  Auslandssemester in einem spanischsprachigen Land vorgesehen sei ( Verweis auf  https://www.fh-kufstein.ac.at/studieren/Bachelor/Sport-Kultur-Veranstaltungsmanagement- VZ).

**False Positives:**

- `Rechtsprechung Einigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FH Kufstein`(organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TRAIN/137038.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137038.1_38`)


Deswegen hier mit beantrage ich Herabsetzung der Strafen und Einen Raten Zahlung.

**False Positives:**

- `Einen Raten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_TRAIN/137083.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137083.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt   Die Beschwerdeführerin (Bf) beantragte in ihrer Erklärung zur Arbeitnehmerveranlagung 2018  die tatsächlichen Kosten unter dem Titel außergewöhnliche Belastungen (ag. B.) bei  Behinderung in Höhe von 767,74 (KZ 439).

**False Positives:**

- `Sachverhalt   Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_TRAIN/137101.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137101.1_62`)


Zur Indexierung/Anpassung von Unterhaltsabsetzbetrag und Familienbonus Plus an das  Preisniveau des Wohnortes des Kindes:  Mit dem Jahressteuergesetz 2018, BGBl. I 62/2018, ausgegeben am 14. August 2018, wurden  u.a. der Familienbonus Plus gemäß § 33 Abs. 3a EStG 1988 eingeführt und der Unterhalts- absetzbetrag gemäß § 33 Abs. 4 EStG (entsprechend dem Familienbonus Plus) indexiert, d.h.  auf das Preisniveau am Wohnort des Kindes außerhalb Österreichs und innerhalb  EU/EWR/Schweiz angepasst – jeweils ab der Veranlagung 2019 (§ 124b Z 335 EStG 1988).

**False Positives:**

- `Familienbonus Plus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_28`)


Unter beantragte Änderungen und Begründungen führte der BF aus:  „Anerkennung der Vorsteuern und Ausgaben It. Beilage als Betriebsausgaben.

**False Positives:**

- `Ausgaben It` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_51`)


Unter beantragte Änderungen und Begründungen führte der BF aus:  „Anerkennung der Vorsteuern und Ausgaben It. Beilage als Betriebsausgaben.

**False Positives:**

- `Ausgaben It` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_63`)


Unter beantragte Änderungen und Begründungen führte der BF aus:  „Anerkennung der Vorsteuern und Ausgaben It. Beilage als Betriebsausgaben.

**False Positives:**

- `Ausgaben It` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_TRAIN/137141.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137141.1_90`)


Bezüglich der Beschwerden betreffend die Einkommensteuer, Umsatzsteuer und  Festsetzungsbescheide Umsatzsteuer wurde begründend ausgeführt:  „In den Schriftsätzen vom 29.02.2016 wurde unter der Überschrift „Begründungen" auf die  Beilagen verwiesen.

**False Positives:**

- `Festsetzungsbescheide Umsatzsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_TRAIN/137360.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137360.1_59`)


Belehrung und Hinweise  Dem Antragsteller steht das Recht zu, innerhalb von sechs Wochen ab Zustellung dieser  Entscheidung eine Beschwerde an den Verfassungsgerichtshof (Freyung 8, 1010 Wien) zu  erheben.

**False Positives:**

- `Hinweise  Dem` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshof`(organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TRAIN/137494.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor in der Beschwerdesache  Yussuf Leuthäußer, Höhenstraße 51P, 8343 Waldsberg, Österreich, über die Beschwerde vom 16. August 2019 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend gemäß 8a FLAG  gekürzte Familienbeihilfe und Kinderabsetzbetrag Steuernummer 23-022/7005  zu Recht  erkannt:    Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Kinderabsetzbetrag Steuernummer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Doktor`(person)
- `Yussuf Leuthäußer`(person)
- `Höhenstraße 51P, 8343 Waldsberg, Österreich`(address)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)
- `23-022/7005`(tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_TRAIN/137494.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137494.1_4`)


Entscheidungsgründe  Sachverhalt und Verfahrensgang  Der Beschwerdeführer (Bf.) ist tschechischer Staatbürger und bezieht für sein im September  2014 geborenes Kind Familienbeihilfe und Kinderabsetzbetrag.

**False Positives:**

- `Verfahrensgang  Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_TRAIN/137558.1`) (sent_id: `deanon_BFG_20260814_TRAIN/137558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Othmar Oelhaf, In der Stockwiesen 24, 4730 Gewerbepark Süd, Österreich, vertreten durch Ilse Maria Bereuter-Hauser, Ofnerstraße 25, 2232 Deutsch-Wagram,  betreffend Beschwerde vom 6. März 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22, nunmehr Finanzamt Österreich, vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 03-656/5352  beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO i.V.m. § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Ilse Maria` — partial — pred is substring of gold: `Ilse Maria Bereuter-Hauser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Othmar Oelhaf`(person)
- `In der Stockwiesen 24, 4730 Gewerbepark Süd, Österreich`(address)
- `Ilse Maria Bereuter-Hauser`(person)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)
- `03-656/5352`(tax_number)

</details>

---

## `german_legal_person_special_titles` 

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
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 2016 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TRAIN/133044.1`) (sent_id: `deanon_BFG_20260814_TRAIN/133044.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache OMedR Dr. Jaden Brabandt, Herd 8i, 4141 Harrau, Österreich, vertreten durch Dr. Klaus Erich Schmidt, Hauptstraße 27, 8582 Rosental/Kainach,  betreffend die Beschwerde vom 25.02.2019 gegen den Bescheid des Finanzamtes Graz- Umgebung vom 31.01.2019 betreffend Umsatzsteuer 2016, Steuernummer 60-356/1910,  beschlossen:   Der Vorlageantrag wird zurückgewiesen.

**False Positives:**

- `Jaden Brabandt` — partial — pred is substring of gold: `OMedR Dr. Jaden Brabandt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OMedR Dr. Jaden Brabandt`(person)
- `Herd 8i, 4141 Harrau, Österreich`(address)
- `Dr. Klaus Erich Schmidt`(person)
- `Finanzamtes`(organisation)
- `60-356/1910`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_60`)


Die Antragstellerin habe das Gutachten des Univ.Prof.ÖkR Mag. Zoltan Marrziniak vom 20.4.2018 vorgelegt, wonach  eine primäre Leistungsreduktion bestehe, die die Wertigkeit einer geistigen Behinderung  erreiche.

**False Positives:**

- `Zoltan Marrziniak` — partial — pred is substring of gold: `Prof.ÖkR Mag. Zoltan Marrziniak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.ÖkR Mag. Zoltan Marrziniak`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_65`)


Beilage ./A Psychiatrisch Neurologisches Gutachten Univ.Prof.ÖkR Mag. Zoltan Marrziniak vom 20.4.2018  Beilage ./B Ärztliches Sachverständigengutachten Maurice Drübert vom 28.1.2004  Zeugeneinvernahme Herr X., Dorf (Onkel)  Beim Wiener Stadtschulrat angeforderte, noch vorzulegende Nachweise über den  Sonderschulbesuch.

**False Positives:**

- `Zoltan Marrziniak` — partial — pred is substring of gold: `Prof.ÖkR Mag. Zoltan Marrziniak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.ÖkR Mag. Zoltan Marrziniak`(person)
- `Maurice Drübert`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_72`)


…  Beilagen:  Psychiatrisch Neurologisches Gutachten Univ.Prof.ÖkR Mag. Zoltan Marrziniak vom 20.4.2018  Ärztliches Sachverständigengutachten Maurice Drübert vom 28.1.2004“

**False Positives:**

- `Zoltan Marrziniak` — partial — pred is substring of gold: `Prof.ÖkR Mag. Zoltan Marrziniak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.ÖkR Mag. Zoltan Marrziniak`(person)
- `Maurice Drübert`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TRAIN/146084.1`) (sent_id: `deanon_BFG_20260814_TRAIN/146084.1_73`)


Das psychiatrisch neurologische Gutachten von Univ.Prof.ÖkR Mag. Zoltan Marrziniak vom 25. Juli 2023 lautet:  „FRAGESTELLUNG  War seit der Geburt die vorhandene psychische Beeinträchtigung so stark ausgeprägt, dass  eine dauernde Erwerbsunfähigkeit bereits vor dem 21 Lebensjahr vorhanden war?

**False Positives:**

- `Zoltan Marrziniak` — partial — pred is substring of gold: `Prof.ÖkR Mag. Zoltan Marrziniak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.ÖkR Mag. Zoltan Marrziniak`(person)

</details>

---

## `german_legal_person_standalone` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4c7a5074`  
**Description:**
Captures standalone capitalized names (First Last) only when preceded by specific legal role indicators or conjunctions, with strict exclusion of headers and court names.

**Content:**
```
(?:^|\s|,|\()(?:Partei|Kl\u00e4ger|Beklagte|Vertreter|Anwalt|Zeuge|Gutachter|Sachverst\u00e4ndige|Vorsitzende|Vorsitzender|Mitglied|Mitglieder|durch|und|sowie)\s+([A-Z][a-z]+\s+[A-Z][a-z]+)(?:\s|,|\)|\.|$)(?!\s*(?:Gericht|Hof|Oberlandes|Landes|Spruch|Kopf|Der|Die|Dem|Den|Zivil|Straf|Handel|Sozial|Weg|Markt|Gruppe|GmbH|AG|Rechtsanw|Versand|Schaf|Zumtobel|Oberste|Landesgerichts|Bezirksgerichts|Zivilrechtssachen|Sozialrechtssachen|Urteilsver|Divitschek|Software|Unterlassung|Feststellung|Partei|Mag\.\s+Istjan|Tr\.\s+|Co\.\s+))
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

