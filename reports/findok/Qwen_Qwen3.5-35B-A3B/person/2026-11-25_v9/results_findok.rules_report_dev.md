# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-11-25T20:28:52.193642

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-25_v9/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
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
| True Positives | 636 |
| False Positives | 425 |
| False Negatives | 1215 |
| Total Gold Entities | 1851 |
| Micro Precision | 59.9% |
| Micro Recall | 34.4% |
| Micro F1 | 43.7% |
| Macro F1 | 43.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `names_in_complaint_context_general` | 19.7% | 86.6% | 11.1% | 238 | 206 | 32 |
| `names_after_legal_roles_general` | 0.3% | 75.0% | 0.2% | 4 | 3 | 1 |
| `legal_titles_with_names` | 28.8% | 66.9% | 18.4% | 508 | 340 | 168 |
| `names_after_herrn_frau` | 8.5% | 52.8% | 4.6% | 163 | 86 | 77 |
| `names_after_bf_or_representative` | 0.1% | 0.7% | 0.1% | 135 | 1 | 134 |
| `names_in_address_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_after_legal_roles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `standalone_names_in_legal_context` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `names_in_complaint_context_general` 🏆

**F1:** 0.197 | **Precision:** 0.866 | **Recall:** 0.111  

**Format:** `regex`  
**Rule ID:** `d82b2f34`  
**Description:**
Matches names appearing after 'in der Beschwerdesache' (genitive case), handling full names including umlauts, titles, and initials like N.R. or JG.

**Content:**
```
(?:in der Beschwerdesache(?:\s+der)?)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s*,\s*(?:Bakk\.?\s+techn\.|LLM|PhD|BA|MA|Dipl|iur)\.?)?)|(?:in der Beschwerdesache(?:\s+der)?)\s+([A-Z]{2,}(?:\.[A-Z])?)|(?:in der Beschwerdesache(?:\s+der)?)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.866 | 0.111 | 0.197 | 238 | 206 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 206 | 32 | 1645 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-229/2263` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Höffert` | `Christine Höffert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adalbert Köseoglu` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

| Predicted | Gold |
|---|---|
| `Ali Jäckle` | `Ali Jäckle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


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

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


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

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


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

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/136405.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136405.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


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

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


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

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Valentin Joebges, LLM` | `Valentin Joebges, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Stephan` (person)
- `Bärngarten 17, 9713 Hochegg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `84-167/9727` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137281.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137281.1_1`)


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

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ludmilla Hühnerfuß, Bakk. techn.` | `Ludmilla Hühnerfuß, Bakk. techn.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dominika Juhass` (person)
- `Singham 20, 3465 Unterstockstall, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/137349.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137349.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Gebhard Kristupeit, Bakk. techn., Wörndlestraße 17, 9112 Untergrafenbach, Österreich, vertreten durch APP Steuerberatung GesmbH, Schenkenstraße  4, 1010 Wien, über die Beschwerde gegen die Bescheide des Finanzamtes Baden Mödling vom  31. Mai 2011 hinsichtlich Haftung betreffend Kapitalertragsteuer für 2007 und 2008,  Steuernummer 83-002/9356  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gebhard Kristupeit, Bakk. techn.` | `Gebhard Kristupeit, Bakk. techn.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Wörndlestraße 17, 9112 Untergrafenbach, Österreich` (address)
- `APP Steuerberatung GesmbH` (organisation)
- `Finanzamtes Baden Mödling` (organisation)
- `83-002/9356` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Anton Böckamp, Bakk. techn., Leopold Kunschak Gasse 25, 9343 Dielach, Österreich, über die Beschwerde vom 8. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Gänserndorf Mistelbach, § 323b BAO) vom  25. November 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 84-669/5568  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne des Beschwerdebegehrens  abgeändert.

| Predicted | Gold |
|---|---|
| `Anton Böckamp, Bakk. techn.` | `Anton Böckamp, Bakk. techn.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Leopold Kunschak Gasse 25, 9343 Dielach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Gänserndorf Mistelbach` (organisation)
- `84-669/5568` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/137518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marlies Seipold, Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich, über die Beschwerde vom 27. Jänner 2020 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 14. Jänner 2020 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum März 2017 bis September 2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Marlies Seipold` | `Marlies Seipold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.-Lorenz-Böhler-Gasse 19, 4204 Habruck, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jaden Grothmann` | `Jaden Grothmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Massimo Friedhoff` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/137573.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137573.1_1`)


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

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


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

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


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

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_1`)


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

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Rebecca Hüllhorst,  Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich, über die Beschwerde vom 8. Juli 2021 gegen den Abweisungsbescheid des  Finanzamtes Österreich vom 25. Juni 2021 betreffend Familienbeihilfe für das Kind To für den  Zeitraum Februar 2020 bis Februar 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rebecca Hüllhorst` | `Rebecca Hüllhorst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brunnwiesengasse 52, 8350 Hohenbrugg an der Raab, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


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

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Bianca Kristeller, Schröckbach 58, 9652 Nostra, Österreich, über die Beschwerde vom 9. Dezember 2021 gegen den Bescheid des Finanzamtes  Österreich vom 8. November 2021 betreffend Familienbeihilfe 10.2020-09.2021  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bianca Kristeller` | `Bianca Kristeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schröckbach 58, 9652 Nostra, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Mehmet Zappe, MA, Wiesel 24, 4632 Oberirrach, Österreich, vertreten durch Petzelbauer & Kleinhappel Rechtsanwälte, Rabensteig 8/3A, 1010  Wien, betreffend einen Antrag auf Fristsetzung gemäß Art. 133 Abs. 1 Z 2 iVm Abs. 7 B-VG vom  10. Oktober 2022 wegen Verletzung der Entscheidungspflicht, Steuernummer 51-912/4171  (SVNR 3727 040311), beschlossen:   Der Fristsetzungsantrag vom 10. Oktober 2022 betreffend die behauptete Säumigkeit des  Bundesfinanzgerichtes im Säumnisbeschwerdeverfahren gegen das Finanzamt Österreich  betreffend einen Antrag auf Familienbeihilfe für den Zeitraum März 2020 bis April 2021 wird  gemäß § 30a Abs. 1 VwGG iVm § 30a Abs. 8 erster Satz VwGG als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mehmet Zappe, MA` | `Mehmet Zappe, MA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wiesel 24, 4632 Oberirrach, Österreich` (address)
- `51-912/4171` (tax_number)
- `3727 040311` (social_security_number)
- `Bundesfinanzgerichtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/138353.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138353.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/138313.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138313.1_1`)


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

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_1`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Christine Gäbelt  in der Beschwerdesache Verena Piechura,  Nußöd 5, 2014 Breitenwaida, Österreich, über die Beschwerde vom 7. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Juni 2022, Ordnungsbegriff Nr1, betreffend die Rückforderung zu Unrecht  bezogener Beträge   1. an Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum Oktober 2021 bis        Juni 2022 für den Sohn B  2.

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Christine Gäbelt` (person)
- `Nußöd 5, 2014 Breitenwaida, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/138725.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138725.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. David Eckerlin  in der Beschwerdesache Margarete Wasmeir,  Voglstraße 19, 4902 Schlaugenham, Österreich, vertreten durch Mag. Kurt Caspari Steuerberatungs KG, Hirnreit 173, 5771  Leogang, über die Beschwerde vom 29. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 11. Juli 2022 betreffend Säumniszuschlag 2022 Steuernummer 09-312/4413  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Margarete Wasmeir` | `Margarete Wasmeir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. David Eckerlin` (person)
- `Voglstraße 19, 4902 Schlaugenham, Österreich` (address)
- `Mag. Kurt Caspari Steuerberatungs KG` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `09-312/4413` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Olaf Koechig, Zmöllach 3, 3542 Litschgraben, Österreich, Beschwerde vom 25. Oktober 2019 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr Finanzamtes Österreich, vom  28. November 2018 betreffend Umsatzsteuer 2012, Umsatzsteuer 2013, Umsatzsteuer 2014  und Umsatzsteuer 2015, Steuernummer 17-913/2665, der Gartfentri Heizung Institut GmbH, vertreten durch  Gustke Forschung GmbH, hinsichtlich des Vorlageantrages der Gartfentri Heizung Institut GmbH  in  Liquidation, beschlossen:  I. Die Beschwerdevorentscheidungen vom 6. April 2022 betreffend Umsatzsteuer 2012,  2013, 2014 und 2015 der Gartfentri Heizung Institut GmbH  in Liquidation werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Olaf Koechig` | `Olaf Koechig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Zmöllach 3, 3542 Litschgraben, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `17-913/2665` (tax_number)
- `Gartfentri Heizung Institut GmbH` (organisation)
- `Gustke Forschung GmbH` (organisation)
- `Gartfentri Heizung Institut GmbH` (organisation)
- `Gartfentri Heizung Institut GmbH` (organisation)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/138952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138952.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Paolo Blasenbreu, Ernst-Ludwig-Gasse 176, 7461 Allersgraben, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019, 64-737/5163, beschlossen:   Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Paolo Blasenbreu` | `Paolo Blasenbreu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Ernst-Ludwig-Gasse 176, 7461 Allersgraben, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)
- `64-737/5163` (tax_number)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Selma Katirci` | `Selma Katirci` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass` (person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich` (address)
- `Brehm & Sahinol Rechtsanwälte OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Muran Grönewald, Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte,  Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 19. Dezember 2019 gegen  die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich) vom  11. Dezember 2019 betreffend Wiederaufnahme § 303 BAO /  ESt 2013 sowie vom 12.12.2019  betreffend Wiederaufnahme § 303 / ESt 2014 und betreffend Wiederaufnahme § 303 / ESt  2015 zu Steuernummer 87-098/9833  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Muran Grönewald` | `Muran Grönewald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich` (address)
- `Pallauf Meißnitzer Staindl & Partner` (organisation)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `87-098/9833` (tax_number)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rebecca Altemüller  in der Beschwerdesache Theodor Strohmeier,  Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich  über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend Abweisung des Antrags vom 20.  März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme  einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Theodor Strohmeier` | `Theodor Strohmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Rebecca Altemüller` (person)
- `Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Laetitia Weckerlin  in der Beschwerdesache Zdenko Graucop,  Lisztpromenade 31, 9170 Zell-Oberwinkel, Österreich, über die Beschwerde vom 25. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 10. Mai 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020  Steuernummer 11-005/1241  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Zdenko Graucop` | `Zdenko Graucop` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Laetitia Weckerlin` (person)
- `Lisztpromenade 31, 9170 Zell-Oberwinkel, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `11-005/1241` (tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Dr. Mag. Elmar Ebertz  in der Beschwerdesache Karlheinz Abke,  Schindlauerweg 53, 2392 Dornbach, Österreich  vertreten durch MedR Anneliese Naupert, Bakk. art., über die Beschwerde vom 30. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 27. April 2022, mit dem das Stundungsansuchen  vom 29. März 2022 abgewiesen wurde, Steuernummer 69-865/2288, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karlheinz Abke` | `Karlheinz Abke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Mag. Elmar Ebertz` (person)
- `Schindlauerweg 53, 2392 Dornbach, Österreich` (address)
- `MedR Anneliese Naupert, Bakk. art.` (person)
- `Finanzamtes Österreich` (organisation)
- `69-865/2288` (tax_number)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/139872.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. in der Beschwerdesache Waldemar Kosiol,  Afinger Hauptstraße 4, 4870 Schneiderweg, Österreich, über die Beschwerde vom 10. Juli 2014 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 7. Juli 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012  Steuernummer 47-100/4541, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waldemar Kosiol` | `Waldemar Kosiol` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Afinger Hauptstraße 4, 4870 Schneiderweg, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)
- `47-100/4541` (tax_number)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/140391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Rebecca Klaprodt, Edt bei Heitzing 6, 4150 Gintersberg, Österreich, vertreten durch DOCUMENTA-Treuhand WP und Stb. GmbH,  Edisonstraße 2, 4600 Wels, über die Beschwerde vom 8. Jänner 2020 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 13. Dezember 2019 betreffend Einkommensteuer  2016 Steuernummer 17-096/4990  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rebecca Klaprodt` | `Rebecca Klaprodt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Susanne Haim` (person)
- `Edt bei Heitzing 6, 4150 Gintersberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `17-096/4990` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Saligergasse` — partial — pred is substring of gold: `Saligergasse 1, 3300 Haag Dorf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

**False Positives:**

- `Rene` — partial — pred is substring of gold: `Reneé Dreyssig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Reneé Dreyssig`(person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich`(address)
- `Mag. Manfred Frühwirth`(person)
- `Finanzamtes Linz`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Helge Göppele`(person)
- `GDJJ Versand`(organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich`(address)
- `Finanzamtes Graz`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `HR OSR Leonie Ercklentz`(person)
- `Karnitzen 135, 9635 Kronhof, Österreich`(address)
- `LKP Steuerberatung OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR. in der Beschwerdesache VetR Elias Voht, Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich, über die Beschwerde vom 23.12.2015 gegen  die  mit   19.11.2015  datierten  Bescheide des Finanzamtes Wien 1/23, betreffend Umsatzsteuer 2013, Körperschaftsteuer  2013, die gemäß den  Beschwerdevorentscheidungen vom 24.02.2016 als zurückgenommen  gilt, Steuernummer 09-XXX/XXX zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Elias Voht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Elias Voht`(person)
- `Bad Mitterndorf 29, 8211 Fünfing bei Gleisdorf, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130973.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130973.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Janosch von Winterfeldt, Freudenthalerstraße 34, 4171 Eckerstorf, Österreich, über die Beschwerde vom 25.11.2019 gegen den  Zurückweisungsbescheid des Finanzamtes Salzburg-Stadt vom 20.11.2019 (Wiederaufnahme  des Verfahrens betreffen Einkommensteuer 2015) zu Recht erkannt:  I. Die Beschwerdevorentscheidung vom 9.1.2020 wird gemäß § 279 Abs 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

**False Positives:**

- `Janosch` — partial — pred is substring of gold: `Janosch von Winterfeldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Janosch von Winterfeldt`(person)
- `Freudenthalerstraße 34, 4171 Eckerstorf, Österreich`(address)
- `Finanzamtes Salzburg-Stadt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Burkhard Krautschenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Joachim Annanias`(person)
- `VetR Burkhard Krautschenko`(person)
- `Geizersgraben 6, 2823 Leiding, Österreich`(address)
- `Mag. Susanne Pöltenstein-Rosenegger`(person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG`(organisation)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Zoltan Dabrowski`(person)
- `OMedR Prof. Hartmut Szardemings`(person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/135653.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Ibrahim de Vrese, LLB, Kitzlermühle 3, 2754 Wopfing, Österreich, über die Beschwerde vom 07.06.2021 wegen behaupteter  Verletzung der Entscheidungspflicht durch das Finanzamt Österreich betreffend Antrag auf  Familienbeihilfe ab 09/2019 Sozialversicherungsnummer 2872011080  beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Ibrahim` — partial — pred is substring of gold: `Ibrahim de Vrese, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Stephan`(person)
- `Ibrahim de Vrese, LLB`(person)
- `Kitzlermühle 3, 2754 Wopfing, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `2872011080`(social_security_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Schmalohr` — partial — pred is substring of gold: `Schmalohr + Kiekebusch Möbel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Dr.in Edith Lohhausen`(person)
- `Schmalohr + Kiekebusch Möbel`(organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich`(address)
- `Michael Haberl`(person)
- `Finanzamtes`(organisation)
- `Finanzamt Judenburg Liezen`(organisation)
- `71-763/1501`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137039.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137039.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Susanne Rohrauer  in der Beschwerdesache der  StadtHandel Planung, Sebastianplatz 18, 3441 Dietersdorf, Österreich  vertreten durch StB, über die Beschwerde vom 7. April 2021 gegen  den Bescheid des FA Salzburg-Stadt  vom 25. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Steuernummer 89-257/7642  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Stadt` — partial — pred is substring of gold: `StadtHandel Planung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Susanne Rohrauer`(person)
- `StadtHandel Planung`(organisation)
- `Sebastianplatz 18, 3441 Dietersdorf, Österreich`(address)
- `FA Salzburg-Stadt`(organisation)
- `89-257/7642`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Adolf Brehmer  in der Beschwerdesache VetR Gotthard Lohscheider,  Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich, vertreten durch „Meinrad Kisewetter“ - Steuerberatungsgesellschaft m.b.H., Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich,  über die Beschwerde vom 28.06.2021, gegen den Bescheid des Finanzamtes Österreich vom  27.05.2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm § 111 BAO, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Gotthard Lohscheider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Adolf Brehmer`(person)
- `VetR Gotthard Lohscheider`(person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich`(address)
- `Meinrad Kisewetter`(person)
- `Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137857.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137857.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Univ.-Prof. Aron Nierenberger  in der Beschwerdesache DDr.in VetR Rosemarie Srama,  Hollgasse 53, 3244 Riegers, Österreich, gegen die Bescheide des Finanzamtes Österreich vom 10. Februar 2020  betreffend Einkommensteuer 2014 bis 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Univ.-Prof. Aron Nierenberger`(person)
- `DDr.in VetR Rosemarie Srama`(person)
- `Hollgasse 53, 3244 Riegers, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/139554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139554.1_2`)


Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Reneé Stienen, Gmundnerberg 16, 4203 Oberwinkl, Österreich, vertreten durch Schmidt & Schmidt KG, Bahnzeile 10, 2130 Mistelbach, über die  Beschwerde vom 5. März 2019 gegen den Bescheid des Finanzamtes Gänserndorf Mistelbach  vom 30. Jänner 2019 betreffend Einkommensteuer 2017, Steuernummer 25-901/2438, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `Reneé Stienen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Reneé Stienen`(person)
- `Gmundnerberg 16, 4203 Oberwinkl, Österreich`(address)
- `Schmidt & Schmidt KG`(organisation)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `25-901/2438`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/141080.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141080.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Abigail Dausener  in der Beschwerdesache HR OSR Samir Fatthauer,  Viehdorferstraße 27, 4192 Steinschild, Österreich, über die Beschwerde vom 16. Februar 2023 gegen die Bescheide des FA Wien 2/20/21/22  vom 11. Jänner 2023 betreffend Abweisung von Anträgen auf Wiederaufnahme der Verfahren  hinsichtlich Umsatz- und Einkommensteuer 2016 zu Recht erkannt:   I.)

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Abigail Dausener`(person)
- `HR OSR Samir Fatthauer`(person)
- `Viehdorferstraße 27, 4192 Steinschild, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait  in der Beschwerdesache   Prof. Ing. Eduard Skroblies, Forchetweg 18, 4692 Albertsham, Österreich,   über die Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf (nunmehr Finanzamt Österreich) vom 10. November 2014 betreffend  Körperschaftsteuer 2011, vom 19. November 2014 betreffend Körperschaftsteuer 2012 und  2013 sowie die Beschwerde vom 12. Juli 2016 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 7. Juli 2016 betreffend Körperschaftsteuer 2014   I. beschlossen:  Der Vorlageantrag betreffend Körperschaftsteuer 2011 wird zurückgewiesen.

**False Positives:**

- `Prof` — similar text (different position): `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`(person)
- `Prof. Ing. Eduard Skroblies`(person)
- `Forchetweg 18, 4692 Albertsham, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OStR Cassandra Schmedtje`(person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich`(address)
- `Helga Kraus`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/141990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141990.1_2`)


Das Bundesfinanzgericht hat durch die Senatsvorsitzende R1, den RichterR2, sowie die  fachkundigen Laienrichter R3 und R4, in der Beschwerdesache VetR Maja Waatsack, Sarottla 115, 8522 Sulzhof, Österreich,  vertreten durch Mag. Wolfgang Schranz, Mahlerstraße 11 Tür 4, 1010 Wien, über die  Beschwerde vom 28. Oktober 2016 gegen die Bescheide des Finanzamtes Wien 8/16/17 vom  25. Juli 2016 betreffend Umsatzsteuer sowie Feststellung der Einkünfte gemäß § 188 BAO für  2009, sowie vom 24. August 2016 betreffend Umsatzsteuer und Feststellung der Einkünfte  gemäß § 188 BAO für die Jahre 2010 bis 2015, Steuernummer 31-345/4688, in der Sitzung  vom 30. August 2023 nach Durchführung einer mündlichen Verhandlung am 30. August 2023 in  Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Vet` — partial — pred is substring of gold: `VetR Maja Waatsack`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Maja Waatsack`(person)
- `Sarottla 115, 8522 Sulzhof, Österreich`(address)
- `Mag. Wolfgang Schranz`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `31-345/4688`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache KzlR Techn R RgR Wigand Beinhorn, Salfeldstraße 54, 9500 Oberwollanig, Österreich, vertreten durch Dr. Robert Austaller, Wildshut 16, 5120 St. Pantaleon, über die  Beschwerde vom 3. März 2021 gegen den Bescheid des Finanzamtes Österreich vom  11. Februar 2021 betreffend Rechtsgebühr, Steuernummer 98-325/7724,  Erfassungsnummer 10-2021, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Kzl` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Techn R RgR Wigand Beinhorn`(person)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `Dr. Robert Austaller`(person)
- `Finanzamtes Österreich`(organisation)
- `98-325/7724`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Geraldine Matuschefski  in der Beschwerdesache der Demircan Metall AG&  atypisch stille Gesellschaft, vertreten durch xx Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen  1.

**False Positives:**

- `Demircan Metall` — partial — pred is substring of gold: `Demircan Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Geraldine Matuschefski`(person)
- `Demircan Metall AG`(organisation)
- `xx Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/143791.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143791.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Erhard Gruetter  in der Beschwerdesache René Kleser,  Dauerkleingärten 17M, 5112 Gresenberg, Österreich, vertreten durch Mag. Andreas Schnegg, Kalkofenstraße 24, 6425 Haiming, über  die Beschwerde vom 19. Februar 2022 gegen den Bescheid des FA Wien 8/16/17  vom 21. Jänner 2022  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016, Steuernummer  85-777/9690, zu Recht erkannt:  I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Ren` — partial — pred is substring of gold: `René Kleser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Erhard Gruetter`(person)
- `René Kleser`(person)
- `Dauerkleingärten 17M, 5112 Gresenberg, Österreich`(address)
- `Mag. Andreas Schnegg`(person)
- `FA Wien 8/16/17`(organisation)
- `85-777/9690`(tax_number)

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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/146422.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Elmira Walkenbach  in der Beschwerdesache der  JLFT Robotik, Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich, über die am 8.August 2023 eingebrachte Beschwerde gegen den  zur Steuernummer 38-455/9315  ergangenen Bescheid des FA Innsbruck  vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Elmira Walkenbach`(person)
- `JLFT Robotik`(organisation)
- `Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich`(address)
- `38-455/9315`(tax_number)
- `FA Innsbruck`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/147347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147347.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/147552.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147552.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Jörg Novakowski  in der Beschwerdesache OSR Samantha Schaffroth,  Kaltenbach 71, 3353 Biberbach, Österreich, über die Beschwerde vom 16. September 2020 gegen den Bescheid des  FA Niederösterreich Mitte  vom 21. August 2022, mit welchen der Antrag auf Wiederaufnahme der Verfahren  betreffend Einkommensteuer für die Jahr 2015 bis 2017 gem. § 303 BAO abgewiesen wurde, zu  Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Jörg Novakowski`(person)
- `OSR Samantha Schaffroth`(person)
- `Kaltenbach 71, 3353 Biberbach, Österreich`(address)
- `FA Niederösterreich Mitte`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/149152.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149152.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/149745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149745.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  HR Manuela Buskotte, Schulboden 10, 8742 Kienberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2017 und 2018, 18-878/6086, zu Recht erkannt:   1.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `HR Manuela Buskotte`(person)
- `Schulboden 10, 8742 Kienberg, Österreich`(address)
- `Mag. Ghesla Steuerberater GmbH`(organisation)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `18-878/6086`(tax_number)

</details>

---

## `names_after_legal_roles_general` 

**F1:** 0.003 | **Precision:** 0.750 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `3894d40c`  
**Description:**
Matches names appearing after specific legal roles like 'durch den Richter', excluding the role itself and handling full names with umlauts.

**Content:**
```
(?:durch den Richter|durch die Richterin)\s+(?!Mag\.?)(?!Dr\.)(?!Priv\.-Doz)(?!Univ\.-Prof)(?!Hon\.-Prof)(?!Techn R)(?!OMedR)(?!KommR)(?!RgR)(?!StR)(?!OStR)(?!HR)(?!Dipl\.-Ing\.?)([A-Z][a-zäöüß]{2,}(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.002 | 0.003 | 4 | 3 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 1 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/143846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Rüdiger Tormählen  in der Beschwerdesache  Melina Weingartz, KLG Aus eigener Kraft 31, 3830 Vestenpoppen, Österreich, über die Beschwerde vom 20. Oktober 2023 gegen den Bescheid  des Finanzamtes Österreich vom 14. September 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 77-866/9586  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rüdiger Tormählen` | `Rüdiger Tormählen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melina Weingartz` (person)
- `KLG Aus eigener Kraft 31, 3830 Vestenpoppen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `77-866/9586` (tax_number)

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

## `legal_titles_with_names` 🏆

**F1:** 0.288 | **Precision:** 0.669 | **Recall:** 0.184  

**Format:** `regex`  
**Rule ID:** `be4682b2`  
**Description:**
Matches person entities with complex German legal/academic titles, allowing multiple consecutive titles and handling titles ending in 'in' or 'Dr.' followed by single-letter names or initials.

**Content:**
```
(?:Mag\.?\s+Mag\.?|OMedR|KommR|RgR|PhD|LL\.M\.?|B\.A\.?|B\.B\.A\.?|MedR|OSR|Techn R|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Dr\.(?:in)?(?:\s+Dr\.(?:in)?)?|StR|OStR|HR|Ri(?:n)?|Dipl\.-Ing\.?|Ing\.?|Prof\.ÖkR|M\.?B\.L\.?|Dipl\.\s+Kfm\.?|Dipl\.\s+Kff\.?)(?:\s+(?:Mag\.?\s+Mag\.?|OMedR|KommR|RgR|PhD|LL\.M\.?|B\.A\.?|B\.B\.A\.?|MedR|OSR|Techn R|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Dr\.(?:in)?(?:\s+Dr\.(?:in)?)?|StR|OStR|HR|Ri(?:n)?|Dipl\.-Ing\.?|Ing\.?|Prof\.ÖkR|M\.?B\.L\.?|Dipl\.\s+Kfm\.?|Dipl\.\s+Kff\.?)?)?\s+[A-Z][a-zäöüß]+(?:\s+(?:ten|van)?[A-Z][a-zäöüß]+)*(?:\s*,\s*(?:Bakk|LLM|PhD|BA|MA|Dipl|iur)\.?\s*(?:iur|phil)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.669 | 0.184 | 0.288 | 508 | 340 | 168 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 340 | 168 | 1511 |

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

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Mag. Michael Franz` (person)
- `Mag. Franz Josef Großin` (person)
- `Finanzamtes Baden Mödling` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_20`)


Seite 3 von 15 Erst anlässlich der mit Bericht vom 27.12.2010 abgeschlossenen Betriebsprüfung wurde die Ungewissheit, ob Liebhaberei im Zusammenhang mit der Vermietung des Objektes in Univ.-Prof.in Miriam Ungruh  vorliegt, beseitigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_69`)


Die ersten Monate bis zur Erlangung der Aufenthalts- und Arbeitsbewilligung für Russland und bis mein Büro bei AG Russland und meine Dienstwohnung bezugsbereit waren, habe ich ausschließlich von Univ.-Prof.in Miriam Ungruh  aus gearbeitet.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_74`)


Sie haben mit mir in Univ.-Prof.in Miriam Ungruh  deren Strategie und Marktauftritt in Russland besprochen (z.B. DivFirmen DivFirmen uvm.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_75`)


o Ich habe russische Kunden, die Wien besuchten, von Univ.-Prof.in Miriam Ungruh  aus betreut;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_76`)


sie nach Univ.-Prof.in Miriam Ungruh  zu Besprechungen und Workshops eingeladen (z.B. DivFirmen DivFirmen; uvm.) o In allen Fällen war ausschlaggebend, dass ich in Univ.-Prof.in Miriam Ungruh (Österreich) für „Westler“ leichter erreichbar war, ohne dass die Leute ein Visum besorgen und den teuren Aufenthalt in Moskau bezahlen mussten, um mich zu sehen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_81`)


o Um mir diese Arbeit in Univ.-Prof.in Miriam Ungruh  und in Österreich zu erleichtern, teilte mir AG zwei Dienstwägen zu: einen in Univ.-Prof.in Miriam Ungruh  und einen in Moskau. In Russland war ich ebenfalls rund um die Uhr im Einsatz: 14 Büros, 14 direkt berichtende Manager, 1200 Mitarbeiter, eine Forschungsstätte, eine PC Fabrik und diverse zusätzliche Infrastruktur wie Service Center, 2000 Partner Firmen, Partnerschaften mit über 100 Universitäten und über 2 Millionen Kunden im Jahr müssen eben betreut werden.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)


Das Büro in Univ.-Prof.in Miriam Ungruh  war auch im Interesse meines Arbeitgebers.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Sascha Hilcker` | `Ing. Sascha Hilcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich` (address)
- `Finanzamtes Wien  3/6/7/11/15` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Shoshana Leuther` | `Univ.-Prof.in Shoshana Leuther` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Seywald` (person)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


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

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rosamunde Galanidis` | `Priv.-Doz.in Rosamunde Galanidis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` | `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` | `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` |

**Missed by this rule (FN):**

- `SeeAutomotive AG` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Agneter` (person)
- `Mag. Belinda  Maria Eder` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Mag. Katharina Moravec` (person)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thassilo Schoenrock, LLM` | `Hon.-Prof. Thassilo Schoenrock, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Hochscharten 126D, 5122 Dorfen, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `06-88-920/2630` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Rauscher` | `Dr. Michael Rauscher` |
| `Dr. Christian Haid` | `Dr. Christian Haid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Franz Glashüttner` (person)
- `Mag. Bruno  Sundl` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

| Predicted | Gold |
|---|---|
| `Ing. StR Samuel Fraesdorff` | `Ing. StR Samuel Fraesdorff` |

**Missed by this rule (FN):**

- `Leroy Kusznierz` (person)
- `Maximilian Jasper` (person)
- `Gustav Nowak` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |
| `OMedR Ottfried Theißl` | `OMedR Ottfried Theißl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


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

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


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

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


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

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dr.in Bianca Gerasimczuk` | `Priv.-Doz.in Dr.in Bianca Gerasimczuk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raimund Diedering, Bakk. iur.` (person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich` (address)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `StR Univ.-Prof. Alvin Paulikat` | `StR Univ.-Prof. Alvin Paulikat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich` (address)
- `Dr Christian Burghardt` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_25`)


Nach dem vorliegenden Beschluss des Bezirksgerichtes Innere Stadt vom 26.11.2010 wurde der  Rechtsanwalt Dr. Burghardt zum Sachwalter gemäß § 268 Abs. 3 Z 2 ABGB bestellt. Der  Sachwalter wurde u.a. für das Aufgabengebiet zur Vertretung vor Ämter und Behörden  bestellt. Die Sachwalterbestellung wirkt insofern konstitutiv, als ab ihrer Wirksamkeit die  Prozess- und Handlungsfähigkeit im dort umschriebenen Ausmaß für den Bf. keinesfalls mehr  gegeben war (VwGH 27.2.2006, 2004/05/0326).

| Predicted | Gold |
|---|---|
| `Dr. Burghardt` | `Dr. Burghardt` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Elvira Thielsen` | `Hon.-Prof.in Elvira Thielsen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |
| `Ing. Edith Schifferdecker` | `Ing. Edith Schifferdecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


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

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

| Predicted | Gold |
|---|---|
| `Dr.in Ing. Viktoria Weigart` | `Dr.in Ing. Viktoria Weigart` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |
| `StR Milena Neidig` | `StR Milena Neidig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


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

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Laurence Vasylenko  in der Beschwerdesache X, Adresse,  über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Umgebung  vom 13. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 02-410/2351  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hon.-Prof.in Laurence Vasylenko` | `Dr.in Hon.-Prof.in Laurence Vasylenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes Graz` (organisation)
- `02-410/2351` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


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

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


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

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


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

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_162`)


Geschäftsführer dieser GmbH sind der zweite Stratege und Ing. Michael FG2 (beide jedenfalls  seit 1.1.2008-heute).

| Predicted | Gold |
|---|---|
| `Ing. Michael` | `Ing. Michael` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_167`)


Geschäftsführer dieser GmbH waren der erste Stratege (jedenfalls 1.1.2008 –12.2021) und Ing.  Eduard FG4 (jedenfalls seit 1.1.2008-heute).

| Predicted | Gold |
|---|---|
| `Ing.  Eduard` | `Ing.  Eduard` |

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

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Schippan  in der Beschwerdesache Judith Kapelle,  Saßbergweg 17, 4860 Haid, Österreich, betreffend Beschwerde vom 2. September 2012 gegen den Bescheid des FA  Waldviertel vom 3. August 2012 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 Steuernummer 31-042/8347  beschlossen:     Der Vorlageantrag vom 30.11.2012 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Petra Schippan` | `Priv.-Doz.in Petra Schippan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Judith Kapelle` (person)
- `Saßbergweg 17, 4860 Haid, Österreich` (address)
- `FA  Waldviertel` (organisation)
- `31-042/8347` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Maurice Bettenhäuser` | `Hon.-Prof. Maurice Bettenhäuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miranda Weissert` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Nancy Stuckenschneider` | `Priv.-Doz.in Nancy Stuckenschneider` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Bruno Karahasan` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `12-630/0045` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


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

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


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

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Vanessa Nowikoff  in der Beschwerdesache des  KommR Lee Ponsard, Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich, über die Beschwerde vom 30. Juli 2020 gegen den Bescheid des  Finanzamtes X. (FA, jetzt Dienststelle des Finanzamt Freistadt Rohrbach Urfahr ) vom 10. Juli 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zur Steuernummer 63-102/2061  zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 (1) BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Vanessa Nowikoff` | `Hon.-Prof.in Vanessa Nowikoff` |
| `KommR Lee Ponsard` | `KommR Lee Ponsard` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `63-102/2061` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache MedR Gertrude Hartges,  Hübing 15, 9535 Farrendorf, Österreich, über die Beschwerde vom 10. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `MedR Gertrude Hartges` | `MedR Gertrude Hartges` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hübing 15, 9535 Farrendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


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

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


BESCHLUSS   Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Frederike Lipienski  in der Beschwerdesache des  Hademar Rüstow, Eck 124T, 2214 Auersthal, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des  FA Amstetten Melk Scheibbs (FA) vom 10. März 2021 über die Abweisung eines Antrages auf Wiederaufnahme §  303 BAO /  ESt 2017 zur Steuernummer 71-651/2158  beschlossen:   Der Vorlageantrag vom 29.Sept.2021 wird gemäß § 260 Abs. 1 lit. a iVm § 264 Abs. 4 lit e und  Abs. 5 BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frederike Lipienski` | `Hon.-Prof.in Frederike Lipienski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hademar Rüstow` (person)
- `Eck 124T, 2214 Auersthal, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `71-651/2158` (tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


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

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_22`)


Insolvenzverwalter ist Dr. Stephan Riel.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Riel` | `Dr. Stephan Riel` |

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Christian Lemanowitz` | `Univ.-Prof. Christian Lemanowitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dietmar Kachelmuss` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pjotr Astore` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Fassmer` (person)
- `Tillisweg 11, 8773 Sparsbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Sheila Nonnmacher` | `Dr.in Sheila Nonnmacher` |
| `Dr. Silvia Gredenberg` | `Dr. Silvia Gredenberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Semertzidou` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `76-265/6028` (tax_number)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr.in Linn Wolek` | `Dr.in Linn Wolek` |
| `MedR Uwe Vaculik` | `MedR Uwe Vaculik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_3`)


Begründung  1.a. Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 11. März  2021, Zahl: MA67/216700111216/2021, wurde Frau MedR Uwe Vaculik (in weiterer Folge:   Beschwerdeführerin) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung 2006 für schuldig erkannt und über sie nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer   Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `MedR Uwe Vaculik` | `MedR Uwe Vaculik` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Natascha Gassner` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Vincent Kohlstruk` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Dr. Hedwig Bavenek` — partial — pred is substring of gold: `Mag.Dr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.DDr. Hedwig Bavenek-Weber in der  Beschwerdesache Merlin Feucht, Alte Straße 2, 8114 Unterfriesach, Österreich, über die Beschwerde vom 12. Dezember 2011  gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14.  November 2011, Steuernummer 57-396/6782, betreffend die Festsetzung der ermäßigten  Glücksspielabgabe gemäß § 58 Abs. 3 GSpG für Glücksspiele im Rahmen von Gewinnspielen  (Preisausschreiben), zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hedwig Bavenek` — partial — pred is substring of gold: `Mag.DDr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.DDr. Hedwig Bavenek-Weber`(person)
- `Merlin Feucht`(person)
- `Alte Straße 2, 8114 Unterfriesach, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `57-396/6782`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Ada Schaeferlein` — partial — pred is substring of gold: `Mag.a Univ.-Prof.in Ada Schaeferlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein`(person)
- `Leroy Sitterle`(person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich`(address)
- `Astoria Stb GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_162`)


Verwaltungsverfahrensrechtes DDr.  Walter, DDr. Maier, Seite 131).

**False Positives:**

- `Dr.  Walter` — partial — pred is substring of gold: `DDr.  Walter,`
- `Dr. Maier` — partial — pred is substring of gold: `DDr. Maier`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `DDr.  Walter,`(person)
- `DDr. Maier`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Dr. Thomas Keppert Steuerberatung` — positional overlap with gold: `Prof. Dr. Thomas Keppert`

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

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

**False Positives:**

- `Dr. Nikolaus` — partial — pred is substring of gold: `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Titus Ohlmer`(person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich`(address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `20-234/9874`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132247.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132247.1_11`)


Fristgerecht wurde bekanntgegeben, dass das Fahrzeug zur Beanstandungszeit PhD Wilhelm Reschke, MBA,  Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich (= Beschwerdeführer, kurz: Bf.) überlassen war.

**False Positives:**

- `PhD Wilhelm Reschke` — partial — pred is substring of gold: `PhD Wilhelm Reschke, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Wilhelm Reschke, MBA`(person)
- `Hirschenschlag 2T, 2232 Deutsch-Wagram, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Dr. Adam Müller` — partial — pred is substring of gold: `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Timon Thoennißen`(person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_35`)


Von einer ursprünglich geplanten Streichung der in den Rechnungen der Möbel Zorkelglanz GmbH  ausgewiesenen Vorsteuern wurde unter Hinweis auf Rz. 1825 UStR Abstand genommen.

**False Positives:**

- `StR Abstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

**False Positives:**

- `Dr.in Ing. Viktoria Weigart  Adr` — partial — gold is substring of pred: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Dr.in Ing. Viktoria Weigart  Dieses Unternehmen` — partial — gold is substring of pred: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)


Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der Dr.in Ing. Viktoria Weigart  Somit traf ihn die Auskunftspflicht.

**False Positives:**

- `Dr.in Ing. Viktoria Weigart  Somit` — partial — gold is substring of pred: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Lieselotte Reinicker`(person)
- `Raingasse 32, 9552 Ossiachberg, Österreich`(address)
- `Dr. X`(person)
- `Finanzamtes`(organisation)
- `FA Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dipl. Kfm. Ing. Ing` — partial — pred is substring of gold: `Dipl. Kfm. Ing. Ing. Jonas Thumberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger`(person)
- `Paullehnerweg 72, 9584 Höfling, Österreich`(address)
- `UNICONSULT Steuerberatungs GmbH & Co KG`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_206`)


(UStR Rz 794; Ruppe/Achatz, UStG 5, § 6, TZ 249/6).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_210`)


Im ersteren  Fall müsste der Land- und Forstwirt, der den Grundstücksumsatz als steuerpflichtig behandeln  möchte, zunächst nach § 22 Abs. 6 für Regelbesteuerung optieren (UStR Rz 794).

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lee Kubbig`(person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_146`)


An der EnnsTouristik Consulting GmbH waren im Streitzeitraum beteiligt:  28.000…..HGesellschaft BFK Baugesellschaft mbH & Co KG  (jedenf. 1.1.08-27.9.11)  25.900…..BFK Holding GmbH ab 28.9.2011  3.500……..Dr. Christian W1 (1.1.2008-31.7.2011)  3.500……..Dr. Christian W2 (1.1.2008-31.7.2011)  7.000..……zweiter Stratege ( jedenfalls ab 1.8.2011-27.9.2011)  10 von 38 Seite 11 von 38

**False Positives:**

- `Dr. Christian` — no gold match — likely missing annotation
- `Dr. Christian` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `EnnsTouristik Consulting GmbH`(organisation)
- `BFK Baugesellschaft mbH & Co KG`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_161`)


An der Traver-Planung GmbH waren beteiligt:    26.600 €…Holding (jedenf. 1.1.2008-12.4.2010)  25.900 €… Holding (13.4.2010-8.2.2015)  26.600 €….Holding (9.2.2015-10.9.2019)  8.400 €……Ing. Michael FG2 (jedenfalls. 1.1.2008-12.4.2010)  9.100 €……Ing. Michael FG2 (13.4.2010-8.2.2015)  8.400 €……Ing. Michael FG2 9.2.2015  35.000 €….Summe

**False Positives:**

- `Ing. Michael` — no gold match — likely missing annotation
- `Ing. Michael` — no gold match — likely missing annotation
- `Ing. Michael` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Traver-Planung GmbH`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_166`)


8.400 €……Ing. Eduard FG4 (jedenf. 1.1.2008-12.4.2010)  9.100 €……Ing. Eduard FG4 (13.4.2010-25.1.2015)  8.400 €……Ing. Eduard FG4 (ab 26.1.2015)  35.000 € …Summe

**False Positives:**

- `Ing. Eduard` — no gold match — likely missing annotation
- `Ing. Eduard` — no gold match — likely missing annotation
- `Ing. Eduard` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_145`)


Ein Gespräch mit Hern OA Dr.  Bieber bezüglich des weiteren psychotherapeutischen Procedere wurde vor der Entlassung  durchgeführt.“

**False Positives:**

- `Dr.  Bieber` — partial — pred is substring of gold: `OA Dr.  Bieber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OA Dr.  Bieber`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_12`)


Mit Verweis  auf die KStR Rz 1536 (Beispiel 3), ist die Steuerbelastung für das Jahr 2014 einmal mit  Sanierungsgewinn (SG) und einmal ohne Sanierungsgewinn zu berechnen.

**False Positives:**

- `StR Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Karina` — partial — pred is substring of gold: `Univ.-Prof.in Karina von Wnuck-Lipinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Karina von Wnuck-Lipinski`(person)
- `Rosemarie Fortwängler`(person)
- `Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `FA Österreich`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

**False Positives:**

- `Dr. Mehes` — partial — pred is substring of gold: `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Mag. Natascha Gassner`(person)
- `Mag. Renate Burtscher`(person)
- `Bernd Feldkircher`(person)
- `Vincent Kohlstruk`(person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich`(address)
- `Bischof-Fuchs Steuerberatungs GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ludger Endel`(person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-868/1042`(tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Jeanne Stockhorst`(person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `22-242/2984`(tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


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

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi über die am 25. Mai 2022 eingebrachte  Beschwerde von Elvira Akcakaya, Dr. Ludwig-Straße 12, 4184 Neuling, Österreich, Firmenbuchnummer FN gegen die an  Beschuldigte gerichtete Vollstreckungsverfügung des Magistrates der Stadt Wien (MA 6 – BA  32) vom 18. Mai 2022, Zahl MA67/Zahl/2021, beschlossen:  Gemäß § 50 in Verbindung mit (iVm) § 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  die Beschwerde als unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Ludwig` — partial — pred is substring of gold: `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elvira Akcakaya`(person)
- `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_14`)


Vergl. hierzu “Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Dr. Franz Leidenmühler` — partial — pred is substring of gold: `Prof. Dr. Franz Leidenmühler`
- `Dr. Heidi Pacher` — partial — pred is substring of gold: `MR Dr. Heidi Pacher`
- `Dr. Juliane Bogner Strauß` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_16`)


Anmerkung:   Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem  “Rechtsgutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben  für das BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang Mazal Wien, den 20. Februar  2017”.

**False Positives:**

- `Univ.-Prof. Dr. Wolfgang Mazal Wien` — partial — gold is substring of pred: `Univ.-Prof. Dr. Wolfgang Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang Mazal`(person)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Josef Schlager  Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`

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

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_41`)


Die  Ladung zur Verhandlung, adressiert an Dr. Karl RA1, mit der Adresse in NÖ wurde von der Post  nicht als verzogen, sondern als unbekannt zurückgestellt. Ein RA Dr. Karl RA1 in NÖ brachte die  Beschwerden zur ersten und zweiten Zwangsstrafe ein (8.2.2019 und 28.5.2019).

**False Positives:**

- `Dr. Karl` — similar text (different position): `Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl`(person)
- `RA Dr. Karl`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_42`)


Ein RA Dr.  Carl RA1 mit identer Adresse in NÖ und identer Handynummer brachte hingegen für die Bf. die  Vorlageanträge (1.4.2019 und 16.8.2019) ein.

**False Positives:**

- `Dr.  Carl` — partial — pred is substring of gold: `RA Dr.  Carl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr.  Carl`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_43`)


Sowohl RA Dr. Carl RA1 als auch RA Dr. Karl RA1  verweisen in ihren Eingaben auf die jeweils nach § 8 RAO erteilte Vollmacht (ohne  Einschränkungen).

**False Positives:**

- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`
- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Carl`(person)
- `RA Dr. Karl`(person)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_45`)


Im Internet scheint sowohl ein RA Dr. Karl RA1 als auch ein RA Dr. Carl RA1  mit der Adresse „AdresseKurz“ in Wien auf.

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`
- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)
- `RA Dr. Carl`(person)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_195`)


Mit Schreiben des RA Dr. Karl RA1 in NÖ vom 23. Dezember 2018 an das FA wurde von der Bf.  in Briefform bekannt gegeben, dass der wirtschaftlicher Eigentümer der Bf. „Dr. Karl RA1“ ist.

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)
- `Dr. Karl`(person)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_233`)


Solchen Parteienvertretern und allfälligen hilfeleistenden Ansprechpersonen (wie im  BMF/Registerbehörde) müssen aber seitens der Bf. korrekte Auskünfte über wahrscheinliche  Datenprobleme bei Einträgen geben werden, wie den unterschiedlichen Erfassungen und  Schreibweisen der Vornamen Karl und Carl, unter denen u.a. Eingaben an das FA getätigt  wurden (vgl. angeführte Beschwerdeschriften und Vorlageanträge der Bf., abwechselnd  eingebracht durch RA Dr. Karl RA1 und RA Dr. Carl RA1, u.a. mit identer Adresse in NÖ, identer  Handynummer im Briefkopf, identen Bankverbindungen und identer Kurzparaphe) oder  13 von 16 Seite 14 von 16

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`
- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `BMF/Registerbehörde`(organisation)
- `RA Dr. Karl`(person)
- `RA Dr. Carl`(person)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_235`)


Auch im Internet  scheint sowohl ein RA Dr. Karl RA1 als auch ein RA Dr. Carl RA1 mit identen Adresse an der  Adresse der Bf. auf (AdresseKurz).

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`
- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)
- `RA Dr. Carl`(person)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_252`)


RA Dr. Karl RA1 (Personenidentität: Berufsmäßiger Parteienvertreter der Bf., Geschäftsführer  der Bf. und wirtschaftlicher Eigentümer der Bf.) verwies in der Beschwerdeschrift (mit damalig  angegebener Adresse in NÖ, Adresse nicht mehr aktuell laut Bekanntgabe in mündlicher  Verhandlung) auf die nach § 8 RAO erteilte Vollmacht (ohne ersichtliche Einschränkungen).

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_4`)


Dr. Dok1, Fachgebiet Allgemeinmedizin, erstellte nach Untersuchung von S. am 2. März 2021  folgendes Gutachten:  Anamnese:  Schwangerschaft und Geburt unauffällig  TE und Paukenröhrchen;

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_40`)


S. wurde am 1. Juli 2021 von Dr.in Dok3 untersucht und folgendes Gutachten erstellt:  Anamnese:  Siehe auch Vorgutachten vom 2.3.2021  Es wurde kein Grad der Behinderung ermittelt. Da zwar gutachterliche Diagnosen gestellt  wurden, jedoch mangels an Anspruchnahme adäquater Therapien eine für die Beurteilung  alltags relevante anhaltende Einschränkung erforderliche ärztliche Verlaufsdokumentation  nicht vorhanden ist.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_79`)


Die Bf. brachte am 25. August 2021 folgenden Vorlageantrag ein:  „In der Beschwerdevorentscheidung vom 20.07.2021 wird unter Zugrundelegung des  Sachverständigengutachtens von Dr. Dok1, der Allgemeinmediziner ist, davon ausgegangen,  dass bei S. X. keine Behinderung vorliegt: Der Sachverständige kommt zum Schluss, dass „kein  Grad der Behinderung zu ermitteln" wäre.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_85`)


Entgegen der Schlussfolgerung im Sachverständigengutachten von Dr. Dok1 ist der Umstand,  dass keine Therapien und keine ärztliche Verlaufsdokumentation vorgelegt wurden, nicht  geeignet darauf zu schließen, dass keine Behinderung vorliegt!

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_91`)


Entgegen den Ausführungen im Sachverständigengutachten von Dr. Dok1 haben sehr wohl  Therapien stattgefunden.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_92`)


Es wird auch darauf hingewiesen, dass die diagnostizierte Erkrankung  einen Dauer- bzw. Endzustand darstellt und daher das Ergebnis des  Sachverständigengutachtens von Dr. Dok1, dass die Diagnose nicht vorliege und auch kein Grad  der Behinderung gegeben wäre, in einem diametralen Widerspruch (den es im Ermitt- lungsverfahren aufzuklären gilt) zur klinisch fachspezifischen Diagnose steht.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_93`)


Dr.in Dok3, Fachgebiet: Ärztin für Allgemein-medizin, erstellte am 31. Jänner 2022 folgendes  Aktengutachten:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Mag. W. klinische und Gesundheitspsychologin allgemein beeidigte und gerichtlich zertifizierte  Sachverständige klinisch psychologisches Privatgutachten vom 5.10.2021  Es liegt eine Asperger-Autismus-Störung vor, die zum Teil widersprüchlichen Ergebnisse,  insbesondere die Selbstbeurteilung des Mj sowie einige seiner Leistungstestergebnisse, welche  deutlich besser ausgefallen sind als es bei einer Person mit Asperger-Autismus zu erwarten  gewesen wäre, lässt sich dahingehend klären, dass der Mj wahrscheinlich auch mitbedingt  durch seine hohe Intelligenz-sich über Jahre hinweg sehr vielen sozialen Kompetenzen kognitiv  erschlossen hat und somit auf heuristischer Basis agieren kann sofern er das vorliegende soziale  Muster schnell und unbeeinträchtigt von Störvariablen erkennt.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_109`)


Im Gutachten vom 2. März 2021 stellte Dr. Dok1, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_111`)


Im Gutachten vom 1. Juli 2021 stellte Dr.in Dok3 ebenfalls keinen Grad der Behinderung fest.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_112`)


Im Aktengutachten vom 31. Jänner 2022 wurde das (inzwischen vorgelegte) Privatgutachten  von MMag. W., MSc, vom 5. Oktober 2021 berücksichtigt und von Dr.in Dok3 die Erkrankung  von S. unter die Pos.Nr. 03.04.01 der Einschätzungsverordnung mit einem Gesamtgrad der  Behinderung von 30 vH rückwirkend ab Oktober 2021 eingereiht.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_167`)


Erst im Vorschulalter fallen Schwierigkeiten auf (u. a.  Kontaktprobleme, wiederkehrende Verhaltensmuster, Missachten von Regeln beim Spielen  etc.) (https://focus-arztsuche.de/magazin/krankheiten/psychische-erkrankungen/was-ist-das- asperger-syndrom-und-wie-erkennt-man-es )  Im Gutachten vom 2. März 2021 stellte Dr. Dok1, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest, dies mit der Begründung, dass zwar gutachterliche Diagnosen gestellt  worden seien, jedoch mangels Inanspruchnahme adäquater Therapien, eine, für die  Beurteilung alltagsrelevanter, anhaltender Einschränkungen erforder-liche, ärztliche  Verlaufsdokumentation, nicht vorhanden sei.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_168`)


Im Gutachten vom 1. Juli 2021 stellte Dr.in Dok3 erneut keinen Grad der Behinderung fest, dies  mit der Begründung, dass keine aktuellen Befunde beigebracht worden seien.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_170`)


Bei der Erstellung des Aktengutachtens vom 31. Jänner 2022 lag der Sachverständigen Dr.in  Dok3 das Privatgutachten von MMag. W., MSc, vom 5. Oktober 2021 vor.

**False Positives:**

- `Dr.in  Dok` — partial — pred is substring of gold: `Dr.in  Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in  Dok3`(person)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_179`)


Unter Einbeziehung der von MMag. W., MSc, in ihrem Gutachten getroffenen Diagnose reihte  Dr.in Dok3X.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3X`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3X`(person)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)


Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Dr. Franz Leidenmühler` — partial — pred is substring of gold: `Prof. Dr. Franz Leidenmühler`
- `Dr. Heidi Pacher` — partial — pred is substring of gold: `MR Dr. Heidi Pacher`
- `Dr. Juliane Bogner Strauß` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_16`)


Anmerkung:   Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem  “Rechtsgutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben  für das BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang  Mazal Wien, den 20. Februar  2017”.

**False Positives:**

- `Univ.-Prof. Dr. Wolfgang  Mazal Wien` — partial — gold is substring of pred: `Univ.-Prof. Dr. Wolfgang  Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang  Mazal`(person)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/138307.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138307.1_3`)


Begründung  Im Fristsetzungsantrag vom 10. Oktober 2022 wird als Sachverhalt Folgendes vorgebracht:   Mit Antrag vom 14.06.2021 beantragte die Beschwerdeführerin die Auszahlung von  Familienbeihilfe für ihr Kind OMedR Amanda Ratzmer, MSc  VNR 4982 010771  für den Zeitraum  März 2020 - April 2021.

**False Positives:**

- `OMedR Amanda Ratzmer` — partial — pred is substring of gold: `OMedR Amanda Ratzmer, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Amanda Ratzmer, MSc`(person)
- `4982 010771`(social_security_number)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Günter Salahi  in der Beschwerdesache Jaden Knauss,  Dossenweg 3, 4132 Atzesberg, Österreich  über die Beschwerde vom 8. Jänner 2021 gegen den Bescheid des Finanzamtes  Österreich vom 3. Dezember 2020 Rückzahlung gemäß § 239 BAO, Steuernummer  15-678/4603  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Günter Salahi` — partial — pred is substring of gold: `Mag. Hon.-Prof. Günter Salahi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Günter Salahi`(person)
- `Jaden Knauss`(person)
- `Dossenweg 3, 4132 Atzesberg, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `15-678/4603`(tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/138662.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138662.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Maurice Kämpfel, Leuzendorfgasse 8, 5660 Eschenau, Österreich, betreffend Beschwerden vom 9. März 2022  gegen die Bescheide des Finanzamtes Österreich vom 21. Oktober 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 und Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 93-599/8471  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Maurice Kämpfel`(person)
- `Leuzendorfgasse 8, 5660 Eschenau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `93-599/8471`(tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/138996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138996.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 6. Dezember 2012 des Beschwerdeführers DDr.in Pamela Gempp, Bosruckgasse 2, 3121 Heitzing, Österreich  Steuernummer:  82-457/9791, gegen den Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt  Österreich) vom 21. November 2012 betreffend Festsetzung der Kraftfahrzeugsteuer für die  Monate 03/2011 bis 09/2012 zu Recht:    I)  Der Beschwerde wird gem. § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Pamela Gempp` — partial — pred is substring of gold: `DDr.in Pamela Gempp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `DDr.in Pamela Gempp`(person)
- `Bosruckgasse 2, 3121 Heitzing, Österreich`(address)
- `82-457/9791`(tax_number)
- `Finanzamtes`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_89`)


Die Tochter der Bf wurde im Zuge des Antragsverfahrens am 8. Juli 2020 im Sozialministerium- service von Dr.in Dok1, Ärztin für Allgemeinmedizin, begutachtet und folgendes Gutachten  erstellt:  "Anamnese:   Asperger Syndrom, F40.2. Spezifische Phobie  Derzeitige Beschwerden:   Laut Auskunft der Mutter: Vor einem Jahr ist meine Dok2 darauf gekommen, dass sie eventuell  ein Asperger Syndrom haben könnte.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_138`)


M. wurde auf Grund der Beschwerde am 6. November 2021 ein weiteres Mal untersucht und  von Dr. Dok2 folgendes Gutachten erstellt:  "Anamnese:  letzte Begutachtung 7-2020 mit 30% wegen Asperger Syndrom  Nun Einspruch da sich ihr Zustand verschlechtert hätte  Schwangerschaft und Geburt unauffällig, nach der Geburt Unruhe und weinen aufgefallen, sie  hätte viel geweint.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `Dr. Dok2`(person)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_215`)


M. ist ledig und lebt in einem eigenen Haushalt.  Im Zuge des Antrags- und Beschwerdeverfahrens wurden seitens des Sozialministeriumservice  zwei Gutachten erstellt.  Im Gutachten vom 8. Juli 2020 stellte Dr.in Dok1, Ärztin für Allgemeinmedizin, die Diagnose  Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 der  Einschätzungsverordnung mit einem Grad der Behinderung von 30 vH. rückwirkend ab  November 2019 (= Austestung).

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `Dr.in Dok1`(person)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_219`)


Im Gutachten vom 6. November 2020 stellte Dr. Dok2, Arzt für Allgemeinmedizin, ebenfalls die  Diagnose Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 mit einem  Grad der Behinderung von 30 vH.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_220`)


Dr. Dok2 wählte, wie schon Dr. Dok1, 2 Stufen über dem unteren Rahmensatz, da eine mäßige  Einschränkung der sozialen Fähigkeiten und die Absolvierung eines Studiums möglich sei.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`
- `Dr. Dok` — similar text (different position): `Dr. Dok2`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)
- `Dr. Dok1`(person)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_279`)


Dr.in Dok1, Ärztin für Allgemeinmedizin, lag bei der Erstellung des Gutachtens vom 8. Juli 2020  der Psychologische Kurz-Befund der X Privatuniversität aus 2019 vor.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_280`)


Dr.in Dok1 reihte die Erkrankung unter die Pos.Nr. 03.04.01 der Einschätzungsverordnung mit  einem Grad der Behinderung von 30 vH.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_282`)


Dem mit dem zweiten Gutachten betrauten Sachverständigen, Dr. Dok2, Arzt für Allge- meinmedizin, lagen bei der Erstellung seines Gutachtens vom 6. November 2020 folgende  Befunde bzw. Unterlagen vor:  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_289`)


akustische Differen- zierungsschwäche  Dr. Dok2 reihte die Erkrankung, übereinstimmend mit Dr. Dok1, unter die Pos.Nr. 03.04.01 mit  einem Grad der Behinderung von 30 vH. und bescheinigte ebenfalls keine Erwerbsunfähigkeit,  dies mit der Begründung, dass keine zweifelsfrei dokumentierte Gesundheitsschädigung  vorliege, die die dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, zur Folge  habe.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`
- `Dr. Dok` — similar text (different position): `Dr. Dok2`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)
- `Dr. Dok1`(person)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Mag` — partial — pred is substring of gold: `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`
- `Univ.-Prof.in Konstanze Lukass` — partial — pred is substring of gold: `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`(person)
- `Selma Katirci`(person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich`(address)
- `Brehm & Sahinol Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Zlatan Tegtmeier  in der Angelegenheit der Parteien  Dipl. Kfm. VetR Gerhard Stranz (Beschwerdeführerin), vertreten durch die   Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H., 9400 Wolfsberg  und Finanzamt Oststeiermark, 1000 Wien, PF 251  als  Amtspartei über die Beschwerden vom 12.

**False Positives:**

- `Dipl. Kfm. Vet` — partial — pred is substring of gold: `Dipl. Kfm. VetR Gerhard Stranz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Zlatan Tegtmeier`(person)
- `Dipl. Kfm. VetR Gerhard Stranz`(person)
- `Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamt Oststeiermark`(organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Dr. Mag. Elmar Ebertz  in der Beschwerdesache Karlheinz Abke,  Schindlauerweg 53, 2392 Dornbach, Österreich  vertreten durch MedR Anneliese Naupert, Bakk. art., über die Beschwerde vom 30. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 27. April 2022, mit dem das Stundungsansuchen  vom 29. März 2022 abgewiesen wurde, Steuernummer 69-865/2288, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. Elmar Ebertz`
- `MedR Anneliese Naupert, Bakk. ` — partial — pred is substring of gold: `MedR Anneliese Naupert, Bakk. art.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mag. Elmar Ebertz`(person)
- `Karlheinz Abke`(person)
- `Schindlauerweg 53, 2392 Dornbach, Österreich`(address)
- `MedR Anneliese Naupert, Bakk. art.`(person)
- `Finanzamtes Österreich`(organisation)
- `69-865/2288`(tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/139621.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139621.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Silvana Hellfritz, Reibersweg 24, 8144 Unterpremstätten, Österreich, betreffend Beschwerde vom 31. Jänner 2021  gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 69-424/6198  beschlossen:   Der Vorlageantrag wird gemäß § 264 Abs 4 lit e Bundesabgabenordnung (BAO) in Verbindung  mit § 260 Abs 1 lit b BAO als verspätet zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Silvana Hellfritz`(person)
- `Reibersweg 24, 8144 Unterpremstätten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `69-424/6198`(tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


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

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Friedhelm Sutor, Taggergasse 3, 3873 Thaures, Österreich, vertreten durch LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32, 4040 Linz, über die Beschwerde  vom 12. Jänner 2021 gegen den Bescheid des Finanzamtes für Großbetriebe vom  16. Dezember 2020 betreffend Normverbrauchsabgabe 06.2015-12.2019 Steuernummer  11-766/4596  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Friedhelm Sutor`(person)
- `Taggergasse 3, 3873 Thaures, Österreich`(address)
- `LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `11-766/4596`(tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_1`)


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

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/140529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140529.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Li Megerlein, Tungassingerstraße 18, 5061 Gfalls, Österreich, über die Beschwerde vom 5. April 2019 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 4. April 2019, Steuernummer  89-939/3728, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Li Megerlein`(person)
- `Tungassingerstraße 18, 5061 Gfalls, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `89-939/3728`(tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_34`)


dazu wurde der betreffende E-Mail- Verkehr mit dem SMS sowie die Stellungnahme des Univ.-Prof. Dr. F, Klinik Ort2, v. 23.3.2022  vorgelegt.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Dr. F`(person)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/141080.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141080.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Abigail Dausener  in der Beschwerdesache HR OSR Samir Fatthauer,  Viehdorferstraße 27, 4192 Steinschild, Österreich, über die Beschwerde vom 16. Februar 2023 gegen die Bescheide des FA Wien 2/20/21/22  vom 11. Jänner 2023 betreffend Abweisung von Anträgen auf Wiederaufnahme der Verfahren  hinsichtlich Umsatz- und Einkommensteuer 2016 zu Recht erkannt:   I.)

**False Positives:**

- `Hon.-Prof.in Mag` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Abigail Dausener`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Abigail Dausener`(person)
- `HR OSR Samir Fatthauer`(person)
- `Viehdorferstraße 27, 4192 Steinschild, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


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

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/141269.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141269.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Miriam Stauffenberg, Armensündergraben 17, 4776 Mayberg, Österreich, über die Beschwerde vom 17. März 2023 gegen  den Bescheid des Finanzamtes Österreich vom 16. März 2023, Steuernummer  78-665/1920, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zu Recht:   I. Der angefochtene Bescheid wird im Sinne der Beschwerdevorentscheidung vom  2. Mai 2023 abgeändert.

**False Positives:**

- `Dr. Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Miriam Stauffenberg`(person)
- `Armensündergraben 17, 4776 Mayberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `78-665/1920`(tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/141414.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141414.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Dr.in Mag.a Elisabeth Wiedenhöfft, LLM, Hirschberg 29, 2870 Guggendorf, Österreich, über die Beschwerde vom 11. November 2021 gegen den Bescheid  des Finanzamtes Österreich vom 5. Oktober 2021 betreffend Antrag auf Bewilligung der  Aussetzung § 212a BAO 2021, Steuernummer 16-471/8115  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Mag` — partial — pred is substring of gold: `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`(person)
- `Hirschberg 29, 2870 Guggendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `16-471/8115`(tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


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

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Ing. Mag` — partial — pred is substring of gold: `Ing. Mag. Hamza Ovacin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Saphira Schnaak`(person)
- `Kürschner Allee 44, 9300 Mail, Österreich`(address)
- `Ing. Mag. Hamza Ovacin`(person)
- `Finanzamtes Österreich`(organisation)
- `50-980/9446`(tax_number)

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache KzlR Techn R RgR Wigand Beinhorn, Salfeldstraße 54, 9500 Oberwollanig, Österreich, vertreten durch Dr. Robert Austaller, Wildshut 16, 5120 St. Pantaleon, über die  Beschwerde vom 3. März 2021 gegen den Bescheid des Finanzamtes Österreich vom  11. Februar 2021 betreffend Rechtsgebühr, Steuernummer 98-325/7724,  Erfassungsnummer 10-2021, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Techn R RgR Wigand Beinhorn`(person)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `Dr. Robert Austaller`(person)
- `Finanzamtes Österreich`(organisation)
- `98-325/7724`(tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_5`)


Aufgrund des Gesetzes waren die erblasserische Witwe M zu 1/3 und die mj. Töchter S, J, L und  KzlR Techn R RgR Wigand Beinhorn (die Beschwerdeführerin, kurz: Bf) zu je 1/6 des Nachlasses als Erben berufen und  haben eine bedingte Erbserklärung abgegeben.

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Techn R RgR Wigand Beinhorn`(person)

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_24`)


……………………“  Beschwerde  Innerhalb offener Frist wurde in einem einheitlichen Schriftsatz Beschwerde gegen die an die  erblichen Töchter ergangenen Gebührenbescheide erhoben und dies wie folgt begründet:  “Mit rechtskräftigem Einantwortungsbeschluss vom 17.3.2016, ……, wurde der Nachlass nach  dem am 10. September 1972 .2015 verstorbenen, zuletzt in Salfeldstraße 54, 9500 Oberwollanig, Österreich  wohnhaft gewesenen  Industriemechaniker, Herrn FM, den aufgrund des Gesetzes bedingt erbantrittserklärten Erben,  der erbl. Witwe M, geb. …., zu einem Drittel und den erbl. Töchtern, mj. S, geb. ….., mj. J, geb.  ……., mj. L, geb. ……., und mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……., zu je einem Sechstel eingeantwortet.

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `10. September 1972`(date)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `KzlR Techn R RgR Wigand Beinhorn`(person)

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_26`)


In dem vor dem Gerichtskommissär Dr. Robert AUSTALLER, öffentlicher Notar in St. Pantaleon,  vor Einantwortung des Nachlasses abgeschlossenen Erbübereinkommen vom 29.1.2016 haben  die Miterbinnen vereinbart, dass:  a) die erbl.

**False Positives:**

- `Dr. Robert` — partial — pred is substring of gold: `Dr. Robert AUSTALLER`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Robert AUSTALLER`(person)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_28`)


Liegenschaft EZ-1 der KG-X  - Bezirksgericht A - mit dem einzigen Grundstück 1061/1 Baufläche (Gebäude), Gärten per 800  m2 samt dem darauf errichteten Wohnhaus Salfeldstraße 54, 9500 Oberwollanig, Österreich  mit einem gerichtlich festgestellten  Schätzwert von EUR 395.000,00 in ihr Alleineigentum übernimmt:  b) die erbl. Töchter mj. S, geb……., mj. J, geb. ……, mj. L, geb. ……., und mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……  die Liegenschaft EZ-2 der KG-X - Bezirksgericht A - mit dem einzigen Grundstück 1061/7  Baufläche (Gebäude), Gärten per 1.051 m2 samt dem darauf errichteten Garagengebäude S- Straße, mit einem gerichtlich festgestellten Schätzwert von EUR 85.000,00 in ihr gleichteiliges  Miteigentum übernehmen;

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht A`(organisation)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `KzlR Techn R RgR Wigand Beinhorn`(person)
- `Bezirksgericht A`(organisation)

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_31`)


Witwe M zum Wertausgleich aus den unterschiedlichen Verkehrswerten der  übernommenen Liegenschaften an die erbl. Töchter mj. S, geb. ……, mj. J, geb. ……., mj. L, geb.  ……., und mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……., jeweils den baren Erbteilsergänzungsbetrag von  wertgesichert EUR 61.870,00 zu bezahlen hat, wobei die Auszahlungsverpflichtung bis zur  Volljährigkeit der vorgenannten erbl. mj.

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Techn R RgR Wigand Beinhorn`(person)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_39`)


Witwe M für den Erwerb der Liegenschaft EZ-1 der KG-X unter Zugrundelegung des  dreifachen Einheitswertes von EUR 90.600,00 zu Steuernummer ….. eine Grunderwerbsteuer in  Höhe von EUR 1.812,00;  b) den erbl. Töchter mj. S, geb. ……, mj. J, geb. ……, mj. L, geb. ……, und mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……,  für den gleichteiligen Erwerb der Liegenschaft EZ-2 der KG-X unter Zugrundelegung des  dreifachen anteiligen Einheitswertes von EUR 6.075,00 zu Steuernummern ……, ……., ……. und  98-325/7724  eine Grunderwerbsteuer in Höhe von jeweils EURO 121,50; vorgeschrieben.

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Techn R RgR Wigand Beinhorn`(person)
- `98-325/7724`(tax_number)

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_93`)


Da im  gegenständlichen Falle der erbl. Witwe M, geb. ….., die sofortige Bezahlung dieser  Erbteilsergänzungsbeträge an ihre Töchter, mj. S, geb. ……, mj. J, geb. ……, mj. L, geb. ……, und  mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……., aufgrund ihrer finanziellen Situation nicht möglich ist und auch in  nächster Zukunft nicht möglich sein wird, ist die pfandrechtliche Sicherstellung der  Erbteilsergänzungsforderungen eine unabdingbare Notwendigkeit.

**False Positives:**

- `Techn R RgR Wigand Beinhorn` — partial — pred is substring of gold: `KzlR Techn R RgR Wigand Beinhorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Techn R RgR Wigand Beinhorn`(person)

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_17`)


Die Bf. legte im Zuge der Beschwerde folgende Unterlagen vor:  Schreiben von Mag. Dr.in Carina B., Psychotherapeutin:  T. befindet sich seit 12. April 2022 auf Grund ihrer psychischen Erkrankung in einer  regelmäßigen ambulanten Psychotherapie bei ihr.

**False Positives:**

- `Dr.in Carina` — partial — pred is substring of gold: `Mag. Dr.in Carina B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Dr.in Carina B.`(person)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/142648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Dora Woditzka  in der Beschwerdesache Bettina Wütherich,  Außerwald 11Y, 6791 Gortipohl, Österreich, über die Beschwerden vom 5. September 2022 gegen die Bescheide des  Finanzamtes Österreich vom 29. August 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 und 2021 Steuernummer 64-696/3269  zu Recht erkannt:   I. Den Beschwerden wird - im Umfang der Beschwerdevorentscheidungen vom 03.02.2023 -  teilweise Folge gegeben.

**False Positives:**

- `Hon.-Prof.in Mag` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Dora Woditzka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Dora Woditzka`(person)
- `Bettina Wütherich`(person)
- `Außerwald 11Y, 6791 Gortipohl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `64-696/3269`(tax_number)

</details>

---

## `names_after_herrn_frau` 🏆

**F1:** 0.085 | **Precision:** 0.528 | **Recall:** 0.046  

**Format:** `regex`  
**Rule ID:** `b17715c5`  
**Description:**
Matches person names preceded by 'Herrn' or 'Frau', explicitly handling initials like N.R., JG, and full names with titles.

**Content:**
```
(?:Herrn|Frau)\s+([A-Z]{2,}(?:\.[A-Z])?|([A-Z][a-z]+(?:\s+(?:ten|van|von|zu|der|die|das)?[A-Z][a-z]+)*))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.528 | 0.046 | 0.085 | 163 | 86 | 77 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 86 | 77 | 1765 |

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

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_98`)


Z1 wurde laut der vorgelegten Protokollsabschrift am 11.6.2018 an der Polizeiinspektion  d_Ort_1 vernommen und gab unter anderem an: „Seit Mitte dem Jahr 2016 bin ich als  Steuerberater für …Herrn Volchert tätig.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_71`)


Im Rahmen der Firmengründung wurde von Herrn Frikel ein  Fahrzeug als sein Beitrag bzw. als Einlage eingebracht.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_73`)


Dieses Kfz wurde von Herrn Frikel selber angeschafft, wo und zu welchen  Bedingungen kann ich nicht angeben.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_75`)


Ich selber war dann in der Folge mehrmals in Österreich bei Herrn Frikel  wenn ich  mit dem Flugzeug anreiste, konnte ich dann den Audi verwenden (so ca. 15 mal pro Jahr) und  damit Kundenbesuche etc. erledigen.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_80`)


Die Bilanz für 2010 ist noch nicht  erstellt. In Deutschland an meinem Wohnsitz bzw. am Firmensitz konnte ich somit nicht  permanent über das KFZ Audi A6 verfügen, es befand sich des öfteren im Besitz des Herrn Frikel in  A/Adr1 und somit an diesem Standort.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_37`)


1) Mit Schreiben vom 13.05.2020 wurde von Herrn Angelstein mitgeteilt, dass er weder  Geschäftsführer der Firma sei noch mit dem Fahrzeug gefahren sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_38`)


Mit Schreiben vom 02.06.2020 wurde durch die Rechtsanwälte des Herrn Angelstein mitgeteilt, dass  dieser keine Lenkerauskunft erteilen könne, da er lediglich für das Fahrzeug mit dem amtlichen  Kennzeichen Auto3 (Anmerkung BFG: nicht gegenständlich) verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_50`)


Mit Schreiben vom 04.06.2020 teilte die rechtsfreundliche Vertretung des Herrn Angelstein  mit, dass der Genannte über das gegenständliche Fahrzeug zum Beanstandungszeitpunkt nicht  verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_51`)


Mit Schreiben vom 18.06.2020 wurde die Zulassungsbesitzerin des gegenständlichen  Fahrzeuges aufgefordert die erteilte Lenkerauskunft durch Vorlage entsprechender  Beweismittel (Unterlagen über die Bestellung des Herrn Angelstein als verantwortlicher Beauftragter  gemäß § 9 Abs. 2 Verwaltungsstrafgesetz 1991) glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_57`)


In der E-Mail Ihres rechtsfreundlichen Vertreters vom 01.10.2020 wurde zum gegenständlich  angelasteten Sachverhalt vorgebracht, die Zulassungsbesitzerin und deren handelsrechtliches  Organ habe der Aufforderung der Behörde zur Lenkerauskunft gesetzestreu entsprochen, zumal  dargelegt worden sei, dass die verlangte Auskunft von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030  Wien, als Verantwortlicher gemäß § 9 VStG erteilt werden könne.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_60`)


Weiters  wurde die Herbeischaffung des Aktes der WKStA zur AZ: AktWKStA, dessen Inhalt die  Übertragung der Meldepflicht gemäß § 9 VStG auf Herrn Angelstein beweisen soll, beantragt.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)
- `Dr.in Ing. Viktoria Weigart` (person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_154`)


In Beantwortung der nunmehr an Herrn Angelstein gerichteten (sechs) Lenkererhebungen der  belangten Behörde bestritt dieser seine Auskunftspflicht mit den Worten   1) bis 5) „dass ich weder ein Geschäftsführer dieser Firma noch mit diesem Fahrzeug gefahren  bin.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)


6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn Angelstein angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_174`)


3. Zulässigkeit des Einspruches:  …  4. Gründe des Einspruches:  Der Vorwurf, der Einschreiter hätte als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin der Firma1 des Fahrzeuges mit dem behördlichen Kennzeichen Auto4  [Anmerkung BFG: nicht gegenständlich] dem ordnungsgemäß zugestellten Verlangen der MA  67 vom 28.01.2020, innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er  dieses Fahrzeug überlassen gehabt hat, sodass dieser zur in der Strafverfügung angegebenen  Tatzeit und Tatort gelenkt hat bzw. vor diesem Zeitpunkt abgestellt hat nicht entsprochen zu  haben und somit die Rechtsvorschriften des § 103 Abs 2 KFG [Anmerkung BFG, gemeint: § 2  (Wiener) Parkometerabgabeverordnung iVm § 4 Abs. 2 Parkometergesetz 2006] trifft nicht zu,  dies aus folgenden Gründen: Es wurde - wie oben erwähnt - vom Einschreiter die Übertragung  der Meldepflicht auf Herrn Angelstein  geb. Herrgeb, übertragen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_191`)


Darin hat die Einschreiterin  und deren handelsrechtliches Organ dargelegt, dass die verlangte Auskunft nicht erteilt werden  kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030 Wien als Verantwortlichen gemäß  § 9 VStG.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_213`)


Darin hat die Einschreiterin und deren handelsrechtliches Organ dargelegt, dass die verlangte  Auskunft nicht erteilt werden kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, als  Verantwortlichen gemäß § 9 VStG.  16 von 22 Seite 17 von 22

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_24`)


Frau Baues ist die Liquidatorin.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Borisowa` | `Borisowa` |
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_405`)


Frau Baues als Vertreterin der Beschwerdeführerin gibt bekannt, dass die Diesellieferungen 2 bis 3  Mal pro Woche stattgefunden haben.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_424`)


Ein Naheverhältnis zwischen Herrn Inn Trikraftglanz und den gegenständlichen  Lieferanten hat es nicht gegeben.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `M.` (person)
- `Finanzamt` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |
| `Baues` | `Baues` |
| `Borisowa` | `Borisowa` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_6`)


Entscheidungsgründe  I. Verfahrensgang  1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Beschwerdeführerin (kurz Bf) ist eine GmbH, deren alleinige Gesellschafterin Frau Schneppensiefen ist.

| Predicted | Gold |
|---|---|
| `Schneppensiefen` | `Schneppensiefen` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_83`)


Am 03.10.2012 wurde dieses Fahrzeug auf eine Frau JH mit dem Kennzeichen K3  zugelassen.

| Predicted | Gold |
|---|---|
| `JH` | `JH` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_122`)


Am  03.10.2012 wurde dieses Fahrzeug auf eine Frau JH mit dem Kennzeichen K3 zugelassen.

| Predicted | Gold |
|---|---|
| `JH` | `JH` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/136657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136657.1_124`)


Noch  dazu wurde das von GL angegebene Kennzeichen erst am 03.10.2012 für Frau JH vergeben.

| Predicted | Gold |
|---|---|
| `JH` | `JH` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_11`)


Unter Bezugnahme auf obige Ausführungen ist festzuhalten, dass Frau Waiser die  exklusive (einzige) Adressatin der Vollstreckungsverfügung vom 18. Mai 2022 ist, die hier aber  von jemandem anderen bekämpft wird.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_15`)


Im vorliegenden Fall hat jedoch nicht die Adressatin der verfahrensgegenständlichen  Vollstreckungsverfügung, nämlich Frau Waiser  sondern FirmaBfInhaberLautFirmenbuch,  Firmenbuchnummer FN im eigenen Namen Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung – direkt oder indirekt – von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt - von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_37`)


Im  Allgemeinen gibt Frau Reifgerste an, dass sich ihre Tochter überwiegend „falsch“ fühle und in sozialen  Situationen sich sehr verunsichert fühle, da sie nicht wisse wie sie sich verhalten solle.

| Predicted | Gold |
|---|---|
| `Reifgerste` | `Reifgerste` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/139889.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139889.1_97`)


Aus den getroffenen Feststellungen, wonach der BF und seine geschiedene Gattin Frau MT je  zur Hälfte Eigentümer der in P, BF-P, gelegenen Liegenschaft mit dem darauf befindlichen  Wohnhaus sind und das p. Bezirksgericht im Scheidungsurteil bestimmt hat, dass die  geschiedene Gattin MT berechtigt ist, nur die Räume im Erdgeschoß des Hauses zu nutzen und  der BF berechtigt ist, den ersten Stock des Hauses zu nutzen, ergibt sich weiters, dass ein  Verkauf des Hauses aufgrund der Eigentumsverhältnisse und der Benutzungsregelungen durch  den BF äußerst erschwert bzw wenn überhaupt nur unter erheblichen Vermögenseinbußen  möglich und die Anschaffung einer adäquaten Wohnung am Beschäftigungsort aus dem  Veräußerungserlös ausgeschlossen wäre.

| Predicted | Gold |
|---|---|
| `MT` | `MT` |

**Missed by this rule (FN):**

- `Bezirksgericht` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Dagobert Duewel (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

| Predicted | Gold |
|---|---|
| `Dagobert Duewel` | `Dagobert Duewel` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_36`)


Dazu werde  festgehalten, dass auf Herrn JW im Beschwerdezeitraum kein Kraftfahrzeug angemeldet  gewesen sei und auch auf Frau PW sei in diesem Zeitraum kein PKW2 angemeldet gewesen.

| Predicted | Gold |
|---|---|
| `PW` | `PW` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_37`)


Mit dem auf Frau PW zugelassenen PKW3 seien im beschwerdegegenständlichen Zeitraum  3 von 15 Seite 4 von 15

| Predicted | Gold |
|---|---|
| `PW` | `PW` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_67`)


Die Gattin des  Gesellschafter-Geschäftsführers, Frau PW hat im Beschwerdezeitraum über ein privates  Fahrzeug (PKW3) verfügt.

| Predicted | Gold |
|---|---|
| `PW` | `PW` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_75`)


Dass auch die  Gattin des Gesellschafter-Geschäftsführers, Frau PW im Beschwerdezeitraum über ein privates  Fahrzeug (PKW3) verfügt hat, ist ebenso unzweifelhaft.

| Predicted | Gold |
|---|---|
| `PW` | `PW` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Olivia Trienes (= Beschwerdeführerin, Bf) bezieht für den Sohn A, geb. 06/1997, laufend  die Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Olivia Trienes` | `Olivia Trienes` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)


Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn Isenmann  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)


Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn Isenmann  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_54`)


Dass der (Original)Ausweis gemäß § 29b StVO 1960 mit der Nr. Nr1 (Nr2) an Herrn Isenmann  geb.  Herrgeb, ausgestellt wurde und dass Herr Ballschmieder laut ZMR mit Datum verstorben ist, ergibt sich  aus dem Schreiben der Bezirkshauptmannschaft Ort vom 16. März 2023.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_13`)


Der Bf. brachte in seinem Einspruch vom 19. Juni 2023 (E-Mail) vor, dass er das Fahrzeug vor  dem Geburtshaus geparkt habe, da seine Frau Wehen gehabt habe.

| Predicted | Gold |
|---|---|
| `Wehen` | `Wehen` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_7`)


In Beantwortung des Ergänzungsersuchens des Finanzamtes (siehe dazu Vorhalt vom  16.02.2024) teilte die Tochter der Bf,Frau Rittcher  dem Finanzamt daraufhin mit, dass sie einerseits  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Rittcher` | `Rittcher` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)
- `Finanzamt` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_11`)


Dagegen erhob die Bf, vertreten durch Frau Rittcher  fristgerecht Beschwerde mit der Begründung,  dass W.B. die FB erhalten hätte und nicht die Bf (siehe dazu Beschwerdeschriftsatz vom  25.03.2024).

| Predicted | Gold |
|---|---|
| `Rittcher` | `Rittcher` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_62`)


Durch den steuerlichen Vertreter wurde am 14.04.2015 im Rahmen einer Gebührenprüfung der  Beschluss des Stiftungsrates der XX Stiftung vom 10.10.2007 über die Vornahme einer  Ausschüttung in Höhe von € 240.000,- an Frau Klopstech beigebracht.

| Predicted | Gold |
|---|---|
| `Klopstech` | `Klopstech` |

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_105`)


Punkt 4   Weder Frau Heumann noch Herr Bf2 hätten jemals in diesem Gebäude gewohnt.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_109`)


Frau Heumann und Herr Bf2 würden seit Dezember 2020 (lt. Meldezettel 18.01.2021) in einer ca.  95m²-großen Wohnung in I 1, J wohnen, welche sich im Eigentum von Frau Heumann befinde.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |
| `Heumann` | `Heumann` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_111`)


3 Parteien davon seien Mieter von Frau Heumann und die 4.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_112`)


Partei sei die mit einem  Wohnrecht ausgestattete Lebensgefährtin des verstorbenen Großvaters von Frau Heumann  welcher  ihr die Liegenschaft übergeben hätte.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_114`)


Davor hätte Frau Heumann und Herr Bf2 in den jeweiligen Elternhäusern gewohnt,Frau Heumann in K 1, L  und Herr Bf2 in Dorf.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |
| `Heumann` | `Heumann` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_130`)


Frau Heumann und Herr Bf2 haben das Objekt erworben um damit ebenfalls Mieteinnahmen zu  erzielen – das Objekt also zu Vermietungszwecken zu nutzen.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_144`)


Die Wohnverhältnisse von Frau Heumann und Herrn Bf2 waren sowohl vor dem Kauf als auch nach  dem Kauf so gestaltet, dass das erworbene Objekt nicht für eigene Wohnzwecke angedacht  war.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_155`)


Zahlreiche Anhaltspunkte weisen klar darauf hin, dass Frau Heumann und Herr Bf2 das Objekt  erworben haben, um es auch tatsächlich zu Vermietungszwecken zu nutzen.

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_158`)


Sie  wohnen seit Dezember 2020 in einer ca. 95m² großen Wohnung im Eigentum von Frau Heumann (siehe Übergabsvertrag).

| Predicted | Gold |
|---|---|
| `Heumann` | `Heumann` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_4`)


Entscheidungsgründe  Mit Strafverfügung vom 1) 14.04.2025, GZ. MA67/GZ1/2025 und 2) 12.05.2025, GZ.  MA67/GZ2/2025, wurde Frau Langness für schuldig erkannt, sie habe das mehrspurige  Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (Land) am

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_15`)


Frau Langness bitte die beiden Strafen umzuleiten, bzw. ihr zu entziehen.

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_29`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde die (zwei) Strafverfahren gegen Frau Langness aufgrund der ihr zur Verfügung stehenden Unterlagen als Beschuldigte eingeleitet und ihr  gegenüber mit Strafverfügung vom 1) 14.04.2025, GZ. MA67/GZ1/2025 und 2) 12.05.2025, GZ.  MA67/GZ2/2025, unter Anlastung einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006  jeweils eine Geldstrafe in Höhe von 75,00 Euro verhängt und für den Fall der Uneinbringlichkeit  jeweils eine Ersatzfreiheitsstrafe von 17 Stunden auferlegt.

| Predicted | Gold |
|---|---|
| `Langness` | `Langness` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_30`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_155`)


Der in der  Anfrage der Möbel Zorkelglanz GmbH an das do. Finanzamt angeführte Sachverhalt entspreche nicht der  Vereinbarung und dem gesetzten Sachverhalt. Zu diesem Thema könnte auch Herrn DI O.C.  zeugenschaftlich befragt werden.

**False Positives:**

- `DI` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möbel Zorkelglanz GmbH`(organisation)
- `Finanzamt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

**False Positives:**

- `Alexander` — partial — pred is substring of gold: `Alexander X.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexander X.`(person)
- `M.`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Inn Trikraftglanz`(person)
- `Inn Trikraftglanz`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

**False Positives:**

- `AB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Baues`(person)
- `Baues`(person)
- `Borisowa`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_16`)


Danach seien monatliche Zahlungen von Herrn WS,  dem Gatten der Gesellschafterin der Bf, in Höhe der Kreditraten auf das Konto der Bf getätigt  worden.

**False Positives:**

- `WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_17`)


Mit Datum 09.09.2004 sei ein Mietvertrag bezüglich der Wohnung zwischen der Bf als  Vermieterin und Herrn MS (Bruder von WS) abgeschlossen worden.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_20`)


Der Mietvertrag sei von Herrn MS sowie seiner  geschiedenen Gattin als Nutzerin der Wohnung unterzeichnet worden.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_37`)


Es sei daher nicht nur ein zeitlicher, sondern auch ein unmittelbarer Zusammenhang zwischen  der Gründung der GmbH und der Scheidung des Herrn MS gegeben.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_61`)


Die Form der Bezahlung der Miete sei aus steuerlicher Sicht unerheblich, da  es zu einem Vermögensabfluss aus der Privatsphäre des Herrn MS gekommen sei.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_79`)


Mit Datum 09.09.2004 wurde ein Mietvertrag bezüglich der gegenständlichen Wohnung  zwischen der Bf als Vermieterin und Herrn MS, dem Schwager der Gesellschafter- Geschäftsführerin, abgeschlossen.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_80`)


Die Vermietung erfolgt aufgrund der, von Herrn MS im Zuge  seiner Ehescheidung übernommenen, Verpflichtung der Wohnversorgung seiner geschiedenen  Gattin und der gemeinsamen Kinder (Scheidungsvergleich vom 28.07.2003).

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_81`)


Der Mietvertrag  wurde von Herrn MS als Mieter und seiner geschiedenen Gattin als Nutzerin unterzeichnet.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_99`)


Es besteht unstrittig ein familiäres Naheverhältnis zwischen der Gesellschafter- Geschäftsführerin und dem Mieter der Wohnung Herrn MS (Schwager).

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_107`)


Die Wohnung wurde im Zusammenhang mit der Scheidung der Herrn MS und seinen daraus  entstandenen Verpflichtungen angemietet.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_112`)


Die Mietzinszahlungen in den Jahren 2004 und 2005 wurden nicht von Herrn MS,  sondern von der S-OEG getätigt.

**False Positives:**

- `MS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_113`)


Auch die Betriebskosten wurden nicht, wie im Mietvertrag vereinbart, von der Nutzerin der  Wohnung beglichen, sondern von Herrn WS, dem Gatten der der Gesellschafter- Geschäftsführerin.

**False Positives:**

- `WS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_287`)


Das Schwergewicht der Überwachungs- und Lenkungstätigkeiten für die Rusnok IT GmbH wurde im  Teil des Streitzeitraumes von 2010-25.9.2011 durch Herrn VN3 S1 durchgeführt, der bei seinen  Tätigkeiten von den beiden anderen Strategen (bis 25.9.2011) unterstützt wurde.

**False Positives:**

- `VN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rusnok IT GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_138`)


Nur weil das Finanzamt  diese Unterlagen nicht mehr im Akt finde, wie in der Bescheidbegründung der BVE behauptet,  heiße das nicht, dass die Behauptung von Herrn BfA unwahr sei.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_186`)


Knackpunkt für das Finanzamt sei, dass keine Nachweise  hinsichtlich einer Vorsprache Herrn BfAs sowie hinsichtlich einer mit diesem getroffenen  Einigung im Akt des FA enthalten sei.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_304`)


Der Anteil an den Einkünften für Herrn BfA beträgt: Euro 10.081,85  Der Anteil an den Einkünften für Frau BfB beträgt: Euro 10.081,84

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_30`)


Am 18.12.2002 kam die Bf. weiters mit dem (vormaligen) Landesgendarmeriekommando für  Kärnten dahingehend überein, dass Frau MartinmüllerA den in der strittigen Liegenschaft befindlichen  Gendarmerieposten - infolge Pensionierung der dort tätigen Raumpflegerin - mit Wirksamkeit  zum 1.1.2003 mitreinigen wird (vgl. Präambel zum Vertrag vom 18.12.2002).

**False Positives:**

- `Martinm` — partial — pred is substring of gold: `MartinmüllerA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MartinmüllerA`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_52`)


Wie eine Einsicht in den im Rahmen der Betriebsprüfung vorgelegten (undatierten)  „Dienstvertrag-Änderung“ zeigt, stand Frau MartinmüllerA seit Jänner 1993 in einem aufrechten  Vertragsverhältnis zur Bf..

**False Positives:**

- `Martinm` — partial — pred is substring of gold: `MartinmüllerA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MartinmüllerA`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/137276.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137276.1_19`)


In dieser  Stellungnahme brachten Sie jedoch entgegen Ihrem früheren Einspruch vor, aus der Apotheke  gekommen zu sein und das Gespräch mit Herrn ML gesucht zu haben.

**False Positives:**

- `ML` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_14`)


Vergl. hierzu “Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)


Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_17`)


Es würden mit Herrn Ing. K. (Geschäftsführer der Fa. X.  2 von 9 Seite 3 von 9

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_19`)


Die Entlehnung des Kfz gehe auf ein privates Ersuchen des Herrn Ing. K. zurück.

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation
- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Magistrat`(organisation)
- `Heimwerk GmbH`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)


Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die Jeremias Kierstan, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Jeremias Kierstan`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_28`)


Der angefochtene Bescheid vom 17.07.2015, mit welchem über den Antrag der Heimwerk GmbH auf  Herabsetzung der Abwassergebühr für 2013 abgesprochen wurde, ist an die Jeremias Kierstan  als  Partei ergangen und an deren Zustellbevollmächtigten, Herrn Vertreter zugestellt worden.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Jeremias Kierstan`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_24`)


Sie wären am  besagten Tag mit Herrn Herr1 unterwegs gewesen.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_25`)


Ebenso könne Herr Herr2, der die  Mitarbeitereinsatzplanung mit Herrn Herr3 vorbereitet bezeugen, dass Ihnen das Fahrzeug als  Verantwortlicher übergeben wurde.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_16`)


Er hat von Herrn AG lediglich ein  Entgelt von insgesamt EUR 2.506,82 erhalten.

**False Positives:**

- `AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_26`)


abzüglich Tankbelegen an Herrn AG abgegeben, 45% durfte der Bf. gleich behalten.

**False Positives:**

- `AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_36`)


Dazu werde  festgehalten, dass auf Herrn JW im Beschwerdezeitraum kein Kraftfahrzeug angemeldet  gewesen sei und auch auf Frau PW sei in diesem Zeitraum kein PKW2 angemeldet gewesen.

**False Positives:**

- `JW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PW`(person)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_60`)


Sämtliche Kosten des Fahrzeuges würden ausschließlich von Herrn JW getragen.

**False Positives:**

- `JW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_76`)


Die Feststellung, dass von der BF keine Nachweise hinsichtlich des Ausmaßes der privaten  Fahrten im Beschwerdezeitraum betreffend das dem Gesellschafter-Geschäftsführer zur  Verfügung gestellte Fahrzeug erbracht werden konnten, gründet sich vor allem darauf, dass  seitens Herrn JW im betreffenden Zeitraum keine Fahrtenbücher oder sonstigen  Aufzeichnungen geführt wurden.

**False Positives:**

- `JW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_160`)


Anders  ausgedrückt, hätte die BF die entsprechenden Nachweise erbringen können, wäre der  anzusetzende geldwerte Vorteil aus der privaten Nutzung durch die von Herrn JW geleisteten  Kostenersätze gedeckt gewesen.

**False Positives:**

- `JW` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_90`)


Wir danken Herrn NN für seine guten Leistungen und bedauern sein  Ausscheiden sehr.

**False Positives:**

- `NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_91`)


Wir wünschen Herrn NN auf seinem weiteren Berufs- und Lebensweg alles  Gute und weiterhin viel Erfolg.“  - AG2:  „Herr VN NN, geboren am Geb., war vom 01.09.2017 bis 31.08.2018 als geschäftsführender  Gesellschafter bei der AG2 tätig.

**False Positives:**

- `NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_106`)


Darüber hinaus oblagen Herrn NN sämtliche Marketingagenden, wie beispielsweise die  Konzeption und Erstellung unserer Homepage sowie die Implementierung unserer Gesellschaft  auf Social Media (Facebook, Instagram, ...).

**False Positives:**

- `NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_107`)


Wir haben Herrn NN als einen teamfähigen und kompetenten Mitarbeiter kennengelernt, der  seine Aufgaben mit großem Engagement zu unserer vollen Zufriedenheit erledigt hat.

**False Positives:**

- `NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_13`)


In seiner Beschwerde „gegen den Haftungsbescheid, zugestellt am 28.12.2016 an Herrn WT“  vom 23.1.2017 brachte der Beschwerdeführer vor, der Wirtschaftstreuhänder würde ihn „in  dieser Angelegenheit“ nicht vertreten.

**False Positives:**

- `WT` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_9`)


Am 16. Februar 2023 langte beim Magistrat per E-Mail ein als Einspruch gewertetes Schreiben  mit dem Betreff ‚Lenkererhebungen Kennz1, Leihvertrag Kennz1‘ ein, indem der  Beschwerdeführer sich bei Frau Reepschläger für das nette Telefonat bedankte, neben der  gegenständlichen Geschäftszahl zahlreiche weitere Geschäftszahlen anführte und als Lenker  Lenker1 (mit seinen persönlichen Daten) bekanntgab.

**False Positives:**

- `Reepschl` — partial — pred is substring of gold: `Reepschläger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat`(organisation)
- `Reepschläger`(person)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_42`)


Am 16. Februar 2023 langte beim Magistrat per E-Mail ein als Einspruch gegen die  Strafverfügung vom 12. Jänner 2023 gewertetes Schreiben mit dem Betreff ‚Lenkererhebungen  Kennz1, Leihvertrag Kennz1‘ ein, indem der Beschwerdeführer sich bei Frau Reepschläger für das nette  Telefonat bedankte, neben der nicht gegenständlichen Geschäftszahl MA67/Zahl4/2023 (die  vermutlich gemeinte Zahl lautet: MA67/Zahl3/2023) zahlreiche weitere Geschäftszahlen  anführte und als Lenker Lenker1 (mit seinen persönlichen Daten) bekanntgab.

**False Positives:**

- `Reepschl` — partial — pred is substring of gold: `Reepschläger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat`(organisation)
- `Reepschläger`(person)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_65`)


Gegen den Zurückweisungsbescheid der belangten Behörde vom 22. März 2023 erhob der  Beschwerdeführer fristgerecht Beschwerde und führte aus, er übersende noch einmal alle  Geschäftszahlen die bis einschließlich 31.03.2023 von Herrn Lenker2 verschuldet worden seien.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_66`)


Er habe die Behörde schon mehrmals gebeten alle (folgenden) Anonymverfügungen direkt an  Herrn Lenker2 zu senden, die für das gegenständliche Kraftfahrzeug mit dem behördlichen  Kennzeichen Kennz1 ausgestellt wurden;

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_72`)


Gegen den Zurückweisungsbescheid der belangten Behörde vom 22. März 2023 erhob der  Beschwerdeführer fristgerecht Beschwerde und führte aus, er übersende noch einmal alle  Geschäftszahlen die bis einschließlich 31.03.2023 von Herrn Lenker2 verschuldet worden seien.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_74`)


Herrn Lenker2 zu senden, die für das gegenständliche Kraftfahrzeug mit dem behördlichen  Kennzeichen Kennz1 ausgestellt wurden.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_24`)


……………………“  Beschwerde  Innerhalb offener Frist wurde in einem einheitlichen Schriftsatz Beschwerde gegen die an die  erblichen Töchter ergangenen Gebührenbescheide erhoben und dies wie folgt begründet:  “Mit rechtskräftigem Einantwortungsbeschluss vom 17.3.2016, ……, wurde der Nachlass nach  dem am 10. September 1972 .2015 verstorbenen, zuletzt in Salfeldstraße 54, 9500 Oberwollanig, Österreich  wohnhaft gewesenen  Industriemechaniker, Herrn FM, den aufgrund des Gesetzes bedingt erbantrittserklärten Erben,  der erbl. Witwe M, geb. …., zu einem Drittel und den erbl. Töchtern, mj. S, geb. ….., mj. J, geb.  ……., mj. L, geb. ……., und mj. KzlR Techn R RgR Wigand Beinhorn, geb. ……., zu je einem Sechstel eingeantwortet.

**False Positives:**

- `FM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `10. September 1972`(date)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `KzlR Techn R RgR Wigand Beinhorn`(person)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_20`)


Das FA wies auf die Meldebestätigung  betreffend die Bf und Ihrem Partner/Lebensgefährten Herrn Schäperjans und auf den ESt- bescheid 2016 vom 1.9.2017 an den Partner der Bf hin.

**False Positives:**

- `Sch` — partial — pred is substring of gold: `Schäperjans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schäperjans`(person)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/143870.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143870.1_75`)


Dass der BF mit Frau MM verheiratet ist, er eine Tochter, SM, hat und es sich beim Wohnsitz  des BF in Slowenien um den Familienwohnsitz handelt, erschließt sich schlüssig aus den  vorgelegten Unterlagen und dem Vorbringen des BF.

**False Positives:**

- `MM` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_67`)


Über die diesbezügliche Rücksprache mit der belangten Behörde sei vom steuerlichen  Vertreter am 7. August 2001 ein Aktenvermerk angelegt worden, welchen folgenden Inhalt  habe:  ….“Haben dies mit Herrn Mag. ***, FA Feldkirch am 7. August 2001 nochmals besprochen und  um einen Lösungsvorschlag gebeten: Nach Mag. *** soll die liechtensteinische FA Spittal Villach  eine  Proformarechnung an die RHO Pharma  ausstellen, somit wird die RHO Pharma  zum "Proforma  Verfügungsberechtigten" und kann die abgeführte Einfuhrumsatzsteuer problemlos als  Vorsteuer geltend machen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Feldkirch`(organisation)
- `FA Spittal Villach`(organisation)
- `RHO Pharma`(organisation)
- `RHO Pharma`(organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Johanna Thönßen, Natrun 54, 9560 Regenfeld, Österreich, vertreten durch seine Ehegattin, Ehegattin, über die Beschwerde vom 22. Juni 2020  gegen den Bescheid des Finanzamtes Österreich vom 2. Juni 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Steuernummer 56-442/5216  nach  der am 04.06.2024 im Beisein der Schriftführerin Frau Schriftführerin durchgeführten  mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Schriftf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johanna Thönßen`(person)
- `Natrun 54, 9560 Regenfeld, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `56-442/5216`(tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_27`)


Mit Vorlageantrag vom 16.07.2024 wurde die Entscheidung über die Beschwerde durch das  Bundesfinanzgericht beantragt und ergänzend wie folgt begründet:  „[…] Ergänzend zur Beschwerde vom 15.02.2024 wird vorgebracht, dass Herrn Luna Fruechtenicht  Seitens der Pensionsversicherungsanstalt zwischenzeitlich eine Waisenpension zugesprochen  wurde und entsprechend die Erwerbsunfähigkeit infolge Krankheit oder Gebrechens ab der  Kindheit über das 18.

**False Positives:**

- `Luna Fruechtenicht  Seitens` — partial — gold is substring of pred: `Luna Fruechtenicht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Luna Fruechtenicht`(person)
- `Pensionsversicherungsanstalt`(organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_150`)


Am 17.1.2025 wandte sich StB, der liechtensteinische steuerliche Vertreter, per E-Mail an die  Richterin und gab folgende Erklärung ab:  „… In dieser Sache haben wir im Jahr 2015 (und früher) das Verfahren für Frau VN-BfNN1-NN2- Bf geführt.

**False Positives:**

- `VN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_151`)


Der Steuerberater von Frau NN1 – Herr Kollege Z von der öStb-Kanzlei – ist cc. gesetzt.

**False Positives:**

- `NN` — partial — pred is substring of gold: `NN1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NN1`(person)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_155`)


Diesem Verzicht stimmt Herr Kollege Z in Vertretung von Frau  NN1 zu.  11 von 34 Seite 12 von 34

**False Positives:**

- `NN` — partial — pred is substring of gold: `NN1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `NN1`(person)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/146981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146981.1_438`)


erklärt, „das Geld“ stamme von einem Hochzeitsgeschenk an Herrn und Frau NN1-Bf im Jahr  2000.

**False Positives:**

- `NN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_128`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Beschwerdeführerin (Frau Bf1 und Herr Bf2 – Vermietungsgemeinschaft) haben die  Liegenschaft in A 7 mit Kaufvertrag vom 30. September 2021 käuflich erworben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_144`)


Die Wohnverhältnisse von Frau Heumann und Herrn Bf2 waren sowohl vor dem Kauf als auch nach  dem Kauf so gestaltet, dass das erworbene Objekt nicht für eigene Wohnzwecke angedacht  war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heumann`(person)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/148832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148832.1_44`)


Mit Schreiben des Bf vom 12.03.2025 nahm dieser zum Ergänzungsersuchen vom 21.01.2025  Stellung und legte eine Bestätigung der NZ vom 24.10.2023 hinsichtlich der an ihn im  Beschwerdejahr ausbezahlten Vergütungen, eine Bestätigung des Herrn JK betreffend den  Erhalt von € 300,00 sowie eine Kontoübersicht der SVS betreffend das Jahr 2020 vor.

**False Positives:**

- `JK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/148832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148832.1_72`)


Der Bf hat im Jahr 2020 € 300,00 an Herrn JK für laufende steuerliche Beratung und  Erledigungen bezahlt. Herr JK ist keine berufsrechtlich befugte Person.

**False Positives:**

- `JK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/148832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148832.1_90`)


Dass der Bf im Jahr 2020 € 300,00 an Herrn JK für laufende steuerliche Beratung und  Erledigungen gezahlt hat, ist der diesbezüglichen Bestätigung des Herrn JK zu entnehmen.

**False Positives:**

- `JK` — no gold match — likely missing annotation
- `JK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_21`)


Im vorliegenden Fall konnte nur Frau Einspruch erheben oder dessen Rechtsvertreterin, nicht  aber eine andere Person.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_27`)


Die Vollmacht wurde an MA67 damals per Post übermittelt. Grudnsätzlich ist die  Frage warum Frau Frau1 überhaupt zu Verantwortung gezogen wird wenn sie nicht die  Zulassungsbesitzerin ist.“

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_75`)


Diverse Bürotätigkeiten der Plöchinger KI GmbH  wie  Telefondienste, Ablage und Vervielfältigung von Unterlagen, Änderung von Verträgen,  Betriebskostenabrechnungen, Empfang von Kunden, Bestückung der Werbetafeln, wurden im  Rahmen der Vereinbarung durch eine bei der Bf. angestellte Mitarbeiterin, nämlich der Mutter  des Geschäftsführers AA, Frau DD erledigt, wobei in diesem Zusammenhang aber nicht  5 von 15 Seite 6 von 15

**False Positives:**

- `DD` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Plöchinger KI GmbH`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_109`)


Zudem wurde vom Geschäftsführer, Herrn Gf., bei der Schlussbesprechung gem § 149 Abs  1 BAO am 12.12.2017 mitgeteilt, dass in Peru keine steuerliche Erfassung der Betriebsstätte  erfolgte, dies wurde auch im Schreiben vom 22.12.2017 bestätigt.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `names_after_bf_or_representative` 💣

**F1:** 0.001 | **Precision:** 0.007 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `90c49816`  
**Description:**
Matches person names immediately following 'Bf.' (Beschwerdeführer) or 'Bf.' abbreviation, ensuring strict word boundaries to avoid matching common nouns.

**Content:**
```
(?:^|\s)Bf\.?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s*,\s*(?:Bakk\.?\s+techn\.|LLM|PhD|BA|MA)\.?)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.007 | 0.001 | 0.001 | 135 | 1 | 134 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 134 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_8`)


Aufgrund der Inanspruchnahme des Bf. Jaden Knauss  als Haftenden iSd § 82 EStG stehe dieses  nach haushaltsrechtlichen Bestimmungen in der Pflicht von den Dienstnehmern, welche eine  Naturalwohnung benützten und Schuldner der Lohnsteuer seien, einen Regress durchzuführen.

| Predicted | Gold |
|---|---|
| `Jaden Knauss` | `Jaden Knauss` |

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

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_30`)


Gegen das abweisende Erkenntnis vom 25.6.2019 des Bundesfinanzgerichts erhob der  rechtsfreundlich vertretene Bf Beschwerde gem. Art 144 B-VG an den Verfassungsgerichtshof.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)
- `Verfassungsgerichtshof`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_53`)


Gegen diesen Aufhebungsbescheid erhob die steuerlich vertretene Bf Berufung (nunmehr  Bescheidbeschwerde).

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_71`)


Gegen diesen Bescheid brachte der steuerlich vertretene Bf Beschwerde ein.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_14`)


Mit Eingabe vom 11. März 2019 erhob der Bf. Beschwerde gegen den  Einkommensteuerbescheid.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_6`)


Mit Schreiben vom 29.10.2013 wurde der steuerlichen Vertretung der Bf Folgendes zur  Kenntnis gebracht und eine Frist zur Beantwortung bis zum 18.11.2013 gesetzt:  "Der österreichischen Finanzverwaltung wurden durch Ihre schweizerische Zahlstelle gemäß  Art 9 des Steuerabkommens der Republik Österreich und der Schweiz Informationen über die  von Ihnen bei dieser Zahlstelle unterhaltenen Konten oder Depots samt jährlichen  Kontoständen übermittelt. Eine Ihrer Zahlstelle erteilte Ermächtigung zur freiwilligen Meldung  1 von 6 Seite 2 von 6

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_24`)


Mit Schriftsatz vom 18.12.2013 erhob die steuerliche Vertretung der Bf Berufung gegen den  Einkommensteuerbescheid für das Jahr 2003 und den Bescheid über die Festsetzung von  Anspruchszinsen 2003, beide vom 09.12.2013 und begründete diese damit, dass die im  Ergänzungsersuchen angeforderten Unterlagen für die Jahre 2003 bis 2012 erst jetzt  vollständig zur Verfügung hätten gestellt werden können.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_93`)


3.2. Verlosung von 2 Tickets und Verlosung des Ersatzes diverser Auslagen des täglichen  Lebens durch die Bf.  Die Bf. bringt vor, dass einerseits ein Preisausschreiben eine Sonderform der Auslobung gemäß  § 860 ABGB und kein Spiel darstelle und andererseits „Spiel“ eine Aktivität mehrerer Mitspieler  begrifflich definiere, hingegen die Entgegennahme eines Geschenkes keine Beteiligung an einem  Spiel sei.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_87`)


Die belangte Behörde schrieb der Bf Grunderwerbsteuer in Höhe von 1.000,20 € vor.

**False Positives:**

- `Grunderwerbsteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_61`)


Die Qualifikation von Strom als körperliches Wirtschaftsgut sei  jedenfalls bereits vor den Abgabenerklärungen der Bf Gegenstand unterschiedlicher  Literaturmeinungen gewesen, weshalb keine offensichtliche Unrichtigkeit vorgelegen sein  könne.

**False Positives:**

- `Gegenstand` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_68`)


Daraus folge, dass die Bf Strom erzeuge und liefere.

**False Positives:**

- `Strom` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_89`)


Zu § 293b BAO merkte der steuerliche Vertreter an, dass dem Finanzamt aus der Aktenlage  zum Zeitpunkt der Erstbescheide zwar bekannt gewesen sei, dass die Bf Strom liefere, nicht  aber, dass sie auch Wärme liefere.

**False Positives:**

- `Strom` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_105`)


Für den Erzeugungsprozess (Rührwerke, Pumpen,  Einbringung der Silage, Trocknung des Schüttgutes) bezieht die Bf Strom von der EVN, welche  der Bf Energieabgaben in Rechnung stellt. Die im Produktionsprozess entstehende Wärme wird  zur Beheizung der Biogasanlage verwendet, aber auch zur Beheizung von Trockenkammern,  die von landwirtschaftlichen Betrieben genutzt werden.

**False Positives:**

- `Strom` — no gold match — likely missing annotation
- `Energieabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_18`)


Weiters wurde begründend  der Rechengang   von der Steuer vor Abzug der Absetzbeträge   über die Abzüge, u.a. dem Familienbonus Plus in Höhe von 750,00 €,   bis zur Steuer nach Abzug der Absetzbeträge  dargestellt.  Dagegen erhob der Bf. Beschwerde, was als Antrag gemäß § 264 BAO auf Entscheidung über  die Beschwerde vom 22. Mai 2020 (Einbringungsdatum) durch das Verwaltungsgericht (hier:  Bundesfinanzgericht) aufzufassen ist.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_66`)


ebenfalls wurde erstmalig vorgebracht, dass auch er, der Bf. Krebs  hat.

**False Positives:**

- `Krebs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_69`)


Nachweis der geltend gemachten Kosten für Familienheimfahrten:  Auf Grund der obigen Ausführungen ist nur der Vollständigkeit halber festzuhalten:  Betreffend Fahrtkosten, welchen laut dem Vorbringen des Bf. Fahrten mit dem eigenen Kfz  zugrunde liegen, ist die Nachweisführung (anders als bspw.

**False Positives:**

- `Fahrten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_430`)


Die Stellungnahme wurde dem Bf. übermittelt. Mit E-Mail vom 31.8.2020 teilte der Bf.  Folgendes mit:  28 von 34 Seite 29 von 34

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_41`)


Mit Schriftsatz vom 24.07.2014 erhob die steuerliche Vertretung des Bf Beschwerde gegen die  erwähnten Bescheide vom 26.06.2014, stellte den Antrag auf mündliche Verhandlung und den  gesamten Berufungssenat und führte aus, dass der Sachverhalt bezüglich der übernommenen  Verkehrsstrafen im Bericht vom 26.06.2014 insoweit unrichtig dargestellt worden sei, als  übernommene Verkehrsstrafen nur dann vorlägen, wenn diese gegen die Dienstnehmer  verhängt würden.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_85`)


Am 5. Juli 2019 erhob die Bf. Einspruch gegen diese Vollstreckungsverfügung.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_96`)


Mit E-Mail vom 3.12.2019 erhob die Bf. Einspruch gegen die Beschwerdevorentscheidung, und  führte aus, sie habe das Fzg nicht gelenkt und bitte um Zusendung einer Lenkererhebung.

**False Positives:**

- `Einspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_901`)


Tatsache ist, dass die Bf. Gastronomiebetriebe in den Streitjahren betrieben hat, deren  Einkünfte aufgrund mangelhafter Aufzeichnungen zu schätzen gewesen sind.

**False Positives:**

- `Gastronomiebetriebe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_43`)


Außerdem studiert der Bf. Jus, wobei die diesbezüglichen geltend gemachten Kosten als  Werbungskosten im Jahr 2018 anerkannt wurden.

**False Positives:**

- `Jus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_9`)


Gegen diesen Bescheid erhob die Bf Beschwerde und beantragte in dieser die Berücksichtigung  des Alleinerzieherabsetzbetrages für ein Kind.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_29`)


Bezogen auf den Einkommensteuerbescheid 2010 wendete der Beschwerdeführer  zusammengefasst ein, die Bf. Steuerberatungsgesellschaft mbH sei von ihrem Mandanten D  mit der Beratung und Unterstützung in kaufmännischen wie finanziellen Angelegenheiten „im  Zusammenhang mit der Errichtung einer neuen Zubringerbahn für sein seit 1964 bestehendes  Schigebiet und Hotel S“ beauftragt worden.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_30`)


Im Jahr 2006 habe die Bf.  Steuerberatungsgesellschaft mbH für D und die Schilift GmbH diverse Agenden übernommen  2 von 10 Seite 3 von 10

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_34`)


Nach erfolgreicher Realisierung des „vorgenannten Investitionsvorhabens“  hätte die Bf. Steuerberatungsgesellschaft mbH laut einer mit D getroffenen Vereinbarung  weiterhin sämtliche Beratungsleistungen für dessen Betriebe und der Schilift GmbH zu  erledigen gehabt.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_35`)


Zum Zeitpunkt der Kapitalerhöhung der Schilift GmbH um EUR 1.365.000,-  auf EUR 1.400.000,- habe die Bf. Steuerberatungsgesellschaft mbH 100 % des Stammkapitals  aus ihrem Mandantenkreis als Gesellschafter gewinnen können.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_37`)


Die Neugesellschafter hätten als weitere Bedingung für ihre Finanzierungs- und  Beteiligungszusagen gefordert, dass die Bf. Steuerberatungsgesellschaft mbH sich an der  Schilift GmbH beteiligen müsse und die Geschäftsführung „durch die WT GmbH, in Person ihres  Gesellschaftergeschäftsführers, [des Beschwerdeführers], selbständig, zu übernehmen war.“

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_39`)


Konsequenz dieser Vereinbarung sei  gewesen, dass die Bf. Steuerberatungsgesellschaft mbH „die langfristige Werthaltigkeit der  empfohlenen Investitionen und Beteiligungen unter allen Umständen erhalten musste, da sie  ansonsten nicht nur die Einnahmen aus den Vertretungen D und dessen Unternehmen, sondern  auch die Einnahmen aus den Vertretungen der restlichen Mitgesellschafter verloren hätte“.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_40`)


Sämtliche Leistungen seien nachweislich von der Bf. Steuerberatungsgesellschaft mbH  abgerechnet worden, sie habe den alleinigen Nutzen aus dieser Beteiligung lukriert.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_49`)


Außenprüfungsverfahren der Bf. Steuerberatungsgesellschaft mbH erstattet worden sei.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_75`)


Der Beschwerdeführer war ausweislich des Firmenbuchs in den Jahren 2008 bis 2010  Alleingesellschafter und bis 11.12.2009 Geschäftsführer der im Firmenbuch zu FN_2  eingetragenen UEHX Medien GmbH (vormals Bf. Steuerberatungsgesellschaft m.b.H.).

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `UEHX Medien GmbH`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_89`)


Einerseits bezieht sich dieses Vorbringen auf einen Zeitpunkt nach Erlassung des  Erstbescheides, andererseits wurde die Sachverhaltsdarstellung vom 5.9.2012 offensichtlich im  Außenprüfungsverfahren bei der Bf. Steuerberatungsgesellschaft mbH erstattet.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_116`)


Insofern der Beschwerdeführer vermeint, seine (unentgeltliche) Geschäftsführertätigkeit für  die Schilift GmbH stelle bei wirtschaftlicher Betrachtungsweise einen Zusammenhang zwischen  seiner Garantieerklärung gegenüber der Traun-Handel AG und seinen Einkünften aus selbständiger Arbeit  als (wesentlich beteiligter) Gesellschafter-Geschäftsführer seiner Wirtschaftstreuhand GmbH  her, ist dem Folgendes entgegenzuhalten: Nach dem Beschwerdevorbringen war die Erzielung  von Einkünften durch die Bf. Steuerberatungsgesellschaft mbH aus Beratungstätigkeiten für D  und dessen Unternehmen und für die neu gewonnenen Mitgesellschafter der Schilift GmbH  von der Erhaltung der „langfristigen Werthaltigkeit der empfohlenen Investitionen und  Beteiligungen“ abhängig.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traun-Handel AG`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_117`)


Dem gegenüber behauptet der Beschwerdeführer nicht einmal, dass  die Höhe seiner eigenen Einkünfte als Gesellschafter-Geschäftsführer der Bf.  Steuerberatungsgesellschaft mbH („jährliche Geschäftsführerentschädigung in Höhe von EUR  36.000,- und sonstige Kostenersätze in Höhe von EUR 15.686,82 [2008 in Einkünften aus  selbständiger Tätigkeit erfasst]“) durch die Umstände seiner Geschäftsführung für die Schilift  GmbH beeinflusst worden wäre.

**False Positives:**

- `Steuerberatungsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schilift  GmbH`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_67`)


Nach dem festgestellten Sachverhalt steht fest, dass die Bf. Entgelte bzw. Betriebseinnahmen  nicht in die Umsatz- und Einkommensteuererklärungen der Beschwerdejahre aufgenommen  hat.

**False Positives:**

- `Entgelte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_189`)


Mit Schreiben (Verständigung vom Ergebnis der Beweisaufnahme) vom   1) 05.08.2020 teilte die belangte Behörde dem rechtsfreundlichen Vertreter des Bf.  gegenständlichen Sachverhalt mit und bot dem Bf. Gelegenheit zur Stellungnahme innerhalb  von zwei Wochen ab Zustellung dieses Schreibens.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_202`)


Diesbezüglich ist bei der Zentralen  Staatsanwaltschaft zur Verfolgung von Wirtschaftsstrafsachen und Korruption (WKStA) unter  der AZ: AktWKStA ein Ermittlungsverfahren gegen Herr anhängig und werden unter der GZ  GZLPD durch das Landeskriminalamt (LKA) Wien, LKA, 1090 Wien, Wasagasse 22, Ermittlungen  vorgenommen.“  2) bis 5) 23.09.2020 und 6) vom 18.09.2020 teilte die belangte Behörde dem  rechtsfreundlichen Vertreter des Bf. gegenständlichen Sachverhalt mit und bot dem Bf.  Gelegenheit zur Stellungnahme innerhalb von zwei Wochen ab Zustellung dieser Schreiben.

**False Positives:**

- `Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_8`)


In der Erklärung zur Arbeitnehmerveranlagung 2017 machte der Bf. Werbungskosten für  Familienheimfahrten im Betrag von € 3.672,00 sowie Sonderausgaben für Versicherungen im  Betrag von € 920,00 geltend.

**False Positives:**

- `Werbungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_12`)


Nach einem erfolglosen Zustellversuch an der Abgabestelle des Bf. wurde das Straferkenntnis  bei der Post Geschäftsstelle Post hinterlegt, ab 02. März 2021 zur Abholung bereitgehalten und  gilt daher mit diesem Tag als zugestellt.  Mit E-Mail vom 07. April 2021 erhob der Bf. Beschwerde und führte (wörtlich) aus:  „wie schon im ersten einspruch beschrieben, lag der behindertenausweis hinter der scheibe..

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_78`)


Des Weiteren machte der Bf. Unterhaltszahlungen an seine Kinder unter dem Titel „Kosten für  doppelte Haushaltsführung“ als Werbungskosten geltend, allerdings übermittelte der Bf. dazu  lediglich zwei Belege, aus denen Zahlungen im Jahr 2021 und somit außerhalb des  beschwerdegegenständlichen Zeitraums hervorgehen.

**False Positives:**

- `Unterhaltszahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_88`)


Für die beschwerdegegenständlichen Jahre machte der Bf. Kosten für Arbeitsmittel, für  Familienheimfahrten und für die „doppelte Haushaltsführung“ als Werbungskosten geltend.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_340`)


In ihrer Vorhaltsbeantwortung vom 30.9.2020 führte die Bf. Folgendes aus:  „…  2. Vorbemerkung zur Verschaffung der Verfügungsmacht  22 von 59 Seite 23 von 59

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_85`)


Mit Eingabe vom 16.12.2015 erhob die damalige steuerliche Vertreterin der Bf. Beschwerde  gegen die oa Bescheide und stellte gleichzeitig die Anträge auf Entscheidung durch den  gesamten Beschwerdesenat sowie die Durchführung einer mündlichen Verhandlung.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_496`)


Es steht daher fest, dass den Lieferanten der Bf. Umsatzsteuerhinterziehungen vorzuwerfen  sind.

**False Positives:**

- `Umsatzsteuerhinterziehungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_550`)


Dieser Umstand spricht für die Gutgläubigkeit der Bf.  Was die anfängliche Verwechslung des Gf. der Bf. betreffend Herrn K. betrifft, wonach er nicht  gewusst habe, welche Funktion Herr K. gehabt habe, ist entgegenzuhalten, dass sich die  Unkenntnis nur auf das erste Zusammentreffen bezog und sich der Bf. dann eine Passkopie und  die Visitenkarte von Herrn K. aushändigen hat lassen.

**False Positives:**

- `Was` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_7`)


In ihrer Abgabenerklärung machte die Bf. Fortbildungskosten iHv. € 6.387,32 geltend.

**False Positives:**

- `Fortbildungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_49`)


KESt 25 %  2.146,00 4.467,00 5.663,00 5.428,00 5.577,00  3 Berufung (Beschwerde)  Mit Schriftsatz vom 08.01.2010 brachte die Bf Berufung (nunmehr Beschwerde) gegen die  Umsatz- und Körperschaftssteuerbescheide sowie die Haftungsbescheide ein.

**False Positives:**

- `Berufung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_82`)


In  den Jahren 2013 und 2015 hat die Bf. Leistungen der Schweizer Krankenversicherung  ÖKK in Anspruch genommen und abgerechnet (vorgelegte Leistungsabrechnungen).

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_170`)


5. EINKOMMENSTEUER 2011 und 2012  WOHNSITZE der Bf.  Die Frage, ob eine Person in Österreich unbeschränkt steuerpflichtig ist, richtet sich nicht nach  Doppelbesteuerungsabkommen, sondern ausschließlich nach den inländischen  steuerrechtlichen Vorschriften.

**False Positives:**

- `Die Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_5`)


Mit Schriftsatz vom 11.12.2015 brachte die steuerliche Vertretung des Bf. Bescheidbeschwerde  gegen die Einkommensteuerbescheide 2010 bis 2013 und gegen die Anspruchszinsenbescheide  2010 bis 2013 alle vom 9.11.2015 (zugestellt am 13.11.2015) beim Finanzamt am 15.12.2015  ein.

**False Positives:**

- `Bescheidbeschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_227`)


Die Einholung eines dritten Sachverständigengutachtens wird als nicht erforderlich angesehen,  weil der Entlassungsbrief (ON 13) ausschließlich auf den tragischen Zustand der Bf Bezug  nimmt, den die Bf seit ihrem Beinahe-Ertrinken im Jahr 2017 hat, und der mit ON 15 vorgelegte  Arztbrief der NÖ Landesnervenklinik Mauer/Amstetten vom 10.04.1997, keinerlei Hinweis auf  den Zeitraum bis zur Vollendung des 21.

**False Positives:**

- `Bezug` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_68`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Firma A als Gruppenträgerin ist, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_66`)


Dass die Bf. Teil einer Unternehmensgruppe als Gruppenträgerin mit den genannten weiteren  Gruppenmitgliedern ist, ergibt eine Einschau des Gerichtes in den elektronischen  Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_67`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Firma A als Gruppenträgerin ist, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_221`)


Der Leistungsaustausch kann also wie folgt skizziert werden:  1. D./Deutschland (bis 31. Oktober 2013) und D./Holland (ab 1. November 2013) bestellen  /beauftragen bei der Bf. Werbeleistungen (Produktmarketing und —promotion) als  Leistungsgegenstand.

**False Positives:**

- `Werbeleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_254`)


Die Außenprüfung will die Bf. durch gesetzlich nicht gedeckte Abgabenerhöhungen zwingen,  am Leistungsaustausch nicht beteiligte Dritte auszuforschen und mit Namen und  Anschriften zu nennen: Die Trafikanten, deren Namen und Anschriften die Bf. erkunden soll,  haben an die Bf. weder Leistungen erbracht noch an die Bf. Leistungen abgerechnet.

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_317`)


Seitens der Bf. wurden die Teilnehmer (Trafikanten) an den Awards - trotz Aufforderung durch  die Außenprüfung- nicht benannt, da die Trafikanten an die Bf. weder Leistungen erbracht  noch an die Bf. Leistungen abgerechnet haben und sich die Bf. daher auch keine  Betriebsausgaben mangels Leistungsbezug von den Trafikanten abgezogen hat.

**False Positives:**

- `Leistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/135625.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135625.1_13`)


Mit Schriftsatz vom 10.12.2020 brachte der Bf Beschwerde ein, ersuchte um Neuberechnung  der ao. Belastung und legte einen Arztbrief vom 07.07.2018 sowie einen Untersuchungsbefund  vom 09.07.2018 vor.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_71`)


In diesem Fall bestünde ein  Familienbeihilfenanspruch des Bf. Andernfalls hat der Bf. für seine Tochter, die nicht  haushaltszugehörig ist, mangels überwiegender Unterhaltleistung weder nach  Gemeinschaftsrecht noch nach innerstaatlichem Recht einen Anspruch auf Familienbeihilfe.

**False Positives:**

- `Andernfalls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_83`)


Ein Vertreter konnte wirksam nur im  Namen des Bf Beschwerde erheben.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_12`)


In diesen wurde ausgeführt, dass  der Bf. Polizeibeamter sei, und seit dem Jahr 2007 mehrere Monate im Jahr auf  Auslandseinsätze für die europäische Grenzschutzagentur Frontex entsandt werde.

**False Positives:**

- `Polizeibeamter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Frontex`(organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/137228.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137228.1_64`)


Außerdem wohnt  der Bf. Im Familienverband mit seiner Mutter gegenüber (cf. Übergabevertrag).

**False Positives:**

- `Im Familienverband` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_69`)


Für den Beschwerdefall bedeutet das:  Indem die Bf Krankengeld bezogen hat, sind ihr während des Jahres Bezüge zugeflossen, die  mit dem gesetzlich vorgesehen Pauschalsteuersatz besteuert wurden.

**False Positives:**

- `Krankengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_14`)


2.) Optionen des Bf   Angesichts dieser Diagnose hatte der Bf im Wesentlichen die folgenden Optionen:   a.) insbesondere radikale Prostatektomie: Bei dieser Methode wird die Prostata entfernt.

**False Positives:**

- `Angesichts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/137527.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137527.1_20`)


Die Entscheidung des Bf  Der Bf entschied sich nach eingehenden ärztlichen Untersuchungen nach Absprache mit Dr.  med. et phil.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_18`)


Mit Fax vom 28.06.2021 erhob die steuerliche Vertretung der Bf Beschwerde gegen den  Bescheid über die Festsetzung einer Zwangsstrafe vom 27.05.2021 in Höhe von 1.000 € und  führte begründend aus, dass es richtig sei, dass die steuerliche Vertretung keine Meldung  durchgeführt habe.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_211`)


Aus den vorgebrachten und vorgelegten Mailverkehr vom Oktober 2021 (vorgebrachter  „mehrtägiger Kontakt mit dem BMF“) über Probleme bei der Eintragung kommt jedenfalls  nicht Ausdruck, dass die Bf. Willens war, die WiEReG-Meldung irgendwie zeitnah  durchzuführen oder allfällige vorgebrachte technische Schwierigkeiten, allfällige  Anfangsschwierigkeiten und Datenprobleme zügig und zeitnah zu überwinden.

**False Positives:**

- `Willens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_79`)


Rechtliche Beurteilung:    Strittig ist, ob dem mj. Bf. Familienbeihilfe und Kinderabsetzbeträge ab jänner 2016 zustehen.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_19`)


Die Beschwerdevorentscheidungen wiesen die Beschwerde als unbegründet ab, wogegen der  Bf. Vorlageantrag einbrachte.

**False Positives:**

- `Vorlageantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/137983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137983.1_35`)


In der Vorhaltsbeantwortung vom 09.05.2022 führte die Bf Folgendes aus:  Das Bachelorstudium „Gesundheits- und Krankenpflege“ sei stark berufsorientiert und eng mit  der pflegerischen Praxis verbunden.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_16`)


Gegen diesen Rückforderungsbescheid reichte die Bf Beschwerde ein und begründete den  Studienabbruch durch eine schwere psychische Erkrankung der Tochter, die einen  Wiedereinstieg für S. in das alte Studium unmöglich gemacht hätte.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_107`)


Unter Abwägung, dass zwar bestimmte Zubehörteile einer höheren privaten Nutzung (z.B.  „Gaming-Tastatur) zuzuordnen sind, andere wiederum weniger, die Festplatte im Jahr 2020 zu  maximal 20% mit Studiumsdateien belegt war, erscheint ein iSd 184 BAO auszuscheidender  Privatanteil iHv 40 % für dieses EDV-Zubehör als angemessen und wird hiermit sowohl dem  Vorbringen des Finanzamtes als auch dem des Bf. Rechnung getragen.

**False Positives:**

- `Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_54`)


Dagegen richtet sich die fristgerecht eingebrachte Beschwerde vom 22. März 2022, in welcher  die Bf. Folgendes ausführt:  „Hiermit leite ich eine Beschwerde gegen den Halter vom Fahrzeug ein!

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/138996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138996.1_26`)


Der BF hat den streitgegenständlichen Pkw Nissan Navara am 02.03.2011  erworben und am 04.03.2011 in Deutschland auf seine Einzelfirma I in Bf Adr D mit dem  deutschen Kennzeichen XY zugelassen.

**False Positives:**

- `Adr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/139401.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139401.1_11`)


Im Zeitraum 10/2010 bis 07/2011 wurden im Auftrag der Bf. Adaptierungs- bzw.  1 von 12 Seite 2 von 12

**False Positives:**

- `Adaptierungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_15`)


Gebäude gehörten nicht  ins Umlaufvermögen der Bf.  Der AfA- Satz betrage nach Ansicht des FA 2,5%.

**False Positives:**

- `Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_169`)


AR der Bf Nr. 2017/229  vom 1.9.2017 in „angeforderte Unterlagen Teil 3“;

**False Positives:**

- `Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_206`)


Über ein mögliches Nahverhältnis der drei Geschwister zur Z1Z2Z3 Privatstiftung ist nichts  ermittelt worden, obwohl diese Privatstiftung die weitaus überwiegenden Gesellschaftsanteile  hält.  Die Gesellschafterin der Mieterin war im Streitzeitraum ausschließlich die Bf Bf Veranlagungs  GmbH (FN 360729 i), deren Alleingesellschafter Linn Brümmer IE war.

**False Positives:**

- `Bf Veranlagungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Linn Brümmer`(person)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_5`)


Mit Eingabe vom 07.03.2020 nahm die Bf. Stellung zu den beantragten Ausgaben.

**False Positives:**

- `Stellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_90`)


Die Berücksichtigung des Pensionistenabsetzbetrages war gemäß § 33 Abs. 6 EStG 1988  deshalb angesetzt worden, da der Bf. kein Anspruch auf Verkehrsabsetzbetrag zugesprochen  worden war und die Bf. Pensionsabfindung im Jahre 2017 bekommen hatte.

**False Positives:**

- `Pensionsabfindung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/139584.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139584.1_257`)


Auch § 23 AlVG ist in diesem Fall nicht anwendbar, weil die Bf. Arbeitslosengeld erhalten hat,  welches keine Bevorschussung von Leistungen aus der Pensionsversicherung darstellte und  darstellt.  Zu den Berechnungen der Negativsteuer ist auszuführen, dass gemäß § 33 Abs. 8 EStG 1988  eine Negativsteuer nur zu erstatten ist, wenn gemäß Z 1 lit. cit.

**False Positives:**

- `Arbeitslosengeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_11`)


Gegen diesen, am 15.05.2019 ausgestellten, Einkommensteuerbescheid 2015 wurde ein  Antrag auf Aufhebung gem. § 299 Abs. 1 BAO gestellt. Dazu vorgelegt wurde eine Aufstellung  der tatsächlich erhaltenen Beträge (EUR 2.506,82), eine Aufstellung der Tage, an denen vom  Bf. Taxifahrten durchgeführt wurden sowie die Bestätigung über den abgeleisteten Zivildienst  im Zeitraum von 01.10.2014 bis 30.06.2015.

**False Positives:**

- `Taxifahrten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_18`)


Am 31.10.2019 brachte der Bf. Beschwerde ein.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/140407.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140407.1_94`)


Es folgt:  In Jahren, in welchen die Bf. Betriebseinnahmen infolge von Immobilienverkäufen lukrierte,  leistete sie aufgrund der dargestellten Vereinbarungen am Tag deren Abschusses sogenannte  „Immobilienanzahlungen“ an die GmbH1  bzw. an die an deren Stelle tretende XY Invest  Gesellschaft mbH (im Schema: GmbH 1).

**False Positives:**

- `Betriebseinnahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_30`)


5. Gegen den Abweisungsbescheid vom 17.03.2023 wurde von der steuerlichen Vertretung des  Bf. Beschwerde eingebracht (eingebracht per FinanzOnline am 14.04.2023).

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_7`)


Investoren mit der Kommanditistin der Bf Treuhandvereinbarungen abschließen und das so in  die KG gelangte Kapital im Wege atypisch stiller Beteiligungen an Unternehmen zur  Finanzierung weitergegeben wird.

**False Positives:**

- `Treuhandvereinbarungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_179`)


Nach der Erklärung, dass erst der erste Zusammenschluss der Bf Betrieblichkeit  und damit das Zusammenschlusserfordernis vermittle findet sich noch der Satz: „Die *TH-Kdt*  GmbH ist neben einer eigenen Einlage auch als Treuhänder für Treugeber tätig.

**False Positives:**

- `Betrieblichkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_489`)


Sie sind bei der Bf Betriebsausgaben und fließen in die allgemeine  Gewinnermittlung ein.

**False Positives:**

- `Betriebsausgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/142566.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142566.1_23`)


Die Zustellung des gegenständlichen Bescheides erfolgte direkt an die Bf. Eine Zustellung an die  zustellbevollmächtigte Vertretung erfolgte nicht.

**False Positives:**

- `Eine Zustellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_BFG_20260814_VALIDATE/142648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142648.1_7`)


Dagegen erhob der Bf. Beschwerden mit der Begründung, dass ihm auch für die Stieftochter  der Familienbonus Plus zustehe, da er auch der Bezieher der Familienbeihilfe für seine  Stieftochter im Zeitraum Juli - Dez 2020 sowie Jänner - Dezember 2021 war.

**False Positives:**

- `Beschwerden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_BFG_20260814_VALIDATE/143650.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143650.1_38`)


Dieser Sachverhalt basiert auf den Angaben des Bf. Wegen des unstrittig vom FA nicht  geforderten Zustellnachweises lässt sich die fehlende Zustellung des streitgegenständlichen  Schriftstückes durch die Post nicht widerlegen.

**False Positives:**

- `Wegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_1`)


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

**Example 93** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_63`)


Dass die Bf. Teil einer Unternehmensgruppe mit den genannten weiteren Gruppenmitgliedern  bzw. der Möhlmeyer Immobilien GmbH als Gruppenträgerin war, ergibt eine Einschau des Gerichtes in den  elektronischen Veranlagungsakt.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Möhlmeyer Immobilien GmbH`(organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_VALIDATE/144086.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144086.1_15`)


Dem Antwortschreiben legte der Bf Belege hinsichtlich der  Fahrtkosten sowie eine Wohnsitz- und Familienstandsbescheinigung der Gemeinde C vom  19.9.2019 bei.

**False Positives:**

- `Belege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_58`)


Mit Schreiben vom 24.08.2023 erinnerte die Nord Ostunisyn GmbH daran, dass dieser Fall auf die Zeit  zwischen 2003 und 2006 zurückgehe, in der Bf. Optionen im Rahmen der S.P. Corp.

**False Positives:**

- `Optionen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nord Ostunisyn GmbH`(organisation)

**Example 96** (doc_id: `deanon_BFG_20260814_VALIDATE/144127.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144127.1_101`)


Sachverhalt   Sachverhaltsmäßig steht fest, dass der Bf. Optionen, die ihm der Arbeitgeber im Jahr 2003 und  2006 eingeräumt hatte, im Jahr 2012 ausgeübt hat.

**False Positives:**

- `Optionen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_8`)


Mit Eingabe vom 28. Juli 2015 hat der Bf Beschwerde gegen den Bescheid über die Festsetzung  der Kapitalertragsteuer erhoben und beantragte die Aussetzung der Einhebung der  vorgeschriebenen Kapitalertragsteuer und der festgesetzten Säumniszuschläge.

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_22`)


Nach Erlangung der Kenntnis von Laseroperationen in A-Stadt habe die Bf. Dr. A3 konsultiert,  welcher sich zur Durchführung einer Operation nach entsprechender Vorbereitung der  Patientin bereit erklärt habe.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. A3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. A3`(person)

**Example 99** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_196`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Ag Bel des Bf.  Der Bf. macht diverse ag Bel für sich und seine Ehegattin geltend.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

## `names_in_address_context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03a0bc4c`  
**Description:**
Matches names that appear immediately before an address pattern (street, number, postal code, city), ensuring the name is not truncated.

**Content:**
```
(?:in der Beschwerdesache(?:\s+der)?|als Beschwerdeführerin|als Beschwerdeführer)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s*,\s*(?:Bakk\.?\s+techn\.|LLM|PhD|BA|MA)\.?)?)|(?:in der Beschwerdesache(?:\s+der)?|als Beschwerdeführerin|als Beschwerdeführer)\s+([A-Z]{2,}(?:\.[A-Z])?)|(?:in der Beschwerdesache(?:\s+der)?|als Beschwerdeführerin|als Beschwerdeführer)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
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

## `names_after_legal_roles` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `238ba189`  
**Description:**
Matches names appearing after specific legal roles like 'Richter', 'Richterin', excluding the role itself and single-letter abbreviations or known titles.

**Content:**
```
(?:durch den Richter|durch die Richterin|durch den Senatsvorsitzenden)\s+(?!Mag\.?)(?!Dr\.)(?!Priv\.-Doz)(?!Univ\.-Prof)(?!Hon\.-Prof)(?!Techn R)(?!OMedR)(?!KommR)(?!RgR)(?!StR)(?!OStR)(?!HR)(?!Dipl\.-Ing\.?)([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]+)*)
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

## `standalone_names_in_legal_context` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d20f7e20`  
**Description:**
Matches standalone person names in contexts like 'vom [Name]' or 'gegen den Bescheid ... [Name]', capturing full names with umlauts, excluding address-like false positives.

**Content:**
```
(?:vom 2[0-9]{3}|vom \d{2}\. \w+ \d{4}|gegen den Bescheid des [A-Za-z]+(?: \w+)* vom \d{2}\. \w+ \d{4})[^a-zA-Z]*([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?!.*(?:GmbH|AG|KG|M\.B\.H.|Gesellschaft))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 13 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_708`)


Eigentümer über den Gegenstand zu verfügen, auf den Erwerber übertragen wurde, wenn der  Lieferant nachweist, dass dieser Gegenstand in einen anderen Mitgliedstaat versandt oder  befördert wurde und wenn der Gegenstand infolge dieser Versendung oder Beförderung den  Liefermitgliedstaat physisch verlassen hat (vgl. in diesem Sinne Urteil vom 16. Dezember 2010,  Euro Tyre Holding, C-430/09, EU:C:2010:786, Rn. 29) (Rn. 30).

**False Positives:**

- `Euro Tyre Holding` — type mismatch — same span as gold: `Euro Tyre Holding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Euro Tyre Holding`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_54`)


Das Bundesfinanzgericht (BFG) hat erwogen:  B) Zur Rechtzeitigkeit der Beschwerde vom 29. März 2021:  Die Bf. hat die Beschwerde mit eingeschriebenem Brief am 29. März 2021 an das Finanzamt  Österreich (Postleitzahl 1000) abgesendet.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_9`)


Ab 1. Jänner 2019 wurde die Familienbeihilfe vom Finanzamt auf Grund der EU-Anpassungs- verordnung, BGBl. II Nr. 318/2018, gültig ab 1. Jänner 2019, indexiert ausbezahlt.  Antrag vom 30. April 2020  Mit Eingabe vom 30. April 2020 stellte der Bf. nachstehenden Antrag:   1 von 20 Seite 2 von 20

**False Positives:**

- `Mit Eingabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_12`)


Bezugnehmend auf die oben genannten EU- Verordnung beantrage ich die Auszahlung der  Familienbeihilfe ohne Indexierung ab 01.01.2019, da die EU-Verordnung subsidiär anwendbar  (in der Rechtshierarchie an der ersten Stelle vor den nationalen Rechtsbestimmungen steht)  ist.“  Bescheid vom 12. Mai 2020  Das Finanzamt wies den Antrag mit Bescheid vom 12. Mai 2020 mit der Begründung ab, dass  das Schreiben vom 23. April 2020, eingelangt am 30. April 2020, als Antrag auf Gewährung der  Familienbeihilfe in Höhe der in § 8 Abs. 3 und 4 des Familienlastenausgleichsgesetzes 1967  festgelegten Beträge und auf Gewährung des Kinderabsetzbetrages in Höhe des in § 33 Abs. 3  erster Satz des Einkommensteuergesetzes 1988 festgelegten Betrages gewertet worden sei.

**False Positives:**

- `Das Finanzamt` — partial — gold is substring of pred: `Finanzamt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_16`)


Beschwerde vom 20. Juli 2020  Der Bf. erhob gegen den Abweisungsbescheid am 20. Juli 2020 - eine vom Finanzamt in  Ermangelung des Vorhandenseins eines Zustellnachweises, respektive der daraus  resultierenden Unmöglichkeit der amtswegigen Feststellung des tatsächlichen  Zustellzeitpunktes - als fristgerecht gewertete Beschwerde.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_20`)


Vorlageantrag vom 10. März 2021  Mit Eingabe vom 10. März 2021 stellte der Bf. den Antrag auf Vorlage des Rechtsmittels an das  Bundesfinanzgericht.

**False Positives:**

- `Mit Eingabe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_33`)


Vertragsverletzungsverfahren  Klage der Europäischen Kommission vom 22. Juli 2020  Nach Stellung des Vorabentscheidungsersuchens des Bundesfinanzgerichts reichte die  Europäische Kommission mit Beschluss vom 14. Mai 2020 im Verfahren INFR(2018)2372 am  22. Juli 2020 Klage gegen die Republik Österreich beim Gerichtshof der Europäischen Union  ein, die zur Zahl C-328/20 protokolliert wurde.

**False Positives:**

- `Nach Stellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichts`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_50`)


Zurücknahme des Vorabentscheidungsersuchens vom 16. April 2020  Mit Beschluss BFG 18.

**False Positives:**

- `Mit Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Christine Gäbelt  in der Beschwerdesache Verena Piechura,  Nußöd 5, 2014 Breitenwaida, Österreich, über die Beschwerde vom 7. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Juni 2022, Ordnungsbegriff Nr1, betreffend die Rückforderung zu Unrecht  bezogener Beträge   1. an Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum Oktober 2021 bis        Juni 2022 für den Sohn B  2.

**False Positives:**

- `Ordnungsbegriff Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Christine Gäbelt`(person)
- `Verena Piechura`(person)
- `Nußöd 5, 2014 Breitenwaida, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Chiara Wälte  in der Beschwerdesache Dagobert Duewel,  Karl Schäfer-Gasse 25, 2161 Poysbrunn, Österreich, über die Beschwerde vom 18. Oktober 2022 gegen die Bescheide des  Finanzamtes Österreich vom 12. September 2022, Ordnungsbegriff Nr1, betreffend Abweisung  der Anträge auf Familienbeihilfe und Erhöhungsbetrag für den Zeitraum ab Juni 2022 zu Recht  erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ordnungsbegriff Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Chiara Wälte`(person)
- `Dagobert Duewel`(person)
- `Karl Schäfer-Gasse 25, 2161 Poysbrunn, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Aurelia Frässdorf  in der Beschwerdesache Janet Giesendorf,  Am Teich 47z, 7322 Lackenbach, Österreich, über die Beschwerde vom 21. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 26. September 2023, Ordnungsbegriff Nr1, betreffend Abweisung  des Antrages auf den Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum April 2019 –  September 2022   zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ordnungsbegriff Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Aurelia Frässdorf`(person)
- `Janet Giesendorf`(person)
- `Am Teich 47z, 7322 Lackenbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_321`)


2000, I- 6973, Randnr 53,  sowie vom 15. März 2007, Reemtsma Cigarettenfabriken, C- 35/05, Slg.

**False Positives:**

- `Reemtsma Cigarettenfabriken` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/147306.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147306.1_279`)


Von Relevanz für die Beurteilung des § 12 Abs. 1 Z 10 KStG 1988 sind insbesondere die  nachstehenden Ausführungen des EuGH in der Rechtssache Lexel AB:  Rn 50: Außerdem ist zum einen dem Steuerpflichtigen, ohne ihn übermäßigen  Verwaltungszwängen zu unterwerfen, im Rahmen der Prüfung, ob es sich um eine rein  künstliche Konstruktion zu ausschließlich steuerlichen Zwecken handelt, die Möglichkeit  einzuräumen, Beweise für etwaige wirtschaftliche Gründe für den Abschluss dieses Geschäfts  beizubringen (Urteil vom 13. März 2007, Test Claimants in the Thin Cap Group Litigation, Rn.  82).

**False Positives:**

- `Test Claimants` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1215, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_204`)

Der Einschreiter **Evelyn Antwerber**  ist handelsrechtlicher Geschäftsführer der Firma1.

- missed: `Evelyn Antwerber` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130162.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130162.1_4`)

Die Gesellschafter der Bf. - die Pflege Nexwerkwald GmbH und **N.N.** - sind jeweils mit einer Stammeinlage von  40.000 € an der Bf. beteiligt.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_168`)

Anhand des (Fach) Ärztlichen Gutachtens des Bundesamtes für Soziales und Behindertenwesen  (Sozialministeriumservice) vom 8.07.2020 beträgt der Grad der Behinderung für Ihre Tochter F.  **M.** 30% ab dem 1.11.2019.

- missed: `M.` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Hon.-Prof. Günter Salahi**  in der Beschwerdesache Jaden Knauss,  Dossenweg 3, 4132 Atzesberg, Österreich  über die Beschwerde vom 8. Jänner 2021 gegen den Bescheid des Finanzamtes  Österreich vom 3. Dezember 2020 Rückzahlung gemäß § 239 BAO, Steuernummer  15-678/4603  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Hon.-Prof. Günter Salahi` (person)
- predicted in sentence: `Hon.-Prof. Günter Salahi`, `Jaden Knauss`

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_65`)

besprochen gelingt es nicht, für Rechtsanwalt  RA1 die verlangte Meldung für seine **Dario Kobben**.

- missed: `Dario Kobben` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)

Zu den vereinbarten Einkaufskonditionen gab Herr **Inn Trikraftglanz**  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

- missed: `Inn Trikraftglanz` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des **Evelyn Antwerber**, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

- missed: `Evelyn Antwerber` (person)
- predicted in sentence: `Dr. Farid Rifaad`

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/147673.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147673.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Armin Treichl** in der Beschwerdesache  Cassandra Heinbichner, Wankmüllerhofstraße 350, 4664 Moosham, Österreich, über die Beschwerde vom 28. Dezember 2023 gegen den Bescheid  des Finanzamtes Österreich vom 23. November 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 72-665/1311  zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

- missed: `Mag. Armin Treichl` (person)
- predicted in sentence: `Cassandra Heinbichner`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch **Dr Christian Burghardt**, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Dr Christian Burghardt` (person)
- predicted in sentence: `StR Univ.-Prof. Alvin Paulikat`

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Alessia von Bauer**  in der Beschwerdesache  Dimitri Seelos, geb. am 19. November 1987  und Dipl.-Ing. Luna Goedecken, BEd MA, geb. am 12. April 1988  als Erben  des Reneé Keles, verstorben am 3. November 1972  über die Beschwerde vom 15. Dezember 2020  gegen die Bescheide des Finanzamtes Österreich vom 27. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2015 bis 2019;

- missed: `Univ.-Prof.in Alessia von Bauer` (person)
- predicted in sentence: `Univ.-Prof.in Alessia`, `Dimitri Seelos`, `Dipl.-Ing. Luna Goedecken`

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden **Mag. Armin Treichl**, den Richter Dr.  Roman Galehr sowie die fachkundigen Laienrichter Mag. Eva-Maria Düringer und Mag. Tino  Ricker in der Beschwerdesache Dirk Hironymus, Am See IV 25, 3071 Hinterholz, Österreich (vormals: RHO Pharma), vertreten  durch Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG, Alpstraße  23, 6890 Lustenau über die Beschwerde vom 05. Oktober 2016 gegen die Bescheide des  Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, Postfach 260, 1000 Wien) vom 12.  September 2016 betreffend Umsatzsteuer 2012, Bescheid über die Wiederaufnahme des  Verfahrens 2012 und vom 09. September 2016 betreffend Umsatzsteuer 2015 Steuernummer  63-114/3997  in Anwesenheit der Schriftführerin Isabella Längle zu Recht erkannt:     I. Die Beschwerde gegen die Wiederaufnahme des Verfahrens Umsatzsteuer 2012  wird als unbegründet abgewiesen.

- missed: `Mag. Armin Treichl` (person)
- predicted in sentence: `Dr.  Roman Galehr`, `Dirk Hironymus`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter **Erwin Agneter** und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

- missed: `Erwin Agneter` (person)
- predicted in sentence: `Dr. Wolfgang Pavlik`, `Dr. Wolfgang Aigner`

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Regina Vogt** in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Regina Vogt` (person)
- predicted in sentence: `Sean Herdling`

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Helga Hochrieser** in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

- missed: `Mag. Helga Hochrieser` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_13`)

Schreiben des Rechtsanwaltes Dr. Karl RA1 (NÖ) an das FA (23. Dezember 2018):  Da das Unternehmensserviceportal für uns dzt nicht zugänglich ist, erlauben wir uns auf diesem  Wege den wirtschaftlichen Eigentümer der **Dario Kobben**  mit Dr. Karl RA1 bekanntzugeben.

- missed: `Dario Kobben` (person)
- predicted in sentence: `Dr. Karl`, `Dr. Karl`

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_111`)

Im Gutachten vom 1. Juli 2021 stellte **Dr.in Dok3** ebenfalls keinen Grad der Behinderung fest.

- missed: `Dr.in Dok3` (person)
- predicted in sentence: `Dr.in Dok`

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_152`)

Zur ag Bel mit SB für die Ehegattin (€ 450,44, Krankheitskosten)  17.04.2013 130,00 Zahnbehandlung Dr. M xxx   - 31,84 Ersatz GKK  02.01.2013 - **Dr. W** sh.

- missed: `Dr. W` (person)
- predicted in sentence: —

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_162`)

Verwaltungsverfahrensrechtes **DDr.  Walter,** DDr. Maier, Seite 131).

- missed: `DDr.  Walter,` (person)
- predicted in sentence: `Dr.  Walter`, `Dr. Maier`

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_193`)

Die Beschwerdeführerin gehört dem Liquiditätsverbund der **Dimitri Dancker**  an.

- missed: `Dimitri Dancker` (person)
- predicted in sentence: —

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin **Mag. Heidemarie Winkler** über die  Beschwerde der Uwe Köhn, Pizet 15, 9441 Waldenstein, Österreich, vom 26. Juli 2018, gegen den Bescheid des  Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom  13. Juli 2018, betreffend Rückforderung von Familienbeihilfe für den Zeitraum September 2016  bis Februar 2018, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO im Umfang der  Beschwerdevorentscheidung, nämlich für 09/2016-02/2017, stattgegeben.

- missed: `Mag. Heidemarie Winkler` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/144550.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144550.1_37`)

Daneben  stehe die Bf. in ständiger Überwachung der Klinik **Dr. A2** in A-Stadt wegen einer erst  vorgenommenen Laseroperation beim zweiten Auge.

- missed: `Dr. A2` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_42`)

Ein **RA Dr.  Carl** RA1 mit identer Adresse in NÖ und identer Handynummer brachte hingegen für die Bf. die  Vorlageanträge (1.4.2019 und 16.8.2019) ein.

- missed: `RA Dr.  Carl` (person)
- predicted in sentence: `Dr.  Carl`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/145832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145832.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache **StR OSR OStR Torsten Schlichtenmeier**, Untere Waldalpe 2, 5204 Voglhub, Österreich, (Beschwerdeführerin, abgekürzt: Bf.), über  deren Beschwerde vom 25. Jänner 2024 gegen den Einkommensteuerbescheid 2022 des  Finanzamtes Österreich vom 11. Jänner 2024 zu Steuernummer 20-897/4296  zu Recht  erkannt:  Der Beschwerde wird teilweise stattgegeben und der angefochtene Bescheid gemäß § 279  Abs. 1 BAO abgeändert.

- missed: `StR OSR OStR Torsten Schlichtenmeier` (person)
- predicted in sentence: `OSR OStR Torsten Schlichtenmeier`

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache **Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.**,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.` (person)
- predicted in sentence: `Univ.-Prof.in Eva Gund, Bakk. `

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_187`)

Die umfangreichen gutachterlichen Ausführungen von **Ronald Bloehdorn** würden  sich wie folgt zusammenfassen lassen:  12 von 22 Seite 13 von 22

- missed: `Ronald Bloehdorn` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Marco Laudacher** in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

- missed: `Mag. Marco Laudacher` (person)
- predicted in sentence: `Rene`

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_61`)

Der Beschwerde war eine Auftragsbestätigung der Post vom 21. April  2020 mit der Auftragsnummer ANr beigelegt, der folgende Abwesenheitsmitteilung  entnommen werden kann:   Bewohner: **Hilde Schorpp**  Adresse: Adresse  Zeitraum: Ab 24.04.2020 bis 31.08.2020  Sendungsarten: RSa-und RSb-Briefe.

- missed: `Hilde Schorpp` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Armin Treichl, den Richter Dr.  Roman Galehr sowie die fachkundigen Laienrichter **Mag. Eva-Maria Düringer** und Mag. Tino  Ricker in der Beschwerdesache Dirk Hironymus, Am See IV 25, 3071 Hinterholz, Österreich (vormals: RHO Pharma), vertreten  durch Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG, Alpstraße  23, 6890 Lustenau über die Beschwerde vom 05. Oktober 2016 gegen die Bescheide des  Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, Postfach 260, 1000 Wien) vom 12.  September 2016 betreffend Umsatzsteuer 2012, Bescheid über die Wiederaufnahme des  Verfahrens 2012 und vom 09. September 2016 betreffend Umsatzsteuer 2015 Steuernummer  63-114/3997  in Anwesenheit der Schriftführerin Isabella Längle zu Recht erkannt:     I. Die Beschwerde gegen die Wiederaufnahme des Verfahrens Umsatzsteuer 2012  wird als unbegründet abgewiesen.

- missed: `Mag. Eva-Maria Düringer` (person)
- predicted in sentence: `Dr.  Roman Galehr`, `Dirk Hironymus`

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/141433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141433.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Corinna Engenhart in der  Beschwerdesache **Juliana Hosius**, Pilgrimweg 14, 4921 Obermauer, Österreich, über die Beschwerde vom 7. Juli 2022 gegen den  Bescheid des Finanzamtes Österreich vom 7. Juni 2022 betreffend Festsetzung einer  Zwangsstrafe nach dem Wirtschaftliche Eigentümer Registergesetz – WiEReg, Steuernummer  67-988/3642, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Juliana Hosius` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)

BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter **Mag. Markus Knechtl LL.M.** in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

- missed: `Mag. Markus Knechtl LL.M.` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_2`)

Das Bundesfinanzgericht hat durch den Richter **Mag. Adolf Brehmer**  in der Beschwerdesache VetR Gotthard Lohscheider,  Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich, vertreten durch „Meinrad Kisewetter“ - Steuerberatungsgesellschaft m.b.H., Langenschönbichl/Kornstraße 31, 9714 Boden, Österreich,  über die Beschwerde vom 28.06.2021, gegen den Bescheid des Finanzamtes Österreich vom  27.05.2021 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm § 111 BAO, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Mag. Adolf Brehmer` (person)
- predicted in sentence: `Vet`

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ingeborg Brockmayer  in der Beschwerdesache des  **Timothy Penzlin**, Ötzeltgasse 264, 6252 Kleinsöll, Österreich, betreffend die Beschwerde vom 25. Jänner 2017 gegen den  Haftungsbescheid des FA Innsbruck  vom 21. Dezember 2016 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

- missed: `Timothy Penzlin` (person)
- predicted in sentence: `Dr.in Ingeborg Brockmayer`

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des **Josepha Peifers** Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Josepha Peifers` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden MMag. Gerald Erwin Ehgartner und die  weiteren Senatsmitglieder **Mag. Elisabeth Traxler**, Mag. Harald Zeller und Christian Ringseis in  der Beschwerdesache Muran Iossifidis, Birken-Siedlung 22, 4715 Unterstetten, Österreich, vertreten durch KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  über die Beschwerde vom 30. August 2023 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 11. Juli 2023 betreffend Beschwerdezinsen (§ 205a BAO) nach  Durchführung einer mündlichen Verhandlung am 29. November 2023 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Mag. Elisabeth Traxler` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_394`)

10. 2015, C-378/14, Tomisław **Trapkowski**,  ECLI:EU:C:2015:720, Rn. 41).

- missed: `Trapkowski` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_17`)

Die Bf. legte im Zuge der Beschwerde folgende Unterlagen vor:  Schreiben von **Mag. Dr.in Carina B.**, Psychotherapeutin:  T. befindet sich seit 12. April 2022 auf Grund ihrer psychischen Erkrankung in einer  regelmäßigen ambulanten Psychotherapie bei ihr.

- missed: `Mag. Dr.in Carina B.` (person)
- predicted in sentence: `Dr.in Carina`

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter **Mag. Markus Knechtl LL.M.** in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

- missed: `Mag. Markus Knechtl LL.M.` (person)
- predicted in sentence: `Ing. Mag`

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138922.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138922.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter **Mag. Gerhard Konrad** in der Beschwerdesache  Olaf Koechig, Zmöllach 3, 3542 Litschgraben, Österreich, Beschwerde vom 25. Oktober 2019 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr Finanzamtes Österreich, vom  28. November 2018 betreffend Umsatzsteuer 2012, Umsatzsteuer 2013, Umsatzsteuer 2014  und Umsatzsteuer 2015, Steuernummer 17-913/2665, der Gartfentri Heizung Institut GmbH, vertreten durch  Gustke Forschung GmbH, hinsichtlich des Vorlageantrages der Gartfentri Heizung Institut GmbH  in  Liquidation, beschlossen:  I. Die Beschwerdevorentscheidungen vom 6. April 2022 betreffend Umsatzsteuer 2012,  2013, 2014 und 2015 der Gartfentri Heizung Institut GmbH  in Liquidation werden aufgehoben.

- missed: `Mag. Gerhard Konrad` (person)
- predicted in sentence: `Olaf Koechig`

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_2`)

Jeffrey Marinopoulos, Moosbauernstraße 12, 9341 Wattein, Österreich, als atypisch still Beteiligte an der vormaligen **Leroy Kusznierz**,  vertreten durch Prof. Thomas Keppert Steuerberatung und Wirtschaftsprüfung GmbH,  Theobaldgasse 19, 1060 Wien,  über die Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Klagenfurt vom  24. April 2012 die Wiederaufnahme des Verfahrens die Feststellung von Einkünften und die  Feststellung von Einkünften gemäß § 188 BAO betreffend, je für das Jahr 2007, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig  zurückgewiesen.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_40`)

7. In der dagegen rechtzeitig erhobenen Beschwerde wird vorgebracht:  Entgegen der Gutachterin würden aus der Aufstellung der Diagnosen von **Dr. D** bereits ab den  ersten Lebenswochen unklare, sich dann über die Jahre verdichtende, massive  Entwicklungsverzögerungen in allen Bereichen – nicht nur sprachlich und motorisch –  hervorgehen.

- missed: `Dr. D` (person)
- predicted in sentence: —

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/147361.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147361.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Emmerich Malert  betreffend den Vorlageantrag der  **Florens Schitterle**, Heidebahn 164, 2443 Deutsch-Brodersdorf, Österreich, vom 31. Dezember 2020 in einer Familienbeihilfenangelegenheit  (Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Mai 2013 bis  Dezember 2014, Bescheid des Finanzamtes Österreich vom 24. März 2020)  beschlossen:  I.  Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig  zurückgewiesen.

- missed: `Florens Schitterle` (person)
- predicted in sentence: `Priv.-Doz. Priv.-Doz. Emmerich Malert`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)

IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter **Mag. Armin Treichl** in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

- missed: `Mag. Armin Treichl` (person)
- predicted in sentence: `Fiona Buedenbender`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_62`)

Beweiswürdigung:  Der Sachverhalt ergibt sich aus den eigenen Wahrnehmungen und Anzeigedaten des  Kontrollorgans der Parkraumüberwachung, den zur Beanstandungszeit angefertigten Fotos,  den Angaben der Zulassungsbesitzerin, der Auskunft des Sozialministeriumservice betreffend  den auf **M.** ausgestellten Parkausweis.

- missed: `M.` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_55`)

Handschriftlich war darauf vermerkt „Bestätigung durch Frau E, Exfrau des Bf. und  Mutter der beiden unterhaltspflichtigen Kinder K1 und K2: Hiermit erkläre ich, dass mein  Exmann **KzlR Diethard Ringhand**  zu allen o.g.

- missed: `KzlR Diethard Ringhand` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paulina Borisowa  in der Beschwerdesache Ilhan Feldmeier, Bakk. rer. nat.,  Sittenbergstraße 9, 4294 Stampfendorf, Österreich, vertreten durch **Mag. Benno Elmar Di Gaspero**, Unterer Platz 7, 9372  Eberstein, über die Beschwerde vom 14. Juni 2024 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juni 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 14-548/3314  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

- missed: `Mag. Benno Elmar Di Gaspero` (person)
- predicted in sentence: `Univ.-Prof.in Paulina Borisowa`, `Ilhan Feldmeier`

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_205`)

19.564,68 €……..Mag. ES IE (2,6919 %)  668.105,92 €……Z1Z2Z3 Privatstiftung (91,9243% )Sonja Schönhut **Linn Brümmer** und Lynn Freimut sind Geschwister (Daten aus dem zentralen Melderegister  betreffend Sonja Schönhut  geb. IE; Firmenbuchdaten FN FN1 t mit den Hinweisen auf die  ehemaligen Gesellschafter Cassandra Ungar  SD IE und die Gesellschafter im Streitzeitraum Mag. AI RR;Linn Brümmer und Lynn Freimut.

- missed: `Linn Brümmer` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_5`)

Gegen diesen Bescheid brachte der Beschwerdeführer **Jason Oberbüscher**  am 11. April 2023 das  Rechtsmittel der Beschwerde ein und führte begründend aus, dass seine   „unter Pkt. 2 angeführte Einkünfte von der ‚FA Linz  RS AG‘ keine Einkünfte aus Lohn- oder  selbstständiger Arbeit seien.

- missed: `Jason Oberbüscher` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_91`)

„Arbeitsplätze“ zu den  genannten Bedingungen in Bestand nahmen, geht aus den Ausführungen der Bf. im Rahmen  der mündlichen Verhandlung hervor, ebenso das Faktum, dass es sich bei einer dieser  Kommanditisten, nämlich DD, gleichzeitig um eine Angestellte der Bf. und Mutter des **GF AA**  handelt (VH-Protokoll vom 10.10.2025, S. 2).

- missed: `GF AA` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)

 Herr **Harald Hilderink**  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_289`)

Es besteht hierzu der  sich allgemein aufdrängende Verdacht, dass die Früchte aus mannigfaltigen Malversationen  (Scheinrechnungen, Organisation von Schwarzarbeit) nicht bloß den Betreibern der **M.** frommt,  sondern systematisch an übergelagerte Nutznießer durchgereicht werden (Durchreichung in  einem mehrstufigen Betrugsmodell).

- missed: `M.` (person)
- predicted in sentence: —

</details>

---

