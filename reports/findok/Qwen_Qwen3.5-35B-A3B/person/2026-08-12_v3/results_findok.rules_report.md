# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-12T19:16:10.635430

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-12_v3/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 0 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2518 |
| Validation documents | 630 |
| Test documents | 791 |
| Train sentences | 4655 |
| Validation sentences | 1352 |
| Test sentences | 90028 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 150 |
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
| Accuracy (exact match) | 98.8% |
| True Positives | 1250 |
| False Positives | 525 |
| False Negatives | 1062 |
| Total Gold Entities | 2312 |
| Micro Precision | 70.4% |
| Micro Recall | 54.1% |
| Micro F1 | 61.2% |
| Macro F1 | 61.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `context_person_beschwerdesache` | 28.1% | 83.7% | 16.9% | 466 | 390 | 76 |
| `context_person_academic_titles` | 45.8% | 70.3% | 33.9% | 1115 | 784 | 331 |
| `context_person_herr_combined` | 5.8% | 39.7% | 3.2% | 184 | 73 | 111 |
| `context_person_initials` | 0.3% | 30.0% | 0.1% | 10 | 3 | 7 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `context_person_beschwerdesache` 🏆

**F1:** 0.281 | **Precision:** 0.837 | **Recall:** 0.169  

**Format:** `regex`  
**Rule ID:** `46de05d0`  
**Description:**
Matches person names specifically appearing after 'Beschwerdesache' (case of complaint), stopping at commas or addresses.

**Content:**
```
Beschwerdesache\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-\s+[A-Z][a-zäöüß]+)*(?:\s+LL\.M\.|\s+LL\.B\.|\s+M\.B\.L\.|\s+MBA\s*|\s+MSc\s*|\s+BSc\s*|\s+Bakk\.\s*iur\.|\s+Bakk\.\s*phil\.|\s+MAS\s*|\s+Bakk\.\s*techn\.)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.837 | 0.169 | 0.281 | 466 | 390 | 76 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 390 | 76 | 1920 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Immanuel Rommel, Dullach 99, 3214 Kreuztanne, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Immanuel Rommel` | `Immanuel Rommel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Dullach 99, 3214 Kreuztanne, Österreich` (address)
- `Monika Pfundner-Lenz` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/128660.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Roderich Heindke,  Zöchgasse 8, 9702 Glanz, Österreich, vertreten durch Stb, Adr_Stb, über die Beschwerde vom 31.07.2010 gegen die  Bescheide des Finanzamtes Kufstein Schwaz vom 5. Oktober 2005 betreffend  Einkommensteuer 2001 und 2002, sowie gegen den Bescheid vom 23. März 2006 betreffend  Einkommensteuer 2003  I. zu Recht erkannt:   Der Beschwerde gegen die Einkommensteuerbescheide 2001 und 2002 wird gemäß § 279 BAO  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Roderich Heindke` | `Roderich Heindke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zöchgasse 8, 9702 Glanz, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/128731.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128731.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Matthew Schiwietz, Haushamer Straße 93, 8283 Bad Blumau, Österreich, über die Beschwerde vom 17. Juli 2013 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 3. Juli 2013 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 Steuernummer zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Matthew Schiwietz` | `Matthew Schiwietz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Haushamer Straße 93, 8283 Bad Blumau, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/128739.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128739.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri. in der Beschwerdesache Melanie Sickora, Leitzersdorfer Straße 10, 4312 Gerersdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am Steinbühel 27b, 4030 Linz, über die  Beschwerde vom 18. November 2013 gegen den Bescheid des Finanzamtes Linz vom  13. November 2013 betreffend Einkommensteuer 2011 und die Beschwerde vom 27. Jänner  2015 gegen den Bescheid vom 19. Jänner 2015 betreffend Einkommensteuer 2012 zu  Steuernummer 22-976/2769  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Sickora` | `Melanie Sickora` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leitzersdorfer Straße 10, 4312 Gerersdorf, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Linz` (organisation)
- `22-976/2769` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/128910.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128910.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gerald Liebig, Max-Fasching-Straße 20, 9361 Reisenberg, Österreich, über die Beschwerde vom 10. Juni 2016 gegen den Bescheid des FA vom 3. Juni 2016  betreffend Einkommensteuer 2014 Steuernummer 40-060/7697  zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Gerald Liebig` | `Gerald Liebig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Max-Fasching-Straße 20, 9361 Reisenberg, Österreich` (address)
- `40-060/7697` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/128975.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinDSW in der Beschwerdesache Veronika Appelius,  Schellgaden 146, 4853 Kaisigen, Österreich, vertreten durch Wijnkamp Advocatuur/Advokatur GmbH, Sirapuit 7, 6460  Imst, und Prodinger & Partner Wirtschaftstreuhand-Steuerberatungs GmbH & Co KG,  Prof.Ferry Porsche Straße 28, 5700 Zell am See, über die Beschwerde vom 7. Februar 2018  gegen den Bescheid des Finanzamtes St. Johann Tamsweg Zell am See vom 21. Dezember 2016  betreffend Umsatzsteuer 2006, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Veronika Appelius` | `Veronika Appelius` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schellgaden 146, 4853 Kaisigen, Österreich` (address)
- `Wijnkamp Advocatuur/Advokatur GmbH` (organisation)
- `Imst, und Prodinger & Partner Wirtschaftstreuhand-Steuerberatungs GmbH & Co KG` (organisation)
- `Finanzamtes St. Johann Tamsweg Zell` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Sandro Birnesser, Guglhof 6, 4906 Anhang, Österreich  vom 13. Januar 2020, vertreten durch Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG, Dr. Gaisbauerstr. 7, 4560 Kirchdorf an der Krems,  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 9. Dezember 2019 betreffend  Wiederaufnahme des Verfahrens gemäß § 303 BAO und Feststellung der Einkünfte gemäß  § 188 BAO für 2006, nach Durchführung einer mündlichen Verhandlung

| Predicted | Gold |
|---|---|
| `Sandro Birnesser` | `Sandro Birnesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Guglhof 6, 4906 Anhang, Österreich` (address)
- `Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG` (organisation)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260811_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Konstanze Schiffgens, Schüttmannweg 7, 4881 Innerlohen, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-396/0074  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Konstanze Schiffgens` | `Konstanze Schiffgens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Schüttmannweg 7, 4881 Innerlohen, Österreich` (address)
- `Mag. Achmed Ghazal Aswad` (person)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `69-396/0074` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260811_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Julia Fixl, Kleinreifling 48, 3521 Reichau, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Julia Fixl` | `Julia Fixl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Kleinreifling 48, 3521 Reichau, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260811_TRAIN/129136.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129136.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Vivian Bürklin, D.-Zeiner-Gasse 17, 4481 Asten, Österreich, über die Vorlageanträge vom 13.4.2020 gegen die Bescheide  (Beschwerdevorentscheidungen) des Finanzamtes Wien 4/5/10 vom 14. bzw 16.8.2019,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 bzw 2018 beschlossen:  I. Die Vorlageanträge werden gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vivian Bürklin` | `Vivian Bürklin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `D.-Zeiner-Gasse 17, 4481 Asten, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260811_TRAIN/129140.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Veronika Splettstösser, Geiter 10, 9531 Labientschach, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 83-370/4398  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Veronika Splettstösser` | `Veronika Splettstösser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Geiter 10, 9531 Labientschach, Österreich` (address)
- `Eva Maria Koller-Rohrschach` (person)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `83-370/4398` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260811_TRAIN/129188.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129188.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Gottfried Rybke, Sankt Magdalen 90, 4650 Kreisbichl, Österreich, betreffend Beschwerde vom 11. Juni 2016 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart vom 13. Mai 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 beschlossen:  Der Vorlageantrag vom 9.2.2020 wird gemäß § 278 Abs. 1 lit. a i.V.m. den §§ 260 Abs. 1 lit. b,  264 Abs. 4 lit. e und 264 Abs. 5 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Gottfried Rybke` | `Gottfried Rybke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sankt Magdalen 90, 4650 Kreisbichl, Österreich` (address)
- `Finanzamtes Bruck  Eisenstadt Oberwart` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260811_TRAIN/129205.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129205.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Wigand Berzing,  Unternberg 4, 4783 Rutzenberg, Österreich, über die Beschwerde vom 10. April 2019 gegen den Bescheid über den Antrag  vom 06.03.2019 auf Mehrkindzuschlag für 2019 aufgrund der Verhältnisse des Jahres 2018  des  Finanzamtes vom 1. April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wigand Berzing` | `Wigand Berzing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unternberg 4, 4783 Rutzenberg, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260811_TRAIN/129218.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129218.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi.in in der Beschwerdesache Lewis Odemar,  Doka-Straße 16A, 6095 Grinzens, Österreich, Ungarn, über die Beschwerde vom 25.11.2019 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 11.11.2019 betreffend Wiederaufnahme des  Einkommensteuerbescheides für das Jahr 2015 zu Recht erkannt:  Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Lewis Odemar` | `Lewis Odemar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Doka-Straße 16A, 6095 Grinzens, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260811_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Guntram Reuttner, Gewerbezone, Technikstraße 28V, 7561 Heiligenkreuz im Lafnitztal, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Guntram Reuttner` | `Guntram Reuttner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Elisabeth Traxler` (person)
- `Gewerbezone, Technikstraße 28V, 7561 Heiligenkreuz im Lafnitztal, Österreich` (address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260811_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Vivian Imai, Übermoos 13, 9361 Moserwinkl, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Vivian Imai` | `Vivian Imai` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Mag. Susanne Haim` (person)
- `Leopold Pichlbauer` (person)
- `Dr.  Karl Penninger` (person)
- `Übermoos 13, 9361 Moserwinkl, Österreich` (address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH` (organisation)
- `Finanzamtes` (organisation)
- `Tanja Grottenthaler` (person)

**Example 16** (doc_id: `deanon_BFG_20260811_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Gloria Chmielarczyk, Bärenweg 17, 2113 Großrußbach, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gloria Chmielarczyk` | `Gloria Chmielarczyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Thomas Leitner` (person)
- `Bärenweg 17, 2113 Großrußbach, Österreich` (address)
- `Grant Thornton Austria GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260811_TRAIN/129404.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Dominika Gerstmeir, Dultstraße 13, 9155 Schwabegg, Österreich, über die Beschwerde vom 27. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 23. Jänner 2020 betreffend Rückforderung von  Familienbeihilfe und Kinderabsetzbeträgen für das Kind x im Zeitraum vom 01.07.2018 bis zum  30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dominika Gerstmeir` | `Dominika Gerstmeir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dultstraße 13, 9155 Schwabegg, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260811_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Linn Rolfink  in der Beschwerdesache Sascha Mertesacker,  Bahnhof Donauuferbahn 33, 9345 Lassenberg, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sascha Mertesacker` | `Sascha Mertesacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Linn Rolfink` (person)
- `Bahnhof Donauuferbahn 33, 9345 Lassenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260811_TRAIN/129432.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Hemma Najok, Hanningweg 1, 4154 Haselbach, Österreich, über die Beschwerde vom 14. Mai 2014 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 13. Mai 2014 betreffend Einkommensteuer 2012 Steuernummer  86-325/6230  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hemma Najok` | `Hemma Najok` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hanningweg 1, 4154 Haselbach, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `86-325/6230` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260811_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Timon Wanitschek, Dr.-Herrmann-Gasse 212, 4142 Mühlholz, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Timon Wanitschek` | `Timon Wanitschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr.-Herrmann-Gasse 212, 4142 Mühlholz, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260811_TRAIN/129773.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Kerstin Westfal, Klockerweg 6, 8242 Sankt Lorenzen am Wechsel, Österreich, über die Beschwerde vom 24. Oktober 2019  gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 10. Oktober 2019  betreffend Abweisung des Antrags auf Familienbeihilfe für den Zeitraum März 2019 bis Mai  2019 sowie ab September 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kerstin Westfal` | `Kerstin Westfal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Klockerweg 6, 8242 Sankt Lorenzen am Wechsel, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260811_TRAIN/129828.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Marianne Klössel, Riesberg 6, 4131 Wölfling, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 90-987/4178  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Marianne Klössel` | `Marianne Klössel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Riesberg 6, 4131 Wölfling, Österreich` (address)
- `Dr. Helmut Herbert Moritz` (person)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `90-987/4178` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260811_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129861.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Larissa Klinkers  in der Beschwerdesache Karim Keizer,  Oberbieler Platz 18, 4362 Kollroßdorf, Österreich  vertreten durch RA MMag. Dr. Alexander Lamplmayr als gerichtlicher  Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der  beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der  Entscheidungspflicht durch das FA Wien 1/23  betreffend die Anträge vom 3.5.2018 auf Zustellung  des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte  Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge  wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung,  Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung  bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum  unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung  hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe  von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen:  a)

| Predicted | Gold |
|---|---|
| `Karim Keizer` | `Karim Keizer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Larissa Klinkers` (person)
- `Oberbieler Platz 18, 4362 Kollroßdorf, Österreich` (address)
- `RA MMag. Dr. Alexander Lamplmayr` (person)
- `FA Wien 1/23` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260811_TRAIN/129907.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Jeremias Petratzek in der Beschwerdesache Hartwig Wintjens,  Franz Josef-Promenade 17, 3170 Ob der Kirche, Österreich, über die Beschwerde vom 20. Februar 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 30. Jänner 2015 betreffend Einkommensteuer 2013  Steuernummer 28-204/7043  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hartwig Wintjens` | `Hartwig Wintjens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Petratzek` (person)
- `Franz Josef-Promenade 17, 3170 Ob der Kirche, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `28-204/7043` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260811_TRAIN/129934.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129934.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Aloisa Aust, Zauch 35, 8261 Wetzawinkel, Österreich, vertreten durch Vertreter über die Beschwerde vom 16. November 2012 gegen die  Bescheide des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2012 betreffend Umsatzsteuer  2009 und 2010, sowie Einkommensteuer 2009 und 2010 Steuernummer 04-495/8889  nach  Durchführung einer mündlichen Verhandlung am 23. September 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Aloisa Aust` | `Aloisa Aust` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zauch 35, 8261 Wetzawinkel, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `04-495/8889` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260811_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Erwin Nehse, Greimelweg 11, 4224 Klausmühle, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

| Predicted | Gold |
|---|---|
| `Erwin Nehse` | `Erwin Nehse` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Greimelweg 11, 4224 Klausmühle, Österreich` (address)
- `LMG  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260811_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Beutell, Axerried 14, 8583 Modriach, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Daisy Beutell` | `Daisy Beutell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Axerried 14, 8583 Modriach, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260811_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hugo Voelp, Weißes Kreuz-Gasse 10f, 8967 Birnberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hugo Voelp` | `Hugo Voelp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Weißes Kreuz-Gasse 10f, 8967 Birnberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260811_TRAIN/130274.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130274.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Georg Glockmann  vertreten durch  Gf. über die Beschwerde vom 16. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 16. Dezember 2019, Steuernummer 91-872/5407, betreffend Feststellung der  Einkünfte gem. § 188 BAO für das Jahr 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Georg Glockmann` | `Georg Glockmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien  4/5/10` (organisation)
- `91-872/5407` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260811_TRAIN/130324.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Susette Keufel, Tresdorf 32, 4842 Ketzerhub, Österreich, über die Beschwerde vom 29. Jänner 2020 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. Jänner 2020 betreffend Rückforderung für Herbert Kreller  für den  Zeitraum März 2018 bis Jänner 2019 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Keufel` | `Susette Keufel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tresdorf 32, 4842 Ketzerhub, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)
- `Herbert Kreller` (person)

**Example 31** (doc_id: `deanon_BFG_20260811_TRAIN/130332.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Igor Pölemann, Heugschwend 10, 3341 Haselgraben, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Igor Pölemann` | `Igor Pölemann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Heugschwend 10, 3341 Haselgraben, Österreich` (address)
- `Sigrid Lamböck` (person)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260811_TRAIN/130367.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Paulina Kovalev, Franz-Wagner-Weg 50, 8130 Pfannberg, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Paulina Kovalev` | `Paulina Kovalev` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Franz-Wagner-Weg 50, 8130 Pfannberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Penelope Veitt, Isengaustraße 12, 3623 Dankholz, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Penelope Veitt` | `Penelope Veitt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Isengaustraße 12, 3623 Dankholz, Österreich` (address)
- `Mag. Margot Artner` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260811_TRAIN/130424.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache Sophie Agahd, Kumpfhub 189, 8510 Neudorf bei Stainz, Österreich  vertreten durch Vertreter, gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 24. November 2015, betreffend Grunderwerbsteuer  aufgrund des Übergabsvertrages mit N.N. (Erf. Nr., Steuernummer), zu Recht erkannt:   Der eingeschränkten Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sophie Agahd` | `Sophie Agahd` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kumpfhub 189, 8510 Neudorf bei Stainz, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260811_TRAIN/130437.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Sheila Potocsnik, Am Turmstein 9G, 4675 Stüblreith, Österreich, über die Beschwerde vom 29. Mai 2019 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 30. April 2019 betreffend Rückforderung der  für VN-Sohn NN für den Zeitraum Jänner 2018 bis Dezember 2018 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sheila Potocsnik` | `Sheila Potocsnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Monika Kofler` (person)
- `Am Turmstein 9G, 4675 Stüblreith, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260811_TRAIN/130442.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Renate Bausch, Kollmitzgraben 6, 4760 Bründl, Österreich, über die Beschwerden vom 27. November 2018 gegen die Bescheide des Finanzamtes  Baden Mödling vom 12. November 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017, Steuernummer , zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Renate Bausch` | `Renate Bausch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kollmitzgraben 6, 4760 Bründl, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260811_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Priv.-Doz.in Alexandra Eissler  in der Beschwerdesache Florian Langkop,  Schafweg 6, 3470 Engelmannsbrunn, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  93-292/7358, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Florian Langkop` | `Florian Langkop` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Priv.-Doz.in Alexandra Eissler` (person)
- `Schafweg 6, 3470 Engelmannsbrunn, Österreich` (address)
- `Mag. András Radics` (person)
- `Finanzamt Wien` (organisation)
- `93-292/7358` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260811_TRAIN/130676.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Yelec Wappenschmidt, Krokusgasse 210, 2022 Immendorf, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Yelec Wappenschmidt` | `Yelec Wappenschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Aigner` (person)
- `Krokusgasse 210, 2022 Immendorf, Österreich` (address)
- `Dr. Elke Hager` (person)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260811_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Eduard Schendzilarz  in der Beschwerdesache Jeffrey Simmeit,  Schrittwiesergasse 14, 8261 Nestelbach im Ilztal, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Linz  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jeffrey Simmeit` | `Jeffrey Simmeit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Univ.-Prof. Eduard Schendzilarz` (person)
- `Schrittwiesergasse 14, 8261 Nestelbach im Ilztal, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260811_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Claudia Husermann, Am Wagram 14, 4675 Untermeggenbach, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 38-175/7258  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Claudia Husermann` | `Claudia Husermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Am Wagram 14, 4675 Untermeggenbach, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `38-175/7258` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260811_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Stephanie Wandmaker, Huttererstraße 37, 5121 Fugging, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stephanie Wandmaker` | `Stephanie Wandmaker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Huttererstraße 37, 5121 Fugging, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260811_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Eleonore Adamy  in der Beschwerdesache Armin Rempel,  Fischauer Gasse 34S, 9132 Glantschach, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Armin Rempel` | `Armin Rempel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Eleonore Adamy` (person)
- `Fischauer Gasse 34S, 9132 Glantschach, Österreich` (address)
- `Anton Hörmann` (person)
- `Finanzamtes` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260811_TRAIN/130967.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130967.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Edeltraud Märtin, Schöpfstraße 46, 8423 Pichla bei Sankt Veit, Österreich, betreffend Beschwerde gegen die Bescheide des Finanzamtes Wien 4/5/10 vom  23. April 2018 betreffend Umsatzsteuer und Einkommensteuer 2016 Steuernummer  37-299/1236  beschlossen:   Der Vorlageantrag vom 21.7.2018 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264 Abs. 4  BAO und § 278 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Edeltraud Märtin` | `Edeltraud Märtin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schöpfstraße 46, 8423 Pichla bei Sankt Veit, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)
- `37-299/1236` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260811_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Peter Viehbacher, Hermann Hlinka Gasse 221, 8264 Hainersdorf, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Viehbacher` | `Peter Viehbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Stefan Pipal` (person)
- `Hermann Hlinka Gasse 221, 8264 Hainersdorf, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260811_TRAIN/131046.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Rosamunde Schmedecke, Damböckgasse 94, 8322 Fladnitz im Raabtal, Österreich, vertreten durch SCHIETZ + MAUREDER Steuerberatung GmbH,  Veldner Straße 29, 4120 Neufelden, über die Beschwerde vom 20. Juni 2017 gegen den  Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 9. Juni 2017 betreffend  Einkommensteuer 2015 Steuernummer 62-456/3911  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosamunde Schmedecke` | `Rosamunde Schmedecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Damböckgasse 94, 8322 Fladnitz im Raabtal, Österreich` (address)
- `SCHIETZ + MAUREDER Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `62-456/3911` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260811_TRAIN/131064.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Waltraud Strelzik, Karl-Hainzl-Straße 9, 5101 Bergheim, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 35-878/3699  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waltraud Strelzik` | `Waltraud Strelzik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Karl-Hainzl-Straße 9, 5101 Bergheim, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `35-878/3699` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260811_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131096.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ronja Geschwandner  in der Beschwerdesache Claire Stelmann,  Heinrichs bei Weitra 31, 6842 Koblach, Österreich, vertreten durch PKF CENTURION Wirtschaftsprüfungs- gesellschaft mbH,  Hegelgasse 8, 1010 Wien, über die Beschwerden gegen die Bescheide des Zollamtes Eisenstadt  Flughafen Wien   1) vom 7. Februar 2018, Zl: a, betreffend Festsetzung der Mineralölsteuer für Jänner 2010 mit €  195.809,84 und Festsetzung des Säumniszuschlages mit € 3.916,20;

| Predicted | Gold |
|---|---|
| `Claire Stelmann` | `Claire Stelmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Ronja Geschwandner` (person)
- `Heinrichs bei Weitra 31, 6842 Koblach, Österreich` (address)

**Example 48** (doc_id: `deanon_BFG_20260811_TRAIN/131270.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hedwig McClain  in der Beschwerdesache Benedikt Niedergesaess,  Hörbrunn 49, 4312 Hartl, Österreich, vertreten durch Dkfm. Erwin Baldauf und Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft,  Innsbrucker Straße 8, 6600 Reutte, über die Beschwerde vom 14. Oktober 2014 gegen die  Bescheide des Finanzamtes Landeck Reutte  1. vom 2. Oktober 2014 betreffend Festsetzung der Normverbrauchsabgabe für den       Zeitraum Dezember 2012 und   2. je vom 6. Oktober 2014 betreffend die Festsetzung von Kraftfahrzeugsteuer für       die Monate 10-12/2012, 01-12/2013 und 01-09/2014  zu Steuernummer 51-211/9456  zu Recht erkannt:     Der Beschwerde wird gemäß § 279 BAO insgesamt Folge gegeben.

| Predicted | Gold |
|---|---|
| `Benedikt Niedergesaess` | `Benedikt Niedergesaess` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Hedwig McClain` (person)
- `Hörbrunn 49, 4312 Hartl, Österreich` (address)
- `Erwin Baldauf` (person)
- `Mag. Reinhard Eberle  Wirtschaftstreuhandgesellschaft OG Steuerberatungs- und Wirtschaftsprüfungsgesellschaft` (organisation)
- `Finanzamtes Landeck Reutte` (organisation)
- `51-211/9456` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260811_TRAIN/131341.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131341.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Siegfried Meerwart, Hintereggele 17, 6341 Kaisertal, Österreich, betreffend Beschwerde vom 23. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 1/23 vom 3. Februar 2016 betreffend   Haftung zur Einbehaltung und Abfuhr der Lohnsteuer, Festsetzung des Dienstgeberbeitrages  (DB) und Festsetzung des Zuschlags zum Dienstgeberbeitrag (DZ) für die Kalenderjahre 2010 bis  2014 sowie Festsetzung von Säumniszuschlägen für Lohnsteuer 2010 bis 2014,  Steuernummer 53-091/0013  beschlossen:  Die Beschwerde wird als gegenstandslos erklärt und das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Siegfried Meerwart` | `Siegfried Meerwart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Hintereggele 17, 6341 Kaisertal, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `53-091/0013` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260811_TRAIN/131407.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Wladimir Zachary, KLG Leopoldau Ladestelle 200, 3613 Els, Österreich, über die Beschwerde vom 9. Oktober 2019  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 10. September 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 12-432/5286  zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wladimir Zachary` | `Wladimir Zachary` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `KLG Leopoldau Ladestelle 200, 3613 Els, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `12-432/5286` (tax_number)

**Example 51** (doc_id: `deanon_BFG_20260811_TRAIN/131483.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Zacharias Kschamer, Bahnhofparkweg 120, 3512 Baumgarten, Österreich, vertreten durch Intercura Teuhand Revisions  GmbH, Bösendorferstr.

| Predicted | Gold |
|---|---|
| `Zacharias Kschamer` | `Zacharias Kschamer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Bahnhofparkweg 120, 3512 Baumgarten, Österreich` (address)
- `Intercura Teuhand Revisions  GmbH` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260811_TRAIN/131522.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Hon.-Prof.in Geraldine Northmann  in der Beschwerdesache  Eugen Hafran, Kohlbach 11, 4673 Hörmeting, Österreich, über die Beschwerde vom 25. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 08. Mai 2020 betreffend Einkommensteuer 2019,  Steuernummer 78-431/6708, zu Recht erkannt:  I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Eugen Hafran` | `Eugen Hafran` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Geraldine Northmann` (person)
- `Kohlbach 11, 4673 Hörmeting, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)
- `78-431/6708` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260811_TRAIN/131581.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Burnus, Kalkstein 120, 8680 Edlach, Österreich, über die Beschwerde vom 27.8,2015 gegen den  Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser vom 28.

| Predicted | Gold |
|---|---|
| `Theodora Burnus` | `Theodora Burnus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Kalkstein 120, 8680 Edlach, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260811_TRAIN/131662.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131662.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Huberta Schlamb, Hochofengasse 2, 6373 Jochberg, Österreich, über die Beschwerde vom 20. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 16. Jänner 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, St.Nr. 04 198/9302, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Huberta Schlamb` | `Huberta Schlamb` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Hochofengasse 2, 6373 Jochberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260811_TRAIN/131687.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131687.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Elmira Blauhut, Oberaich 9, 9560 Wiggis, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft mbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 1. Februar 2017 gegen den Bescheid  des Finanzamtes Gänserndorf Mistelbach vom 12. Jänner 2017 betreffend Einkommensteuer  2015, Steuernummer 19-729/0389, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Elmira Blauhut` | `Elmira Blauhut` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberaich 9, 9560 Wiggis, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft mbH,` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `19-729/0389` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260811_TRAIN/131742.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131742.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Mag.a Mercedes Kröplin  in der Beschwerdesache Gertrude Nguyen, Farbstraße 5, 4274 Oberhofstetten, Österreich  vertreten durch KommR Benjamin Aydeniz, über die Beschwerde vom 4. Juni 2018 gegen den  Bescheid des FA Bruck Eisenstadt Oberwart  vom 26. März 2018 betreffend Einkommensteuer 2016, Steuernummer  67-326/8391, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gertrude Nguyen` | `Gertrude Nguyen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Mercedes Kröplin` (person)
- `Farbstraße 5, 4274 Oberhofstetten, Österreich` (address)
- `KommR Benjamin Aydeniz` (person)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `67-326/8391` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260811_TRAIN/131772.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131772.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Erika Wiesotzki, Hausruckstraße 14, 9346 Grai, Österreich, über die Beschwerde vom 15. Juni 2019 gegen den Bescheid des Finanzamtes  Österreich, vormals des Finanzamtes Salzburg-Land vom 16. Mai 2019 betreffend die  Wiederaufnahme des Verfahren gemäß § 303 Abs.1 BAO zur Einkommensteuer 2013 sowie die  Bescheide vom 17. Mai 2019 betreffend die Wiederaufnahme der Verfahren gemäß § 303  Abs.1 BAO zur Einkommensteuer 2014 und 2015 zu Steuernummer 72-560/7133  zu Recht  erkannt:   1.

| Predicted | Gold |
|---|---|
| `Erika Wiesotzki` | `Erika Wiesotzki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hausruckstraße 14, 9346 Grai, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `72-560/7133` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260811_TRAIN/131773.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Denise Kleine-Tebbe  in der Beschwerdesache Tamara Korthaase,  Ramesedt 15, 2013 Oberparschenbrunn, Österreich ,EU-Land, über die Beschwerde vom 19. Dezember 2017 gegen den  Abweisungsbescheid des Finanzamtes Bruck Leoben Mürzzuschlag vom 11. Dezember 2017  betreffend Ausgleichszahlung (Familienbeihilfe) für Kind1, geb. xx.xx..1994, Kind2, geb.  yy.yy..2002 und Kind3, geb. zz.zz..2000, je für den Zeitraum Jänner 2016 bis Dezember 2016 zu  Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Tamara Korthaase` | `Tamara Korthaase` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Denise Kleine-Tebbe` (person)
- `Ramesedt 15, 2013 Oberparschenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260811_TRAIN/131805.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131805.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Nikolaus Sedlmayr  in der Beschwerdesache Burkhard Kuschmerz,  Kreuzbrunnen 63, 2881 Lehen, Österreich, Deutschland, vertreten durch die Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H. über die Beschwerden gegen die Bescheide des  Finanzamtes Kufstein Schwaz betreffend Einkommensteuer 2017 und Umsatzsteuer 2017  jeweils vom 10. Jänner 2019 zu Recht erkannt:   I. Der Beschwerde gegen den Umsatzsteuerbescheid 2017 wird teilweise Folge  gegeben.

| Predicted | Gold |
|---|---|
| `Burkhard Kuschmerz` | `Burkhard Kuschmerz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Nikolaus Sedlmayr` (person)
- `Kreuzbrunnen 63, 2881 Lehen, Österreich` (address)
- `Wirtschaftstreuhand Kufstein  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260811_TRAIN/131880.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131880.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Ronald Schusterius, Gusswerkstraße 13, 3383 Grub, Österreich, über die Beschwerde vom 14. März 2018 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 21. Februar 2018 betreffend Einkommensteuer 2016,  Steuernummer 15-042/0290  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ronald Schusterius` | `Ronald Schusterius` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Gusswerkstraße 13, 3383 Grub, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `15-042/0290` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260811_TRAIN/131914.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Niklas Achtermeyer, Laubegasse 10, 9220 Rajach, Österreich, über die Beschwerde vom 28. Oktober 2019  gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 7. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Steuernummer 86-329/5811  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Niklas Achtermeyer` | `Niklas Achtermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Mandlmayr` (person)
- `Laubegasse 10, 9220 Rajach, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `86-329/5811` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260811_TRAIN/131969.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterD in der Beschwerdesache Gudrun Weisshäupl, Prälat Strobl-Gasse 4r, 3344 Kogelsbach, Österreich, über die Beschwerde vom 23. Mai 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 26. April 2019 betreffend Rückforderung Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum November 2017 bis April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gudrun Weisshäupl` | `Gudrun Weisshäupl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prälat Strobl-Gasse 4r, 3344 Kogelsbach, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260811_TRAIN/132000.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Clarissa Gebeler  in der Beschwerdesache Theodora Stancyk,  KLG Am Wolfersberg Gruppe 6, 4274 Kollnedt, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und Jugendhilfe,  Karl-Borromäus-Platz 3, 1030 Wien, über die Beschwerde vom 14. August 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 (nunmehr Finanzamtes Österreich ) vom 30. Juli  2020 betreffend Abweisung des Antrages auf Familienbeihilfe für 01/2016 bis 06/2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Theodora Stancyk` | `Theodora Stancyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Clarissa Gebeler` (person)
- `KLG Am Wolfersberg Gruppe 6, 4274 Kollnedt, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260811_TRAIN/132065.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Felix Gajowska, Urreitgasse 7, 8103 Kehr und Plesch, Österreich, gegen die Bescheide des Finanzamtes Wien 4/5/10 vom 21. Februar 2014 betreffend  die auf § 303 Abs. 1 BAO basierende Verfügung der Wiederaufnahme der Verfahren zur  Umsatzsteuer für das Jahr 2010 und zur Einkommensteuer für die Jahre 2010 und 2011 sowie  die auf § 205 Abs. 1 BAO basierende Festsetzung von Anspruchszinsen für die Jahre 2010 bis  2012 beschlossen:  Der Vorlageantrag vom 26.9.2014 wird - betreffend vorgenannter Bescheide - gemäß § 264  Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Felix Gajowska` | `Felix Gajowska` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urreitgasse 7, 8103 Kehr und Plesch, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260811_TRAIN/132165.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBVI in der Beschwerdesache Natascha Fiserova,  Obergäu 3, 9611 Emmersdorf, Österreich, über die Beschwerde vom 25. November 2019 gegen den Abweisungsbescheid  des Finanzamtes Österreich (bisher Finanzamt Salzburg-Land) vom 24. Oktober 2019  betreffend Zuerkennung der Familienbeihilfe für die Tochter To ab Juni 2019 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Natascha Fiserova` | `Natascha Fiserova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergäu 3, 9611 Emmersdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Salzburg-Land` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260811_TRAIN/132244.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132244.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Dragan Junkmanns, Ziegelsdorf 2, 4152 Kielesreith, Österreich, über die Beschwerde vom 6. Mai 2015 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 12. Februar 2016 betreffend Umsatzsteuer 2014 Steuernummer zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dragan Junkmanns` | `Dragan Junkmanns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ziegelsdorf 2, 4152 Kielesreith, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260811_TRAIN/132368.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Hannelore Vecek, Keimstraße 3, 5542 Höch, Österreich, vertreten durch Dr. Peter Eisele, Öffentlicher Notar, 7540 Güssing, Hauptplatz 1, über  die Beschwerde vom 18. Dezember 2017 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel vom 11. Dezember 2017 betreffend Rechtsgebühr,  Steuernummer 10- 42-605/1461, Erf.Nr. 10- 2017, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hannelore Vecek` | `Hannelore Vecek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Keimstraße 3, 5542 Höch, Österreich` (address)
- `Dr. Peter Eisele` (person)
- `Finanzamtes für Gebühren` (organisation)
- `42-605/1461` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260811_TRAIN/132403.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132403.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Olivia Gajdis, An der Schafwiese 36x, 8333 Grub I, Österreich, über die Beschwerde vom 7. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 10. Dezember 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 Steuernummer 85-596/4024  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Olivia Gajdis` | `Olivia Gajdis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `An der Schafwiese 36x, 8333 Grub I, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)
- `85-596/4024` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260811_TRAIN/132406.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ramon Diamantakis, Hochhäuserweg 15, 4792 Prackenberg, Österreich, über die Beschwerde vom 28. August 2019 gegen den Bescheid des Finanzamtes Bruck  Eisenstadt Oberwart, nunmehr Finanzamt Österreich, vom 29. Juli 2019 betreffend  Rückforderung zu Unrecht für die Kinder Wilhelmine Lukaschk, Annette Kasperzack  und Bernarda Kucner  für den  Zeitraum August 2014 bis April 2016 bezogener Beträge an Familienbeihilfe,  Kinderabsetzbetrag und Ausgleichszahlung gemäß Verordnung (EG) 833/2004 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ramon Diamantakis` | `Ramon Diamantakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hochhäuserweg 15, 4792 Prackenberg, Österreich` (address)
- `Finanzamtes Bruck  Eisenstadt Oberwart` (organisation)
- `Finanzamt Österreich` (organisation)
- `Wilhelmine Lukaschk` (person)
- `Annette Kasperzack` (person)
- `Bernarda Kucner` (person)

**Example 70** (doc_id: `deanon_BFG_20260811_TRAIN/132478.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132478.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Cedric Spilner, Schneiting 162, 9971 Kaltenhaus, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 9. März 2015 betreffend Einkommensteuervorauszahlungen 2015 zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Cedric Spilner` | `Cedric Spilner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Schneiting 162, 9971 Kaltenhaus, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260811_TRAIN/132486.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132486.1_2`)


Das Bundesfinanzgericht hat durch die Richterinri in der Beschwerdesache Brian Kraus, Siebenbürger Weg 73, 7474 Höll, Österreich, vertreten durch Thuller & Partner Wirtschaftstreuhand & Steuerberatungs GmbH,  Villacher Straße 83, 9020 Klagenfurt am Wörthersee,  über die Beschwerde vom 27. August 2018 gegen den Einkommensteuerbescheid für das Jahr  2017 des Finanzamtes Klagenfurt (nunmehr Finanzamt Österreich) vom 31. Juli 2018,  Steuernummer 40-663/8578, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Brian Kraus` | `Brian Kraus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siebenbürger Weg 73, 7474 Höll, Österreich` (address)
- `Thuller & Partner Wirtschaftstreuhand & Steuerberatungs GmbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `40-663/8578` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260811_TRAIN/132490.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132490.1_2`)


Das Bundesfinanzgericht hat durch die RichterinRi  in der Beschwerdesache Delia Broz, Mühlgassl 8, 7453 Dörfl, Österreich, vertreten durch Vertreter, Adr1,  über die Beschwerde vom 22. März 2019 gegen den Bescheid des (damaligen) A vom  26. Februar 2019, mittels welchem der Antrag auf Festsetzung der Stabilitätsabgabe gemäß §  201 BAO zum 31.01.2019 abgewiesen wurde,  Steuernummer , zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Delia Broz` | `Delia Broz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mühlgassl 8, 7453 Dörfl, Österreich` (address)

**Example 73** (doc_id: `deanon_BFG_20260811_TRAIN/132501.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Finn Bartholmeh, Kleindurlas 88, 4730 Unterviehbach, Österreich, über die Beschwerde vom 18. Februar 2021 gegen den Bescheid  des Finanzamtes Österreich vom 20. Jänner 2021 betreffend Einkommensteuer 2019, zu Recht  erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finn Bartholmeh` | `Finn Bartholmeh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Unger` (person)
- `Kleindurlas 88, 4730 Unterviehbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260811_TRAIN/132578.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132578.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Estelle Pussamsies, Altfinkensteiner Weg 3f, 3031 Rekawinkel, Österreich, über die Beschwerde vom 11.3.2020 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 6.3.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Estelle Pussamsies` | `Estelle Pussamsies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Altfinkensteiner Weg 3f, 3031 Rekawinkel, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260811_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Heike Zavadil,  Tonibachsteig 13, 4310 Haid, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH, Lehmanngasse 7, 1230 Wien, über die Beschwerde vom 23. Februar 2017 gegen den  Bescheid des Finanzamtes Gänserndorf Mistelbach vom 21. Dezember 2016 betreffend  Einkommensteuer 2014, Steuernummer 95-496/6112, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Heike Zavadil` | `Heike Zavadil` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tonibachsteig 13, 4310 Haid, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht Steuerberatungsgesellschaft  mbH` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `95-496/6112` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260811_TRAIN/132660.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132660.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Judith Sabolcec, Rifer Hauptstraße 81, 2301 Matzneusiedl, Österreich, über die Beschwerde vom 22.10.2019 gegen die Bescheide des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 3.10.2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und 2018, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Judith Sabolcec` | `Judith Sabolcec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Rifer Hauptstraße 81, 2301 Matzneusiedl, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Liu Hülsebusch, Schnackenbergweg 10u, 4722 Usting, Österreich, vertreten durch Dkfm. Freund & Partner Steuerberater GmbH, Schellinggasse 3, 1010  Wien, über die Beschwerde vom 29. Juli 2016 (Eingangsstempel 1. August 2016 ) gegen den  Umsatzsteuerbescheid 2011 und den Bescheid über die Feststellung von Einkünften gemäß  § 188 BAO 2011 des Finanzamtes Baden Mödling vom 5. Juli 2016, Steuernummer  16 39-547/9297, zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Liu Hülsebusch` | `Liu Hülsebusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schnackenbergweg 10u, 4722 Usting, Österreich` (address)
- `Freund & Partner Steuerberater GmbH` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `39-547/9297` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260811_TRAIN/132838.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132838.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Kimberly Wage, Pyhrabruck 25, 9560 Kraßnitz, Österreich, vertreten durch Dr. Eva Deutsch-Goldoni, Waldwiese 4, 2540 Bad  Vöslau, über die Beschwerde vom 12. September 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 22. August 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 37-754/8048  zu Recht erkannt:    I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kimberly Wage` | `Kimberly Wage` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Aigner` (person)
- `Pyhrabruck 25, 9560 Kraßnitz, Österreich` (address)
- `Dr. Eva Deutsch-Goldoni` (person)
- `Finanzamtes  Baden Mödling` (organisation)
- `37-754/8048` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260811_TRAIN/132870.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132870.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Chantal Birkmayer  vertreten  durch Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH, Faberstraße 20-22 Top F 20.21, 5020  Salzburg, über die Beschwerde vom 12. Dezember 2014 gegen den Bescheid des Finanzamtes  Salzburg-Land (nunmehr: Finanzamt Österreich) vom 11. Dezember 2014 betreffend  Körperschaftsteuer 2013, Steuernummer 67-149/8723, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Chantal Birkmayer` | `Chantal Birkmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Axel-Hans Werner Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-149/8723` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260811_TRAIN/132878.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Pamela Stolyarov, Am Roßstall 17, 6274 Distelberg, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 11. Mai 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Pamela Stolyarov` | `Pamela Stolyarov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Am Roßstall 17, 6274 Distelberg, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/128704.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Dr. Brian Ronghe  in der Beschwerdesache  Prof.  Mag. Burkhard Steußloff, Keltensteig 28, 3294 Neuhaus-Langau, Österreich, über die Beschwerde vom 23. September 2016 gegen den Bescheid  des Finanzamtes Linz vom 25. August 2016 betreffend Einkommensteuer 2014 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Brian Ronghe`(person)
- `Mag. Burkhard Steußloff`(person)
- `Keltensteig 28, 3294 Neuhaus-Langau, Österreich`(address)
- `Finanzamtes Linz`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/128709.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache René Wahls, Loreith 10, 3385 Friesing, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

**False Positives:**

- `Ren` — partial — pred is substring of gold: `René Wahls`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `René Wahls`(person)
- `Loreith 10, 3385 Friesing, Österreich`(address)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Nord Keltri, Hölzlhuberstraße 24t, 8413 Oberragnitz, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 60-519/7525  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Nord Keltri` — type mismatch — same span as gold: `Nord Keltri`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `Nord Keltri`(organisation)
- `Hölzlhuberstraße 24t, 8413 Oberragnitz, Österreich`(address)
- `Mag. Dieter Walla & Partner Steuerberater OG`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `60-519/7525`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/128788.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128788.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Mag. OSR Gabriele Elmhorst,  Weiler Haus 8, 4641 Steinhaus, Österreich, vertreten durch RA, Adr RA A, über die Beschwerde vom 25. April 2016 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 18. April 2016 betreffend  Familienbeihilfe für die Kinder 1 K, 2 K, 3 K und 4 K für die Monate August 2015 bis April 2016  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Gabriele Elmhorst`(person)
- `Weiler Haus 8, 4641 Steinhaus, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/128942.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128942.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache RgR Eduard Noelker, Thayablick 17, 4760 Kleinpireth, Österreich, vertreten durch Vertreter, Vertreter Adresse, über die Beschwerde vom 27. März 2014  gegen den Bescheid des Finanzamtes Graz-Stadt vom 24. Februar 2014 betreffend Aufhebung  des Bescheides über die Umsatzsteuer 2010, Steuernummer 53-324/0264, zu Recht  erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Eduard Noelker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RgR Eduard Noelker`(person)
- `Thayablick 17, 4760 Kleinpireth, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)
- `53-324/0264`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/128969.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Tristan Frickmann  in der Beschwerdesache Prof.in DDr.in Heike Birkenbeul,  In Gruben 55, 9862 Oberkremsberg, Österreich, betreffend Beschwerde vom 20. Februar 2018 gegen die Bescheide  des  Finanzamtes Gmunden Vöcklabruck vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 den Beschluss:  I. Die angefochtenen Bescheide vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 und die Beschwerdevorentscheidungen vom 28. März 2018  werden gemäß § 278 Abs 1 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde aufgehoben.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof.in DDr.in Heike Birkenbeul`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Tristan Frickmann`(person)
- `Prof.in DDr.in Heike Birkenbeul`(person)
- `In Gruben 55, 9862 Oberkremsberg, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Kordelia Wilkeit  in der Beschwerdesache Loglogwald-Sicherheit GmbH  Bernatzikgasse 11i, 3040 Schwertfegen, Österreich, vertreten durch zobl.bauer.

**False Positives:**

- `Loglogwald` — partial — pred is substring of gold: `Loglogwald-Sicherheit GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Kordelia Wilkeit`(person)
- `Loglogwald-Sicherheit GmbH`(organisation)
- `Bernatzikgasse 11i, 3040 Schwertfegen, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_20260811_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Li Fatih, Bakk. iur., Siegmar-Bergelt-Weg 38, 8793 Krumpen, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Li Fatih` — partial — pred is substring of gold: `Li Fatih, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Li Fatih, Bakk. iur.`(person)
- `Siegmar-Bergelt-Weg 38, 8793 Krumpen, Österreich`(address)
- `Mag. Walter Dienstl & Partner  KG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  PhD Helena Jungkuhn, Grazer-Straße 111, 8322 Mitterfladnitz, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 53-953/1891  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

**False Positives:**

- `Ph` — partial — pred is substring of gold: `PhD Helena Jungkuhn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `PhD Helena Jungkuhn`(person)
- `Grazer-Straße 111, 8322 Mitterfladnitz, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `53-953/1891`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260811_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Xenia Griesinger  in der Beschwerdesache Valheimkel-Logistik,  Gürtelberg 9, 2135 Kottingneusiedl, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

**False Positives:**

- `Valheimkel` — partial — pred is substring of gold: `Valheimkel-Logistik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Xenia Griesinger`(person)
- `Valheimkel-Logistik`(organisation)
- `Gürtelberg 9, 2135 Kottingneusiedl, Österreich`(address)
- `Finanzamtes  Neunkirchen Wr. Neustadt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260811_TRAIN/130407.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Dagobert Waischnur, Bakk. iur., Jagdhütte Bärnkar 6, 6923 Lauterach, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

**False Positives:**

- `Dagobert Waischnur` — partial — pred is substring of gold: `Dagobert Waischnur, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Dagobert Waischnur, Bakk. iur.`(person)
- `Jagdhütte Bärnkar 6, 6923 Lauterach, Österreich`(address)
- `Harald Schmidt`(person)
- `Finanzamtes Spittal Villach`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260811_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Kaspar Schillings  in der Beschwerdesache Evelyn Wamßler, Bakk. rer. nat.,  Johann-Hanngasse 232, 8755 Möschitzgraben, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Evelyn Wamßler` — partial — pred is substring of gold: `Evelyn Wamßler, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Kaspar Schillings`(person)
- `Evelyn Wamßler, Bakk. rer. nat.`(person)
- `Johann-Hanngasse 232, 8755 Möschitzgraben, Österreich`(address)
- `Vedat Gökdemir`(person)
- `Finanzamtes`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260811_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  RgR Calvin Niepolt, Deichgasse 44B, 4925 Noxberg, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Calvin Niepolt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Unger`(person)
- `RgR Calvin Niepolt`(person)
- `Deichgasse 44B, 4925 Noxberg, Österreich`(address)
- `Astoria Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260811_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alexander Volkert  in der Beschwerdesache Bartholomäus El-Khalil, LLM,  Weg zum Hallenbad 23, 4533 Brandstatt, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Prof.in Finn Stechmüller  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bartholomäus El` — partial — pred is substring of gold: `Bartholomäus El-Khalil, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alexander Volkert`(person)
- `Bartholomäus El-Khalil, LLM`(person)
- `Weg zum Hallenbad 23, 4533 Brandstatt, Österreich`(address)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `Prof.in Finn Stechmüller`(person)

**Example 14** (doc_id: `deanon_BFG_20260811_TRAIN/131299.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Bertha Jäcklin, LLM Bakk. art., Dedenitz 71, 5221 Reitsham, Österreich, über die Beschwerde vom 20. Juni 2013 gegen den Bescheid des  Finanzamtes Salzburg-Land vom 10. Juni 2013 betreffend Einkommensteuer 2011,  Steuernummer 61-491/3586  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bertha Jäcklin` — partial — pred is substring of gold: `Bertha Jäcklin, LLM Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Zwilling`(person)
- `Bertha Jäcklin, LLM Bakk. art.`(person)
- `Dedenitz 71, 5221 Reitsham, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `61-491/3586`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260811_TRAIN/131804.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131804.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Quentin Stirnagel, BEd, Fledermausgasse 119, 8046 Mühl, Österreich, über die Beschwerde  vom 12. Jänner 2017 gegen den Bescheid des Finanzamtes  Österreich vom 16. Dezember 2016 betreffend  Rückforderung von Familienbeihilfe und  Kinderabsetzbeträge (Zeitraum Februar 2014 bis September 2016) zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO wird insofern teilweise Folge gegeben, als nur die für  den Zeitraum Juli 2014 bis September 2016 bezogenen Familienbeihilfen und  Kinderabsetzbeträge zurückgefordert werden.

**False Positives:**

- `Quentin Stirnagel` — partial — pred is substring of gold: `Quentin Stirnagel, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Quentin Stirnagel, BEd`(person)
- `Fledermausgasse 119, 8046 Mühl, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260811_TRAIN/132211.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf., Günther Gradisch Weg 45o, 3442 Asparn, Österreich, über die Beschwerde vom 27. Mai 2016 gegen den  Bescheid des Finanzamtes KirchdorfPerg Steyr vom 27. April 2016 betreffend  Kapitalertragsteuer 2012 und die Bescheide vom 3. Mai 2016 betreffend Körperschaftssteuer  2012, 2013 und 2014, Steuernummer 74-043/6141, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Günther Gradisch Weg 45o, 3442 Asparn, Österreich`(address)
- `Finanzamtes`(organisation)
- `74-043/6141`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260811_TRAIN/132303.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132303.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marion Wijers  in der Beschwerdesache RgR Erwin Ruzicka,  Ochsenmahd 15, 8612 Oberort, Österreich, gegen den Bescheid des Finanzamtes Kitzbühel Lienz vom 07. April 2020,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Rg` — partial — pred is substring of gold: `RgR Erwin Ruzicka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Marion Wijers`(person)
- `RgR Erwin Ruzicka`(person)
- `Ochsenmahd 15, 8612 Oberort, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260811_TRAIN/132743.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Prof. Julian Trapp, Gießgraben 22, 3754 Reichharts, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 20. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 und 2018 zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Julian Trapp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Prof. Julian Trapp`(person)
- `Gießgraben 22, 3754 Reichharts, Österreich`(address)
- `Finanzamtes Feldkirch`(organisation)
- `Finanzamt  Österreich`(organisation)

</details>

---

## `context_person_academic_titles` 🏆

**F1:** 0.458 | **Precision:** 0.703 | **Recall:** 0.339  

**Format:** `regex`  
**Rule ID:** `5c9d22cc`  
**Description:**
Matches person names preceded by academic titles (Mag., Dr., Ing., etc.) including compound titles, hyphenated names, and multiple suffixes like LL.M., MBA, MAS, Bakk., etc.

**Content:**
```
(?:Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?|Mag\.(?:a)?|Mag\.Dr\.|Dr\.(?:in)?|DDr\.(?:in)?|OStR|StR|OMedR|RA|KommR|KzlR|Techn\s+R|Ing\.|LR\d*|Ri\.|R\.|IBV|Maga\.|VetR|MedR|Dipl\.-Ing\.|Dipl\.Kfm\.|Dipl\.Ingenieur\.|Dipl\.Jur\.|Dipl\.Soz\.|Dipl\.Päd\.|Dipl\.Wirt\.Ing\.|Dipl\.Wirt\.Ingenieur\.|Dipl\.Wirtschaftsingenieur\.|Dipl\.Wirtschaftsingenieurin\.|Dipl\.Wirtschaftsingenieur\.|Dipl\.Wirtschaftsingenieurin\.|Dipl\.Wirtschaftsingenieur\.|Dipl\.Wirtschaftsingenieurin\.)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-\s+[A-Z][a-zäöüß]+)*(?:\s+LL\.M\.|\s+LL\.B\.|\s+M\.B\.L\.|\s+MBA\s*|\s+MSc\s*|\s+BSc\s*|\s+Bakk\.\s*iur\.|\s+Bakk\.\s*phil\.|\s+MAS\s*|\s+Bakk\.\s*techn\.|\s+Bakk\.\s*techn\.\s*|\s+LL\.M\.\s*|\s+LL\.B\.\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.703 | 0.339 | 0.458 | 1115 | 784 | 331 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 784 | 331 | 1528 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260811_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Mag. Hon.-Prof. Milan Siepje  in der Beschwerdesache Mag. Constantin Hanses, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Constantin Hanses` | `Mag. Constantin Hanses` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Hon.-Prof. Milan Siepje` (person)
- `Finanzamtes Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/128627.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Immanuel Rommel, Dullach 99, 3214 Kreuztanne, Österreich, vertreten durch Monika Pfundner-Lenz,  Neudorfergasse 1/72, 1210 Wien, über die Beschwerde vom 9.4.2014 gegen den Bescheid des  Magistrats der Stadt Wien, Magistratssabteilung 6, Rechnungs und Abgabewesen vom  19.3.2014, Abgabenkontonummer KtoNr***, betreffend Kommunalsteuer für die Jahre 2007  bis 2012  zu Recht erkannt:   I) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Immanuel Rommel` (person)
- `Dullach 99, 3214 Kreuztanne, Österreich` (address)
- `Monika Pfundner-Lenz` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/128678.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128678.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christoph Kordik in der Beschwerdesache  Hon.-Prof. Bruno Howaldt, Rußbachweg 3, 3040 Alt-Anzing, Österreich, über die Beschwerde vom 13.03.2015 gegen die Bescheide des  Finanzamtes Linz vom 17. Februar 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2009 und 2010 ,Steuernummer [...] ,zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christoph Kordik` | `Mag. Christoph Kordik` |
| `Hon.-Prof. Bruno Howaldt` | `Hon.-Prof. Bruno Howaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rußbachweg 3, 3040 Alt-Anzing, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/128704.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Dr. Brian Ronghe  in der Beschwerdesache  Prof.  Mag. Burkhard Steußloff, Keltensteig 28, 3294 Neuhaus-Langau, Österreich, über die Beschwerde vom 23. September 2016 gegen den Bescheid  des Finanzamtes Linz vom 25. August 2016 betreffend Einkommensteuer 2014 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Brian Ronghe` | `Dr. Brian Ronghe` |
| `Mag. Burkhard Steußloff` | `Mag. Burkhard Steußloff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Keltensteig 28, 3294 Neuhaus-Langau, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/128709.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128709.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache René Wahls, Loreith 10, 3385 Friesing, Österreich, betreffend den Vorlageantrag vom 1.12.2016  gegen die Beschwerdevorentscheidung des Finanzamtes Waldviertel vom 24.10.2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, Steuernummer , beschlossen:   Der Vorlageantrag wird gemäß § 260 Abs. 1 BAO iVm § 264 BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `René Wahls` (person)
- `Loreith 10, 3385 Friesing, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/128731.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128731.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Matthew Schiwietz, Haushamer Straße 93, 8283 Bad Blumau, Österreich, über die Beschwerde vom 17. Juli 2013 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 3. Juli 2013 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 Steuernummer zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Matthew Schiwietz` (person)
- `Haushamer Straße 93, 8283 Bad Blumau, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/128850.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128850.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Desiree Pierrot  in der Beschwerdesache des  Waltraud Odernheimer, Kalgasse 3, 4070 Seebach, Österreich, über die Beschwerde vom 26. August 2015 gegen den  Haftungsbescheid des FA Innsbruck  vom 3. August 2016 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Desiree Pierrot` | `Priv.-Doz.in Desiree Pierrot` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waltraud Odernheimer` (person)
- `Kalgasse 3, 4070 Seebach, Österreich` (address)
- `FA Innsbruck` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260811_TRAIN/128894.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128894.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Babette Ostenrieder  in der Beschwerdesache der  Hugo Rampeltshammer, Sebastianikreuzweg 7, 4150 Hauzenberg, Österreich, über die Beschwerde vom 5. Juni 2019, beim zuständigen  Finanzamt eingelangt am 6. Juni 2019, gegen den Bescheid des Finanzamt Landeck Reutte  vom 24. Mai 2019  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 (Steuernummer  29-044/7749 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO im Umfang der Beschwerdevorentscheidung vom  3.September 2019 Folge gegeben;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Babette Ostenrieder` | `Priv.-Doz.in Babette Ostenrieder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hugo Rampeltshammer` (organisation)
- `Sebastianikreuzweg 7, 4150 Hauzenberg, Österreich` (address)
- `Finanzamt Landeck Reutte` (organisation)
- `29-044/7749` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260811_TRAIN/128969.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Tristan Frickmann  in der Beschwerdesache Prof.in DDr.in Heike Birkenbeul,  In Gruben 55, 9862 Oberkremsberg, Österreich, betreffend Beschwerde vom 20. Februar 2018 gegen die Bescheide  des  Finanzamtes Gmunden Vöcklabruck vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 den Beschluss:  I. Die angefochtenen Bescheide vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 und die Beschwerdevorentscheidungen vom 28. März 2018  werden gemäß § 278 Abs 1 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Tristan Frickmann` | `Priv.-Doz. Tristan Frickmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in DDr.in Heike Birkenbeul` (person)
- `In Gruben 55, 9862 Oberkremsberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260811_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Sandro Birnesser, Guglhof 6, 4906 Anhang, Österreich  vom 13. Januar 2020, vertreten durch Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG, Dr. Gaisbauerstr. 7, 4560 Kirchdorf an der Krems,  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 9. Dezember 2019 betreffend  Wiederaufnahme des Verfahrens gemäß § 303 BAO und Feststellung der Einkünfte gemäß  § 188 BAO für 2006, nach Durchführung einer mündlichen Verhandlung

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandro Birnesser` (person)
- `Guglhof 6, 4906 Anhang, Österreich` (address)
- `Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG` (organisation)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260811_TRAIN/129068.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129068.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Konstanze Schiffgens, Schüttmannweg 7, 4881 Innerlohen, Österreich, vertreten durch Mag. Achmed Ghazal Aswad, Heinrichstraße 22,  8010 Graz, und Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom 26. März 2018 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 2. März 2018 betreffend Aussetzungszinsen  2018 Steuernummer 69-396/0074  uRecht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |
| `Mag. Achmed Ghazal Aswad` | `Mag. Achmed Ghazal Aswad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Konstanze Schiffgens` (person)
- `Schüttmannweg 7, 4881 Innerlohen, Österreich` (address)
- `Rabel & Partner GmbH Wirtschafts- prüfungs- und Steuerberatungsge-  sellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `69-396/0074` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260811_TRAIN/129077.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  Julia Fixl, Kleinreifling 48, 3521 Reichau, Österreich, vertreten durch Mercuria Wirtschaftstreuhand GmbH,  Klagbaumgasse 8, 1040 Wien, über die Beschwerde vom 21. August 2014 gegen die Bescheide  des Finanzamtes Wien 9/18/19 Klosterneuburg vom 16. Juli 2014, betreffend Haftung für  Lohnsteuer sowie Festsetzung von Dienstgeberbeiträgen, jeweils für die Jahre 2010 bis 2012,  zu Recht erkannt:     I. Der Beschwerde wird Folge gegeben:  Die angefochtenen Haftungsbescheide betreffend Lohnsteuer für 2010 bis 2012 werden gemäß  § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julia Fixl` (person)
- `Kleinreifling 48, 3521 Reichau, Österreich` (address)
- `Mercuria Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260811_TRAIN/129086.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Dr.in Lieselotte Bourgois  in der Beschwerdesache OSR Veit Fechler,  Drösingerstraße 59, 3170 Vollberg, Österreich, über die Beschwerde vom 3. April 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 25. März 2019, betreffend Einkommensteuer für  das Jahr 2018 (Arbeitnehmerveranlagung) zu Recht erkannt:    Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Lieselotte Bourgois` | `Dr.in Lieselotte Bourgois` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Veit Fechler` (person)
- `Drösingerstraße 59, 3170 Vollberg, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260811_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. James Albus  in der Beschwerdesache  OStR Fridolin Kumpan Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des FA Amstetten Melk Scheibbs  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. James Albus` | `Priv.-Doz. James Albus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Fridolin Kumpan` (person)
- `FA Amstetten Melk Scheibbs` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260811_TRAIN/129136.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129136.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Vivian Bürklin, D.-Zeiner-Gasse 17, 4481 Asten, Österreich, über die Vorlageanträge vom 13.4.2020 gegen die Bescheide  (Beschwerdevorentscheidungen) des Finanzamtes Wien 4/5/10 vom 14. bzw 16.8.2019,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016 bzw 2018 beschlossen:  I. Die Vorlageanträge werden gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vivian Bürklin` (person)
- `D.-Zeiner-Gasse 17, 4481 Asten, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260811_TRAIN/129140.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Veronika Splettstösser, Geiter 10, 9531 Labientschach, Österreich, vertreten durch Eva Maria Koller-Rohrschach,  Brünner Straße 133/1, 1210 Wien, über die Beschwerde vom 19. Februar 2020 gegen den  Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 3. Februar 2020 betreffend  Säumniszuschlag 2017 Steuernummer 08 - 83-370/4398  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Veronika Splettstösser` (person)
- `Geiter 10, 9531 Labientschach, Österreich` (address)
- `Eva Maria Koller-Rohrschach` (person)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)
- `83-370/4398` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260811_TRAIN/129168.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129168.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner über die Beschwerde des  Charlotte Medick, Oberhaus 36, 4901 Laah, Österreich, vom 10. Mai 2020, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 4. März 2020, MA67/123/2019, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde abgewiesen  und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Medick` (person)
- `Oberhaus 36, 4901 Laah, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260811_TRAIN/129187.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129187.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Kordelia Wilkeit  in der Beschwerdesache Loglogwald-Sicherheit GmbH  Bernatzikgasse 11i, 3040 Schwertfegen, Österreich, vertreten durch zobl.bauer.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Kordelia Wilkeit` | `Hon.-Prof.in Kordelia Wilkeit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Loglogwald-Sicherheit GmbH` (organisation)
- `Bernatzikgasse 11i, 3040 Schwertfegen, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_20260811_TRAIN/129231.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129231.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Elisabeth Traxler in der  Beschwerdesache Guntram Reuttner, Gewerbezone, Technikstraße 28V, 7561 Heiligenkreuz im Lafnitztal, Österreich  vertreten durch EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG, Joseph Haydn-Gasse 40/2, 7000 Eisenstadt,  betreffend Beschwerde vom 4. Mai 2017 gegen den Bescheid des Finanzamtes Wien 1/23 vom  4. April 2017 betreffend Festsetzung des Dienstgeberbeitrages zum Ausgleichsfonds für  Familienbeihilfen ua. für den Zeitraum 01/2012-03/2015 beschlossen:  Der Vorlageantrag vom 20. Juni 2018 wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Elisabeth Traxler` | `Mag. Elisabeth Traxler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Guntram Reuttner` (person)
- `Gewerbezone, Technikstraße 28V, 7561 Heiligenkreuz im Lafnitztal, Österreich` (address)
- `EWT Schuster & Kampits  Wirtschaftstreuhand & Steuerberatungs OG` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260811_TRAIN/129233.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim sowie die fachkundigen Laienrichter Leopold Pichlbauer und Dr.  Karl Penninger in der Beschwerdesache Vivian Imai, Übermoos 13, 9361 Moserwinkl, Österreich  vertreten durch Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH, Denkstraße 49, 4030 Linz, vom  20. Juli 2018 gegen die Bescheide des Finanzamtes Grieskirchen Wels vom 20. Juni 2018  betreffend Umsatzsteuer 2011 und 2012 nach Durchführung einer mündlichen Verhandlung  am 15. Juni 2020 in Anwesenheit der Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |
| `Dr.  Karl Penninger` | `Dr.  Karl Penninger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold Pichlbauer` (person)
- `Vivian Imai` (person)
- `Übermoos 13, 9361 Moserwinkl, Österreich` (address)
- `Treuhand- Union Linz, Wirtschaftsprüfungs- und SteuerberatungsgmbH` (organisation)
- `Finanzamtes` (organisation)
- `Tanja Grottenthaler` (person)

**Example 20** (doc_id: `deanon_BFG_20260811_TRAIN/129254.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Gloria Chmielarczyk, Bärenweg 17, 2113 Großrußbach, Österreich, vertreten durch Grant Thornton Austria GmbH,  Handelskai 92/Gate 2/7A, 1200 Wien, über die Beschwerde vom 30. Oktober 2015 gegen    den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2011 bis 31.12.2011,   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2012 bis 31.12.2012 und   den Bescheid gemäß § 201 BAO des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 17.08.2015 über die Festsetzung der Gebühr nach § 33 TP 5 Absatz 1  Ziffer 1 Gebührengesetz 1957 betreffend den Zeitraum 01.01.2013 bis 31.08.2013  zu Recht:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Thomas Leitner` | `Mag.Dr. Thomas Leitner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gloria Chmielarczyk` (person)
- `Bärenweg 17, 2113 Großrußbach, Österreich` (address)
- `Grant Thornton Austria GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260811_TRAIN/129276.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Estelle Zeippert  in der Beschwerdesache des  Ing. StR Pawel Elsenbruch Bf1-Adr***StB über die Beschwerde vom 13. November 2017 gegen den  Bescheid des Finanzamt Waldviertel  vom 11. Oktober 2017 betreffend Einkommensteuer 2015 zu Recht  erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Estelle Zeippert` | `Univ.-Prof.in Estelle Zeippert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. StR Pawel Elsenbruch` (person)
- `Finanzamt Waldviertel` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260811_TRAIN/129277.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129277.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache des KommR Imre Federschmidt,  Strad 68, 8793 Gimplach, Österreich, über die Beschwerde vom 7. April 2014 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 1. April 2014 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2013 Steuernummer 44-992/1782  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `KommR Imre Federschmidt` | `KommR Imre Federschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Strad 68, 8793 Gimplach, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `44-992/1782` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260811_TRAIN/129379.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129379.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Nadja Zeitel  in der Beschwerdesache des  Michael Berks, Salpeterstraße 14, 9343 Brunn (Zweinitz), Österreich, vertreten durch Mag. Hermann Rupert Zittmayr, Kreuzgasse 2,  6330 Kufstein, über die Beschwerden vom 17.7.2018 und vom 3.8.2018 gegen die Bescheide  des Finanzamt Vorarlberg  vom 15.6.2018 betreffend Einkommensteuer 2012 und vom 17.7.2018  betreffend Einkommensteuer 2013 beschlossen:     Die Beschwerden gelten gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Nadja Zeitel` | `Univ.-Prof.in Nadja Zeitel` |
| `Mag. Hermann Rupert Zittmayr` | `Mag. Hermann Rupert Zittmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Michael Berks` (person)
- `Salpeterstraße 14, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamt Vorarlberg` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260811_TRAIN/129396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129396.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Carmen Schmölz  in der Beschwerdesache des  Anatol Möws Bf1-Adr StR MedR Lukas Chatzopoulos  über die Beschwerde vom 5. August 2019 gegen den  Bescheid des Finanzamt Oststeiermark  vom 10. Juli 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:    Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Carmen Schmölz` | `Hon.-Prof.in Carmen Schmölz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anatol Möws` (person)
- `StR MedR Lukas Chatzopoulos` (person)
- `Finanzamt Oststeiermark` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260811_TRAIN/129421.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Linn Rolfink  in der Beschwerdesache Sascha Mertesacker,  Bahnhof Donauuferbahn 33, 9345 Lassenberg, Österreich, über die Beschwerde vom 22. Jänner 2019 gegen den (Sammel)Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14. Jänner 2019, [...],  betreffend Gebühr (Eingabengebühr gem. § 14 TP 6 GebG) und Gebührenerhöhung zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Linn Rolfink` | `Mag.a Linn Rolfink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sascha Mertesacker` (person)
- `Bahnhof Donauuferbahn 33, 9345 Lassenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260811_TRAIN/129460.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129460.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  KzlR Andrea Marcksteiner, Simon Scheiner-Straße 70, 4722 Waasnerau, Österreich, betreffend Beschwerde vom 30. Juli 2015 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg vom 22. Juli 2015 zu Steuernummer  88-497/8438  betreffend Wiederaufnahme des Verfahrens gemäß § 303 BAO hinsichtlich  Einkommensteuer 2011 und 2012 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |
| `KzlR Andrea Marcksteiner` | `KzlR Andrea Marcksteiner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Simon Scheiner-Straße 70, 4722 Waasnerau, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `88-497/8438` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260811_TRAIN/129477.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129477.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  StR Melina Moebes, Paradeisweg 17, 5212 Edt, Österreich (Bescheidadressat Gruppenmitglied und Gruppenträger), vertreten  durch ICON Wirtschaftstreuhand GmbH, Stahlstraße 14, 4020 Linz, vom 30. Juni 2020, gegen  die Bescheide des Finanzamtes Linz vom 22. Juni 2020 betreffend Feststellungsbescheid  Gruppenmitglied 2015 bis 2017

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `StR Melina Moebes` | `StR Melina Moebes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paradeisweg 17, 5212 Edt, Österreich` (address)
- `ICON Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260811_TRAIN/129484.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129484.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 12.10.2017 der Glanzberdorf, Knotzberg 36, 9330 Krasta, Österreich, vertreten durch Westra  GmbH Steuerberatungsgesellschaft, Körnerstraße 13, 4020 Linz, gegen den Bescheid des  Bundesministers für Finanzen vom 08.09.2017, zugestellt am 12.09.2017, Zahl: BMF- 010221/0192-VI/8/2017, mit dem der Antrag gemäß § 48 BAO vom 16.06.2015 auf  Anrechnung griechischer Gebühren für die Jahre 2010 bis 2014 abgewiesen wurde,   zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Glanzberdorf` (organisation)
- `Knotzberg 36, 9330 Krasta, Österreich` (address)
- `Westra  GmbH Steuerberatungsgesellschaft` (organisation)
- `BMF` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260811_TRAIN/129528.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129528.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache        Timon Wanitschek, Dr.-Herrmann-Gasse 212, 4142 Mühlholz, Österreich, vertreten durch Sedelmayer & Klier Steuerberater und  Wirtschaftsprüfer GmbH, Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 11. Juni  2019 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 5. Juni 2019 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timon Wanitschek` (person)
- `Dr.-Herrmann-Gasse 212, 4142 Mühlholz, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260811_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Li Fatih, Bakk. iur., Siegmar-Bergelt-Weg 38, 8793 Krumpen, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Li Fatih, Bakk. iur.` (person)
- `Siegmar-Bergelt-Weg 38, 8793 Krumpen, Österreich` (address)
- `Mag. Walter Dienstl & Partner  KG` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ralf Schatzl in der Beschwerdesache  PhD Helena Jungkuhn, Grazer-Straße 111, 8322 Mitterfladnitz, Österreich, über die Beschwerden vom 19. Dezember 2017 gegen die  Bescheide des Finanzamtes Salzburg-Land vom 20. November 2017 betreffend die Abweisung  der Anträge auf Wiederaufnahme der Verfahren betreffend die Einkommensteuer 2011, 2012,  2013 und 2014 zu Steuernummer 53-953/1891  zu Recht erkannt:   I. Die Beschwerden gegen die Abweisung der Anträge auf Wiederaufnahme der Verfahren  betreffend die Einkommensteuer 2011, 2012 und 2013 werden gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ralf Schatzl` | `Dr. Ralf Schatzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `PhD Helena Jungkuhn` (person)
- `Grazer-Straße 111, 8322 Mitterfladnitz, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `53-953/1891` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_26`)


Mit Schriftsatz vom 04.08.2020 legte die BF durch ihren ausgewiesenen Vertreter folgende sie  betreffende Unterlagen vor:  Einen radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001 betreffend Sehnen- risse in der die rechte Schulter;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 33** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_32`)


einen radiologischen Befund des Institutes Dr. Doringer  vom 27.08.2014 betreffend die Wirbelsäule;

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 34** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_38`)


Dies ergibt sich aus dem ärztlichen Gutachten des Dr. Christian Dohnalek vom 01.09.2016.

| Predicted | Gold |
|---|---|
| `Dr. Christian Dohnalek` | `Dr. Christian Dohnalek` |

**Example 35** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_42`)


Dies ergibt sich aus dem radiologischen Befund des Institutes Dr. Doringer vom 25.09.2001  sowie der Diagnose der Schulterambulanz des UKH Salzburg vom 27.09.2001.

| Predicted | Gold |
|---|---|
| `Dr. Doringer` | `Dr. Doringer` |

**Example 36** (doc_id: `deanon_BFG_20260811_TRAIN/129671.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129671.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Xenia Griesinger  in der Beschwerdesache Valheimkel-Logistik,  Gürtelberg 9, 2135 Kottingneusiedl, Österreich, über die Beschwerden vom 28.07.2011 gegen die Bescheide des Finanzamtes  Neunkirchen Wr. Neustadt vom 29.06.2011

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Xenia Griesinger` | `Hon.-Prof.in Xenia Griesinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valheimkel-Logistik` (organisation)
- `Gürtelberg 9, 2135 Kottingneusiedl, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260811_TRAIN/129733.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129733.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Bertram Eberhardi  in der Beschwerdesache ÖkR Leander Dornsiepen,  Ursogasse 9, 5724 Pirtendorf, Österreich, vertreten durch Union TAX&LAW, Donau-City-Straße 7, DV Tower/30th floor,  1220 Wien, über die Beschwerde vom 16. April 2019 gegen den Bescheid des Finanzamtes  Innsbruck vom 19. März 2019 betreffend Familienbeihilfe (Ausgleichszahlung) für die Monate  Jänner 2015 bis Dezember 2017, [Ordnungsbegriff],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Bertram Eberhardi` | `Mag. Bertram Eberhardi` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Leander Dornsiepen` (person)
- `Ursogasse 9, 5724 Pirtendorf, Österreich` (address)
- `Finanzamtes  Innsbruck` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260811_TRAIN/129773.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129773.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Kerstin Westfal, Klockerweg 6, 8242 Sankt Lorenzen am Wechsel, Österreich, über die Beschwerde vom 24. Oktober 2019  gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 10. Oktober 2019  betreffend Abweisung des Antrags auf Familienbeihilfe für den Zeitraum März 2019 bis Mai  2019 sowie ab September 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kerstin Westfal` (person)
- `Klockerweg 6, 8242 Sankt Lorenzen am Wechsel, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260811_TRAIN/129778.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129778.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache KzlR Gabriel Blazejewicz, Damnigweg 159, 9181 Wellersdorf, Österreich, über die Beschwerde vom 12. Jänner 2019  gegen den Bescheid des Finanzamtes Wien 8/16/17 vom 9. Jänner 2019 betreffend  Säumniszuschlag nach Durchführung einer mündlichen Verhandlung am 24.6.2020 in  Abwesenheit der Beschwerdeführerin und in Anwesenheit von Vertreter für das Finanzamt zur  Steuernummer 06 69-363/8745  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |
| `KzlR Gabriel Blazejewicz` | `KzlR Gabriel Blazejewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Damnigweg 159, 9181 Wellersdorf, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `69-363/8745` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260811_TRAIN/129789.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129789.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über den Antrag der  Janis Tödt, Franz Defregger-Straße 2, 6212 Pertisau, Österreich, vertreten durch BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, QBC 4 – Am Belvedere 4, 1100 Wien, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 1. Mai 2020, GZ. RV/7100084/2020, betreffend Umsatzsteuer  für das Jahr 2014 erhobenen ordentlichen Revision vom 24. Juni 2020 die aufschiebende  Wirkung zuzuerkennen, beschlossen:  Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janis Tödt` (person)
- `Franz Defregger-Straße 2, 6212 Pertisau, Österreich` (address)
- `BDO Austria GmbH, Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260811_TRAIN/129828.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Marianne Klössel, Riesberg 6, 4131 Wölfling, Österreich, vertreten durch Dr. Helmut Herbert Moritz,  Schottenbastei 6 Tür 8, 1010 Wien, über die Beschwerde vom 14. August 2019 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 4. Juli 2019 betreffend  Einkommensteuer 2018 zu Steuernummer 07 90-987/4178  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |
| `Dr. Helmut Herbert Moritz` | `Dr. Helmut Herbert Moritz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marianne Klössel` (person)
- `Riesberg 6, 4131 Wölfling, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `90-987/4178` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260811_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129861.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Larissa Klinkers  in der Beschwerdesache Karim Keizer,  Oberbieler Platz 18, 4362 Kollroßdorf, Österreich  vertreten durch RA MMag. Dr. Alexander Lamplmayr als gerichtlicher  Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der  beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der  Entscheidungspflicht durch das FA Wien 1/23  betreffend die Anträge vom 3.5.2018 auf Zustellung  des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte  Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge  wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung,  Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung  bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum  unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung  hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe  von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen:  a)

| Predicted | Gold |
|---|---|
| `Dr.in Larissa Klinkers` | `Dr.in Larissa Klinkers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karim Keizer` (person)
- `Oberbieler Platz 18, 4362 Kollroßdorf, Österreich` (address)
- `RA MMag. Dr. Alexander Lamplmayr` (person)
- `FA Wien 1/23` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260811_TRAIN/129872.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache Dipl. Kfm. Thorsten Duchan, Vossenlände 17, 8253 Schmiedviertel, Österreich, vertreten durch Mag. Gugenberger Barbara, Edith-Stein-Weg  2, 6020 Innsbruck, über die Beschwerde vom 30. Jänner 2014 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 23. Jänner 2014 betreffend Einkommensteuer 2012  Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |
| `Mag. Gugenberger Barbara` | `Mag. Gugenberger Barbara` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kfm. Thorsten Duchan` (person)
- `Vossenlände 17, 8253 Schmiedviertel, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260811_TRAIN/129937.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129937.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Birgit Hakim, Himberger Straße 9, 4161 Sonnenwald, Österreich, vom 25. Juni 2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 28. Mai 2020, Zahl: MA67/Zahl, wegen einer  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Abweisung  I. Der Beschwerde wird teilweise Folge gegeben und die Entscheidung des Magistrats der Stadt  Wien in ihrem Ausspruch über die Strafe dahingehend abgeändert, dass die gemäß § 4 Abs. 1  Parkometergesetz 2006 verhängte Geldstrafe von € 140,00 auf € 90,00 und die gemäß § 16  Abs. 1 Verwaltungsstrafgesetz 1991 (VStG) verhängte Ersatzfreiheitsstrafe von 1 Tag 9 Stunden  auf 21 Stunden verringert werden.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Birgit Hakim` (person)
- `Himberger Straße 9, 4161 Sonnenwald, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)
- `Magistrats der Stadt  Wien` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260811_TRAIN/129949.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129949.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Erwin Nehse, Greimelweg 11, 4224 Klausmühle, Österreich, vertreten durch LMG  Steuerberatungsgesellschaft m.b.H., Sochorgasse 3, 2512 Traiskirchen, über die Beschwerde  vom 2. März 2018 gegen den Bescheid des Finanzamtes Baden Mödling vom 21. Februar 2018  betreffend Abweisung des Antrags auf  Wiederaufnahme § 303 BAO / Sonstige 01.2014-

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Nehse` (person)
- `Greimelweg 11, 4224 Klausmühle, Österreich` (address)
- `LMG  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260811_TRAIN/129977.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129977.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Daisy Beutell, Axerried 14, 8583 Modriach, Österreich, über die Beschwerde vom 22. Juni 2017 gegen  den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart vom 12. Juni 2017 betreffend  Familienbeihilfe 01.2016-12.2016 zu Recht erkannt:   Der angefochtene Bescheid wird  - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daisy Beutell` (person)
- `Axerried 14, 8583 Modriach, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260811_TRAIN/130024.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hugo Voelp, Weißes Kreuz-Gasse 10f, 8967 Birnberg, Österreich, über die Beschwerde vom 21. Dezember 2018 gegen den Bescheid  des Finanzamtes Hollabrunn Korneuburg Tulln vom 6. Dezember 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Kinderabsetzbetrages für den  Monat September 2018 nach Durchführung einer mündlichen Verhandlung am 14.10.2020 zu  Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hugo Voelp` (person)
- `Weißes Kreuz-Gasse 10f, 8967 Birnberg, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260811_TRAIN/130332.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Igor Pölemann, Heugschwend 10, 3341 Haselgraben, Österreich, vertreten durch Sigrid Lamböck, Adolfstorgasse 63, 1130 Wien,  über die Beschwerde vom 24. Juni 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 28. Mai 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Igor Pölemann` (person)
- `Heugschwend 10, 3341 Haselgraben, Österreich` (address)
- `Sigrid Lamböck` (person)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260811_TRAIN/130367.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Paulina Kovalev, Franz-Wagner-Weg 50, 8130 Pfannberg, Österreich, über die Beschwerde vom 4. Juni 2020 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 18. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paulina Kovalev` (person)
- `Franz-Wagner-Weg 50, 8130 Pfannberg, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260811_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri1 als Vorsitzenden, den RichterRi2 als  beisitzenden Richter sowie die fachkundigen Laienrichter LaienRi1 und LaienRi2 über die  Beschwerde des Dipl.-Ing. Svenja Liedemann, Donnersbachwald 27, 4891 Vöcklatal, Österreich, vertreten durch STB, Adr2, vom 12. April 2017  gegen den Bescheid des Finanzamtes Spittal Villach vom 10. März 2017, dieses vertreten durch  HR Dr. Amtsvertr, betreffend Einkommensteuer 2013 nach Durchführung einer mündlichen  Verhandlung am 8. Juni 2020 in Anwesenheit der Schriftführerin FOI SF zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Svenja Liedemann` | `Dipl.-Ing. Svenja Liedemann` |
| `Dr. Amtsvertr` | `Dr. Amtsvertr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donnersbachwald 27, 4891 Vöcklatal, Österreich` (address)
- `Finanzamtes Spittal Villach` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260811_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130422.1_199`)


Der Bf führte in seinem Schussantrag aus, dass er die ImmoESt gar nicht schulde, sondern hätte  diese vielmehr sein vormaliger steuerlicher Vertreter, StB Priv.-Doz.in Lucia Teumert  zu tragen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Lucia Teumert` | `Priv.-Doz.in Lucia Teumert` |

**Example 52** (doc_id: `deanon_BFG_20260811_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130422.1_350`)


Eine Haftung des ehemaligen  steuerlichen Vertreters des Bf, StB Priv.-Doz.in Lucia Teumert  auf Grundlage der Bestimmung des § 30c Abs. 3 leg.  cit.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Lucia Teumert` | `Priv.-Doz.in Lucia Teumert` |

**Example 53** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Penelope Veitt, Isengaustraße 12, 3623 Dankholz, Österreich, vertreten durch Mag. Margot Artner,  Luftbadgasse 4/3/-, 1060 Wien, über die Beschwerde vom 21. November 2018 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 22. Oktober 2018, mit welchem der Antrag  auf (erhöhte) Familienbeihilfe ab März 2018 abgewiesen wurde,  nach Durchführung einer  mündlichen Verhandlung am 28. Oktober 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Penelope Veitt` (person)
- `Isengaustraße 12, 3623 Dankholz, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_18`)


FÄ-Betreuung bei Dr. Prause 1 x  wö.; keine Psychotherapie  Sozialanamnese:  Ausbildung: 12 Kl. in Vienna International School-Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 55** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_99`)


Aufnahme, macht Gruppentherapie Fa Behandlung Dr. Prause 1/ Monat  Ausbildung: 12 Kl. in Vienna International School - Abschluss mit Zertifikat 2011;

| Predicted | Gold |
|---|---|
| `Dr. Prause` | `Dr. Prause` |

**Example 56** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_182`)


Beschwerdevorentscheidung 11 06 2019   Vorlageantrag vertreten durch Mag. Artner 19 07 2019:   ..."Insgesamt ergibt sich spätestens ab 06 bzw 08/2013 die Erwerbsunfähigkeit des  Beschwerdeführers auf Grund einer damals wie heute bestehenden Erkrankung".

| Predicted | Gold |
|---|---|
| `Mag. Artner` | `Mag. Artner` |

**Example 57** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_213`)


Halluzinationen,  Vorstellungskonkretisierungen, Gedankenausbreitung sowie Wahnideen (bizarre Ängste) und  Konzentrationsstörungen im Vordergrund gestanden..... zur Untersuchung mitgebrachter  Befund:   Befund Psychiater Dr. Prause Heilsarmee 07 07 2020:   ...wird seit 11/2017 h.o. betreut...von 27 02-

| Predicted | Gold |
|---|---|
| `Dr. Prause Heilsarmee` | `Dr. Prause Heilsarmee` |

**Example 58** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_230`)


Er weist darauf hin,  dass im Befundbericht vom St. Gabriel Hospital in der deutschen Übersetzung Dr. Padesse als  behandelnder psychiatrischer Arzt angeführt ist, aus der Urkunde ergibt sich aber, dass er Dr.  Tadesse Bedasa heißt und der Arzt ist nach wie vor in diesem Krankenhaus beschäftigt  (Ausdruck aus dem Internet).

| Predicted | Gold |
|---|---|
| `Dr. Padesse` | `Dr. Padesse` |
| `Dr.  Tadesse Bedasa` | `Dr.  Tadesse Bedasa` |

**Example 59** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_250`)


Frau Mag. Margot Artner wurde mit Beschluss des BG Favoriten vom 19. Juni 2017, GZ. 50P  82/16f-19, zur Sachwalterin bestellt.  Der Bf. war - außer Ferialjobs - nie berufstätig.

| Predicted | Gold |
|---|---|
| `Mag. Margot Artner` | `Mag. Margot Artner` |

**Example 60** (doc_id: `deanon_BFG_20260811_TRAIN/130437.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der Beschwerdesache  Sheila Potocsnik, Am Turmstein 9G, 4675 Stüblreith, Österreich, über die Beschwerde vom 29. Mai 2019 gegen den Bescheid des  Finanzamtes Hollabrunn Korneuburg Tulln vom 30. April 2019 betreffend Rückforderung der  für VN-Sohn NN für den Zeitraum Jänner 2018 bis Dezember 2018 ausbezahlten  Familienbeihilfe und des Kinderabsetzbetrages zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sheila Potocsnik` (person)
- `Am Turmstein 9G, 4675 Stüblreith, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260811_TRAIN/130444.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130444.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Kaspar Schillings  in der Beschwerdesache Evelyn Wamßler, Bakk. rer. nat.,  Johann-Hanngasse 232, 8755 Möschitzgraben, Österreich, vertreten durch Vedat Gökdemir, Michael-Gaismair-Straße 12 Tür B2, 6020  Innsbruck, über die Beschwerde vom 30. Juli 2019 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 10. Juli 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum September 2014 bis Juni 2018  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Kaspar Schillings` | `Dr. Kaspar Schillings` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Evelyn Wamßler, Bakk. rer. nat.` (person)
- `Johann-Hanngasse 232, 8755 Möschitzgraben, Österreich` (address)
- `Vedat Gökdemir` (person)
- `Finanzamtes` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260811_TRAIN/130475.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130475.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache KzlR Daphne Niehues, Schutzwiesengasse 16, 4730 Breitwies, Österreich, über die Beschwerden vom 22.12.2018  (hinsichtlich des Jahres 2014) und vom 13.01.2019 (hinsichtlich der Jahre 2015 und 2016)  gegen die Berichtigungsbescheide gemäß § 293 BAO zu den Einkommensteuerbescheiden für  die Jahre 2014 bis 2016 jeweils vom 18.12.2018 des Finanzamtes Wien 2/20/21/22   zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `KzlR Daphne Niehues` | `KzlR Daphne Niehues` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Schutzwiesengasse 16, 4730 Breitwies, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260811_TRAIN/130647.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig über die Beschwerde  des Sven Novack, Vilicusweg 8, 4131 Haar, Österreich, vom 1. August 2020 gegen das Straferkenntnis des Magistrates  der Stadt Wien vom 1. Juli 2020, GZ. MA67/GZ, betreffend Verwaltungsübertretung nach § 5  Abs. 2 (Wiener) Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien  Nr. 24/2012, den Beschluss gefasst:  Die Beschwerde vom 1. August 2020 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karoline Windsteig` | `Mag. Karoline Windsteig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Novack` (person)
- `Vilicusweg 8, 4131 Haar, Österreich` (address)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260811_TRAIN/130673.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130673.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Verwaltungsstrafsache  gegen VetR Rebecca Hauffenmeyer, Romualdweg 26Y, 5124 Aich, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idgF in Verbindung mit § 4  Abs. 1 Parkometergesetz 2006 gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006  LGBl. für Wien Nr. 9/2006 idgF, über die Beschwerde vom 18. September 2020 gegen das  Erkenntnis des Magistrates der Stadt Wien vom 7. September 2020, Zahl  MA67/206700473993/2020, beschlossen:  1.) Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  das Beschwerdeverfahren eingestellt.  2. Gemäß § 52 Abs. 1 VwGVG hat der Beschwerdeführer keinen Beitrag zu den Kosten des  Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |
| `VetR Rebecca Hauffenmeyer` | `VetR Rebecca Hauffenmeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Romualdweg 26Y, 5124 Aich, Österreich` (address)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260811_TRAIN/130676.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Aigner in der Beschwerdesache  Yelec Wappenschmidt, Krokusgasse 210, 2022 Immendorf, Österreich, vertreten durch Dr. Elke Hager, Rummelhardtgasse 3 Tür 34, 1090  Wien, über die Beschwerde vom 7. April 2020 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 16. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer XXX/XXXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Dr. Elke Hager` | `Dr. Elke Hager` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Yelec Wappenschmidt` (person)
- `Krokusgasse 210, 2022 Immendorf, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260811_TRAIN/130748.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130748.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Michael Mandlmayr in der  Beschwerdesache Claudia Husermann, Am Wagram 14, 4675 Untermeggenbach, Österreich, betreffend Beschwerde vom 10. Oktober 2016  gegen den Bescheid/die Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf  vom 5. September 2016 betreffend Kapitalertragsteuer 2013 und Kapitalertragsteuer 2014 zu  Steuernummer 38-175/7258  beschlossen:  Der Vorlageantrag vom 28. Juli 2017 wird gemäß § 260 Abs. 1 lit. a BAO in Verbindung mit  § 264 Abs. 5 BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Mandlmayr` | `Dr. Michael Mandlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claudia Husermann` (person)
- `Am Wagram 14, 4675 Untermeggenbach, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `38-175/7258` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260811_TRAIN/130749.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache OStR Ulrich Kuckeland, Bakk. techn., Gaislachkogel 475, 4263 Riemetschlag, Österreich, über die Beschwerde vom 28. Juni 2018 gegen  den Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 19. Juni 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.Dr. Thomas Leitner` | `Mag.Dr. Thomas Leitner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Ulrich Kuckeland, Bakk. techn.` (person)
- `Gaislachkogel 475, 4263 Riemetschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260811_TRAIN/130822.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Stephanie Wandmaker, Huttererstraße 37, 5121 Fugging, Österreich, über die Beschwerde gegen die Bescheide des Finanzamtes Wien  2/20/21/22 betreffend Körperschaftsteuer und Umsatzsteuer für die Jahre 2007 bis 2009 und  über die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer für das Jahr 2010 zu  Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephanie Wandmaker` (person)
- `Huttererstraße 37, 5121 Fugging, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260811_TRAIN/130909.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130909.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache DDr.in Richarda Hierschauer, Richard-Gutscher-Gasse 8, 9064 Ochsendorf, Österreich, vertreten durch Dr. Ulrich Weichselbaumer,  öffentlicher Notar, Roosveltstraße 12, 4400 Steyr, über die Beschwerde vom 17. Februar 2015  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 19. Jänner 2015 betreffend  Abweisung des Antrages vom 12. Jänner 2015 auf Wiederaufnahme des Verfahrens hinsichtlich  Einkommensteuer 2013, Steuernummer 266/1232, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |
| `DDr.in Richarda Hierschauer` | `DDr.in Richarda Hierschauer` |
| `Dr. Ulrich Weichselbaumer` | `Dr. Ulrich Weichselbaumer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Richard-Gutscher-Gasse 8, 9064 Ochsendorf, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260811_TRAIN/130909.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130909.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Kaufvertrag vom 8. Mai 2013 verkauften Ehefrau, DDr.in Richarda Hierschauer (Beschwerdeführer, im  Folgenden kurz als Bf. bezeichnet) und Sohn die Grundstücke A und B sowie x-tel  Miteigentumsanteile aus dem Grundstück C, KG G, (Kaufobjekt 1) an Frau H und y-tel  Miteigentumsanteile aus dem Grundstück C, KG G, (Kaufobjekt 2) an Frau K.  Mit Vorhalt des Finanzamtes vom 6. Oktober 2014 wurde der Bf. darauf hingewiesen, dass die  beantragte Wohnsitzbefreiung nur für das Gebäude sowie für Grund und Boden gelte, soweit  als das Grundstück der Nutzung des Eigenheimes oder der Eigentumswohnung als Garten oder  Nebenfläche diene.

| Predicted | Gold |
|---|---|
| `DDr.in Richarda Hierschauer` | `DDr.in Richarda Hierschauer` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260811_TRAIN/130927.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130927.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Eleonore Adamy  in der Beschwerdesache Armin Rempel,  Fischauer Gasse 34S, 9132 Glantschach, Österreich, vertreten durch Dkfm. Anton Hörmann, Haslacher Straße 20, 83278  Traunstein, Steuerberater, über die Beschwerde vom 13. September 2012 gegen die Bescheide  des Finanzamtes Kitzbühel Lienz vom 14. August 2012, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Mag.a Eleonore Adamy` | `Mag.a Eleonore Adamy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Armin Rempel` (person)
- `Fischauer Gasse 34S, 9132 Glantschach, Österreich` (address)
- `Anton Hörmann` (person)
- `Finanzamtes` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260811_TRAIN/130980.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130980.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger in der Beschwerdesache  RgR Calvin Niepolt, Deichgasse 44B, 4925 Noxberg, Österreich, vertreten durch Astoria Steuerberatung GmbH & Co KG,  Wachaustraße 42/A/3, 3500 Krems an der Donau, über die Beschwerden gegen die Bescheide  des Finanzamtes Waldviertel, 1. vom 17. März 2014 gegen die Bescheide vom 19. Februar 2014  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2011 sowie  Einkommensteuer 2011 und 2012 und 2. vom 21. Oktober 2014 gegen den Bescheid vom  2. Oktober 2014, betreffend Einkommensteuer 2013, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Calvin Niepolt` (person)
- `Deichgasse 44B, 4925 Noxberg, Österreich` (address)
- `Astoria Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260811_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131011.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Stefan Pipal in der Beschwerdesache  Peter Viehbacher, Hermann Hlinka Gasse 221, 8264 Hainersdorf, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 20. April 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Stefan Pipal` | `Mag. Stefan Pipal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Peter Viehbacher` (person)
- `Hermann Hlinka Gasse 221, 8264 Hainersdorf, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260811_TRAIN/131011.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131011.1_89`)


Die Wegstrecke BF-Adr bis Tullnerbach-Pressbaum Bahnhof wird laut Fahrplanauskunft bei der  um 7 Uhr 38 Minuten beginnenden Fahrt in 16 Minuten zurückgelegt, für die Wegstrecke bis  Wien Westbahnhof benötigt der Zug nach den vom Bf. übermittelten Unterlagen 33 Minuten,  die Wegstrecke bis Wien Volkstheater (U3) wird von der U-Bahn in 4 Minuten zurückgelegt, (es  folgt eine Gehzeit von 3 Minuten bei einer Wegstrecke von ca. 100 Metern, welche in die  Berechnung der Zeit nicht einzubeziehen ist, da die Zeit des Fußweges nicht zu berücksichtigen  ist), von der Station Dr. Karl Renner-Ring/Volkstheater bis zur Station Wien Schottentor  werden weitere 4 Minuten benötigt.

| Predicted | Gold |
|---|---|
| `Dr. Karl Renner` | `Dr. Karl Renner` |

**Example 75** (doc_id: `deanon_BFG_20260811_TRAIN/131046.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131046.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Rosamunde Schmedecke, Damböckgasse 94, 8322 Fladnitz im Raabtal, Österreich, vertreten durch SCHIETZ + MAUREDER Steuerberatung GmbH,  Veldner Straße 29, 4120 Neufelden, über die Beschwerde vom 20. Juni 2017 gegen den  Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 9. Juni 2017 betreffend  Einkommensteuer 2015 Steuernummer 62-456/3911  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosamunde Schmedecke` (person)
- `Damböckgasse 94, 8322 Fladnitz im Raabtal, Österreich` (address)
- `SCHIETZ + MAUREDER Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `62-456/3911` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260811_TRAIN/131064.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Waltraud Strelzik, Karl-Hainzl-Straße 9, 5101 Bergheim, Österreich, über die Beschwerde vom 13. Februar 2015 gegen den Bescheid  des Finanzamtes Kirchdorf Perg Steyr vom 14. Jänner 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 zu Steuernummer 35-878/3699  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waltraud Strelzik` (person)
- `Karl-Hainzl-Straße 9, 5101 Bergheim, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `35-878/3699` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260811_TRAIN/131091.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131091.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Ludger Wierig  in der Beschwerdesache der Frau  Lewis Schmeltzle, Pochergasse 7, 8151 Södingberg, Österreich, über die Beschwerde vom 10. April 2015 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 18. März 2015 betreffend Umsatzsteuer 2014 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Ludger Wierig` | `Univ.-Prof. Ludger Wierig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lewis Schmeltzle` (person)
- `Pochergasse 7, 8151 Södingberg, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260811_TRAIN/131096.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131096.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Ronja Geschwandner  in der Beschwerdesache Claire Stelmann,  Heinrichs bei Weitra 31, 6842 Koblach, Österreich, vertreten durch PKF CENTURION Wirtschaftsprüfungs- gesellschaft mbH,  Hegelgasse 8, 1010 Wien, über die Beschwerden gegen die Bescheide des Zollamtes Eisenstadt  Flughafen Wien   1) vom 7. Februar 2018, Zl: a, betreffend Festsetzung der Mineralölsteuer für Jänner 2010 mit €  195.809,84 und Festsetzung des Säumniszuschlages mit € 3.916,20;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Ronja Geschwandner` | `Univ.-Prof.in Ronja Geschwandner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claire Stelmann` (person)
- `Heinrichs bei Weitra 31, 6842 Koblach, Österreich` (address)

**Example 79** (doc_id: `deanon_BFG_20260811_TRAIN/131110.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131110.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Ramona Süsslin  in der Beschwerdesache der  Logmon Technologien, Tschofenigweg 4B, 3494 Altweidling, Österreich, über die Beschwerde vom 4. November 2019 gegen die Bescheide  des FA Deutschlandsberg Leibnitz Voitsberg  vom 30. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 -2017 zur Steuernummer 99-999/9999 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ramona Süsslin` | `Hon.-Prof.in Ramona Süsslin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Logmon Technologien` (organisation)
- `Tschofenigweg 4B, 3494 Altweidling, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260811_TRAIN/131197.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alexander Volkert  in der Beschwerdesache Bartholomäus El-Khalil, LLM,  Weg zum Hallenbad 23, 4533 Brandstatt, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Prof.in Finn Stechmüller  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Volkert` | `Dr. Alexander Volkert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bartholomäus El-Khalil, LLM` (person)
- `Weg zum Hallenbad 23, 4533 Brandstatt, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `Prof.in Finn Stechmüller` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/102855.1`) (sent_id: `deanon_BFG_20260811_TRAIN/102855.1_1`)


IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Mag. Hon.-Prof. Milan Siepje  in der Beschwerdesache Mag. Constantin Hanses, vertreten durch die Sachwalterin******, gegen den Bescheid des Finanzamtes Innsbruck vom 9. März 2012 betreffend die Abweisung eines Antrages auf Familienbeihilfe ab September 2011 zu Recht erkannt: I. Die Beschwerde wird abgewiesen.

**False Positives:**

- `Mag. Hon` — partial — pred is substring of gold: `Mag. Hon.-Prof. Milan Siepje`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Milan Siepje`(person)
- `Mag. Constantin Hanses`(person)
- `Finanzamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128730.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter M. in der Beschwerdesache Nord Keltri, Hölzlhuberstraße 24t, 8413 Oberragnitz, Österreich, diese vertreten durch Mag. Dieter Walla & Partner Steuerberater OG, Kremser  Landstraße 7, 3100 Sankt Pölten, über die Beschwerde vom 2. August 2013 gegen den  Bescheid des Finanzamtes Lilienfeld St. Pölten vom 8. Mai 2013 über die Festsetzung von  Anspruchszinsen 2007 zu Steuernummer 60-519/7525  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Dieter Walla` — partial — pred is substring of gold: `Mag. Dieter Walla & Partner Steuerberater OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M.`(person)
- `Nord Keltri`(organisation)
- `Hölzlhuberstraße 24t, 8413 Oberragnitz, Österreich`(address)
- `Mag. Dieter Walla & Partner Steuerberater OG`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `60-519/7525`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/128969.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128969.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Tristan Frickmann  in der Beschwerdesache Prof.in DDr.in Heike Birkenbeul,  In Gruben 55, 9862 Oberkremsberg, Österreich, betreffend Beschwerde vom 20. Februar 2018 gegen die Bescheide  des  Finanzamtes Gmunden Vöcklabruck vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 den Beschluss:  I. Die angefochtenen Bescheide vom 16. Jänner 2018 betreffend Einkommensteuer 2016  und Umsatzsteuer 2016 und die Beschwerdevorentscheidungen vom 28. März 2018  werden gemäß § 278 Abs 1 BAO unter Zurückverweisung der Sache an die  Abgabenbehörde aufgehoben.

**False Positives:**

- `DDr.in Heike Birkenbeul` — partial — pred is substring of gold: `Prof.in DDr.in Heike Birkenbeul`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Tristan Frickmann`(person)
- `Prof.in DDr.in Heike Birkenbeul`(person)
- `In Gruben 55, 9862 Oberkremsberg, Österreich`(address)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/129005.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129005.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Hon.-Prof.in Dr.in Silke Xeller, BEd,  Spannweide Ost 42, 6271 Finsing, Österreich, vertreten durch Egger & Freidorfer Steuerberatungs-OG, Koloman-Wallisch- Platz 23 Tür II, 8600 Bruck an der Mur, über die Beschwerde vom 29. März 2016 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 15. Jänner 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

**False Positives:**

- `Hon.-Prof.in Dr` — partial — pred is substring of gold: `Hon.-Prof.in Dr.in Silke Xeller, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Silke Xeller, BEd`(person)
- `Spannweide Ost 42, 6271 Finsing, Österreich`(address)
- `Egger & Freidorfer Steuerberatungs-OG`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Sandro Birnesser, Guglhof 6, 4906 Anhang, Österreich  vom 13. Januar 2020, vertreten durch Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG, Dr. Gaisbauerstr. 7, 4560 Kirchdorf an der Krems,  gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 9. Dezember 2019 betreffend  Wiederaufnahme des Verfahrens gemäß § 303 BAO und Feststellung der Einkünfte gemäß  § 188 BAO für 2006, nach Durchführung einer mündlichen Verhandlung

**False Positives:**

- `Dr. Gaisbauerstr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Sandro Birnesser`(person)
- `Guglhof 6, 4906 Anhang, Österreich`(address)
- `Czepl & Partner Steuer- und  Unternehmensberatungs GmbH & Co KG`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129027.1_196`)


b. Schreiben des RgR Dipl.-Ing. Donald Wieg an das Finanzamt zum Konkurs der Bf. vom 6. Juli 2010:  Ich beziehe mich auf das Telefonat vom 5. Juli 2010 und gestatte festzuhalten, dass das  Konkursverfahren über das Vermögen der Tal Synsynlem KG nach der Verteilung aufgehoben worden ist.

**False Positives:**

- `Dipl.-Ing. Donald Wieg` — partial — pred is substring of gold: `RgR Dipl.-Ing. Donald Wieg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Dipl.-Ing. Donald Wieg`(person)
- `Tal Synsynlem KG`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/129033.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129033.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Silvana Kislinger, Grünbaumgarten 11, 8200 Ungerdorf, Österreich  vom 25. Februar 2018 gegen den Bescheid des  Finanzamtes St. Johann Tamsweg Zell am See, Brucker Bundesstraße 13, 5700 Zell am See vom  8. Februar 2018 betreffend Festsetzung der Normverbrauchsabgabe für Jänner 2018 zu Recht  erkannt:  1.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Silvana Kislinger`(person)
- `Grünbaumgarten 11, 8200 Ungerdorf, Österreich`(address)
- `Finanzamtes St. Johann Tamsweg Zell`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260811_TRAIN/129035.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129035.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Hon.-Prof.in Prof.in Ute Missigbrodt, Presseggen 17, 4175 Freilassing, Österreich  vom 19. August 2019 gegen den Bescheid des  Finanzamtes Bruck Eisenstadt Oberwart vom 31. Juli 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 beschlossen:  Der Vorlageantrag vom 23. März 2020 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 264 Abs 4 lit e  BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`
- `Hon.-Prof.in Prof` — partial — pred is substring of gold: `Hon.-Prof.in Prof.in Ute Missigbrodt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Hon.-Prof.in Prof.in Ute Missigbrodt`(person)
- `Presseggen 17, 4175 Freilassing, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260811_TRAIN/129101.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. James Albus  in der Beschwerdesache  OStR Fridolin Kumpan Bf1-Adr***RA über die Beschwerde vom 22. Jänner 2018 gegen den Bescheid  des FA Amstetten Melk Scheibbs  vom 21. Dezember 2017 betreffend Haftung uRecht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `OStR Fridolin Kumpan Bf` — partial — gold is substring of pred: `OStR Fridolin Kumpan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. James Albus`(person)
- `OStR Fridolin Kumpan`(person)
- `FA Amstetten Melk Scheibbs`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260811_TRAIN/129261.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129261.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Univ.-Prof.in Mag.a Lukas Ossipowa, Grübelgasse 138, 5143 Wenigaschau, Österreich, vertreten durch Stb, Steuerberater Wirtschaftstreuhänder, Grübelgasse 138, 5143 Wenigaschau, Österreich, über die  Beschwerde vom 28. August 2013 gegen den Bescheid des Finanzamtes B vom 23. August  2013, Steuernummer , betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Mag` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Lukas Ossipowa`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Lukas Ossipowa`(person)
- `Grübelgasse 138, 5143 Wenigaschau, Österreich`(address)
- `Grübelgasse 138, 5143 Wenigaschau, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260811_TRAIN/129261.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129261.1_5`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Univ.-Prof.in Mag.a Lukas Ossipowa – machte in der elektronisch eingebrachten  Erklärung zur Arbeitnehmerveranlagung 2012 vom 29.06.2013 die Rückzahlung von  Notstandshilfe in Höhe von 12.383,52 € als Werbungskosten geltend.

**False Positives:**

- `Univ.-Prof.in Mag` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Lukas Ossipowa`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Mag.a Lukas Ossipowa`(person)

**Example 11** (doc_id: `deanon_BFG_20260811_TRAIN/129276.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Estelle Zeippert  in der Beschwerdesache des  Ing. StR Pawel Elsenbruch Bf1-Adr***StB über die Beschwerde vom 13. November 2017 gegen den  Bescheid des Finanzamt Waldviertel  vom 11. Oktober 2017 betreffend Einkommensteuer 2015 zu Recht  erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Ing. St` — partial — pred is substring of gold: `Ing. StR Pawel Elsenbruch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Estelle Zeippert`(person)
- `Ing. StR Pawel Elsenbruch`(person)
- `Finanzamt Waldviertel`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260811_TRAIN/129396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129396.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Carmen Schmölz  in der Beschwerdesache des  Anatol Möws Bf1-Adr StR MedR Lukas Chatzopoulos  über die Beschwerde vom 5. August 2019 gegen den  Bescheid des Finanzamt Oststeiermark  vom 10. Juli 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:    Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `StR Med` — partial — pred is substring of gold: `StR MedR Lukas Chatzopoulos`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Carmen Schmölz`(person)
- `Anatol Möws`(person)
- `StR MedR Lukas Chatzopoulos`(person)
- `Finanzamt Oststeiermark`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260811_TRAIN/129437.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Danielle Michelka  in der Beschwerdesache des  Hildegard Erlmeier, Maurer Lange Gasse 6, 3661 Pleißing, Österreich, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamt Kirchdorf Perg Steyr  vom 11. Jänner 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Mag` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Danielle Michelka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Danielle Michelka`(person)
- `Hildegard Erlmeier`(person)
- `Maurer Lange Gasse 6, 3661 Pleißing, Österreich`(address)
- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260811_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129571.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Li Fatih, Bakk. iur., Siegmar-Bergelt-Weg 38, 8793 Krumpen, Österreich, vertreten durch Mag. Walter Dienstl & Partner  KG, Prinz Eugenstr 58, 1040 Wien, über die Beschwerde vom 21. Februar 2019 gegen den  Bescheid des Finanzamtes Wien 4/5/10 vom 16. Jänner 2019 betreffend Festsetzung einer  Zwangsstrafe gem. § 16 WiEReG zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Walter Dienstl` — partial — pred is substring of gold: `Mag. Walter Dienstl & Partner  KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Li Fatih, Bakk. iur.`(person)
- `Siegmar-Bergelt-Weg 38, 8793 Krumpen, Österreich`(address)
- `Mag. Walter Dienstl & Partner  KG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_30`)


einen radiologischen Befund vom 26.02.2014  der Dr.in Monika Wörther-Madl;

**False Positives:**

- `Dr.in Monika Wörther` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Monika Wörther-Madl`(person)

**Example 16** (doc_id: `deanon_BFG_20260811_TRAIN/129583.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129583.1_40`)


Dies ergibt sich aus dem Entlassungsbericht der Kuranstalt Vigaun GmbH & Co. KG nach dem  Rehabilitationsaufenthalt der BF sowie dem Radiologiebefund der Dr.in Monika Wörther-Madl  vom 26.02.2014.

**False Positives:**

- `Dr.in Monika Wörther` — partial — pred is substring of gold: `Dr.in Monika Wörther-Madl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kuranstalt Vigaun GmbH & Co. KG`(organisation)
- `Dr.in Monika Wörther-Madl`(person)

**Example 17** (doc_id: `deanon_BFG_20260811_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129861.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Larissa Klinkers  in der Beschwerdesache Karim Keizer,  Oberbieler Platz 18, 4362 Kollroßdorf, Österreich  vertreten durch RA MMag. Dr. Alexander Lamplmayr als gerichtlicher  Erwachsenenvertreter, Landstraße 50, 4020 Linz,  über die Beschwerde der  beschwerdeführenden Partei vom 25. Juni 2020 wegen behaupteter Verletzung der  Entscheidungspflicht durch das FA Wien 1/23  betreffend die Anträge vom 3.5.2018 auf Zustellung  des Bescheides vom 24.4.2018 betreffend Pfändung eines Kontos an die bestellte  Sachwalterschaft (nunmehr: Erwachsenenvertretung), Rückzahlung der gepfändeten Beträge  wegen rechtsunwirksamer Bescheidzustellung und daher rechtswidriger Kontopfändung,  Gewährung der Akteneinsicht, in eventu auf Einstellung der Exekution und deren Aufschiebung  bis zur Einstellung der Exekution sowie Rückzahlung der das Existenzminimum  unterschreitenden gepfändeten Beträge, in eventu auf Aufhebung der Kontopfändung  hinsichtlich des Teiles des bis zum nächsten Zahlungstermin notwendigen Unterhaltes in Höhe  von 909,00 € und Rücküberweisung dieses Betrages, Steuernummer ***, beschlossen:  a)

**False Positives:**

- `Mag. Dr` — partial — pred is substring of gold: `RA MMag. Dr. Alexander Lamplmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Larissa Klinkers`(person)
- `Karim Keizer`(person)
- `Oberbieler Platz 18, 4362 Kollroßdorf, Österreich`(address)
- `RA MMag. Dr. Alexander Lamplmayr`(person)
- `FA Wien 1/23`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260811_TRAIN/129861.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129861.1_18`)


Das Finanzamt hat die säumigen Bescheide am 07.09.2020 (nämlich Abweisung des Antrages  auf Einstellung der Vollstreckung, Abweisung des Antrages auf Rückzahlung, Bescheid über die  Einschränkung der Vollstreckung, Bescheid betreffend Antrag auf Kontenschutz) erlassen und  dem Bundesfinanzgericht eine Abschrift übermittelt.  Darüber hinaus wurde der Bescheid – Verfügungsverbot am 03.08.2020 zu Handen des  nunmehr bestellten gerichtlichen Erwachsenenvertreters RA MMag. Dr. Alexander Lamplmayr  erlassen.

**False Positives:**

- `Mag. Dr` — partial — pred is substring of gold: `RA MMag. Dr. Alexander Lamplmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RA MMag. Dr. Alexander Lamplmayr`(person)

**Example 19** (doc_id: `deanon_BFG_20260811_TRAIN/130285.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130285.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Univ.-Prof. Ludger Urhahn  in der Beschwerdesache  Hon.-Prof.in Samantha Fielbrand Bf1-Adr***StB über die Beschwerde vom 18. Februar 2019 gegen den Bescheid  des FA Schwechat Gerasdorf  vom 9. Jänner 2019 betreffend Festsetzung eines ersten Säumniszuschlages zu  Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Dr. Univ` — partial — pred is substring of gold: `Dr. Univ.-Prof. Ludger Urhahn`
- `Hon.-Prof.in Samantha Fielbrand Bf` — partial — gold is substring of pred: `Hon.-Prof.in Samantha Fielbrand`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Univ.-Prof. Ludger Urhahn`(person)
- `Hon.-Prof.in Samantha Fielbrand`(person)
- `FA Schwechat Gerasdorf`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260811_TRAIN/130407.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Dagobert Waischnur, Bakk. iur., Jagdhütte Bärnkar 6, 6923 Lauterach, Österreich, vertreten durch Harald Schmidt,  Mallestigerstraße 2, 9583 Faak am See, über die Beschwerden je vom 17.12.2016 gegen die  Bescheide des Finanzamtes Spittal Villach je vom 25. November 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2010 bis 2014 in der mündlichen Verhandlung  vom 09.06.2020 u Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL.M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Dagobert Waischnur, Bakk. iur.`(person)
- `Jagdhütte Bärnkar 6, 6923 Lauterach, Österreich`(address)
- `Harald Schmidt`(person)
- `Finanzamtes Spittal Villach`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260811_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130422.1_349`)


Mit der Vertragserrichtung beauftragt wurde Rechtsanwalt Priv.-Doz. Dominik Haunschild Dieser gilt als  Parteienvertreter iSd § 30c Abs. 3 EStG 1988, welcher unter den genannten Voraussetzungen  für die richtige Berechnung der strittigen Steuer haftet.

**False Positives:**

- `Priv.-Doz. Dominik Haunschild Dieser` — partial — gold is substring of pred: `Priv.-Doz. Dominik Haunschild`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dominik Haunschild`(person)

**Example 22** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_23`)


Lebt seit Herbst 2017 bei der Heilsarmee; seit ca. 2016 besachwaltet (Mag. Artner-Tauscher);

**False Positives:**

- `Mag. Artner` — partial — pred is substring of gold: `Mag. Artner-Tauscher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Artner-Tauscher`(person)

**Example 23** (doc_id: `deanon_BFG_20260811_TRAIN/130475.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130475.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache KzlR Daphne Niehues, Schutzwiesengasse 16, 4730 Breitwies, Österreich, über die Beschwerden vom 22.12.2018  (hinsichtlich des Jahres 2014) und vom 13.01.2019 (hinsichtlich der Jahre 2015 und 2016)  gegen die Berichtigungsbescheide gemäß § 293 BAO zu den Einkommensteuerbescheiden für  die Jahre 2014 bis 2016 jeweils vom 18.12.2018 des Finanzamtes Wien 2/20/21/22   zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Andrea Müller` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `KzlR Daphne Niehues`(person)
- `Schutzwiesengasse 16, 4730 Breitwies, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260811_TRAIN/130559.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130559.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Priv.-Doz.in Alexandra Eissler  in der Beschwerdesache Florian Langkop,  Schafweg 6, 3470 Engelmannsbrunn, Österreich, vertreten durch Mag. András Radics, Obere Hauptstraße 18-20/Top 6, 7100  Neusiedl am See, über die Beschwerde der beschwerdeführenden Partei vom 22.10.2020  wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Wien 8/16/17  betreffend Beschwerde gegen den Einkommensteuerbescheid für 2019, Steuernummer  93-292/7358, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Priv.-Doz.in Priv` — partial — pred is substring of gold: `Priv.-Doz.in Priv.-Doz.in Alexandra Eissler`
- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Radics`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Priv.-Doz.in Alexandra Eissler`(person)
- `Florian Langkop`(person)
- `Schafweg 6, 3470 Engelmannsbrunn, Österreich`(address)
- `Mag. András Radics`(person)
- `Finanzamt Wien`(organisation)
- `93-292/7358`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260811_TRAIN/130696.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130696.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Eduard Schendzilarz  in der Beschwerdesache Jeffrey Simmeit,  Schrittwiesergasse 14, 8261 Nestelbach im Ilztal, Österreich, über die Beschwerde vom 27. Dezember 2016 gegen den Bescheid des  Finanzamt Linz  vom 23. November 2016 betreffend Haftungsinanspruchnahme gemäß §§ 9 iVm 80ff  Bundesabgabenordnung (BAO) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Univ` — partial — pred is substring of gold: `Priv.-Doz. Univ.-Prof. Eduard Schendzilarz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Eduard Schendzilarz`(person)
- `Jeffrey Simmeit`(person)
- `Schrittwiesergasse 14, 8261 Nestelbach im Ilztal, Österreich`(address)
- `Finanzamt Linz`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260811_TRAIN/130749.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache OStR Ulrich Kuckeland, Bakk. techn., Gaislachkogel 475, 4263 Riemetschlag, Österreich, über die Beschwerde vom 28. Juni 2018 gegen  den Bescheid des Finanzamtes Freistadt Rohrbach Urfahr vom 19. Juni 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OStR Ulrich Kuckeland` — partial — pred is substring of gold: `OStR Ulrich Kuckeland, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `OStR Ulrich Kuckeland, Bakk. techn.`(person)
- `Gaislachkogel 475, 4263 Riemetschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260811_TRAIN/131046.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131046.1_17`)


maßgeblich ist die reine  Geldbewegung (VwGH 18.1.1983, 82/14/0076 sowie EStR Rz 4601ff).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260811_TRAIN/131046.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131046.1_36`)


maßgeblich ist die reine  Geldbewegung (VwGH 18.1.1983, 82/14/0076 sowie EStR Rz 4601ff).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `context_person_herr_combined` 🏆

**F1:** 0.058 | **Precision:** 0.397 | **Recall:** 0.032  

**Format:** `regex`  
**Rule ID:** `9f6bdb14`  
**Description:**
Merged: Rules 9f6bdb14 and f810b83c have identical patterns and metrics; merging eliminates redundancy while preserving the high precision (0.83) of the 'Herr' pattern.

**Content:**
```
(?:Herrn?\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.397 | 0.032 | 0.058 | 184 | 73 | 111 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 73 | 111 | 2225 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/129140.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129140.1_46`)


3) Die Fahrzeuge wurden nach Dienstende am Firmensitz: Adresse abgestellt. Die  Fahrzeugschlüssel und Papiere wurden von Herrn Veronika Splettstösser  oder Frau AB persönlich  entgegengenommen und im Büro versperrt aufbewahrt.

| Predicted | Gold |
|---|---|
| `Veronika Splettstösser` | `Veronika Splettstösser` |

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130422.1_92`)


Mit dieser E-Mail entgegnete der Bf in Beantwortung des Vorhaltes der belangten Behörde wie  folgt:   "Ich darf auf Ihr Email vom 06.06.2017 in Sachen Beschwerde Bf — StNr. 61 10-457/0745  zurückkommen und nach Besprechung mit Herrn Liedemann folgenden Lösungsvorschlag unterbreiten:  Grundsätzliche Überlegung:  Der VwGH vertritt in seinem Erkenntnis vom 29.03.2017 zur Hauptwohnsitzbefreiung die  Ansicht, dass sich die Befreiungsbestimmung des § 30 Abs. 2 Z 1 EStG lediglich auf den Grund  und Boden eines bebauten Grundstücks erstreckt, der nach der Verkehrsauffassung einem  üblicherweise als Bauplatz erforderlichen Grundstück entspricht.

| Predicted | Gold |
|---|---|
| `Liedemann` | `Liedemann` |

**Missed by this rule (FN):**

- `10-457/0745` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/130422.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130422.1_106`)


Aus ökonomische Überlegungen (Vermeidung von Sachverständigen- und anderen  Rechtskosten bzw. zur Erlangung von Rechtssicherheit) wäre Herr Liedemann mit folgender Lösung, die  zwar sachlich stark vereinfachend ist, aber auch durch die Erlasslage gedeckt scheint  (Grundanteil lt. VO, Schätzung der anteiligen Anschaffungskosten der steuerhängigen Fläche  nach § 184 BAO aufgrund des VPI = nachvollziehbare Schätzmethode, die auch wie unten  dargestellt nach steuerlichen Grundsätzen plausibilisierbar ist) einverstanden:  Wie von Ihnen vorgeschlagen wird der Grundanteil mit 20% (lt. VO) angenommen und  aliquotiert in einen Teil von 1.000 m2 steuerbefreit und 1.144 m2 steuerpflichtig.

| Predicted | Gold |
|---|---|
| `Liedemann` | `Liedemann` |

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_30`)


Lfd.Nr. Bezeichnung der körperlichen, geistigen oder sinnesbedingten  Funktionseinschränkungen, welche voraussichtlich länger als sechs Monate andauern werden:  Begründung der Rahmensätze: Pos.Nr. Gdb%  1 paranoide Schizophrenie  Unterer Rahmensatz, da verminderte psychische Belastbarkeit 03.07.02 50  Gesamtgrad der Behinderung 50 v. H.  Begründung für den Gesamtgrad der Behinderung:  Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keine Änderung gegenüber dem VGA von 9/2015  der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 07/2014  Herr Penelope Veitt  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Penelope Veitt` | `Penelope Veitt` |

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_111`)


Herr Penelope Veitt  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA  Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Penelope Veitt` | `Penelope Veitt` |

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_172`)


Vorgutachten 14 08 2018:   paranoide Schizophrenie GdB 50%   seit 07/2014   Herr Penelope Veitt  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA    Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Penelope Veitt` | `Penelope Veitt` |

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/130423.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130423.1_219`)


Herr Penelope Veitt  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen: JA   Die Unfähigkeit, sich selbst den Unterhalt zu verschaffen ist nicht vor vollendetem 18.

| Predicted | Gold |
|---|---|
| `Penelope Veitt` | `Penelope Veitt` |

**Example 7** (doc_id: `deanon_BFG_20260811_TRAIN/131199.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131199.1_4`)


Begründung  Verfahrensgang:  1)  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 17. April  2019, MA67/196700091203/2019, wurde Herr Marion Kondo (in weiterer Folge:   Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Marion Kondo` | `Marion Kondo` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260811_TRAIN/131199.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131199.1_11`)


2)  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 22. Oktober  2019, MA67/196700865572/2019, wurde Herr Marion Kondo (in weiterer Folge:   Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Marion Kondo` | `Marion Kondo` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260811_TRAIN/131396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131396.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Volkmar Prangemeier, Burgfried 140, 7131 Halbturn, Österreich, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 15. März 2019 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 20. Februar 2019, Strafnummer 007, in Anwesenheit des  Beschuldigten, der Amtsbeauftragten sowie der Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Über Volkmar Prangemeier  wird gemäß § 33 Abs. 5 FinStrG eine Geldstrafe in Höhe von € 17.600,00  verhängt.

| Predicted | Gold |
|---|---|
| `Volkmar Prangemeier` | `Volkmar Prangemeier` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Burgfried 140, 7131 Halbturn, Österreich` (address)
- `Finanzamt  Wien 9/18/19` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260811_TRAIN/131396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131396.1_6`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 20. Februar 2019,  Strafnummer 007, wurde Herr Volkmar Prangemeier, geb. 1989, Geschäftsführer, wohnhaft in Burgfried 140, 7131 Halbturn, Österreich  in Abwesenheit schuldig erkannt,   „A.) er hat in Wien vorsätzlich unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des  Umsatzsteuergesetzes 1994 entsprechenden Voranmeldungen eine Verkürzung von  1 von 18 Seite 2 von 18

| Predicted | Gold |
|---|---|
| `Volkmar Prangemeier` | `Volkmar Prangemeier` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Burgfried 140, 7131 Halbturn, Österreich` (address)

**Example 11** (doc_id: `deanon_BFG_20260811_TRAIN/131396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131396.1_132`)


Gesellschafter/Geschäftsführer der Metall Brucklemkraft GmbH ist Herr Volkmar Prangemeier.

| Predicted | Gold |
|---|---|
| `Volkmar Prangemeier` | `Volkmar Prangemeier` |

**Missed by this rule (FN):**

- `Metall Brucklemkraft GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260811_TRAIN/131396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131396.1_153`)


Zwischen Herrn Volkmar Prangemeier, Alleingesellschafter und einziger Geschäftsführer der Metall Brucklemkraft GmbH und  Herrn S., seinem Vater, bestand und besteht nicht nur eine persönliche, sondern auch eine  wirtschaftliche Nahebeziehung.

| Predicted | Gold |
|---|---|
| `Volkmar Prangemeier` | `Volkmar Prangemeier` |

**Missed by this rule (FN):**

- `Metall Brucklemkraft GmbH` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260811_TRAIN/132480.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132480.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 8. Oktober  2020, Zahl: MA67/206700566984/2020, wurde Herr Helga Heideking (in weiterer Folge:  Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Helga Heideking` | `Helga Heideking` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260811_TRAIN/132957.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132957.1_3`)


des Herrn Patricia Schoenemeyer, vertreten durch Herrn Dr. Walter Suppan, Rechtsanwalt in Klagenfurt,

| Predicted | Gold |
|---|---|
| `Patricia Schoenemeyer` | `Patricia Schoenemeyer` |

**Missed by this rule (FN):**

- `Dr. Walter Suppan` (person)

**Example 15** (doc_id: `deanon_BFG_20260811_TRAIN/133433.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133433.1_36`)


Herr Marion Rößener  wird ohne sachliche Grundlage um 123 TEUR entreichert, während in  vergleichbaren Fällen im betrieblichen Bereich dies nicht geschieht.

| Predicted | Gold |
|---|---|
| `Marion Rößener` | `Marion Rößener` |

**Example 16** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_529`)


Er gab an, dass der Chef der SubUnt1 ein Janusz, ein  Pole, gewesen sei, und dass der Chef der SubUnt2 ein Herr Thomas, vermutlich ein  Österreicher, gewesen sei.  - Zeuge59 war bei der SubUnt1 vom 8.9. bis 3.10.2008 beschäftigt gewesen und gab an,  dass seine Ansprechperson ein Marek gewesen sei.

| Predicted | Gold |
|---|---|
| `Thomas` | `Thomas` |

**Example 17** (doc_id: `deanon_BFG_20260811_TRAIN/133764.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133764.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Beschluss des Handelsgerichtes Wien vom 22. Juni 2003  wurde über das Vermögen der  BergImmobilien Systeme GmbH  der Konkurs eröffnet, deren Geschäftsführer seit 21. Juli 1951  der  nunmehrige Beschwerdeführer (Bf.) sowie Herr Gernot Thomaschefsky  waren.

| Predicted | Gold |
|---|---|
| `Gernot Thomaschefsky` | `Gernot Thomaschefsky` |

**Missed by this rule (FN):**

- `22. Juni 2003` (date)
- `BergImmobilien Systeme GmbH` (organisation)
- `21. Juli 1951` (date)

**Example 18** (doc_id: `deanon_BFG_20260811_TRAIN/134159.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134159.1_4`)


Es handelt sich hierbei um eine Beschwerde vom  22.7.2020 des Herrn Antonia Hütten.

| Predicted | Gold |
|---|---|
| `Antonia Hütten` | `Antonia Hütten` |

**Example 19** (doc_id: `deanon_BFG_20260811_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134652.1_8`)


Frau Frau erhob gegen die zwei Strafverfügungen 1) und 2) bei der MA 67 am 08.05.2021  Einspruch und brachte vor „Hiermit geben wir bekannt, dass Herr Agnes Eisenacher  nicht Halter des  Fahrzeugs mit dem Kennzeichen 123 ist“.

| Predicted | Gold |
|---|---|
| `Agnes Eisenacher` | `Agnes Eisenacher` |

**Example 20** (doc_id: `deanon_BFG_20260811_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134652.1_19`)


Mit E-Mail vom 08.05.2021 habe Frau Frau im eigenen Namen gegen die an Herrn Agnes Eisenacher  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Agnes Eisenacher` | `Agnes Eisenacher` |

**Example 21** (doc_id: `deanon_BFG_20260811_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134652.1_26`)


Deshalb sei Frau Frau mit Schreiben der Magistratsabteilung 67 vom 09.06.2021 aufgefordert  worden, binnen zwei Wochen eine für das Verwaltungsstrafverfahren gültige Vollmacht von  Herrn Agnes Eisenacher  zu übermitteln.

| Predicted | Gold |
|---|---|
| `Agnes Eisenacher` | `Agnes Eisenacher` |

**Example 22** (doc_id: `deanon_BFG_20260811_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134652.1_28`)


Am 23.06.2021 sei von Herrn  Agnes Eisenacher  lediglich ein Schreiben mit folgendem Inhalt übermittelt worden: „Bezugnehmend  auf Ihr Schreiben an Frau Frau vom 09.06.2021 möchte ich hiermit eigenhändig bestätigen,  dass das Fahrzeug mit dem angegebenen Kennzeichen nicht in meinem Besitz ist und ich auch  nicht weiß, wem es gehört“.

| Predicted | Gold |
|---|---|
| `Agnes Eisenacher` | `Agnes Eisenacher` |

**Example 23** (doc_id: `deanon_BFG_20260811_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134652.1_38`)


Herr Agnes Eisenacher  sei persönlich bei genannter Firma  3 von 7 Seite 4 von 7

| Predicted | Gold |
|---|---|
| `Agnes Eisenacher` | `Agnes Eisenacher` |

**Example 24** (doc_id: `deanon_BFG_20260811_TRAIN/134762.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Leroy Szukala  in der Beschwerdesache Ing. Thomas Wegmann,  Heachgasse, Oberau 17, 4730 Esthofen, Österreich, vertreten durch Herrn Michael Haberl, Steuerberater, Hauptstraße 65, 8962  Gröbming, über die Beschwerde vom 9.7.2018 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 12.6.2018 betreffend Festsetzung des Dienstgeberbeitrages (DB) für die  Jahre 2013, 2014, 2015 und 2016 sowie des Zuschlages zum Dienstgeberbeitrag (DZ) für die  Jahre 2013, 2014, 2015 und 2016 beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Michael Haberl` | `Michael Haberl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Leroy Szukala` (person)
- `Ing. Thomas Wegmann` (person)
- `Heachgasse, Oberau 17, 4730 Esthofen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260811_TRAIN/135755.1`) (sent_id: `deanon_BFG_20260811_TRAIN/135755.1_42`)


An der OG waren Herr Jasper Markhofer  und Herr WL zu jeweils 50 % beteiligt.

| Predicted | Gold |
|---|---|
| `Jasper Markhofer` | `Jasper Markhofer` |

**Example 26** (doc_id: `deanon_BFG_20260811_TRAIN/135755.1`) (sent_id: `deanon_BFG_20260811_TRAIN/135755.1_46`)


Mit Kaufvertrag vom 09.09.2008 verkaufte Herr Jasper Markhofer  das seit 01.03.2008 bestehende  Einzelunternehmen zum Stichtag 01.07.2008 an die Kraftkelzor-Touristik KG

| Predicted | Gold |
|---|---|
| `Jasper Markhofer` | `Jasper Markhofer` |

**Missed by this rule (FN):**

- `Kraftkelzor-Touristik KG` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260811_TRAIN/136737.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136737.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Lucia Artmeyer, geboren am 1970, Gaas 18, 6095 Grinzens, Österreich, vertreten durch Mag. Johann Hanel,  Wirtschaftstreuhänder & Steuerberater, Goldschlagstraße 8, 1150 Wien, wegen der  Finanzvergehen der Finanzordnungswidrigkeiten gemäß § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom 3. Jänner 2022  gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich  Finanzstrafsachen als Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom  30. September 2021, SpS 21, in der Sitzung am 3. Mai 2022 in Anwesenheit der Schriftführerin  zu Recht erkannt:   Der Beschwerde wird stattgegeben und das angefochtene Erkenntnis des Spruchsenates im  Straf- und Kostenausspruch wie folgt abgeändert:   Über Herrn Lucia Artmeyer  wird gemäß § 49 Abs. 2 FinStrG eine Geldstrafe in Höhe von € 2.800,00  verhängt.

| Predicted | Gold |
|---|---|
| `Lucia Artmeyer` | `Lucia Artmeyer` |
| `Lucia Artmeyer` | `Lucia Artmeyer` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Gaas 18, 6095 Grinzens, Österreich` (address)
- `Mag. Johann Hanel` (person)
- `Amt für Betrugsbekämpfung` (organisation)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260811_TRAIN/136737.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136737.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  als Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 30. September 2021,  SpS 21, wurde Herr Lucia Artmeyer, geboren am 1970, Handel, wohnhaft in Gaas 18, 6095 Grinzens, Österreich  in  nichtöffentlicher Sitzung schuldig erkannt, er habe vorsätzlich unter Verletzung der  Verpflichtung zur Abgabe von dem § 21 des UStG 1994 entsprechenden  1 von 13 Seite 2 von 13

| Predicted | Gold |
|---|---|
| `Lucia Artmeyer` | `Lucia Artmeyer` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Amtes für Betrugsbekämpfung` (organisation)
- `Gaas 18, 6095 Grinzens, Österreich` (address)

**Example 29** (doc_id: `deanon_BFG_20260811_TRAIN/136737.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136737.1_46`)


Da von  Herrn Lucia Artmeyer  nach dem Erkennen des Fehlers bzw. der Säumnis ALLES unternommen  wurde, dass insbesondere der Finanz möglichst wenig Schaden entsteht, ist eine Strafe von  EUR 3.200,- meiner Meinung nach zu hoch.

| Predicted | Gold |
|---|---|
| `Lucia Artmeyer` | `Lucia Artmeyer` |

**Example 30** (doc_id: `deanon_BFG_20260811_TRAIN/136737.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136737.1_76`)


Dem Bericht über das Ergebnis der Außenprüfung vom 1. September 2020, ABNr. 222013/20  ist Folgendes zu entnehmen:  „Tz. 1 Handel   Herr Lucia Artmeyer  betreibt neben seiner nichtselbständigen Vollzeittätigkeit einen Handel.

| Predicted | Gold |
|---|---|
| `Lucia Artmeyer` | `Lucia Artmeyer` |

**Example 31** (doc_id: `deanon_BFG_20260811_TRAIN/136737.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136737.1_104`)


Der Vollständigkeit halber ist festzuhalten, dass Herr Lucia Artmeyer  dadurch aber auch das  Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 2 lit. a FinStrG erfüllt hat, da er  unter Verletzung der Verpflichtung zur Abgabe von dem § 21 des UStG 1994 entsprechenden  Umsatzsteuervoranmeldungen eine Verkürzung der dargestellten Vorauszahlungen an  Umsatzsteuer bewirkt hat.

| Predicted | Gold |
|---|---|
| `Lucia Artmeyer` | `Lucia Artmeyer` |

**Example 32** (doc_id: `deanon_BFG_20260811_TRAIN/136737.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136737.1_114`)


Allein aus der Tatsache, dass bereits anlässlich einer Vorprüfung die Verwirklichung von  Abgabenhinterziehungen angesprochen wurde, kann nur der Schluss gezogen werden, dass  Herr Lucia Artmeyer  eine Verkürzung der dargestellten Vorauszahlungen an Umsatzsteuer bewirkt  und das nicht nur für möglich, sondern für gewiss gehalten hat.

| Predicted | Gold |
|---|---|
| `Lucia Artmeyer` | `Lucia Artmeyer` |

**Example 33** (doc_id: `deanon_BFG_20260811_TRAIN/137289.1`) (sent_id: `deanon_BFG_20260811_TRAIN/137289.1_8`)


Entscheidungsgründe  Mit Straferkenntnis vom 21. April 2022, Zahl MA67/Zahl/2021, hat der Magistrat der Stadt  Wien, Magistratsabteilung 67, als belangte Behörde Herrn Doris Goerl (in weiterer Folge:  Beschwerdeführer, kurz Bf.) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt in  dem er das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (D) am 21.  Dezember 2021 um 20:06 Uhr in einer gebührenpflichtigen Kurzparkzone in 1010 Wien, Mölker  Bastei gegenüber 5, abgestellt habe ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Doris Goerl` | `Doris Goerl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien, Magistratsabteilung 67` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/128730.1`) (sent_id: `deanon_BFG_20260811_TRAIN/128730.1_5`)


Entscheidungsgründe  Zum Erkenntnis: Mit Bescheid des Finanzamtes Lilienfeld St. Pölten vom 7. Mai 2013 wurden  die Anspruchszinsen 2007 für die Einkommensteuernachforderung 2007 von Herrn Nord Keltri,  nunmehr Nord Keltri (in weiterer Folge: Bf.) in einer Höhe von € 27.080,78 festgesetzt.

**False Positives:**

- `Nord Keltri` — type mismatch — same span as gold: `Nord Keltri`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `Nord Keltri`(organisation)
- `Nord Keltri`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129571.1_4`)


Laut Firmenbuchauszug ist Herr Mag. WD Geschäftsführer seit 23.7.2009.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/129571.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129571.1_49`)


Im Firmenbuch ist Herr Mag. WD als Geschäftsführer seit x.2009 eingetragen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/129937.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129937.1_12`)


Der Herr Name schon geholfen mir, aber blöd gemacht, die Parkscheine etwas zaubern, ich hab  keine Ahnung was oder wie gemacht, aber er ziehen mir immer Geld wegen Parkscheine +  helfen, ich hab mit Hrn.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/130332.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130332.1_44`)


Dies bestätigt auch ihr Vorgesetzter Herr Mag. … . Der Diplomlehrgang diente also  konkret dazu, den Arbeitsplatz zu sichern und zu erhalten und war daher beruflich notwendig.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/131396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131396.1_110`)


Für die Fortsetzung der Prüfung wurde die Prüferin auf Herrn  Mag A. verwiesen, die steuerliche Vertretung gab bekannt, die USO, auch mangels Kapazitäten,  nicht durchzuführen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/132537.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132537.1_28`)


Mit fristgerechter E-Mail vom 17. Februar 2021 führte der Bf. die drei vorgenannten GZen an  und brachte vor:  „Zu dieser Zeit habe ich in Linz gewohnt und gearbeitet und das Auto mit dem Kennzeichen 123  habe ich für einige Wochen Herrn Herr, geboren am geb überlassen, da er damals neu in  Österreich war und er das Auto nötiger hatte als ich.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260811_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132647.1_16`)


1) Höhe der 2014 in Österreich Steuerpflichtigen Bezüge aus nicht selbständiger Arbeit   Herr Bf. erzielte auch in 2014 Einkünfte aus nichtselbständiger Arbeit als angestellter  Staatsanwalt aus Dienstverhältnissen zu zwei Schweizer Körperschaften öffentlichen Rechtes  (Kanton Nidwalden und Bund).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260811_TRAIN/132647.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132647.1_171`)


Wie den vorgelegten  Einkommensteuererklärungen und späteren Berufungen/Beschwerden entnommen werden  kann, sind Herrn Zavadil Einkünfte niemals unbesteuert geblieben: Österreich besteuert das  Welteinkommen, einerseits im Wege der Anrechnungsmethode, andererseits im Wege der  Befreiungsmethode.

**False Positives:**

- `Zavadil Einkünfte` — partial — gold is substring of pred: `Zavadil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zavadil`(person)

**Example 9** (doc_id: `deanon_BFG_20260811_TRAIN/132743.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132743.1_73`)


Im Schreiben der Privatklink vom 21. Oktober 2019 wird auszugsweise ausgeführt:  "Herr Prof. Julian Trapp  stellte sich bei uns am 07.11.2017 erstmals vor.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Julian Trapp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Julian Trapp`(person)

**Example 10** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_7`)


Unbeschränkt haftende Gesellschafter der Bf. waren bis 9.7.2016 Herr VornameGeser1  NachnameGeser1 und bis 28.9.2012 Herr Geser2.

**False Positives:**

- `Vorname` — no gold match — likely missing annotation
- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_10`)


der KomplementärGes m.b.H. ist seit ihrer Gründung im Jahr 2013 Herr VornameGeser1  NachnameGeser1;

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_11`)


ihr Gesellschafter war bis 24.6.2016 zu 100% Herr VornameGeser1  NachnameGeser1;

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_36`)


In dieser Niederschrift wurde festgehalten, dass lediglich Herr NachnameGeser1 mit diesem  Auto fuhr.

**False Positives:**

- `Nachname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_83`)


Das streitgegenständliche Kfz wurde nur von Herrn VornameGeser1 NachnameGeser1  gefahren, welcher   im Streitjahr 2011 als einer der beiden unbeschränkt haftenden Gesellschafter der Bf.  maßgebenden Einfluss auf die Bf. hatte;

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_88`)


Wie aus dem Beschwerdeverfahren des BFG zu GZ. RV/4100396/2016 – betreffend die  Vorschreibung von Kfz-Steuer und NoVA an Herrn NachnameGeser1 wegen Privatnutzung des  nicht angemeldeten, streitgegenständliche Kfz durch das Finanzamt Spittal Villach –  hervorgeht, präsentierte Herr NachnameGeser1 das streitgegenständliche Kfz von 2011 bis  2015 jährlich beim Sportwagentreffen in KärntnerOrt, wobei er sich einen Verkaufspreis von  ca. 300.000,00 € vorstellte.

**False Positives:**

- `Nachname` — no gold match — likely missing annotation
- `Nachname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)
- `Finanzamt Spittal Villach`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_90`)


Primäre Zweckbestimmung des streitgegenständlichen Kfz, welches sich ab dem Erwerb im  Jahr 2011 bis zum Verkauf im Jahr 2016 im zivilrechtlichen Eigentum der Bf. befand, war die  Ermöglichung der Nutzung durch Herrn VornameGeser1 NachnameGeser1, welcher wie ein  Eigentümer über das Kfz verfügte.

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_94`)


Es ist auch daraus zu  schließen, dass der zivilrechtliche Verkauf des Kfz von der Bf. an die KomplementärGes m.b.H.  im Jahr 2016 nichts daran änderte, dass Herr NachnameGeser1 weiterhin – nunmehr als  Geschäftsführer der KomplementärGes m.b.H. – vollen Zugriff auf das Kfz hatte.

**False Positives:**

- `Nachname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_95`)


Daraus resultiert, dass das streitgegenständliche Kfz vom Kauf im Jahr 2011 bis zum Verkauf im  Jahr 2016 nicht im wirtschaftlichen Eigentum der Bf., sondern im wirtschaftlichen Eigentum  von Herrn NachnameGeser1 gestanden ist.

**False Positives:**

- `Nachname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260811_TRAIN/132794.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132794.1_101`)


vielmehr stand es im wirtschaftlichen  Eigentum des Herrn VornameGeser1 NachnameGeser1.

**False Positives:**

- `Vorname` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260811_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133459.1_72`)


Während die nach der AP an den Masseverwalter der L- GmbH i.L. ergangenen Bescheide  unbekämpft in Rechtskraft erwuchsen, brachte die T-Datenverarbeitungs GmbH gegen die  KeSt-Bescheide 2007-2009 namens des Bf fristgerecht Berufung ein, die in einem  nachgereichten Schriftsatz wir folgt begründet wurde:  „Wir als Vertretung (Vollmacht liegt auf) und im Auftrag und Rücksprache mit Herrn  Rinaldo Vollenhals, Bakk. phil., legen wir folgenden Sachverhalt dar:  Tz. 4 Kapitalertragssteuer verdeckte Gewinnausschüttung  Jahr 2007  1.)

**False Positives:**

- `Rinaldo Vollenhals` — partial — pred is substring of gold: `Rinaldo Vollenhals, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rinaldo Vollenhals, Bakk. phil.`(person)

**Example 21** (doc_id: `deanon_BFG_20260811_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133459.1_100`)


Zusammenfassend muss schon gesagt werden, dass von der Seite der Buchhaltungsführung  durch die Kanzlei XY zu groben Fehlern gekommen ist die Herrn Beschwerdeführer nicht  bekannt sein konnten, da er im vollen Vertrauen die Firmenunterlagen zur Bearbeitung  abgegeben hat und diese Arbeiten naturgemäß nicht geprüft hat.

**False Positives:**

- `Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260811_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133459.1_101`)


Das auch wie der Kunde, A.- Fenster sonderliche Buchungen durchgeführt hat, ist auch nicht Herrn Beschwerdeführer zu  zuschreiben.

**False Positives:**

- `Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260811_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133459.1_102`)


Grundsätzlich sind gewisse Gegebenheiten zu bemängeln, aber es ist Herrn  Beschwerdeführer in keiner Weise eine verdeckte Gewinnausschüttung an zu lasten.

**False Positives:**

- `Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260811_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133459.1_104`)


Herr Rinaldo Vollenhals, Bakk. phil.  ersucht daher höflich um Aufhebung der Bescheide über die Festsetzung der  Kapitalertragssteuer für die Jahre 2007 über € 17.853,95, sowie für 2008 über € 20.933,35 und  2009 über € 8.350,00.“

**False Positives:**

- `Rinaldo Vollenhals` — partial — pred is substring of gold: `Rinaldo Vollenhals, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rinaldo Vollenhals, Bakk. phil.`(person)

**Example 25** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_340`)


Auch im Ermittlungsverfahren des Landesgerichts für Strafsachen, das letztendlich  zum Freispruch von Herrn GeserGf1 geführt habe, habe in der mündlichen Verhandlung  glaubhaft gemacht werden können, dass kein Vertreter der Bf. als faktischer Geschäftsführer  und Dienstgeber der beauftragten Subunternehmen anzusehen gewesen sei.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts für Strafsachen`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_344`)


Bei der Darstellung der Beweiswürdigung  durch das Gericht im oben angeführten Strafverfahren, die letztendlich zum Freispruch von  Herrn GesGfEins geführt habe, stelle sich dieser Sachverhalt ganz anders dar: „Alle Fotos  betreffend SubUnt1 in Betracht ziehend ist zu bemerken, dass der Angeklagte jedenfalls nicht  zu sehen ist auf 18 Bildern zu Vorgängen im Zeitraum 6. Oktober 2008 bis 27. Oktober 2008,  während er nur auf dem Foto vom 27.10.2008 um 11:32:40 Uhr zu sehen ist.

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_425`)


Mit Schreiben vom 25.6.2018 brachte die Bf. – vertreten von  zweiteSteuerberatungsgesellschaft in Abstimmung mit der steuerlichen Vertretung der Bf. –  beim BFG ergänzende Vorbringen ein:  Aus Anlass der sich aufgrund der Außenprüfung ergebenden Steuernachforderung sei es zu  einem gerichtlichen Strafverfahren (strafbestimmender Wertbetrag insgesamt 1.287.404 €)  gekommen, in welchem der Geschäftsführer der Bf., Herr GesGf1 mangels Schuldbeweises  nach ungewöhnlich kurzer Urteilsberatung freigesprochen worden sei (Verweis auf LGSzahl2  vom 2. September 2014).

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_426`)


Des Weiteren sei Herr GeserGf1 auch vom Vorwurf der betrügerischen Krida freigesprochen  worden.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_427`)


Im 70-seitigen Urteil vom 17. Jänner 2012 (0LGSzahl1 h) fänden sich u.a. folgende  Argumente für den Freispruch und damit zur Frage, ob sich Herr GeserGf1 mit den  Subunternehmen SubUnt1 und SubUnt2 Scheinfirmen bedient habe, wie dies die  Finanzbehörde angenommen habe:   Herr GeserGf1 sei weder der faktische Geschäftsführer noch der Dienstgeber der  genannten Subunternehmer gewesen, weil nicht festgestellt habe werden können, dass  er die Dienstnehmer zur WGKK und BUAK angemeldet habe oder anmelden habe lassen  und/oder die Löhne an sie ausbezahlt habe bzw. insgesamt die Gebarung der  Gesellschaften durchgeführt habe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation
- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WGKK`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_428`)


 Insgesamt seien 11 Geschäftsführer anderer Unternehmen aus der Branche und  70 Arbeiter über die Wahrnehmungen bei den Firmen SubUnt1 und SubUnt2 befragt  worden, die einhellig ausgesagt hätten, mit Herrn GeserGf1 nichts zu tun gehabt zu  haben bzw. ihn überhaupt nicht zu kennen.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_429`)


Kein einziger der Arbeiter habe Herrn  GeserGf1 als ,,Chef“ bezeichnet, was in einem relativ kleinen Unternehmen sehr  bemerkenswert sei.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_430`)


 Die Finanzbehörde berufe sich auf Videobeweise, wonach die ,,vorgeschobenen“  Geschäftsführer von SubUnt1 und SubUnt2 Abhebungen vom Bankkonto durchgeführt  hätten und Herr GeserGf1 die abgehobenen Beträge unmittelbar danach vor Ort wieder  kassiert habe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_431`)


Laut Gerichtsurteil sei Herr GeserGf1 jedoch nur einmal auf einem Foto  zu sehen gewesen (und auf allen anderen nicht), was seine Erklärung nachvollziehbar  mache, dass er in eigener Sache in dieser Bank zu tun gehabt habe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_432`)


 Auch die Erhebungen zur finanziellen Situation von Herrn GeserGf1 ließen den Schluss  nicht zu, dass durch Barabhebungen Gelder – nach Abzug der Löhne für die Arbeiter –  in seiner Sphäre verschwunden seien.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_433`)


 Herr GeserGf1 schildere in einer Befragung seine Wahrnehmung der Verantwortlichkeit  und seine gelebte Sorgfaltspflicht im Umgang mit Subfirmen bei der  Geschäftsanbahnung, was im krassen Gegensatz zu den rechtlichen Würdigungen in  den Niederschriften der Finanzbehörde stehe und welche dem Freispruch nicht im  Wege gestanden sei und damit offenbar glaubwürdig erschienen sei.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_438`)


 Deren Aussagen seien hinsichtlich der strittigen Frage, ob Herr GesGf1 faktischer  Geschäftsführer bei zumindest zwei Subunternehmern war, verneinend und inhaltlich  kongruent gewesen   Der Umfang und die Intensität des Beweisverfahrens im Strafverfahren seien im  Vergleich zum Betriebsprüfungsverfahren insofern größer gewesen, als die  Betriebsprüfung die Sachverhalte ausschließlich im Vorhalteverfahren erhoben und nur  Gespräche mit der Geschäftsführung der Bf. und der steuerlichen Vertretung geführt  habe.

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_523`)


Er gab an, dass seine Ansprechperson bei SubUnt1 ein Herr  SubUnt1 gewesen sei und dass er nicht mehr wisse, wer bei SubUnt2 die  Ansprechperson gewesen sei.

**False Positives:**

- `Sub` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_557`)


Aus Seite 18 aao: Die vorsitzende Richterin fragte den Angeklagten, ob sich Herr  GeserGfSubUntZwei um seine GmbH (SubUnt2) ordentlich gekümmert habe oder ob der  Angeklagte auch geholfen habe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_558`)


Der Angeklagte antwortete, dass Herr GeserGfSubUntZwei  sich gekümmert habe, was die Baustelle betroffen habe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_560`)


Aus Seite 18 ff. aaO: Die vorsitzende Richterin fragte den Angeklagten, warum er mit Herrn  GeserGfSubUntZwei in der Bank war.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_561`)


Der Angeklagte antwortete, dass er Herrn  GeserGfSubUntZwei im Voraus immer Geld geborgt habe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_562`)


Er sei mitgewesen, damit Herr  GeserGfSubUntZwei ihm das zurückgebe.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_563`)


Herr GeserGfSubUntZwei habe ihm immer einen  Zettel für das ausgeborgte Geld unterschrieben.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_570`)


Vorsitzende Richterin: „Waren Sie so gut befreundet mit dem Herrn GeserGfSubUntZwei?

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_601`)


Haben Sie diese Behebungen mit der Karte von Herrn  GeserGfSubUntZwei gemacht?“

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_650`)


Staatsanwalt: „Wie soll Herr GeserGfSubUntZwei von der Firma SubUnt2 jemanden bezahlen,  wenn sie das abheben?

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_751`)


Als deren Chef, der ihm  auch den Lohn ausbezahlt habe, erkennt er auf einem vorgehaltenen Foto Herrn  GesGfSubUnt1, ohne dessen Namen zu kennen.

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_774`)


Den Lohn und die  Anweisungen was zu tun sei, habe er von einem Herrn Jovan bekommen.

**False Positives:**

- `Jovan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_791`)


Der Chef dort sei ein  Herr SubUnt1 gewesen.

**False Positives:**

- `Sub` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_891`)


Herr GeserGf1 zur Bankkarte der SubUnt2: Die habe er nur gehabt, wenn er Herrn  GeserGfSubUntZwei Geld geborgt hatte.

**False Positives:**

- `Geser` — no gold match — likely missing annotation
- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 51** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_892`)


Herr GeserGf1 zu Telefonaten mit Lohnbüro Lohnbüro betreffend SubUnt1: Das sei nur zwei-  bis dreimal gewesen.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_894`)


Herr GeserGf1 zu USB-Sticks: Diese und das Notebook habe Herr spätererGesGfSubUnt1 am  Rücksitz seines Autos vergessen.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_898`)


Herr GeserGf1 legte dem Richter einen Ordner vor mit den Unterlagen zu den  Subunternehmern: Firmenbuchauszüge, Gewerbeberechtigungen, Kopien von Reisepässen,  etc. wie auch im Arbeitsbogen der Betriebsprüferin eingescannt vorhanden.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_925`)


 zwei (Zeuge22, Zeuge34) einen Janos als Lohnauszahler bzw. Chef der SubUnt1;   zwei (Zeuge55, Zeuge31) Herrn SubUnt1 als Chef;   sieben (Zeuge53, Zeuge24, Zeuge25, Zeuge26, Zeuge28, Zeuge36, Zeuge37, Zeuge42,  zeuge50) GesGfSubUnt1 als Chef  J/a2) GesGf1 nahm an den Verwaltungsarbeiten der SubUnt1 teil und war an der Erstellung der  Ausgangsrechnungen der SubUnt1 beteiligt.

**False Positives:**

- `Sub` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_958`)


Den Erklärungsversuchen, wonach GesGf1  dem handelsrechtlichen Geschäftsführer der SubUnt2, Herrn GeserGfSubUnt2, Geld  geborgt habe, für welches er die Bankkarte als Sicherheit bekommen habe, und wonach  er nur das hergeborgte Geld mit der Bankkarte abhoben habe, wird hier nicht gefolgt  und werden diese Erklärungsversuche als Schutzbehauptungen gewertet.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_1028`)


Bei einem Teil der beanstandeten Subunternehmer war Herr SubUnt31, der selbst auch  unbeanstandeter Subunternehmer war, der gewerberechtliche Geschäftsführer.

**False Positives:**

- `Sub` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260811_TRAIN/133721.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133721.1_1029`)


Bei einem Teil  der beanstandeten Subunternehmer war Herr GeserGf2 (einer der beiden Gesellschafter- Geschäftsführer der Bf.) der gewerberechtliche Geschäftsführer.

**False Positives:**

- `Geser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260811_TRAIN/134477.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134477.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 18. Dezember 2018 forderte das Finanzamt Herrn Linn Leukhardt, Bakk. rer. nat.  (Beschwerdeführer) auf, einen Beweis zu erbringen, dass im haftungsgegenständlichen  Zeitraum alle Gläubiger der Primärschuldnerin GmbH (Primärschuldnerin) gleichmäßig  befriedigt worden seien (Gläubigergleichbehandlung).

**False Positives:**

- `Linn Leukhardt` — partial — pred is substring of gold: `Linn Leukhardt, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linn Leukhardt, Bakk. rer. nat.`(person)

**Example 59** (doc_id: `deanon_BFG_20260811_TRAIN/134652.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134652.1_39`)


erschienen, dabei habe er mit Herrn Herr gesprochen und ihm den Zahlschein vorgelegt.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260811_TRAIN/134896.1`) (sent_id: `deanon_BFG_20260811_TRAIN/134896.1_27`)


Mit der  Vorhaltbeantwortung vom 10.09.2018 von Herrn StB, wurde die Wohnsitzqualität [des Bf.]  nochmals wie folgt ausführlich dargestellt:  >Wie mir mein deutscher Steuerberaterkollege mitteilt, hat das Finanzamt Ebersberg die  Qualifikation der Wohnsitze meines Mandanten zwecks Zuordnung der von ihm erzielten  Einkünfte in der Vergangenheit ausführlich geprüft und ist dabei zu dem Schluss gekommen,  2 von 20 Seite 3 von 20

**False Positives:**

- `St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260811_TRAIN/135338.1`) (sent_id: `deanon_BFG_20260811_TRAIN/135338.1_8`)


zuständige Herr Prokurist der Bank war auf Urlaub) konnte ich die Grunderwerbsteuer erst  etwas später überweisen.

**False Positives:**

- `Prokurist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260811_TRAIN/136679.1`) (sent_id: `deanon_BFG_20260811_TRAIN/136679.1_80`)


An der Adresse adr10 wohnt nach Angaben  von bb ein Herr Morgan U mit Frau B.  Mit Vorhaltsbeantwortung vom 3.12.21 führt der Bf. aus, er habe bei einem Besuch seines  Freundes in Stockholm im November 2021 Geld erhalten, welches er stellvertretend einzahlen  würde.

**False Positives:**

- `Morgan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260811_TRAIN/137100.1`) (sent_id: `deanon_BFG_20260811_TRAIN/137100.1_19`)


Zum  Masseverwalter wurde Herr Levi LomannB, Adr bestellt.  Gesellschafter der BF GmbH sind Herr C D und die Verlassenschaft nach E F. Geschäftsführer  waren Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `Levi Lomann` — partial — pred is substring of gold: `Levi LomannB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi LomannB`(person)

**Example 64** (doc_id: `deanon_BFG_20260811_TRAIN/137100.1`) (sent_id: `deanon_BFG_20260811_TRAIN/137100.1_56`)


Die von Herrn Dr. K zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260811_TRAIN/137682.1`) (sent_id: `deanon_BFG_20260811_TRAIN/137682.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Frauke Sitz, Bakk. iur., geb. 1970, Purbachgasse 7, 8960 Berg, Österreich  vertreten durch APP Steuerberatung GmbH  Schenkenstraße 4 Tür 6, 1010 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 20. Februar 2021 gegen das Erkenntnis des Spruchsenates beim  ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes  Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 11. November 2020, SpS 20, FV-001  091 704, nach Durchführung einer mündlichen Verhandlung am 14. Juni 2022 in Anwesenheit  des Beschuldigten, seines Verteidigers, des Amtsbeauftragten sowie der Schriftführerin zu  Recht erkannt:   Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das nunmehr beim Amt für Betrugsbekämpfung als Finanzstrafbehörde zur Geschäftszahl FV- 001 091 704 geführte Finanzstrafverfahren wegen des Verdachtes, vorsätzlich unter Verletzung  der Verpflichtung zur Abgabe von gemäß § 21 UStG entsprechenden Voranmeldungen eine  Verkürzung von Umsatzsteuer für 12/2018 in Höhe von € 21.560,18 und für 06/2019 in Höhe  von € 18.265,80 bewirkt zu haben (Spruchpunkt 2), wird das Finanzstrafverfahren gemäß  §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.  Über Herrn Frauke Sitz, Bakk. iur.  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG  eine Geldstrafe in Höhe von € 3.200,00 verhängt.

**False Positives:**

- `Frauke Sitz` — partial — pred is substring of gold: `Frauke Sitz, Bakk. iur.`
- `Frauke Sitz` — similar text (different position): `Frauke Sitz, Bakk. iur.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes`(organisation)
- `Frauke Sitz, Bakk. iur.`(person)
- `Purbachgasse 7, 8960 Berg, Österreich`(address)
- `APP Steuerberatung GmbH`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes  Wien 9/18/19 Klosterneuburg`(organisation)
- `Amt für Betrugsbekämpfung`(organisation)
- `Frauke Sitz, Bakk. iur.`(person)

</details>

---

## `context_person_initials` 

**F1:** 0.003 | **Precision:** 0.300 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `ab16252f`  
**Description:**
Matches person names consisting of initials and a surname (e.g., 'Dr. B.', 'R. in der...').

**Content:**
```
(?:Dr\.|Mag\.|Ing\.|Univ\.-Prof\.|Priv\.-Doz\.|Hon\.-Prof\.|OStR|StR|OMedR|RA|KommR|KzlR|Techn\s+R|LR\d*|Ri\.|R\.|IBV|Maga\.|VetR|MedR|Dipl\.-Ing\.|Dipl\.Kfm\.)\s+([A-Z]\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.300 | 0.001 | 0.003 | 10 | 3 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 7 | 2262 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/129027.1`) (sent_id: `deanon_BFG_20260811_TRAIN/129027.1_27`)


Die Wiederaufnahme erfolgte nach ergänzenden  Ermittlungen hinsichtlich eines allfälligen Veräußerungsgewinnes infolge eines Schreibens  des Masseverwalters (Dr. B.) vom 6. Juli 2010.

| Predicted | Gold |
|---|---|
| `Dr. B.` | `Dr. B.` |

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/130676.1`) (sent_id: `deanon_BFG_20260811_TRAIN/130676.1_12`)


Über BFG-Anfrage beim Polizeikommissariat Protokollstelle Wien, vom 17.04.2020 hinauf teilte  Mag. A., Referat für Kriminal- und Sicherheitspolizei, dem BFG am 21.04.2020 mit, dass ein  Betretungsverbot durch die Anzeige einer Körperverletzung mit dem Vater der Bf.-Kinder als  Täter und den Bf.-Kindern als Opfer bedingt am 09.11.2019, um 10.00 Uhr ausgesprochen  worden wäre.

| Predicted | Gold |
|---|---|
| `Mag. A.` | `Mag. A.` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/131396.1`) (sent_id: `deanon_BFG_20260811_TRAIN/131396.1_145`)


Auf die Frage der BP, warum die  Mietverträge nicht von der Metall Brucklemkraft GmbH direkt abgeschlossen wurden, erklärte der Beschuldigte  im Beisein des Buchhalters Mag. A.: "Mein Vater wollte alles unter Kontrolle haben".

| Predicted | Gold |
|---|---|
| `Mag. A.` | `Mag. A.` |

**Missed by this rule (FN):**

- `Metall Brucklemkraft GmbH` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260811_TRAIN/132838.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132838.1_20`)


Als Beilagen zu der Beschwerde wurden (Beil.1:) die Bestätigung der SRBV GmbH betreffend  verrechnete Leistungen im Jahr 2018 vom 23.01.2019, (Beil.2:) die Krankengeschichte samt  Stellungnahme der Bf. vom 13.09.2019, (Beil. 2/a:) der OP-Bericht des OA Olga Pflugpeil  Herz Jesu-KH  vom 6.12.2001 (Operation an der Wirbelsäule), (Beil.2/b:) der Arztbrief des Prim. Univ.-Prof.  DDr. B., Unfallabteilung Landesklinikum Baden-Mödling vom 06.05.2013   (OP: Oberschenkelknochen- Bruch), (Beil.2/c:) die Niederschrift des Prim. Univ.- Prof.Florens Rybarcsyk  Evangelisches Krankenhaus vom 9.04.2014 zur Operation am Darm vom 8.04.2014,   AZ: 2014/XXXX, (Beil.2/d:) der Befundbericht Therapievorschlag des Dr. Med. Univ. D., Facharzt  für innere Medizin, zum Aortenklappenvitium sowie (Beil.3:) die ersten drei Seiten des  zwischen der Bf. als Residenzbewohnerin und der SRBV abgeschlossenen Vertrages, Ausgabe  2003, übermittelt.   3 von 33 Seite 4 von 33

**False Positives:**

- `Dr. B.` — partial — pred is substring of gold: `Prim. Univ.-Prof.  DDr. B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SRBV GmbH`(organisation)
- `Olga Pflugpeil`(person)
- `Prim. Univ.-Prof.  DDr. B.`(person)
- `Florens Rybarcsyk`(person)

**Example 1** (doc_id: `deanon_BFG_20260811_TRAIN/132838.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132838.1_25`)


Aus dem Arztbrief des Prim. Univ.-Prof. DDr. B., Unfallabteilung des Landesklinikums Baden- Mödling, vom 06.05.2013 (Beilage 2/b) war die nachfolgend abgelichtete Schlussbetrachtung  zur Oberschenkelknochenfraktur zu entnehmen:   „

**False Positives:**

- `Dr. B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260811_TRAIN/132838.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132838.1_144`)


2. Beweiswürdigung  Die Sachverhaltsfeststellungen beruhen auf a) dem Bescheid, mit dem der Bf. Pflegegeld Stufe  1 zuerkannt worden ist, b) den Schreiben der langjährigen Hausärztin Milena von Seefried vom 16.12.2019  und 30.7.2020, c) dem Bericht des OA Olga Pflugpeil  Herz Jesu-KH, vom 6.12.2001 über die Operation  an der Wirbelsäule vom Vortag (Beilage 2/a), d) dem Arztbrief des Prim. Univ.-Prof. DDr. B.,  Unfallabteilung, Landesklinikum Baden Mödling, betreffend die frakturbedingte Operation vom  6.05.2013, e) der Niederschrift des Prim. Univ.- Prof.Florens Rybarcsyk, Evangelisches Krankenhaus, vom  9.04.2014 betreffend die Operation am Darm vom 8.04.2014, f) dem Röntgen-Befund der  Radiologischen Gruppenpraxis Baden OG vom 25.04.2017 (Wirbelsäule), g) dem Befundbericht  des Dr. Med. Univ. D., Facharzt für innere Medizin, vom 9.01.2018, und h) den Aufzeichnungen  zur Kz. 476 im Formular L lab-2018.

**False Positives:**

- `Dr. B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Milena von Seefried`(person)
- `Olga Pflugpeil`(person)
- `Florens Rybarcsyk`(person)

**Example 3** (doc_id: `deanon_BFG_20260811_TRAIN/132838.1`) (sent_id: `deanon_BFG_20260811_TRAIN/132838.1_216`)


Angesichts der Eigenschaft der  Bf. als langjährige Patientin der Milena von Seefried war es der Allgemeinmedizinerin möglich, den  Befundbericht vom 30.07.2020 mit der Darstellung des Status und der Kontinuität der  Behandlung der Bf. zu erstellen und die Angaben durch Vorlage der der Krankengeschichte  beigelegten Beweismittel (a) OP-Bericht des OA Olga Pflugpeil  Herz Jesu-KH, vom 6.12.2001,  b) Arztbrief des Prim. Univ.-Prof. DDr. B. vom 6.05.2013, c) Niederschrift des Prim. Univ.- Prof.Florens Rybarcsyk  Evangelisches KH, vom 9.04.2014, d) Befundbericht des Dr. Med. Univ. D., Facharzt für  innere Medizin, vom 9.01.2018) und den Röntgen-Befund vom 25.04.2017 zu belegen.

**False Positives:**

- `Dr. B.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Milena von Seefried`(person)
- `Olga Pflugpeil`(person)
- `Florens Rybarcsyk`(person)

**Example 4** (doc_id: `deanon_BFG_20260811_TRAIN/133459.1`) (sent_id: `deanon_BFG_20260811_TRAIN/133459.1_99`)


Wegen  detaillierten Leistungsaufzeichnungen müssen wir darauf hinweisen, dass diese nicht vorliegen,  da sämtliche Unterlagen an die neue Geschäftsleitung Herrn R. M. übergeben wurden.

**False Positives:**

- `R. M.` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 5** (doc_id: `deanon_BFG_20260811_TRAIN/135931.1`) (sent_id: `deanon_BFG_20260811_TRAIN/135931.1_56`)


Am 04. November 2019 stellte die Ärztin Dr. F. eine Krankenstandbestätigung für  Zivildienstleistende aus (Bestätigung vom 04.11.2019):  Beginn der Erkrankung    5.11.2019  Voraussichtliche Dauer der Erkrankung  mindestens 6 Monate  Art der Erkrankung  4 von 8 Seite 5 von 8

**False Positives:**

- `Dr. F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260811_TRAIN/135931.1`) (sent_id: `deanon_BFG_20260811_TRAIN/135931.1_62`)


Am 12. Dezember 2019 führte die Ärztin Dr. L. eine Routinekontrolle nach Perimyocarditis mit  stationärer Behandlung in … bis 4.11.2019 durch.

**False Positives:**

- `Dr. L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

