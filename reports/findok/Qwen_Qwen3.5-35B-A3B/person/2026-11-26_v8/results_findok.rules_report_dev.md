# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-26T13:23:04.466119

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-26_v8/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 500 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Training documents | 500 |
| Validation documents | 787 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 1048 |
| Validation sentences | 1787 |
| Dev sentences | 61673 |
| Test sentences | 61001 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | True |
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
| True Positives | 593 |
| False Positives | 107 |
| False Negatives | 1258 |
| Total Gold Entities | 1851 |
| Micro Precision | 84.7% |
| Micro Recall | 32.0% |
| Micro F1 | 46.5% |
| Macro F1 | 46.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `legal_person_judge_title_combined` | 16.8% | 88.7% | 9.3% | 194 | 172 | 22 |
| `legal_person_complainant_context` | 25.5% | 88.2% | 14.9% | 313 | 276 | 37 |
| `legal_person_honorific_context` | 14.2% | 78.0% | 7.8% | 186 | 145 | 41 |
| `legal_person_representative_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `legal_person_preposition_from` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `legal_person_judge_title_combined` 🏆

**F1:** 0.168 | **Precision:** 0.887 | **Recall:** 0.093  

**Format:** `regex`  
**Rule ID:** `0e290b82`  
**Description:**
Captures names following 'durch die Richterin/den Richter' with complex titles, ensuring full name capture including initials.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin)\s+)([A-Z][a-zäöüß]+(?:\s+(?:Hon\.-?Prof\.|Mag\.|Mag\.a|Dr\.|Dr\.in|Univ\.-?Prof\.|Priv\.-?Doz\.|Dipl\.-?Ing\.)?\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+van\s+[A-Z][a-zäöüß]+)*)|(?:Hon\.-?Prof\.|Mag\.|Mag\.a|Dr\.|Dr\.in|Univ\.-?Prof\.|Priv\.-?Doz\.|Dipl\.-?Ing\.)?\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+van\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.887 | 0.093 | 0.168 | 194 | 172 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 172 | 22 | 1679 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_0`)


GZ. RV/5101724/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter Dr. Elias Derneden  in der Beschwerdesache über die Beschwerde vom 14.01.2019 gegen den Bescheid der belangten Behörde vom 04.01.2019 betreffend Familienbeihilfe für den Zeitraum ab März 2018 zu Recht: 1.Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elias Derneden` | `Dr. Elias Derneden` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Mag. Peter Staudinger` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)
- `Finanzamtes Linz` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Kießerling` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Shoshana Leuther` (person)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR OSR Leonie Ercklentz` (person)
- `Karnitzen 135, 9635 Kronhof, Österreich` (address)
- `LKP Steuerberatung OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thomas Hutching` | `Hon.-Prof. Thomas Hutching` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Ruprecht Hauswerth` (person)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Mag. Othmar Feuerbaum` | `Mag. Othmar Feuerbaum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingeborg Kollaczek` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Bogdanowic` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jacqueline Dittus` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joachim Annanias` | `Dr. Joachim Annanias` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Burkhard Krautschenko` (person)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `Mag. Susanne Pöltenstein-Rosenegger` (person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Titus Ohlmer` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edwin Pfaefflin` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Diethard Ringhand` (person)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Hasslbauer` (person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich` (address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich` (address)
- `Procurator Treuhand- und Revisionsges.m.b.H.` (organisation)
- `Bundesministeriums für Finanzen` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Ladwig` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Achmed Karolzak` | `Univ.-Prof. Achmed Karolzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lilia Löffelmann` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Edith Schifferdecker` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich` (address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `73-948/8864` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Christoph Hasenfraz` | `Hon.-Prof. Christoph Hasenfraz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olivia Sahlmüller` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Milena Neidig` (person)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Buedenbender` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fiona Buedenbender` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tristan Potente` (person)
- `Hürth 5, 4362 Schönfichten, Österreich` (address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `61-467/9522` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timothy Overlaender` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Zoltan Dabrowski` | `Priv.-Doz. Zoltan Dabrowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Prof. Hartmut Szardemings` (person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Martin Kuprian` | `Mag. Martin Kuprian` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Werner Böltl` (person)
- `Rydlweg 234, 3860 Dietweis, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Moses Dannebohm` | `Univ.-Prof. Moses Dannebohm` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruperta Schluckner` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Maurice Bettenhäuser` | `Hon.-Prof. Maurice Bettenhäuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miranda Weissert` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Walter Monheim` | `Hon.-Prof. Walter Monheim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Enrico Steudtle` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-940/7308` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Walter Aiglsdorfer` | `Mag. Walter Aiglsdorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hugo Engelsmann` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch Dr. Stephan Riel als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mittel-Verlag` (organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich` (address)
- `Dr. Stephan Riel` (person)
- `Finanzamtes Österreich` (organisation)
- `44-993/1626` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Christian Lemanowitz` | `Univ.-Prof. Christian Lemanowitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dietmar Kachelmuss` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pjotr Astore` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Fassmer` (person)
- `Tillisweg 11, 8773 Sparsbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch Rein & Partner Steuerberatung GmbH & Co KG in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Denis Diekötter` (person)
- `KLG Kreuzbau 16, 8242 Kronegg, Österreich` (address)
- `Rein & Partner Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Günter Jedamczik` | `Univ.-Prof. Günter Jedamczik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Tobias Schönyan` (person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich` (address)
- `Mag. Gernot Thonhauser` (person)
- `Finanzamtes Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 17. September 2020 des Beschwerdeführers Silvester Bartonitz, BEd MBA, Großreifling 222, 8573 Hemmerberg, Österreich  Steuernummer  17-874/6032, vertreten durch den mit Zustellvollmacht ausgewiesenen ****, Adresse,  gegen den Bescheid des Finanzamtes Kirchdorf Perg Steyr (nunmehr Finanzamt Österreich)  vom 17. August 2020 betreffend Haftung für Lohnsteuer 2011 zu Recht:  I)  Der Bescheid betreffend Haftung für Lohnsteuer 2011 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvester Bartonitz, BEd MBA` (person)
- `Großreifling 222, 8573 Hemmerberg, Österreich` (address)
- `17-874/6032` (tax_number)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claire Wienhues` (person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamt` (organisation)
- `61-469/1778` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Tanja Fützenreiter, Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich, über die Beschwerde der Beschwerdeführerin  (Bf.) vom 29. März 2021 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) für  2019 des Finanzamtes Österreich vom 17. März 2021 zur Steuernummer 90-161/7779  zu  Recht erkannt:   Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tanja Fützenreiter` (person)
- `Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `90-161/7779` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerde des  Karim Hainzlmeier, Gälaplana 43, 3205 Mühlhofen, Österreich, gegen den Bescheid des Finanzamtes Bregenz vom 20. Mai 2016  betreffend Einkommensteuer 2015, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karim Hainzlmeier` (person)
- `Gälaplana 43, 3205 Mühlhofen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Melinda Brotke, Jägerloch 26, 8443 Praratheregg, Österreich, vom 22. März 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 3.  März 2021, Zahl MA67/206700943579/2020, wegen einer Verwaltungsübertretung gemäß § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für  Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melinda Brotke` (person)
- `Jägerloch 26, 8443 Praratheregg, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt  Wien` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Nowizki  in der Beschwerdesache Janis Loewenthal,  Georg Grinninger-Straße 15, 3830 Pyhra, Österreich, vertreten durch die [Erwachsenenvertreterin], über die Beschwerde vom  23. August 2019 gegen den Bescheid des Finanzamtes Kitzbühel Lienz (nunmehr: Finanzamt  Österreich) vom 23. Juli 2019 betreffend Familienbeihilfe und Erhöhungsbetrag zur  Familienbeihilfe wegen erheblicher Behinderung ab November 2018, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Zlatan Nowizki` | `Mag. Zlatan Nowizki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janis Loewenthal` (person)
- `Georg Grinninger-Straße 15, 3830 Pyhra, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Juri Boyarzyn, Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich, vom 28. Juli 2020, gegen den Bescheid des Finanzamtes Österreich  vom 16. Juli 2020, betreffend Familienbeihilfe 01.2019-01.2021, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Boyarzyn` (person)
- `Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/137349.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Gebhard Kristupeit, Bakk. techn., Wörndlestraße 17, 9112 Untergrafenbach, Österreich, vertreten durch APP Steuerberatung GesmbH, Schenkenstraße  4, 1010 Wien, über die Beschwerde gegen die Bescheide des Finanzamtes Baden Mödling vom  31. Mai 2011 hinsichtlich Haftung betreffend Kapitalertragsteuer für 2007 und 2008,  Steuernummer 83-002/9356  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Kristupeit, Bakk. techn.` (person)
- `Wörndlestraße 17, 9112 Untergrafenbach, Österreich` (address)
- `APP Steuerberatung GesmbH` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `83-002/9356` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Anton Böckamp, Bakk. techn., Leopold Kunschak Gasse 25, 9343 Dielach, Österreich, über die Beschwerde vom 8. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Gänserndorf Mistelbach, § 323b BAO) vom  25. November 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 84-669/5568  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne des Beschwerdebegehrens  abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Böckamp, Bakk. techn.` (person)
- `Leopold Kunschak Gasse 25, 9343 Dielach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Gänserndorf Mistelbach` (organisation)
- `84-669/5568` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Chen Geßlein  in der Beschwerdesache MedR Techn R Mathilda Elfeldt,  Klingengasse 112, 9556 Waggendorf, Österreich, vertreten durch Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH, Kurandtplatz 1, 9020 Klagenfurt/Wörthersee, über die Beschwerde vom 29. Jänner  2021 gegen den Bescheid des Finanzamt Vorarlberg  vom 18. Jänner 2021 betreffend Einkommensteuer  2019 Steuernummer 43-811/9169  zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Chen Geßlein` | `Mag. Chen Geßlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Techn R Mathilda Elfeldt` (person)
- `Klingengasse 112, 9556 Waggendorf, Österreich` (address)
- `Dr.Baumgartner Wirtschaftstreuhand und Steuerberatungs  GmbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)
- `43-811/9169` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Adolf Brehmer  in der Beschwerdesache VetR Gotthard Lohscheider,  Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich, vertreten durch „Meinrad Kisewetter“ - Steuerberatungsgesellschaft m.b.H., Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich,  über die Beschwerde vom 28.06.2021, gegen den Bescheid des Finanzamtes Österreich vom  27.05.2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm § 111 BAO, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Adolf Brehmer` | `Mag. Adolf Brehmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Gotthard Lohscheider` (person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich` (address)
- `Meinrad Kisewetter` (person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Walter Aiglsdorfer` | `Mag. Walter Aiglsdorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gisbert Löhberg` (person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich` (address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `73-737/2281` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Massimo Friedhoff` | `Univ.-Prof. Massimo Friedhoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Grothmann` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Volkmar Quadfasel, Forstbergstraße 5, 4144 Zanklbach, Österreich, vertreten durch Dr. Sebastian Mariano Volkmar Lenz,  Laurenzerberg 1, 1010 Wien, vom 25. April 2021, gegen den Bescheid des Finanzamtes  Österreich vom 26. März 2021, betreffend Abweisung des Antrages auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe ab Dezember 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Volkmar Quadfasel` (person)
- `Forstbergstraße 5, 4144 Zanklbach, Österreich` (address)
- `Dr. Sebastian Mariano Volkmar Lenz` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Maximiliane Gasparetti, Gschwandtkopf 12, 9330 Althofen, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 23. Dezember 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. November 2016 betreffend  1.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximiliane Gasparetti` (person)
- `Gschwandtkopf 12, 9330 Althofen, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Thomas Schmidt in der Finanzstrafsache  gegen Linda Tumpach, Gengerberg 44, 4052 Ansfelden, Österreich, vertreten durch Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer, Wiener Straße 3, 3100 St. Pölten, über die Beschwerde der Beschuldigten vom  25.11.2019 gegen den Bescheid des Amtes für Betrugsbekämpfung als Finanzstrafbehörde  (ehemals des Finanzamtes Lilienfeld St. Pölten als Finanzstrafbehörde ) vom 17. Oktober 2019,  Strafkontonummer 91-951/0670, betreffend die Abweisung eines  Zahlungserleichterungsansuchens (Stundungs- und Ratenansuchen) gemäß § 156 Abs. 1 des  Finanzstrafgesetzes (FinStrG) in Verbindung mit   § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) beschlossen:  Die Beschwerde wird als unzulässig zurückgewiesen, da es sich beim gegenständlich  bekämpften so genannten Bescheid um einen Nichtbescheid handelt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Thomas Schmidt` | `Mag. Thomas Schmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Linda Tumpach` (person)
- `Gengerberg 44, 4052 Ansfelden, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `91-951/0670` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Richard Reithmayer, Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Bundesstraße  36, 6923 Lauterach, gegen die Bescheide des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer 2015 und 2016 sowie Festsetzung von  Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Richard Reithmayer` (person)
- `Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Herbert Lindermayer  in der Beschwerdesache Anneliese Dreschmann,  Nußbacher Straße 43, 3650 Kehrbach, Österreich, vertreten durch Schwaiger & Partner Steuerberatung, Anton-Eder-Straße 5,  6020 Innsbruck, über die Beschwerde vom 19. Jänner 2021 gegen den Bescheid des FA Graz-Stadt  vom 13. Jänner 2021 betreffend Energieabgabenvergütung 2015 Steuernummer  60-855/1189  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Herbert Lindermayer` | `Priv.-Doz. Herbert Lindermayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anneliese Dreschmann` (person)
- `Nußbacher Straße 43, 3650 Kehrbach, Österreich` (address)
- `Schwaiger & Partner Steuerberatung` (organisation)
- `FA Graz-Stadt` (organisation)
- `60-855/1189` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/138353.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138353.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hubert Wunderlin  in der Beschwerdesache Friedhelm Fomin,  Riedlbachstraße 8, 3970 Oberbrühl, Österreich, vertreten durch ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H., Postfach 257, 1061 Wien Postfach, über die Beschwerde  vom 15. August 2021 gegen den Bescheid des Finanzamtes Österreich vom 13. Juli 2021  betreffend Covid-19 Zahlungserleichterung, Steuernummer 25-245/7156, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Hubert Wunderlin` | `Hon.-Prof. Hubert Wunderlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Friedhelm Fomin` (person)
- `Riedlbachstraße 8, 3970 Oberbrühl, Österreich` (address)
- `ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `25-245/7156` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/138725.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138725.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. David Eckerlin  in der Beschwerdesache Margarete Wasmeir,  Voglstraße 19, 4902 Schlaugenham, Österreich, vertreten durch Mag. Kurt Caspari Steuerberatungs KG, Hirnreit 173, 5771  Leogang, über die Beschwerde vom 29. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 11. Juli 2022 betreffend Säumniszuschlag 2022 Steuernummer 09-312/4413  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. David Eckerlin` | `Univ.-Prof. David Eckerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Margarete Wasmeir` (person)
- `Voglstraße 19, 4902 Schlaugenham, Österreich` (address)
- `Mag. Kurt Caspari Steuerberatungs KG` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `09-312/4413` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Olaf Koechig, Zmöllach 3, 3542 Litschgraben, Österreich, Beschwerde vom 25. Oktober 2019 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr Finanzamtes Österreich, vom  28. November 2018 betreffend Umsatzsteuer 2012, Umsatzsteuer 2013, Umsatzsteuer 2014  und Umsatzsteuer 2015, Steuernummer 17-913/2665, der Gartfentri Heizung Institut GmbH, vertreten durch  Gustke Forschung GmbH, hinsichtlich des Vorlageantrages der Gartfentri Heizung Institut GmbH  in  Liquidation, beschlossen:  I. Die Beschwerdevorentscheidungen vom 6. April 2022 betreffend Umsatzsteuer 2012,  2013, 2014 und 2015 der Gartfentri Heizung Institut GmbH  in Liquidation werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Konrad` | `Mag. Gerhard Konrad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olaf Koechig` (person)
- `Zmöllach 3, 3542 Litschgraben, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `17-913/2665` (tax_number)
- `Gartfentri Heizung Institut GmbH` (organisation)
- `Gustke Forschung GmbH` (organisation)
- `Gartfentri Heizung Institut GmbH` (organisation)
- `Gartfentri Heizung Institut GmbH` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Magdalena Unterreiter, Anichstraße 5, 8953 Donnersbach, Österreich, Deutschland, vom 22. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, als Verwaltungsstrafbehörde vom  10. März 2022, Zl. Zahl, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Magdalena Unterreiter` (person)
- `Anichstraße 5, 8953 Donnersbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/138952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138952.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Paolo Blasenbreu, Ernst-Ludwig-Gasse 176, 7461 Allersgraben, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019, 64-737/5163, beschlossen:   Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paolo Blasenbreu` (person)
- `Ernst-Ludwig-Gasse 176, 7461 Allersgraben, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)
- `64-737/5163` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/138996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 6. Dezember 2012 des Beschwerdeführers DDr.in Pamela Gempp, Bosruckgasse 2, 3121 Heitzing, Österreich  Steuernummer:  82-457/9791, gegen den Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt  Österreich) vom 21. November 2012 betreffend Festsetzung der Kraftfahrzeugsteuer für die  Monate 03/2011 bis 09/2012 zu Recht:    I)  Der Beschwerde wird gem. § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `DDr.in Pamela Gempp` (person)
- `Bosruckgasse 2, 3121 Heitzing, Österreich` (address)
- `82-457/9791` (tax_number)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/139070.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139070.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat in der Revisionssache  Ferdinand Janßon, Robert-Musil-Gasse 10, 4631 Achleiten, Österreich  Steuernummer: 02-858/2848, vertreten durch den RA Mag.  Wolfgang Kempf, Bürgerstraße 41, 4020 Linz, über den Antrag der Revisionswerberin vom 18.  August, der gegen den Beschluss des Bundesfinanzgerichtes vom 5. Juli 2022,  RV/5100264/2021 (belangte Behörde: Finanzamt Österreich), betreffend die  Umsatzsteuerbescheide 2010 – 2017, erhobenen außerordentlichen Revision die  aufschiebende Wirkung zuzuerkennen, den Beschluss:   I)  Gem.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferdinand Janßon` (person)
- `Robert-Musil-Gasse 10, 4631 Achleiten, Österreich` (address)
- `02-858/2848` (tax_number)
- `RA Mag.  Wolfgang Kempf` (person)
- `Bundesfinanzgerichtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Reifgerste` (person)
- `Scherzergütl 18K, 9622 Golz, Österreich` (address)
- `Freimüller Rechtsanwalts GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `M. F.` (person)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Zlatan Tegtmeier  in der Angelegenheit der Parteien  Dipl. Kfm. VetR Gerhard Stranz (Beschwerdeführerin), vertreten durch die   Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H., 9400 Wolfsberg  und Finanzamt Oststeiermark, 1000 Wien, PF 251  als  Amtspartei über die Beschwerden vom 12.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Zlatan Tegtmeier` | `Hon.-Prof. Zlatan Tegtmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kfm. VetR Gerhard Stranz` (person)
- `Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamt Oststeiermark` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/139889.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139889.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 29. Dezember 2021 des Beschwerdeführers Ashley Claesson, Adr BF, Steuernummer:  66-163/5550, gegen den Bescheid des Finanzamtes Österreich vom 1. Dezember 2021  betreffend Einkommensteuer 2020 zu Recht:    I)  Der Beschwerde wird gem. § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ashley Claesson` (person)
- `66-163/5550` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Techn R Christina Heising, Angerweg 46, 4672 Unterseling, Österreich, vom 13. Februar 2023, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 23. Jänner 2023, Zahl MA67/Zahl1/2022, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für  Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Christina Heising` (person)
- `Angerweg 46, 4672 Unterseling, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/140642.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140642.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Emanuel Gentner  in der Beschwerdesache Alva Selmayr,  Hatscheksiedlung 9, 8524 Gamsgebirg, Österreich, vertreten durch at reutte Steuerberatungs GmbH, Unterdorf 1, 6600  Lechaschau, gegen den von der belangten Behörde Finanzamt Österreich am 30. September  2022 zu Steuernummer 35-106/4702  ausgefertigten Einkommensteuerbescheid 2019 zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 Abs. 1 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Emanuel Gentner` | `Univ.-Prof. Emanuel Gentner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alva Selmayr` (person)
- `Hatscheksiedlung 9, 8524 Gamsgebirg, Österreich` (address)
- `at reutte Steuerberatungs GmbH` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-106/4702` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 14. Dezember 2021 der Beschwerdeführerin Hon.-Prof. Igor Rockermair, Myrthengasse 17, 9121 Hungerrain, Österreich  Steuernummer:  95-241/7343, vertreten durch die FUSSEIS Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 63, 4910 Ried im Innkreis, gegen die  Bescheide des Finanzamtes Österreich vom 30. November 2021 betreffend Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2018 – 2020  zu Recht:  I)  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Igor Rockermair` (person)
- `Myrthengasse 17, 9121 Hungerrain, Österreich` (address)
- `95-241/7343` (tax_number)
- `FUSSEIS Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/140867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140867.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Philipp Nosalek  in der Beschwerdesache Merlin Buechner,  Am Waldfriedhof 19-24, 4714 Gferet, Österreich, vertreten durch Dr. Martin Eisenberger, Muchargasse 30, 8010 Graz, über die  Beschwerde vom 17. Mai 2017 gegen den Bescheid des Zollamtes Österreich vom 11. April  2017, Zl. 700000/03287/2017, betreffend Aussetzungszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Philipp Nosalek` | `Hon.-Prof. Philipp Nosalek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Merlin Buechner` (person)
- `Am Waldfriedhof 19-24, 4714 Gferet, Österreich` (address)
- `Dr. Martin Eisenberger` (person)
- `Zollamtes Österreich` (organisation)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/141161.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141161.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor in der Beschwerdesache  Li Wilmering, Pichlernstraße 1, 4751 Stögen, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid  des Finanzamtes Wien 1/23 vom 21. Jänner 2020 betreffend Abweisung eines Antrages auf  Familienbeihilfe, Oktober 2019 bis Jänner 2020 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Christian Doktor` | `Mag. Christian Doktor` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Li Wilmering` (person)
- `Pichlernstraße 1, 4751 Stögen, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/141222.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141222.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Dipl. Kfm. Joshua Klesius, Gartln 5, 9554 Reggen, Österreich, vom 22. Mai 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 25.  April 2023, GZ. MA67/Zahl1/2023, betreffend eine Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF ABl. der Stadt  Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien  Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht:    I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der angefochtene Bescheid  dahingehend abgeändert, dass die verhängte Geldstrafe von 60,00 Euro auf 36,00 Euro und die  für den Fall der Uneinbringlichkeit festgesetzte Ersatzfreiheitsstrafe von 14 auf 8 Stunden  herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kfm. Joshua Klesius` (person)
- `Gartln 5, 9554 Reggen, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt  Wien` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck über die Beschwerde des  Maximilian Mlynarzyk, Kellersteig 6O, 9063 Techmannsdorf, Österreich, vom 7. Juni 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 9.  Mai 2023, GZ. MA67/GZ/2023, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde Folge gegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 1 VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 2 VwGVG iVm § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Mag. Johannes Böck` | `Mag. Johannes Böck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximilian Mlynarzyk` (person)
- `Kellersteig 6O, 9063 Techmannsdorf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/141318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Lara Blaßl, Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich, vertreten durch Dr. Michl Münzker, Landskrongasse 5 Tür 4, 1010  Wien, über die Beschwerde vom 24. Juni 2021 gegen den Bescheid des Finanzamtes Österreich  vom 17. Juni 2021 betreffend Festsetzung einer Zwangsstrafe, Steuernummer  54-324/8831, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lara Blaßl` (person)
- `Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich` (address)
- `Dr. Michl Münzker` (person)
- `Finanzamtes Österreich` (organisation)
- `54-324/8831` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Jürgen Thesen, Mobilheimplatz B III 41, 9702 Nußdorf, Österreich, über die Beschwerde vom 19. Juli 2021 gegen die Bescheide des  Finanzamtes Österreich vom 21. Juni 2021 betreffend Umsatzsteuer 2019 und 2020 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jürgen Thesen` (person)
- `Mobilheimplatz B III 41, 9702 Nußdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/141586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaromir Hendl  in der Beschwerdesache KommR Univ.-Prof. Leander Wehe,  Mahlhofweg 9, 8863 Mitterberg, Österreich, über die Beschwerde vom 23. März 2023 gegen den Bescheid des FA Graz-Stadt  vom 9. März 2023 betreffend Säumniszuschlag 2023 Steuernummer 61-179/3197  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Jaromir Hendl` | `Mag. Jaromir Hendl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Univ.-Prof. Leander Wehe` (person)
- `Mahlhofweg 9, 8863 Mitterberg, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `61-179/3197` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/141855.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141855.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Jaden Savvopoulou, Meiselhueb 28, 3524 Grainbrunn, Österreich, über die Beschwerde vom 3. Dezember 2021 gegen den Bescheid  des Finanzamtes Österreich vom 19. November 2021 betreffend Abweisung des Antrages auf  Aufhebung des Bescheides über die Feststellung von Einkünften 2020 vom 23. Juli 2021 gemäß  § 299 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Savvopoulou` (person)
- `Meiselhueb 28, 3524 Grainbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/142063.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142063.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Frauke Glowatsch, St.Georgen a.W. 12, 4776 Großwaging, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 11.6.2019  und 26.11.2019 gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt  Österreich;

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frauke Glowatsch` (person)
- `St.Georgen a.W. 12, 4776 Großwaging, Österreich` (address)
- `Pallauf Meißnitzer Staindl & Partner` (organisation)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Silke Czejka, Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich, vom 01. September 2022 gegen den Bescheid des Finanzamtes  Österreich vom 30. August 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Monat Mai 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silke Czejka` (person)
- `Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des StR Sabine Lenertz, Am Großboden 22R, 4070 Oberhillinglah, Österreich, vertreten durch TU Pircher & Partner Steuerberatungs GmbH,  Anton-Melzer-Straße 7, 6020 Innsbruck, über die Beschwerde vom 14. April 2023 gegen den  Abweisungsbescheid 2022 des Finanzamtes Österreich vom 17.03.2023, mit dem der Antrag  vom 15.03.2023 auf Aufhebung nach § 299 BAO des Umsatzsteuerfestsetzungsbescheids  01/2022 vom 14.04.2022 abgewiesen wurde, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Sabine Lenertz` (person)
- `Am Großboden 22R, 4070 Oberhillinglah, Österreich` (address)
- `TU Pircher & Partner Steuerberatungs GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Imre Plönnes  in der Beschwerdesache  Jason Oberbüscher, Joseph-von-Wörndle-Weg 23, 4342 Kolbing, Österreich, über die Beschwerde vom 11. April 2023 gegen den Bescheid des  Finanzamtes Österreich vom 13. März 2023 betreffend Einkommensteuervorauszahlungen  2023 und Folgejahre, Steuernummer 88-942/0644, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Imre Plönnes` | `Priv.-Doz. Imre Plönnes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jason Oberbüscher` (person)
- `Joseph-von-Wörndle-Weg 23, 4342 Kolbing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-942/0644` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/142566.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142566.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Emmerich Bublies  in der Beschwerdesache Olaf Leier,  Angerwies 34, 5143 Wiesing, Österreich, vertreten durch Göbel & Hummer Rechtsanwälte OG, Weihburggasse 9, 1010  Wien, betreffend Beschwerde vom 23. Dezember 2022 gegen den Bescheid des Finanzamtes  Österreich vom 12. Dezember 2022 betreffend Festsetzung einer Zwangsstrafe den Beschluss:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Emmerich Bublies` | `Mag. Emmerich Bublies` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olaf Leier` (person)
- `Angerwies 34, 5143 Wiesing, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/142576.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142576.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Carla Würtele, Herta-Nest-Straße 15, 8046 Ursprung, Österreich, vom 23. Oktober 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 13. Oktober 2023,  GZ. MA67/Zahl/2023, wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Carla Würtele` (person)
- `Herta-Nest-Straße 15, 8046 Ursprung, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/142680.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142680.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Moritz Lindstaedt  in der Beschwerdesache Samuel Rattai,  Hilzing 64, 2880 Kranichberg, Österreich, vertreten durch Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH, Lehargasse 3A Tür 14, 1060 Wien, über die Beschwerde vom  7. September 2023 gegen den Bescheid des Finanzamtes Österreich vom 30. August 2023  betreffend Zahlungserleichterungen gem. § 212 BAO, Steuernummer 30-750/1577, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Moritz Lindstaedt` | `Hon.-Prof. Moritz Lindstaedt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Rattai` (person)
- `Hilzing 64, 2880 Kranichberg, Österreich` (address)
- `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `30-750/1577` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/142990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Heidrun Skowronneck, Zimmerbergsiedlung 30P, 3592 Gobelsdorf, Österreich  über die Beschwerde vom 10. Mai 2022 gegen den  Zurückweisungsbescheid des Finanzamtes Österreich vom 22. März 2022 betreffend Antrag  gemäß § 295 Abs 4 BAO auf Aufhebung des Einkommensteuerbescheides 2003 (ergangen am  17.11.2009), Steuernummer 44-117/9037, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Zwilling` | `Mag. Josef Zwilling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heidrun Skowronneck` (person)
- `Zimmerbergsiedlung 30P, 3592 Gobelsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `44-117/9037` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Bodo Heumaier  in der Angelegenheit der Parteien  KzlR HR Lothar Schoeberl, PLZ1 Stadt1 (Beschwerdeführerin), und FA Braunau Ried Schärding  als Amtspartei über die  Beschwerde vom 25.8.2022   gegen den Bescheid des Finanzamtes vom 4.8.2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016   zu Recht erkannt:  Der bekämpfte Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Bodo Heumaier` | `Mag. Bodo Heumaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR HR Lothar Schoeberl` (person)
- `FA Braunau Ried Schärding` (organisation)
- `Finanzamtes` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Madeleine Jahns, Roter Wolf Straße 28, 8422 Hütt, Österreich, vertreten durch Reiner & Reiner Steuerberatungs GmbH,  Schillerstraße 22, 6890 Lustenau, über die Beschwerde vom 2. Juni 2015 gegen den  Verwaltungskostenbeitragsbescheid des Finanzamtes Feldkirch vom 4. Mai 2015, zu Recht  erkannt:  I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Jahns` (person)
- `Roter Wolf Straße 28, 8422 Hütt, Österreich` (address)
- `Reiner & Reiner Steuerberatungs GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/143284.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143284.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Miklos Fölker  in der Beschwerdesache Wilma Husemann,  Oberregau 2, 9702 Laas, Österreich, vertreten durch r.m-s consulting gmbh, Lerchenfelder Straße 88-90 Tür 19,  1080 Wien, gegen den von der belangten Behörde Finanzamt Österreich am 7. Februar 2023 zu  Steuernummer 54-863/0435  ausgefertigten Verspätungszuschlagsbescheid 2020 zu Recht  erkannt:  I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Miklos Fölker` | `Dr. Miklos Fölker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilma Husemann` (person)
- `Oberregau 2, 9702 Laas, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `54-863/0435` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/143315.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143315.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Emanuel Bulthuis, Martinsplatz 47, 6167 Neustift im Stubaital, Österreich, vom 7. Dezember 2022 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für die Monate August und September 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emanuel Bulthuis` (person)
- `Martinsplatz 47, 6167 Neustift im Stubaital, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/143331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143331.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Bernhard Jafarzadehpour  in der Beschwerdesache Benjamin Pfandzelt,  Ulrichgasse 3, 5280 Lach, Österreich, über die Beschwerde vom 26.06.2023 gegen den Bescheid des Finanzamtes  Österreich vom 03.05.2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022,  beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Bernhard Jafarzadehpour` | `Dr. Bernhard Jafarzadehpour` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Benjamin Pfandzelt` (person)
- `Ulrichgasse 3, 5280 Lach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/143501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143501.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Dimitri Usslar  in der Beschwerdesache Jessica Abdulkarim,  vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien,  gegen den Bescheid des Finanzamtes Österreich vom 15. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Dimitri Usslar` | `Mag. Dimitri Usslar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jessica Abdulkarim` (person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

**False Positives:**

- `Univ.-Prof. Ren` — partial — pred is substring of gold: `Univ.-Prof. René Neuendorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. René Neuendorf`(person)
- `Kevin Damiani`(person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich`(address)
- `Finanzamt Oststeiermark`(organisation)
- `Finanzamt Oststeiermark`(organisation)
- `FA Oststeiermark`(organisation)
- `FA Oststeiermark`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Dora Szczepanowski`(person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich`(address)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Laurin` — partial — pred is substring of gold: `Hon.-Prof. Laurin Überschar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Laurin Überschar`(person)
- `Albert Theiselmann`(person)
- `Hochmark 31g, 8323 Unterbuch, Österreich`(address)
- `Radike, Hammerl & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `15-781/1702`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

**False Positives:**

- `Priv.-Doz. Mag` — partial — pred is substring of gold: `Priv.-Doz. Mag. Yorick Schlenbäcker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker`(person)
- `Kordula Arlov`(person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Roland Rößle, Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich, über die Beschwerde des  Beschuldigten vom 7. April 2022 gegen den Zurückweisungsbescheid des Magistrates der Stadt  Wien vom 5. April 2022, Zahl: MA67/216700658355/2021, mit dem der Einspruch vom 18.  Februar 2022 gegen die Strafverfügung vom 3. September 2021 mit derselben Geschäftszahl  gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Dr. Sebastian Pfeiffer` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Roland Rößle`(person)
- `Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Magistrates der Stadt  Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Robert Derici`(person)
- `Exlgasse 12, 9623 Karnitzen, Österreich`(address)
- `Erich Allbrand`(person)
- `12-876/0077`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137857.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137857.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Univ.-Prof. Aron Nierenberger  in der Beschwerdesache DDr.in VetR Rosemarie Srama,  Hollgasse 53, 3244 Riegers, Österreich, gegen die Bescheide des Finanzamtes Österreich vom 10. Februar 2020  betreffend Einkommensteuer 2014 bis 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Dr. Univ` — partial — pred is substring of gold: `Dr. Univ.-Prof. Aron Nierenberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Univ.-Prof. Aron Nierenberger`(person)
- `DDr.in VetR Rosemarie Srama`(person)
- `Hollgasse 53, 3244 Riegers, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Gernot Schellhaas  in der Beschwerdesache Guntram Garweg,  Umspannwerkstraße 21, 3912 Kleinnondorf, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Erhöhungsbetrag zur Familienbeihilfe wegen  erheblicher Behinderung für den Zeitraum September 2015 bis Jänner 2019, Steuernummer  92-268/1285,  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof. Univ` — partial — pred is substring of gold: `Univ.-Prof. Univ.-Prof. Gernot Schellhaas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Gernot Schellhaas`(person)
- `Guntram Garweg`(person)
- `Umspannwerkstraße 21, 3912 Kleinnondorf, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `92-268/1285`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Günter Salahi  in der Beschwerdesache Jaden Knauss,  Dossenweg 3, 4132 Atzesberg, Österreich  über die Beschwerde vom 8. Jänner 2021 gegen den Bescheid des Finanzamtes  Österreich vom 3. Dezember 2020 Rückzahlung gemäß § 239 BAO, Steuernummer  15-678/4603  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Hon` — partial — pred is substring of gold: `Mag. Hon.-Prof. Günter Salahi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Günter Salahi`(person)
- `Jaden Knauss`(person)
- `Dossenweg 3, 4132 Atzesberg, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `15-678/4603`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Annette Preußing, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Dr. Sebastian Pfeiffer` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Sebastian Pfeiffer LL.M.`(person)
- `Annette Preußing`(person)
- `Am Neufeldersee 40, 3385 Uttendorf, Österreich`(address)
- `Magistrates der  Stadt Wien`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/140806.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140806.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Moritz Bonnert  in der Beschwerdesache PhD MedR Romana Hupp,  Süßenberger Straße 7, 5270 Vorbuch, Österreich, vertreten durch Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020 Innsbruck, über die Beschwerde  vom 26. Juli 2013 gegen den Bescheid des FA Salzburg-Land  vom 25. Juni 2013 betreffend  Umsatzsteuer 2011, Steuernummer 16-160/7509, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Priv` — partial — pred is substring of gold: `Dr. Priv.-Doz. Moritz Bonnert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Moritz Bonnert`(person)
- `PhD MedR Romana Hupp`(person)
- `Süßenberger Straße 7, 5270 Vorbuch, Österreich`(address)
- `Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `FA Salzburg-Land`(organisation)
- `16-160/7509`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Finn Rosen  in der Beschwerdesache Dragan Ohlff,  vertreten durch Dr. Sven Rudolf Thorstensen LLM, Neustiftgasse 3/7, 1070 Wien, über die  Beschwerde vom 23. Juli 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom  10. Juli 2019 betreffend den Bescheid über den Ablauf einer Aussetzung der Einhebung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Finn Rosen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dr. Finn Rosen`(person)
- `Dragan Ohlff`(person)
- `Dr. Sven Rudolf Thorstensen LLM`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Saphira Schnaak`(person)
- `Kürschner Allee 44, 9300 Mail, Österreich`(address)
- `Ing. Mag. Hamza Ovacin`(person)
- `Finanzamtes Österreich`(organisation)
- `50-980/9446`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/142564.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142564.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Igor Rolfmeier, Dußwaldweg 41, 3171 Außerhalbach, Österreich, vertreten durch Lenfeld | Leys | Sonderegger -  Rechtsanwälte (GesbR), Malserstraße 19, 6500 Landeck, betreffend Beschwerde vom  19. Oktober 2018 gegen die Bescheide des Finanzamtes Innsbruck vom 4. April 2018  betreffend Wiederaufnahme der Einkommensteuerverfahren für die Jahre 2014 bis 2016,  Steuernummer 06-230/8922:  I. Die Beschwerde wird als verspätet zurückgewiesen.

**False Positives:**

- `Mag. David Hell` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Igor Rolfmeier`(person)
- `Dußwaldweg 41, 3171 Außerhalbach, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `06-230/8922`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Leopold Dobertin, Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich, über die Beschwerden gegen Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg   vom 30. Oktober 2015 gegen den Bescheid vom 9. Oktober 2015 betreffend Festsetzung von  zweiten Säumniszuschlägen,  vom 2. März 2016 gegen den Bescheid vom 11. Jänner 2016 betreffend Festsetzung von dritten  Säumniszuschlägen und  vom 2.1.2020 gegen den Bescheid vom 13.12.2019 betreffend Aufhebung/Abänderung von  Nebengebühren  nach der am 4.12.2023 am Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO  i.V.m. § 274 Abs. 1 Z 1 BAO) in Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und  in Anwesenheit von Mag. Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte  Behörde durchgeführten mündlichen Verhandlung zur Steuernummer 38-992/7403  zu  Recht erkannt:   I. Der Beschwerde vom 30.10.2015 wird teilweise Folge gegeben und zweite  Säumniszuschläge in Höhe von 5.739,66 € festgesetzt.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Leopold Dobertin`(person)
- `Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Holzapfel`(person)
- `Mag. Sebastian Rivo-Wastl, BA`(person)
- `38-992/7403`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dr. Martin Wadepfuhl  in der Beschwerdesache Renate Bürvenig,  Kreuzkapellenweg 7, 5151 Hochberg, Österreich, vertreten durch Ludmilla Flaumbaum, Herrengschwendt 3, 8761 Mühltal, Österreich, über die Beschwerde vom  15. Februar 2021 gegen die Bescheide des Finanzamtes Österreich vom 19. Jänner 2021  betreffend die Haftung für Lohnsteuer für 2015, 2016, 2017, 2018 und 2019, sowie den  Dienstgeberbeitrag zum FLAF für 2015, 2016, 2017, 2018 und 2019 und den Zuschlag zum  Dienstgeberbeitrag für 2015, 2016, 2017, 2018 und 2019 zu Steuernummer 74-041/7335  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Martin Wadepfuhl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Dr. Martin Wadepfuhl`(person)
- `Renate Bürvenig`(person)
- `Kreuzkapellenweg 7, 5151 Hochberg, Österreich`(address)
- `Ludmilla Flaumbaum`(person)
- `Herrengschwendt 3, 8761 Mühltal, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `74-041/7335`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/145816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Priv.-Doz. Lars Tezlow  in der Beschwerdesache Ilona Sadowske,  Laaer-Wald-Straße 254, 4040 Asberg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater KG -  Steuerbüro Specht, Kirchweg 11, 6600 Reutte, gegen den von der belangten Behörde  Finanzamt Österreich am 24. April 2023 zu Steuernummer 48-791/6345  ausgefertigten  Bescheid betreffend Einkommensteuer 2021 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 Abs. 1 BAO abgeändert.

**False Positives:**

- `Univ.-Prof. Priv` — partial — pred is substring of gold: `Univ.-Prof. Priv.-Doz. Lars Tezlow`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Priv.-Doz. Lars Tezlow`(person)
- `Ilona Sadowske`(person)
- `Laaer-Wald-Straße 254, 4040 Asberg, Österreich`(address)
- `Hofmann - Wirtschaftstreuhand - Steuerberater KG -  Steuerbüro Specht`(organisation)
- `Finanzamt Österreich`(organisation)
- `48-791/6345`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146522.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Francois Roeder, Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich, über die Beschwerde vom 12. Juni 2023 gegen  den Bescheid des Finanzamtes Österreich vom 9. Mai 2023 betreffend Säumniszuschlag 2023  nach der am 22.11.2024 am Bundesfinanzgericht in Wien über Antrag der Partei abgehaltenen  mündlichen Verhandlung in Abwesenheit des Beschwerdeführers und in Anwesenheit von  Bernadette Pommer BA MA für das Finanzamt sowie der Schriftführerin Mag. Magdalena  Preslmayr zur Steuernummer 48-847/1680  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung eines ersten  Säumniszuschlages vom 9.5.2023 in Höhe von € 148,00 wird gemäß § 279 BAO als  unbegründet abgewiesen.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Francois Roeder`(person)
- `Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bernadette Pommer`(person)
- `Finanzamt`(organisation)
- `Mag. Magdalena  Preslmayr`(person)
- `48-847/1680`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/147361.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147361.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Emmerich Malert  betreffend den Vorlageantrag der  Florens Schitterle, Heidebahn 164, 2443 Deutsch-Brodersdorf, Österreich, vom 31. Dezember 2020 in einer Familienbeihilfenangelegenheit  (Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Mai 2013 bis  Dezember 2014, Bescheid des Finanzamtes Österreich vom 24. März 2020)  beschlossen:  I.  Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Priv.-Doz. Priv` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Emmerich Malert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Priv.-Doz. Emmerich Malert`(person)
- `Florens Schitterle`(person)
- `Heidebahn 164, 2443 Deutsch-Brodersdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/148962.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148962.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Univ.-Prof. Ramon Löther  in der Beschwerdesache Axel Pommeränke,  Zum Hauptplatz 2, 4030 Linz, Österreich, vertreten durch Mag. Niki Zaar, Babenbergerstraße 9/1/8, 1010 Wien,  betreffend die Vorlage der Bescheide des Finanzamtes Österreich vom 9. Oktober 2023 über  die Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2018 und 2019 im Wege  des Vorlageberichtes vom 21. November 2024 zur Steuernummer 14-979/7189  den  Beschluss:  Das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Priv.-Doz. Univ` — partial — pred is substring of gold: `Priv.-Doz. Univ.-Prof. Ramon Löther`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Ramon Löther`(person)
- `Axel Pommeränke`(person)
- `Zum Hauptplatz 2, 4030 Linz, Österreich`(address)
- `Mag. Niki Zaar`(person)
- `Finanzamtes Österreich`(organisation)
- `14-979/7189`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Wladimir Ferrarese  über die Beschwerde des Hademar Mühlenstedt,  Kohlengasse 373, 8442 Sankt Andrä im Sausal, Österreich, vom 22. Juni 2025, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 20. Juni 2025, GZ. MA67/GZ1/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt  der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, Landesgesetzblatt für Wien Nr. 9/2006 in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als gemäß § 45 Abs. 1  VStG von der Verhängung einer Strafe abgesehen und dem Beschwerdeführer unter Hinweis  auf die Rechtswidrigkeit seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Mag. Mag` — partial — pred is substring of gold: `Mag. Mag. Wladimir Ferrarese`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mag. Wladimir Ferrarese`(person)
- `Hademar Mühlenstedt`(person)
- `Kohlengasse 373, 8442 Sankt Andrä im Sausal, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Jonas Nußer  in der Beschwerdesache Dr.in Flora Lallemand,  Rochusplatz 224, 9530 Bad Bleiberg, Österreich, über die Beschwerde vom 5. November 2024 gegen die Bescheide des  FA Graz-Stadt  vom 27. August 2024 über den Ablauf einer Aussetzung der Einhebung, über die  Festsetzung von Aussetzungszinsen und vom 1. Oktober 2024 über die Abweisung eines  Aussetzungsantrags, Steuernummer 29-953/8923, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Priv.-Doz. Univ` — partial — pred is substring of gold: `Priv.-Doz. Univ.-Prof. Jonas Nußer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Jonas Nußer`(person)
- `Dr.in Flora Lallemand`(person)
- `Rochusplatz 224, 9530 Bad Bleiberg, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `29-953/8923`(tax_number)

</details>

---

## `legal_person_complainant_context` 🏆

**F1:** 0.255 | **Precision:** 0.882 | **Recall:** 0.149  

**Format:** `regex`  
**Rule ID:** `965a0a8f`  
**Description:**
Captures names in 'Beschwerdesache' context, requiring a title or specific name structure to exclude legal entities and partial matches.

**Content:**
```
(?:in\s+der\s+Beschwerdesache(?:\s+(?:der|des))?\s+)(?:(?:Dr\.|Mag\.|Mag\.a|Ing\.|RA|MMag\.|Univ\.-?Prof\.|Priv\.-?Doz\.|Hon\.-?Prof\.|VetR|Bakk\.rer\.nat|Bakk\.techn|Bakk\.phil|LLB|MSc|MBA)\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:van|von)\s+[A-Z][a-zäöüß]+)*)\s*(?=,|\s+(?:AG|KG|GmbH|UG|Bf|KommR|Finanzamt|Behörde|Republik|GmbH|Ltd|Inc))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.882 | 0.149 | 0.255 | 313 | 276 | 37 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 276 | 37 | 1575 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elisabeth Schafstall` | `Elisabeth Schafstall` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Pipers` | `Kai Pipers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Dietlind Mahlstädt` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-229/2263` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Höffert` | `Christine Höffert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adalbert Köseoglu` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emmerich Frydrychowski` | `Emmerich Frydrychowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

| Predicted | Gold |
|---|---|
| `Ali Jäckle` | `Ali Jäckle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Pawils` | `Florentin Pawils` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Alva Jodgalweit` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.DDr. Hedwig Bavenek-Weber in der  Beschwerdesache Merlin Feucht, Alte Straße 2, 8114 Unterfriesach, Österreich, über die Beschwerde vom 12. Dezember 2011  gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14.  November 2011, Steuernummer 57-396/6782, betreffend die Festsetzung der ermäßigten  Glücksspielabgabe gemäß § 58 Abs. 3 GSpG für Glücksspiele im Rahmen von Gewinnspielen  (Preisausschreiben), zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Merlin Feucht` | `Merlin Feucht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.DDr. Hedwig Bavenek-Weber` (person)
- `Alte Straße 2, 8114 Unterfriesach, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `57-396/6782` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Sieglinde Kießerling` | `Sieglinde Kießerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Leroy Sitterle` | `Leroy Sitterle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Hermine Ruprich` | `Hermine Ruprich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rosamunde Galanidis` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Oortwyn` | `Volkmar Oortwyn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Zarin Eckartz` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sean Herdling` | `Sean Herdling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Ingeborg Kollaczek` | `Ingeborg Kollaczek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Othmar Feuerbaum` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Lars Huesgen` | `Lars Huesgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Melina Bankratz` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rudolf Bogdanowic` | `Rudolf Bogdanowic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Janosch von Winterfeldt` | `Janosch von Winterfeldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ottfried Ficici` | `Ottfried Ficici` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jacqueline Dittus` | `Jacqueline Dittus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Titus Ohlmer` | `Titus Ohlmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Edwin Pfaefflin` | `Edwin Pfaefflin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Hasslbauer` | `Charlotte Hasslbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich` (address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich` (address)
- `Procurator Treuhand- und Revisionsges.m.b.H.` (organisation)
- `Bundesministeriums für Finanzen` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Annemarie Schwinge` | `Annemarie Schwinge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Kirstin Matiascheck` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lilia Löffelmann` | `Lilia Löffelmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Achmed Karolzak` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mike Reislehner` | `Mike Reislehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Olivia Ziegeler` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Klocksin` | `Gregor Klocksin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Unterguntschach 85, 3525 Armschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

| Predicted | Gold |
|---|---|
| `Chiara Duchan` | `Chiara Duchan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich` (address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Stephan Zeitlhuber` | `Stephan Zeitlhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Marceline Flory` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Morgenbesser` | `Karl Morgenbesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Susette Glaeßel` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Frauke Galleithner` | `Frauke Galleithner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Heike Lehmensieck` | `Heike Lehmensieck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Höllstein 11, 9852 Neuschitz, Österreich` (address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Olivia Sahlmüller` | `Olivia Sahlmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Christoph Hasenfraz` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sandra Fenn` | `Sandra Fenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Mag. Manuela Meyerhofer` (person)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Jonas Gutkauf` | `Jonas Gutkauf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Adebiola Bayer` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Tristan Potente` | `Tristan Potente` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Hürth 5, 4362 Schönfichten, Österreich` (address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `61-467/9522` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Kevin Damiani` | `Kevin Damiani` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. René Neuendorf` (person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Timothy Overlaender` | `Timothy Overlaender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fatima Eichmayr` | `Fatima Eichmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieskapellenweg 10, 8047 Graz, Österreich` (address)
- `Dr. Klaus Plätzer,` (person)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-455/2359` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinI. in der Beschwerdesache Violetta Bailmann, Schlosserfeld 35, 9632 Hochwart, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 20. Oktober 2016 gegen  die Bescheide des Finanzamtes Spittal Villach vom 22. September 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012 (Steuernummer  82-877/4906 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Violetta Bailmann` | `Violetta Bailmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schlosserfeld 35, 9632 Hochwart, Österreich` (address)
- `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG` (organisation)
- `Finanzamtes Spittal Villach` (organisation)
- `82-877/4906` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erwin Döpkemeier` | `Erwin Döpkemeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

| Predicted | Gold |
|---|---|
| `Dora Szczepanowski` | `Dora Szczepanowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich` (address)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Ruperta Schluckner` | `Ruperta Schluckner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Moses Dannebohm` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Schippan  in der Beschwerdesache Judith Kapelle,  Saßbergweg 17, 4860 Haid, Österreich, betreffend Beschwerde vom 2. September 2012 gegen den Bescheid des FA  Waldviertel vom 3. August 2012 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 Steuernummer 31-042/8347  beschlossen:     Der Vorlageantrag vom 30.11.2012 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Judith Kapelle` | `Judith Kapelle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Petra Schippan` (person)
- `Saßbergweg 17, 4860 Haid, Österreich` (address)
- `FA  Waldviertel` (organisation)
- `31-042/8347` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache August Cernyj, Lusthausstraße 569, 4901 Bruckmühl, Österreich, vertreten durch Casapicola & Gross Wirtschafts- prüfungs- und Steuerberatungs  GmbH, Gluckgasse 3 Tür 15, 1010 Wien, über die Beschwerde vom 19. Juni 2019 gegen die  Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt für Großbetriebe) datiert jeweils  vom 30. April 2019 betreffend Umsatzsteuer für die Jahre 2013 bis 2016 und  Körperschaftsteuer für die Jahre 2013 – 2015 , Steuernummer 12-317/0890  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `August Cernyj` | `August Cernyj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lusthausstraße 569, 4901 Bruckmühl, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `12-317/0890` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bruno Karahasan` | `Bruno Karahasan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Nancy Stuckenschneider` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `12-630/0045` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Lieselotte Schluessel, Hannakstraße 205, 5121 Wimm, Österreich, über die Beschwerde vom 22. Februar 2016  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 10. Februar 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Lieselotte Schluessel` | `Lieselotte Schluessel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Rauner` (person)
- `Gregor Ableidinger` (person)
- `Dr. Franz Kandlhofer` (person)
- `Hannakstraße 205, 5121 Wimm, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Enrico Steudtle` | `Enrico Steudtle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Walter Monheim` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-940/7308` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Albert Theiselmann` | `Albert Theiselmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Laurin Überschar` (person)
- `Hochmark 31g, 8323 Unterbuch, Österreich` (address)
- `Radike, Hammerl & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `15-781/1702` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die Richterin Mag. Riin sowie  die fachkundigen Laienrichter A und B, in der Beschwerdesache Karina Schliekau, Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich,  vertreten durch die Kanzlei, über die Beschwerde vom 15. Februar 2018 gegen den Bescheid  des Finanzamtes Österreich, vormals Finanzamt Wien 3/6/7/11/15 Schwechat und Gerasdorf,  vom 1. Februar 2018 betreffend Feststellung der Einkünfte § 188 BAO 2016, nach  Durchführung einer mündlichen Verhandlung am 17. November 2021 in Anwesenheit der  Schriftführerin C, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Karina Schliekau` | `Karina Schliekau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Riin` (person)
- `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 3/6/7/11/15` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hugo Engelsmann` | `Hugo Engelsmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Armin Heckemanns, Nabuccogasse 10, 2630 Ternitz, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, (im  Beschwerdeverfahren nicht eingeschritten), über die Beschwerde vom 10. Februar 2020 gegen  den Einkommensteuerbescheid 2018 des Finanzamtes Baden Mödling vom 10. Jänner 2020  (und gemäß § 253 Satz 1 BAO auch gegen den Einkommensteuerbescheid 2018 vom  18. September 2020) zu Steuernummer 75-597/1615  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Armin Heckemanns` | `Armin Heckemanns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nabuccogasse 10, 2630 Ternitz, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `Finanzamtes Baden Mödling` (organisation)
- `75-597/1615` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich` (address)
- `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` (organisation)
- `FA Wien 9/18/19  Klosterneuburg` (organisation)
- `79-708/0061` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Isakova, Hörgattern 37, 3244 Kühberg, Österreich, über die Beschwerde vom 1. Juni 2017 gegen  den Bescheid des Finanzamtes Österreich vom 15. Mai 2017 betreffend Familienbeihilfe  01.2016-12.2016 Steuernummer 93-163/8536  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, dass dieser betreffend T1 hinsichtlich der Monate April, August und  September 2016 ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Dimitri Isakova` | `Dimitri Isakova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Hörgattern 37, 3244 Kühberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `93-163/8536` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


BESCHLUSS   Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Frederike Lipienski  in der Beschwerdesache des  Hademar Rüstow, Eck 124T, 2214 Auersthal, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des  FA Amstetten Melk Scheibbs (FA) vom 10. März 2021 über die Abweisung eines Antrages auf Wiederaufnahme §  303 BAO /  ESt 2017 zur Steuernummer 71-651/2158  beschlossen:   Der Vorlageantrag vom 29.Sept.2021 wird gemäß § 260 Abs. 1 lit. a iVm § 264 Abs. 4 lit e und  Abs. 5 BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hademar Rüstow` | `Hademar Rüstow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Frederike Lipienski` (person)
- `Eck 124T, 2214 Auersthal, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `71-651/2158` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sulamith Jedwillat` | `Sulamith Jedwillat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brandenbergweg 15, 8353 Pichla, Österreich` (address)
- `Mag. Michael Payr` (person)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `41-852/7395` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Sieglinde Semertzidou` | `Sieglinde Semertzidou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Sheila Nonnmacher` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Fortwängler` | `Rosemarie Fortwängler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Karina von Wnuck-Lipinski` (person)
- `Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Vincent Kohlstruk` | `Vincent Kohlstruk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Mag. Natascha Gassner` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ludger Endel` | `Ludger Endel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `63-868/1042` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Claire Wienhues` | `Claire Wienhues` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamt` (organisation)
- `61-469/1778` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Stockhorst` | `Jeanne Stockhorst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich` (address)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `22-242/2984` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Tanja Fützenreiter, Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich, über die Beschwerde der Beschwerdeführerin  (Bf.) vom 29. März 2021 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) für  2019 des Finanzamtes Österreich vom 17. März 2021 zur Steuernummer 90-161/7779  zu  Recht erkannt:   Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Tanja Fützenreiter` | `Tanja Fützenreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Seywald` (person)
- `Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `90-161/7779` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  Gwendolin Rittmüller, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gwendolin Rittmüller` | `Gwendolin Rittmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Hon.-Prof.in Hilde Hassenzahl` (person)
- `Matzlröth 29, 3970 Reinprechts, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `10-920/5174` (tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Zlatan Nowizki  in der Beschwerdesache Janis Loewenthal,  Georg Grinninger-Straße 15, 3830 Pyhra, Österreich, vertreten durch die [Erwachsenenvertreterin], über die Beschwerde vom  23. August 2019 gegen den Bescheid des Finanzamtes Kitzbühel Lienz (nunmehr: Finanzamt  Österreich) vom 23. Juli 2019 betreffend Familienbeihilfe und Erhöhungsbetrag zur  Familienbeihilfe wegen erheblicher Behinderung ab November 2018, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Janis Loewenthal` | `Janis Loewenthal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Zlatan Nowizki` (person)
- `Georg Grinninger-Straße 15, 3830 Pyhra, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Robert Derici` | `Robert Derici` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Exlgasse 12, 9623 Karnitzen, Österreich` (address)
- `Erich Allbrand` (person)
- `12-876/0077` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Penelope Splettstösser  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wilhelm Schöbel` | `Wilhelm Schöbel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Penelope Splettstösser` (person)
- `Leopoldgasse 23, 8674 Grubbauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-896/6207` (tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marlies Seipold, Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich, über die Beschwerde vom 27. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 14. Jänner 2020 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum März 2017 bis September 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Seipold` | `Marlies Seipold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Julian Egiede` | `Julian Egiede` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Theras 97, 4565 Haselbäckau, Österreich` (address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `Mag. Michael Sablatnik` (person)
- `88-033/6865` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gisbert Löhberg` | `Gisbert Löhberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich` (address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `73-737/2281` (tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Theodor Siel, Amesberg 28, 6321 Angath, Österreich, über die Beschwerde vom 4. November 2016 gegen den Bescheid des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich) vom 13. Oktober  2016 betreffend Grunderwerbsteuer, Steuernummer 74-672/4502, Erfassungsnummer 10- 2015, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Theodor Siel` | `Theodor Siel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amesberg 28, 6321 Angath, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `74-672/4502` (tax_number)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Barbara Schwalb  in der Beschwerdesache Annalena Mlynarcik,  Ledochowskastraße 5, 4040 Kammerschlag, Österreich, über die Beschwerde vom 02.03.2017 gegen die Bescheide des Finanzamtes  Österreich vom 28. Februar 2017 betreffend Abweisung des Antrages auf Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre Wiederaufnahme § 303 BAO /  ESt 2011  -2013 Steuernummer 09-012/5071  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Annalena Mlynarcik` | `Annalena Mlynarcik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Barbara Schwalb` (person)
- `Ledochowskastraße 5, 4040 Kammerschlag, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `09-012/5071` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Sascha Hilcker` — partial — pred is substring of gold: `Ing. Sascha Hilcker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Sascha Hilcker`(person)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich`(address)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

**False Positives:**

- `Kelderber Beratung Technologien` — type mismatch — same span as gold: `Kelderber Beratung Technologien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Silvia Gebhart`(person)
- `Kelderber Beratung Technologien`(organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich`(address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker`(person)
- `Mag Tatjana Kovacic`(person)
- `Dr  Heinrich Vana,`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `7867 150654`(social_security_number)
- `Europäischen Parlaments`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Theodora Urbanova` — partial — pred is substring of gold: `Theodora Urbanova, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Theodora Urbanova, Bakk. iur.`(person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `54-205/5010`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Elias Voht` — partial — pred is substring of gold: `VetR Elias Voht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Elias Voht`(person)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ruprecht Hauswerth` — partial — pred is substring of gold: `Hon.-Prof. Ruprecht Hauswerth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thomas Hutching`(person)
- `Hon.-Prof. Ruprecht Hauswerth`(person)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich`(address)
- `FA Klosterneuburg`(organisation)
- `26-476/7368`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Gueldner Garten` — type mismatch — same span as gold: `Gueldner Garten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Tamara Steinmüller`(person)
- `Gueldner Garten`(organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich`(address)
- `FA Deutschlandsberg Leibnitz Voitsberg`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Burkhard Krautschenko` — partial — pred is substring of gold: `VetR Burkhard Krautschenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Raimund Diedering` — partial — pred is substring of gold: `Raimund Diedering, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Edith Schifferdecker` — partial — pred is substring of gold: `Ing. Edith Schifferdecker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dominik Mehlig`(person)
- `Ing. Edith Schifferdecker`(person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich`(address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `73-948/8864`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Werner Böltl` — partial — pred is substring of gold: `Ing. Werner Böltl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Kuprian`(person)
- `Ing. Werner Böltl`(person)
- `Rydlweg 234, 3860 Dietweis, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valentin Joebges` — partial — pred is substring of gold: `Valentin Joebges, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Stephan`(person)
- `Valentin Joebges, LLM`(person)
- `Bärngarten 17, 9713 Hochegg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `84-167/9727`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ludmilla Hühnerfuß` — partial — pred is substring of gold: `Ludmilla Hühnerfuß, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dominika Juhass`(person)
- `Ludmilla Hühnerfuß, Bakk. techn.`(person)
- `Singham 20, 3465 Unterstockstall, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137349.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Gebhard Kristupeit, Bakk. techn., Wörndlestraße 17, 9112 Untergrafenbach, Österreich, vertreten durch APP Steuerberatung GesmbH, Schenkenstraße  4, 1010 Wien, über die Beschwerde gegen die Bescheide des Finanzamtes Baden Mödling vom  31. Mai 2011 hinsichtlich Haftung betreffend Kapitalertragsteuer für 2007 und 2008,  Steuernummer 83-002/9356  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Gebhard Kristupeit` — partial — pred is substring of gold: `Gebhard Kristupeit, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Gebhard Kristupeit, Bakk. techn.`(person)
- `Wörndlestraße 17, 9112 Untergrafenbach, Österreich`(address)
- `APP Steuerberatung GesmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `83-002/9356`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Anton Böckamp, Bakk. techn., Leopold Kunschak Gasse 25, 9343 Dielach, Österreich, über die Beschwerde vom 8. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Gänserndorf Mistelbach, § 323b BAO) vom  25. November 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 84-669/5568  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne des Beschwerdebegehrens  abgeändert.

**False Positives:**

- `Anton Böckamp` — partial — pred is substring of gold: `Anton Böckamp, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Anton Böckamp, Bakk. techn.`(person)
- `Leopold Kunschak Gasse 25, 9343 Dielach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Gänserndorf Mistelbach`(organisation)
- `84-669/5568`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Adolf Brehmer  in der Beschwerdesache VetR Gotthard Lohscheider,  Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich, vertreten durch „Meinrad Kisewetter“ - Steuerberatungsgesellschaft m.b.H., Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich,  über die Beschwerde vom 28.06.2021, gegen den Bescheid des Finanzamtes Österreich vom  27.05.2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm § 111 BAO, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Gotthard Lohscheider` — partial — pred is substring of gold: `VetR Gotthard Lohscheider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Adolf Brehmer`(person)
- `VetR Gotthard Lohscheider`(person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich`(address)
- `Meinrad Kisewetter`(person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Mehmet Zappe, MA, Wiesel 24, 4632 Oberirrach, Österreich, vertreten durch Petzelbauer & Kleinhappel Rechtsanwälte, Rabensteig 8/3A, 1010  Wien, betreffend einen Antrag auf Fristsetzung gemäß Art. 133 Abs. 1 Z 2 iVm Abs. 7 B-VG vom  10. Oktober 2022 wegen Verletzung der Entscheidungspflicht, Steuernummer 51-912/4171  (SVNR 3727 040311), beschlossen:   Der Fristsetzungsantrag vom 10. Oktober 2022 betreffend die behauptete Säumigkeit des  Bundesfinanzgerichtes im Säumnisbeschwerdeverfahren gegen das Finanzamt Österreich  betreffend einen Antrag auf Familienbeihilfe für den Zeitraum März 2020 bis April 2021 wird  gemäß § 30a Abs. 1 VwGG iVm § 30a Abs. 8 erster Satz VwGG als unzulässig zurückgewiesen.

**False Positives:**

- `Mehmet Zappe` — partial — pred is substring of gold: `Mehmet Zappe, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mehmet Zappe, MA`(person)
- `Wiesel 24, 4632 Oberirrach, Österreich`(address)
- `51-912/4171`(tax_number)
- `3727 040311`(social_security_number)
- `Bundesfinanzgerichtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Stella Hornscheidt  in der Beschwerdesache Ing. Jaden Stoelzl,  Singham 49, 4274 Straß, Österreich, über die Beschwerden vom 1. Juni 2021 gegen die Bescheide des Finanzamtes  Österreich vom 31. Mai 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016,  2017 und 2018 Steuernummer 25-717/7817  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Jaden Stoelzl` — partial — pred is substring of gold: `Ing. Jaden Stoelzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Stella Hornscheidt`(person)
- `Ing. Jaden Stoelzl`(person)
- `Singham 49, 4274 Straß, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `25-717/7817`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Svenja Kieble  in der Beschwerdesache Vera Henssel, Bakk. rer. nat.,  Lärchenhofweg 43, 4073 Dörnbach, Österreich, über die Beschwerde vom 3. März 2022 gegen die Bescheide des Finanzamtes  Österreich vom 7. Februar 2022, Ordnungsbegriff Nr1, betreffend Abweisung der Anträge auf  Familienbeihilfe und Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung für  den Zeitraum ab August 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vera Henssel` — partial — pred is substring of gold: `Vera Henssel, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Svenja Kieble`(person)
- `Vera Henssel, Bakk. rer. nat.`(person)
- `Lärchenhofweg 43, 4073 Dörnbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/141990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141990.1_2`)


Das Bundesfinanzgericht hat durch die Senatsvorsitzende R1, den RichterR2, sowie die  fachkundigen Laienrichter R3 und R4, in der Beschwerdesache VetR Maja Waatsack, Sarottla 115, 8522 Sulzhof, Österreich,  vertreten durch Mag. Wolfgang Schranz, Mahlerstraße 11 Tür 4, 1010 Wien, über die  Beschwerde vom 28. Oktober 2016 gegen die Bescheide des Finanzamtes Wien 8/16/17 vom  25. Juli 2016 betreffend Umsatzsteuer sowie Feststellung der Einkünfte gemäß § 188 BAO für  2009, sowie vom 24. August 2016 betreffend Umsatzsteuer und Feststellung der Einkünfte  gemäß § 188 BAO für die Jahre 2010 bis 2015, Steuernummer 31-345/4688, in der Sitzung  vom 30. August 2023 nach Durchführung einer mündlichen Verhandlung am 30. August 2023 in  Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Maja Waatsack` — partial — pred is substring of gold: `VetR Maja Waatsack`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Maja Waatsack`(person)
- `Sarottla 115, 8522 Sulzhof, Österreich`(address)
- `Mag. Wolfgang Schranz`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `31-345/4688`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Geraldine Matuschefski  in der Beschwerdesache der Demircan Metall AG&  atypisch stille Gesellschaft, vertreten durch xx Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen  1.

**False Positives:**

- `Demircan Metall` — partial — pred is substring of gold: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Geraldine Matuschefski`(person)
- `Demircan Metall AG`(organisation)
- `xx Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Marion Kloefkorn` — partial — pred is substring of gold: `Ing. Marion Kloefkorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Ing. Marion Kloefkorn`(person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`(address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `40-620/0106`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/144397.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144397.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag. Dario Hukauf, Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich, vertreten durch ALTHUBER SPORNBERGER &  PARTNER Rechtsanwälte GmbH, Doblhoffgasse 9 Tür Top 14, 1010 Wien, über die Beschwerde  vom 3. Jänner 2020 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr Finanzamtes für Großbetriebe ) vom 28. November 2019 betreffend Rückforderung  gem. § 241a BAO von Kapitalertragsteuer 2010 bis 2012 (Evidenznummern ***, ***, ***, ***,  ***, ***, ***, ***), Steuernummer 45-917/5183, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dario Hukauf` — partial — pred is substring of gold: `Mag. Dario Hukauf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag. Dario Hukauf`(person)
- `Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `45-917/5183`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Aloisia Bergauer in der Beschwerdesache  Ing. Christian Marckwordt, Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung Energiekrisenbeitrag Strom für den Zeitraum 1.12.2022-30.06.2023,  Steuernummer 22-821/5972, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Christian Marckwordt` — partial — pred is substring of gold: `Ing. Christian Marckwordt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Aloisia Bergauer`(person)
- `Ing. Christian Marckwordt`(person)
- `Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `22-821/5972`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/145618.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145618.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Chiara Fritschy, Bakk. rer. nat., Großerstraße 25, 4694 Edlach, Österreich, vertreten durch i-tax Steuerberatungs GmbH, Triesterstraße 14,  2351 Wiener Neudorf, über die Beschwerde vom 3. Mai 2022 gegen den Bescheid des  Finanzamtes Österreich vom 4. April 2022 betreffend Forschungsprämie § 108c EStG 1988  2019 Steuernummer 18-489/9430  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Chiara Fritschy` — partial — pred is substring of gold: `Chiara Fritschy, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Chiara Fritschy, Bakk. rer. nat.`(person)
- `Großerstraße 25, 4694 Edlach, Österreich`(address)
- `i-tax Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `18-489/9430`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/145448.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145448.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Ilhan Wolfer, Bakk. phil., Kleinsemmeringstraße 12, 3623 Singenreith, Österreich, (Beschwerdeführer, abgekürzt: Bf.), in  Erledigung der Säumnisbeschwerde vom 25. März 2024 wegen vorgebrachter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich hinsichtlich Einkommensteuer für die  Jahre 2001 bis 2005, Steuernummer 15-079/6612 :  I.) zu Recht erkannt:  Aufgrund der hinsichtlich Einkommensteuer 2004 auf das Bundesfinanzgericht übergegan- genen Zuständigkeit zur Entscheidung über die gemäß § 295 Abs. 1 Bundesabgabenordnung  (BAO) von Amts wegen vorzunehmende, geänderte Festsetzung der Abgabe wird die  Einkommensteuer des Beschwerdeführers für das Jahr 2004 mit -15.455,21 € festgesetzt.

**False Positives:**

- `Ilhan Wolfer` — partial — pred is substring of gold: `Ilhan Wolfer, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Ilhan Wolfer, Bakk. phil.`(person)
- `Kleinsemmeringstraße 12, 3623 Singenreith, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `15-079/6612`(tax_number)
- `Bundesfinanzgericht`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/146116.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146116.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Thomas Bäckert  in der Beschwerdesache Dr. Quentin Tessier,  Krottenhofweg 115, 4364 Großmaseldorf, Österreich, betreffend Beschwerde vom 18. Juni 2023 gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 15. Mai 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  Steuernummer 71-981/5443  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Quentin Tessier` — partial — pred is substring of gold: `Dr. Quentin Tessier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Thomas Bäckert`(person)
- `Dr. Quentin Tessier`(person)
- `Krottenhofweg 115, 4364 Großmaseldorf, Österreich`(address)
- `FA St. Johann Tamsweg Zell am See`(organisation)
- `71-981/5443`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Daphne Cofalla  in der Beschwerdesache Xenia Rieffers, Bakk. techn.,  Almersberg 23, 5440 Voregg, Österreich, betreffend Beschwerde vom 16. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. September 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022   Steuernummer  *** beschlossen:     Die Parteien werden gemäß § 281a BAO formlos in Kenntnis gesetzt, dass nach Auffassung des  Bundesfinanzgerichts in Bezug auf die gegenständliche Beschwerde vom 16. Oktober 2023  gegen den Bescheid vom 6. September 2023 ein Vorlageantrag nicht eingebracht wurde.

**False Positives:**

- `Xenia Rieffers` — partial — pred is substring of gold: `Xenia Rieffers, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Daphne Cofalla`(person)
- `Xenia Rieffers, Bakk. techn.`(person)
- `Almersberg 23, 5440 Voregg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Bundesfinanzgerichts`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Niklas Hussung  in der Beschwerdesache Univ.-Prof. Oliver Ruhsbüldt,  Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich, vertreten durch Gattringer Steuerberatung GmbH, Sonnensteinstraße 12, 4040  Linz, über die Beschwerde vom 31. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 16. Mai 2023 betreffend Einkommensteuer 2021 Steuernummer 26-058/9655  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Oliver Ruhsbüldt` — partial — pred is substring of gold: `Univ.-Prof. Oliver Ruhsbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Niklas Hussung`(person)
- `Univ.-Prof. Oliver Ruhsbüldt`(person)
- `Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich`(address)
- `Gattringer Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `26-058/9655`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/147347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147347.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Tatjana Siegerist, Bakk. phil., Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich, vertreten durch Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH, Wiesentalstraße 40, 90419 Nürnberg, Deutschland, über die  Beschwerde vom 27. Juli 2023 gegen den Bescheid des Magistrats der Stadt Wien, MA 6  Rechnungs- und Abgabenwesen, MA 6/ARL-676259-2022, vom 28. Juni 2023 betreffend  Haftung zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Tatjana Siegerist` — partial — pred is substring of gold: `Tatjana Siegerist, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Lisa Fries`(person)
- `Tatjana Siegerist, Bakk. phil.`(person)
- `Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich`(address)
- `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH`(organisation)
- `Magistrats der Stadt Wien`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/147540.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147540.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Horst Boneck  in der Beschwerdesache Sophie Erben, BA,  Dr.-Gangolf-Sacher-Straße 8, 4656 Kirchham, Österreich, zur Beschwerde vom 19. Dezember 2023 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratsabteilung 68, Feuerwehr und Katastrophenschutz, Berufsfeuerwehr  Wien, Gebührenverrechnung, Am Hof 9-10, 1010 Wien, vom 11. Dezember 2023 betreffend  die Festsetzung von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der  Stadt Wien, Gebührenbescheid ZAHL, beschlossen:  I. Die Parteien werden darüber in Kenntnis gesetzt, dass eine  Beschwerdevorentscheidung noch zu erlassen ist.

**False Positives:**

- `Sophie Erben` — partial — pred is substring of gold: `Sophie Erben, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Horst Boneck`(person)
- `Sophie Erben, BA`(person)
- `Dr.-Gangolf-Sacher-Straße 8, 4656 Kirchham, Österreich`(address)
- `Magistrats  der Stadt Wien, Magistratsabteilung 68`(organisation)
- `Stadt Wien`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

**False Positives:**

- `Dagobert Almasri` — partial — pred is substring of gold: `Ing. Dagobert Almasri`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Ing. Dagobert Almasri`(person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/147829.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147829.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Adrian Urbanavicius  in der Beschwerdesache Liliana Kyriacou, Bakk. techn.,  Nekulagasse 2, 4841 Kien, Österreich, über die Beschwerde vom 19. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 26. Jänner 2022 betreffend Eingabengebühr und  Gebührenerhöhung, Steuernummer 91-338/7063, Erfassungsnummer 10-2021, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Liliana Kyriacou` — partial — pred is substring of gold: `Liliana Kyriacou, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Adrian Urbanavicius`(person)
- `Liliana Kyriacou, Bakk. techn.`(person)
- `Nekulagasse 2, 4841 Kien, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `91-338/7063`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paulina Borisowa  in der Beschwerdesache Ilhan Feldmeier, Bakk. rer. nat.,  Sittenbergstraße 9, 4294 Stampfendorf, Österreich, vertreten durch Mag. Benno Elmar Di Gaspero, Unterer Platz 7, 9372  Eberstein, über die Beschwerde vom 14. Juni 2024 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juni 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 14-548/3314  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Ilhan Feldmeier` — partial — pred is substring of gold: `Ilhan Feldmeier, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Paulina Borisowa`(person)
- `Ilhan Feldmeier, Bakk. rer. nat.`(person)
- `Sittenbergstraße 9, 4294 Stampfendorf, Österreich`(address)
- `Mag. Benno Elmar Di Gaspero`(person)
- `Finanzamtes  Österreich`(organisation)
- `14-548/3314`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/148554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Koolen  in der Beschwerdesache   Univ.-Prof. Brian Salemi, Ulrichskirchen 3, 4184 Neuschlag, Österreich, Philippinen, Steuernummer 63-391/9556  über die Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamt Grieskirchen Wels  vom 1. Februar  2018 betreffend Vorsteuererstattung 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Brian Salemi` — partial — pred is substring of gold: `Univ.-Prof. Brian Salemi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Regina Koolen`(person)
- `Univ.-Prof. Brian Salemi`(person)
- `Ulrichskirchen 3, 4184 Neuschlag, Österreich`(address)
- `63-391/9556`(tax_number)
- `Finanzamt Grieskirchen Wels`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/149152.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149152.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Egon Pontius  in der Beschwerdesache der  Hartmut Hoffmeyer, Karl Kleinrath-Weg 24, 4153 Martschlag, Österreich, betreffend Beschwerde vom 4. Dezember 2024 gegen den  Bescheid des Finanzamtes Österreich vom 6. November 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 15-318/3527, beschlossen:  Der Vorlageantrag vom 9.2.2025 wird gemäß § 264 Abs. 4 lit. e iVm. § 260 Abs. 1 lit. b BAO als  nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Hartmut Hoffmeyer` — type mismatch — same span as gold: `Hartmut Hoffmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Egon Pontius`(person)
- `Hartmut Hoffmeyer`(organisation)
- `Karl Kleinrath-Weg 24, 4153 Martschlag, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `15-318/3527`(tax_number)

</details>

---

## `legal_person_honorific_context` 🏆

**F1:** 0.142 | **Precision:** 0.780 | **Recall:** 0.078  

**Format:** `regex`  
**Rule ID:** `ddf3af2a`  
**Description:**
Merged: Both rules extract person names after 'Herr/Frau'. The first rule has 27 matches (4 TP, 23 FP) and the second has 5 matches (0 TP, 5 FP). Merging them allows for a unified pattern that covers both 'Herr/Frau' prefixes and 'von Herr/Frau' contexts, reducing redundancy. The merged rule retains the negative lookahead to filter out job titles.

**Content:**
```
(?:Herrn?|Frau|von\s+(?:Herrn?|Frau))(?:\s+|[^A-Za-z]{1,3})([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+(?:van|von)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b(?!\s+(?:Sekretärin|Richterin|Richter|Geschäftsführer|Chefsekretärin|Betriebsdirektor|Bevollmächtigten))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.780 | 0.078 | 0.142 | 186 | 145 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 145 | 41 | 1706 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_7`)


Mit Schreiben vom 23.11.2016 legte die Beschwerdeführerin eine Bestätigung ihres  Dienstgebers vor, mit dem folgenden Wortlaut:  "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig  ausschließlich ihre Tätigkeit als Anzeigenverkäuferin (Vertreterin) im Außendienst vom  03.03.2014 bis 31.12.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_10`)


Mit Schreiben vom 28.11.2016 legte die Beschwerdeführerin, eine beim AG GmbH angestellte  Anzeigenverkäuferin, eine Bestätigung ihres Dienstgebers vor, mit dem folgenden Wortlaut:   "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit, als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom 01.01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_12`)


Frau Hainig  ist ab 3. März 2014 als Anzeigenberaterin für die DG  tätig.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_13`)


Frau Hainig  hat als Dienstort Stadt und Stadt1 und wird zu nachstehenden Bedingungen  ganztags angestellt: Kollektivvertrag: kfm, (nichtjournalistische) Angestellte;

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_19`)


Frau Hainig  verrechnet die ersten drei Monate Spesen und Kilometergeld  nach Bedarf, wobei diese mittels Spesenabrechnung und Kilometerbuch abzurechnen und zu  belegen sind.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_21`)


Mit Frau Hainig  wird vorerst ein  befristetes Dienstverhältnis bis 2. Juni 2014 vereinbart, wobei der erste Monat als Probemonat  gilt. Als Dienstort wird vornehmlich Stadt vereinbart, wobei es dem Dienstgeber vorbehalten ist,  die Dienstnehmerin auch an anderen Betriebsstätten des Unternehmens niederösterreichweit  vorübergehend oder dauernd einzusetzen.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_50`)


Die  am 28.11.2016 vorgelegte Bestätigung der DG (im Folgenden kurz: *** Verlagsges.m.b.H.) hat  folgenden Inhalt: „Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung § 17 Abs. 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom Ol. 01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_71`)


…“ Auch ein  Passus im vorgelegten TÜV-Bericht über den Prüftermin am 24.6.2019 steht damit in Einklang:  „Sehr geehrter Herr Volchert  an Ihrem Fahrzeug wurden zum Zeitpunkt der Untersuchung keine  Mängel festgestellt. …“.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_98`)


Z1 wurde laut der vorgelegten Protokollsabschrift am 11.6.2018 an der Polizeiinspektion  d_Ort_1 vernommen und gab unter anderem an: „Seit Mitte dem Jahr 2016 bin ich als  Steuerberater für …Herrn Volchert tätig.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_99`)


…Herr Volchert ist hauptberuflich Angestellter der AG in d_Ort_2.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_105`)


Herr Eugen Volchert  ist polizeilich in der Adr, Plz_1  d_Ort_1 gemeldet und deshalb ist sein Fahrzeug auch in d_Ort_1 zugelassen.

| Predicted | Gold |
|---|---|
| `Eugen Volchert` | `Eugen Volchert` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)


12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr Aldewereld von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

| Predicted | Gold |
|---|---|
| `Aldewereld` | `Aldewereld` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_69`)


Herr Frikel ist ebenso Gesellschafter.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_71`)


Im Rahmen der Firmengründung wurde von Herrn Frikel ein  Fahrzeug als sein Beitrag bzw. als Einlage eingebracht.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_73`)


Dieses Kfz wurde von Herrn Frikel selber angeschafft, wo und zu welchen  Bedingungen kann ich nicht angeben.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_75`)


Ich selber war dann in der Folge mehrmals in Österreich bei Herrn Frikel  wenn ich  mit dem Flugzeug anreiste, konnte ich dann den Audi verwenden (so ca. 15 mal pro Jahr) und  damit Kundenbesuche etc. erledigen.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_80`)


Die Bilanz für 2010 ist noch nicht  erstellt. In Deutschland an meinem Wohnsitz bzw. am Firmensitz konnte ich somit nicht  permanent über das KFZ Audi A6 verfügen, es befand sich des öfteren im Besitz des Herrn Frikel in  A/Adr1 und somit an diesem Standort.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_84`)


Prima Abo 10,00  Gesamt 431,27  Arbeitsmittel:  1. 1. CD Herr Riese und sein Garten 21,00  5 von 26 Seite 6 von 26

| Predicted | Gold |
|---|---|
| `Riese` | `Riese` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über Albert Sengeisen  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Wallnerfeld 8, 3751 Sigmundsherberg, Österreich` (address)
- `Finanzamt  Wien 9/18/19` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)


Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr Albert Sengeisen  als Machthaber über die Gesellschaft  aufgetreten.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Habdank` | `Bernhard Habdank` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_34`)


Mit Lenkerauskunft des rechtsfreundlichen Vertreters der Zulassungsbesitzerin vom  1) 12.05.2020, 2) bis 5) 26.03.2020 und 6) 20.03.2020 wurde mitgeteilt, dass Verantwortlicher  für das Taxi- und Mietwagengewerbe Herr Russbüldt  geb. Herrgeb, AdrHerr, sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)


Die Auskunft könne Herr Russbüldt als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_36`)


In weiterer Folge wurde Herr Russbüldt von der Behörde angeschrieben und um Bekanntgabe des  Fahrzeuglenkers ersucht.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_37`)


1) Mit Schreiben vom 13.05.2020 wurde von Herrn Angelstein mitgeteilt, dass er weder  Geschäftsführer der Firma sei noch mit dem Fahrzeug gefahren sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_38`)


Mit Schreiben vom 02.06.2020 wurde durch die Rechtsanwälte des Herrn Angelstein mitgeteilt, dass  dieser keine Lenkerauskunft erteilen könne, da er lediglich für das Fahrzeug mit dem amtlichen  Kennzeichen Auto3 (Anmerkung BFG: nicht gegenständlich) verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_40`)


In dem durch Ihren Rechtsvertreter dagegen erhobenen Einspruch wurde im Wesentlichen  eingewendet, dass Herr Russbüldt  geb. Herrgeb, AdrHerr der einzige und alleinige Verantwortliche  4 von 22 Seite 5 von 22

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_50`)


Mit Schreiben vom 04.06.2020 teilte die rechtsfreundliche Vertretung des Herrn Angelstein  mit, dass der Genannte über das gegenständliche Fahrzeug zum Beanstandungszeitpunkt nicht  verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_51`)


Mit Schreiben vom 18.06.2020 wurde die Zulassungsbesitzerin des gegenständlichen  Fahrzeuges aufgefordert die erteilte Lenkerauskunft durch Vorlage entsprechender  Beweismittel (Unterlagen über die Bestellung des Herrn Angelstein als verantwortlicher Beauftragter  gemäß § 9 Abs. 2 Verwaltungsstrafgesetz 1991) glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_53`)


Dagegen erhoben Sie mit E-Mail vom 2) und 6) 31.08.2020, 3) und 4) 07.09.2020, 5) 04.09.2020  Einspruch und wiederholten, dass Herr Russbüldt der verantwortliche Fuhrparkleiter gewesen sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_57`)


In der E-Mail Ihres rechtsfreundlichen Vertreters vom 01.10.2020 wurde zum gegenständlich  angelasteten Sachverhalt vorgebracht, die Zulassungsbesitzerin und deren handelsrechtliches  Organ habe der Aufforderung der Behörde zur Lenkerauskunft gesetzestreu entsprochen, zumal  dargelegt worden sei, dass die verlangte Auskunft von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030  Wien, als Verantwortlicher gemäß § 9 VStG erteilt werden könne.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_58`)


Zum Beweis dafür wurde ein  Dokument vom 27.11.2018 vorgelegt, worin die Firmen Firma1 und Firma2 vereinbaren, dass Herr Russbüldt als Fuhrparkleiter für beide angeführten Firmen ab dem 01.12.2018 beauftragt wird.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_60`)


Weiters  wurde die Herbeischaffung des Aktes der WKStA zur AZ: AktWKStA, dessen Inhalt die  Übertragung der Meldepflicht gemäß § 9 VStG auf Herrn Angelstein beweisen soll, beantragt.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_71`)


Aufgrund der Aktenlage ist daher davon auszugehen, dass Herr Russbüldt nicht verantwortlicher  Beauftragter gemäß § 9 Abs. 2 VStG ist.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |
| `Russbüldt` | `Russbüldt` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_105`)


Darin hat der Beschwerdeführer dargelegt, dass der  Beschwerdeführer die verlangte Auskunft nicht erteilen kann, sondern Herr Russbüldt  geb. Herrgeb,  AdrHerr, Verantwortlicher gemäß § 9 VStG.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_110`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_112`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste  gegen ihn Anzeige erstattet werden.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_117`)


Tatsächlich ist Herr Russbüldt mit Bestellungsurkunde vom 27.11.2018 zum Fuhrparkleiter der  Firma1 und der hier nicht in Rede stehenden Firma2 bestellt worden.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)
- `Dr.in Ing. Viktoria Weigart` (person)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_154`)


In Beantwortung der nunmehr an Herrn Angelstein gerichteten (sechs) Lenkererhebungen der  belangten Behörde bestritt dieser seine Auskunftspflicht mit den Worten   1) bis 5) „dass ich weder ein Geschäftsführer dieser Firma noch mit diesem Fahrzeug gefahren  bin.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)


6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn Angelstein angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |
| `Russbüldt` | `Russbüldt` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_169`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_171`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste gegen ihn Anzeige erstattet werden.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_174`)


3. Zulässigkeit des Einspruches:  …  4. Gründe des Einspruches:  Der Vorwurf, der Einschreiter hätte als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin der Firma1 des Fahrzeuges mit dem behördlichen Kennzeichen Auto4  [Anmerkung BFG: nicht gegenständlich] dem ordnungsgemäß zugestellten Verlangen der MA  67 vom 28.01.2020, innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er  dieses Fahrzeug überlassen gehabt hat, sodass dieser zur in der Strafverfügung angegebenen  Tatzeit und Tatort gelenkt hat bzw. vor diesem Zeitpunkt abgestellt hat nicht entsprochen zu  haben und somit die Rechtsvorschriften des § 103 Abs 2 KFG [Anmerkung BFG, gemeint: § 2  (Wiener) Parkometerabgabeverordnung iVm § 4 Abs. 2 Parkometergesetz 2006] trifft nicht zu,  dies aus folgenden Gründen: Es wurde - wie oben erwähnt - vom Einschreiter die Übertragung  der Meldepflicht auf Herrn Angelstein  geb. Herrgeb, übertragen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_191`)


Darin hat die Einschreiterin  und deren handelsrechtliches Organ dargelegt, dass die verlangte Auskunft nicht erteilt werden  kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030 Wien als Verantwortlichen gemäß  § 9 VStG.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_213`)


Darin hat die Einschreiterin und deren handelsrechtliches Organ dargelegt, dass die verlangte  Auskunft nicht erteilt werden kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, als  Verantwortlichen gemäß § 9 VStG.  16 von 22 Seite 17 von 22

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Aron Pommeränke` | `Aron Pommeränke` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_21`)


Da der Gutachter Herr Karina Burfeindt selber sagte, wenn wir auch einen ärztlichen Befund haben, ändert es die ganzen Prozente,  und das haben wir jetzt.

| Predicted | Gold |
|---|---|
| `Karina Burfeindt` | `Karina Burfeindt` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_24`)


Frau Baues ist die Liquidatorin.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)


Zu den vereinbarten Einkaufskonditionen gab Herr Inn Trikraftglanz  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Borisowa` | `Borisowa` |
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_405`)


Frau Baues als Vertreterin der Beschwerdeführerin gibt bekannt, dass die Diesellieferungen 2 bis 3  Mal pro Woche stattgefunden haben.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_415`)


Die Anfrage beim Finanzamt deute vielmehr darauf hin,  dass Herr Inn Trikraftglanz  selbst Zweifel an der Seriosität der in Rede stehenden Lieferanten gehabt habe  und möglicherweise auch ein Naheverhältnis.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_424`)


Ein Naheverhältnis zwischen Herrn Inn Trikraftglanz und den gegenständlichen  Lieferanten hat es nicht gegeben.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `M.` (person)
- `Finanzamt` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |
| `Baues` | `Baues` |
| `Borisowa` | `Borisowa` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_6`)


Entscheidungsgründe  I. Verfahrensgang  1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Beschwerdeführerin (kurz Bf) ist eine GmbH, deren alleinige Gesellschafterin Frau Schneppensiefen ist.

| Predicted | Gold |
|---|---|
| `Schneppensiefen` | `Schneppensiefen` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Finanzamt Salzburg-Land` (organisation)
- `Finanzamt` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_32`)


In dem eingeleiteten Finanzstrafverfahren wurde Herr Harald Hilderink  jedoch beschuldigt,  vorsätzlich die Abgabe und Zahlung der Umsatzsteuervoranmeldungen unterlassen zu haben  und zu einer Geldstrafe von EUR 10.000,00 verurteilt. Gegen diese Straffestsetzung richtet sich  die vorliegende Beschwerde und geben wir als Begründung an:   Die ARGE wurde von einem Steuerberater vertreten, der mit der Abgabe der  Umsatzsteuervoranmeldungen beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)


Herr Harald Hilderink  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)


 Herr Harald Hilderink  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_38`)


Auf die Einhaltung von Fristen war Herr  Harald Hilderink  daher auf seine steuerliche Vertretung angewiesen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_40`)


Herr Harald Hilderink  ist nicht alleine dafür  verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |
| `Harald Hilderink` | `Harald Hilderink` |

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)


Da Herr Harald Hilderink  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)


Herr Harald Hilderink  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_81`)


Herr Harald Hilderink  ist verantwortlicher Geschäftsführer der ARGE.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_89`)


Zum Beschwerdevorbringen, „Herr Harald Hilderink  war auf die Einhaltung von Fristen auf seine  steuerliche Vertretung angewiesen, die mit der Abgabe der Umsatzsteuervoranmeldungen  beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_90`)


Herr Sahin konnte daher davon ausgehen, dass alle Meldungen  ordnungsgemäß und fristgerecht abgegeben werden bzw. die verspätete Abgabe der  Umsatzsteuervoranmeldungen war nicht vorsätzlich!

| Predicted | Gold |
|---|---|
| `Sahin` | `Sahin` |

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_95`)


Herr Harald Hilderink  ist nicht alleine dafür verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Roland Rößle` | `Roland Rößle` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_11`)


Unter Bezugnahme auf obige Ausführungen ist festzuhalten, dass Frau Waiser die  exklusive (einzige) Adressatin der Vollstreckungsverfügung vom 18. Mai 2022 ist, die hier aber  von jemandem anderen bekämpft wird.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_15`)


Im vorliegenden Fall hat jedoch nicht die Adressatin der verfahrensgegenständlichen  Vollstreckungsverfügung, nämlich Frau Waiser  sondern FirmaBfInhaberLautFirmenbuch,  Firmenbuchnummer FN im eigenen Namen Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung – direkt oder indirekt – von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt - von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_208`)


ad Schriftsatz des BMEIA vom 13.9.2018, der lautet (OZ 17):   „Sehr geehrter Herr [Magister],  19 von 38 Seite 20 von 38

**False Positives:**

- `Magister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_8`)


eigene Haus in Slowakei, meine Frau sie kenne keine deutsch, und natürlich eines Einkommen  für Österreich ist zu schwer für 2 Personen, in Slowakei wir haben eigene Haus, Garten und  Animal um welche brauchen wir aufpassen, das macht meine Frau. Ich arbeite nur hier und  sonst ich fahre jedes Wochenende nach Hause.

**False Positives:**

- `Ich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_65`)


Gleiches trifft auf die Ehegattin des Bf. zu.  Erkrankung der Ehegattin und des Bf.:  Im Vorlageantrag wurde erstmalig vorgebracht, ein Umzug nach Österreich sei nicht möglich,  weil seine Frau Krebs hat;

**False Positives:**

- `Krebs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Priv` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_10`)


Ein weiterer ärztlicher Befundbericht von Fr. Dr. **** und Herrn Dr. **** lagen ebenfalls dem  Antrag bei.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_105`)


Darin hat der Beschwerdeführer dargelegt, dass der  Beschwerdeführer die verlangte Auskunft nicht erteilen kann, sondern Herr Russbüldt  geb. Herrgeb,  AdrHerr, Verantwortlicher gemäß § 9 VStG.

**False Positives:**

- `Verantwortlicher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Russbüldt`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

**False Positives:**

- `Alexander` — partial — pred is substring of gold: `Alexander X.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexander X.`(person)
- `M.`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_20`)


In der Wohnung in Polen sind meine Frau, (Name-Gattin) und ich seit dem 08.01.1987  gemeldet, die Meldedaten lege ich Ihnen bei.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Gernot Thonhauser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Jedamczik`(person)
- `ÖkR Tobias Schönyan`(person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich`(address)
- `Mag. Gernot Thonhauser`(person)
- `Finanzamtes Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_8`)


FirmenwortlautBf  xStrasse  Ort  ATU UID-Nr  Herr Herr1  Herr Herr2.“

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_14`)


Vergl. hierzu “Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_84`)


Nachdem im § 37 Abs. 5 Z 3 EStG keine zeitliche Frist normiert ist, stellt  die ungeplante Wideraufnahme der gerichtlichen Sachverständigentätigkeit keine schädliche  Erwerbstätigkeit dar.“   < Schreiben BG A vom 23.7.2019:  „Herr Beschwerdeführer hat die Austragung aus der Liste der Sachverständigen mit 30.6.2016  entsprechend an die Präsidentin des Landesgerichtes W kommuniziert.

**False Positives:**

- `Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_36`)


Zur gemeinsamen mündlichen Verhandlung (Streitsachen: 1. und 2. Zwangsstrafe) erscheinen  zwei Rechtanwälte, Herr Dr. Karl RA1, der auch als Geschäftsführer der Bf. eingetragen ist, und  Herr RA2.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_64`)


Beweis: Person4, als Zeuge, Person3  Folgender Mailverkehr wurde in der mündlichen Verhandlung seitens der Bf. vorgelegt, im  Wesentlichen:  STB2 an BMF1 (BMF Abteilung III/12), gesendet 5. Oktober 2021:  S.g. Herr Ministerialrat, wie schon kürzlich tel.

**False Positives:**

- `Ministerialrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)


Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_17`)


Es würden mit Herrn Ing. K. (Geschäftsführer der Fa. X.  2 von 9 Seite 3 von 9

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_19`)


Die Entlehnung des Kfz gehe auf ein privates Ersuchen des Herrn Ing. K. zurück.

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation
- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)


Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die Jeremias Kierstan, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Jeremias Kierstan`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_28`)


Der angefochtene Bescheid vom 17.07.2015, mit welchem über den Antrag der Heimwerk GmbH auf  Herabsetzung der Abwassergebühr für 2013 abgesprochen wurde, ist an die Jeremias Kierstan  als  Partei ergangen und an deren Zustellbevollmächtigten, Herrn Vertreter zugestellt worden.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Jeremias Kierstan`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_67`)


Herr Dr. Alma Goerts (steuerliche Vertretung) bringe in der  Beschwerde nun selbst vor, dass die Einhaltung gegenständlicher Frist ausschließlich in seiner  Befugnis gelegen habe und er aufgrund des Todesfalls in seinem privaten Umfeld vergessen  habe, einem seiner Mitarbeiter die Weisung zur Einbringung eines Fristverlängerungsantrages  zu erteilen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_70`)


Auch wenn Herr Dr. Alma Goerts  nach eigenen Angaben  bislang noch nie eine Frist versäumt habe, dürfe die Einhaltung von Fristen (Fristenwahrung)  für die Steuerberatungskanzlei nicht "ausschließlich" in seinem alleinigen Bereich liegen bzw.  es müsse durch entsprechende Kontrollmechanismen vorgesorgt werden, dass  Unzulänglichkeiten durch menschliches Versagen (wie z.B. durch Vergessen) aller Voraussicht  nach ausgeschlossen seien.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_71`)


Ein Vergessen der Frist wäre nach Ansicht der Abgabenbehörde  leicht zu verhindern gewesen, wenn einer der sechs Kanzleimitarbeiter Herrn Dr. Alma Goerts  rechtzeitig auf den Ablauf der Frist hingewiesen hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_72`)


Möglicherweise hätten die  Kanzleimitarbeiter keinen Einblick in den Terminplan des Herrn Dr. Alma Goerts (bzw. in den  Fristenkalender).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_73`)


Möglicherweise seien sie aber "vor" Erteilung eines Auftrags durch Herrn Dr.  Alma Goerts  einfach nicht für diese Angelegenheit zuständig.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_67`)


Über die diesbezügliche Rücksprache mit der belangten Behörde sei vom steuerlichen  Vertreter am 7. August 2001 ein Aktenvermerk angelegt worden, welchen folgenden Inhalt  habe:  ….“Haben dies mit Herrn Mag. ***, FA Feldkirch am 7. August 2001 nochmals besprochen und  um einen Lösungsvorschlag gebeten: Nach Mag. *** soll die liechtensteinische FA Spittal Villach  eine  Proformarechnung an die RHO Pharma  ausstellen, somit wird die RHO Pharma  zum "Proforma  Verfügungsberechtigten" und kann die abgeführte Einfuhrumsatzsteuer problemlos als  Vorsteuer geltend machen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Feldkirch`(organisation)
- `FA Spittal Villach`(organisation)
- `RHO Pharma`(organisation)
- `RHO Pharma`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_29`)


Geschäftsführer der Gesellschaft ist seit ihrer Gründung Herr Gf.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_30`)


Herr Gf ist darüber hinaus  alleiniger Gesellschafter-Geschäftsführer der Carrasco Software GmbH  der 100%-igen Muttergesellschaft der  Bf.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Carrasco Software GmbH`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Johanna Thönßen, Natrun 54, 9560 Regenfeld, Österreich, vertreten durch seine Ehegattin, Ehegattin, über die Beschwerde vom 22. Juni 2020  gegen den Bescheid des Finanzamtes Österreich vom 2. Juni 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Steuernummer 56-442/5216  nach  der am 04.06.2024 im Beisein der Schriftführerin Frau Schriftführerin durchgeführten  mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Schriftführerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johanna Thönßen`(person)
- `Natrun 54, 9560 Regenfeld, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `56-442/5216`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_27`)


Mit Vorlageantrag vom 16.07.2024 wurde die Entscheidung über die Beschwerde durch das  Bundesfinanzgericht beantragt und ergänzend wie folgt begründet:  „[…] Ergänzend zur Beschwerde vom 15.02.2024 wird vorgebracht, dass Herrn Luna Fruechtenicht  Seitens der Pensionsversicherungsanstalt zwischenzeitlich eine Waisenpension zugesprochen  wurde und entsprechend die Erwerbsunfähigkeit infolge Krankheit oder Gebrechens ab der  Kindheit über das 18.

**False Positives:**

- `Luna Fruechtenicht  Seitens` — partial — gold is substring of pred: `Luna Fruechtenicht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Luna Fruechtenicht`(person)
- `Pensionsversicherungsanstalt`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_56`)


Ergänzung zu Tz6 F KG  Von welcher Person die Leistung erbracht wurde, ist letztlich nicht von Bedeutung, auch wenn  mehrmals ausgeführt wurde, dass die Leistungen von Herrn *Name* erbracht wurden.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_123`)


4. Naheverhältnis der zwischen der beschwerdeführenden Partei und Eberler Bau KG  B KG, C KG,  D KG, E KG und F KG  Faktischer Geschäftsführer und alleiniger Machthaber sei nach den Feststellungen der  belangten Behörde sowohl bei der beschwerdeführenden Partei als auch bei allen angeführten  KGs Herr *Name*.

**False Positives:**

- `Name` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Eberler Bau KG`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_151`)


Der Steuerberater von Frau NN1 – Herr Kollege Z von der öStb-Kanzlei – ist cc. gesetzt.

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NN1`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_152`)


Herr Kollege Z und ich konnten uns heute abstimmen.

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_155`)


Diesem Verzicht stimmt Herr Kollege Z in Vertretung von Frau  NN1 zu.  11 von 34 Seite 12 von 34

**False Positives:**

- `Kollege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `NN1`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_21`)


Im vorliegenden Fall konnte nur Frau Einspruch erheben oder dessen Rechtsvertreterin, nicht  aber eine andere Person.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_109`)


Zudem wurde vom Geschäftsführer, Herrn Gf., bei der Schlussbesprechung gem § 149 Abs  1 BAO am 12.12.2017 mitgeteilt, dass in Peru keine steuerliche Erfassung der Betriebsstätte  erfolgte, dies wurde auch im Schreiben vom 22.12.2017 bestätigt.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `legal_person_representative_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0fed4db2`  
**Description:**
Captures names following 'vertreten durch' or 'Bevollmächtigten', ensuring it captures the full name including titles.

**Content:**
```
(?:vertreten\s+durch(?:\s+(?:den|der))?)([A-Z][a-zäöüß]+(?:\s+(?:Mag\.a?|Dr\.in?|RA|MMag\.))?)(?:[A-Z][a-z]+(?:[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `legal_person_preposition_from` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8f653722`  
**Description:**
Captures names following 'von' in correspondence contexts, excluding legal entities.

**Content:**
```
(?:Schreiben|E-Mail|Mitteilung|Anfrage)\s+von\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?!\s+(?:Behörde|Republik|Finanzamt|Gericht|AG|KG|GmbH))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 7 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_22`)


Das Arbeitszimmer wird verwendet zur Vorbereitung der  Musikstunden, Download von Noten, Schreiben von Noten und zum Üben auf dem E-Piano, vor  allem wenn der späten Uhrzeit wegen ein Spielen auf dem Flügel nicht mehr möglich ist.

**False Positives:**

- `Noten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_139`)


Wir dürfen hierzu auf das Schreiben von Richter Dr. V hinweisen, der in  seinem Schreiben vom 23.07.2019 darauf hinweist, dass die Bestellung trotz Austragung aus  der Sachverständigenliste erfolgt ist, um Verzögerungen bei gerichtlichen Verfahren zu  vermeiden.

**False Positives:**

- `Richter Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_88`)


Schreiben  von Fr. A, vom 25.11.2020 Behandlung/en / Medikamente / Hilfsmittel: Laut Befund  Schielambulant, Universitäts-Augenklinik Ort3, vom 17.11.2015: Braille- Zeile, Schulcomputer,  Laptop.

**False Positives:**

- `Fr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_133`)


Von August bis Oktober 2022 hat der Sohn dann ein Praktikum am Bezirksgericht F absolviert,  welches ab November 2022 zunächst zu einem befristeten und ab März 2023 zu einem  unbefristeten Dienstverhältnis mit gesamt 25 Wochenstunden geführt hat; bei dieser Tätigkeit  (ua. Schreiben von Urteilen, Diktaten) wird er laufend von der Arbeitsassistenz technisch und  persönlich unterstützt (siehe zu vor: eigene Angaben, Bestätigung XY v. 7.10.2021 und ua.

**False Positives:**

- `Urteilen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_17`)


Die Bf. legte im Zuge der Beschwerde folgende Unterlagen vor:  Schreiben von Mag. Dr.in Carina B., Psychotherapeutin:  T. befindet sich seit 12. April 2022 auf Grund ihrer psychischen Erkrankung in einer  regelmäßigen ambulanten Psychotherapie bei ihr.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Dr.in Carina B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Dr.in Carina B.`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_81`)


Zufolge der vom Bf. weitergeleiteten E-Mail von Wienenergie (E-Mail vom 12. März 2024)  startete der Ladevorgang am 6. April 2023 um 14:38:53 Uhr und war um 17:16:48 Uhr  beendet.

**False Positives:**

- `Wienenergie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/146279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146279.1_83`)


Dem Vorbringen des Bf, die Beschwerdevorentscheidung sei lt. Mitteilung von FinanzOnline  erst am 12.6.2024 zugestellt worden, ist zu entgegnen, dass die Zustellung eines Bescheides  mit der Einbringung in die Databox und nicht mit der Verständigung darüber erfolgt (siehe BFG  20.11.2015, RV/2100371/2015, und 13.11.2024, RV/5100701/2024).

**False Positives:**

- `Finanz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1258, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)

Die **Dr.in Ing. Viktoria Weigart** wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

- missed: `Dr.in Ing. Viktoria Weigart` (person)
- predicted in sentence: `Angelstein`

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  **HR OSR Leonie Ercklentz**, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `HR OSR Leonie Ercklentz` (person)
- predicted in sentence: `Dr. Siegfried Fenz`

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_2`)

Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde des  **OMedR Tanja Kubatsch**, Sand/Bundesstraße 2, 4170 Damreith, Österreich, vom 21. Oktober 2022, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 21. September 2022, GZ. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `OMedR Tanja Kubatsch` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Thomas Schmidt in der Finanzstrafsache  gegen **Linda Tumpach**, Gengerberg 44, 4052 Ansfelden, Österreich, vertreten durch Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer, Wiener Straße 3, 3100 St. Pölten, über die Beschwerde der Beschuldigten vom  25.11.2019 gegen den Bescheid des Amtes für Betrugsbekämpfung als Finanzstrafbehörde  (ehemals des Finanzamtes Lilienfeld St. Pölten als Finanzstrafbehörde ) vom 17. Oktober 2019,  Strafkontonummer 91-951/0670, betreffend die Abweisung eines  Zahlungserleichterungsansuchens (Stundungs- und Ratenansuchen) gemäß § 156 Abs. 1 des  Finanzstrafgesetzes (FinStrG) in Verbindung mit   § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) beschlossen:  Die Beschwerde wird als unzulässig zurückgewiesen, da es sich beim gegenständlich  bekämpften so genannten Bescheid um einen Nichtbescheid handelt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Linda Tumpach` (person)
- predicted in sentence: `Mag. Thomas Schmidt`

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_48`)

Im zentralen  Melderegister scheint ein **Dr. Karl** RA1 ab 2010 mit der Adresse AdresseWien auf (mit  3 von 16 Seite 4 von 16

- missed: `Dr. Karl` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_42`)

K. sei zwar beim Vorstellungsgespräch der Fa. e. mit einer zweiten Person (Kristian **M.**) in den  Firmenräumlichkeiten in T. gewesen, sei aber dabei in keinster Weise in Erscheinung getreten.

- missed: `M.` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_13`)

Mit Schreiben vom 30. Dezember 2020 wurde die Fa. E. – **Balthasar Brendtke** (kurz: E.) unter Anführung  der erforderlichen Daten als jene Person, die das ihr von der Zulassungsbesitzerin des näher  bezeichneten Fahrzeuges zur Verfügung gestellte Fahrzeug einem Dritten überlassen habe,  gemäß § 2 Wiener Parkometergesetz 2006 zur Lenkerauskunft binnen zwei Wochen ab  Zustellung des Schreibens aufgefordert.

- missed: `Balthasar Brendtke` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/147137.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147137.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache RgR Shirley Ribler, Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich, vertreten durch **Dr. Christian Lind**,  Am Ausblick 17, 3110 Neidling, über die Beschwerde vom 2. Jänner 2023 gegen die Bescheide  des Finanzamtes Österreich vom 1. Dezember 2022 betreffend Anspruchszinsen (§ 205 BAO)  2016, 2017 und 2018, Steuernummer 64-511/1773, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Christian Lind` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Marceline Flory**  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Univ.-Prof.in Marceline Flory` (person)
- predicted in sentence: `Stephan Zeitlhuber`

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Mag. Wladimir Ferrarese**  über die Beschwerde des Hademar Mühlenstedt,  Kohlengasse 373, 8442 Sankt Andrä im Sausal, Österreich, vom 22. Juni 2025, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 20. Juni 2025, GZ. MA67/GZ1/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, Amtsblatt  der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, Landesgesetzblatt für Wien Nr. 9/2006 in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 VwGVG wird der Beschwerde insoweit Folge gegeben, als gemäß § 45 Abs. 1  VStG von der Verhängung einer Strafe abgesehen und dem Beschwerdeführer unter Hinweis  auf die Rechtswidrigkeit seines Verhaltens eine Ermahnung erteilt wird.

- missed: `Mag. Mag. Wladimir Ferrarese` (person)
- predicted in sentence: `Mag. Mag`

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/144086.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144086.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Ruperta Wengrzinek**  in der Beschwerdesache Ali Oberste,  Wolfsedt 11, 4211 Lindach, Österreich, Steuernummer 03-949/9780  über die Beschwerde vom 7. August 2019  gegen den Bescheid des Finanzamtes Feldkirch vom 30. Juli 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hon.-Prof.in Ruperta Wengrzinek` (person)
- predicted in sentence: `Ali Oberste`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_162`)

Verwaltungsverfahrensrechtes DDr.  Walter, **DDr. Maier**, Seite 131).

- missed: `DDr. Maier` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Monika Kofler** in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

- missed: `Dr. Monika Kofler` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache **Ing. Edith Schifferdecker**,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

- missed: `Ing. Edith Schifferdecker` (person)
- predicted in sentence: `Hon.-Prof. Dominik Mehlig`, `Edith Schifferdecker`

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_36`)

Zur gemeinsamen mündlichen Verhandlung (Streitsachen: 1. und 2. Zwangsstrafe) erscheinen  zwei Rechtanwälte, Herr **Dr. Karl** RA1, der auch als Geschäftsführer der Bf. eingetragen ist, und  Herr RA2.

- missed: `Dr. Karl` (person)
- predicted in sentence: `Dr`

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Barbara Schwalb**  in der Beschwerdesache Annalena Mlynarcik,  Ledochowskastraße 5, 4040 Kammerschlag, Österreich, über die Beschwerde vom 02.03.2017 gegen die Bescheide des Finanzamtes  Österreich vom 28. Februar 2017 betreffend Abweisung des Antrages auf Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre Wiederaufnahme § 303 BAO /  ESt 2011  -2013 Steuernummer 09-012/5071  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hon.-Prof.in Barbara Schwalb` (person)
- predicted in sentence: `Annalena Mlynarcik`

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_491`)

1.08.2012 begonnene unbefristete Mietverhältnis für Top 4 von den Vertragsparteien Bf. und  **M.M.B.2** unter Einhaltung einer dreimonatigen Kündigungsfrist zum letzten eines Monats  aufgekündigt werden hätte können, offensichtlich.

- missed: `M.M.B.2` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_35`)

Das Finanzamt folgte den Feststellungen der Betriebsprüfung und erließ in Abweichung  der eingebrachten Abgabenerklärung 2015 den Feststellungsbescheid Gruppenmitglied 2015  **Tamara Gottschalch** 22-144/9009  vom 12. März 2018.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_3`)

Entscheidungsgründe  I. Verfahrensgang:  1.) Aufgrund von Erhebungen der Finanzpolizei (Kontrollmitteilung vom 18.1.2010) wurde ua.  aufgrund einer Anhaltung (im September 2009) festgestellt, dass das von **Josefine Frikel** (=  Beschwerdeführer, Bf), österreichischer Staatsbürger, im Inland gelenkte Fahrzeug der Marke  Audi A6 AVANT mit dem deutschen Kennzeichen (Kz) W1, zugelassen auf den deutschen  Staatsbürger A, von diesem der Verwaldgart GmbH bzw. dem Bf als Geschäftsführer seit 1.11.2008 zur  Nutzung zur Verfügung gestellt worden sei;

- missed: `Josefine Frikel` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/147713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147713.1_2`)

Begründung  **Knut Waldhauer**   hat durch seinen steuerlichen Vertreter mit Eingabe vom 04. Jänner 2025, eingelangt am 04.  Jänner 2025, gemäß § 284 Abs. 1 BAO eine Säumnisbeschwerde wegen Verletzung der  Entscheidungspflicht betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 und 2023  erhoben.

- missed: `Knut Waldhauer` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  **Valentin Joebges, LLM**, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Valentin Joebges, LLM` (person)
- predicted in sentence: `Valentin Joebges`

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/143846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143846.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Rüdiger Tormählen**  in der Beschwerdesache  Melina Weingartz, KLG Aus eigener Kraft 31, 3830 Vestenpoppen, Österreich, über die Beschwerde vom 20. Oktober 2023 gegen den Bescheid  des Finanzamtes Österreich vom 14. September 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 77-866/9586  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Rüdiger Tormählen` (person)
- predicted in sentence: `Melina Weingartz`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_42`)

Ein **RA Dr.  Carl** RA1 mit identer Adresse in NÖ und identer Handynummer brachte hingegen für die Bf. die  Vorlageanträge (1.4.2019 und 16.8.2019) ein.

- missed: `RA Dr.  Carl` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_186`)

Über Befragen, worin die Verschreibungen von Vitamin B, C und D zu ersehen seien, gab sie an,  dass **Dr. G** Neurobin (Anm.: dürfte „Neurobion“ sein) in einem Vorjahr verschrieben, die  Ehegattin dieses aber nicht vertragen habe.

- missed: `Dr. G` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/148962.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148962.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Univ.-Prof. Ramon Löther  in der Beschwerdesache Axel Pommeränke,  Zum Hauptplatz 2, 4030 Linz, Österreich, vertreten durch **Mag. Niki Zaar**, Babenbergerstraße 9/1/8, 1010 Wien,  betreffend die Vorlage der Bescheide des Finanzamtes Österreich vom 9. Oktober 2023 über  die Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2018 und 2019 im Wege  des Vorlageberichtes vom 21. November 2024 zur Steuernummer 14-979/7189  den  Beschluss:  Das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

- missed: `Mag. Niki Zaar` (person)
- predicted in sentence: `Priv.-Doz. Univ`, `Axel Pommeränke`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_108`)

13.11.2019,22.11.2019, 6.12.2019 (Mutter), 11.12.2019,  20.12.2019 (Mutter), 08.01.2019  Frau F. **M.** kommt an die psychologische Universitätsambulanz der X Privatuniversität um eine  Autismusdiagnostik durchführen zu lassen.

- missed: `M.` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)

Das Büro in **Univ.-Prof.in Miriam Ungruh**  war auch im Interesse meines Arbeitgebers.

- missed: `Univ.-Prof.in Miriam Ungruh` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_61`)

Der Beschwerde war eine Auftragsbestätigung der Post vom 21. April  2020 mit der Auftragsnummer ANr beigelegt, der folgende Abwesenheitsmitteilung  entnommen werden kann:   Bewohner: **Hilde Schorpp**  Adresse: Adresse  Zeitraum: Ab 24.04.2020 bis 31.08.2020  Sendungsarten: RSa-und RSb-Briefe.

- missed: `Hilde Schorpp` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_168`)

(vgl EuGH 18.09.2019, C-32/18, Michael Moser, EuGH 22.1.2015, C- 378/14, Omislaw **Trapkowski**, EuGH 14.10.2010, C-16/09, Schwemmer, BFG 27.06.2023,  RV/7105857/2017)

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_49`)

Beschwerdesache ist der Anspruch der Beschwerdeführerin (Bf) **Olivia Trienes**  auf den  Erhöhungsbetrag zur Familienbeihilfe für den Sohn A, geb.   .6.1997, wg. erheblicher  Behinderung, konkret wg. "Diabetes Mellitus Typ I", iSd § 8 Abs. 5 f. FLAG 1967 idgF "ab März  2022" strittig.

- missed: `Olivia Trienes` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_145`)

Ein Gespräch mit Hern **OA Dr.  Bieber** bezüglich des weiteren psychotherapeutischen Procedere wurde vor der Entlassung  durchgeführt.“

- missed: `OA Dr.  Bieber` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache **Jaden Grothmann**  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Jaden Grothmann` (person)
- predicted in sentence: `Univ.-Prof. Massimo Friedhoff`

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag.a Stella Hornscheidt**  in der Beschwerdesache Ing. Jaden Stoelzl,  Singham 49, 4274 Straß, Österreich, über die Beschwerden vom 1. Juni 2021 gegen die Bescheide des Finanzamtes  Österreich vom 31. Mai 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016,  2017 und 2018 Steuernummer 25-717/7817  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag.a Stella Hornscheidt` (person)
- predicted in sentence: `Jaden Stoelzl`

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  **Harald Schwalbach**, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

- missed: `Harald Schwalbach` (person)
- predicted in sentence: `Dr. Siegfried Fenz`

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_21`)

Das Regelkontakt- recht entfällt während **Fabios** Weihnachtsferien für beide Kinder.

- missed: `Fabios` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des **Josepha Peifers** Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Josepha Peifers` (person)
- predicted in sentence: `Mag. Josef Ungericht`

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter **Mag. Markus Knechtl LL.M.** in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

- missed: `Mag. Markus Knechtl LL.M.` (person)
- predicted in sentence: `Mag. Markus Knechtl`, `Saphira Schnaak`

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/141080.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141080.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Mag.a Abigail Dausener**  in der Beschwerdesache HR OSR Samir Fatthauer,  Viehdorferstraße 27, 4192 Steinschild, Österreich, über die Beschwerde vom 16. Februar 2023 gegen die Bescheide des FA Wien 2/20/21/22  vom 11. Jänner 2023 betreffend Abweisung von Anträgen auf Wiederaufnahme der Verfahren  hinsichtlich Umsatz- und Einkommensteuer 2016 zu Recht erkannt:   I.)

- missed: `Hon.-Prof.in Mag.a Abigail Dausener` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_104`)

Zu diesem Zweck sei auch ein Mitarbeiter der **Tamara Gottschalch**  vor  Ort gewesen, welcher für den reibungslosen Betrieb der Anlage verantwortlich gewesen sei.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Mag. Anna Mechtler-Höger** in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Mag. Anna Mechtler-Höger` (person)
- predicted in sentence: `Jeremias Kierstan`

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_2`)

Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des **Rosalia Schmieter**, Collmannstraße 3, 3335 Lindau, Österreich  vom 22. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. September 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,idgF,  iVm § 4 Abs. 1 Parkometergesetz 2006, Landesgesetzblatt Nr. 9/2006 idF LGBl für Wien Nr.  24/2012, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

- missed: `Rosalia Schmieter` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/145832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145832.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache **StR OSR OStR Torsten Schlichtenmeier**, Untere Waldalpe 2, 5204 Voglhub, Österreich, (Beschwerdeführerin, abgekürzt: Bf.), über  deren Beschwerde vom 25. Jänner 2024 gegen den Einkommensteuerbescheid 2022 des  Finanzamtes Österreich vom 11. Jänner 2024 zu Steuernummer 20-897/4296  zu Recht  erkannt:  Der Beschwerde wird teilweise stattgegeben und der angefochtene Bescheid gemäß § 279  Abs. 1 BAO abgeändert.

- missed: `StR OSR OStR Torsten Schlichtenmeier` (person)
- predicted in sentence: `Mag. Christian Seywald`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_137`)

 2015 **Gerald Bährensmann**  Gebäude (100) (ER 15001-15008;

- missed: `Gerald Bährensmann` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_22`)

In der dagegen fristgerecht am eingebrachten Beschwerde des Amtsbeauftragten vom  3. Dezember 2020 wird wie folgt ausgeführt:  Angefochten werde die Einstellung gem. § 136 FinStrG hinsichtlich der Geschäftsführerin A B,  Adresse1, sowie des belangten Verbandes die Saskia Sinnwell, Franz-Michel-Willam-Weg 31, 3580 Groß Burgstall, Österreich  mit folgendem  Inhalt:  „Die Grundlage des Verfahrens bildet die Betriebsprüfung vom 09.10.2019 bei der **Saskia Sinnwell**,  bei welcher festgestellt wurde, dass ein Liegenschaftsverkauf im Juni 2019 nicht in der UVA  gemeldet wurde.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_15`)

In den restlichen Wochen der Sommerferien entfällt sein  Regelkontaktrecht zu S.. Der Vater ist berechtigt, **Adrian** gemeinsam mit S. in der zweiten  Woche von Fabios Sommerferien durchgehend zu betreuen.

- missed: `Adrian` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag.a Tamara Steinmüller**  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Mag.a Tamara Steinmüller` (person)
- predicted in sentence: `Gueldner Garten`

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_28`)

Somit geht auch die Darlehensforderung der M-Gesellschaft auf die **Gotthard Angelstein**  über.

- missed: `Gotthard Angelstein` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_283`)

2020-10 **Mike Staengel**  praktischer Arzt: seit Geburt Zeichen eines Aspergersyndroms mit thera- pieresistenten Schlafstörungen, Ruhelosigkeit, stereotypen Bewegungen (Stampfen mit dem  Fuß), Rückzug in eine eigene Welt, was im Kindergarten und in der Schule aufgefallen ist.

- missed: `Mike Staengel` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_62`)

Dem entsprechend wurde am 2.5.2023 von Dr.in E, Allgemeinmedizinerin, vidiert von **Dr. D**  am 3.5.2023, neuerlich ein SMS-Gutachten "mit Untersuchung" (siehe als Beilage für die Bf)  mit auszugsweise folgendem Inhalt erstellt und an das BFG am 26.5.2023 weitergeleitet:  " …. Anamnese:   Angeborene Hornhauttrübung und -vaskularisation beider Augen bei kongenitaler  Sklerokorona, Hornhautverpflanzung mit 10 Monaten rechts ohne Erfolg, seither  Mikrophtalmus rechts    wegen Blasenentleerungsstörungen bis 2018 medikamentöse Therapie   seit 2016 Loch in Nasenscheidewand bekannt   ab 2017 zwei Jahre in psychologischer Betreuung;

- missed: `Dr. D` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_194`)

Der **Gertrude Holzmenger**  ist in zweistufiger Sektor mit der Dorothea Hasslocher  als Zentralinstitut und den  angeschlossenen Dimitri Dancker  als Primärinstitute.

- missed: `Gertrude Holzmenger` (person)
- predicted in sentence: —

</details>

---

