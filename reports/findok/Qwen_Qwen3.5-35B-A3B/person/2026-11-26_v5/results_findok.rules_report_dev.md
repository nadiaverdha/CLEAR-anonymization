# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-26T12:36:50.495468

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-26_v5/config.yaml 
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
| Agentic | False |
| Enable Critic | False |
| Enable Prune | False |
| Critic Interval | 0 |
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
| True Positives | 562 |
| False Positives | 231 |
| False Negatives | 1289 |
| Total Gold Entities | 1851 |
| Micro Precision | 70.9% |
| Micro Recall | 30.4% |
| Micro F1 | 42.5% |
| Macro F1 | 42.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `party_person_defendant` | 26.8% | 92.9% | 15.7% | 312 | 290 | 22 |
| `judge_person` | 20.9% | 79.9% | 12.0% | 278 | 222 | 56 |
| `representative_person` | 5.1% | 46.3% | 2.7% | 108 | 50 | 58 |
| `abbreviated_person_herr_frau` | 0.0% | 0.0% | 0.0% | 61 | 0 | 61 |
| `generic_title_initial_person` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `case_citation_person` | 0.0% | 0.0% | 0.0% | 33 | 0 | 33 |
| `narrative_person_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `party_person_defendant` 🏆

**F1:** 0.268 | **Precision:** 0.929 | **Recall:** 0.157  

**Format:** `regex`  
**Rule ID:** `f3883c29`  
**Description:**
Captures parties identified after 'in der Beschwerdesache' or 'in der Verwaltungsstrafsache', handling hyphenated names, titles like Dr.in, and suffixes like BSc, MSc.

**Content:**
```
(?:in\s+(?:der\s+)?Beschwerdesache(?:\s+des)?|in\s+der\s+Verwaltungsstrafsache)\s+([A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.929 | 0.157 | 0.268 | 312 | 290 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 290 | 22 | 1561 |

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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Sascha Hilcker` | `Ing. Sascha Hilcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Pawils` | `Florentin Pawils` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Alva Jodgalweit` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Dominik Mehlig` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache Aron Pommeränke,  Seenplattenweg 7, 4190 Oberstiftung, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit §  16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für  Wien Nr. 20, in der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, über die  Beschwerde des Beschuldigten vom 26. Jänner 2021 gegen das Erkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 29. Dezember 2020, GZ. MA6/2019,  beschlossen:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 28 Abs. 1  VwGVG, § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG), § 13 Allgemeines  Verwaltungsverfahrensgesetz 1991 (AVG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird das Beschwerdeverfahren eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Aron Pommeränke` | `Aron Pommeränke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Seenplattenweg 7, 4190 Oberstiftung, Österreich` (address)
- `Stadt Wien` (organisation)
- `Magistrates der  Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl. Kfm. Ing. Ing. Jonas Thumberger` | `Dipl. Kfm. Ing. Ing. Jonas Thumberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Paullehnerweg 72, 9584 Höfling, Österreich` (address)
- `UNICONSULT Steuerberatungs GmbH & Co KG` (organisation)
- `FA Braunau Ried Schärding` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

| Predicted | Gold |
|---|---|
| `Dora Szczepanowski` | `Dora Szczepanowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich` (address)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


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

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Denis Diekötter  in KLG Kreuzbau 16, 8242 Kronegg, Österreich, vertreten durch Rein & Partner Steuerberatung GmbH & Co KG in  8230 Hartberg, Alleegasse 13, über die Beschwerde vom 22.3.2017 gegen die Bescheide des  Finanzamtes Baden Mödling (nunmehr Finanzamt Österreich) vom 14.3.2017 betreffend   - Einkommensteuer 2012, 2013, 2014 und 2015 und  - Umsatzsteuer 2012, 2013, 2014 und 2015  zu Recht erkannt:   I. Insoweit sich die Beschwerde gegen die Umsatzsteuerbescheide 2012, 2013, und  2014 richtet, wird dem Beschwerdebegehren gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Denis Diekötter` | `Denis Diekötter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Albert Salzmann` (person)
- `KLG Kreuzbau 16, 8242 Kronegg, Österreich` (address)
- `Rein & Partner Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


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

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


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

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


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

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


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

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


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

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


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

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


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

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Eugen Volchert Hochraingasse` — partial — gold is substring of pred: `Eugen Volchert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Lieselotte Akdas`(person)
- `Eugen Volchert`(person)
- `Hochraingasse 28, 4076 Valtau, Österreich`(address)
- `FA Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Charlotte Hasslbauer Bf` — partial — gold is substring of pred: `Charlotte Hasslbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Charlotte Hasslbauer`(person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich`(address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich`(address)
- `Procurator Treuhand- und Revisionsges.m.b.H.`(organisation)
- `Bundesministeriums für Finanzen`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Raimund Diedering` — partial — pred is substring of gold: `Raimund Diedering, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Josepha Peifers Jägerberg` — partial — gold is substring of pred: `Josepha Peifers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Josepha Peifers`(person)
- `Jägerberg 5, 9062 Bärndorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/139401.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139401.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Dr. Dipl.-Ing. Laurence Goetke,  Unterernsthofen 11, 9311 Leiten, Österreich, vertreten durch STB, Adr1, über die Beschwerde vom 10. Dezember 2019  gegen den Bescheid des A vom 12. November 2019 betreffend Umsatzsteuer 2012,  Steuernummer 42-698/5318, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Dipl.-` — partial — pred is substring of gold: `Dr. Dipl.-Ing. Laurence Goetke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dipl.-Ing. Laurence Goetke`(person)
- `Unterernsthofen 11, 9311 Leiten, Österreich`(address)
- `42-698/5318`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/141414.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141414.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Dr.in Mag.a Elisabeth Wiedenhöfft, LLM, Hirschberg 29, 2870 Guggendorf, Österreich, über die Beschwerde vom 11. November 2021 gegen den Bescheid  des Finanzamtes Österreich vom 5. Oktober 2021 betreffend Antrag auf Bewilligung der  Aussetzung § 212a BAO 2021, Steuernummer 16-471/8115  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Mag.a Elisabeth Wiedenhöfft` — partial — pred is substring of gold: `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`(person)
- `Hirschberg 29, 2870 Guggendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `16-471/8115`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/145618.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145618.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/145448.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145448.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/146030.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146030.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Dr. RgR Nepomuk Gillmeister (Beschwerdeführer, abgekürzt: Bf.), Kraygasse 26, 5134 Bruck im Holz, Österreich  vertreten  durch Steuerberaterin, AdresseSteuerberaterin, über die Beschwerde des Bf. vom 5. Mai 2022  gegen den Einkommensteuerbescheid 2020 des Finanzamtes Österreich vom 26. April 2022 zu  Steuernummer 08-648/8723  zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und der angefochtene Bescheid gemäß § 279  Abs. 1 BAO dahingehend abgeändert, dass die Einkommensteuer für das Jahr 2020 mit  2.663,00 € festgesetzt wird.

**False Positives:**

- `Dr. Rg` — partial — pred is substring of gold: `Dr. RgR Nepomuk Gillmeister`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag. Christian Seywald`(person)
- `Dr. RgR Nepomuk Gillmeister`(person)
- `Kraygasse 26, 5134 Bruck im Holz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `08-648/8723`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/147347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147347.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/147540.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147540.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/147829.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147829.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag.a Dipl.-` — partial — pred is substring of gold: `Mag.a Dipl.-Ing. Leya Mentzel, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

</details>

---

## `judge_person` 🏆

**F1:** 0.209 | **Precision:** 0.799 | **Recall:** 0.120  

**Format:** `regex`  
**Rule ID:** `d3dfb3b6`  
**Description:**
Captures judges with complex titles (Dr., Mag., Priv.-Doz.in, etc.) and hyphenated names after 'durch den Richter' or 'durch die Richterin'. Handles suffixes like LL.M., BSc, MSc and German characters.

**Content:**
```
(?:durch\s+(?:den\s+)?Richter|durch\s+(?:die\s+)?Richterin)\s+([A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.799 | 0.120 | 0.209 | 278 | 222 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 222 | 56 | 1629 |

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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker` (person)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Hermine Roj` | `Mag.a Hermine Roj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corinna Farke` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Tiwald` | `Mag. Wolfgang Tiwald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Renneissen` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fridolin Rummler` | `Mag. Fridolin Rummler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Goncalves` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Matyschek` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosemarie Schan` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janosch von Winterfeldt` (person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Ottfried Theißl` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Tamara Steinmüller` | `Mag.a Tamara Steinmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gueldner Garten` (organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich` (address)
- `FA Deutschlandsberg Leibnitz Voitsberg` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Verwaltungsstrafsache gegen Bernhard Habdank, Jantschweg 6, 4782 Oberteufenbach, Österreich, über die Beschwerde des  Beschuldigten vom 24. November 2020 gegen den Zurückweisungsbescheid des Magistrates  der Stadt Wien, Magistratsabteilung 67 vom 21. September 2020, Zahl:  MA67/206700146315/2020, mit dem der Einspruch gegen die Strafverfügung vom 28. Mai  2020 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen  wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gertraud Hausherr` | `Mag. Gertraud Hausherr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Habdank` (person)
- `Jantschweg 6, 4782 Oberteufenbach, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des Jaden Holzfuss, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Puntigam` | `Mag. Manuela Puntigam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Holzfuss` (person)
- `Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Ladwig` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Susette Glaeßel` | `Mag.a Susette Glaeßel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl Morgenbesser` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Elvira Thielsen` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josepha Peifers` (person)
- `Jägerberg 5, 9062 Bärndorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gebhard Klutentreter` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/135797.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135797.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pjotr Astore` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Fassmer` (person)
- `Tillisweg 11, 8773 Sparsbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Sheila Nonnmacher` | `Dr.in Sheila Nonnmacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Semertzidou` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr.in Linn Wolek` | `Dr.in Linn Wolek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Uwe Vaculik` (person)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Heidemarie Winkler über die  Beschwerde der Uwe Köhn, Pizet 15, 9441 Waldenstein, Österreich, vom 26. Juli 2018, gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom  13. Juli 2018, betreffend Rückforderung von Familienbeihilfe für den Zeitraum September 2016  bis Februar 2018, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der  Beschwerdevorentscheidung, nämlich für 09/2016-02/2017, stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Uwe Köhn` (person)
- `Pizet 15, 9441 Waldenstein, Österreich` (address)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


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

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ulrike Stephan` | `Mag. Ulrike Stephan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentin Joebges, LLM` (person)
- `Bärngarten 17, 9713 Hochegg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `84-167/9727` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137239.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137239.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Henriette Pöpken, Stromsiedlung IV.R 11, 8510 Neurath, Österreich, Deutschland, vom 22. Mai 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. April 2022, Zl. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz  2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Renate Schohaj` | `Mag. Renate Schohaj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Henriette Pöpken` (person)
- `Stromsiedlung IV.R 11, 8510 Neurath, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerde des  Karim Hainzlmeier, Gälaplana 43, 3205 Mühlhofen, Österreich, gegen den Bescheid des Finanzamtes Bregenz vom 20. Mai 2016  betreffend Einkommensteuer 2015, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karim Hainzlmeier` (person)
- `Gälaplana 43, 3205 Mühlhofen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Juri Boyarzyn, Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich, vom 28. Juli 2020, gegen den Bescheid des Finanzamtes Österreich  vom 16. Juli 2020, betreffend Familienbeihilfe 01.2019-01.2021, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Boyarzyn` (person)
- `Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/137349.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137349.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julian Egiede` (person)
- `Theras 97, 4565 Haselbäckau, Österreich` (address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `Mag. Michael Sablatnik` (person)
- `88-033/6865` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache OSR Eugenia Balikci, Richardisweg 14, 5134 Ginshöring, Österreich, vertreten durch Wiener Kinder-und Jugendhilfe  2,20, Dresdner Straße 43, 1200 Wien, über die Beschwerde vom 20. März 2020 gegen den  Bescheid des Finanzamtes Österreich vom 25. Februar 2020 betreffend Familienbeihilfe ab  Jänner 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Eugenia Balikci` (person)
- `Richardisweg 14, 5134 Ginshöring, Österreich` (address)
- `Wiener Kinder-und Jugendhilfe` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


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

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/138159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138159.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Heidemarie Winkler im  Beschwerdeverfahren des Siegfried Bentz, Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich, vom 13.02.2022 gegen den  Pfändungsgebührenbescheid des Magistrats der Stadt Wien Magistratssabteilung 6 Erhebungs-  und Vollstreckungsdienst, vom 31.01.2022, mit:  I. Nach Auffassung des Bundesfinanzgerichts ist in Bezug auf die Beschwerde vom 13.02.2022  gegen den Bescheid vom 31.01.2022 mit Beschwerdevorentscheidung abzusprechen.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Bentz` (person)
- `Brüder Wüster-Gasse 23, 8524 Vochera am Weinberg, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/138313.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138313.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Ibrahim Walterscheid, Wallsiedlung 55, 3970 Walterschlag, Österreich, vertreten durch UNICONSULT Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Wartenburger Straße 1b, 4840 Vöcklabruck, betreffend Beschwerde  vom 27. April 2022 gegen den Bescheid des Finanzamtes Österreich vom 25. März 2022  betreffend Einkommensteuer 2020 Steuernummer 78-985/8140  beschlossen:  Die Beschwerde wird wegen Verspätung gemäß § 260 Abs. 1 lit. b BAO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibrahim Walterscheid` (person)
- `Wallsiedlung 55, 3970 Walterschlag, Österreich` (address)
- `UNICONSULT Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `78-985/8140` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank  in der Beschwerdesache Nicoletta Nipshagen, Obergrafendorfer Straße 11, 9141 Oberburg, Österreich,  über die Beschwerde vom 1. Mai 2021 gegen den Einkommensteuerbescheid  (Arbeitnehmerveranlagung) für das Jahr 2020 des Finanzamtes Österreich vom 26. April 2021,  Steuernummer 02-339/1714, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Helga Woschank` | `Dr. Helga Woschank` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nicoletta Nipshagen` (person)
- `Obergrafendorfer Straße 11, 9141 Oberburg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `02-339/1714` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Janina Gruenaeugl, Geiereckstraße 27, 4720 Güttling, Österreich, Schweden, vertreten durch die Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H., Wagramer Straße 19, 1220  Wien, über die Beschwerde vom 9. Jänner 2017 gegen den Bescheid des Finanzamtes für  Großbetriebe (vormals Bruck Eisenstadt Oberwart) vom 13. April 2015 betreffend Abweisung  eines Antrages auf Rückzahlung Österreichischer Lohnsteuer,Einkommensteuer 2012  Steuernummer 65-008/8295  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janina Gruenaeugl` (person)
- `Geiereckstraße 27, 4720 Güttling, Österreich` (address)
- `Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H.` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `65-008/8295` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


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

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die Beschwerde des  Magdalena Unterreiter, Anichstraße 5, 8953 Donnersbach, Österreich, Deutschland, vom 22. März 2022, gegen das Straferkenntnis des  Magistrates der Stadt Wien, Magistratsabteilung 67, als Verwaltungsstrafbehörde vom  10. März 2022, Zl. Zahl, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Magdalena Unterreiter` (person)
- `Anichstraße 5, 8953 Donnersbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/138952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138952.1_1`)


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

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/138996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138996.1_1`)


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

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/139070.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139070.1_1`)


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

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/139164.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139164.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde des  OMedR Tanja Kubatsch, Sand/Bundesstraße 2, 4170 Damreith, Österreich, vom 21. Oktober 2022, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 21. September 2022, GZ. MA67/Zahl/2022,  wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Diana Sammer` | `Mag. Diana Sammer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Tanja Kubatsch` (person)
- `Sand/Bundesstraße 2, 4170 Damreith, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


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

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde des  Lubomir Vaist, Sulzbachfelderstraße 3, 9361 Judendorf, Österreich, vom 4. Jänner 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 12. Oktober 2022, GZ. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lubomir Vaist` (person)
- `Sulzbachfelderstraße 3, 9361 Judendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/139845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Beate Eichwalder in der  Beschwerdesache Selma Bußejahn, Unterdanegger Straße 26, 2183 St. Ulrich, Österreich, über die Beschwerde vom 24. September 2014  gegen den Bescheid des Finanzamtes Klagenfurt vom 1. September 2014 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 Steuernummer 85-809/5147  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Beate Eichwalder` | `Mag. Beate Eichwalder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Selma Bußejahn` (person)
- `Unterdanegger Straße 26, 2183 St. Ulrich, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `85-809/5147` (tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/139889.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139889.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 29. Dezember 2021 des Beschwerdeführers Ashley Claesson, Adr BF, Steuernummer:  66-163/5550, gegen den Bescheid des Finanzamtes Österreich vom 1. Dezember 2021  betreffend Einkommensteuer 2020 zu Recht:    I)  Der Beschwerde wird gem. § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Günter Narat` | `Mag. Günter Narat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ashley Claesson` (person)
- `66-163/5550` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/140273.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140273.1_1`)


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

- `Mag. Judith Daniela Herdin-` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr.in Laurin Morgenschweis`(person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich`(address)
- `Fatima Beringschmidt`(person)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag.a Univ.-` — partial — pred is substring of gold: `Mag.a Univ.-Prof.in Ada Schaeferlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein`(person)
- `Leroy Sitterle`(person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich`(address)
- `Astoria Stb GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Mag. Mirha Karahodzic` — partial — pred is substring of gold: `Mag. Mirha Karahodzic MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Timon Thoennißen`(person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Evelyn Antwerber`(person)
- `Hertzstraße 25, 5134 Spieglern, Österreich`(address)
- `Dr. Farid Rifaad`(person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Laurence Vasylenko  in der Beschwerdesache X, Adresse,  über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Umgebung  vom 13. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 02-410/2351  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Hon.-` — partial — pred is substring of gold: `Dr.in Hon.-Prof.in Laurence Vasylenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hon.-Prof.in Laurence Vasylenko`(person)
- `Finanzamtes Graz`(organisation)
- `02-410/2351`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

**False Positives:**

- `Dr. Maria-` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Lieselotte Reinicker`(person)
- `Raingasse 32, 9552 Ossiachberg, Österreich`(address)
- `Dr. X`(person)
- `Finanzamtes`(organisation)
- `FA Österreich`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lee Kubbig`(person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

**False Positives:**

- `Mag. Markus Knechtl` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Dora Szczepanowski`(person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich`(address)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Hilde Schorpp, Wandschaml 94, 4625 Grub, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 21. Dezember 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung der Rechtsvorschrift des § 2 in Verbindung mit § 4 Abs. 2  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 2 VStG eingestellt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Hilde Schorpp`(person)
- `Wandschaml 94, 4625 Grub, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ludger Endel`(person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-868/1042`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Jeanne Stockhorst`(person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `22-242/2984`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  Gwendolin Rittmüller, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Hon.-` — partial — pred is substring of gold: `Dr.in Hon.-Prof.in Hilde Hassenzahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hon.-Prof.in Hilde Hassenzahl`(person)
- `Gwendolin Rittmüller`(person)
- `Matzlröth 29, 3970 Reinprechts, Österreich`(address)
- `FA Bruck Eisenstadt Oberwart`(organisation)
- `10-920/5174`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/137857.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137857.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Univ.-Prof. Aron Nierenberger  in der Beschwerdesache DDr.in VetR Rosemarie Srama,  Hollgasse 53, 3244 Riegers, Österreich, gegen die Bescheide des Finanzamtes Österreich vom 10. Februar 2020  betreffend Einkommensteuer 2014 bis 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Dr. Univ.-` — partial — pred is substring of gold: `Dr. Univ.-Prof. Aron Nierenberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Univ.-Prof. Aron Nierenberger`(person)
- `DDr.in VetR Rosemarie Srama`(person)
- `Hollgasse 53, 3244 Riegers, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Günter Salahi  in der Beschwerdesache Jaden Knauss,  Dossenweg 3, 4132 Atzesberg, Österreich  über die Beschwerde vom 8. Jänner 2021 gegen den Bescheid des Finanzamtes  Österreich vom 3. Dezember 2020 Rückzahlung gemäß § 239 BAO, Steuernummer  15-678/4603  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Hon.-` — partial — pred is substring of gold: `Mag. Hon.-Prof. Günter Salahi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Günter Salahi`(person)
- `Jaden Knauss`(person)
- `Dossenweg 3, 4132 Atzesberg, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `15-678/4603`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Jeremias Kierstan, Zwerndorferstraße 68, 3922 Schroffen, Österreich, vertreten durch Peter Schabel,  AdresseVertreter, betreffend Beschwerde vom 09.09.2015 gegen den Bescheid des Magistrats  der Stadt Wien, Magistratssabteilung 31 Wiener Wasser, vom 17.07.2015 betreffend  Herabsetzung der Abwassergebühren für den Zeitraum 01.01.2013 bis 31.12.2013, MA 31-  958035/15, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Jeremias Kierstan`(person)
- `Zwerndorferstraße 68, 3922 Schroffen, Österreich`(address)
- `Peter Schabel`(person)
- `Magistrats  der Stadt Wien`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/138662.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138662.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Maurice Kämpfel, Leuzendorfgasse 8, 5660 Eschenau, Österreich, betreffend Beschwerden vom 9. März 2022  gegen die Bescheide des Finanzamtes Österreich vom 21. Oktober 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 und Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 93-599/8471  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Maurice Kämpfel`(person)
- `Leuzendorfgasse 8, 5660 Eschenau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `93-599/8471`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/138697.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138697.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Lee Gerstmayer, Wüsterstraße 92, 4972 Stelzham, Österreich, über die Beschwerde vom 13. Oktober 2014  gegen den Bescheid des Magistrats der Stadt Wien, Magistratssabteilung 31 Wiener Wasser  vom 12. September 2014 betreffend Wasser- und Abwassergebühr, MA 31-130652/15, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Lee Gerstmayer`(person)
- `Wüsterstraße 92, 4972 Stelzham, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Mag.a Univ.-` — partial — pred is substring of gold: `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`(person)
- `Selma Katirci`(person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich`(address)
- `Brehm & Sahinol Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/139569.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139569.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde des Wladimir Leukhardt, Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich, vom 1. Juli 2014  gegen den Bescheid der Magistratsabteilung 68, Feuerwehr und Katastrophenschutz,  Berufsfeuerwehr Wien, Gebührenverrechnung, vom 17. Juni 2014 betreffend die Festsetzung  von Gebühren für Hilfeleistungen und Beistellungen durch die Feuerwehr der Stadt Wien mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde vom 1. Juli  2014 gegen den Bescheid vom 17. Juni 2014 ein Vorlageantrag nicht eingebracht.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Wladimir Leukhardt`(person)
- `Ignaz Anibas-Straße 106, 8222 Sankt Johann bei Herberstein, Österreich`(address)
- `Stadt Wien`(organisation)
- `Bundesfinanzgerichts`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/139621.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139621.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Silvana Hellfritz, Reibersweg 24, 8144 Unterpremstätten, Österreich, betreffend Beschwerde vom 31. Jänner 2021  gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 69-424/6198  beschlossen:   Der Vorlageantrag wird gemäß § 264 Abs 4 lit e Bundesabgabenordnung (BAO) in Verbindung  mit § 260 Abs 1 lit b BAO als verspätet zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Silvana Hellfritz`(person)
- `Reibersweg 24, 8144 Unterpremstätten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `69-424/6198`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Beschwerdesache Alma Vanek, Laschoberstraße 34, 9074 Pertitschach, Österreich, über die Beschwerde vom 8. Februar 2021  gegen den Einkommensteuerbescheid 2019 des Finanzamtes Österreich vom 15. Jänner 2021  Steuernummer 65-256/4865  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Andrea Müller-` — partial — pred is substring of gold: `Mag. Andrea Müller-Dobler MBA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Alma Vanek`(person)
- `Laschoberstraße 34, 9074 Pertitschach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `65-256/4865`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache RgR Denise Symang, Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich, vertreten durch Mag. Robert Bitsche,  Rechtsanwalt, Nikolsdorfergasse 7-11/15, 1050 Wien, über die Beschwerde vom 9. Oktober  2019 gegen die Bescheide des Finanzamtes Wien 4/5/10 (nunmehr Finanzamt Österreich) vom  11. September 2019 sowie vom 23. September 2019 betreffend Wiederaufnahme  Körperschaftsteuer 2015 bis 2017, Steuernummer 60-977/8084, nach Durchführung einer  mündlichen Verhandlung am 19. Dezember 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Judith Daniela Herdin-` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Friedhelm Sutor, Taggergasse 3, 3873 Thaures, Österreich, vertreten durch LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32, 4040 Linz, über die Beschwerde  vom 12. Jänner 2021 gegen den Bescheid des Finanzamtes für Großbetriebe vom  16. Dezember 2020 betreffend Normverbrauchsabgabe 06.2015-12.2019 Steuernummer  11-766/4596  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Friedhelm Sutor`(person)
- `Taggergasse 3, 3873 Thaures, Österreich`(address)
- `LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `11-766/4596`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Verwaltungsstrafsache gegen Susette Jungabel, Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde des Beschuldigten vom 17. März 2023 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. Februar 2023, GZ.  MA67/Zahl/2022,zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Susette Jungabel`(person)
- `Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/140698.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140698.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Rafaela Heinss, Severgraben 12, 4343 Hütting, Österreich, über die Beschwerde vom 24. März 2016 gegen  die Bescheide des Magistrats der Stadt Wien, Magistratsabteilung 6, Rechnungs- und  Abgabenwesen, vom 09. Februar 2016 betreffend Kommunalsteuer für die Jahre 2010 bis  2012, hat nach Durchführung einer mündlichen Verhandlung am 26.04.2023 in Anwesenheit  der Schriftführerin FOIin SF zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Rafaela Heinss`(person)
- `Severgraben 12, 4343 Hütting, Österreich`(address)
- `Magistrats der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/140806.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140806.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Moritz Bonnert  in der Beschwerdesache PhD MedR Romana Hupp,  Süßenberger Straße 7, 5270 Vorbuch, Österreich, vertreten durch Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020 Innsbruck, über die Beschwerde  vom 26. Juli 2013 gegen den Bescheid des FA Salzburg-Land  vom 25. Juni 2013 betreffend  Umsatzsteuer 2011, Steuernummer 16-160/7509, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Priv.-` — partial — pred is substring of gold: `Dr. Priv.-Doz. Moritz Bonnert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Moritz Bonnert`(person)
- `PhD MedR Romana Hupp`(person)
- `Süßenberger Straße 7, 5270 Vorbuch, Österreich`(address)
- `Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `FA Salzburg-Land`(organisation)
- `16-160/7509`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/140842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140842.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Ferdinand Raumschüssel, Friedhof Hadersdorf-Weidlingau 7, 4910 Hof, Österreich, vertreten durch "CURA" Treuhand- und  Revisions- gesellschaft m.b.H., Gumpendorfer Straße 26, 1060 Wien, über die Beschwerde vom  29. November 2022 gegen den Bescheid des Finanzamtes Österreich vom 22. November 2022  betreffend Festsetzung einer Zwangsstrafe, Steuernummer 36-801/8584, nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Ferdinand Raumschüssel`(person)
- `Friedhof Hadersdorf-Weidlingau 7, 4910 Hof, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `36-801/8584`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Verwaltungsstrafsache gegen Volkmar Ehrenhardt, BEd, Kleinpoxruck 11, 6083 Ellbögen, Österreich, wegen der Verwaltungsübertretung  gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, über die Beschwerde des  Beschuldigten vom 3. Mai 2023 gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 21. April 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Anna Mechtler-` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Volkmar Ehrenhardt, BEd`(person)
- `Kleinpoxruck 11, 6083 Ellbögen, Österreich`(address)
- `Magistrates der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/142564.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142564.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/143717.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Laetitia Rosenmeyer, Thomas Brunner-Weg 117, 3972 Reichenau am Freiwald, Österreich, über die Beschwerde vom 13. April 2023 gegen  den Bescheid des Finanzamtes Österreich vom 5. April 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 06-868/8855  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut-` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Laetitia Rosenmeyer`(person)
- `Thomas Brunner-Weg 117, 3972 Reichenau am Freiwald, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `06-868/8855`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/143736.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143736.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna-Maria Peschl in der  Beschwerdesache Diana Heilken, Alte Mauth Straße 11, 9411 Eselsdorf, Österreich, Steuernummer 63-533/6814  betreffend die  Beschwerde vom 5. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna-` — partial — pred is substring of gold: `Mag. Anna-Maria Peschl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna-Maria Peschl`(person)
- `Diana Heilken`(person)
- `Alte Mauth Straße 11, 9411 Eselsdorf, Österreich`(address)
- `63-533/6814`(tax_number)
- `Finanzamtes Österreich`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Othmar Garbe, Bf. Adresse, Ort in Kärnten, vertreten durch Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee,  über die Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 14. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 – 2015 (Steuernummer 29-838/1383) zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Maga. Ulrike Nussbaumer` — positional overlap with gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Othmar Garbe`(person)
- `Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `29-838/1383`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/144397.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144397.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag. Dario Hukauf, Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich, vertreten durch ALTHUBER SPORNBERGER &  PARTNER Rechtsanwälte GmbH, Doblhoffgasse 9 Tür Top 14, 1010 Wien, über die Beschwerde  vom 3. Jänner 2020 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr Finanzamtes für Großbetriebe ) vom 28. November 2019 betreffend Rückforderung  gem. § 241a BAO von Kapitalertragsteuer 2010 bis 2012 (Evidenznummern ***, ***, ***, ***,  ***, ***, ***, ***), Steuernummer 45-917/5183, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Judith Daniela Herdin-` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag. Dario Hukauf`(person)
- `Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `45-917/5183`(tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr in der  Beschwerdesache Dario Hünervogt, Tirolerwiese 77, 8103 Hörgas, Österreich  vertreten durch zobl.bauer.

**False Positives:**

- `Dr. Maria-` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Dario Hünervogt`(person)
- `Tirolerwiese 77, 8103 Hörgas, Österreich`(address)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/146522.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146522.1_1`)


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

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/147714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147714.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Claire Dummert, Rachenbach 10, 4352 Niederkalmberg, Österreich  vertreten durch Pickerle + Tengg  Wirtschaftsprüfungs- und SteuerberatungsgesmbH, Bahnhofstraße 8, 9500 Villach, über die  Beschwerden vom 25. November 2022 und 28. März 2023 gegen die Bescheide des  Finanzamtes Österreich vom 25. Oktober 2022 und 28. Feber 2023 die Wiederaufnahme der  Einkommensteuerverfahren 2016-2019 und die Einkommensteuer 2016-2020 beschlossen  (Steuernummer 47-092/4894):  I. Gemäß § 278 Abs. 1 BAO werden die angefochtenen Bescheide sowie die in weiterer  Folge erlassenen Beschwerdevorentscheidungen, letztere jeweils datierend mit 11.  April 2023, aufgehoben und die Sache zur Erledigung an die Abgabenbehörde  zurückverwiesen.

**False Positives:**

- `Maga. Ulrike Nussbaumer` — positional overlap with gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Claire Dummert`(person)
- `Rachenbach 10, 4352 Niederkalmberg, Österreich`(address)
- `Pickerle + Tengg  Wirtschaftsprüfungs- und SteuerberatungsgesmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `47-092/4894`(tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Annika Streicher BA LL.M.(WU) in der  Beschwerdesache Dimitri Gaessner, Sauerbrunnberg 15, 8124 Neuhof, Österreich, vertreten durch Miriam Wurmehl, Bakk. phil., Windparkstraße 7, 5092 Gumping, Österreich, über die Beschwerde vom 13. Februar 2024 gegen den Bescheid des Finanzamtes  Österreich vom 16. Jänner 2024 betreffend Verspätungszuschlag / ESt 2020 Steuernummer  90-683/6114  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Annika Streicher` — partial — pred is substring of gold: `Dr. Annika Streicher BA LL.M.(WU)`

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

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Judith Daniela Herdin-` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Jeffrey Stubenrauch, Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich  vertreten durch Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH, Mosetiggasse 1, 1230 Wien, über die Beschwerde vom 31.10.2024  gegen die Bescheide des Finanzamtes Österreich je vom 30.08.2024 die Wiederaufnahme der  Verfahren betreffend Umsatzsteuer 2018-2021, sowie Umsatzsteuer 2018-2022  (Steuernummer 05-888/5257) nach Durchführung einer mündlichen Verhandlung am  10.10.2025   I. beschlossen:  Die Beschwerde vom 31.10.2024 gegen den Umsatzsteuerbescheid 2022 vom 30.  August 2024 wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Mag.a Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Jeffrey Stubenrauch`(person)
- `Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich`(address)
- `Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `05-888/5257`(tax_number)

</details>

---

## `representative_person` 🏆

**F1:** 0.051 | **Precision:** 0.463 | **Recall:** 0.027  

**Format:** `regex`  
**Rule ID:** `ff8c213a`  
**Description:**
Captures legal representatives after 'vertreten durch', explicitly excluding corporate entities ending in GmbH, AG, KG, etc. Handles multiple names separated by '&'.

**Content:**
```
(?:vertreten\s+durch)\s+([A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)+)(?!\s+(?:GmbH|AG|KG|PartG|UG|OHG|SE))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.463 | 0.027 | 0.051 | 108 | 50 | 58 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 50 | 58 | 1801 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Peter Staudinger` | `Mag. Peter Staudinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Jeannette Neuschwender` (person)
- `Zum Kogl 12, 4441 Penz, Österreich` (address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

| Predicted | Gold |
|---|---|
| `Mag. Manfred Frühwirth` | `Mag. Manfred Frühwirth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Marco Laudacher` (person)
- `Reneé Dreyssig` (person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Dr Vana Dr Kolbitsch Mag Breitenecker` | `Dr Vana Dr Kolbitsch Mag Breitenecker` |
| `Mag Tatjana Kovacic` | `Mag Tatjana Kovacic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Mag. Robert Dax` | `Mag. Robert Dax` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernhard Maximowa` (person)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


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

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch Dr. Stephan Riel als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Riel` | `Dr. Stephan Riel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Mittel-Verlag` (organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `44-993/1626` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Michael Payr` | `Mag. Michael Payr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sulamith Jedwillat` (person)
- `Brandenbergweg 15, 8353 Pichla, Österreich` (address)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `41-852/7395` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Silvia Gredenberg` | `Dr. Silvia Gredenberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Sheila Nonnmacher` (person)
- `Sieglinde Semertzidou` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `76-265/6028` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Michael Sablatnik` | `Mag. Michael Sablatnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Elisabeth Hafner` (person)
- `Julian Egiede` (person)
- `Theras 97, 4565 Haselbäckau, Österreich` (address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-033/6865` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Volkmar Quadfasel, Forstbergstraße 5, 4144 Zanklbach, Österreich, vertreten durch Dr. Sebastian Mariano Volkmar Lenz,  Laurenzerberg 1, 1010 Wien, vom 25. April 2021, gegen den Bescheid des Finanzamtes  Österreich vom 26. März 2021, betreffend Abweisung des Antrages auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe ab Dezember 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Sebastian Mariano Volkmar Lenz` | `Dr. Sebastian Mariano Volkmar Lenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Pavlik` (person)
- `Volkmar Quadfasel` (person)
- `Forstbergstraße 5, 4144 Zanklbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache RgR Denise Symang, Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich, vertreten durch Mag. Robert Bitsche,  Rechtsanwalt, Nikolsdorfergasse 7-11/15, 1050 Wien, über die Beschwerde vom 9. Oktober  2019 gegen die Bescheide des Finanzamtes Wien 4/5/10 (nunmehr Finanzamt Österreich) vom  11. September 2019 sowie vom 23. September 2019 betreffend Wiederaufnahme  Körperschaftsteuer 2015 bis 2017, Steuernummer 60-977/8084, nach Durchführung einer  mündlichen Verhandlung am 19. Dezember 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Robert Bitsche` | `Mag. Robert Bitsche` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `RgR Denise Symang` (person)
- `Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich` (address)
- `Finanzamtes Wien 4/5/10` (organisation)
- `Finanzamt Österreich` (organisation)
- `60-977/8084` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/140867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140867.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Philipp Nosalek  in der Beschwerdesache Merlin Buechner,  Am Waldfriedhof 19-24, 4714 Gferet, Österreich, vertreten durch Dr. Martin Eisenberger, Muchargasse 30, 8010 Graz, über die  Beschwerde vom 17. Mai 2017 gegen den Bescheid des Zollamtes Österreich vom 11. April  2017, Zl. 700000/03287/2017, betreffend Aussetzungszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Martin Eisenberger` | `Dr. Martin Eisenberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Philipp Nosalek` (person)
- `Merlin Buechner` (person)
- `Am Waldfriedhof 19-24, 4714 Gferet, Österreich` (address)
- `Zollamtes Österreich` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


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

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/141318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Lara Blaßl, Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich, vertreten durch Dr. Michl Münzker, Landskrongasse 5 Tür 4, 1010  Wien, über die Beschwerde vom 24. Juni 2021 gegen den Bescheid des Finanzamtes Österreich  vom 17. Juni 2021 betreffend Festsetzung einer Zwangsstrafe, Steuernummer  54-324/8831, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michl Münzker` | `Dr. Michl Münzker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Lara Blaßl` (person)
- `Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `54-324/8831` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

| Predicted | Gold |
|---|---|
| `Helga Kraus` | `Helga Kraus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Cassandra Schmedtje` (person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich` (address)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Mag. Hamza Ovacin` | `Ing. Mag. Hamza Ovacin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Saphira Schnaak` (person)
- `Kürschner Allee 44, 9300 Mail, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `50-980/9446` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/141990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141990.1_2`)


Das Bundesfinanzgericht hat durch die Senatsvorsitzende R1, den RichterR2, sowie die  fachkundigen Laienrichter R3 und R4, in der Beschwerdesache VetR Maja Waatsack, Sarottla 115, 8522 Sulzhof, Österreich,  vertreten durch Mag. Wolfgang Schranz, Mahlerstraße 11 Tür 4, 1010 Wien, über die  Beschwerde vom 28. Oktober 2016 gegen die Bescheide des Finanzamtes Wien 8/16/17 vom  25. Juli 2016 betreffend Umsatzsteuer sowie Feststellung der Einkünfte gemäß § 188 BAO für  2009, sowie vom 24. August 2016 betreffend Umsatzsteuer und Feststellung der Einkünfte  gemäß § 188 BAO für die Jahre 2010 bis 2015, Steuernummer 31-345/4688, in der Sitzung  vom 30. August 2023 nach Durchführung einer mündlichen Verhandlung am 30. August 2023 in  Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Schranz` | `Mag. Wolfgang Schranz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Maja Waatsack` (person)
- `Sarottla 115, 8522 Sulzhof, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `31-345/4688` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache KzlR Techn R RgR Wigand Beinhorn, Salfeldstraße 54, 9500 Oberwollanig, Österreich, vertreten durch Dr. Robert Austaller, Wildshut 16, 5120 St. Pantaleon, über die  Beschwerde vom 3. März 2021 gegen den Bescheid des Finanzamtes Österreich vom  11. Februar 2021 betreffend Rechtsgebühr, Steuernummer 98-325/7724,  Erfassungsnummer 10-2021, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Robert Austaller` | `Dr. Robert Austaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Techn R RgR Wigand Beinhorn` (person)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `98-325/7724` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/142259.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Laurin Borchardt, Untertweng-Gartenstraße 24, 4085 Saulehen, Österreich, vertreten durch Dr. Leopold Boyer, Hauptstr 23-25, 2225 Zistersdorf, über die  Beschwerde vom 27. Jänner 2014 gegen den Bescheid des Finanzamtes Klagenfurt vom  20. Dezember 2013 betreffend Umsatzsteuer 1998 bis 2011 sowie Feststellung von Einkünften  1999 bis 2011 zu Steuernummer 05-890/5761  nach der am 27.07.2023 im Beisein der  Schriftführerin *** durchgeführten mündlichen Verhandlung zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Leopold Boyer` | `Dr. Leopold Boyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Laurin Borchardt` (person)
- `Untertweng-Gartenstraße 24, 4085 Saulehen, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `05-890/5761` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143074.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143074.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Joachim Sakarya, Augenbrünnl-Gasse 32, 9131 Tainacherfeld, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor-Keldorfer-Straße 1,  5020 Salzburg, über die Beschwerde vom 14. Jänner 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Dezember 2021 betreffend Abweisung eines Aussetzungsantrages gem. §  212a BAO, Steuernummer 94-841/9471  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Robert Karl Galler` | `Dr. Robert Karl Galler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Joachim Sakarya` (person)
- `Augenbrünnl-Gasse 32, 9131 Tainacherfeld, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `94-841/9471` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/143636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143636.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143791.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143791.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Erhard Gruetter  in der Beschwerdesache René Kleser,  Dauerkleingärten 17M, 5112 Gresenberg, Österreich, vertreten durch Mag. Andreas Schnegg, Kalkofenstraße 24, 6425 Haiming, über  die Beschwerde vom 19. Februar 2022 gegen den Bescheid des FA Wien 8/16/17  vom 21. Jänner 2022  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016, Steuernummer  85-777/9690, zu Recht erkannt:  I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Schnegg` | `Mag. Andreas Schnegg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Erhard Gruetter` (person)
- `René Kleser` (person)
- `Dauerkleingärten 17M, 5112 Gresenberg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)
- `85-777/9690` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/144218.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144218.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Dr. Maria Grohe in der Revisionssache  Torsten Vorholt, Steinleitenweg 55, 9544 Untersee, Österreich, vertreten durch Dr. Schmalzl und Dkfm. Vogler  Steuerberatungsgesellschaft m.b.H., Roseggerstraße 4, 2500 Baden, über den Antrag der  Revisionswerberin vom 8. März 2024, der Revision vom 8. März 2024 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 23. Jänner 2024, GZ. RV/7101341/2020, betreffend  Körperschaftsteuer 2014 - 2017 erhobenen Ordentlichen Revision die aufschiebende Wirkung  zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Dr. Schmalzl` | `Dr. Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Maria Grohe` (person)
- `Torsten Vorholt` (person)
- `Steinleitenweg 55, 9544 Untersee, Österreich` (address)
- `Vogler  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/144197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lukas Escherle  in der Verwaltungsstrafsache gegen  Kirsten Schneppensiefen, Poppenreithstraße 26, 7461 Goberling, Österreich, vertreten durch Albert Höferlin  wegen der  Verwaltungsübertretung gemäß § 16 Abs 1 des Gebrauchsabgabegesetz, über die Beschwerde  der Beschuldigten vom 31.7.2023 gegen das Straferkenntnis des Magistrats der Stadt Wien  vom 14.7.2023 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe auf je € 20,00 (also EUR 100,00) herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Albert Höferlin` | `Albert Höferlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Lukas Escherle` (person)
- `Kirsten Schneppensiefen` (person)
- `Poppenreithstraße 26, 7461 Goberling, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/145502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor in der Beschwerdesache  Lilia Kientze, Techtlgasse 1, 4720 Niederleithen, Österreich, vertreten durch Mag. Magdalena Anna Katharina Ferner, Hernalser  Hauptstrasse 35/14+15, 1170 Wien, über die Beschwerde vom 16. März 2022 gegen den  Bescheid des Finanzamtes Österreich vom 24. Februar 2022 betreffend Abweisung eines  Antrages auf Ausgleichzahlung Familienbeihilfe 08.2020  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Magdalena Anna Katharina Ferner` | `Mag. Magdalena Anna Katharina Ferner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Doktor` (person)
- `Lilia Kientze` (person)
- `Techtlgasse 1, 4720 Niederleithen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/145762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Bruno Hübscher in der Beschwerdesache  Anton Brouwers, Waldenstein 10, 9821 Söbriach, Österreich, vertreten durch Dr. Maria Brandstetter, Stephansplatz 4/VIII, 1010  Wien, über die Beschwerden vom 21. Februar 2013 und vom 4. März 2013 gegen folgende  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr:  Finanzamt Österreich), ergangen zu Steuernummer 75-923/4499,  1.

| Predicted | Gold |
|---|---|
| `Dr. Maria Brandstetter` | `Dr. Maria Brandstetter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Bruno Hübscher` (person)
- `Anton Brouwers` (person)
- `Waldenstein 10, 9821 Söbriach, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)
- `75-923/4499` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/145807.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145807.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Roxana Massott, Gottschallalmstraße 37, 4792 Ficht, Österreich, vertreten durch Mag. Fatma Islekoglu, Rechtsanwältin,  Landstraße 13, 6971 Hard, über die Beschwerde vom 22. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 22. Februar 2024 betreffend Festsetzung der  Normverbrauchsabgabe (Berechnungsstichtag 02.06.2022), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Fatma Islekoglu` | `Mag. Fatma Islekoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Roxana Massott` (person)
- `Gottschallalmstraße 37, 4792 Ficht, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/146141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Rosamunde Löckemann, Kirchblickweg 224, 3754 Haselberg, Österreich, vertreten durch Esra Röhlen, Glasergasse 4, 4240 Vierhöf, Österreich, über die  Beschwerde vom 1. Juni 2023 egen die folgenden in den fünf Sammelbescheiden des  Finanzamtes für Großbetriebe vom 18. April 2023 (Zeitraum Jänner 2018 bis September 2022)  enthaltenen Bescheide des Finanzamtes für Großbetriebe über die „Abweisung von  Vergütungsanträgen gem. § 12a NoVAG 1991“ betreffend die im Spruch genannten Fahrzeuge  zu Recht erkannt:  I.  Die in den Sammelbescheiden enthaltenen Bescheide zu den folgenden Exportfahrzeugen  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Esra Röhlen` | `Esra Röhlen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Rosamunde Löckemann` (person)
- `Kirchblickweg 224, 3754 Haselberg, Österreich` (address)
- `Glasergasse 4, 4240 Vierhöf, Österreich` (address)
- `Finanzamtes für Großbetriebe` (organisation)
- `Finanzamtes für Großbetriebe` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Dipl.-Ing. Mag.a Andrea Johanningmeyer, Tenniszeile 8, 5424 Rengerberg, Österreich, vertreten durch Susanne Neuhäuser, Hartiggasse  22/23, 2700 Wiener Neustadt, vom 12. Dezember 2019 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom  26. November 2019 betreffend Zwangsstrafen 2019 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susanne Neuhäuser` | `Susanne Neuhäuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Daniela Regina Denk` (person)
- `Dipl.-Ing. Mag.a Andrea Johanningmeyer` (person)
- `Tenniszeile 8, 5424 Rengerberg, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/147002.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147002.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/147137.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache RgR Shirley Ribler, Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich, vertreten durch Dr. Christian Lind,  Am Ausblick 17, 3110 Neidling, über die Beschwerde vom 2. Jänner 2023 gegen die Bescheide  des Finanzamtes Österreich vom 1. Dezember 2022 betreffend Anspruchszinsen (§ 205 BAO)  2016, 2017 und 2018, Steuernummer 64-511/1773, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Christian Lind` | `Dr. Christian Lind` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `RgR Shirley Ribler` (person)
- `Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `64-511/1773` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paulina Borisowa  in der Beschwerdesache Ilhan Feldmeier, Bakk. rer. nat.,  Sittenbergstraße 9, 4294 Stampfendorf, Österreich, vertreten durch Mag. Benno Elmar Di Gaspero, Unterer Platz 7, 9372  Eberstein, über die Beschwerde vom 14. Juni 2024 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juni 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 14-548/3314  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Mag. Benno Elmar Di Gaspero` | `Mag. Benno Elmar Di Gaspero` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Paulina Borisowa` (person)
- `Ilhan Feldmeier, Bakk. rer. nat.` (person)
- `Sittenbergstraße 9, 4294 Stampfendorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `14-548/3314` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/148962.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148962.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Univ.-Prof. Ramon Löther  in der Beschwerdesache Axel Pommeränke,  Zum Hauptplatz 2, 4030 Linz, Österreich, vertreten durch Mag. Niki Zaar, Babenbergerstraße 9/1/8, 1010 Wien,  betreffend die Vorlage der Bescheide des Finanzamtes Österreich vom 9. Oktober 2023 über  die Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2018 und 2019 im Wege  des Vorlageberichtes vom 21. November 2024 zur Steuernummer 14-979/7189  den  Beschluss:  Das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Niki Zaar` | `Mag. Niki Zaar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Univ.-Prof. Ramon Löther` (person)
- `Axel Pommeränke` (person)
- `Zum Hauptplatz 2, 4030 Linz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `14-979/7189` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/149721.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149721.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Mag.a Gerda Hellvogt  in der Beschwerdesache Tatjana Wolnik,  Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich, vertreten durch Mag. Ursula Zimmerl, Sternwartestraße 82, 1180 Wien, über  die Beschwerde vom 14. Juli 2025 gegen den Bescheid des Finanzamtes Österreich vom 10. Juli  2025 betreffend Zwangsstrafen 2025, Steuernummer 36-865/6597, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ursula Zimmerl` | `Mag. Ursula Zimmerl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Mag.a Gerda Hellvogt` (person)
- `Tatjana Wolnik` (person)
- `Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `36-865/6597` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Thomas Gell` | `Mag. Thomas Gell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Detlev Bodenmüller` (person)
- `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.` (person)
- `Pux 4, 8753 Paßhammer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `72-997/9457` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

**False Positives:**

- `Sera Trust Gmb` — partial — pred is substring of gold: `Sera Trust GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Thomas Mevis`(person)
- `Lindenhang 30, 4591 Ramsau, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Astoria Stb Gmb` — partial — pred is substring of gold: `Astoria Stb GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein`(person)
- `Leroy Sitterle`(person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich`(address)
- `Astoria Stb GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `NÖ Landesverein` — partial — pred is substring of gold: `NÖ Landesverein für Erwachsenenschutz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Sean Herdling`(person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich`(address)
- `NÖ Landesverein für Erwachsenenschutz`(organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

**False Positives:**

- `Fa Witago  Wirtschaftsprüfungs-` — partial — pred is substring of gold: `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H`

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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Prof. Dr. Thomas Keppert Steuerberatung` — partial — gold is substring of pred: `Prof. Dr. Thomas Keppert`

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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_2`)


Jeffrey Marinopoulos, Moosbauernstraße 12, 9341 Wattein, Österreich, als atypisch still Beteiligte an der vormaligen Leroy Kusznierz,  vertreten durch Prof. Thomas Keppert Steuerberatung und Wirtschaftsprüfung GmbH,  Theobaldgasse 19, 1060 Wien,  über die Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Klagenfurt vom  24. April 2012 die Wiederaufnahme des Verfahrens die Feststellung von Einkünften und die  Feststellung von Einkünften gemäß § 188 BAO betreffend, je für das Jahr 2007, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Prof. Thomas Keppert Steuerberatung` — partial — gold is substring of pred: `Thomas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeffrey Marinopoulos`(person)
- `Moosbauernstraße 12, 9341 Wattein, Österreich`(address)
- `Leroy Kusznierz`(person)
- `Thomas`(person)
- `Finanzamtes Klagenfurt`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dkfm. Anton Lammer  Wirtschaftstreuhand Gmb` — positional overlap with gold: `Anton Lammer  Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `Jacqueline Dittus`(person)
- `Sausal 90O, 4911 Schönfeld, Österreich`(address)
- `Anton Lammer  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Mag. Susanne Pöltenstein-` — partial — pred is substring of gold: `Mag. Susanne Pöltenstein-Rosenegger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Beschwerdesache  des Charlotte Hasslbauer Bf1***, Oed bei Haslach 48, 4782 Aigerding, Österreich Bf1-Adr Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich, vertreten durch  Procurator Treuhand- und Revisionsges.m.b.H., betreffend die Bescheidbeschwerde vom  15. September 2017 betreffend den Bescheid des Bundesministeriums für Finanzen vom  4. August 2017, zugestellt am 18.08.2017, mit dem der Antrag auf Zuerkennung einer  Zuzugsbegünstigung gemäß § 103 Abs. 1 EStG für die Jahre 2017 bis 2031 als unbegründet  abgewiesen wurde  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Procurator Treuhand-` — partial — pred is substring of gold: `Procurator Treuhand- und Revisionsges.m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Charlotte Hasslbauer`(person)
- `Oed bei Haslach 48, 4782 Aigerding, Österreich`(address)
- `Josef Szerencsi-Gasse 57, 5203 Kleinköstendorf, Österreich`(address)
- `Procurator Treuhand- und Revisionsges.m.b.H.`(organisation)
- `Bundesministeriums für Finanzen`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M. Thaler Steuerberatung Kufstein Gmb` — partial — gold is substring of pred: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Achmed Karolzak`(person)
- `Lilia Löffelmann`(person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich`(address)
- `M.`(person)
- `Finanzamtes`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `Maggi Brandl Kathollnig  Rechtsanwalts` — partial — pred is substring of gold: `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Weiß Rechtsanwälte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Regina Vogt`(person)
- `Hon.-Prof.in Elvira Thielsen`(person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_2`)


Saskia Sinnwell, Wien1  beide vertreten durch Christoph Zitz MBA, murtax Steuerberatungs GmbH Kuenburgstraße 10,  5580 Tamsweg  wegen des Finanzvergehens der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG), beim Verband gemäß § 28a Abs. 2 FinStrG, über die Beschwerde  des Amtsbeauftragten vom 17. September 2019 (gemeint wohl richtig: 3. Dezember 2020)  gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19  Klosterneuburg als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. September 2020, SpS 2000, in der Sitzung am 27. Mai 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Christoph Zitz` — partial — pred is substring of gold: `Christoph Zitz MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Saskia Sinnwell`(person)
- `Christoph Zitz MBA`(person)
- `murtax Steuerberatungs GmbH`(organisation)
- `Finanzamt Wien 9/18/19`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `E. Igerz` — partial — pred is substring of gold: `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `Tristan Potente`(person)
- `Hürth 5, 4362 Schönfichten, Österreich`(address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes`(organisation)
- `61-467/9522`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Audit  Partner Austria Wirtschafts-` — partial — pred is substring of gold: `Audit  Partner Austria Wirtschafts- prüfer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Kanzlei Kiffman` — partial — pred is substring of gold: `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Zoltan Dabrowski`(person)
- `OMedR Prof. Hartmut Szardemings`(person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Klaus Plätzer` — partial — pred is substring of gold: `Dr. Klaus Plätzer,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Fatima Eichmayr`(person)
- `Wieskapellenweg 10, 8047 Graz, Österreich`(address)
- `Dr. Klaus Plätzer,`(person)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `67-455/2359`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinI. in der Beschwerdesache Violetta Bailmann, Schlosserfeld 35, 9632 Hochwart, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 20. Oktober 2016 gegen  die Bescheide des Finanzamtes Spittal Villach vom 22. September 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012 (Steuernummer  82-877/4906 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vogelsberger Hoffmann Wacker` — partial — pred is substring of gold: `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Violetta Bailmann`(person)
- `Schlosserfeld 35, 9632 Hochwart, Österreich`(address)
- `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG`(organisation)
- `Finanzamtes Spittal Villach`(organisation)
- `82-877/4906`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache KommR Nicola Sturzbecher, Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich, vertreten durch Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H., Hans-Gasser-Platz 6c, 9500 Villach, über die  Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes Österreich vom  3. Juli 2013 und 25.April 2017 bezüglich Wiederaufnahme des Verfahrens Umsatzsteuer 2009  bis 2011 und Umsatzsteuer 2009 bis 2012 (Steuernummer 19-116/5774 ) beschlossen bzw.  nach Durchführung einer mündlichen Verhandlung am 04.Oktober 2021 zu Recht erkannt:   I. BESCHLUSS  1.

**False Positives:**

- `Arnulf R.` — partial — pred is substring of gold: `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `KommR Nicola Sturzbecher`(person)
- `Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich`(address)
- `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `19-116/5774`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Herrn Mag. Gernot Thonhauser` — partial — gold is substring of pred: `Mag. Gernot Thonhauser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Jedamczik`(person)
- `ÖkR Tobias Schönyan`(person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich`(address)
- `Mag. Gernot Thonhauser`(person)
- `Finanzamtes Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Mag. Grün  Steuerberatungsgesellschaft` — partial — pred is substring of gold: `Mag. Grün  Steuerberatungsgesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Julian Egiede`(person)
- `Theras 97, 4565 Haselbäckau, Österreich`(address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Klagenfurt`(organisation)
- `Finanzamt Österreich`(organisation)
- `Mag. Michael Sablatnik`(person)
- `88-033/6865`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Gisbert Löhberg`(person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich`(address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Österreich`(organisation)
- `73-737/2281`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache OSR Eugenia Balikci, Richardisweg 14, 5134 Ginshöring, Österreich, vertreten durch Wiener Kinder-und Jugendhilfe  2,20, Dresdner Straße 43, 1200 Wien, über die Beschwerde vom 20. März 2020 gegen den  Bescheid des Finanzamtes Österreich vom 25. Februar 2020 betreffend Familienbeihilfe ab  Jänner 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Wiener Kinder-und Jugendhilfe` — type mismatch — same span as gold: `Wiener Kinder-und Jugendhilfe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `OSR Eugenia Balikci`(person)
- `Richardisweg 14, 5134 Ginshöring, Österreich`(address)
- `Wiener Kinder-und Jugendhilfe`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137966.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Thomas Schmidt in der Finanzstrafsache  gegen Linda Tumpach, Gengerberg 44, 4052 Ansfelden, Österreich, vertreten durch Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer, Wiener Straße 3, 3100 St. Pölten, über die Beschwerde der Beschuldigten vom  25.11.2019 gegen den Bescheid des Amtes für Betrugsbekämpfung als Finanzstrafbehörde  (ehemals des Finanzamtes Lilienfeld St. Pölten als Finanzstrafbehörde ) vom 17. Oktober 2019,  Strafkontonummer 91-951/0670, betreffend die Abweisung eines  Zahlungserleichterungsansuchens (Stundungs- und Ratenansuchen) gemäß § 156 Abs. 1 des  Finanzstrafgesetzes (FinStrG) in Verbindung mit   § 260 Abs. 1 lit. a Bundesabgabenordnung (BAO) beschlossen:  Die Beschwerde wird als unzulässig zurückgewiesen, da es sich beim gegenständlich  bekämpften so genannten Bescheid um einen Nichtbescheid handelt.  Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Rechtsanwälte Gloß Pucher Leitner Gloß  Enzenhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Thomas Schmidt`(person)
- `Linda Tumpach`(person)
- `Gengerberg 44, 4052 Ansfelden, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `91-951/0670`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Herrn  Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Herrn Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/138725.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138725.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. David Eckerlin  in der Beschwerdesache Margarete Wasmeir,  Voglstraße 19, 4902 Schlaugenham, Österreich, vertreten durch Mag. Kurt Caspari Steuerberatungs KG, Hirnreit 173, 5771  Leogang, über die Beschwerde vom 29. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 11. Juli 2022 betreffend Säumniszuschlag 2022 Steuernummer 09-312/4413  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Kurt Caspari Steuerberatung` — partial — pred is substring of gold: `Mag. Kurt Caspari Steuerberatungs KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. David Eckerlin`(person)
- `Margarete Wasmeir`(person)
- `Voglstraße 19, 4902 Schlaugenham, Österreich`(address)
- `Mag. Kurt Caspari Steuerberatungs KG`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `09-312/4413`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Olaf Koechig, Zmöllach 3, 3542 Litschgraben, Österreich, Beschwerde vom 25. Oktober 2019 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr Finanzamtes Österreich, vom  28. November 2018 betreffend Umsatzsteuer 2012, Umsatzsteuer 2013, Umsatzsteuer 2014  und Umsatzsteuer 2015, Steuernummer 17-913/2665, der Gartfentri Heizung Institut GmbH, vertreten durch  Gustke Forschung GmbH, hinsichtlich des Vorlageantrages der Gartfentri Heizung Institut GmbH  in  Liquidation, beschlossen:  I. Die Beschwerdevorentscheidungen vom 6. April 2022 betreffend Umsatzsteuer 2012,  2013, 2014 und 2015 der Gartfentri Heizung Institut GmbH  in Liquidation werden aufgehoben.

**False Positives:**

- `Gustke Forschung Gmb` — partial — pred is substring of gold: `Gustke Forschung GmbH`

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

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Freimüller Rechtsanwalts Gmb` — partial — pred is substring of gold: `Freimüller Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Cornelia Reifgerste`(person)
- `Scherzergütl 18K, 9622 Golz, Österreich`(address)
- `Freimüller Rechtsanwalts GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `M. F.`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Muran Grönewald, Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte,  Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 19. Dezember 2019 gegen  die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich) vom  11. Dezember 2019 betreffend Wiederaufnahme § 303 BAO /  ESt 2013 sowie vom 12.12.2019  betreffend Wiederaufnahme § 303 / ESt 2014 und betreffend Wiederaufnahme § 303 / ESt  2015 zu Steuernummer 87-098/9833  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Pallauf Meißnitzer Staindl` — partial — pred is substring of gold: `Pallauf Meißnitzer Staindl & Partner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Muran Grönewald`(person)
- `Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich`(address)
- `Pallauf Meißnitzer Staindl & Partner`(organisation)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `87-098/9833`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ali Brücklmayer  in der Beschwerdesache Ulrike Kudlacek,  Nörsach 15, 4223 Standorf, Österreich, vertreten durch Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH,  Wagnastraße 1, 8430 Leibnitz, über die Beschwerde vom 31. Oktober 2019 gegen den Bescheid  des Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 2. Oktober 2019 betreffend  Aufhebung § 299 BAO /  ESt 2015 Steuernummer 26-799/5403  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Klaus Gaig Wirtschaftsprüfung` — partial — pred is substring of gold: `Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ali Brücklmayer`(person)
- `Ulrike Kudlacek`(person)
- `Nörsach 15, 4223 Standorf, Österreich`(address)
- `Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `26-799/5403`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Finn Rosen  in der Beschwerdesache Dragan Ohlff,  vertreten durch Dr. Sven Rudolf Thorstensen LLM, Neustiftgasse 3/7, 1070 Wien, über die  Beschwerde vom 23. Juli 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom  10. Juli 2019 betreffend den Bescheid über den Ablauf einer Aussetzung der Einhebung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Sven Rudolf Thorstensen` — partial — pred is substring of gold: `Dr. Sven Rudolf Thorstensen LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dr. Finn Rosen`(person)
- `Dragan Ohlff`(person)
- `Dr. Sven Rudolf Thorstensen LLM`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142063.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142063.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Frauke Glowatsch, St.Georgen a.W. 12, 4776 Großwaging, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner,  Rechtsanwälte, Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 11.6.2019  und 26.11.2019 gegen die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt  Österreich;

**False Positives:**

- `Pallauf Meißnitzer Staindl` — partial — pred is substring of gold: `Pallauf Meißnitzer Staindl & Partner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Frauke Glowatsch`(person)
- `St.Georgen a.W. 12, 4776 Großwaging, Österreich`(address)
- `Pallauf Meißnitzer Staindl & Partner`(organisation)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/142680.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142680.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Moritz Lindstaedt  in der Beschwerdesache Samuel Rattai,  Hilzing 64, 2880 Kranichberg, Österreich, vertreten durch Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH, Lehargasse 3A Tür 14, 1060 Wien, über die Beschwerde vom  7. September 2023 gegen den Bescheid des Finanzamtes Österreich vom 30. August 2023  betreffend Zahlungserleichterungen gem. § 212 BAO, Steuernummer 30-750/1577, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Peter Wolf Wirtschaftsprüfungs-` — partial — pred is substring of gold: `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Moritz Lindstaedt`(person)
- `Samuel Rattai`(person)
- `Hilzing 64, 2880 Kranichberg, Österreich`(address)
- `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `30-750/1577`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/143501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143501.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Dimitri Usslar  in der Beschwerdesache Jessica Abdulkarim,  vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien,  gegen den Bescheid des Finanzamtes Österreich vom 15. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Deloitte Tax Wirtschaftsprüfungs Gmb` — partial — pred is substring of gold: `Deloitte Tax Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dimitri Usslar`(person)
- `Jessica Abdulkarim`(person)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/143673.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Sebastian Kötters  in der Beschwerdesache Agnes Hundorf,  Bischofsberg 23, 9123 Unterkrain, Österreich, vertreten durch Mag. Helmut Hirsch Rechtsanwalt, Josef-Krainer-Straße 46/I,  8074 Raaba, über die Beschwerde vom 2. August 2013 gegen den Bescheid des Finanzamt Judenburg Liezen  vom  4. Juli 2013 betreffend Pfändung einer Geldforderung zu Steuernummer 65-832/4960  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Mag. Helmut Hirsch Rechtsanwalt` — partial — gold is substring of pred: `Mag. Helmut Hirsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Sebastian Kötters`(person)
- `Agnes Hundorf`(person)
- `Bischofsberg 23, 9123 Unterkrain, Österreich`(address)
- `Mag. Helmut Hirsch`(person)
- `Finanzamt Judenburg Liezen`(organisation)
- `65-832/4960`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Rauscher und Mag. Glashüttner  als Richter sowie Mag. Aust und Dr. Haid als fachkundige Laienrichter im Beisein des  Schriftführers FOI Dawkins über die Beschwerden der Marion Füchtmann, Hofhaimerplatz 90, 8663 Großveitsch, Österreich, vertreten durch  Dr. Alma Goerts, Primus-Lessiak Weg 6H, 9343 Dielach, Österreich, vom 13.03.2023 gegen den (Sammel-)Bescheid des  Finanzamtes Österreich vom 21.02.2023 betreffend Abweisung von Anträgen auf  Wiedereinsetzung in den vorigen Stand nach mündlicher Verhandlung zu Recht erkannt:  Die Beschwerden werden als unbegründet abgewiesen.

**False Positives:**

- `Dr. Alma Goerts` — partial — gold is substring of pred: `Alma Goerts`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Rauscher`(person)
- `Mag. Glashüttner`(person)
- `Mag. Aust`(person)
- `Dr. Haid`(person)
- `Marion Füchtmann`(person)
- `Hofhaimerplatz 90, 8663 Großveitsch, Österreich`(address)
- `Alma Goerts`(person)
- `Primus-Lessiak Weg 6H, 9343 Dielach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


Das Bundesfinanzgericht hat durch den Senat 6008-1 besetzt mit dem Senatsvorsitzenden  Mag. Johann Fischerlehner, der beisitzenden Richterin Maga. Ulrike Stephan, sowie den  fachkundigen Laienrichtern Michael Hinterreiter, LL.B. und Leopold Pichlbauer in der  Beschwerdesache Philippa Aufheimer, Teichschloßweg 11, 8162 Haufenreith, Österreich, vertreten durch Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH, Bahnhofstraße 13, 4400 Steyr, über die Beschwerde vom 9. März  2023 gegen den Bescheid des Finanzamtes Österreich vom 22. Februar 2023 mit dem der  Antrag gemäß § 299 Abs. 1 Bundesabgabenordnung vom 29.07.2022, eingebracht am  29.07.2022, betreffend den Bescheid über die Wiederaufnahme des Verfahrens gemäß  § 303  Abs. 1 BAO vom 21.12.2021 abgewiesen wurde, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben und der angefochtene  Bescheid dahingehend abgeändert, dass der Bescheid vom 21. Dezember 2021, mit  dem die belangte Behörde zu Einheitswertaktenzeichen EW-AZ die  Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 BAO des mit Bescheid vom  13.12.2016 abgeschlossenen Verfahrens betreffend die Zurechnungsfortschreibung  gemäß § 21 Abs. 4 BeWG zum 01.01.2015 verfügt hat, aufgehoben wird.

**False Positives:**

- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung Gmb` — partial — pred is substring of gold: `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Michael Hinterreiter, LL.B.`(person)
- `Leopold Pichlbauer`(person)
- `Philippa Aufheimer`(person)
- `Teichschloßweg 11, 8162 Haufenreith, Österreich`(address)
- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hoffmann Reitsammer` — partial — pred is substring of gold: `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Ing. Marion Kloefkorn`(person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`(address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `40-620/0106`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/144464.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144464.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Gustav Franzki, Strebersdorfer Friedhof 80, 4712 Haus, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  14. Dezember 2023 gegen den Bescheid des Finanzamtes für Großbetriebe vom 17. November  2023 betreffend Festsetzung Energiekrisenbeitrag-Strom Dezember 2022 bis Juni 2023,  Steuernummer 92-724/7552  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte Gmb` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Krafft`(person)
- `Gustav Franzki`(person)
- `Strebersdorfer Friedhof 80, 4712 Haus, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `92-724/7552`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Calvin Liechtenstein  in der Beschwerdesache KommR Thorsten Voelkerling,  Kirchenbühl 12, 4463 Brunnbach, Österreich, vertreten durch Rechtsanwalt Dr. Gahleithner & Partner OG, Schottengasse 7  Tür 6, 1010 Wien, über die Beschwerde vom 25. September 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 11. September 2019 betreffend den Ablauf der Aussetzung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rechtsanwalt Dr. Gahleithner` — positional overlap with gold: `Dr. Gahleithner & Partner OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Calvin Liechtenstein`(person)
- `KommR Thorsten Voelkerling`(person)
- `Kirchenbühl 12, 4463 Brunnbach, Österreich`(address)
- `Dr. Gahleithner & Partner OG`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Aloisia Bergauer in der Beschwerdesache  Ing. Christian Marckwordt, Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung Energiekrisenbeitrag Strom für den Zeitraum 1.12.2022-30.06.2023,  Steuernummer 22-821/5972, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte Gmb` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Aloisia Bergauer`(person)
- `Ing. Christian Marckwordt`(person)
- `Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `22-821/5972`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/145625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145625.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Fatima Auriga, Tiflisbrücke 7, 8673 Kirchenviertel, Österreich, vertreten durch Sachwalter Dr. Herbert Kaspar sowie die Vindobona-Interbruch  Wirtschaftstreuhand GmbH, Opernring 10/Eingang Goethegasse 3, 1010 Wien, über die  Beschwerde vom 6. Oktober 2020 gegen den Bescheid des Finanzamtes Österreich vom 16. Juli  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018, Steuernummer  36-261/6228  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Sachwalter Dr. Herbert Kaspar` — partial — gold is substring of pred: `Dr. Herbert Kaspar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Fatima Auriga`(person)
- `Tiflisbrücke 7, 8673 Kirchenviertel, Österreich`(address)
- `Dr. Herbert Kaspar`(person)
- `Finanzamtes Österreich`(organisation)
- `36-261/6228`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Beschwerdesache Emanuel Unterlindner, Dr. Hans-Bachmann-Straße 4, 9343 Brunn (Zweinitz), Österreich, vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien, über die Beschwerde vom 29. Juni  2021 gegen die Bescheide über die Wiederaufnahme des Verfahrens betreffend Umsatzsteuer  2011 bis 2014 und Umsatzsteuerbescheide 2011 bis 2014 des Finanzamtes für Großbetriebe,  jeweils vom 6. Mai 2021, Steuernummer 25-482/9290,   A.) zu Recht erkannt:   I.)

**False Positives:**

- `Securitas Revisions-` — partial — pred is substring of gold: `Securitas Revisions- und  Treuhandgesellschaft m.b.H.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Wolfgang Pagitsch`(person)
- `Emanuel Unterlindner`(person)
- `Dr. Hans-Bachmann-Straße 4, 9343 Brunn (Zweinitz), Österreich`(address)
- `Securitas Revisions- und  Treuhandgesellschaft m.b.H.`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `25-482/9290`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_11`)


Dagegen erhob die Bf, vertreten durch Frau Rittcher  fristgerecht Beschwerde mit der Begründung,  dass W.B. die FB erhalten hätte und nicht die Bf (siehe dazu Beschwerdeschriftsatz vom  25.03.2024).

**False Positives:**

- `Frau Rittcher` — partial — gold is substring of pred: `Rittcher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rittcher`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Wladimir Schaeffer  in der Beschwerdesache  Scarlett Ever, Felle 6, 4264 Unterrauchenödt, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom  10. Oktober 2024 gegen den Bescheid des Finanzamtes für Großbetriebe vom 18. September  2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 1. Juli  2023 bis 31. Dezember 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte Gmb` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Wladimir Schaeffer`(person)
- `Scarlett Ever`(person)
- `Felle 6, 4264 Unterrauchenödt, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Niklas Hussung  in der Beschwerdesache Univ.-Prof. Oliver Ruhsbüldt,  Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich, vertreten durch Gattringer Steuerberatung GmbH, Sonnensteinstraße 12, 4040  Linz, über die Beschwerde vom 31. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 16. Mai 2023 betreffend Einkommensteuer 2021 Steuernummer 26-058/9655  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Gattringer Steuerberatung Gmb` — partial — pred is substring of gold: `Gattringer Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Niklas Hussung`(person)
- `Univ.-Prof. Oliver Ruhsbüldt`(person)
- `Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich`(address)
- `Gattringer Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `26-058/9655`(tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/147343.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147343.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Bruno Kleinerts, Emil-Bertalanffy-Weg 4, 9422 Mitterpichling, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1/Freyung, 1010 Wien, über die Beschwerde vom  22. November 2024 gegen die Bescheide des Finanzamtes für Großbetriebe vom 30. August  2024 betreffend Umsatzsteuerzinsen für die Zeiträume 2015, 2016, 01-12/2017, 01-05/2018,  07-09/2018 und 11-12/2018, Steuernummer 41-358/9193, zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Deloitte Tax  Wirtschaftsprüfungs Gmb` — partial — pred is substring of gold: `Deloitte Tax  Wirtschaftsprüfungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Bruno Kleinerts`(person)
- `Emil-Bertalanffy-Weg 4, 9422 Mitterpichling, Österreich`(address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `41-358/9193`(tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/147347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147347.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Tatjana Siegerist, Bakk. phil., Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich, vertreten durch Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH, Wiesentalstraße 40, 90419 Nürnberg, Deutschland, über die  Beschwerde vom 27. Juli 2023 gegen den Bescheid des Magistrats der Stadt Wien, MA 6  Rechnungs- und Abgabenwesen, MA 6/ARL-676259-2022, vom 28. Juni 2023 betreffend  Haftung zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft` — partial — pred is substring of gold: `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Lisa Fries`(person)
- `Tatjana Siegerist, Bakk. phil.`(person)
- `Hofrat-Sturm-Straße 58, 4840 Vöcklabruck, Österreich`(address)
- `Molitor Babel Singer Vitzthum  Partnerschaftsgesellschaft mbH`(organisation)
- `Magistrats der Stadt Wien`(organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

**False Positives:**

- `Sera Trust Gmb` — partial — pred is substring of gold: `Sera Trust GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Ing. Dagobert Almasri`(person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/147955.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147955.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christian Soltendieck  in der Beschwerdesache des Dr. MV  als Masseverwalter (MV) im Insolvenzverfahren der Berthold Grosshans, Gruisla 3Q, 3231 Linsberg, Österreich  vertreten durch  die Berthold Grosshans, Seetal 31, 4661 Altmanning, Österreich  nunmehr vertreten durch Rechtsanwalt Mag. Gregor  Kohlbacher, Keesgasse 11, 8010 Graz, betreffend die Beschwerde vom 12. Oktober 2020 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 15. Mai 2020 über die Zurückweisung eines  Antrages auf Wiedereinsetzung in den vorigen Stand (hinsichtlich Umsatzsteuer 2014 bis 2017  und Umsatzsteuer 1-11/2018), Steuernummer 59-309/9934, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Rechtsanwalt Mag. Gregor  Kohlbacher` — partial — gold is substring of pred: `Mag. Gregor  Kohlbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Christian Soltendieck`(person)
- `Berthold Grosshans`(person)
- `Gruisla 3Q, 3231 Linsberg, Österreich`(address)
- `Berthold Grosshans`(person)
- `Seetal 31, 4661 Altmanning, Österreich`(address)
- `Mag. Gregor  Kohlbacher`(person)
- `Finanzamtes Graz-Stadt`(organisation)
- `59-309/9934`(tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/148079.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148079.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Juliana Haidler  in der Beschwerdesache Helge Gscheidl,  Ragnitzhang 8, 8344 Mahrensdorf, Österreich, vertreten durch Rechtsanwälte F. Niedermann als Inhaberin der UnionTAX &  LAW, Donau-City-Straße 7/DC Tower/30th floor, 1220 Wien, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 9. Februar 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung)   Steuernummer 86-998/8051  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Rechtsanwälte F. Niedermann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Juliana Haidler`(person)
- `Helge Gscheidl`(person)
- `Ragnitzhang 8, 8344 Mahrensdorf, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `86-998/8051`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/148735.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148735.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Lukas Lautenschlaeger, Pelzstraße 31 - 39W, 4710 Grieskirchen, Österreich, vertreten durch Mag. Elke Maria Theißl-Schulmeister,  Weingebirge 3037, 7471 Rechnitz, über die Beschwerde vom 30. Juni 2023 gegen den Bescheid  des Finanzamtes Österreich vom 21. Juni 2023 betreffend Einkommensteuer 2022,  Steuernummer 16-154/3987, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Elke Maria Theißl-` — partial — pred is substring of gold: `Mag. Elke Maria Theißl-Schulmeister`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Lukas Lautenschlaeger`(person)
- `Pelzstraße 31 - 39W, 4710 Grieskirchen, Österreich`(address)
- `Mag. Elke Maria Theißl-Schulmeister`(person)
- `Finanzamtes Österreich`(organisation)
- `16-154/3987`(tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/149000.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149000.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Bernhart Steuerberatungs  Gmb` — partial — pred is substring of gold: `Bernhart Steuerberatungs  GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Jeffrey Stubenrauch, Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich  vertreten durch Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH, Mosetiggasse 1, 1230 Wien, über die Beschwerde vom 31.10.2024  gegen die Bescheide des Finanzamtes Österreich je vom 30.08.2024 die Wiederaufnahme der  Verfahren betreffend Umsatzsteuer 2018-2021, sowie Umsatzsteuer 2018-2022  (Steuernummer 05-888/5257) nach Durchführung einer mündlichen Verhandlung am  10.10.2025   I. beschlossen:  Die Beschwerde vom 31.10.2024 gegen den Umsatzsteuerbescheid 2022 vom 30.  August 2024 wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Aviso Wirtschaftstreuhand-` — partial — pred is substring of gold: `Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Jeffrey Stubenrauch`(person)
- `Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich`(address)
- `Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `05-888/5257`(tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/149813.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149813.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Roy Scheit, Kaiserblickstraße 14, 5700 Bruckberg, Österreich, vertreten durch Intercura Treuhand- und Revisionsgesellschaft mbH,  Bösendorferstraße 2/4/15, 1010 Wien, betreffend die Beschwerden vom 18. Jänner 2024  gegen die Bescheide des Finanzamtes Österreich vom 23. November 2023 betreffend  Umsatzsteuer 2018, Umsatzsteuer 2019, Umsatzsteuer 2020, Umsatzsteuer 2021,  Umsatzsteuer 2022 und Umsatzsteuer-Identifikationsnummer UID 23.11.2023 Steuernummer  30-818/6381  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Intercura Treuhand-` — partial — pred is substring of gold: `Intercura Treuhand- und Revisionsgesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Roy Scheit`(person)
- `Kaiserblickstraße 14, 5700 Bruckberg, Österreich`(address)
- `Intercura Treuhand- und Revisionsgesellschaft mbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `30-818/6381`(tax_number)

</details>

---

## `abbreviated_person_herr_frau` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `edefcae4`  
**Description:**
Captures abbreviated person references like 'Herr M.' or 'Frau M.' found in later text sections.

**Content:**
```
(?:Herr|Frau)\s+([A-Z])\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 61 | 0 | 61 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 61 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_7`)


Weiters übermittle ich beiliegend Rechnungen betreffend den Zeitraum, woraus hervorgeht,  dass Herr H. H. keineswegs vollversorgt war und bis zum gegenwärtigen Zeitpunkt ist und auch  ständig laufende Ausgaben hat.

**False Positives:**

- `H $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_9`)


Des Weiteren musste  Herr H. auch Ausgaben tätigen für diverse Möbel, ein TV-Gerät, Kleidung, usw.

**False Positives:**

- `H $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_11`)


Somit leistet Herr H. sehr wohl laufend Beiträge zu seinem Unterhalt und wird nicht  vollversorgt.“

**False Positives:**

- `H $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_496`)


RA verwies auf die anwesenden Auskunftspersonen S1 und S2 A. und Z.3 zur Fleischqualität in  den Streitjahren, wiederholte die bisherigen Ausführungen zu den nahe gelegenen Lokalen  samt den unterschiedlichen Entwicklungen beim Rohaufschlag und brachte zur Geschichte der  Lokale in den Streitjahren vor, dass Herr A., bedingt durch das sehr beschränkte Platzangebot  im Lokal W-Platz, beschlossen habe, die Nieder Waldbach GmbH zu übernehmen und das Geschäft  auszuweiten.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nieder Waldbach GmbH`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_213`)


Bauvorhaben: Wien4 Bauträger  Die vorgebliche Fremdleistungsfirma PGIV Umwelt Entwicklung GmbH hatte ihre offizielle Geschäftsanschrift in  Firmensitz, wo auch deren angeblicher Alleingesellschafter und Geschäftsführer, Herr D. C.,  geb. 1952, unbekannten Aufenthalts, seinen gemeldeten Wohnsitz innehatte.

**False Positives:**

- `D $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PGIV Umwelt Entwicklung GmbH`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_42`)


„Kuraufenthalt“ der Ehefrau des Bf.  Bezüglich der Notwendigkeit der für die Ehegattin des Bf., Frau E., beantragten Kosten für  „Kuraufenthalt“ in Höhe von Euro 1.634,31 wurde lediglich ein ärztlicher Befundbericht einer  Fachärztin für Orthopädie vorgelegt, in dem einzelne Therapien (z.B. Kälteanwendungen,  Massagen, Schlammpackungen etc.) empfohlen wurden.

**False Positives:**

- `E $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_32`)


2.2 Frau A. W erklärt hiemit, diese Rechtseinräumung anzunehmen.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_274`)


Es ist dann jemand von der Firma, nämlich ein Herr M. gemeinsam mit Herrn K. zu mir  gekommen.

**False Positives:**

- `M $2.` — positional overlap with gold: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_275`)


Frage: Haben Sie nachgefragt bei Herrn M., wer die zweite anwesende Person (gemeint ist der  kein Wort deutsch sprechende Herr K., der Geschäftsführer der e.) ist?

**False Positives:**

- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_277`)


Antwort: Herr M. hat sich bei mir als Geschäftsführer vorgestellt. Herr K. sollte der „Big Boss"  sein.

**False Positives:**

- `M $2.` — positional overlap with gold: `M.`
- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_278`)


Herr K. hat kein Deutsch gesprochen.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_283`)


Herr K. hat dem Geschäft zugestimmt.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_295`)


Herr K. und Herr M. waren da auch  anwesend.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation
- `M $2.` — positional overlap with gold: `M.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_296`)


Auf dem vorgelegten Bild ist Herr K. der mittlere Herr.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_399`)


Bei diesem Besuch waren anwesend: ich, Herr Z, Herr K., Herr M. und die Buchhalterin  gemacht.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation
- `M $2.` — positional overlap with gold: `M.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_550`)


Dieser Umstand spricht für die Gutgläubigkeit der Bf.  Was die anfängliche Verwechslung des Gf. der Bf. betreffend Herrn K. betrifft, wonach er nicht  gewusst habe, welche Funktion Herr K. gehabt habe, ist entgegenzuhalten, dass sich die  Unkenntnis nur auf das erste Zusammentreffen bezog und sich der Bf. dann eine Passkopie und  die Visitenkarte von Herrn K. aushändigen hat lassen.

**False Positives:**

- `K $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_20`)


Folgende beantragten bzw. in den zugrunde gelegten Unterlagen diagnostizierten  Gesundheitsschädigungen erreichen keinen Grad der Behinderung:  Stellungnahme zu Vorgutachten: keines vorliegend  Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  Begründung - GdB liegt rückwirkend vor:  Herr S. X. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen: Es liegt kein Leiden vor, das eine  dauerhafte Erwerbsunfähigkeit bedingt.

**False Positives:**

- `S $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_75`)


Herr S. X. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  4 von 14 Seite 5 von 14

**False Positives:**

- `S $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_107`)


Herr S. X. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde Unfähig- keit, sich selbst den Unterhalt zu verschaffen: Es liegt keine Beeinträchtigung vor, welche eine  dauerhafte Erwerbsunfähigkeit bedingt.

**False Positives:**

- `S $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_22`)


Der Beschwerde beigelegt wurde eine ärztliche Bestätigung des Psychiaters M. vom  07.12.2021, die wie folgt lautet:   „Frau H. steht bei mir in regelmäßiger Betreuung bei F33.-Rezidivierende depressive Störung.

**False Positives:**

- `H $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_66`)


Dazu legt sie ein ärztliche „Attest“ vom 07.12.2021 vor mit folgendem Inhalt:   „Frau H. steht bei mir in regelmäßiger Betreuung bei F33.-Rezidivierende depressive Störung.

**False Positives:**

- `H $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_22`)


Herr L. F. habe sich mit  dem Führerschein ausgewiesen (Verweis auf die beigefügte Kopie des Führerscheins).

**False Positives:**

- `L $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_23`)


Betreffend der GZ. MA67/Zahl/2022 sei der Firma beim Ausfüllen der Lenkerauskunft ein  Fehler unterlaufen, der Lenker sei Herr T., 1040 Wien, Gasse1, gewesen.

**False Positives:**

- `T $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_5`)


Frau F. M. kommt  an die psychologische Universitätsambulanz der X Privatuniversität um eine  Autismusdiagnostik durchführen zu lassen.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_6`)


…  Anamnese:  Die Anamnese wurde mit Frau F. persönlich am 23.10.2019 durchgeführt.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_7`)


Frau F. ist aktuell 27  Jahre alt (Identität überprüft), ledig und lebe alleine in einer Wohnung in Wien.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_12`)


Als Grund vermutet Frau F. unter anderem die mangelnde Struktur der von ihr  besuchten „Alternativ-Schule“ und die vorliegende Legasthenie.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_21`)


In Hinblick auf ihre familiäre Situation berichtet Frau F., dass ihre Eltern verheiratet seien und  sie eine jüngere Schwester (25) habe.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_24`)


Bis auf eine Pollenallergie verneint Frau F. die Frage nach körperlichen Beschwerden oder einer  regelmäßigen Einnahme von Medikamenten.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_28`)


Ihre  sexuelle Entwicklung beschreibt Frau F. als unauffällig.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_29`)


In ihrer Freizeit ordne Frau F. gerne Gegenstände.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_33`)


Beispielsweise gibt die Mutter der Patientin an, dass Sie sich große  Sorgen über Frau F. Zustand mache, da sich ihre Tochter immer mehr zurückziehe und  beispielsweise auch seit dem Sommer keinen Kontakt mehr mit ihren zwei engsten Freun- dinnen habe.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_34`)


Frau F. zeige laut Aussagen ihrer Mutter kein Interesse anderen Personen,  imitiere jedoch soziale Verhaltensweisen von denen sie den Eindruck habe, dass diese sozial  erwünscht seien.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_38`)


In  Hinblick auf starre Verhaltensweisen erzählt sie, dass Frau F. jeden Abend zu ihr zu Besuch  komme und die Patientin sich irritiert fühle bzw. ihr das nicht gefalle, wenn dieses abendliche  Treffen einmal aus unterschiedlichen Gründen ausfalle.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_40`)


Frau F. erscheint jeweils pünktlich zu den ausgemachten Terminen.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_43`)


Darüber hinaus bringt Frau F. Vorbefunde sowie  Tagebucheinträge mit, welche als weitere Informationsquellen für die Befundung  herangezogen werden können.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_44`)


Auch Fragebögen und andere Testinstrumente werden Frau F.  sehr konzentriert und gewissenhaft bearbeitet.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_45`)


Psvchopathologischer Status  Frau F. macht zum Zeitpunkt der klinisch-psychologischen Testungen einen kooperativen, aber  bedrückten Eindruck.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_52`)


Frau F. ist in beiden Affektskalen affizierbar, wobei die Schwingungsfähigkeit der  Patientin im direkten Kontakt nicht beobachtet werden kann.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_56`)


Untersuchungsverfahren  - Exploratives Gespräch  - Verhaltensbeobachtung  - Symptom-Checkliste-SCL-90-R (SCL-90-R)  - WHO Quality ofLife {WHOQOL-BREF)  Strukturiertes Klinisches Interview für DSM-IV (SKID I)  Strukturiertes Klinisches Interview für DSM-IV (SKID II)  Diagnostische Beobachtungsskala für Autistische Störungen (ADOS-2)  Diagnostisches Interview für Autismus -Revidiert (ADI-R)  Theory of Mind (TOM)  - Reading Mind in the Eyes Test (REM)  Zusammenfassung und Empfehlung  Störungsübergreifend zeigt sich, dass Frau F. bei der SCL-90 einen erhöhten Wert bei der Skala  Unsicherheit in Sozialkontakten erreicht.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_57`)


Im Hinblick auf die Lebensqualität von Frau F. wird  deutlich, dass die psychische Lebensqualität mit einem Gesamtscore von 50 am geringsten  ausgeprägt ist, und die Lebensqualität hinsichtlich der Umwelt mit einem Gesamtscore von  90,63 am höchsten ausgeprägt ist.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_59`)


Es zeigt sich, dass Frau F. die Kriterien für eine spezifische Phobie  (Spinnen) erfüllt. Die geschilderten depressiven Symptome (z.B. Antriebslosigkeit, negative  Stimmung) rechtfertigen aufgrund der Dauer und Intensität nicht die Vergabe einer klinischen  Diagnose.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_60`)


Im Hinblick auf die Persönlichkeitsstruktur von Frau F. werden zwanghafte  Persönlichkeitsanteile deutlich, welche jedoch besser durch Symptome der  Autismusspektrumstörung erklärt werden können.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_68`)


Es fällt Frau  F. schwer soziale Zusammenhänge zu erkennen und zu deuten.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_81`)


Die Testergebnisse und Empfehlungen wurden Frau F. im Rahmen eines persönlichen  Gesprächs erläutert.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_108`)


13.11.2019,22.11.2019, 6.12.2019 (Mutter), 11.12.2019,  20.12.2019 (Mutter), 08.01.2019  Frau F. M. kommt an die psychologische Universitätsambulanz der X Privatuniversität um eine  Autismusdiagnostik durchführen zu lassen.

**False Positives:**

- `F $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_114`)


Frau M. F. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde Unfähi- gkeit, sich selbst den Unterhalt zu verschaffen: nach Art und Ausprägung: Kein Leiden welches  eine Erwerbsunfähigkeit begründet.

**False Positives:**

- `M $2.` — positional overlap with gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_157`)


Frau M. F. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Es liegt keine zweifelsfrei dokumentierte Gesundheitsschädigung vor, die die dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, zur Folge hat.

**False Positives:**

- `M $2.` — positional overlap with gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_25`)


Ich kann folgende zusätzliche Angaben machen:   Meines Wissens ist Herr D. am 9.7.2022 nach Wien gereist   Die Dauer seines Aufenthaltes ist mir unbekannt   Über seine Unterkunft in Österreich bin ich nicht informiert   Herr D. ist ein Bekannter, deshalb gibt es auch keinen schriftlichen Mietvertrag   Die Übergabe erfolgte am 10.7.2022 um die Mittagszeit in Wien Josefstadt, Uhlplatz im  Beisein eines Freundes aus Ghana.

**False Positives:**

- `D $2.` — no gold match — likely missing annotation
- `D $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_50`)


Er habe der Behörde durch Nennung aller ihm zur Verfügung  stehenden Informationen mehr als glaubhaft gemacht, dass Herr D. im genannten Zeitraum  das Fahrzeug in seinem Besitz gehabt habe.

**False Positives:**

- `D $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/141508.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141508.1_64`)


Herr D. sei ein Bekannter, weshalb es auch keinen schriftlichen  5 von 11 Seite 6 von 11

**False Positives:**

- `D $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_115`)


Festgestellt wird vom Bundesfinanzgericht, dass der Veräußerer der Eigentumswohnung, Herr  V., hinsichtlich des Verkaufs bzw. der Lieferung der gegenständlichen Eigentumswohnung Top  xx gegenüber dem Finanzamt nicht zur Steuerpflicht optiert hat.

**False Positives:**

- `V $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_144`)


Dienststelle des FAÖ ergänzt: Der Verkäufer, Herr  V., St.Nr. …, hat hinsichtlich der veräußerten Wohnung in der X-Straße xx, Top xx, Ort2  (Miteigentum zu xx/xxx Anteilen an der Liegenschaft in EZ xxx GB xxxxx Ort1, Gst. xxx) weder  Umsatzsteuer erklärt noch abgeführt.

**False Positives:**

- `V $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FAÖ`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_16`)


Da seine Schwester, Frau M. seit ihrem 12.

**False Positives:**

- `M $2.` — positional overlap with gold: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_30`)


Im Zuge des Verfahrens habe festgestellt werden können, dass der Parkausweis gemäß § 29b  StVO mit der Nr. 123 vom Sozialministeriumservice, Landesstelle Wien, für Frau M., geb. 1980,  wohnhaft 1230 Wien, Str2, ausgestellt worden sei.

**False Positives:**

- `M $2.` — positional overlap with gold: `M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/146254.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146254.1_92`)


Als Pächter war Herr A. vorgesehen.

**False Positives:**

- `A $2.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_163`)


M.M.A. und dessen Frau M.M.B. nur sehr ungenau abgesprochen.

**False Positives:**

- `M $2.` — positional overlap with gold: `M.M.B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.M.A.`(person)
- `M.M.B.`(person)

</details>

---

## `generic_title_initial_person` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `94ae579e`  
**Description:**
Captures anonymized or specific title patterns like 'Ing. X..' or 'GF AA' which do not fit standard name structures but are clearly person references in context.

**Content:**
```
(?:Ing\.\s+[A-Z]\.{2}|GF\s+AA)
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

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_91`)


„Arbeitsplätze“ zu den  genannten Bedingungen in Bestand nahmen, geht aus den Ausführungen der Bf. im Rahmen  der mündlichen Verhandlung hervor, ebenso das Faktum, dass es sich bei einer dieser  Kommanditisten, nämlich DD, gleichzeitig um eine Angestellte der Bf. und Mutter des GF AA  handelt (VH-Protokoll vom 10.10.2025, S. 2).

**False Positives:**

- `` — partial — pred is substring of gold: `GF AA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GF AA`(person)

</details>

---

## `case_citation_person` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4070bee0`  
**Description:**
Captures person names at the end of case citations (e.g., 'Tomistaw Trapkowski;').

**Content:**
```
(?:EuGH|BGH|BVerfG)\s+\d+\.\d+\.\d+,\s+\w+-?\d+/\d+,\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)[;:]?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 33 | 0 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 33 | 1851 |

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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_91`)


EuGH  14.07.2005, C-434/03, Charles-Tijmens) ein Zuordnungswahlrecht besteht.

**False Positives:**

- `Charles` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_226`)


Diese Auffassung ist spätestens seit den Urteilen EuGH 11.9.2014, C-394/13, B, und EuGH  22.10.2015, C-378/14, Tomisław Trapkowski, als überholt anzusehen (vgl. BFG 7.2.2017,  RV/7106469/2016).

**False Positives:**

- `Tomis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_227`)


In seinem Erkenntnis VwGH 22.11.2016, Ro 2014/16/0067, hat der Verwaltungsgerichtshof  (ohne Bezug auf die Urteile EuGH 11.9.2014, C-394/13, B, und EuGH 22.10.2015, C-378/14,  Tomisław Trapkowski) klargestellt, dass im Anwendungsbereich des Unionsrechts die  Wohnortklauseln des FLAG 1967 nicht anzuwenden sind:   „14 Sowohl die Mitbeteiligte als auch deren Sohn und dessen leiblicher Vater hatten im  Streitzeitraum nach den Feststellungen im angefochtenen Erkenntnis ihren Wohnort in Ungarn  und sie sind nach dem Revisionsvorbringen sowie dem Akteninhalt ungarische  Staatsangehörige, sodass für sie die Verordnung Nr. 883/2004 gemäß deren Art. 2 Abs. 1 gilt.   15 Daher finden die auf Wohnortklauseln beruhenden Bestimmungen des § 2 Abs. 1 FLAG,  welche den Familienbeihilfenbezug auf den Wohnort im Bundesgebiet abstellt, des § 2 Abs. 8  FLAG, welche auf den wesentlich durch den Wohnort bestimmten Mittelpunkt der  Lebensinteressen im Bundesgebiet abstellt, und des § 5 Abs. 3 FLAG, das einen vom Wohnort  abhängigen Ausschluss der Familienbeihilfe bei ständigem Aufenthalt des Kindes im Ausland  vorsieht, zufolge des Art. 7 der Verordnung Nr. 883/2004 und dessen Anwendungsvorrangs  insoweit keine Anwendung.

**False Positives:**

- `Tomis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Trapkowski`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_131`)


Falls die zweite Übertragung dieser Befähigung vor der  innergemeinschaftlichen Beförderung stattfand, kann diese nicht der Erstlieferung an den  Ersterwerber zugeordnet werden (vgl. EuGH 26.7.2017, C-386/16, Toridas, Rn. 36;

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_321`)


Falls die zweite Übertragung dieser Befähigung vor der innergemeinschaftlichen  Beförderung stattfand, kann diese nicht der Erstlieferung an den Ersterwerber zugeordnet  werden (vgl. EuGH 26.7.2017, C-386/16, Toridas, Rn. 36;

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_322`)


EuGH 19.12.2018, C-414/17, Arex, Rn.  70).

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_342`)


In zahlreichen Urteilen des EuGH wurde bereits klargestellt, dass der Begriff  der „Lieferung" sich nicht auf die Eigentumsübertragung in den durch das anwendbare  nationale Recht vorgesehenen Formen bezieht, sondern dass sie jede Übertragung eines  körperlichen Gegenstands durch eine Partei umfasst, die die andere Partei ermächtigt, über  diesen Gegenstand faktisch so zu verfügen, als wäre sie sein Eigentümer (vgl. ua EuGH  8.2.1990, 320/88, Shipping and Forward Enterprise Safe).

**False Positives:**

- `Shipping` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_830`)


Falls die zweite Übertragung vor der  innergemeinschaftlichen Beförderung stattfand, kann diese nicht der Erstlieferung an den  Ersterwerber zugeordnet werden (EuGH Toridas, Rn. 36, EuGH 19.12.2018, C-414/17, Arex, Rn.  55 von 59 Seite 56 von 59

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_838`)


Falls die zweite Übertragung  dieser Befähigung vor der innergemeinschaftlichen Beförderung stattfand, kann diese nicht  der Erstlieferung an den Ersterwerber zugeordnet werden (vgl. EuGH 26.7.2017, C-386/16,  Toridas, Rn. 36;

**False Positives:**

- `Toridas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_839`)


EuGH 19.12.2018, C-414/17, Arex, Rn. 70).

**False Positives:**

- `Arex` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_77`)


Dazu gehört das kumulative Vorhandensein von technischer  Ausstattung und eigenem Personal über einen längeren Zeitraum an der betreffenden  Betriebsstätte (vgl. zuletzt EuGH 3.6.2021, C-931/19, Titanium und VwGH 7.5.2021,  Ra 2020/15/0115).

**False Positives:**

- `Titanium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/141338.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141338.1_81`)


Folglich kann aufgrund des Innehabens eines Wohnsitzes in Österreich,  wenn das Unternehmen im Ausland betrieben wird, gemäß § 6 Abs. 1 Z 27 UStG 19954 nicht  angewendet werden (vgl. EuGH 26.10.2010, Rs C-97/09, Schmelz und EuGH 6.10.2011,   C-421/10, Stoppelkamp).“  4. Die unionsrechtlichen Grundlagen für die Kleiununternehmerregelung findet sich in der  Richtlinie 206/112/EG des Rates über das gemeinsame Mehrwertsteuersystem  (Mehrwertsteuer-Richtlinie):  Nach Art. 272 Abs. 1 Buchst.

**False Positives:**

- `Stoppelkamp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schmelz`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_168`)


(vgl EuGH 18.09.2019, C-32/18, Michael Moser, EuGH 22.1.2015, C- 378/14, Omislaw Trapkowski, EuGH 14.10.2010, C-16/09, Schwemmer, BFG 27.06.2023,  RV/7105857/2017)

**False Positives:**

- `Michael Moser` — no gold match — likely missing annotation
- `Schwemmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_175`)


(vgl EuGH 22.10.2015, C-378/14,  Tomislaw Trapkowski, BFG 27.06.2023, RV/7105857/2017)

**False Positives:**

- `Tomislaw Trapkowski` — partial — gold is substring of pred: `Trapkowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_177`)


(vgl VwGH 24.06.2021, Ro 2018/16/0040, unter Hinweis auf EuGH  18.09.2019, C-32/18, Michael Moser, Rn 44 und EuGH 22.10.2015, C-378/14, Tomislaw  Trapkowski, Rn 39 bis 41)

**False Positives:**

- `Michael Moser` — no gold match — likely missing annotation
- `Tomislaw  Trapkowski` — partial — gold is substring of pred: `Trapkowski`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Trapkowski`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_183`)


(Vgl EuGH 22.10.2015, C-378/14, Tomislaw Trapkowski, VwGH  24.06.2021, Ro 2018/16/0040, BFG 27.06.2023, RV/7105857/2017)

**False Positives:**

- `Tomislaw Trapkowski` — partial — gold is substring of pred: `Trapkowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trapkowski`(person)
- `BFG`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_390`)


Nach der Rechtsprechung des Europäischen Gerichtshofs setzt die Feststellung einer  missbräuchlichen Praxis auf dem Gebiet der Mehrwertsteuer zum einen voraus, dass die  fraglichen Umsätze trotz formaler Anwendung der Bedingungen der einschlägigen  Bestimmungen der Richtlinien und des zu ihrer Umsetzung erlassenen nationalen Rechts einen  Steuervorteil zum Ergebnis haben, dessen Gewährung dem mit diesen Bestimmungen  verfolgten Ziel zuwiderliefe, und zum anderen aus objektiven Anhaltspunkten ersichtlich ist,  dass mit den fraglichen Umsätzen im Wesentlichen lediglich ein Steuervorteil bezweckt wird  (vgl. EuGH 27.10.2011, C-504/10, Tanoarch, Rn 52;

**False Positives:**

- `Tanoarch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_391`)


EuGH 22.12.2010, C-103/09, Weald  Leasing).

**False Positives:**

- `Weald  Leasing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_401`)


Außerdem verweist der Gerichtshof darauf, dass eine Abgrenzung einer unternehmerischen  Einnahmenerzielung vom privaten Konsum eine Beurteilung der Gesamtheit der  Gegebenheiten des Einzelfalles erforderlich macht (EuGH 26.09.1996, C-230/94, Enkler).

**False Positives:**

- `Enkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_403`)


Fehlen einer Tätigkeit wirtschaftliches Kalkül, ein eigenwirtschaftliches  Interesse und ist sie von der Absicht der Unentgeltlichkeit, der Gefälligkeit, des familiären  Zusammenwirkens bestimmt oder mangelt es an einer leistungsbezogenen Gegenleistung, so  wird sie nicht zur Einnahmenerzielung ausgeübt (vgl. EuGH 29.10.2009, C-246/08, Komm/  Finnland).

**False Positives:**

- `Komm` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_197`)


Das EWR-Abkommen ist ein Abkommen im Sinne des Artikels 310 EGV. Derartige Abkommen  sind von ihrem Inkrafttreten an integrierender Bestandteil der Gemeinschaftsrechtsordnung  und daher im Sinne der Rechtsprechung des Europäischen Gerichtshofes auszulegen (vgl EuGH  15.06.1999, C-321/97, Andersson).

**False Positives:**

- `Andersson` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_213`)


Da es sich bei  der Niederlassungsfreiheit um Primärrecht handelt, genügt bereits die Möglichkeit einer  Diskriminierung, um gegen dieses zu verstoßen (vgl bspw EuGH 13.03.2007, C-524/04, Test  Claimants in the Thin Cap Group Litigation).

**False Positives:**

- `Test  Claimants` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_221`)


Der aus § 12 Abs. 1 Z 10 KStG 1988  resultierende Nachteil sei geeignet, die Ausübung der Niederlassungsfreiheit durch  österreichische Gesellschaften zu behindern, indem diese davon abgebracht werden, eine  Tochtergesellschaft in einem „Niedrigsteuer-Mitgliedstaat“ zu gründen, zu erwerben oder zu  behalten (vgl EuGH 12.09.2006, C-196/04, Cadbury Schweppes und Cadbury Schweppes  Overseas).

**False Positives:**

- `Cadbury Schweppes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_222`)


Daneben sei die unterschiedliche Behandlung österreichischer  Tochtergesellschaften je nach dem Ort des Sitzes ihrer Muttergesellschaft (Hoch- vs.  Niedrigsteuerland) geeignet, die Niederlassungsfreiheit der ausländischen Muttergesellschaft  zu beschränken (vgl EuGH 12.12.2002, C-324/00, Lankhorst-Hohorst).

**False Positives:**

- `Lankhorst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_224`)


Darüber hinaus sind  betroffene innerstaatliche Zahlungen an gemeinnützige, mildtätige oder kirchliche  Gesellschaften nicht mit grenzüberschreitenden Zahlungen an gewinnorientierte ausländische  Gesellschaften vergleichbar (EuGH 12.12.2002, C-324/00, Lankhorst-Hohorst, Rn 28).

**False Positives:**

- `Lankhorst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_228`)


Im Falle einer Beschränkung aus Gründen des öffentlichen Interesses muss die Beschränkung  geeignet sein, die Erreichung des fraglichen Zieles zu gewährleisten, und darf nicht über das  hinausgehen, was hierzu erforderlich ist (EuGH 12.09.2006, C-196/04, Cadbury Schweppes, RN  47).

**False Positives:**

- `Cadbury Schweppes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_239`)


Allein die Möglichkeit, dass die Kredit- und  Lizenzverträge auch von inländischen Gesellschaften ausgeführt werden könnten, reicht nicht  aus um eine rein künstliche Gestaltung anzunehmen (vgl EuGH 12.09.2006, C-196/04, Cadbury  Schweppes plc und Cadbury Schweppes Overseas Ltd).

**False Positives:**

- `Cadbury  Schweppes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_247`)


Die Norm müsste daher sowohl dem Steuerpflichtigen die Möglichkeit zum  Vorbringen wirtschaftlicher Gründe einräumen, als auch objektiv nachvollziehbare Umstände  vorsehen mit denen festgestellt werden kann, ob eine künstliche Konstruktion vorliegt (vgl  EuGH 21.01.2010, C-311/08, Société de Gestion Industrielle SA (SGI)).

**False Positives:**

- `Soci` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_264`)


Zur unionsrechtlichen Beurteilung des konzerninternen Abzugsverbots für niedrig besteuerte  Zinsen und Lizenzgebühren war schließlich insbesondere auf die folgenden Urteile des EuGH  hinzuweisen:  - EuGH 20.01.2021, C-484/19, Lexel AB,  - EuGH 04.10.2024, C-585/22, X BV.  19 von 26 Seite 20 von 26

**False Positives:**

- `Lexel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `narrative_person_name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `41fcad1f`  
**Description:**
Captures full person names appearing after specific legal context markers like 'Verteidiger' or 'Beschuldigte' but excludes the title itself.

**Content:**
```
(?:Verteidiger|Beschuldigte|Antragsteller|Kläger|Beklagte)\s+([A-Z][a-zäöüßÄÖÜß\.\-]+(?:\s+[A-Z][a-zäöüßÄÖÜß\.\-]+)+)(?=\s+[a-z]|\.\s|$)
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

</details>

---

<details>
<summary>❌ False Negatives (1289, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)

Die Auskunft könne Herr **Russbüldt** als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

- missed: `Russbüldt` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_290`)

1994, C-60/93, Rs R.L. **Aldewereld** Rn 10).

- missed: `Aldewereld` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)

Das Bundesfinanzgericht hat durch den Richter **Priv.-Doz. Herbert Lindermayer**  in der Beschwerdesache Anneliese Dreschmann,  Nußbacher Straße 43, 3650 Kehrbach, Österreich, vertreten durch Schwaiger & Partner Steuerberatung, Anton-Eder-Straße 5,  6020 Innsbruck, über die Beschwerde vom 19. Jänner 2021 gegen den Bescheid des FA Graz-Stadt  vom 13. Jänner 2021 betreffend Energieabgabenvergütung 2015 Steuernummer  60-855/1189  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Priv.-Doz. Herbert Lindermayer` (person)
- predicted in sentence: `Anneliese Dreschmann`

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)

IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter **Univ.-Prof. Massimo Friedhoff**  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Univ.-Prof. Massimo Friedhoff` (person)
- predicted in sentence: `Jaden Grothmann`

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)

Herr **Harald Hilderink**  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_138`)

Stellungnahme zu Vorgutachten:   unverändert zum VGA   Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:   x ja   □ nein   GdB liegt vor seit: 05/2018   Begründung – GdB liegt rückwirkend vor:   siehe Vorgutachten   x Dauerzustand   Gutachten erstellt am 21.09.2020 von **Sandro Vulbrecht**  Gutachten vidiert am 21.09.2020 von Janet Aspenleitner

- missed: `Sandro Vulbrecht` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_29`)

Im Urteil vom 22.10.2015, C-378/14 (Tomisiaw **Trapkowski**) hat der Gerichtshof der  Europäischen Union dazu folgende Rechtsansicht vertreten:   Art. 60 Abs. 1 Satz 2 der Verordnung (EG) Nr. 987/2009 des Europäischen Parlaments und des  Rates vom 16. September 2009 zur Festlegung der Modalitäten für die Durchführung der  Verordnung (EG) Nr. 883/2004 über die Koordinierung der Systeme der sozialen Sicherheit ist  dahin auszulegen, dass die in dieser Bestimmung vorgesehene Fiktion dazu führen kann, dass  3 von 33 Seite 4 von 33

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_471`)

Aufgrund der  Neurodermitis stehe der Aufwand mit der Behinderung in Zusammenhang, € 87,48 seien daher  eine ag Bel ohne SB.   24.01.2013 € 50,64 Osspura Theodora Hartzheim, BA Bakk. phil. FK 25,32   26.02.2013 € 50,64 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32   26.03.2013 € 45,00 Osspura **Theodora Hartzheim, BA Bakk. phil.** FK € 25,32  19.06.2013 € 50,4 Osspura Theodora Hartzheim, BA Bakk. phil. FK € 25,32   32 von 43 Seite 33 von 43

- missed: `Theodora Hartzheim, BA Bakk. phil.` (person)
- predicted in sentence: —

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131286.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131286.1_2`)

Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Puntigam über die Beschwerde  des **Jaden Holzfuss**, Clemens-Holzmeister-Gasse 3, 3521 Reichau, Österreich, vom 4. November 2020, gegen die Vollstreckungsverfügung  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 18. April 2020, Zl. Zahl, in  Zusammenhang mit der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, zu  Recht erkannt:  Gemäß § 50 VwGVG wird der Beschwerde Folge gegeben und die angefochtene Voll- streckungsverfügung aufgehoben.

- missed: `Jaden Holzfuss` (person)
- predicted in sentence: `Mag. Manuela Puntigam`

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_11`)

Als Mitglied des Heidrun Schweinebraden  sei die Beschwerdeführerin der **Dorothea Hasslocher**  als Zentralinstitut angeschlossen und damit gemäß § 27a BWG verpflichtet, zur  Sicherung der Finanzmarktstabilität an einem System des gemeinsamen Liquiditätsausgleichs  teilzunehmen (Liquiditätsverbund).

- missed: `Dorothea Hasslocher` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden MMag. Gerald Erwin Ehgartner und die  weiteren Senatsmitglieder Mag. Elisabeth Traxler, Mag. Harald Zeller und **Christian Ringseis** in  der Beschwerdesache Muran Iossifidis, Birken-Siedlung 22, 4715 Unterstetten, Österreich, vertreten durch KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  über die Beschwerde vom 30. August 2023 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 11. Juli 2023 betreffend Beschwerdezinsen (§ 205a BAO) nach  Durchführung einer mündlichen Verhandlung am 29. November 2023 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Christian Ringseis` (person)
- predicted in sentence: `Muran Iossifidis`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache **Theodora Urbanova, Bakk. iur.**, St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Theodora Urbanova, Bakk. iur.` (person)
- predicted in sentence: `Mag. Helga Hochrieser`, `Theodora Urbanova`

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_71`)

Im Rahmen der Firmengründung wurde von Herrn **Frikel** ein  Fahrzeug als sein Beitrag bzw. als Einlage eingebracht.

- missed: `Frikel` (person)
- predicted in sentence: —

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter[...] in der Verwaltungsstrafsache gegen  **Niklas Radschweit**, Kaiserfeld 4, 8673 Steinhöf, Österreich, wegen der Verwaltungsübertretungen gemäß § 16 Abs. 1 des  Wiener Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBI. für Wien Nr. 20, in der  Fassung des LGBI. Nr. 71/2018 in der Fassung des LGBl für Wien Nr. 50/2013 in Verbindung mit  § 1 Abs. 1 GAG und Tarifposten B 1 und B 8 über die Beschwerde der Beschuldigten vom  15.11.2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 -  Abgabenstrafen, vom 20.10.2020, Zahl: MA6/[...], zu Recht erkannt:  I.) Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z. 2 VStG eingestellt.   II.) Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

- missed: `Niklas Radschweit` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)

Herr **Harald Hilderink**  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)

Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau **Waiser** die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

- missed: `Waiser` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_42`)

Die im Firmenbuchregister am 27.06.2017 von Amts wegen gemäß § 30/2 UGB gelöschte KG,  FN 2i, war eine Gesellschaft im Geschäftszweig „Bewirtschaftung und Verwaltung von eigenen  Immobilien“ mit Komplementär O.W.1 und der Rechtsanwältin **Jakob BatheW.** als Kommanditistin.

- missed: `Jakob BatheW.` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_29`)

Aus dem Firmenbuchauszug der **OStR Serena Hammoudi**  geht hervor, dass die  Beschwerdeführerin vom 01.07.2009 bis tt.07.2019 Geschäftsführer der  OStR Serena Hammoudi  war und diese am tt.07.2019 gemäß § 40 FBG infolge von  Vermögenslosigkeit im Firmenbuch gelöscht wurde.

- missed: `OStR Serena Hammoudi` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)

12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr **Aldewereld** von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

- missed: `Aldewereld` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/147137.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147137.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache **RgR Shirley Ribler**, Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich, vertreten durch Dr. Christian Lind,  Am Ausblick 17, 3110 Neidling, über die Beschwerde vom 2. Jänner 2023 gegen die Bescheide  des Finanzamtes Österreich vom 1. Dezember 2022 betreffend Anspruchszinsen (§ 205 BAO)  2016, 2017 und 2018, Steuernummer 64-511/1773, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `RgR Shirley Ribler` (person)
- predicted in sentence: `Mag. Helga Hochrieser`, `Dr. Christian Lind`

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)

Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr **Alois Kleynsteuber** (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

- missed: `Alois Kleynsteuber` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/142680.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142680.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Hon.-Prof. Moritz Lindstaedt**  in der Beschwerdesache Samuel Rattai,  Hilzing 64, 2880 Kranichberg, Österreich, vertreten durch Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH, Lehargasse 3A Tür 14, 1060 Wien, über die Beschwerde vom  7. September 2023 gegen den Bescheid des Finanzamtes Österreich vom 30. August 2023  betreffend Zahlungserleichterungen gem. § 212 BAO, Steuernummer 30-750/1577, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Hon.-Prof. Moritz Lindstaedt` (person)
- predicted in sentence: `Samuel Rattai`, `Dr. Peter Wolf Wirtschaftsprüfungs-`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)

 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr **Harald Hilderink**  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/144450.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144450.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den **Mag. Priv.-Doz. Karl Schultenjohann**  über die Beschwerde der MittelPflege Entwicklung GmbH, Lirkgasse 23, 8412 Sukdull, Österreich, vertreten durch die SBF Steuerberatung OG, Wielandgasse 35, 8010  Graz, vom 12.03.2024 gegen den Bescheid des Finanzamtes Österreich vom 09.02.2024  betreffend Festsetzung eines ersten Säumniszuschlages zu Recht erkannt:  Die Bescheidbeschwerde wird als unbegründet abgewiesen.

- missed: `Mag. Priv.-Doz. Karl Schultenjohann` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/148407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148407.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  des **MedR Erna Noellgen**, Diesting 46, 4151 Salaberg, Österreich, über dessen Beschwerde vom 7. November 2021 gegen den  Bescheid des Finanzamtes Österreich vom 8. Oktober 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 01-405/3031, zu Recht erkannt:   I. Der angefochtene Bescheid wird im Umfang der Beschwerdevorentscheidung vom  16. Mai 2022 abgeändert.

- missed: `MedR Erna Noellgen` (person)
- predicted in sentence: `Mag. Andreas Stanek`

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_2`)

Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde der **Adriana Wottge**,  Ferstelgasse 22, 3282 Forsthub, Österreich, vom 20. Juli 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 14. Juli 2022, Zl. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 2 iVm § 4 Abs. 2 Wiener Parkometergesetz 2006, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Adriana Wottge` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)

Das Büro in **Univ.-Prof.in Miriam Ungruh**  war auch im Interesse meines Arbeitgebers.

- missed: `Univ.-Prof.in Miriam Ungruh` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_203`)

Oiltrade GmbH (Beilage 1)  o Auszug aus dem Gewerberegister (18.11.2013)  o Firmenbuchauszug (27.5.2013)  O Kopien der übergebenen Visitenkarten Hr. K., Hr. **M.**, Hr. X.  O Passkopie Hr. K.  O 1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.  O 3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel  Eingangstüre)  O Bescheid über die Erteilung der UlD -Nummer (31.7.2013)  O Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)  o Bescheid über die Registrierung als Empfänger für Mineralöl  O Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH (Beilage 2)  o Auszug Gewerberegister (4.9.2013)  o Firmenbuchauszug (4.9.2013)  O Angebot vom 26.9.2013  o Passkopie Hr. d.  O Rückstandsbescheinigungen Finanzamt (31 .10.2013,25.11 .2013, 6.12.2013)  Protokoll über Beschuldigteneinvernahme von bf. vom 1.3.2017 (Beilage 3)  2.

- missed: `M.` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Bodo Heumaier  in der Angelegenheit der Parteien  **KzlR HR Lothar Schoeberl**, PLZ1 Stadt1 (Beschwerdeführerin), und FA Braunau Ried Schärding  als Amtspartei über die  Beschwerde vom 25.8.2022   gegen den Bescheid des Finanzamtes vom 4.8.2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016   zu Recht erkannt:  Der bekämpfte Bescheid wird abgeändert.

- missed: `KzlR HR Lothar Schoeberl` (person)
- predicted in sentence: `Mag. Bodo Heumaier`

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch **Dr. Mag. Elmar Ebertz**  in der Beschwerdesache Karlheinz Abke,  Schindlauerweg 53, 2392 Dornbach, Österreich  vertreten durch MedR Anneliese Naupert, Bakk. art., über die Beschwerde vom 30. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 27. April 2022, mit dem das Stundungsansuchen  vom 29. März 2022 abgewiesen wurde, Steuernummer 69-865/2288, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Mag. Elmar Ebertz` (person)
- predicted in sentence: `Karlheinz Abke`

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_43`)

Nach dem vorliegenden gerichtlichen Beschluss ist **Dr. X** als Erwachsenenvertreter des Bf.  zur Vertretung vor Ämtern und Behörden zuständig.

- missed: `Dr. X` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)

Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr **Harald Hilderink**, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Hon.-Prof.in Rebecca Altemüller**  in der Beschwerdesache Theodor Strohmeier,  Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich  über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend Abweisung des Antrags vom 20.  März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme  einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Hon.-Prof.in Rebecca Altemüller` (person)
- predicted in sentence: `Theodor Strohmeier`

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  **Raimund Diedering, Bakk. iur.**, Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Raimund Diedering, Bakk. iur.` (person)
- predicted in sentence: `Raimund Diedering`

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_54`)

Dass der (Original)Ausweis gemäß § 29b StVO 1960 mit der Nr. Nr1 (Nr2) an Herrn Isenmann  geb.  Herrgeb, ausgestellt wurde und dass Herr **Ballschmieder** laut ZMR mit Datum verstorben ist, ergibt sich  aus dem Schreiben der Bezirkshauptmannschaft Ort vom 16. März 2023.

- missed: `Ballschmieder` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut-`, `Frauke Galleithner`

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)

Entscheidungsgründe  I. Verfahrensablauf:  1. Frau **Dagobert Duewel** (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

- missed: `Dagobert Duewel` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/139845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139845.1_6`)

Der Einkommensteuerbescheid erging am 01.09.2014 mit einer Gutschrift in Höhe von  431 Euro, wobei der vom Bf. begehrte Alleinerzieherabsetzbetrag für seine mit ihm im  gemeinsamen Haushalt lebenden Söhne HR Dipl. Kfm. Jörg Möllenkamp (geb. am 1. März 1986) und  **Dipl. Kfm. Quentin Wissmeyer** (geb. 1. März 1986) nicht berücksichtigt wurde.

- missed: `Dipl. Kfm. Quentin Wissmeyer` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_46`)

Der Beschwerdeführerin oblag daher als vertretungsberechtigtes Organ der  **OStR Serena Hammoudi**  die Erfüllung der abgabenrechtlichen Pflichten der  Gesellschaft.

- missed: `OStR Serena Hammoudi` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_79`)

Die Bf. brachte am 25. August 2021 folgenden Vorlageantrag ein:  „In der Beschwerdevorentscheidung vom 20.07.2021 wird unter Zugrundelegung des  Sachverständigengutachtens von **Dr. Dok1**, der Allgemeinmediziner ist, davon ausgegangen,  dass bei S. X. keine Behinderung vorliegt: Der Sachverständige kommt zum Schluss, dass „kein  Grad der Behinderung zu ermitteln" wäre.

- missed: `Dr. Dok1` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin **Mag. Katharina Moravec** zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

- missed: `Mag. Katharina Moravec` (person)
- predicted in sentence: `Fa Witago  Wirtschaftsprüfungs-`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Armin Treichl, den Richter Dr.  Roman Galehr sowie die fachkundigen Laienrichter Mag. Eva-Maria Düringer und Mag. Tino  Ricker in der Beschwerdesache Dirk Hironymus, Am See IV 25, 3071 Hinterholz, Österreich (vormals: RHO Pharma), vertreten  durch Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG, Alpstraße  23, 6890 Lustenau über die Beschwerde vom 05. Oktober 2016 gegen die Bescheide des  Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, Postfach 260, 1000 Wien) vom 12.  September 2016 betreffend Umsatzsteuer 2012, Bescheid über die Wiederaufnahme des  Verfahrens 2012 und vom 09. September 2016 betreffend Umsatzsteuer 2015 Steuernummer  63-114/3997  in Anwesenheit der Schriftführerin **Isabella Längle** zu Recht erkannt:     I. Die Beschwerde gegen die Wiederaufnahme des Verfahrens Umsatzsteuer 2012  wird als unbegründet abgewiesen.

- missed: `Isabella Längle` (person)
- predicted in sentence: `Dirk Hironymus`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_341`)

Auffallend ist in diesem Zusammenhang, dass am gleichen Tag (12.07.2013) bereits durch den  Allgemeinmediziner **Dr. W** Krill Kps und Bioflorin ärztlich verordnet wurden, jedoch kein Pure  EN Kps AI Enzymes.

- missed: `Dr. W` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)

6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn **Angelstein** angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

- missed: `Angelstein` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)

Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn **Isenmann**  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

- missed: `Isenmann` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_261`)

Konkret ist anzunehmen, dass auf den Baustellen der Bauträger über die Firma **M.** vermittelte  Arbeiter zum Einsatz kamen, deren Löhne zum Nettowert kalkuliert wurde.

- missed: `M.` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Gerald Bährensmann, Adr. zu Handen **Mag. Thomas Kollaczia-Putz**, Annagasse 3-3A,  1010 Wien über die Beschwerde vom 22. Oktober 2018 gegen die Bescheide des Finanzamtes  Gmunden Vöcklabruck vom 25. September 2018, Steuernummer 04-246/1421  betreffend  Körperschaftsteuer 2014, Körperschaftsteuer 2015, Körperschaftsteuer 2016, Umsatzsteuer  2014, Umsatzsteuer 2015 und Umsatzsteuer 2016 nach Durchführung einer mündlichen  Verhandlung am 9. Jänner 2025 in Beisein des Schriftführers Markus Blöchl LL.B. LL.M. zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Thomas Kollaczia-Putz` (person)
- predicted in sentence: `Mag. Johann Fischerlehner`, `Gerald Bährensmann`

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)

Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der **Jeremias Kierstan**, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

- missed: `Jeremias Kierstan` (person)
- predicted in sentence: `Herrn  Vertreter`

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_25`)

Mit 3. November 1972  verstarb der Bf. Mit Einantwortungsbeschluss des Bezirksgerichtes  Mattighofen vom 06.06.2023 wurde die Verlassenschaften den erblichen Kindern **Dimitri Seelos**  und Dipl.-Ing. Luna Goedecken, BEd MA  nach Abgabe einer unbedingten Erbserklärung eingeantwortet.

- missed: `Dimitri Seelos` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_43`)

Damit ist als Zwischenergebnis  bereits feststehend, dass das Engagement der **Tamara Gottschalch**  in Peru Betriebsstätten sowohl im  Sinne des § 29 BAO als auch im Sinne des Art 5 OECD-MA darstellen.

- missed: `Tamara Gottschalch` (person)
- predicted in sentence: —

</details>

---

