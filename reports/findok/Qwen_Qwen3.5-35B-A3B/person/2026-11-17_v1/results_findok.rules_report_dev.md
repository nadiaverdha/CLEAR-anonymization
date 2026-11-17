# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-17T13:25:02.425921

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-17_v1/config.yaml 
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
| Validation sentences | 2501 |
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
| Accuracy (exact match) | 97.9% |
| True Positives | 898 |
| False Positives | 819 |
| False Negatives | 953 |
| Total Gold Entities | 1851 |
| Micro Precision | 52.3% |
| Micro Recall | 48.5% |
| Micro F1 | 50.3% |
| Macro F1 | 50.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Names in Legal Context (Complainant/Respondent) with Suffixes` | 27.5% | 76.4% | 16.7% | 406 | 310 | 96 |
| `Legal Titles with Full Names` | 33.5% | 73.6% | 21.7% | 545 | 401 | 144 |
| `Standalone Surnames in Narrative` | 10.9% | 60.7% | 6.0% | 183 | 111 | 72 |
| `Names after 'vertreten durch' (Tightened)` | 1.8% | 48.6% | 0.9% | 35 | 17 | 18 |
| `Frau Preceded Names with Suffixes` | 1.1% | 30.3% | 0.5% | 33 | 10 | 23 |
| `Ing. and Specialized Titles with Names` | 2.6% | 25.5% | 1.4% | 98 | 25 | 73 |
| `Standalone Names in Context (von ... von)` | 0.3% | 15.8% | 0.2% | 19 | 3 | 16 |
| `Anonymized Initials with Title (Fixed)` | 1.9% | 9.8% | 1.1% | 204 | 20 | 184 |
| `Case Citation Surnames` | 0.1% | 1.4% | 0.1% | 73 | 1 | 72 |
| `Role Indicators (Richter/Richterin)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names in Parentheses/Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gesellschafter Full Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Richter Title Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `N.N. Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr.in with Placeholder Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after Hinsichtlich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names after Preposition 'bei' (Tightened)` | 0.0% | 0.0% | 0.0% | 70 | 0 | 70 |
| `Names after Company Prefix 'Fa.' (Tightened)` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Names in Parentheses/Context (Fixed)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complex Academic Titles with Spacing` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Richter Title Names (Concatenated)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Names with Suffixes in Legal Context (Fixed)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone Names in Narrative Context` | 0.0% | 0.0% | 0.0% | 41 | 0 | 41 |
| `Names after Specific Verbs/Contexts (Beschuldigter/Stellungnahme)` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Gutachten von Names` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Names in Legal Context (Complainant/Respondent) with Suffixes` 🏆

**F1:** 0.275 | **Precision:** 0.764 | **Recall:** 0.167  

**Format:** `regex`  
**Rule ID:** `b35975d7`  
**Description:**
Matches full names following 'in der Beschwerdesache' or similar legal contexts, capturing suffixes like LL.M., MBA, Bakk. techn., while explicitly excluding company names (GmbH, AG) and locations.

**Content:**
```
(?:in\s+der\s+Beschwerdesache(?:\s+(?:der|des))?\s+|des\s+)([A-Z][a-z\u00c0-\u00ff]+(?:[ -][A-Z][a-z\u00c0-\u00ff]+)+)(?:,?\s*(?:LL\.M|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MAS|Bakk\. rer\. nat|Bakk\. art\. BEd|BEd\. phil|Bakk\. iur|Bakk\. techn)?)?(?=,|$|[,.](?!.*(?:Straße|Gasse|Platz|Weg|Avenue|Landstraße|Finanzamt|GmbH|AG|Gesellschaft|m\.b\.H)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.764 | 0.167 | 0.275 | 406 | 310 | 96 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 310 | 96 | 1541 |

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

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Reneé Dreyssig` | `Reneé Dreyssig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Mag. Manfred Frühwirth` (person)
- `Finanzamtes Linz` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Pawils` | `Florentin Pawils` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Alva Jodgalweit` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130771.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130771.1_2`)


Das Bundesfinanzgericht hat durch die RichterinR über die Beschwerde des Rosalia Schmieter, Collmannstraße 3, 3335 Lindau, Österreich  vom 22. September 2020, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. September 2020, Zl. Zahl, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, Amtsblatt der Stadt Wien Nr. 51/2005,idgF,  iVm § 4 Abs. 1 Parkometergesetz 2006, Landesgesetzblatt Nr. 9/2006 idF LGBl für Wien Nr.  24/2012, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Rosalia Schmieter` | `Rosalia Schmieter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Collmannstraße 3, 3335 Lindau, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Jaden Holzfuss` | `Jaden Holzfuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Puntigam` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Klocksin` | `Gregor Klocksin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Unterguntschach 85, 3525 Armschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Morgenbesser` | `Karl Morgenbesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Susette Glaeßel` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Harald Schwalbach` | `Harald Schwalbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Frauke Galleithner` | `Frauke Galleithner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132532.1_2`)


über die Beschwerde des Louisa Kannengiser, Pfaffensteig 10, 3595 Atzelsdorf, Österreich, vom 15. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 9. März 2021, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016 in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise Folge gegeben als die von der belangten Behörde mit € 60,00 verhängte Geldstrafe  auf € 48,00 und die für den Fall der Uneinbringlichkeit mit 14 Stunden verhängte Ersatzfrei- heitsstrafe auf 10 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Louisa Kannengiser` | `Louisa Kannengiser` |

**Missed by this rule (FN):**

- `Pfaffensteig 10, 3595 Atzelsdorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter über die Beschwerde des Ivan Thöner, Landlerweg 28, 4273 Kaltenberg, Österreich, vom 7. April 2021 gegen das Straferkenntnis des Magistrates der Stadt Wien vom 25.  Februar 2021, Zahl MA67/Zahl/2020,  betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  46/2016 in Verbindung mit § 4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, den Beschluss gefasst:  Die Beschwerde vom 7. April 2021 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ivan Thöner` | `Ivan Thöner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Landlerweg 28, 4273 Kaltenberg, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

| Predicted | Gold |
|---|---|
| `Dora Szczepanowski` | `Dora Szczepanowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich` (address)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Hilde Schorpp, Wandschaml 94, 4625 Grub, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 21. Dezember 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung der Rechtsvorschrift des § 2 in Verbindung mit § 4 Abs. 2  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 2 VStG eingestellt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Hilde Schorpp` | `Hilde Schorpp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Wandschaml 94, 4625 Grub, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_3`)


über die Beschwerde des Ludmilla Czimmerninks,  Sennemahd 7, 9832 Latzendorf, Österreich, vom 30. Juni 2021, gegen den Bescheid des Magistrates der Stadt Wien,  Magistratsabteilung 6, vom 7. Juni 2021, GZ. MA67/Zahl/2020, betreffend Abweisung des  Antrages vom 14. Mai 2021 auf Bewilligung eines Zahlungsaufschubes bzw. Ratenansuchens,  nach Durchführung einer mündlichen Verhandlung am 2. September 2021, in Anwesenheit des  Beschwerdeführers und der Schriftführerin IP, zu Recht erkannt:  Die Beschwerde wird gemäß § 50 VwGVG als unbegründet abgewiesen und der ange- fochtene Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Ludmilla Czimmerninks` | `Ludmilla Czimmerninks` |

**Missed by this rule (FN):**

- `Sennemahd 7, 9832 Latzendorf, Österreich` (address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 6` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_47`)


II. Das Bundesfinanzgericht hat erwogen: 1. Feststellungen Auf Basis des oben geschilderten Verwaltungsgeschehens und der aktenkundigen Unterlagen wird folgender entscheidungswesentlicher Sachverhalt festgestellt: Die 1998 geborene und im streitgegenständlichen Zeitraum somit bereits volljährige Tochter der Beschwerdeführerin wiederholte vom 12.9.2016 bis 28.4.2017 die 8. Klasse des Bundes-Oberstufenrealgymnasiums Jungroith.

**False Positives:**

- `Bundes-Oberstufenrealgymnasiums Jungroith` — partial — gold is substring of pred: `Jungroith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Jungroith`(city)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

**False Positives:**

- `Beschwerdeführers Jeannette Neuschwender` — partial — gold is substring of pred: `Jeannette Neuschwender`
- `Finanzamtes Salzburg-Land` — type mismatch — same span as gold: `Finanzamtes Salzburg-Land`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Jeannette Neuschwender`(person)
- `Zum Kogl 12, 4441 Penz, Österreich`(address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Peter Staudinger`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_100`)


Nach Z 1 lit. i des Beschlusses Nr. F1 vom 12.09.2009 zur Auslegung des Art. 68 der Verordnung  (EG) Nr. 883/2004 werden für Zwecke vorstehenden Artikels Ansprüche auf Familienleistungen  auch dann als „durch eine Beschäftigung oder eine selbständige Erwerbstätigkeit ausgelöst“,  wenn sie erworben wurden unter anderem wegen Arbeitslosigkeit solange Arbeitsentgelt in  Zusammenhang mit diesem Versicherungsfall zu zahlen ist.

**False Positives:**

- `Beschlusses Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_94`)


Die jüngere Rechtsprechung des Europäischen Gerichtshofs, für die EuGH 25.7.2018, Rs C- 140/17, Gmina Ryjewo, ins Treffen geführt wird, stellt klar, dass eine Einrichtung des  öffentlichen Rechts ein Recht auf Berichtigung der auf eine als Investitionsgut erworbene  Immobilie entrichteten Vorsteuer in Anspruch nehmen kann, wenn der Gegenstand beim  Erwerb sowohl für besteuerte als auch für nicht besteuerte Tätigkeiten verwendet werden  konnte.

**False Positives:**

- `Europäischen Gerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_33`)


Gemäß § 33 Abs. 3a Z 3 EStG 1988 ist der Familienbonus Plus in der Veranlagung (=im  Einkommensteuerbescheid) entsprechend der Antragstellung durch den Steuerpflichtigen zu  berücksichtigen, wobei gemäß lit. b für ein Kind, für das – wie hier – ein Unterhaltsabsetz- betrag gemäß § 33 Abs. 4 Z 3 EStG 1988 zusteht, folgende zwei Varianten möglich sind:  - (Variante 1) beim Familienbeihilfenberechtigten (idR Kindesmutter) oder beim  Unterhaltsleistenden (idR Kindesvater) mit Anspruch auf den Unterhaltsabsetzbetrag der ganze  Familienbonus Plus;  - (Variante 2) beim Familienbeihilfenberechtigten und beim Unterhaltsleistenden mit Anspruch  auf den Unterhaltsabsetzbetrag jeweils die Hälfte des Familienbonus Plus.

**False Positives:**

- `Familienbonus Plus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Neunkirchen Wr` — partial — pred is substring of gold: `Finanzamtes Neunkirchen Wr. Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Sean Herdling`(person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich`(address)
- `NÖ Landesverein für Erwachsenenschutz`(organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

**False Positives:**

- `Herrn Raimund Ladwig` — partial — gold is substring of pred: `Raimund Ladwig`
- `Finanzamtes Bruck Eisenstadt Oberwart` — type mismatch — same span as gold: `Finanzamtes Bruck Eisenstadt Oberwart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Raimund Ladwig`(person)
- `Birkenring 18, 8451 Pernitsch, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Raimund Diedering` — partial — pred is substring of gold: `Raimund Diedering, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Lilienfeld St` — partial — pred is substring of gold: `Finanzamtes Lilienfeld St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich`(address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `73-948/8864`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133681.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133681.1_40`)


I.2. Beschwerdeverfahren  Mit Schreiben vom 13.12.2012 erhob die steuerliche Vertretung des Beschwerdeführers  hinsichtlich der Tz 2 (Vermietung Stallungen) und Tz 5 (Liebhabereivermutung) des  Betriebsprüfungsberichts Beschwerde.

**False Positives:**

- `Betriebsprüfungsberichts Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_371`)


Darin wurde unter Tz 1 im Wesentlichen festgehalten, dass im Zuge von  Ermittlungen des Zollamts St. Pölten, Wr. Neustadt für die Monate August bis Dezember 2013  festgestellt wurde, dass das geprüfte Unternehmen rund 2,5 Mio Liter Diesel von der Fa. J.  Slovenska bezogen und weiterveräußert hat.

**False Positives:**

- `Zollamts St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_436`)


II. Das Bundesfinanzgericht hat erwogen:  1.Wiederaufnahme der Verfahren betreffend Umsatz- und Körperschaftsteuer 2013:  Mit den angefochtenen Bescheiden verfügte die belangte Behörde – in Anlehnung an die  Außenprüfung- die Wiederaufnahme der Verfahren betreffend Umsatz- und  Körperschaftsteuer für das Jahr 2013 aufgrund der Feststellungen in Tz 16-18 des Bp-Berichtes.

**False Positives:**

- `Bp-Berichtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

## `Legal Titles with Full Names` 🏆

**F1:** 0.335 | **Precision:** 0.736 | **Recall:** 0.217  

**Format:** `regex`  
**Rule ID:** `fb1bfea3`  
**Description:**
Matches persons with titles (Dr., Mag., Hon.-Prof., etc.) followed by full names, ensuring multiple titles and suffixes are captured correctly, including cases where title and name are concatenated (e.g., Mag.Dr.).

**Content:**
```
(?:HR|MMag\.|Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Univ\.-Prof\.|Priv\.-Doz\.in?|Priv\.-Doz\.|Hon\.-Prof\.|Hon\.-Prof\.in?|DDr\.in?|RgR|StR|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)(?:\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.|Hon\.-Prof\.in?|DDr\.in?))*\s*[A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+(?:von\s+der\s+|von\s+dem\s+)?[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB(?!.*LLB)|BEd(?!.*BEd)|B\.K(?!.*BK)|Dipl\.Kfm(?!.*Kfm)|MA(?!.*MA)|MBA(?!.*MBA)|MSc(?!.*MSc)|MAS(?!.*MAS)|Bakk\. rer\. nat(?!.*nat)|Bakk\. art\. BEd(?!.*BEd)))?(?=\s|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.736 | 0.217 | 0.335 | 545 | 401 | 144 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 401 | 144 | 1450 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |
| `Mag. Michael Franz` | `Mag. Michael Franz` |
| `Mag. Franz Josef Großin` | `Mag. Franz Josef Großin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alexander Hajicek` (person)
- `Finanzamtes Baden Mödling` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_20`)


Seite 3 von 15 Erst anlässlich der mit Bericht vom 27.12.2010 abgeschlossenen Betriebsprüfung wurde die Ungewissheit, ob Liebhaberei im Zusammenhang mit der Vermietung des Objektes in Univ.-Prof.in Miriam Ungruh  vorliegt, beseitigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_69`)


Die ersten Monate bis zur Erlangung der Aufenthalts- und Arbeitsbewilligung für Russland und bis mein Büro bei AG Russland und meine Dienstwohnung bezugsbereit waren, habe ich ausschließlich von Univ.-Prof.in Miriam Ungruh  aus gearbeitet.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_74`)


Sie haben mit mir in Univ.-Prof.in Miriam Ungruh  deren Strategie und Marktauftritt in Russland besprochen (z.B. DivFirmen DivFirmen uvm.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_75`)


o Ich habe russische Kunden, die Wien besuchten, von Univ.-Prof.in Miriam Ungruh  aus betreut;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_76`)


sie nach Univ.-Prof.in Miriam Ungruh  zu Besprechungen und Workshops eingeladen (z.B. DivFirmen DivFirmen; uvm.) o In allen Fällen war ausschlaggebend, dass ich in Univ.-Prof.in Miriam Ungruh (Österreich) für „Westler“ leichter erreichbar war, ohne dass die Leute ein Visum besorgen und den teuren Aufenthalt in Moskau bezahlen mussten, um mich zu sehen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_81`)


o Um mir diese Arbeit in Univ.-Prof.in Miriam Ungruh  und in Österreich zu erleichtern, teilte mir AG zwei Dienstwägen zu: einen in Univ.-Prof.in Miriam Ungruh  und einen in Moskau. In Russland war ich ebenfalls rund um die Uhr im Einsatz: 14 Büros, 14 direkt berichtende Manager, 1200 Mitarbeiter, eine Forschungsstätte, eine PC Fabrik und diverse zusätzliche Infrastruktur wie Service Center, 2000 Partner Firmen, Partnerschaften mit über 100 Universitäten und über 2 Millionen Kunden im Jahr müssen eben betreut werden.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)


Das Büro in Univ.-Prof.in Miriam Ungruh  war auch im Interesse meines Arbeitgebers.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Mirha Karahodzic MA` | `Mag. Mirha Karahodzic MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elisabeth Schafstall` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Dietlind Mahlstädt` | `Dr.in Dietlind Mahlstädt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kai Pipers` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache der [...], [...], vertreten durch Vertr., Adr.V., über die Beschwerde vom  11.7.2018  gegen den Bescheid des Finanzamtes Wien 1/23 vom 12. Juni 2018, betreffend  Abweisung des Antrags (vom 21.3.2018) auf Familienbeihilfe (für die im Oktober 1989  geborene Jana Papenkord) für den Zeitraum von Jänner 2011 bis Februar 2013 sowie ab März 2013,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Jana Papenkord` (person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `Mag. Manfred Frühwirth` | `Mag. Manfred Frühwirth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Mag. Judith Daniela Herdin-Winter` | `Mag. Judith Daniela Herdin-Winter` |
| `Dr.in Laurin Morgenschweis` | `Dr.in Laurin Morgenschweis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich` (address)
- `Fatima Beringschmidt` (person)
- `Finanzamtes Waldviertel` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag.a Univ.-Prof.in Ada Schaeferlein` | `Mag.a Univ.-Prof.in Ada Schaeferlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leroy Sitterle` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |
| `Univ.-Prof.in Shoshana Leuther` | `Univ.-Prof.in Shoshana Leuther` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `HR OSR Leonie Ercklentz` | `HR OSR Leonie Ercklentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Karnitzen 135, 9635 Kronhof, Österreich` (address)
- `LKP Steuerberatung OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rosamunde Galanidis` | `Priv.-Doz.in Rosamunde Galanidis` |
| `Mag. Wolfgang Moser` | `Mag. Wolfgang Moser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Elias Voht` | `VetR Elias Voht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Zarin Eckartz` | `Priv.-Doz.in Zarin Eckartz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Volkmar Oortwyn` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Melina Bankratz` | `Priv.-Doz.in Melina Bankratz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lars Huesgen` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Belinda  Maria Eder` | `Mag. Belinda  Maria Eder` |
| `Mag. Katharina Moravec` | `Mag. Katharina Moravec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Dr. Wolfgang Aigner` (person)
- `Erwin Agneter` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Mirha Karahodzic MA` | `Mag. Mirha Karahodzic MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Schoenrock, LLM` (person)
- `Hochscharten 126D, 5122 Dorfen, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `06-88-920/2630` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Franz Glashüttner` | `Mag. Franz Glashüttner` |
| `Mag. Bruno  Sundl` | `Mag. Bruno  Sundl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Rauscher` (person)
- `Dr. Christian Haid` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |
| `OMedR Ottfried Theißl` | `OMedR Ottfried Theißl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Tamara Steinmüller` | `Mag.a Tamara Steinmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gueldner Garten` (organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Burkhard Krautschenko` | `VetR Burkhard Krautschenko` |
| `Mag. Susanne Pöltenstein-Rosenegger` | `Mag. Susanne Pöltenstein-Rosenegger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Joachim Annanias` (person)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Puntigam` | `Mag. Manuela Puntigam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Holzfuss` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `KzlR Diethard Ringhand` | `KzlR Diethard Ringhand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_55`)


Handschriftlich war darauf vermerkt „Bestätigung durch Frau E, Exfrau des Bf. und  Mutter der beiden unterhaltspflichtigen Kinder K1 und K2: Hiermit erkläre ich, dass mein  Exmann KzlR Diethard Ringhand  zu allen o.g.

| Predicted | Gold |
|---|---|
| `KzlR Diethard Ringhand` | `KzlR Diethard Ringhand` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Ladwig` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dr.in Bianca Gerasimczuk` | `Priv.-Doz.in Dr.in Bianca Gerasimczuk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Diedering, Bakk. iur.` (person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marceline Flory` | `Univ.-Prof.in Marceline Flory` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Zeitlhuber` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Susette Glaeßel` | `Mag.a Susette Glaeßel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl Morgenbesser` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |
| `Hon.-Prof.in Elvira Thielsen` | `Hon.-Prof.in Elvira Thielsen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Edith Schifferdecker` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` | `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` |
| `OMedR Leonhard Hestermeyer` | `OMedR Leonhard Hestermeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `52-932/8889` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Müller-Dobler MBA MSc` | `Mag. Andrea Müller-Dobler MBA MSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timon Thoennißen` (person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich` (address)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

| Predicted | Gold |
|---|---|
| `Mag. Andrea Müller-Dobler MBA MSc` | `Mag. Andrea Müller-Dobler MBA MSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Evelyn Antwerber` (person)
- `Hertzstraße 25, 5134 Spieglern, Österreich` (address)
- `Dr. Farid Rifaad` (person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |
| `StR Milena Neidig` | `StR Milena Neidig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Laurence Vasylenko  in der Beschwerdesache X, Adresse,  über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Umgebung  vom 13. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 02-410/2351  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hon.-Prof.in Laurence Vasylenko` | `Dr.in Hon.-Prof.in Laurence Vasylenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Graz` (organisation)
- `02-410/2351` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. René Neuendorf` | `Univ.-Prof. René Neuendorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kevin Damiani` (person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Robert Dax` | `Mag. Robert Dax` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Maximowa` (person)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Mag.Dr` — partial — pred is substring of gold: `Mag.Dr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

**False Positives:**

- `BARUNG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `James Hainig`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.DDr. Hedwig Bavenek-Weber in der  Beschwerdesache Merlin Feucht, Alte Straße 2, 8114 Unterfriesach, Österreich, über die Beschwerde vom 12. Dezember 2011  gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14.  November 2011, Steuernummer 57-396/6782, betreffend die Festsetzung der ermäßigten  Glücksspielabgabe gemäß § 58 Abs. 3 GSpG für Glücksspiele im Rahmen von Gewinnspielen  (Preisausschreiben), zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.DDr` — partial — pred is substring of gold: `Mag.DDr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.DDr. Hedwig Bavenek-Weber`(person)
- `Merlin Feucht`(person)
- `Alte Straße 2, 8114 Unterfriesach, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `57-396/6782`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_422`)


Dieses Schreiben wird für alle FAHRZEUGMARKE in Familienbesitz genutzt, wenn  sich diese in Reparatur befinden (beiliegendes Foto).

**False Positives:**

- `HRZEUGMARKE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_425`)


Beigelegt waren das unten angeführte Schreiben und ein Foto von sechs  MARKENFAHRZEUGEN, welche auf einer Wiese abgestellt waren.

**False Positives:**

- `HRZEUGEN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_445`)


Aus den vorgelegten Akten ist ersichtlich, dass VN4 NN mit Bescheid vom 7.9.2016 für das  Kraftfahrzeug mit dem Kennzeichen KENNZ2, Type: FAHRZEUGMARKE, in der Zeit vom  1.10.2016 bis 30.9.2018 eine Ausnahmebewilligung für den 4./5.

**False Positives:**

- `HRZEUGMARKE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv.-Doz. Dipl` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Priv.-Doz. Dipl` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Hon.-Prof. Thassilo Schoenrock` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Schoenrock, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Mag. Ulrike Nussbaumer LL` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `StR Univ` — partial — pred is substring of gold: `StR Univ.-Prof. Alvin Paulikat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `StR Univ.-Prof. Alvin Paulikat`(person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich`(address)
- `Dr Christian Burghardt`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer LL` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_35`)


Von einer ursprünglich geplanten Streichung der in den Rechnungen der Möbel Zorkelglanz GmbH  ausgewiesenen Vorsteuern wurde unter Hinweis auf Rz. 1825 UStR Abstand genommen.

**False Positives:**

- `StR Abstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_206`)


(UStR Rz 794; Ruppe/Achatz, UStG 5, § 6, TZ 249/6).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_210`)


Im ersteren  Fall müsste der Land- und Forstwirt, der den Grundstücksumsatz als steuerpflichtig behandeln  möchte, zunächst nach § 22 Abs. 6 für Regelbesteuerung optieren (UStR Rz 794).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `OMedR Prof` — partial — pred is substring of gold: `OMedR Prof. Hartmut Szardemings`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Zoltan Dabrowski`(person)
- `OMedR Prof. Hartmut Szardemings`(person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_109`)


Im Erkenntnis  heißt es wie folgt: „Da die Beschwerdeführerin somit nach nationalen Regelungen im Streitjahr  in der Schweiz nicht unbeschränkt steuerpflichtig, sondern nur quellensteuerpflichtig war, gilt  sie nicht als in der Schweiz ansässig im Sinne des DBA CH.“

**False Positives:**

- `BA CH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_275`)


Demnach ist nach Art. 4 Abs. 2 lit. a DBA CH als erstes Kriterium zu prüfen:   In welchem Staat hatte die Bf. in den Jahren 2011 und 2012 eine „ständige Wohnstätte“ (Art.  4 Abs. 2 lit. a DBA CH)?

**False Positives:**

- `BA CH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_321`)


Zum Begehren der Bf. auf Durchführung eines Verständigungsverfahrens darf noch  angemerkt werden:  Ein solches ist im Art. 4 Abs. 2 lit. d DBA CH vorgesehen.

**False Positives:**

- `BA CH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_34`)


Die Rechtsmittel und anderen Eingaben enthalten keine Auflistung der dem BASB anlässlich  der Begutachtung vorgelegten oder der den Schriftsätzen beigelegten Befunde und  Unterlagen.

**False Positives:**

- `BASB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_215`)


Es obliegt somit den  Beihilfenbehörden, dem BASB den maßgeblichen Zeitpunkt anlässlich der  Gutachtensanforderung mitzuteilen.

**False Positives:**

- `BASB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

**False Positives:**

- `Mag. Markus Knechtl LL` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Dora Szczepanowski`(person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich`(address)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_99`)


Im Beschwerdefall kam es zu keinem Rückfall des nach Artikel 15 Abs. 1 DBA Frankreich  zugewiesenen Besteuerungsrechts an den Ansässigkeitsstaat Österreich, weil der Bf. in allen  den Jahren 2015 bis 2017 an mehr als an 183 Tagen in Frankreich tätig war und zudem die  Vergütungen von einer Arbeitgeberin (die Holz Nexglanz AG) in ausbezahlt wurden, die in  Frankreich ansässig ist.

**False Positives:**

- `BA Frankreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Holz Nexglanz AG`(organisation)

</details>

---

## `Standalone Surnames in Narrative` 🏆

**F1:** 0.109 | **Precision:** 0.607 | **Recall:** 0.060  

**Format:** `regex`  
**Rule ID:** `b7143f86`  
**Description:**
Matches standalone surnames in narrative contexts where they appear as subjects or objects, specifically targeting cases like 'Frau Ekardt' or 'Karsten Sofka' that were missed. Requires a space after the first word to avoid cutting multi-word names.

**Content:**
```
(?:Frau|Herrn?)\s+([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:\s+[A-Z][a-zA-Z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.607 | 0.060 | 0.109 | 183 | 111 | 72 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 111 | 72 | 1740 |

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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_71`)


…“ Auch ein  Passus im vorgelegten TÜV-Bericht über den Prüftermin am 24.6.2019 steht damit in Einklang:  „Sehr geehrter Herr Volchert  an Ihrem Fahrzeug wurden zum Zeitpunkt der Untersuchung keine  Mängel festgestellt. …“.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_98`)


Z1 wurde laut der vorgelegten Protokollsabschrift am 11.6.2018 an der Polizeiinspektion  d_Ort_1 vernommen und gab unter anderem an: „Seit Mitte dem Jahr 2016 bin ich als  Steuerberater für …Herrn Volchert tätig.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_99`)


…Herr Volchert ist hauptberuflich Angestellter der AG in d_Ort_2.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_105`)


Herr Eugen Volchert  ist polizeilich in der Adr, Plz_1  d_Ort_1 gemeldet und deshalb ist sein Fahrzeug auch in d_Ort_1 zugelassen.

| Predicted | Gold |
|---|---|
| `Eugen Volchert` | `Eugen Volchert` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)


12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr Aldewereld von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

| Predicted | Gold |
|---|---|
| `Aldewereld` | `Aldewereld` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_69`)


Herr Frikel ist ebenso Gesellschafter.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_71`)


Im Rahmen der Firmengründung wurde von Herrn Frikel ein  Fahrzeug als sein Beitrag bzw. als Einlage eingebracht.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_73`)


Dieses Kfz wurde von Herrn Frikel selber angeschafft, wo und zu welchen  Bedingungen kann ich nicht angeben.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_75`)


Ich selber war dann in der Folge mehrmals in Österreich bei Herrn Frikel  wenn ich  mit dem Flugzeug anreiste, konnte ich dann den Audi verwenden (so ca. 15 mal pro Jahr) und  damit Kundenbesuche etc. erledigen.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_80`)


Die Bilanz für 2010 ist noch nicht  erstellt. In Deutschland an meinem Wohnsitz bzw. am Firmensitz konnte ich somit nicht  permanent über das KFZ Audi A6 verfügen, es befand sich des öfteren im Besitz des Herrn Frikel in  A/Adr1 und somit an diesem Standort.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_84`)


Prima Abo 10,00  Gesamt 431,27  Arbeitsmittel:  1. 1. CD Herr Riese und sein Garten 21,00  5 von 26 Seite 6 von 26

| Predicted | Gold |
|---|---|
| `Riese` | `Riese` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)


Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr Albert Sengeisen  als Machthaber über die Gesellschaft  aufgetreten.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Habdank` | `Bernhard Habdank` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_37`)


1) Mit Schreiben vom 13.05.2020 wurde von Herrn Angelstein mitgeteilt, dass er weder  Geschäftsführer der Firma sei noch mit dem Fahrzeug gefahren sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_38`)


Mit Schreiben vom 02.06.2020 wurde durch die Rechtsanwälte des Herrn Angelstein mitgeteilt, dass  dieser keine Lenkerauskunft erteilen könne, da er lediglich für das Fahrzeug mit dem amtlichen  Kennzeichen Auto3 (Anmerkung BFG: nicht gegenständlich) verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_50`)


Mit Schreiben vom 04.06.2020 teilte die rechtsfreundliche Vertretung des Herrn Angelstein  mit, dass der Genannte über das gegenständliche Fahrzeug zum Beanstandungszeitpunkt nicht  verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_51`)


Mit Schreiben vom 18.06.2020 wurde die Zulassungsbesitzerin des gegenständlichen  Fahrzeuges aufgefordert die erteilte Lenkerauskunft durch Vorlage entsprechender  Beweismittel (Unterlagen über die Bestellung des Herrn Angelstein als verantwortlicher Beauftragter  gemäß § 9 Abs. 2 Verwaltungsstrafgesetz 1991) glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_57`)


In der E-Mail Ihres rechtsfreundlichen Vertreters vom 01.10.2020 wurde zum gegenständlich  angelasteten Sachverhalt vorgebracht, die Zulassungsbesitzerin und deren handelsrechtliches  Organ habe der Aufforderung der Behörde zur Lenkerauskunft gesetzestreu entsprochen, zumal  dargelegt worden sei, dass die verlangte Auskunft von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030  Wien, als Verantwortlicher gemäß § 9 VStG erteilt werden könne.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_60`)


Weiters  wurde die Herbeischaffung des Aktes der WKStA zur AZ: AktWKStA, dessen Inhalt die  Übertragung der Meldepflicht gemäß § 9 VStG auf Herrn Angelstein beweisen soll, beantragt.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)
- `Dr.in Ing. Viktoria Weigart` (person)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_154`)


In Beantwortung der nunmehr an Herrn Angelstein gerichteten (sechs) Lenkererhebungen der  belangten Behörde bestritt dieser seine Auskunftspflicht mit den Worten   1) bis 5) „dass ich weder ein Geschäftsführer dieser Firma noch mit diesem Fahrzeug gefahren  bin.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)


6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn Angelstein angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_174`)


3. Zulässigkeit des Einspruches:  …  4. Gründe des Einspruches:  Der Vorwurf, der Einschreiter hätte als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin der Firma1 des Fahrzeuges mit dem behördlichen Kennzeichen Auto4  [Anmerkung BFG: nicht gegenständlich] dem ordnungsgemäß zugestellten Verlangen der MA  67 vom 28.01.2020, innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er  dieses Fahrzeug überlassen gehabt hat, sodass dieser zur in der Strafverfügung angegebenen  Tatzeit und Tatort gelenkt hat bzw. vor diesem Zeitpunkt abgestellt hat nicht entsprochen zu  haben und somit die Rechtsvorschriften des § 103 Abs 2 KFG [Anmerkung BFG, gemeint: § 2  (Wiener) Parkometerabgabeverordnung iVm § 4 Abs. 2 Parkometergesetz 2006] trifft nicht zu,  dies aus folgenden Gründen: Es wurde - wie oben erwähnt - vom Einschreiter die Übertragung  der Meldepflicht auf Herrn Angelstein  geb. Herrgeb, übertragen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_191`)


Darin hat die Einschreiterin  und deren handelsrechtliches Organ dargelegt, dass die verlangte Auskunft nicht erteilt werden  kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030 Wien als Verantwortlichen gemäß  § 9 VStG.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_213`)


Darin hat die Einschreiterin und deren handelsrechtliches Organ dargelegt, dass die verlangte  Auskunft nicht erteilt werden kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, als  Verantwortlichen gemäß § 9 VStG.  16 von 22 Seite 17 von 22

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_21`)


Da der Gutachter Herr Karina Burfeindt selber sagte, wenn wir auch einen ärztlichen Befund haben, ändert es die ganzen Prozente,  und das haben wir jetzt.

| Predicted | Gold |
|---|---|
| `Karina Burfeindt` | `Karina Burfeindt` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_24`)


Frau Baues ist die Liquidatorin.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)


Zu den vereinbarten Einkaufskonditionen gab Herr Inn Trikraftglanz  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Borisowa` | `Borisowa` |
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_405`)


Frau Baues als Vertreterin der Beschwerdeführerin gibt bekannt, dass die Diesellieferungen 2 bis 3  Mal pro Woche stattgefunden haben.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_415`)


Die Anfrage beim Finanzamt deute vielmehr darauf hin,  dass Herr Inn Trikraftglanz  selbst Zweifel an der Seriosität der in Rede stehenden Lieferanten gehabt habe  und möglicherweise auch ein Naheverhältnis.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_424`)


Ein Naheverhältnis zwischen Herrn Inn Trikraftglanz und den gegenständlichen  Lieferanten hat es nicht gegeben.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `M.` (person)
- `Finanzamt` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |
| `Baues` | `Baues` |
| `Borisowa` | `Borisowa` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_6`)


Entscheidungsgründe  I. Verfahrensgang  1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Beschwerdeführerin (kurz Bf) ist eine GmbH, deren alleinige Gesellschafterin Frau Schneppensiefen ist.

| Predicted | Gold |
|---|---|
| `Schneppensiefen` | `Schneppensiefen` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Finanzamt Salzburg-Land` (organisation)
- `Finanzamt` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_32`)


In dem eingeleiteten Finanzstrafverfahren wurde Herr Harald Hilderink  jedoch beschuldigt,  vorsätzlich die Abgabe und Zahlung der Umsatzsteuervoranmeldungen unterlassen zu haben  und zu einer Geldstrafe von EUR 10.000,00 verurteilt. Gegen diese Straffestsetzung richtet sich  die vorliegende Beschwerde und geben wir als Begründung an:   Die ARGE wurde von einem Steuerberater vertreten, der mit der Abgabe der  Umsatzsteuervoranmeldungen beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)


Herr Harald Hilderink  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)


 Herr Harald Hilderink  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_38`)


Auf die Einhaltung von Fristen war Herr  Harald Hilderink  daher auf seine steuerliche Vertretung angewiesen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_40`)


Herr Harald Hilderink  ist nicht alleine dafür  verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |
| `Harald Hilderink` | `Harald Hilderink` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)


Da Herr Harald Hilderink  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)


Herr Harald Hilderink  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_81`)


Herr Harald Hilderink  ist verantwortlicher Geschäftsführer der ARGE.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_89`)


Zum Beschwerdevorbringen, „Herr Harald Hilderink  war auf die Einhaltung von Fristen auf seine  steuerliche Vertretung angewiesen, die mit der Abgabe der Umsatzsteuervoranmeldungen  beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_90`)


Herr Sahin konnte daher davon ausgehen, dass alle Meldungen  ordnungsgemäß und fristgerecht abgegeben werden bzw. die verspätete Abgabe der  Umsatzsteuervoranmeldungen war nicht vorsätzlich!

| Predicted | Gold |
|---|---|
| `Sahin` | `Sahin` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_95`)


Herr Harald Hilderink  ist nicht alleine dafür verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_11`)


Unter Bezugnahme auf obige Ausführungen ist festzuhalten, dass Frau Waiser die  exklusive (einzige) Adressatin der Vollstreckungsverfügung vom 18. Mai 2022 ist, die hier aber  von jemandem anderen bekämpft wird.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_65`)


Gleiches trifft auf die Ehegattin des Bf. zu.  Erkrankung der Ehegattin und des Bf.:  Im Vorlageantrag wurde erstmalig vorgebracht, ein Umzug nach Österreich sei nicht möglich,  weil seine Frau Krebs hat;

**False Positives:**

- `Krebs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_34`)


Mit Lenkerauskunft des rechtsfreundlichen Vertreters der Zulassungsbesitzerin vom  1) 12.05.2020, 2) bis 5) 26.03.2020 und 6) 20.03.2020 wurde mitgeteilt, dass Verantwortlicher  für das Taxi- und Mietwagengewerbe Herr Russbüldt  geb. Herrgeb, AdrHerr, sei.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)


Die Auskunft könne Herr Russbüldt als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_36`)


In weiterer Folge wurde Herr Russbüldt von der Behörde angeschrieben und um Bekanntgabe des  Fahrzeuglenkers ersucht.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_40`)


In dem durch Ihren Rechtsvertreter dagegen erhobenen Einspruch wurde im Wesentlichen  eingewendet, dass Herr Russbüldt  geb. Herrgeb, AdrHerr der einzige und alleinige Verantwortliche  4 von 22 Seite 5 von 22

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_53`)


Dagegen erhoben Sie mit E-Mail vom 2) und 6) 31.08.2020, 3) und 4) 07.09.2020, 5) 04.09.2020  Einspruch und wiederholten, dass Herr Russbüldt der verantwortliche Fuhrparkleiter gewesen sei.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_58`)


Zum Beweis dafür wurde ein  Dokument vom 27.11.2018 vorgelegt, worin die Firmen Firma1 und Firma2 vereinbaren, dass Herr Russbüldt als Fuhrparkleiter für beide angeführten Firmen ab dem 01.12.2018 beauftragt wird.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_71`)


Aufgrund der Aktenlage ist daher davon auszugehen, dass Herr Russbüldt nicht verantwortlicher  Beauftragter gemäß § 9 Abs. 2 VStG ist.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelstein`(person)
- `Russbüldt`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_105`)


Darin hat der Beschwerdeführer dargelegt, dass der  Beschwerdeführer die verlangte Auskunft nicht erteilen kann, sondern Herr Russbüldt  geb. Herrgeb,  AdrHerr, Verantwortlicher gemäß § 9 VStG.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_110`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_112`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste  gegen ihn Anzeige erstattet werden.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_117`)


Tatsächlich ist Herr Russbüldt mit Bestellungsurkunde vom 27.11.2018 zum Fuhrparkleiter der  Firma1 und der hier nicht in Rede stehenden Firma2 bestellt worden.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelstein`(person)
- `Russbüldt`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_169`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_171`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste gegen ihn Anzeige erstattet werden.

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

**False Positives:**

- `Russb` — partial — pred is substring of gold: `Russbüldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

**False Positives:**

- `Aron Pommer` — partial — pred is substring of gold: `Aron Pommeränke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)
- `Aron Pommeränke`(person)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)
- `MittelMarine Planung GmbH`(organisation)
- `Logzor-Event GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

**False Positives:**

- `Alexander` — partial — pred is substring of gold: `Alexander X.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexander X.`(person)
- `M.`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_168`)


Seit 4.8.2014 ist auch Herr DI Wolfgang FG5  Geschäftsführer.

**False Positives:**

- `DI Wolfgang FG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_123`)


Im rechtzeitigen Vorlageantrag brachte der steuerliche Vertreter der Bf. vor, dass Frau bfb und  Herr BfA die betreffende Liegenschaft und folglich die Einkunftsquelle im Jahr 1997 aufgrund  einer Erbschaft (Einantwortungsbeschluss vom26.6.1997) unentgeltlich erworben hätten.

**False Positives:**

- `BfA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_137`)


Herr BfA sei damals persönlich  beim damals zuständigen Finanzamt Wien 6/7/15 vorstellig geworden.

**False Positives:**

- `BfA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Wien 6/7/15`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_138`)


Nur weil das Finanzamt  diese Unterlagen nicht mehr im Akt finde, wie in der Bescheidbegründung der BVE behauptet,  heiße das nicht, dass die Behauptung von Herrn BfA unwahr sei.

**False Positives:**

- `BfA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_140`)


Tatsache sei, dass Herr  BfA seinerzeit persönlich bei der damals zuständigen Abgabenbehörde die AfA-

**False Positives:**

- `BfA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_186`)


Knackpunkt für das Finanzamt sei, dass keine Nachweise  hinsichtlich einer Vorsprache Herrn BfAs sowie hinsichtlich einer mit diesem getroffenen  Einigung im Akt des FA enthalten sei.

**False Positives:**

- `BfAs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_304`)


Der Anteil an den Einkünften für Herrn BfA beträgt: Euro 10.081,85  Der Anteil an den Einkünften für Frau BfB beträgt: Euro 10.081,84

**False Positives:**

- `BfA` — no gold match — likely missing annotation
- `BfB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_30`)


Am 18.12.2002 kam die Bf. weiters mit dem (vormaligen) Landesgendarmeriekommando für  Kärnten dahingehend überein, dass Frau MartinmüllerA den in der strittigen Liegenschaft befindlichen  Gendarmerieposten - infolge Pensionierung der dort tätigen Raumpflegerin - mit Wirksamkeit  zum 1.1.2003 mitreinigen wird (vgl. Präambel zum Vertrag vom 18.12.2002).

**False Positives:**

- `Martinm` — partial — pred is substring of gold: `MartinmüllerA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MartinmüllerA`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_52`)


Wie eine Einsicht in den im Rahmen der Betriebsprüfung vorgelegten (undatierten)  „Dienstvertrag-Änderung“ zeigt, stand Frau MartinmüllerA seit Jänner 1993 in einem aufrechten  Vertragsverhältnis zur Bf..

**False Positives:**

- `Martinm` — partial — pred is substring of gold: `MartinmüllerA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MartinmüllerA`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_31`)


4) Geldannahme Bestätigung vom 23. Juli 2021, in der Herr Herr2 den Erhalt von € 10.000,00  für die Übernahme von fünf Autos vom Bf. bestätigt.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Roland` — partial — pred is substring of gold: `Roland Rößle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Roland Rößle`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_8`)


FirmenwortlautBf  xStrasse  Ort  ATU UID-Nr  Herr Herr1  Herr Herr2.“

**False Positives:**

- `Herr` — no gold match — likely missing annotation
- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Names after 'vertreten durch' (Tightened)` 🏆

**F1:** 0.018 | **Precision:** 0.486 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `111f011a`  
**Description:**
Matches names following 'vertreten durch' ensuring the full name including titles is captured, but explicitly excludes company names by requiring a comma or end-of-string immediately after the name (or a known person suffix).

**Content:**
```
(?:vertreten durch)\s+([A-Z][a-zA-Z]+(?:[ -][A-Z][a-zA-Z]+)+)(?=,|$|[.](?!.*(?:GmbH|AG|Gesellschaft|Partnerschaft|OG|m\.b\.H)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.486 | 0.009 | 0.018 | 35 | 17 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 17 | 18 | 1834 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Dr Vana Dr Kolbitsch Mag Breitenecker` | `Dr Vana Dr Kolbitsch Mag Breitenecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr Christian Burghardt` | `Dr Christian Burghardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `StR Univ.-Prof. Alvin Paulikat` (person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_2`)


Saskia Sinnwell, Wien1  beide vertreten durch Christoph Zitz MBA, murtax Steuerberatungs GmbH Kuenburgstraße 10,  5580 Tamsweg  wegen des Finanzvergehens der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG), beim Verband gemäß § 28a Abs. 2 FinStrG, über die Beschwerde  des Amtsbeauftragten vom 17. September 2019 (gemeint wohl richtig: 3. Dezember 2020)  gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19  Klosterneuburg als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. September 2020, SpS 2000, in der Sitzung am 27. Mai 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christoph Zitz MBA` | `Christoph Zitz MBA` |

**Missed by this rule (FN):**

- `Saskia Sinnwell` (person)
- `murtax Steuerberatungs GmbH` (organisation)
- `Finanzamt Wien 9/18/19` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag Kerstin Friedrich` | `Mag Kerstin Friedrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alfred Klaus Fenzl` | `Alfred Klaus Fenzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Hugo Engelsmann` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Michael Haberl` | `Michael Haberl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Dr.in Edith Lohhausen` (person)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Erich Allbrand` | `Erich Allbrand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Robert Derici` (person)
- `Exlgasse 12, 9623 Karnitzen, Österreich` (address)
- `12-876/0077` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Peter Schabel` | `Peter Schabel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Jeremias Kierstan` (person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich` (address)
- `Magistrats  der Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paula Tschann  in der Beschwerdesache Merlin Dankwort,  Urtelgasse 9y, 8232 Stambach, Österreich  vertreten durch Valerian Stamataki, Schanze 29 12, 3661 Unterthalheim, Österreich, über die Beschwerde vom  6. September 2022 gegen den Bescheid des Finanzamtes Österreich vom 9. August 2022  betreffend Festsetzung eines ersten Säumniszuschlages, Steuernummer 88-049/5894  nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valerian Stamataki` | `Valerian Stamataki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Paula Tschann` (person)
- `Merlin Dankwort` (person)
- `Urtelgasse 9y, 8232 Stambach, Österreich` (address)
- `Schanze 29 12, 3661 Unterthalheim, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-049/5894` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

| Predicted | Gold |
|---|---|
| `Helga Kraus` | `Helga Kraus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Cassandra Schmedtje` (person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dr. Martin Wadepfuhl  in der Beschwerdesache Renate Bürvenig,  Kreuzkapellenweg 7, 5151 Hochberg, Österreich, vertreten durch Ludmilla Flaumbaum, Herrengschwendt 3, 8761 Mühltal, Österreich, über die Beschwerde vom  15. Februar 2021 gegen die Bescheide des Finanzamtes Österreich vom 19. Jänner 2021  betreffend die Haftung für Lohnsteuer für 2015, 2016, 2017, 2018 und 2019, sowie den  Dienstgeberbeitrag zum FLAF für 2015, 2016, 2017, 2018 und 2019 und den Zuschlag zum  Dienstgeberbeitrag für 2015, 2016, 2017, 2018 und 2019 zu Steuernummer 74-041/7335  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ludmilla Flaumbaum` | `Ludmilla Flaumbaum` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Dr. Martin Wadepfuhl` (person)
- `Renate Bürvenig` (person)
- `Kreuzkapellenweg 7, 5151 Hochberg, Österreich` (address)
- `Herrengschwendt 3, 8761 Mühltal, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `74-041/7335` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Georg Kunstmann  in der Beschwerdesache Gerhard Weinbergs,  Löwengrub 29, 8680 Hönigsberg, Österreich, vertreten durch Damian Eccardt, Unterort 18, 4673 Bernhartsdorf, Österreich, über die Beschwerde vom 8.  Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 4. April 2023 betreffend  Umsatzsteuer 2013 sowie über die Beschwerden vom 23. August 2023 gegen die Bescheide  des Finanzamtes Österreich vom 4. August 2023 betreffend Umsatzsteuer 2014, 2015, 2016  und 2017 zu Steuernummer 50-546/1107  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Damian Eccardt` | `Damian Eccardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Georg Kunstmann` (person)
- `Gerhard Weinbergs` (person)
- `Löwengrub 29, 8680 Hönigsberg, Österreich` (address)
- `Unterort 18, 4673 Bernhartsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `50-546/1107` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Caroline Bolzen, Patschweg 38, 9635 Nölbling, Österreich, vertreten durch Christine Maria Brunnthaller, Baumgarten 20 Tür  2, 3512 Mautern/Donau, über die Beschwerde vom 25. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 18. März 2024 betreffend Familienbeihilfe 07.2023-03.2024 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Maria Brunnthaller` | `Christine Maria Brunnthaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Caroline Bolzen` (person)
- `Patschweg 38, 9635 Nölbling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/147002.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Franz Quapp  in der Beschwerdesache  Elvira Mathis, Claudiastraße 7, 2061 Hadres, Österreich, vertreten durch Wladimir Kreissl, Seibersdorf 3, 8141 Bierbaum, Österreich,  über die Beschwerde vom 13. Mai 2015 gegen den Bescheid des (damaligen) Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 9. April 2015  betreffend Säumniszuschlag 2015 Steuernummer 98-983/4004  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Kreissl` | `Wladimir Kreissl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Franz Quapp` (person)
- `Elvira Mathis` (person)
- `Claudiastraße 7, 2061 Hadres, Österreich` (address)
- `Seibersdorf 3, 8141 Bierbaum, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `98-983/4004` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anneliese Furtmeier  in der Beschwerdesache Werner Kachelek,  Heideweg-Siedlung 7, 4030 Linz, Österreich, vertreten durch Eugen Josef Bertsch, Sportplatzweg 11, 6811 Göfis, betreffend  Beschwerde vom 22. August 2019 gegen den Bescheid des FA Spittal Villach (nunmehr Finanzamt  Österreich) vom 29. Juli 2019 über die Abweisung eines Antrages auf Nachsicht gemäß § 236  BAO, Steuernummer 85-278/4119, beschlossen:  Der Vorlageantrag vom 30. September 2019 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 lit. d BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Eugen Josef Bertsch` | `Eugen Josef Bertsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Anneliese Furtmeier` (person)
- `Werner Kachelek` (person)
- `Heideweg-Siedlung 7, 4030 Linz, Österreich` (address)
- `FA Spittal Villach` (organisation)
- `Finanzamt  Österreich` (organisation)
- `85-278/4119` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Univ.-Prof.in Maja Lauers  in der Säumnisbeschwerdesache  Univ.-Prof. Mehmet Klasema, Labon 67, 4861 Looh, Österreich  vertreten durch Jonathan Goessl, über die Beschwerde vom 8. Jänner  2025 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Bescheidbeschwerde vom 12. April 2024 gegen den Bescheid betreffend die  Abweisung des Antrages auf Wiederaufnahme des Verfahrens gemäß § 303 BAO  (Körperschaftsteuer 2021) vom 13. März 2024, Steuernummer 85-153/1153, den Beschluss:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 in Verbindung mit  Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Jonathan Goessl` | `Jonathan Goessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Maja Lauers` (person)
- `Univ.-Prof. Mehmet Klasema` (person)
- `Labon 67, 4861 Looh, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `85-153/1153` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gregor Heumann, Weberweg 49, 4274 Steinbichl, Österreich, vertreten durch Stefan Josef Glechner, Am  Schwarzenbach 8, 4921 Hohenzell, über die Beschwerde vom 10. Februar 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. Jänner 2023 betreffend Feststellung der Einkünfte  § 188 BAO 2021 Steuernummer 31-405/5720  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Stefan Josef Glechner` | `Stefan Josef Glechner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Gregor Heumann` (person)
- `Weberweg 49, 4274 Steinbichl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `31-405/5720` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `RA Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Walter Summersberger`(person)
- `Emmerich Frydrychowski`(person)
- `Wassertheuer 21, 9112 Gletschach, Österreich`(address)
- `Zollamtes Innsbruck`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

**False Positives:**

- `Sera Trust GmbH` — type mismatch — same span as gold: `Sera Trust GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Thomas Mevis`(person)
- `Lindenhang 30, 4591 Ramsau, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `MITTEREGGER Steuerberatungs GmbH` — type mismatch — same span as gold: `MITTEREGGER Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Sieglinde Kießerling`(person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich`(address)
- `MITTEREGGER Steuerberatungs GmbH`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `27-927/6451`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `LKP Steuerberatung OG` — type mismatch — same span as gold: `LKP Steuerberatung OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `HR OSR Leonie Ercklentz`(person)
- `Karnitzen 135, 9635 Kronhof, Österreich`(address)
- `LKP Steuerberatung OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `KPMG Alpen-Treuhand GmbH` — type mismatch — same span as gold: `KPMG Alpen-Treuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kimberly Jeworski`(person)
- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

**False Positives:**

- `WINKEL STEINER WAIBEL Steuerberater GmbH` — type mismatch — same span as gold: `WINKEL STEINER WAIBEL Steuerberater GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Moses Dannebohm`(person)
- `Ruperta Schluckner`(person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich`(address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH`(organisation)
- `Finanzamtes Feldkirch`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135937.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135937.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch V, R sowie die fachkundigen Laienrichter L1 und L2 in der  Beschwerdesache X.AG RNF Unter-Luftfahrt Institut GmbH Somogyihof 83, 8674 Rettenegg, Österreich  vertreten durch Rechtsanwalt RA,  Somogyihof 83, 8674 Rettenegg, Österreich  über die Beschwerde vom 27.07.2021 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 12.07.2021, Steuernummer xxx, über die Abweisung eines  Zahlungserleichterungsansuchens nach der am 24.02.2022 in Abwesenheit der Parteien, in  Anwesenheit der Schriftführerin S durchgeführten mündlichen Verhandlung zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwalt RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Unter-Luftfahrt Institut GmbH`(organisation)
- `Somogyihof 83, 8674 Rettenegg, Österreich`(address)
- `Somogyihof 83, 8674 Rettenegg, Österreich`(address)
- `Finanzamtes für  Großbetriebe`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

**False Positives:**

- `TPA Steuerberatung GmbH` — type mismatch — same span as gold: `TPA Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Helmut Mittermayr`(person)
- `Claire Wienhues`(person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich`(address)
- `TPA Steuerberatung GmbH`(organisation)
- `Finanzamt`(organisation)
- `61-469/1778`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137349.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Gebhard Kristupeit, Bakk. techn., Wörndlestraße 17, 9112 Untergrafenbach, Österreich, vertreten durch APP Steuerberatung GesmbH, Schenkenstraße  4, 1010 Wien, über die Beschwerde gegen die Bescheide des Finanzamtes Baden Mödling vom  31. Mai 2011 hinsichtlich Haftung betreffend Kapitalertragsteuer für 2007 und 2008,  Steuernummer 83-002/9356  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `APP Steuerberatung GesmbH` — type mismatch — same span as gold: `APP Steuerberatung GesmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Gebhard Kristupeit, Bakk. techn.`(person)
- `Wörndlestraße 17, 9112 Untergrafenbach, Österreich`(address)
- `APP Steuerberatung GesmbH`(organisation)
- `Finanzamtes Baden Mödling`(organisation)
- `83-002/9356`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Maximiliane Gasparetti, Gschwandtkopf 12, 9330 Althofen, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 23. Dezember 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. November 2016 betreffend  1.

**False Positives:**

- `KPMG Alpen-Treuhand GmbH` — type mismatch — same span as gold: `KPMG Alpen-Treuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Alois Pichler`(person)
- `Maximiliane Gasparetti`(person)
- `Gschwandtkopf 12, 9330 Althofen, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Olaf Koechig, Zmöllach 3, 3542 Litschgraben, Österreich, Beschwerde vom 25. Oktober 2019 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr Finanzamtes Österreich, vom  28. November 2018 betreffend Umsatzsteuer 2012, Umsatzsteuer 2013, Umsatzsteuer 2014  und Umsatzsteuer 2015, Steuernummer 17-913/2665, der Gartfentri Heizung Institut GmbH, vertreten durch  Gustke Forschung GmbH, hinsichtlich des Vorlageantrages der Gartfentri Heizung Institut GmbH  in  Liquidation, beschlossen:  I. Die Beschwerdevorentscheidungen vom 6. April 2022 betreffend Umsatzsteuer 2012,  2013, 2014 und 2015 der Gartfentri Heizung Institut GmbH  in Liquidation werden aufgehoben.

**False Positives:**

- `Gustke Forschung GmbH` — type mismatch — same span as gold: `Gustke Forschung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Konrad`(person)
- `Olaf Koechig`(person)
- `Zmöllach 3, 3542 Litschgraben, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `17-913/2665`(tax_number)
- `Gartfentri Heizung Institut GmbH`(organisation)
- `Gustke Forschung GmbH`(organisation)
- `Gartfentri Heizung Institut GmbH`(organisation)
- `Gartfentri Heizung Institut GmbH`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/142384.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Thassilo Bergsträsser,  Alois Blumauer-Gasse 1o, 4152 Unternreith, Österreich, vertreten durch VICTORIA Wirtschaftstreuhand GmbH, Prinz-Eugen-Straße  16/1/6, 1040 Wien über die Beschwerde vom 4. August 2021 gegen den Bescheid des  Finanzamtes Österreich vom 19. Juli 2021 betreffend Einkommensteuer 2019 Steuernummer  68-027/9886  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `VICTORIA Wirtschaftstreuhand GmbH` — type mismatch — same span as gold: `VICTORIA Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Thassilo Bergsträsser`(person)
- `Alois Blumauer-Gasse 1o, 4152 Unternreith, Österreich`(address)
- `VICTORIA Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `68-027/9886`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Niklas Hussung  in der Beschwerdesache Univ.-Prof. Oliver Ruhsbüldt,  Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich, vertreten durch Gattringer Steuerberatung GmbH, Sonnensteinstraße 12, 4040  Linz, über die Beschwerde vom 31. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 16. Mai 2023 betreffend Einkommensteuer 2021 Steuernummer 26-058/9655  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gattringer Steuerberatung GmbH` — type mismatch — same span as gold: `Gattringer Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Niklas Hussung`(person)
- `Univ.-Prof. Oliver Ruhsbüldt`(person)
- `Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich`(address)
- `Gattringer Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `26-058/9655`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/147165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147165.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Priv.-Doz.in Antonia Ramdani  in der Beschwerdesache Hedwig Schadek,  Adelsdorf 68, 8755 Feistritzgraben, Österreich, vertreten durch RPW Tulln Steuerberatung GmbH, Franz-Schubert-Straße 8,  3430 Tulln/Donau, betreffend Beschwerde vom 3. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2024 betreffend Säumniszuschlag 2024, Steuernummer  95-051/7682, den Beschluss:  I. Der Vorlageantrag wird gemäß § 260 Abs. 1 lit. b BAO iVm § 264 Abs. 4 lit. e BAO als  nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `RPW Tulln Steuerberatung GmbH` — partial — pred is substring of gold: `RPW Tulln Steuerberatung GmbH,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Antonia Ramdani`(person)
- `Hedwig Schadek`(person)
- `Adelsdorf 68, 8755 Feistritzgraben, Österreich`(address)
- `RPW Tulln Steuerberatung GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)
- `95-051/7682`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

**False Positives:**

- `Sera Trust GmbH` — type mismatch — same span as gold: `Sera Trust GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Ing. Dagobert Almasri`(person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Annika Streicher BA LL.M.(WU) in der  Beschwerdesache Dimitri Gaessner, Sauerbrunnberg 15, 8124 Neuhof, Österreich, vertreten durch Miriam Wurmehl, Bakk. phil., Windparkstraße 7, 5092 Gumping, Österreich, über die Beschwerde vom 13. Februar 2024 gegen den Bescheid des Finanzamtes  Österreich vom 16. Jänner 2024 betreffend Verspätungszuschlag / ESt 2020 Steuernummer  90-683/6114  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Miriam Wurmehl` — partial — pred is substring of gold: `Miriam Wurmehl, Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Annika Streicher BA LL.M.(WU)`(person)
- `Dimitri Gaessner`(person)
- `Sauerbrunnberg 15, 8124 Neuhof, Österreich`(address)
- `Miriam Wurmehl, Bakk. phil.`(person)
- `Windparkstraße 7, 5092 Gumping, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `90-683/6114`(tax_number)

</details>

---

## `Frau Preceded Names with Suffixes` 🏆

**F1:** 0.011 | **Precision:** 0.303 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `2be8e62f`  
**Description:**
Matches persons preceded by 'Frau' or 'Herr', capturing the full name including suffixes (LL.M., MBA, Bakk. techn.), ensuring it's not just a title.

**Content:**
```
(?:Herrn?|Frau)\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MAS|Bakk\. rer\. nat|Bakk\. art\. BEd)?)?)?(?=,|$|[.](?!.*(?:GmbH|AG|Gesellschaft)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.303 | 0.005 | 0.011 | 33 | 10 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 23 | 1841 |

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

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_55`)


Die in concreto erfolgten Verrechnungen bzw. die buchhalterische Erfassung der  verfahrensgegenständlichen Leistungen basieren auf den Angaben der Bf. im Zuge der  mündlichen Verhandlung (vgl. Ausführungen Herr GundelachB, VH-Protokoll S. 9f).

| Predicted | Gold |
|---|---|
| `GundelachB` | `GundelachB` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_10`)


Ein weiterer ärztlicher Befundbericht von Fr. Dr. **** und Herrn Dr. **** lagen ebenfalls dem  Antrag bei.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Inn Trikraftglanz`(person)
- `Inn Trikraftglanz`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Baues`(person)
- `Baues`(person)
- `Borisowa`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_79`)


Mit Datum 09.09.2004 wurde ein Mietvertrag bezüglich der gegenständlichen Wohnung  zwischen der Bf als Vermieterin und Herrn MS, dem Schwager der Gesellschafter- Geschäftsführerin, abgeschlossen.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_83`)


Der Gatte der  Gesellschafter-Geschäftsführerin, Herr WS, hat nach Aufbrauchen des VSt-Guthabens die  Bezahlung der monatlichen Kreditraten übernommen.

**False Positives:**

- `WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_30`)


Als ihre  handelsrechtlichen Geschäftsführer agieren seit xx.2005 Herr B (geb. xxxx) bzw. seit xx.2006  Herr XY.

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_36`)


Zur gemeinsamen mündlichen Verhandlung (Streitsachen: 1. und 2. Zwangsstrafe) erscheinen  zwei Rechtanwälte, Herr Dr. Karl RA1, der auch als Geschäftsführer der Bf. eingetragen ist, und  Herr RA2.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_64`)


Beweis: Person4, als Zeuge, Person3  Folgender Mailverkehr wurde in der mündlichen Verhandlung seitens der Bf. vorgelegt, im  Wesentlichen:  STB2 an BMF1 (BMF Abteilung III/12), gesendet 5. Oktober 2021:  S.g. Herr Ministerialrat, wie schon kürzlich tel.

**False Positives:**

- `Ministerialrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_17`)


Es würden mit Herrn Ing. K. (Geschäftsführer der Fa. X.  2 von 9 Seite 3 von 9

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)


Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die Jeremias Kierstan, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Jeremias Kierstan`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_75`)


Außerdem übersendete der Bf. die Dienstzeugnisse seiner drei oben genannten Arbeitgeber:  - AG1:   „Herr VN NN, geboren am Geb., war vom 1.1.2015 bis 31.8.2017 als Geschäftsführer in  unserem Unternehmen tätig.

**False Positives:**

- `VN NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_91`)


Wir wünschen Herrn NN auf seinem weiteren Berufs- und Lebensweg alles  Gute und weiterhin viel Erfolg.“  - AG2:  „Herr VN NN, geboren am Geb., war vom 01.09.2017 bis 31.08.2018 als geschäftsführender  Gesellschafter bei der AG2 tätig.

**False Positives:**

- `VN NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_104`)


Wir bedauern seine Entscheidung sehr und wünschen ihm für  seine private und berufliche Zukunft viel Erfolg.“  - AG3 Immobilien GmbH:  „Herr VN NN, geb. Geb., wohnhaft in Ort, Straße, war vom 1.09.2018 bis zum 31.12.2018 in  unserem Unternehmen als Immobilienmakler im Bereich Wohn- und Vorsorgeimmobilien  beschäftigt.

**False Positives:**

- `VN NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_24`)


……………………“  Beschwerde  Innerhalb offener Frist wurde in einem einheitlichen Schriftsatz Beschwerde gegen die an die  erblichen Töchter ergangenen Gebührenbescheide erhoben und dies wie folgt begründet:  “Mit rechtskräftigem Einantwortungsbeschluss vom 17.3.2016, ……, wurde der Nachlass nach  dem am 10. September 1972 .2015 verstorbenen, zuletzt in Salfeldstraße 54, 9500 Oberwollanig, Österreich  wohnhaft gewesenen  Industriemechaniker, Herrn FM, den aufgrund des Gesetzes bedingt erbantrittserklärten Erben,  der erbl. Witwe M, geb. …., zu einem Drittel und den erbl. Töchtern, mj. S, geb. ….., mj. J, geb.  ……., mj. L, geb. ……., und mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……., zu je einem Sechstel eingeantwortet.

**False Positives:**

- `FM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `10. September 1972`(date)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `KzlR Techn R RgR Wigand Beinhorn`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_67`)


Herr Dr. Alma Goerts (steuerliche Vertretung) bringe in der  Beschwerde nun selbst vor, dass die Einhaltung gegenständlicher Frist ausschließlich in seiner  Befugnis gelegen habe und er aufgrund des Todesfalls in seinem privaten Umfeld vergessen  habe, einem seiner Mitarbeiter die Weisung zur Einbringung eines Fristverlängerungsantrages  zu erteilen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_70`)


Auch wenn Herr Dr. Alma Goerts  nach eigenen Angaben  bislang noch nie eine Frist versäumt habe, dürfe die Einhaltung von Fristen (Fristenwahrung)  für die Steuerberatungskanzlei nicht "ausschließlich" in seinem alleinigen Bereich liegen bzw.  es müsse durch entsprechende Kontrollmechanismen vorgesorgt werden, dass  Unzulänglichkeiten durch menschliches Versagen (wie z.B. durch Vergessen) aller Voraussicht  nach ausgeschlossen seien.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_71`)


Ein Vergessen der Frist wäre nach Ansicht der Abgabenbehörde  leicht zu verhindern gewesen, wenn einer der sechs Kanzleimitarbeiter Herrn Dr. Alma Goerts  rechtzeitig auf den Ablauf der Frist hingewiesen hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_73`)


Möglicherweise seien sie aber "vor" Erteilung eines Auftrags durch Herrn Dr.  Alma Goerts  einfach nicht für diese Angelegenheit zuständig.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alma Goerts`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_67`)


Über die diesbezügliche Rücksprache mit der belangten Behörde sei vom steuerlichen  Vertreter am 7. August 2001 ein Aktenvermerk angelegt worden, welchen folgenden Inhalt  habe:  ….“Haben dies mit Herrn Mag. ***, FA Feldkirch am 7. August 2001 nochmals besprochen und  um einen Lösungsvorschlag gebeten: Nach Mag. *** soll die liechtensteinische FA Spittal Villach  eine  Proformarechnung an die RHO Pharma  ausstellen, somit wird die RHO Pharma  zum "Proforma  Verfügungsberechtigten" und kann die abgeführte Einfuhrumsatzsteuer problemlos als  Vorsteuer geltend machen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Feldkirch`(organisation)
- `FA Spittal Villach`(organisation)
- `RHO Pharma`(organisation)
- `RHO Pharma`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/144990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144990.1_29`)


Geschäftsführer der Gesellschaft ist seit ihrer Gründung Herr Gf.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_19`)


Es habe sich  laut Bf. um eine Einmalzuwendung einer Stiftung eines Freundes der Familie gehandelt, - Herr  YZ, Schweizer Staatsangehöriger- der bereits vor 5 Jahren verstorben sei.

**False Positives:**

- `YZ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_109`)


Zudem wurde vom Geschäftsführer, Herrn Gf., bei der Schlussbesprechung gem § 149 Abs  1 BAO am 12.12.2017 mitgeteilt, dass in Peru keine steuerliche Erfassung der Betriebsstätte  erfolgte, dies wurde auch im Schreiben vom 22.12.2017 bestätigt.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Ing. and Specialized Titles with Names` 🏆

**F1:** 0.026 | **Precision:** 0.255 | **Recall:** 0.014  

**Format:** `regex`  
**Rule ID:** `e4382ea1`  
**Description:**
Specifically targets titles like Ing., KommR, OSR, ÖkR followed by names, ensuring the full name is captured even if it contains placeholders or is a single word. Excludes 'RichterRi' which is a role, not a title.

**Content:**
```
(?:Ing\. |KommR |OSR |ÖkR |PhD |StR |OStR |OMedR |MedR |VetR |LLB |KzlR|Ri)(?:[A-Z]\.[A-Za-z]+|[A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.255 | 0.014 | 0.026 | 98 | 25 | 73 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 25 | 73 | 1826 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

| Predicted | Gold |
|---|---|
| `Ing. StR Samuel Fraesdorff` | `Ing. StR Samuel Fraesdorff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich` (address)
- `Maximilian Jasper` (person)
- `Wetzles 9, 3243 Lunzen, Österreich` (address)
- `Prof. Dr. Thomas Keppert` (person)
- `Leroy Kusznierz` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

| Predicted | Gold |
|---|---|
| `Ing. StR Samuel Fraesdorff` | `Ing. StR Samuel Fraesdorff` |

**Missed by this rule (FN):**

- `Leroy Kusznierz` (person)
- `Maximilian Jasper` (person)
- `Gustav Nowak` (person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Dominik Mehlig` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Werner Böltl` | `Ing. Werner Böltl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Martin Kuprian` (person)
- `Rydlweg 234, 3860 Dietweis, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache OSR Eugenia Balikci, Richardisweg 14, 5134 Ginshöring, Österreich, vertreten durch Wiener Kinder-und Jugendhilfe  2,20, Dresdner Straße 43, 1200 Wien, über die Beschwerde vom 20. März 2020 gegen den  Bescheid des Finanzamtes Österreich vom 25. Februar 2020 betreffend Familienbeihilfe ab  Jänner 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OSR Eugenia Balikci` | `OSR Eugenia Balikci` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Richardisweg 14, 5134 Ginshöring, Österreich` (address)
- `Wiener Kinder-und Jugendhilfe` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_4`)


Verfahrensgang    Für den mj. Beschwerdeführer (Bf.), geb. am tt.mm.2009, wurde durch den Vormund Wiener   Kinder und Jugendhilfe, Magistratsabteilung 11 des Magistrates der Stadt Wien, am 18.12.2019  ein Antrag auf Gewährung der Familienbeihilfe rückwirkend ab Jänner 2016 gestellt.    Mit Bescheid vom 25. Februar 2020 wurde der Antrag vom 23.12.2019 auf Familienbeihilfe für  den mj. OSR Eugenia Balikci  den Zeitraum ab Jänner 2016 abgewiesen.

| Predicted | Gold |
|---|---|
| `OSR Eugenia Balikci` | `OSR Eugenia Balikci` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_13`)


Der mj. OSR Eugenia Balikci  befand steh im abweisenden Zeitraum ab  Jänner 2016 in einer sozialpädagogischen Wohngemeinschaft der Sozialwerke Clara Fey.

| Predicted | Gold |
|---|---|
| `OSR Eugenia Balikci` | `OSR Eugenia Balikci` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_38`)


Das Bundesfinanzgericht richtete am 2020 folgenden Vorhalt an die Rechtsvertretung des Bf.:  „In der von der Wiener Kinder- und Jugendhilfe, Rechtsvertretung Bezirk 22, gegen den  Abweisungsbescheid des Finanzamtes erhobenen Beschwerde wird vorgebracht, dass sich der  mj. OSR Eugenia Balikci  im abweisenden Zeitraum ab Jänner 2016 in einer sozialpädagogischen  Wohngemeinschaft der Sozialwerke Clara Fey befand und die Sozialwerke Clara Fey wesentlich  auch durch Spenden finanziert würden.

| Predicted | Gold |
|---|---|
| `OSR Eugenia Balikci` | `OSR Eugenia Balikci` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_47`)


Der Minderjährige OSR Eugenia Balikci  befindet sich seit 1.1.2016 in einer sozialpädagogischen  Wohngemeinschaft der Sozialwerke Clara Fey.

| Predicted | Gold |
|---|---|
| `OSR Eugenia Balikci` | `OSR Eugenia Balikci` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/140806.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140806.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Moritz Bonnert  in der Beschwerdesache PhD MedR Romana Hupp,  Süßenberger Straße 7, 5270 Vorbuch, Österreich, vertreten durch Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020 Innsbruck, über die Beschwerde  vom 26. Juli 2013 gegen den Bescheid des FA Salzburg-Land  vom 25. Juni 2013 betreffend  Umsatzsteuer 2011, Steuernummer 16-160/7509, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `PhD MedR Romana Hupp` | `PhD MedR Romana Hupp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Priv.-Doz. Moritz Bonnert` (person)
- `Süßenberger Straße 7, 5270 Vorbuch, Österreich` (address)
- `Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `FA Salzburg-Land` (organisation)
- `16-160/7509` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Calvin Liechtenstein  in der Beschwerdesache KommR Thorsten Voelkerling,  Kirchenbühl 12, 4463 Brunnbach, Österreich, vertreten durch Rechtsanwalt Dr. Gahleithner & Partner OG, Schottengasse 7  Tür 6, 1010 Wien, über die Beschwerde vom 25. September 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 11. September 2019 betreffend den Ablauf der Aussetzung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KommR Thorsten Voelkerling` | `KommR Thorsten Voelkerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Calvin Liechtenstein` (person)
- `Kirchenbühl 12, 4463 Brunnbach, Österreich` (address)
- `Dr. Gahleithner & Partner OG` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_88`)


Im Begleitschreiben vom 29.5.2024 wird ua. nochmals vorgebracht, dass die zugrunde  liegenden Befunde von der Gutachterin PhD Doris Goessing teils unvollständig oder fachlich inkorrekt  interpretiert worden seien.

| Predicted | Gold |
|---|---|
| `PhD Doris Goessing` | `PhD Doris Goessing` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_92`)


mit einem Gendefekt (BFG 12.5.2021, RV/3100566/2020) von der  Gutachterin PhD Doris Goessing auf Ersuchen des BFG mit Schreiben v. 14.3.2021 ua.

| Predicted | Gold |
|---|---|
| `PhD Doris Goessing` | `PhD Doris Goessing` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_97`)


Aus dem CV geht ua. hervor, dass die als Gutachterin für das  Sozialministeriumservice tätige PhD Doris Goessing seit 1995 Fachärztin für Kinder- und Jugendheilkunde ist,  seit 1997 mit dem Additivfach Humangenetik, Habilitation am 22.6.1998 ("Localization of  Cancer Susceptibility Genes"), und seit 2008 mit dem Additivfach Endokrinologie und Diabetes.

| Predicted | Gold |
|---|---|
| `PhD Doris Goessing` | `PhD Doris Goessing` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_171`)


Abgesehen davon verfügt PhD Doris Goessing als Fachärztin für Kinder- und Jugendheilkunde daneben über  eine Zusatzqualifikation im Fach "Humangenetik" und ist als langjährige Ambulanzleiterin,  darunter der Ambulanz für Klinische Genetik, ua. auch mit der Betreuung von Patienten mit  einer seltenen Erkrankung befasst.

| Predicted | Gold |
|---|---|
| `PhD Doris Goessing` | `PhD Doris Goessing` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/147552.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147552.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Jörg Novakowski  in der Beschwerdesache OSR Samantha Schaffroth,  Kaltenbach 71, 3353 Biberbach, Österreich, über die Beschwerde vom 16. September 2020 gegen den Bescheid des  FA Niederösterreich Mitte  vom 21. August 2022, mit welchen der Antrag auf Wiederaufnahme der Verfahren  betreffend Einkommensteuer für die Jahr 2015 bis 2017 gem. § 303 BAO abgewiesen wurde, zu  Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OSR Samantha Schaffroth` | `OSR Samantha Schaffroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Jörg Novakowski` (person)
- `Kaltenbach 71, 3353 Biberbach, Österreich` (address)
- `FA Niederösterreich Mitte` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

| Predicted | Gold |
|---|---|
| `Ing. Dagobert Almasri` | `Ing. Dagobert Almasri` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/148525.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148525.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Julia Schlegl in der Beschwerdesache  KommR Natascha Domroeß, Obere Mölten 6, 9500 St. Georgen, Österreich, über die Beschwerde vom 28. Juni 2024 gegen den Bescheid des  Finanzamt St. Johann Tamsweg Zell am See  vom 17. Juni 2024 betreffend Anspruchszinsen (§ 205 BAO), Steuernummer  55-147/5658, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `KommR Natascha Domroeß` | `KommR Natascha Domroeß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Julia Schlegl` (person)
- `Obere Mölten 6, 9500 St. Georgen, Österreich` (address)
- `Finanzamt St. Johann Tamsweg Zell am See` (organisation)
- `55-147/5658` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/148710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Florentin Tyarks  in der Beschwerdesache KommR Thaddäus Borkowski,  Linke Quergasse 31, 4600 Berg, Österreich, über die Beschwerden vom 16. April 2016 gegen die Bescheide des  Finanzamtes Landeck Reutte (nunmehr: Finanzamt Österreich) vom 15. März 2016 betreffend  Festsetzung des Dienstgeberbeitrages für die Jahre 2010 bis 2014, Steuernummer  01-227/0941,  zu Recht erkannt:  I.  Die Beschwerdevorentscheidung des Finanzamtes Innsbruck vom 19. September 2018, mit  welcher über die Beschwerden vom 15. April 2016 "gegen die Bescheide über die Festsetzung  des Dienstgeberbeitrages 2010-2014" abgesprochen wurde, wird wegen Unzuständigkeit der  bescheiderlassenden Behörde aufgehoben.

| Predicted | Gold |
|---|---|
| `KommR Thaddäus Borkowski` | `KommR Thaddäus Borkowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Florentin Tyarks` (person)
- `Linke Quergasse 31, 4600 Berg, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `01-227/0941` (tax_number)
- `Finanzamtes Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)


Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit PhD Wilhelm Reschke, MBA,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

**False Positives:**

- `PhD Wilhelm Reschke` — partial — pred is substring of gold: `PhD Wilhelm Reschke, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Wilhelm Reschke, MBA`(person)
- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`
- `Ing. Viktoria Weigart` — similar text (different position): `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)


Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der Dr.in Ing. Viktoria Weigart  Somit traf ihn die Auskunftspflicht.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Ing. Melinda Herrwerth` — partial — pred is substring of gold: `Dipl.-Ing. Melinda Herrwerth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Melinda Herrwerth`(person)
- `Dürergasse 7, 4872 Windbichl, Österreich`(address)
- `40-459/9630`(tax_number)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)
- `Lubomir Nakajima`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Ing` — partial — pred is substring of gold: `Dipl. Kfm. Ing. Ing. Jonas Thumberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger`(person)
- `Paullehnerweg 72, 9584 Höfling, Österreich`(address)
- `UNICONSULT Steuerberatungs GmbH & Co KG`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_161`)


An der Traver-Planung GmbH waren beteiligt:    26.600 €…Holding (jedenf. 1.1.2008-12.4.2010)  25.900 €… Holding (13.4.2010-8.2.2015)  26.600 €….Holding (9.2.2015-10.9.2019)  8.400 €……Ing. Michael FG2 (jedenfalls. 1.1.2008-12.4.2010)  9.100 €……Ing. Michael FG2 (13.4.2010-8.2.2015)  8.400 €……Ing. Michael FG2 9.2.2015  35.000 €….Summe

**False Positives:**

- `Ing. Michael FG` — no gold match — likely missing annotation
- `Ing. Michael FG` — no gold match — likely missing annotation
- `Ing. Michael FG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Traver-Planung GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_162`)


Geschäftsführer dieser GmbH sind der zweite Stratege und Ing. Michael FG2 (beide jedenfalls  seit 1.1.2008-heute).

**False Positives:**

- `Ing. Michael FG` — partial — gold is substring of pred: `Ing. Michael`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Michael`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_166`)


8.400 €……Ing. Eduard FG4 (jedenf. 1.1.2008-12.4.2010)  9.100 €……Ing. Eduard FG4 (13.4.2010-25.1.2015)  8.400 €……Ing. Eduard FG4 (ab 26.1.2015)  35.000 € …Summe

**False Positives:**

- `Ing. Eduard FG` — no gold match — likely missing annotation
- `Ing. Eduard FG` — no gold match — likely missing annotation
- `Ing. Eduard FG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_288`)


Dies folgt  daraus, dass Ing. VN3 S1 in dieser Zeit (bis 25.9.2011) der einzige organschaftlich bestellte  Geschäftsführer der Bf war (Firmenbuchauszug Bf; siehe oben Pkt 2), und dass die  Lenkungstätigkeiten der OG in Bezug auf alle Konzerngesellschaften (darunter auch die Bf)  immer durch alle OG-Gesellschafter (Vorlageantrag 23.7.2018, S. 5) durchgeführt worden sind.

**False Positives:**

- `Ing. VN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_290`)


Ab 26.9.2011 bis jedenfalls Ende 2012 bis jedenfalls Ende 2015 wurde die Rusnok IT GmbH durch den  Gesellschafter – Geschäftsführer Ing. VN1 S1 überwacht und gelenkt . Es gab in diesem Teil des  Streitzeitraums (26.9.2011 – jedenfalls 31.7.2014) noch einen Prokuristen, der nicht an der Bf  beteiligt war.

**False Positives:**

- `Ing. VN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rusnok IT GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch der Richter R. in der Beschwerdesache Dipl.-Ing. Emma Chatzistamatis, Senden 22, 4673 Unterbergham, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 17. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierten Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019, Steuernummer 59-959/5444, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Emma Chatzistamatis` — partial — pred is substring of gold: `Dipl.-Ing. Emma Chatzistamatis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Emma Chatzistamatis`(person)
- `Senden 22, 4673 Unterbergham, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `59-959/5444`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/139401.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139401.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Dr. Dipl.-Ing. Laurence Goetke,  Unterernsthofen 11, 9311 Leiten, Österreich, vertreten durch STB, Adr1, über die Beschwerde vom 10. Dezember 2019  gegen den Bescheid des A vom 12. November 2019 betreffend Umsatzsteuer 2012,  Steuernummer 42-698/5318, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ing. Laurence Goetke` — partial — pred is substring of gold: `Dr. Dipl.-Ing. Laurence Goetke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dipl.-Ing. Laurence Goetke`(person)
- `Unterernsthofen 11, 9311 Leiten, Österreich`(address)
- `42-698/5318`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Deborah Stöbesand  in der Beschwerdesache des  Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke, Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich, über die Beschwerde vom 9. Juli 2022 gegen den Bescheid des  FA Waldviertel  vom 7. Juli 2022 betreffend Abweisung eines Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommensteuer für die Jahre 2017 bis 2019 zu Steuernummer  37-369/8758  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Ing. Laurence Wiebecke` — partial — pred is substring of gold: `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Deborah Stöbesand`(person)
- `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`(person)
- `Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich`(address)
- `FA Waldviertel`(organisation)
- `37-369/8758`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_27`)


dieses Bild fügen sich auch die Meldeauskünfte betreffend die Bf und ihrem Lebensgefährten  (= „Partner“) Ing. VN LG: Der Lebensgefährte der Bf hat seit 30.11.2011 bis jedenfalls 31.1.2023  seinen Hauptwohnsitz an derselben Adresse wie die Bf gehabt (Meldeauskunft betreffend den  Lebensgefährten der Bf vom 31.1.2023;

**False Positives:**

- `Ing. VN LG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_16`)


ab  28.01.2015 bis 03.10.2019 änderten sich die Beteiligungsverhältnisse auf 24% XX und 76%Möhlmeyer Immobilien GmbH  Als ihre handelsrechtlichen Geschäftsführer agierten bis 05.02.2021 Ing. BB (geb.  xx.xx.xxxx) einerseits bzw. ab 31.03.2006 XX andererseits.

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `%Möhlmeyer Immobilien GmbH`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_20`)


An ihr sind seit dem  Jahr 2002 Ing. BB (geb. xx.xx.xxxx) zu 34 %, Ing. CC (geb. xx.xx.xxxx) und DD (geb. xx.xx.xxxx) zu  je 33 % beteiligt;

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation
- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_21`)


Ing. BB und Ing. CC fungierten im Beschwerdezeitraum weiters als deren  handelsrechtliche Geschäftsführer;

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation
- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_26`)


Ing. BB, Ing. CC und DD waren in nachfolgenden Zeiträumen – über die Möhlmeyer Immobilien GmbH- an der  Rechtsvorgängerin der Bf. in folgendem Ausmaß beteiligt:  Zeitraum Gesellschafter Beteiligung  16.04.2010 - 27.01.2015 Ing. BB 25,16%   Ing. CC 24,42%   DD 24,42%  27.01.2015 - 03.10.2019 Ing. BB 25,84%   Ing. CC 25,08%   DD 25,08%

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation
- `Ing. CC` — no gold match — likely missing annotation
- `Ing. BB` — no gold match — likely missing annotation
- `Ing. CC` — no gold match — likely missing annotation
- `Ing. BB` — no gold match — likely missing annotation
- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 6

**Gold Entities:**

- `Möhlmeyer Immobilien GmbH-`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_29`)


Als deren Gruppenträgerin fungierte die Möhlmeyer Immobilien GmbH   Mit Gesellschaftsvertrag vom 15./16.05.2006 wurde die EE OEG (nunmehr EE OG; LG  Klagenfurt zu FN xxxxxxx) (erneut) mit dem Sitz in der politischen Gemeinde Ort und der  Adresse in Ort Adresse von Ing. BB (geb. xx.xx.xxxx;

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möhlmeyer Immobilien GmbH`(organisation)
- `LG  Klagenfurt`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_31`)


Beteiligung am Vermögen: 33 %) und Ing. CC (geb. xx.xx.xxxx;

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_33`)


Ing. DD schied in der  Folge per 31.12.2011 als unbeschränkt haftender Gesellschafter aus, welche Funktion er  jedoch per 24.10.2016 wieder aufnahm.

**False Positives:**

- `Ing. DD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_56`)


Ing. CC war in jenen Zeiträumen, in denen er  lediglich zu 24,42% an der Bf. beteiligt war, nicht aufgrund gesellschaftsvertraglicher  Sonderbestimmungen weisungsfrei gestellt. Es kann weiters für die Periode vom 16.04.2010 -  27.01.2015 nicht festgestellt werden, ob dieser Gesellschafter bei der Leistungserbringung  weisungsfrei oder aber weisungsgebunden war bzw. ob für ihn im Zusammenhang mit der  Leistungserbringung ein Unternehmerwagnis bestand.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_70`)


so auch  Ing. CC im Zuge der mündlichen Verhandlung im parallel geführten Vorverfahren  RV/4100093/2018 und RV/4100775/2019 vom 6.7.2021, S. 3).

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_71`)


Die Feststellungen zur  Vertretung der Gesellschafter beruhen ebenso auf den Angaben des Ing. CC in den parallel  geführten Vorverfahren RV/4100093/2018 und RV/4100775/2019 (vgl. Protokoll vom 6.7.2021,  S. 5).

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_79`)


Ing. CC führte im Zuge der mündlichen Verhandlung  vom 6.7.2021 in den parallel geführten Vorverfahren RV/4100093/2018 und  RV/4100775/2019, S. 3. auf Frage des Gerichtes nach Leistungsaufzeichnungen aus, dass solche  nicht existieren würden, „dies wäre auch gar nicht möglich gewesen, wir haben  Managementleistungen für die gesamte Gruppe erbracht, da kann ich ja nicht mit der Stoppuhr  dastehen und mitstoppen, für welche GmbH ich konkret wie viel geleistet habe“, bzw. gab auf  Nachfrage, wie man die strittigen Tätigkeiten pro Tochter bzw. für die Holding unterscheiden  könne an, dass dies de facto nicht möglich sei, da diese „ineinander über (gingen, Anm. der  Verf.), ich habe nicht einmal den Holding-Hut auf und dann den Bf.-Hut, ich habe nur den Bf.- Hut auf“ (VH-Protokoll in den parallel geführten Vorverfahren RV/4100093/2018 und  RV/4100775/2019 vom 6.7.2021, S. 9).

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_93`)


Fakt ist, dass zwischen  der Bf. einerseits und der OG bzw. dessen (unter 25% beteiligten) Gesellschafter Ing. CC  andererseits, eine (persönliche) Weisungsungebundenheit nicht ausdrücklich, und in einer  jeden Zweifel ausschließenden Art und Weise bzw. auch nach außen in Erscheinung tretend  vereinbart worden ist.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_98`)


Auch hat das Beweisverfahren keine weiteren Anhaltspunkte  dafür ergeben, dass der (unwesentlich beteiligte) Gesellschafter den Weisungen der Bf. (etwa  ihres Geschäftsführers, dem wesentlich beteiligten Ing. BB) unterstanden wäre.

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_100`)


Auch konnte ein mit der Tätigkeit für den Gesellschafter Ing. CC verbundenes Risiko nicht  festgestellt werden: So wurden – wie aus den festgestellten Akonti ersichtlich – regelmäßige,  nicht unbeträchtliche Zahlungen an die OG geleistet.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_101`)


Nach messbaren Erfolgen zu leistende  Vergütungen waren gerade nicht vereinbart, sondern richtete sich die Höhe der Pauschale  nach der jeweiligen Größe des Gruppenmitgliedes selbst (vgl. Ing. CC in den parallel geführten  Vorverfahren RV/4100093/2018 und RV/4100775/2019, VH-Protokoll vom 06.07.2021, S. 3).

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_116`)


Es bleibt auch schleierhaft, wie die Parteien  auf den in den Vereinbarungen genannten Stundenaufwand gekommen sind, hat doch der  Gesellschafter Ing. CC selbst expressis verbis im Zuge der mündlichen Verhandlung vom  6.7.2021 in den parallel geführten Vorverfahren RV/4100093/2018 und RV/4100775/2019, S.  3. auf Frage des Gerichtes nach Leistungsaufzeichnungen ausgeführt, dass solche nicht  existieren würden, „dies wäre auch gar nicht möglich gewesen, wir haben  Managementleistungen für die gesamte Gruppe erbracht, da kann ich ja nicht mit der Stoppuhr  dastehen und mitstoppen, für welche GmbH ich konkret wie viel geleistet habe“, bzw. auf  Nachfrage, wie man die strittigen Tätigkeiten pro Tochter bzw. für die Holding unterscheiden  könne ausgeführt, dass dies de facto nicht möglich sei, da diese „ineinander über (gingen, Anm.  der Verf.), ich habe nicht einmal den Holding-Hut auf und dann den Bf.-Hut, ich habe nur den  Bf.-Hut auf“ (VH-Protokoll in den parallel geführten Vorverfahren RV/4100093/2018 und  RV/4100775/2019 vom 6.7.2021, S. 9).

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_206`)


Ein derartiger Fall liegt gegenständlich vor, da –  wie im Sachverhalt festgestellt – nicht alle Gesellschafter in den Streitjahren wesentlich iSd §  22 Z 2 2TS EStG 1988 an der Bf. beteiligt waren: Vom 16.4.2010 bis 27.01.2015 hielt – soweit  für das gegenständliche Verfahren relevant - Ing. CC lediglich 24,42% der Anteile, sodass für ihn  § 22 Z 2 2 TS EStG 1988 nicht einschlägig ist.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_207`)


Sohin erstreckt sich die Bindungswirkung des  Erkenntnisses vollumfänglich nur auf den in den Streitjahren stets wesentlich beteiligten  Gesellschafter Ing. BB; für Ing. CC entfaltet die Entscheidung lediglich für jene Zeiten  Bindungswirkung, in denen auch er mit mehr als 25% beteiligt war.

**False Positives:**

- `Ing. BB` — no gold match — likely missing annotation
- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_223`)


d. Dienstverhältnis iSd § 47 Abs 2 EStG 1988 (Einkünfte nach § 25 Abs. 1 lit a EStG  1988)  Fraglich ist, ob die an den Gesellschafter Ing. CC in der Phase seiner nicht wesentlichen  Beteiligung gezahlten Beträge als Bezüge und Vorteile aus einem bestehenden oder früheren  Dienstverhältnis im Sinne des § 25 Abs. 1 lit a EStG 1988 anzusehen sind, da der  Dienstgeberbeitrag (und dem folgend der Zuschlag zum Dienstgeberbeitrag) nach § 41 FLAG  auch für alle Dienstnehmer, die in einem Dienstverhältnis iSd § 47 Abs. 2 EStG 1988 stehen, zu  leisten ist.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_236`)


Da der Gesellschafter Ing. CC kontinuierlich und über einen längeren Zeitraum die  festgestellten Aufgaben in Bezug auf – wie die Bf. selbst ausgeführt hat – Strategieplanung,  Coaching/Supervision der GF, Bankverhandlungen und Personalrecruiting wahrgenommen hat,  ist das Merkmal der Eingliederung in den betrieblichen Organismus der Bf. zweifelsfrei  gegeben.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_245`)


Für jene  Zeiträume jedoch in denen der Gesellschafter Ing. CC nicht wesentlich beteiligt war, stellen die  Leistungen Einkünfte aus nichtselbständiger Arbeit iSd § 25 Abs 1 lit a leg. cit.

**False Positives:**

- `Ing. CC` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Carl Paulitschky-Gasse` — partial — pred is substring of gold: `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Ing. Marion Kloefkorn`(person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`(address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `40-620/0106`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_190`)


Zu Vitamin B verwies  sie auf die Verschreibung von Neurobin durch Fr.Dipl.-Ing. Joseph Szwarz Dieses enthalte so viele andere  Zusatzstoffe.

**False Positives:**

- `Ing. Joseph Szwarz Dieses` — positional overlap with gold: `Fr.Dipl.-Ing. Joseph Szwarz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fr.Dipl.-Ing. Joseph Szwarz`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_82`)


Zu dem Vorbringen im Vorlageantrag wurde seitens des Sozialministeriumservice am  17.4.2024 folgende ergänzende Stellungnahme abgegeben:  "Die Gutachten von Prof.PhD Doris Goessing sind schlüssig.

**False Positives:**

- `PhD Doris Goessing` — partial — pred is substring of gold: `Prof.PhD Doris Goessing`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.PhD Doris Goessing`(person)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_343`)


M.M.B. ist Mieterin der Top 3, obwohl Ing. M.M.A. die Wohnung Top 1 im Ausmaß  von 193,2 m2 gemietet hat.

**False Positives:**

- `Ing. M.M` — positional overlap with gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.B.`(person)
- `M.M.A.`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_345`)


Der Benutzer der noch nicht fertiggestellten Wohneinheit Top 2 ist der Sohn des Ing. M.M.A..  Statt der Fertigstellung der Wohneinheit Top 2 sind andere Gebäude bzw. Wohneinheiten  (Saunahaus, Ausbau der Wohneinheiten Top 6 und Top 7) errichtet worden.

**False Positives:**

- `Ing. M.M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_346`)


Die besonders luxuriöse Ausstattung der Wohneinheit Top 1 erfolgt nach den Wünschen und  Vorstellungen des Gesellschafters und Geschäftsführers Ing. M.M.A. (z.B. Kosten für a) Küche  und Esszimmer: 90.664,40 € netto; b) "Specksteinofen": 18.200,00 € netto).

**False Positives:**

- `Ing. M.M` — positional overlap with gold: `M.M.A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/147373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147373.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Friedhelm Weigmann  in der Beschwerdesache Dipl.-Ing. Sibylle Leichnam,  Anton-Hölzl-Hof 173, 4890 Ziegelstadl, Österreich, über die Beschwerde vom 16. März 2023 gegen den Bescheid des FA Baden Mödling  vom 15. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022,  Steuernummer 10-035/7116, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Sibylle Leichnam` — partial — pred is substring of gold: `Dipl.-Ing. Sibylle Leichnam`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Friedhelm Weigmann`(person)
- `Dipl.-Ing. Sibylle Leichnam`(person)
- `Anton-Hölzl-Hof 173, 4890 Ziegelstadl, Österreich`(address)
- `FA Baden Mödling`(organisation)
- `10-035/7116`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ing. Leya Mentzel` — partial — pred is substring of gold: `Mag.a Dipl.-Ing. Leya Mentzel, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Alessia von Bauer  in der Beschwerdesache  Dimitri Seelos, geb. am 19. November 1987  und Dipl.-Ing. Luna Goedecken, BEd MA, geb. am 12. April 1988  als Erben  des Reneé Keles, verstorben am 3. November 1972  über die Beschwerde vom 15. Dezember 2020  gegen die Bescheide des Finanzamtes Österreich vom 27. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2015 bis 2019;

**False Positives:**

- `Ing. Luna Goedecken` — partial — pred is substring of gold: `Dipl.-Ing. Luna Goedecken, BEd MA`

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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_25`)


Mit 3. November 1972  verstarb der Bf. Mit Einantwortungsbeschluss des Bezirksgerichtes  Mattighofen vom 06.06.2023 wurde die Verlassenschaften den erblichen Kindern Dimitri Seelos  und Dipl.-Ing. Luna Goedecken, BEd MA  nach Abgabe einer unbedingten Erbserklärung eingeantwortet.

**False Positives:**

- `Ing. Luna Goedecken` — partial — pred is substring of gold: `Dipl.-Ing. Luna Goedecken, BEd MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `3. November 1972`(date)
- `Dimitri Seelos`(person)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)

</details>

---

## `Standalone Names in Context (von ... von)` 💣

**F1:** 0.003 | **Precision:** 0.158 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `c993fc87`  
**Description:**
Matches standalone names appearing in contexts like 'von ... von' or 'bei ... bei', capturing full names including suffixes.

**Content:**
```
(?:von\s+)([A-Z][a-zA-Z]+(?:[ -][A-Z][a-zA-Z]+)+)(?:,?\s*(?:LL\.M(?!.*LLM)|LLB(?!.*LLB)|BEd(?!.*BEd)|B\.K(?!.*BK)|Dipl\.Kfm(?!.*Kfm)|MA(?!.*MA)|MBA(?!.*MBA)|MSc(?!.*MSc)|MAS(?!.*MAS)|Bakk\. rer\. nat(?!.*nat)|Bakk\. art\. BEd(?!.*BEd)))?(?=\s+(?:von|und|oder)|,|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.158 | 0.002 | 0.003 | 19 | 3 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 16 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_138`)


Stellungnahme zu Vorgutachten:   unverändert zum VGA   Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:   x ja   □ nein   GdB liegt vor seit: 05/2018   Begründung – GdB liegt rückwirkend vor:   siehe Vorgutachten   x Dauerzustand   Gutachten erstellt am 21.09.2020 von Sandro Vulbrecht  Gutachten vidiert am 21.09.2020 von Janet Aspenleitner

| Predicted | Gold |
|---|---|
| `Janet Aspenleitner` | `Janet Aspenleitner` |

**Missed by this rule (FN):**

- `Sandro Vulbrecht` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lieselotte Reinicker` | `Lieselotte Reinicker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria-Luise Wohlmayr` (person)
- `Raingasse 32, 9552 Ossiachberg, Österreich` (address)
- `Dr. X` (person)
- `Finanzamtes` (organisation)
- `FA Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi über die am 25. Mai 2022 eingebrachte  Beschwerde von Elvira Akcakaya, Dr. Ludwig-Straße 12, 4184 Neuling, Österreich, Firmenbuchnummer FN gegen die an  Beschuldigte gerichtete Vollstreckungsverfügung des Magistrates der Stadt Wien (MA 6 – BA  32) vom 18. Mai 2022, Zahl MA67/Zahl/2021, beschlossen:  Gemäß § 50 in Verbindung mit (iVm) § 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  die Beschwerde als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Elvira Akcakaya` | `Elvira Akcakaya` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_25`)


Ich beantrage eine bescheidmäßige Erklärung von Ihrer Seite, dass mit der Weitergabe von  Daten der Zulassungsbesitzerin keine Verletzung des Datenschutzgesetzes vorliegt."

**False Positives:**

- `Ihrer Seite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_21`)


– eine Rechnung von memoryking GmbH & Co KG, Berlin, vom 01.12.2018 über ein „deleyCON  2m Optisches Digital Audio Kabel SPDIF – 2x Toslink Stecker Digitalkabel Audiokabel LWL  Digitales Lichtwellenleiter Kabel – Schwarz/Blau“ in Höhe von 6,44 €, (= Rechnung Nr. 13 laut  Auflistung),  – eine Rechnung von amazon.de vom 22.07.2019 (Bestellung vom 17.10.2018) über ein  „Zubehör für Gopro, ccbetter Action Kamerahalterungen für Gopro hero 7 hero 2018 hero 6  Hero 4 Hero 5 Session Hero 1 2 3 3+ für die meisten Sportkameras mit Fall (Schwarz)“ in Höhe  von 19,27 €, (= Rechnung Nr. 14 laut Auflistung),  – eine Rechnung von AfB social & green IT, Ettlingen, vom 30.07.2018 über eine „Logitech 920- 003967 Wireless Combo MK330 – schnurlos Tastatur und Computermaus /2,4 GHz, USB,  QWERTZ deutsches Tastaturlayout) schwarz“ in Höhe von 44 €, (= Rechnung Nr. 15 laut  Auflistung),  – eine Rechnung von Yuanchuang e-business co.LTD., vom 21.05.2018, an C, Adresse2, über  einen „X-Sense CO03D CO Melder Kohlenmonoxid CO-Detektor Batteriebetrieben Sensor und  Alarm mit Digitalanzeige und Höchstwertspeicherung“ in Höhe von 29,99 €, (= Rechnung Nr. 16  laut Auflistung),  – eine Rechnung von SYNCWIRE UK LTD, Manchester, vom 02.04.2018 über ein „DisplayPort  Kabel – 2M Syncwire Vergoldetes DisplayPort zu DisplayPort Kabel High-Speed Auflösung Kabel  unterstützt Fire TV, Apple TV, Ethernet, Aud“ in Höhe von 8,99 €, (= Rechnung Nr. 17 laut  Auflistung),  – eine Rechnung von converter-shop.com, Berlin, vom 16.02.2018 über einen „Bronson++ HE-D  800 – 110 Volt Spannungswandler / Transformator – 800 Watt – In: EURO 220 – 240 Volt / Out:  USA 110 Volt – Ringkerntransformator 800W“ in Höhe von 79,99 €, (= Rechnung Nr. 18 laut  Auflistung),  – eine Rechnung vom RANKEI UK LTD, Manchester, vom 27.09.2018 über ein „Rankie  Verbindungskabel Displayport (DP) auf HDMI, 4K Auflösung Kabel, 1,8 m, Schwarz“ in Höhe von  7,99 €, (= Rechnung Nr. 19 laut Auflistung),  – eine Rechnung vom Hoomil, Shenzhen, vom 24.11.2018, an D, Adresse3, über eine „HOOLIL  Galaxy S7 Hülle, Premium Handy Schutzhülle für Samsung Galaxy S7 Hülle Leder Wallet Tasche  Flip Brieftasche Etui Schale, Schwarz (H3011)“ in Höhe von 12,35 €, (= Rechnung Nr. 20 laut  Auflistung),  – eine Rechnung vom John’s Handy, Wien, vom 27.07.2018, ohne Angabe des Namens und der  Anschrift des Abnehmers der Lieferung, über ein „Samsung galaxy s7 gold SN/IMEI:  356457097886024“ in Höhe von 339 €, (= Rechnung Nr. 21 laut Auflistung),  5 von 18 Seite 6 von 18

**False Positives:**

- `SYNCWIRE UK LTD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `memoryking GmbH & Co KG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_16`)


Danach seien monatliche Zahlungen von Herrn WS,  dem Gatten der Gesellschafterin der Bf, in Höhe der Kreditraten auf das Konto der Bf getätigt  worden.

**False Positives:**

- `Herrn WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_112`)


Die Mietzinszahlungen in den Jahren 2004 und 2005 wurden nicht von Herrn MS,  sondern von der S-OEG getätigt.

**False Positives:**

- `Herrn MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_113`)


Auch die Betriebskosten wurden nicht, wie im Mietvertrag vereinbart, von der Nutzerin der  Wohnung beglichen, sondern von Herrn WS, dem Gatten der der Gesellschafter- Geschäftsführerin.

**False Positives:**

- `Herrn WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_78`)


Zur Jahresfrist, die aus  der Verwaltungspraxis bei Aufnahme einer aktiven Tätigkeit als schädlich betrachtet wird, darf  noch auf die kritische Würdigung von Kanduth-Kristen, § 37 Rz. 35 Jakom EStG12, hingewiesen  werden.

**False Positives:**

- `Kanduth-Kristen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_110`)


Mit Vorlagebericht vom 20.12.2017 legte das Finanzamt die Beschwerde des Bf. dem BFG zur  Entscheidung vor und führte in der diesbezüglichen Stellungnahme u.a. aus, dass bis dato keine  Bestätigungen von Western Union oder Money Gram, die die Geldbehebung durch die  Empfänger bestätigen würden, vorgelegt worden wären.

**False Positives:**

- `Western Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `BFG`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_116`)


BFG 12. 11. 2015, RV/5101378/2015), um Vorlage der im  beiliegenden Vorlagebericht des Finanzamtes vom 20. Dezember 2017 angesprochenen  fehlenden Nachweise (Bestätigungen von Western Union oder Money Gram betreffend der in  7 von 22 Seite 8 von 22

**False Positives:**

- `Western Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Finanzamtes`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/140407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140407.1_20`)


In der umfangreichen Stellungnahme vom 23.04.2018 legte der Prüfer im Wesentlichen  u.a. dar:  Im Zuge der Betriebsprüfung bei GmbH1 (GmbH 1), wurde festgestellt, dass zwischen einer  Reihe von Immobilien-Handel-KGs und der GmbH 1 in den Geschäftsjahren bis 2007  Vereinbarungen über die Bereitstellung von Immobilien gegen Anzahlungen getroffen wurden.

**False Positives:**

- `Immobilien-Handel-KGs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_31`)


Das Erfordernis des Hauptwohnsitzes im  Inland gilt nicht für Staatsangehörige von EWR-Vertragsstaaten, falls Zustellungen durch  Staatsverträge mit dem Vertragsstaat des Wohnsitzes des Zustellungsbevollmächtigten oder  auf andere Weise sichergestellt sind.

**False Positives:**

- `EWR-Vertragsstaaten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_281`)


Zudem sind im Rahmen einer  sachgerechten Schätzung auch Umstände zugunsten des Steuerpflichtigen zu berücksichtigen  und ggf zu schätzen (vgl zB zur Schätzung von Vorsteuern Ritz, BAO6, § 184 Rz. 2).

**False Positives:**

- `Vorsteuern Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146608.1_28`)


Der Beschwerdeführer war zum fraglichen Zeitpunkt im Besitz von AMC-Aktien und hat somit  im August 2022 im Wege einer Sonderdividende APE-Aktien im Ausmaß von 2.470 Stück  bezogen.

**False Positives:**

- `AMC-Aktien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_470`)


Zur Akne-/Narbenbehandlung  07.02.2013 € 43,74 3 * Teebaum Medicamo24 Dr.S   31.05.2013 € 43,74 3* Teebaum Medicamo24 Theodora Hartzheim, BA Bakk. phil.  Ansicht FA:  Es liegt eine zeitnahe ärztliche Verordnung vom 25.3.2013 vor (Anm.: von Theodora Hartzheim, BA Bakk. phil. mit dem  Vermerk „Akne, Fructoseintoleranz, Zöliakie, Milchunverträglichkeit“).

**False Positives:**

- `Theodora Hartzheim` — similar text (different position): `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)
- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_510`)


In der Pilzmischung der Fa. Orthotherapia GmbH ist  Lutein als Inhaltsstoff angeführt, von Theodora Hartzheim, BA Bakk. phil. wurde Lutamax (Inhaltsstoff ebenfalls Lutein) als 6  Monatskur verordnet.

**False Positives:**

- `Theodora Hartzheim` — partial — pred is substring of gold: `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_111`)


3 Parteien davon seien Mieter von Frau Heumann und die 4.

**False Positives:**

- `Frau Heumann` — partial — gold is substring of pred: `Heumann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heumann`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_144`)


Die Wohnverhältnisse von Frau Heumann und Herrn Bf2 waren sowohl vor dem Kauf als auch nach  dem Kauf so gestaltet, dass das erworbene Objekt nicht für eigene Wohnzwecke angedacht  war.

**False Positives:**

- `Frau Heumann` — partial — gold is substring of pred: `Heumann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heumann`(person)

</details>

---

## `Anonymized Initials with Title (Fixed)` 🏆

**F1:** 0.019 | **Precision:** 0.098 | **Recall:** 0.011  

**Format:** `regex`  
**Rule ID:** `b1d01cdf`  
**Description:**
Matches anonymized names with titles like 'Dr.in Dok1', 'Mag. NN', or 'Dr. X' where the name part is clearly a placeholder (mixed case/numbers) or specific known patterns, including single initials like 'M.'.

**Content:**
```
(?:Dr\.in?|Mag\.a?|RA|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|OMedR|MedR|StR|OStR|KzlR|Ri|Richter|Richterin|Herrn?|Frau)\s+([A-Z]\.[A-Za-z]*|[A-Z]\.[A-Z]\.[A-Z]\.|NN|Dok[0-9]+|[A-Z]{2,})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.098 | 0.011 | 0.019 | 204 | 20 | 184 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 20 | 184 | 1831 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_274`)


Es ist dann jemand von der Firma, nämlich ein Herr M. gemeinsam mit Herrn K. zu mir  gekommen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_275`)


Frage: Haben Sie nachgefragt bei Herrn M., wer die zweite anwesende Person (gemeint ist der  kein Wort deutsch sprechende Herr K., der Geschäftsführer der e.) ist?

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_277`)


Antwort: Herr M. hat sich bei mir als Geschäftsführer vorgestellt. Herr K. sollte der „Big Boss"  sein.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_281`)


Antwort: Diese Vereinbarung wurde mit Herrn M. geschlossen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_282`)


Diese Vereinbarung wurde  Herrn K. durch Herrn M. übersetzt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_295`)


Herr K. und Herr M. waren da auch  anwesend.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_337`)


Ich habe mehrere Angebote eingeholt, diese habe ich dann Herrn M. mitgeteilt und er hat mir  dann mitgeteilt, ob er günstiger anbieten kann oder nicht.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_378`)


Ich habe die Preisverhandlungen mit Herrn M. geführt und ich habe  von M. diesen Preis verlangt, da ich bei der e. immer gleich bezahlen musste mit  Eilüberweisung, bei der Fa.F. hatte ich aber ein Zahlungsziel von 30 Tagen vereinbart.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_399`)


Bei diesem Besuch waren anwesend: ich, Herr Z, Herr K., Herr M. und die Buchhalterin  gemacht.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_83`)


Am 03.10.2012 wurde dieses Fahrzeug auf eine Frau JH mit dem Kennzeichen K3  zugelassen.

| Predicted | Gold |
|---|---|
| `JH` | `JH` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_122`)


Am  03.10.2012 wurde dieses Fahrzeug auf eine Frau JH mit dem Kennzeichen K3 zugelassen.

| Predicted | Gold |
|---|---|
| `JH` | `JH` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_124`)


Noch  dazu wurde das von GL angegebene Kennzeichen erst am 03.10.2012 für Frau JH vergeben.

| Predicted | Gold |
|---|---|
| `JH` | `JH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RI` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `James Hainig`(person)
- `Winterhalde 90, 9103 Wandelitzen, Österreich`(address)
- `Finanzamtes`(organisation)
- `85-229/2263`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Marion Endrulat`(person)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Sascha Hilcker`(person)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich`(address)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_5`)


Es liegt im Bereich der der Einrichtungen und nicht im Bereich von Herrn H.,  wann diese Unterlagen zugeschickt werden und ich ersuche diesbezüglich um Verständnis.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_7`)


Weiters übermittle ich beiliegend Rechnungen betreffend den Zeitraum, woraus hervorgeht,  dass Herr H. H. keineswegs vollversorgt war und bis zum gegenwärtigen Zeitpunkt ist und auch  ständig laufende Ausgaben hat.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_9`)


Des Weiteren musste  Herr H. auch Ausgaben tätigen für diverse Möbel, ein TV-Gerät, Kleidung, usw.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_11`)


Somit leistet Herr H. sehr wohl laufend Beiträge zu seinem Unterhalt und wird nicht  vollversorgt.“

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_13`)


Aufgrund der  geringen Einkommen der Eltern von Herrn H. wird von diesen kein Kostenbeitrag  geleistet.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_14`)


Die Ausgaben der vorgelegten Rechnungen wurden ausschließlich durch die erhöhte  Familienbeihilfe von Herrn H. finanziert.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_496`)


RA verwies auf die anwesenden Auskunftspersonen S1 und S2 A. und Z.3 zur Fleischqualität in  den Streitjahren, wiederholte die bisherigen Ausführungen zu den nahe gelegenen Lokalen  samt den unterschiedlichen Entwicklungen beim Rohaufschlag und brachte zur Geschichte der  Lokale in den Streitjahren vor, dass Herr A., bedingt durch das sehr beschränkte Platzangebot  im Lokal W-Platz, beschlossen habe, die Nieder Waldbach GmbH zu übernehmen und das Geschäft  auszuweiten.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_213`)


Bauvorhaben: Wien4 Bauträger  Die vorgebliche Fremdleistungsfirma PGIV Umwelt Entwicklung GmbH hatte ihre offizielle Geschäftsanschrift in  Firmensitz, wo auch deren angeblicher Alleingesellschafter und Geschäftsführer, Herr D. C.,  geb. 1952, unbekannten Aufenthalts, seinen gemeldeten Wohnsitz innehatte.

**False Positives:**

- `D.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_42`)


„Kuraufenthalt“ der Ehefrau des Bf.  Bezüglich der Notwendigkeit der für die Ehegattin des Bf., Frau E., beantragten Kosten für  „Kuraufenthalt“ in Höhe von Euro 1.634,31 wurde lediglich ein ärztlicher Befundbericht einer  Fachärztin für Orthopädie vorgelegt, in dem einzelne Therapien (z.B. Kälteanwendungen,  Massagen, Schlammpackungen etc.) empfohlen wurden.

**False Positives:**

- `E.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_32`)


2.2 Frau A. W erklärt hiemit, diese Rechtseinräumung anzunehmen.

**False Positives:**

- `A.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_155`)


Der in der  Anfrage der Möbel Zorkelglanz GmbH an das do. Finanzamt angeführte Sachverhalt entspreche nicht der  Vereinbarung und dem gesetzten Sachverhalt. Zu diesem Thema könnte auch Herrn DI O.C.  zeugenschaftlich befragt werden.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)
- `Finanzamt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Melinda Herrwerth`(person)
- `Dürergasse 7, 4872 Windbichl, Österreich`(address)
- `40-459/9630`(tax_number)
- `Finanzamtes  Wien 2/20/21/22`(organisation)
- `Finanzamt Österreich`(organisation)
- `Lubomir Nakajima`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_53`)


Am 05.07.2018 hat in der Kanzlei L. eine Besprechung zwischen Ida Katenstroth und Mag. F.  (Fachbereich U.) stattgefunden.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ida Katenstroth`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Inn Trikraftglanz`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_274`)


Es ist dann jemand von der Firma, nämlich ein Herr M. gemeinsam mit Herrn K. zu mir  gekommen.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_275`)


Frage: Haben Sie nachgefragt bei Herrn M., wer die zweite anwesende Person (gemeint ist der  kein Wort deutsch sprechende Herr K., der Geschäftsführer der e.) ist?

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_277`)


Antwort: Herr M. hat sich bei mir als Geschäftsführer vorgestellt. Herr K. sollte der „Big Boss"  sein.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_278`)


Herr K. hat kein Deutsch gesprochen.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_282`)


Diese Vereinbarung wurde  Herrn K. durch Herrn M. übersetzt.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_283`)


Herr K. hat dem Geschäft zugestimmt.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_295`)


Herr K. und Herr M. waren da auch  anwesend.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_296`)


Auf dem vorgelegten Bild ist Herr K. der mittlere Herr.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_399`)


Bei diesem Besuch waren anwesend: ich, Herr Z, Herr K., Herr M. und die Buchhalterin  gemacht.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_550`)


Dieser Umstand spricht für die Gutgläubigkeit der Bf.  Was die anfängliche Verwechslung des Gf. der Bf. betreffend Herrn K. betrifft, wonach er nicht  gewusst habe, welche Funktion Herr K. gehabt habe, ist entgegenzuhalten, dass sich die  Unkenntnis nur auf das erste Zusammentreffen bezog und sich der Bf. dann eine Passkopie und  die Visitenkarte von Herrn K. aushändigen hat lassen.

**False Positives:**

- `K.` — no gold match — likely missing annotation
- `K.` — no gold match — likely missing annotation
- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_551`)


Eine Überprüfung seitens des Gf. der Bf.  über die Identität des Herrn K. hat sehr wohl stattgefunden.

**False Positives:**

- `K.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_17`)


Mit Datum 09.09.2004 sei ein Mietvertrag bezüglich der Wohnung zwischen der Bf als  Vermieterin und Herrn MS (Bruder von WS) abgeschlossen worden.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_20`)


Der Mietvertrag sei von Herrn MS sowie seiner  geschiedenen Gattin als Nutzerin der Wohnung unterzeichnet worden.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_34`)


Ebenso sei es unstrittig, dass Herr WS letztlich sowohl die Betriebskosten als auch die  Kreditraten übernommen habe.

**False Positives:**

- `WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_37`)


Es sei daher nicht nur ein zeitlicher, sondern auch ein unmittelbarer Zusammenhang zwischen  der Gründung der GmbH und der Scheidung des Herrn MS gegeben.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_40`)


Als Nutznießer dieser Konstruktion komme  nur Herr MS in Betracht, um die durch die Scheidungsvereinbarung erforderliche private  Kostentragung der Wohnung in das Erscheinungsbild einer unternehmerischen Vermietung zu  kleiden.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_59`)


Herr MS habe daraus keinen persönlichen  Vorteil, weder in wirtschaftlicher noch in steuerrechtlicher Hinsicht.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_61`)


Die Form der Bezahlung der Miete sei aus steuerlicher Sicht unerheblich, da  es zu einem Vermögensabfluss aus der Privatsphäre des Herrn MS gekommen sei.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_80`)


Die Vermietung erfolgt aufgrund der, von Herrn MS im Zuge  seiner Ehescheidung übernommenen, Verpflichtung der Wohnversorgung seiner geschiedenen  Gattin und der gemeinsamen Kinder (Scheidungsvergleich vom 28.07.2003).

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_81`)


Der Mietvertrag  wurde von Herrn MS als Mieter und seiner geschiedenen Gattin als Nutzerin unterzeichnet.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_99`)


Es besteht unstrittig ein familiäres Naheverhältnis zwischen der Gesellschafter- Geschäftsführerin und dem Mieter der Wohnung Herrn MS (Schwager).

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_104`)


Aus dem Mietvertrag ergibt sich, dass Herr MS zur Bezahlung der Miete verpflichtet war.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_106`)


Da Herr MS der Schwager der Gesellschafter-Geschäftsführerin ist, handelt es sich beim Mieter  der gegenständlichen Eigentumswohnung um einen nahen Angehörigen.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_107`)


Die Wohnung wurde im Zusammenhang mit der Scheidung der Herrn MS und seinen daraus  entstandenen Verpflichtungen angemietet.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_163`)


Seit 6.8.2014 ist auch Herr DI (FH) Christian FG3 Geschäftsführer.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_287`)


Das Schwergewicht der Überwachungs- und Lenkungstätigkeiten für die Rusnok IT GmbH wurde im  Teil des Streitzeitraumes von 2010-25.9.2011 durch Herrn VN3 S1 durchgeführt, der bei seinen  Tätigkeiten von den beiden anderen Strategen (bis 25.9.2011) unterstützt wurde.

**False Positives:**

- `VN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rusnok IT GmbH`(organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_27`)


Im Zeitraum vom xx.2006 bis xx.2019 wurde ihr  Stammkapital einerseits von Herr XY (geb. xx; zu 24 bzw. 26%) und andererseits von der Firma  A (FN xxxxx; zu 76 bzw. 74 %) gehalten.

**False Positives:**

- `XY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_28`)


Seit dem xx.2019 ist Herr BB (geb. xx; zu 24%) ebenfalls  an der Bf. beteiligt;

**False Positives:**

- `BB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_31`)


Per xx.2014 wurde Herr BB als weiterer Geschäftsführer im Firmenbuch eingetragen.

**False Positives:**

- `BB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sulamith Jedwillat`(person)
- `Brandenbergweg 15, 8353 Pichla, Österreich`(address)
- `Mag. Michael Payr`(person)
- `Finanzamtes Wien 12/13/14  Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `41-852/7395`(tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Harald Hilderink`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_19`)


In dieser  Stellungnahme brachten Sie jedoch entgegen Ihrem früheren Einspruch vor, aus der Apotheke  gekommen zu sein und das Gespräch mit Herrn ML gesucht zu haben.

**False Positives:**

- `ML` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch der Richter R. in der Beschwerdesache Dipl.-Ing. Emma Chatzistamatis, Senden 22, 4673 Unterbergham, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 17. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierten Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019, Steuernummer 59-959/5444, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Emma Chatzistamatis`(person)
- `Senden 22, 4673 Unterbergham, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `59-959/5444`(tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_36`)


Zur gemeinsamen mündlichen Verhandlung (Streitsachen: 1. und 2. Zwangsstrafe) erscheinen  zwei Rechtanwälte, Herr Dr. Karl RA1, der auch als Geschäftsführer der Bf. eingetragen ist, und  Herr RA2.

**False Positives:**

- `RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Karl`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_74`)


BMF2 (BMF Sektion III, WiEReG – Registerbehörde) an STB2:  Sehr geehrter Herr STB2, für eine bessere Unterstützung müssten Sie uns bitte einige genauere  Hinweise geben.

**False Positives:**

- `STB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_82`)


Von STB2, gesendet Mittwoch, 6. Oktober 2021:   S.g. Herr BMF2, mit Dank für Ihre Hilfsbereitschaft möchte ich als ehemaliger Mitarbeiter der  FV und Freund des früheren Sektionschefs Dr. Nolz doch festhalten: Das von wem immer  erzwungene WiEReg ist nicht ganz gelungen!

**False Positives:**

- `BMF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Nolz`(person)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_93`)


Gesendet Mittwoch, 6. Oktober 2021, BMF2 an STB2:   In Ihrem Falle wäre Herr RA1 als indirekter wirtschaftlicher Eigentümer mit zwei obersten  Rechtsträgern (der Gesellschaft1 und der Gesellschaft2) mit den entsprechend gehaltenen  Anteilen zu melden.

**False Positives:**

- `RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_110`)


Herr RA1 legt Unterlagen (Mailverkehr mit STB2 vom 6. Oktober 2021) dem BFG vor.

**False Positives:**

- `RA` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_17`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  2010-12 klinischer psychologischer Kurzbefund , MA 10 Wr. Kindergärten (Mag. A.):  Asperger Syndrom . Er hat enorme Stärken im mathematischen und logisch schlussfolgerndem  Denken.

**False Positives:**

- `A.` — partial — pred is substring of gold: `Mag. A.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. A.`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_20`)


Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keines vorliegend  Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  Begründung - GdB liegt rückwirkend vor:  Herr S. X. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen: Es liegt kein Leiden vor, das eine  dauerhafte Erwerbsunfähigkeit bedingt.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_40`)


S. wurde am 1. Juli 2021 von Dr.in Dok3 untersucht und folgendes Gutachten erstellt:  Anamnese:  Siehe auch Vorgutachten vom 2.3.2021  Es wurde kein Grad der Behinderung ermittelt. Da zwar gutachterliche Diagnosen gestellt  wurden, jedoch mangels an Anspruchnahme adäquater Therapien eine für die Beurteilung  alltags relevante anhaltende Einschränkung erforderliche ärztliche Verlaufsdokumentation  nicht vorhanden ist.

**False Positives:**

- `Dok3` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_75`)


Herr S. X. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  4 von 14 Seite 5 von 14

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_93`)


Dr.in Dok3, Fachgebiet: Ärztin für Allgemein-medizin, erstellte am 31. Jänner 2022 folgendes  Aktengutachten:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Mag. W. klinische und Gesundheitspsychologin allgemein beeidigte und gerichtlich zertifizierte  Sachverständige klinisch psychologisches Privatgutachten vom 5.10.2021  Es liegt eine Asperger-Autismus-Störung vor, die zum Teil widersprüchlichen Ergebnisse,  insbesondere die Selbstbeurteilung des Mj sowie einige seiner Leistungstestergebnisse, welche  deutlich besser ausgefallen sind als es bei einer Person mit Asperger-Autismus zu erwarten  gewesen wäre, lässt sich dahingehend klären, dass der Mj wahrscheinlich auch mitbedingt  durch seine hohe Intelligenz-sich über Jahre hinweg sehr vielen sozialen Kompetenzen kognitiv  erschlossen hat und somit auf heuristischer Basis agieren kann sofern er das vorliegende soziale  Muster schnell und unbeeinträchtigt von Störvariablen erkennt.

**False Positives:**

- `Dok3` — partial — pred is substring of gold: `Dr.in Dok3`
- `W.` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_107`)


Herr S. X. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde Unfähig- keit, sich selbst den Unterhalt zu verschaffen: Es liegt keine Beeinträchtigung vor, welche eine  dauerhafte Erwerbsunfähigkeit bedingt.

**False Positives:**

- `S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_111`)


Im Gutachten vom 1. Juli 2021 stellte Dr.in Dok3 ebenfalls keinen Grad der Behinderung fest.

**False Positives:**

- `Dok3` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_112`)


Im Aktengutachten vom 31. Jänner 2022 wurde das (inzwischen vorgelegte) Privatgutachten  von MMag. W., MSc, vom 5. Oktober 2021 berücksichtigt und von Dr.in Dok3 die Erkrankung  von S. unter die Pos.Nr. 03.04.01 der Einschätzungsverordnung mit einem Gesamtgrad der  Behinderung von 30 vH rückwirkend ab Oktober 2021 eingereiht.

**False Positives:**

- `W.` — no gold match — likely missing annotation
- `Dok3` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_168`)


Im Gutachten vom 1. Juli 2021 stellte Dr.in Dok3 erneut keinen Grad der Behinderung fest, dies  mit der Begründung, dass keine aktuellen Befunde beigebracht worden seien.

**False Positives:**

- `Dok3` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_170`)


Bei der Erstellung des Aktengutachtens vom 31. Jänner 2022 lag der Sachverständigen Dr.in  Dok3 das Privatgutachten von MMag. W., MSc, vom 5. Oktober 2021 vor.

**False Positives:**

- `Dok3` — partial — pred is substring of gold: `Dr.in  Dok3`
- `W.` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in  Dok3`(person)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_171`)


In dem Gutachten stellte MMag. W., MSc, folgende Diagnose:  1. Achse: F84.5 Asperger-Syndrom  2.

**False Positives:**

- `W.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_179`)


Unter Einbeziehung der von MMag. W., MSc, in ihrem Gutachten getroffenen Diagnose reihte  Dr.in Dok3X.

**False Positives:**

- `W.` — no gold match — likely missing annotation
- `Dok3` — partial — pred is substring of gold: `Dr.in Dok3X`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Dok3X`(person)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache David Radeke, Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich, über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 18. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierte Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019,   Steuernummer 15-752/7224, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `David Radeke`(person)
- `Zanklbach 10M, 9323 Dürnstein in der Steiermark, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `15-752/7224`(tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_209`)


Somit sei, wie auch 2016, Herr MY1 (ebenfalls ein weitschichtig Verwandter) mit der Behebung  des Geldes in der türkischen Grenzregion beauftragt worden, um dieses später an die  restlichen Verwandten in bar auszuzahlen.

**False Positives:**

- `MY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_210`)


Dies sei aus dem Grund notwendig, da Herr MY1  türkischer Staatsbürger sei und es den syrischen Verwandten in der Türkei nicht möglich sei,  ein Bankkonto zu eröffnen.

**False Positives:**

- `MY` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Rebecca Hüllhorst,  Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich, über die Beschwerde vom 8. Juli 2021 gegen den Abweisungsbescheid des  Finanzamtes Österreich vom 25. Juni 2021 betreffend Familienbeihilfe für das Kind To für den  Zeitraum Februar 2020 bis Februar 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `IBV` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Rebecca Hüllhorst`(person)
- `Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_22`)


Der Beschwerde beigelegt wurde eine ärztliche Bestätigung des Psychiaters M. vom  07.12.2021, die wie folgt lautet:   „Frau H. steht bei mir in regelmäßiger Betreuung bei F33.-Rezidivierende depressive Störung.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_66`)


Dazu legt sie ein ärztliche „Attest“ vom 07.12.2021 vor mit folgendem Inhalt:   „Frau H. steht bei mir in regelmäßiger Betreuung bei F33.-Rezidivierende depressive Störung.

**False Positives:**

- `H.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_2`)


Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde der Adriana Wottge,  Ferstelgasse 22, 3282 Forsthub, Österreich, vom 20. Juli 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 14. Juli 2022, Zl. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Adriana Wottge`(person)
- `Ferstelgasse 22, 3282 Forsthub, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_22`)


Herr L. F. habe sich mit  dem Führerschein ausgewiesen (Verweis auf die beigefügte Kopie des Führerscheins).

**False Positives:**

- `L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_23`)


Betreffend der GZ. MA67/Zahl/2022 sei der Firma beim Ausfüllen der Lenkerauskunft ein  Fehler unterlaufen, der Lenker sei Herr T., 1040 Wien, Gasse1, gewesen.

**False Positives:**

- `T.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Mehmet Zappe, MA, Wiesel 24, 4632 Oberirrach, Österreich, vertreten durch Petzelbauer & Kleinhappel Rechtsanwälte, Rabensteig 8/3A, 1010  Wien, betreffend einen Antrag auf Fristsetzung gemäß Art. 133 Abs. 1 Z 2 iVm Abs. 7 B-VG vom  10. Oktober 2022 wegen Verletzung der Entscheidungspflicht, Steuernummer 51-912/4171  (SVNR 3727 040311), beschlossen:   Der Fristsetzungsantrag vom 10. Oktober 2022 betreffend die behauptete Säumigkeit des  Bundesfinanzgerichtes im Säumnisbeschwerdeverfahren gegen das Finanzamt Österreich  betreffend einen Antrag auf Familienbeihilfe für den Zeitraum März 2020 bis April 2021 wird  gemäß § 30a Abs. 1 VwGG iVm § 30a Abs. 8 erster Satz VwGG als unzulässig zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mehmet Zappe, MA`(person)
- `Wiesel 24, 4632 Oberirrach, Österreich`(address)
- `51-912/4171`(tax_number)
- `3727 040311`(social_security_number)
- `Bundesfinanzgerichtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des Chantal Franzk,  Feldererweg 14 - 20, 5166 Rudersberg, Österreich, vom 14. Juni 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 31. Mai 2022, GZ MA 67/Z2/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit §  4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Berufungsverhandlung am 19. September 2022, im  Beisein der Schriftführerin IP, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Chantal Franzk`(person)
- `Feldererweg 14 - 20, 5166 Rudersberg, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_65`)


Anstatt dessen wurde eine Kopie des Originalparkscheins mit dem Stempel „beglaubigte  Kopie“ vorgelegt, dem ein Schreiben des öffentlichen Notars Mag. P. mit folgendem Text  beigefügt war: „Diese Kopie stimmt mit der Vorderseite des mir vorliegenden Originals  vollkommen überein.

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_84`)


Anstatt dessen wurde eine Kopie des Originalparkscheins mit dem  Stempel „beglaubigte Kopie“ vorgelegt, dem ein Schreiben des öffentlichen Notars Mag. P. mit  folgendem Text beigefügt war: „Diese Kopie stimmt mit der Vorderseite des mir vorliegenden  Originals vollkommen überein.

**False Positives:**

- `P.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_5`)


Frau F. M. kommt  an die psychologische Universitätsambulanz der X Privatuniversität um eine  Autismusdiagnostik durchführen zu lassen.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_6`)


…  Anamnese:  Die Anamnese wurde mit Frau F. persönlich am 23.10.2019 durchgeführt.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_7`)


Frau F. ist aktuell 27  Jahre alt (Identität überprüft), ledig und lebe alleine in einer Wohnung in Wien.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_12`)


Als Grund vermutet Frau F. unter anderem die mangelnde Struktur der von ihr  besuchten „Alternativ-Schule“ und die vorliegende Legasthenie.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_21`)


In Hinblick auf ihre familiäre Situation berichtet Frau F., dass ihre Eltern verheiratet seien und  sie eine jüngere Schwester (25) habe.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_24`)


Bis auf eine Pollenallergie verneint Frau F. die Frage nach körperlichen Beschwerden oder einer  regelmäßigen Einnahme von Medikamenten.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_28`)


Ihre  sexuelle Entwicklung beschreibt Frau F. als unauffällig.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_29`)


In ihrer Freizeit ordne Frau F. gerne Gegenstände.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_33`)


Beispielsweise gibt die Mutter der Patientin an, dass Sie sich große  Sorgen über Frau F. Zustand mache, da sich ihre Tochter immer mehr zurückziehe und  beispielsweise auch seit dem Sommer keinen Kontakt mehr mit ihren zwei engsten Freun- dinnen habe.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_34`)


Frau F. zeige laut Aussagen ihrer Mutter kein Interesse anderen Personen,  imitiere jedoch soziale Verhaltensweisen von denen sie den Eindruck habe, dass diese sozial  erwünscht seien.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_38`)


In  Hinblick auf starre Verhaltensweisen erzählt sie, dass Frau F. jeden Abend zu ihr zu Besuch  komme und die Patientin sich irritiert fühle bzw. ihr das nicht gefalle, wenn dieses abendliche  Treffen einmal aus unterschiedlichen Gründen ausfalle.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_40`)


Frau F. erscheint jeweils pünktlich zu den ausgemachten Terminen.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_43`)


Darüber hinaus bringt Frau F. Vorbefunde sowie  Tagebucheinträge mit, welche als weitere Informationsquellen für die Befundung  herangezogen werden können.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_44`)


Auch Fragebögen und andere Testinstrumente werden Frau F.  sehr konzentriert und gewissenhaft bearbeitet.

**False Positives:**

- `F.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Case Citation Surnames` 💣

**F1:** 0.001 | **Precision:** 0.014 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `9f589fcd`  
**Description:**
Matches surnames appearing in case citations like 'C-280/10, Polski Trawertyn' or 'Rs Schmelz', capturing multi-word names.

**Content:**
```
(?:C-\d+/\d+,\s*|Rs\s+)([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*)[,.]
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.014 | 0.001 | 0.001 | 73 | 1 | 72 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 72 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_88`)


Im Urteil vom 26.10.2010, Rs C-97/09, Schmelz, hat der EuGH die Einschränkung der alten  Kleinunternehmerreglung des § 6 Abs. 1 Z 27 UStG 1994, mit der noch der inländische  Wohnsitz oder Sitz des Unternehmers Voraussetzung für deren Inanspruchnahme war, als  zulässige Beschränkung der Grundfreiheiten der Niederlassungsfreiheit und der  Dienstleistungsfreiheit beurteilt, weil sie sich als Notwendigkeit einer wirksamen  Steuerkontrolle erweise.

| Predicted | Gold |
|---|---|
| `Schmelz` | `Schmelz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_90`)


Von diesem Grundsatz der Aufteilung gemischt genutzter  Wirtschaftsgüter und Dienstleistungen sind jedoch Gebäude und Investitionsgüter  ausgenommen, da für diese in Anbetracht der ständigen EuGH-Rechtsprechung (EuGH  11.07.1991, C-97/90, Lennartz, EuGH 4.10.1995, C-291/92 Armbrecht, EuGH 8.03.2001, C- 415/98 Bakcsi, EuGH 8.05.2003, C-269/00, Seeling, EuGH 21.04.2005, C-25/03, HE;

**False Positives:**

- `Lennartz` — no gold match — likely missing annotation
- `Seeling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_103`)


Das Erkenntnis des BFG vom beispielsweise 2.04.2019, RV/5101020/2013, nimmt  klar und eindeutig Bezug auf die Entscheidung EuGH 25.7.2018, Rs C-140/17, Gmina Ryjewo, in  der der Europäische Gerichtshof nunmehr klargestellt hat, dass eine Einrichtung des  öffentlichen Rechts ein Recht auf Berichtigung der auf eine als Investitionsgut erworbene  Immobilie entrichteten Vorsteuer in Anspruch nehmen kann, wenn der Gegenstand beim  Erwerb sowohl für besteuerte als auch für nicht besteuerte Tätigkeiten verwendet werden  konnte.

**False Positives:**

- `Gmina Ryjewo` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)
- `Europäische Gerichtshof`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_17`)


I Allgemein  Das Bundesfinanzgericht erfüllt die vom EuGH in ständiger Rechtsprechung entwickelten  Kriterien als Gericht iSd Art 267 AEUV (zuletzt EuGH vom 20. September 2018, Rs C-546/16,  Montte SL, Rn 22, 23) und ist als nicht in letzter Instanz berufenes Gericht zur Vorlage von  Fragen über die Auslegung von Sekundärrecht berechtigt.

**False Positives:**

- `Montte SL` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_268`)


Verordnungen sind überdies auch unmittelbar anwendbares Unionsrecht (vgl Leidenmühler,  aaO, 31 unter Hinweis auf EuGH vom 5.2.1963, 26/62, Rs van Gend & Loos, Rn 8, 9; ders, aaO,  34 unter Hinweis auf EuGH vom 9.3.1978, 106/77, Rs Simmenthal II, Rn 17, 18).

**False Positives:**

- `Simmenthal II` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_274`)


Ebenso verkennt das BMWFJ die Unionsrechtslage mit seinen Ausführungen, dass  sich der Wohnort der Familienangehörigen in einem Mitgliedstaat der Union befinden müsse  (EuGH vom 24.1.2019, C-477/17, Balandin, Lukachenko und Holiday on Ice, Rn 38ff, sowie  EuGH vom 5.9.2019, C-801/18, Rs EU gegen Caisse pour l’avenir des enfants, Rn 49, jeweils  mwN).

**False Positives:**

- `Balandin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_299`)


Dass die Ausübung der persönlichen Freiheit  grundsätzlich nicht zu einem Rechtsverlust führen darf, zeigen ua die Urteile EuGH vom 11. Juli  2002, C-224/98, Rs D'Hoop, und EuGH vom 26. November 2009, C-363/08, Rs Slanina.

**False Positives:**

- `Rs Slanina` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_319`)


15 In der Literatur wird § 53 Abs 1 FLAG im Hinblick auf EuGH vom 10.10.1973, 34/73, Rs  Variola, kritisch gesehen (Gebhart in Lenneis/Wanke, aaO, § 53, Rz ).

**False Positives:**

- `Variola` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_417`)


Damit hätte das BMWFJ die Unionsrechtslage  verkannt, wie EuGH vom 24.1.2019, C-477/17, Balandin, Lukachenko und Holiday on Ice, Rn  38ff, sowie auf EuGH vom 5.9.2019, C-801/18, Rs EU gegen Caisse pour l’avenir des enfants, Rn  49, jeweils mwN, zeigen, wo die Familienangehörigen in der Ukraine bzw Weißrussland oder in  Brasilien den Wohnort und ihren tatsächlichen Aufenthaltsort hatten.

**False Positives:**

- `Balandin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_451`)


EuGH vom 8.9.2010, verb Rs C-316/07, C-358/07 bis C-360/07, C- 409/07 und C-410/07, Stoß, Rn 106).

**False Positives:**

- `Stoß` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_474`)


Ad Frage 9: individuell-konkreter Anspruchsfortbestand  59 Falls Frage 8 verneint wird, ist nach Ansicht des BFG fraglich, ob die Bf aus den in Rn 36, 37  und 40 dieses Beschlusses genannten Gründen einen individuell-konkreten Anspruch auf  Fortbestand der Familienbeihilfe iSv wohlerworbenen Rechten erlangt hat (vgl EuGH vom  12.6.1980, 733/79, Rs Laterza, und das in Rn 10 dieses Beschlusses erwähnte Urteil in der Rs  Slanina).

**False Positives:**

- `Laterza` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_48`)


Das Erstattungsverfahren  ist als ein durch Förmlichkeit und Strenge geprägtes Nachweisverfahren, als vereinfachtes  Verfahren konzipiert, in dem der Aspekt der zügigen und sicheren Handhabung überwiegt (vgl.  dazu die wiedergegebenen Argumente des vorlegenden Gerichtes in den Schlussanträgen des  Generalanwalts vom 12.2.1998 "Société générale", Rechtssache C-361/96, CELEX- Nr.61996C0361, Rn. 16 und Urteil des EuGH vom 11.6.1998, C-361/96, Rn. 19, CELEX- Nr.61996J0361).

**False Positives:**

- `Rn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_216`)


2.5 Wohnortklauseln des FLAG 1967 bei Unionsbezug sind nicht anzuwenden   Der Verwaltungsgerichtshof hat in mehreren Erkenntnissen unmittelbar nach dem Urteil EuGH  26.11.2009, Rs C-363/08, Romana Slanina, die Ansicht vertreten, einer in einem anderen  Mitgliedstaat der Union im gemeinsamen Haushalt mit dem Kind lebenden Unionsbürgerin (in  der Schweiz lebenden Schweizer Bürgerin) stehe nach nationalem Recht die Bestimmung des §  2 Abs. 1 FLAG 1967 entgegen.

**False Positives:**

- `Romana Slanina` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_279`)


3. 2001, C-85/99, Offermanns, EU:C:2001:166, Rn. 41, und EuGH  24.

**False Positives:**

- `Offermanns` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_280`)


10. 2013, C-177/12, Lachheb, EU:C:2013:689, Rn. 35).

**False Positives:**

- `Lachheb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_282`)


10. 2010, C-16/09, Schwemmer, Rn. 52 m. w.  N.).

**False Positives:**

- `Schwemmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_131`)


Falls die zweite Übertragung dieser Befähigung vor der  innergemeinschaftlichen Beförderung stattfand, kann diese nicht der Erstlieferung an den  Ersterwerber zugeordnet werden (vgl. EuGH 26.7.2017, C-386/16, Toridas, Rn. 36;

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_133`)


19.12.2018, C-414/17, Arex, Rn. 70).

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_108`)


Im Weiteren verweist Ida Katenstroth auf die Entscheidung  des EuGH in der Rechtssache Kreuzmayr GmbH, C-628/16, Rn. 34, die diese Ansicht wiederholt  und wie folgt ausführt: „Schließlich sind zur Feststellung, ob eine Lieferung als  „innergemeinschaftliche Lieferung“ eingestuft werden kann, die Absichten zu berücksichtigen,  die der Erwerber zum Zeitpunkt des Erwerbs des fraglichen Gegenstandes hatte, sofern sie  durch objektive Gesichtspunkte gestützt werden“.

**False Positives:**

- `Rn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ida Katenstroth`(person)
- `Kreuzmayr GmbH`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_211`)


Dabei handelt es sich wiederum um einen Umstand, der  laut EuGH zu berücksichtigen ist (vgl. C-386/16, Toridas, Rz. 44).

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_321`)


Falls die zweite Übertragung dieser Befähigung vor der innergemeinschaftlichen  Beförderung stattfand, kann diese nicht der Erstlieferung an den Ersterwerber zugeordnet  werden (vgl. EuGH 26.7.2017, C-386/16, Toridas, Rn. 36;

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_322`)


EuGH 19.12.2018, C-414/17, Arex, Rn.  70).

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_830`)


Falls die zweite Übertragung vor der  innergemeinschaftlichen Beförderung stattfand, kann diese nicht der Erstlieferung an den  Ersterwerber zugeordnet werden (EuGH Toridas, Rn. 36, EuGH 19.12.2018, C-414/17, Arex, Rn.  55 von 59 Seite 56 von 59

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_838`)


Falls die zweite Übertragung  dieser Befähigung vor der innergemeinschaftlichen Beförderung stattfand, kann diese nicht  der Erstlieferung an den Ersterwerber zugeordnet werden (vgl. EuGH 26.7.2017, C-386/16,  Toridas, Rn. 36;

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_839`)


EuGH 19.12.2018, C-414/17, Arex, Rn. 70).

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_554`)


Nach Ansicht des BFG lagen bei den Diesellieferanten keine Anhaltspunkte vor, die den Bf. als  erfahrenen Unternehmer in der Mineralölbranche erkennen lassen hätten müssen, dass er mit  seinen Erwerben an Umsätzen teilnahm, die in Umsatzsteuerhinterziehungen einbezogen  waren (vgl. etwa jüngst EuGH 3.10.2019, „Altic“SIA, C-329/18, Rn.29 und 30).

**False Positives:**

- `Rn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_559`)


Nach den Materialien zum AbgSiG 2007 (vgl. RV 270 BlgNr. 23. GP, 12 f) kommt dieser  Bestimmung nur klarstellender Charakter zu, da nach der (damaligen) Judikatur des EuGH  einem Unternehmer kein Recht auf Vorsteuerabzug zusteht, wenn er wusste oder hätte wissen  müssen, dass der betreffende Umsatz oder ein anderer Umsatz in der Lieferkette, der dem  vom Vertragspartner des Unternehmers getätigten Umsatz vorausgegangen oder nachgefolgt  ist, mit einem Mehrwertsteuerbetrug behaftet war (Hinweis auf die Urteile des EuGH vom 12.  Jänner 2006, C-354/03, C- 355/03 und C-484/03, Optigen Ltd. u.a., sowie vom 6. Juli 2006, C- 439/04 und C-440/04, Kittel und Recolta Recycling;

**False Positives:**

- `Optigen Ltd` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_560`)


vgl. etwa jüngst EuGH 3.10.2019, „Altic“  SIA, C-329/18, Rn. 29 und 30).

**False Positives:**

- `Rn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_588`)


Da die Versagung des Vorsteuerabzugsrechts eine Ausnahme vom Grundprinzip ist, das dieses  Recht darstellt, obliegt es der Steuerbehörde, die objektiven Umstände hinreichend  nachzuweisen, die belegen, dass der Steuerpflichtige vom Mehrwertsteuerbetrug wusste oder  hätte wissen müssen (vgl. die Urteile des EuGH vom 21. Juni 2012, C-80/11 und C-142/11,  Mahageben und David, Rn. 49, und vom 6. Dezember 2012, C-285/11, Bonik EOOD, Rn. 43).

**False Positives:**

- `Bonik EOOD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_66`)


2. 2022, C-430/21, RS, EU:C:2022:99, Rn. 50).

**False Positives:**

- `RS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_81`)


Daraus folgt, dass die  Gerichte die Vorschrift in dieser Auslegung auch auf Rechtsverhältnisse, die nach Inkrafttreten  dieser Vorschrift und vor Erlass des auf das Ersuchen um Auslegung ergangenen Urteils  entstanden sind, anwenden können und müssen, wenn alle sonstigen Voraussetzungen für die  Anrufung der zuständigen Gerichte in einem die Anwendung dieser Vorschrift betreffenden  Streit vorliegen (vgl. EuGH 5. 9. 2019, C-331/18, TE, EU:C:2019:665, Rn. 53; EuGH 13.

**False Positives:**

- `TE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_68`)


2. 2022, C-430/21, RS, EU:C:2022:99, Rn. 50).

**False Positives:**

- `RS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_83`)


Daraus folgt, dass die  Gerichte die Vorschrift in dieser Auslegung auch auf Rechtsverhältnisse, die nach Inkrafttreten  dieser Vorschrift und vor Erlass des auf das Ersuchen um Auslegung ergangenen Urteils  entstanden sind, anwenden können und müssen, wenn alle sonstigen Voraussetzungen für die  Anrufung der zuständigen Gerichte in einem die Anwendung dieser Vorschrift betreffenden  Streit vorliegen (vgl. EuGH 5. 9. 2019, C-331/18, TE, EU:C:2019:665, Rn. 53; EuGH 13.

**False Positives:**

- `TE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_152`)


2. 2022, C-430/21, RS, EU:C:2022:99, Rn. 50).

**False Positives:**

- `RS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_167`)


Streit vorliegen (vgl. EuGH 5. 9. 2019, C-331/18, TE, EU:C:2019:665, Rn. 53; EuGH 13.

**False Positives:**

- `TE` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_91`)


Mit dem Urteil vom 6.10.2011, Rs C-421/10, Stoppelkamp, hat der EuGH entschieden, der  Begriff des im Ausland ansässigen Steuerpflichtigen sei derart auszulegen, dass darunter der  Sitz der wirtschaftlichen Tätigkeit zu verstehen sei und nicht der private Wohnsitz.

**False Positives:**

- `Stoppelkamp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_168`)


(vgl EuGH 18.09.2019, C-32/18, Michael Moser, EuGH 22.1.2015, C- 378/14, Omislaw Trapkowski, EuGH 14.10.2010, C-16/09, Schwemmer, BFG 27.06.2023,  RV/7105857/2017)

**False Positives:**

- `Michael Moser` — no gold match — likely missing annotation
- `Schwemmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_175`)


(vgl EuGH 22.10.2015, C-378/14,  Tomislaw Trapkowski, BFG 27.06.2023, RV/7105857/2017)

**False Positives:**

- `Tomislaw Trapkowski` — partial — gold is substring of pred: `Trapkowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_177`)


(vgl VwGH 24.06.2021, Ro 2018/16/0040, unter Hinweis auf EuGH  18.09.2019, C-32/18, Michael Moser, Rn 44 und EuGH 22.10.2015, C-378/14, Tomislaw  Trapkowski, Rn 39 bis 41)

**False Positives:**

- `Michael Moser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Trapkowski`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_183`)


(Vgl EuGH 22.10.2015, C-378/14, Tomislaw Trapkowski, VwGH  24.06.2021, Ro 2018/16/0040, BFG 27.06.2023, RV/7105857/2017)

**False Positives:**

- `Tomislaw Trapkowski` — partial — gold is substring of pred: `Trapkowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_127`)


Die Umsetzung derartiger Optionen kann nur durch nationales Recht  geschehen und ist im Lichte des unionsrechtlichen Grundsatzes der Rechtssicherheit auch  erforderlich (vgl. EuGH 24.07.2003, Rs C-280/00, Altmark Trans, Rn 58ff).

**False Positives:**

- `Altmark Trans` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_128`)


Die Umsetzung derartiger Optionen kann nur durch nationales Recht  geschehen und ist im Lichte des unionsrechtlichen Grundsatzes der Rechtssicherheit auch  erforderlich (vgl. EuGH 24.07.2003, Rs C-280/00, Altmark Trans, Rn 58ff).

**False Positives:**

- `Altmark Trans` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_47`)


11.1988, C-230/87, Naturally Yours Cosmetics, Rn 16;

**False Positives:**

- `Naturally Yours Cosmetics` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_48`)


24. 10.1996, C-317/94,  Elida Gibbs, Rn 28;

**False Positives:**

- `Elida Gibbs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_49`)


3. 7. 1997, C-330/95, Goldsmiths, Rn 15; 15.10.

**False Positives:**

- `Goldsmiths` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_57`)


6. 2016, C-186/15, Kreissparkasse Wiedenbrück, Rn 47;

**False Positives:**

- `Kreissparkasse Wiedenbrück` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_58`)


11. 4. 2018, C- 532/16, SEB bankas, Rn 37 f; 28. 5. 2020, C-684/18, World Comm Trading Gfz, Rn 34.

**False Positives:**

- `World Comm Trading Gfz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_61`)


3. 2014,  C-107/13, FIRIN, Rn 57;

**False Positives:**

- `FIRIN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_62`)


28. 5. 2020, C-684/18, World Comm Trading Gfz, Rn 41.

**False Positives:**

- `World Comm Trading Gfz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_66`)


7 EuGH 11. 7.1991, C-97/90, Lennartz.

**False Positives:**

- `Lennartz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_68`)


7. 1991, C-97/90, Lennartz, Rn 12, wo der EuGH dezidiert festgehalten hat, dass  Art 20 Abs 2 der Sechsten Richtlinie (entspricht Art 187 MwStSystRL) kein Recht auf  Vorsteuerabzug entstehen lassen kann; in diesem Sinne auch EuGH 2.

**False Positives:**

- `Lennartz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_69`)


6. 2005, C-378/02,  Waterschap Zeeuws Viaanderen, Rn 38.

**False Positives:**

- `Waterschap Zeeuws Viaanderen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_86`)


5. 2001, verb Rs C-322/99  und C-232/99, Fischer, Rn 91 f; vgl auch Kuppe/Achatz, UStG5 § 12 Tz 326;

**False Positives:**

- `Fischer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_468`)


dies in Anlehnung an die Ausführungen der  Generalanwältin Kokott im EuGH-Verfahren zum Fall 8.12.2022, Rs C-378/21,Zorsynsud-Transport GmbH. Das  BFG betont darin auch, dass der Anteil unternehmerischer Leistungsempfänger sachgerecht  anhand der Art der Leistung zu schätzen ist.

**False Positives:**

- `Zorsynsud-Transport GmbH` — type mismatch — same span as gold: `Zorsynsud-Transport GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zorsynsud-Transport GmbH`(organisation)
- `BFG`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_524`)


Gleiches dürfte auch aus dem Urteil des EuGH vom 29.05.2001 in der Rechtssache C-86/99,  Freemans, zu gewinnen sein.

**False Positives:**

- `Freemans` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_549`)


Eine konkrete Prüfung der diesbezüglichen Rechtslage durch den  EuGH ist nur deshalb unterblieben, weil dem EuGH im Vorabentscheidungsersuchen und in den  gegenüber dem EuGH abgegebenen Erklärungen kein derartiges Abkommen erwähnt wurde  (vgl. EuGH 15.4.2021, C-593/19, SK Telecom, Rn 46).

**False Positives:**

- `SK Telecom` — type mismatch — same span as gold: `SK Telecom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SK Telecom`(organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_553`)


Vor diesem Hintergrund regen wir an, das BFG möge  • an den Verfassungsgerichtshof einen Normprüfungsantrag dahingehend stellen, ob die  Telekommunikationsdienste-VO BGBl II 383/2003 wegen Verstoßes gegen Art 6.1.3 des  Melbourne Agreements der ITU, BGBl III 1998/14, als gesetzwidrig aufzuheben ist, und  • dem EuGH zur Vorabentscheidung die Frage vorlegen, ob es sich bei Art 6.1.3 des Melbourne  Agreements der ITU, wenn dieses durch einen Mitgliedstaat ratifiziert und in nationales Recht  übernommen wurde, um einen völkerrechtlichen Vertrag handelt, der entsprechend den  Ausführungen des Gerichtshofes in Rn. 46 des Urteils vom EuGH 15.4.2021, C-593/19,  SK Telecom, einer Besteuerung der hier verfahrensgegenständlichen Umsätze durch einen  Mitgliedstaat entgegensteht.

**False Positives:**

- `SK Telecom` — type mismatch — same span as gold: `SK Telecom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Verfassungsgerichtshof`(organisation)
- `SK Telecom`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_390`)


Nach der Rechtsprechung des Europäischen Gerichtshofs setzt die Feststellung einer  missbräuchlichen Praxis auf dem Gebiet der Mehrwertsteuer zum einen voraus, dass die  fraglichen Umsätze trotz formaler Anwendung der Bedingungen der einschlägigen  Bestimmungen der Richtlinien und des zu ihrer Umsetzung erlassenen nationalen Rechts einen  Steuervorteil zum Ergebnis haben, dessen Gewährung dem mit diesen Bestimmungen  verfolgten Ziel zuwiderliefe, und zum anderen aus objektiven Anhaltspunkten ersichtlich ist,  dass mit den fraglichen Umsätzen im Wesentlichen lediglich ein Steuervorteil bezweckt wird  (vgl. EuGH 27.10.2011, C-504/10, Tanoarch, Rn 52;

**False Positives:**

- `Tanoarch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_334`)


Der EuGH führte zum  Vorsteuerabzug iZm missbräuchlicher Rechtsgestaltung in der Rs Halifax im Urteil EuGH vom  21.2.2003, C-255/02, aus:  „84 Wie der Gerichtshof jedoch bereits entschieden hat, bleibt nur dann, wenn kein Fall von  Betrug oder Missbrauch vorliegt, das einmal entstandene Recht auf Vorsteuerabzug  vorbehaltlich etwaiger Berichtigungen gemäß Artikel 20 der Sechsten Richtlinie erhalten (vgl. u.  a. Urteile vom 8. Juni 2000 in den Rechtssachen C-400/98, Breitsohl, Slg.

**False Positives:**

- `Breitsohl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_335`)


2000, I-4321, Randnr.  41, und C-396/98, Schlossstraße, Slg.

**False Positives:**

- `Schlossstraße` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_129`)


zu letzterer  EuGH vom 21.7.2011, Rs Scheuten Solar Technology GmbH, Rs C-397/09).“  10 von 26 Seite 11 von 26

**False Positives:**

- `Scheuten Solar Technology GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_224`)


Darüber hinaus sind  betroffene innerstaatliche Zahlungen an gemeinnützige, mildtätige oder kirchliche  Gesellschaften nicht mit grenzüberschreitenden Zahlungen an gewinnorientierte ausländische  Gesellschaften vergleichbar (EuGH 12.12.2002, C-324/00, Lankhorst-Hohorst, Rn 28).

**False Positives:**

- `Lankhorst-Hohorst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_228`)


Im Falle einer Beschränkung aus Gründen des öffentlichen Interesses muss die Beschränkung  geeignet sein, die Erreichung des fraglichen Zieles zu gewährleisten, und darf nicht über das  hinausgehen, was hierzu erforderlich ist (EuGH 12.09.2006, C-196/04, Cadbury Schweppes, RN  47).

**False Positives:**

- `Cadbury Schweppes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_264`)


Zur unionsrechtlichen Beurteilung des konzerninternen Abzugsverbots für niedrig besteuerte  Zinsen und Lizenzgebühren war schließlich insbesondere auf die folgenden Urteile des EuGH  hinzuweisen:  - EuGH 20.01.2021, C-484/19, Lexel AB,  - EuGH 04.10.2024, C-585/22, X BV.  19 von 26 Seite 20 von 26

**False Positives:**

- `Lexel AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_265`)


In der Entscheidung des EuGH vom 20.01.2021, C-484/19, Lexel AB, befasste sich der EuGH mit  einer schwedischen Regelung, die ein Abzugsverbot für bestimmte Zinszahlungen im Konzern  vorsieht.

**False Positives:**

- `Lexel AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_280`)


Rn 51: Zum anderen erfordert der Grundsatz der Verhältnismäßigkeit, falls sich der betreffende  geschäftliche Vorgang nach einer Prüfung solcher Umstände als eine rein künstliche  Konstruktion erweisen sollte, für die es keine realen wirtschaftlichen Gründe gibt, dass das  Abzugsrecht nur insoweit versagt wird, als die Zinsen den Betrag übersteigen, der ohne eine  besondere Beziehung zwischen den Vertragspartnern vereinbart worden wäre (Urteil vom 13.  März 2007, Test Claimants in the Thin Cap Group Litigation, C-524/04, Rn. 83).

**False Positives:**

- `Rn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_57`)


Im  Zusammenhang mit innergemeinschaftlichen Lieferungen kam der Gerichtshof zum  Ergebnis, dass die Bekanntgabe einer MwSt-Identifikationsnummer lediglich ein formelles  Erfordernis darstelle, das den Anspruch auf Mehrwertsteuerbefreiung nicht in Frage stellen  kann, sofern die materiellen Voraussetzungen einer innergemeinschaftlichen Lieferung  erfüllt sind (vgl. EuGH 27. September 2012, C-587/10, VSTR, EU:C:2012:592 Rn 51).

**False Positives:**

- `VSTR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_161`)


Dabei hat er  festgestellt, dass die Mehrwertsteuerrichtlinie keine Bestimmung über die Berichtigung zu  Unrecht in Rechnung gestellter Mehrwertsteuer durch den Aussteller der Rechnung enthält  und dass es unter diesen Umständen grundsätzlich Sache der Mitgliedstaaten ist, die  Voraussetzungen festzulegen, unter denen zu Unrecht in Rechnung gestellte  Mehrwertsteuer berichtigt werden kann (EuGH 11. April 2013, C-138/12, Rusedespred,  EU:C:2013:233, Rn. 25 und die dort angeführte Rechtsprechung).

**False Positives:**

- `Rusedespred` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_167`)


Der Grundsatz der Neutralität der Mehrwertsteuer verlangt es nach  Auffassung des Gerichtshofes nämlich, dass eine zu Unrecht in Rechnung gestellte  Mehrwertsteuer dann berichtigt werden kann, wenn der Rechnungsaussteller die  Gefährdung des Steueraufkommens rechtzeitig und vollständig beseitigt hat, (EuGH 2. Juli  2020, Rs C-835/18, Terracult, EU:C:2020:520, Rn. 28; 11. April 2013, C-138/12,  Rusedespred, EU:C:2013:233, Rn. 27).

**False Positives:**

- `Terracult` — no gold match — likely missing annotation
- `Rusedespred` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_186`)


Es handelt sich um die  erstmalige Ausstellung der erforderlichen Rechnung, die keine Rückwirkung entfalten  kann“ (vgl. EuGH 08. Dezember 2022, C-247/21, Luxury Trust Automobil, EU:C:2022:966,  Rn 61).

**False Positives:**

- `Luxury Trust Automobil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Role Indicators (Richter/Richterin)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6b4a900`  
**Description:**
Matches full title+name sequences following judicial roles, ensuring titles like Dr., Mag., Priv.-Doz. are included in the capture and suffixes are handled.

**Content:**
```
(?:durch\s+(?:den|die)\s+(?:Richter|Richterin|Ri))\s+(?:OMedR|MedR|StR|OStR|KzlR|LLB|VetR|Ri)?\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|Hon\.-Prof\.|DDr\.in?|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
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

## `Names in Parentheses/Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0c036bc0`  
**Description:**
Matches names appearing in specific contexts like '(Nachname wie Bf.)' or '(geboren am ...)' which often follow a name, capturing the full name.

**Content:**
```
(?:für\s+die\s+Tochter|für\s+das\s+Kind|Nachname\s+wie\s+Bf\.?)\s+([A-Z][a-z]+(?:[ -][A-Z][a-z]+)+)
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

## `Gesellschafter Full Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `46b44975`  
**Description:**
Matches full names following 'Gesellschafter', capturing multi-word names and suffixes, specifically handling cases where the name is just initials or a short form.

**Content:**
```
\bGesellschafter(?:n)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,|$))
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

## `Richter Title Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `65772489`  
**Description:**
Matches full names following 'durch den Richter' or 'durch die Richterin', handling complex titles and ensuring the full name is captured including hyphenated surnames. Handles concatenated titles like 'RichterinRi'.

**Content:**
```
(?:durch\s+(?:den|die)\s+(?:Richter|Richterin|Ri))\s+(?:OMedR|MedR|StR|OStR|KzlR|LLB|VetR|Ri)?\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|Hon\.-Prof\.|DDr\.in?|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
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

## `N.N. Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `67cddbb2`  
**Description:**
Explicitly matches the anonymized name placeholder 'N.N.' which is common in legal texts.

**Content:**
```
\bN\.N\.\b
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

## `Dr.in with Placeholder Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4624ae28`  
**Description:**
Matches anonymized names with titles like 'Dr.in Dok1' or 'Mag. NN'.

**Content:**
```
(?:Dr\.in|Mag\.|RA)\s+([A-Z]\.[A-Za-z]+)
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

## `Names after Hinsichtlich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0df3f6e6`  
**Description:**
Matches names following 'hinsichtlich' which often introduces the person of interest in administrative proceedings.

**Content:**
```
(?:hinsichtlich)\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)+)(?=,|$|[,.])
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

## `Names after Preposition 'bei' (Tightened)` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a12c3bcc`  
**Description:**
Matches names after 'bei' but explicitly excludes common location suffixes and administrative terms to prevent false positives like city names or company names. Added stricter exclusion for common Austrian town names.

**Content:**
```
\bbei\s+([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:[ -][A-Z][a-zA-Z]+)*)(?=,|$|[.](?!.*(?:Straße|Gasse|Platz|Weg|Avenue|Landstraße|Finanzamt|GmbH|AG|Gesellschaft|m\.b\.H)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 70 | 0 | 70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 70 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_82`)


Zusätzlich - als Generaldirektor der größten High-Tech Firma des Landes - waren viele Verpﬂichtungen bei Presse, Fernsehen, Regierung, Kammern und Gewerkschaften etc. wahrzunehmen.

**False Positives:**

- `Presse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_68`)


Auf  das tatsächliche Einsehen der Databox durch den Teilnehmer, beispielsweise durch ein  Öffnen, Lesen oder Ausdrucken eines Bescheides, kommt es für die Bewirkung einer  Zustellung nicht an (vgl. etwa BFG 14.2.2019, RV/7100457/2019, bzw. die bei Ritz, aaO,  genannte Judikatur).

**False Positives:**

- `Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_6`)


Das Kind wohnt bei Antragstellerin

**False Positives:**

- `Antragstellerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_18`)


Diese Rechtsverletzung ergibt sich im Detail aus  folgenden Überlegungen:   ISd § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) besteht der Anspruch auf  Familienbeihilfe bei Personen, die im Bundesgebiet einen Wohnsitz haben, für ein volljähriges  Kind, welches das 24.

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_46`)


Diese Rechtsverletzung ergibt sich  im Detail aus folgenden Überlegungen:   ISd § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) besteht der Anspruch auf  Familienbeihilfe bei Personen, die im Bundesgebiet einen Wohnsitz haben, für ein volljähriges  Kind, welches das 24.

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_43`)


§ 106a Abs. 2 EStG 1988 lautet:   (2) Für ein Kind im Sinne des § 106 Abs. 2 ist bei Steuerpflichtigen, denen der  Unterhaltsabsetzbetrag gewährt wird, von Amts wegen ein Kinderfreibetrag in Höhe von 300  Euro jährlich zu berücksichtigen.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_136`)


Diese Verpflichtung wird durch eine erhöhte  Mitwirkungspflicht der Abgabepflichtigen, wie beispielsweise bei Auslandssachverhalten,  eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_14`)


Prämien für derartige Versicherungen sind  nach der Rechtsprechung des Verwaltungsgerichtshofes eindeutig Werbungskosten und nicht  Sonderausgaben (siehe dazu bei Doralt, ESt-Kommentar, § 16 Tz 220 „Versicherungen";

**False Positives:**

- `Doralt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_44`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (siehe dazu die bei Doralt, EStG  Kommentar, § 16 Tz 220 "Versicherungen" angeführten Judikate, wie zB VwGH vom  22.10.1991, 91/14/0043) sind Prämien für eine Berufsunfähigkeitsversicherung lediglich dann  als Werbungskosten abzugsfähig, wenn ausschließlich die Berufsunfähigkeit infolge eines  4 von 7 Seite 5 von 7

**False Positives:**

- `Doralt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gleisdorf` — partial — pred is substring of gold: `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Elias Voht`(person)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_127`)


Meldungen an den Auftraggeber erfolgten  bei Beginn und Ende einer Baustelle bzw bei Problemen.

**False Positives:**

- `Problemen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_99`)


Für die Zwecke dieses Titels wird bei Personen, die aufgrund oder infolge ihrer  Beschäftigung oder selbstständigen Erwerbstätigkeit eine Geldleistung beziehen, davon  ausgegangen, dass sie diese Beschäftigung oder Tätigkeit ausüben.

**False Positives:**

- `Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_100`)


Dies gilt nicht für  Invaliditäts-, Alters- oder Hinterbliebenenrenten oder für Renten bei Arbeitsunfällen oder  Berufskrankheiten oder für Geldleistungen bei Krankheit, die eine Behandlung von  unbegrenzter Dauer abdecken.

**False Positives:**

- `Krankheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_227`)


Der Hinweis der Behörde, dass bei der Beschwerdeführerin aufgrund der Belehrungen im  Zuge der letzten Betriebsprüfung ein anderer (strengerer) Sorgfaltsmaßstab anzusetzen sei  als bei Branchenkollegen, läuft somit völlig ins Leere.

**False Positives:**

- `Branchenkollegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_49`)


Mit Beschwerdevorentscheidung vom 6.9.2019 (ergänzende Begründung vom 5.9.2019) wies  das Finanzamt die Beschwerde als unbegründet ab: „Nach der Rechtsprechung des VwGH muss  gerade bei Aufwendungen, die auch in den Kreis der privaten Lebensführung fallen können, ein  strenger Maßstab angelegt und eine genaue Unterscheidung vorgenommen werden.

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_154`)


Die Zwischensaison verbrachte die Bf. am (Haupt)Wohnsitz im Ort A-1 im Kreise ihrer Familie,  konkret bei Eltern, Schwester und Schwager und Nichte.

**False Positives:**

- `Eltern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_29`)


Daher liege das Besteuerungsrecht  über die in Rede stehenden Einkünfte ausschließlich bei Frankreich.

**False Positives:**

- `Frankreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134626.1_46`)


In diesem Fall ist nach § 54  Abs. 2 VStG vorzugehen und die Ersatzfreiheitsstrafe zu vollziehen (vgl. zB VwGH 19.05.2014,  2013/09/0126, VwGH 15.04.2020, Ra 2019/09/0105, VwGH 05.06.2020, Ro 2019/04/0228)   Seit der Novelle BGBl. I 57/2018 ist nicht nur bei Zahlungsaufschub, sondern auch bei Be- willigung eines Antrags auf Teilzahlung die Strafvollstreckung gemäß § 54b Abs. 3 letzter  Satz VStG ausdrücklich aufgeschoben;

**False Positives:**

- `Zahlungsaufschub` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_22`)


Ich bin seit Jänner 2020 in Behandlung bei Prim.

**False Positives:**

- `Prim` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_65`)


Dabei ist bei Pensionsabfindungen, die im Jahre 2001 zufließen, nach Abzug  der darauf entfallenden Beiträge im Sinne des § 62 Z 3, 4 und 5 ein Viertel steuerfrei zu belas- sen.

**False Positives:**

- `Pensionsabfindungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_68`)


Erkenntnisse vom 17. Dezember 2009, 2009/16/0188, vom 28. November 2007,  2007/15/0165, vom 20. September 2006, 2006/14/0046, jeweils mwN, vom 15. Juni 2005,  2002/13/0172, vom 29. September 2004, 2000/13/0151, und die bei Tannert,  Finanzstrafgesetz, E 15 bis E 17 zu § 49, referierte hg.

**False Positives:**

- `Tannert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_47`)


Wenn also der  Grundstückserwerber an ein bestimmtes, durch die Planung des Verkäufers oder eines mit  diesem zusammenarbeitenden Organisators vorgegebenes Gebäude gebunden ist, dann ist ein  Kauf mit herzustellendem Gebäude anzunehmen (vgl. die bei Fellner, aaO, § 5 Rz 88a  dargestellte Rechtsprechung, siehe diesbezüglich auch VwGH vom 14.10.1999, 97/16/0219,  17.10.2001, 2001/16/0230 und vom 21.3.2002, 2001/16/0429).

**False Positives:**

- `Fellner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_81`)


Die Verordnung des Bundesministers für Finanzen über die Verlagerung des Ortes der  sonstigen Leistung bei Telekommunikationsdiensten, BGBl. II Nr. 102/1997, ist nicht mehr auf  Umsätze anzuwenden, die nach Ablauf des Tages, an dem die Verordnung im  Bundesgesetzblatt kundgemacht wurde, ausgeführt werden.

**False Positives:**

- `Telekommunikationsdiensten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_136`)


Mit diesem in  Art. 11 Abs. 1 der Verordnung Nr. 883/2004 verankerten Grundsatz sollen  Ungleichbehandlungen beseitigt werden, die bei Arbeitnehmern, die innerhalb der Union zu-  und abwandern, die Folge einer teilweisen oder vollständigen Kumulierung der anwendbaren  15 von 20 Seite 16 von 20

**False Positives:**

- `Arbeitnehmern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision des Bf. an den Verwaltungsgerichtshof ist auf der Grundlage des § 25a Abs. 4  VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine Geldstrafe von  bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht mehr als 400  Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

**False Positives:**

- `Herberstein` — partial — pred is substring of gold: `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Wladimir Leukhardt`(person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich`(address)
- `Stadt Wien`(organisation)
- `Bundesfinanzgerichts`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_260`)


Ergibt sich bei Steuerpflichtigen, die Anspruch auf den Verkehrsabsetzbetrag eine  Einkommensteuer unter null, sind in der damals geltenden Fassung 50% der Werbungskosten  im Sinne des § 16 Abs. 1 Z 4 EStG 1988, das sind Beiträge zur Pflichtversicherung in der  gesetzlichen Sozialversicherung, höchstens aber 400 € jährlich rückzuerstatten (§ 33 Abs. 8 Z 2  EStG 1988).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_261`)


Ergibt sich bei Steuerpflichtigen, die Anspruch auf den Pensionistenabsetzbetrag haben, nach  Abs. 1 und 2 eine Einkommensteuer unter null, sind nach der damals geltenden Fassung des  EStG 75% der Werbungskosten im Sinne des § 16 Abs. 1 Z 4 EStG 1988, höchstens aber 500 €  jährlich rückzuerstatten (§ 33 Abs. 8 Z 3 EStG 1988).

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_114`)


Zur Unzulässigkeit der Revision  Eine Revision des Bf. an den Verwaltungsgerichtshof ist auf der Grundlage des § 25a Abs. 4  VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine Geldstrafe von  bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht mehr als  400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache RgR Denise Symang, Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich, vertreten durch Mag. Robert Bitsche,  Rechtsanwalt, Nikolsdorfergasse 7-11/15, 1050 Wien, über die Beschwerde vom 9. Oktober  2019 gegen die Bescheide des Finanzamtes Wien 4/5/10 (nunmehr Finanzamt Österreich) vom  11. September 2019 sowie vom 23. September 2019 betreffend Wiederaufnahme  Körperschaftsteuer 2015 bis 2017, Steuernummer 60-977/8084, nach Durchführung einer  mündlichen Verhandlung am 19. Dezember 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ilz` — partial — pred is substring of gold: `Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `RgR Denise Symang`(person)
- `Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich`(address)
- `Mag. Robert Bitsche`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `Finanzamt Österreich`(organisation)
- `60-977/8084`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_26`)


verbringt den Großteil der Freizeit alleine vor dem Computer,  außerhalb der Wohnung derzeit nur Spaziergänge mit dem Hund möglich  Derzeitige Beschwerden:  autismustypische Sozialverhaltensauffälligkeiten, Gefühl der Reizüberflutung, Grübelneigung,  repetitive Muster, gelegentlich Einschlafstörung, reduzierter Antrieb  Behandlungen …:  laufende fachärztlich-psychiatrische Behandlung bei DrF, Ort2;

**False Positives:**

- `DrF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_74`)


Psycho(patho)logischer Status:  allseits orientiert, Gedankengang geordnet, nachvollziehbar, erreicht das Ziel, Stimmung  ausgeglichen, Antrieb im Normbereich, Affekt stabil, gute Affizierbarkeit in beiden  Skalenbereichen  Gedächtnis, Auffassung und Aufmerksamkeit gut, Sprache unauffällig, kann sich gut  ausdrücken  Ergebnis der durchgeführten Begutachtung:  1 Insulinpflichtiger Diabetes bei stabiler Stoffwechsellage  oberer Rahmensatz bei Insulin-Sensor Pumpe, damit guter  Allgemeinzustand, HbA1C 5,7%, keine Folgeschäden                                                                       Pos. Nr. 09.02.02           GdB 40 %  Gesamtgrad der Behinderung                  40 v. H.  Begründung für den Gesamtgrad der Behinderung: einziges Leiden  Herr A ist in die Therapie und Pathophysiologie seiner Erkrankung gut eingelesen und erreicht  damit eine stabile Stoffwechsellage mit derzeit ohne Folgeschäden.

**False Positives:**

- `Insulin-Sensor Pumpe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/141222.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141222.1_124`)


Zur Unzulässigkeit der Revision  Eine Revision der Beschwerdeführerin an den Verwaltungsgerichtshof ist auf der Grundlage  des § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen  eine Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe  von nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten  ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_154`)


Zweck des § 15 Abs. 3 GebG ist es zu vermeiden, dass ein Rechtsgeschäft, das nach einem der  erschöpfend angeführten Abgabengesetze steuerbar ist, nicht überdies noch mit einer  Rechtsgebühr belegt wird (vgl. etwa die bei Fellner, Gebühren und Verkehrsteuern, Band I,  Stempel- und Rechtsgebühren, Rz 66 zu § 15 GebG wiedergegebene Rechtsprechung des  Verwaltungsgerichtshofes).

**False Positives:**

- `Fellner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/143328.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143328.1_199`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/143486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143486.1_53`)


Da es sich bei den Rückständen  beinahe ausschließlich um Selbstbemessungsabgaben handelt, die vom Abgabepflichtigen für  den Abgabengläubiger treuhändig einzubehalten und an diesen zeitgerecht abzuführen sind,  sind hier strengere Maßstäbe anzulegen als etwa bei Ertragsteuern.

**False Positives:**

- `Ertragsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_25`)


Beim nächsten Kontrollbesuch bei Dr. A3 habe die Bf. erfahren, dass für diesen  Zweck eine Einfachbrille, zugerichtet auf den cm-Abstand vom Bildschirm zweckmäßiger sei.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. A3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. A3`(person)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_29`)


Seit der  Nachlaserung von Dr. A2 stehe die Bf. unter regelmäßiger Kontrolle bei Dr. A2.

**False Positives:**

- `Dr` — similar text (different position): `Dr. A2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. A2`(person)
- `Dr. A2`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_91`)


Bleiben Sie bis zum Erhalt der Bestätigung bei Ihrem Fahrzeug.

**False Positives:**

- `Ihrem Fahrzeug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/144833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144833.1_130`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_169`)


Die  Einnahme von Vitamin D mit K2 sei mittlerweile Standard bei Osteoporose.

**False Positives:**

- `Osteoporose` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_177`)


 Allergische Reaktion bei Augen, siehe Rezept des Antiallergikers Dr. B (Anlage 6).

**False Positives:**

- `Augen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. B`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/145657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145657.1_29`)


Laut Punkt VII des Dienstvertrages ergibt sich der gewöhnliche Arbeitsort aus den infolge der  vereinbarten Tätigkeit durchzuführenden Besuchen bei Kunden.

**False Positives:**

- `Kunden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/145657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145657.1_51`)


Neben der Betreuung der Kunden zählten zu Ihrer Tätigkeit von Beginn an auch:   die Einpflege der Daten für Anfragen und Aufträge ins System,   Angebotsanfragen und Produktionsabwicklung bei Subunternehmen,   Offertlegung, Datenkontrolle und Druckfreigabeabwicklung mit den Kunden per Mail,   Faktura Vorbereitung- und Kontrolle  Ihre Arbeitsbereiche umfassten daher vorwiegenden Tätigkeiten, für die in der Druckbranche  üblicherweise der Innendienst zuständig sei.

**False Positives:**

- `Subunternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/145816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145816.1_46`)


II. Rechtliche Beurteilung  1. Gestützt auf § 17 Abs. 4 und 5 EStG 1988 normiert § 1 der Gastgewerbepauschalierungs- verordnung 2013 (BGBl. II 488/2012) in der Fassung BGBl. II 355/2020:  „(1) Bei der Ermittlung des Gewinnes bei Betrieben, für die eine Gewerbeberechtigung für  das Gastgewerbe (§ 111 der Gewerbeordnung 1994 - GewO 1994, BGBl. I Nr. 194)  erforderlich ist und während des gesamten Wirtschaftsjahres vorliegt, können nach  Maßgabe der folgenden Bestimmungen Betriebsausgaben pauschal berücksichtigt werden.

**False Positives:**

- `Betrieben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/145832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145832.1_50`)


§ 33 Abs. 7 EStG 1988 in der für das Jahr 2022 anzuwendenden Fassung durch das am 28. Juli  2022 ausgegebene BGBl. I Nr. 135/2022 lautet:  „Ergibt sich bei Steuerpflichtigen, die  – zumindest an 30 Tagen im Kalenderjahr steuerpflichtige Einkünfte gemäß § 2 Abs. 3 Z 1 bis 4  erzielen, oder  – ganzjährig Leistungen nach dem Kinderbetreuungsgeldgesetz (KBGG), BGBl. I Nr. 103/2001 ,  oder Pflegekarenzgeld bezogen haben,  nach Abs. 1 eine Einkommensteuer unter 550 Euro, gilt bei Vorhandensein eines Kindes (§ 106  Abs. 1) Folgendes:  Die Differenz zwischen 550 Euro und der Einkommensteuer nach Abs. 1 ist als  Kindermehrbetrag zu erstatten, wenn  a) der Alleinverdiener- oder Alleinerzieherabsetzbetrag zusteht oder  b) sich auch beim (Ehe)Partner gemäß § 106 Abs. 3, der Einkünfte gemäß § 2 Abs. 3 Z 1 bis 4  erzielt, eine Einkommensteuer nach Abs. 1 unter 550 Euro ergibt;

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_7`)


Er gab darin unter anderem seinen Grad der Behinderung mit  70 % an und beantragte sowohl den pauschalen Freibetrag für das auf die behinderte Person  zugelassene Kraftfahrzeug als auch behinderungsbedingte tatsächliche Kosten von EUR  20.888,- als außergewöhnliche Belastungen bei Behinderung.

**False Positives:**

- `Behinderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_41`)


Er hat für die Behandlung bei Dr. B, Facharzt für  Lungenkrankheiten, EUR 115,-bezahlt (vgl. Rechnung vom 25.11.2021 und  Überweisungsbestätigung).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. B`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. B`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_47`)


Die ärztliche Behandlung bei Dr. B, Facharzt für Lungenkrankheiten, ist nicht durch jene  Gesundheitsbeeinträchtigungen des Beschwerdeführers bedingt, welche bei der Feststellung  des Grades seiner Behinderung berücksichtigt wurden (vgl. die Ausführungen des  Beschwerdeführers in der mündlichen Verhandlung).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. B`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. B`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_72`)


Der Rechtfertigungsbedarf sei somit bei Subjektsteuern höher  als bei Objektsteuern, weil bei letzteren idR ein zumutbares Ausweichverhalten möglich sei.

**False Positives:**

- `Objektsteuern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_264`)


Während bei Stromproduzenten, ohne dies sachlich zu begründen, der Umsatz als  Bemessungsgrundlage herangezogen werde, stelle der EKB-f auf den Gewinn ab.

**False Positives:**

- `Stromproduzenten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_454`)


der Preis für alle Marktteilnehmer wird jedoch durch das letzte  Kraftwerk bestimmt, das zur Deckung der Nachfrage benötigt wird, d. h. durch das Kraftwerk  mit den höchsten Grenzkosten bei Markt-Clearing.

**False Positives:**

- `Markt-Clearing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_462`)


Zur Darlegung VII. und VIII.  Darin sind Aussagen zu „Erhöhte Lebenshaltungskosten bei Krankheiten, Individuell“ bezüglich  der erhöhten Lebensmittelkosten bei Bulimie enthalten.

**False Positives:**

- `Krankheiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_472`)


12.08.2013 € 97,08 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32  09.12.2013 € 45,00 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32  Laut den vorgelegten Belegen wurde das Osspura bei Theodora Hartzheim, BA Bakk. phil. erworben.

**False Positives:**

- `Theodora Hartzheim` — similar text (different position): `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)
- `Theodora Hartzheim, BA Bakk. phil.`(person)
- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_495`)


Das Osspura wurde bei Theodora Hartzheim, BA Bakk. phil. erworben.

**False Positives:**

- `Theodora Hartzheim` — partial — pred is substring of gold: `Theodora Hartzheim, BA Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theodora Hartzheim, BA Bakk. phil.`(person)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_513`)


Die FK von Eur 14,28 (7,14 + 7,14)  sind, da die Bestellung Online erfolgte und die Ausstellung des Privatrezeptes im Zuge der  Ordination bei Dr. B am 30.8.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. B`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. B`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_601`)


Ergibt sich  bei Steuerpflichtigen, die Anspruch auf den Arbeitnehmerabsetzbetrag oder  Grenzgängerabsetzbetrag haben, nach Abs. 1 und 2 keine Einkommensteuer, so sind 10% der  Werbungskosten im Sinne des § 16 Abs. 1 Z 3 lit. a (ausgenommen Betriebsratsumlagen) und  der Werbungskosten im Sinne des § 16 Abs. 1 Z 4 und 5, höchstens aber 110 Euro jährlich,  gutzuschreiben.

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_174`)


Obwohl der Richter hinsichtlich des oben festgestellten Sachverhaltes aufgrund der  dargestellten Erhebungsergebnisse, der aufliegenden Beweismittel und der widersprüchlichen  Aussagen des Geschäftsführers *Name* davon ausgeht, dass dieser dargestellte Sachverhalt  den Tatsachen entspricht, muss doch festgehalten werden, dass es nach ständiger Judikatur  des VwGH (siehe dazu ggfs die beispielhaft angeführten Erkenntnisse bei Ritz, BAO7, § 167, Tz  8) im Abgabenverfahren genügt, wenn von mehreren Möglichkeiten jene als erwiesen  angesehen wird, die gegenüber allen anderen Möglichkeiten eine überragende  Wahrscheinlichkeit für sich hat, die somit mit höchster Wahrscheinlichkeit den Tatsachen  15 von 32 Seite 16 von 32

**False Positives:**

- `Ritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/147055.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147055.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Karl Konstandin  in der Beschwerdesache Barbara West,  Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG, Landstraße 9, 4020  Linz, über die Beschwerde vom 27.11.2024 gegen den Bescheid des Finanzamtes Österreich  vom 6.11.2024 betreffend Abweisung eines Antrages auf bescheidmäßige Festsetzung des  Energiekrisenbeitrages-Strom (EKB-S) für den Zeitraum Jänner 2024 bis Juni 2024 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hischmannsberg` — partial — pred is substring of gold: `Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Karl Konstandin`(person)
- `Barbara West`(person)
- `Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich`(address)
- `BEURLE Rechtsanwälte GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/147867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147867.1_115`)


Zur Unzulässigkeit der Revision  Eine Revision des Bf. an den Verwaltungsgerichtshof ist auf der Grundlage des § 25a Abs. 4  VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine Geldstrafe von  bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht mehr als 400  Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_12`)


Aufgrund diverser  Schwierigkeiten (Verzögerungen bei Sanierungsarbeiten, Schimmelbefall in den EG- Wohnungen, etc.) hätte sich die Inbetriebnahme aller Einheiten verzögert.

**False Positives:**

- `Sanierungsarbeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/148534.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148534.1_37`)


Dieser Betrag erhöht sich für jedes weitere Kind (§ 106 Abs. 1) um den Betrag von 250 Euro  oder den an seine Stelle tretenden Betrag.“  § 33 Abs 7 EStG 1988 idF BGBl. I Nr. 135/2022 (für die Arbeitnehmerveranlagung 2022)  bestimmt:  „Ergibt sich bei Steuerpflichtigen, die  - zumindest an 30 Tagen im Kalenderjahr steuerpflichtige Einkünfte gemäß § 2 Abs. 3 Z 1 bis 4  erzielen, oder  - ganzjährig Leistungen nach dem Kinderbetreuungsgeldgesetz (KBGG), BGBl. I Nr. 103/2001,  oder Pflegekarenzgeld bezogen haben,  nach Abs. 1 eine Einkommensteuer unter 550 Euro, gilt bei Vorhandensein eines Kindes (§ 106  Abs. 1) Folgendes:  Die Differenz zwischen 550 Euro und der Einkommensteuer nach Abs. 1 ist als  Kindermehrbetrag zu erstatten, wenn  a) der Alleinverdiener- oder Alleinerzieherabsetzbetrag zusteht oder  b) sich auch beim (Ehe)Partner gemäß § 106 Abs. 3, der Einkünfte gemäß § 2 Abs. 3 Z 1 bis 4  erzielt, eine Einkommensteuer nach Abs. 1 unter 550 Euro ergibt;

**False Positives:**

- `Steuerpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/148832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat in der  Beschwerdesache Kevin Albani, Zillingberg 61m, 3144 Hummelberg bei Hinterholz, Österreich  Steuernummer: 62-450/1971, über die  Beschwerde vom 15. September 2023 gegen den Bescheid des Finanzamtes Österreich vom 16.  August 2023 betreffend Einkommensteuer 2020 zu Recht:    I)  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Hinterholz` — partial — pred is substring of gold: `Zillingberg 61m, 3144 Hummelberg bei Hinterholz, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Kevin Albani`(person)
- `Zillingberg 61m, 3144 Hummelberg bei Hinterholz, Österreich`(address)
- `62-450/1971`(tax_number)
- `Finanzamtes Österreich`(organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_71`)


leichte Fahrlässigkeit liegt  vor bei Fehlern, die auch einem sorgfältigen Menschen gelegentlich unterlaufen (z.B. VwGH  22.11.1996, 95/17/0112;

**False Positives:**

- `Fehlern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/149083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149083.1_137`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/149274.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149274.1_130`)


Zur Unzulässigkeit der Revision  Eine Revision der Beschwerdeführerin an den Verwaltungsgerichtshof ist auf der Grundlage  des § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen  eine Geldstrafe von bis zu € 750 verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als € 400 verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_140`)


Gem § 48 BAO kann das Bundesministerium für Finanzen (nach  der VwGH-Judikatur richtig: der Bundesminister für Finanzen, vgl. zB VwGH vom 21.7.1993,  91/13/0119) anordnen, bei Abgabepflichtigen, die der Abgabenhoheit mehrerer Staaten  unterliegen, bestimmte Gegenstände aus der Abgabenerhebung ganz oder teilweise  auszuscheiden oder ausländische, auf solche Gegenstände entfallende Abgaben ganz oder  teilweise auf die inländischen Abgaben anzurechnen, soweit dies zur Ausgleichung der in- und  ausländischen Besteuerung oder zur Erzielung einer den Grundsätzen der Gegenseitigkeit  entsprechenden Behandlung erforderlich ist.

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/149672.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149672.1_92`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu € 750 verhängt werden darf und im Erkenntnis eine Geldstrafe von nicht  mehr als € 400 verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen ist.

**False Positives:**

- `Verwaltungsstrafsachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/149721.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149721.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Mag.a Gerda Hellvogt  in der Beschwerdesache Tatjana Wolnik,  Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich, vertreten durch Mag. Ursula Zimmerl, Sternwartestraße 82, 1180 Wien, über  die Beschwerde vom 14. Juli 2025 gegen den Bescheid des Finanzamtes Österreich vom 10. Juli  2025 betreffend Zwangsstrafen 2025, Steuernummer 36-865/6597, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Salzburg` — partial — pred is substring of gold: `Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Mag.a Gerda Hellvogt`(person)
- `Tatjana Wolnik`(person)
- `Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich`(address)
- `Mag. Ursula Zimmerl`(person)
- `Finanzamtes Österreich`(organisation)
- `36-865/6597`(tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Detlev Bodenmüller`(person)
- `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.`(person)
- `Pux 4, 8753 Paßhammer, Österreich`(address)
- `Mag. Thomas Gell`(person)
- `Finanzamtes Österreich`(organisation)
- `72-997/9457`(tax_number)

</details>

---

## `Names after Company Prefix 'Fa.' (Tightened)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eb203b20`  
**Description:**
Matches names after 'Fa.' ensuring the match is a person and not a company name, by requiring a space and capital letter pattern typical of names.

**Content:**
```
\bFa\.\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*)(?=,|$|[.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_11`)


Die Zulassungsbesitzerin, Fa. ZL, Dorf, teilte der Magistratsabteilung 67 im Zuge des an sie  ergangenen Lenkerauskunftsersuchens mit, dass das Fahrzeug zur Beanstandungszeit der Fa.  E., Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich  überlassen war.

**False Positives:**

- `ZL` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/140550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140550.1_38`)


Die Kindesmutter ist seit 25. Jänner 2022 - laufend bei der Fa. XY Gesellschaft, Wien,  beschäftigt.

**False Positives:**

- `XY Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/143412.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143412.1_8`)


Entscheidungsgründe  Verfahrensgang:  Das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen Vienna, zugelassen auf die  Fa. ZL, wurde vom Parkraumüberwachungsorgan KO der Landespolizeidirektion Wien am 11.  Mai 2023 um 17:28 Uhr in der gebührenpflichtigen Kurzparkzone in 1060 Wien, Stumpergasse  24, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `ZL` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

</details>

---

## `Names in Parentheses/Context (Fixed)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6efe971a`  
**Description:**
Matches names appearing in specific contexts like '(Nachname wie Bf.)' or '(geboren am ...)' which often follow a name, capturing the full name.

**Content:**
```
(?:für\s+die\s+Tochter|für\s+das\s+Kind|Nachname\s+wie\s+Bf\.?)\s+([A-Z][a-z]+(?:[ -][A-Z][a-z]+)+)
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

## `Complex Academic Titles with Spacing` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8d838eae`  
**Description:**
Matches persons with complex academic titles that may have spacing issues (e.g., 'Univ- Prof.'), ensuring the full name is captured.

**Content:**
```
(?:Univ\-?\s*Prof\.|Priv\.-Doz\.|Dipl\. Kfm\.|Dipl\.-Ing\.|Hon\.-Prof\.)\s+(?:Mag\.a?|Dr\.in?|RgR|KzlR|LLB|VetR|Ri)?\s+[A-Z][a-zA-ZÀ-ÿ]+(?:-[A-Z][a-zA-ZÀ-ÿ]+)*(?:\s+[A-Z][a-zA-ZÀ-ÿ]+)*(?:-[A-Z][a-zA-ZÀ-ÿ]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc|MSc))?(?=\s|$|[,.])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Zlatan Tegtmeier  in der Angelegenheit der Parteien  Dipl. Kfm. VetR Gerhard Stranz (Beschwerdeführerin), vertreten durch die   Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H., 9400 Wolfsberg  und Finanzamt Oststeiermark, 1000 Wien, PF 251  als  Amtspartei über die Beschwerden vom 12.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Zlatan Tegtmeier`(person)
- `Dipl. Kfm. VetR Gerhard Stranz`(person)
- `Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamt Oststeiermark`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Dipl.-Ing. Mag.a Andrea Johanningmeyer, Tenniszeile 8, 5424 Rengerberg, Österreich, vertreten durch Susanne Neuhäuser, Hartiggasse  22/23, 2700 Wiener Neustadt, vom 12. Dezember 2019 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom  26. November 2019 betreffend Zwangsstrafen 2019 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniela Regina Denk`(person)
- `Dipl.-Ing. Mag.a Andrea Johanningmeyer`(person)
- `Tenniszeile 8, 5424 Rengerberg, Österreich`(address)
- `Susanne Neuhäuser`(person)
- `Finanzamt Schwechat Gerasdorf`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_7`)


An diese E-Mail- Adresse antwortete die WiEReG-Behörde mit einem E-Mail an die zum damaligen Zeitpunkt  geschäftsführende Gesellschafterin, datiert mit 25.05.2019, worin Folgendes mitgeteilt wurde:  "Bezugnehmend auf Ihr Schreiben betreffend die Meldebefreiung der Dipl.-Ing. Mag.a Andrea Johanningmeyer  darf ich Ihnen  mitteilen, dass die Meldebefreiung nach § 6 WiEReG nur dann greift, sofern ausschließlich  1 von 8 Seite 2 von 8

**False Positives:**

- `` — partial — pred is substring of gold: `Dipl.-Ing. Mag.a Andrea Johanningmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Mag.a Andrea Johanningmeyer`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_23`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   An der Dipl.-Ing. Mag.a Andrea Johanningmeyer  sind ***Gesellschafterin unbeschr1*** als unbeschränkt haftende  Gesellschafterin und der Verein „***“ als Kommanditist im verfahrensgegenständlichen  Zeitraum beteiligt.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Mag.a Andrea Johanningmeyer`(person)

</details>

---

## `Richter Title Names (Concatenated)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c5657986`  
**Description:**
Matches full names following 'durch den Richter' or 'durch die Richterin', handling concatenated titles like 'RichterRi'.

**Content:**
```
(?:durch\s+(?:den|die)\s+(?:Richter|Richterin|Ri|RichterRi))\s+(?:OMedR|MedR|StR|OStR|KzlR|LLB|VetR|Ri)?\s+(?:Mag\.a?|Dr\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|Hon\.-Prof\.|DDr\.in?|Ing\.in?|Dipl\.-Ing\.in?|Dipl\. Kfm\.in?|MSc|Bakk\. phil\. B\.in?|MedR|\u00d6kR|BA|OStR|OMedR|KzlR|LLB|VetR|Ri)?\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:\s+[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
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

## `Names with Suffixes in Legal Context (Fixed)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `aa59ba58`  
**Description:**
Matches full names following legal context phrases like 'in der Beschwerdesache', ensuring suffixes like Bakk. techn., MBA are captured.

**Content:**
```
(?:in der Beschwerdesache(?: des)? )([A-Z][a-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+㎙-㎙[A-z]+䑄[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+｝[A-z]+)(?:,? \s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?(?:,? \s*(?:LL\.M\\.|BEd\\.|B\\.K\\.|Dipl\\.Kfm\\.|MA\\.|BSc\\.|MBA\\.|MAS\\.|Bakk\\. rer\\. nat\\.|Bakk\\. art\\. BEd\\.)?)?)?(?=,|$|[,.])
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

## `Standalone Names in Narrative Context` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3d808da1`  
**Description:**
Matches standalone names following prepositions like 'von der', 'mit', 'bei' or appearing as subjects/objects in narrative sentences, capturing full names including hyphenated surnames and suffixes, while excluding company names.

**Content:**
```
(?:von\s+(?:der|die|dem|des)\s+|mit\s+|bei\s+(?!.*(?:Straße|Gasse|Platz|Weg|Avenue|Landstraße|Finanzamt|GmbH|AG|Gesellschaft|m\.b\.H)))\s+([A-Z][a-zA-Z\u00c0-\u00ff]+(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:[ -][A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:-[A-Z][a-zA-Z\u00c0-\u00ff]+)*(?:,?\s*(?:LL\.M(?!.*LLM)|LLB|BEd|B\.K|Dipl\.Kfm|MA|MBA|MSc|MAS|Bakk\. rer\. nat|Bakk\. art\. BEd)?)?)?(?=,|$|[.](?!.*(?:GmbH|AG|Gesellschaft)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 41 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_15`)


Die Belastung  beeinträchtigt gemäß § 34 Abs. 4 EStG 1988 wesentlich die wirtschaftliche Leistungsfähigkeit,  soweit sie einen vom Steuerpflichtigen von seinem Einkommen (§ 2 Abs. 2 in Verbindung mit  Abs. 5) vor Abzug der außergewöhnlichen Belastungen zu berechnenden Selbstbehalt  übersteigt.

**False Positives:**

- `Abs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_69`)


Art. 34, § 1 Budgetbegleitgesetz: Nach Art.34, § 1, Abs. 1 Budgetbegleitgesetz (Steuerliche  Sonderregelungen für die Ausgliederung von Aufgaben der Gebietskörperschaften) gelten die  durch die Ausgliederung und Übertragung von Aufgaben der Gebietskörperschaften an  juristische Personen des privaten oder öffentlichen Rechts sowie an Personenvereinigungen  (Personengemeinschaften), die unter beherrschendem Einfluss einer Gebietskörperschaft  stehen, anfallenden Schriften, Rechtsvorgänge und Rechtsgeschäfte von der  Gesellschaftsteuer, Grunderwerbsteuer und den Stempel- und Rechtsgebühren sowie den  Gerichts- und Justizverwaltungsgebühren befreit.

**False Positives:**

- `Gesellschaftsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_130`)


„Diese Zufallsabhängigkeit sah der VfGH auch bei  Preisausschreiben, obwohl von vornherein feststand, dass irgendjemand der Teilnehmer einen  Gewinn machen würde.

**False Positives:**

- `Preisausschreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_84`)


Nachweise zum Familienwohnsitz in Ungarn, der Unzumutbarkeit der Verlegung des  Familienwohnsitzes,  der Angabe und Nachweis des Haushaltes am Beschäftigungsort nach  dem 18.5.2017, der Kosten im Zusammenhang mit der Wohnung am Beschäftigungsort, des  belegmäßiger Nachweises und der Aufstellung der entstandene Kosten im Zusammenhang mit  Familienheimfahrten, der Frage nach steuerfreien Vergütungen von allfälligen Heimfahrten  durch den Arbeitgeber (Kostenersätze), die Übermittlung des Ausdruckes aus dem  Pendlerrechner, der Frage nach der überwiegende Arbeitszeit und nach der Arbeitsstätte, etc.  blieb der Bf. schuldig.

**False Positives:**

- `Familienheimfahrten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_20`)


– eine Rechnung von amazon.de vom 07.02.2018 über ein „Corsair HX1200 1200 W 80Plus  Platinum PC-Netzteil (Voll-Modulares Kabelmanagement, ATX) schwarz in Höhe von 211,67 €,  (= Rechnung Nr. 2 laut Auflistung),  – eine Rechnung von amazon.de vom 18.01.2018 über ein „Crucial 8GB DDR4 2400 MT/s (PC4- 19200) DR x8 DIMM 288-Oin – CT8G4DFD824A“ in Höhe von 84,73 €, (= Rechnung Nr. 3 laut  Auflistung),  – eine Rechnung der Firma Ganz Einfach GmbH, Hannover, vom 28.01.2018 über eine „CSL –  4 G Hochleistungs LTE Antenne 15 dBi MIMO Technik Verstärker-Antenne“ in Höhe von  19,01 €, (= Rechnung Nr. 4 laut Auflistung),  – eine Rechnung von amazon.de vom 15.05.2018 über einen „Bronson++ HE-D 1000 – 110 Volt  Spannungswandler / Transformer – 1000 Watt – In: EURO 220 – 240 Volt / Out: USA 110 Volt –  Ringkerntransformator 1000 W – Bronson“ in Höhe von 71,24 €, (= Rechnung Nr. 5 laut  Auflistung),  – eine Rechnung von amazon.de vom 16.05.2018 über eine „Saft LS 14250 ½ AA 3,6V Li-SOCI2  Batterie (5-er Pack) weiß/grün“ in Höhe von 14,26 €, (= Rechnung Nr. 6 laut Auflistung),  – eine Rechnung von amazon.de vom 04.07.2018 über einen „LUPUSEC Drahtloser  Sensoreingang für die XT Alarmanlagen kompatibel mit der XT1 und XT2 Funk Alarmanlagen,  Energieklasse A, 12020“ in Höhe von 60,14 €, (= Rechnung Nr. 7 laut Auflistung),  – eine Rechnung von amazon.de vom 03.07.2018 über eine 720P HD WLAN Wifi IP Kamera  LE203, Sicherheitskamera, Überwachungskamera, IP Cam, drahtlos, steuerbar mit  Bewegungsmelder, 2 Wege Audio, IR Nachtsicht, integrierbar in User Smarthome  Alarmsystem“ in Höhe von 153,36 €, (= Rechnung Nr. 8 laut Auflistung),  – eine Rechnung von amazon.de vom 22.07.2018 über eine „SanDisk Ultra 64 GB microSDXC  Speicherkarte + Adapter bis zu 100 MB/Sek, Class 10, U1, A1, Grau, Rot“ in Höhe von 18,65 €,  (= Rechnung Nr. 9 laut Auflistung),  – eine Rechnung von amazon.de vom 23.11.2018 über ein „Samsung Galaxy S7 Smartphone  (5,1 Zoll (12,9 cm) Touch-Display, 32GB interner Speicher, Android OS) black“ in Höhe von  261,18 €, (= Rechnung Nr. 10 laut Auflistung),  – eine Rechnung von amazon.de vom 23.11.2018 über eine Samsung EVO Select microSDXC 65  GB MB-ME64GA/EU Speicherkarte“ in Höhe von 17,14 €, (= Rechnung Nr. 11 laut Auflistung),  – eine Rechnung von amazon.de vom 23.11.2018 über eine „Medion P61078 Lifebeat- Muktiroom Soundbar mit 2 x 18 W RMS Ausgangsleistung, eingebautem 36 W RMS  Subwooofer, Bluetooth-Funktion und DLNA kompatibel“ in Höhe von 121 €, (= Rechnung Nr. 12  laut Auflistung),  4 von 18 Seite 5 von 18

**False Positives:**

- `Bewegungsmelder` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_35`)


Die Tochter der Bf. war zum Antragszeitpunkt 14 Jahre alt.  Für einen Anspruch auf den Erhöhungsbetrag zur Familienbeihilfe ab Mai 2016, so wie von der  Bf. beantragt, müsste daher durch ein Gutachten des Sozialministeriumservice ein Grad der  Behinderung von 50% beginnend mit dem Antragszeitraum vorliegen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_129`)


Auf die polizeiliche Meldung als Hauptwohnsitz kommt es nicht an (vgl. zum Ganzen die bei  Walter-Mayer, Zustellrecht, Seite 32f, zitierte Rechtsprechung sowie das Erkenntnis des VwGH  28.01.1985, 85/18/0011, 0012, 0013, wonach zur Auslegung des Begriffes der Wohnung im  Sinne des § 4 des Zustellgesetzes auf die Rechtsprechung zur Rechtslage vor Erlassung des  Zustellgesetzes, insbesondere zu § 22 Abs. 1 AVG 1950, zurückgegriffen werden kann).

**False Positives:**

- `Walter-Mayer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_116`)


Ein solcher Eingriff sei aber nach der Rechtsprechung mit  Art. 6 Abs. 1 EMRK vereinbar, wenn die Auskunfts-pflichten zum angestrebten Zweck nicht  unverhältnismäßig sind und den Kerngehalt des Verbots nicht verletzen (vgl. Grabenwarter  /Pabel, Europäische Menschenrechtskonvention5, Rz 123 zu Art. 6 EMRK, mwN, vgl. auch  VwGH 13.07.2017, Ra 2014/17/0018).

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_118`)


Es ist der Bf. zwar  zuzustimmen, dass das Arbeiten mit potenziell infektiösen Materialien eine Gefährdung der  Gesundheit bzw. des Lebens mit sich bringen können (UFS 18.4.2011, RV/1685-W/04) oder bei  Arbeitnehmern, die mit fremden Blut oder Harn in Kontakt kommen können, eine  9 von 12 Seite 10 von 12

**False Positives:**

- `Arbeitnehmern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_101`)


Die Bf. hat sich somit iSd obigen Ausgeführten im Rahmen ihrer Möglichkeiten von der  Existenz, der Seriosität und Leistungsfähigkeit ihres Lieferanten überzeugt.

**False Positives:**

- `Existenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_378`)


Ich habe die Preisverhandlungen mit Herrn M. geführt und ich habe  von M. diesen Preis verlangt, da ich bei der e. immer gleich bezahlen musste mit  Eilüberweisung, bei der Fa.F. hatte ich aber ein Zahlungsziel von 30 Tagen vereinbart.

**False Positives:**

- `Eilüberweisung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)
- `M.`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_519`)


Nach Ansicht des Senates hat sich die Bf. somit im Rahmen ihrer Möglichkeiten von der  Existenz, der Seriosität und Leistungsfähigkeit ihrer Lieferanten überzeugt.

**False Positives:**

- `Existenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_32`)


Diese Unterkunft hingegen  werde an weniger als 70 Tagen pro Jahr benützt, was die Klassifizierung als Wohnsitz - bei  Abgabenpflichtigen, deren Mittelpunkt der Lebensinteressen sich mindestens fünf Jahre im  Ausland befand, gemäß Zweitwohnsitz-Verordnung (BGBI II 2003/528) - jedenfalls ausschließe.

**False Positives:**

- `Abgabenpflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_38`)


Diese Verpflichtung wird  durch eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.“

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_69`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes ist die Zwangsläufigkeit bei  Krankheitskosten, die durch die gesetzliche Krankenversicherung gedeckten Kosten  übersteigen, nur dann gegeben, wenn sie aus triftigen medizinischen Gründen erfolgen.

**False Positives:**

- `Krankheitskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_15`)


Sie wohne in einer WG mit  Studentinnen.

**False Positives:**

- `Studentinnen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_30`)


Lt. Firmenbuch ist der Geschäftszweig der XY Consulting GmbH, FN 888888y die „Erbringung  von wirtschaftlichen Beratungs- und Dienstleistungen, Unternehmensberatung, Handel mit  Immobilien, Bilanzbuchhaltung“

**False Positives:**

- `Immobilien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `XY Consulting GmbH`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_153`)


Entsprechend den Intentionen des Gesetzgebers, die Dauer des Anspruches auf Familienbeihilfe  bei volljährigen Schülern vom Schulerfolg abhängig zu machen, ist die Familienbeihilfe bei  Kindern, die die Externistenreifeprüfung ablegen wollen, nach folgenden Richtlinien zu  gewähren:  Um die Externistenreifeprüfung zu erlangen, sind bis zu 13 Zulassungsprüfungen und eine  Hauptprüfung (= die eigentliche Reifeprüfung) abzulegen.

**False Positives:**

- `Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_103`)


Nach § 7 Abs. 1 EStG 1988 in der für den gegenständlichen Fall anzuwenden Fassung sind bei  Wirtschaftsgütern, deren Verwendung oder Nutzung durch den Steuerpflichtigen zur Erzielung  von Einkünften sich erfahrungsgemäß auf einen Zeitraum von mehr als einem Jahr erstreckt  (abnutzbares Anlagevermögen), die Anschaffungs- oder Herstellungskosten gleichmäßig  verteilt auf die betriebsgewöhnliche Nutzungsdauer abzusetzen (Absetzung für Abnutzung).

**False Positives:**

- `Wirtschaftsgütern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_93`)


Laut Auskunft der Patientin: Ganz viele meiner Verhaltensweisen deuten nach dem heutigen  Wissensstand auf eine Asperger Symptomatik hin, weil ich grundsätzlich ein Problem habe mit  Veränderungen.

**False Positives:**

- `Veränderungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_173`)


Ab diesem Zeitpunkt bis  einschließlich 2019 erhielt die Bf. steuerfreie Gelder vom Arbeitsmarktservice und von der  WGKK, im Jahr 2017 zusätzlich einen Bezug von der Bundespensionskasse AG.

**False Positives:**

- `WGKK` — type mismatch — same span as gold: `WGKK`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WGKK`(organisation)
- `Bundespensionskasse AG`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_207`)


Diese Verpflichtung  wird durch eine erhöhte Mitwirkungspflicht des Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_86`)


Verlaufsbericht, Wohnheim f. Fachschüler, Y-Institut- Schulverein, für Menschen mit  Sehbehinderung, Blindheit und weiteren Behinderungen, Ort3, vom 15.02.2018.

**False Positives:**

- `Sehbehinderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_295`)


Gemäß § 2 Abs 2 EStG ist Einkommen der Gesamtbetrag der Einkünfte nach Ausgleich mit  Verlusten, die sich aus einzelnen Einkunftsarten ergeben und nach Abzug der Sonderausgaben,  außergewöhnlichen Belastungen und des Freibetrages nach § 105 EStG.

**False Positives:**

- `Verlusten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_63`)


(2) Gegenstand von Auskunftsbescheiden sind Rechtsfragen im Zusammenhang mit  Umgründungen, Unternehmensgruppen und Verrechnungspreisen.

**False Positives:**

- `Umgründungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/144397.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144397.1_60`)


Es kann daher nicht abgeleitet werden, dass die Bestimmung des § 241a BAO von der  Notwendigkeit, eine Abgabenfestsetzung vorzunehmen, entbinden könnte.

**False Positives:**

- `Notwendigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_61`)


eine erhöhte Mitwirkungspflicht der Abgabepflichtigen, wie beispielsweise bei  Auslandssachverhalten, eingeschränkt.

**False Positives:**

- `Auslandssachverhalten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_200`)


Bei einer Verwendung im Zusammenhang mit  Berufsbildern, bei welchen die berufliche Nutzung eines solchen Gerätes nach dem Urteil  gerecht und billig denkender Menschen zweckmäßig erscheint, kommt zugleich dem Kriterium  der Notwendigkeit seiner beruflichen Nutzung keine entscheidende Bedeutung zu. Doch  bedarf es, gerade wenn Aufwendungen vergleichbarer Art häufig auch in der Privatsphäre  anfallen, einer sorgfältigen Prüfung der beruflichen Veranlassung (VwGH 27.1.2011,  2010/15/0197;

**False Positives:**

- `Berufsbildern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_263`)


Hält man sich nämlich vor Augen, dass dem vom VwGH  entschiedenen Fall die Sanierung von bestehenden Aufzugssystemen zugrunde lag, wobei  einerseits Leichtbaukabinen sowie Notrufsysteme geliefert und eingebaut, wie auch Mängel  behoben wurden und die dort maßgeblichen Arbeiten auch die Erneuerung von  Fangkorbgleitachsen, Seilen, Antrieben, Dichtsätzen und Seilschlössern miteinschloss, somit  Maßnahmen, die keine Schadensbehebungen darstellen, kann der Rechtsansicht der  Beschwerdeführerin, wonach eine Großreparatur eine solche zur Voraussetzung haben müsse,  nicht gefolgt werden.

**False Positives:**

- `Maßnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/146608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146608.1_70`)


[…]  § 27a EStG 1988 in der für das streitgegenständliche Jahr maßgeblichen Fassung lautet  auszugsweise:  (1) Einkünfte aus Kapitalvermögen unterliegen  1. im Fall von Geldeinlagen und nicht verbrieften sonstigen Geldforderungen bei  Kreditinstituten, ausgenommen Ausgleichzahlungen und Leihgebühren gemäß § 27 Abs. 5 Z 4,  einem besonderen Steuersatz von 25%,  2. in allen anderen Fällen einem besonderen Steuersatz von 27,5%  und sind bei der Berechnung der Einkommensteuer des Steuerpflichtigen weder beim  Gesamtbetrag der Einkünfte noch beim Einkommen (§ 2 Abs. 2) zu berücksichtigen, sofern nicht  die Regelbesteuerung (Abs. 5) anzuwenden ist.

**False Positives:**

- `Kreditinstituten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_508`)


Verunreinigung oder Verschmutzung in einem laufenden Bauverfahren ist der Zustand der  Belastung bzw. die Kontamination von Oberflächen, Objekten, Substanzen oder Räumen mit  Substanzen, die im jeweiligen Kontext als Schmutz bzw. Dreck angesehen werden, die also als  gesundheitlich und ökologisch bedenklich oder ästhetisch abstoßend wahrgenommen werden.

**False Positives:**

- `Substanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit Eingabe vom 8.5.2014 (Übermittlung per Fax am 9.5.2014) erstattete die im Fürstentum  Liechtenstein ansässige Stb-Kanzlei an die Leiterin der Strafsachenstelle des Finanzamtes  Baden eine Selbstanzeige gemäß § 29 FinStrG für NN1-Bf-NN2-Bf VN-Bf, in der Folge kurz mit  Bf. bezeichnet, und ihren Mann NN1-Bf VN-M-Bf.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_122`)


Im Ergänzungsersuchen vom 20.10.2014, auf  welches sich die händische Bescheidbegründung vom 16.6.2015 beziehe, sei jedoch davon die  Rede, dass es steuerfreie Substanzzahlungen erst ab 31.7.2008 gebe.

**False Positives:**

- `Rede` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Univ.-Prof.in Maja Lauers  in der Säumnisbeschwerdesache  Univ.-Prof. Mehmet Klasema, Labon 67, 4861 Looh, Österreich  vertreten durch Jonathan Goessl, über die Beschwerde vom 8. Jänner  2025 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Bescheidbeschwerde vom 12. April 2024 gegen den Bescheid betreffend die  Abweisung des Antrages auf Wiederaufnahme des Verfahrens gemäß § 303 BAO  (Körperschaftsteuer 2021) vom 13. März 2024, Steuernummer 85-153/1153, den Beschluss:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 in Verbindung mit  Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Abs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Maja Lauers`(person)
- `Univ.-Prof. Mehmet Klasema`(person)
- `Labon 67, 4861 Looh, Österreich`(address)
- `Jonathan Goessl`(person)
- `Finanzamt Österreich`(organisation)
- `85-153/1153`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/147714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147714.1_50`)


Dies befreit die Abgabenpflichtigen aber nicht von der  Verpflichtung, ihrerseits zur Klärung des maßgebenden Sachverhaltes beizutragen und die für  den Bestand und Umfang einer Abgabenpflicht bedeutsamen Umstände vollständig und  wahrheitsgemäß offenzulegen (§ 119 Abs 1 BAO).

**False Positives:**

- `Verpflichtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/147874.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147874.1_11`)


Gegen die vom  Finanzamt erlassene abweisende Beschwerdevorentscheidung vom 17.06.2024 wurde von der  Bf. mit Schreiben vom 26. Juni 2024 der Antrag auf Entscheidung durch das  Bundesfinanzgericht (Vorlageantrag) eingebracht.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/147920.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147920.1_11`)


Damit verbunden seien Ausgaben im Zusammenhang mit  Telefonaten, Kundenbesuchen, etc., die durch das Vertreterpauschale abgegolten werden  sollen.

**False Positives:**

- `Telefonaten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_126`)


Des Weiteren (siehe Beilagen Bf2 Bf1 Verzögerungen Vermietung Text und Bf2 Bf1  Verzögerungen Vermietung Aufstellung) werde zwar angegeben, dass beabsichtigt gewesen  sei, das Gebäude zu vermieten, aber aufgrund von Schwierigkeiten (Verzögerungen bei  Sanierungsarbeiten, Schimmelbefall) sich die Inbetriebnahme aller vier Einheiten verzögert  hätte.

**False Positives:**

- `Sanierungsarbeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/148710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148710.1_13`)


Die Erlassung der Beschwerdevorentscheidung durch das Finanzamt Innsbruck ergibt sich  offensichtlich aus der ausdrücklichen Anführung des Finanzamtes Innsbruck im von der  Bearbeiterin, einer Mitarbeiterin des Fachbereiches des Finanzamtes Innsbruck, verwendeten  Vordruckes "Verf 40".

**False Positives:**

- `Bearbeiterin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Innsbruck`(organisation)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamtes Innsbruck`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/149304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149304.1_70`)


Dass sich die schauspielerischen Tätigkeiten des Bf. auf längere als die in den jeweiligen  Lohnzetteln angegebenen Zeiträume erstreckten, ergibt sich aus der vom Bf. vorgelegten  Übersichtstabelle, in der die zusätzlich zu den Dreharbeiten ausgeübten Zusatztätigkeiten  (Lernen des Drehbuchs, Synchronisation etc.) angeführt sind, seinem glaubhaften Vorbringen  im Rahmen der mündlichen Verhandlung und den vorgelegten Verträgen mit  Filmproduktionsfirmen.

**False Positives:**

- `Filmproduktionsfirmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_86`)


Nach § 48 BAO idF vor BGBl. I Nr. 62/2019 kann das Bundesministerium für Finanzen bei  Abgabepflichtigen, die der Abgabenhoheit mehrerer Staaten unterliegen, soweit dies zur  Ausgleichung der in- und ausländischen Besteuerung oder zur Erzielung einer den Grundsätzen  der Gegenseitigkeit entsprechenden Behandlung erforderlich ist, anordnen, bestimmte  Gegenstände der Abgabenerhebung ganz oder teilweise aus der Abgabepflicht auszuscheiden  oder ausländische, auf solche Gegenstände entfallende Abgaben ganz oder teilweise auf die  inländischen Abgaben anzurechnen.

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesministerium für Finanzen`(organisation)

</details>

---

## `Names after Specific Verbs/Contexts (Beschuldigter/Stellungnahme)` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `13cd73d9`  
**Description:**
Matches names following specific legal contexts like 'Beschuldigter an', 'Stellungnahme', or 'gegenst∘ndliche Antragstellerin' which often introduce the person of interest.

**Content:**
```
(?:Beschuldigter an |Stellungnahme |gegenst∘ndliche Antragstellerin \(AS \)|Antragstellerin )([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:[ -][A-Z][a-zA-Z]+)*)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_296`)


Beschwerden dem  Bundesfinanzgericht zur Entscheidung vorgelegt und in der Stellungnahme Folgendes  ausgeführt:  „Nachdem in den Erstbescheiden U 2017 und U 2018 der Gesamtbetrag der steuerpflichtigen  Lieferungen, sonstigen Leistungen und Eigenverbrauch (einschließlich steuerpflichtiger  Anzahlungen) /Vorsteuern zwecks Verfahrensbeschleunigung wegen ho. unbekannter Umsätze  2017 und 2018 mit +/- 0,00 angesetzt (vgl. BFG 23.3.2022, GZ. RV/2100108/2020) und dies mit  Beschwerde gerügt wurde, waren die Umsätze gemäß § 184 BAO zu schätzen.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `BFG`(organisation)

</details>

---

## `Gutachten von Names` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `659cb5a6`  
**Description:**
Matches names appearing after 'Gutachten von' which introduces an expert witness or author.

**Content:**
```
(?:Gutachten von)\s+([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)*(?:[ -][A-Z][a-zA-Z]+)*)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_82`)


Zu dem Vorbringen im Vorlageantrag wurde seitens des Sozialministeriumservice am  17.4.2024 folgende ergänzende Stellungnahme abgegeben:  "Die Gutachten von Prof.PhD Doris Goessing sind schlüssig.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof.PhD Doris Goessing`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.PhD Doris Goessing`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_32`)


Der Substanzwert ist  der niedrigste für Gesellschaftsanteile an der Dr.in Flora Lallemand  anzusetzende Wert, selbst wenn man  das gesamte Potential an Mehrwertsteuerrückforderungen durch das Finanzamt berücksichtigt  (Gutachten von Mag. H., gerichtlich beeideter Sachverständiger ON 35 u 48).

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Flora Lallemand`(person)
- `Finanzamt`(organisation)
- `Mag. H.`(person)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (953, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_183`)

(Vgl EuGH 22.10.2015, C-378/14, Tomislaw **Trapkowski**, VwGH  24.06.2021, Ro 2018/16/0040, BFG 27.06.2023, RV/7105857/2017)

- missed: `Trapkowski` (person)
- predicted in sentence: `Tomislaw Trapkowski`

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_330`)

Darin hat die  Firma **M.** in diesem Zeitraum 01-04/2013 fakturierte Bauleistungen in Höhe von € 90.570,80  ausgewiesen, ohne über Eigen- oder Fremdkapazitäten zur Ausführung dieser Arbeiten zu  23 von 29 Seite 24 von 29

- missed: `M.` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)

12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr **Aldewereld** von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

- missed: `Aldewereld` (person)
- predicted in sentence: `Aldewereld`

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_110`)

Die Finanzierung sei mittels Einlage des **M.M.A.** [380.386,00 € im Prüfungszeitraum 03/2011  bis Wirtschaftsjahr 02/2015] und der M.M.B. [250.000 € (= Verkaufserlös betreff bisheriges  Wohnhaus im  Dezember 2012] jeweils in die Firma erfolgt.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch **Dr. Stephan Riel** als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Stephan Riel` (person)
- predicted in sentence: `Mag. Gerhard Groschedl`, `Mittel-Verlag`

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Silvia Gebhart** in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Silvia Gebhart` (person)
- predicted in sentence: `Erwin Döpkemeier`, `Mag Kerstin Friedrich`

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_43`)

Nach dem vorliegenden gerichtlichen Beschluss ist **Dr. X** als Erwachsenenvertreter des Bf.  zur Vertretung vor Ämtern und Behörden zuständig.

- missed: `Dr. X` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_226`)

Diese Auffassung ist spätestens seit den Urteilen EuGH 11.9.2014, C-394/13, B, und EuGH  22.10.2015, C-378/14, Tomisław **Trapkowski**, als überholt anzusehen (vgl. BFG 7.2.2017,  RV/7106469/2016).

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_87`)

Die an M.M.B. vermietete (und nur notdürftig eingerichtete) Wohnung Top 3 (85,11 m2) werde  laut Auskunft von **M.M.A.** von den Kindern bewohnt.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_166`)

Unterschriften auf den von der Firma **M.** vorgelegten Kassa-Eingang-Belegen, die überdies nur  in Schwarz-Weiß-Kopien vorgelegt wurden.

- missed: `M.` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_193`)

Die Vertreterin des Finanzamtes beantragt die teilweise Stattgabe der Beschwerde, und zwar  die Anerkennung der Beträge laut BVE und zusätzlich der Fahrtkosten zu **Univ.-Prof. Massimo Brokmeyer**(€ 25,20)), im  Übrigen die Abweisung der Beschwerde.

- missed: `Univ.-Prof. Massimo Brokmeyer` (person)
- predicted in sentence: `Univ.-Prof. Massimo`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_101`)

Betreff das „Gebäude (3) Rohbau“ hätte das im Zuge der Erhebungen im Bauamt festgestellte  Ansuchen der Bf. um Bewilligung zur Errichtung eines "Saunahauses" (Nutzfläche 114,35 m2)  am 17.06.2014 der Aussage des **M.M.A.** bei der Betriebsbesichtigung hinsichtlich des Neubaus  weiterer Wohnungen widersprochen.

- missed: `M.M.A.` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Annika Streicher BA LL.M.(WU)** in der  Beschwerdesache Dimitri Gaessner, Sauerbrunnberg 15, 8124 Neuhof, Österreich, vertreten durch Miriam Wurmehl, Bakk. phil., Windparkstraße 7, 5092 Gumping, Österreich, über die Beschwerde vom 13. Februar 2024 gegen den Bescheid des Finanzamtes  Österreich vom 16. Jänner 2024 betreffend Verspätungszuschlag / ESt 2020 Steuernummer  90-683/6114  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Annika Streicher BA LL.M.(WU)` (person)
- predicted in sentence: `BA LL`, `Dimitri Gaessner`, `Miriam Wurmehl`

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Barbara Straka** in der Verwaltungsstraf- sache gegen Imre Bschorer, Karchham 233Q, 2733 Hornungstal, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde des Beschuldigten vom 26. Juli 2023 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 24. Juli 2023, GZ. MA67/Zahl/2023, zu Recht  erkannt:  Der Beschwerde wird gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorgani- sationsrecht (WAOR) insoweit Folge gegeben, als die verhängte Geldstrafe von 60,00 € auf  36,00 € und die für den Fall der Uneinbringlichkeit mit 14 Stunden festgesetzte Ersatzfreiheits- strafe auf 8 Stunden herabgesetzt wird.

- missed: `Dr. Barbara Straka` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_74`)

Die **Leroy Kusznierz**  wurde  schließlich am xx.xx.2020 im Firmenbuch des Gericht gelöscht.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_18`)

Am besagten Tag habe er **M.** zu  verschiedenen Örtlichkeiten gefahren.

- missed: `M.` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_89`)

Die Tochter der Bf wurde im Zuge des Antragsverfahrens am 8. Juli 2020 im Sozialministerium- service von **Dr.in Dok1**, Ärztin für Allgemeinmedizin, begutachtet und folgendes Gutachten  erstellt:  "Anamnese:   Asperger Syndrom, F40.2. Spezifische Phobie  Derzeitige Beschwerden:   Laut Auskunft der Mutter: Vor einem Jahr ist meine Dok2 darauf gekommen, dass sie eventuell  ein Asperger Syndrom haben könnte.

- missed: `Dr.in Dok1` (person)
- predicted in sentence: `Dok1`

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen **Flora Thierry**, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

- missed: `Flora Thierry` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_4`)

Die Gesellschafter der Bf. - die Pflege Nexwerkwald GmbH und **N.N.** - sind jeweils mit einer Stammeinlage von  40.000 € an der Bf. beteiligt.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_94`)

Eingangs ist - zumal die **Leroy Kusznierz**  per xx.xx.2020 endete - die Frage der Rechtsnachfolge zu  klären: Kraft der ausdrücklichen gesetzlichen Anordnung des § 191 Abs. 2 BAO – als lex  specialis zur im § 19 Abs. 1 BAO normierten Gesamtrechtsnachfolge – haben  Feststellungsbescheide nach Beendigung einer Personenvereinigung (Personengemeinschaft)  an die Personen, denen gemeinschaftliche Einkünfte zugeflossen sind, zu ergehen.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_436`)

Der Vorhaltsbeantwortung waren fünf Anlagen angeschlossen:  Anlage 1:  1/1: Letter of confirmation vom 26.8.2020  1/2: Bestätigungsschreiben (beglaubigte Übersetzung aus dem Englischen vom 17.9.2020) vom  26.8.2020  1/3: Letter of confirmation vom 26.8.2020  1/4: CMR 80722597 an ZL vom 13.6.2016  Anlage 2:  2/1: Letter of confirmation vom 26.8.2020  2/2: CMR 80265439 an F.B. vom 17.3.2015  2/3: CMR 80828354 an F.B. vom 27.9.2015  2/4: CMR 80914347 an R.U. vom 5.12.2016  2/5: CMR 80914350 an R.U. vom 2.12.2016  Anlage 3:  3/1: This Document has been issud on the request of vom 27.8.2020  3/2: Dieses Dokument wird ausgestellt auf Ansuchen vom 27.8.2020 (Übersetzung vom  29.9.2020)  3/3: This Document has been issud on the request of vom 27.8.2020  3/4: Invoice der Bf. an N. vom 12.10.15  3/5: Invoice der Bf. an N. vom 26.9.16  3/6: CMR an CL vom 9.10.2015  3/7: Purchase Order vom 1.10.2015 (N. an CL)  3/8: Purchase Order vom 20.9.2016 (N. an CL)  3/9: CMR JBL an CL vom 26.9.2016  3/10: CMR 80409868 an K. (Polska) vom 7.8.2015  3/11: CMR 80423569 an K. (Polska) vom 26.8.2015  3/12: CMR 80236735 an Ko. (N.L.) vom 10.2.2015  3/13: CMR 80392557 an Ko. (Polska) vom 21.7.2015  3/14: CMR 80388656 an M. (Polska) vom 24.7.2015  3/15: CMR 80320800 an **M.** (Polska) vom 8.5.2015  3/16: CMR 80257940 an S. (Polska) vom 6.3.2015  3/17: CMR 80323928 an S. (Polska) vom 18.5.2015  3/18: CMR 80265443 an S. (Polska) vom 18.3.2015  3/19: CMR 80423566 an S. (Polska) vom 24.8.2015  3/20: CMR 80673863 an Ko. (Polska) vom 22.4.2016  29 von 59 Seite 30 von 59

- missed: `M.` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_378`)

Ich habe die Preisverhandlungen mit Herrn M. geführt und ich habe  von **M.** diesen Preis verlangt, da ich bei der e. immer gleich bezahlen musste mit  Eilüberweisung, bei der Fa.F. hatte ich aber ein Zahlungsziel von 30 Tagen vereinbart.

- missed: `M.` (person)
- predicted in sentence: `M.`, `Eilüberweisung`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Friedhelm Sutor, Taggergasse 3, 3873 Thaures, Österreich, vertreten durch LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32, 4040 Linz, über die Beschwerde  vom 12. Jänner 2021 gegen den Bescheid des Finanzamtes für Großbetriebe vom  16. Dezember 2020 betreffend Normverbrauchsabgabe 06.2015-12.2019 Steuernummer  11-766/4596  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Friedhelm Sutor`

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_92`)

Der Spruch des Auskunftsbescheids lautet auszugsweise:  „Über den im Namen und Auftrag der **Madeleine Jahns**, … gestellten Antrag vom 17.8.2014  (eingelangt am 20.8.2014) auf Erteilung eines Auskunftsbescheides gemäß § 118 BAO spricht  das Finanzamt Feldkirch wie folgt ab:  I. Die im Antrag formulierten Rechtsfragen zu dem in der Begründung dieses Bescheides  dargelegten Sachverhalt wird durch das Finanzamt Feldkirch wie folgt beurteilt:  Die im Antrag vom 17.8.2014 und in der beigelegten 32 seitigen Sachverhalts- und  Rechtsproblembeschreibung mit Strategiepapier dargestellten Bedingungen werden gem. Art 9  DBA Österreich-Liechtenstein nicht als Bedingungen angesehen, welche zwischen  unabhängigen Unternehmen vereinbart oder auferlegt werden würden.

- missed: `Madeleine Jahns` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dr. Siegfried Fenz** in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Siegfried Fenz` (person)
- predicted in sentence: `HR OSR Leonie Ercklentz`, `LKP Steuerberatung OG`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dr. Wolfgang Pavlik** über die Beschwerde der  Silke Czejka, Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich, vom 01. September 2022 gegen den Bescheid des Finanzamtes  Österreich vom 30. August 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Monat Mai 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Wolfgang Pavlik` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_12`)

Diese Rechnung (die USt ausweisend, Beilage 3 zum Protokoll) vom 12.6.2019 wurde ihr vom  Steuerberater am 20.6.2019 wiederum per Email (Beilage 2 zum Protokoll) übermittelt.  Der Kaufvertrag wurde am 17.6.2019 unterfertigt, wobei der Käufer die Vorsteuer auf das  Abgabenkonto der **Saskia Sinnwell**  überrechnen hätte sollen und diese wiederum als USt abgeführt  hätte werden sollen.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Maria-Luise Wohlmayr** in der  Beschwerdesache Dario Hünervogt, Tirolerwiese 77, 8103 Hörgas, Österreich  vertreten durch zobl.bauer.

- missed: `Dr. Maria-Luise Wohlmayr` (person)
- predicted in sentence: `Dario Hünervogt`

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_19`)

Am 18.06.2012 habe der Augenarzt **Dr.  A1**, A-Stadt, (siehe Befund vom 15.03.2011, Untersuchung vom 21.12.2011 und 18.06.2012  (Befunde beiliegend) seiner Patientin Bf. mündlich erklärt, sie möge einen Augenfacharzt für  ihre Operation selbst aussuchen.

- missed: `Dr.  A1` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache **Dr. RgR Nepomuk Gillmeister** (Beschwerdeführer, abgekürzt: Bf.), Kraygasse 26, 5134 Bruck im Holz, Österreich  vertreten  durch Steuerberaterin, AdresseSteuerberaterin, über die Beschwerde des Bf. vom 5. Mai 2022  gegen den Einkommensteuerbescheid 2020 des Finanzamtes Österreich vom 26. April 2022 zu  Steuernummer 08-648/8723  zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und der angefochtene Bescheid gemäß § 279  Abs. 1 BAO dahingehend abgeändert, dass die Einkommensteuer für das Jahr 2020 mit  2.663,00 € festgesetzt wird.

- missed: `Dr. RgR Nepomuk Gillmeister` (person)
- predicted in sentence: `Mag. Christian Seywald`, `RgR Nepomuk Gillmeister`

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für **M. F.** ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `M. F.` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch **Dr. X**, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

- missed: `Dr. X` (person)
- predicted in sentence: `Lieselotte Reinicker`

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_220`)

**Dr. Dok2** wählte, wie schon Dr. Dok1, 2 Stufen über dem unteren Rahmensatz, da eine mäßige  Einschränkung der sozialen Fähigkeiten und die Absolvierung eines Studiums möglich sei.

- missed: `Dr. Dok2` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_15`)

Der Bf. brachte in seiner Stellungnahme vom 11. September 2023 vor, dass er bei der  Ausweisinhaberin **M.** als persönlicher Assistent (Verweis auf beiliegende Lohnbestätigung)  angestellt sei.

- missed: `M.` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Dr. Hans Rauner** über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

- missed: `Dr. Hans Rauner` (person)
- predicted in sentence: `Pjotr Astore`

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_471`)

Aufgrund der  Neurodermitis stehe der Aufwand mit der Behinderung in Zusammenhang, € 87,48 seien daher  eine ag Bel ohne SB.   24.01.2013 € 50,64 Osspura Theodora Hartzheim, BA Bakk. phil. FK 25,32   26.02.2013 € 50,64 Osspura **Theodora Hartzheim, BA Bakk. phil.** FK € 25,32   26.03.2013 € 45,00 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32  19.06.2013 € 50,4 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32   32 von 43 Seite 33 von 43

- missed: `Theodora Hartzheim, BA Bakk. phil.` (person)
- predicted in sentence: `BA Bakk`, `BA Bakk`, `BA Bakk`, `BA Bakk`

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/147955.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147955.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christian Soltendieck  in der Beschwerdesache des Dr. MV  als Masseverwalter (MV) im Insolvenzverfahren der **Berthold Grosshans**, Gruisla 3Q, 3231 Linsberg, Österreich  vertreten durch  die Berthold Grosshans, Seetal 31, 4661 Altmanning, Österreich  nunmehr vertreten durch Rechtsanwalt Mag. Gregor  Kohlbacher, Keesgasse 11, 8010 Graz, betreffend die Beschwerde vom 12. Oktober 2020 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 15. Mai 2020 über die Zurückweisung eines  Antrages auf Wiedereinsetzung in den vorigen Stand (hinsichtlich Umsatzsteuer 2014 bis 2017  und Umsatzsteuer 1-11/2018), Steuernummer 59-309/9934, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als unzulässig zurückgewiesen.

- missed: `Berthold Grosshans` (person)
- predicted in sentence: `Hon.-Prof. Christian Soltendieck`, `Mag. Gregor  Kohlbacher`

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/128833.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128833.1_12`)

Mit Bescheid vom 12. Juni 2018 wies das Finanzamt den Antrag vom 21.3.2018 auf  Familienbeihilfe für **Jana Papenkord**  ab Jänner 2011 ab.

- missed: `Jana Papenkord` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_346`)

Die besonders luxuriöse Ausstattung der Wohneinheit Top 1 erfolgt nach den Wünschen und  Vorstellungen des Gesellschafters und Geschäftsführers Ing. **M.M.A.** (z.B. Kosten für a) Küche  und Esszimmer: 90.664,40 € netto; b) "Specksteinofen": 18.200,00 € netto).

- missed: `M.M.A.` (person)
- predicted in sentence: `Ing. M.M`

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_470`)

Zur Akne-/Narbenbehandlung  07.02.2013 € 43,74 3 * Teebaum Medicamo24 Dr.S   31.05.2013 € 43,74 3* Teebaum Medicamo24 **Theodora Hartzheim, BA Bakk. phil.**  Ansicht FA:  Es liegt eine zeitnahe ärztliche Verordnung vom 25.3.2013 vor (Anm.: von Theodora Hartzheim, BA Bakk. phil. mit dem  Vermerk „Akne, Fructoseintoleranz, Zöliakie, Milchunverträglichkeit“).

- missed: `Theodora Hartzheim, BA Bakk. phil.` (person)
- predicted in sentence: `BA Bakk`, `Theodora Hartzheim`, `BA Bakk`

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_58`)

Zum Beweis dafür wurde ein  Dokument vom 27.11.2018 vorgelegt, worin die Firmen Firma1 und Firma2 vereinbaren, dass Herr **Russbüldt** als Fuhrparkleiter für beide angeführten Firmen ab dem 01.12.2018 beauftragt wird.

- missed: `Russbüldt` (person)
- predicted in sentence: `Russb`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/145892.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145892.1_26`)

In meiner Straße gibt's es 2 **Gotthard Sträßner**.

- missed: `Gotthard Sträßner` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_82`)

Von STB2, gesendet Mittwoch, 6. Oktober 2021:   S.g. Herr BMF2, mit Dank für Ihre Hilfsbereitschaft möchte ich als ehemaliger Mitarbeiter der  FV und Freund des früheren Sektionschefs **Dr. Nolz** doch festhalten: Das von wem immer  erzwungene WiEReg ist nicht ganz gelungen!

- missed: `Dr. Nolz` (person)
- predicted in sentence: `BMF`

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)

Die Auskunft könne Herr **Russbüldt** als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

- missed: `Russbüldt` (person)
- predicted in sentence: `Russb`

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_134`)

Mit Mail vom 03.10.2018 hat **Ida Katenstroth** zu der am 01.10.2018 vom Prüfer übermittelten  Prüfungsfeststellung wie folgt Stellung genommen:  Pkt .1.2  Seitens der AP wird auf das Urteil des EuGH vom 22.04.2010 hingewiesen.

- missed: `Ida Katenstroth` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_491`)

1.08.2012 begonnene unbefristete Mietverhältnis für Top 4 von den Vertragsparteien Bf. und  **M.M.B.2** unter Einhaltung einer dreimonatigen Kündigungsfrist zum letzten eines Monats  aufgekündigt werden hätte können, offensichtlich.

- missed: `M.M.B.2` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_48`)

Im zentralen  Melderegister scheint ein **Dr. Karl** RA1 ab 2010 mit der Adresse AdresseWien auf (mit  3 von 16 Seite 4 von 16

- missed: `Dr. Karl` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_79`)

Die weiteren Feststellungen zur Historie der **Leroy Kusznierz**  fußen auf den im Firmenbuch  ersichtlichen Änderungen, respektive den diesen Eintragungen zugrunde liegenden und in der  dortigen Urkundensammlung hinterlegten Anträgen (Antrag auf Eintragung einer  Kommanditgesellschaft vom Datum;

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache **Mehmet Zappe, MA**, Wiesel 24, 4632 Oberirrach, Österreich, vertreten durch Petzelbauer & Kleinhappel Rechtsanwälte, Rabensteig 8/3A, 1010  Wien, betreffend einen Antrag auf Fristsetzung gemäß Art. 133 Abs. 1 Z 2 iVm Abs. 7 B-VG vom  10. Oktober 2022 wegen Verletzung der Entscheidungspflicht, Steuernummer 51-912/4171  (SVNR 3727 040311), beschlossen:   Der Fristsetzungsantrag vom 10. Oktober 2022 betreffend die behauptete Säumigkeit des  Bundesfinanzgerichtes im Säumnisbeschwerdeverfahren gegen das Finanzamt Österreich  betreffend einen Antrag auf Familienbeihilfe für den Zeitraum März 2020 bis April 2021 wird  gemäß § 30a Abs. 1 VwGG iVm § 30a Abs. 8 erster Satz VwGG als unzulässig zurückgewiesen.

- missed: `Mehmet Zappe, MA` (person)
- predicted in sentence: `R.`, `Mehmet Zappe`

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_66`)

Der selbstsüchtige **Riese** 10,08  46.

- missed: `Riese` (person)
- predicted in sentence: —

</details>

---

