# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-17T15:23:20.107805

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-17_v3/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 3148 |
| Validation documents | 787 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 7310 |
| Validation sentences | 2144 |
| Dev sentences | 61673 |
| Test sentences | 61001 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 150 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
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
| Accuracy (exact match) | 98.3% |
| True Positives | 694 |
| False Positives | 277 |
| False Negatives | 1157 |
| Total Gold Entities | 1851 |
| Micro Precision | 71.5% |
| Micro Recall | 37.5% |
| Micro F1 | 49.2% |
| Macro F1 | 49.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Names after 'in der Beschwerdesache' context` | 21.7% | 95.0% | 12.3% | 239 | 227 | 12 |
| `Names after 'Frau' or 'Herr' (Accusative/Dative)` | 1.6% | 88.2% | 0.8% | 17 | 15 | 2 |
| `Names after 'Beschwerde des' (Genitive)` | 3.6% | 87.2% | 1.8% | 39 | 34 | 5 |
| `Single Word Names after 'Herrn' or 'Frau'` | 6.4% | 79.5% | 3.3% | 78 | 62 | 16 |
| `Names with Split Titles (e.g. Univ- Prof.)` | 29.8% | 76.3% | 18.5% | 448 | 342 | 106 |
| `Names after 'von' (Family/Relation Context)` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Names with 'VetR' and similar standalone titles` | 1.4% | 28.9% | 0.7% | 45 | 13 | 32 |
| `Names after 'Bf,' (Comma separated)` | 0.0% | 0.0% | 0.0% | 99 | 0 | 99 |
| `Names after 'von' (Befunden/Gutachten)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after 'Arbeitsplatz des' (Contextual)` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Names after 'Herrn' or 'Frau' (Accusative/Dative)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after 'von' (General Context)` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Names after 'durch' (Judge/Representative)` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Names after 'in der Beschwerdesache' context` 🏆

**F1:** 0.217 | **Precision:** 0.950 | **Recall:** 0.123  

**Format:** `regex`  
**Rule ID:** `8ee5a0d4`  
**Description:**
Captures the name following 'in der Beschwerdesache' with titles, using a capture group to exclude the context phrase.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|in\s+der\s+Sache|in\s+der\s+Revisionssache|in\s+der\s+Verwaltungsstrafsache)\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+r\.\s+nat\.|\s+art\.|\s+techn\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.|Techn\s+R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.950 | 0.123 | 0.217 | 239 | 227 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 227 | 12 | 1624 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emmerich Frydrychowski` | `Emmerich Frydrychowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Klocksin` | `Gregor Klocksin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Unterguntschach 85, 3525 Armschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Frauke Galleithner` | `Frauke Galleithner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

| Predicted | Gold |
|---|---|
| `Dora Szczepanowski` | `Dora Szczepanowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marlies Seipold, Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich, über die Beschwerde vom 27. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 14. Jänner 2020 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum März 2017 bis September 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Seipold` | `Marlies Seipold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jaden Grothmann` | `Jaden Grothmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Massimo Friedhoff` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Maximiliane Gasparetti, Gschwandtkopf 12, 9330 Althofen, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 23. Dezember 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. November 2016 betreffend  1.

| Predicted | Gold |
|---|---|
| `Maximiliane Gasparetti` | `Maximiliane Gasparetti` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Gschwandtkopf 12, 9330 Althofen, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache David Radeke, Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich, über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 18. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierte Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019,   Steuernummer 15-752/7224, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `David Radeke` | `David Radeke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-752/7224` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Richard Reithmayer, Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Bundesstraße  36, 6923 Lauterach, gegen die Bescheide des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer 2015 und 2016 sowie Festsetzung von  Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Richard Reithmayer` | `Richard Reithmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Herbert Lindermayer  in der Beschwerdesache Anneliese Dreschmann,  Nußbacher Straße 43, 3650 Kehrbach, Österreich, vertreten durch Schwaiger & Partner Steuerberatung, Anton-Eder-Straße 5,  6020 Innsbruck, über die Beschwerde vom 19. Jänner 2021 gegen den Bescheid des FA Graz-Stadt  vom 13. Jänner 2021 betreffend Energieabgabenvergütung 2015 Steuernummer  60-855/1189  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anneliese Dreschmann` | `Anneliese Dreschmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Herbert Lindermayer` (person)
- `Nußbacher Straße 43, 3650 Kehrbach, Österreich` (address)
- `Schwaiger & Partner Steuerberatung` (organisation)
- `FA Graz-Stadt` (organisation)
- `60-855/1189` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Gernot Schellhaas  in der Beschwerdesache Guntram Garweg,  Umspannwerkstraße 21, 3912 Kleinnondorf, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Erhöhungsbetrag zur Familienbeihilfe wegen  erheblicher Behinderung für den Zeitraum September 2015 bis Jänner 2019, Steuernummer  92-268/1285,  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Guntram Garweg` | `Guntram Garweg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Univ.-Prof. Gernot Schellhaas` (person)
- `Umspannwerkstraße 21, 3912 Kleinnondorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `92-268/1285` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Bianca Kristeller, Schröckbach 58, 9652 Nostra, Österreich, über die Beschwerde vom 9. Dezember 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2021 betreffend Familienbeihilfe 10.2020-09.2021  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bianca Kristeller` | `Bianca Kristeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schröckbach 58, 9652 Nostra, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/138353.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138353.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hubert Wunderlin  in der Beschwerdesache Friedhelm Fomin,  Riedlbachstraße 8, 3970 Oberbrühl, Österreich, vertreten durch ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H., Postfach 257, 1061 Wien Postfach, über die Beschwerde  vom 15. August 2021 gegen den Bescheid des Finanzamtes Österreich vom 13. Juli 2021  betreffend Covid-19 Zahlungserleichterung, Steuernummer 25-245/7156, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Friedhelm Fomin` | `Friedhelm Fomin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Hubert Wunderlin` (person)
- `Riedlbachstraße 8, 3970 Oberbrühl, Österreich` (address)
- `ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `25-245/7156` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/138313.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Ibrahim Walterscheid, Wallsiedlung 55, 3970 Walterschlag, Österreich, vertreten durch UNICONSULT Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Wartenburger Straße 1b, 4840 Vöcklabruck, betreffend Beschwerde  vom 27. April 2022 gegen den Bescheid des Finanzamtes Österreich vom 25. März 2022  betreffend Einkommensteuer 2020 Steuernummer 78-985/8140  beschlossen:  Die Beschwerde wird wegen Verspätung gemäß § 260 Abs. 1 lit. b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ibrahim Walterscheid` | `Ibrahim Walterscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Wallsiedlung 55, 3970 Walterschlag, Österreich` (address)
- `UNICONSULT Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `78-985/8140` (tax_number)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Günter Salahi  in der Beschwerdesache Jaden Knauss,  Dossenweg 3, 4132 Atzesberg, Österreich  über die Beschwerde vom 8. Jänner 2021 gegen den Bescheid des Finanzamtes  Österreich vom 3. Dezember 2020 Rückzahlung gemäß § 239 BAO, Steuernummer  15-678/4603  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jaden Knauss` | `Jaden Knauss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Hon.-Prof. Günter Salahi` (person)
- `Dossenweg 3, 4132 Atzesberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `15-678/4603` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank  in der Beschwerdesache Nicoletta Nipshagen, Obergrafendorfer Straße 11, 9141 Oberburg, Österreich,  über die Beschwerde vom 1. Mai 2021 gegen den Einkommensteuerbescheid  (Arbeitnehmerveranlagung) für das Jahr 2020 des Finanzamtes Österreich vom 26. April 2021,  Steuernummer 02-339/1714, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Nicoletta Nipshagen` | `Nicoletta Nipshagen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helga Woschank` (person)
- `Obergrafendorfer Straße 11, 9141 Oberburg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `02-339/1714` (tax_number)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Janina Gruenaeugl, Geiereckstraße 27, 4720 Güttling, Österreich, Schweden, vertreten durch die Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H., Wagramer Straße 19, 1220  Wien, über die Beschwerde vom 9. Jänner 2017 gegen den Bescheid des Finanzamtes für  Großbetriebe (vormals Bruck Eisenstadt Oberwart) vom 13. April 2015 betreffend Abweisung  eines Antrages auf Rückzahlung Österreichischer Lohnsteuer,Einkommensteuer 2012  Steuernummer 65-008/8295  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Janina Gruenaeugl` | `Janina Gruenaeugl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elisabeth Hafner` (person)
- `Geiereckstraße 27, 4720 Güttling, Österreich` (address)
- `Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H.` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `65-008/8295` (tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jeremias Kierstan` | `Jeremias Kierstan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich` (address)
- `Peter Schabel` (person)
- `Magistrats  der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)


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

</details>

---

## `Names after 'Frau' or 'Herr' (Accusative/Dative)` 🏆

**F1:** 0.016 | **Precision:** 0.882 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `7078c2ee`  
**Description:**
Captures full title and name following 'Herrn' or 'Frau', ensuring the name includes at least a first and last name (or title + first + last) to avoid partial matches.

**Content:**
```
(?:Herrn|Frau)\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.882 | 0.008 | 0.016 | 17 | 15 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 15 | 2 | 1836 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Borisowa` (person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_424`)


Ein Naheverhältnis zwischen Herrn Inn Trikraftglanz und den gegenständlichen  Lieferanten hat es nicht gegeben.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `M.` (person)
- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Dagobert Duewel (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

| Predicted | Gold |
|---|---|
| `Dagobert Duewel` | `Dagobert Duewel` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Olivia Trienes (= Beschwerdeführerin, Bf) bezieht für den Sohn A, geb. 06/1997, laufend  die Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Olivia Trienes` | `Olivia Trienes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_27`)


Mit Vorlageantrag vom 16.07.2024 wurde die Entscheidung über die Beschwerde durch das  Bundesfinanzgericht beantragt und ergänzend wie folgt begründet:  „[…] Ergänzend zur Beschwerde vom 15.02.2024 wird vorgebracht, dass Herrn Luna Fruechtenicht  Seitens der Pensionsversicherungsanstalt zwischenzeitlich eine Waisenpension zugesprochen  wurde und entsprechend die Erwerbsunfähigkeit infolge Krankheit oder Gebrechens ab der  Kindheit über das 18.

**False Positives:**

- `Luna Fruechtenicht  Seitens` — partial — gold is substring of pred: `Luna Fruechtenicht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Luna Fruechtenicht`(person)
- `Pensionsversicherungsanstalt`(organisation)

</details>

---

## `Names after 'Beschwerde des' (Genitive)` 🏆

**F1:** 0.036 | **Precision:** 0.872 | **Recall:** 0.018  

**Format:** `regex`  
**Rule ID:** `284fd772`  
**Description:**
Captures the name following 'Beschwerde des/der', excluding common non-person nouns, and handling split titles.

**Content:**
```
(?:Beschwerde\s+(?:des|der)\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?!\s+(?:Abgabepflichtigen|Verein|Gesellschaft|AG|mbH|GmbH|KG|UG|Stiftung|Beh\u00f6rde|Amt|Finanzamt|Gericht|Kommission|Ausschuss|Komitee|Firma|Unternehmen|Organisation|Institution|Partei|Bewegung|Bund|Land|Stadt|Gemeinde|Bezirk|Kreis|Region|Kanton|Kommune|Verband|Kammer|Institute|Institut|Forschung|Lehrstuhl|Klinik|Krankenhaus|Hochschule|Universit\u00e4t|Schule|Akademie|Zentrum|Institut|B\u00fcro|Praxis|Wohnung|Haus|Geb\u00e4ude|Grundst\u00fcck|Fl\u00e4che|Land|Gebiet|Territorium|Staat|Reich|Kaiserreich|Republik|Monarchie|Demokratie|Diktatur|Faschismus|Kommunismus|Sozialismus|Kapitalismus|Liberalismus|Konservatismus|Nationalismus|Internationalismus|Globalismus|Regionalismus|F\u00f6deralismus|Zentralismus|Autokratie|Oligarchie|Anarchie|Totalitarismus|Demokratie|Rechtsstaat|Verfassungsstaat|Sozialstaat|Wohlfahrtsstaat|Marktwirtschaft|Planwirtschaft|Mischwirtschaft|Sozialmarktwirtschaft|Freie Marktwirtschaft|Sozialistische Marktwirtschaft|Kapitalistische Marktwirtschaft|Neoliberale Marktwirtschaft|Sozialdemokratische Marktwirtschaft|Konservative Marktwirtschaft|Libert\u00e4re Marktwirtschaft|Anarchistische Marktwirtschaft|Faschistische Marktwirtschaft|Kommunistische Marktwirtschaft|Sozialistische Planwirtschaft|Kapitalistische Planwirtschaft|Neoliberale Planwirtschaft|Sozialdemokratische Planwirtschaft|Konservative Planwirtschaft|Libert\u00e4re Planwirtschaft|Anarchistische Planwirtschaft|Faschistische Planwirtschaft|Kommunistische Planwirtschaft|Sozialistische Mischwirtschaft|Kapitalistische Mischwirtschaft|Neoliberale Mischwirtschaft|Sozialdemokratische Mischwirtschaft|Konservative Mischwirtschaft|Libert\u00e4re Mischwirtschaft|Anarchistische Mischwirtschaft|Faschistische Mischwirtschaft|Kommunistische Mischwirtschaft|Sozialistische Marktwirtschaft|Kapitalistische Marktwirtschaft|Neoliberale Marktwirtschaft|Sozialdemokratische Marktwirtschaft|Konservative Marktwirtschaft|Libert\u00e4re Marktwirtschaft|Anarchistische Marktwirtschaft|Faschistische Marktwirtschaft|Kommunistische Marktwirtschaft|Sozialistische Planwirtschaft|Kapitalistische Planwirtschaft|Neoliberale Planwirtschaft|Sozialdemokratische Planwirtschaft|Konservative Planwirtschaft|Libert\u00e4re Planwirtschaft|Anarchistische Planwirtschaft|Faschistische Planwirtschaft|Kommunistische Planwirtschaft|Sozialistische Mischwirtschaft|Kapitalistische Mischwirtschaft|Neoliberale Mischwirtschaft|Sozialdemokratische Mischwirtschaft|Konservative Mischwirtschaft|Libert\u00e4re Mischwirtschaft|Anarchistische Mischwirtschaft|Faschistische Mischwirtschaft|Kommunistische Mischwirtschaft)(?=\s|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.872 | 0.018 | 0.036 | 39 | 34 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 34 | 5 | 1817 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_2`)


Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Rosalia Schmieter, Collmannstraße 3, 3335 Lindau, Österreich  vom 22. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. September 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,idgF,  iVm § 4 Abs. 1 Parkometergesetz 2006, Landesgesetzblatt Nr. 9/2006 idF LGBl für Wien Nr.  24/2012, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Rosalia Schmieter` | `Rosalia Schmieter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Collmannstraße 3, 3335 Lindau, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Jaden Holzfuss` | `Jaden Holzfuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Puntigam` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Harald Schwalbach` | `Harald Schwalbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_2`)


über die Beschwerde des Louisa Kannengiser, Pfaffensteig 10, 3595 Atzelsdorf, Österreich, vom 15. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. März 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016 in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise Folge gegeben als die von der belangten Behörde mit € 60,00 verhängte Geldstrafe  auf € 48,00 und die für den Fall der Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfrei- heitsstrafe auf 10 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Louisa Kannengiser` | `Louisa Kannengiser` |

**Missed by this rule (FN):**

- `Pfaffensteig 10, 3595 Atzelsdorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)


über die Beschwerde der Balthasar Brendtke, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Balthasar Brendtke` | `Balthasar Brendtke` |

**Missed by this rule (FN):**

- `Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

| Predicted | Gold |
|---|---|
| `Evelyn Antwerber` | `Evelyn Antwerber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Hertzstraße 25, 5134 Spieglern, Österreich` (address)
- `Dr. Farid Rifaad` (person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Hilde Schorpp, Wandschaml 94, 4625 Grub, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 21. Dezember 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung der Rechtsvorschrift des § 2 in Verbindung mit § 4 Abs. 2  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 2 VStG eingestellt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Hilde Schorpp` | `Hilde Schorpp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Wandschaml 94, 4625 Grub, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_3`)


über die Beschwerde des Ludmilla Czimmerninks,  Sennemahd 7, 9832 Latzendorf, Österreich, vom 30. Juni 2021, gegen den Bescheid des Magistrates der Stadt Wien,  Magistratsabteilung 6, vom 7. Juni 2021, GZ. MA67/Zahl/2020, betreffend Abweisung des  Antrages vom 14. Mai 2021 auf Bewilligung eines Zahlungsaufschubes bzw. Ratenansuchens,  nach Durchführung einer mündlichen Verhandlung am 2. September 2021, in Anwesenheit des  Beschwerdeführers und der Schriftführerin IP, zu Recht erkannt:  Die Beschwerde wird gemäß § 50 VwGVG als unbegründet abgewiesen und der ange- fochtene Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Ludmilla Czimmerninks` | `Ludmilla Czimmerninks` |

**Missed by this rule (FN):**

- `Sennemahd 7, 9832 Latzendorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 6` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Theobald Atacan, Göschl 12, 3544 Eisenberg, Österreich, vom 22. November 2021, gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 13. Oktober  2021, Zl. MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 3 Abs. 1  Kontrolleinrichtungenverordnung, Abl. der Stadt Wien Nr. 33/2018, idgF, in Verbindung mit § 4  Abs. 3 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF, zu Recht:  Die Beschwerde wird gemäß § 50 VwGVG in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Theobald Atacan` | `Theobald Atacan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Göschl 12, 3544 Eisenberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Pjotr Astore` | `Pjotr Astore` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Rauner` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

| Predicted | Gold |
|---|---|
| `Juliana Fassmer` | `Juliana Fassmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Tillisweg 11, 8773 Sparsbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerde des  Karim Hainzlmeier, Gälaplana 43, 3205 Mühlhofen, Österreich, gegen den Bescheid des Finanzamtes Bregenz vom 20. Mai 2016  betreffend Einkommensteuer 2015, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Karim Hainzlmeier` | `Karim Hainzlmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Gälaplana 43, 3205 Mühlhofen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde des  Melinda Brotke, Jägerloch 26, 8443 Praratheregg, Österreich, vom 22. März 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 3.  März 2021, Zahl MA67/206700943579/2020, wegen einer Verwaltungsübertretung gemäß § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der  Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für  Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Melinda Brotke` | `Melinda Brotke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Jägerloch 26, 8443 Praratheregg, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt  Wien` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Juri Boyarzyn, Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich, vom 28. Juli 2020, gegen den Bescheid des Finanzamtes Österreich  vom 16. Juli 2020, betreffend Familienbeihilfe 01.2019-01.2021, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juri Boyarzyn` | `Juri Boyarzyn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Volkmar Quadfasel, Forstbergstraße 5, 4144 Zanklbach, Österreich, vertreten durch Dr. Sebastian Mariano Volkmar Lenz,  Laurenzerberg 1, 1010 Wien, vom 25. April 2021, gegen den Bescheid des Finanzamtes  Österreich vom 26. März 2021, betreffend Abweisung des Antrages auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe ab Dezember 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Quadfasel` | `Volkmar Quadfasel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Forstbergstraße 5, 4144 Zanklbach, Österreich` (address)
- `Dr. Sebastian Mariano Volkmar Lenz` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_2`)


Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde des Ariadne Schmalzried, Nejesgasse 7K, 6094 Bachl, Österreich, vom 20. Juli 2020, gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  12. Mai 2020, betreffend Abweisung des Antrages auf Gewährung der Familienbeihilfe in Höhe  der gemäß § 8 Abs. 3 und 4 FLAG 1967 festgesetzten Beträge sowie des Kinderabsetzbetrages  in Höhe des in § 33 Abs. 3 erster Satz EStG 1988 festgesetzten Betrages zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ariadne Schmalzried` | `Ariadne Schmalzried` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nejesgasse 7K, 6094 Bachl, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde der Adriana Wottge,  Ferstelgasse 22, 3282 Forsthub, Österreich, vom 20. Juli 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 14. Juli 2022, Zl. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Adriana Wottge` | `Adriana Wottge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferstelgasse 22, 3282 Forsthub, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138513.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Univ.-Prof.in Verena Sobzig  über die Beschwerde des  Peter Scheidhauer, Klimaweg 103, 8232 Untersafen, Österreich, vom 31.05.2022 gegen den Bescheid des Finanzamtes Österreich vom  26.04.2022 betreffend Abweisung eines Antrages auf Nachsicht zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Scheidhauer` | `Peter Scheidhauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Verena Sobzig` (person)
- `Klimaweg 103, 8232 Untersafen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Chantal Franzk,  Feldererweg 14 - 20, 5166 Rudersberg, Österreich, vom 14. Juni 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 31. Mai 2022, GZ MA 67/Z2/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit §  4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Berufungsverhandlung am 19. September 2022, im  Beisein der Schriftführerin IP, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Chantal Franzk` | `Chantal Franzk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Feldererweg 14 - 20, 5166 Rudersberg, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Magdalena Unterreiter, Anichstraße 5, 8953 Donnersbach, Österreich, Deutschland, vom 22. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, als Verwaltungsstrafbehörde vom  10. März 2022, Zl. Zahl, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magdalena Unterreiter` | `Magdalena Unterreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Anichstraße 5, 8953 Donnersbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Cornelia Reifgerste` | `Cornelia Reifgerste` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Scherzergütl 18K, 9622 Golz, Österreich` (address)
- `Freimüller Rechtsanwalts GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `M. F.` (person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

| Predicted | Gold |
|---|---|
| `Wladimir Leukhardt` | `Wladimir Leukhardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich` (address)
- `Stadt Wien` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde des  Lubomir Vaist, Sulzbachfelderstraße 3, 9361 Judendorf, Österreich, vom 4. Jänner 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 12. Oktober 2022, GZ. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Lubomir Vaist` | `Lubomir Vaist` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Sulzbachfelderstraße 3, 9361 Judendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde des Noah Blanck, Ägidiweg 63, 4111 Hamberg, Österreich, vom 7. Juni 2022, gegen den Bescheid des  Finanzamtes Österreich vom 24. Mai 2022, betreffend Abweisung des Antrages auf  Familienbeihilfe ab Juli 2020, zu Recht:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Noah Blanck` | `Noah Blanck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Ägidiweg 63, 4111 Hamberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johannes Böck über die Beschwerde des  Maximilian Mlynarzyk, Kellersteig 6O, 9063 Techmannsdorf, Österreich, vom 7. Juni 2023, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde vom 9.  Mai 2023, GZ. MA67/GZ/2023, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde Folge gegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 1 VStG eingestellt.  II. Gemäß § 52 Abs. 1 und 2 VwGVG iVm § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Maximilian Mlynarzyk` | `Maximilian Mlynarzyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johannes Böck` (person)
- `Kellersteig 6O, 9063 Techmannsdorf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Silke Czejka, Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich, vom 01. September 2022 gegen den Bescheid des Finanzamtes  Österreich vom 30. August 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Monat Mai 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silke Czejka` | `Silke Czejka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri über die Beschwerde der Silvia Burscheid,  Sackgasse 48, 8664 Kleinveitsch, Österreich, vom 16. Jänner 2023 gegen den Bescheid des Finanzamtes Österreich vom  19. Dezember 2022 betreffend Abweisung des Antrages auf Gewährung der Familienbeihilfe  und Kinderabsetzbetrag von Juni 2021 bis September 2022, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO insofern teilweise Folge gegeben, als nur die für den  Zeitraum Juni 2021 bis August 2022 bezogenen Familienbeihilfen und Kinderabsetzbeträge  zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Silvia Burscheid` | `Silvia Burscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sackgasse 48, 8664 Kleinveitsch, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/142429.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142429.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser über die Beschwerde  des Bernhard Voronov, Prof.-Leopold-Farnleitner-Weg 18, 4673 Grub, Österreich, vom 3. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 22. April 2022, betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe vom 31. Jänner 2022 für S., V.nr. Nr., ab Jänner 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bernhard Voronov` | `Bernhard Voronov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Prof.-Leopold-Farnleitner-Weg 18, 4673 Grub, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Irene Kohler über die Beschwerde des  Desiree Hannecken, Lasseestraße 13, 5144 Handenberg, Österreich, vom 5. Oktober 2023 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 28. September 2023, GZ. MA67/Zahl/2023,  wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung  in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Desiree Hannecken` | `Desiree Hannecken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Irene Kohler` (person)
- `Lasseestraße 13, 5144 Handenberg, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/143315.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143315.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Emanuel Bulthuis, Martinsplatz 47, 6167 Neustift im Stubaital, Österreich, vom 7. Dezember 2022 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für die Monate August und September 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emanuel Bulthuis` | `Emanuel Bulthuis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Martinsplatz 47, 6167 Neustift im Stubaital, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner über die Beschwerde  des Herbert Leitzmann, Schörgendorfstraße 80D, 9560 Förolach, Österreich, vom 30. Juni 2023, gegen die drei Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 21. Juni 2023,   GZen 1) MA67/Zahl1/2023, 2) MA67/Zahl2/2023 und   3) MA67/Zahl3/2023, alle drei wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  werden die drei Straferkenntnisse des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Herbert Leitzmann` | `Herbert Leitzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Ebner` (person)
- `Schörgendorfstraße 80D, 9560 Förolach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143486.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde des Danielle Conraths, Rollfährestraße 2I, 4132 Atzesberg, Österreich, vom 8. Mai 2022 gegen den Bescheid des  FA Gmunden Vöcklabruck  vom 12. April 2022 betreffend Zahlungserleichterungen § 212 BAO 2022 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Danielle Conraths` | `Danielle Conraths` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniela Regina Denk` (person)
- `Rollfährestraße 2I, 4132 Atzesberg, Österreich` (address)
- `FA Gmunden Vöcklabruck` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Moritz Weaving, Zwieselsteintajen 14, 9911 Schrottendorf, Österreich, vom 20. Mai 2024, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 17. April 2024, GZ.  MA67/GZ/2024, wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis des Magistrates der Stadt  Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Moritz Weaving` | `Moritz Weaving` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Zwieselsteintajen 14, 9911 Schrottendorf, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt  Wien` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Frederik Grossmayer  über die Beschwerde des Jonathan Gagarin,  Paul Has-Gasse 2, 5251 Aigertsham, Österreich, vom 4. Juli 2025, gegen die zwei Zurückweisungsbescheide des Magistrates der  Stadt Wien, Magistratsabteilung 67, beide vom 3. Juli 2025, GZen 1) MA67/GZ1/2025 und 2)  MA67/GZ2/2025, zu Recht erkannt:  Gem. § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und werden die zwei  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Jonathan Gagarin` | `Jonathan Gagarin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Frederik Grossmayer` (person)
- `Paul Has-Gasse 2, 5251 Aigertsham, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

**False Positives:**

- `Xaver Plaumert` — partial — pred is substring of gold: `Xaver Plaumert, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Dr. Wolfgang Aigner`(person)
- `Erwin Agneter`(person)
- `Mag. Belinda  Maria Eder`(person)
- `Xaver Plaumert, BEd`(person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich`(address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Mag. Katharina Moravec`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_283`)


Die umfangreichen Ermittlungen der Abgabenbehörde haben ergeben, dass es sich bei den  drei genannten Firmen um Scheinfirmen handelt.   Anzumerken ist in diesem Zusammenhang, dass die in der Beschwerde erwähnte  abgabenrechtliche Beschwerde der Starnberg Beratung GmbH gegen den Haftungsbescheid mit ho.

**False Positives:**

- `Starnberg Beratung Gmb` — partial — pred is substring of gold: `Starnberg Beratung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Starnberg Beratung GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter über die Beschwerde des Ivan Thöner, Landlerweg 28, 4273 Kaltenberg, Österreich, vom 7. April 2021 gegen das Straferkenntnis des Magistrates der Stadt Wien vom 25.  Februar 2021, Zahl MA67/Zahl/2020,  betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016 in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, den Beschluss gefasst:  Die Beschwerde vom 7. April 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

**False Positives:**

- `Ivan Th` — partial — pred is substring of gold: `Ivan Thöner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ivan Thöner`(person)
- `Landlerweg 28, 4273 Kaltenberg, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_35`)


Die Beschwerde der Heimwerk GmbH war daher als unzulässig zurückzuweisen.

**False Positives:**

- `Heimwerk Gmb` — partial — pred is substring of gold: `Heimwerk GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimwerk GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Xenia Oelschlagel, BSc, Franz-Adelpoller-Hof 124, 4932 Ried, Österreich, vom 2. Juli 2019 gegen den Bescheid des  FA Wien 2/20/21/22  vom 4. Juni 2019 betreffend Haftungsbescheid / Sonstige 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Xenia Oelschlagel` — partial — pred is substring of gold: `Xenia Oelschlagel, BSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniela Regina Denk`(person)
- `Xenia Oelschlagel, BSc`(person)
- `Franz-Adelpoller-Hof 124, 4932 Ried, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)

</details>

---

## `Single Word Names after 'Herrn' or 'Frau'` 🏆

**F1:** 0.064 | **Precision:** 0.795 | **Recall:** 0.033  

**Format:** `regex`  
**Rule ID:** `19a6a077`  
**Description:**
Captures single-word names following 'Herrn' or 'Frau' in contexts where the name is a surname only (e.g., 'Herrn Hus').

**Content:**
```
(?:Herrn|Frau)\s+([A-Z][a-z\u00df]+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.795 | 0.033 | 0.064 | 78 | 62 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 62 | 16 | 1789 |

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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_12`)


Frau Hainig  ist ab 3. März 2014 als Anzeigenberaterin für die DG  tätig.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_13`)


Frau Hainig  hat als Dienstort Stadt und Stadt1 und wird zu nachstehenden Bedingungen  ganztags angestellt: Kollektivvertrag: kfm, (nichtjournalistische) Angestellte;

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_19`)


Frau Hainig  verrechnet die ersten drei Monate Spesen und Kilometergeld  nach Bedarf, wobei diese mittels Spesenabrechnung und Kilometerbuch abzurechnen und zu  belegen sind.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_21`)


Mit Frau Hainig  wird vorerst ein  befristetes Dienstverhältnis bis 2. Juni 2014 vereinbart, wobei der erste Monat als Probemonat  gilt. Als Dienstort wird vornehmlich Stadt vereinbart, wobei es dem Dienstgeber vorbehalten ist,  die Dienstnehmerin auch an anderen Betriebsstätten des Unternehmens niederösterreichweit  vorübergehend oder dauernd einzusetzen.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_50`)


Die  am 28.11.2016 vorgelegte Bestätigung der DG (im Folgenden kurz: *** Verlagsges.m.b.H.) hat  folgenden Inhalt: „Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung § 17 Abs. 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom Ol. 01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_98`)


Z1 wurde laut der vorgelegten Protokollsabschrift am 11.6.2018 an der Polizeiinspektion  d_Ort_1 vernommen und gab unter anderem an: „Seit Mitte dem Jahr 2016 bin ich als  Steuerberater für …Herrn Volchert tätig.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_71`)


Im Rahmen der Firmengründung wurde von Herrn Frikel ein  Fahrzeug als sein Beitrag bzw. als Einlage eingebracht.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_73`)


Dieses Kfz wurde von Herrn Frikel selber angeschafft, wo und zu welchen  Bedingungen kann ich nicht angeben.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_75`)


Ich selber war dann in der Folge mehrmals in Österreich bei Herrn Frikel  wenn ich  mit dem Flugzeug anreiste, konnte ich dann den Audi verwenden (so ca. 15 mal pro Jahr) und  damit Kundenbesuche etc. erledigen.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_80`)


Die Bilanz für 2010 ist noch nicht  erstellt. In Deutschland an meinem Wohnsitz bzw. am Firmensitz konnte ich somit nicht  permanent über das KFZ Audi A6 verfügen, es befand sich des öfteren im Besitz des Herrn Frikel in  A/Adr1 und somit an diesem Standort.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_37`)


1) Mit Schreiben vom 13.05.2020 wurde von Herrn Angelstein mitgeteilt, dass er weder  Geschäftsführer der Firma sei noch mit dem Fahrzeug gefahren sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_38`)


Mit Schreiben vom 02.06.2020 wurde durch die Rechtsanwälte des Herrn Angelstein mitgeteilt, dass  dieser keine Lenkerauskunft erteilen könne, da er lediglich für das Fahrzeug mit dem amtlichen  Kennzeichen Auto3 (Anmerkung BFG: nicht gegenständlich) verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_50`)


Mit Schreiben vom 04.06.2020 teilte die rechtsfreundliche Vertretung des Herrn Angelstein  mit, dass der Genannte über das gegenständliche Fahrzeug zum Beanstandungszeitpunkt nicht  verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_51`)


Mit Schreiben vom 18.06.2020 wurde die Zulassungsbesitzerin des gegenständlichen  Fahrzeuges aufgefordert die erteilte Lenkerauskunft durch Vorlage entsprechender  Beweismittel (Unterlagen über die Bestellung des Herrn Angelstein als verantwortlicher Beauftragter  gemäß § 9 Abs. 2 Verwaltungsstrafgesetz 1991) glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_57`)


In der E-Mail Ihres rechtsfreundlichen Vertreters vom 01.10.2020 wurde zum gegenständlich  angelasteten Sachverhalt vorgebracht, die Zulassungsbesitzerin und deren handelsrechtliches  Organ habe der Aufforderung der Behörde zur Lenkerauskunft gesetzestreu entsprochen, zumal  dargelegt worden sei, dass die verlangte Auskunft von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030  Wien, als Verantwortlicher gemäß § 9 VStG erteilt werden könne.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_60`)


Weiters  wurde die Herbeischaffung des Aktes der WKStA zur AZ: AktWKStA, dessen Inhalt die  Übertragung der Meldepflicht gemäß § 9 VStG auf Herrn Angelstein beweisen soll, beantragt.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)
- `Dr.in Ing. Viktoria Weigart` (person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_154`)


In Beantwortung der nunmehr an Herrn Angelstein gerichteten (sechs) Lenkererhebungen der  belangten Behörde bestritt dieser seine Auskunftspflicht mit den Worten   1) bis 5) „dass ich weder ein Geschäftsführer dieser Firma noch mit diesem Fahrzeug gefahren  bin.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)


6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn Angelstein angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_174`)


3. Zulässigkeit des Einspruches:  …  4. Gründe des Einspruches:  Der Vorwurf, der Einschreiter hätte als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin der Firma1 des Fahrzeuges mit dem behördlichen Kennzeichen Auto4  [Anmerkung BFG: nicht gegenständlich] dem ordnungsgemäß zugestellten Verlangen der MA  67 vom 28.01.2020, innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er  dieses Fahrzeug überlassen gehabt hat, sodass dieser zur in der Strafverfügung angegebenen  Tatzeit und Tatort gelenkt hat bzw. vor diesem Zeitpunkt abgestellt hat nicht entsprochen zu  haben und somit die Rechtsvorschriften des § 103 Abs 2 KFG [Anmerkung BFG, gemeint: § 2  (Wiener) Parkometerabgabeverordnung iVm § 4 Abs. 2 Parkometergesetz 2006] trifft nicht zu,  dies aus folgenden Gründen: Es wurde - wie oben erwähnt - vom Einschreiter die Übertragung  der Meldepflicht auf Herrn Angelstein  geb. Herrgeb, übertragen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_191`)


Darin hat die Einschreiterin  und deren handelsrechtliches Organ dargelegt, dass die verlangte Auskunft nicht erteilt werden  kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030 Wien als Verantwortlichen gemäß  § 9 VStG.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_213`)


Darin hat die Einschreiterin und deren handelsrechtliches Organ dargelegt, dass die verlangte  Auskunft nicht erteilt werden kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, als  Verantwortlichen gemäß § 9 VStG.  16 von 22 Seite 17 von 22

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_24`)


Frau Baues ist die Liquidatorin.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_405`)


Frau Baues als Vertreterin der Beschwerdeführerin gibt bekannt, dass die Diesellieferungen 2 bis 3  Mal pro Woche stattgefunden haben.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |
| `Baues` | `Baues` |
| `Borisowa` | `Borisowa` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_6`)


Entscheidungsgründe  I. Verfahrensgang  1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Beschwerdeführerin (kurz Bf) ist eine GmbH, deren alleinige Gesellschafterin Frau Schneppensiefen ist.

| Predicted | Gold |
|---|---|
| `Schneppensiefen` | `Schneppensiefen` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_11`)


Unter Bezugnahme auf obige Ausführungen ist festzuhalten, dass Frau Waiser die  exklusive (einzige) Adressatin der Vollstreckungsverfügung vom 18. Mai 2022 ist, die hier aber  von jemandem anderen bekämpft wird.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_15`)


Im vorliegenden Fall hat jedoch nicht die Adressatin der verfahrensgegenständlichen  Vollstreckungsverfügung, nämlich Frau Waiser  sondern FirmaBfInhaberLautFirmenbuch,  Firmenbuchnummer FN im eigenen Namen Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung – direkt oder indirekt – von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt - von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_37`)


Im  Allgemeinen gibt Frau Reifgerste an, dass sich ihre Tochter überwiegend „falsch“ fühle und in sozialen  Situationen sich sehr verunsichert fühle, da sie nicht wisse wie sie sich verhalten solle.

| Predicted | Gold |
|---|---|
| `Reifgerste` | `Reifgerste` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)


Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn Isenmann  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)


Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn Isenmann  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_54`)


Dass der (Original)Ausweis gemäß § 29b StVO 1960 mit der Nr. Nr1 (Nr2) an Herrn Isenmann  geb.  Herrgeb, ausgestellt wurde und dass Herr Ballschmieder laut ZMR mit Datum verstorben ist, ergibt sich  aus dem Schreiben der Bezirkshauptmannschaft Ort vom 16. März 2023.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_13`)


Der Bf. brachte in seinem Einspruch vom 19. Juni 2023 (E-Mail) vor, dass er das Fahrzeug vor  dem Geburtshaus geparkt habe, da seine Frau Wehen gehabt habe.

| Predicted | Gold |
|---|---|
| `Wehen` | `Wehen` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_7`)


In Beantwortung des Ergänzungsersuchens des Finanzamtes (siehe dazu Vorhalt vom  16.02.2024) teilte die Tochter der Bf,Frau Rittcher  dem Finanzamt daraufhin mit, dass sie einerseits  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Rittcher` | `Rittcher` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Finanzamt` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_11`)


Dagegen erhob die Bf, vertreten durch Frau Rittcher  fristgerecht Beschwerde mit der Begründung,  dass W.B. die FB erhalten hätte und nicht die Bf (siehe dazu Beschwerdeschriftsatz vom  25.03.2024).

| Predicted | Gold |
|---|---|
| `Rittcher` | `Rittcher` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_62`)


Durch den steuerlichen Vertreter wurde am 14.04.2015 im Rahmen einer Gebührenprüfung der  Beschluss des Stiftungsrates der XX Stiftung vom 10.10.2007 über die Vornahme einer  Ausschüttung in Höhe von € 240.000,- an Frau Klopstech beigebracht.

| Predicted | Gold |
|---|---|
| `Klopstech` | `Klopstech` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_105`)


Punkt 4   Weder Frau Heumann noch Herr Bf2 hätten jemals in diesem Gebäude gewohnt.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_109`)


Frau Heumann und Herr Bf2 würden seit Dezember 2020 (lt. Meldezettel 18.01.2021) in einer ca.  95m²-großen Wohnung in I 1, J wohnen, welche sich im Eigentum von Frau Heumann befinde.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |
| `Heumann` | `Heumann` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_111`)


3 Parteien davon seien Mieter von Frau Heumann und die 4.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_112`)


Partei sei die mit einem  Wohnrecht ausgestattete Lebensgefährtin des verstorbenen Großvaters von Frau Heumann  welcher  ihr die Liegenschaft übergeben hätte.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_114`)


Davor hätte Frau Heumann und Herr Bf2 in den jeweiligen Elternhäusern gewohnt,Frau Heumann in K 1, L  und Herr Bf2 in Dorf.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |
| `Heumann` | `Heumann` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_130`)


Frau Heumann und Herr Bf2 haben das Objekt erworben um damit ebenfalls Mieteinnahmen zu  erzielen – das Objekt also zu Vermietungszwecken zu nutzen.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_144`)


Die Wohnverhältnisse von Frau Heumann und Herrn Bf2 waren sowohl vor dem Kauf als auch nach  dem Kauf so gestaltet, dass das erworbene Objekt nicht für eigene Wohnzwecke angedacht  war.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_155`)


Zahlreiche Anhaltspunkte weisen klar darauf hin, dass Frau Heumann und Herr Bf2 das Objekt  erworben haben, um es auch tatsächlich zu Vermietungszwecken zu nutzen.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_158`)


Sie  wohnen seit Dezember 2020 in einer ca. 95m² großen Wohnung im Eigentum von Frau Heumann (siehe Übergabsvertrag).

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_4`)


Entscheidungsgründe  Mit Strafverfügung vom 1) 14.04.2025, GZ. MA67/GZ1/2025 und 2) 12.05.2025, GZ.  MA67/GZ2/2025, wurde Frau Langness für schuldig erkannt, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (Land) am

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_15`)


Frau Langness bitte die beiden Strafen umzuleiten, bzw. ihr zu entziehen.

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_29`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde die (zwei) Strafverfahren gegen Frau Langness aufgrund der ihr zur Verfügung stehenden Unterlagen als Beschuldigte eingeleitet und ihr  gegenüber mit Strafverfügung vom 1) 14.04.2025, GZ. MA67/GZ1/2025 und 2) 12.05.2025, GZ.  MA67/GZ2/2025, unter Anlastung einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006  jeweils eine Geldstrafe in Höhe von 75,00 Euro verhängt und für den Fall der Uneinbringlichkeit  jeweils eine Ersatzfreiheitsstrafe von 17 Stunden auferlegt.

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_30`)


Mit E- Mail vom 1) 07.05.2025 und 2) 02.06.2025 erhob Bf1 im eigenen Namen Einspruch  gegen obigen zwei Strafverfügungen, wobei im Wesentlichen darauf verwiesen wurde, dass Frau Langness das KFZ zu den Beanstandungszeitpunkten nicht ‚benutzt‘ habe.

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_65`)


Gleiches trifft auf die Ehegattin des Bf. zu.  Erkrankung der Ehegattin und des Bf.:  Im Vorlageantrag wurde erstmalig vorgebracht, ein Umzug nach Österreich sei nicht möglich,  weil seine Frau Krebs hat;

**False Positives:**

- `Krebs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_10`)


Ein weiterer ärztlicher Befundbericht von Fr. Dr. **** und Herrn Dr. **** lagen ebenfalls dem  Antrag bei.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

**False Positives:**

- `Alexander` — partial — pred is substring of gold: `Alexander X.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexander X.`(person)
- `M.`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_14`)


Vergl. hierzu “Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)


Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_17`)


Es würden mit Herrn Ing. K. (Geschäftsführer der Fa. X.  2 von 9 Seite 3 von 9

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_19`)


Die Entlehnung des Kfz gehe auf ein privates Ersuchen des Herrn Ing. K. zurück.

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation
- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)


Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die Jeremias Kierstan, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Jeremias Kierstan`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_28`)


Der angefochtene Bescheid vom 17.07.2015, mit welchem über den Antrag der Heimwerk GmbH auf  Herabsetzung der Abwassergebühr für 2013 abgesprochen wurde, ist an die Jeremias Kierstan  als  Partei ergangen und an deren Zustellbevollmächtigten, Herrn Vertreter zugestellt worden.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Jeremias Kierstan`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_67`)


Über die diesbezügliche Rücksprache mit der belangten Behörde sei vom steuerlichen  Vertreter am 7. August 2001 ein Aktenvermerk angelegt worden, welchen folgenden Inhalt  habe:  ….“Haben dies mit Herrn Mag. ***, FA Feldkirch am 7. August 2001 nochmals besprochen und  um einen Lösungsvorschlag gebeten: Nach Mag. *** soll die liechtensteinische FA Spittal Villach  eine  Proformarechnung an die RHO Pharma  ausstellen, somit wird die RHO Pharma  zum "Proforma  Verfügungsberechtigten" und kann die abgeführte Einfuhrumsatzsteuer problemlos als  Vorsteuer geltend machen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Feldkirch`(organisation)
- `FA Spittal Villach`(organisation)
- `RHO Pharma`(organisation)
- `RHO Pharma`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_21`)


Im vorliegenden Fall konnte nur Frau Einspruch erheben oder dessen Rechtsvertreterin, nicht  aber eine andere Person.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_109`)


Zudem wurde vom Geschäftsführer, Herrn Gf., bei der Schlussbesprechung gem § 149 Abs  1 BAO am 12.12.2017 mitgeteilt, dass in Peru keine steuerliche Erfassung der Betriebsstätte  erfolgte, dies wurde auch im Schreiben vom 22.12.2017 bestätigt.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names with Split Titles (e.g. Univ- Prof.)` 🏆

**F1:** 0.298 | **Precision:** 0.763 | **Recall:** 0.185  

**Format:** `regex`  
**Rule ID:** `de0eb9fb`  
**Description:**
Captures full title and name following legal titles including complex multi-word titles like 'Techn R', 'Univ.-Prof.in', 'Priv.-Doz.in', ensuring the full name is captured even with spaces in titles.

**Content:**
```
(?:Techn\s+R\s+|Techn\.\s*R\s+|Techn\.R\s+|Univ\.-?Prof\.(?:\.in)?\s+|Priv\.-?Doz\.(?:\.in)?\s+|Hon\.-?Prof\.(?:\.in)?\s+|Hon\.-?Prof\.|Dr\.(?:\s+Priv\.-Doz\.)?\s+|Dr\.in\s+|Mag\.(?:\s+Univ\.-Prof\.)?\s+|Mag\.a\s+|Ing\.|Bakk\.(?:\s+iur\.)?\s+|LLM\s+|BSc\s+|RA\.?\s+|StB\.?\s+|Gf-?\s+|\u00d6kR\s+|Dipl\.-Ing\.|RgR\s+|OStR\s+|HR\s+|Fr\.PhD\s+|VetR\s+|DDr\.|LL\.B\.(?:\s+LL\.M\.)?\s+|B\.iur\.(?:\s+r\.\s+nat\.)?\s+|i\.iur\.(?:\s+r\.\s+nat\.)?\s+|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?\s+|LL\.M\.(?:\s+LL\.B\.)?\s+|M\.B\.L\.|LL\.B\.|MBA\s+|MSc\s+|DI\s+|Dipl\.(?:\s+Kff\.)?\s+|StR\s+|KommR\s+|KzlR\s+)([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.763 | 0.185 | 0.298 | 448 | 342 | 106 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 342 | 106 | 1509 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Hajicek` | `Dr. Alexander Hajicek` |
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Michael Franz` | `Mag. Michael Franz` |
| `Mag. Franz Josef Großin` | `Mag. Franz Josef Großin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |
| `Mag. Peter Staudinger` | `Mag. Peter Staudinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)

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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Dr.in Laurin Morgenschweis` | `Dr.in Laurin Morgenschweis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich` (address)
- `Fatima Beringschmidt` (person)
- `Finanzamtes Waldviertel` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theodora Urbanova, Bakk. iur.` (person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `54-205/5010` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Moser` | `Mag. Wolfgang Moser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rosamunde Galanidis` (person)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Elias Voht` | `VetR Elias Voht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thomas Hutching` | `Hon.-Prof. Thomas Hutching` |
| `Hon.-Prof. Ruprecht Hauswerth` | `Hon.-Prof. Ruprecht Hauswerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sean Herdling` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |
| `Mag. Belinda  Maria Eder` | `Mag. Belinda  Maria Eder` |
| `Mag. Katharina Moravec` | `Mag. Katharina Moravec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Agneter` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Rauscher` | `Dr. Michael Rauscher` |
| `Dr. Christian Haid` | `Dr. Christian Haid` |
| `Mag. Bruno  Sundl` | `Mag. Bruno  Sundl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Franz Glashüttner` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Ottfried Theißl` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ottfried Ficici` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joachim Annanias` | `Dr. Joachim Annanias` |
| `VetR Burkhard Krautschenko` | `VetR Burkhard Krautschenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `Mag. Susanne Pöltenstein-Rosenegger` (person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Puntigam` | `Mag. Manuela Puntigam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Holzfuss` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |
| `KzlR Diethard Ringhand` | `KzlR Diethard Ringhand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_55`)


Handschriftlich war darauf vermerkt „Bestätigung durch Frau E, Exfrau des Bf. und  Mutter der beiden unterhaltspflichtigen Kinder K1 und K2: Hiermit erkläre ich, dass mein  Exmann KzlR Diethard Ringhand  zu allen o.g.

| Predicted | Gold |
|---|---|
| `KzlR Diethard Ringhand` | `KzlR Diethard Ringhand` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Kirstin Matiascheck` | `Dr.in Kirstin Matiascheck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Schwinge` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Olivia Ziegeler` | `Mag.a Olivia Ziegeler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mike Reislehner` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Susette Glaeßel` | `Mag.a Susette Glaeßel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl Morgenbesser` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Univ.-Prof. Alvin Paulikat` (person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Dr Christian Burghardt` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Elvira Thielsen` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Edith Schifferdecker` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Meyerhofer` | `Mag. Manuela Meyerhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sandra Fenn` (person)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

| Predicted | Gold |
|---|---|
| `Dr. Farid Rifaad` | `Dr. Farid Rifaad` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Evelyn Antwerber` (person)
- `Hertzstraße 25, 5134 Spieglern, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |
| `StR Milena Neidig` | `StR Milena Neidig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jonas Gutkauf` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger` (person)
- `Paullehnerweg 72, 9584 Höfling, Österreich` (address)
- `UNICONSULT Steuerberatungs GmbH & Co KG` (organisation)
- `FA Braunau Ried Schärding` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Robert Dax` | `Mag. Robert Dax` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Maximowa` (person)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Lieselotte Schluessel, Hannakstraße 205, 5121 Wimm, Österreich, über die Beschwerde vom 22. Februar 2016  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 10. Februar 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gregor Ableidinger` (person)
- `Lieselotte Schluessel` (person)
- `Hannakstraße 205, 5121 Wimm, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Vanessa Nowikoff  in der Beschwerdesache des  KommR Lee Ponsard, Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich, über die Beschwerde vom 30. Juli 2020 gegen den Bescheid des  Finanzamtes X. (FA, jetzt Dienststelle des Finanzamt Freistadt Rohrbach Urfahr ) vom 10. Juli 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zur Steuernummer 63-102/2061  zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 (1) BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `KommR Lee Ponsard` | `KommR Lee Ponsard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Vanessa Nowikoff` (person)
- `Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `63-102/2061` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Armin Heckemanns, Nabuccogasse 10, 2630 Ternitz, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, (im  Beschwerdeverfahren nicht eingeschritten), über die Beschwerde vom 10. Februar 2020 gegen  den Einkommensteuerbescheid 2018 des Finanzamtes Baden Mödling vom 10. Jänner 2020  (und gemäß § 253 Satz 1 BAO auch gegen den Einkommensteuerbescheid 2018 vom  18. September 2020) zu Steuernummer 75-597/1615  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Silvia Gredenberg` | `Dr. Silvia Gredenberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Armin Heckemanns` (person)
- `Nabuccogasse 10, 2630 Ternitz, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `75-597/1615` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Ibrahim de Vrese, LLB, Kitzlermühle 3, 2754 Wopfing, Österreich, über die Beschwerde vom 07.06.2021 wegen behaupteter  Verletzung der Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Familienbeihilfe ab 09/2019 Sozialversicherungsnummer 2872011080  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Ulrike Stephan` | `Mag. Ulrike Stephan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibrahim de Vrese, LLB` (person)
- `Kitzlermühle 3, 2754 Wopfing, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `2872011080` (social_security_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_9`)


Im Schriftsatz vom 04.11.2020 führte der Bf dazu Folgendes aus:  Die Ehegattin habe sich 2018 auf Grund ihrer Sehschwäche einer Augenoperation bei KzlR Karola Priester  unterzogen.

| Predicted | Gold |
|---|---|
| `KzlR Karola Priester` | `KzlR Karola Priester` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_49`)


Laut dieser Rechnung wurden bei der Ehegattin des Bf  refraktive Eingriffe an beiden Augen durch Augenarzt KzlR Karola Priester durchgeführt.

| Predicted | Gold |
|---|---|
| `KzlR Karola Priester` | `KzlR Karola Priester` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_51`)


Im Arztbrief vom 07.07.2018 erstellte KzlR Karola Priester anlässlich einer bei der Ehegattin des Bf  durchgeführten Untersuchung die Diagnose: BA: Myoper Astigmatismus und hielt in der  Anamnese fest, dass die Ehegattin des Bf keine Brille mehr tragen will und Information über  Operationsmöglichkeiten erhalten möchte.

| Predicted | Gold |
|---|---|
| `KzlR Karola Priester` | `KzlR Karola Priester` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_52`)


Einem Untersuchungsbefund des KzlR Karola Priester vom 09.07.2018 ist neben der Diagnose: BA: Myoper  Astigmatismus zu entnehmen, dass ein ausführliches Beratungsgespräch, sowohl über die  Möglichkeit der konservativen Korrektur (Brille und/oder Kontaktlinsen), als auch über die  5 von 8 Seite 6 von 8

| Predicted | Gold |
|---|---|
| `KzlR Karola Priester` | `KzlR Karola Priester` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_76`)


Aus dem Untersuchungsbefund des KzlR Karola Priester vom 09.07.2018 ist vielmehr ableitbar,  dass bei der Ehegattin des Bf auch die Möglichkeit der konservativen Korrektur der  Fehlsichtigkeit durch eine von der gesetzlichen Sozialversicherung im Rahmen des § 137 ASVG  bezahlte Brille und/oder durch von der gesetzlichen Krankenkasse im Rahmen des § 137 ASVG  bezahlte Kontaktlinsen bestanden hätte.

| Predicted | Gold |
|---|---|
| `KzlR Karola Priester` | `KzlR Karola Priester` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_78`)


Laut dem Arztbrief des Augenarztes KzlR Karola Priester vom 07.07.2018 wollte die Ehegattin des  Bf keine Brille mehr tragen.

| Predicted | Gold |
|---|---|
| `KzlR Karola Priester` | `KzlR Karola Priester` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Isakova, Hörgattern 37, 3244 Kühberg, Österreich, über die Beschwerde vom 1. Juni 2017 gegen  den Bescheid des Finanzamtes Österreich vom 15. Mai 2017 betreffend Familienbeihilfe  01.2016-12.2016 Steuernummer 93-163/8536  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, dass dieser betreffend T1 hinsichtlich der Monate April, August und  September 2016 ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimitri Isakova` (person)
- `Hörgattern 37, 3244 Kühberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `93-163/8536` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Edith Lohhausen` | `Dr.in Edith Lohhausen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Michael Haberl` (person)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache KommR Nicola Sturzbecher, Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich, vertreten durch Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H., Hans-Gasser-Platz 6c, 9500 Villach, über die  Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes Österreich vom  3. Juli 2013 und 25.April 2017 bezüglich Wiederaufnahme des Verfahrens Umsatzsteuer 2009  bis 2011 und Umsatzsteuer 2009 bis 2012 (Steuernummer 19-116/5774 ) beschlossen bzw.  nach Durchführung einer mündlichen Verhandlung am 04.Oktober 2021 zu Recht erkannt:   I. BESCHLUSS  1.

| Predicted | Gold |
|---|---|
| `KommR Nicola Sturzbecher` | `KommR Nicola Sturzbecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich` (address)
- `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `19-116/5774` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Theobald Atacan, Göschl 12, 3544 Eisenberg, Österreich, vom 22. November 2021, gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 13. Oktober  2021, Zl. MA67/Zahl/2021, wegen der Verwaltungsübertretung gemäß § 3 Abs. 1  Kontrolleinrichtungenverordnung, Abl. der Stadt Wien Nr. 33/2018, idgF, in Verbindung mit § 4  Abs. 3 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idgF, zu Recht:  Die Beschwerde wird gemäß § 50 VwGVG in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theobald Atacan` (person)
- `Göschl 12, 3544 Eisenberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Elisabeth Schafstall`(person)
- `Leithagürtel 20, 4251 Steinwald, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

**False Positives:**

- `Mag. Judith Daniela` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr.in Laurin Morgenschweis`(person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich`(address)
- `Fatima Beringschmidt`(person)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`
- `Hon.-Prof. Thassilo Schoenrock` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Schoenrock, LLM`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `StR Samuel Fraesdorff` — partial — pred is substring of gold: `Ing. StR Samuel Fraesdorff`
- `Dr. Thomas Keppert Steuerberatung` — positional overlap with gold: `Prof. Dr. Thomas Keppert`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

**False Positives:**

- `StR Samuel Fraesdorff` — partial — pred is substring of gold: `Ing. StR Samuel Fraesdorff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leroy Kusznierz`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Maximilian Jasper`(person)
- `Gustav Nowak`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Bianca Gerasimczuk` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Bianca Gerasimczuk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Alvin Paulikat` — partial — pred is substring of gold: `StR Univ.-Prof. Alvin Paulikat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `StR Univ.-Prof. Alvin Paulikat`(person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich`(address)
- `Dr Christian Burghardt`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_236`)


StB Steblein Wind GmbH2.6.2021, S. 3 „mehrere Hüte“), erfolgten im Einvernehmen zwischen den Strategen  und dienten dem Ziel , die Abläufe im Konzern möglichst effizient zu gestalten;

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_301`)


StB Steblein Wind GmbH  2.6.2021, S. 5, S. 12;

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_305`)


StB Steblein Wind GmbH  2.6.2021, S. 12 ; StB Steblein Wind GmbH 12.5.2021, S. 5).  cc.)

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH`
- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH`(organisation)
- `Steblein Wind GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_310`)


Schreiben der Steuerberaterin vom 4.12.2017, ad 7 ; StB Steblein Wind GmbH2.6.2021, S. 5, S. 12;

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_315`)


Schreiben der Steuerberaterin vom 4.12.2017,  ad 7 ; StB Steblein Wind GmbH2.6.2021, S. 5, S. 12;

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_320`)


StB Steblein Wind GmbH2.6.2021 S. 13).  ff.)

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH2.6.2021`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH2.6.2021`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_382`)


Auch im Zusammenhang mit der Tragung der Kosten aus dem Managementvertrag trat die OG  nach außen hin in Erscheinung, weil die Leasingverträge betreffend die Kraftfahrzeuge, mit  welchen die OG – Gesellschafter bei der Lenkung der Konzerngesellschaften, darunter der Bf,  unterwegs waren, durch die OG als Leasingnehmer unterfertigt worden sind (StB Steblein Wind GmbH 12.5.2021, S. 3 und 5).

**False Positives:**

- `StB Steblein Wind` — positional overlap with gold: `Steblein Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steblein Wind GmbH`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Dora Szczepanowski`(person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich`(address)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Martin Yüksekkaya, Bonnleiten 21S, 4724 Aigen, Österreich  vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31. März 2014 gegen den Bescheid des Finanzamtes für Großbetriebe vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2012  (Steuernummer 68-939/1151 ) nach Durchführung einer mündlichen Verhandlung am  06.07.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Martin Yüksekkaya`(person)
- `Bonnleiten 21S, 4724 Aigen, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `68-939/1151`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Wendelin Kasprowitz, Oberwinden 31, 8820 Kulm am Zirbitz, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für Großbetriebe je  vom 13. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  2013-2015 (Steuernummer 01-056/7050 ) nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Wendelin Kasprowitz`(person)
- `Oberwinden 31, 8820 Kulm am Zirbitz, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `01-056/7050`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Brian Nieclaassen, Eiblweg 116, 4893 Brandstatt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 29.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe vom  8. August 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2013-

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Brian Nieclaassen`(person)
- `Eiblweg 116, 4893 Brandstatt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache KommR Nicola Sturzbecher, Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich, vertreten durch Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H., Hans-Gasser-Platz 6c, 9500 Villach, über die  Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes Österreich vom  3. Juli 2013 und 25.April 2017 bezüglich Wiederaufnahme des Verfahrens Umsatzsteuer 2009  bis 2011 und Umsatzsteuer 2009 bis 2012 (Steuernummer 19-116/5774 ) beschlossen bzw.  nach Durchführung einer mündlichen Verhandlung am 04.Oktober 2021 zu Recht erkannt:   I. BESCHLUSS  1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `KommR Nicola Sturzbecher`(person)
- `Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich`(address)
- `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `19-116/5774`(tax_number)

</details>

---

## `Names after 'von' (Family/Relation Context)` 

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `bb3830e3`  
**Description:**
Captures names following 'von' in contexts like 'Kindesmutter von', 'Vater von', etc., ensuring the name is a person.

**Content:**
```
(?:Kindesmutter|Vater|Mutter|Sohn|Tochter|Ehefrau|Ehemann|Elternteil|Angehörige|Angehöriger)\s+(?:von\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_49`)


 Der Bf. wohnt seit dem Jahr 2010 mit seiner Ehefrau, Ashley Petzack, und dem  gemeinsamen Sohn Werner Puskeppeleit  in Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich.

| Predicted | Gold |
|---|---|
| `Werner Puskeppeleit` | `Werner Puskeppeleit` |

**Missed by this rule (FN):**

- `Ashley Petzack` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/145657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145657.1_60`)


Feststellungen betreffend die auswärtige Berufsausbildung der Tochter  Die Ausbildung der Tochter ergibt sich aus der glaubhaften Darstellung in der Beschwerde, die  auch von der belangten Behörde bereits in der Beschwerdevorentscheidung zugunsten der  Beschwerdeführerin berücksichtigt wurde.

**False Positives:**

- `Die Ausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names with 'VetR' and similar standalone titles` 🏆

**F1:** 0.014 | **Precision:** 0.289 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `e1aefbb2`  
**Description:**
Captures names immediately following specific standalone titles like 'VetR', 'Ing.', 'Bakk.' without requiring 'Herrn/Frau' prefix.

**Content:**
```
(?:VetR|Ing\.|Bakk\.|Dipl\.-Ing\.|RA\.|StB\.|MedR|KommR|OStR|HR|Fr\.PhD|KzlR|Techn\s+R)\s+([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.289 | 0.007 | 0.014 | 45 | 13 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 13 | 32 | 1838 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Sascha Hilcker` | `Ing. Sascha Hilcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Dominik Mehlig` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Melinda Herrwerth` | `Dipl.-Ing. Melinda Herrwerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dürergasse 7, 4872 Windbichl, Österreich` (address)
- `40-459/9630` (tax_number)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)
- `Lubomir Nakajima` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache MedR Gertrude Hartges,  Hübing 15, 9535 Farrendorf, Österreich, über die Beschwerde vom 10. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MedR Gertrude Hartges` | `MedR Gertrude Hartges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hübing 15, 9535 Farrendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `MedR Uwe Vaculik` | `MedR Uwe Vaculik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Linn Wolek` (person)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_3`)


Begründung  1.a. Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 11. März  2021, Zahl: MA67/216700111216/2021, wurde Frau MedR Uwe Vaculik (in weiterer Folge:   Beschwerdeführerin) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung 2006 für schuldig erkannt und über sie nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer   Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `MedR Uwe Vaculik` | `MedR Uwe Vaculik` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch der Richter R. in der Beschwerdesache Dipl.-Ing. Emma Chatzistamatis, Senden 22, 4673 Unterbergham, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 17. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierten Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019, Steuernummer 59-959/5444, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Emma Chatzistamatis` | `Dipl.-Ing. Emma Chatzistamatis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Senden 22, 4673 Unterbergham, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-959/5444` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Stella Hornscheidt  in der Beschwerdesache Ing. Jaden Stoelzl,  Singham 49, 4274 Straß, Österreich, über die Beschwerden vom 1. Juni 2021 gegen die Bescheide des Finanzamtes  Österreich vom 31. Mai 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016,  2017 und 2018 Steuernummer 25-717/7817  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Jaden Stoelzl` | `Ing. Jaden Stoelzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Stella Hornscheidt` (person)
- `Singham 49, 4274 Straß, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `25-717/7817` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Marion Kloefkorn` | `Ing. Marion Kloefkorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich` (address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG` (organisation)
- `Finanzamtes Österreich` (organisation)
- `40-620/0106` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Aloisia Bergauer in der Beschwerdesache  Ing. Christian Marckwordt, Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung Energiekrisenbeitrag Strom für den Zeitraum 1.12.2022-30.06.2023,  Steuernummer 22-821/5972, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Christian Marckwordt` | `Ing. Christian Marckwordt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Aloisia Bergauer` (person)
- `Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `22-821/5972` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/147373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147373.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Friedhelm Weigmann  in der Beschwerdesache Dipl.-Ing. Sibylle Leichnam,  Anton-Hölzl-Hof 173, 4890 Ziegelstadl, Österreich, über die Beschwerde vom 16. März 2023 gegen den Bescheid des FA Baden Mödling  vom 15. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022,  Steuernummer 10-035/7116, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Sibylle Leichnam` | `Dipl.-Ing. Sibylle Leichnam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Friedhelm Weigmann` (person)
- `Anton-Hölzl-Hof 173, 4890 Ziegelstadl, Österreich` (address)
- `FA Baden Mödling` (organisation)
- `10-035/7116` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

| Predicted | Gold |
|---|---|
| `Ing. Dagobert Almasri` | `Ing. Dagobert Almasri` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/148407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148407.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  des MedR Erna Noellgen, Diesting 46, 4151 Salaberg, Österreich, über dessen Beschwerde vom 7. November 2021 gegen den  Bescheid des Finanzamtes Österreich vom 8. Oktober 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 01-405/3031, zu Recht erkannt:   I. Der angefochtene Bescheid wird im Umfang der Beschwerdevorentscheidung vom  16. Mai 2022 abgeändert.

| Predicted | Gold |
|---|---|
| `MedR Erna Noellgen` | `MedR Erna Noellgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Diesting 46, 4151 Salaberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `01-405/3031` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Dipl.-Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

**False Positives:**

- `MedR Ottfried Theißl` — partial — pred is substring of gold: `OMedR Ottfried Theißl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Ute Gspan`(person)
- `OMedR Ottfried Theißl`(person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich`(address)
- `FA Wien 8/16/17`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Leonhard Hestermeyer` — partial — pred is substring of gold: `OMedR Leonhard Hestermeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski`(person)
- `OMedR Leonhard Hestermeyer`(person)
- `Sägerweg 5, 5450 Reitsam, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `52-932/8889`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`
- `Ing. Viktoria Weigart` — similar text (different position): `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Ing. Viktoria Weigart  Dieses Unternehmen` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)


Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der Dr.in Ing. Viktoria Weigart  Somit traf ihn die Auskunftspflicht.

**False Positives:**

- `Ing. Viktoria Weigart  Somit` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Jonas Thumberger` — partial — pred is substring of gold: `Dipl. Kfm. Ing. Ing. Jonas Thumberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger`(person)
- `Paullehnerweg 72, 9584 Höfling, Österreich`(address)
- `UNICONSULT Steuerberatungs GmbH & Co KG`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_3`)


Begründung  Im Fristsetzungsantrag vom 10. Oktober 2022 wird als Sachverhalt Folgendes vorgebracht:   Mit Antrag vom 14.06.2021 beantragte die Beschwerdeführerin die Auszahlung von  Familienbeihilfe für ihr Kind OMedR Amanda Ratzmer, MSc  VNR 4982 010771  für den Zeitraum  März 2020 - April 2021.

**False Positives:**

- `MedR Amanda Ratzmer` — partial — pred is substring of gold: `OMedR Amanda Ratzmer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Amanda Ratzmer, MSc`(person)
- `4982 010771`(social_security_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde des  OMedR Tanja Kubatsch, Sand/Bundesstraße 2, 4170 Damreith, Österreich, vom 21. Oktober 2022, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 21. September 2022, GZ. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `MedR Tanja Kubatsch` — partial — pred is substring of gold: `OMedR Tanja Kubatsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `OMedR Tanja Kubatsch`(person)
- `Sand/Bundesstraße 2, 4170 Damreith, Österreich`(address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/139401.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139401.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Dr. Dipl.-Ing. Laurence Goetke,  Unterernsthofen 11, 9311 Leiten, Österreich, vertreten durch STB, Adr1, über die Beschwerde vom 10. Dezember 2019  gegen den Bescheid des A vom 12. November 2019 betreffend Umsatzsteuer 2012,  Steuernummer 42-698/5318, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Laurence Goetke` — partial — pred is substring of gold: `Dr. Dipl.-Ing. Laurence Goetke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dipl.-Ing. Laurence Goetke`(person)
- `Unterernsthofen 11, 9311 Leiten, Österreich`(address)
- `42-698/5318`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Dr. Mag. Elmar Ebertz  in der Beschwerdesache Karlheinz Abke,  Schindlauerweg 53, 2392 Dornbach, Österreich  vertreten durch MedR Anneliese Naupert, Bakk. art., über die Beschwerde vom 30. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 27. April 2022, mit dem das Stundungsansuchen  vom 29. März 2022 abgewiesen wurde, Steuernummer 69-865/2288, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `MedR Anneliese Naupert` — partial — pred is substring of gold: `MedR Anneliese Naupert, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mag. Elmar Ebertz`(person)
- `Karlheinz Abke`(person)
- `Schindlauerweg 53, 2392 Dornbach, Österreich`(address)
- `MedR Anneliese Naupert, Bakk. art.`(person)
- `Finanzamtes Österreich`(organisation)
- `69-865/2288`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Deborah Stöbesand  in der Beschwerdesache des  Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke, Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich, über die Beschwerde vom 9. Juli 2022 gegen den Bescheid des  FA Waldviertel  vom 7. Juli 2022 betreffend Abweisung eines Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommensteuer für die Jahre 2017 bis 2019 zu Steuernummer  37-369/8758  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dipl.-Ing. Laurence Wiebecke` — partial — pred is substring of gold: `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Deborah Stöbesand`(person)
- `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`(person)
- `Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich`(address)
- `FA Waldviertel`(organisation)
- `37-369/8758`(tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/140806.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140806.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Moritz Bonnert  in der Beschwerdesache PhD MedR Romana Hupp,  Süßenberger Straße 7, 5270 Vorbuch, Österreich, vertreten durch Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020 Innsbruck, über die Beschwerde  vom 26. Juli 2013 gegen den Bescheid des FA Salzburg-Land  vom 25. Juni 2013 betreffend  Umsatzsteuer 2011, Steuernummer 16-160/7509, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `MedR Romana Hupp` — partial — pred is substring of gold: `PhD MedR Romana Hupp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Moritz Bonnert`(person)
- `PhD MedR Romana Hupp`(person)
- `Süßenberger Straße 7, 5270 Vorbuch, Österreich`(address)
- `Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `FA Salzburg-Land`(organisation)
- `16-160/7509`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait  in der Beschwerdesache   Prof. Ing. Eduard Skroblies, Forchetweg 18, 4692 Albertsham, Österreich,   über die Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf (nunmehr Finanzamt Österreich) vom 10. November 2014 betreffend  Körperschaftsteuer 2011, vom 19. November 2014 betreffend Körperschaftsteuer 2012 und  2013 sowie die Beschwerde vom 12. Juli 2016 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 7. Juli 2016 betreffend Körperschaftsteuer 2014   I. beschlossen:  Der Vorlageantrag betreffend Körperschaftsteuer 2011 wird zurückgewiesen.

**False Positives:**

- `Ing. Eduard Skroblies` — partial — pred is substring of gold: `Prof. Ing. Eduard Skroblies`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`(person)
- `Prof. Ing. Eduard Skroblies`(person)
- `Forchetweg 18, 4692 Albertsham, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_190`)


Zu Vitamin B verwies  sie auf die Verschreibung von Neurobin durch Fr.Dipl.-Ing. Joseph Szwarz Dieses enthalte so viele andere  Zusatzstoffe.

**False Positives:**

- `Dipl.-Ing. Joseph Szwarz Dieses` — positional overlap with gold: `Fr.Dipl.-Ing. Joseph Szwarz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fr.Dipl.-Ing. Joseph Szwarz`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_41`)


XXX/2 und XXX/4 per E-Mail an w.p. @ ...at  übermittelt.   Am 12.08.2010 wurde die Übergabe des Grundstücks EZ xxx Grundbuch A-Ort, A-Platz, A-Ort in  der Konkurssache Fa. A-KG von Anwalt StR Ing. Hedwig Mendle als Masseverwalter der KG an die Bf.,  vertreten durch M.M.A., als Käufer auf der Grundlage des Kaufvertrags vom 28.04.2010  protokolliert.

**False Positives:**

- `Ing. Hedwig Mendle` — partial — pred is substring of gold: `StR Ing. Hedwig Mendle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Ing. Hedwig Mendle`(person)
- `M.M.A.`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Leya Mentzel` — partial — pred is substring of gold: `Mag.a Dipl.-Ing. Leya Mentzel, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Alessia von Bauer  in der Beschwerdesache  Dimitri Seelos, geb. am 19. November 1987  und Dipl.-Ing. Luna Goedecken, BEd MA, geb. am 12. April 1988  als Erben  des Reneé Keles, verstorben am 3. November 1972  über die Beschwerde vom 15. Dezember 2020  gegen die Bescheide des Finanzamtes Österreich vom 27. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2015 bis 2019;

**False Positives:**

- `Dipl.-Ing. Luna Goedecken` — partial — pred is substring of gold: `Dipl.-Ing. Luna Goedecken, BEd MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Alessia von Bauer`(person)
- `Dimitri Seelos`(person)
- `19. November 1987`(date)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)
- `12. April 1988`(date)
- `Reneé Keles`(person)
- `3. November 1972`(date)
- `Finanzamtes Österreich`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_25`)


Mit 3. November 1972  verstarb der Bf. Mit Einantwortungsbeschluss des Bezirksgerichtes  Mattighofen vom 06.06.2023 wurde die Verlassenschaften den erblichen Kindern Dimitri Seelos  und Dipl.-Ing. Luna Goedecken, BEd MA  nach Abgabe einer unbedingten Erbserklärung eingeantwortet.

**False Positives:**

- `Dipl.-Ing. Luna Goedecken` — partial — pred is substring of gold: `Dipl.-Ing. Luna Goedecken, BEd MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `3. November 1972`(date)
- `Dimitri Seelos`(person)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)

</details>

---

## `Names after 'Bf,' (Comma separated)` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8fd8f42b`  
**Description:**
Captures full title and name immediately following 'Bf,' or 'Bf.', handling missing spaces and ensuring valid name structure.

**Content:**
```
Bf[.,]\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s+|\s+r\.\s+nat\.)?|i\.iur\.(?:\s+|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s+|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)*(?:\s+(?:LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|BSc)?)?(?=\s|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 99 | 0 | 99 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 99 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_8`)


Name, Adresse und Geburtsdatum des Bf. Am 23. Juli 2014 erließ das Finanzamt einen Bescheid mit folgendem Inhalt: „Bescheid: Der Antrag von …. Bf. …. vom 15.7.2014, eingebracht am 22.7.2014 betreffend den Antrag auf Wertfortschreibung wird abgewiesen.

**False Positives:**

- `Am` — similar text (different position): `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_14`)


Mit Eingabe vom 11. März 2019 erhob der Bf. Beschwerde gegen den  Einkommensteuerbescheid.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_93`)


3.2. Verlosung von 2 Tickets und Verlosung des Ersatzes diverser Auslagen des täglichen  Lebens durch die Bf.  Die Bf. bringt vor, dass einerseits ein Preisausschreiben eine Sonderform der Auslobung gemäß  § 860 ABGB und kein Spiel darstelle und andererseits „Spiel“ eine Aktivität mehrerer Mitspieler  begrifflich definiere, hingegen die Entgegennahme eines Geschenkes keine Beteiligung an einem  Spiel sei.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_18`)


Weiters wurde begründend  der Rechengang   von der Steuer vor Abzug der Absetzbeträge   über die Abzüge, u.a. dem Familienbonus Plus in Höhe von 750,00 €,   bis zur Steuer nach Abzug der Absetzbeträge  dargestellt.  Dagegen erhob der Bf. Beschwerde, was als Antrag gemäß § 264 BAO auf Entscheidung über  die Beschwerde vom 22. Mai 2020 (Einbringungsdatum) durch das Verwaltungsgericht (hier:  Bundesfinanzgericht) aufzufassen ist.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_66`)


ebenfalls wurde erstmalig vorgebracht, dass auch er, der Bf. Krebs  hat.

**False Positives:**

- `Krebs ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_69`)


Nachweis der geltend gemachten Kosten für Familienheimfahrten:  Auf Grund der obigen Ausführungen ist nur der Vollständigkeit halber festzuhalten:  Betreffend Fahrtkosten, welchen laut dem Vorbringen des Bf. Fahrten mit dem eigenen Kfz  zugrunde liegen, ist die Nachweisführung (anders als bspw.

**False Positives:**

- `Fahrten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_430`)


Die Stellungnahme wurde dem Bf. übermittelt. Mit E-Mail vom 31.8.2020 teilte der Bf.  Folgendes mit:  28 von 34 Seite 29 von 34

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_85`)


Am 5. Juli 2019 erhob die Bf. Einspruch gegen diese Vollstreckungsverfügung.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_96`)


Mit E-Mail vom 3.12.2019 erhob die Bf. Einspruch gegen die Beschwerdevorentscheidung, und  führte aus, sie habe das Fzg nicht gelenkt und bitte um Zusendung einer Lenkererhebung.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_901`)


Tatsache ist, dass die Bf. Gastronomiebetriebe in den Streitjahren betrieben hat, deren  Einkünfte aufgrund mangelhafter Aufzeichnungen zu schätzen gewesen sind.

**False Positives:**

- `Gastronomiebetriebe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_43`)


Außerdem studiert der Bf. Jus, wobei die diesbezüglichen geltend gemachten Kosten als  Werbungskosten im Jahr 2018 anerkannt wurden.

**False Positives:**

- `Jus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_29`)


Bezogen auf den Einkommensteuerbescheid 2010 wendete der Beschwerdeführer  zusammengefasst ein, die Bf. Steuerberatungsgesellschaft mbH sei von ihrem Mandanten D  mit der Beratung und Unterstützung in kaufmännischen wie finanziellen Angelegenheiten „im  Zusammenhang mit der Errichtung einer neuen Zubringerbahn für sein seit 1964 bestehendes  Schigebiet und Hotel S“ beauftragt worden.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_30`)


Im Jahr 2006 habe die Bf.  Steuerberatungsgesellschaft mbH für D und die Schilift GmbH diverse Agenden übernommen  2 von 10 Seite 3 von 10

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_34`)


Nach erfolgreicher Realisierung des „vorgenannten Investitionsvorhabens“  hätte die Bf. Steuerberatungsgesellschaft mbH laut einer mit D getroffenen Vereinbarung  weiterhin sämtliche Beratungsleistungen für dessen Betriebe und der Schilift GmbH zu  erledigen gehabt.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_35`)


Zum Zeitpunkt der Kapitalerhöhung der Schilift GmbH um EUR 1.365.000,-  auf EUR 1.400.000,- habe die Bf. Steuerberatungsgesellschaft mbH 100 % des Stammkapitals  aus ihrem Mandantenkreis als Gesellschafter gewinnen können.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_37`)


Die Neugesellschafter hätten als weitere Bedingung für ihre Finanzierungs- und  Beteiligungszusagen gefordert, dass die Bf. Steuerberatungsgesellschaft mbH sich an der  Schilift GmbH beteiligen müsse und die Geschäftsführung „durch die WT GmbH, in Person ihres  Gesellschaftergeschäftsführers, [des Beschwerdeführers], selbständig, zu übernehmen war.“

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_39`)


Konsequenz dieser Vereinbarung sei  gewesen, dass die Bf. Steuerberatungsgesellschaft mbH „die langfristige Werthaltigkeit der  empfohlenen Investitionen und Beteiligungen unter allen Umständen erhalten musste, da sie  ansonsten nicht nur die Einnahmen aus den Vertretungen D und dessen Unternehmen, sondern  auch die Einnahmen aus den Vertretungen der restlichen Mitgesellschafter verloren hätte“.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_40`)


Sämtliche Leistungen seien nachweislich von der Bf. Steuerberatungsgesellschaft mbH  abgerechnet worden, sie habe den alleinigen Nutzen aus dieser Beteiligung lukriert.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_49`)


Außenprüfungsverfahren der Bf. Steuerberatungsgesellschaft mbH erstattet worden sei.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_75`)


Der Beschwerdeführer war ausweislich des Firmenbuchs in den Jahren 2008 bis 2010  Alleingesellschafter und bis 11.12.2009 Geschäftsführer der im Firmenbuch zu FN_2  eingetragenen UEHX Medien GmbH (vormals Bf. Steuerberatungsgesellschaft m.b.H.).

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `UEHX Medien GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_89`)


Einerseits bezieht sich dieses Vorbringen auf einen Zeitpunkt nach Erlassung des  Erstbescheides, andererseits wurde die Sachverhaltsdarstellung vom 5.9.2012 offensichtlich im  Außenprüfungsverfahren bei der Bf. Steuerberatungsgesellschaft mbH erstattet.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_116`)


Insofern der Beschwerdeführer vermeint, seine (unentgeltliche) Geschäftsführertätigkeit für  die Schilift GmbH stelle bei wirtschaftlicher Betrachtungsweise einen Zusammenhang zwischen  seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus selbständiger Arbeit  als (wesentlich beteiligter) Gesellschafter-Geschäftsführer seiner Wirtschaftstreuhand GmbH  her, ist dem Folgendes entgegenzuhalten: Nach dem Beschwerdevorbringen war die Erzielung  von Einkünften durch die Bf. Steuerberatungsgesellschaft mbH aus Beratungstätigkeiten für D  und dessen Unternehmen und für die neu gewonnenen Mitgesellschafter der Schilift GmbH  von der Erhaltung der „langfristigen Werthaltigkeit der empfohlenen Investitionen und  Beteiligungen“ abhängig.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traun-Handel AG`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_117`)


Dem gegenüber behauptet der Beschwerdeführer nicht einmal, dass  die Höhe seiner eigenen Einkünfte als Gesellschafter-Geschäftsführer der Bf.  Steuerberatungsgesellschaft mbH („jährliche Geschäftsführerentschädigung in Höhe von EUR  36.000,- und sonstige Kostenersätze in Höhe von EUR 15.686,82 [2008 in Einkünften aus  selbständiger Tätigkeit erfasst]“) durch die Umstände seiner Geschäftsführung für die Schilift  GmbH beeinflusst worden wäre.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schilift  GmbH`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_67`)


Nach dem festgestellten Sachverhalt steht fest, dass die Bf. Entgelte bzw. Betriebseinnahmen  nicht in die Umsatz- und Einkommensteuererklärungen der Beschwerdejahre aufgenommen  hat.

**False Positives:**

- `Entgelte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Oberweissburg` — partial — pred is substring of gold: `Oberweissburg 52, 4081 Hartkirchen, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich`(address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `73-948/8864`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_189`)


Mit Schreiben (Verständigung vom Ergebnis der Beweisaufnahme) vom   1) 05.08.2020 teilte die belangte Behörde dem rechtsfreundlichen Vertreter des Bf.  gegenständlichen Sachverhalt mit und bot dem Bf. Gelegenheit zur Stellungnahme innerhalb  von zwei Wochen ab Zustellung dieses Schreibens.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_202`)


Diesbezüglich ist bei der Zentralen  Staatsanwaltschaft zur Verfolgung von Wirtschaftsstrafsachen und Korruption (WKStA) unter  der AZ: AktWKStA ein Ermittlungsverfahren gegen Herr anhängig und werden unter der GZ  GZLPD durch das Landeskriminalamt (LKA) Wien, LKA, 1090 Wien, Wasagasse 22, Ermittlungen  vorgenommen.“  2) bis 5) 23.09.2020 und 6) vom 18.09.2020 teilte die belangte Behörde dem  rechtsfreundlichen Vertreter des Bf. gegenständlichen Sachverhalt mit und bot dem Bf.  Gelegenheit zur Stellungnahme innerhalb von zwei Wochen ab Zustellung dieser Schreiben.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_8`)


In der Erklärung zur Arbeitnehmerveranlagung 2017 machte der Bf. Werbungskosten für  Familienheimfahrten im Betrag von € 3.672,00 sowie Sonderausgaben für Versicherungen im  Betrag von € 920,00 geltend.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_12`)


Nach einem erfolglosen Zustellversuch an der Abgabestelle des Bf. wurde das Straferkenntnis  bei der Post Geschäftsstelle Post hinterlegt, ab 02. März 2021 zur Abholung bereitgehalten und  gilt daher mit diesem Tag als zugestellt.  Mit E-Mail vom 07. April 2021 erhob der Bf. Beschwerde und führte (wörtlich) aus:  „wie schon im ersten einspruch beschrieben, lag der behindertenausweis hinter der scheibe..

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_78`)


Des Weiteren machte der Bf. Unterhaltszahlungen an seine Kinder unter dem Titel „Kosten für  doppelte Haushaltsführung“ als Werbungskosten geltend, allerdings übermittelte der Bf. dazu  lediglich zwei Belege, aus denen Zahlungen im Jahr 2021 und somit außerhalb des  beschwerdegegenständlichen Zeitraums hervorgehen.

**False Positives:**

- `Unterhaltszahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_88`)


Für die beschwerdegegenständlichen Jahre machte der Bf. Kosten für Arbeitsmittel, für  Familienheimfahrten und für die „doppelte Haushaltsführung“ als Werbungskosten geltend.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_340`)


In ihrer Vorhaltsbeantwortung vom 30.9.2020 führte die Bf. Folgendes aus:  „…  2. Vorbemerkung zur Verschaffung der Verfügungsmacht  22 von 59 Seite 23 von 59

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_85`)


Mit Eingabe vom 16.12.2015 erhob die damalige steuerliche Vertreterin der Bf. Beschwerde  gegen die oa Bescheide und stellte gleichzeitig die Anträge auf Entscheidung durch den  gesamten Beschwerdesenat sowie die Durchführung einer mündlichen Verhandlung.

**False Positives:**

- `Beschwerde ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_496`)


Es steht daher fest, dass den Lieferanten der Bf. Umsatzsteuerhinterziehungen vorzuwerfen  sind.

**False Positives:**

- `Umsatzsteuerhinterziehungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_550`)


Dieser Umstand spricht für die Gutgläubigkeit der Bf.  Was die anfängliche Verwechslung des Gf. der Bf. betreffend Herrn K. betrifft, wonach er nicht  gewusst habe, welche Funktion Herr K. gehabt habe, ist entgegenzuhalten, dass sich die  Unkenntnis nur auf das erste Zusammentreffen bezog und sich der Bf. dann eine Passkopie und  die Visitenkarte von Herrn K. aushändigen hat lassen.

**False Positives:**

- `Was` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_7`)


In ihrer Abgabenerklärung machte die Bf. Fortbildungskosten iHv. € 6.387,32 geltend.

**False Positives:**

- `Fortbildungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_82`)


In  den Jahren 2013 und 2015 hat die Bf. Leistungen der Schweizer Krankenversicherung  ÖKK in Anspruch genommen und abgerechnet (vorgelegte Leistungsabrechnungen).

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_170`)


5. EINKOMMENSTEUER 2011 und 2012  WOHNSITZE der Bf.  Die Frage, ob eine Person in Österreich unbeschränkt steuerpflichtig ist, richtet sich nicht nach  Doppelbesteuerungsabkommen, sondern ausschließlich nach den inländischen  steuerrechtlichen Vorschriften.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_5`)


Mit Schriftsatz vom 11.12.2015 brachte die steuerliche Vertretung des Bf. Bescheidbeschwerde  gegen die Einkommensteuerbescheide 2010 bis 2013 und gegen die Anspruchszinsenbescheide  2010 bis 2013 alle vom 9.11.2015 (zugestellt am 13.11.2015) beim Finanzamt am 15.12.2015  ein.

**False Positives:**

- `Bescheidbeschwerde ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_68`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Firma A als Gruppenträgerin ist, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_66`)


Dass die Bf. Teil einer Unternehmensgruppe als Gruppenträgerin mit den genannten weiteren  Gruppenmitgliedern ist, ergibt eine Einschau des Gerichtes in den elektronischen  Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_67`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Firma A als Gruppenträgerin ist, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_221`)


Der Leistungsaustausch kann also wie folgt skizziert werden:  1. D./Deutschland (bis 31. Oktober 2013) und D./Holland (ab 1. November 2013) bestellen  /beauftragen bei der Bf. Werbeleistungen (Produktmarketing und —promotion) als  Leistungsgegenstand.

**False Positives:**

- `Werbeleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_254`)


Die Außenprüfung will die Bf. durch gesetzlich nicht gedeckte Abgabenerhöhungen zwingen,  am Leistungsaustausch nicht beteiligte Dritte auszuforschen und mit Namen und  Anschriften zu nennen: Die Trafikanten, deren Namen und Anschriften die Bf. erkunden soll,  haben an die Bf. weder Leistungen erbracht noch an die Bf. Leistungen abgerechnet.

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_317`)


Seitens der Bf. wurden die Teilnehmer (Trafikanten) an den Awards - trotz Aufforderung durch  die Außenprüfung- nicht benannt, da die Trafikanten an die Bf. weder Leistungen erbracht  noch an die Bf. Leistungen abgerechnet haben und sich die Bf. daher auch keine  Betriebsausgaben mangels Leistungsbezug von den Trafikanten abgezogen hat.

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_71`)


In diesem Fall bestünde ein  Familienbeihilfenanspruch des Bf. Andernfalls hat der Bf. für seine Tochter, die nicht  haushaltszugehörig ist, mangels überwiegender Unterhaltleistung weder nach  Gemeinschaftsrecht noch nach innerstaatlichem Recht einen Anspruch auf Familienbeihilfe.

**False Positives:**

- `Andernfalls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_12`)


In diesen wurde ausgeführt, dass  der Bf. Polizeibeamter sei, und seit dem Jahr 2007 mehrere Monate im Jahr auf  Auslandseinsätze für die europäische Grenzschutzagentur Frontex entsandt werde.

**False Positives:**

- `Polizeibeamter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Frontex`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_64`)


Außerdem wohnt  der Bf. Im Familienverband mit seiner Mutter gegenüber (cf. Übergabevertrag).

**False Positives:**

- `Im Familienverband` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_211`)


Aus den vorgebrachten und vorgelegten Mailverkehr vom Oktober 2021 (vorgebrachter  „mehrtägiger Kontakt mit dem BMF“) über Probleme bei der Eintragung kommt jedenfalls  nicht Ausdruck, dass die Bf. Willens war, die WiEReG-Meldung irgendwie zeitnah  durchzuführen oder allfällige vorgebrachte technische Schwierigkeiten, allfällige  Anfangsschwierigkeiten und Datenprobleme zügig und zeitnah zu überwinden.

**False Positives:**

- `Willens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_79`)


Rechtliche Beurteilung:    Strittig ist, ob dem mj. Bf. Familienbeihilfe und Kinderabsetzbeträge ab jänner 2016 zustehen.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_19`)


Die Beschwerdevorentscheidungen wiesen die Beschwerde als unbegründet ab, wogegen der  Bf. Vorlageantrag einbrachte.

**False Positives:**

- `Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_8`)


Aufgrund der Inanspruchnahme des Bf. Jaden Knauss  als Haftenden iSd § 82 EStG stehe dieses  nach haushaltsrechtlichen Bestimmungen in der Pflicht von den Dienstnehmern, welche eine  Naturalwohnung benützten und Schuldner der Lohnsteuer seien, einen Regress durchzuführen.

**False Positives:**

- `Jaden Knauss ` — partial — gold is substring of pred: `Jaden Knauss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jaden Knauss`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_107`)


Unter Abwägung, dass zwar bestimmte Zubehörteile einer höheren privaten Nutzung (z.B.  „Gaming-Tastatur) zuzuordnen sind, andere wiederum weniger, die Festplatte im Jahr 2020 zu  maximal 20% mit Studiumsdateien belegt war, erscheint ein iSd 184 BAO auszuscheidender  Privatanteil iHv 40 % für dieses EDV-Zubehör als angemessen und wird hiermit sowohl dem  Vorbringen des Finanzamtes als auch dem des Bf. Rechnung getragen.

**False Positives:**

- `Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_6`)


Mit Haftungsbescheid vom 22. Mai 2019 wurde Olaf Koechig (Bf, Gesellschafter der Gartfentri Heizung Institut GmbH  als  Haftungspflichtiger gemäß § 9 iVm §§ 80 ff Bundesabgabenordnung (BAO) für die  aushaftenden Abgabenschuldigkeiten der Gartfentri Heizung Institut GmbH  im Ausmaß von 318.077,07 € in Anspruch  genommen und aufgefordert, diesen Betrag innerhalb eines Monats ab Zustellung dieses  Bescheides zu entrichten.

**False Positives:**

- `Gesellschafter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Olaf Koechig`(person)
- `Gartfentri Heizung Institut GmbH`(organisation)
- `Gartfentri Heizung Institut GmbH`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_54`)


Dagegen richtet sich die fristgerecht eingebrachte Beschwerde vom 22. März 2022, in welcher  die Bf. Folgendes ausführt:  „Hiermit leite ich eine Beschwerde gegen den Halter vom Fahrzeug ein!

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_15`)


Gebäude gehörten nicht  ins Umlaufvermögen der Bf.  Der AfA- Satz betrage nach Ansicht des FA 2,5%.

**False Positives:**

- `Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_5`)


Mit Eingabe vom 07.03.2020 nahm die Bf. Stellung zu den beantragten Ausgaben.

**False Positives:**

- `Stellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_90`)


Die Berücksichtigung des Pensionistenabsetzbetrages war gemäß § 33 Abs. 6 EStG 1988  deshalb angesetzt worden, da der Bf. kein Anspruch auf Verkehrsabsetzbetrag zugesprochen  worden war und die Bf. Pensionsabfindung im Jahre 2017 bekommen hatte.

**False Positives:**

- `Pensionsabfindung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_257`)


Auch § 23 AlVG ist in diesem Fall nicht anwendbar, weil die Bf. Arbeitslosengeld erhalten hat,  welches keine Bevorschussung von Leistungen aus der Pensionsversicherung darstellte und  darstellt.  Zu den Berechnungen der Negativsteuer ist auszuführen, dass gemäß § 33 Abs. 8 EStG 1988  eine Negativsteuer nur zu erstatten ist, wenn gemäß Z 1 lit. cit.

**False Positives:**

- `Arbeitslosengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_11`)


Gegen diesen, am 15.05.2019 ausgestellten, Einkommensteuerbescheid 2015 wurde ein  Antrag auf Aufhebung gem. § 299 Abs. 1 BAO gestellt. Dazu vorgelegt wurde eine Aufstellung  der tatsächlich erhaltenen Beträge (EUR 2.506,82), eine Aufstellung der Tage, an denen vom  Bf. Taxifahrten durchgeführt wurden sowie die Bestätigung über den abgeleisteten Zivildienst  im Zeitraum von 01.10.2014 bis 30.06.2015.

**False Positives:**

- `Taxifahrten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_18`)


Am 31.10.2019 brachte der Bf. Beschwerde ein.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/140407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140407.1_94`)


Es folgt:  In Jahren, in welchen die Bf. Betriebseinnahmen infolge von Immobilienverkäufen lukrierte,  leistete sie aufgrund der dargestellten Vereinbarungen am Tag deren Abschusses sogenannte  „Immobilienanzahlungen“ an die GmbH1  bzw. an die an deren Stelle tretende XY Invest  Gesellschaft mbH (im Schema: GmbH 1).

**False Positives:**

- `Betriebseinnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_30`)


5. Gegen den Abweisungsbescheid vom 17.03.2023 wurde von der steuerlichen Vertretung des  Bf. Beschwerde eingebracht (eingebracht per FinanzOnline am 14.04.2023).

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/142566.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142566.1_23`)


Die Zustellung des gegenständlichen Bescheides erfolgte direkt an die Bf. Eine Zustellung an die  zustellbevollmächtigte Vertretung erfolgte nicht.

**False Positives:**

- `Eine Zustellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/142648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142648.1_7`)


Dagegen erhob der Bf. Beschwerden mit der Begründung, dass ihm auch für die Stieftochter  der Familienbonus Plus zustehe, da er auch der Bezieher der Familienbeihilfe für seine  Stieftochter im Zeitraum Juli - Dez 2020 sowie Jänner - Dezember 2021 war.

**False Positives:**

- `Beschwerden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/143650.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143650.1_38`)


Dieser Sachverhalt basiert auf den Angaben des Bf. Wegen des unstrittig vom FA nicht  geforderten Zustellnachweises lässt sich die fehlende Zustellung des streitgegenständlichen  Schriftstückes durch die Post nicht widerlegen.

**False Positives:**

- `Wegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Othmar Garbe, Bf. Adresse, Ort in Kärnten, vertreten durch Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee,  über die Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 14. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 – 2015 (Steuernummer 29-838/1383) zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Adresse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Othmar Garbe`(person)
- `Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `29-838/1383`(tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_63`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Möhlmeyer Immobilien GmbH als Gruppenträgerin war, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möhlmeyer Immobilien GmbH`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_58`)


Mit Schreiben vom 24.08.2023 erinnerte die Nord Ostunisyn GmbH daran, dass dieser Fall auf die Zeit  zwischen 2003 und 2006 zurückgehe, in der Bf. Optionen im Rahmen der S.P. Corp.

**False Positives:**

- `Optionen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nord Ostunisyn GmbH`(organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_101`)


Sachverhalt   Sachverhaltsmäßig steht fest, dass der Bf. Optionen, die ihm der Arbeitgeber im Jahr 2003 und  2006 eingeräumt hatte, im Jahr 2012 ausgeübt hat.

**False Positives:**

- `Optionen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_22`)


Nach Erlangung der Kenntnis von Laseroperationen in A-Stadt habe die Bf. Dr. A3 konsultiert,  welcher sich zur Durchführung einer Operation nach entsprechender Vorbereitung der  Patientin bereit erklärt habe.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. A3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. A3`(person)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_196`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Ag Bel des Bf.  Der Bf. macht diverse ag Bel für sich und seine Ehegattin geltend.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_299`)


Zur ag Bel des Bf.  Aus Sicht des BFG sind dem Bf. die Aufwendungen für Arztkosten, Fahrten zu Ärzten sowie die  Lesebrille als ag Bel zu gewähren (€ 88,47 laut BVE).

**False Positives:**

- `Aus Sicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_111`)


Die im Verfahren vorgelegte Gleitzeitvereinbarung des Bf mit seinem Dienstgeber vom  August 2017 ließ ausreichend Spielraum für eine flexible Anpassung des Arbeitsbeginns bzw.  Arbeitsendes an die Fahrpläne des Regionalbusses 9999 durch den Bf. Auch an Arbeitstagen  mit Arbeitsbeginnzeiten zwischen 8:30 und 9:30 Uhr, die nach den Arbeitsaufzeichnungen des  Bf weitaus überwogen, standen nach einer regelmäßigen/überwiegenden Arbeitszeit von neun  Stunden zumutbare Busverbindungen zur Verfügung.

**False Positives:**

- `Auch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/145502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145502.1_6`)


Von 18.6. – 10.6.2018 bezog die Bf. Wochengeld, danach Karenzgeld  Am 9.4.2018 erfolgte die Anzeige einer Lebendgeburt des ersten Kindes der Bf.

**False Positives:**

- `Wochengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/145625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145625.1_13`)


Zudem habe die Bf. Mindestsicherung bezogen, die von der MA 40 zu einer Rückforderung des  Überbezuges geführt habe.

**False Positives:**

- `Mindestsicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_513`)


…“   Mit Antwortschreiben vom 8. Jänner 2024 (OZ. 61) führte die Bf. Folgendes aus:  „…  1.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_587`)


…“  Mit Antwortschreiben vom 7. März 2024 (OZ. 90) führte die Bf. Folgendes aus:  „ …  1.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_21`)


4)  Daraufhin wurde am 31. Oktober 2022 seitens des Bf. Folgendes eingereicht:   Einzelaufstellung zur Kennzahl 719 – Arbeitsmittel (bzw. die jährliche AfA bei  Anschaffungen über 800 Euro):  [c/1] Geringwertige Wirtschaftsgüter 957,07 €;  [c/2] AfA Anschaffung 2017: 419,23 €;  [c/3] Telefonkosten 214,50 €;  (Summe 1.590,80 €; vgl.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_30`)


Auf das bereits ergangene Vorhalteschreiben wird verwiesen.“  6)  Daraufhin wurde am 17. Jänner 2023 seitens des Bf. Folgendes eingereicht:   Einzelaufstellung zur Kennzahl 719 … [wie am 31. Oktober 2022 eingereicht, s.oben]   Einzelaufstellung zur Kennzahl 724 … [wie am 31. Oktober 2022 eingereicht, s.oben].   Auftragsbestätigung zur Überweisung … [wie am 31. Oktober 2022 eingereicht, s.oben]   Handschriftlich geführtes Fahrtenbuch mit Summe 2.413 x 0,42 = 1.013,46.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_245`)


(NameEinzelunternehmer) als Auftragnehmer abgeschlossene  Vertrag vom 11. März 2020 nennt als Auftraggeber die „Partei_lokaleParteiorganisation“ und  nicht den Bf.  Der Bf. hat den Vertrag als Vertreter der „Partei_lokaleParteiorganisation“ unterfertigt.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_408`)


Mit den vom Bf. am 17. Jänner 2023 bei der belangten Behörde eingereichten Rechnungen von  gastronomischen Betrieben aus dem Jahr 2020 hat der Bf. Aufwendungen für Essen und  Getränke nachgewiesen.

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_185`)


Ansicht Bf.   Es sei dem Bf. nicht bekannt, dass in Österreich die freie Arztwahl abgeschafft worden sei, oder  die Versorgung/Hilfestellung/Pflege/Hilfsbedürftigkeit bei immungeschwächten,  13 von 43 Seite 14 von 43

**False Positives:**

- `Es` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_271`)


Ansicht Bf.   Der Bf. führte aus, dass der Allergiepass ein Behindertenhilfsmittel im weiteren Sinn sei, da  Unverträglichkeiten Teil des Krankheitsbildes bei Neurodermitis und Asthma und ursächlich für  den Grad der Behinderung seien, wie auch die Chemie- und Medikamentenunverträglichkeit.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_346`)


Ansicht Bf.   Zu A.i.-Enzymen:   Daosin sei ein Mittel nur für die Histaminintoleranz, A.i.-Enzyme würden laut Bf. jedoch bei  Fruktose-, Laktose- und Histaminintoleranz Wirkung zeigen.

**False Positives:**

- `Zu` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_571`)


Es wäre am Bf. Verblieben, seine Vorbringen durch  entsprechende Unterlagen nachvollziehbar zu dokumentieren.

**False Positives:**

- `Verblieben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_82`)


Am 10.7.2015 erhob die Bf. Beschwerde gegen den Bescheid betreffend Wiederaufnahme  des Verfahrens betreffend Einkommensteuer 2007 und beantragte „die Wiederaufnahme des  Bescheides rückgängig zu machen und den zu Grunde liegenden Einkommensteuerbescheid  wieder in den vorigen Stand zu setzen.“  6 von 34 Seite 7 von 34

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_88`)


Mit Eingabe vom 5.10.2015 erhob die Bf. Beschwerde gegen die Bescheide betreffend  Einkommensteuer 2007 und Anspruchszinsen zur Einkommensteuer 2007 und stellte den  Antrag, den Einkommensteuerbescheid wieder in den vorigen Stand, sowie die  Aussetzungszinsen auf null zu setzen.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/147420.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147420.1_16`)


Am 20. März 2024 erhob die Bf. Beschwerde gegen diesen Bescheid.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_10`)


Es sei  weder glaubhaft noch nachvollziehbar, dass der Bf. Ausgaben (Provisionen Dritter) im  Veranlagungsverfahren unbekannt gewesen seien bzw. erst danach „neu hervorgekommen“  1 von 5 Seite 2 von 5

**False Positives:**

- `Ausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/148735.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148735.1_5`)


Am 30. Juni 2023 erhob die Bf. Beschwerde und führte zur Begründung – wörtlich dargestellt –  aus:  "… Der Bescheid ist hinsichtlich der Einstufung meiner Tätigkeit als nebenberufliche  Vortragende an der Akademie und der damit verbundenen eingehobenen Lohnsteuer samt  damit verbundener Reduktion meiner Abgabengutschrift um rd.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_94`)


Als weiteren Grund für die verspätete Einreichung der Abgabenerklärungen führte der  steuerliche Vertreter des Bf. Schwierigkeiten, geeignetes Personal zu finden, an.

**False Positives:**

- `Schwierigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/149152.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149152.1_8`)


Der dargestellte Verfahrensgang und hier entscheidungswesentliche Sachverhalt ergibt sich  aus den vom Finanzamt vorgelegten Aktenteilen, insbesondere auch aus den Ausführungen der  Bf.  Rechtliche Würdigung:  1 von 3 Seite 2 von 3

**False Positives:**

- `Rechtliche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/149304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149304.1_64`)


In  Zusammenhang mit dieser Tätigkeit machte der Bf. Betriebsausgaben unter den  Kennzahlen 9110, 9160 und 9259 geltend.

**False Positives:**

- `Betriebsausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_74`)


Nichts destotrotz überließ die Bf. Teile des vorstehenden Objekts an die Plöchinger KI GmbH zur  Mitbenutzung, wobei nicht feststellbar ist, ob und wenn ja wie viele Quadratmeter dabei  tatsächlich in Unterbestand gegeben wurden.

**False Positives:**

- `Teile` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Plöchinger KI GmbH`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_47`)


Beweiswürdigung  Der festgestellte Sachverhalt, der zugleich dem Verfahrensablauf entspricht, ist unstrittig und  gründet sich auf den Inhalt des vorgelegten Verwaltungsaktes bzw die Eingaben der Bf.   Unstrittig ist insbesondere der entscheidungserhebliche Sachverhalt, wonach mit dem  Umsatzsteuerbescheid 2015 vom 30. Juni 2017 eine Abgabennachforderung iHv 308.650,49  Euro, deren Aussetzung von der Bf mehrfach beantragt und auch bewilligt worden war,  festgesetzt wurde.

**False Positives:**

- `Unstrittig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/149813.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149813.1_5`)


Mit Beschwerden vom 21. Dezember 2023 erhob die Bf. Einwendungen gegen die oa.  Bescheide.

**False Positives:**

- `Einwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_16`)


Weitere Ausführungen  dazu erfolgten nicht durch den Bf.  Mit Beschwerdevorentscheidungen für die Jahre 2015 bis 2019, jeweils vom 18.01.2021,  wurden die Beschwerden als unbegründet abgewiesen.

**False Positives:**

- `Mit Beschwerdevorentscheidungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_25`)


Mit 3. November 1972  verstarb der Bf. Mit Einantwortungsbeschluss des Bezirksgerichtes  Mattighofen vom 06.06.2023 wurde die Verlassenschaften den erblichen Kindern Dimitri Seelos  und Dipl.-Ing. Luna Goedecken, BEd MA  nach Abgabe einer unbedingten Erbserklärung eingeantwortet.

**False Positives:**

- `Mit Einantwortungsbeschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `3. November 1972`(date)
- `Dimitri Seelos`(person)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)

</details>

---

## `Names after 'von' (Befunden/Gutachten)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45258c48`  
**Description:**
Captures the name following 'von' in specific contexts using a capture group to exclude the context phrase.

**Content:**
```
(?:Befunden|Gutachten|Stellungnahme|Aussage|Schreiben|Einspruch|Antrag|Ansuchen|E-Mail|Mail|Bescheinigung|Bescheid|Verf\u00fcgung|Urteil|Entscheidung|Klage|Rechtsmittel|Vertretung|Anwalt|Rechtsanwalt|Notar|Gericht|Beh\u00f6rde|Amt|Finanzamt|Magistrat|Bundesfinanzgericht|Verwaltungsgericht|Verwaltungsstrafbeh\u00f6rde|VfGH|OGH|VwGH|BFG)\s+(?:von\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
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

## `Names after 'Arbeitsplatz des' (Contextual)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `494f2df2`  
**Description:**
Captures full title and name following 'Arbeitsplatz des' or 'Arbeitsplatz der', ensuring valid name structure.

**Content:**
```
(?:Arbeitsplatz\s+(?:des|der)\s+)(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)*(?:\s+(?:LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|BSc)?)?(?=\s|,|\.|\n|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_85`)


Im Beschwerdefall ist eine Verlegung des Familienwohnsitzes auf Dauer schon deswegen  unzumutbar, da der Arbeitsplatz des Bf. ständig wechselt (siehe Fahrtenbuch).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_122`)


Zu den Stoffen, welche lt.  Gefahrstoffliste im Tätigkeitsbereich der Bf. verwendet werden und die nach Angaben der Bf.  ebenfalls eine Gefährdung für ihr Leben und Gesundheit darstellten, ist festzuhalten, dass  selbst nach den Angaben in der dem Bundesfinanzgericht vorliegenden Liste der Arbeitsstoffe  („Gefahrstoffliste B“) von den in den Labors und am Arbeitsplatz der Bf. verwendeten  Arbeitsstoffen keine oder keine besonderen Gefährdungen zu erwarten sind und diese Stoffe  unter Benützung entsprechender Schutzkleidung und technischer Schutzmaßnahmen  verwendet werden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

## `Names after 'Herrn' or 'Frau' (Accusative/Dative)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c40bbb94`  
**Description:**
Captures full title and name following 'Herrn' or 'Frau', ensuring the name includes at least a first and last name (or title + first + last) to avoid partial matches.

**Content:**
```
(?:Herrn|Frau)\s+(?:(?:Dr\.(?:\s+Priv\.-Doz\.)?|Dr\.in|Mag\.(?:\s+Univ\.-Prof\.)?|Mag\.a|Univ\.-Prof\.(?:\.in)?|Priv\.-Doz\.(?:\.in)?|Hon\.-Prof\.(?:\.in)?|Hon\.-Prof\.|MedR|KommR|Ing\.|Bakk\.(?:\s+iur\.)?|LLM|BSc|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|RgR|OStR|HR|Fr\.PhD|Mag\.|VetR|DDr\.|LL\.B\.(?:\s+LL\.M\.)?|B\.iur\.(?:\s|\s+r\.\s+nat\.)?|i\.iur\.(?:\s|\s+r\.\s+nat\.)?|Bakk\.(?:\s+r\.\s+nat\.|\s+art\.)?|LL\.M\.(?:\s|\s+LL\.B\.)?|M\.B\.L\.|LL\.B\.|MBA|MSc|\u00d6kR\s+Dipl\.-Ing\.|DI|Dipl\.(?:\s+Kff\.)?|StR|\u00d6kR\s+Dipl\.-Ing\.)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
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

## `Names after 'von' (General Context)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `48220079`  
**Description:**
Captures the name following 'von' in broader legal contexts, handling split titles and ensuring full name capture.

**Content:**
```
(?:Befunden|Gutachten|Stellungnahme|Aussage|Schreiben|Einspruch|Antrag|Ansuchen|E-Mail|Mail|Bescheinigung|Bescheid|Verf\u00fcgung|Urteil|Entscheidung|Klage|Rechtsmittel|Vertretung|Anwalt|Rechtsanwalt|Notar|Gericht|Beh\u00f6rde|Amt|Finanzamt|Magistrat|Bundesfinanzgericht|Verwaltungsgericht|Verwaltungsstrafbeh\u00f6rde|VfGH|OGH|VwGH|BFG|Online\s+Wettprodukt|Liegenschaft|Zeitraum|Angaben|des|der)\s+(?:von\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn\s+R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_139`)


Wir dürfen hierzu auf das Schreiben von Richter Dr. V hinweisen, der in  seinem Schreiben vom 23.07.2019 darauf hinweist, dass die Bestellung trotz Austragung aus  der Sachverständigenliste erfolgt ist, um Verzögerungen bei gerichtlichen Verfahren zu  vermeiden.

**False Positives:**

- `Richter Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Names after 'durch' (Judge/Representative)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d7c5313e`  
**Description:**
Captures the name following 'durch den Richter' or 'durch die Richterin', handling split titles and ensuring full name capture.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin)\s+)(?:(?:Dr\.|Mag\.|Univ\.-?Prof\.|Hon\.-?Prof\.|Priv\.-?Doz\.|Ing\.|Bakk\.|LL\.M\.|LLM|BSc|B\.iur\.|i\.iur\.|M\.B\.L\.|LL\.B\.|MBA|MSc|PhD|MA|StR|RA\.|StB\.|MedR|KommR|VetR|DDr\.|RgR|OStR|HR|Fr\.PhD|\u00d6kR|DI|Dipl\.|Techn\s+R|KommR|KzlR)\s+)?([A-Z][a-z\u00df]+(?:\s+[A-Z][a-z\u00df]+)+)(?=\s|,|\.|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dieter Brennscheid, Bakk. rer. nat. in der Beschwerdesache Ines Gora,  Thunhausweg 19, 8311 Wetzawinkel, Österreich, über die Beschwerde vom 30. September 2016 gegen die Bescheide des  Finanzamtes Österreich vom 12. Juli 2016 betreff a) Umsatzsteuer für die Jahre 2011 bis 2015,  b) Festsetzung von ersten Säumniszuschlägen vom 09.08.2016,  c) Festsetzung von  Stundungszinsen vom 09.09.2016, Steuernummer 68-68-ZZZZZ (ehemals  18-383/0472 )  nach Durchführung einer mündlichen Verhandlung am 26.11.2024 zu Recht erkannt:      I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2011 bis 2015 wird gemäß        § 279 BAO Folge gegeben.

**False Positives:**

- `Dieter Brennscheid` — partial — pred is substring of gold: `Dieter Brennscheid, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dieter Brennscheid, Bakk. rer. nat.`(person)
- `Ines Gora`(person)
- `Thunhausweg 19, 8311 Wetzawinkel, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `18-383/0472`(tax_number)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1157, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)

Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der **Dr.in Ing. Viktoria Weigart**  Somit traf ihn die Auskunftspflicht.

- missed: `Dr.in Ing. Viktoria Weigart` (person)
- predicted in sentence: `Ing. Viktoria Weigart  Somit`

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  **HR OSR Leonie Ercklentz**, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `HR OSR Leonie Ercklentz` (person)
- predicted in sentence: `Dr. Siegfried Fenz`

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_220`)

**Dr. Dok2** wählte, wie schon Dr. Dok1, 2 Stufen über dem unteren Rahmensatz, da eine mäßige  Einschränkung der sozialen Fähigkeiten und die Absolvierung eines Studiums möglich sei.

- missed: `Dr. Dok2` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_51`)

Das **Jaden Knauss**  beantragte daraufhin mit Schreiben vom 29.06.2021 die Vorlage der Beschwerde  zur Entscheidung durch das Bundesfinanzgericht und verwies auf die Ausführungen des  Antrages vom 28.09.2020.

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_40`)

S. wurde am 1. Juli 2021 von **Dr.in Dok3** untersucht und folgendes Gutachten erstellt:  Anamnese:  Siehe auch Vorgutachten vom 2.3.2021  Es wurde kein Grad der Behinderung ermittelt. Da zwar gutachterliche Diagnosen gestellt  wurden, jedoch mangels an Anspruchnahme adäquater Therapien eine für die Beurteilung  alltags relevante anhaltende Einschränkung erforderliche ärztliche Verlaufsdokumentation  nicht vorhanden ist.

- missed: `Dr.in Dok3` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_275`)

Frage: Haben Sie nachgefragt bei Herrn **M.**, wer die zweite anwesende Person (gemeint ist der  kein Wort deutsch sprechende Herr K., der Geschäftsführer der e.) ist?

- missed: `M.` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_110`)

Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr **Russbüldt**  geb. Herrgeb, AdrHerr.

- missed: `Russbüldt` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin **Mag. Judith Daniela Herdin-Winter** in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Mag. Judith Daniela Herdin-Winter` (person)
- predicted in sentence: `Mag. Judith Daniela`, `Dipl.-Ing. Leya Mentzel`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen **Timon Thoennißen**, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

- missed: `Timon Thoennißen` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_378`)

Die Voraussetzungen für einen Abzug von der Kosten des Herrn **M.** als außergewöhnliche  Belastung im Jahr 2018 liegen insgesamt nicht vor.

- missed: `M.` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_3`)

Entscheidungsgründe  I. Verfahrensgang  1. Verfahren vor der belangten Behörde:  Die Beschwerdeführerin **Volkmar Oortwyn** (in der Folge als Bf bezeichnet) machte am 20.11.2019  einen handschriftlichen Antrag auf Rückzahlung eines Betrages von 360 € an die belangte  Behörde.

- missed: `Volkmar Oortwyn` (person)
- predicted in sentence: —

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr **Kirsten Renneissen** – ist Malermeister und betreibt ein  Einzelunternehmen.

- missed: `Kirsten Renneissen` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_22`)

In ihrer Sachverhaltswürdigung kommt der angefochtene Bescheid zum Ergebnis, die erste  Lieferung in der Reihe sei die „bewegte“, weil der erste (**M.** GmbH) oder der zweite  Unternehmer (Bf.) in der Reihe den Transport durchführt oder beauftragt.

- missed: `M.` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_238`)

Anzumerken ist, dass ein **Dr. Karl** RA1  (Jahrgang XYZ) zumindest seit 1981 mit diversen Haupt- und Nebenwohnsitzen im  Melderegister aufscheint, ab 2010 mit der Adresse AdresseWien als Hauptwohnsitz.

- missed: `Dr. Karl` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_25`)

Die zuständige  EU-Sozialkommissarin Marianne **Thyssen** hatte Österreichs Pläne in der Vergangenheit  wiederholt kritisch beurteilt und vor einer Diskriminierung gewarnt.

- missed: `Thyssen` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_139`)

Offene Forderungen wurden versucht durch Gegenforderungen auszugleichen (Niederschrift  vom 22.06.2018):   2015 **Gerald Bährensmann**  Werbung (6700) ER 15210 v. 30.10.2015 – Gegenrechnung Eberler Bau KG  Rechnung 01.07.2020 Leistungszeitraum 2016;

- missed: `Gerald Bährensmann` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache **Theodora Urbanova, Bakk. iur.**, St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Theodora Urbanova, Bakk. iur.` (person)
- predicted in sentence: `Mag. Helga Hochrieser`, `Theodora Urbanova`

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149853.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149853.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Bodo Stocklauser  in der Beschwerdesache des  **Kirstin Nitschner**, Fabjan-Hafner-Passage 11, 5274 Alharting, Österreich, betreffend die Beschwerde vom 27. Februar 2024 (bzw. den  ebenfalls als „Beschwerde“ bezeichneten Vorlageantrag vom 7. Juni 2024) gegen den Bescheid  des Finanzamtes Österreich vom 14. Februar 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023, Steuernummer 77-148/0749, beschlossen:  Der Vorlageantrag vom 7. Juni 2024 wird gemäß § 264 Abs. 4 lit. e iVm. § 260 Abs. 1 lit. b BAO  als nicht fristgerecht eingebracht zurückgewiesen.

- missed: `Kirstin Nitschner` (person)
- predicted in sentence: `Univ.-Prof. Bodo Stocklauser`

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter **Mag. Markus Knechtl LL.M.** in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

- missed: `Mag. Markus Knechtl LL.M.` (person)
- predicted in sentence: `Mag. Markus Knechtl`, `Robert Derici`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/145368.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145368.1_34`)

Herr **Gotthard Dinkelmann**  hat in eigener Recherche noch herausgefunden, dass bei unbeschränkter  Schweizer Steuerpflicht nur ein sehr enger Kostenkatalog berücksichtigt werden könnte:  „Schuldzinsen, Beiträge in die Säule 2b und 3a, berufliche Weiterbildungskosten, bezahlte  Alimente, Unterstützungsbeiträge“ und bei beschränkter Steuerpflicht lediglich „Beiträge an  die Säule 2b und 3a sowie Wochenaufenthaltskosten“.

- missed: `Gotthard Dinkelmann` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_13`)

Der mj. **OSR Eugenia Balikci**  befand steh im abweisenden Zeitraum ab  Jänner 2016 in einer sozialpädagogischen Wohngemeinschaft der Sozialwerke Clara Fey.

- missed: `OSR Eugenia Balikci` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Caroline Bolzen, Patschweg 38, 9635 Nölbling, Österreich, vertreten durch **Christine Maria Brunnthaller**, Baumgarten 20 Tür  2, 3512 Mautern/Donau, über die Beschwerde vom 25. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 18. März 2024 betreffend Familienbeihilfe 07.2023-03.2024 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Christine Maria Brunnthaller` (person)
- predicted in sentence: `Dr. Susanne Zankl`, `Caroline Bolzen`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_284`)

2004-3 Schulpsychologisches Gutachten,**Adrian Fischäß**: Legastheniediagnose, spezifische Förderung  wurde empfohlen (außerschulische Legastheniebetreuung)  2004 Institut für angewandte Heilpädagogik: seit Okt.

- missed: `Adrian Fischäß` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Hon.-Prof. Adalbert Köseoglu**  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hon.-Prof. Adalbert Köseoglu` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Rechtssache Brian Nieclaassen, Eiblweg 116, 4893 Brandstatt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 29.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe vom  8. August 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2013-

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/145618.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145618.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  **Chiara Fritschy, Bakk. rer. nat.**, Großerstraße 25, 4694 Edlach, Österreich, vertreten durch i-tax Steuerberatungs GmbH, Triesterstraße 14,  2351 Wiener Neudorf, über die Beschwerde vom 3. Mai 2022 gegen den Bescheid des  Finanzamtes Österreich vom 4. April 2022 betreffend Forschungsprämie § 108c EStG 1988  2019 Steuernummer 18-489/9430  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

- missed: `Chiara Fritschy, Bakk. rer. nat.` (person)
- predicted in sentence: `Dr. Hans Blasina`, `Chiara Fritschy`

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/141586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141586.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaromir Hendl  in der Beschwerdesache **KommR Univ.-Prof. Leander Wehe**,  Mahlhofweg 9, 8863 Mitterberg, Österreich, über die Beschwerde vom 23. März 2023 gegen den Bescheid des FA Graz-Stadt  vom 9. März 2023 betreffend Säumniszuschlag 2023 Steuernummer 61-179/3197  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `KommR Univ.-Prof. Leander Wehe` (person)
- predicted in sentence: `Mag. Jaromir Hendl`, `Univ.-Prof. Leander Wehe`

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Rechtssache Martin Yüksekkaya, Bonnleiten 21S, 4724 Aigen, Österreich  vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31. März 2014 gegen den Bescheid des Finanzamtes für Großbetriebe vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2012  (Steuernummer 68-939/1151 ) nach Durchführung einer mündlichen Verhandlung am  06.07.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_82`)

Von STB2, gesendet Mittwoch, 6. Oktober 2021:   S.g. Herr BMF2, mit Dank für Ihre Hilfsbereitschaft möchte ich als ehemaliger Mitarbeiter der  FV und Freund des früheren Sektionschefs **Dr. Nolz** doch festhalten: Das von wem immer  erzwungene WiEReg ist nicht ganz gelungen!

- missed: `Dr. Nolz` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_111`)

Zudem hat der Europäische Gerichtshof im Urteil  „**Schmelz**“, Rs C-97/09, die Ansicht der Generalanwältin nicht geteilt, wonach der Begriff  Ansässigkeit so  auszulegen sei, dass eine Person lediglich einen dauerhaften festen  Bezugspunkt in den betroffenen Staat haben müsse und der Eigentümer einer Immobilie als  ansässiger Steuerpflichtiger zu betrachten sei, auch wenn dieser die Immobilie nicht selbst als  Wohnung nutze.

- missed: `Schmelz` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_13`)

Mit Schreiben vom 30. Dezember 2020 wurde die Fa. E. – **Balthasar Brendtke** (kurz: E.) unter Anführung  der erforderlichen Daten als jene Person, die das ihr von der Zulassungsbesitzerin des näher  bezeichneten Fahrzeuges zur Verfügung gestellte Fahrzeug einem Dritten überlassen habe,  gemäß § 2 Wiener Parkometergesetz 2006 zur Lenkerauskunft binnen zwei Wochen ab  Zustellung des Schreibens aufgefordert.

- missed: `Balthasar Brendtke` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143518.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Marlene Halberschmidt  betreffend den Antrag der **Karim Haaff**, KLG Gartenfreunde Pottendorf 2, 3073 Hendelgraben, Österreich,   auf Gewährung der Verfahrenshilfe gemäß § 292 BAO im Beschwerdeverfahren zum Bescheid  des Finanzamt Linz  vom 12.06.2023 hinsichtlich Rückforderung vonFamilienbeihilfe und  Kinderabsetzbetrag für ihre vier Kinder für den Monat 07/2018 und den Zeitraum 04/2019- 08/2020   beschlossen:   Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

- missed: `Karim Haaff` (person)
- predicted in sentence: `Mag.a Marlene Halberschmidt`

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_34`)

Mit Lenkerauskunft des rechtsfreundlichen Vertreters der Zulassungsbesitzerin vom  1) 12.05.2020, 2) bis 5) 26.03.2020 und 6) 20.03.2020 wurde mitgeteilt, dass Verantwortlicher  für das Taxi- und Mietwagengewerbe Herr **Russbüldt**  geb. Herrgeb, AdrHerr, sei.

- missed: `Russbüldt` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142502.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Priv.-Doz.in Gloria Rejngardt**   in der Beschwerdesache des Estelle Klaffer, Moosscheibe 14, 4942 Außerguggenberg, Österreich,   betreffend den Bescheid des Finanzamt Schwechat Gerasdorf  vom 24. März 2020   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2019, Steuernummer  88-435/1011,   zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Priv.-Doz.in Gloria Rejngardt` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_94`)

13.01.2022**:Sascha Reink**  AM und Orthopädin: SV-GA FLAG: Anamnese: Seit der Geburt besteht eine  Blindheit bds.

- missed: `:Sascha Reink` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_148`)

2020-10 **Mike Staengel**  praktischer Arzt: seit Geburt Zeichen eines Aspergersyndroms mit thera- pieresistenten Schlafstörungen, Ruhelosigkeit, stereotypen Bewegungen (Stampfen mit dem  Fuß), Rückzug in eine eigene Welt, was im Kindergarten und in der Schule aufgefallen ist.

- missed: `Mike Staengel` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_2`)

Jeffrey Marinopoulos, Moosbauernstraße 12, 9341 Wattein, Österreich, als atypisch still Beteiligte an der vormaligen **Leroy Kusznierz**,  vertreten durch Prof. Thomas Keppert Steuerberatung und Wirtschaftsprüfung GmbH,  Theobaldgasse 19, 1060 Wien,  über die Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Klagenfurt vom  24. April 2012 die Wiederaufnahme des Verfahrens die Feststellung von Einkünften und die  Feststellung von Einkünften gemäß § 188 BAO betreffend, je für das Jahr 2007, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_86`)

(Lt. Auskunft von **M.M.A.** schlafe  der Sohn wegen eines Streits mit seiner Schwester in dieser Wohnung).

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_175`)

Die bei **Magdalena Rönecke**  als Zentralinstitut zu haltende Liquiditätsreserve speist sich aber zum Teil aus von  derBeschwerdeführerin gehaltenen gesicherten bzw gedeckten Einlagen.

- missed: `Magdalena Rönecke` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_51`)

Anlässlich einer Besprechung mit dem Prüfer am 22.05.2018 wurde von dem zwischenzeitlich  von S. beauftragten Wirtschaftsprüfer und Steuerberater **Ida Katenstroth** (Kanzlei L. in L.) die Auffassung  vertreten, dass von zwei einzelnen Lieferungen und nicht von einem Reihengeschäft  auszugehen sei.

- missed: `Ida Katenstroth` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Markus Knechtl LL.M.** in der  Beschwerdesache Leopold Dobertin, Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich, über die Beschwerden gegen Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg   vom 30. Oktober 2015 gegen den Bescheid vom 9. Oktober 2015 betreffend Festsetzung von  zweiten Säumniszuschlägen,  vom 2. März 2016 gegen den Bescheid vom 11. Jänner 2016 betreffend Festsetzung von dritten  Säumniszuschlägen und  vom 2.1.2020 gegen den Bescheid vom 13.12.2019 betreffend Aufhebung/Abänderung von  Nebengebühren  nach der am 4.12.2023 am Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO  i.V.m. § 274 Abs. 1 Z 1 BAO) in Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und  in Anwesenheit von Mag. Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte  Behörde durchgeführten mündlichen Verhandlung zur Steuernummer 38-992/7403  zu  Recht erkannt:   I. Der Beschwerde vom 30.10.2015 wird teilweise Folge gegeben und zweite  Säumniszuschläge in Höhe von 5.739,66 € festgesetzt.

- missed: `Mag. Markus Knechtl LL.M.` (person)
- predicted in sentence: `Mag. Markus Knechtl`, `Leopold Dobertin`, `Mag. Martin Holzapfel`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `Mag. Ulrike Nussbaumer`, `Chiara Duchan`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_5`)

Die **Tamara Gottschalch**  ist Gruppenmitglied.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_4`)

Entscheidungsgründe      Verfahrensgang  **Theodor Strohmeier**, in der Folge kurz mit Bf. bezeichnet, ist tschechische Staatsangehörige.

- missed: `Theodor Strohmeier` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_193`)

 eine Zusammenschlussbilanz der „**Uwe Gudian** & atypisch Stille“ mit Werten von Null;

- missed: `Uwe Gudian` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  **Gwendolin Rittmüller**, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Gwendolin Rittmüller` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)

Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr **Albert Sengeisen**  als Machthaber über die Gesellschaft  aufgetreten.

- missed: `Albert Sengeisen` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_13`)

Die Firma1 habe sich bei der Leistungserbringung diverser  Subunternehmer bedient, die wiederum in einem Naheverhältnis zum Kommanditisten bzw.  Komplementär der **Leroy Kusznierz**  gestanden seien.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_167`)

Erst im Vorschulalter fallen Schwierigkeiten auf (u. a.  Kontaktprobleme, wiederkehrende Verhaltensmuster, Missachten von Regeln beim Spielen  etc.) (https://focus-arztsuche.de/magazin/krankheiten/psychische-erkrankungen/was-ist-das- asperger-syndrom-und-wie-erkennt-man-es )  Im Gutachten vom 2. März 2021 stellte **Dr. Dok1**, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest, dies mit der Begründung, dass zwar gutachterliche Diagnosen gestellt  worden seien, jedoch mangels Inanspruchnahme adäquater Therapien, eine, für die  Beurteilung alltagsrelevanter, anhaltender Einschränkungen erforder-liche, ärztliche  Verlaufsdokumentation, nicht vorhanden sei.

- missed: `Dr. Dok1` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_214`)

Das FA hat es unterlassen, den Geschäftsführer der bf. GmbH und der Mieterin **Linn Brümmer** IE,   PLZ1 Stadt1, Straße 3 3, als Zeugen zu befragen, ob das im Juni 2017 verkaufte Haus mit der  Anlagennummer Anlagennummer1-0, das Ende Juni 2017 im Musterhauspark „UX Teich1“,  PLZ5 Stadt7 (die Adresse desselben Musterhausparks wird im Allgemeinen auch als PLZ4 Stadt6  15 von 29 Seite 16 von 29

- missed: `Linn Brümmer` (person)
- predicted in sentence: —

</details>

---

